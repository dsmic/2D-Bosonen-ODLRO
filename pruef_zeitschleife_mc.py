#!/usr/bin/env python3
"""Monte-Carlo-Prüfung der Ausbeute der Zeitschleife (Anhang Z, Z.10, Punkt 4).

Modell wie pruef_zeitschleife_spiegel.py: harte Bosonen auf dem Ring Z_L, Trotter-Zeit, Gewicht lam^Sprünge, Zellen =
Paare. Statt alle geschlossenen Geschichten aufzuzählen, wird C exakt per Transfermatrix gezogen; die Konstruktion läuft
mit zufälligen Wahlen (Gesetze wie im Aufzähl-Skript); f(O) wird exakt mit der Dichteformel berechnet.
  ∫ f² dµ = ∫ f dν = |ν| · E[f | angenommen],   Ausbeute = |ν|²/∫f² = |ν| / E[f | angenommen]  ≤  q0 = |µ|.
Abweg-Varianten: "zelle" (alt, eingeengt), "frei" (Spiegel, freier Anfang), "festzelle" (Spiegel, Anfang gleichverteilt in
der Zelle von Y_m = Variante a). --querschritt erzwingt im Abweg d ≠ 0.
Aufruf: python3 pruef_zeitschleife_mc.py --L 8 --N 6 --w 2 --abweg festzelle --querschritt --proben 3000 [--seed 1]
"""
import argparse
import functools
import itertools

import numpy as np

from pruef_gegenluecke import baue, uebergaenge, bahnen, beweger


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--L', type=int, default=6)
    ap.add_argument('--N', type=int, default=2)
    ap.add_argument('--beta', type=int, default=4)
    ap.add_argument('--w', type=int, default=1)
    ap.add_argument('--lam', type=float, default=0.7)
    ap.add_argument('--abweg', choices=('zelle', 'frei', 'festzelle'), default='frei')
    ap.add_argument('--S', type=int, default=2, help='Halbschritte je Scheibe (gerade)')
    ap.add_argument('--zelle', type=int, default=2, help='Plätze je Zelle')
    ap.add_argument('--locker', action='store_true', help='Testmodell: wählbar = Stück endet in der Zelle (Anfang beliebig)')
    ap.add_argument('--querschritt', action='store_true')
    ap.add_argument('--proben', type=int, default=2000)
    ap.add_argument('--seed', type=int, default=1)
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
    rng = np.random.default_rng(a.seed)
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

    def belegung(st):
        return tuple(frozenset(b[t] for b in st) for t in range(S + 1))

    def wegstuecke(wg, n):
        return [tuple(wg[t][l] for t in range(S + 1)) for l in range(n)]

    def ziehe(gewichte):
        g = np.asarray(gewichte, float)
        return rng.choice(len(g), p=g / g.sum())

    # ------------------------------------------------ Transfermatrizen und exaktes Ziehen geschlossener Geschichten
    cs = [frozenset(c) for c in itertools.combinations(range(L), N)]
    idx = {c: i for i, c in enumerate(cs)}
    n = len(cs)
    T = []
    for h in range(H):
        Th = np.zeros((n, n))
        for c in cs:
            for (c1, k) in uebergaenge(c, h, B):
                Th[idx[c], idx[c1]] += lam ** k
        T.append(Th)
    suffix = [None] * (H + 1)
    suffix[H] = np.eye(n)
    for h in range(H - 1, -1, -1):
        suffix[h] = T[h] @ suffix[h + 1]
    ZN = np.trace(suffix[0])

    def ziehe_geschichte():
        i0 = ziehe(np.diag(suffix[0]))
        weg = [i0]
        for h in range(H - 1):
            gew = T[h][weg[-1]] * suffix[h + 1][:, i0]
            weg.append(ziehe(gew))
        return [cs[i] for i in weg]

    offen = np.zeros((n, n))
    for c in cs:
        for xx in c:
            for yy in range(L):
                if yy == xx or yy not in c:
                    offen[idx[c], idx[(c - {xx}) | {yy}]] += 1.0
    q0 = np.trace(offen @ suffix[0]) / (N * M * ZN)

    # ------------------------------------------------ Vorwärts mit zufälligen Wahlen
    def vorwaerts():
        confs = ziehe_geschichte()
        conf = list(confs) + [confs[0]]
        st = [bahnen(conf, S * k, S * k + S, S * k, B) for k in range(w)]
        x = sorted(conf[0])[rng.integers(N)]
        start = x
        for k in range(w):
            s = st[k]
            j0 = [b for b in s if b[0] == start][0]
            a0 = zelle(j0[-1])
            dl = list(zuege)
            d = dl[ziehe([zuege[v] for v in dl])]
            cz = stern(a0, d); m = abs(d)
            waehl = [[b for b in s if wb(b, c) and b != j0] for c in cz[1:]]
            if any(len(wl) == 0 for wl in waehl):
                return None
            tup = tuple(wl[rng.integers(len(wl))] for wl in waehl)
            I = (j0,) + tup
            andere = [b for b in s if b not in I]
            occ = belegung(andere)
            wege = bew(tuple(I[l][0] for l in range(1, m + 1)), tuple(I[l - 1][-1] for l in range(1, m + 1)), occ, S * k)
            if not wege:
                return None
            wg, _ = wege[ziehe([lam ** kk for _, kk in wege])]
            st[k] = andere + wegstuecke(wg, m)
            start = I[m][-1]
        kopf = start
        for k in range(w - 1, -1, -1):
            s = st[k]
            if a.abweg == 'zelle':
                occ = belegung(s)
                frei = [p for p in range(L) if zelle(p) == zelle(kopf) and p not in occ[0]]
                if not frei:
                    return None
                hn = frei[rng.integers(len(frei))]
                wege = bew((hn,), (kopf,), occ, S * k)
                if not wege:
                    return None
                wg, _ = wege[ziehe([lam ** kk for _, kk in wege])]
                st[k] = s + wegstuecke(wg, 1)
                kopf = hn
                continue
            dl = list(zuege_ab)
            d = dl[ziehe([zuege_ab[v] for v in dl])]
            cz = stern(zelle(kopf), d); m = abs(d)
            waehl = [[b for b in s if wb(b, c)] for c in cz[1:]]
            if any(len(wl) == 0 for wl in waehl):
                return None
            tup = tuple(wl[rng.integers(len(wl))] for wl in waehl)
            andere = [b for b in s if b not in tup]
            occ = belegung(andere)
            Yalt = [kopf] + [b[-1] for b in tup]
            sj = tuple(b[0] for b in tup)
            frei = [p for p in range(L) if p not in occ[0] and p not in sj]
            if a.abweg == 'festzelle':
                frei = [p for p in frei if zelle(p) == zelle(Yalt[m])]
                if not frei:
                    return None
                sp = frei[rng.integers(len(frei))]
                wege = bew(sj + (sp,), tuple(Yalt[:m]) + (Yalt[m],), occ, S * k)
                if not wege:
                    return None
                wg, _ = wege[ziehe([lam ** kk for _, kk in wege])]
            else:
                wahl = [(sp, wg, kk) for sp in frei for wg, kk in bew(sj + (sp,), tuple(Yalt[:m]) + (Yalt[m],), occ, S * k)]
                if not wahl:
                    return None
                sp, wg, _ = wahl[ziehe([lam ** kk for _, _, kk in wahl])]
            st[k] = andere + wegstuecke(wg, m + 1)
            kopf = sp
        O = list(conf[:H])
        for kk in range(w):
            for t in range(S + 1):
                O[S * kk + t] = frozenset(b[t] for b in st[kk])
        return (x, kopf, tuple(O))

    # ------------------------------------------------ Dichteformel (wie pruef_zeitschleife_spiegel.py, drei Varianten)
    def phi_auf(st, S0, Yo, k):
        if S0 in {b[0] for b in st} or Yo in {b[-1] for b in st}:
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
                summe += pd * sel * Z((S0,) + sj, (tup[0][-1],) + tuple(Yalt), occ, S * k) / Z(sj, tuple(b[-1] for b in tup), occ, S * k)
        return summe

    def F_auf(G, x, z):
        summe = 0.0
        opt = [[x]] + [[p for p in range(L) if p not in {b[0] for b in G[k]}] for k in range(1, w)] + [[z]]
        for l in itertools.product(*opt):
            prod = 1.0
            for k in range(w):
                prod *= phi_auf(G[k], l[k], l[k + 1], k)
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
            if a.abweg == 'zelle':
                occ = belegung(rest)
                frei = [p for p in range(L) if zelle(p) == zelle(Ym) and p not in occ[0]]
                if hk not in frei:
                    return
                runter(k + 1, Ym, faktor / (len(frei) * Z((hk,), (Ym,), occ, S * k)), G + [rest])
                return
            for d, pd in zuege_ab.items():
                m = abs(d)
                cz = stern((zelle(Ym) - d) % K, d)
                if m == 0:
                    occ = belegung(rest)
                    if a.abweg == 'festzelle':
                        frei = [p for p in range(L) if p not in occ[0] and zelle(p) == zelle(Ym)]
                        if hk not in frei:
                            continue
                        Zneu = len(frei) * Z((hk,), (Ym,), occ, S * k)
                    else:
                        Zneu = sum(Z((p,), (Ym,), occ, S * k) for p in range(L) if p not in occ[0])
                    runter(k + 1, Ym, faktor * pd / Zneu, G + [rest])
                    continue
                kand = [[b for b in rest if kandidat(b, cz[l], cz[l - 1])] for l in range(1, m + 1)]
                for tup in itertools.product(*kand):
                    Yalt = [b[-1] for b in tup[1:]] + [Ym]
                    if any(zelle(Yalt[l - 1]) != cz[l] for l in range(1, m + 1)):
                        continue
                    andere = [b for b in rest if b not in tup]
                    occ = belegung(andere)
                    sel = 1.0
                    for l in range(1, m + 1):
                        sel /= sum(1 for b in andere if wb(b, cz[l])) + 1
                    sj = tuple(b[0] for b in tup)
                    br = tuple(b[-1] for b in tup)
                    if a.abweg == 'festzelle':
                        frei = [p for p in range(L) if p not in occ[0] and p not in sj and zelle(p) == zelle(Ym)]
                        if hk not in frei:
                            continue
                        Zneu = len(frei) * Z(sj + (hk,), br + (Ym,), occ, S * k)
                    else:
                        Zneu = sum(Z(sj + (p,), br + (Ym,), occ, S * k) for p in range(L) if p not in occ[0] and p not in sj)
                    for wg, kk in bew(sj, tuple(Yalt), occ, S * k):
                        runter(k + 1, tup[0][-1], faktor * pd * sel * lam ** kk / Zneu, G + [andere + wegstuecke(wg, m)])

        runter(0, y, 1.0, [])
        return M * erg[0]

    # ------------------------------------------------ Schätzen
    fs = []
    angenommen = 0
    for i in range(a.proben):
        O = vorwaerts()
        if O is None:
            continue
        angenommen += 1
        fs.append(f_formel(O))
    fs = np.array(fs)
    p = angenommen / a.proben
    if angenommen < 2:
        print(f"L={L} N={N} w={w} Abweg={a.abweg} Querschritt={a.querschritt} locker={a.locker}: nur {angenommen} von {a.proben} angenommen")
        return
    ef = fs.mean()
    # Fehler der Ausbeute p/E[f]: Delta-Methode mit Binomial- und Stichprobenfehler
    sp = np.sqrt(p * (1 - p) / a.proben)
    sf = fs.std(ddof=1) / np.sqrt(len(fs)) if len(fs) > 1 else np.nan
    ausbeute = p / ef
    s_ausb = ausbeute * np.sqrt((sp / p) ** 2 + (sf / ef) ** 2)
    print(f"L={L} N={N} w={w} lam={lam} Abweg={a.abweg} Querschritt={a.querschritt} locker={a.locker} Proben={a.proben}: "
          f"|ν| = {p:.4f} ± {sp:.4f}, E[f|ang.] = {ef:.4f} ± {sf:.4f}, Ausbeute |ν|²/∫f² = {ausbeute:.4f} ± {s_ausb:.4f} "
          f"≤ q0 = {q0:.4f}   (max f = {fs.max():.2f})", flush=True)


if __name__ == '__main__':
    main()
