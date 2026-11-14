#!/usr/bin/env python3
"""Exakte Prüfung der Dichteformel des zeitartigen Staffellaufs (Anhang Gegen-Lücke, Lemma G1) an einem Mini-System.

Modell: harte Bosonen auf dem Ring Z_L, Weltlinien in diskreter Zeit (Trotter: gerade Bindungen, dann ungerade),
Gewicht lam^(Zahl der Sprünge), periodisch in der Zeit (Spur über beta Schritte). Zellen = Paare von Plätzen.
Lücke von Zeit 0 bis T = w Scheiben (Scheibe = s Schritte).

Vorwärts (wie §9 der OpenAI-Arbeit „density-uniform“, angepasst an die Lücke):
  geschlossene Geschichte omega ~ P;  Schwanz-Teilchen gleichverteilt (1/N);  je Scheibe Zug d (Route);
  j0 = Teilchen am Loch (muss wählbar sein), j_l gleichverteilt unter den wählbaren Teilchen der Zelle c_l;
  Stück von j0 löschen, Brücken S_l -> Y_{l-1} aus dem exakt bedingten Gesetz neu ziehen.  -> Lücken-Geschichte O.
Rückwärts (Dichteformel):  f(O) = (M/N) * sum_{Route, Lochplätze, Tupel} pi(R) * prod_k sel_k * Zalt_k / Zbr_k,
  Gamma(O) = lam^hops(O) / (M Z_N).   Geprüft wird nu(O) = f(O) Gamma(O) für alle O.
Aufruf: python3 pruef_gegenluecke.py [--L 6] [--N 3] [--beta 4] [--w 2] [--lam 0.7]
"""
import argparse
import itertools
from collections import defaultdict

import numpy as np


def baue(L):
    gerade = [(i, i + 1) for i in range(0, L, 2)]
    ungerade = [(i, (i + 1) % L) for i in range(1, L, 2)]
    return gerade, ungerade


def bindungen(h, B):
    return B[0] if h % 2 == 0 else B[1]


def uebergaenge(conf, h, B):
    """Alle Folgekonfigurationen (frozenset) nach Halbschritt h mit Zahl der Sprünge."""
    wahl = []
    for (i, j) in bindungen(h, B):
        a, b = i in conf, j in conf
        if a != b:
            wahl.append((i, j))
    erg = []
    for maske in itertools.product((0, 1), repeat=len(wahl)):
        neu = set(conf)
        for (i, j), springt in zip(wahl, maske):
            if springt:
                if i in neu:
                    neu.remove(i); neu.add(j)
                else:
                    neu.remove(j); neu.add(i)
        erg.append((frozenset(neu), sum(maske)))
    return erg


def spruenge(c0, c1, h, B):
    """Zahl der Sprünge zwischen zwei Konfigurationen im Halbschritt h (None, falls unzulässig)."""
    n = 0
    for (i, j) in bindungen(h, B):
        vor = (i in c0, j in c0); nach = (i in c1, j in c1)
        if sum(vor) != sum(nach):
            return None
        if vor != nach:
            if sum(vor) != 1:
                return None
            n += 1
    alle = {x for b in bindungen(h, B) for x in b}
    if (c0 - alle) or (c1 - alle):
        return None
    return n


def bahnen(confs, t0, t1, h0, B):
    """Verfolgt die Teilchen von Zeit t0 bis t1: Liste von Trajektorien (Tupel der Plätze)."""
    tr = [[p] for p in sorted(confs[t0])]
    for t in range(t0, t1):
        h = h0 + (t - t0)
        nachher = confs[t + 1]
        for bahn in tr:
            p = bahn[-1]
            for (i, j) in bindungen(h, B):
                if p in (i, j):
                    q = j if p == i else i
                    if p in nachher:
                        bahn.append(p)
                    else:
                        assert q in nachher and q not in confs[t]
                        bahn.append(q)
                    break
    return [tuple(b) for b in tr]


def beweger(starts, enden, andere_occ, h0, B, aufzaehlen=False):
    """Summe (oder Liste) über Geschichten markierter Teilchen starts[l] -> enden[l] durch die Halbschritte
    h0, h0+1, ... bei festen anderen Teilchen (andere_occ[t] = Menge zur Zeit t der Scheibe). Gewicht lam^Sprünge
    wird als Sprungzahl zurückgegeben."""
    n = len(starts)
    schritte = len(andere_occ) - 1
    if n == 0:
        return [((), 0)] if aufzaehlen else {0: 1}
    zust = {tuple(starts): [((tuple(starts),), 0)]} if aufzaehlen else {tuple(starts): {0: 1}}
    for t in range(schritte):
        h = h0 + t
        neu = defaultdict(list) if aufzaehlen else defaultdict(lambda: defaultdict(int))
        for pos, daten in zust.items():
            optionen = []
            for p in pos:
                for (i, j) in bindungen(h, B):
                    if p in (i, j):
                        optionen.append([p, j if p == i else i])
                        break
            for wahl in itertools.product((0, 1), repeat=n):
                nach = tuple(opt[w] for opt, w in zip(optionen, wahl))
                if len(set(nach)) < n:
                    continue
                c0 = frozenset(pos) | andere_occ[t]
                c1 = frozenset(nach) | andere_occ[t + 1]
                if len(c0) != len(pos) + len(andere_occ[t]) or len(c1) != len(nach) + len(andere_occ[t + 1]):
                    continue
                hs = spruenge(c0, c1, h, B)
                if hs is None:
                    continue
                k = sum(wahl)
                if hs != k + _spr_andere(andere_occ[t], andere_occ[t + 1], h, B):
                    continue
                if aufzaehlen:
                    for (wege, kk) in daten:
                        neu[nach].append((wege + (nach,), kk + k))
                else:
                    for kk, v in daten.items():
                        neu[nach][kk + k] += v
        zust = neu
    ziel = tuple(enden)
    if aufzaehlen:
        return zust.get(ziel, [])
    return dict(zust.get(ziel, {}))


def _spr_andere(a0, a1, h, B):
    n = 0
    for (i, j) in bindungen(h, B):
        if (i in a0, j in a0) != (i in a1, j in a1):
            n += 1
    return n


def wert(poly, lam):
    return sum(v * lam ** k for k, v in poly.items())


def zelle(i):
    return i // 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--L', type=int, default=6)
    ap.add_argument('--N', type=int, default=3)
    ap.add_argument('--beta', type=int, default=4, help='Schritte (je 2 Halbschritte)')
    ap.add_argument('--w', type=int, default=2, help='Scheiben der Lücke, je 1 Schritt')
    ap.add_argument('--lam', type=float, default=0.7)
    a = ap.parse_args()
    L, N, lam = a.L, a.N, a.lam
    K = L // 2
    B = baue(L)
    H = 2 * a.beta                     # Halbschritte gesamt
    Tidx = 2 * a.w                     # Index der Zeit T
    zuege = {-1: 0.25, 0: 0.3, 1: 0.25, 2: 0.2}    # Routengesetz je Scheibe

    def zellen_stern(a0, d):
        s = 1 if d > 0 else -1
        return [(a0 + l * s) % K for l in range(abs(d) + 1)]

    # --- alle geschlossenen Geschichten
    confs0 = [frozenset(c) for c in itertools.combinations(range(L), N)]
    trans = {(c, h % 2): uebergaenge(c, h, B) for c in confs0 for h in (0, 1)}
    geschichten = []

    def dfs(weg, k):
        h = len(weg) - 1
        if h == H:
            if weg[-1] == weg[0]:
                geschichten.append((tuple(weg[:-1]), k))
            return
        for (c1, n) in trans[(weg[-1], h % 2)]:
            dfs(weg + [c1], k + n)
    for c in confs0:
        dfs([c], 0)
    ZN = sum(lam ** k for _, k in geschichten)
    print(f"geschlossene Geschichten: {len(geschichten)}, Z_N = {ZN:.6f}")

    # --- Vorwärts: nu(O) durch vollständige Aufzählung
    nu = defaultdict(float)
    for confs, kh in geschichten:
        conf = list(confs) + [confs[0]]
        P = lam ** kh / ZN
        stuecke = [bahnen(conf, 2 * k, 2 * k + 2, 2 * k, B) for k in range(a.w)]

        def scheibe(k, j0bahn_start, faktor, neue_confs):
            """Rekursion über die Scheiben; j0bahn_start = Startplatz des zu löschenden Stücks."""
            if k == a.w:
                y = j0bahn_start
                x = neue_confs['x']
                O = [None] * H
                for t in range(H):
                    if t in neue_confs:
                        O[t] = neue_confs[t]
                    else:
                        O[t] = conf[t]
                O[Tidx] = conf[Tidx] - {y}
                O[0] = conf[0] - {x}
                schl = (x, y, tuple(O))
                nu[schl] += faktor
                return
            st = stuecke[k]
            j0 = [b for b in st if b[0] == j0bahn_start]
            assert len(j0) == 1
            j0 = j0[0]
            a0 = zelle(j0[0])
            if zelle(j0[-1]) != a0:
                return                                       # j0 nicht wählbar: verwerfen
            for d, pd in zuege.items():
                cz = zellen_stern(a0, d)
                m = abs(d)
                waehlbar = [[b for b in st if zelle(b[0]) == c and zelle(b[-1]) == c and b is not j0] for c in cz[1:]]
                if any(len(wl) == 0 for wl in waehlbar):
                    continue
                for tup in itertools.product(*waehlbar):
                    if len(set(tup)) < m:
                        continue
                    sel = 1.0
                    for wl in waehlbar:
                        sel /= len(wl)
                    I = (j0,) + tup
                    andere = [b for b in st if all(b is not i for i in I)]
                    occ = [frozenset(b[t] for b in andere) for t in range(3)]
                    starts = [I[l][0] for l in range(1, m + 1)]
                    enden = [I[l - 1][-1] for l in range(1, m + 1)]
                    wege = beweger(starts, enden, occ, 2 * k, B, aufzaehlen=True)
                    Zbr = sum(lam ** kk for _, kk in wege)
                    if Zbr == 0:
                        continue
                    for (wg, kk) in wege:
                        nc = dict(neue_confs)
                        for t in range(3):
                            pos = set(occ[t]) | (set(wg[t]) if m > 0 else set())
                            nc[2 * k + t] = frozenset(pos)
                        loch_oben = I[m][-1]
                        scheibe(k + 1, loch_oben, faktor * pd * sel * lam ** kk / Zbr, nc)

        for xstart in sorted(conf[0]):
            scheibe(0, xstart, P / N, {'x': xstart})

    print(f"Lücken-Konfigurationen mit nu > 0: {len(nu)}, |nu| = {sum(nu.values()):.6f}")

    # --- Rückwärts: Dichteformel
    M = L

    def gamma(O):
        x, y, confs = O
        k = 0
        for t in range(H):
            c0 = confs[t]
            c1 = confs[(t + 1) % H]
            if t == Tidx:
                c0 = c0 | {y}
            if t == H - 1:
                c1 = c1 | {x}
            if t == 0:
                pass
            n = spruenge(c0, c1, t, B)
            if n is None:
                return 0.0
            k += n
        return lam ** k / (M * ZN)

    def f_formel(O):
        x, y, confs = O
        conf = list(confs) + [confs[0] | {x}]
        summe = 0.0
        a0 = zelle(x)
        for ds in itertools.product(list(zuege), repeat=a.w):
            zs = [a0]
            for d in ds:
                zs.append(zellen_stern(zs[-1], d)[-1])
            if zs[-1] != zelle(y):
                continue
            pi = np.prod([zuege[d] for d in ds])
            loch_opt = [[x]] + [[p for p in range(L) if zelle(p) == zs[k] and p not in conf[2 * k]]
                                for k in range(1, a.w)] + [[y]]
            for loecher in itertools.product(*loch_opt):
                prod_k = 1.0
                for k in range(a.w):
                    d = ds[k]; m = abs(d)
                    cz = zellen_stern(zs[k], d)
                    st = bahnen(conf, 2 * k, 2 * k + 2, 2 * k, B)
                    kand = [[b for b in st if zelle(b[0]) == cz[l] and zelle(b[-1]) == cz[l - 1]]
                            for l in range(1, m + 1)]
                    teil = 0.0
                    for br in itertools.product(*kand):
                        if len(set(br)) < m:
                            continue
                        andere = [b for b in st if all(b is not q for q in br)]
                        occ = [frozenset(b[t] for b in andere) for t in range(3)]
                        S = [loecher[k]] + [b[0] for b in br]
                        Y = [b[-1] for b in br] + [loecher[k + 1]]
                        if any(zelle(S[l]) != cz[l] or zelle(Y[l]) != cz[l] for l in range(m + 1)):
                            continue
                        sel = 1.0
                        for l in range(1, m + 1):
                            g = sum(1 for b in andere if zelle(b[0]) == cz[l] and zelle(b[-1]) == cz[l]) + 1
                            sel /= g
                        Zalt = wert(beweger(S, Y, occ, 2 * k, B), lam)
                        Zbr = wert(beweger([b[0] for b in br], [b[-1] for b in br], occ, 2 * k, B), lam)
                        teil += sel * Zalt / Zbr
                    prod_k *= teil
                    if prod_k == 0:
                        break
                summe += pi * prod_k
        return (M / N) * summe

    fehler = 0.0
    zweit = 0.0
    for O, v in nu.items():
        g = gamma(O)
        f = f_formel(O)
        fehler = max(fehler, abs(v - f * g) / v)
        zweit += v * f
    print(f"größter relativer Fehler nu(O) gegen f(O) Gamma(O): {fehler:.2e}")
    # Masse von Gamma exakt aus Transfermatrizen
    def sektor(n):
        cs = [frozenset(c) for c in itertools.combinations(range(L), n)]
        return cs, {c: i for i, c in enumerate(cs)}
    csN, iN = sektor(N); csM, iM = sektor(N - 1)

    def transfer(cs, idx, h):
        Tm = np.zeros((len(cs), len(cs)))
        for c in cs:
            for (c1, n) in uebergaenge(c, h, B):
                Tm[idx[c], idx[c1]] += lam ** n
        return Tm
    weg = np.zeros((len(csN), len(csM)))            # Entnahme: N -> N-1
    for c in csN:
        for x in c:
            weg[iN[c], iM[c - {x}]] += 1.0
    dazu = weg.T.copy()                             # Einsetzen: N-1 -> N
    prod = weg.copy()
    for h in range(Tidx):
        prod = prod @ transfer(csM, iM, h)
    prod = prod @ dazu
    for h in range(Tidx, H):
        prod = prod @ transfer(csN, iN, h)
    Gmasse = np.trace(prod) / (M * ZN)
    Gsum = sum(gamma(O) for O in nu)
    numasse = sum(nu.values())
    print(f"|Gamma| = {Gmasse:.6f} (davon auf dem Träger von nu: {Gsum:.6f}),  |nu| = {numasse:.6f}")
    print(f"zweites Moment int f^2 dGamma = {zweit:.6f};  Cauchy-Schwarz: |nu|^2/int f^2 = {numasse**2 / zweit:.6f} "
          f"<= |Gamma| = {Gmasse:.6f}")


if __name__ == '__main__':
    main()
