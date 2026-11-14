#!/usr/bin/env python3
"""Scharfes L2: Doob-Verhältnis r = g h / Z und die Aufenthaltszeit zweier bedingter Stücke, exakt in fester Umgebung.

Torus 3s x 3s, Umgebung: Poisson(rho (3s)^2) freie Irrfahrten (faule Schritte, Sprungwahrscheinlichkeit p je Zeitschritt),
Belegung occ[t, x]. Teststück i (Start S_i in der Mittelzelle): Vorwärts f_i(t, x) = P(bei x zur Zeit t, bisher
ausgewichen), Rückwärts b(t, x) = P(ab (x, t) bis T auszuweichen), Z_i = sum_x f_i(T, x) (= p*).
Bedingte Randverteilung p^h_i = f_i b / Z_i, freie p_i. Exakt:
    kappa_L = E[L | beide weichen aus] / E[L frei] = sum_{t,x} p^h_1 p^h_2 / sum_{t,x} p_1 p_2,
L = gemeinsame Aufenthaltszeit (Zahl der Zeitschritte am selben Platz). Worst-Case wäre kappa_L <= 1/(Z_1 Z_2).
Erwartung (dünnes Bild): kappa_L - 1 ~ K/ln(1/rho) mit K = m/ln(1/rho), obwohl Z ~ exp(-2 pi K) winzig ist.
Aufruf: python3 l2_doob.py [--rho 0.05 0.0125 0.003] [--m 1 2 4 8] [--umgebungen 12] [--p 0.4]
"""
import argparse
import json
import os
import time

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))


def schritt(f, p):
    return (1 - p) * f + (p / 4) * (np.roll(f, 1, 0) + np.roll(f, -1, 0) + np.roll(f, 1, 1) + np.roll(f, -1, 1))


def umgebung(rng, Lb, rho, T, p):
    n = rng.poisson(rho * Lb * Lb)
    x = rng.integers(Lb, size=n)
    y = rng.integers(Lb, size=n)
    occ = np.zeros((T + 1, Lb, Lb), dtype=bool)
    dx = np.array([1, -1, 0, 0])
    dy = np.array([0, 0, 1, -1])
    occ[0, x, y] = True
    for t in range(1, T + 1):
        spr = rng.random(n) < p
        d = rng.integers(4, size=n)
        x = np.where(spr, (x + dx[d]) % Lb, x)
        y = np.where(spr, (y + dy[d]) % Lb, y)
        occ[t, x, y] = True
    return occ


def eins(rng, s, rho, p):
    Lb = 3 * s
    T = int(round(s * s / (p / 4 * 4) * 1.0 / 1.0 * (1.0)))      # Dauer delta = s^2 (Varianz je Koordinate ~ p/2 je Schritt)
    T = int(round(2 * s * s / p))                                  # so dass die Varianz je Koordinate ~ s^2 ist
    occ = umgebung(rng, Lb, rho, T, p)
    # Startpunkte in der Mittelzelle, frei von Umgebung zur Zeit 0, verschieden
    while True:
        S = rng.integers(s, size=4) + s
        if (S[0], S[1]) != (S[2], S[3]) and not occ[0, S[0], S[1]] and not occ[0, S[2], S[3]]:
            break
    frei = ~occ
    # Rückwärts: b(T) = frei(T); b(t) = frei(t) * schritt(b(t+1))
    b = np.empty((T + 1, Lb, Lb))
    b[T] = frei[T]
    for t in range(T - 1, -1, -1):
        b[t] = frei[t] * schritt(b[t + 1], p)
    zaehler = 0.0
    nenner = 0.0
    a11 = 0.0
    a22 = 0.0
    f1 = np.zeros((Lb, Lb)); f1[S[0], S[1]] = 1.0
    f2 = np.zeros((Lb, Lb)); f2[S[2], S[3]] = 1.0
    q1 = f1.copy(); q2 = f2.copy()                                 # frei
    Z1 = b[0, S[0], S[1]]
    Z2 = b[0, S[2], S[3]]
    for t in range(T + 1):
        if t > 0:
            f1 = frei[t] * schritt(f1, p)
            f2 = frei[t] * schritt(f2, p)
            q1 = schritt(q1, p)
            q2 = schritt(q2, p)
        h1 = f1 * b[t] / Z1
        h2 = f2 * b[t] / Z2
        zaehler += np.sum(h1 * h2)
        nenner += np.sum(q1 * q2)
        w = q1 * q2
        r1 = np.divide(h1, q1, out=np.zeros_like(h1), where=q1 > 0)
        r2 = np.divide(h2, q2, out=np.zeros_like(h2), where=q2 > 0)
        a11 += np.sum(w * r1 * r1)
        a22 += np.sum(w * r2 * r2)
    return zaehler / nenner, Z1, Z2, a11 / nenner, a22 / nenner


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--rho', type=float, nargs='+', default=[0.05, 0.0125, 0.003])
    ap.add_argument('--m', type=float, nargs='+', default=[1, 2, 4, 8])
    ap.add_argument('--umgebungen', type=int, default=12)
    ap.add_argument('--p', type=float, default=0.4)
    ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    erg = []
    print("   rho      m    s   K=m/ln(1/rho)   kappa_L (Median, Mittel, Max)      Z (Median)     Worst-Case 1/Z^2 (Median)")
    for rho in a.rho:
        for m in a.m:
            s = int(round(np.sqrt(m / rho)))
            if 3 * s > 150:
                continue
            t0 = time.time()
            werte = [eins(rng, s, rho, a.p) for _ in range(a.umgebungen)]
            k = np.array([w[0] for w in werte])
            cs = np.array([np.sqrt(w[3] * w[4]) for w in werte])
            Z = np.array([np.sqrt(w[1] * w[2]) for w in werte])
            e = dict(rho=rho, m=m, s=s, K=m / np.log(1 / rho), kappa_median=float(np.median(k)),
                     kappa_mittel=float(k.mean()), kappa_max=float(k.max()), Z_median=float(np.median(Z)),
                     cs_median=float(np.median(cs)), cs_durch_kappa_median=float(np.median(cs / k)))
            erg.append(e)
            print(f"  {rho:.4f}  {m:4.1f}  {s:3d}   {e['K']:.3f}          {e['kappa_median']:.3f}  {e['kappa_mittel']:.3f}  "
                  f"{e['kappa_max']:.3f}       {e['Z_median']:.2e}     {1 / e['Z_median'] ** 2:.2e}   CS-Schranke {e['cs_median']:.3f} "
                  f"(CS/kappa {e['cs_durch_kappa_median']:.2f})   [{time.time() - t0:.0f} s]",
                  flush=True)
    with open(os.path.join(HIER, 'ergebnisse', 'l2_doob.json'), 'w') as fh:
        json.dump(erg, fh, indent=1)


if __name__ == '__main__':
    main()
