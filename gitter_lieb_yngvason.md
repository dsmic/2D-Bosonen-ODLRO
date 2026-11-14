# Grundenergie des verdünnten 2D-Gitter-Bosegases

Eigenständige Notiz, Fassung 1, 2026-11-10. Teil des Programms [manuskript\_verduennt.md](manuskript_verduennt.md) (Lemmata 3.1–3.5, Satz 3.10). Kennzeichnung: [S] bewiesen, [B] Beweisskizze, [N] numerisch.

## Satz

Harte Bosonen auf (ℤ/Lℤ)² mit Nächstnachbar-Sprung 1, N = ρL², E\_N die Grundenergie von H = −A, ε\_N = E\_N + 4N. Mit der **Gitter-Streulänge**

```text
a = e^{−γ} 2^{−3/2} ≈ 0,1985        (Potentialkern a(x) = (2/π) ln(|x|/a) + O(|x|^{−2}))
```

und Y = 1/ln(1/(ρa²)) gilt im thermodynamischen Limes

```text
ε_N / N  =  4πρ Y · (1 + o(1))        für ρ → 0
```

- obere Schranke ε\_N/N ≤ 4πρY(1 + O(ln ln(1/ρ)/ln(1/ρ))) **[S]**, modulo der Standard-Asymptotik des Potentialkerns;
- untere Schranke ε\_N/N ≥ 4πρY(1 − C Y^{1/5}) **[B]**, nach dem Muster von Lieb–Yngvason (2D, J. Stat. Phys. 103, 2001).

Das ist das Gittergegenstück zum Lieb–Yngvason-Gesetz E/N = 4πρ/|ln(ρa²)| im Kontinuum (ħ²/2m = 1, kinetischer Operator L = −Δ\_Gitter). Eine Gitterfassung haben wir in der Literatur nicht gefunden (Literatursuche 2026-11-10: Lieb–Yngvason 2000/2001, Fournais et al. 2024 im Kontinuum, Sütő für Gitter-Oberschranken).

## 1. Harter Kern als Dirichlet-Bedingung [S]

Auf markierten Konfigurationen gilt K\_N = Σ\_i L\_i = 4N − A, mit L\_i dem Graph-Laplace-Operator in der Koordinate i und Φ = 0 auf Doppelbesetzungen. Der Grundzustand ist positiv, eindeutig und symmetrisch, also gilt ε\_N = min spec K\_N (Lemma 3.1 des Manuskripts).

## 2. Obere Schranke [S]

**Einfügeschranke (Lemma 3.5).** Für f: Λ → [0, 1], f(0) = 0, symmetrisch:

```text
ε_k − ε_{k−1}  ≤  2ρ′ D(f) / (1 − ρ′ S(f)),      ρ′ = (k−1)/M,  D(f) = Σ_Kanten (∇f)²,  S(f) = Σ (1 − f²)
```

Der Beweis benutzt Dysons Nächster-Nachbar-Jastrow F = min\_j f(x − x\_j) und die Kippidentität ⟨gψ, Kgψ⟩ − E‖gψ‖² = ½ Σ A ψψ′(g − g′)². Er braucht keine Dichte-Information über den alten Zustand.

**Summation.** ε\_N = Σ\_{k=1}^{N} (ε\_k − ε\_{k−1}). Mit f\_R = min(1, a(z)/a\_R), a\_R = (2/π) ln(R/a), gilt D(f\_R) = 4/a\_R (1 + O(1/R)) = 2π/ln(R/a) · (1 + O(1/R)) und S(f\_R) ≤ 2R²/a\_R (1 + o(1)). Damit

```text
ε_N / N  ≤  ρ · D(f_R) / (1 − ρ S(f_R))  ≤  2πρ / ln(R/a) · (1 + O(ρR²/ln R))
```

Mit R² = 1/(ρ t²) und t² ~ ln(1/ρ) folgt ln(R/a) = ½ ln(1/(ρa²)) − ln t, also ε\_N/N ≤ 4πρY(1 + O(ln ln(1/ρ)/ln(1/ρ))).

**Numerik [N].** Für das chemische Potential (doppelte Ordnung) gibt die Schranke mit optimalem R das 1,79-Fache (ρ = 10⁻¹) bis 1,16-Fache (ρ = 10⁻⁸) von 8πρY. Auf 6×6 und 8×8 liegt sie 2–22 % über dem exakten Wert (l1d\_schranke.py). Das Wurm-μ bei ρ = 1/16 … 1/4 liegt 21–26 % über 8πρY, passend zur bekannten nächsten Ordnung (§16.1).

## 3. Untere Schranke [B]

**Diskretes Dyson-Lemma [S].** Für f mit f(0) = 0 auf einem Bereich B und S ⊂ B gilt

```text
Σ_{Kanten in B} (∇f)²  ≥  Σ_{y∈S} U(y) f(y)²,      U = μ / R_eff(0 ↔ S),      Σ U = 1/R_eff
```

Dabei ist μ die Austrittsverteilung des Einheitsstroms. Beweis: Stromzerlegung in Pfade und Cauchy–Schwarz mit den Stromgewichten; der Potentialabfall ist längs jedes Pfades R\_eff. Für die Schale „Abstand ≥ R“ ist 1/R\_eff = 2π/ln(R/a) (1 + o(1)), numerisch auf 0,04 % bei R = 128 (l1\_dyson\_reff.py). Anders als im Kontinuum ist keine Sternförmigkeit nötig.

**Weitere Schritte [B]** (wie Lieb–Yngvason):

1. *Viele Teilchen:* das Dyson-Lemma für Teilchen i in der Nachbarzelle seines nächsten Nachbarn, mit Strom in beliebig geformten Zellen. Das ergibt Σ L\_i ≥ ε Σ L\_i + (1 − ε) W mit weichem Nächster-Nachbar-Potential W vom Gewicht 2π/ln(R/a) je Teilchen.
2. *Neumann-Kästen der Seite ℓ und Temple:* Grundzustand von T\_Q ist die Konstante, Lücke 2 − 2cos(π/ℓ). Im gleichverteilten Zustand ist ⟨W\_Q⟩ = n(n−1)/ℓ² · 2π/ln(R/a) · (1 − O(nR²/ℓ²)). Das gibt 4π je Teilchen und Dichte, mit den Bedingungen n² ≪ ε ln(R/a) und nℓ² ≪ εR ln.
3. *Verteilung auf die Kästen:* Konvexität, ε\_j/j nichtfallend (Lemma 3.6). Optimieren mit ρℓ² ~ Y^{−1/5}, ε ~ Y^{1/5}.

**Grenzen [N].** Die Kette Dyson → weiches Potential bleibt für zwei Teilchen in Kästen bis b = 12 gültig und behält 36–50 % der exakten Energie. Temple ist bei diesen Größen aber nicht anwendbar, weil ln(R/a) ≈ 3 zu klein ist (l1\_dyson\_kette.py). Die untere Schranke ist rein asymptotisch.

**Rechnergestützte Alternative [N + B].** Über die Neumann-Zerlegung gilt streng ε\_N ≥ Σ\_Q e\_b(n\_Q). Die exakten Kastenenergien folgen e\_b(2) = 4π/(b²(ln b + 1,7)) · (1 + o(1)) (Fit über b = 4 … 24, Grenzwert 0,97 · 4π), mit e\_b(3)/e\_b(2) ≈ 3,2 (paar-additiv) (l1\_kasten2.py). Mit linearer Paarung e\_b(n) ≥ (n/2) e\_b(2) [S] folgt ε\_N/N ≥ πρY(1 + o(1)), also ein Viertel der scharfen Konstante, für realistische ρ.

## 4. Offen

1. Untere Schranke Schritt 1–3 mit allen Konstanten ausschreiben.
2. Restglied der Potentialkern-Asymptotik mit expliziter Konstante zitieren (z. B. Fukai–Uchiyama; Kozma–Schreiber).
3. Kandidat für eine Prüfung in Lean: das diskrete Dyson-Lemma und die Einfügeschranke sind kurz, endlich und kombinatorisch (Lean-Kandidaten werden still gesammelt).
