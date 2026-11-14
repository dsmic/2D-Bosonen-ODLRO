#!/usr/bin/env python3
"""Numerische Prüfung der umgekehrten Hölder-Ungleichung für den Einfügequotienten (Anhang G.8.4, Weg c).

u_a(η) = φ_a(η)/ψ_{N+1}(η),  φ_a = a*(1_a) ψ_N,  also φ_a(η) = Σ_{x ∈ a∩η} ψ_N(η \\ x),  für (N+1)-Konfigurationen η.
Normen unter ψ_{N+1}²:  ‖u‖_p^p = Σ_η φ_a(η)^p ψ_{N+1}(η)^{2−p},   ‖u‖_2 = ‖φ_a‖.
Vergleich: Gleichverteilung (ψ konstant, RK-Punkt ohne Korrelationen), dort ist u_a ∝ n_a(η).
Ausgabe: R_p = ‖u‖_p/‖u‖_2 (p = 3, 4), dasselbe für die Gleichverteilung, max u/‖u‖_2, und das Gewicht großer u.
Aufruf: python3 pruef_einfuegequotient.py
"""
import itertools
import json
import os
import time

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

HIER = os.path.dirname(os.path.abspath(__file__))


def sektor(L, N):
    M = L * L
    x, y = np.arange(M) // L, np.arange(M) % L
    nb = np.stack([((x + dx) % L) * L + (y + dy) % L for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))], 1)
    T = np.array(list(itertools.combinations(range(M), N)), dtype=np.int64)
    basis = M ** np.arange(N)[::-1]
    keys = T @ basis
    src, dst = [], []
    for p in range(N):
        for d in range(4):
            neu = nb[T[:, p], d]
            ok = np.ones(T.shape[0], dtype=bool)
            for q in range(N):
                if q != p:
                    ok &= neu != T[:, q]
            idx = np.nonzero(ok)[0]
            Tn = T[idx].copy()
            Tn[:, p] = neu[idx]
            Tn.sort(axis=1)
            src.append(idx)
            dst.append(np.searchsorted(keys, Tn @ basis))
    src, dst = np.concatenate(src), np.concatenate(dst)
    A = sp.coo_matrix((np.ones(src.size), (src, dst)), shape=(T.shape[0],) * 2).tocsr()
    return T, keys, A


def grundzustand(A):
    w, v = eigsh(A, k=1, which='LA', tol=1e-12)
    psi = np.abs(v[:, 0])
    return psi / np.linalg.norm(psi)


def phi_a(L, TN1, TN, keysN, psiN, zelle):
    M = L * L
    N = TN.shape[1]
    basis = M ** np.arange(N)[::-1]
    phi = np.zeros(TN1.shape[0])
    inzelle = np.zeros(M, dtype=bool); inzelle[list(zelle)] = True
    for p in range(N + 1):
        rest = np.delete(TN1, p, axis=1)
        mask = inzelle[TN1[:, p]]
        idx = np.searchsorted(keysN, rest[mask] @ basis)
        phi[mask] += psiN[idx]
    return phi


def kennzahlen(phi, psi):
    u = np.where(psi > 0, phi / np.maximum(psi, 1e-300), 0.0)
    w = psi ** 2
    n2 = np.sqrt(np.sum(w * u ** 2))
    r3 = np.sum(w * u ** 3) ** (1 / 3) / n2
    r4 = np.sum(w * u ** 4) ** (1 / 4) / n2
    mx = u.max() / n2
    gross = np.sum(w[u > 3 * n2] * u[u > 3 * n2] ** 2) / n2 ** 2      # Anteil der L²-Masse bei u > 3‖u‖₂
    return r3, r4, mx, gross


def main():
    faelle = [(6, 3, 2), (6, 3, 3), (6, 4, 2), (6, 4, 3), (7, 3, 2), (7, 3, 3), (8, 2, 2), (8, 2, 4), (8, 3, 2), (8, 3, 4)]
    erg = []
    for (L, N, s) in faelle:
        t0 = time.time()
        TN, keysN, AN = sektor(L, N)
        TN1, keysN1, AN1 = sektor(L, N + 1)
        psiN, psiN1 = grundzustand(AN), grundzustand(AN1)
        zelle = [i * L + j for i in range(s) for j in range(s)]
        phi = phi_a(L, TN1, TN, keysN, psiN, zelle)
        r3, r4, mx, gross = kennzahlen(phi, psiN1)
        # Gleichverteilung als Vergleich
        psiN_u = np.full(TN.shape[0], 1 / np.sqrt(TN.shape[0]))
        psiN1_u = np.full(TN1.shape[0], 1 / np.sqrt(TN1.shape[0]))
        phi_u = phi_a(L, TN1, TN, keysN, psiN_u, zelle)
        r3u, r4u, mxu, grossu = kennzahlen(phi_u, psiN1_u)
        rho = (N + 1) / (L * L)
        m = rho * s * s
        e = dict(L=L, N=N, s=s, rho=rho, m=m, R3=r3, R4=r4, max=mx, gross=gross, R3_gleich=r3u, R4_gleich=r4u,
                 max_gleich=mxu, norm2=float(np.linalg.norm(phi)), schranke_2s2m=float(np.sqrt(2 * s * s * max(m, 1))))
        erg.append(e)
        print(f"L={L} N={N}→{N + 1} s={s} (ρ={rho:.3f}, m={m:.2f}):  R3={r3:.3f} R4={r4:.3f} max={mx:.2f} "
              f"L²-Anteil(u>3‖u‖)={gross:.4f}   | gleichverteilt: R3={r3u:.3f} R4={r4u:.3f} max={mxu:.2f}   "
              f"‖φ‖={e['norm2']:.3f} ≤ √(2s²m)={e['schranke_2s2m']:.3f}  [{time.time() - t0:.0f} s]", flush=True)
    with open(os.path.join(HIER, 'ergebnisse', 'pruef_einfuegequotient.json'), 'w') as fh:
        json.dump(erg, fh, indent=1)


if __name__ == '__main__':
    main()
