#!/usr/bin/env python3
"""Anhang F (Dichteschranke unterhalb der Zellskala): exakte Prüfung der Bausteine auf kleinen Tori.

Harte Bosonen auf dem L×L-Torus, H = −A, ε_k = E_k + 4k, ψ der Grundzustand.
(1) Neumann-Zerlegung mit gemischten Kästen (fein in F, grob sonst):
      kleinster Eigenwert von  ℒ_N − Σ_Q λ_min(b_Q) n_Q 1{n_Q ≥ 2}  ist ≥ 0      (ℒ_N = 4N − A).
(2) Lemma F2 (Kippen auf der Skala R), g = exp(λ n_χ), χ = Rampe der Breite R um V:
      E(Φ_g) − E_N  ≤  2 e^{2λ/R} λ² R^{−2} E_g[n_{V''}],     V'' = {d_∞(x, V) ≤ R}.
(3) Lemma F1 bei festem h (vor dem Mitteln über h), für beliebige Zustände Φ:
      E(Φ) − E_N  ≥  c_{b1} (E n_F − #fein) + c_b (E n^in_{Ω\\F} − #grob) − μ̄ E[j] − F_h,
    mit p_h = cos θ_h, θ_h(x) = (π/2) clip((d_∞(x,F) − 1 − h s)/s, 0, 1), E[j] = E Σ_x p_h(x)² n_x,
    F_h = Σ_{geordnete Sprünge} Φ Φ′ (1 − cos(θ_x − θ_y)), c_b = λ_min(b) exakt, μ̄ = max_k (ε_k − ε_{k−1}) exakt.
    Dazu die scharfe Zwischenstufe ohne das Abzählen der Kästen (sie hat wenig Spielraum und prüft Vorzeichen und Faktoren):
      E(Φ) − E_N  ≥  E[ Σ_Q λ_min(b_Q) n^in_Q 1{n^in_Q ≥ 2} ] − μ̄ E[j] − F_h,
    wobei n^in_Q die Innen-Teilchen im Kasten Q zählt (jedes Teilchen bei x ist unabhängig mit Wahrscheinlichkeit p_h(x)² innen).
(4) Zahlen zu Satz F3: C_E, θ_F(ε), λ₀ und der Exponent der Ausnahmewahrscheinlichkeit.
(5) Lemma F6 (Potentialenergie im gestörten Grundzustand Ψ von H − vΣW, W = w·χ) bei festem h, scharfe Form:
      E_Ψ[ Σ_Q λ_min(b_Q) n^in_Q 1{n^in_Q ≥ 2} ]  ≤  v E_Ψ[n_W] + μ̄^{vW} E_Ψ[j] + F_h,     μ̄^{vW} = max_k (ε^{vW}_k − ε^{vW}_{k−1}),
    und Lemma 6.8 für ein Zeitfenster:  E_ψ exp(∫_0^Δ w n_χ(t) dt)  ≤  exp(Δ (E_0(H) − E_0(H − w n_χ))).
(6) Lemma P5 in der Form mit der gemeinsamen Aufenthaltszeit (ohne (G3)): Irrfahrt X (Rate 1 je Nachbar) ab x, feste
    Linien Y_j (stückweise konstant):   P(X trifft eine Linie in [0, τ])  ≤  𝔏 / min_j inf_{σ ≤ τ} g_j(σ),
      𝔏 = ∫_0^{2τ} Σ_j p_t(x, Y_j(t)) dt,     g_j(σ) = ∫_0^τ p_u(Y_j(σ), Y_j(σ+u)) du.
(7) Lemma F8 (deterministisch), Bausteine: Zeitfenster I_i = [2^i − 1, 2^{i+1} − 1), Radien ρ_{k,i} = 2^k 2^{(i+1)/2}.
    (a) Schalengewichte: p_u(x, y) ≤ 2^{−i} a_{k,i} für u ∈ I_i, |x − y|_∞ > ρ_{k−1,i}, mit dem exakten Kern (Bessel),
        a_{k,i} = exp(−min(4^k/32, 2^k 2^{(i+1)/2}/16));  dazu S_2 = Σ â_k 4^k und S_3 = Σ â_k 8^k.
    (b) Überdeckung: Kugel B(x, ρ_{k,i}) in einem Gitterquadrat der Seite R (R minimal in ℛ mit R ≥ 8ρ), Fenster
        t₀ + I_i in einem Gitterfenster der zugelassenen Länge Δ; Zahl der Quadrate der Seite R₀ für B(x, ρ + r/2).
    (c) Schalenformel auf zufälligen Linien:  𝔏(x) ≤ Σ_i 2^{−i} Σ_k a_{k,i} ∫_{I_i} n(B(x, ρ_{k,i}); u) du,  und unter (G4)
        die Kurzzeit-Schranke  n(B(x, ρ); u) ≤ t_r^{−1} ∫_0^{t_r} n(B(x, ρ + r/2); t) dt  für u ≤ t_r.
(8) Bausteine zu F.11 (Seltenheit) und F.12 (Lemma P6 mit (G1″), (G2_A), (G4)):
    (a) Lemma F11a: P(sup_{u≤t} |Y_u − Y_0|_∞ ≥ a) ≤ 4 exp(−a²/(4,4 t)) für a ≤ 2,2 t, exakt über die Irrfahrt mit
        Absorption bei ±a; dazu die Form mit r = 16a, t_r = r²/(16β): ≤ 4 e^{−β/70,4}.
    (b) (G4′) ⇒ (G4): Schwankung ≤ r/8 in jedem Gitterfenster der Länge t_r gibt Verschiebung ≤ r/4 über jede Zeit ≤ t_r;
        Überdeckung eines Intervalls der Länge ℓ ≤ Δ/2 durch ein Fenster der zwei Zeitgitter (von t_a aufwärts, von t_b abwärts).
    (c) Brücke von S nach S + d in der Zeit δ, exakter Kern: (W2) Zuwachs über die Dauer Δ,
          p_{δ−Δ}(d − z)/p_δ(d) ≤ 4π (1+δ)/(1+δ−Δ) exp(|d|²(|d|_∞+|z|_∞)/(4δ²) + |d||z|/(2δ)),
        (W3) Randverteilung zur Zeit a (b = δ − a, m = (a/δ) d): obere und untere Gauß-Schranke.
    (d) Schlauch-Schritt in P6b″: P(|Q_{i+1} − m_{i+1}| ≤ ½√τ′ | Q_i) ≥ c₂ = 0,001 und Randdichte ≤ 12π/τ′.
(9) Zahlen zu F.11 und F.12 (C_b, C₆, λ₁, j₁, J, c_q).
Aufruf: python3 pruef_feinskala.py [--gross]      (--gross: zusätzlich 12×12 mit N = 3, etwa eine Minute)
"""
import argparse
import itertools

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh


class Torus:
    def __init__(self, L):
        self.L, self.M = L, L * L
        self.x, self.y = np.divmod(np.arange(self.M), L)
        self.nb = np.stack([((self.x + dx) % L) * L + (self.y + dy) % L
                            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))], 1)

    def platz(self, x, y):
        return (x % self.L) * self.L + (y % self.L)

    def abstand(self, menge):
        """ℓ∞-Torusabstand jedes Platzes zur Platzmenge."""
        L = self.L
        dx = np.abs(self.x[:, None] - self.x[menge][None, :]); dx = np.minimum(dx, L - dx)
        dy = np.abs(self.y[:, None] - self.y[menge][None, :]); dy = np.minimum(dy, L - dy)
        return np.maximum(dx, dy).min(1)


class System:
    """N harte Bosonen auf dem Torus: Basis, Sprungmatrix mit Sprungplätzen, Grundzustand."""

    def __init__(self, T, N):
        self.T, self.N = T, N
        M = T.M
        self.conf = np.array(list(itertools.combinations(range(M), N)), dtype=np.int64)
        gew = M ** np.arange(N - 1, -1, -1, dtype=np.int64)
        schl = self.conf @ gew                       # lexikographisch sortiert
        rows, cols, xs, ys = [], [], [], []
        for p in range(N):
            for d in range(4):
                q = T.nb[self.conf[:, p], d]
                frei = ~(self.conf == q[:, None]).any(1)
                r = np.nonzero(frei)[0]
                neu = self.conf[r].copy()
                neu[:, p] = q[r]
                neu.sort(1)
                rows.append(r); cols.append(np.searchsorted(schl, neu @ gew))
                xs.append(self.conf[r, p]); ys.append(q[r])
        self.rows, self.cols = np.concatenate(rows), np.concatenate(cols)
        self.xs, self.ys = np.concatenate(xs), np.concatenate(ys)
        D = len(self.conf)
        self.A = sp.coo_matrix((np.ones(len(self.rows)), (self.rows, self.cols)), shape=(D, D)).tocsr()
        if D == 1:
            self.E, self.psi = 0.0, np.ones(1)
        else:
            w, v = eigsh(self.A, k=1, which='LA', tol=1e-13)
            self.E = -float(w[0])
            self.psi = np.abs(v[:, 0]) / np.linalg.norm(v[:, 0])

    def grund_mit_potential(self, pot):
        """Grundzustand von H − Σ_i pot(x_i): (Energie, Vektor ≥ 0)."""
        d = pot[self.conf].sum(1)
        if len(self.conf) == 1:
            return -float(d[0]), np.ones(1)
        w, v = eigsh(self.A + sp.diags(d), k=1, which='LA', tol=1e-13)
        return -float(w[0]), np.abs(v[:, 0]) / np.linalg.norm(v[:, 0])

    def energie(self, phi):
        return -float(phi @ (self.A @ phi))

    def dichte(self, phi):
        return np.bincount(self.conf.ravel(), weights=np.repeat(phi * phi, self.N), minlength=self.T.M)

    def gewichtet(self, chi):
        return chi[self.conf].sum(1)


def lam_min(b):
    """min_y des kleinsten Eigenwerts des Neumann-Laplace-Operators im b×b-Kasten mit Dirichlet-Punkt y."""
    n = b * b
    Lq = np.zeros((n, n))
    for x in range(b):
        for y in range(b):
            i = x * b + y
            for (u, v) in ((x + 1, y), (x, y + 1)):
                if u < b and v < b:
                    j = u * b + v
                    Lq[i, i] += 1; Lq[j, j] += 1; Lq[i, j] -= 1; Lq[j, i] -= 1
    best = np.inf
    for k in range(n):
        keep = [i for i in range(n) if i != k]
        if keep:
            best = min(best, np.linalg.eigvalsh(Lq[np.ix_(keep, keep)])[0])
    return float(best) if np.isfinite(best) else np.inf


def grob_label(T, b):
    return (T.x // b) * (T.L // b) + (T.y // b)


def pruefe_zerlegung(S, b, b1, feine_grobkaesten):
    """(1): gemischte Zerlegung; die groben Kästen in feine_grobkaesten sind fein (b1) unterteilt."""
    T, N = S.T, S.N
    lab_g = grob_label(T, b)
    lab_f = (T.x // b1) * (T.L // b1) + (T.y // b1)
    fein = np.isin(lab_g, feine_grobkaesten)
    lab = np.where(fein, lab_f + 10 ** 6, lab_g)
    lam = np.where(fein, lam_min(b1), lam_min(b))
    lc = lab[S.conf]
    gleich = (lc[:, :, None] == lc[:, None, :]).sum(2)
    Dd = (lam[S.conf] * (gleich >= 2)).sum(1)
    Op = 4 * N * sp.identity(len(S.conf)) - S.A - sp.diags(Dd)
    w = eigsh(Op.tocsr(), k=1, which='SA', tol=1e-10)[0][0]
    return float(w)


def geometrie(T, V, R, b, b1, s, h):
    dV = T.abstand(V)
    chi = np.clip(1.0 - dV / R, 0.0, 1.0)
    V2 = dV <= R
    lab_g = grob_label(T, b)
    F = np.isin(lab_g, np.unique(lab_g[V2]))
    dF = T.abstand(np.nonzero(F)[0])
    theta = 0.5 * np.pi * np.clip((dF - 1.0 - h * s) / s, 0.0, 1.0)
    innen = theta < 0.5 * np.pi - 1e-14
    grob_om = np.unique(lab_g[innen | F])
    n_grob = len(np.setdiff1d(grob_om, np.unique(lab_g[F])))
    n_fein = int(F.sum()) // (b1 * b1)
    lab = np.where(F, (T.x // b1) * (T.L // b1) + (T.y // b1) + 10 ** 6, lab_g)
    lam = np.where(F, lam_min(b1), lam_min(b))
    return dict(chi=chi, V2=V2, F=F, theta=theta, n_grob=n_grob, n_fein=n_fein, lab=lab, lam=lam)


def ballung_innen(S, lab, lam, p2):
    """Je Konfiguration: E über die Färbung von Σ_Q λ_Q n^in_Q 1{n^in_Q ≥ 2}."""
    P, Lb, Lm = p2[S.conf], lab[S.conf], lam[S.conf]
    D = np.zeros(len(S.conf))
    for i in range(S.N):
        allein = np.ones(len(S.conf))
        for j in range(S.N):
            if j != i:
                allein *= np.where(Lb[:, j] == Lb[:, i], 1.0 - P[:, j], 1.0)
        D += Lm[:, i] * P[:, i] * (1.0 - allein)
    return D


def pruefe_F1_F2(S, eps, V, R, b, b1, s, hs, lams, rng, name):
    T = S.T
    mu = max(eps[k] - eps[k - 1] for k in range(1, S.N + 1))
    cb, cb1 = lam_min(b), lam_min(b1)
    schlimm_F1, schlimm_F2, schlimm_sch, zeilen = np.inf, np.inf, np.inf, []
    for h in hs:
        geo = geometrie(T, V, R, b, b1, s, h)
        p2 = np.cos(geo['theta']) ** 2
        dth = geo['theta'][S.xs] - geo['theta'][S.ys]
        Dsch = ballung_innen(S, geo['lab'], geo['lam'], p2)
        zust = [(f"λ={l:g}", np.exp(l * S.gewichtet(geo['chi'])) * S.psi) for l in lams]
        zust += [(f"zufall{i}", S.psi * rng.uniform(0.2, 1.8, len(S.psi))) for i in range(2)]
        for (zn, phi) in zust:
            phi = phi / np.linalg.norm(phi)
            dE = S.energie(phi) - S.E
            dens = S.dichte(phi)
            nF = dens[geo['F']].sum()
            Ej = (p2 * dens).sum()
            Fh = float(np.sum(phi[S.rows] * phi[S.cols] * (1.0 - np.cos(dth))))
            rhs = cb1 * (nF - geo['n_fein']) + cb * ((p2 * dens)[~geo['F']].sum() - geo['n_grob']) - mu * Ej - Fh
            schlimm_F1 = min(schlimm_F1, dE - rhs)
            scharf = float(phi * phi @ Dsch) - mu * Ej - Fh
            schlimm_sch = min(schlimm_sch, dE - scharf)
            assert scharf >= rhs - 1e-10, "scharfe Form muss die abgezählte Form implizieren"
            if zn.startswith("λ=") and h == hs[0]:
                l = float(zn[2:])
                ob = 2.0 * np.exp(2 * l / R) * l * l / (R * R) * dens[geo['V2']].sum()
                schlimm_F2 = min(schlimm_F2, ob - dE)
                zeilen.append(f"      {zn:7s} E−E_N = {dE:9.6f} ≤ F2-Schranke {ob:9.6f};  E_g n_F = {nF:6.4f}")
    print(f"  {name}: b={b}, b1={b1}, R={R}, s={s}, |F|={int(geo['F'].sum())}, #fein={geo['n_fein']}, "
          f"c_b={cb:.4f}, c_b1={cb1:.4f}, μ̄={mu:.4f}")
    for z in zeilen:
        print(z)
    print(f"      F1: min (links − rechts) über h ∈ {hs} und alle Zustände = {schlimm_F1:+.3e}   "
          f"{'ok' if schlimm_F1 >= -1e-9 else 'VERLETZT'};   scharfe Form: {schlimm_sch:+.3e}   "
          f"{'ok' if schlimm_sch >= -1e-9 else 'VERLETZT'};   F2: min Spielraum = {schlimm_F2:+.3e}   "
          f"{'ok' if schlimm_F2 >= -1e-9 else 'VERLETZT'}")
    return schlimm_F1 >= -1e-9 and schlimm_F2 >= -1e-9 and schlimm_sch >= -1e-9


def pruefe_F6(T, N, V, R, b, b1, s, hs, ws, name):
    """(5): scharfe Form von Lemma F6 im gestörten Grundzustand, dazu Lemma 6.8 für ein Zeitfenster."""
    from scipy.sparse.linalg import expm_multiply
    Ss = [System(T, k) for k in range(1, N + 1)]
    S = Ss[-1]
    geo0 = geometrie(T, V, R, b, b1, s, 0.0)
    chi = geo0['chi']
    schlimm, schlimm68, zeilen = np.inf, np.inf, []
    for w in ws:
        pot = w * chi
        eW = {0: 0.0}
        for k in range(1, N + 1):
            eW[k] = Ss[k - 1].grund_mit_potential(pot)[0] + 4 * k
        muW = max(eW[k] - eW[k - 1] for k in range(1, N + 1))
        EW, psiW = S.grund_mit_potential(pot)
        dens = S.dichte(psiW)
        nW = float((pot * dens).sum())
        for h in hs:
            geo = geometrie(T, V, R, b, b1, s, h)
            p2 = np.cos(geo['theta']) ** 2
            dth = geo['theta'][S.xs] - geo['theta'][S.ys]
            Dsch = ballung_innen(S, geo['lab'], geo['lam'], p2)
            links = float(psiW * psiW @ Dsch)
            rechts = nW + muW * float((p2 * dens).sum()) + float(np.sum(psiW[S.rows] * psiW[S.cols] * (1 - np.cos(dth))))
            schlimm = min(schlimm, rechts - links)
        # Lemma 6.8 für ein Fenster der Länge Δ
        for Delta in (0.5, 2.0):
            d = pot[S.conf].sum(1)
            v = expm_multiply(Delta * (S.A + sp.diags(d) + S.E * sp.identity(len(S.conf))), S.psi)
            mom = float(S.psi @ v)
            schr = np.exp(Delta * (S.E - EW))
            schlimm68 = min(schlimm68, schr / mom)
            zeilen.append(f"      w={w:g}, Δ={Delta:g}: E exp(∫w n_χ) = {mom:.6f} ≤ {schr:.6f}")
        zeilen.append(f"      w={w:g}: E_Ψ[n_W]/w = {nW / w:.4f} (ungestört {float((chi * S.dichte(S.psi)).sum()):.4f}), μ̄^W = {muW:.4f}")
    print(f"  {name}: b={b}, b1={b1}, R={R}, s={s}")
    for z in zeilen:
        print(z)
    ok = schlimm >= -1e-9 and schlimm68 >= 1 - 1e-9
    print(f"      F6 (scharf): min (rechts − links) = {schlimm:+.3e}   {'ok' if schlimm >= -1e-9 else 'VERLETZT'};   "
          f"Lemma 6.8: min Schranke/Moment = {schlimm68:.4f}   {'ok' if schlimm68 >= 1 - 1e-9 else 'VERLETZT'}")
    return ok


def pruefe_P5(rng):
    """(6): Treffwahrscheinlichkeit gegen gemeinsame Aufenthaltszeit, exakt auf dem 12×12-Torus."""
    from scipy.linalg import expm
    T = Torus(12)
    M = T.M
    Q = np.zeros((M, M))
    for i in range(M):
        for j in T.nb[i]:
            Q[i, j] += 1.0
        Q[i, i] = -4.0
    dt, nsub = 0.25, 5
    Psub = expm(dt / (nsub - 1) * Q)
    alles = True
    print("  (6) Lemma P5 mit gemeinsamer Aufenthaltszeit (12×12-Torus, Linien stückweise konstant auf Schritten 0,25):")
    for (tau, m, art) in ((2.0, 1, 'diffusiv'), (4.0, 1, 'diffusiv'), (2.0, 2, 'diffusiv'), (4.0, 3, 'diffusiv'),
                          (2.0, 1, 'heranlaufend'), (4.0, 2, 'heranlaufend')):
        K = int(round(2 * tau / dt))
        x = T.platz(6, 6)
        # Linienbahnen: Start im Abstand 4 bis 5, je Schritt mit Wahrscheinlichkeit 0,5 ein Sprung
        Y = np.zeros((m, K + 1), dtype=int)
        for j in range(m):
            while True:
                y = T.platz(6 + rng.integers(-5, 6), 6 + rng.integers(-5, 6))
                if 4 <= T.abstand([x])[y] <= 5 and y not in Y[:j, 0]:
                    break
            for k in range(K + 1):
                Y[j, k] = y
                if art == 'heranlaufend' and k < 6:
                    dx = np.sign(((T.x[x] - T.x[y] + 6) % 12) - 6); dy = np.sign(((T.y[x] - T.y[y] + 6) % 12) - 6)
                    z = T.platz(T.x[y] + dx, T.y[y]) if dx != 0 and rng.random() < 0.5 else T.platz(T.x[y], T.y[y] + dy)
                    if z != x and z != y:
                        y = z
                elif rng.random() < 0.5:
                    y = T.nb[y, rng.integers(4)]
        # Treffwahrscheinlichkeit bis τ: Walker lebt, solange er auf keinem besetzten Platz ist
        v = np.zeros(M); v[x] = 1.0
        for k in range(int(round(tau / dt))):
            bes = np.unique(Y[:, k])
            v[bes] = 0.0
            frei = np.setdiff1d(np.arange(M), bes)
            v2 = np.zeros(M)
            v2[frei] = v[frei] @ expm(dt * Q[np.ix_(frei, frei)])
            v = v2
        v[np.unique(Y[:, int(round(tau / dt))])] = 0.0
        p_treff = 1.0 - v.sum()
        # 𝔏 und g_j über Simpson je Schritt
        gew = np.array([1, 4, 2, 4, 1]) * (dt / (nsub - 1)) / 3.0
        def kern_reihe(start, schritte):
            """p_t(start, ·) an den Stützstellen der ersten 'schritte' Schritte: Liste von (nsub × M)-Feldern."""
            z = np.zeros(M); z[start] = 1.0
            aus = []
            for _ in range(schritte):
                st = [z]
                for _ in range(nsub - 1):
                    st.append(st[-1] @ Psub)
                aus.append(np.array(st)); z = st[-1]
            return aus
        kr = kern_reihe(x, K)
        L_ges = sum(float(gew @ kr[k][:, Y[j, k]]) for k in range(K) for j in range(m))
        g_min = np.inf
        Kt = int(round(tau / dt))
        for j in range(m):
            for k0 in range(Kt + 1):          # σ an Schrittgrenzen (g ist dazwischen glatt; grobe Infimum-Suche)
                krj = kern_reihe(Y[j, k0], Kt)
                g_min = min(g_min, sum(float(gew @ krj[k][:, Y[j, min(k0 + k, K)]]) for k in range(Kt)))
        ok = p_treff <= L_ges / g_min * (1 + 1e-9)
        alles &= ok
        print(f"      τ={tau:g}, {m} Linie(n), {art:12s}: P(Treffer) = {p_treff:.4f} ≤ 𝔏/min g = {L_ges:.4f}/{g_min:.4f} = "
              f"{L_ges / g_min:.4f}   {'ok' if ok else 'VERLETZT'}")
    return alles


def a_gewicht(k, i):
    return 1.0 if k == 0 else float(np.exp(-min(4.0 ** k / 32.0, 2.0 ** k * 2.0 ** ((i + 1) / 2.0) / 16.0)))


def pruefe_F8(rng):
    """(7): Bausteine des deterministischen Lemmas F8."""
    from scipy.special import ive
    ok_alles = True
    print("  (7) Lemma F8, Bausteine")
    # (a) Schalengewichte gegen den exakten Kern q_u(k) = e^{-2u} I_k(2u)
    schlimm = 0.0
    for i in range(0, 18):
        for f in (0.0, 0.25, 0.5, 0.75, 0.999):
            u = 2.0 ** i - 1 + f * 2.0 ** i
            q0 = float(ive(0, 2 * u)) if u > 0 else 1.0
            schlimm = max(schlimm, q0 * q0 * (1 + u))                 # Schale 0: p_u ≤ 1/(1+u) ≤ 2^{-i}
            for k in range(1, 14):
                d = int(np.floor(2.0 ** (k - 1) * 2.0 ** ((i + 1) / 2.0))) + 1
                pk = (float(ive(d, 2 * u)) if u > 0 else 0.0) * q0
                schr = 2.0 ** (-i) * a_gewicht(k, i)
                schlimm = max(schlimm, pk / schr if schr > 1e-290 else (0.0 if pk < 1e-290 else np.inf))
    S2 = 1.0 + sum(np.exp(-min(4.0 ** k / 32, 2.0 ** k * np.sqrt(2) / 16)) * 4.0 ** k for k in range(1, 40))
    S3 = 1.0 + sum(np.exp(-min(4.0 ** k / 32, 2.0 ** k * np.sqrt(2) / 16)) * 8.0 ** k for k in range(1, 40))
    ok = schlimm <= 1 + 1e-12 and S2 <= 185 and S3 <= 4200
    ok_alles &= ok
    print(f"      (a) max p_u/(2^-i a_ki) = {schlimm:.4f} ≤ 1;  S_2 = {S2:.1f} ≤ 185,  S_3 = {S3:.1f} ≤ 4200   {'ok' if ok else 'VERLETZT'}")
    # (b) Überdeckung
    r, beta, R0, J = 16, 1.0, 128, 4
    t_r = r * r / (16 * beta)
    Rs = [R0 * 2 ** j for j in range(J + 1)]
    fehler, faelle = 0, 0
    for _ in range(400):
        x = int(rng.integers(-10 ** 6, 10 ** 6)); t0 = float(rng.uniform(-10 ** 4, 10 ** 4))
        for i in range(0, 12):
            for k in range(0, 12):
                rho = 2.0 ** k * 2.0 ** ((i + 1) / 2.0)
                if 2.0 ** (i + 1) > t_r and 8 * rho <= Rs[-1]:
                    faelle += 1
                    R = min(Rr for Rr in Rs if Rr >= 8 * rho)
                    if R > R0:
                        q = int(np.floor(np.log2(R * R / 16.0)))
                        Delta = 2.0 ** q
                        gut = (R * R / 32.0 < Delta <= R * R / 16.0) and R < 16 * rho and Delta <= 16 * rho * rho
                    else:
                        Delta = 2.0 ** (i + 1)
                        gut = t_r <= Delta <= R0 * R0 / 16.0
                    lo, hi = x - int(np.floor(rho)), x + int(np.floor(rho))
                    a = (R // 2) * (lo // (R // 2))
                    gut &= hi <= a + R - 1                                   # Kugel im Gitterquadrat
                    ta, tb = t0 + 2.0 ** i - 1, t0 + 2.0 ** (i + 1) - 1
                    at = (Delta / 2) * np.floor(ta / (Delta / 2))
                    gut &= tb <= at + Delta + 1e-9                           # Fenster im Gitterfenster
                    fehler += (not gut)
                if 2.0 ** (i + 1) <= t_r and rho >= 0.75 * r:
                    faelle += 1
                    lo, hi = x - int(np.floor(rho + r / 2)), x + int(np.floor(rho + r / 2))
                    zahl = hi // R0 - lo // R0 + 1
                    fehler += not (zahl <= (2 * rho + r + 1) / R0 + 2)
    ok = fehler == 0
    ok_alles &= ok
    print(f"      (b) Überdeckung: {faelle} Fälle, {fehler} Fehler   {'ok' if ok else 'VERLETZT'}")
    # (c) Schalenformel und Kurzzeit-Schranke auf zufälligen Linien
    dt = 0.25
    for (name, r, beta, m, W, T, psprung) in (("schnell", 4, 1.0, 400, 60, 63, 0.5), ("(G4)", 16, 1.0, 600, 120, 63, 0.01)):
        t_r = r * r / (16 * beta)
        K = int(round((T + 1) / dt))
        pos = rng.integers(-W, W + 1, size=(m, 2))
        pos = pos[np.abs(pos).max(1) >= r]
        mm = len(pos)
        bahn = np.zeros((mm, K + 1, 2), dtype=int)
        bahn[:, 0] = pos
        richt = np.array([(1, 0), (-1, 0), (0, 1), (0, -1)])
        for kk in range(1, K + 1):
            spr = rng.random(mm) < psprung
            bahn[:, kk] = bahn[:, kk - 1] + richt[rng.integers(4, size=mm)] * spr[:, None]
        dinf = np.abs(bahn).max(2)                                   # Abstand zu x = 0, [Linie, Schritt]
        # exaktes 𝔏 (Simpson je Schritt, Linie steht während des Schritts)
        gew = np.array([1, 4, 2, 4, 1]) * (dt / 4) / 3.0
        L = 0.0
        for kk in range(K):
            us = kk * dt + np.arange(5) * dt / 4
            ax, ay = np.abs(bahn[:, kk, 0]), np.abs(bahn[:, kk, 1])
            nah = (ax < 60) & (ay < 60)
            if nah.any():
                for w_, u in zip(gew, us):
                    if u == 0:
                        continue
                    L += w_ * float(np.sum(ive(ax[nah], 2 * u) * ive(ay[nah], 2 * u)))
        # Schalenformel
        rechts = 0.0
        iT = int(np.floor(np.log2(1 + T)))
        for i in range(0, iT + 1):
            k0, k1 = int(round((2 ** i - 1) / dt)), min(int(round((2 ** (i + 1) - 1) / dt)), K)
            for k in range(0, 12):
                rho = 2.0 ** k * 2.0 ** ((i + 1) / 2.0)
                integ = float((dinf[:, k0:k1] <= rho).sum()) * dt
                rechts += 2.0 ** (-i) * a_gewicht(k, i) * integ
        ok = L <= rechts * (1 + 1e-9)
        zeile = f"      (c) {name:8s}: r={r}, {mm} Linien, 𝔏 = {L:.5f} ≤ Schalenformel {rechts:.5f}   {'ok' if ok else 'VERLETZT'}"
        if name == "(G4)":
            kr = int(round(t_r / dt))
            versch = np.abs(bahn[:, :kr + 1] - bahn[:, :1]).max(2).max(1)
            g4 = bool((versch <= r / 4).all())
            verl = 0
            for rho in (0.75 * r, r, 1.5 * r, 3 * r):
                mittel = float((dinf[:, :kr] <= rho + r / 2).sum()) * dt / t_r
                verl += int(((dinf[:, :kr + 1] <= rho).sum(0) > mittel + 1e-9).any())
            ok &= g4 and verl == 0
            zeile += f";  (G4) erfüllt: {g4}, Kurzzeit-Schranke verletzt: {verl}"
        ok_alles &= ok
        print(zeile)
    return ok_alles


def q1(t, k):
    """1D-Kern e^{-2t} I_|k|(2t)."""
    from scipy.special import ive
    return ive(np.abs(k), 2.0 * t)


def p2(t, x):
    return q1(t, x[..., 0]) * q1(t, x[..., 1])


def pruefe_F11_F12(rng):
    """(8): Bausteine zu F.11 (Seltenheit) und F.12 (Lemma P6 mit den neuen Bedingungen)."""
    from scipy.special import ive  # noqa: F401 (q1 benutzt ive)
    from scipy.linalg import expm
    ok_alles = True
    print("  (8) Seltenheit und Lemma P6 neu (F.11, F.12), Bausteine")
    # (a) Lemma F11a: P(sup_{u≤t} |Y_u − Y_0|_∞ ≥ a) ≤ 4 exp(−a²/(4,4 t)) für a ≤ 2,2 t
    schlimm, faelle = 0.0, 0
    for a in (2, 4, 8, 16, 32, 64):
        n = 2 * a - 1
        G = -2.0 * np.eye(n) + np.eye(n, k=1) + np.eye(n, k=-1)
        for x in (0.25, 0.5, 1, 2, 4, 8, 16, 32, 64):
            t = a * a / x
            if a > 2.2 * t:
                continue
            ueb = float(expm(t * G)[a - 1].sum())                 # 1D: bis t nicht bei ±a gewesen
            P = 1.0 - ueb * ueb
            schr = 4.0 * np.exp(-a * a / (4.4 * t))
            schlimm = max(schlimm, P / schr)
            faelle += 1
    ok = schlimm <= 1.0
    ok_alles &= ok
    print(f"      (a) Lemma F11a (Doob): {faelle} Fälle, max P/Schranke = {schlimm:.4f} ≤ 1   {'ok' if ok else 'VERLETZT'}")
    zeile = "          r = 16a, t_r = r²/(16β):  "
    for (a, beta) in ((16, 16.0), (64, 80.0), (160, 200.0), (320, 400.0)):
        n = 2 * a - 1
        G = -2.0 * np.eye(n) + np.eye(n, k=1) + np.eye(n, k=-1)
        t = 16.0 * a * a / beta
        ueb = float(expm(t * G)[a - 1].sum())
        P = 1.0 - ueb * ueb
        ok = P <= 4 * np.exp(-beta / 70.4)
        ok_alles &= ok
        zeile += f"β={beta:g}: {P:.3g} ≤ {4 * np.exp(-beta / 70.4):.3g};  "
    print(zeile)
    # (b) (G4′) ⇒ (G4) und die zwei Zeitgitter
    fehler, faelle = 0, 0
    for _ in range(300):
        r = 16 * int(rng.integers(1, 5)); t_r = float(rng.uniform(1, 5)); Ng = int(rng.integers(4, 30))
        K = Ng * 40                                                        # Schritte je Scheibe, 40 je Fenster
        y = np.cumsum(rng.integers(-1, 2, size=(K + 1, 2)) * (rng.random((K + 1, 1)) < 0.2), axis=0)
        osz = max(np.abs(y[m * 40:(m + 1) * 40 + 1] - y[m * 40:(m + 1) * 40 + 1][:, None]).max() for m in range(Ng))
        if osz > r / 8:
            continue
        faelle += 1
        versch = max(np.abs(y[i:i + 41] - y[i]).max() for i in range(0, K - 40))
        fehler += versch > r / 4
    for _ in range(20000):
        ta = float(rng.uniform(-100, 100)); Delta = float(rng.uniform(0.1, 10)); tb = ta + Delta * float(rng.uniform(2, 30))
        ell = float(rng.uniform(0, Delta / 2)); a = float(rng.uniform(ta, tb - ell))
        f = ta + (Delta / 2) * np.floor((a - ta) / (Delta / 2))
        e = tb - (Delta / 2) * np.floor((tb - a - ell) / (Delta / 2))
        vor = f <= a + 1e-12 and a + ell <= f + Delta + 1e-12 and f + Delta <= tb + 1e-12
        rueck = e - Delta <= a + 1e-12 and a + ell <= e + 1e-12 and e - Delta >= ta - 1e-12
        faelle += 1
        fehler += not (vor or rueck)
    ok = fehler == 0
    ok_alles &= ok
    print(f"      (b) (G4′) ⇒ (G4) auf Zufallsbahnen und Überdeckung durch die zwei Zeitgitter: {faelle} Fälle, {fehler} Fehler   "
          f"{'ok' if ok else 'VERLETZT'}")
    # (c) Brücken-Werkzeuge (W2), (W3) mit dem exakten Kern
    schl2, schl3o, schl3u, faelle = 0.0, 0.0, np.inf, 0
    for delta in (40.0, 300.0, 2500.0):
        for fr in (0.05, 0.2, 0.5):
            Dl = fr * delta
            for d in ((0, 0), (int(delta ** 0.5), 0), (int(2 * delta ** 0.5), int(delta ** 0.5)), (int(delta / 4), int(delta / 4)),
                      (int(delta / 2), 0)):
                d = np.array(d)
                pd = float(p2(delta, d))
                if pd < 1e-250:
                    continue
                m = int(4 * Dl ** 0.5) + 3
                zz = np.stack(np.meshgrid(np.arange(-m, m + 1), np.arange(-m, m + 1), indexing='ij'), -1).reshape(-1, 2)
                zz = np.concatenate([zz, zz * 3, zz * 7])
                # (W2)
                links = p2(delta - Dl, d - zz) / pd
                dn, di = np.hypot(*d), np.abs(d).max()
                zn, zi = np.hypot(zz[:, 0], zz[:, 1]), np.abs(zz).max(1)
                rechts = 4 * np.pi * (1 + delta) / (1 + delta - Dl) * np.exp(np.minimum(dn * dn * (di + zi) / (4 * delta ** 2)
                                                                                       + dn * zn / (2 * delta), 700.0))
                schl2 = max(schl2, float((links / rechts).max()))
                # (W3): a = Dl, b = delta − Dl
                a, b = Dl, delta - Dl
                P = p2(a, zz) * p2(b, d - zz) / pd
                mm = (a / delta) * d
                ab = np.hypot(zz[:, 0] - mm[0], zz[:, 1] - mm[1])
                yn, yi = zn, zi
                wn, wi = np.hypot(d[0] - zz[:, 0], d[1] - zz[:, 1]), np.abs(d - zz).max(1)
                vor = (1 + delta) / ((1 + a) * (1 + b))
                oben = 4 * np.pi * vor * np.exp(np.minimum(-(delta / (4 * a * b)) * ab ** 2 + yn ** 2 * yi / (4 * a * a)
                                                            + wn ** 2 * wi / (4 * b * b), 700.0))
                schl3o = max(schl3o, float((P / oben).max()))
                gilt = (yi <= a) & (wi <= b) & (P > 1e-280)
                if a >= 1 and b >= 1 and gilt.any():
                    unten = vor / (16 * np.pi ** 2) * np.exp(-(delta / (4 * a * b)) * ab ** 2 - dn * dn * di / (4 * delta ** 2))
                    schl3u = min(schl3u, float((P[gilt] / unten[gilt]).min()))
                faelle += 1
    ok = schl2 <= 1 and schl3o <= 1 and schl3u >= 1
    ok_alles &= ok
    print(f"      (c) Brücke, {faelle} Fälle: (W2) max links/rechts = {schl2:.4f} ≤ 1;  (W3) oben {schl3o:.4f} ≤ 1, "
          f"unten min = {schl3u:.3f} ≥ 1   {'ok' if ok else 'VERLETZT'}")
    # (d) Schlauch-Schritt in P6b″ und Randdichte der Brücke
    c2min, dmax = np.inf, 0.0
    for tp in (64.0, 256.0, 1024.0):
        rad = 0.5 * tp ** 0.5
        for fD in (0.5, 1.0, 1.5):
            Dl = fD * tp
            for fr in (0.5, 1.0, 5.0, 50.0):
                rem = Dl + fr * tp
                for kap in (0.0, 0.5, 1.0):
                    for e in ((1.0, 0.0), (0.7071, 0.7071)):
                        for off in ((0.0, 0.0), (rad, 0.0), (-rad, 0.0), (0.0, rad), (0.7 * rad, 0.7 * rad), (-0.7 * rad, 0.7 * rad)):
                            e_, off_ = np.array(e), np.array(off)
                            drift = kap / tp ** 0.5 * e_
                            mi = -off_                                   # Q_i = 0
                            v = np.rint(mi + rem * drift).astype(int)
                            mi1 = mi + Dl * drift
                            g = int(rad) + 2
                            c = np.rint(mi1).astype(int)
                            yy = np.stack(np.meshgrid(np.arange(c[0] - g, c[0] + g + 1), np.arange(c[1] - g, c[1] + g + 1), indexing='ij'), -1).reshape(-1, 2)
                            drin = np.hypot(yy[:, 0] - mi1[0], yy[:, 1] - mi1[1]) <= rad
                            P = p2(Dl, yy) * p2(rem - Dl, v - yy) / float(p2(rem, v))
                            c2min = min(c2min, float(P[drin].sum()))
                            # Randdichte: a = Dl ≥ τ′ nur für fD ≥ 1, b = rem − Dl ≥ τ′/2
                            if fD >= 1.0:
                                dmax = max(dmax, float(P[drin].max()) * tp)
    ok = c2min >= 4e-4 and dmax <= 12 * np.pi * np.exp(0.5)   # Schranken mit (K2′), Anhang K (bis 2026-11-13: 1e-3, 12π)
    ok_alles &= ok
    print(f"      (d) Schlauch-Schritt: kleinste Wahrscheinlichkeit = {c2min:.4f} ≥ c₂ = 0,001;  größte Randdichte · τ′ = {dmax:.3f} ≤ 12π   "
          f"{'ok' if ok else 'VERLETZT'}")
    return ok_alles


def konstanten_F12():
    print("\n(9) Zahlen zu F.11 und F.12")
    Cb = 8 * np.pi * np.exp(9 / 4)
    print(f"    C_b = 8π e^(9/4) = {Cb:.1f};  C₆ = ln 2 + ln(2/c₂) = {np.log(2) + np.log(2000):.2f} (c₂ = 0,001)")
    for n in (1e6, 1e12, 1e30):
        l1 = np.sqrt(17 * np.log(352 * n))
        j1 = int(np.ceil(l1 * l1))
        print(f"    n = {n:.0e}:  λ₁ = {l1:.1f} (für γ_n ≤ λ₁/12),  j₁ = {j1},  J = {4 * (l1 * l1 + 1):.0f},  "
              f"log₁₀ der ζ²-Bedingung aus P6b″ ≈ {(j1 - 1) * np.log10(4e-4):.0f} + log₁₀(θ^(1/2)/(2,0·10⁵ c̄_R j₁^1,5))")
    H, KF = 17, 17
    CE = 53 * np.pi * H * H * KF
    print(f"    c_q = ζ² (H C_E)^(1/2)/5003 = {np.sqrt(H * CE) / 5003:.3f} ζ²   (H = {H}, C_E = {CE:.3g})")


def konstanten():
    print("\n(4) Zahlen zu Satz F3 (R² = θ ln(1/ρ)/ρ; Grenzfall ρ → 0, ohne die Korrekturen (1 + o(1)))")
    C_T, C_1 = 2 * np.exp(0.25), 20.0
    print(f"    C_T = 2e^(1/4) = {C_T:.3f}, C_1 = {C_1:g}")
    for (H, K) in ((17, 17), (25, 17), (17, 540)):
        C_E = 53 * np.pi * H * H * K
        print(f"    H = {H}, K = {K}:  C_E = 53πH²K = {C_E:.3g}")
        for e in (1.0, 0.1, 0.01):
            th = e * e / (144 * C_1 * C_E)
            l0 = np.sqrt(e / (24 * C_1 * C_T))
            print(f"       ε = {e:5.2f}:  θ_F = ε²/(144 C_1 C_E) = {th:.2e},  λ₀ = {l0:.4f},  "
                  f"P(n_V ≥ ε ln(1/ρ)) ≤ ρ^{l0 * e:.2e}")
        print(f"       Skalenform: N_F(R) ≤ c_F R √(ρ ln(1/ρ)) mit c_F = 4,1 √(C_1 C_E) = {4.1 * np.sqrt(C_1 * C_E):.3g}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gross', action='store_true')
    a = ap.parse_args()
    rng = np.random.default_rng(1)
    print("λ_min(b) exakt:  " + ",  ".join(f"b={b}: {lam_min(b):.5f} (π/(2b²ln b) = {np.pi / (2 * b * b * np.log(b)):.5f})"
                                           for b in (2, 3, 4, 6)))
    alles = True
    faelle = [(8, 2), (8, 3), (12, 2)] + ([(12, 3)] if a.gross else [])
    for (L, N) in faelle:
        T = Torus(L)
        eps = {0: 0.0}
        S = None
        for k in range(1, N + 1):
            S = System(T, k)
            eps[k] = S.E + 4 * k
        print(f"\nL = {L}, N = {N}: E_N = {S.E:.6f}, ε_k = " + ", ".join(f"{eps[k]:.5f}" for k in range(1, N + 1)))
        # (1) gemischte Zerlegung
        for (b, b1, fk) in ((4, 2, [0]), (4, 2, [0, 1])) + (((6, 3, [0]), (6, 2, [0])) if L == 12 else ()):
            w = pruefe_zerlegung(S, b, b1, fk)
            ok = w >= -1e-8
            alles &= ok
            print(f"  (1) Zerlegung b={b}, fein b1={b1} in den groben Kästen {fk}: kleinster Eigenwert = {w:+.6f}   "
                  f"{'ok' if ok else 'VERLETZT'}")
        # (2), (3)
        print("  (2), (3):")
        if L == 8:
            V = [T.platz(x, y) for x in (1, 2) for y in (1, 2)]
            alles &= pruefe_F1_F2(S, eps, V, 1, 4, 2, 1, (0.0, 0.5, 1.0), (0.0, 0.5, 1.0, 2.0), rng, "V 2×2")
            alles &= pruefe_F1_F2(S, eps, V, 1, 4, 2, 2, (0.0, 0.5), (0.0, 0.5, 1.0, 2.0), rng, "V 2×2")
        else:
            V = [T.platz(x, y) for x in (5, 6) for y in (5, 6)]
            alles &= pruefe_F1_F2(S, eps, V, 1, 4, 2, 2, (0.0, 0.5, 1.5), (0.0, 0.5, 1.0, 2.0), rng, "V 2×2")
            V1 = [T.platz(5, 5)]
            alles &= pruefe_F1_F2(S, eps, V1, 2, 4, 2, 1, (0.0, 0.5, 1.0), (0.0, 0.5, 1.0, 2.0), rng, "V 1×1")
            alles &= pruefe_F1_F2(S, eps, V1, 2, 4, 2, 2, (0.0, 0.5), (0.0, 0.5, 1.0, 2.0), rng, "V 1×1")
            V3 = [T.platz(x, y) for x in (2, 3) for y in (2, 3)]
            alles &= pruefe_F1_F2(S, eps, V3, 1, 6, 3, 2, (0.0, 0.5, 1.0), (0.0, 0.5, 1.0, 2.0), rng, "V 2×2")
            alles &= pruefe_F1_F2(S, eps, V3, 1, 6, 2, 2, (0.0, 0.5, 1.0), (0.0, 0.5, 1.0, 2.0), rng, "V 2×2")
    print("\n(5) Lemma F6 und Lemma 6.8")
    T12 = Torus(12)
    alles &= pruefe_F6(Torus(8), 3, [Torus(8).platz(x, y) for x in (1, 2) for y in (1, 2)], 1, 4, 2, 2, (0.0, 0.5),
                       (0.05, 0.2, 0.5), "8×8, N=3, V 2×2")
    alles &= pruefe_F6(T12, 2, [T12.platz(5, 5)], 2, 4, 2, 2, (0.0, 0.5, 1.0), (0.02, 0.1, 0.3), "12×12, N=2, V 1×1")
    if a.gross:
        alles &= pruefe_F6(T12, 3, [T12.platz(5, 5)], 2, 4, 2, 2, (0.0, 0.5), (0.02, 0.1, 0.3), "12×12, N=3, V 1×1")
    print()
    alles &= pruefe_P5(rng)
    print()
    alles &= pruefe_F8(rng)
    print()
    alles &= pruefe_F11_F12(rng)
    konstanten()
    konstanten_F12()
    print("\nGesamt: " + ("alle Prüfungen bestanden" if alles else "MINDESTENS EINE PRÜFUNG VERLETZT"))


if __name__ == '__main__':
    main()
