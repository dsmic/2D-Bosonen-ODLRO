#!/usr/bin/env python3
"""L1d numerisch: exakte Jastrow-Einfügeschranke für das chemische Potential (einpunkt_zeitroute.md §16.2).

Alte Teilchen im exakten Grundzustand psi_{k-1}, neues markiertes Teilchen gleichverteilt: Psi0 = psi (x) 1/sqrt(M),
Eigenvektor des Operators ohne neu-alt-Ausschluss zum Eigenwert E_{k-1} - 4. Mit F = prod_j f(x_neu - x_j), f(0) = 0:
    mu + 4 <= sum_{Kanten} Psi0 Psi0' (F - F')^2 / <Psi0, F^2 Psi0>        (Kippidentität, exakt)
Kanten: Sprünge des neuen Teilchens (auch auf alte Plätze, dort F = 0) und Sprünge alter Teilchen (auch auf den Platz
des neuen). Markierte Versuchszustände sind erlaubt: der markierte Grundzustand mit hartem Kern ist positiv, also
symmetrisch, also der bosonische. Profile: Born (f = 1 außer 0), f_R = min(1, a(x)/a(R)) mit dem Potentialkern a der
2D-Irrfahrt (unendliches Gitter, Mindestbild-Abstand), und das beste Paarprofil (Optimierung über Abstandsklassen).
Aufruf: python3 l1d_einfuegen.py --L 6 --k 3 4 5 6
"""
import argparse
import json
import os
import sys
import time

import numpy as np
from scipy.optimize import minimize
from scipy.sparse.linalg import eigsh

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "z2", "zweipaar_graph"))
import falk_bruch as fb  # noqa: E402
from einpunkt_kriterium import perron  # noqa: E402


def potentialkern(xmax, n=1200):
    """a(x) = (2 pi)^-2 int (1 - cos k.x) / (1 - (cos k1 + cos k2)/2) dk  für 0 <= x1, x2 <= xmax."""
    k = (np.arange(n) + 0.5) * 2 * np.pi / n - np.pi
    K1, K2 = np.meshgrid(k, k, indexing="ij")
    nenner = 1 - (np.cos(K1) + np.cos(K2)) / 2
    a = np.zeros((xmax + 1, xmax + 1))
    for i in range(xmax + 1):
        for j in range(xmax + 1):
            a[i, j] = np.mean((1 - np.cos(K1 * i + K2 * j)) / nenner)
    return a


def grundenergie(S):
    if S.n == 1:
        return 0.0
    return -float(eigsh(-S.H, k=1, which="LA", tol=1e-12, return_eigenvectors=False)[0])


def rechne(L, k, a_kern):
    t0 = time.perf_counter()
    kompat, ziel, *_ = fb.geometrie("bosonen", L)
    M = L * L
    Salt = fb.Sektor(k - 1, kompat, ziel)
    Sneu = fb.Sektor(k, kompat, ziel)
    psi = perron(Salt.H)
    E_alt = float(psi @ (Salt.H @ psi))
    E_neu = grundenergie(Sneu)
    mu_wahr = E_neu - E_alt
    T = Salt.T                                            # (n, k-1) Plätze
    n = Salt.n
    x, y = np.arange(M) // L, np.arange(M) % L
    dx = np.abs((x[:, None] - x[None, :] + L // 2) % L - L // 2)
    dy = np.abs((y[:, None] - y[None, :] + L // 2) % L - L // 2)
    klasse = dx * (L + 1) + dy                            # Abstandsklasse (|dx|, |dy|), symmetrisch genug
    klassen, kl_idx = np.unique(np.minimum(dx, dy) * (L + 1) + np.maximum(dx, dy), return_inverse=True)
    kl_idx = kl_idx.reshape(M, M)
    # Sprünge alter Teilchen: Zielkonfigurationen (Index) je (i, p, d)
    alt_ziel = []
    for p in range(k - 1):
        for d in range(ziel.shape[1]):
            neu = ziel[T[:, p], d]
            ok = np.ones(n, bool)
            for q in range(k - 1):
                if q != p:
                    ok &= neu != T[:, q]
            idx = np.nonzero(ok)[0]
            Tn = T[idx].copy()
            Tn[:, p] = neu[idx]
            Tn.sort(axis=1)
            alt_ziel.append((idx, np.searchsorted(Salt.keys, fb.s8.schluessel(Tn, M))))
    w = psi ** 2 / M

    def schranke(fkl):
        fmat = fkl[kl_idx]                                # f(x - y), x neu, y alt
        F = np.ones((n, M))
        for p in range(k - 1):
            F *= fmat[:, T[:, p]].T                       # (n, M)
        nenner = float(np.sum(w[:, None] * F ** 2))
        zz = 0.0
        for d in range(ziel.shape[1]):                    # neues Teilchen springt x -> ziel[x, d]
            zz += np.sum(w[:, None] * (F - F[:, ziel[:, d]]) ** 2)
        zz *= 0.5
        za = 0.0
        for idx, jdx in alt_ziel:                         # alte Sprünge i -> j, neues fest
            za += np.sum((psi[idx] * psi[jdx] / M)[:, None] * (F[idx] - F[jdx]) ** 2)
        za *= 0.5
        return (zz + za) / nenner

    # Profile
    ab = np.array([[min(c // (L + 1), c % (L + 1)), max(c // (L + 1), c % (L + 1))] for c in klassen])
    a_werte = a_kern[ab[:, 0], ab[:, 1]]
    f_born = (a_werte > 0).astype(float)
    erg = dict(L=L, k=k, rho=k / M, mu_wahr_plus4=mu_wahr + 4, born=schranke(f_born))
    for R in (1.0, 1.5, 2.0, 3.0, 4.0):
        aR = (2 / np.pi) * (np.log(R) + np.euler_gamma + 1.5 * np.log(2)) if R > 1 else 1.0
        erg[f"R{R:g}"] = schranke(np.minimum(1.0, a_werte / aR))
    # bestes Paarprofil: f(0) = 0 fest, übrige Klassen frei in [0, 1]
    frei = np.nonzero(a_werte > 0)[0]
    x0 = np.minimum(1.0, a_werte[frei] / a_werte.max())

    def ziel_f(v):
        f = np.zeros(len(klassen))
        f[frei] = v
        return schranke(f)
    opt = minimize(ziel_f, x0, method="L-BFGS-B", bounds=[(0.0, 1.0)] * len(frei), options=dict(maxiter=200))
    erg["opt"] = float(opt.fun)
    erg["f_opt"] = {f"{tuple(ab[i])}": float(v) for i, v in zip(frei, opt.x)}
    erg["zeit_s"] = time.perf_counter() - t0
    print(f"L={L} k={k} rho={k / M:.3f}: mu+4 wahr {erg['mu_wahr_plus4']:.4f} | Born {erg['born']:.4f} | "
          + " ".join(f"R={R:g}: {erg[f'R{R:g}']:.4f}" for R in (1.0, 1.5, 2.0, 3.0, 4.0))
          + f" | bestes Paarprofil {erg['opt']:.4f}  [{erg['zeit_s']:.0f} s]", flush=True)
    return erg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", type=int, default=6)
    ap.add_argument("--k", type=int, nargs="+", default=[2, 3, 4, 5])
    a = ap.parse_args()
    a_kern = potentialkern(a.L)
    print("Potentialkern a(1,0) =", round(a_kern[1, 0], 6), " a(2,0) =", round(a_kern[2, 0], 6),
          " (Asymptotik (2/pi)(ln r + gamma + 1.5 ln 2) bei r=2:", round(2 / np.pi * (np.log(2) + np.euler_gamma + 1.5 * np.log(2)), 6), ")")
    alle = [rechne(a.L, k, a_kern) for k in a.k]
    with open(os.path.join(HIER, "ergebnisse", f"l1d_L{a.L}.json"), "w") as fh:
        json.dump(alle, fh, indent=1)


if __name__ == "__main__":
    main()
