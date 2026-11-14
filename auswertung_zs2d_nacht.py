#!/usr/bin/env python3
"""Auswertung des Nachtlaufs zs2d_nacht.sh: ∫f²dµ = |ν|·E[f|ang.] je (m, Variante, w), Wachstumsfaktoren je Scheibe.

Fehler: |ν| binomial, E[f] über Blockmittel (20 Blöcke) wegen schwerer Schwänze; ∫f² mit Fehlerfortpflanzung.
Aufruf: python3 auswertung_zs2d_nacht.py [Ordner]
"""
import re
import sys

import numpy as np

ordner = sys.argv[1] if len(sys.argv) > 1 else 'ergebnisse/zs2d_nacht'
systeme = ['m1', 'm1.5', 'm3']
mwert = {'m1': 1.0, 'm1.5': 1.5, 'm3': 3.0}
varianten = ['a', 'zgq', 'festl', 'zg', 'ballqR1', 'ballqR2', 'ballqR3', 'ballR1', 'ballR2', 'ballR3',
             'bnR1', 'bnR2', 'bnR3', 'freinq', 'frei', 'zelle']
namen = {'a': 'Variante a', 'zgq': 'zellgew. + Quer', 'festl': 'festzelle locker', 'zg': 'zellgewicht',
         'frei': 'frei', 'zelle': 'zelle',
         **{f'ballR{R}': f'Ball R={R}' for R in (1, 2, 3)}, **{f'ballqR{R}': f'Ball R={R} + Quer' for R in (1, 2, 3)},
         **{f'bnR{R}': f'Ball R={R} nie quer' for R in (1, 2, 3)}, 'freinq': 'frei nie quer'}


def lade(s, v, w):
    d = np.load(f'{ordner}/{s}_{v}_w{w}.npy')
    proben, ang = int(d[0]), int(d[1])
    f = d[2:]
    txt = open(f'{ordner}/{s}_{v}_w{w}.txt').read()
    q0 = float(re.search(r'q0 = \|µ\| = ([0-9.]+)', txt).group(1))
    # Endstand der Textdatei kann mehr Proben haben als die letzte Sicherung
    m = re.findall(r'mc: Proben (\d+), \|ν\| = ([0-9.]+)', txt)
    return proben, ang, f, q0


def blockfehler(f, nb=20):
    n = len(f) // nb
    if n < 2:
        return f.std(ddof=1) / np.sqrt(max(len(f), 1))
    bm = f[:n * nb].reshape(nb, n).mean(axis=1)
    return bm.std(ddof=1) / np.sqrt(nb)


erg = {}
for s in systeme:
    for v in varianten:
        for w in range(1, 5):
            try:
                proben, ang, f, q0 = lade(s, v, w)
            except (FileNotFoundError, AttributeError, ValueError):
                continue
            if len(f) < 2:
                continue
            p = ang / proben
            sp = np.sqrt(p * (1 - p) / proben)
            ef = f.mean()
            sf = blockfehler(f)
            I = p * ef
            sI = I * np.sqrt((sp / p) ** 2 + (sf / ef) ** 2)
            erg[(s, v, w)] = dict(proben=proben, ang=ang, p=p, ef=ef, sf=sf, I=I, sI=sI, q0=q0,
                                  eff=p / ef / q0, med=np.median(f), mx=f.max(),
                                  anteil_max=f.max() / f.sum())

print(f"Nachtlauf {ordner}: ∫f²dµ = |ν|·E[f|ang.]; Fehler E[f] aus 20 Blockmitteln\n")
print(f"{'System':6s} {'Variante':17s} {'w':>2s} {'Proben':>8s} {'|ν|':>7s} {'E[f]':>18s} {'∫f²dµ':>18s} "
      f"{'Eff.':>7s} {'Median f':>9s} {'max f':>9s} {'max/Σf':>7s}")
for s in systeme:
    for v in varianten:
        for w in range(1, 5):
            e = erg.get((s, v, w))
            if not e:
                continue
            print(f"{s:6s} {namen[v]:17s} {w:2d} {e['proben']:8d} {e['p']:7.4f} {e['ef']:9.4g} ± {e['sf']:6.2g} "
                  f"{e['I']:9.4g} ± {e['sI']:6.2g} {e['eff']:7.4f} {e['med']:9.3g} {e['mx']:9.3g} {e['anteil_max']:7.4f}")
        if any((s, v, w) in erg for w in range(1, 5)):
            print()

print("Wachstumsfaktoren von ∫f²dµ je Scheibe (w → w+1) und geometrisches Mittel über w = 1..4:\n")
print(f"{'Variante':17s} " + " ".join(f"{s:>30s}" for s in systeme))
for v in varianten:
    zeile = f"{namen[v]:17s} "
    if not any((s, v, 1) in erg for s in systeme):
        continue
    for s in systeme:
        fak = []
        for w in range(1, 4):
            a_, b_ = erg.get((s, v, w)), erg.get((s, v, w + 1))
            if a_ and b_:
                fak.append(b_['I'] / a_['I'])
        gm = (erg[(s, v, 4)]['I'] / erg[(s, v, 1)]['I']) ** (1 / 3) if (s, v, 4) in erg and (s, v, 1) in erg else float('nan')
        zeile += f"{' '.join(f'{x:5.2f}' for x in fak):>22s} | {gm:5.2f} "
    print(zeile)

print("\nPrüfung der Vorhersage aus Z.8: (Faktor − 1)·m (geometrisches Mittel über w = 1..4) — konstant, falls ~1/m:\n")
for v in varianten:
    zeile = f"{namen[v]:17s} "
    if not any((s, v, 1) in erg for s in systeme):
        continue
    for s in systeme:
        if (s, v, 4) in erg and (s, v, 1) in erg:
            gm = (erg[(s, v, 4)]['I'] / erg[(s, v, 1)]['I']) ** (1 / 3)
            zeile += f"  m={mwert[s]:3.1f}: (F−1) = {gm - 1:6.3f}, (F−1)·m = {(gm - 1) * mwert[s]:6.3f}"
    print(zeile)
