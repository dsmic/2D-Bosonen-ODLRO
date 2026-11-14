#!/usr/bin/env python3
"""Pflasterung für beliebiges L (Anhang Z, Z.13): Prüfung der Rechteckfassung von Lemma 6.3 und 6.3a.

Für ein Rechteck Q mit Seiten b und b′ ∈ {b, b + 1} (Neumann-Laplace L_Q, nur Kanten in Q) ist der effektive Widerstand
von y zur Gleichverteilung in der Kosinus-Eigenbasis
    R_y = Σ_{(p,q) ≠ 0} φ_p(y₁)² ψ_q(y₂)² / (λ_p + μ_q),  λ_p = 2 − 2cos(πp/b),  μ_q = 2 − 2cos(πq/b′).
Behauptet (Lemma 6.3b):  R_y ≤ (2/π) ln b + 3,4  für alle y, und  λ_min(Q) ≥ 1/(1/λ₂ + |Q| R_y) ≥ π/(2|Q| (ln b + 5,8)),
λ₂ = 2 − 2cos(π/b′) die Lücke der längeren Seite.
Geprüft: Maximum von R_y über alle y (b ≤ 128) bzw. in der Ecke (größere b, dort liegt das Maximum), und die λ-Schranke.
Außerdem die Eigenschaften der ausgeglichenen Teilung einer Seite L in n = ⌊L/s⌋ Abschnitte.
Aufruf: python3 pruef_pflasterung.py   (kleiner Speicherbedarf)
"""
import numpy as np


def widerstand(b, bs, alle_y):
    p = np.arange(b)
    q = np.arange(bs)
    lp = 2 - 2 * np.cos(np.pi * p / b)
    mq = 2 - 2 * np.cos(np.pi * q / bs)
    W = lp[:, None] + mq[None, :]
    W[0, 0] = 1.0
    W = 1.0 / W
    W[0, 0] = 0.0
    cp = np.where(p == 0, np.sqrt(1.0 / b), np.sqrt(2.0 / b))
    cq = np.where(q == 0, np.sqrt(1.0 / bs), np.sqrt(2.0 / bs))
    y1s = range(b) if alle_y else (0,)
    y2s = range(bs) if alle_y else (0,)
    P1 = np.array([(cp * np.cos(np.pi * p * (y + 0.5) / b)) ** 2 for y in y1s])
    P2 = np.array([(cq * np.cos(np.pi * q * (y + 0.5) / bs)) ** 2 for y in y2s])
    R = P1 @ W @ P2.T
    i = np.unravel_index(R.argmax(), R.shape)
    return float(R.max()), (int(i[0]), int(i[1])), float(mq[1] if bs > 1 else lp[1])


ok = True
print("Lemma 6.3b (Rechtecke b × b′, b′ ∈ {b, b+1})")
print("     b    b′   max_y R_y   Ort        (2/π)ln b + 3,4   λ-Schranke·2|Q|(ln b + 5,8)/π")
for b in (2, 3, 4, 5, 8, 16, 32, 64, 128, 256, 512, 1024):
    for bs in (b, b + 1):
        alle = b <= 128
        Rm, ort, lam2 = widerstand(b, bs, alle)
        gr = 2 / np.pi * np.log(b) + 3.4
        flaeche = b * bs
        lam = 1.0 / (1.0 / lam2 + flaeche * Rm)
        verh = lam * 2 * flaeche * (np.log(b) + 5.8) / np.pi
        gut = Rm <= gr and verh >= 1
        ok &= gut
        print(f"  {b:5d} {bs:5d}   {Rm:8.4f}   {str(ort) if alle else 'Ecke':9s}  {gr:8.4f}          {verh:7.3f}   {'ok' if gut else 'VERLETZT'}")

print()
print("Ausgeglichene Teilung: L = n q + r, r Abschnitte der Länge q + 1, n − r der Länge q, n = ⌊L/s⌋ ≥ 16")
rng = np.random.default_rng(5)
schlecht = 0
for _ in range(20000):
    s = int(rng.integers(16, 400))
    L = int(rng.integers(16 * s, 200 * s))
    n = L // s
    qq, r = divmod(L, n)
    seiten = [qq + 1] * r + [qq] * (n - r)
    if sum(seiten) != L or min(seiten) < s or max(seiten) > 17 * s / 16 + 1 or max(seiten) > 9 * s / 8:
        schlecht += 1
print(f"  20 000 Zufallsfälle (16 ≤ s < 400, 16 s ≤ L < 200 s): Seiten in [s, 17s/16 + 1] ⊂ [s, 9s/8], Summe = L: "
      f"{'alle ok' if schlecht == 0 else f'{schlecht} VERLETZT'}")
ok &= schlecht == 0
print("Pflasterung: " + ("alle Prüfungen bestanden" if ok else "MINDESTENS EINE PRÜFUNG VERLETZT"))
