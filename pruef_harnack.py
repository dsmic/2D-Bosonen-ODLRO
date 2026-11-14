#!/usr/bin/env python3
"""Parabolischer Harnack-Effekt für das Einsetzen (Anhang G.8.4, Beweisweg für Lemma J).

Für die reine Einfügung φ_Λ(η) = Σ_{x∈η} ψ_N(η\\x) und die Jastrow-Einfügung Φ_J(η) = Σ_{x∈η} ψ_N(η\\x) G(x; η\\x)
wird v_τ = e^{−τ(H_{N+1} − E_{N+1})} v_0 gerechnet. Es gilt v_τ/ψ_{N+1} = P_τ(v_0/ψ_{N+1}) (Doob-Halbgruppe), und für
τ → ∞ wird das konstant. Gemessen: Schwankungsbreite max/min von v_τ/ψ_{N+1} über alle Konfigurationen, und die
Breite zwischen den 1-%- und 99-%-Quantilen (gewichtet mit ψ²). Lokaler Harnack-Effekt hieße: Die Breite fällt bei
τ = O(1) auf ein festes Niveau, unabhängig von L; nur die letzte Annäherung an 1 ist langsam (global).
Aufruf: python3 pruef_harnack.py
"""
import numpy as np
from scipy.sparse.linalg import expm_multiply

import pruef_einfuegequotient as pe
from pruef_unterloesung import potentialkern


def gewichtete_quantile(r, w, qs):
    o = np.argsort(r)
    c = np.cumsum(w[o]); c /= c[-1]
    return [r[o][np.searchsorted(c, q)] for q in qs]


def lauf(L, N, R, taus):
    M = L * L
    TN, keysN, AN = pe.sektor(L, N)
    TN1, keysN1, AN1 = pe.sektor(L, N + 1)
    psiN, psi = pe.grundzustand(AN), pe.grundzustand(AN1)
    E = -float(psi @ (AN1 @ psi))
    a = potentialkern(L)
    f = np.minimum(1.0, a / np.max(a[:R + 1, :R + 1]))
    basis = M ** np.arange(N)[::-1]
    phi = np.zeros(TN1.shape[0]); PhiJ = np.zeros(TN1.shape[0])
    for p in range(N + 1):
        x = TN1[:, p]
        rest = np.delete(TN1, p, axis=1)
        amp = psiN[np.searchsorted(keysN, rest @ basis)]
        dx = (rest // L - (x // L)[:, None]) % L
        dy = (rest % L - (x % L)[:, None]) % L
        phi += amp; PhiJ += amp * np.prod(f[dx, dy], axis=1)
    w = psi ** 2
    H = -AN1
    erg = {}
    for name, v0 in (('rein', phi), ('Jastrow', PhiJ)):
        zeilen = []
        v = v0.copy(); t_alt = 0.0
        for t in taus:
            v = expm_multiply(-(t - t_alt) * (H - E * np.eye(1) if False else H), v) * np.exp((t - t_alt) * E)
            t_alt = t
            r = v / psi
            q1, q99 = gewichtete_quantile(r, w, (0.01, 0.99))
            zeilen.append((t, r.max() / r.min(), q99 / q1))
        erg[name] = zeilen
    return erg


taus = [0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0]
for (L, N, R) in ((6, 3, 3), (8, 3, 3), (10, 2, 4), (12, 2, 4)):
    erg = lauf(L, N, R, taus)
    print(f"L={L} N={N}→{N + 1} (ρ={(N + 1) / L**2:.3f}):")
    for name, zeilen in erg.items():
        print(f"  {name:8s} max/min:  " + "  ".join(f"τ={t:g}:{a:.2f}" for t, a, b in zeilen))
        print(f"  {'':8s} q99/q1:   " + "  ".join(f"τ={t:g}:{b:.2f}" for t, a, b in zeilen), flush=True)
