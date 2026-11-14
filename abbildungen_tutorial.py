#!/usr/bin/env python3
"""Abbildungen für tutorial_beweis_verduennt.md (schematisch, Abb. 3 mit Simulation). Im Tutorial benutzt: abb1_bad, abb2_offen,
abb3_routen, abb6_zeitschleife (Abb. 4), abb4_staffellauf (Abb. 5), abb5_schleifen (Abb. 6); abb2_luecke und abb5_gegenluecke
zeigen die erste Fassung mit Lücke (Anhang G). Ausgabe: abbildungen/*.png
Aufruf: python3 abbildungen_tutorial.py
"""
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
AUS = os.path.join(HIER, 'abbildungen')
os.makedirs(AUS, exist_ok=True)

# Okabe-Ito: farbfehlsichtig unterscheidbar
BLAU, ROT, GRUEN, GRAU, HELLGRAU, TINTE = '#0072B2', '#D55E00', '#009E73', '#555555', '#BBBBBB', '#222222'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9, 'axes.edgecolor': '#888888',
                     'axes.linewidth': 0.6, 'savefig.dpi': 220, 'savefig.bbox': 'tight'})


def speichern(fig, name):
    fig.savefig(os.path.join(AUS, name), facecolor='white')
    plt.close(fig)
    print('geschrieben:', name)


# ---------------------------------------------------------------- Abb. 1: Bad um ein Teilchen
def konfiguration(rng, L, n, verboten):
    besetzt = set()
    while len(besetzt) < n:
        p = (int(rng.integers(L)), int(rng.integers(L)))
        if p in verboten or p in besetzt:
            continue
        if any(abs(p[0] - q[0]) + abs(p[1] - q[1]) <= 1 for q in besetzt):
            continue                       # schematisch: etwas Abstand, wie ein abstoßendes Gas
        besetzt.add(p)
    return sorted(besetzt)


def abb1():
    rng = np.random.default_rng(3)
    L, n = 14, 22
    x0 = (7, 7)
    fig, axs = plt.subplots(1, 2, figsize=(6.6, 3.6))
    loch = {(x0[0] + i, x0[1] + j) for i in range(-1, 2) for j in range(-1, 2)}
    links = konfiguration(rng, L, n, loch)
    rechts = konfiguration(rng, L, n, set())
    for ax, konf, titel in ((axs[0], links, 'Bad um ein Teilchen bei x\n(P$_x$: Teilchen bei x herausgenommen)'),
                            (axs[1], rechts, 'Grundzustand mit N − 1 Teilchen\n(Q = ψ$_{N−1}^2$, weiß nichts von x)')):
        gx, gy = np.meshgrid(np.arange(L), np.arange(L))
        ax.scatter(gx, gy, s=2, color=HELLGRAU, zorder=1)
        ax.scatter([p[0] for p in konf], [p[1] for p in konf], s=46, color=TINTE, zorder=3)
        ax.set_xlim(-0.8, L - 0.2); ax.set_ylim(-0.8, L - 0.2); ax.set_aspect('equal')
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_title(titel, fontsize=9)
    ax = axs[0]
    ax.add_patch(Circle(x0, 1.45, facecolor=ROT, alpha=0.10, edgecolor='none', zorder=0))
    ax.scatter([x0[0]], [x0[1]], s=60, facecolor='white', edgecolor=ROT, linewidth=1.6, zorder=4)
    ax.annotate('x', x0, xytext=(x0[0] + 0.45, x0[1] + 0.45), color=ROT, fontsize=10, fontweight='bold')
    ax.annotate('Korrelationsloch', (x0[0] + 0.15, x0[1] - 1.45), xytext=(x0[0] + 0.15, -2.0), fontsize=8,
                color=ROT, ha='center', arrowprops=dict(arrowstyle='-', color=ROT, lw=0.7))
    for a in axs:
        a.set_ylim(-2.5, L - 0.2)
    fig.text(0.5, 0.02, 'Kondensat, wenn beide Verteilungen gut überlappen:  N₀/N ≥ (Affinität von P$_x$ und Q)²',
             ha='center', fontsize=9)
    fig.subplots_adjust(bottom=0.1, wspace=0.08)
    speichern(fig, 'abb1_bad.png')


# ---------------------------------------------------------------- Abb. 2: Weltlinien mit Lücke
def linie(rng, t0, t1, x, rate=0.5):
    """Irrfahrt in stetiger Zeit auf ℤ von (x, t0) bis t1: Sprungzeiten und Lagen."""
    zeiten, lagen, t = [t0], [x], t0
    while True:
        t += rng.exponential(1 / rate)
        if t >= t1:
            return np.array(zeiten), np.array(lagen)
        zeiten.append(t); lagen.append(lagen[-1] + rng.choice((-1, 1)))


def lage(l, t):
    zeiten, lagen = l
    return lagen[np.searchsorted(zeiten, t, side='right') - 1]


def treppe(l, t1):
    zeiten, lagen = l
    xs, ts = [lagen[0]], [zeiten[0]]
    for z, x in zip(zeiten[1:], lagen[1:]):
        xs += [xs[-1], x]; ts += [z, z]
    xs.append(xs[-1]); ts.append(t1)
    return np.array(xs), np.array(ts)


def abb2():
    rng = np.random.default_rng(11)
    T, unten, oben = 6.0, -1.6, 7.6
    xs_t, ys_k = 7, 12
    while True:
        durch = [linie(rng, unten, oben, x) for x in (1, 4, 10, 15, 18)]
        schwanz = linie(rng, 0.0, -unten, xs_t)                  # rückwärts in der Zeit erzeugt
        schwanz = (np.concatenate([[unten], -schwanz[0][:0:-1]]), schwanz[1][::-1])
        kopf = linie(rng, T, oben, ys_k)
        ok = True
        for t in np.linspace(unten, oben, 900):
            pos = [lage(l, t) for l in durch]
            if t <= 0:
                pos.append(lage(schwanz, t))
            if t >= T:
                pos.append(lage(kopf, t))
            if len(set(pos)) < len(pos):
                ok = False; break
        if ok and xs_t not in [lage(l, 0.0) for l in durch] and ys_k not in [lage(l, T) for l in durch]:
            break
    fig, ax = plt.subplots(figsize=(6.4, 3.9))
    for l in durch:
        x, t = treppe(l, oben); ax.plot(x, t, color=GRAU, lw=1.3)
    x, t = treppe(schwanz, 0.0); ax.plot(x, t, color=GRAU, lw=1.3)
    x, t = treppe(kopf, oben); ax.plot(x, t, color=GRAU, lw=1.3)
    ax.axhspan(0, T, color=ROT, alpha=0.06, lw=0)
    ax.annotate('', xy=(ys_k, T), xytext=(xs_t, 0),
                arrowprops=dict(arrowstyle='-|>', linestyle=(0, (4, 3)), color=ROT, lw=1.2, shrinkA=5, shrinkB=5))
    ax.scatter([xs_t], [0], marker='s', s=40, color=ROT, zorder=5)
    ax.scatter([ys_k], [T], s=48, facecolor='white', edgecolor=ROT, linewidth=1.6, zorder=5)
    ax.text(xs_t - 0.3, -0.75, 'Schwanz\n(x, 0)', fontsize=8, color=ROT, va='center', ha='right')
    ax.text(ys_k - 0.3, T + 0.75, 'Kopf\n(y, T)', fontsize=8, color=ROT, va='center', ha='right')
    ax.text(1.02, (T / 2 - unten) / (oben - unten), 'Lücke der Länge T:\nnur N − 1 Linien', fontsize=8.5, color=ROT,
            va='center', transform=ax.transAxes)
    ax.text(1.02, (-0.8 - unten) / (oben - unten), 'N Linien', fontsize=8.5, color=GRAU, va='center',
            transform=ax.transAxes)
    ax.text(1.02, (T + 0.8 - unten) / (oben - unten), 'N Linien', fontsize=8.5, color=GRAU, va='center',
            transform=ax.transAxes)
    ax.set_xlim(-0.5, 20.5); ax.set_ylim(unten, oben)
    ax.set_xlabel('Raum (Schnitt durch das Gitter)'); ax.set_ylabel('imaginäre Zeit τ')
    ax.set_yticks([0, T]); ax.set_yticklabels(['0', 'T']); ax.set_xticks([])
    for sp in ('top', 'right'):
        ax.spines[sp].set_visible(False)
    speichern(fig, 'abb2_luecke.png')


# ---------------------------------------------------------------- Abb. 3: Begegnungen von Routen
def irrfahrt(rng, n, t):
    schritte = np.array([(1, 0), (-1, 0), (0, 1), (0, -1)])
    return np.cumsum(schritte[rng.integers(4, size=(n, t))], axis=1)


def routen(rng, n, t, beta=0.25, stufen=13):
    """Häggström–Mossel-artig: je Zeitschritt eine Stufe l mit Gewicht 2^(−l beta);
    auf Stufe l bleibt die Richtung über Blöcke der Länge 2^l gleich."""
    schritte = np.array([(1, 0), (-1, 0), (0, 1), (0, -1)])
    p = 2.0 ** (-beta * np.arange(stufen)); p /= p.sum()
    tt = np.arange(t)
    pos = np.zeros((n, t, 2), dtype=np.int64)
    for i in range(n):
        richt = [rng.integers(4, size=t // 2 ** l + 1) for l in range(stufen)]
        l = rng.choice(stufen, size=t, p=p)
        d = np.array([richt[l[k]][tt[k] >> l[k]] for k in range(t)])
        pos[i] = np.cumsum(schritte[d], axis=0)
    return pos


def abb3():
    rng = np.random.default_rng(5)
    n, t = 1500, 4096
    a, b = irrfahrt(rng, n, t), irrfahrt(rng, n, t)
    treff_d = np.all(a == b, axis=2)
    ra, rb = routen(rng, n, t), routen(rng, n, t)
    treff_r = np.all(ra == rb, axis=2)
    zeiten = np.arange(1, t + 1)
    fig, axs = plt.subplots(1, 2, figsize=(6.8, 3.0))
    ax = axs[0]
    abst_d = np.linalg.norm(a[0] - b[0], axis=1)
    abst_r = np.linalg.norm(ra[0] - rb[0], axis=1)
    ax.plot(zeiten, abst_d + 1, color=BLAU, lw=0.9)
    ax.plot(zeiten, abst_r + 1, color=ROT, lw=0.9)
    ax.set_xscale('log'); ax.set_yscale('log')
    ax.set_xlabel('Zeitschritte t'); ax.set_ylabel('Abstand + 1')
    ax.set_title('ein Beispielpaar', fontsize=9)
    ax.text(0.03, 0.93, 'diffusiv', color=BLAU, transform=ax.transAxes, fontsize=8.5)
    ax.text(0.03, 0.83, 'gewählte Routen', color=ROT, transform=ax.transAxes, fontsize=8.5)
    ax = axs[1]
    kum_d = np.cumsum(treff_d.mean(0)); kum_r = np.cumsum(treff_r.mean(0))
    ax.plot(zeiten, kum_d, color=BLAU, lw=1.8, label='diffusive Linien (α = 1/2)')
    ax.plot(zeiten, kum_r, color=ROT, lw=1.8, label='Routen (α ≈ 3/4)')
    ax.set_xscale('log'); ax.set_xlabel('Zeitschritte t'); ax.set_ylabel('mittlere Zahl der Begegnungen')
    ax.set_title(f'Mittel über {n} Paare', fontsize=9)
    ax.text(t, kum_d[-1], f' {kum_d[-1]:.1f}', color=TINTE, va='center', fontsize=8)
    ax.text(t, kum_r[-1], f' {kum_r[-1]:.1f}', color=TINTE, va='center', fontsize=8)
    ax.legend(frameon=False, fontsize=8, loc='upper left')
    for ax in axs:
        ax.grid(color='#e6e6e6', lw=0.5); ax.set_axisbelow(True)
        for s in ('top', 'right'):
            ax.spines[s].set_visible(False)
    fig.tight_layout()
    print(f'  Abb. 3: Begegnungen bis t = {t}: diffusiv {kum_d[-1]:.2f}, Routen {kum_r[-1]:.2f}; '
          f'bei t = 512: {kum_d[511]:.2f} / {kum_r[511]:.2f}')
    speichern(fig, 'abb3_routen.png')


# ---------------------------------------------------------------- Abb. 4: Staffellauf über drei Scheiben
def stueck(rng, x0, x1, t0, t1):
    """Linienstück von (x0, t0) nach (x1, t1): senkrecht mit Sprüngen (Treppe)."""
    n = abs(x1 - x0)
    zeiten = np.sort(rng.uniform(t0 + 0.15, t1 - 0.15, size=n + 2))
    pkt, x = [(x0, t0)], x0
    schritte = [np.sign(x1 - x0)] * n + [0.0, 0.0]
    rng.shuffle(schritte)
    for zt, s in zip(zeiten, schritte):
        if s == 0:
            pkt += [(x, zt), (x + 0.12, zt), (x + 0.12, zt + 0.05), (x, zt + 0.05)] if False else []
            continue
        pkt += [(x, zt), (x + s * 0.5, zt)]
        x += s * 0.5
    pkt.append((x, t1))
    return np.array(pkt)


def abb4():
    rng = np.random.default_rng(2)
    zellen, scheiben = 5, 3
    # Lage der Linie jeder Zelle an den Scheibengrenzen (in Halbzellen-Einheiten)
    X = np.array([[c + 0.5 + rng.choice([-0.25, 0, 0.25]) for _ in range(scheiben + 1)] for c in range(zellen)])
    X[2, 2] = X[2, 3] = 2.4
    X2b = [2.82] * (scheiben + 1)      # zweites Teilchen in Zelle 2: Umstieg innerhalb der Zelle in Scheibe 1
    fig, ax = plt.subplots(figsize=(6.2, 4.9))
    route = {0: [0, 1, 2], 1: [2], 2: [2, 3]}
    for k, zs in route.items():
        for c in zs:
            ax.add_patch(Rectangle((c, k), 1, 1, facecolor=ROT, alpha=0.07, edgecolor='none'))
    for c in range(zellen + 1):
        ax.plot([c, c], [-0.45, scheiben + 0.45], color='#dddddd', lw=0.6, zorder=0)
    for k in range(scheiben + 1):
        ax.plot([0, zellen], [k, k], color='#cccccc', lw=0.6, ls=(0, (2, 2)), zorder=0)
    ersetzt = {(0, 0), (1, 0), (2, 0), (2, 1), (3, 2)}        # (Zelle, Scheibe): altes Stück weg
    bruecken = [((1, 0), (0, 1)), ((2, 0), (1, 1))]           # (Zelle Start, Scheibe), (Zelle Ende, Scheibe)

    def gerade(x0, x1, t0, t1, **kw):
        xm = x1 if abs(x1 - x0) < 0.3 else None
        if xm is not None:
            ax.plot([x0, x0, x1, x1], [t0, (t0 + t1) / 2, (t0 + t1) / 2, t1], **kw)
        else:
            tm = np.linspace(t0, t1, 5)[1:-1]
            xs = np.linspace(x0, x1, 4)
            px, pt = [x0], [t0]
            for i, z in enumerate(tm):
                px += [xs[i], xs[i + 1]]; pt += [z, z]
            px.append(x1); pt.append(t1)
            ax.plot(px, pt, **kw)

    for c in range(zellen):
        for k in range(scheiben):
            if (c, k) in ersetzt:
                gerade(X[c, k], X[c, k + 1], k, k + 1, color=HELLGRAU, lw=1.0, ls=(0, (1.5, 2)))
            else:
                gerade(X[c, k], X[c, k + 1], k, k + 1, color=GRAU, lw=1.4)
        if c != 0:
            ax.plot([X[c, 0], X[c, 0]], [-0.45, 0], color=GRAU, lw=1.4)
        if c != 2:
            ax.plot([X[c, 3], X[c, 3]], [3, 3.45], color=GRAU, lw=1.4)
    ax.plot([X[0, 0], X[0, 0]], [-0.45, 0], color=GRAU, lw=1.4)
    ax.plot([X[3, 3], X[3, 3]], [3, 3.45], color=GRAU, lw=1.4)
    ax.plot([X[2, 3], X[2, 3]], [3, 3.45], color=GRAU, lw=1.4)
    for (cs, ks), (ce, ke) in bruecken:
        gerade(X[cs, ks], X[ce, ke], ks, ke, color=BLAU, lw=2.0)
    # zweites Teilchen in Zelle 2: Scheibe 0 unverändert, Scheibe 1 und 2 ersetzt
    gerade(X2b[0], X2b[1], 0, 1, color=GRAU, lw=1.4)
    for k in (1, 2):
        gerade(X2b[k], X2b[k + 1], k, k + 1, color=HELLGRAU, lw=1.0, ls=(0, (1.5, 2)))
    ax.plot([X2b[0], X2b[0]], [-0.45, 0], color=GRAU, lw=1.4)
    ax.plot([X2b[3], X2b[3]], [3, 3.45], color=GRAU, lw=1.4)
    gerade(X2b[1], X[2, 2], 1, 2, color=BLAU, lw=2.0)        # Scheibe 1: j₁ an das Ende von j₀ umgehängt
    gerade(X[3, 2], X2b[3], 2, 3, color=BLAU, lw=2.0)        # Scheibe 2: Querschritt nach Zelle 3
    # Loch: Schwanz, Zwischenlagen, Lage zur Zeit 3δ
    loch = [(X[0, 0], 0), (X[2, 1], 1), (X2b[2], 2), (X[3, 3], 3)]
    for (x0, t0), (x1, t1) in zip(loch[:-1], loch[1:]):
        ax.add_patch(FancyArrowPatch((x0, t0), (x1, t1), arrowstyle='-|>', mutation_scale=9, color=ROT,
                                     lw=1.1, ls=(0, (4, 3)), zorder=4, shrinkA=4, shrinkB=4))
    ax.scatter([loch[0][0]], [0], marker='s', s=38, color=ROT, zorder=6)
    ax.scatter([p[0] for p in loch[1:]], [p[1] for p in loch[1:]], s=40, facecolor='white', edgecolor=ROT,
               linewidth=1.5, zorder=6)
    ax.text(X[0, 0] + 0.08, -0.3, 'Schwanz', color=ROT, fontsize=8)
    ax.text(X[3, 3] + 0.1, 3.22, 'Loch', color=ROT, fontsize=8)
    for l, c in enumerate((0, 1, 2)):
        ax.text(X[c, 0] - 0.05, 0.05, f'S{"₀₁₂"[l]}', fontsize=7.5, ha='right', va='bottom', color=TINTE)
        ax.text(X[c, 1] + 0.07, 1.04, f'Y{"₀₁₂"[l]}', fontsize=7.5, ha='left', va='bottom', color=TINTE)
    texte = {0: 'Scheibe 0\nc₀ → c₁ → c₂\n(m = 2)', 1: 'Scheibe 1\nUmstieg in\nder Zelle\n(m = 1, c₁ = c₀)',
             2: 'Scheibe 2\nein Quer-\nschritt (m = 1)'}
    for k, s in texte.items():
        ax.text(zellen + 0.1, k + 0.5, s, fontsize=8.5, va='center', color=TINTE)
    for c in range(zellen):
        ax.text(c + 0.5, -0.62, f'Zelle {c}', ha='center', fontsize=7.5, color=GRAU)
    ax.plot([], [], color=GRAU, lw=1.4, label='unverändertes Linienstück')
    ax.plot([], [], color=HELLGRAU, lw=1.0, ls=(0, (1.5, 2)), label='gelöscht bzw. ersetzt')
    ax.plot([], [], color=BLAU, lw=2.0, label='neu gezogene Brücke')
    ax.plot([], [], color=ROT, lw=1.1, ls=(0, (4, 3)), label='Weg des Lochs')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.06), ncol=2, frameon=False, fontsize=8.5)
    ax.set_xlim(-0.1, zellen + 0.05); ax.set_ylim(-0.75, 3.55)
    ax.set_xticks([]); ax.set_yticks(range(4)); ax.set_ylabel('Zeit (in Scheiben δ)')
    for s in ('top', 'right', 'bottom'):
        ax.spines[s].set_visible(False)
    speichern(fig, 'abb4_staffellauf.png')


# ---------------------------------------------------------------- Abb. 5: Gegen-Lücke
def abb5():
    fig = plt.figure(figsize=(6.9, 3.3))
    ax = fig.add_axes([0.0, 0.08, 0.36, 0.84])
    t = np.linspace(0, 1, 50)
    ax.fill_betweenx(t, 0.15 + 0.7 * t - 0.06, 0.15 + 0.7 * t + 0.06, color=ROT, alpha=0.30, lw=0)
    ax.fill_betweenx(t, 0.85 - 0.7 * t - 0.06, 0.85 - 0.7 * t + 0.06, color=BLAU, alpha=0.30, lw=0)
    ax.add_patch(Circle((0.5, 0.5), 0.12, facecolor='none', edgecolor=TINTE, lw=0.9, ls=(0, (2, 2))))
    ax.text(0.5, 0.5, 'Begeg-\nnung', ha='center', va='center', fontsize=7.5)
    ax.text(0.15, -0.04, 'R′ baut\ndie Lücke', fontsize=8, color=ROT, ha='center', va='top')
    ax.text(0.85, -0.04, 'R wertet\naus', fontsize=8, color=BLAU, ha='center', va='top')
    ax.text(0.30, 0.86, 'j: nur R', fontsize=8, color=BLAU, ha='left')
    ax.text(0.70, 0.86, 'l: nur R′', fontsize=8, color=ROT, ha='right')
    ax.set_xlim(0, 1); ax.set_ylim(-0.24, 1.02); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel('Raum'); ax.set_ylabel('Zeit')
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    bx = fig.add_axes([0.40, 0.04, 0.59, 0.92])
    zeilen = ['C  geschlossen', 'O  = Lücke längs R′', 'Ĉ  = O + Linie längs R', 'B  = C + Linie längs R']
    werte = [['N', 'N', 'N'], ['N', 'N − 1', 'N'], ['N + 1', 'N − 1', 'N'], ['N + 1', 'N', 'N']]
    farbe = {'N': '#eeeeee', 'N − 1': '#f6d3bf', 'N + 1': '#c6dcee'}
    spalten = ['j (nur R)', 'l (nur R′)', 'sonst']
    x0, b, h = 0.43, 0.17, 0.16
    for i, z in enumerate(zeilen):
        y = 0.72 - i * (h + 0.03)
        bx.text(0.0, y + h / 2, z, va='center', fontsize=8.5)
        for k in range(3):
            w = werte[i][k]
            bx.add_patch(Rectangle((x0 + k * (b + 0.02), y), b, h, facecolor=farbe[w], edgecolor='#999999', lw=0.5))
            bx.text(x0 + k * (b + 0.02) + b / 2, y + h / 2, w, ha='center', va='center', fontsize=9)
    for k, s in enumerate(spalten):
        bx.text(x0 + k * (b + 0.02) + b / 2, 0.92, s, ha='center', fontsize=8.5, color=(BLAU, ROT, GRAU)[k])

    def zeile_y(i):
        return 0.72 - i * (h + 0.03)

    bx.text(0.0, 0.0, 'Auf j: O = C und Ĉ = B.   Auf l: Ĉ = O und B = C.', fontsize=8.5, color=GRUEN, va='top',
            fontweight='bold')
    bx.text(0.0, -0.09, 'Also ist der Quotient Ĉ/O überall gleich B/C: Die bedingten Zustandssummen\n'
            '(gleiche Teilchenzahl, gleicher Rand) kürzen sich, Kosten nur an Begegnungen.',
            fontsize=8, color=TINTE, va='top')
    bx.set_xlim(0, 1.05); bx.set_ylim(-0.25, 1.0); bx.axis('off')
    speichern(fig, 'abb5_gegenluecke.png')


# ---------------------------------------------------------------- Abb. 2 (neu): offene Konfiguration zu gleicher Zeit
def abb2_offen():
    rng = np.random.default_rng(11)
    unten, oben = -3.0, 3.0
    xs_t, ys_k = 6, 13
    while True:
        durch = [linie(rng, unten, oben, x) for x in (1, 3, 9, 16, 19)]
        schwanz = linie(rng, 0.0, -unten, xs_t)
        schwanz = (np.concatenate([[unten], -schwanz[0][:0:-1]]), schwanz[1][::-1])
        kopf = linie(rng, 0.0, oben, ys_k)
        ok = True
        for t in np.linspace(unten, oben, 900):
            pos = [lage(l, t) for l in durch]
            pos.append(lage(schwanz, t) if t <= 0 else lage(kopf, t))
            if len(set(pos)) < len(pos):
                ok = False; break
        if ok and xs_t not in [lage(l, 0.0) for l in durch] and ys_k not in [lage(l, 0.0) for l in durch]:
            break
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for l in durch:
        x, t = treppe(l, oben); ax.plot(x, t, color=GRAU, lw=1.3)
    x, t = treppe(schwanz, 0.0); ax.plot(x, t, color=GRAU, lw=1.3)
    x, t = treppe(kopf, oben); ax.plot(x, t, color=GRAU, lw=1.3)
    ax.axhline(0, color=ROT, lw=0.6, ls=(0, (3, 3)), alpha=0.6)
    ax.scatter([xs_t], [0], marker='s', s=42, color=ROT, zorder=5)
    ax.scatter([ys_k], [0], s=50, facecolor='white', edgecolor=ROT, linewidth=1.6, zorder=5)
    ax.text(xs_t - 0.3, -0.55, 'Schwanz\n(x, 0)', fontsize=8, color=ROT, ha='right', va='center')
    ax.text(ys_k + 0.35, 0.55, 'Kopf\n(y, 0)', fontsize=8, color=ROT, ha='left', va='center')
    ax.text(1.02, 0.5, 'Zeit 0:\nhier endet eine Linie\nund eine beginnt', fontsize=8.5, color=ROT, va='center',
            transform=ax.transAxes)
    ax.text(1.02, 0.85, 'N Linien', fontsize=8.5, color=GRAU, va='center', transform=ax.transAxes)
    ax.text(1.02, 0.15, 'N Linien', fontsize=8.5, color=GRAU, va='center', transform=ax.transAxes)
    ax.set_xlim(-0.5, 20.5); ax.set_ylim(unten, oben)
    ax.set_xlabel('Raum (Schnitt durch das Gitter)'); ax.set_ylabel('imaginäre Zeit τ')
    ax.set_yticks([0]); ax.set_yticklabels(['0']); ax.set_xticks([])
    for sp in ('top', 'right'):
        ax.spines[sp].set_visible(False)
    speichern(fig, 'abb2_offen.png')


# ---------------------------------------------------------------- Abb. 6: die Zeitschleife
def abb6_zeitschleife():
    rng = np.random.default_rng(4)
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    T = 1.0
    for xl in np.linspace(0.05, 0.95, 9):
        t = np.linspace(-0.15, 1.15, 14)
        xx = xl + np.cumsum(rng.normal(0, 0.008, t.size))
        ax.step(xx, t, color=HELLGRAU, lw=1.0, where='post', zorder=0)
    x0, y0, c = 0.22, 0.78, 0.55
    n = 40
    tu = np.linspace(0, T, n)
    xu = x0 + (c - x0) * tu / T + np.cumsum(rng.normal(0, 0.012, n)) * (1 - np.abs(2 * tu / T - 1)) * 0.6
    xu[0], xu[-1] = x0, c
    td = np.linspace(T, 0, n)
    xd = c + (y0 - c) * (1 - td / T) + np.cumsum(rng.normal(0, 0.012, n)) * (1 - np.abs(2 * td / T - 1)) * 0.6
    xd[0], xd[-1] = c, y0
    ax.plot(xu, tu, color=ROT, lw=2.0, ls=(0, (4, 2)))
    ax.plot(xd, td, color=BLAU, lw=2.4)
    ax.annotate('', xy=(xu[n // 2 + 1], tu[n // 2 + 1]), xytext=(xu[n // 2 - 1], tu[n // 2 - 1]),
                arrowprops=dict(arrowstyle='-|>', color=ROT, lw=1.2))
    ax.annotate('', xy=(xd[n // 2 + 1], td[n // 2 + 1]), xytext=(xd[n // 2 - 1], td[n // 2 - 1]),
                arrowprops=dict(arrowstyle='-|>', color=BLAU, lw=1.2))
    ax.axhline(0, color=TINTE, lw=0.6, ls=(0, (3, 3)))
    ax.axhline(T, color=TINTE, lw=0.4, ls=(0, (1, 3)))
    ax.scatter([x0], [0], marker='s', s=46, color=ROT, zorder=5)
    ax.scatter([y0], [0], s=54, facecolor='white', edgecolor=ROT, linewidth=1.6, zorder=5)
    ax.scatter([c], [T], s=26, color=TINTE, zorder=5)
    ax.text(x0, -0.09, 'Schwanz (x, 0)', ha='center', va='top', fontsize=8.5, color=ROT)
    ax.text(y0, -0.09, 'Kopf (y, 0)', ha='center', va='top', fontsize=8.5, color=ROT)
    ax.text(c, T + 0.05, 'Wende (Zeit T)', ha='center', va='bottom', fontsize=8.5, color=TINTE)
    ax.text(0.30, 0.62, 'hinauf (U):\nLoch wandert nach oben,\nStücke werden gelöscht', fontsize=8.5, color=ROT,
            ha='right', va='center')
    ax.text(0.75, 0.62, 'hinab (D):\nKopf wandert nach unten,\nStücke werden eingefügt', fontsize=8.5, color=BLAU,
            ha='left', va='center')
    ax.text(0.5, -0.25, 'zu jeder Zeit 0 < t < T:  eine Linie weniger längs U, eine mehr längs D  ⇒  N Linien',
            ha='center', fontsize=8.5, color=TINTE)
    ax.set_xlim(0, 1); ax.set_ylim(-0.32, 1.18)
    ax.set_xticks([]); ax.set_yticks([0, T]); ax.set_yticklabels(['0', 'T'])
    ax.set_xlabel('Raum'); ax.set_ylabel('imaginäre Zeit')
    for sp in ('top', 'right'):
        ax.spines[sp].set_visible(False)
    speichern(fig, 'abb6_zeitschleife.png')


# ---------------------------------------------------------------- Abb. 5 (neu): zwei Schleifen und die Linienzahlen
def abb5_schleifen():
    fig = plt.figure(figsize=(7.0, 3.4))
    ax = fig.add_axes([0.0, 0.08, 0.34, 0.84])
    t = np.linspace(0, 1, 60)
    for (cx, farbe, name, dx) in ((0.42, ROT, 'R′', -0.06), (0.62, BLAU, 'R', 0.06)):
        up = 0.15 + (cx - 0.15) * t + dx * np.sin(np.pi * t)
        dn = cx + (0.85 - cx) * t - dx * np.sin(np.pi * t)
        ax.plot(up, t, color=farbe, lw=2.0, ls=(0, (4, 2)) if farbe == ROT else '-')
        ax.plot(dn, 1 - t, color=farbe, lw=2.0, ls=(0, (4, 2)) if farbe == ROT else '-')
        ax.text(cx, 1.04, name, color=farbe, ha='center', fontsize=9)
    ax.scatter([0.15], [0], marker='s', s=36, color=TINTE, zorder=5)
    ax.scatter([0.85], [0], s=40, facecolor='white', edgecolor=TINTE, lw=1.3, zorder=5)
    ax.text(0.15, -0.07, 'x', ha='center', va='top', fontsize=9); ax.text(0.85, -0.07, 'y', ha='center', va='top', fontsize=9)
    ax.axhline(0, color=TINTE, lw=0.5, ls=(0, (3, 3)))
    ax.set_xlim(0, 1); ax.set_ylim(-0.2, 1.12); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel('Raum'); ax.set_ylabel('Zeit')
    for sp in ('top', 'right'):
        ax.spines[sp].set_visible(False)
    bx = fig.add_axes([0.38, 0.02, 0.62, 0.94])
    zeilen = ['C  geschlossen', 'O  = Schleife längs R′', 'Ĉ  = O + Rückweg längs R', 'B  = C + Rückweg längs R']
    werte = [['0', '0', '0', '0'], ['−1', '+1', '0', '0'], ['−1', '+1', '+1', '−1'], ['0', '0', '+1', '−1']]
    farbe = {'0': '#eeeeee', '−1': '#f6d3bf', '+1': '#c6dcee'}
    spalten = ['U′', 'D′', 'U', 'D']
    x0, b, h = 0.40, 0.11, 0.15
    for i, z in enumerate(zeilen):
        y = 0.70 - i * (h + 0.03)
        bx.text(0.0, y + h / 2, z, va='center', fontsize=8.3)
        for k in range(4):
            wv = werte[i][k]
            bx.add_patch(Rectangle((x0 + k * (b + 0.015), y), b, h, facecolor=farbe[wv], edgecolor='#999999', lw=0.5))
            bx.text(x0 + k * (b + 0.015) + b / 2, y + h / 2, wv, ha='center', va='center', fontsize=9)
        bx.text(x0 + 4 * (b + 0.015) + 0.01, y + h / 2, 'Summe N', va='center', fontsize=8, color=GRAU)
    for k, sname in enumerate(spalten):
        bx.text(x0 + k * (b + 0.015) + b / 2, 0.90, sname, ha='center', fontsize=9, color=(ROT, ROT, BLAU, BLAU)[k])
    bx.text(0.0, 0.0, 'Linienzahl relativ zu C zur Zeit 0 < t < T, nahe den Hälften der beiden Schleifen.\n'
            'B hat zu jeder Zeit N Linien: wieder eine offene Konfiguration zu gleicher Zeit.', fontsize=8,
            color=TINTE, va='top')
    bx.set_xlim(0, 1.08); bx.set_ylim(-0.14, 1.0); bx.axis('off')
    speichern(fig, 'abb5_schleifen.png')


if __name__ == '__main__':
    abb1(); abb2(); abb3(); abb4(); abb5(); abb2_offen(); abb6_zeitschleife(); abb5_schleifen()
