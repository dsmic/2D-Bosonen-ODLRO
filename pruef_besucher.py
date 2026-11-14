#!/usr/bin/env python3
"""Numerische Prüfung zu satz_3_9 §10.8 (Besucher eines Kastens): Gilt die punktweise Kernschranke

    K_v(d) = P_0( X_δ = d, N ≥ v )  ≤  η_v · p_{c1 δ}(d)      für alle d,

mit einer Folge η_v, deren Logarithmus überlinear in v fällt? N ist die Zahl der Zellen (Seite s), die die
Irrfahrt (Rate 1 je Nachbar, also Gesamtrate 4) in der Zeit δ = s² besucht. Geprüft wird

    Q_v(c1) = max_d  P_{0→d}(N ≥ v) · p_δ(d) / p_{c1 δ}(d)

über Verschiebungen d = λ s (Achse und Diagonale). P_{0→d}(N ≥ v) wird mit exakt gezogenen Brücken geschätzt:
je Koordinate eine 1D-Brücke (Sprungzahl aus der Bessel-Verteilung, Reihenfolge der Schritte gleichverteilt),
die beiden Koordinaten gleichverteilt verschränkt (die Sprungzeiten sind unabhängig gleichverteilt).
Start an einer Zellecke (ungünstigster Fall) und gleichverteilt in der Zelle.
Zum Vergleich: der Schwanz der freien Irrfahrt und die Schranke aus Lemma T4.

Aufruf: python3 pruef_besucher.py [--proben 200000] [--s 8 16]
"""
import argparse
import math
import numpy as np
from numba import njit
from scipy.special import ive, gammaln


def bessel_cdf(d, delta):
    """CDF der Zahl k (n = |d| + 2k Sprünge) einer 1D-Brücke mit Rate 2 über die Zeit δ: P(k) ∝ δ^{2k}/(k!(|d|+k)!)."""
    d = abs(int(d))
    kmax = int(delta + 12 * math.sqrt(delta) + 50)
    k = np.arange(kmax + 1)
    lw = 2 * k * math.log(delta) - gammaln(k + 1) - gammaln(d + k + 1)
    w = np.exp(lw - lw.max())
    return np.cumsum(w) / w.sum()


@njit(cache=True)
def ziehe_k(cdf, u):
    lo, hi = 0, cdf.shape[0] - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if cdf[mid] < u:
            lo = mid + 1
        else:
            hi = mid
    return lo


@njit(cache=True)
def lauf(proben, dx, dy, cdfx, cdfy, s, ecke, seed, vmax):
    """Histogramm der Zellzahl N für Brücken von 0 nach (dx, dy); Start an der Ecke oder gleichverteilt in der Zelle."""
    np.random.seed(seed)
    W = 400
    stempel = np.zeros((2 * W + 1, 2 * W + 1), dtype=np.int64)
    hist = np.zeros(vmax + 2, dtype=np.int64)
    for p in range(1, proben + 1):
        kx = ziehe_k(cdfx, np.random.random())
        ky = ziehe_k(cdfy, np.random.random())
        nx = abs(dx) + 2 * kx
        ny = abs(dy) + 2 * ky
        n = nx + ny
        # Schritte je Koordinate: (n+d)/2 nach oben, (n-d)/2 nach unten, gleichverteilt angeordnet
        sx = np.empty(nx, dtype=np.int64)
        upx = (nx + dx) // 2
        for i in range(nx):
            sx[i] = 1 if i < upx else -1
        np.random.shuffle(sx)
        sy = np.empty(ny, dtype=np.int64)
        upy = (ny + dy) // 2
        for i in range(ny):
            sy[i] = 1 if i < upy else -1
        np.random.shuffle(sy)
        welche = np.empty(n, dtype=np.int64)
        for i in range(n):
            welche[i] = 0 if i < nx else 1
        np.random.shuffle(welche)
        if ecke:
            x, y = 0, 0
        else:
            x, y = np.random.randint(0, s), np.random.randint(0, s)
        cx, cy = x // s, y // s
        stempel[cx + W, cy + W] = p
        N = 1
        ix, iy = 0, 0
        for i in range(n):
            if welche[i] == 0:
                x += sx[ix]
                ix += 1
            else:
                y += sy[iy]
                iy += 1
            cx = (x + s * W) // s - W
            cy = (y + s * W) // s - W
            if stempel[cx + W, cy + W] != p:
                stempel[cx + W, cy + W] = p
                N += 1
        hist[min(N, vmax + 1)] += 1
    return hist


@njit(cache=True)
def lauf_frei(proben, delta, s, ecke, seed, vmax):
    """Zellzahl der freien Irrfahrt in der Zeit δ (Sprungzahl Poisson(4δ), Richtungen gleichverteilt)."""
    np.random.seed(seed)
    W = 400
    stempel = np.zeros((2 * W + 1, 2 * W + 1), dtype=np.int64)
    hist = np.zeros(vmax + 2, dtype=np.int64)
    for p in range(1, proben + 1):
        n = np.random.poisson(4.0 * delta)
        if ecke:
            x, y = 0, 0
        else:
            x, y = np.random.randint(0, s), np.random.randint(0, s)
        stempel[x // s + W, y // s + W] = p
        N = 1
        for i in range(n):
            r = np.random.randint(0, 4)
            if r == 0:
                x += 1
            elif r == 1:
                x -= 1
            elif r == 2:
                y += 1
            else:
                y -= 1
            cx = (x + s * W) // s - W
            cy = (y + s * W) // s - W
            if stempel[cx + W, cy + W] != p:
                stempel[cx + W, cy + W] = p
                N += 1
        hist[min(N, vmax + 1)] += 1
    return hist


def schwanz(hist):
    """P(N ≥ v) für v = 0, 1, …, aus dem Histogramm."""
    t = np.cumsum(hist[::-1])[::-1]
    return t / hist.sum()


def p_kern(t, d):
    return float(ive(abs(d[0]), 2 * t) * ive(abs(d[1]), 2 * t))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proben", type=int, default=200000)
    ap.add_argument("--s", type=int, nargs="+", default=[8, 16])
    a = ap.parse_args()
    vmax = 60
    lambdas = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0, 12.0]
    c1s = [2.0, 4.0]
    for s in a.s:
        delta = s * s
        print(f"=== s = {s}, δ = s² = {delta}, Proben je Verschiebung: {a.proben} ===")
        for ecke in (True, False):
            art = "Start an der Zellecke" if ecke else "Start gleichverteilt in der Zelle"
            hf = lauf_frei(a.proben, delta, s, ecke, 7, vmax)
            Pf = schwanz(hf)
            tails = {}
            for lam in lambdas:
                for richtung in ("Achse", "Diagonale"):
                    if lam == 0 and richtung == "Diagonale":
                        continue
                    if richtung == "Achse":
                        d = (int(round(lam * s)), 0)
                    else:
                        q = int(round(lam * s / math.sqrt(2)))
                        d = (q, q)
                    h = lauf(a.proben, d[0], d[1], bessel_cdf(d[0], delta), bessel_cdf(d[1], delta), s, ecke,
                             11 + int(10 * lam) + (0 if richtung == "Achse" else 500), vmax)
                    tails[(lam, richtung, d)] = schwanz(h)
            print(f"--- {art} ---")
            kopf = "   v   P_frei(N≥v)   T4-Schranke  " + "  ".join(f"log Q_v(c1={c})  argmax λ" for c in c1s)
            print(kopf)
            for v in range(1, vmax + 1):
                t4 = min(1.0, math.exp(-0.2 * (v / 9 - 1) ** 2)) if v > 9 else 1.0
                zeile = f"  {v:3d}   {Pf[v]:10.3e}   {t4:10.3e}  "
                gut = Pf[v] > 0
                for c in c1s:
                    best, arg = -np.inf, None
                    for (lam, richtung, d), T in tails.items():
                        if T[v] <= 0:
                            continue
                        r = math.log(T[v]) + math.log(p_kern(delta, d)) - math.log(p_kern(c * delta, d))
                        if r > best:
                            best, arg = r, f"{lam:.1f} {richtung[0]}"
                    if arg is None:
                        zeile += "        –             –    "
                    else:
                        gut = True
                        zeile += f"   {best:8.3f}      {arg:8s}"
                if gut:
                    print(zeile)
            # Wie groß ist P_{0→d}(N ≥ v) bei großer Verschiebung, und was gäbe der Vergleich über (W1)?
            print("    Brücken-Schwanz P_{0→d}(N ≥ v) für einige v, je λ (Achse):")
            for lam in lambdas:
                key = [k for k in tails if k[0] == lam and k[1] == "Achse"][0]
                T = tails[key]
                werte = "  ".join(f"v={v}: {T[v]:.2e}" for v in (4, 8, 12, 16, 20, 24, 32, 40) if v <= vmax)
                print(f"      λ = {lam:3.1f}:  {werte}")
        print()


if __name__ == "__main__":
    main()
