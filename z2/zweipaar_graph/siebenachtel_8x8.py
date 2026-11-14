#!/usr/bin/env python
"""7/8-Füllung exakt: P Paare auf dem 8x8-Torus (P = 4 ist 7/8), voller Konfigurationsgraph.

- alle berührungsfreien P-Paar-Konfigurationen, Eckschritte, Komponenten
- Drift d, Poisson Lambda h = d auf der Hauptkomponente (CG mit pyamg-Vorkonditionierer)
- rho_s L^2 / t_c = <deg>/4 - 2 E / |C| (RK-Punkt), Abgleich mit stufe_a.md §15
- Zwei-Paar-Zerlegung: d = d2 + R mit d2(D) = sum_{p<q} d_2(rel(p,q)) aus two_pair_graph
- Paarsummen-Korrektor f2 = sum_{p<q} h_2(rel(p,q)) = d2 / 7: Anteil am paramagnetischen Abzug,
  mit Amplitude 1 und mit optimaler Amplitude lambda
- H^{-1}-Energien der Quellen d2 und R einzeln

Aufruf: python siebenachtel_8x8.py [--L 8] [--P 2 3 4]  -> ergebnisse/siebenachtel_8x8.json
"""

import argparse
import json
import os
import time

import numpy as np
import pyamg
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import cg

import two_pair_graph as tp

HIER = os.path.dirname(os.path.abspath(__file__))
LIT = {(8, 2): (1.8993, 1.9048), (8, 3): (2.6817, 2.6995), (8, 4): (3.3279, 3.3671)}  # stufe_a.md §15


def bindungen(L):
    nb = 2 * L * L
    b = np.arange(nb)
    ax, ay, o = b // 2 // L, (b // 2) % L, b % 2
    return ax, ay, o


def konfigurationen(L, P, kompat):
    """alle berührungsfreien P-Teilmengen der Bindungen, aufsteigend sortiert (n x P)."""
    nb = kompat.shape[0]
    T = np.arange(nb)[:, None]
    for _ in range(P - 1):
        ok = np.ones((T.shape[0], nb), bool)
        for i in range(T.shape[1]):
            ok &= kompat[T[:, i]]
        ok &= np.arange(nb)[None, :] > T[:, -1:]
        r, c = np.nonzero(ok)
        T = np.concatenate([T[r], c[:, None]], axis=1)
    return T


def schluessel(T, nb):
    k = np.zeros(T.shape[0], np.int64)
    for i in range(T.shape[1]):
        k = k * nb + T[:, i]
    return k


def loese(Lap, b, ml, rtol=1e-10):
    """CG mit AMG-Vorkonditionierer (Hierarchie ml einmal je Matrix). b muss Summe 0 haben
    (Bild des Neumann-Laplace). Meldet das erreichte Residuum; Abbruch nur, wenn es > 1e-6 bleibt."""
    if not np.any(b):
        return np.zeros_like(b), 0, 0.0
    it = [0]
    x, flag = cg(Lap, b, rtol=rtol, atol=0.0, M=ml.aspreconditioner(), maxiter=5000,
                 callback=lambda _x: it.__setitem__(0, it[0] + 1))
    x -= x.mean()
    res = float(np.linalg.norm(Lap @ x - b) / np.linalg.norm(b))
    if res > 1e-6:
        raise RuntimeError(f"CG nicht konvergiert (flag {flag}, Residuum {res:.1e})")
    return x, it[0], res


def rechne(L, P):
    t0 = time.perf_counter()
    ax, ay, o = bindungen(L)
    nb = ax.size
    anker = np.stack([ax, ay], 1)
    kompat = tp.kompatibel(L, anker[:, None, :], o[:, None], anker[None, :, :], o[None, :])
    np.fill_diagonal(kompat, False)
    tab = tp.schritt_tabelle()
    ziel = np.array([[((ax[b] + s[0]) % L * L + (ay[b] + s[1]) % L) * 2 + s[2] for s in tab[o[b]]]
                     for b in range(nb)])
    qx2 = np.array([[s[3] for s in tab[o[b]]] for b in range(nb)])

    T = konfigurationen(L, P, kompat)
    N = T.shape[0]
    keys = schluessel(T, nb)                         # schon aufsteigend (lexikographisch erzeugt)
    assert np.all(np.diff(keys) > 0)
    t_konf = time.perf_counter() - t0

    # Übergänge: Paar in Slot p macht Eckschritt k
    src, dst, q = [], [], []
    for p in range(P):
        andere = [i for i in range(P) if i != p]
        for k in range(4):
            neu = ziel[T[:, p], k]
            ok = np.ones(N, bool)
            for i in andere:
                ok &= kompat[neu, T[:, i]]
            idx = np.nonzero(ok)[0]
            Tn = T[idx].copy()
            Tn[:, p] = neu[idx]
            Tn.sort(axis=1)
            t = np.searchsorted(keys, schluessel(Tn, nb))
            assert np.all(keys[t] == schluessel(Tn, nb))
            src.append(idx)
            dst.append(t)
            q.append(qx2[T[idx, p], k])
    src, dst, q = (np.concatenate(x) for x in (src, dst, q))
    M = src.size
    A = sp.coo_matrix((np.ones(M), (src, dst)), shape=(N, N)).tocsr()
    asym = abs(A - A.T)
    assert asym.nnz == 0 or asym.max() == 0
    grad = np.bincount(src, minlength=N).astype(float)
    d2x = np.bincount(src, weights=q, minlength=N)            # 2 d
    d = d2x / 2
    ncomp, lab = connected_components(A, directed=False)
    groessen = np.bincount(lab)
    c = int(np.argmax(groessen))
    haupt = np.nonzero(lab == c)[0]
    komp_summen = np.bincount(lab, weights=d2x, minlength=ncomp)
    t_graph = time.perf_counter() - t0 - t_konf

    # Zwei-Paar-Anteil der Drift
    g2 = tp.Relativgraph(L)
    d2pair = np.zeros((nb, nb))
    for i in range(nb):
        r = np.stack([(ax - ax[i]) % L, (ay - ay[i]) % L], 1)
        code = tp.kodiere(L, o[i], r[:, 0], r[:, 1], o)
        j = g2.idx[code]
        ok = j >= 0
        d2pair[i, ok] = g2.d2[j[ok]]
    dzwei = np.zeros(N)
    for i in range(P):
        for j in range(i + 1, P):
            dzwei += d2pair[T[:, i], T[:, j]]
    rest = d - dzwei

    # Poisson auf der Hauptkomponente
    pos = -np.ones(N, np.int64)
    pos[haupt] = np.arange(haupt.size)
    m = (lab[src] == c)
    s_h, t_h, q_h = pos[src[m]], pos[dst[m]], q[m] / 2
    n = haupt.size
    Ah = sp.coo_matrix((np.ones(s_h.size), (s_h, t_h)), shape=(n, n)).tocsr()
    Lap = (sp.diags(np.asarray(Ah.sum(axis=1)).ravel()) - Ah).tocsr()
    t1 = time.perf_counter()
    dh, d2h, rh = d[haupt], dzwei[haupt], rest[haupt]
    ml = pyamg.smoothed_aggregation_solver(Lap, symmetry="symmetric")
    h, it, res = loese(Lap, dh, ml)
    t_poisson = time.perf_counter() - t1
    E = float(dh @ h)
    E_dir = float(0.5 * np.sum((h[s_h] - h[t_h]) ** 2))
    deg4 = float(grad[haupt].mean() / 4)
    rho = deg4 - 2 * E / n

    # Quellen getrennt
    h2q, _, _ = loese(Lap, d2h - d2h.mean(), ml)
    hR, _, _ = loese(Lap, rh - rh.mean(), ml)
    E_zwei = float((d2h - d2h.mean()) @ h2q)
    E_rest = float((rh - rh.mean()) @ hR)
    E_kreuz = float((d2h - d2h.mean()) @ hR)

    # Paarsummen-Korrektor f2 = d2 / 7 im Leitwertfunktional Q(f) = (1/|C|) sum_{D->D'} (dx + f(D') - f(D))^2
    f2 = d2h / 7.0
    grad_f = f2[t_h] - f2[s_h]
    K = float(np.sum(q_h ** 2) / n)
    B = float(np.sum(q_h * grad_f) / n)
    C2 = float(np.sum(grad_f ** 2) / n)
    Q1 = K + 2 * B + C2
    lam = -B / C2 if C2 > 0 else 0.0
    Qopt = K - B * B / C2 if C2 > 0 else K
    abzug = K - rho
    # Winkel zwischen f2 und dem exakten Korrektor h in der Dirichlet-Metrik
    gh = h[t_h] - h[s_h]
    cosw = float(np.sum(gh * grad_f) / np.sqrt(np.sum(gh ** 2) * np.sum(grad_f ** 2))) if C2 > 0 else float("nan")

    lit = LIT.get((L, P))
    erg = dict(
        L=L, P=P, rho_b=P / (2 * L * L), konfigurationen=int(N), uebergaenge=int(M), komponenten=int(ncomp),
        hauptkomponente=int(n), eingefrorene=int(np.sum(groessen == 1)),
        max_komponentensumme=float(np.abs(komp_summen).max() / 2),
        zustaende_drift_ne0=int(np.sum(d != 0)), anteil_drift_ne0=float(np.mean(dh != 0)),
        anteil_rest_ne0=float(np.mean(rh != 0)),
        E=E, E_dirichlet=E_dir, cg_iter=it, residuum=res, rho_s_L2=rho, grad_viertel=deg4,
        rho_lit=lit[0] if lit else None, grad_viertel_lit=lit[1] if lit else None,
        paramagnetisch=abzug, s=rho / deg4,
        E_quelle_zwei=E_zwei, E_quelle_rest=E_rest, E_kreuz=E_kreuz,
        Q_f2_lambda1=Q1, lambda_opt=lam, Q_f2_opt=Qopt,
        anteil_geschlossen_lambda1=(K - Q1) / abzug if abzug else float("nan"),
        anteil_geschlossen_opt=(K - Qopt) / abzug if abzug else float("nan"),
        cos_f2_h=cosw,
        t_konfigurationen_s=t_konf, t_graph_s=t_graph, t_poisson_s=t_poisson,
        t_gesamt_s=time.perf_counter() - t0,
    )
    return erg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", type=int, default=8)
    ap.add_argument("--P", type=int, nargs="+", default=[2, 3, 4])
    a = ap.parse_args()
    alle = []
    for P in a.P:
        e = rechne(a.L, P)
        alle.append(e)
        print(f"\nL={e['L']} P={e['P']} (rho_b = {e['rho_b']:.5f}): {e['konfigurationen']} Konfigurationen, "
              f"{e['uebergaenge']} Übergänge, {e['komponenten']} Komponenten (Haupt {e['hauptkomponente']}, "
              f"eingefroren {e['eingefrorene']}), max |Sigma_C d| = {e['max_komponentensumme']}")
        print(f"  E = {e['E']:.8f} (Dirichlet {e['E_dirichlet']:.8f}), CG+AMG {e['cg_iter']} It., Residuum {e['residuum']:.1e}")
        print(f"  rho_s L^2 = {e['rho_s_L2']:.5f} (Lit. {e['rho_lit']}), <deg>/4 = {e['grad_viertel']:.5f} "
              f"(Lit. {e['grad_viertel_lit']}), s = {e['s']:.5f}, Abzug = {e['paramagnetisch']:.5f}")
        print(f"  Drift != 0 in {100 * e['anteil_drift_ne0']:.1f} %, Rest (Mehrkörper) != 0 in {100 * e['anteil_rest_ne0']:.2f} %")
        print(f"  Quellenenergien: d2 {e['E_quelle_zwei']:.5f}, Rest {e['E_quelle_rest']:.5f}, Kreuz {e['E_kreuz']:.5f} "
              f"(Summe {e['E_quelle_zwei'] + e['E_quelle_rest'] + 2 * e['E_kreuz']:.5f})")
        print(f"  Paarsummen-Korrektor f2 = sum h_2: schließt {100 * e['anteil_geschlossen_lambda1']:.1f} % des Abzugs (lambda = 1), "
              f"{100 * e['anteil_geschlossen_opt']:.1f} % bei lambda* = {e['lambda_opt']:.4f}; cos(f2, h) = {e['cos_f2_h']:.4f}")
        print(f"  Zeit: Konfigurationen {e['t_konfigurationen_s']:.1f} s, Graph {e['t_graph_s']:.1f} s, "
              f"Poisson {e['t_poisson_s']:.1f} s, gesamt {e['t_gesamt_s']:.1f} s")
    pfad = os.path.join(HIER, "ergebnisse", f"siebenachtel_{a.L}x{a.L}.json")
    with open(pfad, "w") as fh:
        json.dump(alle, fh, indent=1)
    print(f"\n-> {pfad}")


if __name__ == "__main__":
    main()
