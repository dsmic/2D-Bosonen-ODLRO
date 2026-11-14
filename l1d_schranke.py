#!/usr/bin/env python3
"""L1d streng: Einfügeschranke mit Dyson-Nächster-Nachbar-Jastrow (einpunkt_zeitroute.md §16.4).

Satz: Für f: Torus -> [0, 1], f(0) = 0, mit D_x = D_y (gitter-symmetrisch) und rho' S(f) < 1 gilt
    E_k - E_{k-1} + 4  <=  2 rho' D(f) / (1 - rho' S(f)),   rho' = (k-1)/M,
    D(f) = sum_Kanten (f(z) - f(z'))^2,   S(f) = sum_z (1 - f(z)^2).
Hier: f_R(z) = min(1, a(z)/a_R) mit dem Potentialkern a der 2D-Irrfahrt, a_R = (2/pi)(ln R + gamma + 1.5 ln 2).
Teil 1: kleine Tori (Mindestbild), Vergleich mit dem wahren mu (exakt, aus l1d_L6/L8.json) und Born 8 rho' (grob).
Teil 2: unendliches Gitter, optimales R je rho, Vergleich mit Lieb-Yngvason 8 pi rho / ln(1/(rho a^2)).
Aufruf: python3 l1d_schranke.py
"""
import json
import os

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
A_GITTER = np.exp(-np.euler_gamma) * 2 ** -1.5


def kern_exakt(xmax, n=1600):
    k = (np.arange(n) + 0.5) * 2 * np.pi / n - np.pi
    K1, K2 = np.meshgrid(k, k, indexing="ij")
    nen = 1 - (np.cos(K1) + np.cos(K2)) / 2
    a = np.zeros((xmax + 1, xmax + 1))
    for i in range(xmax + 1):
        for j in range(i, xmax + 1):
            a[i, j] = a[j, i] = np.mean((1 - np.cos(K1 * i + K2 * j)) / nen)
    return a


def kern_feld(X, Y, a_klein):
    """a(z) auf einem Gitterfeld: exakt für |x|,|y| <= xmax, sonst Asymptotik (Fehler O(r^-2))."""
    r = np.hypot(X, Y)
    a = np.where(r > 0, (2 / np.pi) * (np.log(np.maximum(r, 1e-12)) + np.euler_gamma + 1.5 * np.log(2)), 0.0)
    m = a_klein.shape[0] - 1
    ax, ay = np.abs(X), np.abs(Y)
    innen = (ax <= m) & (ay <= m)
    a[innen] = a_klein[ax[innen], ay[innen]]
    return a


def a_R(R):
    return (2 / np.pi) * (np.log(R) + np.euler_gamma + 1.5 * np.log(2))


def D_S_unendlich(R, a_klein):
    h = int(np.ceil(R)) + 3
    X, Y = np.meshgrid(np.arange(-h, h + 1), np.arange(-h, h + 1), indexing="ij")
    f = np.minimum(1.0, kern_feld(X, Y, a_klein) / a_R(R))
    D = np.sum((f[1:, :] - f[:-1, :]) ** 2) + np.sum((f[:, 1:] - f[:, :-1]) ** 2)
    S = np.sum(1 - f ** 2)
    return D, S


def D_S_torus(L, R, a_klein):
    x = np.arange(L)
    d = np.minimum(x, L - x)
    X, Y = np.meshgrid(d, d, indexing="ij")
    f = np.minimum(1.0, kern_feld(X, Y, a_klein) / a_R(R))
    D = np.sum((f - np.roll(f, 1, 0)) ** 2) + np.sum((f - np.roll(f, 1, 1)) ** 2)
    S = np.sum(1 - f ** 2)
    return D, S


def main():
    a_klein = kern_exakt(12)
    print("Teil 1: kleine Tori, strenge Schranke min_R 2 rho' D/(1 - rho' S) gegen wahres mu + 4")
    for L in (6, 8):
        pfad = os.path.join(HIER, "ergebnisse", f"l1d_L{L}.json")
        wahr = {e["k"]: e["mu_wahr_plus4"] for e in json.load(open(pfad))} if os.path.exists(pfad) else {}
        for k in sorted(wahr):
            rp = (k - 1) / (L * L)
            best = (np.inf, None)
            for R in np.linspace(1.0, L / 2, 40):
                D, S = D_S_torus(L, R, a_klein)
                if rp * S < 1:
                    best = min(best, (2 * rp * D / (1 - rp * S), R))
            print(f"  L={L} k={k}: wahr {wahr[k]:.4f}  streng {best[0]:.4f} (R = {best[1]:.2f}, "
                  f"+{100 * (best[0] / wahr[k] - 1):.0f} %)  Born 8rho' = {8 * rp:.4f}")
    print("Teil 2: unendliches Gitter, optimales R")
    print("   rho        streng      LY 8 pi rho/ln(1/rho a^2)   streng/LY   Born/LY   R_opt")
    Rs = np.unique(np.round(np.geomspace(1.5, 3000, 120), 2))
    tab = [(R,) + D_S_unendlich(R, a_klein) for R in Rs]
    erg = []
    for rho in (1e-1, 3e-2, 1e-2, 1e-3, 1e-4, 1e-6, 1e-8):
        werte = [(2 * rho * D / (1 - rho * S), R) for R, D, S in tab if rho * S < 1]
        b, R = min(werte)
        LY = 8 * np.pi * rho / np.log(1 / (rho * A_GITTER ** 2))
        erg.append(dict(rho=rho, streng=b, LY=LY, R_opt=R))
        print(f"  {rho:8.0e}   {b:.4e}   {LY:.4e}                   {b / LY:6.3f}     {8 * rho / LY:6.2f}    {R:7.1f}")
    with open(os.path.join(HIER, "ergebnisse", "l1d_schranke.json"), "w") as fh:
        json.dump(erg, fh, indent=1)


if __name__ == "__main__":
    main()
