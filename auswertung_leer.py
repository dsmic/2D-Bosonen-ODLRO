#!/usr/bin/env python3
"""Lochkosten aus den Leer-Wahrscheinlichkeiten (scan_leer.py): -ln P(tau) = c0 + DeltaE * tau im Schwanz.
Mittelt die Summen S(tau) über Seeds gleicher Dichte; Fit über tau mit P in [P_min, P_max] und tau >= tau_min.
Aufruf: python3 auswertung_leer.py [--pmin 1e-7] [--pmax 1e-2] [--taumin 2]
"""
import argparse
import glob
import json
import os
from collections import defaultdict

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pmin', type=float, default=1e-7)
    ap.add_argument('--pmax', type=float, default=1e-2)
    ap.add_argument('--taumin', type=float, default=2.0)
    a = ap.parse_args()
    summe = defaultdict(lambda: None)
    info = {}
    for f in sorted(glob.glob(os.path.join(HIER, 'ergebnisse', 'leer_L*_s*.json'))):
        d = json.load(open(f))
        for h, b in d['bloecke'].items():
            key = (d['L'], d['rho_ziel'], int(h))
            S = np.array(b['S']); A = b['anzahl']; n = b['n_mittel'] * A
            if summe[key] is None:
                summe[key] = [S.copy(), A, n]
            else:
                summe[key][0] += S; summe[key][1] += A; summe[key][2] += n
            info[key] = (d['taus'], d['beta'])
    erg = []
    for key in sorted(summe):
        S, A, n = summe[key]
        taus, beta = info[key]
        taus = np.array(taus)
        P = S / (beta * A)
        m = (P > a.pmin) & (P < a.pmax) & (taus >= a.taumin)
        if m.sum() >= 3:
            dE, c0 = np.polyfit(taus[m], -np.log(P[m]), 1)
        else:
            dE, c0 = float('nan'), float('nan')
        L, rho, h = key
        e = dict(L=L, rho=rho, h=h, m=float(n / A), P0=float(P[0]), dE=float(dE), c0=float(c0), punkte=int(m.sum()),
                 tau_max=float(taus[m].max()) if m.any() else None)
        erg.append(e)
        print(f"L={L} rho={rho:.4f} h={h}: <n_Q> = {e['m']:.3f}, P(leer) = {e['P0']:.4f}, "
              f"Delta E = {dE:.4f} (c0 = {c0:.2f}, {e['punkte']} Punkte bis tau = {e['tau_max']})   "
              f"Delta E / (rho h^2) = {dE / (rho * h * h):.3f}", flush=True)
    with open(os.path.join(HIER, 'ergebnisse', 'auswertung_leer.json'), 'w') as fh:
        json.dump(erg, fh, indent=1)


if __name__ == '__main__':
    main()
