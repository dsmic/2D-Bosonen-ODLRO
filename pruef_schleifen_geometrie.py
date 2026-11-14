#!/usr/bin/env python3
"""Geometrie der Zeitschleifen (Anhang S): numerische Prüfung der Lemmata S1 und S2.

Teil 1 (Lemma S1): Skelette nach OpenAI §8.1 (dyadische Geschwindigkeiten, Querabweichung bis zur Mitte vorwärts,
  danach rückwärts gelesen), die erste Koordinate als Zeit gelesen: Fortschritt σ ∈ [0, W], Zeit min(σ, W − σ),
  Querlage ⌊σ d/W + Z_{min(σ, W−σ)}⌋.  Zwei unabhängige Schleifen mit denselben Endpunkten.  Gezählt werden Begegnungen
  zur selben Zeit u (|Lagedifferenz|_∞ ≤ R): gleiche Hälften (U–U′, D–D′, wie bei OpenAI) und Gegenhälften
  (U–D′, D–U′, neu).  Ausgabe: Mittelwerte und E e^{θJ} in Abhängigkeit von W, ohne Torus und mit Torus (n Zellen).
Teil 2 (Lemma S2): orientierte Umwege.  Schlechte Raum-Zeit-Zellen unabhängig mit Wahrscheinlichkeit p, dazu
  „Kuppeln“ (Ring zu einer Zeit, der sich später schließt).  Je Scheibe k: Füllung F_k (schlechte Zellen plus endliche
  Komplement-Komponenten), Außenraum E_k.  Lage zur Zeit t_k: r_k = nächster Punkt von E_{k−1} ∩ E_k zu b_k;
  Weg in Scheibe k: kürzester Weg in E_k.  Geprüft: alle Wege gültig; Schwanz der Abweichung |r_k − b_k|.
  (Das ist die Fassung von Lemma S2 bis 2026-11-13 abends; sie trug nicht, Review 2026-11-13, W2.)
Teil 3 (Lemma S2, Fassung seit 2026-11-13 abends = OA §8.2): Kanten-Komponenten der schlechten Zellen, Füllung je
  Komponente (endliche Kanten-Komponenten ihres Komplements, gehoben), F_k = Vereinigung, E_k = Komplement.
  r_k wie in Teil 2.  Weg: Kantenweg σ(r_k, r_{k+1}) längs der geraden Strecke, OAs Umwegverfahren (betritt σ eine
  äußerste Füllung, wird das Stück bis zum letzten Besuch durch einen Sternpfad auf dem Außenrand ersetzt), danach
  chronologische Schleifenlöschung.  Geprüft: Außenrand im Sterngraph zusammenhängend und in E_k; Weg in E_k;
  Weglänge ≤ 2 d_∞ + Σ 6|T| (getroffene Komponenten).  Zusätzlich diagonale Ringe (Zellen nur über Ecken
  verbunden, Gegenbeispiel aus W2): Sie werden nicht gefüllt, und der Weg läuft durch sie hindurch.
Aufruf: python3 pruef_schleifen_geometrie.py [teil1] [teil2] [teil3]      (ohne Angabe: alle)
"""
from collections import deque

import numpy as np

CVEL = (1 - 2 ** -0.25) / 2


def skelett_z(rng, h, stufen):
    """Z_t, t = 0..h, für zwei Querkoordinaten (OpenAI §8.1)."""
    Z = np.zeros((h + 1, 2))
    i = np.arange(1, h + 1)
    v = np.zeros((h, 2))
    for l in range(stufen):
        nbl = (h - 1) // 2 ** l + 1
        U = rng.uniform(-1, 1, size=(nbl, 2))
        v += CVEL * 2 ** (-l / 4) * U[(i - 1) // 2 ** l]
    Z[1:] = np.cumsum(v, axis=0)
    return Z


def lagen(Z, d, W):
    w = W // 2
    u = np.arange(w + 1)
    U = np.floor(u[:, None] * d[None, :] / W + Z[:w + 1])
    D = np.floor((W - u)[:, None] * d[None, :] / W + Z[:w + 1])
    return U, D


def nah(A, B, R, n):
    diff = A - B
    if n:
        diff = (diff + n // 2) % n - n // 2
    return np.max(np.abs(diff), axis=1) <= R


def teil1():
    rng = np.random.default_rng(1)
    R = 1
    print("Teil 1: Begegnungen zweier Schleifen-Skelette (R = 1), 4000 Paare je Zeile")
    print(f"{'n':>4} {'W':>5} {'d':>12} {'E J_gleich':>10} {'E J_gegen':>9} {'e^(.005J)':>9} {'e^(.01J)':>9} "
          f"{'e^(.02J)':>9} {'J 99%':>6} {'J 99,9%':>7} {'max J':>6}")
    faelle = [(0, W, frac) for W in (64, 256, 1024, 4096) for frac in (0.0, 0.5, 1.0)]
    faelle += [(64, W, 0.5) for W in (8, 64, 256, 1024, 4096)]
    for n, W, frac in faelle:
        w = W // 2
        stufen = int(np.ceil(np.log2(W))) + 8
        d = np.array([frac * W, 0.5 * frac * W]) if n == 0 else np.array([frac * min(W, n / 2), 0.0])
        Jg, Jx = [], []
        for _ in range(4000):
            U1, D1 = lagen(skelett_z(rng, w, stufen), d, W)
            U2, D2 = lagen(skelett_z(rng, w, stufen), d, W)
            Jg.append(nah(U1, U2, R, n).sum() + nah(D1, D2, R, n).sum())
            Jx.append(nah(U1, D2, R, n).sum() + nah(D1, U2, R, n).sum())
        Jg, Jx = np.array(Jg), np.array(Jx)
        J = Jg + Jx
        dd = "(" + ",".join(str(int(round(v))) for v in d) + ")"
        print(f"{n:4d} {W:5d} {dd:>12} {Jg.mean():10.2f} {Jx.mean():9.2f} {np.mean(np.exp(0.005 * J)):9.3f} "
              f"{np.mean(np.exp(0.01 * J)):9.3f} {np.mean(np.exp(0.02 * J)):9.3f} {np.quantile(J, 0.99):6.0f} "
              f"{np.quantile(J, 0.999):7.0f} {J.max():6d}", flush=True)


# ---------------------------------------------------------------- Teil 2
NB4 = ((1, 0), (-1, 0), (0, 1), (0, -1))


def aussenraum(bad):
    """E = größte 4-Komponente des Komplements (Torus); F = Komplement von E (Füllung)."""
    n = bad.shape[0]
    lab = -np.ones((n, n), dtype=int)
    groesse = []
    for i in range(n):
        for j in range(n):
            if bad[i, j] or lab[i, j] >= 0:
                continue
            c = len(groesse)
            q = deque([(i, j)]); lab[i, j] = c; g = 0
            while q:
                a, b = q.popleft(); g += 1
                for da, db in NB4:
                    x, y = (a + da) % n, (b + db) % n
                    if not bad[x, y] and lab[x, y] < 0:
                        lab[x, y] = c; q.append((x, y))
            groesse.append(g)
    if not groesse:
        return np.zeros_like(bad)
    return lab == int(np.argmax(groesse))


def torusdist(a, b, n):
    d = np.abs(np.asarray(a) - np.asarray(b)) % n
    return np.max(np.minimum(d, n - d), axis=-1)


def weg_in(E, a, b):
    """Kürzester 4-Weg in E von a nach b (Länge) oder None."""
    n = E.shape[0]
    if not (E[a] and E[b]):
        return None
    dist = {a: 0}; q = deque([a])
    while q:
        p = q.popleft()
        if p == b:
            return dist[p]
        for da, db in NB4:
            x = ((p[0] + da) % n, (p[1] + db) % n)
            if E[x] and x not in dist:
                dist[x] = dist[p] + 1; q.append(x)
    return None


def teil2():
    rng = np.random.default_rng(2)
    n, W = 48, 96
    print("\nTeil 2: orientierte Umwege, n = 48, W = 96 Scheiben, 40 Skelette je Zeile")
    print(f"{'p':>6} {'Kuppeln':>8} {'ungültig':>9} {'P(Abw≥1)':>9} {'P(Abw≥2)':>9} {'P(Abw≥4)':>9} {'P(Abw≥8)':>9} "
          f"{'max Abw':>8} {'mittl. Mehrweg':>15}")
    for p, kuppeln in ((0.01, 0), (0.03, 0), (0.06, 0), (0.03, 20), (0.06, 20)):
        bad = rng.random((W, n, n)) < p
        for _ in range(kuppeln):                       # Ring zur Zeit k0, Deckel ab k0 + dk
            k0 = rng.integers(1, W - 12); dk = rng.integers(2, 8)
            c = rng.integers(0, n, 2); r = rng.integers(2, 5)
            for k in range(k0, k0 + dk + 1):
                for a in range(-r, r + 1):
                    for b in range(-r, r + 1):
                        rand = max(abs(a), abs(b)) == r
                        if rand or k == k0 + dk:
                            bad[k, (c[0] + a) % n, (c[1] + b) % n] = True
        E = np.array([aussenraum(bad[k]) for k in range(W)])
        A = [E[0]] + [E[k - 1] & E[k] for k in range(1, W)]
        abw, mehr, ungueltig = [], [], 0
        for _ in range(40):
            Z = skelett_z(rng, W, 14)                  # eine zeitlich gerichtete Hälfte über alle W Scheiben
            d = rng.integers(-n // 4, n // 4 + 1, 2)
            k = np.arange(W)
            b = np.floor(k[:, None] * d[None, :] / W + Z[:W]).astype(int) % n
            r = []
            for k in range(W):
                kand = np.argwhere(A[k])
                dd = torusdist(kand, b[k], n)
                r.append(tuple(kand[np.argmin(dd)]))
                abw.append(dd.min())
            for k in range(W - 1):
                L = weg_in(E[k], r[k], r[k + 1])
                if L is None:
                    ungueltig += 1
                else:
                    mehr.append(L - torusdist(np.array(r[k]), np.array(r[k + 1]), n))
        abw = np.array(abw)
        print(f"{p:6.2f} {kuppeln:8d} {ungueltig:9d} {np.mean(abw >= 1):9.4f} {np.mean(abw >= 2):9.4f} "
              f"{np.mean(abw >= 4):9.5f} {np.mean(abw >= 8):9.5f} {abw.max():8d} {np.mean(mehr):15.3f}", flush=True)


# ---------------------------------------------------------------- Teil 3: OAs Konstruktion
NB8 = tuple((a, b) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0))


def komponenten_und_fuellungen(bad):
    """Kanten-Komponenten von bad (Torus) und ihre Füllungen (gehoben, zurückprojiziert).
    Rückgabe: Liste (Zellen der Komponente, Füllung als Menge), Feld 'aussen' mit der Nummer der äußersten Füllung
    (−1 außerhalb aller Füllungen)."""
    n = bad.shape[0]
    gesehen = np.zeros_like(bad, dtype=bool)
    komp = []
    for i, j in np.argwhere(bad):
        if gesehen[i, j]:
            continue
        gehoben = {(int(i), int(j))}; q = deque([(int(i), int(j))]); gesehen[i, j] = True
        while q:                                       # BFS mit gehobenen Koordinaten
            a, b = q.popleft()
            for da, db in NB4:
                x, y = a + da, b + db
                if bad[x % n, y % n] and not gesehen[x % n, y % n]:
                    gesehen[x % n, y % n] = True; gehoben.add((x, y)); q.append((x, y))
        xs = [c[0] for c in gehoben]; ys = [c[1] for c in gehoben]
        x0, x1, y0, y1 = min(xs) - 1, max(xs) + 1, min(ys) - 1, max(ys) + 1
        aussen = set(); q = deque()
        for x in range(x0, x1 + 1):                    # Rand des Kastens gehört zum Äußeren
            for y in (y0, y1):
                if (x, y) not in gehoben and (x, y) not in aussen:
                    aussen.add((x, y)); q.append((x, y))
        for y in range(y0, y1 + 1):
            for x in (x0, x1):
                if (x, y) not in gehoben and (x, y) not in aussen:
                    aussen.add((x, y)); q.append((x, y))
        while q:
            a, b = q.popleft()
            for da, db in NB4:
                x, y = a + da, b + db
                if x0 <= x <= x1 and y0 <= y <= y1 and (x, y) not in gehoben and (x, y) not in aussen:
                    aussen.add((x, y)); q.append((x, y))
        fuell = {(x % n, y % n) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1) if (x, y) not in aussen}
        komp.append(({(c[0] % n, c[1] % n) for c in gehoben}, fuell))
    aussen_id = -np.ones(bad.shape, dtype=int)
    for k in sorted(range(len(komp)), key=lambda k: len(komp[k][1])):   # größere Füllung überschreibt kleinere
        for c in komp[k][1]:
            aussen_id[c] = k
    return komp, aussen_id


def strecke(a, b, n):
    """Kantenweg von a nach b längs der geraden Strecke (Torus, kürzeste Hebung); Liste von Zellen."""
    d = [((b[0] - a[0] + n // 2) % n) - n // 2, ((b[1] - a[1] + n // 2) % n) - n // 2]
    pkt = [tuple(a)]; x, y = 0, 0
    L = abs(d[0]) + abs(d[1])
    for s in range(1, L + 1):                          # gierig der Geraden folgen, je Schritt eine Koordinate
        if abs(d[0]) * (abs(y) + 0.5) >= abs(d[1]) * (abs(x) + 0.5) and x != d[0]:
            x += int(np.sign(d[0]))
        elif y != d[1]:
            y += int(np.sign(d[1]))
        else:
            x += int(np.sign(d[0]))
        pkt.append(((a[0] + x) % n, (a[1] + y) % n))
    return pkt


def sternpfad(rand, von, nach, n):
    """Kürzester Sternpfad in der Zellmenge rand von 'von' nach 'nach' (oder None)."""
    vorg = {von: None}; q = deque([von])
    while q:
        p = q.popleft()
        if p == nach:
            pfad = []
            while p is not None:
                pfad.append(p); p = vorg[p]
            return pfad[::-1]
        for da, db in NB8:
            x = ((p[0] + da) % n, (p[1] + db) % n)
            if x in rand and x not in vorg:
                vorg[x] = p; q.append(x)
    return None


def umweg(sig, komp, aussen_id, n):
    """OAs Umwegverfahren auf dem Kantenweg sig; Rückgabe (Weg nach Schleifenlöschung, Fehlertext, getroffene Komp.)."""
    weg, i, getroffen = [sig[0]], 1, set()
    while i < len(sig):
        k = aussen_id[sig[i]]
        if k < 0:
            weg.append(sig[i]); i += 1; continue
        fuell = komp[k][1]
        letzt = max(j for j in range(i, len(sig)) if sig[j] in fuell)
        if letzt + 1 >= len(sig):
            return None, 'Ende in Füllung', getroffen
        getroffen.add(k)
        rand = {((c[0] + da) % n, (c[1] + db) % n) for c in fuell for da, db in NB4} - fuell
        p = sternpfad(rand, sig[i - 1], sig[letzt + 1], n)
        if p is None:
            return None, 'Rand nicht sternzusammenhängend', getroffen
        if any(aussen_id[c] >= 0 for c in rand):
            return None, 'Rand in einer Füllung', getroffen
        weg.extend(p[1:]); i = letzt + 2
    geloescht, pos = [], {}                            # chronologische Schleifenlöschung
    for c in weg:
        if c in pos:
            del geloescht[pos[c] + 1:]
            pos = {x: j for j, x in enumerate(geloescht)}
        else:
            pos[c] = len(geloescht); geloescht.append(c)
    return geloescht, None, getroffen


def teil3():
    rng = np.random.default_rng(3)
    n, W = 48, 96
    print("\nTeil 3: OAs Umwegverfahren (Lemma S2 seit 2026-11-13 abends), n = 48, W = 96, 40 Skelette je Zeile")
    print(f"{'p':>6} {'Kuppeln':>8} {'Diag.ringe':>10} {'Fehler':>7} {'Länge>Schranke':>15} {'P(Abw≥1)':>9} "
          f"{'P(Abw≥2)':>9} {'max Abw':>8} {'mittl. Mehrweg':>15} {'max Länge/Schranke':>19}")
    for p, kuppeln, diag in ((0.01, 0, 0), (0.03, 0, 0), (0.06, 0, 0), (0.03, 20, 0), (0.06, 20, 0),
                             (0.03, 0, 40), (0.06, 20, 40)):
        bad = rng.random((W, n, n)) < p
        for _ in range(kuppeln):
            k0 = rng.integers(1, W - 12); dk = rng.integers(2, 8)
            c = rng.integers(0, n, 2); r = rng.integers(2, 5)
            for k in range(k0, k0 + dk + 1):
                for a in range(-r, r + 1):
                    for b in range(-r, r + 1):
                        if max(abs(a), abs(b)) == r or k == k0 + dk:
                            bad[k, (c[0] + a) % n, (c[1] + b) % n] = True
        for _ in range(diag):                          # diagonaler Ring |a| + |b| = r über viele Scheiben
            k0 = rng.integers(0, W - 20); c = rng.integers(0, n, 2); r = rng.integers(3, 8)
            for k in range(k0, k0 + 20):
                for a in range(-r, r + 1):
                    for b in (r - abs(a), -(r - abs(a))):
                        bad[k, (c[0] + a) % n, (c[1] + b) % n] = True
        daten = [komponenten_und_fuellungen(bad[k]) for k in range(W)]
        E = np.array([daten[k][1] < 0 for k in range(W)])
        A = [E[0]] + [E[k - 1] & E[k] for k in range(1, W)]
        abw, mehr, fehler, ueber, quot = [], [], 0, 0, []
        for _ in range(40):
            Z = skelett_z(rng, W, 14)
            d = rng.integers(-n // 4, n // 4 + 1, 2)
            kk = np.arange(W)
            b = np.floor(kk[:, None] * d[None, :] / W + Z[:W]).astype(int) % n
            r = []
            for k in range(W):
                kand = np.argwhere(A[k])
                dd = torusdist(kand, b[k], n)
                r.append(tuple(int(v) for v in kand[np.argmin(dd)]))
                abw.append(dd.min())
            for k in range(W - 1):
                komp, aussen_id = daten[k]
                sig = strecke(r[k], r[k + 1], n)
                weg, fehl, getroffen = umweg(sig, komp, aussen_id, n)
                if fehl is not None or any(aussen_id[c] >= 0 for c in weg) or weg[-1] != r[k + 1]:
                    fehler += 1; continue
                dinf = int(torusdist(np.array(r[k]), np.array(r[k + 1]), n))
                treff = {kk2 for kk2, (zellen, _) in enumerate(komp) if any(c in zellen for c in sig)}
                schranke = 2 * dinf + 6 * sum(len(komp[kk2][0]) for kk2 in treff) + 1
                ueber += len(weg) > schranke
                quot.append(len(weg) / schranke)
                mehr.append(len(weg) - 1 - dinf)
        abw = np.array(abw)
        print(f"{p:6.2f} {kuppeln:8d} {diag:10d} {fehler:7d} {ueber:15d} {np.mean(abw >= 1):9.4f} "
              f"{np.mean(abw >= 2):9.4f} {abw.max():8d} {np.mean(mehr):15.3f} {max(quot):19.3f}", flush=True)
    # Gegenbeispiel aus W2 einzeln: diagonaler Ring, Strecke quer hindurch
    n = 40
    bad = np.zeros((n, n), dtype=bool)
    for a in range(-8, 9):
        for b in (8 - abs(a), -(8 - abs(a))):
            bad[(20 + a) % n, (20 + b) % n] = True
    komp, aussen_id = komponenten_und_fuellungen(bad)
    sig = strecke((20, 15), (20, 33), n)               # von innen nach außen, kreuzt den Ring bei (20, 28)
    weg, fehl, _ = umweg(sig, komp, aussen_id, n)
    print(f"  Diagonaler Ring (32 Zellen der Größe 1), Strecke von innen nach außen: Komponenten {len(komp)}, "
          f"gefüllte Zellen außerhalb des Rings {int((aussen_id >= 0).sum()) - int(bad.sum())}, "
          f"Strecke trifft Ringzellen {sum(bool(bad[c]) for c in sig)}, Weglänge {len(weg) - 1} bei d_∞ = {len(sig) - 1}, "
          f"Weg in E: {all(aussen_id[c] < 0 for c in weg)}, Fehler: {fehl}")


if __name__ == '__main__':
    import sys
    alle = not any(a in sys.argv for a in ('teil1', 'teil2', 'teil3'))
    if alle or 'teil1' in sys.argv:
        teil1()
    if alle or 'teil2' in sys.argv:
        teil2()
    if alle or 'teil3' in sys.argv:
        teil3()
