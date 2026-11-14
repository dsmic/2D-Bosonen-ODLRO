#!/usr/bin/env python3
"""Scharfes L2, Paarfehler: Kommt D = ln kappa(alle) - sum_j ln kappa(j) von Fallenpaaren?
D2 = sum_{j<k, beide nah} [ln kappa(j,k) - ln kappa(j) - ln kappa(k)]  (Mayer-artig, zweite Ordnung).
Fallen in Reichweite: Sup-Abstand < 1,5 s von der Startzelle; Paare nur unter Fallen mit Abstand < s.
Aufruf: python3 l2_paare.py [--rho 0.0125] [--m 2 4] [--umgebungen 15 6]
"""
import argparse
import json
import os

import numpy as np

from l2_lokal import kappa


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--rho', type=float, default=0.0125)
    ap.add_argument('--m', type=float, nargs='+', default=[2, 4])
    ap.add_argument('--umgebungen', type=int, nargs='+', default=[15, 6])
    ap.add_argument('--p', type=float, default=0.4)
    a = ap.parse_args()
    rng = np.random.default_rng(23)
    dx = np.array([1, -1, 0, 0]); dy = np.array([0, 0, 1, -1])
    erg = []
    for m, nU in zip(a.m, a.umgebungen):
        s = int(round(np.sqrt(m / a.rho)))
        Lb = 3 * s; T = int(round(2 * s * s / a.p))
        D_l, D2_l, Dmax_paar, npaar = [], [], [], []
        for _ in range(nU):
            n = rng.poisson(a.rho * Lb * Lb)
            X = np.zeros((T + 1, n), dtype=np.int64); Y = np.zeros((T + 1, n), dtype=np.int64)
            X[0] = rng.integers(Lb, size=n); Y[0] = rng.integers(Lb, size=n)
            for t in range(1, T + 1):
                spr = rng.random(n) < a.p
                d = rng.integers(4, size=n)
                X[t] = np.where(spr, (X[t - 1] + dx[d]) % Lb, X[t - 1]); Y[t] = np.where(spr, (Y[t - 1] + dy[d]) % Lb, Y[t - 1])
            c = 1.5 * s
            dmin = np.max(np.stack([np.abs(X - c), np.abs(Y - c)]), axis=0).min(axis=0) if n else np.zeros(0)
            reich = np.nonzero(dmin < 1.5 * s)[0]
            nah = np.nonzero(dmin < s)[0]

            def occ_von(js):
                o = np.zeros((T + 1, Lb, Lb), dtype=bool)
                for j in js:
                    o[np.arange(T + 1), X[:, j], Y[:, j]] = True
                return o
            o_alle = occ_von(reich)
            while True:
                S = rng.integers(s, size=4) + s
                if (S[0], S[1]) != (S[2], S[3]) and not o_alle[0, S[0], S[1]] and not o_alle[0, S[2], S[3]]:
                    break
            lk_alle = np.log(kappa(o_alle, S, a.p))
            einz = {j: np.log(kappa(occ_von([j]), S, a.p)) for j in reich}
            D = lk_alle - sum(einz.values())
            paar = []
            for i1 in range(len(nah)):
                for i2 in range(i1 + 1, len(nah)):
                    j, k = nah[i1], nah[i2]
                    paar.append(np.log(kappa(occ_von([j, k]), S, a.p)) - einz[j] - einz[k])
            D2 = float(np.sum(paar)) if paar else 0.0
            D_l.append(D); D2_l.append(D2); Dmax_paar.append(max(paar) if paar else 0.0); npaar.append(len(paar))
            print(f"   m={m:g}: D = {D:+.3f}   D2 = {D2:+.3f}   größter Paarbeitrag {Dmax_paar[-1]:+.3f}   ({len(paar)} Paare)",
                  flush=True)
        D_l, D2_l = np.array(D_l), np.array(D2_l)
        e = dict(m=m, s=s, D=D_l.tolist(), D2=D2_l.tolist(), korr=float(np.corrcoef(D_l, D2_l)[0, 1]) if len(D_l) > 2 else None,
                 rest_mittel=float(np.mean(D_l - D2_l)), rest_streuung=float(np.std(D_l - D2_l)),
                 D_streuung=float(np.std(D_l)), paare_mittel=float(np.mean(npaar)))
        erg.append(e)
        print(f"m={m:g} s={s}: Korrelation D/D2 = {e['korr']:.2f}; Streuung D {e['D_streuung']:.3f}, "
              f"Streuung (D - D2) {e['rest_streuung']:.3f}; Mittel D {D_l.mean():+.3f}, D2 {D2_l.mean():+.3f}", flush=True)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ergebnisse', 'l2_paare.json'), 'w') as fh:
        json.dump(erg, fh, indent=1)


if __name__ == '__main__':
    main()
