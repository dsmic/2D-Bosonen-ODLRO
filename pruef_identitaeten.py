#!/usr/bin/env python
"""Prüft die exakten Identitäten aus weltlinien_beweisobjekt.md auf 4x4, N = 4 (Token-Graph, Perron-Vektor):
N0/N = (1-rho+1/M)<F>_w, sum E n_k = 4N - lambda_N, RK-Wert (M-N+1)/M, rho1 aus e^{beta A} gegen Perron-Formel.
Aufruf: python pruef_identitaeten.py
"""
import itertools, numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import eigsh, expm_multiply
L, N = 4, 4; M = L*L
nb = lambda s: [((s%L+1)%L)+L*(s//L), ((s%L-1)%L)+L*(s//L), s%L+L*((s//L+1)%L), s%L+L*((s//L-1)%L)]
def token(n):
    K = list(itertools.combinations(range(M), n)); idx = {c:i for i,c in enumerate(K)}
    r, c = [], []
    for i,k in enumerate(K):
        s = set(k)
        for x in k:
            for y in nb(x):
                if y not in s: r.append(i); c.append(idx[tuple(sorted(s-{x}|{y}))])
    return K, idx, sp.csr_matrix((np.ones(len(r)),(r,c)),shape=(len(K),len(K)))
K, idx, A = token(N); Km, idxm, Am = token(N-1)
lam, v = eigsh(A, k=1, which='LA'); lam = lam[0]; psi = np.abs(v[:,0]); psi /= np.linalg.norm(psi)
lamm = eigsh(Am, k=1, which='LA', return_eigenvectors=False)[0]
# Fasern
N0 = 0; Fw = 0; nk = {}
ks = [(2*np.pi*a/L, 2*np.pi*b/L) for a in range(L) for b in range(L)]
amp = {q: np.zeros(len(Km), complex) for q in range(M)}
for j,S in enumerate(Km):
    V = [x for x in range(M) if x not in S]
    phi = np.array([psi[idx[tuple(sorted(S+(x,)))]] for x in V])
    w = phi@phi; F = phi.sum()**2/(len(V)*w)
    N0 += phi.sum()**2/M; Fw += w*F
    for q,(kx,ky) in enumerate(ks):
        amp[q][j] = (np.exp(1j*(kx*np.array([x%L for x in V])+ky*np.array([x//L for x in V])))*phi).sum()/np.sqrt(M)
nk = np.array([np.vdot(amp[q],amp[q]).real for q in range(M)])
E = np.array([4-2*np.cos(kx)-2*np.cos(ky) for kx,ky in ks])
print("N0/N =", N0/N, " (1-rho+1/M)<F>_w =", (1-N/M+1/M)*Fw/N, " n_{k=0}/N =", nk[0]/N)
print("sum E n_k =", (E*nk).sum(), " 4N - lambda_N =", 4*N-lam)
print("Kosten 4 + lam_{N-1} - lam_N =", 4+lamm-lam, "; Torus-Luecke 4-2-2cos(2pi/L) =", 2-2*np.cos(2*np.pi/L))
# RK: uniform -> N0/N = (M-N+1)/M
u = np.ones(len(K))/np.sqrt(len(K)); N0rk = 0
for S in Km:
    V = [x for x in range(M) if x not in S]; N0rk += (sum(u[idx[tuple(sorted(S+(x,)))]] for x in V))**2/M
print("RK N0/N =", N0rk/N, " (M-N+1)/M =", (M-N+1)/M)
# Weltlinien: rho1 aus e^{beta t A} gegen Perron
beta = 12.0; x0, y0 = 0, 2+L*2
num = 0; den = 0
P = expm_multiply(beta*(A - lam*sp.identity(len(K))), sp.identity(len(K)).toarray())
den = np.trace(P)
for S in Km:
    if x0 in S or y0 in S: continue
    num += P[idx[tuple(sorted(S+(y0,)))], idx[tuple(sorted(S+(x0,)))]]
r1 = sum(psi[idx[tuple(sorted(S+(x0,)))]]*psi[idx[tuple(sorted(S+(y0,)))]] for S in Km if x0 not in S and y0 not in S)
print("rho1(x,y) Weltlinien beta=12:", num/den, " Perron:", r1)
