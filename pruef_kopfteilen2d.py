#!/usr/bin/env python3
"""Geteilte Kopfscheiben im zweiten Moment, Testmodell auf dem 2D-Torus (Anhang M, M.9.5, Restsatz M14).

Monte Carlo wie zeitschleife2d.py --modus mc (C im Grundzustand per Doob, Konstruktion zufällig, f exakt).
Zusätzlich wird ∫f² dµ = ∫ f dν nach der Länge K der gemeinsamen Kopfkette zerlegt:

  H′ = (h′_0 = y, h′_1, …, h′_w)   Kopflagen der bauenden Route R′ zu den Zeiten t_0, …, t_w (t_w = Wende),
  f(O) = Σ_H f_H(O)                 Dichteformel, nach den verdeckten Kopflagen H der auswertenden Route R zerlegt,
  K(H, H′) = Zahl der übereinstimmenden Kopflagen von unten (K ≥ 1, weil h_0 = h′_0 = y).

K = 1: nur das unterste neue Stück ist geteilt (Übergabe uebergabe_m14_kopf.md: k = 0); allgemein K = k + 1.
Geschätzt wird A(K) = |ν| · E[f_K(O) | angenommen] mit f_K = Σ_{H: K(H,H′(O)) = K} f_H(O); Σ_K A(K) = ∫f² dµ.
Ebenso für den Schwanz: L′ = (x, h′_1, …, h′_w) Lochplätze von R′ (h′_w = Wende), L die verdeckten Lochplätze von R,
K_T(L, L′) = Zahl der übereinstimmenden Lochplätze von unten (K_T ≥ 1, weil h_0 = h′_0 = x). Ausgegeben werden
die Verteilung von K, die von K_T und die gemeinsame Tabelle.
Die Zerlegung wird für die ersten Proben gegen zeitschleife2d.f_formel geprüft.

Aufruf (System m = 1 des Nachtlaufs, Variante c mit Pflicht-Querschritt):
  python3 pruef_kopfteilen2d.py --Lx 6 --Ly 4 --N 6 --cx 2 --cy 2 --S 8 --w 3 --abweg ball --radius 3 \
      --querschritt --locker --zuege alle --proben 100000 --zeit 0.3
"""
import argparse
import itertools
import time
from collections import defaultdict

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import LinearOperator, eigs

from zeitschleife2d import Gitter, Schleife


class SchleifeK(Schleife):
    def f_zerlegt(self, x, y, fenster, Hs, Ls):
        """f(O) nach (K, K_T) zerlegt; Hs = Kopflagen, Ls = Lochplätze von R′ zu t_0 … t_w."""
        S, w = self.S, self.w
        stO = [self.G.bahnen(fenster, S * k, S * k + S, S * k) for k in range(w)]
        assert Hs[0] == y and Ls[0] == x
        vec = {(y, x, 1, True, 1, True): 1.0}
        for k in range(w):
            dd = defaultdict(list)
            for (hb, ht, a, Gk) in self.ab_daten(stO[k], k):
                dd[hb].append((ht, a, tuple(sorted(Gk))))
            neu = defaultdict(float)
            for (kopf, loch, K, ok, KT, okT), val in vec.items():
                for (ht, a, gkey) in dd.get(kopf, ()):
                    if ok and ht == Hs[k + 1]:
                        K2, ok2 = K + 1, True
                    else:
                        K2, ok2 = K, False
                    zeile = self.phi_mat(gkey, k)[loch]
                    for Yo in ([ht] if k == w - 1 else np.nonzero(zeile)[0]):
                        v = zeile[Yo]
                        if not v:
                            continue
                        Yo = int(Yo)
                        if okT and Yo == Ls[k + 1]:
                            KT2, okT2 = KT + 1, True
                        else:
                            KT2, okT2 = KT, False
                        neu[(ht, Yo, K2, ok2, KT2, okT2)] += val * a * v
            vec = neu
        erg = defaultdict(float)
        for (_, _, K, _, KT, _), v in vec.items():
            erg[(K, KT)] += self.M * v
        return erg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Lx', type=int, default=6)
    ap.add_argument('--Ly', type=int, default=4)
    ap.add_argument('--cx', type=int, default=2)
    ap.add_argument('--cy', type=int, default=2)
    ap.add_argument('--N', type=int, default=6)
    ap.add_argument('--S', type=int, default=8)
    ap.add_argument('--w', type=int, default=2)
    ap.add_argument('--lam', type=float, default=0.7)
    ap.add_argument('--abweg', choices=('zelle', 'frei', 'festzelle', 'zellgewicht', 'ball'), default='ball')
    ap.add_argument('--querschritt', action='store_true')
    ap.add_argument('--radius', type=int, default=3)
    ap.add_argument('--locker', action='store_true')
    ap.add_argument('--zuege', choices=('nachbar', 'alle'), default='alle')
    ap.add_argument('--proben', type=int, default=10000)
    ap.add_argument('--zeit', type=float, default=0.0, help='Zeitgrenze in Stunden (0 = keine)')
    ap.add_argument('--zwischen', type=int, default=2000)
    ap.add_argument('--pruefen', type=int, default=30, help='so viele Proben gegen f_formel prüfen')
    ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    G = Gitter(a.Lx, a.Ly, a.cx, a.cy, a.zuege)
    S, w, N, lam = a.S, a.w, a.N, a.lam
    T = S * w
    mod = SchleifeK(G, N, S, w, lam, a.abweg, a.querschritt, a.locker, radius=a.radius)
    mod.numpy_phi = True
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

    def ziehe_fenster():
        weg = [cs[ziehe(l0 * r0)]]
        for h in range(T):
            opts = G.uebergaenge(weg[-1], h)
            weg.append(opts[ziehe([lam ** kk * phase[(h % 4) + 1][idx[c1]] for (c1, kk) in opts])][0])
        return weg

    def ablegen(fenster, stuecke):
        O = list(fenster)
        for kk in range(w):
            for t in range(S + 1):
                O[S * kk + t] = frozenset(b[t] for b in stuecke[kk])
        return tuple(O)

    def vorwaerts_zufall(fenster):
        st = [G.bahnen(fenster, S * k, S * k + S, S * k) for k in range(w)]
        x = sorted(fenster[0])[int(rng.integers(N))]
        start = x
        Ls = [x]
        for k in range(w):
            r = mod.auf_zufall(st[k], start, k, rng)
            if r is None:
                return None
            st[k], start = r
            Ls.append(start)
        Hs = [None] * (w + 1)
        Hs[w] = start
        kopf = start
        for k in range(w - 1, -1, -1):
            r = mod.ab_zufall(st[k], kopf, k, rng)
            if r is None:
                return None
            st[k], kopf = r
            Hs[k] = kopf
        return x, kopf, ablegen(fenster, st), tuple(Hs), tuple(Ls)

    print(f"Gitter {G.Lx}×{G.Ly}, Zellen {G.cx}×{G.cy} ({G.Kx}×{G.Ky}), N={N} (m = {N * G.cx * G.cy / M:.2f} je Zelle), "
          f"S={S}, w={w}, lam={lam}, Abweg={a.abweg}{' R=' + str(a.radius) if a.abweg == 'ball' else ''}, "
          f"Querschritt={a.querschritt}, locker={a.locker}, Züge {G.zuege}  [Aufbau {time.time() - t_start:.0f} s]",
          flush=True)

    summen = defaultdict(list)
    summenT = defaultdict(list)
    gemeinsam = defaultdict(float)
    angenommen = 0
    t0 = time.time()
    maxfehler = 0.0

    def bericht(proben, schluss=False):
        if angenommen < 2:
            print(f"  [{proben}] nur {angenommen} angenommen", flush=True)
            return
        p = angenommen / proben
        Ks = sorted(summen)
        werte = {K: np.array(summen[K]) for K in Ks}
        ges = sum(werte.values())
        ef = ges.mean()
        s_ef = ges.std(ddof=1) / np.sqrt(len(ges))
        kopf_ = "  mc:" if schluss else "   .."
        print(f"{kopf_} Proben {proben}, angenommen {angenommen}, |ν| = {p:.4f}, ∫f² = |ν|·E[f] = {p * ef:.4g} "
              f"(E[f|ang.] = {ef:.4g} ± {s_ef:.2g}), Prüffehler Σ_K f_K gegen f = {maxfehler:.1e}  "
              f"[{time.time() - t0:.0f} s]", flush=True)
        rest = ef
        for K in Ks:
            mK = werte[K].mean()
            sK = werte[K].std(ddof=1) / np.sqrt(len(werte[K]))
            fort = (rest - mK) / rest if rest > 0 else float('nan')
            print(f"       K = {K}: Anteil A(K)/∫f² = {mK / ef:.4f} ± {sK / ef:.4f};  Fortsetzung A(>K)/A(≥K) = {fort:.4f}",
                  flush=True)
            rest -= mK
        wT = {K: np.array(summenT[K]) for K in sorted(summenT)}
        restT = ef
        for K in sorted(wT):
            mK = wT[K].mean()
            sK = wT[K].std(ddof=1) / np.sqrt(len(wT[K]))
            fort = (restT - mK) / restT if restT > 0 else float('nan')
            print(f"       Schwanz K_T = {K}: Anteil = {mK / ef:.5f} ± {sK / ef:.5f};  Fortsetzung = {fort:.5f}", flush=True)
            restT -= mK
        if schluss:
            gs = sum(gemeinsam.values())
            print("       gemeinsam (K, K_T): " + ", ".join(f"({a_},{b_}): {v / gs:.4f}" for (a_, b_), v in sorted(gemeinsam.items())), flush=True)

    i = 0
    for i in range(1, a.proben + 1):
        O = vorwaerts_zufall(ziehe_fenster())
        if O is not None:
            angenommen += 1
            mod.leeren()
            x, y, fen, Hs, Ls = O
            zer = mod.f_zerlegt(x, y, list(fen), Hs, Ls)
            for K in range(1, w + 2):
                summen[K].append(sum(v for (K_, _), v in zer.items() if K_ == K))
                summenT[K].append(sum(v for (_, KT_), v in zer.items() if KT_ == K))
            for kk, v in zer.items():
                gemeinsam[kk] += v
            if angenommen <= a.pruefen:
                mod.leeren()
                f = mod.f_formel(x, y, list(fen))
                maxfehler = max(maxfehler, abs(sum(zer.values()) - f) / f)
        if a.zwischen and i % a.zwischen == 0 and i < a.proben:
            bericht(i)
        if a.zeit and time.time() - t0 > 3600 * a.zeit:
            break
    bericht(i, schluss=True)


if __name__ == '__main__':
    main()
