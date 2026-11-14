#!/usr/bin/env python3
"""Lücken-Green-Funktion G(tau) bei k = 0 mit dem kanonischen Wurm (wurm_nb4.py, hist_tau), harte Bosonen L x L.

Ziel: Z0 = lim_tau G(tau) e^{(E0(N-1)-E0(N)) tau} / G(0) und damit H^2 = Z0 N0/N bei großen L
(einpunkt_zeitroute.md; exakt auf 4x4 .. 6x6 ist Z0 ~ 0,999). Der Wurm misst hist_tau ~ exp(-mu tau) G(tau);
mu ist nur Gewicht der Lücke und wird aus dem großkanonischen Lauf gleicher Dichte genommen (Runde 1),
ein Rest-Exponent wird bei der Auswertung angepasst. Je Block: nZ, E, Windungen, g-Klassen und hist_tau grob
(128 Bins); am Ende hist_tau fein (512 Bins) und hist_eq als npz.
Geprüft gegen exakt mit pruef_gtau.py (4x4, N = 4, beta = 4: chi^2 = 18 bei 15 Freiheitsgraden).

Aufruf: python3 scan_gtau.py L beta --rho 0.0625 --mu-von ergebnisse/bos_L32_b64_r0.0625_s1.json [--stunden 12]
"""
import argparse
import json
import os
import sys
import time

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, '..', 'z2', 'weltlinien'))
import wurm_nb4 as wn  # noqa: E402
from gitter_bosonen import quadratgitter  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('L', type=int)
    ap.add_argument('beta', type=float)
    ap.add_argument('--rho', type=float, required=True)
    ap.add_argument('--mu-von', required=True)
    ap.add_argument('--stunden', type=float, default=12.0)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--block', type=float, default=2000.0, help='Schritte je Block in Einheiten M*beta')
    a = ap.parse_args()
    L, beta = a.L, a.beta
    g = quadratgitter(L)
    M = g['M']
    n = int(round(a.rho * M))
    mu = float(json.load(open(a.mu_von))['mu'])
    s = wn.neu(g, n, beta, mu=mu, kanonisch=True, seed=a.seed)
    s['p'] = np.array([x * 0.95 for x in (0.25, 0.2, 0.2, 0.1, 0.1, 0.15)] + [0.05])
    wn.seed_rng(a.seed)
    name = f"gtau_L{L}_b{beta:g}_r{a.rho:g}_s{a.seed}"
    out = os.path.join(HIER, 'ergebnisse', name + '.json')
    t0 = time.time()
    for _ in range(12):
        wn.lauf(s, int(1000 * M * beta), 5)
    t_therm = time.time() - t0
    block = int(a.block * M * beta)
    reihe = {k: [] for k in ('nZ', 'E', 'W2', 'g0', 'gx', 'gd')}
    tau_bl = []
    s['hist_eq'][:] = 0
    s['hist_tau'][:] = 0
    vorher = np.zeros_like(s['hist_tau'])
    while time.time() - t0 < a.stunden * 3600:
        acc = wn.lauf(s, block, 5)
        if acc[0] == 0:
            continue
        r = wn.auswerten(s, acc)
        reihe['nZ'].append(r['nZ'])
        reihe['E'].append(r['E'])
        reihe['W2'].append((r['Wx2'] + r['Wy2']) / 2)
        for i, k in enumerate(('g0', 'gx', 'gd')):
            reihe[k].append(r['g_counts'][i] / r['g_norm'] / s['n_cls'][i])
        neu = s['hist_tau'] - vorher
        vorher = s['hist_tau'].copy()
        tau_bl.append(neu.reshape(128, -1).sum(axis=1).tolist())
        res = {'L': L, 'M': M, 'N': n, 'beta': beta, 'rho': n / M, 'mu': mu, 'mu_von': a.mu_von, 'seed': a.seed,
               'blocks': len(tau_bl), 'time_s': time.time() - t0, 't_therm_s': t_therm, 'reihe': reihe,
               'hist_tau_bloecke_128': tau_bl}
        with open(out, 'w') as fh:
            json.dump(res, fh)
        np.savez(out.replace('.json', '.npz'), hist_tau=s['hist_tau'], hist_eq=s['hist_eq'])
    print(f"{name}: {len(tau_bl)} Blöcke, N = {n}, mu = {mu:.5f}  [{time.time() - t0:.0f} s]")


if __name__ == '__main__':
    main()
