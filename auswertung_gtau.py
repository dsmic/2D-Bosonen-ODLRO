#!/usr/bin/env python3
"""Z0 aus den kanonischen G(tau)-Läufen (scan_gtau.py): hist(tau) ~ exp(kappa tau) (A + sum B e^{-eps tau}).
Plateau-Fit von log hist auf [f1 beta, f2 beta] -> kappa, A; hist(0) aus quadratischer Extrapolation der ersten Bins;
Z0 = A / hist(0). Fehler: Jackknife über 10 Blockgruppen.
Aufruf: python3 auswertung_gtau.py [--f1 0.2] [--f2 0.45]
"""
import argparse
import glob
import json
import os

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))


def z0(h, beta, f1, f2):
    nb = h.size
    tau = (np.arange(nb) + 0.5) * beta / nb
    m = (tau >= f1 * beta) & (tau <= f2 * beta) & (h > 0)
    k, logA = np.polyfit(tau[m], np.log(h[m]), 1)
    # hist(0): quadratische Extrapolation der ersten 4 Bins
    c = np.polyfit(tau[:4], np.log(h[:4]), 2)
    h0 = np.exp(c[-1])
    return np.exp(logA) / h0, k


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--f1', type=float, default=0.2)
    ap.add_argument('--f2', type=float, default=0.45)
    a = ap.parse_args()
    erg = []
    for f in sorted(glob.glob(os.path.join(HIER, 'ergebnisse', 'gtau_L*_s*.json'))):
        d = json.load(open(f))
        B = np.array(d['hist_tau_bloecke_128'])
        if B.shape[0] < 10:
            continue
        Z, k = z0(B.sum(0), d['beta'], a.f1, a.f2)
        gruppen = np.array_split(np.arange(B.shape[0]), 10)
        jk = np.array([z0(B[np.setdiff1d(np.arange(B.shape[0]), g)].sum(0), d['beta'], a.f1, a.f2)[0] for g in gruppen])
        fehler = np.sqrt(9 / 10 * np.sum((jk - jk.mean()) ** 2))
        e = dict(datei=os.path.basename(f), L=d['L'], N=d['N'], rho=d['rho'], beta=d['beta'], bloecke=int(B.shape[0]),
                 Z0=float(Z), fehler=float(fehler), kappa=float(k))
        erg.append(e)
        print(f"{e['datei']:36s} L={e['L']} N={e['N']} Blöcke {e['bloecke']:4d}:  Z0 = {Z:.4f} ± {fehler:.4f}   "
              f"(Rest-Exponent {k:+.4f})", flush=True)
    with open(os.path.join(HIER, 'ergebnisse', 'auswertung_gtau.json'), 'w') as fh:
        json.dump(erg, fh, indent=1)


if __name__ == '__main__':
    main()
