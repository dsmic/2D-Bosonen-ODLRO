#!/usr/bin/env python3
"""Lokale Einfüge- und Löschverhältnisse im exakten Grundzustand: Vorstufe zu Baustein 2 (einpunkt_zeitroute.md).

Einfügen in Zelle c (Block von s x s Plätzen; in 1D s aufeinanderfolgende Plätze), unter Q = psi_{N-1}^2:
    f_c(S) = sum_{x in c} psi_N(S+x) / psi_{N-1}(S),    G_ein = E_Q f_c^2 / (E_Q f_c)^2 = |u_c|^2 / <psi_{N-1}, u_c>^2,
    u_c = sum_{x in c} b_x psi_N.
Löschen in Zelle c, unter P = psi_N^2:
    d_c(S') = sum_{x in c cap S'} psi_{N-1}(S'-x) / psi_N(S'),  G_los = |v_c|^2 / <psi_N, v_c>^2,  v_c = sum_{x in c} b_x^+ psi_{N-1}.
G - 1 ist die relative Varianz, also die Kosten einer Begegnung zweier Routen in derselben Zelle (gleichzeitige
Näherung, ohne Zeitausdehnung der Zelle). Kontrolle: c = ganzes Gitter gibt G_ein = 1/Z0.
Budget aus skelett_begegnungen.py: log G < alpha_max (0,012 bei Skala 1, 0,17 bei Skala 8).
Aufruf: python3 lokale_einfuegung.py --modell bosonen --L 6 --N 3 4 5 6 [--s 1 2 3]
"""
import argparse
import json
import os
import sys
import time

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "z2", "zweipaar_graph"))
import falk_bruch as fb  # noqa: E402
from einpunkt_kriterium import perron  # noqa: E402


def zelle(modell, L, s):
    if modell == "bosonen1d":
        return np.arange(L) < s
    x, y = np.arange(L * L) // L, np.arange(L * L) % L
    return (x < s) & (y < s)


def rechne(modell, L, N, ss):
    t0 = time.perf_counter()
    kompat, ziel, *_ = fb.geometrie(modell, L)
    M = kompat.shape[0]
    S = {q: fb.Sektor(q, kompat, ziel) for q in (N - 1, N)}
    psi, phi = perron(S[N].H), perron(S[N - 1].H)
    ab = fb.entfernen(S[N], S[N - 1], M)                 # ab[a, i]: Index von S[N].T[a] ohne Teilchen i
    T = S[N].T
    erg = []
    for s in ss:
        inc = zelle(modell, L, s)[T]                      # Teilchen i der Konfiguration a liegt in c
        u = np.bincount(ab[inc], weights=np.broadcast_to(psi[:, None], T.shape)[inc], minlength=S[N - 1].n)
        G_ein = float(u @ u) / float(phi @ u) ** 2
        v = np.where(inc, phi[ab], 0.0).sum(axis=1)
        G_los = float(v @ v) / float(psi @ v) ** 2
        erg.append(dict(s=int(s), zellplaetze=int(zelle(modell, L, s).sum()), G_ein=G_ein, G_los=G_los))
    out = dict(modell=modell, L=L, M=M, N=N, rho=N / M, zellen=erg, zeit_s=time.perf_counter() - t0)
    txt = "  ".join(f"s={e['s']}: {e['G_ein'] - 1:.4f}/{e['G_los'] - 1:.4f}" for e in erg)
    print(f"{modell:9s} L={L:2d} N={N:2d} rho={N / M:.3f}  G-1 (ein/los): {txt}  [{out['zeit_s']:.0f} s]", flush=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modell", choices=["bosonen", "bosonen1d"], default="bosonen")
    ap.add_argument("--L", type=int, nargs="+", default=[6])
    ap.add_argument("--N", type=int, nargs="*", default=[])
    ap.add_argument("--rho", type=float, default=None)
    ap.add_argument("--s", type=int, nargs="+", default=None)
    ap.add_argument("--aus", default=None)
    a = ap.parse_args()
    alle = []
    for L in a.L:
        M = L * L if a.modell == "bosonen" else L
        Ns = [int(round(a.rho * M))] if a.rho is not None else a.N
        ss = a.s or ([1, 2, 3, L] if a.modell == "bosonen" else [1, 2, 4, L])
        alle += [rechne(a.modell, L, N, ss) for N in Ns]
    if a.aus:
        with open(os.path.join(HIER, "ergebnisse", a.aus), "w") as fh:
            json.dump(alle, fh, indent=1)


if __name__ == "__main__":
    main()
