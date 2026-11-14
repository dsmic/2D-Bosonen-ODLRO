#!/usr/bin/env python3
"""Prüfung von hist_tau (wurm_nb4.py) gegen die exakte kanonische Lücken-Green-Funktion bei k = 0.

G(tau) = Tr[exp(-(beta-tau) H_N) b_0^+ exp(-tau H_{N-1}) b_0] / Z_N,  b_0 = M^(-1/2) sum_x b_x.
Wurm (kanonisch, N fest): hist_tau(tau) ~ exp(-mu tau) G(tau). Verglichen werden die normierten Formen des
Bin-Integrals von exp(-mu tau) G(tau) in 16 Bins, Fehler aus Blöcken; außerdem der Prüfzähler der Teilchenzahl-Abkürzung (muss 0 sein).
Aufruf: python3 pruef_gtau.py [--L 4] [--N 4] [--beta 4] [--mu -2.5] [--minuten 3]
"""
import argparse
import itertools
import os
import sys
import time

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, 'z2', 'weltlinien'))
import wurm_nb4 as wn  # noqa: E402
from gitter_bosonen import quadratgitter  # noqa: E402


def exakt(L, N, beta, taus):
    M = L * L
    nb = [[((s % L + dx) % L) + L * ((s // L + dy) % L) for dx, dy in ((1, 0), (0, 1))] for s in range(M)]
    kanten = [(s, t) for s in range(M) for t in nb[s]]

    def sektor(n):
        konf = [sum(1 << i for i in c) for c in itertools.combinations(range(M), n)]
        idx = {c: i for i, c in enumerate(konf)}
        H = np.zeros((len(konf), len(konf)))
        for i, c in enumerate(konf):
            for s, t in kanten:
                if (c >> s & 1) != (c >> t & 1):
                    H[i, idx[c ^ (1 << s) ^ (1 << t)]] -= 1.0
        return konf, idx, H
    kN, iN, HN = sektor(N)
    km, im, Hm = sektor(N - 1)
    B = np.zeros((len(km), len(kN)))
    for i, c in enumerate(kN):
        for x in range(M):
            if c >> x & 1:
                B[im[c ^ (1 << x)], i] += 1.0 / np.sqrt(M)
    EN, VN = np.linalg.eigh(HN)
    Em, Vm = np.linalg.eigh(Hm)
    W = np.abs(Vm.T @ B @ VN) ** 2                     # |<b|b_0|a>|^2
    e0 = min(EN.min(), Em.min())
    ZN = np.exp(-beta * (EN - e0)).sum()
    G = np.array([np.exp(-tau * (Em - e0))[:, None] * W * np.exp(-(beta - tau) * (EN - e0))[None, :]
                  for tau in taus]).sum(axis=(1, 2)) / ZN
    return G, EN.min(), Em.min()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--L', type=int, default=4)
    ap.add_argument('--N', type=int, default=4)
    ap.add_argument('--beta', type=float, default=4.0)
    ap.add_argument('--mu', type=float, default=None)
    ap.add_argument('--minuten', type=float, default=3.0)
    ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    L, N, beta = a.L, a.N, a.beta
    nbin = 16
    fein = (np.arange(nbin * 32) + 0.5) * beta / (nbin * 32)
    Gf, E0N, E0m = exakt(L, N, beta, fein)
    mu = a.mu if a.mu is not None else E0N - E0m
    H_ex = (np.exp(-mu * fein) * Gf).reshape(nbin, 32).mean(axis=1)      # erwartetes Bin-Integral
    g = quadratgitter(L)
    s = wn.neu(g, N, beta, mu=mu, kanonisch=True, seed=a.seed)
    s['p'] = np.array([x * 0.95 for x in (0.25, 0.2, 0.2, 0.1, 0.1, 0.15)] + [0.05])
    wn.seed_rng(a.seed)
    M = g['M']
    wn.lauf(s, int(2000 * M * beta), 5)
    t0 = time.time()
    pruef = 0.0
    bloecke = []
    while time.time() - t0 < 60 * a.minuten:
        s['hist_tau'][:] = 0
        acc = wn.lauf(s, int(5000 * M * beta), 5)
        pruef += acc[8]
        bloecke.append(s['hist_tau'].reshape(nbin, -1).sum(axis=1).copy())
    B = np.array(bloecke)
    h = B.sum(axis=0)
    form = B / B.sum(axis=1, keepdims=True)                 # Form je Block
    f_w, f_e = h / h.sum(), H_ex / H_ex.sum()
    err = form.std(axis=0, ddof=1) / np.sqrt(len(B))
    print(f"L={L} N={N} beta={beta} mu={mu:.4f} (E0(N)-E0(N-1) = {E0N - E0m:.4f}); {len(B)} Blöcke, "
          f"Zählungen {h.sum():.0f}, Prüfzähler (muss 0 sein) = {pruef:.0f}")
    print(" tau     Wurm-Form   exakt      rel. Abw.   (W-e)/Blockfehler")
    for i in range(nbin):
        mitte = (i + 0.5) * beta / nbin
        print(f"{mitte:5.2f}  {f_w[i]:.6f}  {f_e[i]:.6f}  {f_w[i] / f_e[i] - 1:+.5f}   {(f_w[i] - f_e[i]) / err[i]:+6.2f}")
    chi2 = np.sum(((f_w - f_e) / err) ** 2)
    print(f"chi^2 = {chi2:.1f} bei {nbin - 1} Freiheitsgraden")


if __name__ == '__main__':
    main()
