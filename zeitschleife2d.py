#!/usr/bin/env python3
"""Zeitschleife auf dem 2D-Torus ohne Verwerfung durch leere Zellen (Anhang Z, Z.10).

Testgröße: Ausbeute |ν|²/∫f²dµ ≤ |µ| = q0 (Cauchy–Schwarz), f = dν/dµ; Effizienz = Ausbeute/q0.

Modell: harte Bosonen auf dem Lx×Ly-Torus, Trotter-Zeit mit vier Bindungsklassen (waagrecht gerade/ungerade, senkrecht
gerade/ungerade; Halbschritt h benutzt Klasse h mod 4), Gewicht lam^Sprünge. Zellen aus cx×cy Plätzen. Fenster [0, T],
T = S·w, aus w Scheiben zu S Halbschritten (S Vielfaches von 4).

Konstruktion (Anhang G.12.1 im Kleinen):
  Aufweg, Scheibe k: j0 = Stück am Loch, a0 = Endzelle von j0; Zug d unter den ausführbaren gezogen (Gesetz ∝ π(d));
    d = 0: j0 gelöscht, neues Loch = Ende von j0;  d ≠ 0: wählbares Stück j1 der Zelle a0+d gleichverteilt, Brücke
    j1: Anfang → Ende von j0 aus dem exakt bedingten Gesetz, j0 gelöscht, neues Loch = altes Ende von j1.
  Abweg, Scheibe k (von oben), Kopf oben gegeben:
    "zelle"     neuer Anfang gleichverteilt unter den freien Plätzen der Kopfzelle, Weg zum Kopf (keine Querschritte);
    "frei"      Spiegel: Zug d; d ≠ 0: wählbares Stück b der Zelle Kopfzelle+d wird zum Kopf umgeleitet, ein neues
                Stück läuft zum alten Ende von b; Anfang des neuen Stücks über alle freien Plätze mitgezogen;
    "festzelle" wie "frei", Anfang gleichverteilt unter den freien Plätzen der Zielzelle (Variante a);
    "zellgewicht" wie "frei", Anfang aus dem bedingten Gesetz, aber nur unter den freien Plätzen der Zielzelle;
    "ball"      wie "frei", Anfang aus dem bedingten Gesetz unter den freien Plätzen im Abstand ≤ --radius von Y_m.
  --querschritt: im Abweg kein d = 0.  Wählbar in c: Ende in c und (ohne --locker) Anfang in c.
  Ausführbar heißt: wählbare Liste nicht leer und (festzelle) ein freier Platz in der Zielzelle. Das hängt nur von
  Endpunkten ab; die Dichteformel führt die Normierung über die ausführbaren Züge mit. Verworfen wird nur, wenn ein
  gezogener Weg nicht existiert (harte Kerne, Reichweite).
Dichte f(O) = M · Σ (Gewichtsverhältnis · Rückwärtswahrscheinlichkeiten), dynamische Programmierung über die Scheiben
mit Zustand (Kopf, Loch); Zustandssummen markierter Teilchen per Vorwärts-DP (Pfade werden nur für den alten Weg des
umgeleiteten Stücks im Abweg aufgezählt).

Modi:
  exakt  alle Fenstergeschichten (Rest der Periode als Transfermatrix-Faktor, in ν und µ gleich) und alle Vorwärtszweige
         aufzählen, Vorwärtszweige über den unabhängigen langsamen beweger; prüft ν = fµ; exakte Ausbeute
  mc     C exakt gezogen (--beta > 0 periodisch, --beta 0 Grundzustand per Doob), Konstruktion zufällig, f exakt;
         Ausbeute = |ν| / E[f | angenommen]
Aufruf:
  python3 zeitschleife2d.py --modus exakt --Lx 4 --Ly 2 --N 2 --S 4 --beta 2 --w 2 --abweg festzelle --querschritt
  python3 zeitschleife2d.py --modus mc --Lx 6 --Ly 4 --N 6 --S 8 --beta 0 --w 2 --abweg festzelle --querschritt
"""
import argparse
import itertools
import time
from collections import defaultdict

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import LinearOperator, eigs


# ====================================================================== Gitter
class Gitter:
    def __init__(self, Lx, Ly, cx, cy, zuege_art='nachbar'):
        assert Lx % 2 == 0 and Ly % 2 == 0 and Lx % cx == 0 and Ly % cy == 0
        self.Lx, self.Ly, self.cx, self.cy = Lx, Ly, cx, cy
        self.M = Lx * Ly
        self.Kx, self.Ky = Lx // cx, Ly // cy
        klassen = [[], [], [], []]
        gesehen = set()
        for y in range(Ly):
            for x in range(Lx):
                i = self.idx(x, y)
                for (j, kl) in ((self.idx((x + 1) % Lx, y), 0 if x % 2 == 0 else 1),
                                (self.idx(x, (y + 1) % Ly), 2 if y % 2 == 0 else 3)):
                    b = frozenset((i, j))
                    if i != j and b not in gesehen:
                        gesehen.add(b)
                        klassen[kl].append((i, j))
        self.klassen = klassen
        self.partner = [dict() for _ in range(4)]
        for k in range(4):
            for (i, j) in klassen[k]:
                assert i not in self.partner[k] and j not in self.partner[k], "Klasse ist keine Paarung"
                self.partner[k][i] = j
                self.partner[k][j] = i
        self.bondplaetze = [set(self.partner[k]) for k in range(4)]
        self.bond_arrays = [(np.array([i for i, j in klassen[k]], dtype=int), np.array([j for i, j in klassen[k]], dtype=int))
                            for k in range(4)]
        zuege = [(0, 0)]
        if zuege_art == 'alle':
            zuege += [(dx, dy) for dy in range(self.Ky) for dx in range(self.Kx) if (dx, dy) != (0, 0)]
        elif self.Kx >= 3:
            zuege += [(1, 0), (-1, 0)]
        elif self.Kx == 2:
            zuege += [(1, 0)]
        if zuege_art == 'alle':
            pass
        elif self.Ky >= 3:
            zuege += [(0, 1), (0, -1)]
        elif self.Ky == 2:
            zuege += [(0, 1)]
        self.zuege = zuege
        self.zelle_von = [self._zelle(i) for i in range(self.M)]
        self.plaetze_in = defaultdict(list)
        for i in range(self.M):
            self.plaetze_in[self.zelle_von[i]].append(i)

    def idx(self, x, y):
        return x + self.Lx * y

    def abstand(self, i, j):
        dx = abs(i % self.Lx - j % self.Lx)
        dy = abs(i // self.Lx - j // self.Lx)
        return min(dx, self.Lx - dx) + min(dy, self.Ly - dy)

    def _zelle(self, i):
        x, y = i % self.Lx, i // self.Lx
        return (x // self.cx) + self.Kx * (y // self.cy)

    def zelle(self, i):
        return self.zelle_von[i]

    def zellschritt(self, c, d):
        cx_, cy_ = c % self.Kx, c // self.Kx
        return (cx_ + d[0]) % self.Kx + self.Kx * ((cy_ + d[1]) % self.Ky)

    def zellschritt_inv(self, c, d):
        return self.zellschritt(c, (-d[0], -d[1]))

    # -------------------------------------------------------------- Übergänge ganzer Konfigurationen
    def uebergaenge(self, conf, h):
        k = h % 4
        aktiv = [(i, j) for (i, j) in self.klassen[k] if (i in conf) != (j in conf)]
        erg = []
        for maske in itertools.product((0, 1), repeat=len(aktiv)):
            neu = set(conf)
            for (i, j), s in zip(aktiv, maske):
                if s:
                    if i in neu:
                        neu.remove(i); neu.add(j)
                    else:
                        neu.remove(j); neu.add(i)
            erg.append((frozenset(neu), sum(maske)))
        return erg

    def spruenge(self, c0, c1, h):
        k = h % 4
        n = 0
        for (i, j) in self.klassen[k]:
            vor = (i in c0, j in c0)
            nach = (i in c1, j in c1)
            if sum(vor) != sum(nach):
                return None
            if vor != nach:
                if sum(vor) != 1:
                    return None
                n += 1
        bp = self.bondplaetze[k]
        if {p for p in c0 if p not in bp} != {p for p in c1 if p not in bp}:
            return None
        return n

    def spr_andere(self, a0, a1, h):
        k = h % 4
        return sum(1 for (i, j) in self.klassen[k] if (i in a0, j in a0) != (i in a1, j in a1))

    def bahnen(self, confs, t0, t1, h0):
        tr = [[p] for p in sorted(confs[t0])]
        for t in range(t0, t1):
            k = (h0 + t - t0) % 4
            nach = confs[t + 1]
            for b in tr:
                p = b[-1]
                if p in nach:
                    b.append(p)
                else:
                    q = self.partner[k].get(p)
                    assert q is not None and q in nach and q not in confs[t]
                    b.append(q)
        return [tuple(b) for b in tr]

    def beweger(self, starts, enden, andere_occ, h0, aufzaehlen=False):
        """Unabhängige (langsame) Aufzählung: Geschichten markierter Teilchen starts → enden bei festen anderen."""
        n = len(starts)
        schritte = len(andere_occ) - 1
        if n == 0:
            return [((), 0)] if aufzaehlen else {0: 1}
        if any(p in andere_occ[0] for p in starts) or len(set(starts)) < n:
            return [] if aufzaehlen else {}
        zust = {tuple(starts): [((tuple(starts),), 0)]} if aufzaehlen else {tuple(starts): {0: 1}}
        for t in range(schritte):
            h = h0 + t
            k = h % 4
            neu = defaultdict(list) if aufzaehlen else defaultdict(lambda: defaultdict(int))
            sa = self.spr_andere(andere_occ[t], andere_occ[t + 1], h)
            for pos, daten in zust.items():
                optionen = []
                for p in pos:
                    q = self.partner[k].get(p)
                    optionen.append([p] if q is None else [p, q])
                for wahl in itertools.product(*[range(len(o)) for o in optionen]):
                    nach = tuple(o[w] for o, w in zip(optionen, wahl))
                    if len(set(nach)) < n:
                        continue
                    c0 = frozenset(pos) | andere_occ[t]
                    c1 = frozenset(nach) | andere_occ[t + 1]
                    if len(c0) != n + len(andere_occ[t]) or len(c1) != n + len(andere_occ[t + 1]):
                        continue
                    hs = self.spruenge(c0, c1, h)
                    if hs is None or hs != sum(wahl) + sa:
                        continue
                    kk = sum(wahl)
                    if aufzaehlen:
                        for (wege, k0) in daten:
                            neu[nach].append((wege + (nach,), k0 + kk))
                    else:
                        for k0, v in daten.items():
                            neu[nach][k0 + kk] += v
            zust = neu
        ziel = tuple(enden)
        if aufzaehlen:
            return zust.get(ziel, [])
        return dict(zust.get(ziel, {}))


# ====================================================================== Modell
class Schleife:
    def __init__(self, G, N, S, w, lam, abweg, querschritt, locker, p0=0.3, radius=1, nie_quer=False):
        self.G, self.N, self.S, self.w, self.lam = G, N, S, w, lam
        self.radius = radius
        self.ball = [[j for j in range(G.M) if G.abstand(i, j) <= radius] for i in range(G.M)]
        self.abweg, self.querschritt, self.locker = abweg, querschritt, locker
        self.M = G.M
        nz = len(G.zuege) - 1
        assert nz >= 1
        self.pi_auf = {d: (p0 if d == (0, 0) else (1 - p0) / nz) for d in G.zuege}
        if nie_quer:
            assert not querschritt
            self.pi_ab = {(0, 0): 1.0}
        elif querschritt:
            self.pi_ab = {d: 1.0 / nz for d in G.zuege if d != (0, 0)}
        else:
            self.pi_ab = dict(self.pi_auf)
        self.lp = [lam ** j for j in range(S * (N + 2) + 4)]
        self.verworfen = defaultdict(int)
        self.numpy_phi = True
        self.leeren()

    def leeren(self):
        self._lage = {}
        self._phi = {}
        self._bew = {}
        self._Tc = {}
        self._phim = {}

    # ---------------------------------------------------------- numpy: Schrittmatrizen und Propagatoren
    def T_liste(self, occ, h4):
        """Schrittmatrizen eines markierten Teilchens bei festen anderen occ: T[p, n] = Gewicht p → n."""
        key = (occ, h4)
        r = self._Tc.get(key)
        if r is not None:
            return r
        M, lam = self.M, self.lam
        diag = np.arange(M)
        r = []
        for t in range(self.S):
            k = (h4 + t) % 4
            frei0 = np.ones(M, bool)
            frei0[list(occ[t])] = False
            bleib = frei0.copy()
            bleib[list(occ[t + 1])] = False
            T = np.zeros((M, M))
            T[diag, diag] = bleib
            bp, bq = self.G.bond_arrays[k]
            ok = frei0[bp] & frei0[bq]
            bp, bq = bp[ok], bq[ok]
            T[bp, bq] = lam
            T[bq, bp] = lam
            r.append((T, bp, bq))
        P = np.eye(M)
        for T, _, _ in r:
            P = P @ T
        r = (r, P)
        self._Tc[key] = r
        return r

    def zwei(self, Ts, L):
        """Zwei markierte Teilchen, gestapelt: L[c, p1, p2] → Endschicht (harte Kerne untereinander)."""
        ar = np.arange(self.M)
        for T, bp, bq in Ts:
            Ln = np.matmul(np.matmul(T.T, L), T)
            if len(bp):
                f = T[bp, bq] * T[bq, bp]
                Ln[:, bq, bp] -= L[:, bp, bq] * f
                Ln[:, bp, bq] -= L[:, bq, bp] * f
            Ln[:, ar, ar] = 0.0
            L = Ln
        return L

    def phi_mat(self, gkey, k):
        """Aufweg-Rückwärtsfaktor als Matrix Φ[S0, Yo] (alle Löcher unten auf einmal)."""
        key = (gkey, k)
        r = self._phim.get(key)
        if r is not None:
            return r
        G, M = self.G, self.M
        st = list(gkey)
        h4 = self.h4(k)
        _, P = self.T_liste(self.belegung(st), h4)
        z = G.zelle_von
        normz = {}
        spalte = np.empty(M)
        for Yo in range(M):
            c = z[Yo]
            if c not in normz:
                normz[c] = sum(self.pi_auf[d] for d in self.ausf_auf(st, None, c))
            spalte[Yo] = normz[c]
        PHI = self.pi_auf[(0, 0)] * P / spalte[None, :]
        for j1 in st:
            Y0 = j1[-1]
            a0 = z[Y0]
            ds = [d for d in self.pi_auf if d != (0, 0) and (self.locker or z[j1[0]] == G.zellschritt(a0, d))]
            if not ds:
                continue
            andere = [b for b in st if b != j1]
            Tsa, Pa = self.T_liste(self.belegung(andere), h4)
            Zbr = Pa[j1[0], Y0]
            if Zbr <= 0:
                continue
            kan = np.array([s_ for s_ in range(M) if s_ != j1[0]])
            L = np.zeros((len(kan), M, M))
            L[np.arange(len(kan)), kan, j1[0]] = 1.0
            L = self.zwei(Tsa, L)
            for d in ds:
                c1 = G.zellschritt(a0, d)
                for Yo in G.plaetze_in[c1]:
                    col = L[:, Y0, Yo]
                    if not col.any():
                        continue
                    vor = andere + [(j1[0], Yo)]
                    norm = sum(self.pi_auf[dd] for dd in self.ausf_auf(vor, None, a0))
                    g = sum(1 for b in vor if self.wb(b, c1))
                    PHI[kan, Yo] += self.pi_auf[d] / norm / g / Zbr * col
        PHI[[b[0] for b in st], :] = 0.0
        self._phim[key] = PHI
        return PHI

    def h4(self, k):
        return (self.S * k) % 4

    # ---------------------------------------------------------- Hilfen (Stücke: Tupel der Orte, t = 0..S)
    def wb(self, b, c):
        z = self.G.zelle_von
        return z[b[-1]] == c and (self.locker or z[b[0]] == c)

    def belegung(self, st):
        return tuple(frozenset(b[t] for b in st) for t in range(self.S + 1))

    def stuecke(self, pfad, n):
        return [tuple(pfad[t][l] for t in range(self.S + 1)) for l in range(n)]

    def frei_ball(self, starts, Y):
        return [p for p in self.ball[Y] if p not in starts]

    def frei_in(self, starts, c=None):
        if c is None:
            return [p for p in range(self.M) if p not in starts]
        return [p for p in self.G.plaetze_in[c] if p not in starts]

    # ---------------------------------------------------------- DP markierter Teilchen
    def _opts(self, pos, o0, o1, k):
        partner = self.G.partner[k]
        optionen = []
        for p in pos:
            o = []
            if p not in o1:
                o.append((p, 0))
            q = partner.get(p)
            if q is not None and q not in o0 and q not in pos and q not in o1:
                o.append((q, 1))
            if not o:
                return []
            optionen.append(o)
        if len(pos) == 1:
            return [((c[0],), c[1]) for c in optionen[0]]
        erg = []
        for combo in itertools.product(*optionen):
            nach = tuple(c[0] for c in combo)
            if len(set(nach)) < len(nach):
                continue
            erg.append((nach, sum(c[1] for c in combo)))
        return erg

    def _schichten(self, init, occ, h4):
        lp = self.lp
        lay = defaultdict(float)
        for s, wg in init:
            if len(set(s)) == len(s) and not any(p in occ[0] for p in s):
                lay[s] += wg
        schichten = [lay]
        for t in range(self.S):
            k = (h4 + t) % 4
            neu = defaultdict(float)
            o0, o1 = occ[t], occ[t + 1]
            for s, wg in schichten[-1].items():
                for nach, j in self._opts(s, o0, o1, k):
                    neu[nach] += wg * lp[j]
            schichten.append(neu)
        return schichten

    def lage(self, init, occ, h4):
        """Endschicht der Vorwärts-DP; init = Tupel (Zustand, Gewicht)."""
        key = (init, occ, h4)
        r = self._lage.get(key)
        if r is None:
            r = dict(self._schichten(init, occ, h4)[-1])
            self._lage[key] = r
        return r

    def Z(self, starts, enden, occ, h4):
        return self.lage(((tuple(starts), 1.0),), occ, h4).get(tuple(enden), 0.0)

    def _vorg(self, s1, layer, o0, o1, k):
        partner = self.G.partner[k]
        kand = []
        for p in s1:
            q = partner.get(p)
            kand.append((p,) if q is None else (p, q))
        erg = []
        for s0 in itertools.product(*kand):
            if s0 not in layer:
                continue
            for nach, j in self._opts(s0, o0, o1, k):
                if nach == s1:
                    erg.append((s0, j))
        return erg

    def ziehe_pfad(self, init, ende, occ, h4, rng):
        sch = self._schichten(init, occ, h4)
        if sch[-1].get(ende, 0.0) <= 0:
            return None
        pfad = [ende]
        s1 = ende
        for t in range(self.S, 0, -1):
            k = (h4 + t - 1) % 4
            vg = self._vorg(s1, sch[t - 1], occ[t - 1], occ[t], k)
            g = np.array([sch[t - 1][s0] * self.lp[j] for s0, j in vg])
            s1 = vg[int(rng.choice(len(vg), p=g / g.sum()))][0]
            pfad.append(s1)
        return pfad[::-1]

    def pfade(self, starts, ende, occ, h4):
        sch = self._schichten(((tuple(starts), 1.0),), occ, h4)
        if sch[-1].get(ende, 0.0) <= 0:
            return []
        erg = []

        def rueck(t, s1, suffix, kk):
            if t == 0:
                erg.append(([s1] + suffix, kk))
                return
            k = (h4 + t - 1) % 4
            for s0, j in self._vorg(s1, sch[t - 1], occ[t - 1], occ[t], k):
                rueck(t - 1, s0, [s1] + suffix, kk + j)
        rueck(self.S, ende, [], 0)
        return erg

    # ---------------------------------------------------------- Ausführbarkeit (nur Endpunkte)
    def ausf_auf(self, st, j0, a0):
        erg = []
        for d in self.pi_auf:
            if d == (0, 0):
                erg.append(d)
                continue
            c1 = self.G.zellschritt(a0, d)
            if any(self.wb(b, c1) for b in st if b != j0):
                erg.append(d)
        return erg

    def ausf_ab(self, st, kopf):
        G = self.G
        starts = {b[0] for b in st}
        e0 = G.zelle(kopf)
        erg = []
        for d in self.pi_ab:
            if d == (0, 0):
                if self.abweg in ('festzelle', 'zellgewicht') and not self.frei_in(starts, e0):
                    continue
                erg.append(d)
                continue
            c1 = G.zellschritt(e0, d)
            if not any(self.wb(b, c1) for b in st):
                continue
            if self.abweg in ('festzelle', 'zellgewicht') and not self.frei_in(starts, c1):
                continue
            erg.append(d)
        return erg

    # ---------------------------------------------------------- Vorwärts, zufällig (DP-Ziehen)
    def _zug(self, pi, ausf, rng):
        g = np.array([pi[d] for d in ausf])
        return ausf[int(rng.choice(len(ausf), p=g / g.sum()))]

    def auf_zufall(self, st, start, k, rng):
        G = self.G
        j0 = [b for b in st if b[0] == start]
        if len(j0) != 1:
            self.verworfen['auf: kein j0'] += 1
            return None
        j0 = j0[0]
        a0 = G.zelle(j0[-1])
        d = self._zug(self.pi_auf, self.ausf_auf(st, j0, a0), rng)
        if d == (0, 0):
            return [b for b in st if b != j0], j0[-1]
        c1 = G.zellschritt(a0, d)
        waehl = [b for b in st if b != j0 and self.wb(b, c1)]
        j1 = waehl[int(rng.integers(len(waehl)))]
        andere = [b for b in st if b != j0 and b != j1]
        pfad = self.ziehe_pfad((((j1[0],), 1.0),), (j0[-1],), self.belegung(andere), self.h4(k), rng)
        if pfad is None:
            self.verworfen['auf: Brücke'] += 1
            return None
        return andere + self.stuecke(pfad, 1), j1[-1]

    def ab_zufall(self, st, kopf, k, rng):
        G = self.G
        starts = {b[0] for b in st}
        h4 = self.h4(k)
        if self.abweg == 'zelle':
            frei = self.frei_in(starts, G.zelle(kopf))
            if not frei:
                self.verworfen['ab: Zelle voll'] += 1
                return None
            hn = frei[int(rng.integers(len(frei)))]
            pfad = self.ziehe_pfad((((hn,), 1.0),), (kopf,), self.belegung(st), h4, rng)
            if pfad is None:
                self.verworfen['ab: Weg'] += 1
                return None
            return st + self.stuecke(pfad, 1), hn
        ausf = self.ausf_ab(st, kopf)
        if not ausf:
            self.verworfen['ab: kein Zug ausführbar'] += 1
            return None
        d = self._zug(self.pi_ab, ausf, rng)
        e0 = G.zelle(kopf)
        if d == (0, 0):
            tup, ziel_zelle = (), e0
        else:
            c1 = G.zellschritt(e0, d)
            waehl = [b for b in st if self.wb(b, c1)]
            tup, ziel_zelle = (waehl[int(rng.integers(len(waehl)))],), c1
        andere = [b for b in st if b not in tup]
        occ = self.belegung(andere)
        sj = tuple(b[0] for b in tup)
        enden = ((kopf,) if tup else ()) + ((tup[0][-1] if tup else kopf),)
        if self.abweg == 'festzelle':
            frei = self.frei_in(starts, ziel_zelle)
            sp_ = frei[int(rng.integers(len(frei)))]
            init = ((sj + (sp_,), 1.0),)
        elif self.abweg == 'zellgewicht':
            init = tuple((sj + (s,), 1.0) for s in self.frei_in(starts, ziel_zelle))
        elif self.abweg == 'ball':
            init = tuple((sj + (s,), 1.0) for s in self.frei_ball(starts, enden[-1]))
        else:
            init = tuple((sj + (s,), 1.0) for s in self.frei_in(starts))
        pfad = self.ziehe_pfad(init, enden, occ, h4, rng)
        if pfad is None:
            self.verworfen['ab: Weg (d=0)' if not tup else 'ab: Weg (Querschritt)'] += 1
            return None
        return andere + self.stuecke(pfad, len(sj) + 1), pfad[0][-1]

    # ---------------------------------------------------------- Vorwärts, alle Zweige (unabhängig, beweger)
    def bew(self, starts, enden, occ, k):
        key = (tuple(starts), tuple(enden), occ, k)
        r = self._bew.get(key)
        if r is None:
            r = self.G.beweger(list(starts), list(enden), list(occ), self.h4(k), aufzaehlen=True)
            self._bew[key] = r
        return r

    def wegstuecke(self, wg, n):
        return [tuple(wg[t][l] for t in range(self.S + 1)) for l in range(n)]

    def schritt_auf(self, st, start, k):
        G = self.G
        j0 = [b for b in st if b[0] == start]
        if len(j0) != 1:
            return []
        j0 = j0[0]
        a0 = G.zelle(j0[-1])
        ausf = self.ausf_auf(st, j0, a0)
        norm = sum(self.pi_auf[d] for d in ausf)
        erg = []
        for d in ausf:
            pd = self.pi_auf[d] / norm
            if d == (0, 0):
                erg.append((pd, [b for b in st if b != j0], j0[-1]))
                continue
            c1 = G.zellschritt(a0, d)
            waehl = [b for b in st if b != j0 and self.wb(b, c1)]
            for j1 in waehl:
                andere = [b for b in st if b != j0 and b != j1]
                wege = self.bew((j1[0],), (j0[-1],), self.belegung(andere), k)
                Zbr = sum(self.lam ** kk for _, kk in wege)
                for wg, kk in wege:
                    erg.append((pd / len(waehl) * self.lam ** kk / Zbr, andere + self.wegstuecke(wg, 1), j1[-1]))
        return erg

    def schritt_ab(self, st, kopf, k):
        G = self.G
        starts = {b[0] for b in st}
        erg = []
        if self.abweg == 'zelle':
            occ = self.belegung(st)
            frei = self.frei_in(starts, G.zelle(kopf))
            for hn in frei:
                wege = self.bew((hn,), (kopf,), occ, k)
                Zs = sum(self.lam ** kk for _, kk in wege)
                for wg, kk in wege:
                    erg.append((1.0 / len(frei) * self.lam ** kk / Zs, st + self.wegstuecke(wg, 1), hn))
            return erg
        ausf = self.ausf_ab(st, kopf)
        norm = sum(self.pi_ab[d] for d in ausf)
        e0 = G.zelle(kopf)
        for d in ausf:
            pd = self.pi_ab[d] / norm
            if d == (0, 0):
                tupel_liste, ziel_zelle = [()], e0
            else:
                c1 = G.zellschritt(e0, d)
                tupel_liste, ziel_zelle = [(b,) for b in st if self.wb(b, c1)], c1
            for tup in tupel_liste:
                sel = 1.0 / len(tupel_liste) if tup else 1.0
                andere = [b for b in st if b not in tup]
                occ = self.belegung(andere)
                sj = tuple(b[0] for b in tup)
                Ym = tup[0][-1] if tup else kopf
                enden = ((kopf,) if tup else ()) + (Ym,)
                if self.abweg == 'festzelle':
                    frei = self.frei_in(starts, ziel_zelle)
                    for sp_ in frei:
                        wege = self.bew(sj + (sp_,), enden, occ, k)
                        Zs = sum(self.lam ** kk for _, kk in wege)
                        for wg, kk in wege:
                            erg.append((pd * sel / len(frei) * self.lam ** kk / Zs,
                                        andere + self.wegstuecke(wg, len(sj) + 1), sp_))
                else:
                    if self.abweg == 'ball':
                        kandidaten = self.frei_ball(starts, Ym)
                    else:
                        kandidaten = self.frei_in(starts, ziel_zelle if self.abweg == 'zellgewicht' else None)
                    wahl = [(sp_, wg, kk) for sp_ in kandidaten
                            for wg, kk in self.bew(sj + (sp_,), enden, occ, k)]
                    Zs = sum(self.lam ** kk for _, _, kk in wahl)
                    for sp_, wg, kk in wahl:
                        erg.append((pd * sel * self.lam ** kk / Zs, andere + self.wegstuecke(wg, len(sj) + 1), sp_))
        return erg

    # ---------------------------------------------------------- Dichteformel (DP)
    def phi_alle(self, gkey, S0, k):
        """Aufweg-Rückwärtsfaktor der Scheibe k: Lücken-Stücke gkey, Loch unten S0 → {Loch oben Yo: Faktor}."""
        key = (gkey, S0, k)
        r = self._phi.get(key)
        if r is not None:
            return r
        G = self.G
        st = list(gkey)
        h4 = self.h4(k)
        erg = defaultdict(float)
        if S0 not in {b[0] for b in st}:
            # d = 0: j0 = S0 → Yo wieder einsetzen
            lay = self.lage((((S0,), 1.0),), self.belegung(st), h4)
            p0 = self.pi_auf[(0, 0)]
            for (Yo,), z in lay.items():
                ausf = self.ausf_auf(st, None, G.zelle(Yo))
                erg[Yo] += p0 / sum(self.pi_auf[d] for d in ausf) * z
            # d ≠ 0: j1 = überbrücktes Stück (Anfang in c1 = a0 + d, Ende Y0 in a0)
            for j1 in st:
                Y0 = j1[-1]
                a0 = G.zelle(Y0)
                andere = None
                for d in self.pi_auf:
                    if d == (0, 0):
                        continue
                    c1 = G.zellschritt(a0, d)
                    if not self.locker and G.zelle(j1[0]) != c1:
                        continue
                    if andere is None:
                        andere = [b for b in st if b != j1]
                        occa = self.belegung(andere)
                        Zbr = self.Z((j1[0],), (Y0,), occa, h4)
                        lay2 = self.lage((((S0, j1[0]), 1.0),), occa, h4)
                    if Zbr <= 0:
                        continue
                    for (ya, Yo), z in lay2.items():
                        if ya != Y0 or G.zelle(Yo) != c1:
                            continue
                        vor = andere + [(j1[0], Yo)]
                        ausf = self.ausf_auf(vor, None, a0)
                        norm = sum(self.pi_auf[dd] for dd in ausf)
                        g = sum(1 for b in vor if self.wb(b, c1))
                        erg[Yo] += self.pi_auf[d] / norm / g * z / Zbr
        r = dict(erg)
        self._phi[key] = r
        return r

    def ab_daten(self, st, k):
        """Abweg-Rückwärtsdaten der Scheibe k: Liste (Kopf unten, Kopf oben, Faktor, Lücken-Stücke)."""
        G = self.G
        h4 = self.h4(k)
        erg = []
        for neu in st:
            hb, Ym = neu[0], neu[-1]
            rest = [b for b in st if b != neu]
            starts_rest = {b[0] for b in rest}
            occ_rest = self.belegung(rest)
            if self.abweg == 'zelle':
                frei = self.frei_in(starts_rest, G.zelle(Ym))
                if hb in frei:
                    Zs = self.Z((hb,), (Ym,), occ_rest, h4)
                    erg.append((hb, Ym, 1.0 / (len(frei) * Zs), rest))
                continue
            for d in self.pi_ab:
                if d == (0, 0):
                    ausf = self.ausf_ab(rest, Ym)
                    if d not in ausf:
                        continue
                    norm = sum(self.pi_ab[dd] for dd in ausf)
                    if self.abweg == 'festzelle':
                        frei = self.frei_in(starts_rest, G.zelle(Ym))
                        if hb not in frei:
                            continue
                        Zneu = len(frei) * self.Z((hb,), (Ym,), occ_rest, h4)
                    elif self.abweg == 'zellgewicht':
                        if G.zelle(hb) != G.zelle(Ym):
                            continue
                        init = tuple(((s,), 1.0) for s in self.frei_in(starts_rest, G.zelle(Ym)))
                        Zneu = self.lage(init, occ_rest, h4).get((Ym,), 0.0)
                    elif self.abweg == 'ball':
                        if G.abstand(hb, Ym) > self.radius:
                            continue
                        init = tuple(((s,), 1.0) for s in self.frei_ball(starts_rest, Ym))
                        Zneu = self.lage(init, occ_rest, h4).get((Ym,), 0.0)
                    else:
                        init = tuple(((s,), 1.0) for s in self.frei_in(starts_rest))
                        Zneu = self.lage(init, occ_rest, h4).get((Ym,), 0.0)
                    erg.append((hb, Ym, self.pi_ab[d] / norm / Zneu, rest))
                    continue
                c1 = G.zelle(Ym)
                e0 = G.zellschritt_inv(c1, d)
                for j1 in rest:
                    kopf_top = j1[-1]
                    if G.zelle(kopf_top) != e0 or (not self.locker and G.zelle(j1[0]) != c1):
                        continue
                    andere = [b for b in rest if b != j1]
                    vor = andere + [(j1[0], Ym)]
                    ausf = self.ausf_ab(vor, kopf_top)
                    if d not in ausf:
                        continue
                    norm = sum(self.pi_ab[dd] for dd in ausf)
                    g = sum(1 for b in vor if self.wb(b, c1))
                    occ = self.belegung(andere)
                    if self.abweg == 'festzelle':
                        frei = self.frei_in(starts_rest, c1)
                        if hb not in frei:
                            continue
                        Zneu = len(frei) * self.Z((j1[0], hb), (kopf_top, Ym), occ, h4)
                    elif self.abweg == 'zellgewicht':
                        if G.zelle(hb) != c1:
                            continue
                        init = tuple(((j1[0], s), 1.0) for s in self.frei_in(starts_rest, c1))
                        Zneu = self.lage(init, occ, h4).get((kopf_top, Ym), 0.0)
                    elif self.abweg == 'ball':
                        if G.abstand(hb, Ym) > self.radius:
                            continue
                        init = tuple(((j1[0], s), 1.0) for s in self.frei_ball(starts_rest, Ym))
                        Zneu = self.lage(init, occ, h4).get((kopf_top, Ym), 0.0)
                    else:
                        init = tuple(((j1[0], s), 1.0) for s in self.frei_in(starts_rest))
                        Zneu = self.lage(init, occ, h4).get((kopf_top, Ym), 0.0)
                    fak = self.pi_ab[d] / norm / g / Zneu
                    for pfad, kk in self.pfade((j1[0],), (Ym,), occ, h4):
                        erg.append((hb, kopf_top, fak * self.lp[kk], andere + self.stuecke(pfad, 1)))
        return erg

    def f_formel(self, x, y, fenster):
        S, w = self.S, self.w
        stO = [self.G.bahnen(fenster, S * k, S * k + S, S * k) for k in range(w)]
        vec = {(y, x): 1.0}
        for k in range(w):
            dd = defaultdict(list)
            for (hb, ht, a, Gk) in self.ab_daten(stO[k], k):
                dd[hb].append((ht, a, tuple(sorted(Gk))))
            neu = defaultdict(float)
            for (kopf, loch), val in vec.items():
                for (ht, a, gkey) in dd.get(kopf, ()):
                    if self.numpy_phi:
                        zeile = self.phi_mat(gkey, k)[loch]
                        if k == w - 1:
                            v = zeile[ht]
                            if v:
                                neu[(ht, ht)] += val * a * v
                        else:
                            for Yo in np.nonzero(zeile)[0]:
                                neu[(ht, int(Yo))] += val * a * zeile[Yo]
                        continue
                    ph = self.phi_alle(gkey, loch, k)
                    if k == w - 1:
                        v = ph.get(ht, 0.0)
                        if v:
                            neu[(ht, ht)] += val * a * v
                    else:
                        for Yo, v in ph.items():
                            neu[(ht, Yo)] += val * a * v
            vec = neu
        return self.M * sum(vec.values())


# ====================================================================== Hauptprogramm
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--modus', choices=('exakt', 'mc'), default='exakt')
    ap.add_argument('--Lx', type=int, default=4)
    ap.add_argument('--Ly', type=int, default=2)
    ap.add_argument('--cx', type=int, default=2)
    ap.add_argument('--cy', type=int, default=2)
    ap.add_argument('--N', type=int, default=2)
    ap.add_argument('--S', type=int, default=4)
    ap.add_argument('--beta', type=int, default=2, help='Trotter-Zyklen der Periode (je 4 Halbschritte); 0 = Grundzustand')
    ap.add_argument('--w', type=int, default=1)
    ap.add_argument('--lam', type=float, default=0.7)
    ap.add_argument('--abweg', choices=('zelle', 'frei', 'festzelle', 'zellgewicht', 'ball'), default='frei')
    ap.add_argument('--querschritt', action='store_true')
    ap.add_argument('--nie_quer', action='store_true', help='Abweg nur mit Zug d = 0 (keine Route, nur Einfügen)')
    ap.add_argument('--radius', type=int, default=1, help="Abweg ball: Anfang im Torus-Manhattan-Abstand ≤ R von Y_m")
    ap.add_argument('--locker', action='store_true')
    ap.add_argument('--zuege', choices=('nachbar', 'alle'), default='nachbar',
                    help="Züge des Sternpfads: Nachbarzellen oder alle Zellen (Ersatz für Umwege im kleinen Modell)")
    ap.add_argument('--proben', type=int, default=1000)
    ap.add_argument('--zeit', type=float, default=0.0, help='Zeitgrenze in Stunden (0 = keine)')
    ap.add_argument('--zwischen', type=int, default=200, help='Zwischenstand alle so viele Proben')
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--phi_dict', action='store_true', help='Aufweg-Faktor über die Dictionary-DP (Gegenprobe)')
    ap.add_argument('--fdatei', default='', help='f-Werte der angenommenen Proben als .npy sichern (mit Zwischenständen)')
    a = ap.parse_args()
    G = Gitter(a.Lx, a.Ly, a.cx, a.cy, a.zuege)
    S, w, N, lam = a.S, a.w, a.N, a.lam
    T = S * w
    assert S % 4 == 0
    H = 4 * a.beta
    if a.beta > 0:
        assert T <= H
    mod = Schleife(G, N, S, w, lam, a.abweg, a.querschritt, a.locker, radius=a.radius, nie_quer=a.nie_quer)
    mod.numpy_phi = not a.phi_dict
    M = G.M
    rng = np.random.default_rng(a.seed)
    t_start = time.time()

    cs = [frozenset(c) for c in itertools.combinations(range(M), N)]
    idx = {c: i for i, c in enumerate(cs)}
    n = len(cs)

    def transfer(h):
        r, c, v = [], [], []
        for cc in cs:
            for (c1, kk) in G.uebergaenge(cc, h):
                r.append(idx[cc]); c.append(idx[c1]); v.append(lam ** kk)
        return sp.csr_matrix((v, (r, c)), shape=(n, n))

    A = [transfer(h) for h in range(4)]

    def ziehe(gew):
        g = np.asarray(gew, float)
        return int(rng.choice(len(g), p=g / g.sum()))

    if a.beta > 0:
        Ad = [A[h].toarray() for h in range(4)]
        suffix = [None] * (H + 1)
        suffix[H] = np.eye(n)
        for h in range(H - 1, -1, -1):
            suffix[h] = Ad[h % 4] @ suffix[h + 1]
        Pz = suffix[0]
        Rest = suffix[T]                       # Gewicht von Zeit T bis H (≡ 0)
        ZN = float(np.trace(Pz))
        q0 = sum(Pz[idx[(cc - {xx}) | {yy}], idx[cc]]
                 for cc in cs for xx in cc for yy in range(M) if yy == xx or yy not in cc) / (N * M * ZN)

        def ziehe_fenster():
            i0 = ziehe(np.diag(Pz))
            weg = [i0]
            for h in range(H - 1):
                weg.append(ziehe(Ad[h % 4][weg[-1]] * suffix[h + 1][:, i0]))
            return [cs[weg[t % H]] for t in range(T + 1)]
    else:
        def mv(v):
            for h in (3, 2, 1, 0):
                v = A[h] @ v
            return v

        def mvT(v):
            for h in (0, 1, 2, 3):
                v = A[h] @ v
            return v
        _, rvec = eigs(LinearOperator((n, n), matvec=mv, dtype=float), k=1, which='LM', tol=1e-12)
        _, lvec = eigs(LinearOperator((n, n), matvec=mvT, dtype=float), k=1, which='LM', tol=1e-12)
        r0 = np.abs(np.real(rvec[:, 0])); l0 = np.abs(np.real(lvec[:, 0]))
        phase = [None] * 5
        phase[4] = r0
        for h in (3, 2, 1, 0):
            phase[h] = A[h] @ phase[h + 1]
        offen = np.zeros(n)
        for cc in cs:
            s_ = 0.0
            for xx in cc:
                rest_ = cc - {xx}
                for yy in range(M):
                    if yy == xx or yy not in cc:
                        s_ += r0[idx[rest_ | {yy}]]
            offen[idx[cc]] = s_
        q0 = float(l0 @ offen) / (N * M * float(l0 @ r0))

        def ziehe_fenster():
            weg = [cs[ziehe(l0 * r0)]]
            for h in range(T):
                opts = G.uebergaenge(weg[-1], h)
                weg.append(opts[ziehe([lam ** kk * phase[(h % 4) + 1][idx[c1]] for (c1, kk) in opts])][0])
            return weg

    print(f"Gitter {G.Lx}×{G.Ly}, Zellen {G.cx}×{G.cy} ({G.Kx}×{G.Ky}), N={N}, S={S}, w={w}, lam={lam}, "
          f"beta={a.beta}, Abweg={a.abweg}{' R=' + str(a.radius) if a.abweg == 'ball' else ''}{' nie quer' if a.nie_quer else ''}, Querschritt={a.querschritt}, locker={a.locker}, Züge {G.zuege}; "
          f"q0 = |µ| = {q0:.6f}  [Aufbau {time.time() - t_start:.0f} s]", flush=True)

    def ablegen(fenster, stuecke):
        O = list(fenster)
        for kk in range(w):
            for t in range(S + 1):
                O[S * kk + t] = frozenset(b[t] for b in stuecke[kk])
        return tuple(O)

    # ------------------------------------------------------------- Modus exakt
    if a.modus == 'exakt':
        assert a.beta > 0
        fenster_liste = []

        def dfs(weg, kk):
            if len(weg) == T + 1:
                fenster_liste.append((tuple(weg), kk))
                return
            for (c1, m) in G.uebergaenge(weg[-1], len(weg) - 1):
                dfs(weg + [c1], kk + m)
        for cc in cs:
            dfs([cc], 0)
        nu = defaultdict(float)
        for fenster, kh in fenster_liste:
            P = lam ** kh * Rest[idx[fenster[T]], idx[fenster[0]]] / ZN
            if P == 0:
                continue
            st0 = [G.bahnen(list(fenster), S * k, S * k + S, S * k) for k in range(w)]

            def runter(stuecke, kopf, k, p, x):
                if k < 0:
                    nu[(x, kopf, ablegen(fenster, stuecke))] += p
                    return
                for (q, neu_st, hn) in mod.schritt_ab(stuecke[k], kopf, k):
                    s2 = list(stuecke); s2[k] = neu_st
                    runter(s2, hn, k - 1, p * q, x)

            def hoch(stuecke, start, k, p, x):
                if k == w:
                    runter(stuecke, start, w - 1, p, x)
                    return
                for (q, neu_st, loch) in mod.schritt_auf(stuecke[k], start, k):
                    s2 = list(stuecke); s2[k] = neu_st
                    hoch(s2, loch, k + 1, p * q, x)

            for x in sorted(fenster[0]):
                hoch(list(st0), x, 0, P / N, x)

        def mu(O):
            x, y, fen = O
            kk = 0
            for t in range(T):
                m = G.spruenge(fen[t], fen[t + 1], t)
                if m is None:
                    return 0.0
                kk += m
            return lam ** kk * Rest[idx[fen[T]], idx[(fen[0] - {y}) | {x}]] / (N * M * ZN)

        masse = sum(nu.values())
        if masse == 0:
            print(f"  exakt: Fenster {len(fenster_liste)}, kein Zweig erreicht ein O (|ν| = 0)", flush=True)
            return
        zweit = 0.0
        fehler = 0.0
        sfmu = 0.0
        t0 = time.time()
        for O, v in nu.items():
            m_ = mu(O)
            mod.leeren()
            f = mod.f_formel(O[0], O[1], list(O[2]))
            fehler = max(fehler, abs(v - f * m_) / v)
            sfmu += f * m_
            zweit += v * v / m_
        print(f"  exakt: Fenster {len(fenster_liste)}, O mit ν>0: {len(nu)}, |ν| = {masse:.6f} (Σ fµ = {sfmu:.6f}), "
              f"∫f² = {zweit:.6g}, Ausbeute = {masse ** 2 / zweit:.6f} = {masse ** 2 / zweit / q0:.4f}·q0;  "
              f"größter relativer Fehler |ν − fµ|/ν = {fehler:.2e}  [{time.time() - t0:.0f} s]", flush=True)
        return

    # ------------------------------------------------------------- Modus mc
    def vorwaerts_zufall(fenster):
        st = [G.bahnen(fenster, S * k, S * k + S, S * k) for k in range(w)]
        x = sorted(fenster[0])[int(rng.integers(N))]
        start = x
        for k in range(w):
            r = mod.auf_zufall(st[k], start, k, rng)
            if r is None:
                return None
            st[k], start = r
        kopf = start
        for k in range(w - 1, -1, -1):
            r = mod.ab_zufall(st[k], kopf, k, rng)
            if r is None:
                return None
            st[k], kopf = r
        return x, kopf, ablegen(fenster, st)

    fs = []
    angenommen = 0
    t0 = time.time()

    def bericht(proben, schluss=False):
        p = angenommen / proben
        sp_ = np.sqrt(p * (1 - p) / proben)
        if angenommen < 2:
            print(f"  [{proben}] nur {angenommen} angenommen", flush=True)
            return
        f_ = np.array(fs)
        ef = f_.mean()
        sf = f_.std(ddof=1) / np.sqrt(len(f_))
        aus = p / ef
        s_aus = aus * np.sqrt((sp_ / p) ** 2 + (sf / ef) ** 2)
        kopf_ = "  mc:" if schluss else "   ..."
        if a.fdatei:
            np.save(a.fdatei, np.array([proben, angenommen] + list(fs), dtype=float))
        print(f"{kopf_} Proben {proben}, |ν| = {p:.4f} ± {sp_:.4f}, E[f|ang.] = {ef:.4g} ± {sf:.2g}, "
              f"Ausbeute = {aus:.4f} ± {s_aus:.4f} = ({aus / q0:.3f} ± {s_aus / q0:.3f})·q0  "
              f"(max f = {f_.max():.3g}, Median f = {np.median(f_):.3g})  [{time.time() - t0:.0f} s]", flush=True)
        if schluss:
            print("     verworfen: " + ", ".join(f"{k_} {v_}" for k_, v_ in sorted(mod.verworfen.items())), flush=True)

    i = 0
    for i in range(1, a.proben + 1):
        O = vorwaerts_zufall(ziehe_fenster())
        if O is not None:
            angenommen += 1
            mod.leeren()
            fs.append(mod.f_formel(O[0], O[1], list(O[2])))
        if a.zwischen and i % a.zwischen == 0 and i < a.proben:
            bericht(i)
        if a.zeit and time.time() - t0 > 3600 * a.zeit:
            break
    bericht(i, schluss=True)


if __name__ == '__main__':
    main()
