#!/usr/bin/env python3
"""Größenordnungen für beweis_verlustbilanz.md: Konstanten der Beweiskette und die Schwelle ρ* auf vier Stufen.

Alles hier ist Schätzung [H]. Konstanten, die der Beweis nur als „C“ angibt, sind auf 1 gesetzt (zu günstig);
insbesondere C_P = C e^{CA²} aus Lemma P5″ (Anhang P). Mit C_P > 1 wächst n wie C_P².
Formeln: Anhang F (F.10.4, F.12.6), Anhang P (P.7), Anhang M (C(K), C′(K), M.9.6–M.9.8), Anhang Z (Z.9),
Anhang S (b₀ ≈ 600 bei R* = 1), Tutorial §9.3.
Aufruf: python3 verlustbilanz_zahlen.py
"""
import math

# ---- Stufe D: der Beweis mit seinen Konstanten
C_b = 8 * math.pi * math.exp(11 / 4)          # Lemma P6a″ mit (K2′)
C_P = 1.0                                     # C e^{CA²} aus Lemma P5″, hier zu günstig 1
eps_P = 1 / (4 * math.log(2) * C_b * C_P)
C_L = 2.4e9                                   # Lemma F8 (Anhang F)
H, K_F = 17, 17
C_E = 53 * math.pi * H ** 2 * K_F             # Anhang F, F.11
theta_P = eps_P ** 2 / (16 * C_L ** 2 * C_E)  # Folgerung F9
C_strich = 4900                               # Lemma P6″, kurze Brücken: p₁ = ½ e^{−C′(n+1)}
print(f"C_b = {C_b:.0f}, ε_P = {eps_P:.2e}, C_E = {C_E:.2e}, θ_P = {theta_P:.2e}")
print("Stufe D (Beweis, C_P = 1):")
for K in (25, 100, 540):
    n = K / theta_P
    ln_p = C_strich * n                       # ln(1/p), p = ½ min(p_P, c₁p₁)
    lam1 = math.sqrt(17 * math.log(352 * n))
    D_K = lam1 * math.sqrt(n) + 3             # Kasten des Defekts (F.12.6)
    D_c = math.sqrt(C_strich * n / 0.25)      # Ball des Abwegs: C e^{−cD_c²} ≤ c₁p₁/4, c ≈ 1/4
    R = D_c + math.sqrt(C_strich * n)         # cut-Radius (B1)
    R_ss = D_K + R + 4 * D_c                  # R*″ grob
    Lam2 = (D_c + 2) ** 2
    CK = 6 * (math.log(4 * math.pi) + (Lam2 + 1) / 2) + 5 * ln_p
    CsK = 8 * (math.log(4 * math.pi) + (Lam2 + 1) / 2) + 7 * ln_p
    alpha = 1 / (150 * (1 + R_ss) ** 2)       # b₀ = C(1 + R*)², b₀ ≈ 600 bei R* = 1
    lg_zeta2 = -133 * math.log10(352 * n)
    print(f"  K = {K:3d}: n = {n:.1e}, ln(1/p₁) = {ln_p:.1e}, D_c = {D_c:.1e}, D_K = {D_K:.1e}, R*″ ≈ {R_ss:.1e}, "
          f"α ≈ {alpha:.0e}, ζ² ≈ 10^{lg_zeta2:.0f}")
    print(f"           C(K) = {CK:.1e}  →  c ≈ exp(−2C(K)) = exp(−{2 * CK:.1e});   "
          f"η ≤ 1/4 verlangt ln m ≳ 2C′(K) = {2 * CsK:.1e}  →  ln ln(1/ρ*) ≈ {2 * CsK:.1e}")

# ---- Stufe C: Buchführung des Beweises, aber wahre Eingänge (p ≈ e^{−2πK}, D ≈ 3, b₋ ≈ 0,2)
print("Stufe C (Buchführung des Beweises, wahre Eingänge):")
for K in (25, 100):
    Lam2, ln_p = 25, 2 * math.pi * K
    CK = 6 * math.log(4 * math.pi * math.exp((Lam2 + 1) / 2)) + 5 * ln_p
    CsK = 8 * math.log(4 * math.pi * math.exp((Lam2 + 1) / 2)) + 7 * ln_p
    print(f"  K = {K:3d}: ln(1/ρ*) ≈ e^(2C′(K))/b₋ ≈ 10^{2 * CsK / math.log(10) + math.log10(4 / 0.2):.0f},  "
          f"c ≈ 10^{-2 * CK / math.log(10):.0f}")

# ---- Stufe B: Heuristik der Methode (Tutorial §9.3)
print("Stufe B (Methode mit wahren Konstanten, Tutorial §9.3):")
for K, bm in ((25, 2.8e-4), (100, 1.2e-5)):
    for name, k2 in (("scharf e^{0,54K}", 0.54), ("grob e^{4πK}", 4 * math.pi)):
        ln_rho = k2 * K + math.log((2.5 + 1 / (2 * bm * K)) / 0.07)
        print(f"  K = {K:3d}, κ₂ {name}: ln(1/ρ*) ≈ 10^{ln_rho / math.log(10):.1f}")

# ---- Vergleichswerte
y_lo, y_hi = 0.01, 0.9
for _ in range(60):
    y = (y_lo + y_hi) / 2
    if 1 - y + y * math.log(y) - y / 2 > 0:
        y_lo = y
    else:
        y_hi = y
print(f"Poisson-Vergleich: größtes b₋ mit P(n < 2b₋m) ≤ e^(−b₋m): {y_lo / 2:.3f}")
print(f"2D-Bogoliubov, Verarmung 1/ln(1/(ρa²)) bei ρ = 1/16: {1 / math.log(16 / 0.1985 ** 2):.3f}")
