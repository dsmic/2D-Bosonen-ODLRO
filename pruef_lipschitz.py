#!/usr/bin/env python3
"""Lipschitz-Einschub auf dem Gitter (Satz T2, Schritt 4; satz_3_9_dichteschranken.md §10): exakte Prüfung.

Harte Bosonen auf (ℤ/Lℤ)², ℒ = 4N − A (Lemma 6.1, Grundenergie ε_N ≥ 0). Für eine Funktion a ≥ 0 auf den Plätzen sei
A = Σ_i a(x_i) (Multiplikator) und W₀(x) = 2a(x)/δ + Σ_{y∼x} (cosh(a(x) − a(y)) − 1).
Behauptung:  λ_max( e^A e^{−δℒ} e^A )  ≤  exp(−δ E₀(ℒ − Σ_i W₀(x_i))).
Geprüft für zufällige glatte a (Gauß-Hügel verschiedener Höhe und Breite) und mehrere δ.
Aufruf: python3 pruef_lipschitz.py
"""
import itertools

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh, expm_multiply


def sektor(L, N):
    M = L * L
    x, y = np.arange(M) // L, np.arange(M) % L
    nb = np.stack([((x + dx) % L) * L + (y + dy) % L for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))], 1)
    T = list(itertools.combinations(range(M), N))
    idx = {t: i for i, t in enumerate(T)}
    r, c = [], []
    for i, t in enumerate(T):
        s = set(t)
        for p in t:
            for q in nb[p]:
                if q not in s:
                    r.append(i); c.append(idx[tuple(sorted((s - {p}) | {q}))])
    A = sp.coo_matrix((np.ones(len(r)), (r, c)), shape=(len(T),) * 2).tocsr()
    return np.array(T), A, nb


def main():
    rng = np.random.default_rng(7)
    print(f"{'L':>2} {'N':>2} {'Höhe':>5} {'Breite':>6} {'δ':>5} {'λ_max(X)':>12} {'Schranke':>12} {'Verhältnis':>10}")
    for L, N in ((4, 2), (5, 2), (5, 3), (6, 2)):
        T, A, nb = sektor(L, N)
        Lop = 4 * N * sp.identity(T.shape[0]) - A
        M = L * L
        xs, ys = np.arange(M) // L, np.arange(M) % L
        for hoehe, breite in ((0.2, 1.0), (0.5, 1.5), (1.0, 2.0), (2.0, 1.0)):
            c0 = rng.integers(0, L, 2)
            dx = np.minimum(np.abs(xs - c0[0]), L - np.abs(xs - c0[0]))
            dy = np.minimum(np.abs(ys - c0[1]), L - np.abs(ys - c0[1]))
            a = hoehe * np.exp(-(dx ** 2 + dy ** 2) / (2 * breite ** 2))
            Ak = a[T].sum(1)
            for delta in (0.5, 2.0, 8.0):
                W0 = 2 * a / delta + np.array([sum(np.cosh(a[x] - a[y]) - 1 for y in nb[x]) for x in range(M)])
                Hw = Lop - sp.diags(W0[T].sum(1))
                E0 = eigsh(Hw, k=1, which='SA', tol=1e-12)[0][0]
                eA = np.exp(Ak)
                # λ_max(X) mit Potenzmethode über Lanczos auf dem symmetrischen Operator X v = e^A e^{−δℒ} e^A v
                from scipy.sparse.linalg import LinearOperator
                X = LinearOperator(Lop.shape, matvec=lambda v: eA * expm_multiply(-delta * Lop, eA * v), dtype=float)
                lam = eigsh(X, k=1, which='LA', tol=1e-10)[0][0]
                schranke = np.exp(-delta * E0)
                print(f"{L:2d} {N:2d} {hoehe:5.1f} {breite:6.1f} {delta:5.1f} {lam:12.6g} {schranke:12.6g} {lam / schranke:10.4f}",
                      flush=True)


if __name__ == '__main__':
    main()
