#!/usr/bin/env python3
"""Vergleichsprinzip für den Einfügequotienten (Anhang G.8.4, Weg A): Gibt es eine Jastrow-Einfügung Φ̃ mit
(H_{N+1} − E_{N+1}) Φ̃ ≤ 0 punktweise?  Dann folgt ψ_{N+1} ≥ Φ̃ / ⟨ψ_{N+1}, Φ̃⟩ punktweise (e^{−tH} positivitätserhaltend).

Kandidaten (η eine (N+1)-Konfiguration):
  G=1      Φ̃(η) = Σ_{x∈η} ψ_N(η\\x)                               (reines Einsetzen)
  Jastrow  Φ̃(η) = Σ_{x∈η} ψ_N(η\\x) Π_{j∈η\\x} f(x − x_j)          f = min(1, a(·)/a_R), a = Potentialkern
  Dyson    Φ̃(η) = Σ_{x∈η} ψ_N(η\\x) f(Abstand zum nächsten Nachbarn)
Ausgegeben: Anteil der Konfigurationen mit (H − E_{N+1})Φ̃ > 0 (gewichtet mit ψ_{N+1}²), größte relative Verletzung
max((H − E)Φ̃/Φ̃), und das Ergebnis für u = φ/ψ, falls man Φ̃ ≤ C ψ benutzt.
Aufruf: python3 pruef_unterloesung.py
"""
import numpy as np

import pruef_einfuegequotient as pe


def potentialkern(L, gross=256):
    """Potentialkern der 2D-Irrfahrt (a(0)=0, a(e1)=1) auf dem unendlichen Gitter, ausgewertet für Abstände im L-Torus
    (kürzester Torus-Vektor)."""
    k = 2 * np.pi * np.arange(gross) / gross
    k1, k2 = np.meshgrid(k, k, indexing='ij')
    nenner = 4 - 2 * np.cos(k1) - 2 * np.cos(k2)
    nenner[0, 0] = np.inf
    a = np.zeros((L, L))
    for dx in range(L):
        for dy in range(L):
            x = min(dx, L - dx); y = min(dy, L - dy)
            a[dx, dy] = np.mean((1 - np.cos(k1 * x + k2 * y)) / nenner) * 4   # Normierung: a(e1) = 1
    return a / a[1, 0]


def pruefe(L, N, R):
    M = L * L
    TN, keysN, AN = pe.sektor(L, N)
    TN1, keysN1, AN1 = pe.sektor(L, N + 1)
    psiN, psiN1 = pe.grundzustand(AN), pe.grundzustand(AN1)
    E1 = -float(psiN1 @ (AN1 @ psiN1))
    a = potentialkern(L)
    aR = np.max(a[:R + 1, :R + 1]) if R < L else np.max(a)
    f = np.minimum(1.0, a / aR)
    basis = M ** np.arange(N)[::-1]
    n1 = TN1.shape[0]
    phi = {'G=1': np.zeros(n1), 'Jastrow': np.zeros(n1), 'Dyson': np.zeros(n1)}
    for p in range(N + 1):
        x = TN1[:, p]
        rest = np.delete(TN1, p, axis=1)
        amp = psiN[np.searchsorted(keysN, rest @ basis)]
        dx = (rest // L - (x // L)[:, None]) % L
        dy = (rest % L - (x % L)[:, None]) % L
        fj = f[dx, dy]
        phi['G=1'] += amp
        phi['Jastrow'] += amp * np.prod(fj, axis=1)
        phi['Dyson'] += amp * np.min(fj, axis=1)
    w = psiN1 ** 2
    for name, Ph in phi.items():
        v = -(AN1 @ Ph) - E1 * Ph                      # (H − E_{N+1}) Φ̃ mit H = −A
        pos = Ph > 0
        rel = np.where(pos, v / np.maximum(Ph, 1e-300), 0)
        anteil = w[rel > 1e-12].sum()
        c = float(psiN1 @ Ph)
        verh = np.where(psiN1 > 0, Ph / (c * psiN1), 0)      # Φ̃/(⟨ψ,Φ̃⟩ψ) ≤ 1, falls Unterlösung
        print(f"  {name:8s}: Verletzung (H−E)Φ̃>0 auf Gewicht {anteil:.3f}, max (H−E)Φ̃/Φ̃ = {rel.max():+.3f}, "
              f"min = {rel.min():+.3f};  max Φ̃/(⟨ψ,Φ̃⟩ψ) = {verh.max():.3f}", flush=True)


for (L, N, R) in ((6, 3, 2), (6, 3, 3), (8, 2, 3), (8, 3, 3), (8, 3, 4)):
    print(f"L={L} N={N}→{N + 1} R={R}:")
    pruefe(L, N, R)


def entnahmequotient(L, N, R):
    """q(η, x) = ψ_N(η\\x) · G(x; η\\x) / ψ_{N+1}(η), normiert auf den ψ²-gewichteten Mittelwert; Verteilung über (η, x).
    Konstantes q hieße: der Grundzustand hat punktweise exakt Jastrow-Struktur bezüglich des Einsetzens."""
    M = L * L
    TN, keysN, AN = pe.sektor(L, N)
    TN1, keysN1, AN1 = pe.sektor(L, N + 1)
    psiN, psiN1 = pe.grundzustand(AN), pe.grundzustand(AN1)
    a = potentialkern(L)
    aR = np.max(a[:R + 1, :R + 1])
    f = np.minimum(1.0, a / aR)
    basis = M ** np.arange(N)[::-1]
    qs, ws, qs1 = [], [], []
    for p in range(N + 1):
        x = TN1[:, p]
        rest = np.delete(TN1, p, axis=1)
        amp = psiN[np.searchsorted(keysN, rest @ basis)]
        dx = (rest // L - (x // L)[:, None]) % L
        dy = (rest % L - (x % L)[:, None]) % L
        G = np.prod(f[dx, dy], axis=1)
        qs.append(amp * G / psiN1); qs1.append(amp / psiN1); ws.append(psiN1 ** 2)
    q, q1, w = np.concatenate(qs), np.concatenate(qs1), np.concatenate(ws)
    for name, arr in (('mit Jastrow G', q), ('ohne (G=1)  ', q1)):
        m = np.sum(w * arr) / np.sum(w)
        r = arr / m
        perz = np.percentile(r, [0.1, 1, 50, 99, 99.9])
        print(f"  {name}: min {r.min():.3f}  max {r.max():.3f}  Perzentile 0,1/1/50/99/99,9 %: "
              + " / ".join(f"{v:.3f}" for v in perz), flush=True)


print("Entnahmequotient q = ψ_N(η\\x)·G/ψ_{N+1}(η), relativ zum Mittel:")
for (L, N, R) in ((6, 3, 3), (8, 2, 3), (8, 3, 3), (8, 3, 4), (10, 2, 4)):
    print(f"L={L} N={N}→{N + 1} R={R}:")
    entnahmequotient(L, N, R)
