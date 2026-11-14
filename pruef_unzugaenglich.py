#!/usr/bin/env python3
"""Anhang U (unzugängliche Stücke sind selten, Antwort auf Befund K2): exakte Prüfung der Kippidentität für
Markenmengen am Mini-Ring.

Modell und Hilfsfunktionen wie pruef_gegenluecke.py (harte Bosonen auf dem Ring Z_L, Trotter-Zeit, Gewicht
lam^Sprünge, periodisch in der Zeit). Betrachtet wird eine Scheibe aus --schritte Schritten (je 2 Halbschritte;
mit einem einzigen Schritt läge die Bahn durch ihre Endpunkte fest, und es wäre immer a = 1). Ein Stück ist die
Bahn eines Teilchens in dieser Scheibe, von S nach E. Für ein Stück p und eine Familie F fester Stücke ist
    a_p(F)  =  B_p(weicht F aus)        (B_p = freie Brücke von S nach E, Gewicht lam^Sprünge),
und für ein Paar A = {p, p'} ist Xi_A(F) = B_A(beide weichen F und einander aus).

Geprüft wird (Anhang U, Lemma U2 und U1):
 (1) Identität für ein Stück:   E[ Σ_p 1/a_p(F_p^alle) ]  =  Σ_{Pfeile S→E} Z^{p frei}[a > 0] / Z_N  ≤  Σ Z^{p frei} / Z_N.
 (2) Identität für Paare:       E[ Σ_{Paare A} 1/Xi_A(F_{A^c}) ]  =  Σ_{Pfeilpaare} Z^{A frei}[Xi > 0] / Z_N  ≤  Σ Z^{A frei} / Z_N.
     Z^{A frei}: Die Stücke von A sind in der Scheibe freie Brücken ohne jede Wechselwirkung; an den Scheibenrändern
     sitzen alle Teilchen auf verschiedenen Plätzen. [a > 0] schränkt auf Umgebungen ein, denen die Brücke überhaupt
     ausweichen kann (in stetiger Zeit ist das immer so; in Trotter-Zeit nicht).
 (3) Kippungleichung für Paare, für mehrere Schwellen q:
        E[ #{Paare A: a_p(F_{A^c}) < q für beide p} ]  ≤  q² · Σ Z^{A frei} / Z_N.
 (4) Entkopplung (Lemma U1), für jede Geschichte und jedes Paar:
        a_p(F_{A^c})  ≤  a_p(F_p^alle) + B_p(trifft das andere Stück),
     und damit  #{Paare, beide stark unzugänglich (a_p(F_p^alle) < q)}  ≤  #{Paare: a_p(F_{A^c}) < q + h_p für beide}.
Aufruf: python3 pruef_unzugaenglich.py [--L 6] [--N 3] [--beta 4] [--schritte 2] [--lam 0.7]
"""
import argparse
import itertools

import numpy as np

from pruef_gegenluecke import baue, uebergaenge, bahnen, beweger, wert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--L', type=int, default=6)
    ap.add_argument('--N', type=int, default=3)
    ap.add_argument('--beta', type=int, default=4, help='Schritte (je 2 Halbschritte)')
    ap.add_argument('--schritte', type=int, default=2, help='Schritte der betrachteten Scheibe')
    ap.add_argument('--lam', type=float, default=0.7)
    a = ap.parse_args()
    L, N, lam = a.L, a.N, a.lam
    B = baue(L)
    H = 2 * a.beta
    Ts = 2 * a.schritte                     # Halbschritte der Scheibe
    assert Ts < H
    leer = [frozenset()] * (Ts + 1)

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
    print(f"L = {L}, N = {N}, beta = {a.beta}, Scheibe = {a.schritte} Schritte, lam = {lam}")
    print(f"geschlossene Geschichten: {len(geschichten)}, Z_N = {ZN:.6f}")

    # freier Ein-Teilchen-Kern der Scheibe
    p1 = np.zeros((L, L))
    for S in range(L):
        for E in range(L):
            p1[S, E] = wert(beweger([S], [E], leer, 0, B), lam)

    qs = (0.3, 0.5, 0.7, 0.9)
    links1 = 0.0
    links2 = 0.0
    P1 = {q: 0.0 for q in qs}
    P2w = {q: 0.0 for q in qs}          # beide gegen F_{A^c}
    P2s = {q: 0.0 for q in qs}          # beide gegen alle anderen (stark)
    P2e = {q: 0.0 for q in qs}          # beide gegen F_{A^c} mit Schwelle q + h_p
    entk_verletzt = 0
    hmax = 0.0
    for confs, kh in geschichten:
        conf = list(confs) + [confs[0]]
        P = lam ** kh / ZN
        st = bahnen(conf, 0, Ts, 0, B)

        def a_gegen(p, hindernisse):
            occ = [frozenset(b[t] for b in hindernisse) for t in range(Ts + 1)]
            return wert(beweger([p[0]], [p[-1]], occ, 0, B), lam) / p1[p[0], p[-1]]

        a_alle = [a_gegen(p, [b for b in st if b is not p]) for p in st]
        for i, p in enumerate(st):
            links1 += P / a_alle[i]
            for q in qs:
                P1[q] += P * (a_alle[i] < q)
        for i, j in itertools.combinations(range(len(st)), 2):
            p, pp = st[i], st[j]
            rest = [b for b in st if b is not p and b is not pp]
            occ = [frozenset(b[t] for b in rest) for t in range(Ts + 1)]
            xi = wert(beweger([p[0], pp[0]], [p[-1], pp[-1]], occ, 0, B), lam) / (p1[p[0], p[-1]] * p1[pp[0], pp[-1]])
            links2 += P / xi
            ai, aj = a_gegen(p, rest), a_gegen(pp, rest)
            hi, hj = 1.0 - a_gegen(p, [pp]), 1.0 - a_gegen(pp, [p])
            hmax = max(hmax, hi, hj)
            entk_verletzt += (ai > a_alle[i] + hi + 1e-12) + (aj > a_alle[j] + hj + 1e-12)
            for q in qs:
                P2w[q] += P * (ai < q and aj < q)
                P2s[q] += P * (a_alle[i] < q and a_alle[j] < q)
                P2e[q] += P * (ai < q + hi and aj < q + hj)

    # rechte Seiten: Z^{A frei}/Z_N, einmal ganz und einmal nur über Umgebungen mit a > 0 bzw. Xi > 0
    def sektor(n):
        cs = [frozenset(c) for c in itertools.combinations(range(L), n)]
        return cs, {c: i for i, c in enumerate(cs)}

    def rest_geschichten(c0):
        """Alle Hartkern-Geschichten der Teilchen in c0 über die Scheibe: Liste (Besetzungen je Zeit, Sprünge)."""
        liste = [((c0,), 0)]
        for h in range(Ts):
            neu_l = []
            for (occ, k) in liste:
                for (c1, n1) in uebergaenge(occ[-1], h, B):
                    neu_l.append((occ + (c1,), k + n1))
            liste = neu_l
        return liste

    csN, iN = sektor(N)
    Taus = np.eye(len(csN))                         # Rest der Periode: Halbschritte Ts … H−1
    for h in range(Ts, H):
        Tm = np.zeros((len(csN), len(csN)))
        for c in csN:
            for (c1, n) in uebergaenge(c, h, B):
                Tm[iN[c], iN[c1]] += lam ** n
        Taus = Taus @ Tm
    rechts1 = rechts1p = rechts2 = rechts2p = 0.0
    rg_cache = {}

    def rg(c):
        if c not in rg_cache:
            rg_cache[c] = rest_geschichten(c)
        return rg_cache[c]

    for c0 in csN:
        for S in sorted(c0):
            for (occ, k) in rg(c0 - {S}):
                for E in range(L):
                    c2 = occ[-1] | {E}
                    if E in occ[-1] or p1[S, E] == 0.0:
                        continue
                    t = Taus[iN[c2], iN[c0]]
                    if t == 0.0:
                        continue
                    g = t * lam ** k * p1[S, E] / ZN
                    rechts1 += g
                    if wert(beweger([S], [E], list(occ), 0, B), lam) > 0:
                        rechts1p += g
        if N >= 2:
            for S1, S2 in itertools.combinations(sorted(c0), 2):
                for (occ, k) in rg(c0 - {S1, S2}):
                    frei = [x for x in range(L) if x not in occ[-1]]
                    for E1, E2 in itertools.permutations(frei, 2):
                        if p1[S1, E1] == 0.0 or p1[S2, E2] == 0.0:
                            continue
                        c2 = occ[-1] | {E1, E2}
                        t = Taus[iN[c2], iN[c0]]
                        if t == 0.0:
                            continue
                        g = t * lam ** k * p1[S1, E1] * p1[S2, E2] / ZN
                        rechts2 += g
                        if wert(beweger([S1, S2], [E1, E2], list(occ), 0, B), lam) > 0:
                            rechts2p += g

    ok = True
    f1 = abs(links1 - rechts1p) / rechts1p
    f2 = abs(links2 - rechts2p) / rechts2p
    ok &= f1 < 1e-12 and f2 < 1e-12 and rechts1p <= rechts1 + 1e-12 and rechts2p <= rechts2 + 1e-12
    print(f"(1) ein Stück:  E[Σ_p 1/a_p] = {links1:.10f} = Σ Z^(p frei)[a>0]/Z_N = {rechts1p:.10f} (relativer Fehler {f1:.1e})"
          f"  ≤  R1 = Σ Z^(p frei)/Z_N = {rechts1:.6f}")
    print(f"(2) Paare:      E[Σ_A 1/Xi_A] = {links2:.10f} = Σ Z^(A frei)[Xi>0]/Z_N = {rechts2p:.10f} (relativer Fehler {f2:.1e})"
          f"  ≤  R2 = Σ Z^(A frei)/Z_N = {rechts2:.6f}")
    print("(3) Kippungleichung:")
    for q in qs:
        g1 = P1[q] <= q * rechts1 + 1e-12
        g2 = P2w[q] <= q * q * rechts2 + 1e-12
        ok &= g1 and g2
        print(f"      q = {q}:  E[#Stücke mit a < q] = {P1[q]:.5f} ≤ q·R1 = {q * rechts1:.5f};   "
              f"E[#Paare, beide a(F_A^c) < q] = {P2w[q]:.5f} ≤ q²·R2 = {q * q * rechts2:.5f}   {'ok' if g1 and g2 else 'VERLETZT'}")
    print(f"(4) Entkopplung: verletzt in {entk_verletzt} Fällen (größte Treffwahrscheinlichkeit h = {hmax:.3f})")
    ok &= entk_verletzt == 0
    for q in qs:
        g = P2s[q] <= P2e[q] + 1e-12
        ok &= g
        print(f"      q = {q}:  E[#Paare, beide stark unzugänglich] = {P2s[q]:.5f} ≤ E[#Paare, a(F_A^c) < q + h] = {P2e[q]:.5f}"
              f"   {'ok' if g else 'VERLETZT'}")
    print("Gesamt: " + ("alle Prüfungen bestanden" if ok else "MINDESTENS EINE PRÜFUNG VERLETZT"))


if __name__ == '__main__':
    main()
