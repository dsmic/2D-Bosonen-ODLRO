#!/usr/bin/env python3
"""Zugänglichkeit statt Lemma P* (Anhang P): exakte Prüfung der Spektralschranke.

Für eine Scheibe der Dauer δ, in der die Teilchen einer Menge A (|A| = k, markiert) mit niemandem wechselwirken, ist
  R_k(δ) = Z(A frei in der Scheibe) / Z_N  →  e^{δ E_N} ⟨ψ_N, e^{−δ H_rel} ψ_N⟩      (β → ∞),
mit ψ_N dem bosonischen Grundzustand, als symmetrische Funktion markierter Teilchen geschrieben (null auf Stößen), und
H_rel: Teilchen aus A springen frei auf jeden Nachbarplatz, die übrigen nur auf Plätze ohne andere Nicht-A-Teilchen.
Behauptung (Anhang P, Lemma P2):  R_k(δ) ≤ e^{δ(ε_N − ε_{N−k})},   ε_j = E_j + 4j,   und ε_N − ε_{N−k} ≤ k μ̄.
Zusammen mit der Identität E[Π_{i∈A} 1/a_i] ≤ R_k(δ) folgt P(alle i ∈ A unzugänglich) ≤ (p* e^{δ μ̄})^k.
Ausgabe je System: E_N, ε-Differenzen, R_k(δ) und e^{δ(ε_N − ε_{N−k})} für mehrere δ.
Aufruf: python3 pruef_zugaenglich.py
"""
import itertools

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh, expm_multiply


def nachbarn(L):
    M = L * L
    x, y = np.arange(M) // L, np.arange(M) % L
    return np.stack([((x + dx) % L) * L + (y + dy) % L for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))], 1)


def boson_grund(L, N, nb):
    M = L * L
    T = list(itertools.combinations(range(M), N))
    idx = {t: i for i, t in enumerate(T)}
    r, c = [], []
    for i, t in enumerate(T):
        s = set(t)
        for p in t:
            for q in nb[p]:
                if q not in s:
                    u = tuple(sorted((s - {p}) | {q}))
                    r.append(i); c.append(idx[u])
    A = sp.coo_matrix((np.ones(len(r)), (r, c)), shape=(len(T),) * 2).tocsr()
    if len(T) == 1:
        return 0.0, np.ones(1), T
    w, v = eigsh(A, k=1, which='LA', tol=1e-13)
    psi = np.abs(v[:, 0])
    return -float(w[0]), psi / np.linalg.norm(psi), T


def markiert(L, N, k, nb, psiB, TB):
    """ψ_N als markierte symmetrische Funktion und H_rel mit den Teilchen 0..k−1 frei."""
    M = L * L
    zust = list(itertools.product(range(M), repeat=N))
    idx = {z: i for i, z in enumerate(zust)}
    psiidx = {t: i for i, t in enumerate(TB)}
    psi = np.zeros(len(zust))
    for i, z in enumerate(zust):
        if len(set(z)) == N:
            psi[i] = psiB[psiidx[tuple(sorted(z))]]
    psi /= np.linalg.norm(psi)
    r, c = [], []
    for i, z in enumerate(zust):
        for a in range(N):
            for q in nb[z[a]]:
                if a >= k and any(z[b] == q for b in range(k, N) if b != a):
                    continue
                u = list(z); u[a] = q
                r.append(i); c.append(idx[tuple(u)])
    A = sp.coo_matrix((np.ones(len(r)), (r, c)), shape=(len(zust),) * 2).tocsr()
    return psi, -A


def main():
    deltas = [0.5, 1, 2, 4, 8, 16, 32]
    print(f"{'L':>2} {'N':>2} {'k':>2} {'ε_N−ε_{N−k}':>12}   " + "  ".join(f"{'δ=' + str(d):>17}" for d in deltas))
    for L, N in ((4, 2), (4, 3), (5, 3), (6, 2), (6, 3)):
        nb = nachbarn(L)
        E = {}
        for j in range(0, N + 1):
            E[j] = boson_grund(L, j, nb)[0] if j > 0 else 0.0
        eps = {j: E[j] + 4 * j for j in E}
        _, psiB, TB = boson_grund(L, N, nb)
        for k in range(1, N):
            psi, Hrel = markiert(L, N, k, nb, psiB, TB)
            de = eps[N] - eps[N - k]
            zeile = []
            v = psi.copy(); t_alt = 0.0
            for d in deltas:
                v = expm_multiply(-(d - t_alt) * Hrel, v); t_alt = d
                R = np.exp(d * E[N]) * float(psi @ v)
                zeile.append(f"{R:8.4f} ≤ {np.exp(d * de):7.4f}" if R <= np.exp(d * de) * (1 + 1e-10)
                             else f"{R:8.4f} > {np.exp(d * de):7.4f}!")
            print(f"{L:2d} {N:2d} {k:2d} {de:12.5f}   " + "  ".join(zeile), flush=True)


if __name__ == '__main__':
    main()
