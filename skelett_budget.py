#!/usr/bin/env python3
"""Budget je Zellpaar für den zeitartigen Staffellauf: Begegnungen der Sternpfade zweier Skelette (zwei Querrichtungen).

Wie skelett_begegnungen.py, aber verallgemeinert und mit dem für die Kosten richtigen Zähler:
  v_i = c(beta) sum_l 2^{-l beta} U_{l, floor((i-1)/2^l)},  c(beta) = (1 - 2^{-beta})/2  (|v| <= 1/2),
  Basispunkt b_t = A * (Z_t + D t)  (A = Querzellen je Zeitscheibe, D = gemeinsame Drift je Schritt, in Einheiten von v),
  Sternpfad Seg(t) = Zellen auf der Strecke b_t -> b_{t+1} (gerundet, je Querrichtung nacheinander wie im Preprint),
  J_A = sum_t #{(c, c') in Seg1(t) x Seg2(t): |c - c'|_inf <= R}   (beide Hälften, gespiegelt wie im Preprint).
Die Kosten einer Begegnung fallen je nahem Zellpaar an; Bedingung des Beweises: log(1 + Kosten je Paar) < alpha_max(J_A).
Aufruf: python3 skelett_budget.py [--beta 0.125 0.25 0.375 0.5] [--A 1 2 4 8 16 32] [--D 0 0.5] [--w 2048] [--proben 20000]
"""
import argparse
import json
import os
import time

import numpy as np
from numba import njit

HIER = os.path.dirname(os.path.abspath(__file__))


@njit(cache=True)
def _seed(s):
    np.random.seed(s)


@njit(cache=True)
def pfad(h, beta):
    c = (1.0 - 2.0 ** (-beta)) / 2.0
    v = np.zeros(h)
    lmax = 0
    while (1 << lmax) < h:
        lmax += 1
    for l in range(lmax + 1):
        nb = ((h - 1) >> l) + 1
        U = 2.0 * np.random.random(nb) - 1.0
        gew = c * 2.0 ** (-l * beta)
        for i in range(h):
            v[i] += gew * U[i >> l]
    Z = np.zeros(h + 1)
    for i in range(h):
        Z[i + 1] = Z[i] + v[i]
    return Z


@njit(cache=True)
def segment(x0, y0, x1, y1, buf):
    """Zellen von (x0, y0) nach (x1, y1): erst x, dann y (wie die Sternpfade im Preprint); Rückgabe Anzahl."""
    n = 0
    sx = 1 if x1 >= x0 else -1
    x = x0
    buf[n, 0] = x
    buf[n, 1] = y0
    n += 1
    while x != x1:
        x += sx
        buf[n, 0] = x
        buf[n, 1] = y0
        n += 1
    sy = 1 if y1 >= y0 else -1
    y = y0
    while y != y1:
        y += sy
        buf[n, 0] = x1
        buf[n, 1] = y
        n += 1
    return n


@njit(cache=True)
def zaehle(w, beta, A, D, R, proben):
    h = w // 2
    J = np.zeros(proben, dtype=np.int64)
    s1 = np.zeros((4096, 2), dtype=np.int64)
    s2 = np.zeros((4096, 2), dtype=np.int64)
    for p in range(proben):
        Zx1, Zy1, Zx2, Zy2 = pfad(h, beta), pfad(h, beta), pfad(h, beta), pfad(h, beta)
        tot = 0
        for t in range(h):
            # Basispunkte (gemeinsame Drift D in beiden Querrichtungen)
            a0x = int(np.round(A * (Zx1[t] + D * t)))
            a0y = int(np.round(A * (Zy1[t] + D * t)))
            a1x = int(np.round(A * (Zx1[t + 1] + D * (t + 1))))
            a1y = int(np.round(A * (Zy1[t + 1] + D * (t + 1))))
            b0x = int(np.round(A * (Zx2[t] + D * t)))
            b0y = int(np.round(A * (Zy2[t] + D * t)))
            b1x = int(np.round(A * (Zx2[t + 1] + D * (t + 1))))
            b1y = int(np.round(A * (Zy2[t + 1] + D * (t + 1))))
            # schneller Ausschluss über die Abstände der Rechtecke
            if (max(a0x, a1x) + R < min(b0x, b1x) or max(b0x, b1x) + R < min(a0x, a1x) or
                    max(a0y, a1y) + R < min(b0y, b1y) or max(b0y, b1y) + R < min(a0y, a1y)):
                continue
            n1 = segment(a0x, a0y, a1x, a1y, s1)
            n2 = segment(b0x, b0y, b1x, b1y, s2)
            for i in range(n1):
                for j in range(n2):
                    if abs(s1[i, 0] - s2[j, 0]) <= R and abs(s1[i, 1] - s2[j, 1]) <= R:
                        tot += 1
        J[p] = 2 * tot
    return J


def kennzahlen(J):
    J = np.asarray(J, dtype=float)
    res = {'mittel': float(J.mean()), 'q99': float(np.quantile(J, 0.99))}
    n1, n2 = np.quantile(J, 0.9), np.quantile(J, 0.999)
    ns = np.linspace(n1, n2, 12)
    P = np.array([(J >= n).mean() for n in ns])
    ok = P > 0
    res['alpha_max'] = float(-np.polyfit(ns[ok], np.log(P[ok]), 1)[0]) if ok.sum() > 3 and n2 > n1 else float('nan')
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--beta', type=float, nargs='+', default=[0.125, 0.25, 0.375, 0.5])
    ap.add_argument('--A', type=float, nargs='+', default=[1, 2, 4, 8, 16, 32])
    ap.add_argument('--D', type=float, nargs='+', default=[0.0, 0.5])
    ap.add_argument('--w', type=int, default=2048)
    ap.add_argument('--proben', type=int, default=20000)
    ap.add_argument('--R', type=int, default=1)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--aus', default='skelett_budget.json')
    a = ap.parse_args()
    _seed(a.seed)
    alle = []
    for D in a.D:
        for beta in a.beta:
            for A in a.A:
                t0 = time.time()
                J = zaehle(a.w, beta, A, D, a.R, a.proben)
                k = kennzahlen(J)
                alle.append(dict(beta=beta, A=A, D=D, w=a.w, R=a.R, proben=a.proben, **k))
                print(f"D={D:4.2f} beta={beta:5.3f} A={A:5.1f}: E J_A = {k['mittel']:8.2f}  q99 {k['q99']:7.0f}  "
                      f"alpha_max = {k['alpha_max']:.4f}   [{time.time() - t0:.0f} s]", flush=True)
    with open(os.path.join(HIER, 'ergebnisse', a.aus), 'w') as fh:
        json.dump(alle, fh, indent=1)


if __name__ == '__main__':
    main()
