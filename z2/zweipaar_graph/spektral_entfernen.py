#!/usr/bin/env python
"""Spektrum nach dem Herausnehmen eines Teilchens mit Impuls k: Quasiteilchen oder Kontinuum?

psi_N = Grundzustand (N Teilchen bzw. Paare), u_k = A_k psi_N (Sektor N-1). Lanczos mit H_{N-1} - E0(N-1), Start u_k:
    eps_min(k) = niedrigste Ritz-Energie mit Gewicht > 1e-4 des Gewichts n_k,
    Z(k)       = Gewicht dieser Energie / n_k   (Quasiteilchengewicht),
    eps_h(k)   = n_k / chi^-(k)                 (harmonisches Mittel; steuert chi^-),
    eps_a(k)   = c^-(k) / n_k                   (arithmetisches Mittel),
jeweils relativ zur freien Dispersion E(k). Ungleichung (I) chi^- E <= rho heißt (n_k/rho) * E/eps_h <= 1.
Modelle: bosonen (2D), bosonen1d, stufe_a (Paare, Mittelgitter, E = 4 - 4 cos(kx/2) cos(ky/2)).
Aufruf: python spektral_entfernen.py --modell bosonen --L 6 --N 3
"""
import argparse
import json
import os
import time

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import eigsh

import falk_bruch as fb

HIER = os.path.dirname(os.path.abspath(__file__))


def freie_dispersion(modell, kx, ky):
    if modell == "bosonen":
        return 4 - 2 * np.cos(kx) - 2 * np.cos(ky)
    if modell == "bosonen1d":
        return 2 - 2 * np.cos(kx)
    return 4 - 4 * np.cos(kx / 2) * np.cos(ky / 2)


def lanczos(H, v0, schritte=120):
    """Ritz-Werte und Gewichte |<Ritz|v0>|^2 (normiert auf |v0|^2) mit voller Reorthogonalisierung."""
    n0 = np.linalg.norm(v0)
    V = [v0 / n0]
    a, b = [], []
    for j in range(schritte):
        w = H @ V[-1]
        aj = np.vdot(V[-1], w).real
        w = w - aj * V[-1] - (b[-1] * V[-2] if j > 0 else 0)
        for q in V:                                   # volle Reorthogonalisierung
            w = w - np.vdot(q, w) * q
        a.append(aj)
        bj = np.linalg.norm(w)
        if bj < 1e-10 or j == schritte - 1:
            break
        b.append(bj)
        V.append(w / bj)
    T = np.diag(a) + np.diag(b[:len(a) - 1], 1) + np.diag(b[:len(a) - 1], -1)
    th, S = np.linalg.eigh(T)
    return th, n0 ** 2 * np.abs(S[0, :]) ** 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modell", choices=["bosonen", "bosonen1d", "stufe_a"], default="bosonen")
    ap.add_argument("--L", type=int, default=4)
    ap.add_argument("--N", type=int, default=2)
    a = ap.parse_args()
    t0 = time.perf_counter()
    kompat, ziel, rx, ry, kgitter = fb.geometrie(a.modell, a.L)
    M = kompat.shape[0]
    N = a.N
    S = {q: fb.Sektor(q, kompat, ziel) for q in (N - 1, N)}
    A = -S[N].H
    nc, lab = connected_components(A, directed=False)
    haupt = np.nonzero(lab == np.argmax(np.bincount(lab)))[0]
    w, v = eigsh(A[haupt][:, haupt], k=1, which="LA", tol=1e-12)
    psi = np.zeros(S[N].n)
    psi[haupt] = np.abs(v[:, 0]) / np.linalg.norm(v[:, 0])
    Hm = S[N - 1].H
    E0m = -float(eigsh(-Hm, k=1, which="LA", tol=1e-12, return_eigenvectors=False)[0]) if S[N - 1].n > 1 else 0.0
    ab = fb.entfernen(S[N], S[N - 1], M)
    rho = N / M
    zeilen = []
    gesehen = set()
    for kx, ky in kgitter:
        E = freie_dispersion(a.modell, kx, ky)
        if E < 1e-12:
            continue
        schl = round(E, 9)
        ph = np.exp(1j * (kx * rx[S[N].T] + ky * ry[S[N].T])) * psi[:, None]
        u = (np.bincount(ab.ravel(), weights=ph.real.ravel(), minlength=S[N - 1].n)
             + 1j * np.bincount(ab.ravel(), weights=ph.imag.ravel(), minlength=S[N - 1].n)) / np.sqrt(M)
        nk = float(np.vdot(u, u).real)
        if nk < 1e-14:
            continue
        Hs = (Hm - E0m * fb.sp.identity(S[N - 1].n)).tocsr()
        th, gw = lanczos(Hs, u)
        rel = gw > 1e-4 * nk
        j = np.argmin(np.where(rel, th, np.inf))
        eps_min, Z = float(th[j]), float(gw[j] / nk)
        pos = th > 1e-9
        chim = float(np.sum(gw[pos] / th[pos]))
        cm = float(np.sum(gw * th))
        zeilen.append(dict(kx=kx, ky=ky, E=float(E), n_k=nk, eps_min=eps_min, Z=Z, eps_h=nk / chim, eps_a=cm / nk,
                           I_verh=chim * E / rho))
        gesehen.add(schl)
    z = zeilen
    em = np.array([x["eps_min"] / x["E"] for x in z])
    eh = np.array([x["eps_h"] / x["E"] for x in z])
    Zs = np.array([x["Z"] for x in z])
    I = np.array([x["I_verh"] for x in z])
    nr = np.array([x["n_k"] / rho for x in z])
    print(f"{a.modell} L={a.L} N={N} (rho={rho:.4f}): eps_min/E in [{em.min():.3f}, {em.max():.3f}], "
          f"eps_h/E in [{eh.min():.3f}, {eh.max():.3f}], Z in [{Zs.min():.3f}, {Zs.max():.3f}], "
          f"n_k/rho max {nr.max():.3f}, (I) max chi-E/rho {I.max():.3f}  [{time.perf_counter() - t0:.0f} s]", flush=True)
    # Verlauf längs einer Richtung: k entlang x
    weg = sorted([x for x in z if abs(x["ky"]) < 1e-12], key=lambda x: x["kx"])
    if weg:
        print("   k_x/pi:   " + "  ".join(f"{x['kx'] / np.pi:5.2f}" for x in weg))
        print("   eps_min/E " + "  ".join(f"{x['eps_min'] / x['E']:5.2f}" for x in weg))
        print("   Z         " + "  ".join(f"{x['Z']:5.2f}" for x in weg))
        print("   n_k/rho   " + "  ".join(f"{x['n_k'] / rho:5.2f}" for x in weg))
    with open(os.path.join(HIER, "ergebnisse", "einseitig", f"spektral_{a.modell}_L{a.L}_N{N}.json"), "w") as fh:
        json.dump(dict(modell=a.modell, L=a.L, N=N, rho=rho, k=zeilen), fh, indent=1)


if __name__ == "__main__":
    main()
