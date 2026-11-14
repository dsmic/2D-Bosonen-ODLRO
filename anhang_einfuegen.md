# Anhang E: Einfügen im Dirichlet-Quadrat und untere Schwänze

Stand 2026-11-13. Antwort auf Befund W6 des Reviews ([review\_2026-11-11.md](review_2026-11-11.md)). Ersetzt den Beweis von Satz 3.9 (b) in [satz\_3\_9\_dichteschranken.md](satz_3_9_dichteschranken.md) §4 und die Fassung von Lemma 12.1 und Folgerung 12.2 in §12.3. Prüfprogramm: [pruef\_einfuegen.py](pruef_einfuegen.py), Ausgabe in ergebnisse/pruef\_einfuegen.txt.

## Auf einer Seite

- **Die Lücke.** Schritt 2 von §4 fügt Teilchen in Quadrate mit Dirichlet-Rand ein und benutzt dafür die Einfügeschranke Lemma 6.5. Die ist nur auf dem Torus bewiesen.
- **Eine zweite Lücke, beim Nachrechnen gefunden.** §4 kippt mit der Innenzahl n\_U° und verweist für die Kosten auf Lemma B. Lemma B gilt aber nur für eine glatte Zählgröße, und die glatte Größe n\_φ von Lemma B ist ≥ n\_U. Für untere Schwänze zeigt die Markov-Ungleichung dann in die falsche Richtung. Folgerung 12.2 setzt die harte Zahl n\_U in Lemma T3 ein. Dort kostet jeder Sprung über den Zellrand O(λ²) und nicht O(λ²/s²).
- **Lemma E1 [S].** Im Dirichlet-Quadrat der Seite ℓ kostet jedes eingefügte Teilchen höchstens die Dirichlet-Grundenergie λ\_D plus die Hälfte der Torus-Schranke aus Lemma 6.5. Dabei ist die Dichte durch (k − 1) max φ² ≤ 4(k − 1)/(ℓ + 1)² zu ersetzen. Der Faktor 4 ist das Verhältnis von Maximum zu Mittel von φ²; er ist der Preis dafür, dass man nicht weiß, wo die alten Teilchen sitzen.
- **Eine Zählgröße für alles.** S\_U = Σ\_x w(x) n\_x mit einem Gewicht w, das auf dem inneren Teil jeder Zelle gleich 1 ist und am Zellrand glatt auf 0 fällt. Es gilt n\_U° ≤ S\_U ≤ n\_U. Lokalisierung, Kippung und Lemma T3 laufen alle über S\_U.
- **Lemma E3 [S]:** ε(Φ) − ε\_N ≥ A\_low − μ̄′ E\_Φ S\_U für jeden Zustand Φ. **Satz E [S]** (eine Zeit) und **Folgerung E4 [S, gegeben Lemma T3 und Satz 3.9 (a^W)]** (viele Zeiten) ersetzen Satz 3.9 (b) und Folgerung 12.2.
- **Preis:** c₃ ≈ c₁²/(512πκ\_μ (8πκ\_μ + c₁)) statt (c₁²/800)/(8πκ\_μ + c₁/2), und b₋ = c₃″/8 statt c₃/4. Das ist etwa 6- bis 8-mal kleiner (Tabelle in E.6). Für die Existenz zählt nur, dass b₋ eine feste positive Konstante ist.

## E.0 Bezeichnungen

- **Gitter und Energien** wie in satz\_3\_9 §0: ℒ\_n = 4n − A auf Hartkern-Konfigurationen von Λ, ε\_n die Grundenergie, ε(Φ) = ⟨Φ, ℒΦ⟩. Ferner Y = 1/ln(1/(ρa²)), ε\_N/N ≥ c₁ρY (Lemma 3.3), M = |Λ|.
- **Schrankenfunktion von Lemma 6.5.** Für f: ℤ² → [0, 1] mit f(0) = 0, endlich vielen Stellen mit f ≠ 1 und gleichen Kantensummen in beiden Richtungen sei g\_f(x) = 2x D(f)/(1 − x V(f)) für x V(f) < 1, und μ\_6.5(x) = inf\_f g\_f(x). Lemma 6.5 sagt: ε\_n − ε\_{n−1} ≤ μ\_6.5((n − 1)/M).
- **Zwei Eigenschaften von μ\_6.5.** Jedes g\_f ist wachsend und konvex mit g\_f(0) = 0. Also ist μ\_6.5 wachsend, und μ\_6.5(tx) ≤ t μ\_6.5(x) für 0 ≤ t ≤ 1.
- **μ̄ = μ\_6.5(ρ₊)** mit ρ₊ = (N + k − 1)/M, k wie in Lemma E3. Das deckt alle Zuwächse bis N + k ab. In den Tabellen steht μ̄ = κ\_μ 8πρY; κ\_μ bezieht sich hier auf die Dichte ρ₊ ≤ (1 + η)ρ.
- **Zellen.** s ist durch 8 teilbar und s ≥ 64. Jede Zelle Q hat in der Mitte das Quadrat Q° der Seite s/2. Für x ∈ Q sei d(x) der ℓ∞-Abstand von x zu Q°, also d ∈ {0, …, s/4}, und d = s/4 auf der äußersten Lage. U ist eine Vereinigung von u Zellen, I die Vereinigung ihrer Q°, |U| = u s², m = ρs².
- **Masken.** ϑ\_p = (π/2) min(1, 8d/s), p = cos ϑ\_p, q = sin ϑ\_p; außerhalb von U ist ϑ\_p = π/2. Ferner ϑ\_w = (π/2) clip(8d/s − 1, 0, 1) und w = cos² ϑ\_w; außerhalb von U ist w = 0.
- **Zählgrößen.** X\_U = Σ\_x p(x)² n\_x (erwartete Zahl der Innen-Teilchen beim Lokalisieren) und S\_U = Σ\_x w(x) n\_x (glatte Innenzahl).

**Eigenschaften der Masken [S].**

- **(a)** n\_I ≤ X\_U ≤ S\_U ≤ n\_U. Denn p = 1 auf I, p > 0 nur bei d < s/8, dort ist w = 1, und w ≤ 1\_U.
- **(b)** Über jede Kante ändern sich ϑ\_p und ϑ\_w um höchstens Δ = 4π/s.
- **(c)** Eine Kante, über die sich ϑ\_p ändert, hat beide Endpunkte bei d ≤ s/8, wo w = 1 ist. Für die Menge Z⁺ dieser Endpunkte gilt also n\_{Z⁺} ≤ S\_U.
- **(d)** Für jede Kante x ∼ y gilt

```text
( w(x) − w(y) )²  ≤  72π² w(x)/s²  +  2304π⁴/s⁴,        |w(x) − w(y)| ≤ 0,44
```

  und die linke Seite ist 0, außer beide Endpunkte liegen im Ring R = {s/8 ≤ d ≤ s/4} ⊂ U.

*Beweis von (d).* Für a, b ∈ [0, π/2] ist |cos² a − cos² b| = |sin(a + b)| |sin(a − b)| ≤ |a − b| (cos a + cos b) ≤ |a − b| (2 cos a + |a − b|). Mit |a − b| ≤ Δ und (u + v)² ≤ (9/8)u² + 9v² folgt (Δw)² ≤ Δ² (4,5 w(x) + 9Δ²). Einsetzen von Δ = 4π/s gibt die Formel; für s ≥ 64 ist Δ(2 + Δ) ≤ 0,44. ∎

## E.1 Lemma E1: Einfügen im Dirichlet-Quadrat [S]

**Lemma E1.** Sei Q ein Gitterquadrat der Seite ℓ und ℒ^D\_k = 4k − A\_Q der Hartkern-Operator für k Teilchen in Q; Sprünge aus Q heraus entfallen (Dirichlet-Rand). ε^D\_k sei seine Grundenergie, ε^D\_0 = 0. φ > 0 sei der normierte Grundzustand für ein Teilchen, mit

```text
λ_D = 8 sin²( π/(2(ℓ+1)) )  ≤  2π²/(ℓ+1)²,        φ_max²  ≤  4/(ℓ+1)²
```

Für k ≥ 1, x\_k = (k − 1) φ\_max² und jedes f wie in E.0 mit x\_k V(f) < 1 gilt

```text
ε^D_k − ε^D_{k−1}  ≤  λ_D + 2 x_k D(f) / (1 − x_k V(f))
ε^D_k              ≤  k ( λ_D + ½ μ_6.5(x_k) )  ≤  k ( λ_D + ½ μ_6.5( 4(k−1)/(ℓ+1)² ) )
```

*Beweis.* Wie Lemma 6.5, mit φ an der Stelle der Konstanten.

1. **Gelockerter Operator.** ℒ\_rel = ℒ^D\_{k−1} ⊗ 1 + 1 ⊗ (−Δ\_Q) auf Paaren (alte Konfiguration X, neuer Platz x); das neue Teilchen sieht die alten nicht. Mit dem Grundzustand ψ ≥ 0 von ℒ^D\_{k−1} ist Ψ₀ = ψ ⊗ φ Eigenfunktion zum Eigenwert ε^D\_{k−1} + λ\_D.
2. **Versuchszustand.** F(X, x) = min\_j f(x − x\_j). FΨ₀ verschwindet, wenn das neue Teilchen auf einem alten sitzt. Auf solchen Funktionen stimmen die Formen von ℒ\_rel und ℒ^D\_k überein, und ε^D\_k ist höchstens der Rayleigh-Quotient (wie in Lemma 6.5, Schritte 2 und 3).
3. **Kippidentität** (Lemma 6.2) für die Eigenfunktion Ψ₀: ε^D\_k ≤ ε^D\_{k−1} + λ\_D + 𝒩/𝒵 mit 𝒩 = Σ\_Kanten Ψ₀Ψ₀′ (F − F′)² und 𝒵 = ‖FΨ₀‖². Kanten aus Q heraus kommen in 𝒩 nicht vor; sie stecken als Diagonalteil in λ\_D.
4. **Nenner.** 1 − F² ≤ Σ\_j (1 − f(x − x\_j)²) und Σ\_x φ(x)² (1 − f(x − x\_j)²) ≤ φ\_max² V(f). Also 𝒵 ≥ 1 − x\_k V(f).
5. **Sprünge des neuen Teilchens.** φ(x)φ(x′) ≤ φ\_max² und |min a − min b| ≤ max |a − b|. Sie tragen ≤ (k − 1) φ\_max² D(f) bei.
6. **Sprünge eines alten Teilchens j** in Richtung e: Nur der j-te Eintrag im Minimum ändert sich, und Σ\_x φ(x)² (f(x − x\_j) − f(x − x\_j − e))² ≤ φ\_max² D(f)/2 (gleiche Kantensummen). Mit Σ\_Kanten ψψ′ = ⟨ψ, A\_Q ψ⟩/2 ≤ 2(k − 1) tragen sie ≤ (k − 1) φ\_max² D(f) bei.
7. **Summe.** Das gibt die erste Zeile. Wegen Konvexität ist g\_f(x\_{k′}) ≤ ((k′ − 1)/(k − 1)) g\_f(x\_k), und Σ\_{k′=1}^{k} (k′ − 1)/(k − 1) = k/2. Infimum über f und Monotonie von μ\_6.5 geben die zweite Zeile. ∎

*Vergleich mit dem Torus.* Lemma 6.5 hat die Dichte (k − 1)/M; hier steht (k − 1) φ\_max² ≈ 4(k − 1)/ℓ². Der wahre Wert läge beim Mittel von φ², also um den Faktor 4 tiefer. Für den Beweis ist das gleichgültig: Es verschiebt nur η und damit c₃.

## E.2 Lemma E2: Produkt aus Außen- und Innenzustand [S]

**Lemma E2.** Sei I ⊂ Λ, Φ\_a ein normierter Zustand mit n\_a Teilchen, der auf Konfigurationen mit einem Teilchen in I verschwindet, und Φ\_b ein normierter Zustand mit n\_b Teilchen, alle in I. Setze Φ(X) = Φ\_a(X \ I) Φ\_b(X ∩ I) für |X ∩ I| = n\_b und sonst 0. Dann ist Φ normiert, und

```text
ε(Φ)  =  ε(Φ_a) + ε^D_I(Φ_b),        ε^D_I(Φ_b) = ⟨Φ_b, (4n_b − A_I) Φ_b⟩,        also  ε(Φ_a) ≥ ε_{n_a+n_b} − ε^D_I(Φ_b)
```

*Beweis.* Ein Sprung über den Rand von I ändert |X ∩ I| und führt auf eine Konfiguration, auf der Φ und Φ\_a verschwinden. Er trägt weder zu ⟨Φ, AΦ⟩ noch zu ⟨Φ\_a, AΦ\_a⟩ bei. Sprünge außerhalb von I geben ⟨Φ\_a, AΦ\_a⟩, Sprünge in I geben ⟨Φ\_b, A\_I Φ\_b⟩; besetzte Zielplätze sind in beiden Rechnungen gesperrt. Der Diagonalteil 4(n\_a + n\_b) zerfällt ebenso. ∎

## E.3 Lemma E3: Energieungleichung mit der glatten Innenzahl [S]

**Annahmen.** s² ≥ 316/(c₁ρY), η = c₁ρY/(32 μ̄) (= c₁/(256πκ\_μ)), k\_Q = ⌊ηm⌋ ≥ 1 Teilchen je Q°, k = u k\_Q.

**Lemma E3.** Für jeden normierten N-Teilchen-Zustand Φ gilt

```text
ε(Φ) − ε_N  ≥  A_low − μ̄′ E_Φ S_U
A_low = (c₁ρY/2) k  ≥  (c₁ρY)² ρ|U| (1 − 1/(ηm)) / (64 μ̄),        μ̄′ = μ̄ + 32π²/s²  ≤  μ̄ + c₁ρY
```

*Beweis.*

1. **Lokalisieren** mit ϑ\_p (Lemma 6.7). Im Sektor mit j Innen-Teilchen sei Ψ\_j(η\_innen, η\_außen) der Anteil von UΦ, w\_j = ‖Ψ\_j‖², also Σ\_j w\_j j = E\_Φ X\_U. Der Fehler ist F ≤ (Δ²/2) · 4 E\_Φ n\_{Z⁺} ≤ (32π²/s²) E\_Φ S\_U (Eigenschaft (c)). Lässt man den harten Kern zwischen den Farben fallen, ändern sich die Formen nicht, denn Ψ\_j verschwindet auf Überlappungen. Der Innen-Teil ist ≥ 0.
2. **Außen-Teil und Einfügen.** Für festes η\_innen verschwindet Ψ\_j(η\_innen, ·) auf Konfigurationen mit einem Teilchen in I, denn dort ist q = 0. Lemma E2 mit Φ\_b = Produkt der Dirichlet-Grundzustände von k\_Q Teilchen in jedem Q° gibt für den normierten Außen-Teil ε ≥ ε\_{N−j+k} − ε^D\_I(k).
3. **Kosten des Einfügens** (Lemma E1 mit ℓ = s/2). λ\_D ≤ 8π²/s² ≤ c₁ρY/4. Die Dichte ist 4(k\_Q − 1)/(s/2 + 1)² < 16ηρ, also ½ μ\_6.5(·) ≤ ½ (16ηρ/ρ₊) μ̄ ≤ 8ημ̄ = c₁ρY/4. Zusammen ε^D\_I(k) ≤ (c₁ρY/2) k.
4. **Energiebilanz.** Lemma 6.6 und 3.3: ε\_{N+k} ≥ ε\_N (1 + k/N) ≥ ε\_N + c₁ρY k. Lemma 6.5 bis N + k: ε\_{N−j+k} ≥ ε\_{N+k} − jμ̄.
5. **Zusammen:** ε(Φ) − ε\_N ≥ (c₁ρY/2) k − μ̄ E\_Φ X\_U − F ≥ A\_low − μ̄′ E\_Φ S\_U, mit X\_U ≤ S\_U. Ferner k ≥ u (ηm − 1) = ηρ|U| (1 − 1/(ηm)). ∎

## E.4 Satz E: untere Schwänze zu einer Zeit [S]

**Weitere Annahmen** (aus Lemma A, satz\_3\_9 §1): Kastenseite b ≤ s/4 mit c\_b − μ̄ − C\_L/s² ≥ c\_b/4 (wie in §3) und c\_b s² ≥ 2(C\_T + C\_T′/s²), mit C\_T = 45π² ≈ 444 und C\_T′ = 1440π⁴ ≈ 1,4·10⁵. Die letzte Bedingung gilt für kleine ρ, denn c\_b s² ≥ πHm/(2(ln b + 3,6)) → πHK.

**Satz E** (neue Fassung von Satz 3.9 (b))**.** Für 0 ≤ λ ≤ ½ gilt

```text
log E_ψ e^{−λ S_U}  ≤  −λ c₃′ ρ|U|,        c₃′ = (c₃ − ε₁)/(1 + ε₂),        c₃ = A_low/(μ̄′ ρ|U|)  ≥  (c₁ρY)² (1 − 1/(ηm)) / (64 μ̄ μ̄′)
ε₁ = 2 C_V C_T′ / (s⁴ b² ρ μ̄′),        ε₂ = C_T / (4 s² μ̄′)  ≤  0,014 c₁/κ_μ
P( n_Q < 2b₋m für alle Zellen Q ⊂ U )  ≤  exp( −(c₃′/2 − b₋) ρ|U| )  ≤  e^{−b₋ ρ|U|}        für b₋ ≤ c₃′/4
```

Für ρ → 0 geht ε₁ → 0, denn s⁴b²ρμ̄′ = m · b² · s²μ̄′ mit s²μ̄′ ≥ 632 und b, m → ∞. ε₂ bleibt eine feste kleine Zahl.

*Beweis.*

1. **Kippen** mit g = e^{−λS\_U/2}, Φ\_g = gψ/‖gψ‖, E\_g der Erwartungswert unter ψ²g²/⟨g²⟩. Es ist d/dλ log E\_ψ e^{−λS\_U} = −E\_g S\_U.
2. **Kosten der Kippung** (Lemma 3.2 wie in Lemma B): (g − g′)² ≤ min(g, g′)² (λ|Δw|/2)² e^{λ|Δw|}, ψψ′ min(g, g′)² ≤ ½(ψ²g² + ψ′²g′²), höchstens 4 Sprünge je Teilchen, e^{λ|Δw|} ≤ 1,25. Mit (d) folgt ε(Φ\_g) − ε\_N ≤ λ² (C\_T E\_g S\_U/s² + C\_T′ E\_g n\_U/s⁴).
3. **Der Ring** (Lemma A für Φ\_g, mit n\_U ≤ n\_φ): (c\_b/4) E\_g n\_φ − C\_V c\_b |U|/b² ≤ ε(Φ\_g) − ε\_N ≤ (c\_b/8) E\_g n\_φ. Also E\_g n\_U ≤ 8 C\_V |U|/b².
4. **Lemma E3 für Φ\_g** zusammen mit 2 und 3, λ² ≤ ¼: (μ̄′ + C\_T/(4s²)) E\_g S\_U ≥ A\_low − 2 C\_V C\_T′ |U|/(s⁴b²), also E\_g S\_U ≥ c₃′ ρ|U|.
5. **Integrieren** von 0 bis λ gibt die erste Zeile. Markov mit λ = ½ und S\_U ≤ n\_U (Eigenschaft (a)) gibt die zweite: Wenn alle n\_Q < 2b₋m, ist S\_U < 2b₋ρ|U|. ∎

## E.5 Folgerung E4: untere Schwänze zu vielen Zeiten [S, gegeben Lemma T3 und Satz 3.9 (a^W)]

**Folgerung E4** (neue Fassung von Folgerung 12.2)**.** Seien U\_k Zellvereinigungen zu Zeiten t₁ < … < t\_n mit Abständen ≥ s²/1000 und 0 ≤ λ ≤ ½. Dann gilt

```text
log E exp( −λ Σ_k S_{U_k}(t_k) )  ≤  −(λ/2) c₃″ ρ Σ_k |U_k|,        c₃″ = min( c₃′, c₃ − ε₃ ),        ε₃ = 580π⁴ C_a / (s⁴ μ̄′)
P( n_Q(t_k) < 2b₋m für alle (Q, k) ∈ 𝒜 )  ≤  exp( −λ (c₃″/2 − 2b₋) m |𝒜| )  =  e^{−b₋ m |𝒜|}        für λ = ½, b₋ = c₃″/8
```

*Beweis.* A\_k = −λ S\_{U\_k}, τ\_k = t\_{k+1} − t\_k.

1. **Zerlegen** wie in Folgerung 11.2: E[Π\_k e^{A\_k(t\_k)}] = e^{(t\_n − t₁)ε\_N} ⟨ψ, e^{A₁} e^{−τ₁ℒ} e^{A₂} ⋯ e^{A\_n} ψ⟩. Jedes e^{A\_k} wird halbiert, und Cauchy–Schwarz gibt das Produkt aus ‖e^{A₁/2}ψ‖, ‖e^{A\_n/2}ψ‖ und den Faktoren ‖e^{A/2} e^{−τℒ} e^{A/2}‖^{1/2} für A = A\_k und A = A\_{k+1}.
2. **Ränder.** ‖e^{A/2}ψ‖² = E\_ψ e^{−λS\_U} ≤ e^{−λc₃′ρ|U|} nach Satz E.
3. **Verkürzen.** ‖e^{A/2} e^{−τℒ} e^{A/2}‖ = ‖e^{−τℒ/2} e^{A/2}‖² ≤ e^{−(τ − δ\_T)ε\_N} ‖e^{A/2} e^{−δ\_Tℒ} e^{A/2}‖ für δ\_T ≤ τ. Gewählt wird δ\_T = λ/μ̄′ ≤ s²/1264.
4. **Lemma T3** mit A/2 = −(λ/2) S\_U und Zeit δ\_T: W₀(x) = −μ̄′ w(x) + Σ\_{y∼x} (cosh(λΔw/2) − 1). Mit cosh z − 1 ≤ (z²/2) cosh z und (d) ist die Summe ≤ λ² (36,3π² w(x)/s² + 1159π⁴ 1\_R(x)/s⁴). Für λ ≤ ½ und s²μ̄′ ≥ 632 ist der erste Teil ≤ μ̄′w(x)/2. Also ℋ̃ ≥ ℒ + (μ̄′/2) S\_U − κ n\_U mit κ = 1159π⁴λ²/s⁴ ≤ 290π⁴/s⁴.
5. **Energie.** E₀(ℋ̃) − ε\_N ≥ ½ [E₀(ℒ + μ̄′S\_U) − ε\_N] + ½ [E₀(ℒ − 2κ n\_U) − ε\_N]. Der erste Term ist ≥ ½ A\_low: Für jedes Φ ist ε(Φ) − ε\_N + μ̄′ E\_Φ S\_U ≥ max(0, A\_low − μ̄′x) + μ̄′x ≥ A\_low mit x = E\_Φ S\_U (Lemma E3; das ist Lemma 12.1 mit θ = μ̄′). Der zweite ist ≥ −κ C\_a ρ|U| nach Satz 3.9 (a^W) mit Hellmann–Feynman, wie in Folgerung 11.2, und n\_U ≤ n\_φ.
6. **Zusammen:** δ\_T (E₀(ℋ̃) − ε\_N) ≥ (λ/2)(c₃ − ε₃) ρ|U|. Eine innere Zeit bekommt das aus zwei halben Faktoren; eine Randzeit aus einem halben Faktor und aus Schritt 2. Markov mit S ≤ n wie in Satz E. ∎

## E.6 Zahlen

Grenzwerte für ρ → 0 bei K = K\_b, also ε₁, ε₃ → 0 und 1/(ηm) → 0; ε₂ = 0,014 c₁/κ\_μ ist mitgenommen ([pruef\_einfuegen.py](pruef_einfuegen.py), Teil 3).

| c₁                             | κ\_μ | η        | c₃       | b₋ = c₃′/8 | b₋ bisher | K\_b = ρs²/ln(1/(ρa²)) |
|--------------------------------|------|----------|----------|------------|-----------|------------------------|
| 3π/16 (Lemma 3.3 ohne Paarung) | 1,5  | 4,9·10⁻⁴ | 3,8·10⁻⁶ | 4,7·10⁻⁷   | 3·10⁻⁶    | ≈ 540                  |
| π (exakte Kastenenergien)      | 1,5  | 2,6·10⁻³ | 1,0·10⁻⁴ | 1,2·10⁻⁵   | 8·10⁻⁵    | ≈ 100                  |
| 4π (Lieb–Yngvason)             | 1    | 1,6·10⁻² | 2,6·10⁻³ | 2,8·10⁻⁴   | 1,8·10⁻³  | ≈ 25                   |

Woher der Faktor kommt: 2 aus dem Maximum von φ² (Lemma E1, gegen die alte Rechnung mit dem chemischen Potential), κ\_μ aus der ehrlichen Schranke μ̄ statt 8πρY, 2 aus b₋ = c₃/8 statt c₃/4, dazu der Lokalisierungsfehler 32π²/s² statt 8π²/s² im Nenner. K\_b bleibt.

## E.7 Prüfung

| Teil | Inhalt                                                                                     | Ergebnis                                            |
|------|--------------------------------------------------------------------------------------------|-----------------------------------------------------|
| 1    | Lemma E1 exakt: Dirichlet-Quadrate ℓ = 3, 4, 5, 6, 8, k ≤ 4 (ℓ = 8: k ≤ 3), drei Profile f | Zuwachs- und Summenschranke in allen Fällen erfüllt |
| 2    | Ungleichungen aus (d), Schritt 2 von Satz E und Schritt 4 von Folgerung E4                 | auf feinem Gitter erfüllt                           |
| 3    | c₃ und b₋ der Tabelle E.6                                                                  | wie angegeben                                       |

Schon bei ℓ = 6 liegt die Summenschranke für k = 2 nur um den Faktor 1,35 über dem wahren ε^D\_k/k.

## E.8 Was sich ändert und was offen bleibt

- **satz\_3\_9 §4:** Satz 3.9 (b) ist jetzt Satz E, mit S\_U statt n\_U°, λ ≤ ½ und b₋ = c₃″/8. Die Rate ist e^{−b₋ρ|U|} statt e^{−c₃ρ|U|}.
- **satz\_3\_9 §12.3:** Der Eingang ist Lemma E3 (S\_U, neues A\_low, μ̄′ = μ̄ + 32π²/s²). Lemma 12.1 gilt wörtlich mit S\_U statt n\_U. Folgerung 12.2 ist Folgerung E4.
- **Weiter hinten:** b₋ geht in κ₀, ζ und κ\_U nur als feste positive Konstante ein (Anhänge L, U, Z). Die Aussagen bleiben; die Zahlenbeispiele mit b₋ im Tutorial (§9, Ü 9.1) werden mit den neuen Werten größer.
- **Offen:** Die Konstanten sind grob (Faktor 4 in Lemma E1, Halbierung in Schritt 5 von E4). Für die Existenz ist das ohne Belang.
- **Frühere Fassung** (bis 2026-11-12, satz\_3\_9 §4): Schritt 2 mit „Lemma 3.5 im Quadrat“ ohne Beweis, Kippung mit n\_U° über Lemma B, Folgerung 12.2 mit der harten Zahl n\_U in Lemma T3.
