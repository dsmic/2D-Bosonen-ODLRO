#!/usr/bin/env python3
"""Anhang L (Lochstück j0, Wählbarkeit über zwei Scheiben): exakte Prüfung der Dichteformel am Mini-Ring.

Modell und Hilfsfunktionen wie pruef_gegenluecke.py (harte Bosonen auf dem Ring Z_L, Trotter-Zeit, Gewicht
lam^Sprünge, Zellen = Paare von Plätzen, Aufweg über w Scheiben zu je einem Schritt, Ziel: Lückenmaß Gamma_T).
Ein Stück heißt hier regulär (= wählbar), wenn Anfang und Ende in derselben Zelle liegen.

Neue Regel (Anhang L, L.1), gegenüber pruef_gegenluecke.py:
  (a) Zwei Scheiben: In Scheibe k < w-1 wird j_m gleichverteilt unter den Stücken der Zelle c_m gewählt, die in
      Scheibe k wählbar sind UND deren Fortsetzung in Scheibe k+1 regulär ist ("doppelt wählbar").
      Dann ist das Lochstück j0 jeder Scheibe k >= 1 regulär; verworfen wird seinetwegen nie.
  (b) Umstieg in jeder Scheibe: Zug d = 0 heißt Umstieg innerhalb der Zelle (m = 1, c_1 = c_0, j_1 != j0).
  (c) Erste Scheibe: Das Stück des Schwanz-Teilchens muss regulär sein, sonst wird verworfen (einmal).

Dichteformel (Lemma L3):
  f(O) = (M/N) * sum_{Route, Lochplätze} pi(R) * sum_{Tupel aller Scheiben} prod_k sel_k(C^) Zalt_k / Zbr_k,
  sel_k = prod_{l<m} 1/g_{c_l}(C^)  *  1/g+_{c_m}(C^),
  g+ = Zahl der doppelt wählbaren Stücke der Zelle c_m im hypothetischen geschlossenen Zustand C^ (ohne j0).
  g+ hängt von den alten Stücken der Scheibe k+1 ab; die Summen über die Tupel der Scheiben sind dadurch gekoppelt.
Geprüft wird nu(O) = f(O) Gamma(O) für alle Lücken-Geschichten O mit nu > 0.
Aufruf: python3 pruef_lochstueck.py [--L 6] [--N 3] [--beta 4] [--w 2] [--lam 0.7]
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
    ap.add_argument('--beta', type=int, default=4, help='Schritte (je 2 Halbschritte)')
    ap.add_argument('--w', type=int, default=2, help='Scheiben der Lücke, je 1 Schritt')
    ap.add_argument('--lam', type=float, default=0.7)
    a = ap.parse_args()
    L, N, lam, w = a.L, a.N, a.lam, a.w
    K = L // 2
    B = baue(L)
    H = 2 * a.beta
    Tidx = 2 * w
    zuege = {-1: 0.25, 0: 0.3, 1: 0.25, 2: 0.2}

    def sternpfad(a0, d):
        """Zellen c_0..c_m; d = 0 ist der Umstieg innerhalb der Zelle."""
        if d == 0:
            return [a0, a0]
        s = 1 if d > 0 else -1
        return [(a0 + l * s) % K for l in range(abs(d) + 1)]

    def regulaer(b):
        return zelle(b[0]) == zelle(b[-1])

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
    print(f"L = {L}, N = {N}, beta = {a.beta}, w = {w}, lam = {lam}")
    print(f"geschlossene Geschichten: {len(geschichten)}, Z_N = {ZN:.6f}")

    # --- Vorwärts: nu(O) durch vollständige Aufzählung
    nu = defaultdict(float)
    verworfen_erste = 0.0          # Masse, die in Scheibe 0 verworfen wird (Schwanz-Stück nicht regulär)
    verworfen_leer = 0.0           # Masse, die verworfen wird, weil ein Kandidat fehlt
    for confs, kh in geschichten:
        conf = list(confs) + [confs[0]]
        P = lam ** kh / ZN
        stuecke = [bahnen(conf, 2 * k, 2 * k + 2, 2 * k, B) for k in range(w)]
        # reg_start[k][Platz]: ist das Stück der Scheibe k, das an diesem Platz beginnt, regulär?
        reg_start = [{b[0]: regulaer(b) for b in st} for st in stuecke]

        def scheibe(k, loch, faktor, neue_confs):
            nonlocal verworfen_erste, verworfen_leer
            if k == w:
                y = loch
                x = neue_confs['x']
                O = [neue_confs[t] if t in neue_confs else conf[t] for t in range(H)]
                O[Tidx] = conf[Tidx] - {y}
                O[0] = conf[0] - {x}
                nu[(x, y, tuple(O))] += faktor
                return
            st = stuecke[k]
            j0 = [b for b in st if b[0] == loch]
            assert len(j0) == 1
            j0 = j0[0]
            a0 = zelle(j0[0])
            if not regulaer(j0):
                assert k == 0, "Regel (a) verletzt: j0 einer späteren Scheibe ist nicht regulär"
                verworfen_erste += faktor
                return
            for d, pd in zuege.items():
                cz = sternpfad(a0, d)
                m = len(cz) - 1
                waehlbar = []
                for l in range(1, m + 1):
                    kand = [b for b in st if zelle(b[0]) == cz[l] and zelle(b[-1]) == cz[l] and b is not j0]
                    if l == m and k < w - 1:
                        kand = [b for b in kand if reg_start[k + 1][b[-1]]]              # doppelt wählbar
                    waehlbar.append(kand)
                if any(len(wl) == 0 for wl in waehlbar):
                    verworfen_leer += faktor * pd
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
                        verworfen_leer += faktor * pd * sel
                        continue
                    for (wg, kk) in wege:
                        nc = dict(neue_confs)
                        for t in range(3):
                            nc[2 * k + t] = frozenset(set(occ[t]) | set(wg[t]))
                        scheibe(k + 1, I[m][-1], faktor * pd * sel * lam ** kk / Zbr, nc)

        for xstart in sorted(conf[0]):
            scheibe(0, xstart, P / N, {'x': xstart})

    numasse = sum(nu.values())
    print(f"Lücken-Geschichten mit nu > 0: {len(nu)}, |nu| = {numasse:.6f}")
    print(f"verworfen in Scheibe 0 (Schwanz-Stück nicht regulär): {verworfen_erste:.6f};  "
          f"verworfen mangels Kandidaten oder Brücken: {verworfen_leer:.6f};  Summe mit |nu|: "
          f"{numasse + verworfen_erste + verworfen_leer:.6f}")

    # --- Rückwärts: Dichteformel mit gekoppelten Scheiben
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
            n = spruenge(c0, c1, t, B)
            if n is None:
                return 0.0
            k += n
        return lam ** k / (M * ZN)

    def f_formel(O):
        x, y, confs = O
        conf = list(confs) + [confs[0] | {x}]
        st_k = [bahnen(conf, 2 * k, 2 * k + 2, 2 * k, B) for k in range(w)]
        reg_o = [{b[0]: regulaer(b) for b in st} for st in st_k]                 # Stücke von O
        summe = 0.0
        a0 = zelle(x)
        for ds in itertools.product(list(zuege), repeat=w):
            zs = [a0]
            for d in ds:
                zs.append(sternpfad(zs[-1], d)[-1])
            if zs[-1] != zelle(y):
                continue
            pi = np.prod([zuege[d] for d in ds])
            loch_opt = [[x]] + [[p for p in range(L) if zelle(p) == zs[k] and p not in conf[2 * k]]
                                for k in range(1, w)] + [[y]]
            for loecher in itertools.product(*loch_opt):
                opts = []
                for k in range(w):
                    cz = sternpfad(zs[k], ds[k])
                    m = len(cz) - 1
                    st = st_k[k]
                    kand = [[b for b in st if zelle(b[0]) == cz[l] and zelle(b[-1]) == cz[l - 1]]
                            for l in range(1, m + 1)]
                    ol = []
                    for br in itertools.product(*kand):
                        if len(set(br)) < m:
                            continue
                        andere = [b for b in st if all(b is not q for q in br)]
                        occ = [frozenset(b[t] for b in andere) for t in range(3)]
                        S = [loecher[k]] + [b[0] for b in br]
                        Y = [b[-1] for b in br] + [loecher[k + 1]]
                        if any(zelle(S[l]) != cz[l] or zelle(Y[l]) != cz[l] for l in range(m + 1)):
                            continue                                              # alte Stücke regulär, auch j0
                        sel = 1.0
                        for l in range(1, m):
                            sel /= 1 + sum(1 for b in andere if zelle(b[0]) == cz[l] and zelle(b[-1]) == cz[l])
                        kand_m = [b[-1] for b in andere if zelle(b[0]) == cz[m] and zelle(b[-1]) == cz[m]]
                        Zalt = wert(beweger(S, Y, occ, 2 * k, B), lam)
                        Zbr = wert(beweger([b[0] for b in br], [b[-1] for b in br], occ, 2 * k, B), lam)
                        ol.append((sel * Zalt / Zbr, kand_m, frozenset(b[0] for b in br)))
                    opts.append(ol)
                if any(len(ol) == 0 for ol in opts):
                    continue
                # von oben nach unten: R_k[i] = Wert der Scheiben k..w-1, wenn Scheibe k die Möglichkeit i hat
                Rk = []
                for (val, kand_m, _) in opts[w - 1]:
                    # oberste Scheibe: j_m nur wählbar; g zählt wie bisher
                    Rk.append(val / (1 + len(kand_m)))
                for k in range(w - 2, -1, -1):
                    neu = []
                    for (val, kand_m, _) in opts[k]:
                        tot = 0.0
                        for (o2, r2) in zip(opts[k + 1], Rk):
                            br_starts = o2[2]
                            # Fortsetzung in C^: Brücken-Anfänge tragen dort reguläre alte Stücke
                            gplus = 1 + sum(1 for e in kand_m if (e in br_starts) or reg_o[k + 1][e])
                            tot += r2 / gplus
                        neu.append(val * tot)
                    Rk = neu
                summe += pi * sum(Rk)
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
    csN, iN = sektor(N)
    csM, iM = sektor(N - 1)

    def transfer(cs, idx, h):
        Tm = np.zeros((len(cs), len(cs)))
        for c in cs:
            for (c1, n) in uebergaenge(c, h, B):
                Tm[idx[c], idx[c1]] += lam ** n
        return Tm
    weg = np.zeros((len(csN), len(csM)))
    for c in csN:
        for x in c:
            weg[iN[c], iM[c - {x}]] += 1.0
    dazu = weg.T.copy()
    prod = weg.copy()
    for h in range(Tidx):
        prod = prod @ transfer(csM, iM, h)
    prod = prod @ dazu
    for h in range(Tidx, H):
        prod = prod @ transfer(csN, iN, h)
    Gmasse = np.trace(prod) / (M * ZN)
    print(f"|Gamma| = {Gmasse:.6f},  |nu| = {numasse:.6f}")
    print(f"zweites Moment int f^2 dGamma = {zweit:.6f};  Cauchy-Schwarz: |nu|^2/int f^2 = {numasse**2 / zweit:.6f} "
          f"<= |Gamma| = {Gmasse:.6f}")
    print("Dichteformel " + ("exakt bestätigt" if fehler < 1e-12 else "VERLETZT"))


if __name__ == '__main__':
    main()
