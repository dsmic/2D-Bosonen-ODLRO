#!/usr/bin/env python3
"""Auswertung der Läufe kopfteilen2d_start.sh (ergebnisse/kopfteilen2d/*_w*.txt) als Markdown-Tabelle.

Je Lauf der letzte Bericht: angenommene Proben, ∫f² dµ, der Teil mit k = 0 (K = 1), der Anteil mit k ≥ 1 und A(K) absolut (das letzte Glied ist das Teilen bis zur Wende).
Aufruf: python3 auswertung_kopfteilen2d.py [Verzeichnis]
"""
import glob
import os
import re
import sys

d = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ergebnisse', 'kopfteilen2d')
zeilen = []
for f in sorted(glob.glob(os.path.join(d, '*_w*.txt'))):
    t = open(f).read().splitlines()
    kopf = t[0]
    m = re.search(r'Gitter (\S+), Zellen (\S+) .*?N=(\d+) \(m = ([\d.]+) je Zelle\).*?w=(\d+)', kopf)
    if not m:
        continue
    gitter, zellen, N, mm, w = m.groups()
    idx = [i for i, z in enumerate(t) if 'Proben' in z and '∫f²' in z]
    if not idx:
        continue
    i = idx[-1]
    b = t[i]
    ang = int(re.search(r'angenommen (\d+)', b).group(1))
    zf = re.search(r'∫f² = \|ν\|·E\[f\] = ([\d.]+)', b).group(1)
    ef, sf = re.search(r'E\[f\|ang\.\] = ([\d.]+) ± ([\d.e-]+)', b).groups()
    anteile, fort = {}, {}
    for z in t[i + 1:]:
        mk = re.match(r'\s+K = (\d+): Anteil A\(K\)/∫f² = ([\d.]+) ± ([\d.]+);\s+Fortsetzung A\(>K\)/A\(≥K\) = (-?[\d.]+)', z)
        if not mk:
            break
        K = int(mk.group(1))
        anteile[K] = (float(mk.group(2)), float(mk.group(3)))
        fort[K] = float(mk.group(4))
    rel = float(sf) / float(ef)
    k1 = 1 - anteile[1][0]
    zeilen.append((float(mm), gitter, int(w), f'{gitter}, Zellen {zellen}, N = {N}', mm.replace('.', ','), w, str(ang),
                   f'{float(zf):.2f} ± {float(zf) * rel:.2f}'.replace('.', ','),
                   f'{anteile[1][0] * float(zf):.2f} ± {anteile[1][1] * float(zf):.2f}'.replace('.', ','),
                   f'{k1:.2f} ± {anteile[1][1]:.2f}'.replace('.', ','),
                   ' / '.join(f'{anteile[K][0] * float(zf):.2f}'.replace('.', ',') for K in sorted(anteile))))
zeilen.sort()
kopf = ['System', 'm', 'w', 'Proben', '∫f²dµ', 'Teil mit k = 0', 'Anteil k ≥ 1', 'A(K) für K = 1, 2, … (letzte: Teilen bis zur Wende)']
print('| ' + ' | '.join(kopf) + ' |')
print('|' + '|'.join('-' * (len(k) + 2) for k in kopf) + '|')
for z in zeilen:
    print('| ' + ' | '.join(z[3:]) + ' |')
