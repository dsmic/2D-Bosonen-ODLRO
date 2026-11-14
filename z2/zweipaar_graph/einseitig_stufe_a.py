#!/usr/bin/env python
"""Einseitige Ungleichungen (I), (II) für Stufe A (Paare auf dem Mittelgitter), exakt auf dem L x L-Torus.

Kanonisch: psi = Grundzustand mit P Paaren (Hauptkomponente, d-Eichung), A_k = (2N)^(-1/2) sum_b e^{ik.m_b} a_b,
    n_k = |A_k psi|^2,  c^-(k) = <A psi|(H_{P-1} - E0(P-1))|A psi>,  chi^-(k) = <A psi|(H_{P-1} - E0(P-1))^-1|A psi>
(k != 0; A_k psi steht senkrecht auf dem (P-1)-Grundzustand). Freie Paardispersion E(k) = 4 - 4 cos(kx/2) cos(ky/2).
(I)  chi^- E <= rho_b,   (II) c^- <= C rho_b,  Kette n_0/P >= 1 - sqrt(C) J_A,  J_A = Mittel von E^(-1/2) über die
Brillouin-Zone des Mittelgitters. Nur die Entfernungsseite wird gebraucht (Sektoren P und P-1).
Aufruf: python einseitig_stufe_a.py --L 8 --P 2 3 4
"""
import argparse
import json
import os
import time

import numpy as np
import pyamg
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import cg, eigsh

import falk_bruch as fb

HIER = os.path.dirname(os.path.abspath(__file__))


def J_A(n=2000):
    kx = (np.arange(2 * n) + 0.5) * 4 * np.pi / (2 * n)
    ky = (np.arange(n) + 0.5) * 2 * np.pi / n
    KX, KY = np.meshgrid(kx, ky, indexing="ij")
    E = 4 - 4 * np.cos(KX / 2) * np.cos(KY / 2)
    return float(np.mean(1 / np.sqrt(E)))


def rechne(L, P):
    t0 = time.perf_counter()
    kompat, ziel, rx, ry, kgitter = fb.geometrie("stufe_a", L)
    M = kompat.shape[0]
    S = {q: fb.Sektor(q, kompat, ziel) for q in (P - 1, P)}
    # Grundzustand im Sektor P auf der Hauptkomponente
    A = -S[P].H
    nc, lab = connected_components(A, directed=False)
    haupt = np.nonzero(lab == np.argmax(np.bincount(lab)))[0]
    w, v = eigsh(A[haupt][:, haupt], k=1, which="LA", tol=1e-12)
    psi = np.zeros(S[P].n)
    psi[haupt] = np.abs(v[:, 0]) / np.linalg.norm(v[:, 0])
    # (P-1)-Sektor: Grundzustand für die Projektion
    if S[P - 1].n > 1:
        A1 = -S[P - 1].H
        w1, v1 = eigsh(A1, k=1, which="LA", tol=1e-12)
        E0m, phi0 = -float(w1[0]), np.abs(v1[:, 0])
        Mm = (S[P - 1].H - (E0m - 1e-9) * sp.identity(S[P - 1].n)).tocsr()
        ml = pyamg.smoothed_aggregation_solver(Mm, symmetry="symmetric")
    ab = fb.entfernen(S[P], S[P - 1], M)
    nrm = 1.0 / np.sqrt(M)
    rho = P / M
    erg = []
    for (kx, ky) in kgitter:
        ph = np.exp(1j * (kx * rx[S[P].T] + ky * ry[S[P].T])) * psi[:, None]
        u = nrm * (np.bincount(ab.ravel(), weights=ph.real.ravel(), minlength=S[P - 1].n)
                   + 1j * np.bincount(ab.ravel(), weights=ph.imag.ravel(), minlength=S[P - 1].n))
        nk = float(np.vdot(u, u).real)
        E = 4 - 4 * np.cos(kx / 2) * np.cos(ky / 2)
        if E < 1e-12 or S[P - 1].n == 1:
            erg.append((kx, ky, E, nk, np.nan, np.nan))
            continue
        u = u - phi0 * np.vdot(phi0, u)                    # Projektion (k != 0: ohnehin ~0)
        cm = float(np.vdot(u, Mm @ u).real)
        chim = 0.0
        for teil in (u.real, u.imag):
            if np.any(teil):
                x, _ = cg(Mm, teil, rtol=1e-10, atol=0.0, M=ml.aspreconditioner(), maxiter=3000)
                chim += float(teil @ x)
        erg.append((kx, ky, E, nk, cm, chim))
    a = np.array(erg)
    nz = a[:, 2] > 1e-12
    E, nk, cm, chim = a[nz, 2], a[nz, 3], a[nz, 4], a[nz, 5]
    n0 = a[~nz, 3][0]
    ein = np.sqrt(cm * chim)
    r1 = chim * E / rho
    C = cm.max() / rho
    J = J_A()
    out = dict(L=L, P=P, rho_b=rho, n0_durch_P=float(n0 / P), max_chiE_durch_rho=float(r1.max()),
               C=float(C), J_A=J, kette_C=float(1 - np.sqrt(C) * J),
               einseitig_endlich=float((P - ein.sum()) / P), zeit_s=time.perf_counter() - t0)
    print(f"Stufe A L={L} P={P} (rho_b = {rho:.4f}): n0/P = {n0 / P:.4f}; (I) max chi-E/rho = {r1.max():.3f}; "
          f"(II) C = max c-/rho = {C:.3f}; J_A = {J:.4f}; Kette 1 - sqrt(C) J = {1 - np.sqrt(C) * J:+.3f} "
          f"(nötig C < {1 / J ** 2:.2f}); endlich mit exakten c-, chi-: n0/P >= {(P - ein.sum()) / P:.4f}  "
          f"[{time.perf_counter() - t0:.0f} s]", flush=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", type=int, default=8)
    ap.add_argument("--P", type=int, nargs="+", default=[2, 3, 4])
    a = ap.parse_args()
    alle = [rechne(a.L, P) for P in a.P]
    with open(os.path.join(HIER, "ergebnisse", f"einseitig_stufe_a_L{a.L}.json"), "w") as fh:
        json.dump(alle, fh, indent=1)


if __name__ == "__main__":
    main()
