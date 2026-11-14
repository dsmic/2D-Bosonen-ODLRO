#!/usr/bin/env python3
"""Abwärts-Hälfte der Zeitschleife (Anhang G.11): exakter Ein-Teilchen-Test in 2D.

Ein Teilchen, stetige Zeit, Rate 1 je Nachbar: P_t(h, h') = e^{-4t} I_{dx}(2t) I_{dy}(2t).  |µ| = N0/N = 1.
Aufweg: das Loch fährt auf der Linie mit (für N = 1 gibt es nichts umzusteigen).
Abweg, Variante "Zelle": neuer Kopf gleichverteilt in der s×s-Zelle des alten Kopfes, Stück aus dem exakt bedingten
  Gesetz.  Dann gilt exakt  ∫ f² dµ = Σ_z P_2T(z, z) · M · (s^{-4})^w (V^w 1)(z)  mit  V(h, h') = 1/P_δ(h, h')
  auf der Zelle; je Scheibe wächst ∫ f² also um den Faktor λ_max(V)/s⁴ ≥ 1/P(Linie bleibt in der Zelle).
Abweg, Variante "frei" (Spiegelbild des Aufwegs): neuer Kopf mit freiem Anfang; Faktor je Scheibe genau 1.
Ausgabe: λ_max(V)/s⁴, sein Logarithmus (zu vergleichen mit dem Budget α_max ≈ 0,07), und 1/P(bleiben).
Aufruf: python3 pruef_abwaerts_einteilchen.py
"""
import numpy as np
from scipy.special import ive


def kern(dx, dy, t):
    return ive(np.abs(dx), 2 * t) * ive(np.abs(dy), 2 * t)        # e^{-4t} I_dx(2t) I_dy(2t)


def faktor(s, delta):
    xs = np.array([(i, j) for i in range(s) for j in range(s)])
    d = xs[:, None, :] - xs[None, :, :]
    P = kern(d[..., 0], d[..., 1], delta)                            # P_δ(h, h') innerhalb der Zelle
    V = 1.0 / P
    lam = np.max(np.linalg.eigvalsh((V + V.T) / 2))                  # V ist symmetrisch
    bleiben = P.sum(axis=1).mean()                                   # P(Linie nach δ wieder in der Zelle), Start gleichverteilt
    return lam / s ** 4, 1.0 / bleiben


print(f"{'s':>4} {'δ/s²':>6} {'Faktor je Scheibe':>18} {'ln Faktor':>10} {'1/P(bleiben)':>13}")
for s in (4, 8, 16):
    for q in (0.25, 0.5, 1.0):
        F, b = faktor(s, q * s * s)
        print(f"{s:4d} {q:6.2f} {F:18.3f} {np.log(F):10.3f} {b:13.3f}", flush=True)
