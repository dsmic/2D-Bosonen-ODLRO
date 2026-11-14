# Satz 3.9: Dichteschranken im Grundzustand, mit Konstanten

Teil von [manuskript\_verduennt.md](manuskript_verduennt.md). Fassung 2, 2026-11-10: Die Zellenschranke für mehrere Teilchen gilt ohne Paarung (jedes Teilchen benutzt seinen eigenen Laplace-Operator, siehe tutorial\_beweis\_verduennt.md §6.3). Das macht c\_b dreimal größer; H und C\_a sinken um den Faktor 3, K\_a bleibt. Alle Konstanten sind explizit, aber grob. §5 sagt, wo die Grobheit sitzt und was sie für den Staffellauf bedeutet.

## 0. Rahmen

Harte Bosonen auf Λ = (ℤ/Lℤ)², N = ρM, ψ = ψ\_N > 0 der Grundzustand, E\_N die Grundenergie, ε\_k = E\_k + 4k. Y = 1/ln(1/(ρa²)), a = e^{−γ}2^{−3/2}.

**Eingangsgrößen**, alle aus dem Manuskript:

| Symbol | Bedeutung                                             | Wert                                                                                                                                                     | Quelle                    |
|--------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| μ̄      | max\_{k ≤ N+k₀} (ε\_k − ε\_{k−1})                     | μ̄ = κ\_μ · 8πρY, κ\_μ = 1,2 … 1,8 bei realistischem ρ, → 1 für ρ → 0                                                                                     | Lemma 3.5 [S]             |
| c₁ρY   | Untergrenze für ε\_N/N                                | c₁ = 3π/16 (Lemma 3.3 ohne Paarung, [S]; Fassung 1 mit Paarung: π/16); c₁ ≈ π (exakte Kastenenergien, [S] rechnergestützt); c₁ → 4π (Lieb–Yngvason, [B]) | Lemma 3.3, §28, Satz 3.10 |
| c\_b   | Ballungskosten je überzähligem Teilchen im b×b-Kasten | c\_b = π/(2b² ln b) (Fassung 1 mit Paarung: π/(6b² ln b))                                                                                                | Lemma 3.3 [S]             |

*Zu c\_b (Nachtrag 2026-11-13, Review W5).* Die Form π/(2b² ln b) ist für 4 ≤ b ≤ 512 exakt nachgerechnet. Für alle b ≥ 2 ist bewiesen: λ\_min(b) ≥ π/(2b² (ln b + 3,6)) (Tutorial Lemma 6.3a). Für b > 512 ist c\_b in diesem Sinn zu lesen, also c\_b = πHρ/(ln(1/(Hρ)) + 7,2) bei 1/b² = Hρ. Die Konstanten der Spalten „ρ → 0“ ändern sich dadurch nicht; bei endlichem ρ kommt der Faktor ln b/(ln b + 3,6) dazu.

Zellen sind Quadrate der Seite s. U ist eine Vereinigung von u Zellen, |U| = u s², m = ρs². Für die Abschneidefunktion gilt φ\_U(x) = e^{−d(x,U)/s} (Graphenabstand), n\_φ = Σ\_x φ\_U(x) n\_x.

## 1. Grundungleichung durch Lokalisierung [S]

**Lemma A.** Für jeden normierten N-Teilchen-Hartkernzustand Φ und jede Kastenseite b ≤ s/4 gilt

```text
E(Φ) − E_N  ≥  ( c_b − μ̄ − C_L/s² ) · E_Φ[n_φ]  −  C_V c_b |U| / b²,        C_L = π² e² ≈ 72,9,   C_V = 29 (1 + 2b/s)²
```

*Beweis.*

1. **Masken.** Für h ≥ 0 sei p\_h = cos θ\_h mit θ\_h(x) = (π/2) · clip((d(x,U) − hs)/s, 0, 1). Dann ist p\_h = 1 auf U\_h = {d ≤ hs} und 0 außerhalb Ω\_h = {d ≤ (h+1)s}. Über eine Kante ändert sich θ höchstens um π/(2s), also ist 1 − cos(Δθ) ≤ π²/(8s²).
2. **Lemma 3.7** (Lokalisierung mit zwei Farben): E(Φ) ≥ Σ\_j w\_j (E^{innen}\_j(Ω\_h) + E\_{N−j}) − F\_h. Der Fehler ist F\_h ≤ (π²/(8s²)) Σ\_Kanten |ΦΦ′| 1{Sprung berührt Z\_h}, mit Z\_h der Übergangszone. Mit |ΦΦ′| ≤ ½(Φ² + Φ′²) und höchstens 4 Sprüngen je Teilchen folgt F\_h ≤ (π²/(2s²)) E\_Φ[n\_{Z\_h⁺}], wobei Z\_h⁺ die Zone samt Nachbarn ist. Die Innen-Zahl hat E\_w[j] = E\_Φ[Σ\_x p\_h(x)² n\_x].
3. **Innen.** −A auf Ω\_h mit hartem Kern ist ≥ −4j + Σ\_i L\_i^{Ω\_h, Neumann}, weil der Grad in Ω\_h höchstens 4 ist. Man pflastert den Torus fest mit Kästen der Seite b (für beliebiges L ausgeglichen, Seiten b und b + 1, Anhang Z, Z.13) und nimmt die Vereinigung Ω′\_h aller Kästen, die Ω\_h schneiden. Erlaubt man den j Teilchen das größere Gebiet Ω′\_h, sinkt die Energie nur. Neumann-Kästen und Lemma 3.3 für mehrere Teilchen (für Rechtecke Lemma 6.3b) geben E^{innen}\_j ≥ −4j + c\_b (j − #Kästen(Ω\_h)), denn Σ\_Q n\_Q 1{n\_Q ≥ 2} ≥ j − #Q; #Kästen(Ω\_h) zählt die Kästen, die Ω\_h schneiden (Review H6; bis 2026-11-13 standen hier die Randkästen nicht ausdrücklich).
4. **Außen.** Herausnehmen von j Teilchen gewinnt höchstens μ̄ je Teilchen: E\_{N−j} ≥ E\_N + 4j − j μ̄.
5. **Zusammen** für festes h: E(Φ) − E\_N ≥ (c\_b − μ̄) E\_w[j] − c\_b #Kästen(Ω\_h) − (π²/(2s²)) E\_Φ[n\_{Z\_h⁺}].
6. **Mitteln über h** mit Dichte e^{−h}:
   - ∫ p\_h(x)² e^{−h} dh ≥ ∫\_{h ≥ d/s} e^{−h} dh = φ(x).
   - ∫ 1{x ∈ Z\_h⁺} e^{−h} dh ≤ (1 + 1/s) e^{1 + 1/s} φ(x) ≤ 2e² φ(x) für s ≥ 1.
   - #Kästen(Ω\_h) ≤ (2h + 3)² u (s/b + 2)², und ∫(2h + 3)² e^{−h} dh = 29.
   - Bei Koeffizient c\_b − μ̄ ≥ 0 und E\_w[j] ≥ E n\_φ folgt die Behauptung. ∎

## 2. Kippschranke [S]

**Lemma B.** Für g = e^{±λ n\_φ}, 0 ≤ λ ≤ 1, s ≥ 6 und Φ\_g = gψ/‖gψ‖ gilt

```text
E(Φ_g) − E_N  ≤  C_K λ² s^{−2} E_g[n_φ],        C_K = 16 e ≈ 43,5
```

E\_g bezeichnet den Erwartungswert unter ψ²g²/⟨g²⟩.

*Beweis.* Lemma 3.2 gibt E(Φ\_g) − E\_N = Σ\_Kanten ψψ′(g − g′)²/⟨g²⟩.

- Bei einem Sprung x → y ändert sich n\_φ um Δ mit |Δ| ≤ (e^{1/s} − 1) e^{1/s} φ(x) ≤ 2e^{1/s} φ(x)/s.
- (g − g′)² ≤ min(g, g′)² (λΔ)² e^{2λ|Δ|} und ψψ′ min(g, g′)² ≤ ½(ψ²g² + ψ′²g′²).
- Jede Konfiguration hat höchstens 4 Sprünge je Teilchen, und φ² ≤ φ. Das ergibt den Faktor 16 e^{(2 + 4λ)/s}/s² ≤ 16e/s² für s ≥ 6. ∎

## 3. Obere Schwänze (Satz 3.9 a)

**Satz.** Sei b mit c\_b ≥ 2μ̄ und s² ≥ 4(C\_L + C\_K)/c\_b. Dann gilt für 0 ≤ λ ≤ 1

```text
log E_ψ e^{2λ n_φ}  ≤  2λ · C_a ρ |U|,        C_a = 4 C_V / (ρ b²)
```

*Beweis.* Lemma A für Φ\_g mit g = e^{λn\_φ} und Lemma B geben (c\_b − μ̄ − (C\_L + C\_K)/s²) E\_g n\_φ ≤ C\_V c\_b |U|/b². Der Klammerausdruck ist ≥ c\_b/4, also E\_g n\_φ ≤ 4C\_V|U|/b² = C\_a ρ|U|. Integration von d/dλ log E e^{2λn\_φ} = 2E\_g n\_φ. ∎

**Wahl der Konstanten.** Mit D₀ = 1/b² = Hρ ist c\_b = π Hρ/ln(1/(Hρ)). Die Bedingung c\_b ≥ 2μ̄ = 16πκ\_μ ρY verlangt H ≥ 16 κ\_μ ln(1/(Hρ))/ln(1/(ρa²)) ≈ 16κ\_μ.

| Größe                                                                  | ρ → 0 (κ\_μ = 1) | realistisch (κ\_μ = 1,5) |
|------------------------------------------------------------------------|------------------|--------------------------|
| H                                                                      | 17               | 25                       |
| C\_a = 4C\_V H                                                         | ≈ 2,0·10³        | ≈ 2,9·10³                |
| s² ≥ 4(C\_L + C\_K)/c\_b = 148 ln(1/(Hρ))/(Hρ) ⇒ K\_a = ρs²/ln(1/(Hρ)) | ≈ 8,7            | ≈ 5,9                    |

Für eine Zelle folgt per Markov P(n\_Q ≥ t) ≤ exp(2C\_a m − 2t). Die obere Schwelle ist also b₊ ≈ 2C\_a: Erst Zellen mit mehr als ~5·10³ m Teilchen sind sicher selten.

## 4. Untere Schwänze (Satz 3.9 b)

*Neue Fassung seit 2026-11-13 (Review W6). Beweis in [anhang\_einfuegen.md](anhang_einfuegen.md) (Anhang E).*

**Satz [S].** Sei U eine Vereinigung von u Zellen, s durch 8 teilbar, s ≥ 64 und s² ≥ 316/(c₁ρY). Es gelten die Bedingungen von Lemma A wie in §3 und c\_b s² ≥ 2(C\_T + C\_T′/s²) mit C\_T = 45π², C\_T′ = 1440π⁴. S\_U = Σ\_x w(x) n\_x sei die glatte Innenzahl: w = 1 im Inneren jeder Zelle bis zum Abstand s/8 vom mittleren Quadrat der Seite s/2, danach glatt auf 0 am Zellrand. Es ist n\_U° ≤ S\_U ≤ n\_U. Für 0 ≤ λ ≤ ½ gilt

```text
log E_ψ e^{−λ S_U}  ≤  −λ c₃′ ρ|U|,        c₃′ = (c₃ − ε₁)/(1 + ε₂),        c₃  ≥  c₁² (1 − 1/(ηm)) / ( 512π κ_μ (8π κ_μ + c₁) )
P(n_Q < 2b₋ m für alle Q ⊂ U)  ≤  e^{−b₋ ρ|U|},        b₋ = c₃″/8,        c₃″ = min(c₃′, c₃ − ε₃)  (Folgerung 12.2)
```

Dabei ist η = c₁/(256πκ\_μ) der Einfügeanteil; ε₁, ε₃ → 0 für ρ → 0, und ε₂ ≤ 0,014 c₁/κ\_μ.

*Beweisweg* (Anhang E).

1. **Einfügen im Dirichlet-Quadrat** (Lemma E1): wie Lemma 6.5, mit dem Dirichlet-Grundzustand φ statt der Konstanten. Je Teilchen kostet es höchstens λ\_D + ½ μ\_6.5((k − 1) max φ²), bei k = ⌊ηm⌋ Teilchen im Quadrat der Seite s/2 also ≤ 8π²/s² + 8ημ̄.
2. **Produktzustand** (Lemma E2): Außenzustand ohne Teilchen in den inneren Quadraten mal Innenzustand; die Energien addieren sich exakt.
3. **Energieungleichung** (Lemma E3): Lokalisieren mit Rampenbreite s/8 (Fehler ≤ (32π²/s²) E S\_U), Einfügen, Lemma 6.6. Für jeden Zustand Φ gilt ε(Φ) − ε\_N ≥ A\_low − μ̄′ E\_Φ S\_U mit μ̄′ = μ̄ + 32π²/s².
4. **Kippen** mit e^{−λS\_U/2}: Kosten ≤ λ² (C\_T S\_U/s² + C\_T′ n\_U/s⁴); den Ringterm begrenzt Lemma A. Integrieren in λ und Markov. ∎

**Zahlen** (Grenzwerte ρ → 0 bei K = K\_b; [pruef\_einfuegen.py](pruef_einfuegen.py)).

| c₁                             | κ\_μ | c₃       | b₋       | K\_b = ρs²/ln(1/(ρa²)) |
|--------------------------------|------|----------|----------|------------------------|
| 3π/16 (Lemma 3.3 ohne Paarung) | 1,5  | 3,8·10⁻⁶ | 4,7·10⁻⁷ | ≈ 540                  |
| π (exakte Kastenenergien)      | 1,5  | 1,0·10⁻⁴ | 1,2·10⁻⁵ | ≈ 100                  |
| 4π (Lieb–Yngvason)             | 1    | 2,6·10⁻³ | 2,8·10⁻⁴ | ≈ 25                   |

*Frühere Fassung (bis 2026-11-12).* log E\_ψ e^{−2n\_U°} ≤ −2c₃ρ|U| mit c₃ = (c₁²/800)/(8πκ\_μ + c₁/2), b₋ = c₃/4 (also 3·10⁻⁶, 8·10⁻⁵, 1,8·10⁻³) und Rate e^{−c₃ρ|U|}. Schritt 2 benutzte Lemma 6.5 im Dirichlet-Quadrat ohne Beweis, und Schritt 5 kippte mit n\_U° über Lemma B, das nur für glatte Gewichte gilt (Review W6).

## 5. Isolation (Satz 3.9 c) [B]

Ein Teilchen heißt nicht isoliert, wenn ein anderes im Abstand r = ζρ^{−1/2} liegt.

- Wie Lemma 4.4 der dichte-uniformen Arbeit: Q\_r = Σ\_χ χ(n\_χ − 1)\_+ über feine Kästen der Seite r mit glatter Abschneidung χ. Es gilt #nicht isoliert in S ≤ 2Q\_r.
- Ein Teil der Innenenergie wird reserviert, c\_r = π/(2r² ln r) ≈ π ρ/(ζ² ln(1/(ζ²ρ))) je überzähligem Teilchen.
- Mit Lemma A und Kippung λQ\_r (λ ≤ λ₀ = ζ, Kippkosten ≤ C λ² r^{−2} E n) folgt E\_g Q\_r ≤ C\_c ζ² ρ|S|, mit grob C\_c ~ 2C\_V H ≈ 1·10³.
- Daraus P(#nicht isoliert ≥ k′) ≤ exp(C\_c λ₀ ζ² ρ|S| − λ₀k′).

## 6. Bilanz: Wo die Konstanten grob sind, und was das bedeutet

**Herkunft der großen Zahlen.**

1. **C\_a ~ 2–3·10³** (obere Schwänze): Die Mittelung über die Maskenbreite h kostet das Nachbarschaftsvolumen (Faktor 29). Die Kastenzahl im Volumenterm kostet H ≈ 17–25, der Klammernenner einen Faktor 4. Das ist eine reine Beweisschranke. Wahr ist E n\_U = ρ|U|, und der Grundzustand ist sogar unter-Poisson.
2. **b₋ ~ 10⁻⁵** (untere Schwänze): Der Gewinn je hinzugefügtem Teilchen ist nur c₁ρY ~ ε\_N/N, die *halbe* Ordnung des chemischen Potentials, weil Lemma 3.6 mit ε/N statt μ arbeitet. Dagegen steht μ̄ ≈ 8πρY. Das Verhältnis μ̄/c₁ ≈ 12 erzwingt einen kleinen Einfügeanteil η = c₁/(256πκ\_μ) und gibt c₃ ≈ c₁²/(512πκ\_μ (8πκ\_μ + c₁)); darin steckt der Faktor 4 aus max φ² im Dirichlet-Quadrat (Anhang E, Lemma E1). Bis 2026-11-12 stand hier c₃ ~ c₁²/(800 · 8π).
3. **K ~ 6 … 1600:** Lokalisierungs- und Dirichlet-Kosten (C\_L ≈ 73, C\_K ≈ 44, Dirichlet ≈ 79, jeweils /s²) gegen die Energieskala c\_b bzw. c₁ρY. Obere Schwänze K\_a ≈ 6–9, untere Schwänze K\_b ≈ 25 (Lieb–Yngvason) bis 540 (Lemma 3.3 allein).

**Folgen für den Staffellauf.**

- **Wählbarkeit:** Garantiert sind nur ≥ 2b₋m Teilchen je guter Zelle. Die Wahrscheinlichkeit eines geteilten Labels ist dann ≤ 1/(2b₋m), also braucht man m ≫ 1/b₋ ~ 10⁵ (mit b₋ aus Anhang E; vorher 10⁴).
- **Exponentialmomente bei kleinem λ:** Im scharfen L2 (§6 des Manuskripts) braucht man log E e^{λn} ≈ λρ|U|(1 + O(λ)) für λ ~ 1/ln(1/ρ). Die Schranke hier gibt λ C\_a ρ|U| mit C\_a ~ 3·10³. Das ist ein Faktor 10³ im Exponenten, und es verlangt ln(1/ρ) ≫ 10³.
- **Insgesamt:** Mit diesen Konstanten ist ρ\* ein Turm von Exponentialen. Für den reinen Existenzsatz reicht das. Jede Schwelle, die man ausrechnen möchte, braucht schärfere Dichteschranken.

**Was schärfen würde.**

| Maßnahme                                                                                         | Wirkung                                   |     |              |     |                                                                                                |
|--------------------------------------------------------------------------------------------------|-------------------------------------------|-----|--------------|-----|------------------------------------------------------------------------------------------------|
| Lemma 3.6 mit μ statt ε/N (konkave Energie, zweite Ordnung)                                      | Faktor 2 im Gewinn, b₋ etwa 4-fach größer |     |              |     |                                                                                                |
| c₁ → 4π (Lieb–Yngvason)                                                                          | b₋ ~ 2·10⁻³, K ~ 25                       |     |              |     |                                                                                                |
| Breitere Übergangszonen mit optimiertem Profil                                                   | C\_L und C\_V kleiner                     |     |              |     |                                                                                                |
| **Varianzschranke unter Kippung**, Var\_g(n\_U) ≤ C\_var E\_g n\_U, statt der Mittelwertschranke | log E e^{λn} ≤ λρ                         | U   | + C\_var λ²ρ | U   | . Der Fehler wird zweiter Ordnung in λ, und für λ ~ 1/ln ist nur noch C\_var λ klein zu halten |
| Numerisch vorab: Var(n\_U)/E n\_U im Wurm messen (unter-Poisson erwartet, < 1)                   | zeigt das realistische C\_var             |     |              |     |                                                                                                |

Die Varianzschranke ist der eigentliche Hebel: Sie macht die Exponentialmomente bei kleinem λ scharf, und genau diese braucht das scharfe L2.

## 7. Vermutung: Unter-Poisson unter allen Kippungen [N + H]

**Numerik** ([l1\_varianz.py](l1_varianz.py), exakte Grundzustände). Var\_g(n\_U)/E\_g(n\_U) für Blöcke U der Seite h und Kippungen g = e^{λn\_U}:

| L, N (ρ)     | h   | λ = −1 | λ = 0 | λ = 0,5 | λ = 1 |
|--------------|-----|--------|-------|---------|-------|
| 8, 3 (0,047) | 2   | 0,98   | 0,86  | 0,71    | 0,52  |
| 8, 4 (0,062) | 3   | 0,94   | 0,71  | 0,53    | 0,39  |
| 8, 4 (0,062) | 4   | 0,89   | 0,59  | 0,43    | 0,30  |
| 6, 4 (0,111) | 3   | 0,88   | 0,57  | 0,41    | 0,29  |
| 6, 6 (0,167) | 4   | 0,64   | 0,37  | 0,27    | 0,18  |

In allen 48 berechneten Fällen (L = 6 und 8, h = 2–4, λ ∈ {−1; 0; 0,5; 1}) gilt Var\_g < E\_g.

**Vorbehalt Endlichkeit [N].** Die Tori sind kanonisch und klein. Schon die Gleichverteilung auf N-Teilmengen (ohne jede Korrelation) gibt hypergeometrisch Var/E = (1 − |U|/M)(M − N)/(M − 1) < 1. Bei λ = 0 liegt der gemessene Wert in allen fünf Zeilen darunter, aber ein großer Teil der Unterdrückung ist dieser Endlichkeitseffekt:

| L, N | h   | hypergeometrisch | gemessen | Verhältnis |
|------|-----|------------------|----------|------------|
| 8, 3 | 2   | 0,908            | 0,86     | 0,95       |
| 8, 4 | 3   | 0,818            | 0,71     | 0,87       |
| 8, 4 | 4   | 0,714            | 0,59     | 0,83       |
| 6, 4 | 3   | 0,686            | 0,57     | 0,83       |
| 6, 6 | 4   | 0,476            | 0,37     | 0,78       |

Der echte Test ist großkanonisch und groß, im Wurm bei L = 32: Var(n\_U)/E(n\_U) für Blöcke der Seite h, ungekippt und gekippt. Gekippt heißt dabei: umgewichtet mit e^{λ n\_U(0)}, das ist für kleines |λ| ohne neue Läufe machbar. Erwartung ohne Kippung: Die Suprafluidität drückt S(k) → 0 für k → 0, also ist großes U stark unter-Poisson (Varianz ~ Rand). Kritisch sind kleine Blöcke und λ > 0.

**Vermutung.** Für den Grundzustand harter Bosonen und jede Kippung g = e^{λ n\_U} gilt Var\_g(n\_U) ≤ E\_g(n\_U).

**Folge [S, bedingt].** f(λ) = log E e^{λ n\_U} erfüllt f″ = Var ≤ E = f′, mit f(0) = 0 und f′(0) = ρ|U|. Daraus folgt

```text
log E_ψ e^{λ n_U}  ≤  (e^λ − 1) ρ |U|        für alle λ ≥ 0      (Poisson-Schranke, ohne große Konstante)
```

Damit entfiele der Faktor C\_a ~ 10³ aus §3 ganz. Die Exponentialmomente bei kleinem λ wären scharf, genau wie das scharfe L2 sie braucht. Die untere Schranke (λ < 0) ist durch Unter-Poisson allein nicht gegeben; sie bleibt bei §4.

**Mögliche Beweiswege [H].**

1. **Negative Assoziation bzw. starke Rayleigh-Eigenschaft** (Borcea–Brändén–Liggett, dieselbe Theorie wie in der OpenAI-Arbeit zum Heisenberg-Ferromagneten). Die Gleichverteilung auf N-Teilmengen (RK-Punkt) ist stark Rayleigh. Bleibt die Eigenschaft für das Grundzustandsmaß ψ² entlang einer Interpolation erhalten, etwa unter der Doob-Dynamik?
2. **Direkt über das Kippargument:** Var\_g ist die zweite Ableitung. Eine Variante von Lemma A mit Kippung durch n\_U² statt n\_U?
3. **Physikalisch:** Var/E = 1 − ρ + ρ Σ\_{x≠y∈U} h(x−y)/|U|. Das ist unter-Poisson, solange die Paarkorrelation h im Mittel über U negativ ist, also bei hartem Kern und kleinem ρ plausibel.

## 8. Defekte Zellen sind selten (Satz 3.9 d)

Fassung 1, 2026-11-10. Gebraucht in [anhang\_gegenluecke.md](anhang_gegenluecke.md) G.5 und G.8. Gegenstück zu OpenAI „density-uniform“ (OA) Satz 7.2 mit Satz 6.1, Gleichung (17).

### 8.1 Aussage

Wählbarkeit und Brauchbarkeit sind wie in Anhang G.5.1 festgelegt (Isolation, Makro-Bedingung mit Radius D s, Randintervalle, Scores). Eine Zelle heißt **defekt**, wenn ihre Zahl n\_Q von Stück-Enden unter 2b₋m oder über b₊m/2 liegt, oder wenn mindestens der Anteil ε/4 ihrer Stücke einen der Wählbarkeitstests mit der strengeren Score-Schwelle C₀ − Δ\_A nicht besteht. Jede unbrauchbare Zelle ist defekt.

**Satz 3.9 (d) [B].** D und ε seien so gewählt, dass C\_a Σ\_{j≥0} D\_j³ e^{−κD\_j²} ≤ 10⁻⁴ b₋ ε mit D\_j = 2^j D; danach ζ klein und C₀ groß. Dann gibt es q(ρ) → 0 für ρ → 0, sodass für jede Menge U von Zellen gilt:

```text
P(alle Zellen von U sind defekt)  ≤  q^{|U|}
```

Gründe für Defekt sind: zu wenige Teilchen (Satz 3.9 b), zu viele (a), fehlende Isolation (c), hohe Scores, Trajektorien-Fehler. Neu sind hier nur die Trajektorien.

### 8.2 Lemma T1: Ein markiertes Teilchen wandert höchstens wie ein freies [S]

**Lemma T1.** Im stationären Grundzustandsprozess harter Bosonen auf (ℤ/Lℤ)², beliebiges N, gilt für jedes markierte Teilchen i, seine gelistete (über den Torus hinweg fortgesetzte) Verschiebung Δx\_i in eine Koordinatenrichtung über die Zeit δ und alle reellen θ:

```text
E[ e^{θ Δx_i} ]  ≤  e^{2δ(cosh θ − 1)}          (exakt der Wert der freien Irrfahrt, Rate 1 je Nachbar)
E[ e^{θ′ J_i} ]  ≤  e^{4δ(e^{θ′} − 1)}           (J_i = Zahl der Sprünge von i; Poisson-Schranke)
```

Gemeinsam für eine *feste* Menge S von Marken gilt E e^{Σ\_{i∈S} θ\_i Δx\_i} ≤ Π\_{i∈S} e^{2δ(cosh θ\_i − 1)}.

*Beweis.*

1. **Doob-Darstellung.** Mit unterscheidbaren Teilchen (markierte Fassung, Lemma 6.1 des Tutorials) und dem positiven Grundzustand ψ gilt E[F(ω₀) G(ω\_δ)] = e^{δE} ⟨Fψ, e^{−δH} Gψ⟩.
2. **Eichtransformation.** In der Pfadentwicklung von e^{−δH} trägt ein Sprung von i um ±1 in x-Richtung bei Gewichtung mit e^{θ x\_i} den Faktor e^{±θ}. Also ist E e^{θΔx\_i} = e^{δE} ⟨ψ, e^{−δH\_θ} ψ⟩, wobei H\_θ aus H entsteht, indem die x-Sprünge von i mit e^{±θ} statt 1 gewichtet werden. Auf dem Torus ist das ein wohldefinierter, nicht symmetrischer Operator (gelistete Verschiebung).
3. **Numerischer Wertebereich.** Für jeden Operator B mit Re B = (B + B\*)/2 ≥ λ gilt ‖e^{−δB}‖ ≤ e^{−δλ}, denn d/dt ‖e^{−tB}v‖² = −2⟨e^{−tB}v, (Re B) e^{−tB}v⟩. Hier ist Re H\_θ = H − (cosh θ − 1) A\_i^x, und A\_i^x (x-Sprünge von i auf freie Plätze) hat Zeilensummen ≤ 2, also A\_i^x ≤ 2. Damit Re H\_θ ≥ E − 2(cosh θ − 1).
4. Zusammen: E e^{θΔx\_i} ≤ e^{δE} ‖e^{−δH\_θ}‖ ≤ e^{2δ(cosh θ − 1)}. Für die Sprungzahl gewichtet man alle Sprünge von i mit e^{θ′}; dann ist Re H\_{θ′} = H − (e^{θ′} − 1) A\_i ≥ E − 4(e^{θ′} − 1). Für mehrere feste Marken addieren sich die Korrekturen. ∎

*Folge.* Chernoff: P(|Δx\_i| > d) ≤ 2 e^{−d²/(4δ)(1 + o(1))} für d ≤ δ, gaußisch wie bei der freien Irrfahrt. Die Doob-Drift (Abstoßung naher Teilchen) kann die Verschiebung also nicht vergrößern.

*Exakte Prüfung [N]* ([pruef\_markiert.py](pruef_markiert.py), markierte Teilchen auf kleinen Tori):

| L, N, δ | θ = 0,25 | θ = 0,5 | θ = 1 | θ = 2 |
|---------|----------|---------|-------|-------|
| 4, 2, 1 | 0,995    | 0,980   | 0,922 | 0,735 |
| 4, 3, 2 | 0,979    | 0,919   | 0,715 | 0,285 |
| 5, 2, 3 | 0,989    | 0,956   | 0,846 | 0,555 |

Angegeben ist E e^{θΔx}/e^{2δ(cosh θ − 1)}. Es ist immer < 1: Der harte Kern blockiert Sprünge, das Teilchen wandert weniger als ein freies.

**Warum T1 allein nicht reicht.** Für den Defekt-Satz braucht man die *Zahl* der fehlgehenden Stücke mit Ende in U. Die Menge dieser Teilchen hängt von der Konfiguration ab. Summiert man T1 über alle möglichen Markenmengen, verliert jede Cauchy–Schwarz-Abschätzung einen Faktor von der Größe der Zahl der Marken (∼ N^{k/2}). Das lösen die gefärbten Operatoren in 8.3.

### 8.3 Satz T2: Lokalisiertes Exponentialmoment der Trajektorien-Fehler [B]

J\_U^{fail} zähle die Stücke mit Ende in U, die die Makro-Bedingung oder die Randintervall-Bedingung verletzen.

**Satz T2 (OA (17)).**

```text
log E exp(J_U^fail)  ≤  C (Σ_{j≥0} D_j³ e^{−κ D_j²} + o_ρ(1)) · C_a ρ |U|
```

*Beweisweg* (OA §6, aufs Gitter und den Grundzustand übertragen):

1. **Kern eines fehlgehenden Stücks.** Fehler werden in Klassen j geteilt (größter Abstand vom Ende in (D\_j s, 2D\_j s]). Der Gitter-Wärmeleitungskern eines Stücks der Klasse j ist ≤ C e^{−c D\_j²} mal dem Kern einer Irrfahrt mit vergrößerter Diffusion c₁ > 1 im Gebiet Ω\_j (Abstand ≤ (2D\_j + 4)s von U, Dirichlet-Rand). Auf dem Gitter gilt das gaußische Verhalten für Verschiebungen bis ~ δ/s; darüber fallen Gitterkerne schneller (Poisson-Schwanz), was nur hilft.
2. **Gefärbter Operator.** Ein-Teilchen-Raum h̃ = ℓ²(Λ) ⊕ ⊕\_j ℓ²(Ω\_j); die Einbettung ṽf = (f, (√η\_j p\_j f)\_j) mit η\_j = e^{−κD\_j²} und Abschneidefunktionen p\_j; Ṽ = ṽ^{⊗N}. Die Grundfarbe sind die harten Bosonen. Markierte Farbe j ist eine freie Irrfahrt in Ω\_j mit Diffusion c₁ und Energielücke M\_j = κ D\_j²/δ, ohne Wechselwirkung. Weglassen des harten Kerns für markierte Teilchen vergrößert das Gewicht (Indikatoren ≤ 1). Daher majorisiert T = Ṽ\* e^{−δ𝐇} Ṽ den getesteten Kern punktweise, wie in OA.
3. **Grundzustand statt Spur.** Aus E e^J ≤ Z^{−1} Tr(e^{−(β−δ)H} T) und Hölder für Schatten-Normen folgt im Limes β → ∞: E e^J ≤ e^{δE\_N} λ\_max(T).
4. **Lipschitz-Einschub** (OA Lemma 6.2). Ṽ = e^A Ũ mit einer Isometrie Ũ und A = Σ\_i a(x\_i), a = ½ log(1 + Σ\_j η\_j p\_j²). Min-max gibt λ\_max(T) ≤ λ\_max(e^A e^{−δ𝐇} e^A) ≤ e^{−δ E₀(H̃)} mit H̃ = 𝐇 − Σ\_i W₀(x\_i). Auf dem Gitter ist W₀ = 2a/δ + 4(cosh|∇a|\_∞ − 1); das ist das Gegenstück zu 2a/δ + c₁|∇a|².
5. **Energiebilanz.** Ein Teilchen von der Grundfarbe in Farbe j zu setzen, kostet mindestens M\_j − μ̄ (Einfügeschranke, Lemma 3.5). Das ist ≥ 0, wenn D² ≳ 8πκ\_μ K/κ, also D von der Ordnung √K. Die anziehende Kraft W₀ ~ η/δ ist klein gegen c\_b; nach Lemma A gewinnt sie höchstens C δ^{−1} η C\_a ρ|U|. Also δ(E\_N − E₀(H̃)) ≤ C Σ\_j η\_j D\_j³ C\_a ρ|U| (Faktor D\_j³ aus |Ω\_j|).

### 8.4 Zusammensetzen (wie OA Satz 7.2)

Man zerlegt die defekten Zellen von U nach dem Grund; mindestens ein Drittel teilt einen Grund.

- **Zählgründe:** Satz 3.9 (a), (b).
- **Fehlende Isolation:** Satz 3.9 (c) zur Zeit t\_k und t\_{k+1}.
- **Scores** an getrennten Ankerpunkten: Summe der Scores ≤ Zeitintegral einer lokalen Teilchenzahl (OA Lemma 7.1). Exponentialmoment nach Lemma 6.8 des Tutorials und Satz 3.9 (a).
- **Trajektorien:** Satz T2 mit exponentieller Markov-Ungleichung.

Jede Möglichkeit ist ≤ e^{−c λ₀ m u}; es gibt ≤ 5 · 2^u Teilmengen, also q = C₁ e^{−cλ₀ m/3} → 0 wegen m = K ln(1/ρ) → ∞.

### 8.5 Stand und Folgen

- **[S]:** Lemma T1. Es ist auch für sich nützlich, etwa für das Lochstück j₀ (Anhang G.5.1).
- **[B]:** Satz T2 und das Zusammensetzen, beide eng nach OA. Die Eingaben sind vorhanden: obere Schwänze mit schwach anziehendem Potential, Einfügeschranke, Lemma 6.8.
- **Konstanten:** D wächst wie √K, damit die Farblücke M\_j das chemische Potential überwiegt. Die Bedingung C\_a e^{−κD²} ≲ 10⁻⁴ b₋ε verlangt D² ≳ ln(C\_a/(b₋ε))/κ. Beides sind feste Zahlen, unabhängig von ρ; sie gehen nur in die Konstanten der Stoßkosten ein (Verschiebungen bis D s).

## 9. Defekt-Lemma für die Zeitschleife (Satz D)

Fassung 1, 2026-11-10 abends; D6 und D7 am 2026-11-12 an [anhang\_feinskala.md](anhang_feinskala.md) (Anhang F) angepasst, D5 an [anhang\_unzugaenglich.md](anhang_unzugaenglich.md) (Anhang U). Erweitert §8 auf viele Scheiben und auf die neuen Gütebedingungen aus [anhang\_ausweichen.md](anhang_ausweichen.md) (Anhang P). Gebraucht in [anhang\_schleifen.md](anhang_schleifen.md) S.3 (Peierls-Eingang q) und im Aufsummieren von Satz 5.2.

### 9.1 Defektgründe

Eine Raum-Zeit-Zelle (Q, k), also Zelle Q in Scheibe k, heißt **defekt**, wenn einer der folgenden Gründe vorliegt. Alle sind lokal: Sie hängen nur von den Weltlinien in einem Raum-Zeit-Kasten der Seite C D s um (Q, k) ab. Für D6 und D7 ist das der Kasten 𝔎\_c vom Radius R\_K = D\_K s (Anhang F, F.11.1 und F.12.6); D\_K ist eine feste Zahl, aber viel größer als D.

| Grund | Inhalt                                                                                                    | Quelle der Seltenheit                        | Form der Schranke (Stand 2026-11-10; aktuell §12.4) |
|-------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------|-----------------------------------------------------|
| D1    | zu wenige oder zu viele Teilchen zu t\_k oder t\_{k+1}                                                    | Satz 3.9 (a), (b)                            | Energie [B]                                         |
| D2    | fehlende Isolation; getrennt gezählt mit dem Anteil ε₁ (Anhang L, Klausel (iii))                          | Satz 3.9 (c)                                 | Energie [B]                                         |
| D3    | hohe Scores                                                                                               | OA Lemma 7.1, Lemma 6.8 des Tutorials        | Energie [B]                                         |
| D4    | Fehlgänger (Makro-Bedingung, Randintervalle), gezählt nach End- und Anfangszelle (Anhang L, Klausel (iv)) | Satz T2, für die Anfangszelle mit Zeitumkehr | gefärbt [B]                                         |
| D5    | mindestens (ε/4) b₋ m reguläre Stücke mit Ende in der Zelle nicht streng zugänglich                       | Anhang U, Satz U                             | gefärbt [S, gegeben Satz T2]                        |
| D6    | (G1″) verletzt: zeitgemittelte Teilchenzahl in einem Gitterquadrat zu groß                                | Anhang F, Satz F7 und Satz F10               | Energie [S]                                         |
| D7    | (G2) oder (G4) für eine Linie im Kasten verletzt                                                          | Lemma R (a); Anhang F, Satz F11; Satz T2     | gefärbt [S, gegeben Satz T2]                        |

**Lemma 9.0 (Defekte sind scheibenweise erklärt) [S]** (Review 2026-11-13, H1 (b)). Ob (Q, k) defekt ist, hängt nur von den Weltlinien im Zeitintervall [t\_k, t\_{k+1}] ab, einschließlich der Lagen zu den beiden Randzeiten. Die Zeitfenster der einzelnen Tests sind:

| Test                              | Zeitfenster                                    | Ort                    |
|-----------------------------------|------------------------------------------------|------------------------|
| Teilchenzahl (D1), Isolation (D2) | Lagen zu t\_k und t\_{k+1}                     | §9.1, Anhang L (iii)   |
| Fehlgänger (D4)                   | Stücke der Scheibe k, also [t\_k, t\_{k+1}]    | Satz T2, Anhang L (iv) |
| Zugänglichkeit (D5)               | Stücke und freie Brücken innerhalb der Scheibe | Anhang U, U.1          |
| (G1″) (D6)                        | Gitterfenster, die in der Scheibe liegen       | Anhang F, F.11.1       |
| (G2\_A) (D7)                      | dyadische Fenster mit σ + 2^{i₁+1} ≤ t\_{k+1}  | Anhang F, F.12         |
| (G4′) (D7)                        | Gitter G\_m in [t\_k, t\_{k+1}]                | Anhang F, Satz F11     |

*Beweis.* Jede Zeile ist die Definition des Tests an der angegebenen Stelle; keiner greift über die Scheibengrenzen hinaus. ∎

Damit zerfällt {alle Zellen von 𝒜 defekt} an jeder Scheibengrenze in einen Teil vor und einen nach dieser Zeit. Das benutzen Lemma M14b und M14b′ (Anhang M, M.9.6 und M.9.11).

### 9.2 Aussage

**Satz D [S nach OA, ohne Literatur-Eingang (Gitterkern elementar, Anhang K, seit 2026-11-13); bis 2026-11-13: [B]; Stand in §12.4, Kette in Anhang Z, Z.12].** Es gibt q(ρ) → 0 für ρ → 0 (bei festen K, D, A, ε, ζ, κ), sodass für jede Menge 𝒜 von Raum-Zeit-Zellen gilt

```text
P_cl( alle Zellen von 𝒜 sind defekt )  ≤  q^{|𝒜|}
µ_ab( alle Zellen von 𝒜 sind defekt )  ≤  (C/M²) · q^{|𝒜|/4}        (Bezugsmaß der Zeitschleife)
```

Die zweite Zeile ist die Übertragung aus Anhang G.11.2 für Ereignisse auf (0, T).

### 9.3 Beweisweg

1. **Jede Schranke als Operatornorm.** Für jeden Grund g gibt es eine Zählgröße N\_g(U, k) der defekten Zellen in U × {k} und eine Kippung, deren Operatornorm je Scheibe beschränkt ist:
   - D1–D3, D6: Grundzustandsenergie mit Zusatzpotential (Satz 3.9 (a), (b), (c) und Lemma 6.8; für D6 in der Form von Satz F7). Lemma 6.8 ist schon eine Aussage über ein Produkt von Normen je Zeitschritt.
   - D4, D7: gefärbter Operator, λ\_max(T) ≤ e^{−δE₀(H̃)} (Satz T2, Schritt 3–4). Das ist eine Norm, keine bloße Erwartung.
   - D5: gefärbter Operator wie bei D4 (Anhang U, Lemma U3: Satz T2 für einen vorgegebenen Kern), nach Entkopplung und Kippidentität (Lemma U1, U2). Die Fassung bis 2026-11-11 berief sich auf Lemma P2; das ist eine Normschranke nur für feste Marken (Review K2).
2. **Viele Scheiben.** Die Kippungen verschiedener Scheiben wirken auf verschiedene Zeitintervalle. Im Grenzfall β → ∞ ist der Erwartungswert ein Matrixelement ⟨ψ\_N, Π\_k (gekippter Scheibenoperator) ψ\_N⟩ und damit höchstens das Produkt der Normen. So werden die Ein-Scheiben-Schranken multiplikativ, ohne Verlust.
3. **Mischen der Gründe.** Ist jede Zelle von 𝒜 defekt, so teilt man 𝒜 nach dem ersten zutreffenden Grund in höchstens 7 Teile. Es gibt ≤ 7^{|𝒜|} Aufteilungen. Für eine feste Aufteilung gibt Hölder mit Exponent 7 das Produkt der Ein-Grund-Schranken, je hoch 1/7. Jede Ein-Grund-Schranke ist ≤ e^{−c\_g m |𝒜\_g|} (D1–D4 und D7 mit (G2), m = K ln(1/ρ)), ≤ e^{−k₀|𝒜\_g|} (D5, Satz U, mit k₀ → ∞) oder ≤ q\_g^{|𝒜\_g|} mit q\_g → 0 (D6: q\_g = q₁^{1/(4m\_D²)} nach Satz F10; D7 mit (G4): q\_g = q₄^{1/(4m₄²)} nach Satz F11).
4. **Ergebnis.** q = 7 · max\_g (Ein-Grund-Rate)^{1/7}. Die Raten von D1–D4 und D7 mit (G2) gehen für ρ → 0 gegen 0, weil m → ∞. Die Raten von D6 und D7 mit (G4) gehen nach Satz F10 und Satz F11 gegen 0, aber nur langsam (wie exp(−c (ln(1/ρ))^{1/4}/ln ln(1/ρ)) und wie eine Potenz von ln(1/ρ), je hoch 1/(4m²)). Die Rate von D5 ist e^{−k₀} mit k₀ ~ ln(1/ρ)/ln ln(1/ρ); sie geht ebenfalls gegen 0 (Anhang U; κ = κ\_U ist dabei fest, eine Gruppengröße M gibt es nicht mehr). Dann ist auch q klein.
5. **Übertragung auf µ\_ab.** Das Ereignis „alle Zellen von 𝒜 defekt“ ist symmetrisch und liegt in (0, T); Anhang G.11.2 gibt den Exponenten 1/4.
6. **Nachtrag 2026-11-13: Teilchenzahl N + 1 und Anfangszustände** ([anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M.9.6, Lemma M14b). Die Schritte 1 und 2 geben Normschranken; sie gelten für jeden Anfangszustand, nur die Zeitränder der diagonalen Kippungen (D1, D2) werden zu einer Zeit im Grundzustand abgeschätzt. Von der Teilchenzahl hängen die Eingänge nur über ρ = N/M und μ̄ ab, und μ̄ ist schon als Maximum über k ≤ N + k₀ erklärt (§0). Also gilt jede Ein-Grund-Schranke mit denselben Konstanten auch im Sektor N + 1 (Dichte ρ(1 + 1/N)). Lemma M14b benutzt das für das Bezugsmaß µ\_ab^{(k)} mit spätem Schnitt, das auf [0, t\_k) N + 1 Teilchen hat. *Ausdrücklich (Review 2026-11-13, H1 (a)):* Alle Eingänge werden für das System mit N′ ∈ {N − 1, N, N + 1} Teilchen und der Dichte ρ′ = N′/M benutzt: Satz 3.9 (a^W) (formuliert für 0 ≤ J ≤ N; für N + 1 wendet man ihn auf das System mit N + 1 Teilchen an), Lemma 11.1 (k ≤ N′), Lemma A, Lemma A\_iso und Lemma E3 (gegen E\_{N′}). Die Konstanten ändern sich um Faktoren 1 + O(1/N). Den Sektor N − 1 braucht Lemma M14b′ (Anhang M, M.9.11, später Anfang am Schwanz).

### 9.4 Zu D6 und D7 im Einzelnen

- **D6 (zeitgemittelte Dichte; Fassung vom 2026-11-12).** (G1″) verlangt für Gitterquadrate aller Skalen von 8b bis s\_F/8 und für Gitterfenster passender Länge, dass die zeitgemittelte Teilchenzahl ≤ N\*(R) = 2c̄\_R R (ρ ln(1/ρ))^{1/2} + (ln(1/ρ))^{3/4} ist. Satz F7 (Anhang F) gibt dafür Exponentialmomente, multiplikativ über Familien, deren gleichzeitig aktive Gebiete disjunkt sind. Nach Ausdünnen auf Zellen mit disjunkten Kästen folgt P(alle Zellen von 𝒜 sind (G1″)-defekt) ≤ q₁^{|𝒜|/(4m\_D²)} (Satz F10). *Frühere Fassung:* (G1) auf einem Zeitgitter, über Satz 3.9 (a) und Lemma T1. Satz 3.9 (a) gilt aber nur ab der Zellskala und gibt auf der Skala √τ keine Schranke, die mit θ klein wird (Review K1).
- **D7 (Regularität).** (G2) betrifft Verschiebungen einzelner Linien über dyadische Zeitfenster. Für eine feste Marke gibt Lemma T1 Gauß-Schwänze je Fenster, gemeinsam über disjunkte Fenster durch die Norm-Produkt-Struktur. Für die *zufällige* Menge der Linien im Kasten braucht man wie bei Satz T2 eine Färbung: Farbe (i, w) markiert ein Teilchen, das im Fenster w der Skala 2^i unruhig ist; die Farbe kostet die Lücke c A² je Fenster. Das ist Satz T2 mit mehreren Skalen statt einer. (G4) betrifft die Schwankung in Fenstern der einen Länge t\_r = r²/(16β). Lemma F11a gibt für die freie Irrfahrt die Wahrscheinlichkeit ≤ 4e^{−β/71} je Fenster, und Satz F11 macht daraus mit einem Fach in Satz T2 die Schranke über viele Zellen. (G3) und das Fach R3 entfallen.
- **Kalibrierung [N]** ([pruef\_regularitaet.py](pruef_regularitaet.py), freie Irrfahrt mit Rate 1 je Nachbar, τ = 4096, 300 Bahnen): P((G2) versagt irgendwo) = 1; 0,95; 0,42; 0,03; 0 für A = 3, 4, 5, 6, 8; der mittlere Anteil unruhiger Fenster ist 41 %, 15 %, 4 %, 0,8 %, 0. (Für die frühere Bedingung (G3) war die Schranke B ≤ 1 + log₂(4β) im Mittel 6,5 und höchstens 8.) Also A ≈ 6–8; das gibt in Lemma P5 eine große, aber feste Konstante.

### 9.5 Stand

*Nachtrag:* Der aktuelle Stand steht in §12.4; die Tabelle unten ist der Stand vom 2026-11-11 (D2 und D3 sind seit §12.1 und §12.2 erledigt, Review 2026-11-13, H6).

| Teil                                      | Stand                                                                           |
|-------------------------------------------|---------------------------------------------------------------------------------|
| D5 (Zugänglichkeit)                       | [S], gegeben Satz T2 §10.3–§10.6 und Lemma F13 (Anhang U)                       |
| Normform und Produkt über Scheiben        | [S] für D1–D3, D6 (Lemma 6.8); [B] für D4, D5, D7 (über Satz T2)                |
| Mischen der Gründe, Übertragung auf µ\_ab | [S], gegeben die Ein-Grund-Schranken                                            |
| D4 (Satz T2), D7 (Fächer R2, G4)          | [S], gegeben die Eingänge (§10.7); Besucher eines Kastens §10.8, mit C\_β ≥ 500 |
| Ein-Grund-Schranke D1                     | [S] über §11 (Satz 3.9 a^W, Folgerung 11.2)                                     |
| Ein-Grund-Schranke D6                     | [S] über Anhang F (Satz F7, Satz F10)                                           |
| Ein-Grund-Schranken D2, D3                | [B] (Satz 3.9 c; OA Lemma 7.1)                                                  |

Der eigentliche Rest war damit **Satz T2**, einmal für die Makro-Fehlgänger und einmal für die Regularität; er ist in §10 ausgeschrieben. Beide folgen demselben Bauplan nach OA §6. Neu gegenüber OA ist auf dem Gitter nur der Lipschitz-Einschub mit W₀ = 2a/δ + 4(cosh|∇a|\_∞ − 1) (§8.3, Schritt 4).

## 10. Satz T2 ausgeschrieben (Gitter, Grundzustand)

Fassung 1, 2026-11-10 abends. Ersetzt die Skizze §8.3 und deckt die Defektgründe D4 und D7 aus §9. Vorbild ist OA §6 (Proposition 6.1, Lemma 6.2, §6.3). Im Grundzustand ist der Beweis an zwei Stellen einfacher als bei OA: λ\_max statt Spur und Hölder, und keine ideale Bose-Summe für die markierten Farben. Neu ist der Lipschitz-Einschub auf dem Gitter.

### 10.0 Rahmen

- **Energie:** ℒ = H + 4N = Σ\_i L\_i (Lemma 6.1 des Tutorials), Grundenergie ε\_N, Grundzustand ψ ≥ 0. Der freie Ein-Teilchen-Kern ist e^{−δL} = e^{δΔ} = p\_δ, die Irrfahrt mit Rate 1 je Nachbar.
- **Scheibe** der Dauer δ = s². Jedes Teilchen hat in ihr ein Stück von S (Anfang) nach E (Ende). U ist eine Vereinigung von Zellen.
- **Fächer** (bins) eines fehlerhaften Stücks mit Ende in U; jedes Fach b hat eine Reichweite h\_b und eine Kleinheit η\_b:

| Fach             | Fehler                                                              | h\_b | η\_b          |
|------------------|---------------------------------------------------------------------|------|---------------|
| j ≥ 0 (makro)    | größter Abstand vom Ende in (D\_j s, 2D\_j s], D\_j = 2^j D         | D\_j | e^{−κD\_j²}   |
| ∗ (Rand)         | verlässt in den Randintervallen die kleine Kugel, sonst kein Fehler | D    | e^{−κ r\_∗}   |
| R2 (Regularität) | (G2\_A) aus Anhang P verletzt, sonst kein Fehler                    | D    | C δ τ^{−c(A)} |
| G4 (Kurzzeit)    | (G4′) aus Anhang F verletzt, sonst kein Fehler                      | D    | C p₄^{1/3}    |

- **Wahl von η\_b:** so, dass die Fehlerwahrscheinlichkeit des Fachs für die freie Brücke ≤ c η\_b^{3/2} ist. Die Tabelle gibt die Größenordnung; für R2 etwa ist genau genommen η\_{R2} = (Cδτ^{−c(A)})^{2/3}. Das Fach G4 (seit 2026-11-12 anstelle von R3, B ≥ b₀ aus (G3)) wird mit dem Gewicht w = 1 + p₄^{−1/2} statt e gezählt; dann muss die Fehlerwahrscheinlichkeit ≤ c η\_b^{3/2}/(w − 1) sein, und der Beweis bleibt sonst gleich (Anhang F, F.11.3, mit p₄ dort).
- **Gebiete:** Ω\_b = {x : d(x, U) < (2h\_b + 4)s} mit Dirichlet-Rand (periodisch, falls Ω\_b der ganze Torus ist), Abschneidefunktion 0 ≤ p\_b ≤ 1, gleich 1 für d(x, U) ≤ 2h\_b s, 0 ab (2h\_b + 2)s, |∇p\_b| ≤ C/s. In 2D ist |Ω\_b| ≤ C h\_b² |U|.
- **Zählgröße:** J\_U^{fail} zählt die Stücke mit Ende in U, die in einem Fach fehlerhaft sind.

### 10.1 Aussage

**Satz T2 [S, gegeben die Eingänge in 10.7].** Es gibt c₁ > 1, κ > 0 und C, unabhängig von D, A und ζ, sodass für jede Zellvereinigung U

```text
log E exp( J_U^fail )  ≤  C C_a ρ |U| · Σ_b η_b h_b²
```

Dabei wirkt der Erwartungswert unter dem Grundzustands-Pfadmaß einer Scheibe. Für mehrere Scheiben gilt die Summe der Ein-Scheiben-Schranken (10.4). Die Bedingungen an die Fächer sind δ M\_b ≥ 2δμ̄ mit δM\_b = log(1/η\_b)/2, also

```text
D² ≳ 32πK/κ,        c(A) ln τ ≳ 32πK,        log(1/η_{G4}) ≳ 32πK,        κ r_∗ ≳ 32πK
```

Alle sind feste Bedingungen bei festem K; die zweite und die dritte verlangen ρ klein genug (die dritte: ln ln(1/ρ) ≳ 96πK/(C\_β/71 − 1)).

### 10.2 Schritt 1: Kern eines fehlerhaften Stücks

K\_b(E, S) = p\_δ(S, E) · P\_{S→E}(Fehler im Fach b) ist der freie Kern der Stücke von S nach E, die im Fach b fehlerhaft sind. Behauptung:

```text
K_b(E, S)  ≤  (e − 1)^{−1} η_b e^{−δM_b} · p_b(E) p_b(S) · [e^{c₁δΔ_{Ω_b}}](E, S)
```

- **Makro-Fach j.** Ist |S − E| > h\_j s/2, so vergleicht man Gauß-Kerne. Auf dem Gitter gilt p\_δ(d) ≤ (C/δ) e^{−c|d|²/δ} und p\_{c₁δ}(d) ≥ (c/δ) e^{−C|d|²/(c₁δ)} im diffusiven Bereich |d| ≤ δ. Mit c₁ ≥ 2C/c folgt p\_δ(d) ≤ C e^{−c h\_j²/8} p\_{c₁δ}(d). Für |d| ≥ δ fallen Gitterkerne schneller (Poisson-Bereich), das hilft nur. Ist |S − E| ≤ h\_j s/2, so muss die Brückenschwankung ≥ h\_j s/2 sein, mit Wahrscheinlichkeit ≤ C e^{−ch\_j²}, und p\_δ ≤ C p\_{c₁δ}.
- **Fächer ∗, R2, G4.** Dort ist |S − E| ≤ Ds, also p\_δ ≤ C p\_{c₁δ}. Die Fehlerwahrscheinlichkeit der Brücke ist höchstens C-mal die der freien Irrfahrt: auf [0, δ/2] vorwärts, auf [δ/2, δ] rückwärts, mit beschränkter Dichte wie in Anhang P, Lemma P6, Schritt 2. Für die freie Irrfahrt sind die Fehler selten: Rand C e^{−cr\_∗}; R2 ≤ C δ τ^{−c(A)} nach Anhang P, P7 (Kalibrierung A ≈ 6–8); G4 ≤ 4N\_g e^{−β/71} nach Lemma F11a (Anhang F, F.11.3), mit N\_g = δ/t\_r Fenstern.
- **Lokalisierung (alle Fächer).** Für jedes beitragende Paar liegt die Strecke von S nach E im Abstand ≤ 2h\_b s von U. Eine Irrfahrt der Dauer c₁δ bleibt mit Wahrscheinlichkeit ≥ q\* > 0 im Schlauch der Breite s um diese Strecke, der in Ω\_b liegt. Also ist p\_{c₁δ}(S, E) ≤ q\*^{−1} [e^{c₁δΔ\_{Ω\_b}}](E, S). Auf dem Träger ist p\_b(E) = p\_b(S) = 1.
- **Konstanten.** Wählt man κ klein und D, r\_∗, A und C\_β groß, so wird der Vorfaktor ≤ (e − 1)^{−1} η\_b e^{−δM\_b} mit δM\_b = log(1/η\_b)/2.

### 10.3 Schritt 2: Gefärbter Operator und Majorisierung

- **Ein-Teilchen-Raum:** h̃ = ℓ²(Λ) ⊕ ⊕\_b ℓ²(Ω\_b), Grundfarbe und eine Farbe je Fach.
- **Einbettung:** ṽf = (f, (√η\_b p\_b f)\_b), Ṽ = ṽ^{⊗N}.
- **Gefärbter Hamilton-Operator ℋ:** Teilchen der Grundfarbe haben L\_i mit hartem Kern untereinander. Ein Teilchen der Farbe b hat −c₁Δ\_{Ω\_b} + M\_b und wechselwirkt mit niemandem.
- **T = Ṽ\* e^{−δℋ} Ṽ** majorisiert den getesteten Scheibenkern elementweise. Man entwickelt e^{J} = Π\_i (1 + (e − 1) 1{Stück i endet in U und ist fehlerhaft}) nach Teilmengen markierter Marken. Für eine feste Teilmenge lässt man alle Wechselwirkungen weg, an denen markierte Marken beteiligt sind; das vergrößert das nichtnegative Gewicht. Für jede markierte Marke zerlegt man in Fächer und wendet Schritt 1 an. Die Summe über alle Farbzuordnungen ist genau der Kern von T.

### 10.4 Schritt 3: Grundzustand statt Spur, und viele Scheiben

Unter dem stationären Pfadmaß ist E[F(Stücke der Scheibe)] = e^{δε\_N} ⟨ψ, K\_F ψ⟩ mit dem getesteten Kern K\_F ≥ 0. Weil ψ ≥ 0 und K\_{e^J} ≤ T elementweise,

```text
E e^{J}  ≤  e^{δε_N} ⟨ψ, T ψ⟩  ≤  e^{δε_N} ‖T‖
```

Für Scheiben k = 1, …, n mit Zählgrößen J\_k ist der Kern des ganzen Fensters das Produkt der Scheibenkerne, also E e^{Σ J\_k} ≤ e^{nδε\_N} ⟨ψ, T\_1 ⋯ T\_n ψ⟩ ≤ Π\_k e^{δε\_N} ‖T\_k‖. Das ist die Normform, die Satz D in §9 braucht.

### 10.5 Schritt 4: Lipschitz-Einschub auf dem Gitter

Mit a(x) = ½ log(1 + Σ\_b η\_b p\_b(x)²) und A = Σ\_i a(x\_i) ist Ṽ = e^A Ũ mit einer Isometrie Ũ, also T = Ũ\* X Ũ mit X = e^A e^{−δℋ} e^A und ‖T‖ ≤ ‖X‖.

**Lemma T3 (Gitter-Einschub) [S].**

```text
‖ e^A e^{−δℋ} e^A ‖  ≤  exp( −δ E₀(ℋ̃) ),        ℋ̃ = ℋ − Σ_i W₀(x_i),        W₀(x) = 2a(x)/δ + c₁ Σ_{y∼x} (cosh(a(x) − a(y)) − 1)
```

*Beweis.* Für 0 ≤ t ≤ δ sei U\_t = e^{f(t)A} e^{−tℋ} e^A mit f(t) = −1 + 2t/δ, also U₀ = 1 und U\_δ = X. Für y(t) = U\_t v gilt y′ = (2A/δ) y − e^{fA} ℋ e^{−fA} y. Für den kinetischen Teil auf einer Kante (Sprung eines Teilchens, im Konfigurationsraum) gilt mit u = e^{fA}y, w = e^{−fA}y und Δa = a(x) − a(y):

```text
(u(x) − u(y)) (w(x) − w(y))  =  (y(x) − y(y))² − 2 y(x) y(y) (cosh(f Δa) − 1)
                             ≥  (y(x) − y(y))² − (y(x)² + y(y)²) (cosh(Δa) − 1)        (|f| ≤ 1)
```

Summiert über alle erlaubten Sprünge ergibt das ⟨u, ℋ\_kin w⟩ ≥ ⟨y, ℋ\_kin y⟩ − ⟨y, Σ\_i c\_i Σ\_{y∼x\_i}(cosh − 1) y⟩, mit c\_i ∈ {1, c₁}. Der harte Kern und die Farblücken sind diagonal und vertauschen mit e^{±fA}. Also ist ½ d/dt ‖y‖² ≤ −⟨y, ℋ̃ y⟩ ≤ −E₀(ℋ̃) ‖y‖², und Integration gibt ‖X‖ ≤ e^{−δE₀(ℋ̃)}. ∎

**Exakte Prüfung [N]** ([pruef\_lipschitz.py](pruef_lipschitz.py), harte Bosonen auf 4×4 bis 6×6, N = 2, 3, Gauß-Hügel a mit Höhe 0,2–2 und Breite 1–2, δ = 0,5, 2, 8): In allen 48 Fällen ist λ\_max(X) ≤ e^{−δE₀(ℋ̃)}. Für kleine a ist die Schranke scharf (Verhältnis 0,995–0,997 bei Höhe 0,2 und δ = 0,5).

### 10.6 Schritt 5: Energiebilanz

- **Potential:** a ≤ ½ Σ\_b η\_b p\_b², und Σ\_{y∼x}(cosh(Δa) − 1) ≤ C|∇a|² ≤ C Σ\_b η\_b |∇p\_b|². Mit |∇p\_b| ≤ C/s und s² = δ folgt 0 ≤ W₀ ≤ (C/δ) Σ\_b η\_b 1\_{Ω\_b}, und ‖W₀‖\_∞ ≤ C Σ\_b η\_b/δ ist klein gegen μ̄.
- **Sektoren:** Auf dem Sektor mit J Teilchen der Grundfarbe und k\_b Teilchen der Farbe b (J + Σ k\_b = N) ist

  ```text
  ℋ̃  ≥  E₀(ℒ_J − Σ W₀)  +  Σ_b k_b (M_b − ‖W₀‖_∞)
  ```

  denn markierte Teilchen haben kinetische Energie ≥ 0 (Dirichlet) und keine Wechselwirkung.
- **Grundfarbe:** E₀(ℒ\_J − ΣW₀) ≥ ε\_J − ∫₀¹ ⟨Σ\_i W₀(x\_i)⟩\_{J, −tW₀} dt (Hellmann–Feynman). Der Dichte-Eingang gibt ⟨n\_{Ω\_b}⟩\_{J,−tW₀} ≤ C\_a ρ |Ω\_b|, also ist der Verlust ≤ (C/δ) Σ\_b η\_b C\_a ρ |Ω\_b|.
- **Teilchenzahl:** ε\_J ≥ ε\_N − (N − J) μ̄, durch Teleskop.
- **Zusammen:** Mit M\_b ≥ μ̄ + ‖W₀‖\_∞ (Bedingung in 10.1) fallen die Sektorterme weg, und

  ```text
  δ ( ε_N − E₀(ℋ̃) )  ≤  C C_a ρ Σ_b η_b |Ω_b|  ≤  C C_a ρ |U| Σ_b η_b h_b²
  ```

Mit Schritt 3 und 4 folgt Satz T2. ∎

### 10.7 Eingänge und Stand

| Eingang                                                                | Stand                                                                                                                                             |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Gauß-Schranken des Gitterkerns, Brücken-Maximum, Schlauch              | [S] (Anhang K: (K1), (K2′) elementar seit 2026-11-13; davor bis auf die Bessel-Quotienten [Lit]; bis 2026-11-12: [Lit], Lawler–Limic Kap. 2)      |
| Seltenheit der Fehler R2, G4, ∗ für die freie Irrfahrt                 | R2: Lemma R (a) (Anhang K) [S]; G4: Lemma F11a (Anhang F) [S]; ∗: [S] mit τ₀ = r²/(440 r\_∗) und Lemma F11a (Anhang Z, Z.12; bis 2026-11-13: [B]) |
| Dichte-Eingang ⟨n\_B⟩\_{J,−W} ≤ C\_a ρ\|B\| für J ≤ N, schwaches W ≥ 0 | [S] (§11, Satz 3.9 (a^W))                                                                                                                         |
| Einfügeschranke μ̄ (Lemma 6.5 des Tutorials)                            | [S]                                                                                                                                               |
| Lemma T3 (Gitter-Einschub)                                             | [S], exakt geprüft                                                                                                                                |
| Majorisierung, Grundzustand, Energiebilanz                             | [S]                                                                                                                                               |

**Unterschied zu OA.**

- 2D: Der Faktor ist h\_b², nicht h\_b³.
- Grundzustand: E e^J ≤ e^{δε\_N}‖T‖ statt Spur und Hölder.
- Die markierten Farben kosten direkt ihre Lücke; die ideale Bose-Summe entfällt.
- Neu sind die Regularitäts-Fächer R2 und G4 für Anhang P und der Gitter-Einschub mit cosh statt |∇a|².

Damit ist Satz T2 bewiesen bis auf die Eingänge. Der wichtigste offene Eingang ist der Dichte-Eingang mit schwachem anziehendem Potential, gleichmäßig in der Teilchenzahl J ≤ N. Er ist eine Variante von Satz 3.9 (a) (§3), die man ohnehin für die Peierls-Schranke über mehrere Zeiten braucht (Tutorial §10, Punkt 3).

### 10.8 Besucher eines Kastens (Nachtrag 2026-11-13) [S, gegeben Satz T2]

*Anlass:* Anhang F, F.11.3, zweite Bemerkung, und Anhang M, Klausel (v). D7 verlangt (G2\_A) und (G4′) für *jede* Linie, die den Kasten 𝔎\_c vom Radius D\_K s in der Scheibe besucht. Satz T2 und Satz F11 zählen Stücke nach ihrem Ende. Ein Stück mit Makro-Fehler kann 𝔎\_c besuchen und weit entfernt enden; in Satz T2 fällt es dann ins Makro-Fach, dessen Kleinheit e^{−κD\_j²} nicht mit ρ verschwindet.

**Befund: Fächer nach der Reiseweite reichen nicht.** Für eine einzelne Zelle genügt es, Besucher nach der Reiseweite in Fächer mit eigenen Gebieten zu teilen. Die erwartete Zahl irregulärer Besucher ist dann ≤ C(D\_K) m p\_irr → 0 (p\_irr aus Anhang M, Lemma M2). Für die *gemeinsame* Seltenheit, die Satz D braucht, reicht das nicht. Eine einzige irreguläre Linie, die in ihrer Scheibe v Zellen besucht, macht bis zu (2D\_K + 1)² v Zellen D7-defekt. Kostet ein solcher Weg nur e^{−cv} (etwa über die Reichweite √v), so ist die Rate je Zelle e^{−c/(2D\_K+1)²}. Sie ist fest und geht nicht gegen 0. Eine Peierls-Schranke mit kleinem q verlangt deshalb einen *überlinearen* Schwanz für die Zahl der besuchten Zellen (Lemma T4), und zwar punktweise im Brückenkern (Lemma T5). Der Vergleich über die Halbbrücken-Dichte (W1) reicht dafür nicht, weil sein Faktor e^{λ²/4} den Schwanz auffrisst; Cauchy–Schwarz zur halben Zeit vermeidet ihn.

**Lemma T4 (Zahl der besuchten Zellen) [S, gegeben Lemma F11a].** Sei N die Zahl der Zellen (Seite s), die die Irrfahrt mit Rate 1 je Nachbar in der Zeit δ = s² besucht. Dann gilt

```text
P( N ≥ v )  ≤  C exp( −0,2 (v/9 − 1)² )
```

*Beweis.*

1. **Ausgänge.** τ₁ sei die erste Zeit, zu der die Irrfahrt den ℓ∞-Ball vom Radius s um ihren Startpunkt verlässt, τ₂ die entsprechende Zeit ab dort, und so fort. Nach der starken Markov-Eigenschaft sind die τ\_i unabhängig und gleich verteilt. Zwischen zwei Ausgängen bleibt die Bahn in einem Quadrat der Seite 2s, das höchstens 9 Zellen trifft. Mit N₁ = Zahl der Ausgänge bis δ ist also N ≤ 9(N₁ + 1).
2. **Kurze Ausgangszeiten sind selten.** Nach Lemma F11a ist P(τ ≤ u s²) ≤ 4 exp(−1/(4,4u)); für u < 1/(2,2 s) braucht die Bahn mindestens s Sprünge, was noch seltener ist. Mit u ↦ λu + 1/(4,4u) ≥ 2(λ/4,4)^{1/2} folgt E e^{−λτ/s²} ≤ C (1 + λ^{1/2}) e^{−0,953 λ^{1/2}}.
3. **Viele Ausgänge.** N₁ ≥ k heißt τ₁ + … + τ\_k ≤ s². Exponentielle Tschebyscheff-Ungleichung mit λ = (0,953 k/2)²: P(N₁ ≥ k) ≤ e^{λ} (C(1 + λ^{1/2}) e^{−0,953 λ^{1/2}})^k ≤ exp(−0,227 k² + k ln(Ck)) ≤ C e^{−0,2k²}. ∎

**Numerische Prüfung [N]** ([pruef\_besucher.py](pruef_besucher.py), Ausgaben in ergebnisse/pruef\_besucher\_s8.txt und \_s16.txt). Gemessen wird Q\_v = max\_d P₀(X\_δ = d, N ≥ v)/p\_{c₁δ}(d) mit exakt gezogenen Brücken (Verschiebung λs, λ ≤ 12, Achse und Diagonale; 2·10⁵ bzw. 5·10⁴ Brücken je Verschiebung; Start an der Zellecke, dem ungünstigsten Fall):

| v   | log Q\_v, s = 8, c₁ = 2 | log Q\_v, s = 16, c₁ = 2 | log Q\_v, s = 16, c₁ = 4 |
|-----|-------------------------|--------------------------|--------------------------|
| 10  | −1,25                   | −0,86                    | −0,69                    |
| 15  | −5,33                   | −4,36                    | −5,22                    |
| 20  | −11,3                   | −9,97                    | −12,6                    |
| 25  | −19,3                   | −17,5                    | −21,4                    |
| 30  | −28,3                   | −26,7                    | −35,0                    |

Der Abfall ist überlinear (etwa −0,03 v²) und hängt kaum von s ab. Das Maximum liefern Brücken mit großer Verschiebung: Sie besuchen etwa 2,5λ Zellen, und der Gauß-Faktor p\_δ/p\_{c₁δ} ≈ e^{−λ²(1−1/c₁)/4} gibt e^{−c v²}. Für v ≥ 26 liegt das Maximum am Rand λ = 12 des geprüften Bereichs; der Verlauf folgt dort der Gauß-Rechnung.

**Lemma T5 (punktweise Kernschranke) [S, gegeben (K1), (K2′), Lemma T4, Lemma R (a), Lemma F11a].** Sei c₁ ≥ 4 und |d|\_∞ ≤ δ. Mit N wie in Lemma T4 und „irr“ für eine Verletzung von (G2\_A) oder (G4′) gilt

```text
P₀( X_δ = d, N ≥ v )         ≤  119 c₁ · sup_x P_x( N ≥ v/2 )^{1/2} · p_{c₁δ}(d)
P₀( X_δ = d, irr )           ≤  C c₁ · p_irr^{1/2} · p_{c₁δ}(d)
P₀( X_δ = d, N ≥ v, irr )    ≤  C c₁ · ( p_irr · sup_x P_x(N ≥ v/2) )^{1/4} · p_{c₁δ}(d)
```

Dabei ist p\_irr die Wahrscheinlichkeit, dass die freie Irrfahrt auf einem Zeitstück der Länge 2δ/3 (G2\_A) oder (G4′) verletzt (Lemma R (a), Lemma F11a).

*Beweis.*

1. **Halbe Zeit.** Die besuchten Zellen sind die Vereinigung der in [0, δ/2] und der in [δ/2, δ] besuchten; aus N ≥ v folgt also N ≥ v/2 auf einer Hälfte. Für die erste Hälfte sei A das Ereignis und a\_y = P₀(X\_{δ/2} = y, A) ≤ p\_{δ/2}(y). Nach der Markov-Eigenschaft und Cauchy–Schwarz ist

   ```text
   P₀(X_δ = d, A)  =  Σ_y a_y p_{δ/2}(d − y)  ≤  (Σ_y a_y)^{1/2} (Σ_y p_{δ/2}(y) p_{δ/2}(d − y)²)^{1/2}  ≤  P(A)^{1/2} (1 + δ/2)^{−1/2} p_δ(d)^{1/2}
   ```

   denn max p\_{δ/2} ≤ (1 + δ/2)^{−1} nach (K1). Die zweite Hälfte gibt dasselbe mit Start in d, weil die Irrfahrt umkehrbar ist und die Umkehr die besuchten Zellen nicht ändert.
2. **Vergleich der Kerne.** Nach (K1) ist p\_δ(d)^{1/2} ≤ (1 + δ)^{−1/2} exp(−|d|²/(8(δ + |d|\_∞))) ≤ (1 + δ)^{−1/2} exp(−|d|²/(4c₁δ)), denn 8(δ + |d|\_∞) ≤ 16δ ≤ 4c₁δ. Nach (K2′) ist exp(−|d|²/(4c₁δ)) ≤ 4π e^{1/2} (1 + c₁δ) p\_{c₁δ}(d) (bis 2026-11-13 mit dem scharfen (K2) ohne e^{1/2}, daher dort 72 statt 119). Zusammen mit Schritt 1 und (1 + c₁δ)/((1 + δ/2)(1 + δ))^{1/2} ≤ 2^{1/2}·2c₁ folgt die erste Zeile.
3. **Irregularität.** Alle Testfenster von (G2\_A) und (G4′) sind kürzer als δ/3 (Horizonte ≤ τ ≪ δ, t\_r ≪ δ). Jede Verletzung liegt also ganz in [0, 2δ/3] oder ganz in [δ/3, δ]. Schritt 1 mit der Zeit 2δ/3 statt δ/2 gibt die zweite Zeile.
4. **Beides.** Das Minimum zweier Schranken ist höchstens ihr geometrisches Mittel. ∎

Für |d|\_∞ > δ ist p\_δ(d) Poisson-klein (Satz T2, Schritt 1); solche Stücke liegen in den Makro-Fächern.

**Satz T2′ (eigene Gebiete und Gewichte je Fach) [S, gegeben wie Satz T2].** Die Fächer b seien disjunkte Fehlerarten mit Reichweite h\_b, Gebiet U\_b (Zellvereinigung), Gewicht w\_b > 1 und Kleinheit η\_b, sodass für Ende E ∈ U\_b gilt: K\_b(E, S) ≤ (w\_b − 1)^{−1} η\_b e^{−δM\_b} p\_b(E) p\_b(S) [e^{c₁δΔ\_{Ω\_b}}](E, S) mit δM\_b = log(1/η\_b)/2 ≥ 2δμ̄; Ω\_b und p\_b werden aus U\_b gebildet wie in 10.0. J\_b zählt die Stücke mit Ende in U\_b, die im Fach b fehlerhaft sind. Dann ist

```text
log E Π_b w_b^{J_b}  ≤  C C_a ρ Σ_b η_b h_b² |U_b|
```

*Beweis.* Wörtlich Satz T2. In Schritt 2 trägt jedes markierte Stück des Fachs b den Faktor w\_b − 1 statt e − 1, den die Voraussetzung ausgleicht, wie beim Fach G4 (F.11.3). Die Gebiete Ω\_b, Abschneidefunktionen p\_b und die Kleinheiten sind schon in Satz T2 fachweise; mit U\_b statt U bleibt jeder Schritt gleich, und |Ω\_b| ≤ C h\_b² |U\_b|. ∎

**Folgerung T6 (Besucher) [S, gegeben Satz T2′, Lemma T5].** Sei C\_β ≥ 500. Dann gibt es q\_vis(ρ) → 0, sodass für jede Menge 𝒜 von Raum-Zeit-Zellen

```text
P( jede Zelle von 𝒜 hat einen Besucher, der (G2_A) oder (G4′) verletzt )  ≤  q_vis^{|𝒜| / (4 m_D²)}
```

*Beweis.*

1. **Ausdünnen** wie in Satz F10: 𝒜′ ⊆ 𝒜 mit |𝒜′| ≥ |𝒜|/(2m\_D)², je zwei Zellen derselben Scheibe mindestens m\_D Zellen auseinander.
2. **Fächer.** Fach i ≥ 0: irregulär und 2^i ≤ N < 2^{i+1}. Ein solches Stück besucht 𝔎\_c nur, wenn sein Ende in U\_i(c) liegt, den Zellen im Abstand ≤ D\_K + 2^{i+1} + 1 von Q\_c. Es besucht die Kästen von höchstens μ\_i = 2^{i+3} Zellen aus 𝒜′, denn jede besuchte Zelle liegt in den Kästen von höchstens vier m\_D-getrennten Zellen. U\_i ist die Vereinigung der U\_i(c), c ∈ 𝒜′, also |U\_i| ≤ |𝒜′| (2D\_K + 2^{i+2} + 3)² s².
3. **Markov.** T = Σ\_{c∈𝒜′} (Zahl der irregulären Besucher von 𝔎\_c) ist auf dem Ereignis ≥ |𝒜′| und ≤ Σ\_i μ\_i J\_i. Für t ≥ 1 ist also P ≤ e^{−t|𝒜′|} E Π\_i (e^{tμ\_i})^{J\_i}.
4. **Kleinheiten.** Nach Lemma T5 (dritte Zeile, mit Lemma T4) und der Lokalisierung aus Satz T2, Schritt 1, gilt die Voraussetzung von Satz T2′ mit w\_i = e^{tμ\_i}, h\_i = 2^{i+1} + 2 und η\_i = C (e^{t 2^{i+3}} c₁ (p\_irr e^{−0,2(2^i/36 − 1)²})^{1/4})^{2/3}. Der Gauß-Schwanz schlägt für jedes feste t das Gewicht. Also ist Σ\_i η\_i h\_i² |U\_i| ≤ |𝒜′| s² C(t, D\_K, c₁) p\_irr^{1/6}, und Satz T2′ gibt log E Π ≤ |𝒜′| m C′(t) p\_irr^{1/6}.
5. **Grenzwert.** p\_irr ist höchstens p₄ plus der Anteil von (G2\_A), eine Potenz von ρ. Nach F.11.3, Schritt 4, ist p₄ ≲ β (ln(1/ρ))^{1 − C\_β/71}; für C\_β ≥ 500 geht m p\_irr^{1/6} gegen 0. Man wählt t = t(ρ) → ∞ so langsam, dass m C′(t) p\_irr^{1/6} ≤ 1, und erhält q\_vis = e^{1 − t(ρ)} → 0. Die Bedingung δM\_i ≥ 2δμ̄ gilt, weil η\_i ≤ C(t) p\_irr^{1/6} → 0. ∎

*Stand:* D7 für Besucher eines Kastens ist damit [S, gegeben Satz T2], unter der Bedingung C\_β ≥ 500 (bisher 300). Der Grund geht in Satz D wie D6 und D7 mit dem Exponenten 1/(4m\_D²) ein.

## 11. Dichte-Eingang: Satz 3.9 (a) mit anziehendem Potential, gleichmäßig in der Teilchenzahl

Fassung 1, 2026-11-10 abends. Das ist der Eingang von Satz T2 (§10.6) und der Peierls-Schranke über viele Zeiten (Satz D, Grund D1; D6 läuft seit 2026-11-12 über Anhang F). Die Konstanten sind die aus §3, mit etwas mehr Spielraum.

### 11.1 Aussage

Für 0 ≤ J ≤ N und ein Potential 0 ≤ W ≤ w₀ auf den Plätzen sei H^W\_J = H\_J − Σ\_i W(x\_i), Ψ = Ψ^W\_J > 0 sein Grundzustand und ε^W\_J = E₀(H^W\_J) + 4J.

**Satz 3.9 (a^W) [S].** Seien b und s wie in §3, aber mit

```text
c_b ≥ 2μ̄,        s² ≥ 8 (C_L + C_K)/c_b,        w₀ ≤ c_b/8
```

Dann gilt für jede Zellvereinigung U, jedes 0 ≤ J ≤ N und 0 ≤ λ ≤ 1

```text
log E_Ψ e^{2λ n_φ}  ≤  2λ C_a ρ |U|,        insbesondere  E_Ψ n_B ≤ C_a ρ |B|  für jede Zellvereinigung B
```

mit demselben C\_a = 4C\_V/(ρb²) wie in §3. Dabei ist ρ = N/M die Dichte des vollen Systems; die Schranke hängt nicht von J ab.

### 11.2 Lemma 11.1: Einfügen mit anziehendem Potential

**Lemma 11.1 [S].** Für 1 ≤ k ≤ N und jedes W ≥ 0 gilt ε^W\_k − ε^W\_{k−1} ≤ 2ρ′D(f)/(1 − ρ′V(f)) mit ρ′ = (k − 1)/M, für jedes zulässige Profil f aus Lemma 6.5 des Tutorials. Insbesondere ist max\_{k ≤ N}(ε^W\_k − ε^W\_{k−1}) ≤ μ̄, mit der Schranke μ̄ ohne Potential.

*Beweis.* Wie Lemma 6.5, mit Ψ₀ = Ψ^W\_{k−1} ⊗ 1.

1. Ψ₀ ist Eigenvektor von ℒ^{(0)} − Σ\_{alt} W mit ℒ^{(0)} = ℒ\_{k−1} ⊗ 1 + 1 ⊗ L\_neu, zum Eigenwert ε^W\_{k−1}, denn L\_neu 1 = 0. Das Potential wirkt hier nur auf die alten Teilchen.
2. Die Kippidentität (Lemma 6.2) gilt für V − A mit beliebigem diagonalem V, also auch für dieses Operator-Paar. Mit F wie in Lemma 6.5 ist ⟨FΨ₀, (ℒ^{(0)} − Σ\_{alt}W) FΨ₀⟩ = ε^W\_{k−1} ‖FΨ₀‖² + 𝒩.
3. Auf Funktionen, die bei Stößen verschwinden, stimmt die Form von ℒ\_k mit der von ℒ^{(0)} überein. Der volle Operator ℒ\_k − Σ\_{alle} W hat zusätzlich −⟨FΨ₀, W(x\_neu) FΨ₀⟩ ≤ 0.
4. Die Schranken für 𝒩 und 𝒵 = ‖FΨ₀‖² in Lemma 6.5 benutzen nur, dass Ψ^W\_{k−1} normiert ist (Σ\_Kanten Ψ₀Ψ₀′ ≤ 2(k − 1), 𝒵 ≥ M − (k − 1)V). Also folgt ε^W\_k ≤ ε^W\_{k−1} + 𝒩/𝒵 wie dort. ∎

**Exakte Prüfung [N]** ([pruef\_einfuegen\_potential.py](pruef_einfuegen_potential.py), 6×6, k ≤ 5, Gauß-Mulde der Tiefe w₀ = 0,05 bis 3): Die Zuwächse sind mit Mulde stets kleiner als ohne und liegen unter 8ρ′/(1 − ρ′); bei w₀ = 3 werden sie sogar negativ (0,178 statt 0,717 bei k = 5).

### 11.3 Beweis von Satz 3.9 (a^W)

**Lemma A^W.** Für jeden normierten J-Teilchen-Hartkernzustand Φ gilt

```text
⟨Φ, H^W_J Φ⟩ − E₀(H^W_J)  ≥  ( c_b − μ̄ − w₀ − C_L/s² ) · E_Φ[n_φ]  −  C_V c_b |U| / b²
```

*Beweis.* Wie Lemma A (§1), mit drei Änderungen:

1. **Lokalisierung:** Das Potential ist diagonal und teilt sich in Innen- und Außenanteil; der Lokalisierungsfehler ist derselbe.
2. **Innen:** Jedes Innen-Teilchen hat zusätzlich −W ≥ −w₀, also E^{innen,W}\_j ≥ −4j − w₀ j + c\_b(j − #Kästen).
3. **Außen:** Mit Lemma 11.1 ist E₀(H^W\_{J−j}) ≥ E₀(H^W\_J) + 4j − jμ̄ (Teleskop über k ≤ J ≤ N). ∎

**Lemma B^W.** Lemma B gilt wörtlich für H^W\_J und Ψ, denn die Kippidentität verlangt nur V − A mit diagonalem V.

**Zusammen.** Mit Φ\_g = gΨ/‖gΨ‖, g = e^{λn\_φ}:

```text
( c_b − μ̄ − w₀ − (C_L + C_K)/s² ) E_g n_φ  ≤  C_V c_b |U| / b²
```

Nach den Bedingungen in 11.1 ist die Klammer ≥ c\_b − c\_b/2 − c\_b/8 − c\_b/8 = c\_b/4. Also E\_g n\_φ ≤ 4C\_V|U|/b² = C\_a ρ|U|, und Integration über λ gibt die Behauptung. J kommt nur über μ̄ (Maximum über k ≤ N) und über Lemma 11.1 vor; beides ist gleichmäßig. ∎

**Konstanten.** Gegenüber §3 verdoppelt sich die Bedingung an s²: K\_a ≈ 17 statt 8,7 (ρ → 0). Die Bedingung w₀ ≤ c\_b/8 ist in allen Anwendungen weit erfüllt. In Satz T2 ist w₀ ≤ C Σ\_b η\_b/δ, und w₀/c\_b ≈ C Σ\_b η\_b/(π H K) ≪ 1.

### 11.4 Folgerung: viele Zeiten

Für Satz D braucht man obere Schwänze der Teilchenzahl gemeinsam zu vielen Zeiten t\_1 < … < t\_n.

**Folgerung 11.2 [S].** Mit Abschneidefunktionen φ\_k zu Zellvereinigungen U\_k und 0 ≤ λ ≤ λ₀ (λ₀ klein gegen δ c\_b) gilt

```text
log E exp( Σ_k λ n_{φ_k}(t_k) )  ≤  Σ_k  C λ C_a ρ |U_k| · (1 + o(1))
```

*Beweis.* E[Π\_k e^{λn\_k(t\_k)}] = e^{(t\_n − t\_1)ε\_N} ⟨ψ, e^{A\_1} e^{−(t\_2−t\_1)ℒ} e^{A\_2} ⋯ e^{A\_n} ψ⟩ mit A\_k = λ n\_{φ\_k}. Man teilt jedes e^{A\_k} in zwei Hälften. Jedes Zwischenstück ist e^{A\_k/2} e^{−tℒ} e^{A\_{k+1}/2}; Cauchy–Schwarz gibt ‖e^{A/2} e^{−tℒ} e^{A′/2}‖ ≤ ‖e^{A/2} e^{−tℒ} e^{A/2}‖^{1/2} ‖e^{A′/2} e^{−tℒ} e^{A′/2}‖^{1/2}. Jeder Faktor ist nach Lemma T3 (§10.5) ≤ exp(−t E₀(ℒ − ΣW₀)) mit W₀ = λφ/t + O(λ²/s²) φ, und nach Satz 3.9 (a^W) mit Hellmann–Feynman ist ε\_N − E₀(ℒ − ΣW₀) ≤ (λ/t + Cλ²/s²) C\_a ρ|U|. Die beiden Ränder ψ e^{A\_1/2} und e^{A\_n/2} ψ schätzt man mit Satz 3.9 (a) zu einer Zeit ab. ∎

Für Zeitabstände t ≥ δ ist W₀ klein, wie verlangt. Das liefert den Grund D1 aus Satz D gemeinsam über Zeitgitter. (D6 in der früheren Fassung, Kreisscheiben unterhalb der Zellskala, liefert es nicht; dafür steht jetzt Satz F7 in Anhang F.)

### 11.5 Stand

| Teil                                 | Stand              |
|--------------------------------------|--------------------|
| Lemma 11.1 (Einfügen mit Potential)  | [S], exakt geprüft |
| Lemma A^W, Lemma B^W, Satz 3.9 (a^W) | [S]                |
| Folgerung 11.2 (viele Zeiten)        | [S], über Lemma T3 |
| Gleichmäßigkeit in J ≤ N             | [S]                |

Damit ist der Dichte-Eingang von Satz T2 bewiesen. In Satz D sind jetzt D1, D4, D5, D6 und D7 bis auf Einzelheiten bewiesen. Offen bleiben dort D2 (Isolation, Satz 3.9 c) und D3 (Scores, nach OA Lemma 7.1), beide als Skizze. Dazu kommen die unteren Schwänze (Satz 3.9 b) mit Zusatzpotential, falls man sie gemeinsam über viele Zeiten braucht.

## 12. Punkt 3 schließen: Scores, Isolation, untere Schwänze über viele Zeiten

Fassung 1, 2026-11-10 spät abends. Danach sind alle Defektgründe von Satz D (§9) behandelt.

### 12.1 Scores werden nicht gebraucht (D3 entfällt)

- **Wozu OA sie braucht.** OA (15) definiert Scores A^±, und OA (16) schätzt mit ihnen die erwartete Wechselwirkung einer freien Brücke mit festen Pfaden ab. Das ist der Eingang für Jensen in OA (29), die Untergrenze der Normierer. Anderswo kommen die Scores nicht vor (OA §10.4 benutzt sie nur „where (16) is needed“).
- **Was bei uns an ihre Stelle tritt.** Beim harten Kern ersetzt Anhang P die Jensen-Schranke: zugängliche Teilchen (Satz P3) und Lemma P5/P6 unter den Gütebedingungen (G1″), (G2\_A), (G4) (bis 2026-11-11: (G1)–(G3)). Diese sind die Defektgründe D5, D6, D7.
- **In 2D passten die OA-Scores ohnehin nicht.** Mit w(t) = min(1, 1/t) wächst die Gauß-Summe im Score wie ρ(1 + t), und der mittlere Score wird ≈ ρδ = m statt O(1).
- **Folge:** Die Score-Bedingung in der Wählbarkeit (Anhang G.5.1, Punkt 4) wird gestrichen; an ihre Stelle tritt die Güte der Zellumgebung (G1″), (G2\_A), (G4). D3 entfällt in Satz D.

### 12.2 Isolation (Satz 3.9 c, D2) [S]

**Zählgröße.** Für Kästen der Seite 2r mit Gitterversatz o ∈ {0, …, 2r − 1}² sei

```text
Q(η)  =  (2r)^{−2} Σ_o Σ_B (n_{B,o}(η) − 1)_+ ,        über die Kästen B des Gitters o in S
```

- **Nicht isolierte Teilchen.** Zwei Teilchen im Abstand ≤ r liegen für mindestens ein Viertel der Versätze im selben Kasten, und Σ\_B (n\_B − 1)\_+ ≥ ½ #{Teilchen, die ihren Kasten teilen}. Also ist N\_iso ≤ 8Q.
- **Glattheit.** Ein Sprung ändert n\_{B,o} nur für die Versätze, bei denen er eine Kastengrenze kreuzt, das ist ein Anteil 1/(2r). Also ist |ΔQ| ≤ 1/r je Sprung.

**Lemma A\_iso.** Für jeden normierten Zustand Φ gilt

```text
E(Φ) − E_N  ≥  λ_min(2r) · E_Φ[Q]  −  μ̄ · E_Φ[n_{S⁺}]  −  (C_L/s²) E_Φ[n_{S⁺}]
```

*Beweis.* Lokalisieren auf S wie Lemma A (§1); innen für jeden Versatz o Neumann-Kästen der Seite 2r und Lemma 3.3 für mehrere Teilchen in der Form ℒ ≥ λ\_min Σ\_B n\_B 1{n\_B ≥ 2} ≥ λ\_min Σ\_B (n\_B − 1)\_+. Mitteln über o. Außen gewinnt das Herausnehmen höchstens μ̄ je Teilchen. ∎

**Satz 3.9 (c) [S].** Mit λ₀ = c ζ/√ln(1/ρ) und C\_iso = 70 C\_a gilt

```text
log E e^{λ₀ Q}  ≤  λ₀ C_iso ζ² ρ |S|,        P(N_iso ≥ k′)  ≤  exp( λ₀ C_iso ζ² ρ|S| − λ₀ k′/8 )
```

*Beweis.*

1. **Kippen** mit g = e^{λQ}, λ ≤ λ₀. Wegen |ΔQ| ≤ 1/r kostet es nach Lemma B höchstens C λ² r^{−2} E\_g n\_{S⁺}. Mit λ ≤ λ₀ ist λ²/r² ≤ c²ζ²ρ/(ζ² ln(1/ρ)) ≪ μ̄.
2. **Lemma A\_iso** für Φ\_g gibt λ\_min(2r) E\_g Q ≤ (μ̄ + C\_L/s² + Cλ²/r²) E\_g n\_{S⁺}.
3. **Konstanten:** μ̄/λ\_min(2r) = 8πκ\_μ ρY · 2(2r)² ln(2r)/π = 64 κ\_μ ζ² · Y ln(2r) ≤ 33 κ\_μ ζ², denn Y ln(2r) → ½. Mit E\_g n\_{S⁺} ≤ C\_a ρ|S| (Satz 3.9 a für den gekippten Zustand, dessen Energie nach Schritt 1 nahe E\_N liegt) folgt E\_g Q ≤ C\_iso ζ² ρ|S|.
4. Integration über λ und Markov mit N\_iso ≤ 8Q. ∎

**Rate in Satz D.** Defekt durch Isolation heißt: mindestens der Anteil ε/4 der ≥ b₋m Stück-Enden einer Zelle ist nicht isoliert. Für u solche Zellen gibt der Satz die Schranke exp(−λ₀ m u (εb₋/32 − C\_iso ζ²)). Für ζ² < εb₋/(64 C\_iso) ist der Klammerausdruck positiv. λ₀ m = cζK √ln(1/ρ) → ∞, also geht die Rate gegen 0, wie Satz D verlangt. *Nachtrag 2026-11-12:* Für das Lochstück j₀ wird die Isolation zusätzlich getrennt gezählt, mit dem kleineren Anteil ε₁ = ε/(12 (2D + 3)²) ([anhang\_lochstueck.md](anhang_lochstueck.md), Klausel (iii)). Mit ε₁ statt ε/4 lautet der Klammerausdruck ε₁b₋/32 − C\_iso ζ², und die Bedingung wird ζ² ≤ εb₋/(768 (2D + 3)² C\_iso).

**Viele Zeiten.** Lemma T3 (§10.5) benutzt nirgends, dass A eine Summe über Teilchen ist; es gilt für jede Funktion A auf dem Konfigurationsraum. Mit A = λQ/2 entsteht das schwache Paarpotential W₀ = λQ/t + O(λ²/r²). Lemma A\_iso gilt mit diesem Zusatz, solange λ/t ≤ λ\_min(2r)/2; das Einfügen nach Lemma 11.1 wird durch ein anziehendes Paarpotential nur leichter. Wie in Folgerung 11.2 folgt die Schranke gemeinsam zu vielen Zeiten t\_k, t\_{k+1}, und genau dort braucht man Isolation.

### 12.3 Untere Schwänze über viele Zeiten (D1, zu wenige Teilchen) [S]

*Neue Fassung seit 2026-11-13 (Review W6). Beweise in [anhang\_einfuegen.md](anhang_einfuegen.md) (Anhang E).*

**Eingang** (Lemma E3). Für jeden Zustand Φ ist ε(Φ) − ε\_N ≥ A\_low − μ̄′ E\_Φ S\_U mit A\_low ≥ (c₁ρY)² ρ|U| (1 − 1/(ηm))/(64μ̄) und μ̄′ = μ̄ + 32π²/s². S\_U ist die glatte Innenzahl aus §4.

**Lemma 12.1 (abstoßendes Potential) [S].** Für θ ≥ 0 gilt E₀(ℒ + θ S\_U) − ε\_N ≥ min(θ, μ̄′) A\_low/μ̄′.

*Beweis.* Für jedes Φ ist ⟨Φ, (ℒ + θS\_U)Φ⟩ − ε\_N ≥ max(0, A\_low − μ̄′x) + θx mit x = E\_Φ S\_U; der erste Term ist ≥ 0, weil ε\_N die Grundenergie ist. Das Minimum über x ≥ 0 liegt bei x = A\_low/μ̄′, wenn θ ≤ μ̄′, sonst bei x = 0. ∎

**Folgerung 12.2 (= Folgerung E4) [S, gegeben Lemma T3 und Satz 3.9 (a^W)].** Für Zellvereinigungen U\_k zu Zeiten t\_k mit Abständen ≥ s²/1000 und 0 ≤ λ ≤ ½ gilt

```text
log E exp( −λ Σ_k S_{U_k}(t_k) )  ≤  −(λ/2) c₃″ ρ Σ_k |U_k|,        c₃″ = min(c₃′, c₃ − ε₃),        ε₃ = 580π⁴ C_a/(s⁴ μ̄′)
```

*Beweis* (Anhang E.5). Wie Folgerung 11.2, mit drei Änderungen. Die Kippung läuft über die glatte Zahl S\_U; dann sind die cosh-Terme von Lemma T3 je Teilchen O(λ²/s²) · w, bis auf einen Ringterm O(λ²/s⁴) n\_U, den Satz 3.9 (a^W) mit Hellmann–Feynman auffängt. Lemma T3 wird nur auf der Zeit δ\_T = λ/μ̄′ angewandt; der Rest e^{−(τ − δ\_T)ℒ} hat die Norm e^{−(τ − δ\_T)ε\_N}. Die Ränder schätzt Satz 3.9 (b) zu einer Zeit ab. ∎

Daraus folgt P(n\_Q < 2b₋m für alle (Q, k) ∈ 𝒜) ≤ e^{−b₋ m |𝒜|} mit λ = ½ und b₋ = c₃″/8.

*Frühere Fassung (bis 2026-11-12).* Eingang mit n\_U und A\_low = (c₁²/800) ρ²Y|U|; Lemma T3 mit A = −(λ/2) n\_U, wo ein Sprung über den Zellrand O(λ²) kostet und nicht O(λ²/s²); Lemma 12.1 ohne das Minimum mit μ̄′. Ergebnis war −λc₃″ρ Σ\_k |U\_k| (1 − o(1)) mit c₃″ ≈ c₁²/(6400πκ\_μ).

### 12.4 Stand von Satz D

| Grund                            | Stand                                                         |
|----------------------------------|---------------------------------------------------------------|
| D1 zu viele / zu wenige Teilchen | [S] (§11, Folgerung 11.2; §12.3, Folgerung 12.2 = Anhang E)   |
| D2 Isolation                     | [S] (§12.2)                                                   |
| D3 Scores                        | entfällt (§12.1)                                              |
| D4 Fehlgänger                    | [S] (Satz T2, T2′, §10 und §10.8), Gitterkern [S] (Anhang K)  |
| D5 Unzugänglichkeit              | [S] über Satz T2 (Anhang U, Satz U)                           |
| D6 zeitgemittelte Dichte (G1″)   | [S] (Anhang F: Satz F7, Satz F10)                             |
| D7 Regularität (G2), (G4)        | [S] über Satz T2; freie Irrfahrt: Lemma R (a), Lemma F11a [S] |
| Mischen, Übertragung auf µ\_ab   | [S] (§9.3, Anhang G.11.2)                                     |

*Nachtrag 2026-11-13:* Beide Eingänge sind geschlossen, der Gitterkern in Anhang K ((K1), (K2′) elementar), die Seltenheit der Regularitätsverletzung in Lemma R (a) und Lemma F11a. Satz D ist damit [S nach OA] ohne Literatur-Eingang. Frühere Fassung: **Damit ist Punkt 3 bis auf zwei Eingänge geschlossen:** die Standard-Schranken des Gitterkerns (Literatur) und die Seltenheit der Regularitätsverletzung für eine freie Irrfahrt (eine Aussage über eine einzelne Irrfahrt, numerisch kalibriert mit A ≈ 6–8).

*Nachtrag 2026-11-12.* D6 und der (G3)-Teil von D7 waren in der Fassung vom 2026-11-10 nicht gedeckt (Review K1): (G1) lebt unterhalb der Zellskala, und (G3) verlangte ein festes C₁. Beide sind ersetzt, durch (G1″) und (G4); die Seltenheit steht in Anhang F, Satz F10 und Satz F11. Die Raten dieser beiden Gründe gehen nur langsam gegen 0, und der Kasten des Defekts hat den Radius D\_K s mit großem D\_K. Die übrigen Befunde des Reviews zu §9–§12 sind davon nicht berührt. D5 war nur für feste Marken bewiesen (Review K2); die Fassung für die Stücke der Zellen, ohne zurückgehaltene Gruppe, steht in Anhang U. D2 und D4 zählen wegen des Lochstücks auch nach der Anfangszelle (Anhang L).
