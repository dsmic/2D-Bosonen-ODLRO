#!/usr/bin/env python3
"""L1c streng: lambda_min(b, y) >= 1/(1/lambda_2 + b^2 R_y) (Poincaré + Thomson), R_y = effektiver Widerstand von y
zur Gleichverteilung im b x b-Neumann-Gitter, exakt über die Cosinus-Eigenbasis:
    R_y = sum_{(p,q) != 0} phi_pq(y)^2 / lambda_pq,  lambda_pq = 4 - 2 cos(pi p/b) - 2 cos(pi q/b).
Vergleich mit dem wahren lambda_min (Ecke, zellschranke_punkt.py) und mit (2/pi) ln b (Viertelebene).
Zweiter Teil (Tutorial Lemma 6.3a, Review W5): R_y <= (2/pi) ln b + 2,12 für ALLE b >= 2 und alle y, also
    lambda_min(b) >= pi / (2 b^2 (ln b + 3,6)).
Geprüft werden die beiden elementaren Ungleichungen des Beweises, die Gittersumme und das Maximum von R_y über alle y.
Aufruf: python3 l1c_widerstand.py
"""
import numpy as np

wahr = {4: 0.079241, 8: 0.013045, 16: 0.002406, 32: 0.000475, 64: 0.000098, 128: 0.000021}
print("   b    R_Ecke    R_Ecke-(2/pi)ln b   R_Mitte-(1/(2pi))ln b   Schranke·b²ln b   wahr·b²ln b (Ecke)")
for b in (4, 8, 16, 32, 64, 128, 256, 512):
    p = np.arange(b)
    lam1 = 2 - 2 * np.cos(np.pi * p / b)
    LAM = lam1[:, None] + lam1[None, :]
    c = np.where(p == 0, np.sqrt(1.0 / b), np.sqrt(2.0 / b))

    def R(y1, y2):
        phi1 = c * np.cos(np.pi * p * (y1 + 0.5) / b)
        phi2 = c * np.cos(np.pi * p * (y2 + 0.5) / b)
        Z = (phi1[:, None] * phi2[None, :]) ** 2
        Z[0, 0] = 0.0
        L = LAM.copy()
        L[0, 0] = 1.0
        return float(np.sum(Z / L))
    Re, Rm = R(0, 0), R(b // 2, b // 2)
    lam2 = lam1[1]
    schranke = 1.0 / (1.0 / lam2 + b * b * Re)
    w = wahr.get(b)
    print(f"{b:5d}  {Re:8.4f}   {Re - 2 / np.pi * np.log(b):8.4f}           {Rm - 1 / (2 * np.pi) * np.log(b):8.4f}"
          f"             {schranke * b * b * np.log(b):8.4f}"
          + (f"          {w * b * b * np.log(b):.4f}" if w else ""))

print()
print("Lemma 6.3a: Schranke für alle b")
x = np.linspace(1e-4, np.pi / 2, 1501)
X, Y = np.meshgrid(x, x)
g2 = float((1 / (np.sin(X) ** 2 + np.sin(Y) ** 2) - 1 / (X ** 2 + Y ** 2)).max())
g1 = float((1 / np.sin(x) ** 2 - 1 / x ** 2).max())
ok = g2 <= np.pi ** 2 / 12 and g1 <= np.pi ** 2 / 12
print(f"  1/(sin²x+sin²y) − 1/(x²+y²) ≤ {g2:.4f},  1/sin²x − 1/x² ≤ {g1:.4f};  beide ≤ π²/12 = {np.pi ** 2 / 12:.4f}   {'ok' if ok else 'VERLETZT'}")
for n in (1, 2, 5, 20, 100, 1000):
    q = np.arange(1, n + 1)
    S = float((1.0 / (q[:, None] ** 2 + q[None, :] ** 2)).sum())
    gr = 0.5 + np.pi / 2 * np.log(np.sqrt(2) * n)
    ok &= S <= gr
    print(f"  n = {n:5d}:  Σ 1/(p²+q²) = {S:8.4f} ≤ ½ + (π/2) ln(√2 n) = {gr:8.4f}")
print("     b   max_y R_y  Ort     (2/π)ln b + 2,12   λ-Schranke / [π/(2b²(ln b+3,6))]")
for b in (2, 3, 4, 6, 8, 16, 32, 64, 128, 256, 512, 1024, 2048):
    p = np.arange(b)
    lam1 = 2 - 2 * np.cos(np.pi * p / b)
    W = lam1[:, None] + lam1[None, :]
    W[0, 0] = 1.0
    W = 1.0 / W
    W[0, 0] = 0.0
    c = np.where(p == 0, np.sqrt(1.0 / b), np.sqrt(2.0 / b))
    ys = range(b) if b <= 256 else (0,)                      # alle y bis b = 256, darüber nur die Ecke
    PH = np.array([(c * np.cos(np.pi * p * (y + 0.5) / b)) ** 2 for y in ys])
    R = np.einsum('ap,pq,bq->ab', PH, W, PH)
    i = np.unravel_index(R.argmax(), R.shape)
    Rm = float(R.max())
    gr = 2 / np.pi * np.log(b) + 2.12
    verh = (1.0 / (1.0 / lam1[1] + b * b * Rm)) / (np.pi / (2 * b * b * (np.log(b) + 3.6)))
    gut = Rm <= gr and verh >= 1 and (b > 256 or tuple(int(v) for v in i) == (0, 0))
    ok &= gut
    print(f"  {b:5d}  {Rm:8.4f}  {'Ecke' if tuple(int(v) for v in i) == (0, 0) else str(i):6s}  {gr:8.4f}           {verh:6.3f}   {'ok' if gut else 'VERLETZT'}")
print("Lemma 6.3a: " + ("alle Prüfungen bestanden" if ok else "MINDESTENS EINE PRÜFUNG VERLETZT"))

