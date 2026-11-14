#!/usr/bin/env python3
"""L2: Einfluss der Umgebung auf die Treffwahrscheinlichkeit zweier neu gezogener Stücke (Schätzung von kappa_2).

Torus 3s x 3s (3 x 3 Zellen der Seite s, m = rho s^2 Teilchen je Zelle). Zwei Testteilchen starten gleichverteilt in der
mittleren Zelle, die Umgebung mit Dichte rho (Poisson-Zahl, verschiedene Startplätze) im ganzen Torus. Alle machen
Irrfahrten in stetiger Zeit (Rate 1 je Nachbar), diskretisiert mit dt (Sprungwahrscheinlichkeit 4 dt je Schritt),
Dauer delta = s^2. Treffen = gleicher Platz nach einem Schritt oder Platztausch. Umgebung ist ein freies Gas (Näherung).
Gemessen: P_frei = P(Test 1 trifft Test 2), P_aus = P(beide meiden die Umgebung),
          P_bed = P(Test 1 trifft Test 2 | beide meiden die Umgebung),  kappa_umg = P_bed / P_frei.
Aufruf: python3 l2_kappa.py [--m 10] [--rho 0.2 0.05 0.0125] [--proben 4000] [--dt 0.1]
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
def lauf(s, rho, dt, proben):
    Lb = 3 * s
    M = Lb * Lb
    schritte = int(round(s * s / dt))
    p = 4.0 * dt
    dx = np.array([1, -1, 0, 0])
    dy = np.array([0, 0, 1, -1])
    n_frei = 0
    n_aus = 0
    n_bed = 0
    belegt = np.zeros(M, dtype=np.int64)
    for _ in range(proben):
        nU = np.random.poisson(rho * M)
        # Startplätze: Test 1, Test 2 in der Mittelzelle, Umgebung überall, alle verschieden
        n = nU + 2
        x = np.zeros(n, dtype=np.int64)
        y = np.zeros(n, dtype=np.int64)
        belegt[:] = 0
        k = 0
        while k < n:
            if k < 2:
                xx = s + np.random.randint(s)
                yy = s + np.random.randint(s)
            else:
                xx = np.random.randint(Lb)
                yy = np.random.randint(Lb)
            if belegt[xx * Lb + yy] == 0:
                belegt[xx * Lb + yy] = 1
                x[k] = xx
                y[k] = yy
                k += 1
        t12 = False
        t1u = False
        t2u = False
        for _t in range(schritte):
            ox1, oy1, ox2, oy2 = x[0], y[0], x[1], y[1]
            for i in range(n):
                if np.random.random() < p:
                    d = np.random.randint(4)
                    x[i] = (x[i] + dx[d]) % Lb
                    y[i] = (y[i] + dy[d]) % Lb
            if not t12:
                if (x[0] == x[1] and y[0] == y[1]) or (x[0] == ox2 and y[0] == oy2 and x[1] == ox1 and y[1] == oy1):
                    t12 = True
            if not (t1u and t2u):
                for i in range(2, n):
                    if not t1u and x[i] == x[0] and y[i] == y[0]:
                        t1u = True
                    if not t2u and x[i] == x[1] and y[i] == y[1]:
                        t2u = True
        if t12:
            n_frei += 1
        if not t1u and not t2u:
            n_aus += 1
            if t12:
                n_bed += 1
    return n_frei, n_aus, n_bed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--m', type=float, default=10.0)
    ap.add_argument('--rho', type=float, nargs='+', default=[0.2, 0.05, 0.0125])
    ap.add_argument('--proben', type=int, default=4000)
    ap.add_argument('--dt', type=float, default=0.1)
    ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    _seed(a.seed)
    erg = []
    for rho in a.rho:
        s = int(round(np.sqrt(a.m / rho)))
        t0 = time.time()
        nf, na, nb = lauf(s, rho, a.dt, a.proben)
        Pf = nf / a.proben
        Pa = na / a.proben
        Pb = nb / max(na, 1)
        e = dict(rho=rho, m=a.m, s=s, P_frei=Pf, P_aus=Pa, P_bed=Pb, kappa_umg=Pb / Pf if Pf > 0 else float('nan'),
                 fehler_P_frei=float(np.sqrt(Pf * (1 - Pf) / a.proben)), fehler_P_bed=float(np.sqrt(Pb * (1 - Pb) / max(na, 1))))
        erg.append(e)
        print(f"rho={rho:.4f} s={s:3d} (m={a.m:g}): P_frei = {Pf:.4f} ± {e['fehler_P_frei']:.4f}, "
              f"P(beide meiden Umgebung) = {Pa:.4f}, P_bed = {Pb:.4f} ± {e['fehler_P_bed']:.4f}, "
              f"kappa_umg = {e['kappa_umg']:.3f}   [{time.time() - t0:.0f} s]", flush=True)
    with open(os.path.join(HIER, 'ergebnisse', f'l2_kappa_m{a.m:g}.json'), 'w') as fh:
        json.dump(erg, fh, indent=1)


if __name__ == '__main__':
    main()
