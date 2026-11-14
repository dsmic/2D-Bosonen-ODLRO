# Prüfung: ChatGPT-Verlauf „ODLRO im Bose-Hubbard-Modell“ (2026-11-09)

Gegenstand: geteilter Verlauf (29 Nachrichten, über die JSON-Schnittstelle der Freigabe vollständig gelesen). Thema: ODLRO für harte Bosonen auf dem Quadratgitter, Übergang zu t-J mit d-Wellen-Paaroperator. Kennzeichnung wie in [stufe_a.md](stufe_a.md): [S], [Lit], [B], [N], [H], [L]. Rechnung: [zweipaar_graph/odlro_teilnahme_8x8.py](zweipaar_graph/odlro_teilnahme_8x8.py).

## Kurzurteil

- Die exakten Teile des Verlaufs stimmen: XY-Abbildung, Kommutatoridentität, zirkulante Dichtematrix, Fourierform von H, Sütős Varianzschranke. Keiner davon bringt ODLRO näher; sie formulieren das Ziel um.
- „Ansatz A“ (Nullmode und Energie) ist die Infrarotschranken-Methode von Dyson–Lieb–Simon / Kennedy–Lieb–Shastry, ohne ihren entscheidenden Baustein (Reflexionspositivität). Sie trägt bei halber Füllung (bewiesen) und sonst nicht; für Stufe A und t-J gar nicht.
- „Ansatz B“ (Sütő, Harnack für Fock-Amplituden) zielt auf eine punktweise Vergleichbarkeit, die viel zu stark und nach unseren exakten Zahlen falsch ist (Konstante 116 schon auf 8×8). Gebraucht wird nur eine gemittelte Aussage. Die lässt sich exakt formulieren und ist bei Stufe A numerisch sehr gut erfüllt (unten, Satz 1).
- Beim Übergang zu t-J mit d-Wellen-Paaroperator bleibt fast nichts: Positivität, Spinalgebra, Fourieridentität und Reflexionspositivität fallen weg. Was bleibt, ist genau der Weg über Stufe A.

## 1. Was im Verlauf stimmt und was nicht

| Aussage im Verlauf                                                          | Bewertung                                                                                                                                                                                 |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| γ\_xy = g(y−x) zirkulant, λ\_max ≥ Σ\_r g(r)                                | [S]. Bei positiven Amplituden ist g ≥ 0 und dann sogar λ\_max = n₀ (Perron-Frobenius für γ)                                                                                               |
| Gleichamplitudiger Zustand: ⟨b\_x†b\_y⟩ = N(M−N)/(M(M−1))                   | [S], nachgerechnet; n₀ = N(M−N+1)/M ≈ (1−ρ)N. Das ist der RK-Punkt der harten Bosonen, Gegenstück zu §10                                                                                  |
| XY-Abbildung, S⁺S⁻ = S² − (S^z)² + S^z                                      | [S]. Aber ⟨S²⟩ ≳ M² ist nur eine andere Schreibweise für ODLRO                                                                                                                            |
| Kennedy–Lieb–Shastry 1988, Kubo 1988                                        | [Lit] richtig zitiert: Grundzustandsordnung des XY-Modells, d ≥ 2, alle Spins. Für harte Bosonen heißt das ODLRO bei halber Füllung                                                      |
| H + 4JN = 2J Σ\_{k≠0} (2 − cos k\_x − cos k\_y) n\_k                        | [S], gilt für beliebige Operatoren b\_x (lineare Umformung), also auch hart. E₀ + 4JN ist aber extensiv, Θ(M), nicht klein: Die Hard-Core-Abstoßung hebt die Energie um einen Volumenterm |
| Var\_{P\_a}(B) ≤ 6λ (Sütő)                                                  | [S], nachgerechnet: E\_{P\_a}[B] = λ, E\_{P\_a}[AB] = λ², B² − 6B ≤ AB ≤ B² + 6B                                                                                                          |
| d\_G(X, X−x+y) = d\_Λ(x,y)                                                  | [S] für Punktbosonen (ununterscheidbar, Kette schieben). **Für Stufe A falsch:** ausgedehnte harte Paare müssen Nachbarn umordnen (Transportproblem §17, §26–28)                          |
| Wegzahlvergleich bei m = d\_G ⇒ a\_X/a\_Y = O(1)                            | [H], vom Verlauf selbst als Lücke benannt. Zusätzlich: Die Schranke benutzt nur Grade, nicht den Grundzustand; sie kann den Grenzwert m → ∞ nicht kontrollieren                            |
| „b₀ ist kein Zirkelschluss“                                                 | ⟨b₀†b₀⟩ ≥ cN *ist* die Definition (bei Translationsinvarianz). Kein Zirkel, aber auch kein Fortschritt; der Einwand im Verlauf war berechtigt                                             |

## 2. Ansatz A ist die Infrarotschranken-Methode

- Ziel im Verlauf: Σ\_{k≠0} n\_k ≤ (1−δ)N aus „Grundzustand + Hard-Core-Bedingung“. Genau das leistet die Methode von Dyson–Lieb–Simon, in d = 2 bei T = 0 Kennedy–Lieb–Shastry:
  1. Summenregel: (1/M) Σ\_k ⟨S^x\_{−k}S^x\_k⟩ = ⟨(S^x\_0)²⟩ = ¼ (Spin ½, exakt). Das ist die „Hard-Core-Bedingung“.
  2. Infrarotschranke: ĝ(k) ≤ ½ √(c(k)/ε(k)), c(k) = ⟨[S^x\_{−k},[H,S^x\_k]]⟩, aus Gaußscher Dominanz.
  3. Bleibt (1/M) Σ\_{k≠0} der Schranke < ¼, so trägt k = 0 einen makroskopischen Anteil.
- Schritt 2 braucht **Reflexionspositivität**. Sie gilt für das XY-Modell; ein Feld h Σ S^z (Füllung ≠ ½) gibt im Doppelkommutator einen k-unabhängigen Beitrag h⟨S^z⟩, und die Abschätzung schließt nicht mehr. Aizenman–Lieb–Seiringer–Solovej–Yngvason (2004) beschränken sich ausdrücklich auf halbe Füllung, „dictated by our method of proof“ [Lit]. Für ρ ≠ ½ ist BEC harter Bosonen auf ℤ² meines Wissens offen.
- **Für Stufe A:** Die Fourieridentität gilt dort auch, mit den projizierten Paaroperatoren auf dem Mittelgitter: H\_A − (ε₀ − 4t\_c)P = t\_c Σ\_{k≠0} (4 − ε(k)) n\_k mit ε(k) = 4 cos(k\_x/2) cos(k\_y/2). Zusammen mit der RK-Schranke E₀ ≤ (ε₀ − 4t\_c)P + t\_c⟨B⟩\_gleich ist das **genau Satz §9** (Nachbarkohärenz ≥ 1,78 je Paar bei 7/8), nicht ODLRO. Das Infrarotproblem (kleine k ≠ 0 kosten fast keine Energie) bleibt. Reflexionspositivität für Eckschritte mit Ausschlusszone 22 bei ρ\_b = 1/32 ist nicht in Sicht.

## 3. Was Ansatz B wirklich braucht: Teilnahmezahl statt Harnack

**Satz 1 [S, Identität].** Stufe A, d-Eichung, Zustand ψ ≥ 0 im Modellraum, P Paare, 2N Bindungen. Für eine Konfiguration E aus P−1 Paaren sei G\_E die Menge der freien Plätze für ein weiteres Paar, φ\_E(b) = ψ(E ∪ b) die bedingte Ein-Paar-Wellenfunktion und

```text
S_E = Σ_{b∈G_E} φ_E(b),   w_E = Σ_{b∈G_E} φ_E(b)²,   F_E = S_E² / (|G_E| w_E) ∈ (0, 1]
```

Dann gilt exakt Σ\_{b,b′} ρ₁(b,b′) = Σ\_E S\_E², also mit u = gleichförmige Mode und ⟨·⟩\_w = Mittel mit Gewicht w\_E/P (Σ\_E w\_E = P):

```text
N_0 = ⟨u|ρ_1|u⟩ = (1/2N) Σ_E F_E |G_E| w_E,      (1 − 23(P−1)/2N) ⟨F⟩_w  ≤  n_0 = N_0/P  ≤  ⟨F⟩_w
```

*Beweis.* ρ₁(b,b′) = Σ\_{D∋b′} ψ(D ∖ b′ ∪ b) ψ(D), und D ↦ E = D ∖ b′ ist eine Bijektion auf die E mit b′ ∈ G\_E. Summe über b,b′ gibt Σ\_E S\_E². Jedes D zerfällt auf P Arten in (E, b), also Σ\_E w\_E = P. Schließlich 2N − 23(P−1) ≤ |G\_E| ≤ 2N (§10). □

Bei Translationsinvarianz und ψ ≥ 0 ist N₀ = λ\_max(ρ₁). **ODLRO ⇔ lim inf ⟨F⟩\_w > 0** (für ρ\_b < 1/23): Die Wellenfunktion *eines* Paares bei festgehaltener Umgebung muss über einen positiven Anteil ihres freien Raums ausgebreitet sein, im quadratischen Mittel und gewichtet, nicht punktweise. Am RK-Punkt ist F ≡ 1, das ist §10.

Bemerkungen:

- Der Verlauf sucht a\_{X−x+y} ≥ c a\_X für fast alle Transfers. Das ist eine L^∞-Aussage. Sie impliziert F ≥ c², ist aber viel stärker als nötig. Mit φ = Mittel·(1 + η) gilt F = 1/(1 + Var η): Es genügt eine **beschränkte relative Varianz** der bedingten Amplitude.
- Die globale Variante ist wertlos: Cauchy–Schwarz über E gibt n₀ ≥ R⟨|G|⟩/2N mit R = (Σψ)²/(|𝒞| Σψ²). Für einen Zustand aus lokalen Faktoren (Jastrow) fällt R aber exponentiell in M. Der „gleichamplitudige Zustand“ im Verlauf entspricht R = 1. Nötig ist nur die bedingte, Ein-Paar-Version.
- Ein Kristall verletzt das Kriterium (φ\_E sitzt auf der Lücke, F ~ 1/M); ein Zustand aus kurzreichweitigen, beschränkten Faktoren (Jastrow mit f → 1) erfüllt es gleichmäßig in L. Das Kriterium trennt genau Suprafluid und Kristall.

**Exakt, 8×8-Torus (Grundzustand von H\_A, Lanczos, 3 075 264 Konfigurationen bei P = 4) [N]:**

| P       | n₀ (H\_A) | ⟨F⟩\_w | min\_E F\_E | ⟨\|G\_E\|⟩/2N | Harnack max/min auf G\_E: Median / 99 % / max | n₀ (RK) |
|---------|-----------|--------|-------------|---------------|-----------------------------------------------|---------|
| 2       | 0,752     | 0,917  | 0,917       | 0,820         | 4,7 / 4,7 / 4,7                               | 0,820   |
| 3       | 0,561     | 0,864  | 0,825       | 0,650         | 7,9 / 56 / 56                                 | 0,657   |
| 4 (7/8) | 0,357     | 0,728  | 0,648       | 0,489         | 21 / 79 / 116                                 | 0,512   |

- n₀ und E₀ stimmen mit der ED aus §8 überein (0,75 / 0,56 / 0,36).
- **Die punktweise Harnack-Konstante ist groß und wächst mit der Dichte, F bleibt in jeder einzelnen Umgebung ≥ 0,65.** Der Verlauf arbeitet also auf eine Ungleichung hin, die schon auf 8×8 nur mit Konstante ~100 gilt und im großen System (seltene dichte Gebiete) unbeschränkt sein dürfte. Die richtige Zielgröße ist ⟨F⟩\_w.
- Der Unterschied zu RK (0,512 gegen 0,357) zerfällt in ⟨F⟩ = 0,73 und einen um 5 % kleineren freien Raum (0,489 gegen 0,512; H\_A bevorzugt engere Packung).

## 4. Voraussetzungen, damit der Weg ODLRO trägt

| Voraussetzung                                          | harte Bosonen ℤ²     | Stufe A (H\_A)                                  | Stufe B / B+                    | t-J                                      |
|--------------------------------------------------------|----------------------|-------------------------------------------------|---------------------------------|------------------------------------------|
| stoquastisch (Positivität, Perron-Frobenius)           | ja                   | ja, d-Eichung (Satz A)                          | B: ja; B+: nein (§20)           | nein (Fermionvorzeichen)                 |
| ρ₁ ≥ 0, also λ\_max = n₀                               | ja                   | ja                                              | B: ja                           | nein                                     |
| Irreduzibilität                                        | ja                   | ℤ² und Box ja, Torus Hauptkomponente (§12)      | wie A                           | –                                        |
| Spin-½-Algebra (XY, S⁺S⁻-Identität)                    | ja                   | nein (Ausschlusszone 22, Mittelgitter)          | nein                            | nein (Paare überlappen)                  |
| Fourieridentität H = Σ ε(k) n\_k                       | ja                   | ja, projizierte Paaroperatoren (= §9)           | nein (Spin-Energie)             | nein (Ein-Elektron-Hüpfen)               |
| Reflexionspositivität + Infrarotschranke               | nur halbe Füllung    | nicht in Sicht                                  | nein                            | nein                                     |
| Teilnahmekriterium ⟨F⟩\_w ≥ c                          | sinnvoll, offen      | sinnvoll; [N] 0,73 auf 8×8; Beweis offen [L]    | B sinnvoll; B+ nicht definiert  | nicht definiert (Vorzeichen in S\_E)     |
| T > 0                                                  | kein ODLRO (KT)      | kein ODLRO (Koma–Tasaki, §13)                   | ebenso                          | ebenso (Koma–Tasaki)                     |

## 5. Was beim Übergang zu t-J mit d-Wellen-Paaroperator bleibt

- **Bleibt:** Definition (⟨Δ₀†Δ₀⟩ extensiv), Translationsstruktur, d-Wellen-Formfaktor, Koma–Tasaki bei T > 0.
- **Fällt weg:**
  - Positivität. Damit ist g(r) nicht mehr ≥ 0, n₀ nicht mehr automatisch λ\_max, und S\_E kann sich wegheben.
  - Die Spinalgebra. Bindungspaare überlappen; nur Yangs η-Paare auf einem Platz haben eine Pseudospin-Algebra, und die schließt t-J aus.
  - Die Fourieridentität. Die kinetische Energie ist Ein-Elektron-Hüpfen, keine Paarbewegung.
  - Die Reflexionspositivität.
- **Folge:** Der Weg zu einem Satz führt nur über die Reduktion t-J → Stufe A. Dort gilt das Bosonengerüst (Satz A) exakt. Offen ist dann Kriterium F für H\_A, dazu der Modellabstand A → t-J (§6).

## 6. Vorschlag

1. Zielaussage für Stufe A umstellen: nicht punktweise Harnack, sondern **⟨F\_E⟩\_w ≥ c gleichmäßig in L** (äquivalent zu ODLRO, Satz 1).
2. ~~Größere Systeme~~ erledigt (2026-11-09, stufe_a.md §32 Nachtrag): Im Jastrow-Zustand ist F bei festem R\_h in L konvergent (L bis 128), ⟨F⟩ ≈ 0,40–0,44 und n₀ ≈ 0,14–0,16 im energetisch guten Bereich; RK im Volumen n₀ = ρ\_b/z\* ∈ [0,395; 0,409]. Offen: F des wahren Grundzustands (Wurm, G(L/2) bei T → 0).
3. Beweisrichtung [H]: F ist eine Aussage über eine einzelne Paarposition bei festgehaltener Umgebung, also lokal. Ein Lemma „log ψ₀(E ∪ b) − log ψ₀(E ∪ b′) ist eine beschränkte Summe lokaler Beiträge um b und b′ plus ein Rest mit beschränktem zweitem Moment“ würde genügen. Das ist eine Clusterform von ψ₀, deutlich schwächer als die Harnack-Ungleichung des Verlaufs. Ob sie sich aus der Feynman–Kac-Darstellung von ψ₀ (Doob-Prozess, §14) gewinnen lässt, ist die eigentliche offene Frage.

## Quellen

- T. Kennedy, E. H. Lieb, B. S. Shastry, The XY model has long-range order for all spins and all dimensions greater than one, Phys. Rev. Lett. 61 (1988) 2582, [Princeton](https://collaborate.princeton.edu/en/publications/the-xy-model-has-long-range-order-for-all-spins-and-all-dimension/).
- K. Kubo, T. Kishi, Existence of long-range order in the XXZ model, Phys. Rev. Lett. 61 (1988) 2585, [APS](https://link.aps.org/doi/10.1103/PhysRevLett.61.2585).
- M. Aizenman, E. H. Lieb, R. Seiringer, J. P. Solovej, J. Yngvason, Bose–Einstein quantum phase transition in an optical lattice model, Phys. Rev. A 70 (2004) 023612, [arXiv:cond-mat/0403240](https://arxiv.org/abs/cond-mat/0403240).
- A. Sütő, Ground state of the hard-core Bose gas on lattice I, [arXiv:cond-mat/9905421](https://arxiv.org/abs/cond-mat/9905421); Nonuniform ground state …, [arXiv:cond-mat/0011334](https://arxiv.org/abs/cond-mat/0011334).
- B. Nachtergaele u. a., Quantum spin systems after DLS 1978, [arXiv:math-ph/0603017](https://arxiv.org/abs/math-ph/0603017) (Übersicht Reflexionspositivität).
