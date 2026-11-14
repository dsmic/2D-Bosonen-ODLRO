#!/usr/bin/env python3
"""Auswertung Runde 1 (harte Bosonen, Wurm, großkanonisch): n_k und chi(k) E(k) bei kleinem k.

Aus den Kopf-Schwanz-Histogrammen (wurm_nb4, scan_bos.py):
  g_w(r)  = hist_eq(r) / (sum nZ * Cw M beta * 2w)      Fenstermittel von G(r, tau) über tau in [0, w)
  n_k     = sum_r cos(k.r) g(r),  g(0) := rho (exakt; das Fenstermittel liegt dort um O(w) zu tief)
  chi(k)  = sum_r cos(k.r) hist_all(r) / (sum nZ * 2 Cw M beta)   (Duhamel, = chi^- + chi^+ bei T -> 0;
            Eichung geprüft mit pruef_chi.py gegen exakt, 4x4: Abweichung < 1 %)
  rho_s   = T <W^2> / 2 (je Richtung gemittelt).
Vergleich: Josephson/Bogoliubov chi(k) E(k) -> n0 / (2 rho_s) bei kleinem k (Bogoliubov: 1/2 bei kleiner Dichte),
also chi^- E -> n0/(4 rho_s) erst für k -> 0 (bei endlichem k ist chi^-/chi = v²/(u²+v²) < 1/2, Bogoliubov);
Ungleichung (I) chi^- E <= rho ist im Phononbereich verletzt, wenn n0/(4 rho_s) > rho.
n0 grob aus g(L/2, 0)/rho (obere Schranke, 1/L-Korrektur nicht abgezogen).
Aufruf: python3 auswertung_runde1.py [Dateimuster ...]   (Standard: ergebnisse/bos_L16_*_s1 und bos_L32_*_s1)
"""
import glob
import json
import os
import sys

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
W_FENSTER = 0.05


def lade(stamm):
    d = json.load(open(stamm + '.json'))
    z = np.load(stamm + '.npz')
    return d, z['hist_eq'], z['hist_all']


def auswerten(stamm, nk_max=4):
    d, he, ha = lade(stamm)
    L, M, beta = d['L'], d['M'], d['beta']
    Cw = 1.0 / (10 * M * beta)
    nZ = float(np.sum(d['reihe']['nZ']))
    rho = d['rho']
    idx = np.arange(L)
    g = he[2 * idx[:, None] % (2 * L), 2 * idx[None, :] % (2 * L)] / (nZ * Cw * M * beta * 2 * W_FENSTER)
    D = ha[2 * idx[:, None] % (2 * L), 2 * idx[None, :] % (2 * L)] / (nZ * 2 * Cw * M * beta)
    g0_w = g[0, 0]
    g = g.copy()
    g[0, 0] = rho
    dx = np.where(idx <= L // 2, idx, idx - L)
    W2 = float(np.mean(d['reihe']['W2'][len(d['reihe']['W2']) // 10:]))
    rho_s = W2 / beta / 2
    n0_grob = g[L // 2, 0] / rho
    zeilen = []
    for n in range(1, nk_max + 1):
        k = 2 * np.pi * n / L
        ph = np.cos(k * dx)[:, None] * np.ones(L)[None, :]
        nk = float(np.sum(ph * g))
        chi = float(np.sum(ph * D))
        E = 4 - 2 * np.cos(k) - 2
        zeilen.append((n, k, nk / rho, chi * E))
    return dict(stamm=os.path.basename(stamm), L=L, beta=beta, rho=rho, mu=d['mu'], blocks=d['blocks'],
                stunden=d['time_s'] / 3600, g0_w_durch_rho=g0_w / rho, rho_s=rho_s, fs=rho_s / rho, n0_grob=n0_grob,
                josephson=n0_grob * rho / (2 * rho_s), k=zeilen)


def main():
    muster = sys.argv[1:] or [os.path.join(HIER, 'ergebnisse', f'bos_L{L}_b{2 * L}_r*_s1.json') for L in (16, 32)]
    staemme = sorted({f[:-5] for m in muster for f in glob.glob(m if m.endswith('.json') else m + '.json')})
    alle = []
    for st in staemme:
        r = auswerten(st)
        alle.append(r)
        print(f"{r['stamm']}: rho = {r['rho']:.4f}, {r['blocks']} Blöcke ({r['stunden']:.1f} h), g0_w/rho = "
              f"{r['g0_w_durch_rho']:.4f}, f_s = rho_s/rho = {r['fs']:.3f}, n0 (grob, g(L/2)/rho) = {r['n0_grob']:.3f}")
        for n, k, nkr, chiE in r['k']:
            print(f"   k = {n}·2π/L = {k:.3f}:  n_k/rho = {nkr:7.3f}   chi·E = {chiE:.4f}"
                  f"   (chi^- = Anteil v²/(u²+v²) davon, -> 1/2 erst für k -> 0; (I) verlangt chi^-E <= rho = {r['rho']:.4f})")
        print(f"   Josephson-Erwartung bei k -> 0: chi·E -> n0/(2 rho_s) ≈ {r['josephson']:.4f}")
    with open(os.path.join(HIER, 'ergebnisse', 'auswertung_runde1.json'), 'w') as fh:
        json.dump(alle, fh, indent=1)


if __name__ == '__main__':
    main()
