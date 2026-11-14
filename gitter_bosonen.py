"""Harte Bosonen auf dem L x L-Quadratgitter (periodisch) im Format von z2/weltlinien/gitter.py.

Plätze s = x + L y, Nachbarn = vier Nächstnachbarn, keine erweiterten Ausschlusslisten (der Ausschluss auf demselben
Platz steckt in der Weltliniendarstellung). H = -t sum_<xy> (b_x^+ b_y + h.c.) - mu N.
"""
import numpy as np


def quadratgitter(L):
    M = L * L
    mid = [(float(s % L), float(s // L)) for s in range(M)]
    schritte = ((1, 0), (-1, 0), (0, 1), (0, -1))
    eck = [[((s % L + dx) % L) + L * ((s // L + dy) % L) for dx, dy in schritte] for s in range(M)]
    eck_d = [[[float(dx), float(dy)] for dx, dy in schritte] for _ in range(M)]

    def mindisp(a, b):
        return [(mid[b][i] - mid[a][i] + L / 2) % L - L / 2 for i in range(2)]

    return {'L': L, 'M': M, 'mid': mid, 'konflikt': [[] for _ in range(M)],
            'eck': np.array(eck, dtype=np.int64), 'eck_d': np.array(eck_d), 'mindisp': mindisp}
