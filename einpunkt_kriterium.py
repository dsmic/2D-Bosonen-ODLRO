#!/usr/bin/env python
"""Einpunkt-Kriterium: Affinität zwischen Faser (Bad um ein Teilchen bei x) und (N-1)-Grundzustand, exakt.

u = b_0 psi_N (b_0 = M^(-1/2) sum_x b_x), n_0 = |u|^2 (k = 0-Besetzung),
<psi_{N-1}, u> = sqrt(N) * Hq,   Hq = sum_{S not 0} psi_{N-1}(S) psi_N(S+0) / sqrt(rho)  (Bhattacharyya-Affinität).
Streng: n_0/N >= Hq^2 (Cauchy-Schwarz). Z0 = N Hq^2 / n_0 = Quasiteilchengewicht bei k = 0.
Modelle wie in z2/zweipaar_graph/falk_bruch.py: bosonen (2D), bosonen1d, stufe_a (Paare).
Aufruf: python einpunkt_kriterium.py --modell bosonen1d --L 8 12 16 --rho 0.25
        python einpunkt_kriterium.py --modell bosonen --L 4 --N 2 3 4
"""
import argparse
import json
import os
import sys
import time

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import eigsh

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "z2", "zweipaar_graph"))
import falk_bruch as fb  # noqa: E402


def perron(H):
    """Grundzustand (positiv) auf der größten Zusammenhangskomponente."""
    if H.shape[0] == 1:
        return np.ones(1)
    A = -H
    _, lab = connected_components(A, directed=False)
    haupt = np.nonzero(lab == np.argmax(np.bincount(lab)))[0]
    _, v = eigsh(A[haupt][:, haupt], k=1, which="LA", tol=1e-12)
    psi = np.zeros(H.shape[0])
    psi[haupt] = np.abs(v[:, 0]) / np.linalg.norm(v[:, 0])
    return psi


def rechne(modell, L, N):
    t0 = time.perf_counter()
    kompat, ziel, *_ = fb.geometrie(modell, L)
    M = kompat.shape[0]
    S = {q: fb.Sektor(q, kompat, ziel) for q in (N - 1, N)}
    psi, phi = perron(S[N].H), perron(S[N - 1].H)
    ab = fb.entfernen(S[N], S[N - 1], M)
    u = np.bincount(ab.ravel(), weights=np.repeat(psi, N), minlength=S[N - 1].n) / np.sqrt(M)
    n0 = float(u @ u)
    ov = float(phi @ u)
    Hq2 = ov ** 2 / N
    erg = dict(modell=modell, L=L, M=M, N=N, rho=N / M, n0_durch_N=n0 / N, Hq2=Hq2, Z0=ov ** 2 / n0,
               dim=S[N].n, zeit_s=time.perf_counter() - t0)
    print(f"{modell:9s} L={L:3d} N={N:3d} rho={N / M:.4f}  n0/N={n0 / N:.5f}  Hq^2={Hq2:.5f}  "
          f"Z0={ov ** 2 / n0:.5f}  [dim {S[N].n}, {erg['zeit_s']:.0f} s]", flush=True)
    return erg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modell", choices=["bosonen", "bosonen1d", "stufe_a"], default="bosonen")
    ap.add_argument("--L", type=int, nargs="+", default=[4])
    ap.add_argument("--N", type=int, nargs="*", default=[])
    ap.add_argument("--rho", type=float, default=None, help="statt --N: N = rho * M je L")
    ap.add_argument("--aus", default=None)
    a = ap.parse_args()
    alle = []
    for L in a.L:
        M = L * L if a.modell == "bosonen" else (L if a.modell == "bosonen1d" else 2 * L * L)
        Ns = [int(round(a.rho * M))] if a.rho is not None else a.N
        alle += [rechne(a.modell, L, N) for N in Ns]
    if a.aus:
        os.makedirs(os.path.join(HIER, "ergebnisse"), exist_ok=True)
        with open(os.path.join(HIER, "ergebnisse", a.aus), "w") as fh:
            json.dump(alle, fh, indent=1)


if __name__ == "__main__":
    main()
