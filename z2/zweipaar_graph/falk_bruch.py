#!/usr/bin/env python
"""Dyson-Lieb-Simon-Kette ohne Reflexionspositivität, exakt auf kleinen Tori: Stufe A oder harte Bosonen.

Objekte: Stufe A = Bindungen (Paare, Ausschlusszone 22, Eckschritte, Mittelgitter-Impulse);
         harte Bosonen = Plätze (nur Ausschluss auf demselben Platz, Nächstnachbar-Sprünge, Quadratgitter-Impulse).
Ordnungsparameter A_k = M^(-1/2) sum_j exp(i k.r_j) a_j (M = Zahl der Objekte), a_j entfernt das Teilchen auf j,
a_j^+ setzt eines, falls verträglich (d-Eichung bei Stufe A). Großkanonisch H - mu N, Grundzustand im Sektor N,
mu in (E0(N) - E0(N-1), E0(N+1) - E0(N)).

Für jedes k exakt: n_k = <A^+A>, m_k = <AA^+>, g_k = (n_k + m_k)/2,
  c_k   = <[A^+,[H_mu,A]]>                     (Doppelkommutator, Erwartungswert lokaler Operatoren)
  chi_k = <A^+(H-E0+mu)^-1 A> + <A(H-E0-mu)^-1 A^+>   (statische Suszeptibilität)
Falk-Bruch: g_k <= 1/2 sqrt(c_k chi_k). Summenregel sum_k (n_k + m_k) = N + Phi.
Kette: g_0 >= (N + Phi)/2 - sum_{k != 0} 1/2 sqrt(c_k chi_k)  -> Vergleich mit exaktem g_0.
Die Kette ist das Gerüst von Dyson-Lieb-Simon / Kennedy-Lieb-Shastry; dort wird chi_k durch die
Infrarotschranke ersetzt (Reflexionspositivität), hier durch den exakten Wert (bester Fall).

Aufruf: python falk_bruch.py --modell bosonen --L 4 --N 8 [--mu-anteil 0.5]
        python falk_bruch.py --modell stufe_a --L 8 --N 3
"""

import argparse
import json
import os
import time

import numpy as np
import pyamg
import scipy.sparse as sp
from scipy.sparse.linalg import cg, eigsh

import siebenachtel_8x8 as s8
import two_pair_graph as tp

HIER = os.path.dirname(os.path.abspath(__file__))


def geometrie(modell, L):
    """kompat (MxM, True = verträglich), ziel (M x 4), Positionen rx, ry, k-Gitter (Liste von (kx, ky))."""
    if modell == "stufe_a":
        ax, ay, o = s8.bindungen(L)
        M = ax.size
        anker = np.stack([ax, ay], 1)
        kompat = tp.kompatibel(L, anker[:, None, :], o[:, None], anker[None, :, :], o[None, :])
        np.fill_diagonal(kompat, False)
        tab = tp.schritt_tabelle()
        ziel = np.array([[((ax[b] + s[0]) % L * L + (ay[b] + s[1]) % L) * 2 + s[2] for s in tab[o[b]]]
                         for b in range(M)])
        rx, ry = ax + 0.5 * (o == 0), ay + 0.5 * (o == 1)
        kgitter = [(2 * np.pi * n1 / L, 2 * np.pi * n2 / L) for n1 in range(2 * L) for n2 in range(L)]
    elif modell == "bosonen1d":
        M = L
        x = np.arange(M)
        kompat = ~np.eye(M, dtype=bool)
        ziel = np.stack([(x + 1) % L, (x - 1) % L], 1)
        rx, ry = x.astype(float), np.zeros(M)
        kgitter = [(2 * np.pi * n1 / L, 0.0) for n1 in range(L)]
    else:
        M = L * L
        x, y = np.arange(M) // L, np.arange(M) % L
        kompat = ~np.eye(M, dtype=bool)
        ziel = np.stack([((x + dx) % L) * L + (y + dy) % L for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))], 1)
        rx, ry = x.astype(float), y.astype(float)
        kgitter = [(2 * np.pi * n1 / L, 2 * np.pi * n2 / L) for n1 in range(L) for n2 in range(L)]
    return kompat, ziel, rx, ry, kgitter


class Sektor:
    def __init__(self, N, kompat, ziel):
        M = kompat.shape[0]
        self.N = N
        if N == 0:
            self.T = np.zeros((1, 0), np.int64)
            self.keys = np.zeros(1, np.int64)
            self.n = 1
            self.H = sp.csr_matrix((1, 1))
            return
        self.T = s8.konfigurationen(None, N, kompat)
        self.n = self.T.shape[0]
        self.keys = s8.schluessel(self.T, M)
        src, dst = [], []
        for p in range(N):
            for k in range(ziel.shape[1]):
                neu = ziel[self.T[:, p], k]
                ok = np.ones(self.n, bool)
                for i in range(N):
                    if i != p:
                        ok &= kompat[neu, self.T[:, i]]
                idx = np.nonzero(ok)[0]
                Tn = self.T[idx].copy()
                Tn[:, p] = neu[idx]
                Tn.sort(axis=1)
                src.append(idx)
                dst.append(np.searchsorted(self.keys, s8.schluessel(Tn, M)))
        src, dst = np.concatenate(src), np.concatenate(dst)
        A = sp.coo_matrix((np.ones(src.size), (src, dst)), shape=(self.n, self.n)).tocsr()
        self.H = (-A).tocsr()


def entfernen(oben, unten, M):
    idx = np.zeros((oben.n, oben.N), np.int64)
    for i in range(oben.N):
        rest = np.delete(oben.T, i, axis=1)
        k = s8.schluessel(rest, M) if oben.N > 1 else np.zeros(oben.n, np.int64)
        j = np.searchsorted(unten.keys, k)
        assert np.all(unten.keys[j] == k)
        idx[:, i] = j
    return idx


def loese(Mat, b, ml):
    x, _ = cg(Mat, b, rtol=1e-11, atol=0.0, M=ml.aspreconditioner(), maxiter=3000)
    r = np.linalg.norm(Mat @ x - b) / max(np.linalg.norm(b), 1e-300)
    if r > 1e-7:
        raise RuntimeError(f"CG: Residuum {r:.1e}")
    return x


def grundzustand(H):
    if H.shape[0] == 1:
        return 0.0, np.ones(1)
    w, v = eigsh(-H, k=1, which="LA", tol=1e-12)
    psi = np.abs(v[:, 0])
    return -float(w[0]), psi / np.linalg.norm(psi)


def rechne(modell, L, N, mu_anteile):
    t0 = time.perf_counter()
    kompat, ziel, rx, ry, kgitter = geometrie(modell, L)
    M = kompat.shape[0]
    S = {q: Sektor(q, kompat, ziel) for q in (N - 1, N, N + 1)}
    E0 = {q: grundzustand(S[q].H)[0] for q in S}
    _, psi = grundzustand(S[N].H)
    mu_lo, mu_hi = E0[N] - E0[N - 1], E0[N + 1] - E0[N]
    print(f"{modell} L={L} N={N} (Dichte {N / M:.4f} je Objekt): Dimensionen {S[N-1].n}/{S[N].n}/{S[N+1].n}; "
          f"mu-Intervall ({mu_lo:.4f}, {mu_hi:.4f}) konvex {mu_lo < mu_hi}  [{time.perf_counter() - t0:.0f} s]",
          flush=True)
    ab = entfernen(S[N], S[N - 1], M) if N > 0 else None
    auf = entfernen(S[N + 1], S[N], M)
    nrm = 1.0 / np.sqrt(M)

    def u_vec(k):
        ph = np.exp(1j * (k[0] * rx[S[N].T] + k[1] * ry[S[N].T])) * psi[:, None]
        return nrm * (np.bincount(ab.ravel(), weights=ph.real.ravel(), minlength=S[N - 1].n)
                      + 1j * np.bincount(ab.ravel(), weights=ph.imag.ravel(), minlength=S[N - 1].n))

    def v_vec(k):
        ph = np.exp(-1j * (k[0] * rx[S[N + 1].T] + k[1] * ry[S[N + 1].T]))
        return nrm * (ph * psi[auf]).sum(axis=1)

    vek = [(u_vec(k), v_vec(k)) for k in kgitter]
    nk = np.array([np.vdot(u, u).real for u, _ in vek])
    mk = np.array([np.vdot(v, v).real for _, v in vek])
    Phi = float(mk.sum())
    gk = 0.5 * (nk + mk)
    i0 = 0
    assert abs(kgitter[0][0]) + abs(kgitter[0][1]) == 0
    assert abs(nk.sum() - N) < 1e-8
    print(f"  Summenregeln: sum n_k = {nk.sum():.6f}, Phi = sum m_k = {Phi:.4f}; Kondensat n_0/N = {nk[i0] / N:.4f}, "
          f"g_0 = {gk[i0]:.4f}  [{time.perf_counter() - t0:.0f} s]", flush=True)
    erg = []
    for f in mu_anteile:
        mu = mu_lo + f * (mu_hi - mu_lo)
        Mm = (S[N - 1].H + (mu - E0[N]) * sp.identity(S[N - 1].n)).tocsr()
        Mp = (S[N + 1].H + (-mu - E0[N]) * sp.identity(S[N + 1].n)).tocsr()
        mlm = pyamg.smoothed_aggregation_solver(Mm, symmetry="symmetric") if S[N - 1].n > 1 else None
        mlp = pyamg.smoothed_aggregation_solver(Mp, symmetry="symmetric")
        ck, chik = np.zeros(len(kgitter)), np.zeros(len(kgitter))
        cm_k, chim_k = np.zeros(len(kgitter)), np.zeros(len(kgitter))      # nur Entfernungsseite (A psi)
        cache = {}
        for j, (k, (u, v)) in enumerate(zip(kgitter, vek)):
            schl = (round(np.cos(k[0]) * 1e9), round(np.cos(k[1]) * 1e9))   # k und -k gleich (psi reell)
            ck[j] = np.vdot(u, Mm @ u).real + np.vdot(v, Mp @ v).real
            if schl in cache and False:
                chik[j] = cache[schl]
                continue
            chi = 0.0
            for seite, (vec, Mat, ml) in enumerate(((u, Mm, mlm), (v, Mp, mlp))):
                for teil in (vec.real, vec.imag):
                    if np.any(teil):
                        beitrag = float(teil @ (loese(Mat, teil, ml) if ml is not None else teil / Mat[0, 0]))
                        chi += beitrag
                        if seite == 0:
                            chim_k[j] += beitrag
            chik[j] = chi
            cm_k[j] = np.vdot(u, Mm @ u).real
        schr = 0.5 * np.sqrt(ck * chik)
        assert np.all(gk <= schr * (1 + 1e-8)), "Falk-Bruch verletzt"
        rest = np.delete(schr, i0).sum()
        exakt_rest = np.delete(gk, i0).sum()
        g0_u = 0.5 * (N + Phi) - rest
        # einseitige Kette: n_k <= sqrt(c^- chi^-), n_0 >= N - sum_{k != 0} sqrt(c^- chi^-)
        einseitig = np.sqrt(cm_k * chim_k)
        assert np.all(nk <= einseitig * (1 + 1e-8) + 1e-14)
        n0_ein = N - np.delete(einseitig, i0).sum()
        print(f"    einseitig: n_0 exakt {nk[i0]:.4f}, Kette n_0 >= {n0_ein:+.4f} ({100 * n0_ein / nk[i0]:+.0f} %); "
              f"sum_k!=0 sqrt(c-chi-) = {np.delete(einseitig, i0).sum():.4f} gegen sum n_k = {np.delete(nk, i0).sum():.4f}",
              flush=True)
        if modell in ("bosonen", "bosonen1d"):
            kk = np.array(kgitter)
            Ek = (4 - 2 * np.cos(kk[:, 0]) - 2 * np.cos(kk[:, 1])) if modell == "bosonen" else (2 - 2 * np.cos(kk[:, 0]))
            nz = Ek > 1e-12
            rho_ = N / M
            print(f"    einseitige Ungleichungen: max chi-*E/rho = {(chim_k[nz] * Ek[nz]).max() / rho_:.3f}, "
                  f"max chi+*E/(1-rho) = {((chik - chim_k)[nz] * Ek[nz]).max() / (1 - rho_):.3f}, "
                  f"C = max c-/rho = {cm_k[nz].max() / rho_:.3f}", flush=True)
        e = dict(mu_anteil=f, mu=mu, k=[list(k) for k in kgitter], n_k=nk.tolist(), m_k=mk.tolist(),
                 c_k=ck.tolist(), chi_k=chik.tolist(), cm_k=cm_k.tolist(), chim_k=chim_k.tolist(),
                 n0_einseitig=float(n0_ein),
                 g0_exakt=float(gk[i0]), g0_schranke=float(g0_u),
                 anteil_g0_garantiert=float(g0_u / gk[i0]), summe_schranke=float(rest), summe_exakt=float(exakt_rest),
                 faktor=float(rest / exakt_rest), straffheit_min=float((gk / schr).min()),
                 straffheit_k0=float(gk[i0] / schr[i0]))
        erg.append(e)
        print(f"  mu-Anteil {f:.2f}: g_0 exakt {gk[i0]:.4f}, Kette garantiert {g0_u:+.4f} "
              f"({100 * g0_u / gk[i0]:+.0f} %); sum_k!=0 Schranke {rest:.4f} gegen exakt {exakt_rest:.4f} "
              f"(Faktor {rest / exakt_rest:.3f})  [{time.perf_counter() - t0:.0f} s]", flush=True)
        if modell in ("bosonen", "bosonen1d"):
            # Infrarotschranke (Gaußsche Dominanz, Dyson-Lieb-Simon): chi(k) <= 1/(J E(k)), J = 1
            kk = np.array(kgitter)
            Ek = (4 - 2 * np.cos(kk[:, 0]) - 2 * np.cos(kk[:, 1])) if modell == "bosonen" else (2 - 2 * np.cos(kk[:, 0]))
            nz = Ek > 1e-12
            ratio = chik[nz] * Ek[nz]
            schr_ir = 0.5 * np.sqrt(ck[nz] / Ek[nz])
            g0_ir = 0.5 * (N + Phi) - schr_ir.sum()
            e.update(ir_verhaeltnis_max=float(ratio.max()), ir_verhaeltnis_min=float(ratio.min()),
                     ir_verletzt=int((ratio > 1 + 1e-9).sum()), g0_schranke_ir=float(g0_ir),
                     summe_schranke_ir=float(schr_ir.sum()))
            print(f"    Infrarot: chi*E(k) in [{ratio.min():.3f}, {ratio.max():.3f}] (<= 1 verlangt; verletzt in "
                  f"{e['ir_verletzt']} von {nz.sum()} Moden); Kette mit chi -> 1/E: garantiert {g0_ir:+.4f} "
                  f"({100 * g0_ir / gk[i0]:+.0f} % von g_0)", flush=True)
    return dict(modell=modell, L=L, N=N, M=M, dichte=N / M, n0_durch_N=float(nk[i0] / N), Phi=Phi,
                g0=float(gk[i0]), ergebnisse=erg)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modell", choices=["stufe_a", "bosonen", "bosonen1d"], default="bosonen")
    ap.add_argument("--L", type=int, default=4)
    ap.add_argument("--N", type=int, nargs="+", default=[8])
    ap.add_argument("--mu-anteil", type=float, nargs="+", default=[0.5])
    a = ap.parse_args()
    alle = [rechne(a.modell, a.L, N, a.mu_anteil) for N in a.N]
    pfad = os.path.join(HIER, "ergebnisse", f"falk_bruch_{a.modell}_L{a.L}_N{'_'.join(map(str, a.N))}.json")
    with open(pfad, "w") as fh:
        json.dump(alle, fh, indent=1)


if __name__ == "__main__":
    main()
