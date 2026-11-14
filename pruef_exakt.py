#!/usr/bin/env python3
"""Exakte großkanonische Werte bei endlicher Temperatur für harte Bosonen auf L x L (volle Diagonalisierung je
Teilchenzahl), zum Vergleich mit scan_bos.py bei festem mu: <N>, <H_kin>, g(r) = <b_{x+r}^+ b_x> für r = 0,
(L/2, 0), (L/2, L/2).
Aufruf: python3 pruef_exakt.py L beta mu
"""
import itertools
import sys

import numpy as np


def main():
    L, beta, mu = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    M = L * L
    nb = [[((s % L + dx) % L) + L * ((s // L + dy) % L) for dx, dy in ((1, 0), (0, 1))] for s in range(M)]
    kanten = [(s, t) for s in range(M) for t in nb[s]]

    def verschiebe(s, rx, ry):
        return ((s % L + rx) % L) + L * ((s // L + ry) % L)
    teile = []
    for N in range(M + 1):
        konf = [sum(1 << i for i in c) for c in itertools.combinations(range(M), N)]
        idx = {c: i for i, c in enumerate(konf)}
        n = len(konf)
        H = np.zeros((n, n))
        for i, c in enumerate(konf):
            for s, t in kanten:
                if (c >> s & 1) != (c >> t & 1):
                    j = idx[c ^ (1 << s) ^ (1 << t)]
                    H[i, j] -= 1.0
        E, V = np.linalg.eigh(H)
        # Erwartungswerte von O_r = (1/M) sum_x b_{x+r}^+ b_x in den Eigenzuständen
        ops = {}
        for r in ((0, 0), (L // 2, 0), (L // 2, L // 2)):
            O = np.zeros((n, n))
            for i, c in enumerate(konf):
                for x in range(M):
                    y = verschiebe(x, *r)
                    if not (c >> x & 1):
                        continue
                    if y == x:
                        O[i, i] += 1.0 / M
                    elif not (c >> y & 1):
                        O[idx[c ^ (1 << x) ^ (1 << y)], i] += 1.0 / M
            ops[r] = np.sum(V * (O @ V), axis=0)          # <n|O|n>, BLAS statt einsum
        teile.append((N, E, ops))
    emin = min(np.min(E - mu * N) for N, E, _ in teile)
    Z = Nm = Em = 0.0
    gm = {r: 0.0 for r in teile[0][2]}
    for N, E, ops in teile:
        w = np.exp(-beta * (E - mu * N - emin))
        Z += w.sum()
        Nm += N * w.sum()
        Em += (w * E).sum()
        for r in gm:
            gm[r] += (w * ops[r]).sum()
    Nm, Em = Nm / Z, Em / Z
    g = {r: v / Z for r, v in gm.items()}
    r0, rx, rd = (0, 0), (L // 2, 0), (L // 2, L // 2)
    print(f"exakt L={L} beta={beta} mu={mu}: rho = {Nm / M:.5f}, E_kin/M = {Em / M:.5f}, g0 = {g[r0]:.5f}, "
          f"g(L/2,0) = {g[rx]:.5f} (/g0 {g[rx] / g[r0]:.4f}), g(L/2,L/2) = {g[rd]:.5f} (/g0 {g[rd] / g[r0]:.4f})")


if __name__ == '__main__':
    main()
