#!/usr/bin/env python3
"""Begegnungen zweier unabhängiger Zufallsrouten (Skelette) mit gleichen Endpunkten: Dimensionszählung numerisch.

Skelett wie in OpenAI, "A density-uniform condensate bound for dilute Bose gases", §8.1 (nach Benjamini-Pemantle-
Peres und Häggström-Mossel): erste Koordinate (bei uns die imaginäre Zeit) läuft 0..w, in jeder Querrichtung
    Z_t = sum_{i<=t} v_i,   v_i = c_vel sum_l 2^{-l/4} U_{l, floor((i-1)/2^l)},   U ~ gleichverteilt [-1, 1],
gelesen bis zur Mitte und gespiegelt zurück (verschwindet an beiden Enden); die lineare Drift zwischen den
Endpunkten ist beiden Routen gemeinsam und fällt aus der Differenz heraus. Variante "diffusiv": nur l = 0 mit
v_i = U_i / 2 (Schwankung ~ t^{1/2}). Begegnungen (wie J0 dort, ohne die Zwischenecken):
    J = 2 * #{ t <= w/2 : max_q |round(Z_t^q) - round(Z'_t^q)| <= R }.
Gemessen: Mittelwert von J, Schwanzrate alpha_max aus P(J >= n) ~ exp(-alpha_max n), E exp(alpha J).
Erwartung: q = 2 dyadisch beschränkt (Satz 8.1 dort), q = 2 diffusiv ~ log w (marginal), q = 1 dyadisch ~ w^{1/4},
q = 1 diffusiv ~ w^{1/2}. Für den Staffellauf: Kosten G je Begegnung sind tragbar, solange log G < alpha_max.
--skala A: Querschritte mal A (Raumzellen je Zeitschritt; bei uns frei wählbar, im Preprint |v| <= 1/2).
Aufruf: python3 skelett_begegnungen.py [--w 64 256 1024 4096 16384] [--proben 20000] [--R 1] [--skala 1] [--nur q2dy]
"""
import argparse
import json
import os
import time

import numpy as np
from numba import njit

HIER = os.path.dirname(os.path.abspath(__file__))
C_VEL = (1 - 2 ** -0.25) / 2


@njit(cache=True)
def _seed(s):
    np.random.seed(s)


@njit(cache=True)
def pfad(h, dyadisch, skala):
    """Z_0..Z_h einer Querrichtung."""
    v = np.zeros(h)
    if dyadisch:
        lmax = 0
        while (1 << lmax) < h:
            lmax += 1
        for l in range(lmax + 1):
            nb = ((h - 1) >> l) + 1
            U = 2.0 * np.random.random(nb) - 1.0
            gew = C_VEL * 2.0 ** (-l / 4.0)
            for i in range(h):
                v[i] += gew * U[i >> l]
    else:
        for i in range(h):
            v[i] = (2.0 * np.random.random() - 1.0) / 2.0
    Z = np.zeros(h + 1)
    for i in range(h):
        Z[i + 1] = Z[i] + skala * v[i]
    return Z


@njit(cache=True)
def begegnungen(w, q, dyadisch, R, proben, skala):
    h = w // 2
    J = np.zeros(proben, dtype=np.int64)
    for p in range(proben):
        nah = np.ones(h + 1, dtype=np.bool_)
        for c in range(q):
            Z1 = pfad(h, dyadisch, skala)
            Z2 = pfad(h, dyadisch, skala)
            for t in range(h + 1):
                if abs(np.round(Z1[t]) - np.round(Z2[t])) > R:
                    nah[t] = False
        J[p] = 2 * np.sum(nah)
    return J


def kennzahlen(J):
    J = np.asarray(J, dtype=float)
    res = {'mittel': float(J.mean()), 'median': float(np.median(J)), 'q99': float(np.quantile(J, 0.99)),
           'max': float(J.max())}
    # Schwanzrate: Steigung von log P(J >= n) zwischen dem 90 %- und dem 99,9 %-Quantil
    n1, n2 = np.quantile(J, 0.9), np.quantile(J, 0.999)
    ns = np.linspace(n1, n2, 12)
    P = np.array([(J >= n).mean() for n in ns])
    ok = P > 0
    res['alpha_max'] = float(-np.polyfit(ns[ok], np.log(P[ok]), 1)[0]) if ok.sum() > 3 and n2 > n1 else float('nan')
    for a in (0.05, 0.1, 0.2):
        res[f'E_exp_{a}'] = float(np.mean(np.exp(a * J)))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--w', type=int, nargs='+', default=[64, 256, 1024, 4096, 16384])
    ap.add_argument('--proben', type=int, default=20000)
    ap.add_argument('--R', type=int, default=1)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--skala', type=float, default=1.0, help='Querzellen je Zeitschritt (Anisotropie), multipliziert v')
    ap.add_argument('--nur', default='', help='z. B. q2dy: nur diesen Fall')
    a = ap.parse_args()
    _seed(a.seed)
    alle = []
    for q in (2, 1):
        for dy in (True, False):
            name = f"q={q} {'dyadisch' if dy else 'diffusiv'}"
            if a.nur and a.nur != f"q{q}{'dy' if dy else 'di'}":
                continue
            for w in a.w:
                t0 = time.time()
                J = begegnungen(w, q, dy, a.R, a.proben, a.skala)
                k = kennzahlen(J)
                alle.append(dict(q=q, dyadisch=dy, w=w, R=a.R, skala=a.skala, proben=a.proben, **k))
                print(f"{name:14s} w = {w:6d}: E J = {k['mittel']:8.2f}  Median {k['median']:6.0f}  q99 {k['q99']:7.0f}  "
                      f"alpha_max = {k['alpha_max']:.3f}  E e^(0.05 J) = {k['E_exp_0.05']:.3g}  "
                      f"E e^(0.1 J) = {k['E_exp_0.1']:.3g}  [{time.time() - t0:.0f} s]", flush=True)
    with open(os.path.join(HIER, 'ergebnisse', f'skelett_begegnungen_R{a.R}_s{a.skala:g}{a.nur}.json'), 'w') as fh:
        json.dump(alle, fh, indent=1)


if __name__ == '__main__':
    main()
