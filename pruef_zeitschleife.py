#!/usr/bin/env python3
"""Exakte Prüfung der Dichteformel für die Zeitschleife (Anhang G.10) am Mini-Ring.

Modell wie pruef_gegenluecke.py: harte Bosonen auf dem Ring, Trotter-Zeit, Gewicht lam^Sprünge, periodisch.
Vorwärts aus einer geschlossenen Geschichte C:
  Schwanz-Teilchen gleichverteilt (1/N) bei (x, 0);
  aufwärts, Scheiben k = 0 … w−1: Lösch-Staffellauf wie G.1 (Zug d, Tupel, Brücken aus exakt bedingtem Gesetz);
  oben: Loch bei h_w;
  abwärts, Scheiben k = w−1 … 0: neuer Kopf h' gleichverteilt unter den freien Plätzen der Zelle des alten Kopfes
  (zur Zeit t_k, im aktuellen Zustand); neues Stück von (h', t_k) nach (alter Kopf, t_{k+1}) aus dem exakt
  bedingten Gesetz.
Ergebnis O: offene Konfiguration zu gleicher Zeit, Schwanz x, Kopf y = h'_0 (Zeit 0).
Ziel µ(O) = W(O)/(N M Z_N).  Dichteformel:
  f(O) = M Σ_{Aufwärts-Daten} π Π_k sel_k Zalt_k/Zbr_k · Π_k 1/(nfrei_k · Zein_k),
die Abwärts-Daten sind durch O bestimmt (Linie ab dem Kopf nach oben verfolgen).  Geprüft: ν(O) = f(O) µ(O).
Aufruf: python3 pruef_zeitschleife.py [--L 6] [--N 3] [--beta 4] [--w 2] [--lam 0.7]
"""
import argparse
import itertools
from collections import defaultdict

import numpy as np

from pruef_gegenluecke import baue, uebergaenge, spruenge, bahnen, beweger, wert, zelle


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--L', type=int, default=6)
    ap.add_argument('--N', type=int, default=3)
    ap.add_argument('--beta', type=int, default=4)
    ap.add_argument('--w', type=int, default=2)
    ap.add_argument('--lam', type=float, default=0.7)
    a = ap.parse_args()
    L, N, lam, w = a.L, a.N, a.lam, a.w
    K = L // 2
    B = baue(L)
    H = 2 * a.beta
    Tidx = 2 * w
    M = L
    zuege = {-1: 0.25, 0: 0.3, 1: 0.25, 2: 0.2}

    def stern(a0, d):
        s = 1 if d > 0 else -1
        return [(a0 + l * s) % K for l in range(abs(d) + 1)]

    def zellplaetze(c):
        return [p for p in range(L) if zelle(p) == c]

    # geschlossene Geschichten
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
    print(f"geschlossene Geschichten: {len(gesch)}, Z_N = {ZN:.6f}", flush=True)

    nu = defaultdict(float)

    def occ_aus(stuecke, t):
        return frozenset(b[t] for b in stuecke)

    for confs, kh in gesch:
        conf = list(confs) + [confs[0]]
        P = lam ** kh / ZN
        st0 = [bahnen(conf, 2 * k, 2 * k + 2, 2 * k, B) for k in range(w)]

        def abwaerts(stuecke, kopf_oben, k, faktor, x):
            """stuecke[k] = Liste der Stücke je Scheibe nach dem Aufwärtslauf (und Einfügungen darüber)."""
            if k < 0:
                y = kopf_oben
                O = list(conf[:H])
                for kk in range(w):
                    for t in range(3):
                        O[2 * kk + t] = frozenset(b[t] for b in stuecke[kk])
                schl = (x, y, tuple(O))
                nu[schl] += faktor
                return
            st = stuecke[k]
            occ = [occ_aus(st, t) for t in range(3)]
            frei = [p for p in zellplaetze(zelle(kopf_oben)) if p not in occ[0]]
            for hn in frei:
                wege = beweger([hn], [kopf_oben], occ, 2 * k, B, aufzaehlen=True)
                Zein = sum(lam ** kk for _, kk in wege)
                if Zein == 0:
                    continue
                for (wg, kk) in wege:
                    neu = tuple(p[0] for p in wg)
                    st_neu = [list(s) for s in stuecke]
                    st_neu[k] = st + [neu]
                    abwaerts(st_neu, hn, k - 1, faktor * lam ** kk / (Zein * len(frei)), x)

        def aufwaerts(k, start, faktor, stuecke, x):
            if k == w:
                abwaerts(stuecke, start, w - 1, faktor, x)
                return
            st = stuecke[k]
            j0 = [b for b in st if b[0] == start]
            assert len(j0) == 1
            j0 = j0[0]
            a0 = zelle(j0[0])
            if zelle(j0[-1]) != a0:
                return
            for d, pd in zuege.items():
                cz = stern(a0, d)
                m = abs(d)
                waehl = [[b for b in st if zelle(b[0]) == c and zelle(b[-1]) == c and b is not j0] for c in cz[1:]]
                if any(len(wl) == 0 for wl in waehl):
                    continue
                for tup in itertools.product(*waehl):
                    sel = 1.0
                    for wl in waehl:
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
                        brueck = [tuple(wg[t][l] for t in range(3)) for l in range(m)] if m > 0 else []
                        st_neu = [list(s) for s in stuecke]
                        st_neu[k] = andere + brueck
                        aufwaerts(k + 1, I[m][-1], faktor * pd * sel * lam ** kk / Zbr, st_neu, x)

        for x in sorted(conf[0]):
            aufwaerts(0, x, P / N, [list(s) for s in st0], x)

    print(f"offene Konfigurationen mit nu > 0: {len(nu)}, |nu| = {sum(nu.values()):.6f}", flush=True)

    def gewicht(O):
        x, y, confs = O
        c0 = (confs[0] - {y}) | {x}                    # Zeit 0⁻ (unterhalb): Schwanz noch da, Kopf noch nicht
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

    def f_formel(O):
        x, y, confs = O
        conf = list(confs) + [(confs[0] - {y}) | {x}]
        # Stücke je Scheibe in O
        stO = [bahnen(list(confs) + [confs[0]], 2 * k, 2 * k + 2, 2 * k, B) for k in range(w)]
        # Abwärts-Daten: Linie ab dem Kopf (y, 0) nach oben verfolgen
        ein = []
        pos = y
        for k in range(w):
            b = [s for s in stO[k] if s[0] == pos]
            if len(b) != 1:
                return 0.0
            ein.append(b[0]); pos = b[0][-1]
        hw = pos
        fak_ab = 1.0
        for k in range(w):
            andere = [s for s in stO[k] if s is not ein[k]]
            occ = [frozenset(s[t] for s in andere) for t in range(3)]
            frei = [p for p in zellplaetze(zelle(ein[k][-1])) if p not in occ[0]]
            if ein[k][0] not in frei:
                return 0.0
            Zein = wert(beweger([ein[k][0]], [ein[k][-1]], occ, 2 * k, B), lam)
            fak_ab /= (len(frei) * Zein)
        # Aufwärts-Daten wie G1, mit Stücken ohne die eingefügten
        stU = [[s for s in stO[k] if s is not ein[k]] for k in range(w)]
        summe = 0.0
        a0 = zelle(x)
        for ds in itertools.product(list(zuege), repeat=w):
            zs = [a0]
            for d in ds:
                zs.append(stern(zs[-1], d)[-1])
            if zs[-1] != zelle(hw):
                continue
            pi = np.prod([zuege[d] for d in ds])
            loch_opt = [[x]]
            for k in range(1, w):
                occk = frozenset(s[0] for s in stU[k])
                loch_opt.append([p for p in zellplaetze(zs[k]) if p not in occk])
            loch_opt.append([hw])
            for loecher in itertools.product(*loch_opt):
                prod_k = 1.0
                for k in range(w):
                    d = ds[k]; m = abs(d)
                    cz = stern(zs[k], d)
                    st = stU[k]
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
                        if loecher[k] in occ[0] or loecher[k + 1] in occ[2]:
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
        return M * summe * fak_ab

    fehler = 0.0
    zweit = 0.0
    for O, v in nu.items():
        f = f_formel(O)
        g = mu(O)
        fehler = max(fehler, abs(v - f * g) / v)
        zweit += v * f
    numasse = sum(nu.values())
    print(f"größter relativer Fehler nu(O) gegen f(O) µ(O): {fehler:.2e}")
    # q0 = |µ| exakt per Transfermatrix: (1/(N M Z)) Σ_{x,y} Tr(T^H b_y⁺ b_x) mit Öffnen bei Zeit 0
    cs = [frozenset(c) for c in itertools.combinations(range(L), N)]
    idx = {c: i for i, c in enumerate(cs)}
    Tm = np.eye(len(cs))
    for h in range(H):
        Th = np.zeros((len(cs), len(cs)))
        for c in cs:
            for (c1, n) in uebergaenge(c, h, B):
                Th[idx[c], idx[c1]] += lam ** n
        Tm = Tm @ Th
    offen = np.zeros((len(cs), len(cs)))           # Zeit 0: Teilchen bei x weg, bei y dazu (auch y = x)
    for c in cs:
        for xx in c:
            for yy in range(L):
                if yy == xx or yy not in c:
                    c2 = (c - {xx}) | {yy}
                    offen[idx[c], idx[c2]] += 1.0
    q0 = np.trace(offen @ Tm) / (N * M * ZN)
    print(f"|nu| = {numasse:.6f}, zweites Moment = {zweit:.6f}, |nu|²/zweites Moment = {numasse**2 / zweit:.6f}"
          f"  ≤  q0 = |µ| = {q0:.6f}")


if __name__ == '__main__':
    main()
