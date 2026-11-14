#!/usr/bin/env python3
"""Hängt der normierte Einfügequotient Θ(ζ,x)/G(x;ζ) von der Umgebung jenseits der Jastrow-Reichweite R ab?
Θ(ζ,x) = ψ_{N+1}(ζ∪x)/ψ_N(ζ),  G = Π_j f(x − x_j),  f = min(1, a/a_R).  Gewicht: ψ_N(ζ)² über alle ζ und freien x.
Ausgabe: Mittel von log(Θ/G) gruppiert nach der Zahl der Teilchen im Ring R < |x − x_j|_∞ ≤ R + w (fern) und nach der
Zahl im Ring |x − x_j|_∞ ≤ R (nah); Standardabweichung; Momente E[(Θ/G / Mittel)^{−η}].
Aufruf: python3 pruef_theta_umgebung.py
"""
import numpy as np

import pruef_einfuegequotient as pe
from pruef_unterloesung import potentialkern


def lauf(L, N, R, w=2):
    M = L * L
    TN, keysN, AN = pe.sektor(L, N)
    TN1, keysN1, AN1 = pe.sektor(L, N + 1)
    psiN, psiN1 = pe.grundzustand(AN), pe.grundzustand(AN1)
    a = potentialkern(L)
    f = np.minimum(1.0, a / np.max(a[:R + 1, :R + 1]))
    basis1 = M ** np.arange(N + 1)[::-1]
    werte, gew, nah, fern = [], [], [], []
    for x in range(M):
        frei = ~np.any(TN == x, axis=1)
        Z = TN[frei]
        neu = np.sort(np.concatenate([Z, np.full((Z.shape[0], 1), x)], axis=1), axis=1)
        psi1 = psiN1[np.searchsorted(keysN1, neu @ basis1)]
        th = psi1 / psiN[frei]
        dx = (Z // L - x // L) % L; dy = (Z % L - x % L) % L
        dxs = np.minimum(dx, L - dx); dys = np.minimum(dy, L - dy)
        dinf = np.maximum(dxs, dys)
        G = np.prod(f[dx, dy], axis=1)
        werte.append(np.log(th / G)); gew.append(psiN[frei] ** 2)
        nah.append(np.sum(dinf <= R, axis=1)); fern.append(np.sum((dinf > R) & (dinf <= R + w), axis=1))
    v, g, n1, n2 = map(np.concatenate, (werte, gew, nah, fern))
    g = g / g.sum()
    mu = np.sum(g * v); sd = np.sqrt(np.sum(g * (v - mu) ** 2))
    print(f"L={L} N={N}→{N + 1} R={R}: log(Θ/G): Mittel {mu:.3f}, Streuung {sd:.3f}, min {v.min() - mu:+.3f}, "
          f"max {v.max() - mu:+.3f}", flush=True)
    for name, n in (('nah  (≤R)', n1), (f'fern (R..R+{w})', n2)):
        zeilen = []
        for k in range(0, n.max() + 1):
            m = n == k
            if g[m].sum() > 1e-4:
                zeilen.append(f"{k}: {np.sum(g[m] * v[m]) / g[m].sum() - mu:+.3f} (Gewicht {g[m].sum():.3f})")
        print(f"   nach Zahl {name}: " + "   ".join(zeilen), flush=True)
    for eta in (0.5, 1.0, 2.0):
        print(f"   E[(Θ/G)^(−{eta})]·e^(η·Mittel) = {np.sum(g * np.exp(-eta * (v - mu))):.4f}", flush=True)


for (L, N, R) in ((8, 2, 2), (8, 3, 2), (10, 2, 2), (10, 2, 3), (12, 2, 3)):
    lauf(L, N, R)
