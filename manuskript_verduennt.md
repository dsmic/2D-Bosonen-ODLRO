# Kondensat verdünnter harter Bosonen in 2D bei T = 0: Manuskript

> **Überholt (Vermerk 2026-11-13, Review H1).** Diese Fassung 1 beschreibt den Weg über die zeitartige Lücke mit Gegen-Lücke, G⁺ und Δ₂. Er ist seit Anhang G, G.10, durch die Zeitschleife ersetzt. Gültig ist die Zeitschleife: [tutorial\_beweis\_verduennt.md](tutorial_beweis_verduennt.md) §10, [anhang\_gegenluecke.md](anhang_gegenluecke.md) G.10 bis G.12, [anhang\_zweites\_moment.md](anhang_zweites_moment.md) (Anhang Z, Stand der Beweiskette in Z.12 und Z.13) und [anhang\_buchfuehrung.md](anhang_buchfuehrung.md) (Anhang M). Auch L₀ = 16 s(ρ) ist überholt (Anhang Z, Z.13).

Fassung 1, 2026-11-10. Geordnete Fassung des Beweisprogramms aus [einpunkt\_zeitroute.md](einpunkt_zeitroute.md) (§1–§30) und [beweisplan\_verduennt.md](beweisplan_verduennt.md). Kennzeichnung je Aussage: **[S]** bewiesen (Beweis hier), **[B]** Beweisskizze mit genauer Aussage, **[Lit]** aus der Literatur, **[N]** numerisch belegt. In Klammern stehen die Abschnitte des Arbeitsdokuments und die Skripte.

## 0. Überblick

**Hauptsatz (bedingt).** Es gibt ρ\* > 0 und c > 0 mit folgender Eigenschaft. Für harte Bosonen auf (ℤ/Lℤ)² mit Dichte ρ < ρ\* oder 1 − ρ < ρ\* gilt im Grundzustand N₀/N ≥ c, gleichmäßig in L ≥ L₀(ρ) = 16 s(ρ), s² = K ln(1/ρ)/ρ (Geltungsbereich und kleine Systeme: [tutorial\_beweis\_verduennt.md](tutorial_beweis_verduennt.md) §0.1; Fassung vom 2026-11-12, vorher „gleichmäßig in L“). Bewiesen ist das unter der Voraussetzung der mit [B] markierten Aussagen von §3–§6.

**Strategie in vier Sätzen.**

- Kondensat folgt, wenn das Bad um ein herausgenommenes Teilchen dem Grundzustand mit einem Teilchen weniger gleicht (§2). Das ist äquivalent dazu, dass eine beliebig lange Lücke in den Weltlinien nur O(1) kostet.
- Die Lücke wird längs einer zufälligen Route durch die Raum-Zeit ℤ² × ℤ ≅ ℤ³ getragen, mit exakt normierten lokalen Umbauten (§5).
- Im zweiten Moment entstehen Kosten nur dort, wo sich zwei unabhängige Routen begegnen. In ℤ³ gibt es nach Benjamini–Pemantle–Peres Routen mit beschränkten Begegnungen (§4).
- Die Kosten je Begegnung sind in 2D logarithmisch klein, ~ 1/ln(1/ρ) (§6). Dafür braucht man scharfe Energieschranken (§3).

**Abhängigkeiten.**

```text
§2 Einpunkt-Kriterium ──────────────────────────────────────────────► Hauptsatz
        ▲
§5 Staffellauf + Gegen-Lücke:  G⁻(T) ≥ a² / E[e^{θ J}]
        ▲                 ▲                        ▲
§4 Routen (Budget)    §6 Kreuzkosten (L2)      §3 Dichteschranken (L1)
                          ▲                        ▲
                     §3 Energieschranken: Dirichlet-Form, Kippen, Zelle, Dyson, Einfügen, Monotonie, Lokalisierung
```

## 1. Modell und Bezeichnungen

- Λ = (ℤ/Lℤ)², M = L², N Teilchen, ρ = N/M. Konfigurationen sind N-Teilmengen von Λ. H = −A mit A der Adjazenz des Konfigurationsgraphen (ein Teilchen springt zu einem freien Nachbarplatz, Gewicht 1). E\_N ist die Grundenergie, ψ\_N > 0 der Perron-Vektor, normiert.
- b\_x vernichtet ein Teilchen bei x (Hartkern-Bose-Operator), b₀ = M^{−1/2} Σ\_x b\_x, N₀ = ⟨ψ\_N, b₀⁺ b₀ ψ\_N⟩ die Besetzung von k = 0.
- **Markierte Fassung.** Markierte Konfigurationen sind (x₁, …, x\_N) mit paarweise verschiedenen x\_i. L\_i ist der Graph-Laplace-Operator des Gitters, wirkend auf die Koordinate i: (L\_i Φ)(x) = Σ\_{y ∼ x\_i} (Φ(x) − Φ(x\_{i→y})), mit Φ := 0 auf Stoßkonfigurationen (Dirichlet). K\_N = Σ\_i L\_i und ε\_N = E\_N + 4N.
- **Gitter-Streulänge** a = e^{−γ} 2^{−3/2} ≈ 0,1985: Der Potentialkern der einfachen Irrfahrt ist a(x) = (2/π) ln(|x|/a) + O(|x|^{−2}). Y = 1/ln(1/(ρa²)).
- **Weltlinien.** Die Dyson-Entwicklung von e^{−βH} gibt ein Maß auf Besetzungsgeschichten mit Gewicht 1 je Sprung (Lebesgue-Maß der Sprungzeiten). Im Grenzfall β → ∞ mit ψ\_N an den Enden ist das der stationäre Doob-Prozess mit Raten ψ\_N(η′)/ψ\_N(η), reversibel zu ψ\_N².

## 2. Reduktion auf das Einpunkt-Kriterium

**Lemma 2.1 (Einpunkt-Kriterium) [S].** Sei P\_x(S) = ψ\_N(S ∪ {x})²/ρ für (N−1)-Mengen S ∌ x (Palm-Maß des Bades) und Q = ψ\_{N−1}². Sei H̄ = Σ\_S √(P\_x(S) Q(S)), unabhängig von x. Dann gilt

```text
N₀/N ≥ H̄²,        ρ₁(x,y)/ρ ≥ 2H̄² − 1   für alle x ≠ y.
```

*Beweis.*
1. Σ\_{S ∌ x} ψ\_N(S ∪ x)² = ⟨n\_x⟩ = ρ, also ist P\_x normiert.
2. ⟨ψ\_{N−1}, b₀ψ\_N⟩ = M^{−1/2} Σ\_x Σ\_S ψ\_{N−1}(S) ψ\_N(S ∪ x) = M^{1/2} √ρ H̄ = √N H̄, wegen Translationsinvarianz der Perron-Vektoren.
3. Da ψ\_{N−1} ein Einheitsvektor ist, gilt |⟨ψ\_{N−1}, b₀ψ\_N⟩|² ≤ ‖b₀ψ\_N‖² = N₀.
4. Punktweise: a\_x(S) = ψ\_N(S ∪ x)/√ρ ist ein Einheitsvektor mit ⟨a\_x, a\_y⟩ = ρ₁(x,y)/ρ und ⟨a\_x, ψ\_{N−1}⟩ = H̄. Zerlegt man a\_x = H̄ψ\_{N−1} + √(1 − H̄²) e\_x mit e\_x ⟂ ψ\_{N−1}, folgt ⟨a\_x, a\_y⟩ ≥ H̄² − (1 − H̄²). ∎

**Lemma 2.2 (Lücken-Green-Funktion) [S].** G(τ) = ⟨b₀ψ\_N, e^{−τ(H\_{N−1} − E\_{N−1})} b₀ψ\_N⟩ ist vollständig monoton, mit G(0) = N₀ und G(τ) ↓ N H̄² für τ → ∞.

*Beweis.* Spektralzerlegung: G(τ) = Σ\_n |⟨n, b₀ψ\_N⟩|² e^{−τ(E\_n − E\_{N−1})}, jeder Summand ist nichtnegativ und fallend. Der Grundzustand des (N−1)-Sektors ist eindeutig (Perron), daher ist der Grenzwert |⟨ψ\_{N−1}, b₀ψ\_N⟩|² = N H̄². ∎

*Deutung.* G(τ)/N ist das Gewicht einer Lücke der Länge τ im Wurm (Kopf und Schwanz τ auseinander, über die Lage summiert). Eine untere Schranke für G(T) bei irgendeinem T ergibt N₀/N ≥ G(T)/N. Numerisch gilt Z₀ = N H̄²/N₀ ≈ 0,999 auf 4×4 bis 6×6 [N] (§2, einpunkt\_kriterium.py).

**Teilchen-Loch [S].** b ↔ b⁺ lässt H unverändert, und für x ≠ y ist ⟨b\_x⁺ b\_y⟩ gleich der entsprechenden Lochkorrelation. Der Fall 1 − ρ < ρ\* folgt also aus ρ < ρ\*.

## 3. Energieschranken und Dichtekontrolle

**Lemma 3.1 (harter Kern als Dirichlet-Bedingung) [S].** Auf markierten Hartkern-Konfigurationen ist K\_N = 4N − A\_N. Der Grundzustand von K\_N ist positiv und eindeutig (der markierte Konfigurationsgraph ist für N ≤ M − 2 auf dem 2D-Torus zusammenhängend), also symmetrisch. Insbesondere ist ε\_N = E\_N + 4N.

*Beweis.* (Σ\_i L\_i Φ)(c) = Σ\_i Σ\_{y∼x\_i} Φ(c) − Σ\_{erlaubte Sprünge} Φ(c′) = 4N Φ(c) − (AΦ)(c), weil Sprünge auf besetzte Plätze wegen Φ = 0 auf der Stoßmenge nur den Diagonalbeitrag liefern. ∎

**Lemma 3.2 (Kippidentität) [S].** K = κ − A mit symmetrischem A ≥ 0 elementweise, Kψ = Eψ und ψ > 0. Dann gilt für jedes reelle g

```text
⟨gψ, K gψ⟩ − E ‖gψ‖²  =  ½ Σ_{c,c′} A_{cc′} ψ(c) ψ(c′) (g(c) − g(c′))².
```

*Beweis.* Ausmultiplizieren und Σ\_{c′} A\_{cc′} ψ(c′) = (κ − E) ψ(c) verwenden. ∎

*Anwendungen:* Kippschranke für g = e^{λ n\_φ}, sie kostet ≤ C λ² s^{−2} E\_g n\_φ (§16.5). Einfügeschranke (Lemma 3.5).

**Lemma 3.3 (Zellenschranke) [S].** Q sei ein b×b-Kasten mit Neumann-Laplace L\_Q (nur innere Kanten) und y ∈ Q. Für f mit f(y) = 0 gilt

```text
⟨f, L_Q f⟩ ≥ ‖f‖² / (1/λ₂ + b² R_y),      λ₂ = 2 − 2cos(π/b),      R_y = effektiver Widerstand von y zur Gleichverteilung.
```

*Beweis.* ‖f‖² = ‖f − f̄‖² + b² f̄². Poincaré gibt ‖f − f̄‖² ≤ ⟨f, L\_Q f⟩/λ₂. Für jeden Einheitsfluss θ von y zur Gleichverteilung ist f̄ = f̄ − f(y) = ⟨θ, ∇f⟩. Cauchy–Schwarz und das Thomson-Prinzip geben f̄² ≤ R\_y ⟨f, L\_Q f⟩. ∎

*Zahlen [N]* (l1c\_widerstand.py): max\_y R\_y = R\_Ecke = (2/π) ln b − 0,1820 (b ≥ 32; −0,168 bei b = 4), dazu 1/(λ₂b²) ≤ 0,107. Also λ\_min ≥ π/(2b² ln b) für alle y und b ≥ 4. Exakt geprüft für b ≤ 512; für alle b fehlt die Standard-Asymptotik der Neumann-Green-Funktion mit Restglied.

*Mehrere Teilchen [S].* Neumann-Zerlegung (Kanten zwischen Kästen weglassen). Für ein Teilchen in einem Kasten mit n\_Q ≥ 2 verschwindet Φ als Funktion seiner Koordinate am Platz eines anderen, also gibt Lemma 3.3 für jedes Teilchen einzeln Σ\_i L\_i ≥ (π/(2b² ln b)) Σ\_Q n\_Q 1{n\_Q ≥ 2}. Fassung 1 paarte die Teilchen und verlor einen Faktor 3.

**Lemma 3.4 (diskretes Dyson-Lemma) [S].** B sei ein Gitterbereich, 0 ∈ B, S ⊂ B, θ der Einheitsstrom von 0 nach S (S geerdet, Einheitswiderstände), μ seine Austrittsverteilung auf S. Für f mit f(0) = 0 gilt

```text
Σ_{Kanten in B} (∇f)²  ≥  Σ_{y∈S} U(y) f(y)²,      U = μ / R_eff(0 ↔ S).
```

*Beweis.* Der Strom ist kreisfrei und zerfällt in ein Wahrscheinlichkeitsmaß auf Pfaden P von 0 nach S mit P(e ∈ P) = θ\_e. Cauchy–Schwarz längs P mit den Gewichten θ\_e gibt f(Ende)² ≤ (Σ\_{e∈P} (∇\_e f)²/θ\_e)(Σ\_{e∈P} θ\_e). Der zweite Faktor ist der Potentialabfall, für jeden Pfad gleich R\_eff. Mitteln über P ergibt die Behauptung. ∎

*Zahlen [N]* (l1\_dyson\_reff.py): Für die Schale „Abstand ≥ R“ ist R\_eff = (1/2π) ln(R/a) bis auf 0,04 % (R = 128) bzw. 2 % (R = 2). Das Gewicht 1/R\_eff ist also die Lieb–Yngvason-Konstante 2π/ln(R/a). Anders als im Kontinuum braucht man keine Sternförmigkeit.

**Lemma 3.5 (Einfügeschranke) [S].** Sei f: Λ → [0, 1] mit f(0) = 0 und gleichen Kantensummen in x- und y-Richtung, D(f) = Σ\_Kanten (∇f)², S(f) = Σ\_z (1 − f(z)²), ρ′ = (k−1)/M, ρ′ S(f) < 1. Dann gilt, auch mit beliebigem anziehendem Außenpotential −W ≤ 0:

```text
E_k − E_{k−1} + 4  ≤  2ρ′ D(f) / (1 − ρ′ S(f)).
```

*Beweis.*
1. Gelockerter Operator K\_rel = K\_{k−1} ⊗ 1 + 1 ⊗ L\_neu (neu–alt-Stöße erlaubt). Ψ₀ = ψ\_{k−1} ⊗ 1 erfüllt K\_rel Ψ₀ = ε\_{k−1} Ψ₀.
2. Versuchsfaktor F(η, x) = min\_j f(x − x\_j) (Dyson: nur der nächste Nachbar). FΨ₀ verschwindet auf neu–alt-Stößen, also ist ⟨FΨ₀, K\_k FΨ₀⟩ = ⟨FΨ₀, K\_rel FΨ₀⟩. Das Außenpotential auf dem neuen Teilchen ist ≤ 0 und darf entfallen.
3. Lemma 3.2 gibt ε\_k − ε\_{k−1} ≤ N/Z mit N = Σ\_Kanten Ψ₀Ψ₀′ (F − F′)² und Z = ‖FΨ₀‖².
4. Z ≥ M − (k−1) S(f), weil 1 − min\_j f\_j² ≤ Σ\_j (1 − f\_j²).
5. Sprünge des neuen Teilchens: |min a − min b| ≤ max|a − b|, also tragen sie ≤ (k−1) D(f) bei.
6. Sprünge des alten Teilchens j: Nur der j-te Term im Minimum ändert sich. Mit ψψ′ ≥ 0 und Σ\_Kanten ψψ′ ≤ 2(k−1) tragen sie ≤ (k−1) D(f) bei. ∎

*Auswertung [N]* (l1d\_schranke.py): Mit f\_R = min(1, a(z)/a\_R) ist die Schranke asymptotisch 8πρY(1 + O(ln ln/ln)), also Lieb–Yngvason-scharf. Verhältnis zu 8πρY: 1,79 (ρ = 10⁻¹), 1,36 (10⁻³), 1,16 (10⁻⁸). Die Born-Schranke 8ρ wäre um ln(1/ρa²)/π zu groß, und dieser Faktor würde den kleinen Parameter in §6 auffressen.

**Lemma 3.6 (Energie je Teilchen nichtfallend) [S].** ε\_{j−1}/(j−1) ≤ ε\_j/j.

*Beweis.* Sei Φ der j-Grundzustand und Φ(·, z) der bedingte (j−1)-Zustand bei festem Teilchen j an z. Jeder Kantenterm eines Sprungs auf z ist in beiden Systemen Φ², weil Φ dort verschwindet. Also ist Σ\_z ⟨Φ(·,z), K\_{j−1} Φ(·,z)⟩ = Σ\_{i<j} ⟨Φ, L\_i Φ⟩ = ((j−1)/j) ε\_j, und das ist ≥ ε\_{j−1}. ∎

**Lemma 3.7 (Lokalisierung mit zwei Farben) [S].** Sei p = cos θ, q = sin θ: Λ → [0, 1]. U färbt jedes Teilchen bei x mit Amplitude p(x) innen und q(x) außen. U ist eine Isometrie vom Hartkern-Raum in Hartkern ⊗ Hartkern, und

```text
⟨Φ, HΦ⟩ = ⟨UΦ, (H_innen + H_außen) UΦ⟩ − Σ_{η∼η′} Φ(η) Φ(η′) (1 − cos(θ_x − θ_y)).
```

Der Fehler ist ≤ 4 max(Δθ)² E\_Φ[n\_Übergang]. H\_innen + H\_außen erhält die Innen-Zahl j. Stöße zwischen den Farben zuzulassen senkt das Infimum, also ist der erste Term ≥ Σ\_j w\_j (E^{innen}\_j + E\_{N−j}).

*Beweis.* Matrixelemente direkt ausrechnen. Ein Sprung x → y erhält im Bild das Gewicht p\_x p\_y + q\_x q\_y = cos(θ\_x − θ\_y). Im Bild sitzen nie zwei Teilchen auf einem Platz. ∎

**Lemma 3.8 (Raum-Zeit-Exponentialmomente) [S].** Für das Grundzustands-Pfadmaß und diagonales, zeitabhängiges W\_t gilt

```text
log E_ψ[ exp ∫₀ᵀ W(η_t, t) dt ]  ≤  ∫₀ᵀ [ E₀(H) − E₀(H − W_t) ] dt.
```

*Beweis.* Feynman–Kac: Der Erwartungswert ist ⟨ψ, 𝒯 exp(−∫(H − E₀ − W\_t)) ψ⟩. Jeder Faktor e^{−dt(H − E₀ − W\_t)} hat die Norm e^{−dt(E₀(H − W\_t) − E₀)}. ∎

*Nutzen:* Mehrzeit-Peierls (§4) und untere Schwänze aus Einzeit-Schranken mit Außenpotential.

**Satz 3.9 (Dichteschranken L1) [B, (a) und (b) mit Konstanten ausgeschrieben in [satz\_3\_9\_dichteschranken.md](satz_3_9_dichteschranken.md)].** Für Vereinigungen U von Zellen der Seite s mit s² ≥ K ln(1/ρ)/ρ:

- (a) log E e^{λ n\_{φU}} ≤ C λ ρ |U| für 0 ≤ λ ≤ 1;
- (b) P(n\_Q < 2b₋ m für alle Q ⊂ U) ≤ C e^{−c m u};
- (c) Isolation: P(#nicht isoliert in S ≥ k′) ≤ exp(C λ₀ ζ² ρ|S| − λ₀ k′).

*Beweisweg.*
- (a): Lemmata 3.2, 3.3, 3.5, 3.7 wie in Lemma 4.2 der dichte-uniformen OpenAI-Arbeit, mit Ballungsdichte D₀ = Hρ, H ≈ 17–25.
- (b): Negative Kippung, dazu Lemma 3.6 mit der Energie-Untergrenze ε\_N ≥ (3π/16) ρN/ln(4/ρ) aus Lemma 3.3, und Lemma 3.5.
- (c): reservierte Ballungsenergie aus Lemma 3.3.

In allen Verhältnissen kürzt sich der Logarithmus, nur dank Lemma 3.5 (§16.6).

*Konstante [B + N]* (§28, satz\_3\_9\_dichteschranken.md): (a) braucht K ≈ 6–9, mit C\_a ≈ 2·10³–3·10³. (b) braucht mit der Untergrenze 3π/16 etwa K ~ 540. Mit exakten Kastenenergien (e\_b(2) → 4π/(b² ln b), l1\_kasten2.py) und linearer Paarung wird c₁ → π, also K ~ 100; mit Lieb–Yngvason (c₁ → 4π) K ~ 25.

**Satz 3.10 (Gitter-Lieb–Yngvason) [B, Kern S].** ε\_N/N ≥ 4πρY(1 − C Y^{1/5}). Zusammen mit Lemma 3.5 ist das in führender Ordnung scharf.

*Beweisweg* (§30):
1. Lemma 3.4 für jedes Teilchen in der Nachbarzelle seines nächsten Nachbarn. Strom in beliebig geformten Zellen genügt.
2. Neumann-Kästen mit Temple.
3. Konvexität bei der Verteilung auf die Kästen.

*Einschränkung [N]* (§30.1): Temple braucht n² ≪ ε ln(R/a) und ist bei erreichbaren Größen nicht anwendbar. Der Satz ist rein asymptotisch.

## 4. Routen in der Raum-Zeit

**Satz 4.1 (Skelette mit beschränkten Begegnungen) [Lit + N].** Im Zellgitter ℤ² × ℤ (Raum × Zeitscheiben) gibt es zufällige Routen von einer Zelle zu einer gleichverteilten Zielzelle. Zwei unabhängige Routen mit gleichen Endpunkten haben eine Begegnungszahl J mit E e^{θJ} ≤ C(θ) für θ < α\_max, gleichmäßig in der Länge.

- *Literatur:* Benjamini–Pemantle–Peres 1998 (orientierte Pfade in ℤ³), Häggström–Mossel 1998, Konstruktion wie in §8.1 der dichte-uniformen OpenAI-Arbeit.
- *Budget je Zellpaar [N]* (§11, §14, §19): α\_max ≈ 0,046 hart (β = ¼, A ≈ 16, Drift D ≈ 0). Mit weichen Abstandsgewichten und ohne Rauschen auf der kürzesten Skala ist α\_max ≈ 0,07 für die ganze Route und ≈ 0,11 im Inneren.
- *Zeitartige Routen dürfen steil sein* (D ≈ 0), weil G monoton ist (Lemma 2.2). Räumliche Routen dürfen das nicht.

**Lemma 4.2 (Umwege) [Lit + B].** Schlechte Zellen werden auf dem Außenrand ihrer Komponente umgangen (Timár: Außenränder sind über Diagonalnachbarn zusammenhängend). Die Peierls-Schranke über mehrere Zeiten folgt aus Lemma 3.8 und Satz 3.9 mit Außenpotential. Geteilte Umwege ändern das Budget nicht [N] (§17).

## 5. Der zeitartige Staffellauf

**Definition 5.1 (Konstruktion)** (§13). Zeitscheiben der Länge δ, Zellen der Seite s, je Scheibe ein Sternpfad c₀ = B\_k, …, c\_m = B\_{k+1} mit je einem wählbaren Teilchen j\_l in c\_l.

- Das Stück von j₀ wird gelöscht; das Loch steht am Boden bei S\_{j₀}.
- Für l = 1, …, m wird das Stück von j\_l aus dem exakt normierten bedingten Gesetz neu gezogen, als Brücke von S\_{j\_l} nach Y\_{j\_{l−1}}. Möglich ist das wegen der Raum-Zeit-Markov-Eigenschaft: Gegeben der Rand eines Raum-Zeit-Bereichs, ist das Innere gleichverteilt über die verträglichen Geschichten.
- Am Deckel fehlt Y\_{j\_m}, also ist das Loch eine Zelle weitergerückt.

Der Schwanz liegt in Scheibe 0, der Kopf nach T ~ L in einer gleichverteilten Zielzelle.

**Lemma 5.2 (gemeinsames Maß) [Lit].** Gibt es ν mit Masse m und ∫(dν/dP)² dP ≤ C\_P, ∫(dν/dQ)² dQ ≤ C\_Q, so ist die Affinität H(P, Q) ≥ m²/√(C\_P C\_Q). Hier: Masse ≥ a ⇒ G̃⁻(T) ≥ a²/∫ f² dμ.

**Satz 5.3 (Gegen-Lücken-Bilanz) [B]** (§10). Im zweiten Moment wird mit der Gegen-Lücke verglichen: der geschlossene Zustand plus eine zusätzliche Linie längs der zweiten Route. Fern von Begegnungen stehen sich bedingte Zustandssummen mit gleicher Teilchenzahl und gleichem Rand gegenüber und kürzen sich exakt. Es folgt

```text
a²  ≤  G⁻(T) G⁺(T) e^{−Δ₂ T} E[ e^{θ J} ],      Δ₂ = E₀(N+1) + E₀(N−1) − 2E₀(N) ≥ 0,      G⁺ ≤ 1,
```

also G⁻(T) ≥ a²/E[e^{θJ}], mit θ = log(1 + Kosten je Begegnung).

## 6. Kosten je Begegnung (L2)

**Lemma 6.1 (Verklebe-Identität) [S].** Zwei Stücke werden unabhängig auf „Ausweichen“ (A¹, A²) in derselben festen Umgebung bedingt. r\_i(x,t) = P(A^i | X^i\_t = x)/P(A^i) ist das Doob-Verhältnis. Dann gilt

```text
κ_L := E[L | A¹A²] / E[L]  =  E_w[r₁ r₂]  =  P_L(A¹ ∩ A²) / (P(A¹) P(A²)),
```

mit L der gemeinsamen Aufenthaltszeit, w der freien Treffpunktverteilung und P\_L dem mit L gewichteten Paargesetz. Der Beweis ist Umschreiben der Definitionen.

**Befunde [N]** (§21–§27):
- Worst-Case wäre κ ≤ 1/P(A)² ~ e^{4πK}. Exakt ist κ\_L = 1,2–2,4 und folgt ln κ\_L ≈ 0,27 m/ln s, also κ₂ ≈ e^{0,54K} (l2\_doob.py).
- Cauchy–Schwarz auf ein Stück verliert nur 0–8 %.
- κ\_q ist über die Umgebungen leicht-schwänzig (l2\_linear.py).
- Fallen jenseits ~ √δ sind irrelevant (l2\_lokal.py).
- ln κ ≈ Σ\_Fallen ln κ(Falle) im Mittel (l2\_additiv.py).
- Der Campbell-Exponent ist Φ ≈ 0,5 m/ln s (l2\_einefalle.py).
- Der Paarfehler D ist im Wesentlichen ein Paareffekt mit |u₂| ≤ 0,1 (l2\_paare.py).

**Satz 6.2 (scharfes L2) [B].** E\_Umg[κ\_q^p] ≤ exp(p c(p) m/ln s). Beweisweg:

1. **Lokalisierung (Harnack):** Nur Fallen in Reichweite √δ zählen [B].
2. **Zerlegung:** ln κ\_q = Σ\_j ln κ(γ\_j) + D. Mit Hölder zerfällt E κ in das Produkt über die Fallen und den Faktor E e^{qD}.
3. **Campbell [S, Lit]:** E[Π\_j f(γ\_j)] = exp(∫(f − 1) dν) für Poisson-Fallen.
4. **Eine Falle [B]:** ν ∫(κ₁ − 1) ist über Fangvolumina V, V₂ ausdrückbar (§26). Grob ≤ C(ζ) m/ln δ, weil V₂ ≤ V₁ und das 2D-Wiener-Würstchen E V ≈ 2πδ/ln δ hat.
5. **Paarfehler [B, Lit]:** Konzentration für Poisson-Funktionale (Wu, PTRF 118 (2000); Bachmann–Peccati, EJP 21 (2016)) mit kleinen Hinzufüge-Kosten D\_γ D.
6. **Vom Poisson-Feld zum Grundzustand [B]:** über Satz 3.9 und Lemma 3.8.

**Kosten je Begegnung.** (e^C − 1)/m + κ₂ · P\_δ mit P\_δ ≈ 1,23/(ln √δ + 2,1) (Bessel-Rechnung, l2\_treffen.py).

## 7. Zusammensetzen und Schwelle

Reihenfolge der Konstanten:

1. Skelett (β, A, D, R) ⇒ Budget α\_max.
2. Zellgeometrie s² = K ln(1/ρ)/ρ, Scheibe δ ~ s².
3. L1-Konstanten (H, K, ζ, b₋, b₊).
4. Wählbarkeit und Peierls.
5. Schwelle aus κ₂ P\_δ + (e^C − 1)/m < α\_max.

Mit κ₂ ≈ e^{0,54K} und P\_δ ~ 1/ln(1/ρ) gilt

```text
ln(1/ρ*)  ≈  e^{0,54 K} · C′ / α_max
```

Bei K ~ 25–100 (realistisch erreichbar, §28, §30.1; Zahlen in tutorial\_beweis\_verduennt.md §9.3) ist ρ\* doppelt exponentiell klein. Das reicht für den Existenzsatz, ist aber physikalisch bedeutungslos.

## 8. Offene Punkte und Stand

| Nr. | Punkt | Stand | Gewicht |
|-----|-------|-------|---------|
| 1 | Satz 3.9 vollständig mit Konstanten (obere und untere Schwänze, Isolation, mit Außenpotential) | [B] | Kern des verdünnten Teils |
| 2 | Satz 5.3 ausschreiben (Buchführung wie §9–§10 der dichte-uniformen Arbeit, Sternpfade, Auswahlgewichte) | [B] | lang, mechanisch |
| 3 | Satz 6.2: Harnack-Lokalisierung, Fangvolumen-Schranke, Poisson-Konzentration, Übergang zum Grundzustand | [B] | neu, mittel |
| 4 | Lemma 4.2: volle 3D-Umwege und Verwerfung großer Komponenten | [Lit/B] | Geometrie |
| 5 | **Skalen entkoppeln** (kleine Staffellaufzellen, große L1-Zellen), damit ρ\* nicht doppelt exponentiell klein ist | offen | **für eine vernünftige Schwelle entscheidend** |
| 6 | Satz 3.10 (Gitter-Lieb–Yngvason) mit Konstanten; eigenständig interessant | [B] | Nebenergebnis |

**Laufende Numerik** (Fertigmeldung ≈ 2026-11-10 21:45): Z₀ bei L = 16 und 32 aus G(τ) (scan\_gtau.py) und Lochkosten auf der Zellskala aus Leerwahrscheinlichkeiten (scan\_leer.py). Die Lochkosten entscheiden, ob das Feynman–Kac-Lochargument für Punkt 5 trägt.

## Anhang: Skripte

| Skript | prüft | Abschnitt |
|--------|-------|-----------|
| einpunkt\_kriterium.py | Lemma 2.1 scharf (Z₀ ≈ 0,999) | §2 |
| pruef\_gtau.py, scan\_gtau.py | Lemma 2.2 im Wurm | §3 |
| zellschranke\_punkt.py, l1c\_widerstand.py | Lemma 3.3 | §16.5 |
| l1d\_einfuegen.py, l1d\_schranke.py | Lemma 3.5 | §16.3–§16.4 |
| l1\_kastenenergie.py, l1\_kasten2.py | Kastenenergien, K | §28 |
| l1\_dyson\_reff.py, l1\_dyson\_kette.py | Lemma 3.4, Satz 3.10 | §29–§30.1 |
| l1\_loch.py, scan\_leer.py | Lochkosten | §29.1 |
| skelett\_begegnungen.py, skelett\_budget.py, skelett\_budget2.py, skelett\_umwege.py | Satz 4.1, Lemma 4.2 | §11, §14, §17, §19 |
| l2\_treffen.py, l2\_kappa.py, l2\_doob.py, l2\_linear.py, l2\_lokal.py, l2\_additiv.py, l2\_einefalle.py, l2\_paare.py | §6 | §18–§27 |
