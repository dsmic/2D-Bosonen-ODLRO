#!/usr/bin/env python3
"""Treffwahrscheinlichkeit bewegter Ziele in 2D (Anhang P, P.7): exakte Vorwärtsrechnung.

Wanderer: faule Irrfahrt auf ℤ² (Sprungwahrscheinlichkeit p je Schritt, gleichverteilt auf 4 Nachbarn), Start im
Ursprung. Ziel: feste Bahn Y_t, Startabstand d. f_t(x) = P(Wanderer bei x zur Zeit t, Ziel bisher nicht getroffen);
getroffen heißt: gleicher Platz nach einem Schritt. Dauer τ Schritte. Bahnen:
  ruhend         Y_t = (d, 0)
  ballistisch    läuft mit Geschwindigkeit 1 Platz je Schritt auf den Ursprung zu und bleibt dort
  diffusiv(A)    Abstand d (1 − √(t/t_A))_+ mit A √(p t_A) = d, danach ruhend im Ursprung
  Irrfahrt       unabhängige faule Irrfahrt ab (d, 0), gemittelt über Proben (das „getemperte“ Bild)
Vergleich: ln(√(pτ)/d)/ln(√(pτ)) und die Schranke aus P.7 mit dem Zusatz ln A.
Aufruf: python3 pruef_treffen_bewegt.py
"""
import numpy as np


def schritt(f, p):
    return (1 - p) * f + (p / 4) * (np.roll(f, 1, 0) + np.roll(f, -1, 0) + np.roll(f, 1, 1) + np.roll(f, -1, 1))


def treffen(bahn, tau, p, G):
    f = np.zeros((G, G)); c = G // 2
    f[c, c] = 1.0
    getroffen = 0.0
    for t in range(1, tau + 1):
        f = schritt(f, p)
        y = bahn[t]
        i, j = c + y[0], c + y[1]
        getroffen += f[i, j]
        f[i, j] = 0.0
    return getroffen


def main():
    p, tau, d = 0.4, 6000, 12
    G = 2 * int(5 * np.sqrt(p * tau)) + 2 * d + 1
    rng = np.random.default_rng(3)
    t = np.arange(tau + 1)
    bahnen = {'ruhend': np.stack([np.full(tau + 1, d), np.zeros(tau + 1, int)], 1),
              'ballistisch': np.stack([np.maximum(d - t, 0), np.zeros(tau + 1, int)], 1)}
    for A in (1, 2, 4, 8):
        tA = (d / A) ** 2 / p
        r = np.maximum(d * (1 - np.sqrt(t / tA)), 0)
        bahnen[f'diffusiv A={A}'] = np.stack([np.round(r).astype(int), np.zeros(tau + 1, int)], 1)
    ref = np.log(np.sqrt(p * tau) / d) / np.log(np.sqrt(p * tau))
    print(f"τ = {tau}, p = {p}, d = {d}, Ausbreitung √(pτ) = {np.sqrt(p * tau):.1f};  ln(√(pτ)/d)/ln √(pτ) = {ref:.3f}")
    for name, b in bahnen.items():
        print(f"  {name:16s}  P(Treffer) = {treffen(b, tau, p, G):.4f}", flush=True)
    werte = []
    for _ in range(60):
        schritte = rng.integers(0, 4, size=tau)
        dxy = np.array([(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)])
        lazy = rng.random(tau) < p
        inc = np.where(lazy[:, None], dxy[1 + (schritte % 4)], 0)
        b = np.vstack([[d, 0], [d, 0] + np.cumsum(inc, 0)])
        b = np.clip(b, -(G // 2) + 1, G // 2 - 1)
        werte.append(treffen(b, tau, p, G))
    werte = np.array(werte)
    print(f"  {'Irrfahrt':16s}  P(Treffer) Mittel = {werte.mean():.4f}, Streuung = {werte.std():.4f}, "
          f"Max = {werte.max():.4f} (60 Bahnen)")


if __name__ == '__main__':
    main()
