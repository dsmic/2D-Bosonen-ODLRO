#!/usr/bin/env python3
"""L2 numerisch: Treffwahrscheinlichkeit zweier Teilchen in 2D (Relativbewegung: Irrfahrt, Rate 2 je Nachbar).

P(Treffen vor exponentieller Zeit mit Mittel delta | Startabstand d) = g(d)/g(0),
g(x) = int_0^inf e^{-t/delta} ive(x1, 4t) ive(x2, 4t) dt   (ive = e^{-z} I_nu(z); exakt für den Gitterkern).
Mit r = rho^{-1/2}, d = r, delta = kappa r^2. Erwartung: P ~ C(kappa) / ln(1/rho), also P * ln(1/rho) -> C(kappa).
Aufruf: python3 l2_treffen.py
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import ive


def g(x1, x2, lam):
    f = lambda t: np.exp(-lam * t) * ive(x1, 4 * t) * ive(x2, 4 * t)
    T = 60.0 / lam
    stellen = [0.0] + list(np.geomspace(1e-3, T, 60))
    s = 0.0
    for a, b in zip(stellen[:-1], stellen[1:]):
        s += quad(f, a, b, limit=200)[0]
    return s


print("  kappa     r      rho        P(Treffen)   P·ln(1/rho)")
for kappa in (0.5, 1.0, 2.0, 4.0):
    for r in (4, 8, 16, 32, 64, 128, 256):
        lam = 1.0 / (kappa * r * r)
        P = g(r, 0, lam) / g(0, 0, lam)
        rho = 1.0 / r ** 2
        print(f"  {kappa:4.1f}  {r:5d}   {rho:.2e}   {P:.4f}       {P * np.log(1 / rho):.3f}")
