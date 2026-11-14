#!/usr/bin/env python3
"""Scharfes L2, Lokalisierung: Wie hängt kappa_L davon ab, welche Fallen man berücksichtigt?
Gleiche Umgebung, nur Fallen behalten, deren Bahn irgendwann im Sup-Abstand < D vom Mittelpunkt der Startzelle ist.
D = s/8, s/4, s/2, s, 1,5 s, alle. Wenn kappa_L(D) schon bei kleinem D sättigt, kürzen sich ferne Fallen (Harnack).
Aufruf: python3 l2_lokal.py [--rho 0.0125] [--m 4 8] [--umgebungen 30]
"""
import argparse
import json
import os

import numpy as np

from l2_doob import schritt


def kappa(occ, S, p):
    T = occ.shape[0] - 1
    frei = ~occ
    b = np.empty(occ.shape); b[T] = frei[T]
    for t in range(T - 1, -1, -1):
        b[t] = frei[t] * schritt(b[t + 1], p)
    Lb = occ.shape[1]
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
    return za / ne


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--rho', type=float, default=0.0125)
    ap.add_argument('--m', type=float, nargs='+', default=[4, 8])
    ap.add_argument('--umgebungen', type=int, default=30)
    ap.add_argument('--p', type=float, default=0.4)
    a = ap.parse_args()
    rng = np.random.default_rng(11)
    erg = []
    for m in a.m:
        s = int(round(np.sqrt(m / a.rho)))
        Lb = 3 * s; T = int(round(2 * s * s / a.p))
        Ds = [s / 8, s / 4, s / 2, s, 1.5 * s, np.inf]
        tab = []
        for _ in range(a.umgebungen):
            n = rng.poisson(a.rho * Lb * Lb)
            x = rng.integers(Lb, size=n); y = rng.integers(Lb, size=n)
            dx = np.array([1, -1, 0, 0]); dy = np.array([0, 0, 1, -1])
            X = np.zeros((T + 1, n), dtype=np.int64); Y = np.zeros((T + 1, n), dtype=np.int64)
            X[0], Y[0] = x, y
            for t in range(1, T + 1):
                spr = rng.random(n) < a.p
                d = rng.integers(4, size=n)
                X[t] = np.where(spr, (X[t - 1] + dx[d]) % Lb, X[t - 1]); Y[t] = np.where(spr, (Y[t - 1] + dy[d]) % Lb, Y[t - 1])
            c = 1.5 * s
            dmin = np.max(np.stack([np.abs(X - c), np.abs(Y - c)]), axis=0).min(axis=0) if n else np.zeros(0)
            occ0 = np.zeros((T + 1, Lb, Lb), dtype=bool)
            for j in range(n):
                occ0[np.arange(T + 1), X[:, j], Y[:, j]] = True
            while True:
                S = rng.integers(s, size=4) + s
                if (S[0], S[1]) != (S[2], S[3]) and not occ0[0, S[0], S[1]] and not occ0[0, S[2], S[3]]:
                    break
            zeile = []
            for D in Ds:
                occ = np.zeros((T + 1, Lb, Lb), dtype=bool)
                for j in np.nonzero(dmin < D)[0]:
                    occ[np.arange(T + 1), X[:, j], Y[:, j]] = True
                zeile.append(np.log(kappa(occ, S, a.p)))
            tab.append(zeile)
        tab = np.array(tab)
        voll = tab[:, -1]
        txt = "  ".join(f"D={D / s if np.isfinite(D) else np.inf:.3g}s: {tab[:, i].mean():.3f}" for i, D in enumerate(Ds))
        anteil = [float(np.mean(tab[:, i]) / np.mean(voll)) for i in range(len(Ds))]
        print(f"m={m:g} s={s}: mittleres ln kappa_L je Fallenradius D:  {txt}", flush=True)
        print("        Anteil am vollen Wert: " + "  ".join(f"{v:.2f}" for v in anteil)
              + f"   | mittlere |Δ ln kappa| zwischen D = s und alle: {np.mean(np.abs(tab[:, 3] - voll)):.3f}", flush=True)
        erg.append(dict(m=m, s=s, D_durch_s=[float(D / s) if np.isfinite(D) else None for D in Ds],
                        mittel_lnk=[float(v) for v in tab.mean(axis=0)], anteil=anteil))
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ergebnisse', 'l2_lokal.json'), 'w') as fh:
        json.dump(erg, fh, indent=1)


if __name__ == '__main__':
    main()
