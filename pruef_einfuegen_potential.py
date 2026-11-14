#!/usr/bin/env python3
"""Einfügeschranke mit anziehendem Potential (satz_3_9_dichteschranken.md §11, Lemma 11.1): exakte Prüfung.

Harte Bosonen auf (ℤ/Lℤ)², ℒ_k − Σ_i W(x_i) mit W ≥ 0 (Gauß-Mulde der Tiefe w0). ε^W_k = Grundenergie.
Behauptung: ε^W_k − ε^W_{k−1} ≤ 8ρ′/(1 − ρ′), ρ′ = (k−1)/M (Lemma 6.5 mit f = 1 − δ₀), unabhängig von W.
Zum Vergleich die Zuwächse ohne Potential und die lokale Dichte in der Mulde.
Aufruf: python3 pruef_einfuegen_potential.py
"""
import itertools

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh


def sektor(L, k, W):
    M = L * L
    x, y = np.arange(M) // L, np.arange(M) % L
    nb = np.stack([((x + dx) % L) * L + (y + dy) % L for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))], 1)
    T = list(itertools.combinations(range(M), k))
    idx = {t: i for i, t in enumerate(T)}
    r, c = [], []
    for i, t in enumerate(T):
        s = set(t)
        for p in t:
            for q in nb[p]:
                if q not in s:
                    r.append(i); c.append(idx[tuple(sorted((s - {p}) | {q}))])
    A = sp.coo_matrix((np.ones(len(r)), (r, c)), shape=(len(T),) * 2).tocsr()
    Tn = np.array(T)
    H = 4 * k * sp.identity(len(T)) - A - sp.diags(W[Tn].sum(1))
    if len(T) == 1:
        return H.toarray()[0, 0], Tn, np.ones(1)
    w, v = eigsh(H, k=1, which='SA', tol=1e-12)
    return w[0], Tn, np.abs(v[:, 0])


def main():
    L = 6
    M = L * L
    xs, ys = np.arange(M) // L, np.arange(M) % L
    d2 = np.minimum(xs, L - xs) ** 2 + np.minimum(ys, L - ys) ** 2
    print(f"L = {L}; Mulde W(x) = w0 · exp(−|x|²/2) um den Ursprung")
    print(f"{'w0':>5} {'k':>2} {'ε^W_k − ε^W_k−1':>17} {'ohne W':>9} {'Schranke 8ρ′/(1−ρ′)':>20} {'Teilchen in Mulde (r≤1)':>24}")
    for w0 in (0.0, 0.05, 0.2, 1.0, 3.0):
        W = w0 * np.exp(-d2 / 2)
        e_alt = 0.0
        for k in range(1, 6):
            e, T, psi = sektor(L, k, W)
            e0, _, _ = sektor(L, k, np.zeros(M)) if w0 > 0 else (e, None, None)
            rho_p = (k - 1) / M
            schranke = 8 * rho_p / (1 - rho_p)
            mulde = (psi ** 2 * (d2[T] <= 1).sum(1)).sum() / (psi ** 2).sum()
            if k == 1:
                print(f"{w0:5.2f} {k:2d} {e:17.5f} {'':>9} {'(ε^W_1 = Grundenergie eines Teilchens)':>20}")
            else:
                print(f"{w0:5.2f} {k:2d} {e - e_alt:17.5f} {e0 - e0_alt:9.5f} {schranke:20.5f} {mulde:24.3f}")
            e_alt, e0_alt = e, e0
        print()


if __name__ == '__main__':
    main()
