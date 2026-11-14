#!/usr/bin/env python3
"""Scharfes L2, quenched-lokale Form: hängt ln kappa_q je Umgebung linear von der lokalen Teilchenzahl ab?
Verwendet umgebung/schritt aus l2_doob.py. Je Umgebung: kappa_L (exakt), n_ges (Umgebungsteilchen im Torus 3s x 3s),
n_nah (Umgebungsteilchen, die irgendwann in der 3s/2-Umgebung der Startzelle sind).
Regression ln kappa = a + b n_nah; Vergleich b mit 0,27/(ln s * typische Zahl).
Aufruf: python3 l2_linear.py [--rho 0.0125] [--m 4 8] [--umgebungen 80]
"""
import argparse
import json
import os

import numpy as np

from l2_doob import schritt


def lauf(rng, s, rho, p):
    Lb = 3 * s
    T = int(round(2 * s * s / p))
    n = rng.poisson(rho * Lb * Lb)
    x = rng.integers(Lb, size=n); y = rng.integers(Lb, size=n)
    dx = np.array([1, -1, 0, 0]); dy = np.array([0, 0, 1, -1])
    occ = np.zeros((T + 1, Lb, Lb), dtype=bool)
    nah = np.zeros(n, dtype=bool)
    lo, hi = s - s // 2, 2 * s + s // 2
    for t in range(T + 1):
        if t > 0:
            spr = rng.random(n) < p
            d = rng.integers(4, size=n)
            x = np.where(spr, (x + dx[d]) % Lb, x); y = np.where(spr, (y + dy[d]) % Lb, y)
        occ[t, x, y] = True
        nah |= (x >= lo) & (x < hi) & (y >= lo) & (y < hi)
    while True:
        S = rng.integers(s, size=4) + s
        if (S[0], S[1]) != (S[2], S[3]) and not occ[0, S[0], S[1]] and not occ[0, S[2], S[3]]:
            break
    frei = ~occ
    b = np.empty((T + 1, Lb, Lb)); b[T] = frei[T]
    for t in range(T - 1, -1, -1):
        b[t] = frei[t] * schritt(b[t + 1], p)
    f1 = np.zeros((Lb, Lb)); f1[S[0], S[1]] = 1.0
    f2 = np.zeros((Lb, Lb)); f2[S[2], S[3]] = 1.0
    q1, q2 = f1.copy(), f2.copy()
    Z1, Z2 = b[0, S[0], S[1]], b[0, S[2], S[3]]
    za = ne = 0.0
    for t in range(T + 1):
        if t > 0:
            f1 = frei[t] * schritt(f1, p); f2 = frei[t] * schritt(f2, p)
            q1 = schritt(q1, p); q2 = schritt(q2, p)
        za += np.sum(f1 * b[t] / Z1 * f2 * b[t] / Z2)
        ne += np.sum(q1 * q2)
    return za / ne, n, int(nah.sum()), np.sqrt(Z1 * Z2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--rho', type=float, default=0.0125)
    ap.add_argument('--m', type=float, nargs='+', default=[4, 8])
    ap.add_argument('--umgebungen', type=int, default=80)
    ap.add_argument('--p', type=float, default=0.4)
    a = ap.parse_args()
    rng = np.random.default_rng(7)
    erg = []
    for m in a.m:
        s = int(round(np.sqrt(m / a.rho)))
        daten = np.array([lauf(rng, s, a.rho, a.p) for _ in range(a.umgebungen)])
        k, nges, nnah, Z = daten.T
        lk = np.log(k)
        A = np.vstack([np.ones_like(nnah), nnah]).T
        (c0, c1), *_ = np.linalg.lstsq(A, lk, rcond=None)
        r = np.corrcoef(nnah, lk)[0, 1]
        rz = np.corrcoef(-np.log(Z), lk)[0, 1]
        rest = lk - (c0 + c1 * nnah)
        e = dict(rho=a.rho, m=m, s=s, a=float(c0), b=float(c1), b_mal_lns=float(c1 * np.log(s)), korr_n=float(r),
                 korr_logZ=float(rz), rest_max=float(rest.max()), n_nah_mittel=float(nnah.mean()), lnk_mittel=float(lk.mean()),
                 lnk_max=float(lk.max()))
        mom = {f'E_kappa^{q}': float(np.mean(k ** q)) for q in (1, 2, 3, 4)}
        e.update(mom); e['quantile_lnk'] = [float(v) for v in np.quantile(lk, [0.5, 0.9, 0.99])]
        e['werte'] = [float(v) for v in k]
        erg.append(e)
        print('   Momente: ' + '  '.join(f'E k^{q} = {mom[f"E_kappa^{q}"]:.3f} (ln/q = {np.log(mom[f"E_kappa^{q}"]) / q:.3f})' for q in (1, 2, 3, 4))
              + f'   ln kappa Quantile 50/90/99 %: ' + ' / '.join(f'{v:.3f}' for v in e['quantile_lnk']), flush=True)
        print(f"m={m:g} s={s}: ln kappa = {c0:.3f} + {c1:.4f}·n_nah  (b·ln s = {c1 * np.log(s):.3f}), Korrelation mit n_nah {r:.2f}, "
              f"mit -ln Z {rz:.2f}; <n_nah> = {nnah.mean():.1f}, <ln kappa> = {lk.mean():.3f}, max ln kappa = {lk.max():.3f}, "
              f"max Rest über der Geraden {rest.max():.3f}", flush=True)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ergebnisse', 'l2_linear.json'), 'w') as fh:
        json.dump(erg, fh, indent=1)


if __name__ == '__main__':
    main()
