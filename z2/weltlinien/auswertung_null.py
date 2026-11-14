#!/usr/bin/env python3
"""ODLRO des Grundzustands von H_A aus Wurm-Läufen (wurm_nb4): n_0 aus der gleichzeitigen Paarkorrelation.

n_0 = lim g(r)/g(0) (d-Eichung, g >= 0; bei Translationsinvarianz ist das der Anteil der k = 0-Mode).
1. Plateauwerte g(L/2,0)/g(0) und g(L/2,L/2)/g(0) je (L, beta), Seeds mit nZ gewichtet, Fehler aus der Streuung
   der Seeds.
2. Extrapolation n_0 + a/L (2D-Grundzustand: Phasenfluktuationen geben eine 1/r-Korrektur) je beta.
3. Profil g(r)/g(0) längs der Achse aus den vollen Histogrammen (npz) und Anpassung
   n_0 + a (1/r + 1/(L - r)) für r >= rmin (Bildterm des Torus), je Lauf.
Bei T > 0 fällt g(r) letztlich wie r^(-eta), eta = T/(2 pi rho_s) ~ 0,06 bei T = 0,02; das ist nur für
L >> c/T sichtbar und hier nicht modelliert.
Aufruf: python3 auswertung_null.py [--rmin 4]  -> ergebnisse/auswertung_null.json
"""
import argparse
import glob
import json
import os

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
ERG = os.path.join(HIER, "ergebnisse")


def laeufe(L, b):
    out = []
    for f in sorted(glob.glob(os.path.join(ERG, f"nb4_L{L}_b{b}_s*.json"))):
        d = json.load(open(f))
        R = d["reihe"]
        if not R["nZ"]:
            continue
        out.append(dict(datei=f, w=np.array(R["nZ"]), g0=np.array(R["g0"]), gx=np.array(R["gx"]),
                        gd=np.array(R["gd"]), N=np.array(R["N"]), M=2 * d["L"] ** 2, bloecke=d["blocks"],
                        h=d["time_s"] / 3600))
    return out


def plateau(rs):
    w = np.concatenate([r["w"] for r in rs])
    g0 = (w * np.concatenate([r["g0"] for r in rs])).sum() / w.sum()
    rho = (w * np.concatenate([r["N"] for r in rs])).sum() / w.sum() / rs[0]["M"]
    # g(0) = <n> = rho exakt; das gemessene g0 ist wegen des Zeitfensters w etwas zu klein (bosonen_odlro/README)
    res = {"g0": float(g0), "rho": float(rho), "korrektur": float(g0 / rho), "seeds": len(rs),
           "bloecke": int(sum(r["bloecke"] for r in rs))}
    for k in ("gx", "gd"):
        je = [(r["w"] * r[k]).sum() / (r["w"] * r["g0"]).sum() for r in rs]
        ges = (w * np.concatenate([r[k] for r in rs])).sum() / w.sum() / g0
        res[k] = float(ges)
        res[k + "_fehler"] = float(np.std(je, ddof=1) / np.sqrt(len(je))) if len(je) > 1 else float("nan")
    return res


def profil(L, b, rmin):
    """g(r)/g(0) längs x (gleiche Orientierung, r = 0..L/2), über Seeds summiert; Anpassung je Seed für Fehler."""
    dateien = sorted(glob.glob(os.path.join(ERG, f"nb4_L{L}_b{b}_s*.npz")))
    if not dateien:
        return None
    r = np.arange(0, L // 2 + 1)
    kurven = []
    for f in dateien:
        h = np.load(f)["hist_eq"]
        if h[0, 0] <= 0:
            continue
        # Achse x und y mitteln (ix = 2 dx mod 2L, iy = 0), Spiegelbild r <-> L - r mitnehmen
        gx = np.array([0.25 * (h[(2 * x) % (2 * L), 0] + h[(-2 * x) % (2 * L), 0]
                              + h[0, (2 * x) % (2 * L)] + h[0, (-2 * x) % (2 * L)]) for x in r])
        kurven.append(gx / h[0, 0])
    if not kurven:
        return None
    sel = r >= rmin
    X = np.stack([np.ones(sel.sum()), 1.0 / r[sel] + 1.0 / (L - r[sel])], axis=1)

    def fit(y):
        c, *_ = np.linalg.lstsq(X, y[sel], rcond=None)
        return c
    cs = np.array([fit(k) for k in kurven])
    mittel = np.mean(kurven, axis=0)
    c = fit(mittel)
    fe = cs.std(axis=0, ddof=1) / np.sqrt(len(cs)) if len(cs) > 1 else [np.nan, np.nan]
    return {"r": r.tolist(), "g_durch_g0": mittel.tolist(), "n0": float(c[0]), "n0_fehler": float(fe[0]),
            "a": float(c[1]), "seeds": len(kurven)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rmin", type=int, default=4)
    a = ap.parse_args()
    erg = {}
    for b in ("18.18", "25", "50"):
        zeilen = {}
        for L in (16, 24, 32, 48, 64):
            rs = laeufe(L, b)
            if not rs:
                continue
            p = plateau(rs)
            p["profil"] = profil(L, b, a.rmin)
            zeilen[L] = p
            pr = p["profil"]
            prs = (f"  Profil-Fit n0 = {pr['n0']:.4f} ± {pr['n0_fehler']:.4f} (a = {pr['a']:.3f}), "
                   f"mit rho normiert {pr['n0'] * p['korrektur']:.4f}" if pr else "")
            print(f"T = {1 / float(b):.4f}  L = {L:3d}: [g0/rho = {p['korrektur']:.4f}] g(L/2,0)/g(0) = {p['gx']:.4f} ± {p['gx_fehler']:.4f}, "
                  f"g(L/2,L/2)/g(0) = {p['gd']:.4f} ± {p['gd_fehler']:.4f}  [{p['seeds']} Seeds, {p['bloecke']} Blöcke]"
                  + prs)
        if len(zeilen) >= 2:
            Ls = np.array(sorted(zeilen))
            for k in ("gx", "gd"):
                y = np.array([zeilen[L][k] for L in Ls])
                e = np.array([zeilen[L][k + "_fehler"] for L in Ls])
                wgt = 1 / np.maximum(e, 1e-4) ** 2
                X = np.stack([np.ones(len(Ls)), 1.0 / Ls], axis=1)
                C = np.linalg.inv(X.T @ (wgt[:, None] * X))
                c = C @ X.T @ (wgt * y)
                zeilen[f"fit_{k}"] = {"n0": float(c[0]), "n0_fehler": float(np.sqrt(C[0, 0])), "a": float(c[1])}
                kor = np.mean([zeilen[L]["korrektur"] for L in Ls])
                print(f"   T = {1 / float(b):.4f}, Fit {k} = n0 + a/L über L = {Ls.tolist()}: "
                      f"n0 = {c[0]:.4f} ± {np.sqrt(C[0, 0]):.4f}, a = {c[1]:.3f}; mit rho normiert {c[0] * kor:.4f}")
        erg[b] = zeilen
    with open(os.path.join(ERG, "auswertung_null.json"), "w") as fh:
        json.dump({b: {str(k): v for k, v in z.items()} for b, z in erg.items()}, fh, indent=1)


if __name__ == "__main__":
    main()
