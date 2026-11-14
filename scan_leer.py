#!/usr/bin/env python3
"""Lochkosten im Wurm: Wahrscheinlichkeit, dass ein h x h-Block eine Zeit tau lang leer bleibt (harte Bosonen, 2D).

Im Z-Sektor (geschlossene Weltlinien, wurm_nb4) ist die Blockbesetzung n_Q(t) stückweise konstant; aus den Ereignissen
der Blockplätze (jeder Sprung kippt die Besetzung eines Platzes) folgen die maximalen Leer-Intervalle (periodisch in beta).
    P(tau) = sum_Intervalle max(0, Länge - tau) / beta,   gemittelt über alle L^2 Blocklagen und Konfigurationen.
Für großes tau erwartet: -ln P(tau) ~ c0 + tau * Delta E (Feynman-Kac, Lochenergie im thermodynamischen Limes).
Großkanonisch mit festem mu aus Runde 1. Ausgabe je Block: P(tau) auf einem tau-Gitter, dazu Kontrolle <n_Q>.
Aufruf: python3 scan_leer.py L beta --rho 0.0625 --mu-von ergebnisse/bos_L32_b64_r0.0625_s1.json --h 4 6 8 [--stunden 8]
"""
import argparse
import json
import os
import sys
import time

import numpy as np
from numba import njit

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, '..', 'z2', 'weltlinien'))
import wurm_nb4 as wn  # noqa: E402
from gitter_bosonen import quadratgitter  # noqa: E402


@njit(cache=True)
def leer_statistik(tim, cnt, n0, L, h, beta, taus, S, nmit):
    """Addiert zu S[k] die Summe über alle Blocklagen und Leer-Intervalle von max(0, Länge - taus[k]);
    zu nmit[0] das Zeitintegral der Blockbesetzung (Kontrolle), zu nmit[1] die Zahl der Blöcke."""
    K = taus.shape[0]
    maxev = 0
    for q in range(L * L):
        maxev += cnt[q]
    zt = np.empty(maxev + 1)
    zs = np.empty(maxev + 1, dtype=np.int64)
    zustand = np.zeros(L * L, dtype=np.int64)
    for bx in range(L):
        for by in range(L):
            m = 0
            n = 0
            for i in range(h):
                for j in range(h):
                    q = ((bx + i) % L) * L + (by + j) % L
                    zustand[q] = n0[q]
                    n += n0[q]
                    for e in range(cnt[q]):
                        zt[m] = tim[q, e]
                        zs[m] = q
                        m += 1
            ordnung = np.argsort(zt[:m])
            # Laufende Besetzung; Leer-Intervalle; periodisch: Intervall über beta -> 0 zusammenfügen
            t_prev = 0.0
            integral = 0.0
            erstes_leer = -1.0          # Länge des Leer-Intervalls ab 0 (falls n(0) = 0)
            leer_start = 0.0 if n == 0 else -1.0
            for k in range(m):
                e = ordnung[k]
                t = zt[e]
                integral += n * (t - t_prev)
                q = zs[e]
                zustand[q] = 1 - zustand[q]
                n_neu = n + (1 if zustand[q] == 1 else -1)
                if n == 0 and n_neu > 0:
                    laenge = t - leer_start
                    if leer_start == 0.0 and erstes_leer < 0.0:
                        erstes_leer = laenge
                    else:
                        for kk in range(K):
                            if laenge > taus[kk]:
                                S[kk] += laenge - taus[kk]
                if n > 0 and n_neu == 0:
                    leer_start = t
                n = n_neu
                t_prev = t
            integral += n * (beta - t_prev)
            if n == 0:
                laenge = beta - leer_start
                if erstes_leer >= 0.0:
                    laenge += erstes_leer
                    erstes_leer = -1.0
                if m == 0:
                    laenge = beta                # ganz leer: zählt mit Länge beta (Obergrenze)
                for kk in range(K):
                    if laenge > taus[kk]:
                        S[kk] += laenge - taus[kk]
            if erstes_leer >= 0.0:
                for kk in range(K):
                    if erstes_leer > taus[kk]:
                        S[kk] += erstes_leer - taus[kk]
            nmit[0] += integral / beta
            nmit[1] += 1.0
            for i in range(h):
                for j in range(h):
                    q = ((bx + i) % L) * L + (by + j) % L
                    zustand[q] = 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('L', type=int)
    ap.add_argument('beta', type=float)
    ap.add_argument('--rho', type=float, required=True)
    ap.add_argument('--mu-von', required=True)
    ap.add_argument('--h', type=int, nargs='+', default=[4, 6, 8])
    ap.add_argument('--stunden', type=float, default=8.0)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--schritte', type=float, default=200.0, help='Schritte zwischen Messungen in Einheiten M*beta')
    a = ap.parse_args()
    L, beta = a.L, a.beta
    g = quadratgitter(L)
    M = g['M']
    mu = float(json.load(open(a.mu_von))['mu'])
    s = wn.neu(g, max(1, int(round(a.rho * M))), beta, mu=mu, kanonisch=False, seed=a.seed)
    s['p'] = np.array([x * 0.95 for x in (0.25, 0.2, 0.2, 0.1, 0.1, 0.15)] + [0.05])
    wn.seed_rng(a.seed)
    taus = np.concatenate([[0.0], np.geomspace(0.25, beta / 2, 40)])
    S = {h: np.zeros(taus.size) for h in a.h}
    nmit = {h: np.zeros(2) for h in a.h}
    name = f"leer_L{L}_b{beta:g}_r{a.rho:g}_s{a.seed}"
    out = os.path.join(HIER, 'ergebnisse', name + '.json')
    t0 = time.time()
    for _ in range(12):
        wn.lauf(s, int(1000 * M * beta), 5)
    mess = 0
    nN = 0.0
    while time.time() - t0 < a.stunden * 3600:
        acc = wn.lauf(s, int(a.schritte * M * beta), 5)
        if s['iv'][wn.I_HEAD] >= 0:
            continue                                   # nur geschlossene Konfigurationen
        for h in a.h:
            leer_statistik(s['tim'], s['cnt'], s['n0'].astype(np.int64), L, h, beta, taus, S[h], nmit[h])
        mess += 1
        nN += s['iv'][wn.I_N0]
        if mess % 20 == 0:
            speichern(out, L, beta, a, mu, mess, nN, taus, t0, S, nmit)
    speichern(out, L, beta, a, mu, mess, nN, taus, t0, S, nmit)
    print(f"{name}: {mess} Messungen", flush=True)


def speichern(out, L, beta, a, mu, mess, nN, taus, t0, S, nmit):
    if mess == 0:
        return
    if True:
        if True:
            res = {'L': L, 'beta': beta, 'rho_ziel': a.rho, 'mu': mu, 'seed': a.seed, 'messungen': mess,
                   'N_mittel': nN / mess, 'taus': taus.tolist(), 'zeit_s': time.time() - t0,
                   'bloecke': {str(h): {'S': S[h].tolist(), 'n_mittel': float(nmit[h][0] / max(nmit[h][1], 1)),
                                        'anzahl': float(nmit[h][1]),
                                        'P': (S[h] / (beta * max(nmit[h][1], 1))).tolist()} for h in a.h}}
            with open(out, 'w') as fh:
                json.dump(res, fh)


if __name__ == '__main__':
    main()
