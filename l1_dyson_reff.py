#!/usr/bin/env python3
"""Diskretes Dyson-Lemma: R_eff(0 <-> Schale) auf Z^2, Schale = Gitterpunkte mit Euklid-Abstand >= R (geerdet).
Vergleich mit (1/2 pi) ln(R/a), a = e^{-gamma} 2^{-3/2} (Gitter-Streulänge): Gewicht des weichen Potentials 1/R_eff.
Aufruf: python3 l1_dyson_reff.py
"""
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve

a = np.exp(-np.euler_gamma) * 2 ** -1.5
print("   R    R_eff        (1/2pi) ln(R/a)    1/R_eff (Gewicht)   2pi/ln(R/a)")
for R in (2, 4, 8, 16, 32, 64, 128):
    h = R + 2
    xs = np.arange(-h, h + 1)
    X, Y = np.meshgrid(xs, xs, indexing='ij')
    innen = (X ** 2 + Y ** 2 < R * R)
    idx = -np.ones(X.shape, dtype=np.int64)
    idx[innen] = np.arange(innen.sum())
    n = innen.sum()
    rows, cols, vals = [], [], []
    diag = np.zeros(n)
    I, J = np.nonzero(innen)
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        I2, J2 = I + di, J + dj
        diag += 1
        nb_innen = innen[I2, J2]
        rows.append(idx[I[nb_innen], J[nb_innen]]); cols.append(idx[I2[nb_innen], J2[nb_innen]])
    rows, cols = np.concatenate(rows), np.concatenate(cols)
    Lmat = sp.csr_matrix((-np.ones(rows.size), (rows, cols)), shape=(n, n)) + sp.diags(diag)
    b = np.zeros(n); b[idx[h, h]] = 1.0                   # Einheitsstrom in 0, Schale (außen) geerdet
    v = spsolve(Lmat.tocsc(), b)
    Reff = v[idx[h, h]]
    print(f"{R:5d}  {Reff:.5f}      {np.log(R / a) / (2 * np.pi):.5f}          {1 / Reff:.5f}           {2 * np.pi / np.log(R / a):.5f}")
