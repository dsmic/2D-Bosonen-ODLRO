#!/usr/bin/env python3
"""Auswertung der Läufe kopfteilen2d_schwanz_start.sh und kopfteilen2d_schwanz_S.sh (ergebnisse/kopfteilen2d_schwanz/).

Je Lauf der letzte Bericht: Zellgröße s² (Plätze je Zelle), Scheibendauer S, m, Proben, ∫f² dµ und die Fortsetzung des
Teilens über Scheibe 0 hinaus, am Kopf (K ≥ 2) und am Schwanz (K_T ≥ 2), jeweils als Anteil von ∫f².
Aufruf: python3 auswertung_kopfteilen2d_schwanz.py [Verzeichnis]
"""
import glob
import os
import re
import sys

d = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ergebnisse',
                                                        'kopfteilen2d_schwanz')
zeilen = []
for f in sorted(glob.glob(os.path.join(d, '*_w*.txt'))):
    t = open(f).read().splitlines()
    m = re.search(r'Gitter (\S+), Zellen (\d+)×(\d+) .*?N=(\d+) \(m = ([\d.]+) je Zelle\), S=(\d+), w=(\d+)', t[0])
    if not m:
        continue
    gitter, cx, cy, N, mm, S, w = m.groups()
    idx = [i for i, z in enumerate(t) if 'Proben' in z and '∫f²' in z]
    if not idx:
        continue
    i = idx[-1]
    ang = int(re.search(r'angenommen (\d+)', t[i]).group(1))
    zf = float(re.search(r'∫f² = \|ν\|·E\[f\] = ([\d.]+)', t[i]).group(1))
    kopf = schwanz = None
    for z in t[i + 1:]:
        mk = re.match(r'\s+K = 1: Anteil A\(K\)/∫f² = ([\d.]+) ± ([\d.]+)', z)
        if mk:
            kopf = (1 - float(mk.group(1)), float(mk.group(2)))
        ms = re.match(r'\s+Schwanz K_T = 1: Anteil = ([\d.]+) ± ([\d.]+)', z)
        if ms:
            schwanz = (1 - float(ms.group(1)), float(ms.group(2)))
    if kopf is None or schwanz is None:
        continue
    s2 = int(cx) * int(cy)
    zeilen.append((int(S), s2, float(mm), f'{gitter}, N = {N}', str(s2), S, mm.replace('.', ','), str(ang),
                   f'{zf:.2f}'.replace('.', ','),
                   f'{kopf[0]:.3f} ± {kopf[1]:.3f}'.replace('.', ','),
                   f'{schwanz[0]:.3f} ± {schwanz[1]:.3f}'.replace('.', ',')))
zeilen.sort()
k = ['System', 's²', 'S', 'm', 'Proben', '∫f²dµ', 'Kopf: Anteil K ≥ 2', 'Schwanz: Anteil K\\_T ≥ 2']
print('| ' + ' | '.join(k) + ' |')
print('|' + '|'.join('-' * (len(x) + 2) for x in k) + '|')
for z in zeilen:
    print('| ' + ' | '.join(z[3:]) + ' |')
