"""Stufe A als Modell harter Bosonen auf dem Mittelgitter (Bindungsmitten des L x L-Quadratgitters, periodisch).

Plätze m = Bindungen k = 0..2N-1 (k < N waagerecht von Platz s=k nach s+x, sonst senkrecht von s=k-N nach s+y).
Nachbarn = Eckschritte (zwei Bindungen mit gemeinsamem Platz im rechten Winkel), 4 pro Platz.
Ausschluss: zwei Paare dürfen sich nicht berühren (kein Platz der einen Bindung gleich oder Nachbar eines Platzes der
anderen); 22 ausgeschlossene Bindungen pro Bindung.
Hamiltonoperator in der d-Eichung: H = -t * sum_{Eckschritte} (b^dag_m' b_m + h.c.) (Konstante weggelassen).
Verschiebung eines Eckschritts in Einheiten der Gitterkonstante: (+-1/2, +-1/2).
"""
import numpy as np


def site(x, y, L):
    return (x % L) + L * (y % L)


def mittelgitter(L):
    N = L * L
    bonds = [(s, site(s % L + 1, s // L, L)) for s in range(N)] + [(s, site(s % L, s // L + 1, L)) for s in range(N)]
    mid = [((s % L) + 0.5, float(s // L)) for s in range(N)] + [(float(s % L), (s // L) + 0.5) for s in range(N)]
    nbr_sites = [[site(x + 1, y, L), site(x - 1, y, L), site(x, y + 1, L), site(x, y - 1, L)]
                 for x, y in ((s % L, s // L) for s in range(N))]
    zone = [{u, v} | set(nbr_sites[u]) | set(nbr_sites[v]) for u, v in bonds]
    M = 2 * N
    konflikt = [sorted(j for j in range(M) if j != k and (zone[k] & set(bonds[j]))) for k in range(M)]
    by_pair = {frozenset(b): k for k, b in enumerate(bonds)}

    def mindisp(a, b):
        d = [(mid[b][i] - mid[a][i] + L / 2) % L - L / 2 for i in range(2)]
        return d

    eck, eck_d = [], []
    for k, (u, v) in enumerate(bonds):
        nb, dd = [], []
        for q, o in ((u, v), (v, u)):
            for w in nbr_sites[q]:
                if w == o:
                    continue
                kk = by_pair.get(frozenset((q, w)))
                if kk is None or kk == k:
                    continue
                # rechter Winkel: w nicht auf der Geraden o-q (dann wäre es dieselbe Orientierung)
                if (k < N) == (kk < N):
                    continue
                nb.append(kk)
                dd.append(mindisp(k, kk))
        assert len(nb) == 4, (k, nb)
        eck.append(nb)
        eck_d.append(dd)
    return {'L': L, 'M': M, 'bonds': bonds, 'mid': mid, 'konflikt': konflikt,
            'eck': np.array(eck, dtype=np.int64), 'eck_d': np.array(eck_d), 'mindisp': mindisp}


def konfigurationen(g, n):
    """Alle berührungsfreien Mengen von n Mittelplätzen (aufsteigend)."""
    M, konf = g['M'], [set(c) for c in g['konflikt']]
    out = []

    def rec(start, chosen, verboten):
        if len(chosen) == n:
            out.append(tuple(chosen))
            return
        for k in range(start, M):
            if k in verboten:
                continue
            rec(k + 1, chosen + [k], verboten | konf[k] | {k})

    rec(0, [], set())
    return out
