#!/usr/bin/env python3
"""Lochenergie exakt: Delta E = E_0(N; Torus ohne h x h-Block) - E_0(N; Torus), harte Bosonen, H = -A.
Weich: E_0(H + lam * n_Block) - E_0(H) für lam = 0,1 … 10 (konkav in lam, Steigung bei 0 = <n_Block>).
Für das Feynman-Kac-Lochargument (einpunkt_zeitroute.md §28): P(Block eine Zeit delta leer) <= exp(-delta Delta E).
Aufruf: python3 l1_loch.py [--L 8] [--N 2 3 4] [--h 1 2 3 4]
"""
import argparse
import itertools
import json
import os
import time

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

HIER = os.path.dirname(os.path.abspath(__file__))


def gitter(L):
    M = L * L
    x, y = np.arange(M) // L, np.arange(M) % L
    nb = np.stack([((x + dx) % L) * L + (y + dy) % L for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))], 1)
    return M, nb


def sektor(M, nb, erlaubt, N, pot=None):
    plaetze = np.nonzero(erlaubt)[0]
    T = np.array(list(itertools.combinations(plaetze, N)), dtype=np.int64)
    basis = M ** np.arange(N)[::-1]
    keys = T @ basis
    n = T.shape[0]
    src, dst = [], []
    for p in range(N):
        for d in range(4):
            neu = nb[T[:, p], d]
            ok = erlaubt[neu].copy()
            for q in range(N):
                if q != p:
                    ok &= neu != T[:, q]
            idx = np.nonzero(ok)[0]
            Tn = T[idx].copy()
            Tn[:, p] = neu[idx]
            Tn.sort(axis=1)
            src.append(idx); dst.append(np.searchsorted(keys, Tn @ basis))
    src, dst = np.concatenate(src), np.concatenate(dst)
    H = -sp.coo_matrix((np.ones(src.size), (src, dst)), shape=(n, n)).tocsr()
    if pot is not None:
        H = H + sp.diags(pot[T].sum(axis=1))
    return H


def e0(H):
    return -float(eigsh(-H, k=1, which='LA', tol=1e-11, return_eigenvectors=False)[0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--L', type=int, default=8)
    ap.add_argument('--N', type=int, nargs='+', default=[2, 3, 4])
    ap.add_argument('--h', type=int, nargs='+', default=[1, 2, 3, 4])
    ap.add_argument('--weich', type=float, nargs='*', default=[0.1, 0.3, 1.0, 3.0, 10.0])
    a = ap.parse_args()
    M, nb = gitter(a.L)
    alle = []
    for N in a.N:
        t0 = time.time()
        frei = np.ones(M, dtype=bool)
        E_voll = e0(sektor(M, nb, frei, N))
        for h in a.h:
            blk = np.zeros(M, dtype=bool)
            for i in range(h):
                for j in range(h):
                    blk[i * a.L + j] = True
            E_loch = e0(sektor(M, nb, ~blk, N))
            weich = {}
            for lam in a.weich:
                weich[lam] = e0(sektor(M, nb, frei, N, pot=lam * blk.astype(float))) - E_voll
            rho = N / M
            e = dict(L=a.L, N=N, h=h, rho=rho, E_voll=E_voll, dE_hart=E_loch - E_voll, dE_weich=weich,
                     dE_durch_rho=(E_loch - E_voll) / rho, erwartet_n_block=rho * h * h)
            alle.append(e)
            print(f"L={a.L} N={N} (rho={rho:.4f}) h={h}: Delta E hart = {E_loch - E_voll:.5f}  (/rho = {e['dE_durch_rho']:.3f}); "
                  "weich: " + "  ".join(f"lam={l:g}: {v:.5f}" for l, v in weich.items())
                  + f"   [<n_Block> = {rho * h * h:.3f}; {time.time() - t0:.0f} s]", flush=True)
    with open(os.path.join(HIER, 'ergebnisse', f'l1_loch_L{a.L}.json'), 'w') as fh:
        json.dump(alle, fh, indent=1)


if __name__ == '__main__':
    main()
