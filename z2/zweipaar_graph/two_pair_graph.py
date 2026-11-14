#!/usr/bin/env python
"""Zwei-Paar-Relativgraph des Stufe-A-Dimermodells (RK-Punkt).

Konstruiert den Graphen der relativen Zwei-Paar-Zustände auf dem L x L-Torus,
bestimmt seine Zusammenhangskomponenten, die Driftfunktion d_2, löst die
Poisson-Gleichung L_rel h_2 = d_2 komponentenweise und berechnet die
H^{-1}-Energie E_2(L) = <d_2, L_rel^{-1} d_2>.

Konventionen (ausführlich in README.md):
- Bindung = (Anker a, Orientierung o), o = 0 (h): {a, a+e_x}, o = 1 (v): {a, a+e_y}.
- Relativzustand s = (alpha, r_x, r_y, beta): Paar 1 hat Anker (0,0) und Orientierung
  alpha, Paar 2 Anker r (mod L) und Orientierung beta. Die Paare sind markiert
  (geordnet); jeder physikalische Zustand kommt zweimal vor, (alpha,r,beta) und
  (beta,-r,alpha). Auf markierten Paaren wirkt die Translationsgruppe frei.
- Eckschritt: {u,v} -> {v,w}, u,v,w rechtwinklig mit Ecke v; q_x = (w_x - u_x)/2
  in ungewrappten lokalen Koordinaten, also immer +-1/2. Gerade Schritte
  (u,v,w kollinear, q_x in {0, +-1}) nur mit --gerade (nicht Stufe A).
- Berührungsverbot: alle Endpunkte zweier Paare haben Torus-L1-Abstand > 1.

Aufrufe:
    python two_pair_graph.py selbsttest
    python two_pair_graph.py lauf --L 16 24 32 48 64 96 --jobs 6
    pytest two_pair_graph.py
"""

import argparse
import csv
import json
import os
import resource
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import cg, splu

try:  # optional, wird nur benutzt, wenn vorhanden
    import pyamg  # noqa: F401
    HAT_PYAMG = True
except ImportError:
    HAT_PYAMG = False

H, V = 0, 1
ONAME = {H: "h", V: "v"}
EINH = np.array([[1, 0], [0, 1]], dtype=np.int64)       # Bindungsrichtung je Orientierung
OFF2 = np.array([[1, 0], [0, 1]], dtype=np.int64)       # 2 x (Mitte - Anker)


# ---------------------------------------------------------------------------
# Elementare Schritte eines einzelnen Paares
# ---------------------------------------------------------------------------

def schritte(o, gerade=False):
    """Alle elementaren Schritte eines Paares mit Anker (0,0) und Orientierung o.

    Direkt aus der Definition: Pivot v ist ein Endpunkt, u der andere, w = v + d
    mit d senkrecht zu v - u (Eckschritt) bzw. d = v - u (gerader Schritt).
    Neue Bindung {v, w}. Rückgabe: Liste von Tupeln
    (dax, day, o_neu, qx2, art), qx2 = 2 q_x = w_x - u_x (ungewrappt).
    """
    e0 = np.array([0, 0])
    e1 = EINH[o]
    aus = []
    for v, u in ((e1, e0), (e0, e1)):
        a = v - u
        richtungen = [(np.array([-a[1], a[0]]), "ecke"), (np.array([a[1], -a[0]]), "ecke")]
        if gerade:
            richtungen.append((a.copy(), "gerade"))
        for d, art in richtungen:
            w = v + d
            anker = v if d[0] + d[1] > 0 else w
            o_neu = H if d[0] != 0 else V
            aus.append((int(anker[0]), int(anker[1]), o_neu, int(w[0] - u[0]), art))
    return aus


def schritt_tabelle(gerade=False):
    """Tabelle als Arrays je Orientierung: (dax, day, o_neu, qx2)."""
    tab = {}
    for o in (H, V):
        s = schritte(o, gerade)
        tab[o] = np.array([x[:4] for x in s], dtype=np.int64)
    return tab


# ---------------------------------------------------------------------------
# Geometrie auf dem Torus
# ---------------------------------------------------------------------------

def torus_l1(L, p, q):
    """Torus-L1-Abstand zwischen Punktarrays p, q (letzte Achse = 2)."""
    d = np.abs(p - q) % L
    d = np.minimum(d, L - d)
    return d[..., 0] + d[..., 1]


def endpunkte(anker, o):
    """Endpunkte (ungewrappt) für Arrays von Ankern (...,2) und Orientierungen (...)."""
    return anker, anker + EINH[o]


def kompatibel(L, a1, o1, a2, o2):
    """Berührungsverbot (vektorisiert): alle 4 Endpunktpaare mit Torus-L1 > 1."""
    p0, p1 = endpunkte(a1, o1)
    q0, q1 = endpunkte(a2, o2)
    m = torus_l1(L, p0, q0)
    m = np.minimum(m, torus_l1(L, p0, q1))
    m = np.minimum(m, torus_l1(L, p1, q0))
    m = np.minimum(m, torus_l1(L, p1, q1))
    return m > 1


# ---------------------------------------------------------------------------
# Kodierung der Relativzustände
# ---------------------------------------------------------------------------

def kodiere(L, alpha, rx, ry, beta):
    return ((alpha * L + rx) * L + ry) * 2 + beta


def dekodiere(L, code):
    beta = code % 2
    t = code // 2
    ry = t % L
    t = t // L
    rx = t % L
    alpha = t // L
    return alpha, rx, ry, beta


def mitte2(L, alpha, rx, ry, beta):
    """2 x (Mitte Paar 2 - Mitte Paar 1), Minimalbild in [-L, L)."""
    mx = 2 * rx + OFF2[beta, 0] - OFF2[alpha, 0]
    my = 2 * ry + OFF2[beta, 1] - OFF2[alpha, 1]
    mx = (mx + L) % (2 * L) - L
    my = (my + L) % (2 * L) - L
    return mx, my


# ---------------------------------------------------------------------------
# Graphaufbau
# ---------------------------------------------------------------------------

class Relativgraph:
    """Zustände, gerichtete elementare Übergänge, Drift, Generator."""

    def __init__(self, L, gerade=False):
        if L < 6 or L % 2:
            raise ValueError("L muss gerade und >= 6 sein (sonst wickeln Sperrzonen um den Torus)")
        self.L = L
        self.gerade = gerade
        self.tab = schritt_tabelle(gerade)
        self.voll_grad = 2 * len(self.tab[H])
        t0 = time.perf_counter()
        self._zustaende()
        self._kanten()
        self.t_aufbau = time.perf_counter() - t0
        t0 = time.perf_counter()
        self.ncomp, self.labels = connected_components(self.A, directed=False)
        self.t_komp = time.perf_counter() - t0

    def _zustaende(self):
        L = self.L
        al, rx, ry, be = np.meshgrid(np.arange(2), np.arange(L), np.arange(L), np.arange(2),
                                     indexing="ij")
        al, rx, ry, be = (x.ravel().astype(np.int64) for x in (al, rx, ry, be))
        null = np.zeros((al.size, 2), dtype=np.int64)
        r = np.stack([rx, ry], axis=1)
        ok = kompatibel(L, null, al, r, be)
        codes = kodiere(L, al, rx, ry, be)[ok]
        self.codes = codes
        self.N = codes.size
        self.idx = np.full(4 * L * L, -1, dtype=np.int64)
        self.idx[codes] = np.arange(self.N)
        self.alpha, self.rx, self.ry, self.beta = dekodiere(L, codes)

    def _kanten(self):
        L = self.L
        src, dst, q2, wer, fehlend, falsch = [], [], [], [], 0, 0
        for mover in (0, 1):
            for o in (H, V):
                eigen = self.alpha if mover == 0 else self.beta
                sel = np.nonzero(eigen == o)[0]
                a, x, y, b = self.alpha[sel], self.rx[sel], self.ry[sel], self.beta[sel]
                for dax, day, o_neu, qx2 in self.tab[o]:
                    if mover == 0:      # Paar 1 springt, dann neu zentrieren
                        na, nx, ny, nb = np.full_like(a, o_neu), (x - dax) % L, (y - day) % L, b
                    else:               # Paar 2 springt
                        na, nx, ny, nb = a, (x + dax) % L, (y + day) % L, np.full_like(b, o_neu)
                    # Berührungsverbot direkt neu prüfen (unabhängig vom Index)
                    null = np.zeros((sel.size, 2), dtype=np.int64)
                    ok = kompatibel(L, null, na, np.stack([nx, ny], axis=1), nb)
                    t = self.idx[kodiere(L, na, nx, ny, nb)]
                    fehlend += int(np.sum(ok & (t < 0)))
                    falsch += int(np.sum(~ok & (t >= 0)))
                    keep = ok & (t >= 0)
                    src.append(sel[keep])
                    dst.append(t[keep])
                    q2.append(np.full(int(keep.sum()), qx2, dtype=np.int64))
                    wer.append(np.full(int(keep.sum()), mover, dtype=np.int8))
        self.src = np.concatenate(src)
        self.dst = np.concatenate(dst)
        self.q2 = np.concatenate(q2)            # 2 q_x, ganzzahlig
        self.mover = np.concatenate(wer)
        self.fehlend = fehlend                  # zulässiges Ziel, aber nicht im Index
        self.falsch_im_index = falsch           # unzulässiges Ziel im Index
        self.M = self.src.size
        N = self.N
        # Adjazenz mit Multiplizität (Duplikate werden addiert, nicht verschmolzen)
        self.A = sp.coo_matrix((np.ones(self.M), (self.src, self.dst)), shape=(N, N)).tocsr()
        self.grad = np.bincount(self.src, minlength=N).astype(np.float64)
        self.Lap = (sp.diags(self.grad) - self.A).tocsr()
        self.d2x2 = np.bincount(self.src, weights=self.q2, minlength=N).astype(np.int64)  # 2 d_2
        self.d2 = self.d2x2 / 2.0

    # --- abgeleitete Größen -------------------------------------------------
    def mitte2(self):
        return mitte2(self.L, self.alpha, self.rx, self.ry, self.beta)

    def max_multiplizitaet(self):
        return int(self.A.data.max()) if self.A.nnz else 0

    def max_asymmetrie(self):
        D = abs(self.A - self.A.T)
        return float(D.max()) if D.nnz else 0.0

    def komponentensummen2(self):
        """exakte ganzzahlige Summen von 2 d_2 je Komponente"""
        return np.bincount(self.labels, weights=self.d2x2, minlength=self.ncomp).astype(np.int64)


# ---------------------------------------------------------------------------
# Symmetrien
# ---------------------------------------------------------------------------

def spiegel_x(L, alpha, rx, ry, beta):
    """x -> -x: Anker (ax,ay,o) -> (-ax - [o=h], ay)."""
    c1x = -(alpha == H).astype(np.int64)
    c2x = -rx - (beta == H).astype(np.int64)
    return alpha, (c2x - c1x) % L, ry % L, beta


def spiegel_y(L, alpha, rx, ry, beta):
    """y -> -y: Anker (ax,ay,o) -> (ax, -ay - [o=v])."""
    c1y = -(alpha == V).astype(np.int64)
    c2y = -ry - (beta == V).astype(np.int64)
    return alpha, rx % L, (c2y - c1y) % L, beta


def tausch(L, alpha, rx, ry, beta):
    """Paare vertauschen: (alpha, r, beta) -> (beta, -r, alpha)."""
    return beta, (-rx) % L, (-ry) % L, alpha


def kanten_schluessel(N, src, dst, q2, mover=None):
    k = (src.astype(np.int64) * N + dst) * 9 + (q2 + 4)
    if mover is not None:
        k = k * 2 + mover
    return k


# ---------------------------------------------------------------------------
# Poisson-Gleichung
# ---------------------------------------------------------------------------

def loese_poisson(g, rtol=1e-12, lu_max=200_000):
    """Löst L_rel h = d_2 je Komponente, Mittel 0 je Komponente.

    CG mit Jacobi-Vorkonditionierung (pyamg, falls installiert, als Vorkonditionierer
    für große Komponenten). Für Komponenten bis lu_max Zustände zusätzlich direkte
    LU-Lösung des geerdeten Systems als Gegenprobe.
    """
    N = g.N
    h = np.zeros(N)
    order = np.argsort(g.labels, kind="stable")
    grenzen = np.searchsorted(g.labels[order], np.arange(g.ncomp + 1))
    info = []
    t0 = time.perf_counter()
    for c in range(g.ncomp):
        knoten = order[grenzen[c]:grenzen[c + 1]]
        n = knoten.size
        b = g.d2[knoten]
        rec = dict(komp=c, groesse=int(n), iter=0, res=0.0, lu_diff=float("nan"))
        if n == 1 or not np.any(b):
            info.append(rec)
            continue
        sub = g.Lap[knoten][:, knoten].tocsr()
        if HAT_PYAMG and n > 50_000:
            ml = pyamg.smoothed_aggregation_solver(sub, symmetry="symmetric")
            Mpre = ml.aspreconditioner()
        else:
            Mpre = sp.diags(1.0 / sub.diagonal())
        zaehler = [0]

        def cb(_xk):
            zaehler[0] += 1

        x, flag = cg(sub, b, rtol=rtol, atol=0.0, maxiter=20 * n + 1000, M=Mpre, callback=cb)
        if flag != 0:
            raise RuntimeError(f"CG nicht konvergiert (Komponente {c}, flag {flag})")
        x -= x.mean()
        rec["iter"] = zaehler[0]
        rec["res"] = float(np.linalg.norm(sub @ x - b) / np.linalg.norm(b))
        if n <= lu_max:
            lu = splu(sub[:-1, :-1].tocsc())
            y = np.append(lu.solve(b[:-1]), 0.0)
            y -= y.mean()
            rec["lu_diff"] = float(np.max(np.abs(x - y)) / max(np.max(np.abs(y)), 1e-300))
        h[knoten] = x
        info.append(rec)
    t_poisson = time.perf_counter() - t0
    return h, info, t_poisson


def energien(g, h):
    """E_C = <d,h>_C und Dirichlet-Form je Komponente."""
    E_poisson = np.bincount(g.labels, weights=g.d2 * h, minlength=g.ncomp)
    # jede gerichtete Kante kommt mit ihrer Rückkante vor -> Faktor 1/2 = jede
    # ungerichtete physikalische Kante genau einmal
    w = 0.5 * (h[g.src] - h[g.dst]) ** 2
    E_dirichlet = np.bincount(g.labels[g.src], weights=w, minlength=g.ncomp)
    return E_poisson, E_dirichlet


# ---------------------------------------------------------------------------
# Fernfeld: Monopol, Dipol, Fourier
# ---------------------------------------------------------------------------

def fernfeld(g):
    mx2, my2 = g.mitte2()
    linf2 = np.maximum(np.abs(mx2), np.abs(my2))
    nz = g.d2x2 != 0
    unvoll = g.grad < g.voll_grad
    res = dict(
        monopol2=int(g.d2x2.sum()),
        dipol_x=float(np.sum(mx2 * g.d2x2) / 4.0),     # sum m_x d_2  (m = mx2/2, d = d2x2/2)
        dipol_y=float(np.sum(my2 * g.d2x2) / 4.0),
        quadrupol_xy=float(np.sum(mx2 * my2 * g.d2x2) / 8.0),
        n_drift=int(nz.sum()),
        radius_drift=float(linf2[nz].max() / 2.0) if nz.any() else 0.0,
        radius_blockiert=float(linf2[unvoll].max() / 2.0) if unvoll.any() else 0.0,
    )
    # Dipol je Orientierungssektor (alpha, beta)
    for a in (H, V):
        for b in (H, V):
            m = (g.alpha == a) & (g.beta == b)
            res[f"dipol_x_{ONAME[a]}{ONAME[b]}"] = float(np.sum(mx2[m] * g.d2x2[m]) / 4.0)
            res[f"dipol_y_{ONAME[a]}{ONAME[b]}"] = float(np.sum(my2[m] * g.d2x2[m]) / 4.0)
    # Freier Graph außerhalb: alle Zustände jenseits des Blockaderadius haben vollen Grad
    aussen = linf2 > 2 * res["radius_blockiert"]
    res["aussen_voller_grad"] = bool(np.all(g.grad[aussen] == g.voll_grad))
    return res


def fourier(g, nmax=None):
    """d_2^(k) für k = 2 pi n / L längs x, y und Diagonale.

    'gesamt' summiert über alle vier Orientierungssektoren (die im Auftrag verlangte
    Größe); das ist die Projektion auf die langsame, sektorsymmetrische Mode des freien
    Relativgitters. Zusätzlich je Sektor (alpha, beta). Da m halbzahlig ist und
    k = 2 pi n / L, ist exp(i k m) wohldefiniert modulo L (kein Repräsentantenproblem).
    """
    L = g.L
    nmax = nmax or max(4, L // 4)
    mx2, my2 = g.mitte2()
    nz = g.d2x2 != 0
    mx2, my2, d = mx2[nz], my2[nz], g.d2[nz]
    sek = np.array([f"{ONAME[a]}{ONAME[b]}" for a, b in zip(g.alpha[nz], g.beta[nz])])
    aus = {}
    for name, (ex, ey) in dict(x=(1, 0), y=(0, 1), diag=(1, 1)).items():
        n = np.arange(1, nmax + 1)
        kx = 2 * np.pi * n * ex / L
        ky = 2 * np.pi * n * ey / L
        terme = np.exp(1j * (np.outer(kx, mx2 / 2.0) + np.outer(ky, my2 / 2.0))) * d
        eintrag = dict(k=np.hypot(kx, ky).tolist(), gesamt=np.abs(terme.sum(axis=1)).tolist())
        for s in ("hh", "hv", "vh", "vv"):
            eintrag[s] = np.abs(terme[:, sek == s].sum(axis=1)).tolist()
        aus[name] = eintrag
    return aus


def fourier_exponent(k, a):
    """lokale Steigung log|d^| / log k aus den zwei kleinsten k; nan, wenn |d^| ~ 0."""
    k, a = np.asarray(k), np.asarray(a)
    if a[0] < 1e-12 or a[1] < 1e-12:
        return float("nan")
    return float(np.log(a[1] / a[0]) / np.log(k[1] / k[0]))


# ---------------------------------------------------------------------------
# Steifigkeit (Prüfung gegen stufe_a.md §15)
# ---------------------------------------------------------------------------

def steifigkeit_L2(g, E_poisson):
    """rho_s L^2 / t_c = <deg>/4 - 2 E / |R| auf der größten Komponente (RK-Punkt)."""
    groessen = np.bincount(g.labels)
    c = int(np.argmax(groessen))
    maske = g.labels == c
    deg_mittel = g.grad[maske].mean()
    return deg_mittel / 4.0 - 2.0 * E_poisson[c] / maske.sum(), deg_mittel / 4.0


# ---------------------------------------------------------------------------
# Unabhängige Kontrolle auf dem vollen Torus (kleine L)
# ---------------------------------------------------------------------------

def voller_torus(L, gerade=False):
    """Zwei ungeordnete Paare auf dem vollen L x L-Torus, ohne Relativkoordinaten.

    Liefert Zahl der Konfigurationen, gerichtete Übergänge, Komponenten, Energie
    <d, Lambda^{-1} d> (direkte LU je Komponente) und die quotientierte Kantenmenge
    (aus allen markierten Konfigurationen mit Paar 1 am Ursprung).
    """
    tab = schritt_tabelle(gerade)
    nb = 2 * L * L
    bx = np.arange(nb) // 2 // L
    by = (np.arange(nb) // 2) % L
    bo = np.arange(nb) % 2
    anker = np.stack([bx, by], axis=1)
    kompat = kompatibel(L, anker[:, None, :], bo[:, None], anker[None, :, :], bo[None, :])
    np.fill_diagonal(kompat, False)

    def bindung(ax, ay, o):
        return ((ax % L) * L + (ay % L)) * 2 + o

    ziele = np.array([[bindung(bx[b] + s[0], by[b] + s[1], s[2]) for s in tab[bo[b]]]
                      for b in range(nb)])
    qs = np.array([[s[3] for s in tab[bo[b]]] for b in range(nb)])
    i, j = np.nonzero(np.triu(kompat, 1))
    nconf = i.size
    cid = -np.ones((nb, nb), dtype=np.int64)
    cid[i, j] = np.arange(nconf)
    cid[j, i] = np.arange(nconf)
    src, dst, q = [], [], []
    for p_bew, p_fest in ((i, j), (j, i)):
        for k in range(ziele.shape[1]):
            neu = ziele[p_bew, k]
            ok = kompat[neu, p_fest]
            src.append(cid[p_bew[ok], p_fest[ok]])
            dst.append(cid[neu[ok], p_fest[ok]])
            q.append(qs[p_bew[ok], k])
    src, dst, q = (np.concatenate(x) for x in (src, dst, q))
    A = sp.coo_matrix((np.ones(src.size), (src, dst)), shape=(nconf, nconf)).tocsr()
    grad = np.bincount(src, minlength=nconf).astype(float)
    Lap = (sp.diags(grad) - A).tocsr()
    d = np.bincount(src, weights=q / 2.0, minlength=nconf)
    ncomp, lab = connected_components(A, directed=False)
    # Der volle Zwei-Paar-Graph ist vierdimensional; direkte LU hat dort großen Fill-in,
    # deshalb hier CG (eigene Matrix, eigene Drift, unabhängig vom Relativgraphen).
    E_komp = np.zeros(ncomp)
    for c in range(ncomp):
        kn = np.nonzero(lab == c)[0]
        if kn.size < 2 or not np.any(d[kn]):
            continue
        sub = Lap[kn][:, kn].tocsr()
        y, flag = cg(sub, d[kn], rtol=1e-13, atol=0.0, maxiter=50 * kn.size,
                     M=sp.diags(1.0 / sub.diagonal()))
        if flag != 0:
            raise RuntimeError("CG auf dem vollen Torus nicht konvergiert")
        E_komp[c] = float(d[kn] @ (y - y.mean()))
    E = float(E_komp.sum())
    c = int(np.argmax(np.bincount(lab)))
    kn = np.nonzero(lab == c)[0]
    deg4 = grad[kn].mean() / 4.0
    rho = deg4 - 2.0 * E_komp[c] / kn.size

    # Quotientierte Kantenmenge: markierte Konfigurationen (Paar 1, Paar 2), Paar 1 am Ursprung
    rel_kanten = []
    for o1 in (H, V):
        b1 = bindung(0, 0, o1)
        for b2 in np.nonzero(kompat[b1])[0]:
            for mover in (0, 1):
                bew, fest = (b1, b2) if mover == 0 else (b2, b1)
                for k in range(ziele.shape[1]):
                    neu = ziele[bew, k]
                    if not kompat[neu, fest]:
                        continue
                    n1, n2 = (neu, b2) if mover == 0 else (b1, neu)
                    # neu zentrieren: Paar 1 an den Ursprung schieben
                    sx, sy = bx[n1], by[n1]
                    s_code = kodiere(L, o1, bx[b2], by[b2], bo[b2])
                    t_code = kodiere(L, bo[n1], (bx[n2] - sx) % L, (by[n2] - sy) % L, bo[n2])
                    rel_kanten.append((s_code, t_code, int(qs[bew, k]), mover))
    return dict(nconf=nconf, nkanten=int(src.size), ncomp=int(ncomp), E=E,
                rho_L2=rho, deg4=deg4, rel_kanten=rel_kanten)


# ---------------------------------------------------------------------------
# Tests (A: numerisch verifiziert für die gerechneten L)
# ---------------------------------------------------------------------------

TEST_L = (6, 8, 10, 16)
# exakte Werte aus stufe_a.md §15 (vollständige Aufzählung, Einheiten rho_s L^2 / t_c)
LIT_RHO = {6: (1.7843, 1.7959), 8: (1.8993, 1.9048), 10: (1.9403, 1.9435)}


def test_schritte_aus_definition():
    """Eckschritte: vier je Paar, Pivot an gemeinsamem Endpunkt, senkrecht, verschieden,
    q_x = +-1/2, exakte Inverse mit -q_x."""
    erwartet = {H: {(1, 0, V, 1), (1, -1, V, 1), (0, -1, V, -1), (0, 0, V, -1)},
                V: {(0, 1, H, 1), (-1, 1, H, -1), (0, 0, H, 1), (-1, 0, H, -1)}}
    for o in (H, V):
        s = schritte(o)
        assert len(s) == 4
        assert {x[:4] for x in s} == erwartet[o], (o, s)
        for dax, day, on, qx2, art in s:
            assert art == "ecke" and on != o and abs(qx2) == 1
            alt = {tuple(p) for p in np.array(endpunkte(np.array([0, 0]), o)).tolist()}
            neu = {tuple(p) for p in np.array(endpunkte(np.array([dax, day]), on)).tolist()}
            assert len(alt & neu) == 1                      # gemeinsamer Pivot
            # Inverse: von der neuen Bindung zurück, mit -q_x
            rueck = [(dax + x[0], day + x[1], x[2], x[3]) for x in schritte(on)]
            assert (0, 0, o, -qx2) in rueck
            assert sum(1 for r in rueck if r[:3] == (0, 0, o)) == 1
        assert sum(x[3] for x in s) == 0


def test_kanten_eigenschaften():
    """Rückkante mit -q_x vorhanden, Generator symmetrisch, Multiplizität 1,
    keine fehlenden Ziele, Berührungsverbot nach jedem Sprung."""
    for L in TEST_L:
        g = Relativgraph(L)
        assert g.fehlend == 0 and g.falsch_im_index == 0
        k = kanten_schluessel(g.N, g.src, g.dst, g.q2, g.mover)
        kr = kanten_schluessel(g.N, g.dst, g.src, -g.q2, g.mover)
        ks = np.sort(k)
        assert np.unique(k).size == k.size                 # keine zusammengefassten Sprünge
        pos = np.searchsorted(ks, kr)
        assert np.all(ks[np.minimum(pos, ks.size - 1)] == kr)
        assert g.max_asymmetrie() == 0.0
        assert g.max_multiplizitaet() == 1
        al, x, y, be = dekodiere(L, g.codes[g.dst])
        null = np.zeros((g.M, 2), dtype=np.int64)
        assert np.all(kompatibel(L, null, al, np.stack([x, y], 1), be))
        assert np.all(np.abs(g.q2) == 1)


def test_paarzahl_und_einzelsprung():
    """Jede Kante bewegt genau ein Paar um einen Eckschritt; beide Paare bleiben verschieden.
    Geprüft in absoluten Koordinaten im Rahmen des Ausgangszustands."""
    L = 10
    g = Relativgraph(L)
    for e in range(g.M):
        a, x, y, b = (int(t) for t in dekodiere(L, g.codes[g.src[e]]))
        a2, x2, y2, b2 = (int(t) for t in dekodiere(L, g.codes[g.dst[e]]))
        vorher = {(0, 0, a), (x, y, b)}
        if g.mover[e] == 0:   # Paar 2 bleibt absolut fest, Paar 1 neu bei (x - x2, y - y2)
            p1 = ((x - x2) % L, (y - y2) % L, a2)
            nachher = {p1, (x, y, b2)}
            assert b2 == b
        else:
            nachher = {(0, 0, a2), (x2, y2, b2)}
            assert a2 == a
        assert len(vorher) == 2 and len(nachher) == 2
        assert len(vorher & nachher) == 1                  # genau ein Paar bewegt


def test_komponentensummen_und_symmetrie():
    """Komponentensummen von d_2 exakt 0; d_2 ungerade unter x-Spiegelung, gerade unter
    y-Spiegelung und Paartausch; Spiegelungen/Tausch sind Graph-Automorphismen."""
    for L in TEST_L:
        g = Relativgraph(L)
        assert np.all(g.komponentensummen2() == 0)
        k = np.sort(kanten_schluessel(g.N, g.src, g.dst, g.q2))
        for abb, vz in ((spiegel_x, -1), (spiegel_y, 1), (tausch, 1)):
            bild = g.idx[kodiere(L, *abb(L, g.alpha, g.rx, g.ry, g.beta))]
            assert np.all(bild >= 0)
            assert np.array_equal(np.sort(bild), np.arange(g.N))
            assert np.array_equal(bild[bild], np.arange(g.N))     # Involution
            assert np.array_equal(g.d2x2[bild], vz * g.d2x2)
            kb = np.sort(kanten_schluessel(g.N, bild[g.src], bild[g.dst], vz * g.q2))
            assert np.array_equal(kb, k)


def test_poisson_und_dirichlet():
    """CG konvergiert, LU-Gegenprobe, Poisson-Energie = Dirichlet-Form."""
    for L in TEST_L:
        g = Relativgraph(L)
        h, info, _ = loese_poisson(g, rtol=1e-12)
        for r in info:
            if r["iter"]:
                assert r["res"] < 1e-10 and r["lu_diff"] < 1e-8, r
        Ep, Ed = energien(g, h)
        assert np.allclose(Ep, Ed, rtol=1e-9, atol=1e-12)
        assert np.all(Ep >= -1e-12)


def test_voller_torus():
    """Unabhängige Konstruktion auf dem vollen Torus: gleiche Kantenmenge nach Quotient,
    |C| = |R| L^2 / 2, Kanten = M L^2 / 2, Energie = E_2 L^2 / 2, Steifigkeit wie §15."""
    for L in (6, 8, 10):
        g = Relativgraph(L)
        v = voller_torus(L)
        assert v["nconf"] * 2 == g.N * L * L
        assert v["nkanten"] * 2 == g.M * L * L
        rel = sorted(v["rel_kanten"])
        unsere = sorted(zip(g.codes[g.src].tolist(), g.codes[g.dst].tolist(),
                            g.q2.tolist(), g.mover.tolist()))
        assert rel == unsere
        h, _, _ = loese_poisson(g)
        Ep, _ = energien(g, h)
        assert abs(v["E"] - Ep.sum() * L * L / 2) < 1e-8 * max(1.0, v["E"])
        rho, deg4 = steifigkeit_L2(g, Ep)
        assert abs(rho - v["rho_L2"]) < 1e-10
        lit_rho, lit_deg4 = LIT_RHO[L]
        assert abs(rho - lit_rho) < 1.5e-4 and abs(deg4 - lit_deg4) < 1.5e-4, (L, rho, deg4)


def test_8x8_zahlen():
    """8 x 8, zwei Paare: 6720 Konfigurationen, eine Komponente (stufe_a.md §5)."""
    g = Relativgraph(8)
    assert g.N * 64 // 2 == 6720 and g.ncomp == 1


def test_drift_lokal():
    """d_2 verschwindet außerhalb eines festen Radius, unabhängig von L."""
    radien = set()
    for L in TEST_L:
        f = fernfeld(Relativgraph(L))
        radien.add((f["n_drift"], f["radius_drift"], f["dipol_x"], f["dipol_y"]))
        assert f["monopol2"] == 0 and f["aussen_voller_grad"]
    assert len(radien) == 1, radien


def test_lokaler_korrektor():
    """d_2 ist Eigenvektor des Generators: A d_2 = 0, Grad 7 auf dem Träger, also
    L_rel d_2 = 7 d_2, h_2 = d_2 / 7 und E_2 = |d_2|^2 / 7 = 4/7 (16 Zustände mit |d_2| = 1/2).
    Summe über die Sektoren von d_2^(k) verschwindet für alle k; je Sektor Dipol +-4."""
    for L in (12, 16, 24):
        g = Relativgraph(L)
        assert np.all(g.A @ g.d2x2 == 0)                   # exakt, ganzzahlig
        assert set(g.grad[g.d2x2 != 0].tolist()) == {7.0}
        h, _, _ = loese_poisson(g)
        assert np.max(np.abs(h - g.d2 / 7.0)) < 1e-12
        Ep, _ = energien(g, h)
        assert abs(Ep.sum() - 4.0 / 7.0) < 1e-12
        f = fernfeld(g)
        assert f["dipol_x_hv"] == 4.0 and f["dipol_x_vh"] == -4.0 and f["dipol_y_hv"] == 0.0
        fo = fourier(g)
        assert max(max(fo[r]["gesamt"]) for r in fo) < 1e-12


ALLE_TESTS = [test_schritte_aus_definition, test_kanten_eigenschaften, test_paarzahl_und_einzelsprung,
              test_komponentensummen_und_symmetrie, test_poisson_und_dirichlet, test_voller_torus,
              test_8x8_zahlen, test_drift_lokal, test_lokaler_korrektor]


def selbsttest():
    fehler = 0
    for t in ALLE_TESTS:
        t0 = time.perf_counter()
        try:
            t()
            doc = " ".join(t.__doc__.split())
            print(f"[A] BESTANDEN  {t.__name__:38s} {time.perf_counter() - t0:6.2f} s\n      {doc}")
        except Exception as ex:  # noqa: BLE001
            fehler += 1
            print(f"[A] FEHLER     {t.__name__:40s} {type(ex).__name__}: {ex}")
    print(f"\n{len(ALLE_TESTS) - fehler}/{len(ALLE_TESTS)} Tests bestanden "
          f"(numerisch verifiziert für L in {TEST_L}; kein Beweis für andere L).")
    return fehler


# ---------------------------------------------------------------------------
# Lauf für ein L
# ---------------------------------------------------------------------------

def rechne(L, gerade=False, rtol=1e-12, lu_max=200_000, fenster=4.5):
    t_ges = time.perf_counter()
    g = Relativgraph(L, gerade)
    h, info, t_poisson = loese_poisson(g, rtol=rtol, lu_max=lu_max)
    Ep, Ed = energien(g, h)
    ff = fernfeld(g)
    rho, deg4 = steifigkeit_L2(g, Ep)
    groessen = np.bincount(g.labels)
    fo = fourier(g)
    # Ist d_2 Eigenvektor des Generators? Dann ist h_2 = d_2 / lambda exakt lokal.
    dd = float(g.d2 @ g.d2)
    lam = float(g.d2 @ (g.Lap @ g.d2)) / dd if dd else float("nan")
    eig_res = float(np.linalg.norm(g.Lap @ g.d2 - lam * g.d2) / np.linalg.norm(lam * g.d2)) if dd else 0.0
    iters = [r["iter"] for r in info if r["iter"]]
    resid = [r["res"] for r in info if r["iter"]]
    lud = [r["lu_diff"] for r in info if r["iter"] and np.isfinite(r["lu_diff"])]
    zeile = dict(
        L=L, gerade=int(gerade), zustaende=g.N, komponenten=g.ncomp,
        groesste_komponente=int(groessen.max()), gerichtete_uebergaenge=g.M,
        fehlende_zielzustaende=g.fehlend, unzulaessig_im_index=g.falsch_im_index,
        max_multiplizitaet=g.max_multiplizitaet(), max_asymmetrie=g.max_asymmetrie(),
        zustaende_drift_ne0=ff["n_drift"], max_komponentensumme=float(np.abs(g.komponentensummen2()).max() / 2),
        E2=float(Ep.sum()), E2_dirichlet=float(Ed.sum()),
        rel_diff_poisson_dirichlet=float(abs(Ep.sum() - Ed.sum()) / max(abs(Ep.sum()), 1e-300)),
        cg_iter_max=max(iters) if iters else 0, residuum_max=max(resid) if resid else 0.0,
        lu_diff_max=max(lud) if lud else float("nan"),
        rho_s_L2=rho, grad_viertel=deg4, paramagnetisch=deg4 - rho,
        monopol=ff["monopol2"] / 2, dipol_x=ff["dipol_x"], dipol_y=ff["dipol_y"],
        dipol_x_hv=ff["dipol_x_hv"], dipol_x_vh=ff["dipol_x_vh"],
        dipol_y_hv=ff["dipol_y_hv"], dipol_y_vh=ff["dipol_y_vh"],
        fourier_gesamt_max=float(max(max(fo[r]["gesamt"]) for r in fo)),
        fourier_exp_hv_x=fourier_exponent(fo["x"]["k"], fo["x"]["hv"]),
        fourier_exp_hv_y=fourier_exponent(fo["y"]["k"], fo["y"]["hv"]),
        lambda_rayleigh=lam, eigen_residuum=eig_res, max_abs_A_d=float(np.abs(g.A @ g.d2).max()),
        radius_drift=ff["radius_drift"], radius_blockiert=ff["radius_blockiert"],
        fernfeld_frei=int(ff["aussen_voller_grad"]),
        t_aufbau_s=g.t_aufbau, t_komponenten_s=g.t_komp, t_poisson_s=t_poisson,
        t_gesamt_s=time.perf_counter() - t_ges,
        peak_rss_MB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
    )
    # Nahbereich für die Bilder
    mx2, my2 = g.mitte2()
    nah = np.maximum(np.abs(mx2), np.abs(my2)) <= 2 * fenster
    nahfeld = dict(alpha=g.alpha[nah].tolist(), beta=g.beta[nah].tolist(),
                   mx=(mx2[nah] / 2).tolist(), my=(my2[nah] / 2).tolist(),
                   d2=g.d2[nah].tolist(), h2=h[nah].tolist(), grad=g.grad[nah].tolist(),
                   komp=g.labels[nah].tolist(), voll_grad=g.voll_grad)
    return dict(zeile=zeile, fourier=fo, nahfeld=nahfeld)


# ---------------------------------------------------------------------------
# Bilder
# ---------------------------------------------------------------------------

BLAU, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
ROT, GRAU_MITTE, TEXT2 = "#e34948", "#f0efec", "#52514e"


def bilder(ergebnisse, ausgabe):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap, ListedColormap, BoundaryNorm

    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False,
                         "axes.edgecolor": TEXT2, "axes.labelcolor": "#0b0b0b",
                         "xtick.color": TEXT2, "ytick.color": TEXT2, "font.size": 10,
                         "axes.grid": True, "grid.color": "#e6e5e1", "grid.linewidth": 0.6,
                         "figure.facecolor": "#fcfcfb", "axes.facecolor": "#fcfcfb"})
    zs = sorted((e["zeile"] for e in ergebnisse), key=lambda z: z["L"])
    Ls = np.array([z["L"] for z in zs], float)
    E = np.array([z["E2"] for z in zs])

    for name, x, xl in (("E2_gegen_L", Ls, "L"), ("E2_gegen_logL", np.log(Ls), "log L")):
        fig, ax = plt.subplots(figsize=(5.2, 3.6))
        ax.plot(x, E, color=BLAU, lw=2, marker="o", ms=8, mec="#fcfcfb", mew=2)
        ax.set_xlabel(xl)
        ax.set_ylabel(r"$E_2(L)=\langle d_2,\mathcal{L}_{\rm rel}^{-1}d_2\rangle$")
        ax.set_title(r"$H^{-1}$-Energie der Zwei-Paar-Drift", loc="left")
        fig.tight_layout()
        fig.savefig(os.path.join(ausgabe, name + ".png"), dpi=150)
        plt.close(fig)

    if len(Ls) >= 3:
        # Abweichung von E_2(L_max); bei exakter L-Unabhängigkeit auf Rundungsniveau
        fig, ax = plt.subplots(figsize=(5.2, 3.6))
        diff = np.abs(E - E[-1]) / abs(E[-1])
        boden = np.finfo(float).eps
        ax.semilogy(Ls, np.maximum(diff, boden), color=BLAU, lw=2, marker="o", ms=8,
                    mec="#fcfcfb", mew=2)
        ax.axhline(boden, color=TEXT2, lw=1, ls="--")
        ax.annotate("Maschinengenauigkeit", (Ls[0], boden), color=TEXT2, xytext=(0, 4),
                    textcoords="offset points", fontsize=8)
        ax.set_xlabel("L")
        ax.set_ylabel(rf"$|E_2(L)-E_2({int(Ls[-1])})|\,/\,E_2$")
        ax.set_title("Abhängigkeit von L", loc="left")
        fig.tight_layout()
        fig.savefig(os.path.join(ausgabe, "E2_konvergenz.png"), dpi=150)
        plt.close(fig)

    gross = max(ergebnisse, key=lambda e: e["zeile"]["L"])
    zl = gross["zeile"]
    fo = gross["fourier"]
    boden = 1e-17
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    reihen = ((("x", "hv"), r"Sektor (h,v), $k\parallel e_x$", BLAU, "-"),
              (("y", "hv"), r"Sektor (h,v), $k\parallel e_y$", ORANGE, "-"),
              (("diag", "hv"), r"Sektor (h,v), $k\parallel(1,1)$", AQUA, "-"),
              (("x", "gesamt"), r"Summe aller Sektoren, $k\parallel e_x$", TEXT2, ":"))
    for (rich, sek), lab, col, ls in reihen:
        k = np.array(fo[rich]["k"])
        a = np.maximum(np.array(fo[rich][sek]), boden)
        ax.loglog(k, a, color=col, lw=2, ls=ls, marker="o", ms=4, label=lab)
    k = np.array(fo["x"]["k"])
    if abs(zl["dipol_x_hv"]) > 0:
        ax.loglog(k, abs(zl["dipol_x_hv"]) * k, color="#0b0b0b", lw=1, ls="--",
                  label=rf"$|p_x^{{hv}}|\,|k|$, $p_x^{{hv}}={zl['dipol_x_hv']:+.2f}$")
    ax.set_xlabel(r"$|k|$")
    ax.set_ylabel(r"$|\widehat{d}_2(k)|$  (Boden $10^{-17}$ = null)")
    ax.set_title(f"Fourier-Betrag der Drift, L = {zl['L']}", loc="left")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(ausgabe, "fourier_d2.png"), dpi=150)
    plt.close(fig)

    nf = gross["nahfeld"]
    al, be = np.array(nf["alpha"]), np.array(nf["beta"])
    mx, my = np.array(nf["mx"]), np.array(nf["my"])

    def vierfeld(werte, titel, datei, cmap, norm, cbar_label, ticks=None, komp=None):
        fig, axs = plt.subplots(2, 2, figsize=(8.4, 8.0), sharex=True, sharey=True)
        for a in (H, V):
            for b in (H, V):
                ax = axs[a, b]
                m = (al == a) & (be == b)
                sc = ax.scatter(mx[m], my[m], c=werte[m], cmap=cmap, norm=norm, s=60, marker="s",
                                edgecolors="#fcfcfb", linewidths=1.0)
                ax.scatter([0], [0], marker="+", s=80, color="#0b0b0b")
                ax.set_title(f"Paar 1 {ONAME[a]}, Paar 2 {ONAME[b]}", loc="left", fontsize=10)
                ax.set_aspect("equal")
                if komp is not None and len(set(komp.tolist())) > 1:
                    for xx, yy, kk in zip(mx[m], my[m], komp[m]):
                        ax.annotate(str(kk), (xx, yy), fontsize=5, ha="center", va="center")
        for ax in axs[1]:
            ax.set_xlabel(r"$m_x$ (Mitte 2 $-$ Mitte 1)")
        for ax in axs[:, 0]:
            ax.set_ylabel(r"$m_y$")
        fig.suptitle(titel, x=0.02, ha="left")
        fig.colorbar(sc, ax=axs, shrink=0.6, label=cbar_label, ticks=ticks)
        fig.savefig(os.path.join(ausgabe, datei), dpi=150)
        plt.close(fig)

    dcm = ListedColormap(["#1c5cab", "#6da7ec", "#d9d8d4", "#f2a3a2", ROT])
    dnorm = BoundaryNorm([-1.25, -0.75, -0.25, 0.25, 0.75, 1.25], dcm.N)
    vierfeld(np.array(nf["d2"]), f"Drift $d_2(s)$ im Nahbereich, L = {zl['L']}", "drift_nahbereich.png",
             dcm, dnorm, r"$d_2$", ticks=[-1, -0.5, 0, 0.5, 1])
    hv = np.array(nf["h2"])
    hm = max(np.abs(hv).max(), 1e-12)
    hcm = LinearSegmentedColormap.from_list("bgr", [BLAU, GRAU_MITTE, ROT])
    vierfeld(hv, f"Korrektor $h_2(s)$ im Nahbereich, L = {zl['L']}", "korrektor_nahbereich.png",
             hcm, matplotlib.colors.Normalize(-hm, hm), r"$h_2$")
    gcm = ListedColormap(["#0d366b", "#104281", "#184f95", "#1c5cab", "#256abf", "#3987e5",
                          "#6da7ec", "#9ec5f4", "#cde2fb"][: nf["voll_grad"] + 1][::-1][::-1])
    gnorm = BoundaryNorm(np.arange(-0.5, nf["voll_grad"] + 1.5), gcm.N)
    vierfeld(np.array(nf["grad"]), f"Erlaubte Sprünge und Komponenten, L = {zl['L']}"
             + (" (eine Komponente)" if zl["komponenten"] == 1 else ""),
             "grad_komponenten_nahbereich.png", gcm, gnorm, "Zahl erlaubter Sprünge",
             ticks=list(range(nf["voll_grad"] + 1)), komp=np.array(nf["komp"]))


# ---------------------------------------------------------------------------
# Hauptprogramm
# ---------------------------------------------------------------------------

SPALTEN = [("L", "{:>5d}"), ("zustaende", "{:>9d}"), ("komponenten", "{:>5d}"),
           ("groesste_komponente", "{:>9d}"), ("gerichtete_uebergaenge", "{:>10d}"),
           ("fehlende_zielzustaende", "{:>4d}"), ("max_asymmetrie", "{:>5.1g}"),
           ("zustaende_drift_ne0", "{:>4d}"), ("max_komponentensumme", "{:>5.1g}"),
           ("E2", "{:>12.8f}"), ("rel_diff_poisson_dirichlet", "{:>8.1e}"), ("cg_iter_max", "{:>6d}"),
           ("residuum_max", "{:>8.1e}"), ("t_aufbau_s", "{:>7.3f}"), ("t_komponenten_s", "{:>7.3f}"),
           ("t_poisson_s", "{:>8.3f}"), ("peak_rss_MB", "{:>7.0f}")]
KOEPFE = ["L", "Zustände", "Komp", "größte", "Übergänge", "fehl", "asym", "d≠0", "ΣC", "E_2",
          "P−D", "CG-it", "Resid", "t_Graph", "t_Komp", "t_Poiss", "RSS MB"]


def lauf(args):
    os.makedirs(args.out, exist_ok=True)
    kw = dict(gerade=args.gerade, rtol=args.rtol, lu_max=args.lu_max)
    t0 = time.perf_counter()
    if args.jobs > 1:
        with ProcessPoolExecutor(max_workers=args.jobs, max_tasks_per_child=1) as ex:
            ergebnisse = list(ex.map(rechne, args.L, *[[kw[k]] * len(args.L) for k in ("gerade", "rtol", "lu_max")]))
    else:
        ergebnisse = [rechne(L, **kw) for L in args.L]
    ergebnisse.sort(key=lambda e: e["zeile"]["L"])
    print(" ".join(f"{k:>{len(f.format(0 if 'd' in f else 0.0))}s}" for k, (_, f) in zip(KOEPFE, SPALTEN)))
    for e in ergebnisse:
        z = e["zeile"]
        print(" ".join(f.format(z[k]) for k, f in SPALTEN))
    print("\nZusatz je L: rho_s L^2/t_c (RK, größte Komponente), Dipol, Radien")
    for e in ergebnisse:
        z = e["zeile"]
        print(f"  L={z['L']:4d}  rho_s L^2 = {z['rho_s_L2']:.8f}  <deg>/4 = {z['grad_viertel']:.8f}  "
              f"paramagnetisch = {z['paramagnetisch']:.3e}  p = ({z['dipol_x']:+.3f}, {z['dipol_y']:+.3f})  "
              f"Radius Drift {z['radius_drift']}  Blockade {z['radius_blockiert']}  "
              f"Fernfeld frei {bool(z['fernfeld_frei'])}  LU-Diff {z['lu_diff_max']:.1e}")
    suffix = "_gerade" if args.gerade else ""
    csvpfad = os.path.join(args.out, f"zweipaar{suffix}.csv")
    with open(csvpfad, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(ergebnisse[0]["zeile"].keys()))
        w.writeheader()
        for e in ergebnisse:
            w.writerow(e["zeile"])
    with open(os.path.join(args.out, f"zweipaar{suffix}_fourier.json"), "w") as fh:
        json.dump({e["zeile"]["L"]: e["fourier"] for e in ergebnisse}, fh)
    if not args.keine_bilder:
        bilder(ergebnisse, args.out)
    print(f"\nCSV: {csvpfad}   Gesamtzeit {time.perf_counter() - t0:.1f} s   pyamg: {HAT_PYAMG}")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="befehl", required=True)
    sub.add_parser("selbsttest", help="alle automatischen Tests")
    q = sub.add_parser("lauf", help="Rechnung für mehrere L")
    q.add_argument("--L", type=int, nargs="+", default=[16, 24, 32, 48, 64, 96])
    q.add_argument("--jobs", type=int, default=1, help="parallele Prozesse (je L einer)")
    q.add_argument("--gerade", action="store_true", help="auch gerade Schritte (nicht Stufe A)")
    q.add_argument("--rtol", type=float, default=1e-12)
    q.add_argument("--lu-max", type=int, default=200_000, help="LU-Gegenprobe bis zu dieser Komponentengröße")
    q.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "ergebnisse"))
    q.add_argument("--keine-bilder", action="store_true")
    a = p.parse_args(argv)
    if a.befehl == "selbsttest":
        sys.exit(1 if selbsttest() else 0)
    lauf(a)


if __name__ == "__main__":
    main()
