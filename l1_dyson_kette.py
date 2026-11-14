#!/usr/bin/env python3
"""Prüfung der Kette Dyson -> weiches Potential -> Temple für n = 2 Teilchen im b x b-Neumann-Kasten.
U_x(y): Dyson-Potential mit Quelle x, Ziel S = {y: |y - x| >= R} (geerdet), Einheitsstrom, U = Austrittsstrom / R_eff.
W(x1, x2) = U_{x2}(x1) + U_{x1}(x2). Streng gilt e_b(2) >= lambda_min(eps T + (1-eps) W) (T = L_1 + L_2, ohne harten Kern).
Temple mit der Konstanten: E0 >= <W'> - (<W'^2> - <W'>^2)/(eps*lam2 - <W'>), W' = (1-eps) W, lam2 = 2 - 2 cos(pi/b).
Aufruf: python3 l1_dyson_kette.py
"""
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh, spsolve

from l1_kasten2 import matrix as hartkern_matrix
from scipy.sparse.linalg import lobpcg
import pyamg


def laplace(b):
    n = b * b
    x, y = np.arange(n) // b, np.arange(n) % b
    r, c = [], []
    for dx, dy in ((1, 0), (0, 1)):
        ok = (x + dx < b) & (y + dy < b)
        i = np.nonzero(ok)[0]; j = (x[i] + dx) * b + (y[i] + dy)
        r += [i, j]; c += [j, i]
    r, c = np.concatenate(r), np.concatenate(c)
    A = sp.csr_matrix((np.ones(r.size), (r, c)), shape=(n, n))
    return (sp.diags(np.asarray(A.sum(1)).ravel()) - A).tocsr(), x, y


def dyson_U(b, R):
    Lq, x, y = laplace(b)
    n = b * b
    U = np.zeros((n, n))                  # U[x_quelle, y]
    for q in range(n):
        S = (x - x[q]) ** 2 + (y - y[q]) ** 2 >= R * R
        if not S.any():
            continue
        frei = ~S
        idx = np.nonzero(frei)[0]
        A = Lq[idx][:, idx].tocsc()
        rhs = np.zeros(idx.size); rhs[np.searchsorted(idx, q)] = 1.0
        v_frei = spsolve(A, rhs)
        v = np.zeros(n); v[idx] = v_frei
        Reff = v[q]
        # Strom in S-Punkte: sum über Nachbarn z in frei von v(z)
        strom = np.asarray(-(Lq[S][:, frei] @ v_frei)).ravel()   # -L_{y,z} = 1 für Kanten
        U[q, np.nonzero(S)[0]] = strom / Reff
    return U


for b in (6, 8, 10, 12):
    H = hartkern_matrix(b)
    ml = pyamg.smoothed_aggregation_solver(H, symmetry='symmetric')
    w, _ = lobpcg(H, np.random.default_rng(1).random((H.shape[0], 1)), M=ml.aspreconditioner(), largest=False, tol=1e-10, maxiter=3000)
    e2 = w[0]
    Lq, _, _ = laplace(b)
    n = b * b
    I = sp.identity(n, format='csr')
    T = sp.kron(Lq, I) + sp.kron(I, Lq)
    lam2 = 2 - 2 * np.cos(np.pi / b)
    for R in (2, 3, max(4, b // 3)):
        U = dyson_U(b, R)
        Wmat = (U.T + U).ravel()          # W(x1, x2) = U[x2, x1] + U[x1, x2], Index x1*n + x2
        for eps in (0.2, 0.5):
            Hs = eps * T + (1 - eps) * sp.diags(Wmat)
            lmin = eigsh(Hs, k=1, sigma=-1e-6, which='LM', return_eigenvectors=False)[0]
            Wp = (1 - eps) * Wmat
            m1, m2 = Wp.mean(), (Wp ** 2).mean()
            temple = m1 - (m2 - m1 ** 2) / (eps * lam2 - m1) if eps * lam2 > m1 else float('nan')
            print(f"b={b:3d} R={R:2d} eps={eps:.1f}: e_b(2) exakt {e2:.5f}  >=  lambda_min(weich) {lmin:.5f} "
                  f"({100 * lmin / e2:.0f} %)   Temple {temple:.5f} ({100 * temple / e2:.0f} %)   <W'> = {m1:.5f}", flush=True)
