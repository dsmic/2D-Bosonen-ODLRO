#!/usr/bin/env python3
"""Budget-Hebel: weiche Abstandsgewichte und getrennte Zählung Endbereich / Inneres (einpunkt_zeitroute.md §19).

Wie skelett_budget.py (D = 0), aber
  J_weich = sum_t sum_{(c, c')} w(|c - c'|_inf),  w = (1, 0.45, 0.18, 0.08) für Abstand 0..3 (Treffwahrscheinlichkeit
            relativ zu "gleiche Zelle", Bessel-Rechnung l2_treffen.py, Zellseite ~ sqrt(delta)),
  J_innen = nur Zeiten t >= t0 (von beiden Enden aus gezählt; die Hälften sind gespiegelt).
Budget = Schwanzrate alpha_max von P(J >= n), in Einheiten der Kosten eines Paares in derselben Zelle.
--b0: Verstärkung der kürzesten Skala (Querschub je Schritt), gegen klebrige Wiederbegegnungen.
Aufruf: python3 skelett_budget2.py [--b0 1 2 4 8] [--A 4 8 16] [--t0 0 8 32 128] [--beta 0.25] [--w 2048] [--proben 20000]
"""
import argparse
import json
import os
import time

import numpy as np
from numba import njit

from skelett_budget import segment, _seed, kennzahlen

HIER = os.path.dirname(os.path.abspath(__file__))
W = np.array([1.0, 0.45, 0.18, 0.08])


@njit(cache=True)
def pfad(h, beta, b0):
    """Skelett mit verstärkter kürzester Skala: Gewicht b0 statt 1 auf Stufe 0."""
    c = (1.0 - 2.0 ** (-beta)) / 2.0
    v = np.zeros(h)
    lmax = 0
    while (1 << lmax) < h:
        lmax += 1
    for l in range(lmax + 1):
        nb = ((h - 1) >> l) + 1
        U = 2.0 * np.random.random(nb) - 1.0
        gew = c * 2.0 ** (-l * beta) * (b0 if l == 0 else 1.0)
        for i in range(h):
            v[i] += gew * U[i >> l]
    Z = np.zeros(h + 1)
    for i in range(h):
        Z[i + 1] = Z[i] + v[i]
    return Z


@njit(cache=True)
def zaehle(w, beta, A, proben, t0, gew, b0):
    h = w // 2
    Rmax = gew.shape[0] - 1
    Jh = np.zeros(proben)
    Jw = np.zeros(proben)
    s1 = np.zeros((4096, 2), dtype=np.int64)
    s2 = np.zeros((4096, 2), dtype=np.int64)
    for p in range(proben):
        Zx1, Zy1, Zx2, Zy2 = pfad(h, beta, b0), pfad(h, beta, b0), pfad(h, beta, b0), pfad(h, beta, b0)
        th, tw = 0.0, 0.0
        for t in range(t0, h):
            a0x = int(np.round(A * Zx1[t])); a0y = int(np.round(A * Zy1[t]))
            a1x = int(np.round(A * Zx1[t + 1])); a1y = int(np.round(A * Zy1[t + 1]))
            b0x = int(np.round(A * Zx2[t])); b0y = int(np.round(A * Zy2[t]))
            b1x = int(np.round(A * Zx2[t + 1])); b1y = int(np.round(A * Zy2[t + 1]))
            if (max(a0x, a1x) + Rmax < min(b0x, b1x) or max(b0x, b1x) + Rmax < min(a0x, a1x) or
                    max(a0y, a1y) + Rmax < min(b0y, b1y) or max(b0y, b1y) + Rmax < min(a0y, a1y)):
                continue
            n1 = segment(a0x, a0y, a1x, a1y, s1)
            n2 = segment(b0x, b0y, b1x, b1y, s2)
            for i in range(n1):
                for j in range(n2):
                    d = max(abs(s1[i, 0] - s2[j, 0]), abs(s1[i, 1] - s2[j, 1]))
                    if d <= 1:
                        th += 1.0
                    if d <= Rmax:
                        tw += gew[d]
        Jh[p] = 2 * th
        Jw[p] = 2 * tw
    return Jh, Jw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--A', type=float, nargs='+', default=[4, 8, 16])
    ap.add_argument('--t0', type=int, nargs='+', default=[0, 8, 32, 128])
    ap.add_argument('--beta', type=float, default=0.25)
    ap.add_argument('--w', type=int, default=2048)
    ap.add_argument('--proben', type=int, default=20000)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--b0', type=float, nargs='+', default=[1.0])
    ap.add_argument('--aus', default='skelett_budget2.json')
    a = ap.parse_args()
    _seed(a.seed)
    alle = []
    for b0 in a.b0:
     for A in a.A:
        for t0 in a.t0:
            t1 = time.time()
            Jh, Jw = zaehle(a.w, a.beta, A, a.proben, t0, W, b0)
            kh, kw = kennzahlen(Jh), kennzahlen(Jw)
            alle.append(dict(A=A, t0=t0, beta=a.beta, b0=b0, hart=kh, weich=kw))
            print(f"b0={b0:4.1f} A={A:4.0f} t0={t0:4d}: hart E J = {kh['mittel']:7.2f} alpha_max = {kh['alpha_max']:.4f} | "
                  f"weich E J = {kw['mittel']:7.2f} alpha_max = {kw['alpha_max']:.4f}   [{time.time() - t1:.0f} s]", flush=True)
    with open(os.path.join(HIER, 'ergebnisse', a.aus), 'w') as fh:
        json.dump(alle, fh, indent=1)


if __name__ == '__main__':
    main()
