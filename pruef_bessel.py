#!/usr/bin/env python3
"""Prüfung zu Anhang K, K.1 (Fassung 2026-11-13): elementare Bausteine von (K1) und der Fehler in Schritt 1.

q_t(k) = e^{-2t} I_|k|(2t), r_j = I_j(z)/I_{j-1}(z), z = 2t.
(a) g(z) = sqrt(z) e^{-z} I_0(z) ist nicht monoton: Höchstwert bei z ≈ 1, danach fällt g von oben gegen 1/sqrt(2π).
(b) Log-Konkavität von k ↦ q_t(k), also r_{j+1} ≤ r_j.
(c) Elementares Quotientenpaar ℓ_j = z/(j + sqrt(j²+z²)) ≤ r_j ≤ Ũ_j = z/(j − 1 + sqrt((j+1)²+z²)).
(d) Segura-Paar L_j = z/(j − ½ + sqrt((j+½)²+z²)) ≤ r_j ≤ U_j = z/(j − ½ + sqrt((j−½)²+z²)) (Literatur), nur zum Vergleich.
(e) q_t(0) ≤ Q(t) = min(e^{−2t+t²}, sqrt(π)/(4 sqrt t)) für alle t, und q_t(0) ≥ 1/sqrt(4πt) für t ≥ 1.
(f) (K1) aus Q(t) und Ũ_j: log Q + Σ log Ũ_j ≤ −½ log(1+t) − k²/(4(t+k)).
Aufruf: python3 pruef_bessel.py
"""
import numpy as np
from scipy.special import ive

np.seterr(over="ignore")

ok = True
print("(a) g(z) = sqrt(z) e^{-z} I0(z)")
zs = np.concatenate([np.linspace(0.01, 5, 500), np.geomspace(5, 1e6, 200)])
g = np.sqrt(zs) * ive(0, zs)
i = int(np.argmax(g))
print(f"    Höchstwert {g[i]:.5f} bei z = {zs[i]:.3f}; g(2) = {np.sqrt(2) * ive(0, 2):.5f}; g(1e6) = {g[-1]:.7f}; 1/sqrt(2π) = {1 / np.sqrt(2 * np.pi):.7f}")
fallend = bool(np.all(np.diff(g[i:]) <= 1e-15))
print(f"    ab dem Höchstwert fallend: {fallend}; überall ≥ 1/sqrt(2π) ab z = 2: {bool(np.all(g[zs >= 2] >= 1 / np.sqrt(2 * np.pi)))}")
ok &= fallend

print("(b)–(d) Quotienten")
v_lk = v_el = v_se = 0
for z in np.geomspace(1e-3, 1e5, 400):
    J = int(min(3 * z + 60, 3000))
    I = ive(np.arange(0, J + 1), z)
    gut = I > 1e-280
    for j in range(1, J):
        if not (gut[j - 1] and gut[j] and gut[j + 1]):
            break
        r = I[j] / I[j - 1]
        r1 = I[j + 1] / I[j]
        if r1 > r * (1 + 1e-12):
            v_lk += 1
        lo = z / (j + np.sqrt(j * j + z * z))
        hi = z / (j - 1 + np.sqrt((j + 1) ** 2 + z * z))
        if not (lo <= r * (1 + 1e-12) and r <= hi * (1 + 1e-12)):
            v_el += 1
        Ls = z / (j - 0.5 + np.sqrt((j + 0.5) ** 2 + z * z))
        Us = z / (j - 0.5 + np.sqrt((j - 0.5) ** 2 + z * z))
        if not (Ls <= r * (1 + 1e-12) and r <= Us * (1 + 1e-12)):
            v_se += 1
print(f"    Verletzungen: Log-Konkavität {v_lk}, elementares Paar {v_el}, Segura-Paar {v_se}")
ok &= v_lk == 0 and v_el == 0

print("(e) q_t(0)")
ts = np.concatenate([np.linspace(1e-4, 1, 400), np.geomspace(1, 1e6, 300)])
q0 = ive(0, 2 * ts)
Q = np.minimum(np.exp(-2 * ts + ts ** 2), np.sqrt(np.pi) / (4 * np.sqrt(ts)))
e1 = bool(np.all(q0 <= Q * (1 + 1e-13)))
e2 = bool(np.all(q0[ts >= 1] >= 1 / np.sqrt(4 * np.pi * ts[ts >= 1])))
e3 = bool(np.all(Q <= (1 + ts) ** -0.5 * (1 + 1e-13)))
print(f"    q_t(0) ≤ Q(t): {e1};  q_t(0) ≥ 1/sqrt(4πt) für t ≥ 1: {e2};  Q(t) ≤ (1+t)^(-1/2): {e3}")
ok &= e1 and e2 and e3

print("(f) (K1) aus Q(t) und Ũ_j")
mn, arg = np.inf, None
for t in np.concatenate([np.linspace(1e-4, 1, 600), np.geomspace(1, 1e5, 400)]):
    z = 2 * t
    K = int(30 * t + 40)
    j = np.arange(1, K + 1)
    lU = np.log(z / (j - 1 + np.sqrt((j + 1) ** 2 + z * z)))
    s = np.concatenate([[0.0], np.cumsum(lU)])
    k = np.arange(0, K + 1)
    Qt = min(np.exp(-2 * t + t * t), np.sqrt(np.pi) / (4 * np.sqrt(t)))
    spiel = -(np.log(Qt) + s) - 0.5 * np.log1p(t) - k ** 2 / (4 * (t + k))
    m = int(np.argmin(spiel))
    if spiel[m] < mn:
        mn, arg = spiel[m], (t, int(k[m]))
print(f"    kleinster log-Spielraum {mn:.5f} bei (t, k) = ({arg[0]:.4g}, {arg[1]})")
ok &= mn >= -1e-12
print("(g) (K2′) aus q_t(0) ≥ 1/sqrt(4πt) und ℓ_j, Faktor e^{-1/4} je Koordinate")
mn, arg = np.inf, None
for t in np.concatenate([np.linspace(1, 50, 500), np.geomspace(50, 1e5, 300)]):
    z = 2 * t
    k = np.arange(0, int(t) + 1)
    j = np.arange(1, int(t) + 1)
    s_l = np.concatenate([[0.0], np.cumsum(np.log(z / (j + np.sqrt(j * j + z * z))))])
    spiel = -0.5 * np.log(4 * np.pi * t) + s_l - (-0.25 - 0.5 * np.log(4 * np.pi * (1 + t)) - k ** 2 / (4 * t))
    m = int(np.argmin(spiel))
    if spiel[m] < mn:
        mn, arg = spiel[m], (t, int(k[m]))
print(f"    kleinster log-Spielraum {mn:.5f} bei (t, k) = ({arg[0]:.4g}, {arg[1]})")
ok &= mn >= -1e-12
print("(h) scharfes (K2) über die Segura-Kette q_t(0)·Π L_j (exaktes q_t(0)), nur zur Auskunft")
mn, arg = np.inf, None
for t in np.concatenate([np.linspace(1, 100, 600), np.geomspace(100, 1e4, 100)]):
    z = 2 * t
    k = np.arange(0, int(t) + 1)
    j = np.arange(1, int(t) + 1)
    s_L = np.concatenate([[0.0], np.cumsum(np.log(z / (j - 0.5 + np.sqrt((j + 0.5) ** 2 + z * z))))])
    spiel = np.log(ive(0, z)) + s_L + 0.5 * np.log(4 * np.pi * (1 + t)) + k ** 2 / (4 * t)
    m = int(np.argmin(spiel))
    if spiel[m] < mn:
        mn, arg = spiel[m], (t, int(k[m]))
print(f"    kleinster log-Spielraum {mn:.5f} bei (t, k) = ({arg[0]:.4g}, {arg[1]}); negativ heißt: die Kette reicht nicht")
print("Anhang K, K.1: " + ("alle Prüfungen bestanden" if ok else "MINDESTENS EINE PRÜFUNG VERLETZT"))
