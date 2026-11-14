#!/usr/bin/env python3
"""e_b(2) für große Neumann-Kästen: zwei Hartkern-Teilchen, sum L_i mit Dirichlet auf Doppelbesetzung.
Vektorisiert; kleinster Eigenwert mit LOBPCG und pyamg-Vorkonditionierer. Ausgabe e_b(2) · b^2 ln b.
Aufruf: python3 l1_kasten2.py 10 12 16 20 24
"""
import sys

import numpy as np
import pyamg
import scipy.sparse as sp
from scipy.sparse.linalg import lobpcg


def matrix(b):
    M = b * b
    i1, i2 = np.triu_indices(M, k=1)
    n = i1.size
    index = -np.ones((M, M), dtype=np.int64)
    index[i1, i2] = np.arange(n)
    index[i2, i1] = np.arange(n)
    x, y = np.arange(M) // b, np.arange(M) % b
    grad = np.zeros(M)
    nachbar = []
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ok = (x + dx >= 0) & (x + dx < b) & (y + dy >= 0) & (y + dy < b)
        ziel = np.where(ok, (x + dx) * b + (y + dy), -1)
        nachbar.append(ziel)
        grad += ok
    diag = grad[i1] + grad[i2]
    r, c = [], []
    for ziel in nachbar:
        for a, bb in ((i1, i2), (i2, i1)):          # Teilchen a springt, bb bleibt
            z = ziel[a]
            ok = (z >= 0) & (z != bb)
            r.append(np.arange(n)[ok]); c.append(index[z[ok], bb[ok]])
    r, c = np.concatenate(r), np.concatenate(c)
    H = sp.csr_matrix((-np.ones(r.size), (r, c)), shape=(n, n)) + sp.diags(diag)
    return H.tocsr()


for b in map(int, sys.argv[1:]):
    H = matrix(b)
    ml = pyamg.smoothed_aggregation_solver(H, symmetry='symmetric')
    rng = np.random.default_rng(1)
    X = rng.random((H.shape[0], 1))
    w, _ = lobpcg(H, X, M=ml.aspreconditioner(), largest=False, tol=1e-9, maxiter=2000)
    print(f"b={b:3d}  dim={H.shape[0]:7d}  e_b(2) = {w[0]:.6e}   e_b(2)·b²·ln b = {w[0] * b * b * np.log(b):.4f}", flush=True)
