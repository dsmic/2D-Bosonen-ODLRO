#!/usr/bin/env python3
"""Prüft Lemma T1 (markiertes Teilchen) exakt: Im stationären Grundzustandsprozess harter Bosonen gilt für die
gelistete x-Verschiebung eines markierten Teilchens  E e^{θ Δx} ≤ e^{2δ(cosh θ − 1)}  (freie Irrfahrt, Rate 1 je Nachbar).
Markierte Fassung: N unterscheidbare Teilchen auf dem L×L-Torus, Sprung auf freie Nachbarplätze; Teilchen 0 trägt die
Gewichte e^{±θ} für Sprünge in ±x. E e^{θΔx} = e^{δE} <ψ, e^{−δ H_θ} ψ>.
Aufruf: python3 pruef_markiert.py
"""
import itertools

import numpy as np
from scipy.linalg import expm


def rechne(L, N, delta, thetas):
    M = L * L
    zust = [c for c in itertools.permutations(range(M), N)]
    idx = {c: i for i, c in enumerate(zust)}
    n = len(zust)

    def matrix(theta):
        Hm = np.zeros((n, n))
        for c in zust:
            belegt = set(c)
            for p in range(N):
                x, y = divmod(c[p], L)
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    q = ((x + dx) % L) * L + (y + dy) % L
                    if q in belegt:
                        continue
                    neu = list(c); neu[p] = q
                    w = np.exp(theta * dx) if p == 0 else 1.0
                    Hm[idx[c], idx[tuple(neu)]] -= w
        return Hm
    H0 = matrix(0.0)
    w, v = np.linalg.eigh(H0)
    E, psi = w[0], np.abs(v[:, 0])
    erg = []
    for th in thetas:
        wert = np.exp(delta * E) * psi @ expm(-delta * matrix(th)) @ psi
        frei = np.exp(2 * delta * (np.cosh(th) - 1))
        erg.append((th, wert, frei))
    return E, erg


for (L, N, delta) in ((4, 2, 1.0), (4, 3, 2.0), (5, 2, 3.0)):
    E, erg = rechne(L, N, delta, (0.25, 0.5, 1.0, 2.0))
    print(f"L={L} N={N} δ={delta}: E={E:.4f}")
    for th, wert, frei in erg:
        print(f"   θ={th:4.2f}:  E e^(θΔx) = {wert:.6f}   Schranke frei = {frei:.6f}   Verhältnis {wert / frei:.4f}")
