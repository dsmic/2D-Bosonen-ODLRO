#!/usr/bin/env python3
"""Prüfung zu Anhang E (Review W6): Einfügen im Dirichlet-Quadrat und glatte Zählgröße.

(1) Lemma E1 exakt: harte Bosonen im l x l-Quadrat mit Dirichlet-Rand (Sprünge aus dem Quadrat kosten wie
    Sprünge auf einen Nullzustand). Geprüft werden für jedes k
        eps_k - eps_{k-1} <= lam_D + g((k-1) phi_max^2)          (Zuwachs)
        eps_k             <= k (lam_D + g((k-1) phi_max^2)/2)     (Summe, Konvexität)
    mit g(x) = 2 x D(f) / (1 - x V(f)) für zwei Profile f (f = 1 - delta_0 und ein logarithmisches Profil).
(2) Die elementaren Ungleichungen des Beweises: |cos^2 a - cos^2 b| <= |a-b| (2 cos a + |a-b|),
    (e^z - 1)^2 <= z^2 e^{2z}, cosh z - 1 <= (z^2/2) cosh z.
(3) Zahlen: c3 = c1^2 / (512 pi kappa (8 pi kappa + c1)) und b_- = c3/8 für die Tabelle in satz_3_9 §4.
Aufruf: python3 pruef_einfuegen.py
"""
import itertools
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigsh

A_GITTER = np.exp(-np.euler_gamma) / 2 ** 1.5


def eps_dirichlet(l, k):
    """Grundenergie von k harten Bosonen im l x l-Quadrat, H = 4k - A (Dirichlet)."""
    if k == 0:
        return 0.0
    plaetze = [(i, j) for i in range(l) for j in range(l)]
    konf = list(itertools.combinations(range(l * l), k))
    index = {c: n for n, c in enumerate(konf)}
    H = lil_matrix((len(konf), len(konf)))
    for n, c in enumerate(konf):
        H[n, n] = 4.0 * k
        besetzt = set(c)
        for x in c:
            i, j = plaetze[x]
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + di, j + dj
                if 0 <= a < l and 0 <= b < l:
                    y = a * l + b
                    if y not in besetzt:
                        neu = tuple(sorted((besetzt - {x}) | {y}))
                        H[n, index[neu]] -= 1.0
    H = H.tocsr()
    if H.shape[0] <= 400:
        return float(np.linalg.eigvalsh(H.toarray())[0])
    return float(eigsh(H, k=1, which='SA', tol=1e-10)[0][0])


def profil_kennzahlen(f):
    """D(f) = Summe über Kanten von Z^2 der (Δf)^2, V(f) = Summe (1 - f^2); f als Funktion auf Z^2."""
    R = 12
    D = 0.0
    V = 0.0
    for i in range(-R, R + 1):
        for j in range(-R, R + 1):
            V += 1 - f(i, j) ** 2
            D += (f(i + 1, j) - f(i, j)) ** 2 + (f(i, j + 1) - f(i, j)) ** 2
    return D, V


def f_delta(i, j):
    return 0.0 if (i, j) == (0, 0) else 1.0


def mach_f_log(Rf):
    def f(i, j):
        r = np.hypot(i, j)
        if r == 0:
            return 0.0
        return float(min(1.0, np.log(r / A_GITTER) / np.log(Rf / A_GITTER)))
    return f


ok = True
print("(1) Lemma E1: Einfügen im Dirichlet-Quadrat, exakt")
profile = [("f = 1 − δ₀", f_delta), ("f log, R = 2", mach_f_log(2.0)), ("f log, R = 3", mach_f_log(3.0))]
kenn = [(name, *profil_kennzahlen(f)) for name, f in profile]
for name, D, V in kenn:
    print(f"    {name:14s}  D = {D:.4f}   V = {V:.4f}")
print("    l  k   eps_k        Zuwachs   Schranke(Zuwachs)   eps_k/k   Schranke(Summe)/k   Profil")
for l, kmax in ((3, 4), (4, 4), (5, 4), (6, 4), (8, 3)):
    lamD = 8 * np.sin(np.pi / (2 * (l + 1))) ** 2
    phi2 = (2.0 / (l + 1)) ** 2 * np.max(np.sin(np.pi * np.arange(1, l + 1) / (l + 1))) ** 4
    vorher = 0.0
    for k in range(1, kmax + 1):
        e = eps_dirichlet(l, k)
        zuw = e - vorher
        x = (k - 1) * phi2
        beste = None
        for name, D, V in kenn:
            if x * V >= 1:
                continue
            g = 2 * x * D / (1 - x * V)
            sz, ss = lamD + g, lamD + g / 2
            if beste is None or ss < beste[2]:
                beste = (name, sz, ss)
            ok &= zuw <= sz + 1e-9 and e / k <= ss + 1e-9
        if beste is None:
            print(f"   {l:2d} {k:2d}   {e:9.5f}   {zuw:8.5f}   (x V ≥ 1 für alle Profile)")
        else:
            print(f"   {l:2d} {k:2d}   {e:9.5f}   {zuw:8.5f}   {beste[1]:9.5f}           {e / k:8.5f}  {beste[2]:9.5f}           {beste[0]}")
        vorher = e

print("(2) elementare Ungleichungen")
a = np.linspace(0, np.pi / 2, 801)
A_, B_ = np.meshgrid(a, a)
lhs = np.abs(np.cos(A_) ** 2 - np.cos(B_) ** 2)
rhs = np.abs(A_ - B_) * (2 * np.cos(A_) + np.abs(A_ - B_))
u1 = bool((lhs <= rhs + 1e-12).all())
z = np.linspace(0, 1, 1001)
u2 = bool(((np.exp(z) - 1) ** 2 <= z ** 2 * np.exp(2 * z) + 1e-15).all())
u3 = bool((np.cosh(z) - 1 <= z ** 2 / 2 * np.cosh(z) + 1e-15).all())
ok &= u1 and u2 and u3
print(f"    |cos²a − cos²b| ≤ |a−b|(2cos a + |a−b|): {'ok' if u1 else 'VERLETZT'};  (e^z−1)² ≤ z²e^(2z): {'ok' if u2 else 'VERLETZT'};"
      f"  cosh z − 1 ≤ (z²/2)cosh z: {'ok' if u3 else 'VERLETZT'}")

print("(3) Zahlen für satz_3_9 §4 (Grenzwerte ρ → 0)")
print("    c1          κ_μ   η = c1/(256πκ_μ)   c3            b_- = c3/8    K_b")
for name, c1, kap in (("3π/16", 3 * np.pi / 16, 1.5), ("π", np.pi, 1.5), ("4π", 4 * np.pi, 1.0)):
    c3 = c1 ** 2 / (512 * np.pi * kap * (8 * np.pi * kap + c1))
    print(f"    {name:8s}  {kap:4.1f}   {c1 / (256 * np.pi * kap):.3e}          {c3:.3e}     {c3 / 8:.3e}     {316 / c1:6.1f}")
print("Anhang E: " + ("alle Prüfungen bestanden" if ok else "MINDESTENS EINE PRÜFUNG VERLETZT"))
