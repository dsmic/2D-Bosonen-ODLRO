#!/usr/bin/env python3
"""Eine Falle, zwei Stücke: Campbell-Exponent Phi = nu * Volumen * E_y,gamma[kappa_1 - 1] (Startpunkt der Falle
gleichverteilt im Torus). Für Poisson-Fallen ist E_Umg[prod_j kappa(gamma_j)] = exp(Phi) exakt (Campbell).
Vergleich mit dem gemessenen mittleren ln kappa (§25) und Skalierung mit s (Erwartung Phi ~ c m / ln s).
Aufruf: python3 l2_einefalle.py [--faelle 0.05:4 0.0125:4 0.0125:2 0.0125:8 0.003:2] [--fallen 200]
"""
import argparse
import json
import os

import numpy as np

from l2_lokal import kappa


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--faelle', nargs='+', default=['0.05:4', '0.0125:4', '0.0125:2', '0.0125:8', '0.003:2'])
    ap.add_argument('--fallen', type=int, default=200)
    ap.add_argument('--p', type=float, default=0.4)
    a = ap.parse_args()
    rng = np.random.default_rng(17)
    dx = np.array([1, -1, 0, 0]); dy = np.array([0, 0, 1, -1])
    erg = []
    for fall in a.faelle:
        rho, m = map(float, fall.split(':'))
        s = int(round(np.sqrt(m / rho)))
        Lb = 3 * s; T = int(round(2 * s * s / a.p))
        werte = []
        for _ in range(a.fallen):
            # Teststarts in der Mittelzelle, eine Falle mit gleichverteiltem Start (nicht auf den Teststarts)
            S = rng.integers(s, size=4) + s
            while (S[0], S[1]) == (S[2], S[3]):
                S = rng.integers(s, size=4) + s
            while True:
                x0, y0 = rng.integers(Lb), rng.integers(Lb)
                if (x0, y0) != (S[0], S[1]) and (x0, y0) != (S[2], S[3]):
                    break
            occ = np.zeros((T + 1, Lb, Lb), dtype=bool)
            x, y = x0, y0
            occ[0, x, y] = True
            for t in range(1, T + 1):
                if rng.random() < a.p:
                    d = rng.integers(4)
                    x = (x + dx[d]) % Lb; y = (y + dy[d]) % Lb
                occ[t, x, y] = True
            werte.append(kappa(occ, S, a.p) - 1.0)
        w = np.array(werte)
        Phi = rho * Lb * Lb * w.mean()
        fehler = rho * Lb * Lb * w.std(ddof=1) / np.sqrt(len(w))
        e = dict(rho=rho, m=m, s=s, Phi=float(Phi), fehler=float(fehler), Phi_mal_lns_durch_m=float(Phi * np.log(s) / m),
                 anteil_negativ=float(np.mean(w < 0)))
        erg.append(e)
        print(f"rho={rho} m={m:g} s={s}: Phi = {Phi:.3f} ± {fehler:.3f}   Phi·ln s/m = {e['Phi_mal_lns_durch_m']:.3f}   "
              f"(Anteil Fallen mit kappa_1 < 1: {100 * e['anteil_negativ']:.0f} %)", flush=True)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ergebnisse', 'l2_einefalle.json'), 'w') as fh:
        json.dump(erg, fh, indent=1)


if __name__ == '__main__':
    main()
