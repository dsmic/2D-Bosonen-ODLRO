#!/usr/bin/env python3
"""Eichung des zeitintegrierten Wurm-Histogramms hist_all gegen die exakte Duhamel-Suszeptibilität (harte Bosonen).

Exakt (großkanonisch, H = -sum (b^+b + h.c.) - mu N, endliches beta):
    chi(k) = beta (A_k^+, A_k)_Duhamel = (1/Z) sum_{n in N, m in N-1} |<m|A_k|n>|^2 (e^{-beta E_m} - e^{-beta E_n}) / (E_n - E_m),
A_k = M^{-1/2} sum_x e^{i k.x} b_x. Nur Zustände mit merklichem Boltzmann-Gewicht (einer der beiden) gehen ein.
Wurm: D(r) = hist_all[2 dx, 2 dy] / (Summe nZ * K); chi_W(k) = sum_r e^{-i k.r} D(r). K wird angepasst (Verhältnis).
Infrarotschranke (Duhamel, gilt bei jeder Temperatur, wenn reflexionspositiv): chi(k) E(k) <= 1, E(k) = 4 - 2 cos kx - 2 cos ky.
Aufruf: python3 pruef_chi.py L beta mu ergebnisse/bos_L4_b4_mu-2.3_s1 [weitere Läufe ...]
"""
import itertools
import json
import sys

import numpy as np
import scipy.sparse as sp

SCHNITT = 1e-14


def sektor(L, N):
    M = L * L
    konf = [sum(1 << i for i in c) for c in itertools.combinations(range(M), N)]
    idx = {c: i for i, c in enumerate(konf)}
    n = len(konf)
    zeilen, spalten = [], []
    for i, c in enumerate(konf):
        for s in range(M):
            for t in (((s % L + 1) % L) + L * (s // L), (s % L) + L * ((s // L + 1) % L)):
                if (c >> s & 1) != (c >> t & 1):
                    zeilen.append(i)
                    spalten.append(idx[c ^ (1 << s) ^ (1 << t)])
    H = sp.coo_matrix((-np.ones(len(zeilen)), (zeilen, spalten)), shape=(n, n)).toarray()
    return konf, idx, H


def main():
    L, beta, mu = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    M = L * L
    spek = {}
    for N in range(M + 1):
        konf, idx, H = sektor(L, N)
        E, V = np.linalg.eigh(H)
        spek[N] = (konf, idx, E - mu * N, V)
    emin = min(s[2].min() for s in spek.values())
    Z = sum(np.exp(-beta * (s[2] - emin)).sum() for s in spek.values())
    ks = [(2 * np.pi * a / L, 2 * np.pi * b / L) for a in range(L) for b in range(L)]
    chi = np.zeros(len(ks))
    for N in range(1, M + 1):
        konfN, idxN, EN, VN = spek[N]
        konfm, idxm, Em, Vm = spek[N - 1]
        wN = np.exp(-beta * (EN - emin))
        wm = np.exp(-beta * (Em - emin))
        if wN.max() < SCHNITT and wm.max() < SCHNITT:
            continue
        # b_x als Matrix N -> N-1
        bx = []
        for x in range(M):
            z, s_ = [], []
            for i, c in enumerate(konfN):
                if c >> x & 1:
                    z.append(idxm[c ^ (1 << x)])
                    s_.append(i)
            bx.append(sp.csr_matrix((np.ones(len(z)), (z, s_)), shape=(len(konfm), len(konfN))))
        # nur Paare (m, n), bei denen mindestens einer merkliches Gewicht hat
        nN = np.nonzero(wN > SCHNITT)[0]
        nm = np.nonzero(wm > SCHNITT)[0]
        rn = np.setdiff1d(np.arange(len(EN)), nN)

        def beitrag(T, Ea, Eb, wa, wb):          # T[m, n], Ea = E_m, Eb = E_n
            dE = Eb[None, :] - Ea[:, None]
            with np.errstate(divide='ignore', invalid='ignore'):
                f = (wa[:, None] - wb[None, :]) / dE
            nah = np.abs(dE) < 1e-10
            f[nah] = beta * wb[np.nonzero(nah)[1]]
            return float((np.abs(T) ** 2 * f).sum())
        for j, (kx, ky) in enumerate(ks):
            Ak = sum(np.exp(1j * (kx * (x % L) + ky * (x // L))) * bx[x] for x in range(M)) / np.sqrt(M)
            if len(nN):                                   # n mit Gewicht, alle m
                T1 = Vm.T @ (Ak @ VN[:, nN])
                chi[j] += beitrag(T1, Em, EN[nN], wm, wN[nN])
            if len(nm) and len(rn):                       # m mit Gewicht, n ohne Gewicht
                T2 = (Vm[:, nm].T @ Ak) @ VN[:, rn]
                chi[j] += beitrag(T2, Em[nm], EN[rn], wm[nm], wN[rn])
    chi /= Z
    E_k = np.array([4 - 2 * np.cos(kx) - 2 * np.cos(ky) for kx, ky in ks])
    print(f"exakt L={L} beta={beta} mu={mu}:")
    for (kx, ky), c, e in zip(ks, chi, E_k):
        print(f"  k = ({kx / np.pi:.2f}, {ky / np.pi:.2f}) pi: chi = {c:.5f}, chi*E = {c * e:.4f}")
    for lauf in sys.argv[4:]:
        d = json.load(open(lauf + '.json'))
        h = np.load(lauf + '.npz')['hist_all']
        nZ = float(np.sum(d['reihe']['nZ']))
        D = np.array([[h[(2 * dx) % (2 * L), (2 * dy) % (2 * L)] for dy in range(L)] for dx in range(L)]) / nZ
        chiW = np.array([sum(D[dx, dy] * np.cos(kx * dx + ky * dy) for dx in range(L) for dy in range(L))
                         for kx, ky in ks])
        K = chiW / chi
        print(f"{lauf}: K = chi_W/chi je k: Mittel {K.mean():.5f}, Streuung {K.std() / K.mean():.4f} (relativ); "
              f"Cw M beta = {1 / 10:.5f} (Cw = 1/(10 M beta))")


if __name__ == '__main__':
    main()
