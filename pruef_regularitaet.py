#!/usr/bin/env python3
"""Gütebedingungen (G2), (G3) aus Anhang P, P.7: Wie oft versagen sie für freie Irrfahrten? (Lemma T1: markierte
Teilchen wandern höchstens wie freie.)

Irrfahrt auf ℤ² in stetiger Zeit, Rate 1 je Nachbar (Sprungzeiten exakt simuliert), Dauer 2τ.
(G2_A): Für σ auf einem Gitter der Weite 1 in [0, τ] und die Fenster W_i = [2^i, 2^{i+1}] mit A² ≤ 2^i ≤ τ/2: ruhig, wenn
  sup_{u∈W_i} |Y_{σ+u} − Y_σ|_∞ ≤ A 2^{i/2}. Versagen: an irgendeinem σ ist weniger als die Hälfte ruhig.
(G3): für Startabstand d (Punkt x im Abstand d von Y_0 in der ungünstigsten Richtung, nämlich dort, wohin Y läuft):
  schnelle Fenster W ⊂ [0, d²] mit inf |x − Y_t| < d/2; gemessen über B ≤ 1 + log₂(4β), β = sup_t |Y_t − Y_0|²/max(t,1).
Aufruf: python3 pruef_regularitaet.py
"""
import numpy as np


def bahn(rng, T):
    n = rng.poisson(4 * T)
    t = np.sort(rng.uniform(0, T, n))
    r = rng.integers(0, 4, n)
    d = np.array([(1, 0), (-1, 0), (0, 1), (0, -1)])[r]
    pos = np.vstack([[0, 0], np.cumsum(d, 0)])
    return np.concatenate([[0.0], t]), pos


def auf_gitter(t, pos, gitter):
    idx = np.searchsorted(t, gitter, side='right') - 1
    return pos[idx]


def main():
    import sys
    rng = np.random.default_rng(5)
    tau = int(sys.argv[1]) if len(sys.argv) > 1 else 4096
    gitter = np.arange(0, 2 * tau + 1)
    proben = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    print(f"τ = {tau}, {proben} Bahnen je A")
    print(f"{'A':>4} {'P(G2 versagt)':>14} {'mittl. Anteil unruhig':>22}")
    bahnen = []
    for _ in range(proben):
        t, pos = bahn(rng, 2 * tau)
        bahnen.append(auf_gitter(t, pos, gitter))
    alist = (6.0, 7.0, 8.0) if tau > 16384 else ((5.0, 6.0, 7.0, 8.0) if tau > 4096 else (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0))
    for A in alist:
        stufen = [i for i in range(0, 20) if A * A <= 2 ** i <= tau / 2]
        versagt, anteile = 0, []
        for Y in bahnen:
            schlecht = False
            for sig in range(0, tau + 1, 8):
                unruhig = 0
                for i in stufen:
                    w = Y[sig + 2 ** i: sig + 2 ** (i + 1) + 1] - Y[sig]
                    if np.abs(w).max() > A * 2 ** (i / 2):
                        unruhig += 1
                anteile.append(unruhig / len(stufen))
                if unruhig > len(stufen) / 2:
                    schlecht = True
            versagt += schlecht
        print(f"{A:4.1f} {versagt / proben:14.3f} {np.mean(anteile):22.3f}", flush=True)
    print("\n(G3): β = sup_t |Y_t − Y_0|²/max(t,1) über [0, τ], Schranke B ≤ 1 + log₂(4β)")
    beta = np.array([np.max(np.max(np.abs(Y[1:tau + 1]), 1) ** 2 / np.maximum(np.arange(1, tau + 1), 1)) for Y in bahnen])
    B = 1 + np.log2(4 * beta)
    print(f"  β: Median {np.median(beta):.2f}, 99 % {np.quantile(beta, 0.99):.2f}, Max {beta.max():.2f};  "
          f"B-Schranke: Mittel {B.mean():.2f}, 99 % {np.quantile(B, 0.99):.2f}, Max {B.max():.2f}")


if __name__ == '__main__':
    main()
