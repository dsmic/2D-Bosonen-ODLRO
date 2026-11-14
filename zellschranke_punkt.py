#!/usr/bin/env python3
"""L1c numerisch: kleinster Eigenwert des Neumann-Graph-Laplace-Operators auf einem b x b-Kasten mit Dirichlet-Bedingung
in einem Punkt y (das Partnerteilchen). Erwartung 2D: lambda_min(b, y) ~ c / (b^2 ln b) (Punktkapazität), Minimum über y.
Hintergrund: H + 4N = sum_i L_i mit Dirichlet auf der Stoßmenge (einpunkt_zeitroute.md §16).
Aufruf: python3 zellschranke_punkt.py
"""
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh


def laplace_kasten(b):
    n = b * b
    r, c = [], []
    for x in range(b):
        for y in range(b):
            i = x * b + y
            if x + 1 < b:
                r += [i, i + b]; c += [i + b, i]
            if y + 1 < b:
                r += [i, i + 1]; c += [i + 1, i]
    A = sp.csr_matrix((np.ones(len(r)), (r, c)), shape=(n, n))
    return sp.diags(np.asarray(A.sum(axis=1)).ravel()) - A


print(" b    y=Ecke        y=Rand-Mitte  y=Mitte      min·b²·ln b")
for b in (4, 8, 16, 32, 64, 128):
    L = laplace_kasten(b)
    werte = []
    for (px, py) in ((0, 0), (0, b // 2), (b // 2, b // 2)):
        k = px * b + py
        keep = np.array([i for i in range(b * b) if i != k])
        Lk = L[keep][:, keep]
        lam = eigsh(Lk, k=1, sigma=0, which='LM', return_eigenvectors=False)[0]
        werte.append(lam)
    m = min(werte)
    print(f"{b:4d}  {werte[0]:.6f}  {werte[1]:.6f}  {werte[2]:.6f}   {m * b * b * np.log(b):.4f}")
