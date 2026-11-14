#!/usr/bin/env python3
"""Exakte Hartkern-Grundenergie e_b(n) im b x b-Neumann-Kasten (Graph-Laplace nur innen, Dirichlet auf Doppelbesetzung):
e_b(n) = kleinster Eigenwert von sum_i L_i auf n-Teilchen-Hartkern-Konfigurationen, = E_0 + 4n mit H = -A_innen + Grad.
Vergleich mit der Paarungsschranke (L1c): e_b(2) >= pi/(2 b^2 ln b), und Untergrenze je Teilchen.
Aufruf: python3 l1_kastenenergie.py
"""
import itertools

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh


def kasten(b, n):
    M = b * b
    nb = [[] for _ in range(M)]
    for x in range(b):
        for y in range(b):
            i = x * b + y
            if x + 1 < b:
                nb[i].append(i + b); nb[i + b].append(i)
            if y + 1 < b:
                nb[i].append(i + 1); nb[i + 1].append(i)
    konf = list(itertools.combinations(range(M), n))
    idx = {c: k for k, c in enumerate(konf)}
    r, c, v = [], [], []
    diag = np.zeros(len(konf))
    for k, cf in enumerate(konf):
        s = set(cf)
        for x in cf:
            for y in nb[x]:
                diag[k] += 1.0                       # Kante x-y (Neumann: nur innere Kanten zählen)
                if y not in s:
                    j = idx[tuple(sorted(s - {x} | {y}))]
                    r.append(k); c.append(j); v.append(-1.0)
                # y besetzt: Dirichlet-Term (Psi(c) - 0)^2, also nur Diagonale
    H = sp.csr_matrix((v, (r, c)), shape=(len(konf), len(konf))) + sp.diags(diag)
    return float(eigsh(H, k=1, sigma=-1e-3, which='LM', return_eigenvectors=False)[0])


print("  b   e_b(2)·b²·ln b   (Paarungsschranke pi/2 = 1.571)   e_b(3)·b²·ln b   e_b(3)/e_b(2)")
for b in (4, 6, 8, 10, 12, 14):
    e2 = kasten(b, 2)
    e3 = kasten(b, 3) if b <= 10 else float('nan')
    f = b * b * np.log(b)
    print(f"{b:3d}   {e2 * f:8.3f}                                         {e3 * f:8.3f}        {e3 / e2:6.3f}", flush=True)
