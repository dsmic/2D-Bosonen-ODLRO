#!/usr/bin/env python3
"""Musterlösungen zu den Rechenübungen in tutorial_beweis_verduennt.md (eigenständig, nur numpy/scipy).

Harte Bosonen auf dem L x L-Torus, H = -A (A = Adjazenz des Konfigurationsgraphen, ein Teilchen springt
zu einem freien Nachbarplatz). Basis: alle N-Teilmengen des Gitters, sortiert.

  Ü 2.1  N0/N, Hq^2 und Z0 = N Hq^2 / N0 für kleine Systeme
  Ü 3.3  G(tau) aus der Spektralzerlegung: vollständig monoton, G(0) = N0, G(inf) = N Hq^2
  Ü 6.3  Einfügeschranke mit f = 1 - delta_0 gegen exakte Einfügeenergien eps_k - eps_{k-1}
  Ü 6.4  eps_j / j nichtfallend

Aufruf: python3 tutorial_uebungen.py
"""
import itertools

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh


def gitter(L):
    M = L * L
    x, y = np.arange(M) // L, np.arange(M) % L
    nb = np.stack([((x + dx) % L) * L + (y + dy) % L for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))], 1)
    return M, nb


def sektor(L, N):
    """Basis (Zeilen = sortierte Platzlisten) und H = -A als dünne Matrix."""
    M, nb = gitter(L)
    T = np.array(list(itertools.combinations(range(M), N)), dtype=np.int64).reshape(-1, N)
    if N == 0:
        return T, sp.csr_matrix((1, 1))
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
    H = -sp.coo_matrix((np.ones(src.size), (src, dst)), shape=(T.shape[0],) * 2).tocsr()
    return T, H


def grundzustand(H):
    if H.shape[0] <= 2:
        w, v = np.linalg.eigh(H.toarray())
        return w[0], np.abs(v[:, 0])
    w, v = eigsh(-H, k=1, which='LA', tol=1e-13)
    return -w[0], np.abs(v[:, 0]) / np.linalg.norm(v[:, 0])


def b0(L, TN, psi, TN1):
    """u = b_0 psi_N mit b_0 = M^{-1/2} sum_x b_x, als Vektor im (N-1)-Sektor."""
    M = L * L
    N = TN.shape[1]
    basis = M ** np.arange(N - 1)[::-1]
    keys = TN1 @ basis
    u = np.zeros(TN1.shape[0])
    for p in range(N):
        rest = np.delete(TN, p, axis=1)
        u += np.bincount(np.searchsorted(keys, rest @ basis), weights=psi, minlength=TN1.shape[0])
    return u / np.sqrt(M)


def uebung_2_1():
    print("Ü 2.1: Einpunkt-Kriterium N0/N >= Hq^2")
    for L, N in ((3, 2), (4, 2), (4, 3), (4, 4), (5, 3)):
        TN, HN = sektor(L, N)
        TN1, HN1 = sektor(L, N - 1)
        _, psi = grundzustand(HN)
        _, phi = grundzustand(HN1)
        u = b0(L, TN, psi, TN1)
        N0 = u @ u
        Hq2 = (phi @ u) ** 2 / N
        print(f"  L={L} N={N} rho={N / L**2:.4f}:  N0/N = {N0 / N:.5f}   Hq^2 = {Hq2:.5f}   Z0 = {N * Hq2 / N0:.5f}")


def uebung_3_1(L=4, N=3):
    print(f"Ü 3.3: G(tau) für L={L}, N={N}")
    TN, HN = sektor(L, N)
    TN1, HN1 = sektor(L, N - 1)
    _, psi = grundzustand(HN)
    u = b0(L, TN, psi, TN1)
    w, V = np.linalg.eigh(HN1.toarray())
    c2 = (V.T @ u) ** 2
    for tau in (0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0):
        G = np.sum(c2 * np.exp(-tau * (w - w[0])))
        print(f"  tau = {tau:5.2f}:  G = {G:.5f}")
    print(f"  tau = inf  :  G = {c2[0]:.5f}  (= N Hq^2)")
    gross = np.argsort(-c2)[:4]
    print("  größte Gewichte |<n|b0 psi_N>|^2 und Anregungsenergien E_n - E_0:",
          ", ".join(f"{c2[i]:.4f} @ {w[i] - w[0]:.4f}" for i in gross))


def uebung_6_3_6_4(L=6, Nmax=5):
    print(f"Ü 6.3/6.4: Einfügeenergien und eps_j/j auf {L}x{L}")
    M = L * L
    eps = [0.0]
    for N in range(1, Nmax + 1):
        _, H = sektor(L, N)
        E, _ = grundzustand(H)
        eps.append(E + 4 * N)
    for k in range(1, Nmax + 1):
        rho_s = (k - 1) / M
        schranke = 8 * rho_s / (1 - rho_s)
        q = f"{eps[k] / k:.5f}" if k > 0 else "-"
        print(f"  k={k}: eps_k = {eps[k]:.5f}   eps_k - eps_(k-1) = {eps[k] - eps[k - 1]:.5f}   "
              f"Schranke 8 rho'/(1 - rho') = {schranke:.5f}   eps_k/k = {q}")


if __name__ == '__main__':
    uebung_2_1()
    uebung_3_1()
    uebung_6_3_6_4()
