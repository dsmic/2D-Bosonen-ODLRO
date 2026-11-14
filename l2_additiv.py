#!/usr/bin/env python3
"""Scharfes L2, Produktvermutung: ln kappa(alle Fallen) gegen sum_j ln kappa(nur Falle j).
Wenn ln kappa(alle) <= sum_j ln kappa(j) (Subadditivität) gilt, folgt für Poisson-Fallen mit der Campbell-Formel
E_Umg[kappa] <= exp(nu * int (kappa_1(gamma) - 1)) — das Problem reduziert sich auf eine Falle und zwei Stücke.
Nur Fallen im Sup-Abstand < 1,5 s von der Startzelle (Lokalisierung, l2_lokal.py).
Aufruf: python3 l2_additiv.py [--rho 0.0125] [--m 2 4 8] [--umgebungen 20]
"""
import argparse
import json
import os

import numpy as np

from l2_lokal import kappa


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--rho', type=float, default=0.0125)
    ap.add_argument('--m', type=float, nargs='+', default=[2, 4, 8])
    ap.add_argument('--umgebungen', type=int, default=20)
    ap.add_argument('--p', type=float, default=0.4)
    a = ap.parse_args()
    rng = np.random.default_rng(13)
    erg = []
    for m in a.m:
        s = int(round(np.sqrt(m / a.rho)))
        Lb = 3 * s; T = int(round(2 * s * s / a.p))
        voll, summe, ndiff = [], [], []
        for _ in range(a.umgebungen):
            n = rng.poisson(a.rho * Lb * Lb)
            dx = np.array([1, -1, 0, 0]); dy = np.array([0, 0, 1, -1])
            X = np.zeros((T + 1, n), dtype=np.int64); Y = np.zeros((T + 1, n), dtype=np.int64)
            X[0] = rng.integers(Lb, size=n); Y[0] = rng.integers(Lb, size=n)
            for t in range(1, T + 1):
                spr = rng.random(n) < a.p
                d = rng.integers(4, size=n)
                X[t] = np.where(spr, (X[t - 1] + dx[d]) % Lb, X[t - 1]); Y[t] = np.where(spr, (Y[t - 1] + dy[d]) % Lb, Y[t - 1])
            c = 1.5 * s
            dmin = np.max(np.stack([np.abs(X - c), np.abs(Y - c)]), axis=0).min(axis=0) if n else np.zeros(0)
            nah = np.nonzero(dmin < 1.5 * s)[0]
            occ = np.zeros((T + 1, Lb, Lb), dtype=bool)
            for j in nah:
                occ[np.arange(T + 1), X[:, j], Y[:, j]] = True
            while True:
                S = rng.integers(s, size=4) + s
                if (S[0], S[1]) != (S[2], S[3]) and not occ[0, S[0], S[1]] and not occ[0, S[2], S[3]]:
                    break
            lk = np.log(kappa(occ, S, a.p))
            einzeln = 0.0
            for j in nah:
                o = np.zeros((T + 1, Lb, Lb), dtype=bool)
                o[np.arange(T + 1), X[:, j], Y[:, j]] = True
                einzeln += np.log(kappa(o, S, a.p))
            voll.append(lk); summe.append(einzeln); ndiff.append(len(nah))
        voll, summe = np.array(voll), np.array(summe)
        diff = voll - summe
        e = dict(m=m, s=s, lnk_voll_mittel=float(voll.mean()), summe_einzeln_mittel=float(summe.mean()),
                 diff_mittel=float(diff.mean()), diff_max=float(diff.max()), anteil_subadditiv=float(np.mean(diff <= 0)),
                 fallen_mittel=float(np.mean(ndiff)), korr=float(np.corrcoef(voll, summe)[0, 1]))
        erg.append(e)
        print(f"m={m:g} s={s} ({e['fallen_mittel']:.0f} Fallen in Reichweite): ln kappa(alle) = {voll.mean():.3f}, "
              f"sum_j ln kappa(j) = {summe.mean():.3f}, Korrelation {e['korr']:.2f}; Differenz Mittel {diff.mean():+.3f}, "
              f"Max {diff.max():+.3f}; subadditiv in {100 * e['anteil_subadditiv']:.0f} % der Umgebungen", flush=True)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ergebnisse', 'l2_additiv.json'), 'w') as fh:
        json.dump(erg, fh, indent=1)


if __name__ == '__main__':
    main()
