#!/usr/bin/env python
"""Dyson-Lieb-Simon-Kette mit Infrarotschranke im unendlichen Volumen, harte Bosonen (J = 1).

Exakt gilt für harte Bosonen (Spin-1/2-XY mit Feld):
    c(k) = 8 <b^+b>_nn - 8 <(n-1/2)(n-1/2)>_nn (cos kx + cos ky) + mu (2 rho - 1)  =  alpha + beta (cos kx + cos ky).
(Für rho -> 0: c(k) -> E(k), Integral -> 1, Schranke -> 0.)
Mit Infrarotschranke chi(k) <= 1/E(k), E(k) = 4 - 2 cos kx - 2 cos ky, Falk-Bruch und Summenregel
sum_k g_k = M/2 folgt im unendlichen Volumen
    g_0 / M  >=  1/2 - 1/2 Int_{BZ} d^2k/(2 pi)^2 sqrt(c(k) / E(k)).
alpha, beta werden aus den exakten c_k der falk_bruch-Läufe angepasst (Residuum prüft die Formel); die
Nachbarkorrelationen hängen kaum von L ab. Vergleich mit dem Kondensat je Platz n_0/M der endlichen Rechnung.
Aufruf: python ir_integral.py ergebnisse/falk_bruch_bosonen_L*.json
"""
import json
import sys

import numpy as np


def integral(alpha, beta, n=1600):
    """Int d^2k/(2pi)^2 sqrt(c/E) über die Brillouin-Zone, Mittelpunktsregel (k = 0 nie getroffen)."""
    k = (np.arange(n) + 0.5) * 2 * np.pi / n - np.pi
    kx, ky = np.meshgrid(k, k, indexing="ij")
    E = 4 - 2 * np.cos(kx) - 2 * np.cos(ky)
    c = alpha + beta * (np.cos(kx) + np.cos(ky))
    return float(np.mean(np.sqrt(np.maximum(c, 0) / E)))


def main():
    zeilen = []
    for pfad in sys.argv[1:]:
        for lauf in json.load(open(pfad)):
            if lauf["modell"] != "bosonen":
                continue
            for e in lauf["ergebnisse"]:
                if "c_k" not in e:
                    continue
                k = np.array(e["k"])
                c = np.array(e["c_k"])
                X = np.stack([np.ones(len(k)), np.cos(k[:, 0]) + np.cos(k[:, 1])], 1)
                (al, be), *_ = np.linalg.lstsq(X, c, rcond=None)
                res = float(np.abs(X @ [al, be] - c).max())
                I = integral(al, be)
                I_fein = integral(al, be, 3200)
                schranke = 0.5 - 0.5 * I_fein
                n0_pro_platz = lauf["n0_durch_N"] * lauf["N"] / lauf["M"]
                zeilen.append((lauf["L"], lauf["N"], lauf["dichte"], e["mu_anteil"], al, be, res, I, I_fein, schranke,
                               n0_pro_platz))
    zeilen.sort()
    print(" L  N  Dichte  mu-Ant   alpha     beta   Resid   Int(1600) Int(3200)  Schranke g0/M   n0/M (endlich)")
    for z in zeilen:
        print(f"{z[0]:2d} {z[1]:2d}  {z[2]:.4f}  {z[3]:.2f}  {z[4]:8.4f} {z[5]:8.4f}  {z[6]:.0e}  {z[7]:.4f}    {z[8]:.4f}    "
              f"{z[9]:+.4f}        {z[10]:.4f}")


if __name__ == "__main__":
    main()
