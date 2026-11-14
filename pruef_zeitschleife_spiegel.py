#!/usr/bin/env python3
"""Zeitschleife mit gespiegelter Abwärts-Hälfte (Anhang G.11): exakte Prüfung am Mini-Ring.

Modell wie pruef_gegenluecke.py: harte Bosonen auf dem Ring Z_L, Trotter-Zeit, Gewicht lam^Sprünge, Zellen = Paare.
Vorwärts aus einer geschlossenen Geschichte C, Schwanz-Teilchen x gleichverteilt (1/N):
  Aufweg, Scheiben k = 0 … w−1 (wie Tutorial §5.2): j0 = Stück am Loch, c0 = Endzelle von j0 (keine Bedingung an j0),
    Zug d, Sternpfad c0 … c_m, j_l gleichverteilt unter den wählbaren Stücken von c_l (Anfang und Ende in c_l),
    j0 löschen, Brücken j_l: S_l → Y_{l−1} aus dem exakt bedingten Gesetz.  Neues Loch oben bei Y_m.
  Abweg, Scheiben k = w−1 … 0, Variante
    "zelle":   neuer Kopf gleichverteilt unter den freien Plätzen der Zelle des alten Kopfes, Stück exakt bedingt
               (die Fassung aus G.10.5; keine Querschritte);
    "spiegel": Spiegelbild des Aufwegs.  Kopf oben bei Y_0, e0 = Zelle von Y_0, Zug d, Sternpfad e0 … e_m,
               j_l gleichverteilt unter den wählbaren Stücken von e_l; neu gezogen werden gemeinsam die Brücken
               j_l: S_l → Y_{l−1} (Y_l = altes Ende von j_l) und ein neues Stück S' → Y_m mit freiem Anfang S'
               (Summe über alle freien Plätze); neuer Kopf S'.
Ergebnis O: offene Konfiguration zu gleicher Zeit (Schwanz x, Kopf y), Ziel µ(O) = W(O)/(N M Z_N).
Ausgegeben: |ν|, ∫ f² dµ = Σ ν²/µ, |ν|²/∫f² ≤ q0 = |µ|.  Mit --formel zusätzlich die Dichteformel der Spiegel-Variante
  f(O) = M Σ_{Abweg-Daten, alte Wege} Π_k π sel W(alt)/Z_neu · Σ_{Aufweg-Daten} Π_k π sel Zalt/Zbr,
  alle Kopf- und Lochplätze zwischen den Scheiben verdeckt (summiert), und die größte Abweichung ν − f µ.
Aufruf: python3 pruef_zeitschleife_spiegel.py [--L 6] [--N 2] [--beta 4] [--w 2] [--lam 0.7]
        [--abweg spiegel|zelle] [--formel]
"""
import argparse
import functools
import itertools
from collections import defaultdict

import numpy as np

from pruef_gegenluecke import baue, uebergaenge, spruenge, bahnen, beweger


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--L', type=int, default=6)
    ap.add_argument('--N', type=int, default=2)
    ap.add_argument('--beta', type=int, default=4)
    ap.add_argument('--w', type=int, default=2)
    ap.add_argument('--lam', type=float, default=0.7)
    ap.add_argument('--abweg', choices=('spiegel', 'zelle'), default='spiegel')
    ap.add_argument('--formel', action='store_true')
    ap.add_argument('--start', choices=('frei', 'zelle'), default='frei',
                    help='Spiegel-Abweg: Anfang des neuen Stücks frei oder gleichverteilt in der Zelle von Y_m')
    ap.add_argument('--S', type=int, default=2, help='Halbschritte je Scheibe (gerade)')
    ap.add_argument('--zelle', type=int, default=2, help='Plätze je Zelle')
    ap.add_argument('--locker', action='store_true', help='Testmodell: wählbar = Stück endet in der Zelle (Anfang beliebig)')
    ap.add_argument('--querschritt', action='store_true', help='Abweg mit Querschritt in jeder Scheibe (kein d = 0)')
    a = ap.parse_args()
    L, N, lam, w = a.L, a.N, a.lam, a.w
    S = a.S
    cz_gr = a.zelle
    K = L // cz_gr

    def zelle(i):
        return i // cz_gr

    assert L % cz_gr == 0 and S % 2 == 0 and S * a.w <= 2 * a.beta
    B = baue(L)
    H = 2 * a.beta
    M = L
    zuege = {-1: 0.25, 0: 0.3, 1: 0.25, 2: 0.2}
    zuege_ab = {-1: 0.35, 1: 0.35, 2: 0.3} if a.querschritt else zuege

    def stern(a0, d):
        s = 1 if d > 0 else -1
        return [(a0 + l * s) % K for l in range(abs(d) + 1)]

    def wb(b, c):
        return zelle(b[-1]) == c and (a.locker or zelle(b[0]) == c)

    def kandidat(b, cl, cv):
        return zelle(b[-1]) == cv and (a.locker or zelle(b[0]) == cl)

    @functools.lru_cache(maxsize=None)
    def bew(starts, enden, occ, h0):
        return tuple(beweger(list(starts), list(enden), list(occ), h0, B, aufzaehlen=True))

    def Z(starts, enden, occ, h0):
        return sum(lam ** k for _, k in bew(tuple(starts), tuple(enden), occ, h0))

    def belegung(stuecke):
        return tuple(frozenset(b[t] for b in stuecke) for t in range(S + 1))

    def wegstuecke(wg, n):
        return [tuple(wg[t][l] for t in range(S + 1)) for l in range(n)]

    # ---------------------------------------------------------------- geschlossene Geschichten
    confs0 = [frozenset(c) for c in itertools.combinations(range(L), N)]
    trans = {(c, h % 2): uebergaenge(c, h, B) for c in confs0 for h in (0, 1)}
    gesch = []

    def dfs(weg, k):
        h = len(weg) - 1
        if h == H:
            if weg[-1] == weg[0]:
                gesch.append((tuple(weg[:-1]), k))
            return
        for (c1, n) in trans[(weg[-1], h % 2)]:
            dfs(weg + [c1], k + n)
    for c in confs0:
        dfs([c], 0)
    ZN = sum(lam ** k for _, k in gesch)

    # ---------------------------------------------------------------- vorwärts
    nu = defaultdict(float)
    for confs, kh in gesch:
        conf = list(confs) + [confs[0]]
        P = lam ** kh / ZN
        st0 = [bahnen(conf, S * k, S * k + S, S * k, B) for k in range(w)]

        def ablegen(stuecke, x, y, faktor):
            O = list(conf[:H])
            for kk in range(w):
                for t in range(S + 1):
                    O[S * kk + t] = frozenset(b[t] for b in stuecke[kk])
            nu[(x, y, tuple(O))] += faktor

        def abwaerts(stuecke, kopf, k, faktor, x):
            if k < 0:
                ablegen(stuecke, x, kopf, faktor)
                return
            st = stuecke[k]
            if a.abweg == 'zelle':
                occ = belegung(st)
                frei = [p for p in range(L) if zelle(p) == zelle(kopf) and p not in occ[0]]
                for hn in frei:
                    wege = bew((hn,), (kopf,), occ, S * k)
                    Zein = sum(lam ** kk for _, kk in wege)
                    for wg, kk in wege:
                        st_neu = list(stuecke)
                        st_neu[k] = st + wegstuecke(wg, 1)
                        abwaerts(st_neu, hn, k - 1, faktor * lam ** kk / (Zein * len(frei)), x)
                return
            e0 = zelle(kopf)
            for d, pd in zuege_ab.items():
                cz = stern(e0, d)
                m = abs(d)
                waehl = [[b for b in st if wb(b, c)] for c in cz[1:]]
                if any(len(wl) == 0 for wl in waehl):
                    continue
                for tup in itertools.product(*waehl):
                    sel = float(np.prod([1.0 / len(wl) for wl in waehl]))
                    andere = [b for b in st if b not in tup]
                    occ = belegung(andere)
                    Yalt = [kopf] + [b[-1] for b in tup]
                    sj = tuple(b[0] for b in tup)
                    frei = [p for p in range(L) if p not in occ[0] and p not in sj]
                    if a.start == 'zelle':
                        frei = [p for p in frei if zelle(p) == zelle(Yalt[m])]
                        for sp in frei:
                            wege = bew(sj + (sp,), tuple(Yalt[:m]) + (Yalt[m],), occ, S * k)
                            Zs = sum(lam ** kk for _, kk in wege)
                            for wg, kk in wege:
                                st_neu = list(stuecke)
                                st_neu[k] = andere + wegstuecke(wg, m + 1)
                                abwaerts(st_neu, sp, k - 1, faktor * pd * sel * lam ** kk / (Zs * len(frei)), x)
                        continue
                    wahl = []
                    for sp in frei:
                        for wg, kk in bew(sj + (sp,), tuple(Yalt[:m]) + (Yalt[m],), occ, S * k):
                            wahl.append((sp, wg, kk))
                    Zneu = sum(lam ** kk for _, _, kk in wahl)
                    for sp, wg, kk in wahl:
                        st_neu = list(stuecke)
                        st_neu[k] = andere + wegstuecke(wg, m + 1)
                        abwaerts(st_neu, sp, k - 1, faktor * pd * sel * lam ** kk / Zneu, x)

        def aufwaerts(k, start, faktor, stuecke, x):
            if k == w:
                abwaerts(stuecke, start, w - 1, faktor, x)
                return
            st = stuecke[k]
            j0 = [b for b in st if b[0] == start][0]
            a0 = zelle(j0[-1])
            for d, pd in zuege.items():
                cz = stern(a0, d)
                m = abs(d)
                waehl = [[b for b in st if wb(b, c) and b != j0] for c in cz[1:]]
                if any(len(wl) == 0 for wl in waehl):
                    continue
                for tup in itertools.product(*waehl):
                    sel = float(np.prod([1.0 / len(wl) for wl in waehl]))
                    I = (j0,) + tup
                    andere = [b for b in st if b not in I]
                    occ = belegung(andere)
                    wege = bew(tuple(I[l][0] for l in range(1, m + 1)), tuple(I[l - 1][-1] for l in range(1, m + 1)),
                               occ, S * k)
                    Zbr = sum(lam ** kk for _, kk in wege)
                    for wg, kk in wege:
                        st_neu = list(stuecke)
                        st_neu[k] = andere + wegstuecke(wg, m)
                        aufwaerts(k + 1, I[m][-1], faktor * pd * sel * lam ** kk / Zbr, st_neu, x)

        for x in sorted(conf[0]):
            aufwaerts(0, x, P / N, list(st0), x)

    # ---------------------------------------------------------------- Zielmaß und zweites Moment
    def gewicht(O):
        x, y, confs = O
        c0 = (confs[0] - {y}) | {x}
        k = spruenge(confs[H - 1], c0, H - 1, B)
        if k is None:
            return 0.0
        for t in range(H - 1):
            n = spruenge(confs[t], confs[t + 1], t, B)
            if n is None:
                return 0.0
            k += n
        return lam ** k

    def mu(O):
        return gewicht(O) / (N * M * ZN)

    numasse = sum(nu.values())
    if not nu:
        print(f"L={L} N={N} w={w} Abweg={a.abweg} Start={a.start} Querschritt={a.querschritt}: alles verworfen (ν = 0)")
        return
    zweit = sum(v * v / mu(O) for O, v in nu.items())

    cs = [frozenset(c) for c in itertools.combinations(range(L), N)]
    idx = {c: i for i, c in enumerate(cs)}
    Tm = np.eye(len(cs))
    for h in range(H):
        Th = np.zeros((len(cs), len(cs)))
        for c in cs:
            for (c1, n) in uebergaenge(c, h, B):
                Th[idx[c], idx[c1]] += lam ** n
        Tm = Tm @ Th
    offen = np.zeros((len(cs), len(cs)))
    for c in cs:
        for xx in c:
            for yy in range(L):
                if yy == xx or yy not in c:
                    offen[idx[c], idx[(c - {xx}) | {yy}]] += 1.0
    q0 = np.trace(offen @ Tm) / (N * M * ZN)
    print(f"L={L} N={N} w={w} lam={lam} Abweg={a.abweg} Start={a.start} Querschritt={a.querschritt}: O mit nu>0: {len(nu)}, |nu| = {numasse:.6f}, "
          f"∫f² = {zweit:.6f}, |nu|²/∫f² = {numasse ** 2 / zweit:.6f} ≤ q0 = {q0:.6f}", flush=True)

    if not a.formel or a.abweg != 'spiegel':
        return

    # ---------------------------------------------------------------- Dichteformel (Spiegel-Variante)
    def phi_auf(st, S0, Yo, k):
        """Faktor einer Aufweg-Scheibe: Loch unten bei S0, oben bei Yo, st = Stücke der Lücken-Konfiguration."""
        anf = {b[0] for b in st}
        end = {b[-1] for b in st}
        if S0 in anf or Yo in end:
            return 0.0
        summe = 0.0
        for d, pd in zuege.items():
            m = abs(d)
            cz = stern((zelle(Yo) - d) % K, d)
            if m == 0:
                summe += pd * Z((S0,), (Yo,), belegung(st), S * k)
                continue
            kand = [[b for b in st if kandidat(b, cz[l], cz[l - 1])] for l in range(1, m + 1)]
            for tup in itertools.product(*kand):
                Yalt = [b[-1] for b in tup[1:]] + [Yo]
                if any(zelle(Yalt[l - 1]) != cz[l] for l in range(1, m + 1)):
                    continue
                andere = [b for b in st if b not in tup]
                occ = belegung(andere)
                sel = 1.0
                for l in range(1, m + 1):
                    sel /= sum(1 for b in andere if wb(b, cz[l])) + 1
                sj = tuple(b[0] for b in tup)
                Zalt = Z((S0,) + sj, (tup[0][-1],) + tuple(Yalt), occ, S * k)
                Zbr = Z(sj, tuple(b[-1] for b in tup), occ, S * k)
                summe += pd * sel * Zalt / Zbr
        return summe

    def F_auf(G, x, z):
        summe = 0.0
        optionen = [[x]] + [[p for p in range(L) if p not in {b[0] for b in G[k]}] for k in range(1, w)] + [[z]]
        for loecher in itertools.product(*optionen):
            prod = 1.0
            for k in range(w):
                prod *= phi_auf(G[k], loecher[k], loecher[k + 1], k)
                if prod == 0.0:
                    break
            summe += prod
        return summe

    def f_formel(O):
        x, y, confs = O
        stO = [bahnen(list(confs) + [confs[0]], S * k, S * k + S, S * k, B) for k in range(w)]
        erg = [0.0]

        def runter(k, hk, faktor, G):
            if k == w:
                erg[0] += faktor * F_auf(G, x, hk)
                return
            st = stO[k]
            neu = [b for b in st if b[0] == hk]
            if len(neu) != 1:
                return
            neu = neu[0]
            rest = [b for b in st if b != neu]
            Ym = neu[-1]
            for d, pd in zuege_ab.items():
                m = abs(d)
                cz = stern((zelle(Ym) - d) % K, d)
                if m == 0:
                    occ = belegung(rest)
                    if a.start == 'zelle':
                        frei = [sp for sp in range(L) if sp not in occ[0] and zelle(sp) == zelle(Ym)]
                        if hk not in frei:
                            continue
                        Zneu = len(frei) * Z((hk,), (Ym,), occ, S * k)
                    else:
                        Zneu = sum(Z((sp,), (Ym,), occ, S * k) for sp in range(L) if sp not in occ[0])
                    runter(k + 1, Ym, faktor * pd / Zneu, G + [rest])
                    continue
                kand = [[b for b in rest if kandidat(b, cz[l], cz[l - 1])] for l in range(1, m + 1)]
                for tup in itertools.product(*kand):
                    Yalt = [b[-1] for b in tup[1:]] + [Ym]          # alte Enden von j_1 … j_m
                    if any(zelle(Yalt[l - 1]) != cz[l] for l in range(1, m + 1)):
                        continue
                    andere = [b for b in rest if b not in tup]
                    occ = belegung(andere)
                    sel = 1.0
                    for l in range(1, m + 1):
                        sel /= sum(1 for b in andere if wb(b, cz[l])) + 1
                    sj = tuple(b[0] for b in tup)
                    br = tuple(b[-1] for b in tup)
                    if a.start == 'zelle':
                        frei = [sp for sp in range(L) if sp not in occ[0] and sp not in sj and zelle(sp) == zelle(Ym)]
                        if hk not in frei:
                            continue
                        Zneu = len(frei) * Z(sj + (hk,), br + (Ym,), occ, S * k)
                    else:
                        Zneu = sum(Z(sj + (sp,), br + (Ym,), occ, S * k)
                                   for sp in range(L) if sp not in occ[0] and sp not in sj)
                    for wg, kk in bew(sj, tuple(Yalt), occ, S * k):
                        runter(k + 1, tup[0][-1], faktor * pd * sel * lam ** kk / Zneu, G + [andere + wegstuecke(wg, m)])

        runter(0, y, 1.0, [])
        return M * erg[0]

    fehler = 0.0
    for O, v in nu.items():
        fehler = max(fehler, abs(v - f_formel(O) * mu(O)) / v)
    print(f"  Dichteformel Spiegel-Variante: größter relativer Fehler nu(O) gegen f(O) µ(O) = {fehler:.2e}", flush=True)


if __name__ == '__main__':
    main()
