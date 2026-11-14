#!/usr/bin/env python3
"""Wurm-Algorithmus für Stufe A in numba: wurm_nb3.py plus Histogramme der Kopf-Schwanz-Abstände (G-Sektor).

hist_eq[ix, iy]: gleichzeitige Paarkorrelation (Zeitfenster w, Ordnung "erst vernichten", wie die bisherigen Klassen);
hist_all[ix, iy]: über die Zeit integriert (omega = 0), jede G-Messung ohne Überlappung, nur großkanonisch.
hist_tau[ib]: Zeitabstand vom vernichtenden zum erzeugenden Ende (Länge der Lücke), über alle Verschiebungen summiert
(k = 0), ib = floor(tau / beta * len(hist_tau)); kanonisch nur Konfigurationen mit n Teilchen außerhalb der Lücke.
Gewicht der Lücke im Wurm: exp(-mu tau), also G_k=0(tau) ~ exp(mu tau) hist_tau (bis auf eine Konstante).
Index ix = 2 dx mod 2L, iy = 2 dy mod 2L mit der Verschiebung (dx, dy) vom vernichtenden zum erzeugenden Ende.
hist(r) / hist(0) = g(r) / g(0). Die Kette ist dieselbe wie in wurm_nb3.py (Messungen ziehen keine Zufallszahlen).

wurm_nb3.py: wurm_nb2.py plus der Zug "Kink verschieben" (Lehre 9 der README).

Neu gegenüber wurm_nb2.py: Liste aller Kinks (klist, kpos) und ein siebter G-Sektor-Zug, der einen zufälligen Kink
gleichverteilt zwischen den benachbarten Ereignissen seiner beiden Plätze verschiebt (Annahme exp(-V dT) und Radiusregel;
Teilchenzahl und Windung bleiben). Damit können zurückgelassene Überlappungen abgebaut werden, ohne dass der Kopf
zurückkehrt. Mit p[6] = 0 ist die Kette bitgleich zu wurm_nb2.py.

Frühere Unterschiede (wurm_nb2 gegenüber wurm_nb):

Unterschiede zu wurm_nb.py (bei gleichem Seed bitgleiche Ergebnisse, siehe test_nb2.py):
  - Ereignistabelle als ein Datensatz je Ereignis (32 Byte: t, dx, dy, a, b, typ) statt fünf getrennter Felder.
  - Liste der verletzten Plätze (vlist, vpos); radius_ok und das Zurücksetzen laufen nur über diese Liste, nicht
    über alle M Plätze.
  - Abstand (Radiusregel) und Messklasse aus Koordinaten statt aus M x M-Tabellen.
  - int32 für Plätze und Ereignisnummern; kleinere Kapazität je Platz, die bei Bedarf verdoppelt wird.
  - fwd ohne Gleitkomma-Modulo (gleiches Ergebnis für Zeiten in [0, beta]).

Großkanonisch oder kanonisch, weicher Ausschluss im G-Sektor (Strafgewicht exp(-V T_viol)) mit Radiusregel
(Überlappungen nur an Plätzen im Abstand <= R vom Kopf). Die Radiusregel wird vor dem Zug geprüft (die neuen
Überlappzeiten folgen aus den Beiträgen), daher kein Zurücknehmen.

Zustand in Arrays:
  tim[M, CAP], eid[M, CAP], cnt[M]   Ereignisse je Platz (sortiert)
  ev[E] (t, dx, dy, a, b, typ)       Ereignistabelle (Typ 1 Kink a -> b, 2 Kopf, 3 Schwanz)
  n0[M], vsite[M], vflag[M]          Besetzung bei 0, Überlappzeit je Platz, Platz verletzt
  vlist[nv], vpos[M]                 verletzte Plätze und ihre Position in vlist (-1: nicht verletzt)
Mitgeführt: Kinkzahl, Summe der Kink-Verschiebungen (Windung), Teilchenzahl bei 0, T_viol.
"""
import numpy as np
import numba as nb
from numba import njit

CAP = 32          # Anfangskapazität je Platz; wird verdoppelt, wenn ein Platz CAP - RAND erreicht
RAND = 8          # ein Zug fügt je Platz höchstens 2 Ereignisse hinzu
ECAP = 200000
TOL = 1e-12
EV = np.dtype([('t', np.float64), ('dx', np.float32), ('dy', np.float32), ('a', np.int32), ('b', np.int32),
               ('typ', np.int32), ('pad', np.int32)], align=True)

# Indizes in den Skalar-Arrays
I_HEAD, I_TAIL, I_NFREE, I_NK, I_N0, I_SEED, I_NV, I_VOLL = 0, 1, 2, 3, 4, 5, 6, 7
F_T, F_MU, F_SDX, F_SDY = 0, 1, 2, 3


def neu(g, n, beta, t=1.0, mu=0.0, V=30.0, R=3.5, Cw=None, Delta=None, w=0.05, seed=1, kanonisch=False):
    """Zustand anlegen; Rückgabe: dict mit Konstanten und Arrays."""
    M, L = g['M'], g['L']
    rng = np.random.default_rng(seed)
    konf = np.array([np.pad(np.array(c, dtype=np.int32), (0, 22 - len(c)), constant_values=-1) for c in g['konflikt']])
    xy = np.array(g['mid'], dtype=np.float64)
    # Anzahl der Plätze je Messklasse (1 = r 0, 2 = (0, L/2), 3 = (L/2, L/2)), von Platz 0 aus gezählt
    n_cls = [sum(1 for j in range(M) if klasse(xy, L, 0, j) == c) for c in (1, 2, 3)]
    s = {
        'M': M, 'L': L, 'beta': beta, 't': t, 'V': V, 'w': w, 'kan': 1 if kanonisch else 0, 'n': n,
        'Cw': Cw if Cw is not None else 1.0 / (10 * M * beta),
        'Delta': Delta if Delta is not None else min(beta / 2, 1.0),
        'konf': konf, 'eck': np.array(g['eck'], dtype=np.int32), 'eck_d': np.array(g['eck_d'], dtype=np.float64),
        'xy': xy, 'R': float(R) if R is not None else 1e9, 'n_cls': n_cls,
        'tim': np.zeros((M, CAP)), 'eid': np.zeros((M, CAP), dtype=np.int32), 'cnt': np.zeros(M, dtype=np.int32),
        'ev': np.zeros(ECAP, dtype=EV),
        'free': np.arange(ECAP - 1, -1, -1, dtype=np.int32),
        'n0': np.zeros(M, dtype=np.int8), 'vsite': np.zeros(M), 'vflag': np.zeros(M, dtype=np.int8),
        'vlist': np.zeros(M, dtype=np.int32), 'vpos': np.full(M, -1, dtype=np.int32),
        'klist': np.zeros(ECAP, dtype=np.int32), 'kpos': np.full(ECAP, -1, dtype=np.int32),
        'hist_eq': np.zeros((2 * L, 2 * L)), 'hist_all': np.zeros((2 * L, 2 * L)), 'hist_tau': np.zeros(512),
        'iv': np.array([-1, -1, ECAP, 0, 0, seed, 0, 0], dtype=np.int64),
        'fv': np.array([0.0, mu, 0.0, 0.0]),
        'p': np.array([0.2, 0.16, 0.16, 0.08, 0.08, 0.12, 0.2]),   # Zeit, Kink+, Kink-, Umhängen, Abhängen, Schließen,
                                                                   # Kink verschieben
    }
    occ = []
    while len(occ) < n:
        k = int(rng.integers(M))
        if k not in occ and not any(k in g['konflikt'][o] for o in occ):
            occ.append(k)
    for k in occ:
        s['n0'][k] = 1
    s['iv'][I_N0] = n
    return s


# ---------------------------------------------------------------------------- Grundfunktionen
@njit(cache=True)
def fwd(a, b, beta):
    # gleich (b - a) % beta für a, b in [0, beta], ohne Division
    x = b - a
    if x < 0.0:
        x += beta
    elif x >= beta:
        x -= beta
    return x


@njit(cache=True)
def abstand2(xy, L, i, j):
    """Periodische Verschiebung von i nach j (wie in gitter.py)."""
    dx = (xy[j, 0] - xy[i, 0] + L / 2) % L - L / 2
    dy = (xy[j, 1] - xy[i, 1] + L / 2) % L - L / 2
    return dx, dy


@njit(cache=True)
def nah(xy, L, R, i, j):
    dx, dy = abstand2(xy, L, i, j)
    return np.sqrt(dx * dx + dy * dy) <= R


@njit(cache=True)
def klasse(xy, L, i, j):
    """Messklasse: 1 = gleicher Platz, 2 = (0, L/2), 3 = (L/2, L/2), sonst 0."""
    dx, dy = abstand2(xy, L, i, j)
    ax, ay = abs(dx), abs(dy)
    if ax < 1e-9 and ay < 1e-9:
        return 1
    if (ax < 1e-9 and abs(ay - L / 2) < 1e-9) or (ay < 1e-9 and abs(ax - L / 2) < 1e-9):
        return 2
    if abs(ax - L / 2) < 1e-9 and abs(ay - L / 2) < 1e-9:
        return 3
    return 0


@njit(cache=True)
def bis_right(tim, cnt, m, x):
    lo, hi = 0, cnt[m]
    while lo < hi:
        mid = (lo + hi) // 2
        if tim[m, mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


@njit(cache=True)
def bis_left(tim, cnt, m, x):
    lo, hi = 0, cnt[m]
    while lo < hi:
        mid = (lo + hi) // 2
        if tim[m, mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


@njit(cache=True)
def occ_after(tim, cnt, n0, m, x):
    return n0[m] ^ (bis_right(tim, cnt, m, x) & 1)


@njit(cache=True)
def occ_before(tim, cnt, n0, m, x):
    return n0[m] ^ (bis_left(tim, cnt, m, x) & 1)


@njit(cache=True)
def n_in(tim, cnt, m, a, b):
    if a < b:
        return bis_left(tim, cnt, m, b) - bis_right(tim, cnt, m, a)
    return (cnt[m] - bis_right(tim, cnt, m, a)) + bis_left(tim, cnt, m, b)


@njit(cache=True)
def occ_time(tim, cnt, n0, m, a, b, beta):
    length = fwd(a, b, beta)
    if length == 0.0:
        return 0.0
    o = occ_after(tim, cnt, n0, m, a)
    k = cnt[m]
    if k == 0:
        return length * o
    tot = 0.0
    last = 0.0
    i = bis_right(tim, cnt, m, a)
    for st in range(k):
        d = fwd(a, tim[m, (i + st) % k], beta)
        if d >= length or d == 0.0:
            break
        if o:
            tot += d - last
        o ^= 1
        last = d
    if o:
        tot += length - last
    return tot


@njit(cache=True)
def add_ev(tim, eid, cnt, iv, m, x, e):
    c = cnt[m]
    if c >= tim.shape[1]:
        raise RuntimeError('Kapazität je Platz überschritten')
    if c + 1 >= tim.shape[1] - RAND:
        iv[I_VOLL] = 1
    i = bis_left(tim, cnt, m, x)
    for j in range(c, i, -1):
        tim[m, j] = tim[m, j - 1]
        eid[m, j] = eid[m, j - 1]
    tim[m, i] = x
    eid[m, i] = e
    cnt[m] = c + 1


@njit(cache=True)
def rem_ev(tim, eid, cnt, m, e):
    c = cnt[m]
    i = 0
    while eid[m, i] != e:
        i += 1
    for j in range(i, c - 1):
        tim[m, j] = tim[m, j + 1]
        eid[m, j] = eid[m, j + 1]
    cnt[m] = c - 1


@njit(cache=True)
def dist_back(tim, eid, cnt, m, x, beta, ex1, ex2):
    d = beta
    best = -1
    for i in range(cnt[m]):
        e = eid[m, i]
        if e == ex1 or e == ex2:
            continue
        y = fwd(tim[m, i], x, beta)
        if 0.0 < y < d:
            d = y
            best = e
    return d, best


@njit(cache=True)
def dist_fwd(tim, eid, cnt, m, x, beta, ex1, ex2):
    d = beta
    best = -1
    for i in range(cnt[m]):
        e = eid[m, i]
        if e == ex1 or e == ex2:
            continue
        y = fwd(x, tim[m, i], beta)
        if 0.0 < y < d:
            d = y
            best = e
    return d, best


# ---------------------------------------------------------------------------- Überlappungen
@njit(cache=True)
def terms(tim, cnt, n0, konf, m, a, b, beta, ausser, out_s, out_o, k0):
    """Beiträge der Konfliktpartner von m im Bogen a -> b an out_s/out_o ab Index k0; Rückgabe (Summe, neues k)."""
    tot = 0.0
    k = k0
    for j in range(konf.shape[1]):
        s_ = konf[m, j]
        if s_ < 0 or s_ == ausser:
            continue
        o = occ_time(tim, cnt, n0, s_, a, b, beta)
        if o > 0.0:
            out_s[k] = s_
            out_o[k] = o
            k += 1
            tot += o
    return tot, k


@njit(cache=True)
def radius_ok(vsite, vflag, vlist, iv, xy, L, R, ms, signs, starts, out_s, out_o, nterm, newhead):
    """Prüft, ob nach Anwendung der Beiträge alle verletzten Plätze nahe newhead liegen (ohne anzuwenden)."""
    # Änderungen je betroffenem Platz sammeln (kleine Listen)
    aff = np.empty(64, dtype=np.int64)
    dv = np.zeros(64)
    na = 0
    for t_ in range(nterm):
        m = ms[t_]
        sg = signs[t_]
        for k in range(starts[t_], starts[t_ + 1]):
            for q in (m, out_s[k]):
                f = -1
                for i in range(na):
                    if aff[i] == q:
                        f = i
                        break
                if f < 0:
                    aff[na] = q
                    dv[na] = 0.0
                    f = na
                    na += 1
                dv[f] += sg * out_o[k]
    # alte verletzte Plätze, die nicht betroffen sind, bleiben verletzt
    for iq in range(iv[I_NV]):
        q = vlist[iq]
        betroffen = False
        for i in range(na):
            if aff[i] == q:
                betroffen = True
                break
        if not betroffen and not nah(xy, L, R, newhead, q):
            return False
    for i in range(na):
        if vsite[aff[i]] + dv[i] > 1e-12 and not nah(xy, L, R, newhead, aff[i]):
            return False
    return True


@njit(cache=True)
def apply_terms(vsite, vflag, vlist, vpos, iv, ms, signs, starts, out_s, out_o, nterm):
    for t_ in range(nterm):
        m = ms[t_]
        sg = signs[t_]
        for k in range(starts[t_], starts[t_ + 1]):
            s_ = out_s[k]
            vsite[m] += sg * out_o[k]
            vsite[s_] += sg * out_o[k]
            for q in (m, s_):
                if vsite[q] > 1e-12:
                    if not vflag[q]:
                        vflag[q] = 1
                        nv = iv[I_NV]
                        vlist[nv] = q
                        vpos[q] = nv
                        iv[I_NV] = nv + 1
                else:
                    vsite[q] = 0.0
                    if vflag[q]:
                        vflag[q] = 0
                        nv = iv[I_NV] - 1
                        p_ = vpos[q]
                        last = vlist[nv]
                        vlist[p_] = last
                        vpos[last] = p_
                        vpos[q] = -1
                        iv[I_NV] = nv


# ---------------------------------------------------------------------------- Ereignisverwaltung
@njit(cache=True)
def alloc(free, iv):
    iv[I_NFREE] -= 1
    return free[iv[I_NFREE]]


@njit(cache=True)
def release(free, iv, e):
    free[iv[I_NFREE]] = e
    iv[I_NFREE] += 1


@njit(cache=True)
def toggle(n0, iv, m):
    n0[m] ^= 1
    iv[I_N0] += 1 if n0[m] else -1


# ---------------------------------------------------------------------------- Hauptschleife
@njit(cache=True)
def seed_rng(s):
    np.random.seed(s)


@njit(cache=True)
def laufe(tim, eid, cnt, ev, free, n0, vsite, vflag, vlist, vpos, klist, kpos, hist_eq, hist_all, hist_tau, iv, fv,
          konf, eck,
          eck_d, xy, R,
          p, M, L, beta, t, V, w, kan, n, Cw, Delta, it0, nsteps, mevery):
    """Schritte it0 ... nsteps-1; Rückgabe (Summen, erreichter Schritt). Kehrt vorzeitig zurück, wenn ein Platz
    fast voll ist (iv[I_VOLL]); lauf() vergrößert dann die Felder und setzt fort."""
    out_s = np.empty(256, dtype=np.int64)
    out_o = np.empty(256)
    ms = np.empty(2, dtype=np.int64)
    signs = np.empty(2)
    starts = np.zeros(3, dtype=np.int64)
    acc = np.zeros(9)          # nZ, sK, sN, sWx2, sWy2, g1, g2, g3, Prüfzähler (kanonisch, M <= 64)
    ntau = hist_tau.shape[0]
    pz, pkp, pkm, pum, pab, pzu = p[0], p[1], p[2], p[3], p[4], p[5]
    for it in range(it0, nsteps):
        if iv[I_VOLL]:
            return acc, it
        head = iv[I_HEAD]
        mu = fv[F_MU]
        if head < 0:
            # ---------------------------------------------------- Wurm einsetzen
            m = int(np.random.random() * M)
            tt = np.random.random() * beta
            d = (2.0 * np.random.random() - 1.0) * Delta
            th = (tt + d) % beta
            if d > 0:
                a1, a2 = tt, th
            else:
                a1, a2 = th, tt
            if n_in(tim, cnt, m, a1, a2) == 0:
                cc = occ_after(tim, cnt, n0, m, a1)
                nterm = 0
                dT = 0.0
                if cc == 0:
                    dT, k = terms(tim, cnt, n0, konf, m, a1, a2, beta, -1, out_s, out_o, 0)
                    ms[0] = m
                    signs[0] = 1.0
                    starts[0] = 0
                    starts[1] = k
                    nterm = 1
                A = Cw * M * beta * 2 * Delta * pzu * np.exp(mu * abs(d) * (1 - 2 * cc) - V * dT)
                if A >= 1.0 or np.random.random() < A:
                    et = alloc(free, iv)
                    eh = alloc(free, iv)
                    ev[et].typ = 3
                    ev[et].t = tt
                    ev[et].a = m
                    ev[eh].typ = 2
                    ev[eh].t = th
                    ev[eh].a = m
                    add_ev(tim, eid, cnt, iv, m, tt, et)
                    add_ev(tim, eid, cnt, iv, m, th, eh)
                    if a2 < a1:
                        toggle(n0, iv, m)
                    iv[I_HEAD] = eh
                    iv[I_TAIL] = et
                    fv[F_T] = dT
                    apply_terms(vsite, vflag, vlist, vpos, iv, ms, signs, starts, out_s, out_o, nterm)
        else:
            x_ = np.random.random()
            h = ev[head].a
            th = ev[head].t
            if x_ < pz:
                # ------------------------------------------------ Kopf in der Zeit
                db, _ = dist_back(tim, eid, cnt, h, th, beta, head, -2)
                df, _ = dist_fwd(tim, eid, cnt, h, th, beta, head, -2)
                s = -db + np.random.random() * (db + df)
                if s != 0.0:
                    if s > 0:
                        a1 = th
                        a2 = (th + s) % beta
                        cc = occ_after(tim, cnt, n0, h, th)
                        wraps = th + s >= beta
                    else:
                        a1 = (th + s) % beta
                        a2 = th
                        cc = occ_before(tim, cnt, n0, h, th)
                        wraps = th + s < 0
                    sg = 1.0 if cc == 0 else -1.0
                    dd, k = terms(tim, cnt, n0, konf, h, a1, a2, beta, -1, out_s, out_o, 0)
                    dT = sg * dd
                    ms[0] = h
                    signs[0] = sg
                    starts[0] = 0
                    starts[1] = k
                    A = np.exp(mu * abs(s) * (1 - 2 * cc) - V * dT)
                    if (A >= 1.0 or np.random.random() < A) and radius_ok(vsite, vflag, vlist, iv, xy, L, R, ms, signs, starts,
                                                                          out_s, out_o, 1, h):
                        tn = (th + s) % beta
                        rem_ev(tim, eid, cnt, h, head)
                        ev[head].t = tn
                        add_ev(tim, eid, cnt, iv, h, tn, head)
                        if wraps:
                            toggle(n0, iv, h)
                        fv[F_T] += dT
                        apply_terms(vsite, vflag, vlist, vpos, iv, ms, signs, starts, out_s, out_o, 1)
            elif x_ < pz + pkp:
                # ------------------------------------------------ Kink einsetzen
                r = int(np.random.random() * 4)
                j = eck[h, r]
                ok = True
                if occ_before(tim, cnt, n0, h, th) == 1:
                    dh, _ = dist_back(tim, eid, cnt, h, th, beta, head, -2)
                    dj, _ = dist_back(tim, eid, cnt, j, th, beta, -2, -2)
                    ell = min(dh, dj)
                    tk_un = th - np.random.random() * ell
                    tk = tk_un % beta
                    if occ_before(tim, cnt, n0, j, th) != 0:
                        ok = False
                    a1, a2 = tk, th
                    src, dst = h, j
                    dx0, dx1 = eck_d[h, r, 0], eck_d[h, r, 1]
                    wraps = tk_un < 0
                else:
                    dh, _ = dist_fwd(tim, eid, cnt, h, th, beta, head, -2)
                    dj, _ = dist_fwd(tim, eid, cnt, j, th, beta, -2, -2)
                    ell = min(dh, dj)
                    tk_un = th + np.random.random() * ell
                    tk = tk_un % beta
                    if occ_after(tim, cnt, n0, j, th) != 0:
                        ok = False
                    a1, a2 = th, tk
                    src, dst = j, h
                    dx0, dx1 = -eck_d[h, r, 0], -eck_d[h, r, 1]
                    wraps = tk_un >= beta
                if ok:
                    d1, k1 = terms(tim, cnt, n0, konf, j, a1, a2, beta, h, out_s, out_o, 0)
                    d2, k2 = terms(tim, cnt, n0, konf, h, a1, a2, beta, j, out_s, out_o, k1)
                    dT = d1 - d2
                    ms[0] = j
                    signs[0] = 1.0
                    ms[1] = h
                    signs[1] = -1.0
                    starts[0] = 0
                    starts[1] = k1
                    starts[2] = k2
                    A = t * ell * 4 * pkm / pkp * np.exp(-V * dT)
                    if (A >= 1.0 or np.random.random() < A) and radius_ok(vsite, vflag, vlist, iv, xy, L, R, ms, signs, starts,
                                                                          out_s, out_o, 2, j):
                        ek = alloc(free, iv)
                        ev[ek].typ = 1
                        ev[ek].t = tk
                        ev[ek].a = src
                        ev[ek].b = dst
                        ev[ek].dx = dx0
                        ev[ek].dy = dx1
                        rem_ev(tim, eid, cnt, h, head)
                        add_ev(tim, eid, cnt, iv, h, tk, ek)
                        add_ev(tim, eid, cnt, iv, j, tk, ek)
                        ev[head].a = j
                        add_ev(tim, eid, cnt, iv, j, th, head)
                        if wraps:
                            toggle(n0, iv, h)
                            toggle(n0, iv, j)
                        klist[iv[I_NK]] = ek
                        kpos[ek] = iv[I_NK]
                        iv[I_NK] += 1
                        fv[F_SDX] += dx0
                        fv[F_SDY] += dx1
                        fv[F_T] += dT
                        apply_terms(vsite, vflag, vlist, vpos, iv, ms, signs, starts, out_s, out_o, 2)
            elif x_ < pz + pkp + pkm:
                # ------------------------------------------------ Kink entfernen
                j = h
                ok = True
                if occ_before(tim, cnt, n0, j, th) == 1:
                    _, ek = dist_back(tim, eid, cnt, j, th, beta, head, -2)
                    if ek < 0 or ev[ek].typ != 1 or ev[ek].b != j:
                        ok = False
                    else:
                        tk = ev[ek].t
                        hh = ev[ek].a
                        a1, a2 = tk, th
                        if n_in(tim, cnt, hh, a1, a2) > 0:
                            ok = False
                        dh, _ = dist_back(tim, eid, cnt, hh, th, beta, ek, -2)
                        dj, _ = dist_back(tim, eid, cnt, j, th, beta, ek, head)
                        wraps = tk > th
                else:
                    _, ek = dist_fwd(tim, eid, cnt, j, th, beta, head, -2)
                    if ek < 0 or ev[ek].typ != 1 or ev[ek].a != j:
                        ok = False
                    else:
                        tk = ev[ek].t
                        hh = ev[ek].b
                        a1, a2 = th, tk
                        if n_in(tim, cnt, hh, a1, a2) > 0:
                            ok = False
                        dh, _ = dist_fwd(tim, eid, cnt, hh, th, beta, ek, -2)
                        dj, _ = dist_fwd(tim, eid, cnt, j, th, beta, ek, head)
                        wraps = tk < th
                if ok:
                    ell = min(dh, dj)
                    d1, k1 = terms(tim, cnt, n0, konf, hh, a1, a2, beta, j, out_s, out_o, 0)
                    d2, k2 = terms(tim, cnt, n0, konf, j, a1, a2, beta, hh, out_s, out_o, k1)
                    dT = d1 - d2
                    ms[0] = hh
                    signs[0] = 1.0
                    ms[1] = j
                    signs[1] = -1.0
                    starts[0] = 0
                    starts[1] = k1
                    starts[2] = k2
                    A = pkp / (t * ell * 4 * pkm) * np.exp(-V * dT)
                    if (A >= 1.0 or np.random.random() < A) and radius_ok(vsite, vflag, vlist, iv, xy, L, R, ms, signs, starts,
                                                                          out_s, out_o, 2, hh):
                        rem_ev(tim, eid, cnt, hh, ek)
                        rem_ev(tim, eid, cnt, j, ek)
                        nk_ = iv[I_NK] - 1
                        p_ = kpos[ek]
                        letzter = klist[nk_]
                        klist[p_] = letzter
                        kpos[letzter] = p_
                        kpos[ek] = -1
                        iv[I_NK] -= 1
                        fv[F_SDX] -= ev[ek].dx
                        fv[F_SDY] -= ev[ek].dy
                        ev[ek].typ = 0
                        release(free, iv, ek)
                        rem_ev(tim, eid, cnt, j, head)
                        ev[head].a = hh
                        add_ev(tim, eid, cnt, iv, hh, th, head)
                        if wraps:
                            toggle(n0, iv, hh)
                            toggle(n0, iv, j)
                        fv[F_T] += dT
                        apply_terms(vsite, vflag, vlist, vpos, iv, ms, signs, starts, out_s, out_o, 2)
            elif x_ < pz + pkp + pkm + pum:
                # ------------------------------------------------ Umhängen
                j = h
                ok = True
                if occ_after(tim, cnt, n0, j, th) == 1:
                    _, ek = dist_back(tim, eid, cnt, j, th, beta, head, -2)
                    if ek < 0 or ev[ek].typ != 1 or ev[ek].a != j:
                        ok = False
                    else:
                        tk = ev[ek].t
                        xx = ev[ek].b
                        a1, a2 = tk, th
                        wraps = tk > th
                        ell, _ = dist_fwd(tim, eid, cnt, j, tk, beta, ek, head)
                else:
                    _, ek = dist_fwd(tim, eid, cnt, j, th, beta, head, -2)
                    if ek < 0 or ev[ek].typ != 1 or ev[ek].b != j:
                        ok = False
                    else:
                        tk = ev[ek].t
                        xx = ev[ek].a
                        a1, a2 = th, tk
                        wraps = tk < th
                        ell, _ = dist_back(tim, eid, cnt, j, tk, beta, ek, head)
                if ok:
                    dT, k1 = terms(tim, cnt, n0, konf, j, a1, a2, beta, -1, out_s, out_o, 0)
                    ms[0] = j
                    signs[0] = 1.0
                    starts[0] = 0
                    starts[1] = k1
                    A = np.exp(-V * dT + mu * fwd(a1, a2, beta)) * pab / (4 * t * ell * pum)
                    if (A >= 1.0 or np.random.random() < A) and radius_ok(vsite, vflag, vlist, iv, xy, L, R, ms, signs, starts,
                                                                          out_s, out_o, 1, xx):
                        rem_ev(tim, eid, cnt, j, ek)
                        rem_ev(tim, eid, cnt, xx, ek)
                        nk_ = iv[I_NK] - 1
                        p_ = kpos[ek]
                        letzter = klist[nk_]
                        klist[p_] = letzter
                        kpos[letzter] = p_
                        kpos[ek] = -1
                        iv[I_NK] -= 1
                        fv[F_SDX] -= ev[ek].dx
                        fv[F_SDY] -= ev[ek].dy
                        ev[ek].typ = 0
                        release(free, iv, ek)
                        rem_ev(tim, eid, cnt, j, head)
                        ev[head].a = xx
                        ev[head].t = tk
                        add_ev(tim, eid, cnt, iv, xx, tk, head)
                        if wraps:
                            toggle(n0, iv, j)
                        fv[F_T] += dT
                        apply_terms(vsite, vflag, vlist, vpos, iv, ms, signs, starts, out_s, out_o, 1)
            elif x_ < pz + pkp + pkm + pum + pab:
                # ------------------------------------------------ Abhängen
                xx = h
                tau = th
                r = int(np.random.random() * 4)
                j = eck[xx, r]
                ok = True
                if occ_after(tim, cnt, n0, xx, tau) == 1:
                    if occ_after(tim, cnt, n0, j, tau) != 1:
                        ok = False
                    else:
                        ell, _ = dist_fwd(tim, eid, cnt, j, tau, beta, -2, -2)
                        th_un = tau + np.random.random() * ell
                        a1 = tau
                        a2 = th_un % beta
                        wraps = th_un >= beta
                        src, dst = j, xx
                        dx0, dx1 = -eck_d[xx, r, 0], -eck_d[xx, r, 1]
                else:
                    if occ_before(tim, cnt, n0, j, tau) != 1:
                        ok = False
                    else:
                        ell, _ = dist_back(tim, eid, cnt, j, tau, beta, -2, -2)
                        th_un = tau - np.random.random() * ell
                        a1 = th_un % beta
                        a2 = tau
                        wraps = th_un < 0
                        src, dst = xx, j
                        dx0, dx1 = eck_d[xx, r, 0], eck_d[xx, r, 1]
                if ok:
                    dd, k1 = terms(tim, cnt, n0, konf, j, a1, a2, beta, -1, out_s, out_o, 0)
                    dT = -dd
                    ms[0] = j
                    signs[0] = -1.0
                    starts[0] = 0
                    starts[1] = k1
                    A = np.exp(-V * dT - mu * fwd(a1, a2, beta)) * 4 * t * ell * pum / pab
                    if (A >= 1.0 or np.random.random() < A) and radius_ok(vsite, vflag, vlist, iv, xy, L, R, ms, signs, starts,
                                                                          out_s, out_o, 1, j):
                        ek = alloc(free, iv)
                        ev[ek].typ = 1
                        ev[ek].t = tau
                        ev[ek].a = src
                        ev[ek].b = dst
                        ev[ek].dx = dx0
                        ev[ek].dy = dx1
                        rem_ev(tim, eid, cnt, xx, head)
                        add_ev(tim, eid, cnt, iv, xx, tau, ek)
                        add_ev(tim, eid, cnt, iv, j, tau, ek)
                        thn = th_un % beta
                        ev[head].a = j
                        ev[head].t = thn
                        add_ev(tim, eid, cnt, iv, j, thn, head)
                        if wraps:
                            toggle(n0, iv, j)
                        klist[iv[I_NK]] = ek
                        kpos[ek] = iv[I_NK]
                        iv[I_NK] += 1
                        fv[F_SDX] += dx0
                        fv[F_SDY] += dx1
                        fv[F_T] += dT
                        apply_terms(vsite, vflag, vlist, vpos, iv, ms, signs, starts, out_s, out_o, 1)
            elif x_ >= pz + pkp + pkm + pum + pab + pzu:
                # ------------------------------------------------ Kink verschieben
                nk = iv[I_NK]
                if nk > 0:
                    e = klist[int(np.random.random() * nk)]
                    ka, kb, t0 = ev[e].a, ev[e].b, ev[e].t
                    db1, _ = dist_back(tim, eid, cnt, ka, t0, beta, e, -2)
                    db2, _ = dist_back(tim, eid, cnt, kb, t0, beta, e, -2)
                    df1, _ = dist_fwd(tim, eid, cnt, ka, t0, beta, e, -2)
                    df2, _ = dist_fwd(tim, eid, cnt, kb, t0, beta, e, -2)
                    db = min(db1, db2)
                    df = min(df1, df2)
                    s = -db + np.random.random() * (db + df)
                    if s != 0.0:
                        # s > 0: ka gewinnt (t0, t0+s), kb verliert; s < 0: ka verliert (t0+s, t0), kb gewinnt
                        if s > 0:
                            a1, a2 = t0, (t0 + s) % beta
                            gew, verl = ka, kb
                            wraps = t0 + s >= beta
                        else:
                            a1, a2 = (t0 + s) % beta, t0
                            gew, verl = kb, ka
                            wraps = t0 + s < 0
                        d1, k1 = terms(tim, cnt, n0, konf, gew, a1, a2, beta, verl, out_s, out_o, 0)
                        d2, k2 = terms(tim, cnt, n0, konf, verl, a1, a2, beta, gew, out_s, out_o, k1)
                        dT = d1 - d2
                        ms[0] = gew
                        signs[0] = 1.0
                        ms[1] = verl
                        signs[1] = -1.0
                        starts[0] = 0
                        starts[1] = k1
                        starts[2] = k2
                        A = np.exp(-V * dT)
                        if (A >= 1.0 or np.random.random() < A) and radius_ok(vsite, vflag, vlist, iv, xy, L, R, ms,
                                                                              signs, starts, out_s, out_o, 2, h):
                            tn = (t0 + s) % beta
                            rem_ev(tim, eid, cnt, ka, e)
                            rem_ev(tim, eid, cnt, kb, e)
                            ev[e].t = tn
                            add_ev(tim, eid, cnt, iv, ka, tn, e)
                            add_ev(tim, eid, cnt, iv, kb, tn, e)
                            if wraps:
                                toggle(n0, iv, ka)
                                toggle(n0, iv, kb)
                            fv[F_T] += dT
                            apply_terms(vsite, vflag, vlist, vpos, iv, ms, signs, starts, out_s, out_o, 2)
            else:
                # ------------------------------------------------ Wurm entfernen
                tail = iv[I_TAIL]
                m = h
                if ev[tail].a == m:
                    tt = ev[tail].t
                    ok = True
                    if fwd(tt, th, beta) < Delta:
                        a1, a2 = tt, th
                    elif fwd(th, tt, beta) < Delta:
                        a1, a2 = th, tt
                    else:
                        ok = False
                    if ok and n_in(tim, cnt, m, a1, a2) == 0:
                        cc = occ_after(tim, cnt, n0, m, a1)
                        dd, k1 = terms(tim, cnt, n0, konf, m, a1, a2, beta, -1, out_s, out_o, 0)
                        dT = dd if cc == 0 else -dd
                        if abs(fv[F_T] + dT) <= 1e-7:
                            nn = iv[I_N0] + ((1 - 2 * n0[m]) if a2 < a1 else 0)
                            if kan == 0 or nn == n:
                                A = np.exp(mu * fwd(a1, a2, beta) * (1 - 2 * cc) - V * dT) / (
                                    Cw * M * beta * 2 * Delta * pzu)
                                if A >= 1.0 or np.random.random() < A:
                                    rem_ev(tim, eid, cnt, m, head)
                                    rem_ev(tim, eid, cnt, m, tail)
                                    ev[head].typ = 0
                                    ev[tail].typ = 0
                                    release(free, iv, head)
                                    release(free, iv, tail)
                                    if a2 < a1:
                                        toggle(n0, iv, m)
                                    iv[I_HEAD] = -1
                                    iv[I_TAIL] = -1
                                    fv[F_T] = 0.0
                                    for iq in range(iv[I_NV]):
                                        q = vlist[iq]
                                        vsite[q] = 0.0
                                        vflag[q] = 0
                                        vpos[q] = -1
                                    iv[I_NV] = 0
        # ---------------------------------------------------- Messen
        if it % mevery == 0:
            if iv[I_HEAD] < 0:
                acc[0] += 1
                acc[1] += iv[I_NK]
                acc[2] += iv[I_N0]
                wx = np.round(fv[F_SDX] / L)
                wy = np.round(fv[F_SDY] / L)
                acc[3] += wx * wx
                acc[4] += wy * wy
            elif abs(fv[F_T]) < 1e-7:
                hd = iv[I_HEAD]
                tl = iv[I_TAIL]
                hm, th2 = ev[hd].a, ev[hd].t
                tm, tt2 = ev[tl].a, ev[tl].t
                hv = occ_before(tim, cnt, n0, hm, th2) == 1
                if hv:
                    tv, te, vm, em = th2, tt2, hm, tm
                else:
                    tv, te, vm, em = tt2, th2, tm, hm
                ddx, ddy = abstand2(xy, L, vm, em)
                ix = int(np.floor(2.0 * ddx + 0.5)) % (2 * L)
                iy = int(np.floor(2.0 * ddy + 0.5)) % (2 * L)
                ib = int(fwd(tv, te, beta) / beta * ntau)
                if ib >= ntau:
                    ib = ntau - 1
                if kan == 0:
                    hist_all[ix, iy] += 1.0
                    hist_tau[ib] += 1.0
                else:
                    nout = iv[I_N0] + (1 if te < tv else 0)     # Teilchen außerhalb der Lücke
                    if nout == n:
                        hist_tau[ib] += 1.0
                    if M <= 64:                                  # Prüfung der Abkürzung gegen die volle Zählung
                        nn2 = 0
                        for q in range(M):
                            nn2 += occ_after(tim, cnt, n0, q, te)
                        if nn2 != nout:
                            acc[8] += 1
                if fwd(tv, te, beta) < w:
                    zaehlt = True
                    if kan == 1:
                        nn = 0
                        for q in range(M):
                            nn += occ_after(tim, cnt, n0, q, te)
                        zaehlt = nn == n
                    if zaehlt:
                        hist_eq[ix, iy] += 1.0
                        c = klasse(xy, L, vm, em)
                        if c > 0:
                            acc[4 + c] += 1
    return acc, nsteps


def lauf(s, nsteps, mevery=5):
    """Führt nsteps Schritte aus; Rückgabe der Summen (nZ, Kinks, N, Wx^2, Wy^2, g-Zählungen).
    Wird ein Platz fast voll, verdoppelt sich die Kapazität je Platz, und der Lauf geht beim selben Schritt weiter."""
    acc = np.zeros(9)
    it = 0
    s.setdefault('hist_tau', np.zeros(512))
    while True:
        a, it = laufe(s['tim'], s['eid'], s['cnt'], s['ev'], s['free'], s['n0'], s['vsite'], s['vflag'], s['vlist'],
                      s['vpos'], s['klist'], s['kpos'], s['hist_eq'], s['hist_all'], s['hist_tau'], s['iv'], s['fv'], s['konf'], s['eck'], s['eck_d'], s['xy'], s['R'], s['p'], s['M'],
                      s['L'], s['beta'], s['t'], s['V'], s['w'], s['kan'], s['n'], s['Cw'], s['Delta'], it, nsteps,
                      mevery)
        acc += a
        if it >= nsteps:
            return acc
        cap = 2 * s['tim'].shape[1]
        for k in ('tim', 'eid'):
            groesser = np.zeros((s['M'], cap), dtype=s[k].dtype)
            groesser[:, :s[k].shape[1]] = s[k]
            s[k] = groesser
        s['iv'][I_VOLL] = 0


def auswerten(s, acc):
    nZ = acc[0]
    norm = nZ * s['Cw'] * s['M'] * s['beta'] * 2 * s['w']
    return {'nZ': nZ, 'E': -acc[1] / nZ / s['beta'] * s['t'], 'N': acc[2] / nZ, 'Wx2': acc[3] / nZ,
            'Wy2': acc[4] / nZ, 'g_counts': acc[5:8].tolist(), 'g_norm': norm}
