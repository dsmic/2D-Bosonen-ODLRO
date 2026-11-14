#!/usr/bin/env python3
"""Kern-Schranken (K1), (K2) für die Irrfahrt in stetiger Zeit, Rate 1 je Nachbar (Anhang K): explizite Konstanten.

Eine Koordinate: q_t(k) = e^{−2t} I_|k|(2t) (Sprünge ±1 mit Rate 1 je Richtung); in 2D p_t(x) = q_t(x₁) q_t(x₂).
(K1, 1D)  q_t(k) ≤ C₁ (1+t)^{−1/2} exp(−c₁ k²/(t + |k|))      für alle t ≥ 0, k
(K2, 1D)  q_t(k) ≥ c₂ (1+t)^{−1/2} exp(−C₂ k²/t)              für t ≥ 1, |k| ≤ t
Ausgegeben: für mehrere c₁ das nötige C₁ = sup q √(1+t) e^{c₁k²/(t+|k|)}, für mehrere C₂ das größte c₂ = inf(...).
Gitter: t von 0 bis 10⁵ (logarithmisch), k von 0 bis 30t + 30.
Aufruf: python3 pruef_kernschranken.py
"""
import numpy as np
from scipy.special import ive


def logq(t, k):
    """log q_t(k) = log(e^{−2t} I_|k|(2t)), stabil: scipy, sonst gleichmäßige Debye-Asymptotik für große Ordnung."""
    k = np.abs(np.asarray(k, float)); t = np.asarray(t, float)
    with np.errstate(divide='ignore', invalid='ignore'):
        v = np.log(ive(k, 2 * t))
        schlecht = ~np.isfinite(v)
        if np.any(schlecht):
            kk, tt = k[schlecht], t[schlecht]
            z = 2 * tt / kk
            r = np.sqrt(1 + z * z)
            v[schlecht] = -0.5 * np.log(2 * np.pi * kk) - 0.25 * np.log(1 + z * z) + kk * (r + np.log(z / (1 + r))) - 2 * tt
    return v


def main():
    ts = np.concatenate([[0.05, 0.2, 0.5], np.logspace(0, 5, 70)])
    print("(K1, 1D): nötiges C₁ für gegebenes c₁")
    for c1 in (0.1, 0.2, 0.25, 0.3, 0.4):
        best = 0.0
        for t in ts:
            k = np.arange(0, int(30 * t + 30))
            v = logq(np.full(k.shape, t), k) + 0.5 * np.log(1 + t) + c1 * k ** 2 / (t + k + 1e-300)
            best = max(best, np.exp(v.max()))
        print(f"  c₁ = {c1:4.2f}:  C₁ = {best:.4f}")
    print("(K2, 1D): größtes c₂ für gegebenes C₂ (t ≥ 1, |k| ≤ t)")
    for C2 in (0.25, 0.5, 1.0, 2.0):
        worst = np.inf
        for t in ts[ts >= 1]:
            k = np.arange(0, int(t) + 1)
            v = logq(np.full(k.shape, t), k) + 0.5 * np.log(1 + t) + C2 * k ** 2 / t
            worst = min(worst, np.exp(v.min()))
        print(f"  C₂ = {C2:4.2f}:  c₂ = {worst:.4f}")


if __name__ == '__main__':
    main()
