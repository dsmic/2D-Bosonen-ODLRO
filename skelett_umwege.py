#!/usr/bin/env python3
"""L4 numerisch: Budget je Zellpaar, wenn beide Skelette um dieselben schlechten Raum-Zeit-Zellen umgelenkt werden.

Skelette wie skelett_budget.py (zwei Querrichtungen x, y; erste Koordinate = Zeitscheibe t), Sternpfad je Schritt.
Schlechte Zellen: unabhängig mit Wahrscheinlichkeit q (Hash von (x, y, t, seed), also ohne Speicher; die gleiche
Umgebung für beide Routen). Umlenkung (vereinfachte Form von §8.2 des Preprints): Trifft eine Sternpfadzelle eine
schlechte Zelle, wird ihre Komponente in der Zeitscheibe bestimmt (Nachbarschaft in x, y) und die Zelle durch die
nächstgelegene gute Randzelle ersetzt (feste Reihenfolge bei Gleichstand), deterministisch und nur abhängig von
Komponente und Position. So werden beide Routen auf dieselben Randzellen gedrückt; das ist der gefährliche Effekt.
Gezählt: J_A = sum_t #{(c, c') nahe (|c - c'|_inf <= R) in den umgelenkten Sternpfaden}, beide Hälften.
--tau: schlechte Zellen bleiben tau Zeitscheiben lang schlecht (Schläuche entlang der Zeit).
Aufruf: python3 skelett_umwege.py [--tau 1 4 16 64] [--q 0 0.01 0.03 0.1 0.2] [--A 16] [--beta 0.25] [--w 2048] [--proben 20000]
"""
import argparse
import json
import os
import time

import numpy as np
from numba import njit

HIER = os.path.dirname(os.path.abspath(__file__))


@njit(cache=True)
def _seed(s):
    np.random.seed(s)


@njit(cache=True)
def pfad(h, beta):
    c = (1.0 - 2.0 ** (-beta)) / 2.0
    v = np.zeros(h)
    lmax = 0
    while (1 << lmax) < h:
        lmax += 1
    for l in range(lmax + 1):
        nb = ((h - 1) >> l) + 1
        U = 2.0 * np.random.random(nb) - 1.0
        gew = c * 2.0 ** (-l * beta)
        for i in range(h):
            v[i] += gew * U[i >> l]
    Z = np.zeros(h + 1)
    for i in range(h):
        Z[i + 1] = Z[i] + v[i]
    return Z


@njit(cache=True)
def schlecht(x, y, t, seed, schwelle, tau=1):
    if tau > 1:                                           # Persistenz: Blöcke der Länge tau, Phase je Platz
        ph = ((x * 92821 + y * 68917 + seed * 7919) % tau + tau) % tau
        t = (t + ph) // tau
    z = np.uint64(x * 73856093) ^ np.uint64(y * 19349663) ^ np.uint64(t * 83492791) ^ np.uint64(seed * 2654435761)
    z = (z ^ (z >> np.uint64(33))) * np.uint64(0xff51afd7ed558ccd)
    z = (z ^ (z >> np.uint64(33))) * np.uint64(0xc4ceb9fe1a85ec53)
    z = z ^ (z >> np.uint64(33))
    return z < schwelle


@njit(cache=True)
def umlenken(x, y, t, seed, schwelle, qx, qy, tau):
    """Gute Ersatzzelle für (x, y) in Zeitscheibe t (Komponente per Breitensuche, max. 4096 Zellen)."""
    if not schlecht(x, y, t, seed, schwelle, tau):
        return x, y
    n = 1
    qx[0] = x
    qy[0] = y
    k = 0
    bx, by, bd = 0, 0, 1 << 30
    while k < n:
        cx, cy = qx[k], qy[k]
        k += 1
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = cx + dx, cy + dy
                if schlecht(nx, ny, t, seed, schwelle, tau):
                    if abs(dx) + abs(dy) == 1:           # Komponente: Nächstnachbarn
                        neu = True
                        for i in range(n):
                            if qx[i] == nx and qy[i] == ny:
                                neu = False
                                break
                        if neu and n < qx.shape[0]:
                            qx[n] = nx
                            qy[n] = ny
                            n += 1
                else:                                    # gute Randzelle (Sup-Norm-Nachbar)
                    d = (nx - x) ** 2 + (ny - y) ** 2
                    if d < bd or (d == bd and (nx < bx or (nx == bx and ny < by))):
                        bx, by, bd = nx, ny, d
    return bx, by


@njit(cache=True)
def segment(x0, y0, x1, y1, t, seed, schwelle, buf, qx, qy, tau):
    n = 0
    sx = 1 if x1 >= x0 else -1
    x, y = x0, y0
    while True:
        ux, uy = umlenken(x, y, t, seed, schwelle, qx, qy, tau)
        buf[n, 0] = ux
        buf[n, 1] = uy
        n += 1
        if x == x1:
            break
        x += sx
    sy = 1 if y1 >= y0 else -1
    while y != y1:
        y += sy
        ux, uy = umlenken(x1, y, t, seed, schwelle, qx, qy, tau)
        buf[n, 0] = ux
        buf[n, 1] = uy
        n += 1
    return n


@njit(cache=True)
def zaehle(w, beta, A, R, proben, q, seed0, tau):
    h = w // 2
    schwelle = np.uint64(q * 18446744073709551615.0) if q > 0 else np.uint64(0)
    J = np.zeros(proben, dtype=np.int64)
    s1 = np.zeros((8192, 2), dtype=np.int64)
    s2 = np.zeros((8192, 2), dtype=np.int64)
    qx = np.zeros(4096, dtype=np.int64)
    qy = np.zeros(4096, dtype=np.int64)
    for p in range(proben):
        seed = seed0 + p                                  # neue Umgebung je Probe, gleiche für beide Routen
        Zx1, Zy1, Zx2, Zy2 = pfad(h, beta), pfad(h, beta), pfad(h, beta), pfad(h, beta)
        tot = 0
        for t in range(h):
            a0x = int(np.round(A * Zx1[t])); a0y = int(np.round(A * Zy1[t]))
            a1x = int(np.round(A * Zx1[t + 1])); a1y = int(np.round(A * Zy1[t + 1]))
            b0x = int(np.round(A * Zx2[t])); b0y = int(np.round(A * Zy2[t]))
            b1x = int(np.round(A * Zx2[t + 1])); b1y = int(np.round(A * Zy2[t + 1]))
            if (max(a0x, a1x) + R + 3 < min(b0x, b1x) or max(b0x, b1x) + R + 3 < min(a0x, a1x) or
                    max(a0y, a1y) + R + 3 < min(b0y, b1y) or max(b0y, b1y) + R + 3 < min(a0y, a1y)):
                continue
            n1 = segment(a0x, a0y, a1x, a1y, t, seed, schwelle, s1, qx, qy, tau)
            n2 = segment(b0x, b0y, b1x, b1y, t, seed, schwelle, s2, qx, qy, tau)
            for i in range(n1):
                for j in range(n2):
                    if abs(s1[i, 0] - s2[j, 0]) <= R and abs(s1[i, 1] - s2[j, 1]) <= R:
                        tot += 1
        J[p] = 2 * tot
    return J


def kennzahlen(J):
    J = np.asarray(J, dtype=float)
    res = {'mittel': float(J.mean()), 'q99': float(np.quantile(J, 0.99))}
    n1, n2 = np.quantile(J, 0.9), np.quantile(J, 0.999)
    ns = np.linspace(n1, n2, 12)
    P = np.array([(J >= n).mean() for n in ns])
    ok = P > 0
    res['alpha_max'] = float(-np.polyfit(ns[ok], np.log(P[ok]), 1)[0]) if ok.sum() > 3 and n2 > n1 else float('nan')
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--q', type=float, nargs='+', default=[0.0, 0.01, 0.03, 0.1, 0.2])
    ap.add_argument('--A', type=float, default=16.0)
    ap.add_argument('--beta', type=float, default=0.25)
    ap.add_argument('--w', type=int, default=2048)
    ap.add_argument('--proben', type=int, default=20000)
    ap.add_argument('--R', type=int, default=1)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--tau', type=int, nargs='+', default=[1], help='Persistenz schlechter Zellen in Zeitscheiben')
    a = ap.parse_args()
    _seed(a.seed)
    alle = []
    for tau in a.tau:
      for q in a.q:
        t0 = time.time()
        J = zaehle(a.w, a.beta, a.A, a.R, a.proben, q, 1000 * a.seed, tau)
        k = kennzahlen(J)
        alle.append(dict(q=q, tau=tau, A=a.A, beta=a.beta, w=a.w, R=a.R, proben=a.proben, **k))
        print(f"tau={tau:4d} q={q:5.3f} A={a.A:g} beta={a.beta:g}: E J_A = {k['mittel']:8.2f}  q99 {k['q99']:7.0f}  "
              f"alpha_max = {k['alpha_max']:.4f}   [{time.time() - t0:.0f} s]", flush=True)
    with open(os.path.join(HIER, 'ergebnisse', f'skelett_umwege_A{a.A:g}_tau{"-".join(map(str, a.tau))}.json'), 'w') as fh:
        json.dump(alle, fh, indent=1)


if __name__ == '__main__':
    main()
