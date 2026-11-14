#!/usr/bin/env python3
"""Varianz der Blockbesetzung im exakten Grundzustand, auch unter Kippung g = e^{lam n_U}:
Var_g(n_U) / E_g(n_U) (Poisson: 1). Für den Hebel in satz_3_9_dichteschranken.md §6.
Aufruf: python3 l1_varianz.py
"""
import os
import sys

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "z2", "zweipaar_graph"))
import falk_bruch as fb  # noqa: E402
from einpunkt_kriterium import perron  # noqa: E402

for L, N in ((6, 4), (6, 6), (8, 3), (8, 4)):
    kompat, ziel, *_ = fb.geometrie("bosonen", L)
    S = fb.Sektor(N, kompat, ziel)
    psi = perron(S.H)
    w = psi ** 2
    x, y = S.T // L, S.T % L
    zeilen = []
    for h in (2, 3, 4):
        if h >= L:
            continue
        n = ((x < h) & (y < h)).sum(axis=1).astype(float)
        teile = []
        for lam in (0.0, 0.5, 1.0, -1.0):
            g2 = np.exp(2 * lam * n) * w
            g2 /= g2.sum()
            E = (g2 * n).sum()
            V = (g2 * n * n).sum() - E * E
            teile.append(f"lam={lam:+.1f}: E={E:.3f} Var/E={V / E:.3f}")
        print(f"L={L} N={N} rho={N / L / L:.3f} h={h}:  " + "   ".join(teile), flush=True)
