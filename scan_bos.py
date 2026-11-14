#!/usr/bin/env python3
"""Wurm (z2/weltlinien/wurm_nb4.py) für harte Bosonen auf dem L x L-Quadratgitter, großkanonisch.

Gemessen je Block (wie scan_nb4.py): Energie, Teilchenzahl, Windungen <W_x^2>, <W_y^2> (rho_s = T <W^2>/2 je Richtung
gemittelt, siehe README), gleichzeitige Korrelation g(r) bei r = 0, (L/2, 0), (L/2, L/2), dazu die vollen
Kopf-Schwanz-Histogramme (gleichzeitig: hist_eq; über die Zeit integriert, omega = 0: hist_all) am Ende als npz.
mu wird auf die Zieldichte rho eingeregelt (Robbins-Monro), oder mit --mu fest gehalten (Prüfung gegen exakt).

Aufruf: python3 scan_bos.py L beta --rho 0.25 [--stunden 1] [--seed 1]
        python3 scan_bos.py 4 4 --mu -2.3 --stunden 0.1        (fester Wert, für pruef_exakt.py)
"""
import argparse
import json
import os
import sys
import time

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, 'z2', 'weltlinien'))
import wurm_nb4 as wn  # noqa: E402
from gitter_bosonen import quadratgitter  # noqa: E402


def gewichtet(arr, nbin=20):
    w = arr['nZ']
    nbin = min(nbin, len(w))
    teile = np.array_split(np.arange(len(w)), nbin)
    mean, err = {}, {}
    for k, x in arr.items():
        if k == 'nZ':
            continue
        mean[k] = float((w * x).sum() / w.sum())
        b = [(w[i] * x[i]).sum() / w[i].sum() for i in teile]
        err[k] = float(np.std(b, ddof=1) / np.sqrt(nbin)) if nbin > 1 else float('nan')
    return mean, err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('L', type=int)
    ap.add_argument('beta', type=float)
    ap.add_argument('--rho', type=float, default=None)
    ap.add_argument('--mu', type=float, default=None)
    ap.add_argument('--stunden', type=float, default=1.0)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--block', type=float, default=2000.0, help='Schritte je Block in Einheiten M*beta')
    ap.add_argument('--tag', type=str, default='')
    a = ap.parse_args()
    L, beta = a.L, a.beta
    if (a.rho is None) == (a.mu is None):
        sys.exit('genau eines von --rho oder --mu angeben')
    g = quadratgitter(L)
    M = g['M']
    rho = a.rho if a.rho is not None else 0.25
    P = max(1, int(round(rho * M)))
    mu0 = a.mu if a.mu is not None else -4.0 + 8.0 * rho     # grobe Startschätzung, wird nachgeregelt
    s = wn.neu(g, P, beta, mu=mu0, kanonisch=False, seed=a.seed)
    s['p'] = np.array([x * 0.95 for x in (0.25, 0.2, 0.2, 0.1, 0.1, 0.15)] + [0.05])
    wn.seed_rng(a.seed)
    n_cls = s['n_cls']
    name = (f"bos_L{L}_b{beta:g}_" + (f"r{rho:g}" if a.mu is None else f"mu{a.mu:g}") + f"_s{a.seed}{a.tag}")
    out = os.path.join(HIER, 'ergebnisse', name + '.json')
    t0 = time.time()
    rund = int(1000 * M * beta)
    mu_hist = []
    for runde in range(24):
        acc = wn.lauf(s, rund, 5)
        if acc[0] > 0 and runde >= 2 and a.mu is None:
            gain = 1.0 / (1 + (runde - 2) / 3)
            s['fv'][wn.F_MU] += gain * 2.0 * (rho * M - acc[2] / acc[0]) / M
        mu_hist.append((float(s['fv'][wn.F_MU]), float(acc[2] / acc[0]) if acc[0] else None))
    t_therm = time.time() - t0
    block = int(a.block * M * beta)
    blocks = []
    s['hist_eq'][:] = 0
    s['hist_all'][:] = 0
    while time.time() - t0 < a.stunden * 3600:
        acc = wn.lauf(s, block, 5)
        if acc[0] == 0:
            continue
        r = wn.auswerten(s, acc)
        gs = {k: r['g_counts'][i] / r['g_norm'] / n_cls[i] for i, k in enumerate(('g0', 'gx', 'gd'))}
        blocks.append({'nZ': r['nZ'], 'E': r['E'], 'N': r['N'], 'Wx2': r['Wx2'], 'Wy2': r['Wy2'], **gs})
        arr = {k: np.array([b_[k] for b_ in blocks]) for k in blocks[0]}
        arr['W2'] = (arr['Wx2'] + arr['Wy2']) / 2
        mean, err = gewichtet(arr)
        res = {'L': L, 'M': M, 'beta': beta, 'T': 1 / beta, 'rho_ziel': a.rho, 'mu': float(s['fv'][wn.F_MU]),
               'mu_fest': a.mu is not None, 'seed': a.seed, 'mu_hist': mu_hist, 'blocks': len(blocks),
               'time_s': time.time() - t0, 't_therm_s': t_therm, 'mean': mean, 'err': err,
               'rho': mean['N'] / M, 'reihe': {k: arr[k].tolist() for k in ('nZ', 'E', 'N', 'W2', 'g0', 'gx', 'gd')}}
        with open(out, 'w') as fh:
            json.dump(res, fh)
        np.savez(out.replace('.json', '.npz'), hist_eq=s['hist_eq'], hist_all=s['hist_all'])
    print(f"{name}: {len(blocks)} Blöcke, rho = {res['rho']:.4f}, mu = {res['mu']:.4f}, E/M = {mean['E'] / M:.5f}, "
          f"g0 = {mean['g0']:.4f}, g(L/2,0)/g0 = {mean['gx'] / mean['g0']:.4f}, <W^2> = {mean['W2']:.4f}  "
          f"[{time.time() - t0:.0f} s]")


if __name__ == '__main__':
    main()
