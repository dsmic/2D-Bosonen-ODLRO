# Anhang F: Dichteschranken unterhalb der Zellskala

Stand 2026-11-12 (F.7–F.10 am 2026-11-11 ergänzt; F.11 und F.12 am 2026-11-12 ausgeschrieben). Antwort auf Befund K1 in [review\_2026-11-11.md](review_2026-11-11.md). Gehört zu [anhang\_ausweichen.md](anhang_ausweichen.md) P.7 (Gütebedingungen (G1), (G3), Lemma P5, P6a) und zu [satz\_3\_9\_dichteschranken.md](satz_3_9_dichteschranken.md) §9 (Defektgründe D6, D7). Bezeichnungen wie in satz\_3\_9 §0–§3 und §11. Kennzeichnung: [S] bewiesen, [B] Beweisskizze, [N] numerisch. Die Ergebnisse sind am 2026-11-12 in Anhang P, satz\_3\_9 §9–§12, Anhang K, Z und G eingearbeitet (F.14, Punkt 5); die Beweise stehen hier.

## Auf einer Seite

- **Problem (K1).** Lemma P6a braucht, dass eine Irrfahrt im Teilintervall τ = θ ln(1/ρ)/ρ mit kleiner Wahrscheinlichkeit eine Linie trifft. Bisher sollte das aus (G1) (Dichte zur Startzeit) und (G3) (kein schnelles Heranlaufen) folgen. (G1) war auf der Skala √τ nicht durch Satz 3.9 (a) gedeckt (Zirkel zwischen C₀ und θ), und (G3) verlangte ein festes C₁, das die Regularitätsschranke nicht hergibt.
- **Ergebnis 1: Dichte unterhalb der Zelle (F.2–F.5).** Die Energiemethode reicht, wenn man zwei Kastengrößen benutzt: feine Kästen nur dort, wo gezählt wird, grobe in der Übergangszone der Lokalisierung. In einem Gebiet der Größe R = √τ ist die zertifizierbare Teilchenzahl von der Ordnung (C\_E θ)^{1/2} ln(1/ρ); sie wird mit θ klein gegen ln(1/ρ).
- **Ergebnis 2: Raum-Zeit (F.7, F.8).** Dieselbe Energieungleichung beschränkt direkt die Potentialenergie in einem anziehenden Zusatzpotential (Lemma F6). Mit Lemma 6.8 folgen Exponentialmomente für zeitgemittelte Teilchenzahlen, multiplikativ über beliebige Familien von Gebieten, Skalen und Zeitfenstern (Satz F7). Hölder über die Skalen ist nicht nötig.
- **Ergebnis 3: (G3) entfällt (F.9, F.10).** Der Zähler in Lemma P5 ist, über alle Linien summiert, die erwartete gemeinsame Aufenthaltszeit 𝔏(x) = ∫ Σ\_y p\_t(x, y) n\_y(t) dt. Das ist eine reine Dichtegröße in Raum-Zeit; die Bahnen einzelner Linien kommen nicht mehr vor. Unter der zeitgemittelten Dichtebedingung (G1″) und einer Kurzzeit-Bedingung (G4) ist 𝔏(x) ≤ [C\_𝔏 (C\_E θ)^{1/2} + ε\_fern(θ) + o(1)] ln(1/ρ) (Lemma F8, deterministisch und mit allen Konstanten; Folgerung F9).
- **Kein Zirkel, und b₀ entfällt.** P6a gibt ε\_P vor (über A), danach wählt man θ ≤ θ\_P = ε\_P²/(16 C\_𝔏² C\_E). C₀, C₁ und b₀ kommen nicht mehr vor. An die Stelle von b₀ tritt die Kurzzeit-Schwelle β(ρ) ~ ln ln(1/ρ). Sie geht nur in Terme der Ordnung o(ln(1/ρ)) und in die Defektraten ein; θ, n = K/θ und p\* hängen nicht von ρ ab, und σ\_ρ geht gegen 0.
- **Ergebnis 4: Seltenheit (F.11).** (G1″) ist gemeinsam über viele Zellen selten: Satz F7, nach Ausdünnen auf Zellen mit disjunkten Kästen (Satz F10). (G4) ist selten nach einer Doob-Schranke für die freie Irrfahrt und einem Fach in Satz T2 (Satz F11); es ersetzt das Fach R3. Für eine einzelne Linie geben (G4) und (G2\_A) allein P\_treff ≤ C ln ln(1/ρ)/ln(1/ρ) (Lemma F13).
- **Ergebnis 5: Lemma P6 neu (F.12).** Kurze Brücke, mittlerer Schritt und Hauptlemma sind mit (G1″), (G2\_A) und (G4) neu bewiesen, mit allen Konstanten. Neu ist, dass die Zwischenzeiten der Zerlegung zufällig gewählt werden: Die Zahl schlechter Zwischenpunkte wird dadurch ein Zeitmittel, und das beschränkt (G1″).
- **Preis.** Die Konstanten sind winzig: θ\_P ≈ 10⁻²⁶ ε\_P² (mit C\_𝔏 ≈ 2,4·10⁹), ζ² polynomial klein in n = K/θ mit Exponent um 117, und die Defektraten gehen nur sehr langsam gegen 0. Für den Existenzsatz ist das gleichgültig.
- **Offen** bleibt in K1 nichts Eigenes mehr. Geerbt ist: Satz F11 hängt an Satz T2 und dessen Eingängen (F.14). Die guten Endpunkte, die Lemma P6″ voraussetzt, liefert im Aufweg die Wählbarkeit über zwei Scheiben ([anhang\_lochstueck.md](anhang_lochstueck.md), Anhang L, Antwort auf Befund K3).

| Teil                                                                   | Stand                    | Prüfung                             |
|------------------------------------------------------------------------|--------------------------|-------------------------------------|
| Lemma F1 (zweiskalige Lokalisierung)                                   | [S]                      | pruef\_feinskala.py, exakt [N]      |
| Lemma F2 (Kippen auf der Skala R)                                      | [S]                      | pruef\_feinskala.py, exakt [N]      |
| Satz F3 (obere Schwänze zu einer Zeit, Gebiet der Größe R)             | [S]                      | folgt aus F1, F2                    |
| Folgerung F4 (viele Zeiten, punktweise)                                | [S, gegeben Lemma T3]    | –                                   |
| Lemma F6 (Potentialenergie, mehrere Gebiete, gemischte Skalen)         | [S]                      | pruef\_feinskala.py, exakt [N]      |
| Satz F7 (Raum-Zeit-Momente zeitgemittelter Zahlen)                     | [S]                      | Lemma 6.8 exakt [N]                 |
| Lemma P5 mit 𝔏 statt (G3)                                              | [S, gegeben (K2′)]       | pruef\_feinskala.py, exakt [N]      |
| Lemma F8 (deterministisch: 𝔏 klein bei kleiner zeitgemittelter Dichte) | [S]                      | pruef\_feinskala.py, Bausteine [N]  |
| Folgerung F9 (𝔏 ≤ ε\_P ln(1/ρ) für θ ≤ θ\_P)                           | [S, gegeben (G1″), (G4)] | –                                   |
| Satz F10 ((G1″) selten, gemeinsam über viele Zellen)                   | [S]                      | –                                   |
| Lemma F11a, Satz F11 ((G4) selten)                                     | [S, gegeben Satz T2]     | pruef\_feinskala.py, Doob exakt [N] |
| Lemma F13 (eine einzelne Linie, P\_treff)                              | [S, gegeben (K1), (K2′)] | –                                   |
| Lemma P6a″, P6b″, P6″ (Ausweichen mit den neuen Bedingungen)           | [S, gegeben (K1), (K2′)] | pruef\_feinskala.py, Bausteine [N]  |

## F.0 Was gebraucht wird

**Die Größe, auf die es ankommt.** Lemma P5 schätzt für eine Linie Y\_j die Treffwahrscheinlichkeit durch E[L\_j]/inf g\_j ab, mit der gemeinsamen Aufenthaltszeit L\_j = ∫₀^{2τ} 1{X\_t = Y\_j(t)} dt und dem Nenner g\_j(σ) = ∫₀^τ p\_u(Y\_j(σ), Y\_j(σ + u)) du ≥ c e^{−CA²} log₂(τ/A²) unter (G2\_A). Der Zähler ist E[L\_j] = ∫₀^{2τ} p\_t(x, Y\_j(t)) dt. Über die Linien summiert:

```text
P_x( Treffer in [0, τ] )  ≤  C_P · 𝔏(x) / log₂(τ/A²),        𝔏(x) = ∫_0^{2τ} Σ_y p_t(x, y) n_y(t) dt,        C_P = C e^{CA²}
```

Denn zu jeder Zeit sitzen die Linien auf verschiedenen Plätzen, also ist Σ\_j p\_t(x, Y\_j(t)) = Σ\_y p\_t(x, y) n\_y(t). Lemma P6a braucht P\_x(Treffer) ≤ 1/(4C\_b). Wegen log₂(τ/A²) ≈ ln(1/ρ)/ln 2 genügt

```text
𝔏(x)  ≤  ε_P ln(1/ρ),        ε_P = 1 / (4 ln 2 · C_b C_P) · (1 − o(1))
```

- **Bisher** wurde E[L\_j] je Linie durch den Anfangsabstand und die Zahl der schnellen Fenster abgeschätzt, E[L\_j] ≤ C(φ(d\_j²/τ) + B\_j(x)), und dann mit (G1) zur Startzeit summiert. Daher kamen (G3) und die Konstante C₁.
- **Typisch** ist 𝔏(x) ≈ ρ · 2τ = 2θ ln(1/ρ), also weit unter ε\_P ln(1/ρ), sobald θ klein ist. Es geht nur um die Zertifizierung: Ausnahmen müssen selten sein, und zwar multiplikativ über viele Zellen und Zeiten.
- **Satz 3.9 (a) reicht dafür nicht** (Review K1): Er kontrolliert nur Zellvereinigungen. Für ein Gebiet vom Radius √τ gibt er n ≤ C\_a K ln(1/ρ), unabhängig von θ.
- **Aufbau.** F.1–F.6 behandeln die Dichte zu einer festen Zeit, F.7–F.8 die Dichte in Raum-Zeit, F.9–F.10 die Anwendung auf 𝔏, F.11 die Seltenheit der Bedingungen, F.12 Lemma P6 mit den neuen Bedingungen.

## F.1 Rahmen

- **Wie bisher:** Torus Λ, N = ρM, ψ der Grundzustand, ε\_k = E\_k + 4k, μ̄ = max\_{k ≤ N}(ε\_k − ε\_{k−1}). c\_b = λ\_min(b) ist die Zellenschranke (Lemma 6.3), c\_b ≥ π/(2b² ln b). Die grobe Kastenseite b erfüllt c\_b ≥ 2μ̄, also 1/b² = Hρ. Die Lokalisierungsskala s erfüllt s² ≥ 8(C\_L + C\_K)/c\_b wie in satz\_3\_9 §11. Abstände sind ℓ∞-Abstände auf dem Torus.
- **Gebiet und Rampe:** V ⊂ Λ liegt in einem Quadrat der Seite R, R ≥ 8. χ(x) = clip(1 − d(x, V)/R, 0, 1) ist die Rampe der Breite R um V, n\_χ = Σ\_x χ(x) n\_x, und V″ = {x : d(x, V) ≤ R}. Es gilt 1\_V ≤ χ ≤ 1\_{V″}, und über eine Kante ändert sich χ um höchstens 1/R.
- **Feines Gebiet V⁺:** die Vereinigung der groben Kästen (eines festen b-Gitters), die V″ treffen. Seine Seite ist ≤ 3R + b + 1. V⁺ wird mit feinen Kästen der Seite b₁ gepflastert, b₁ teilt b.
- **Masken:** θ\_h(x) = (π/2) clip((d(x, V⁺) − 1 − hs)/s, 0, 1), p\_h = cos θ\_h. Also p\_h = 1 auf V⁺ und auf dessen Nachbarplätzen.
- **Abkürzung:** ℓ\_ρ = ln(1/ρ).

Zur Teilbarkeit (L Vielfaches von b, b Vielfaches von b₁) gilt dasselbe wie überall im Projekt (Review W7): Kästen mit Seiten in [b, 2b) ändern nur Konstanten.

## F.2 Lemma F1: zweiskalige Lokalisierung [S]

**Lemma F1.** Sei c\_b − μ̄ ≥ C\_L/s², s ≥ 2 und 3R + b + 1 ≤ 3s. Für jeden normierten N-Teilchen-Zustand Φ gilt

```text
E(Φ) − E_N  ≥  ( c_{b₁} − μ̄ ) · E_Φ[ n_{V⁺} ]  −  c_{b₁} |V⁺| / b₁²  −  c_b N_grob,        N_grob ≤ 53 (s/b + 2)²
```

Mit V⁺ = U und b₁ = b ist das Lemma A aus satz\_3\_9 §1, bis auf Konstanten. Neu ist nur, dass die beiden Kastengrößen getrennt sind.

*Beweis.*

1. **Lokalisieren.** Lemma 6.7 (zwei Farben) mit der Maske p\_h gibt E(Φ) = ⟨UΦ, (H\_innen + H\_außen) UΦ⟩ − F\_h mit F\_h = Σ Φ(η)Φ(η′)(1 − cos(θ\_x − θ\_y)) über die geordneten Sprünge. Wie in Lemma A ist F\_h ≤ (π²/(2s²)) E\_Φ[n\_{Z\_h⁺}], wobei Z\_h⁺ die Plätze sind, an denen ein Sprung die Maske ändert. Plätze in V⁺ gehören nie dazu, weil θ\_h auf V⁺ und seinen Nachbarn verschwindet.
2. **Innen.** Die Innen-Teilchen leben auf Ω\_h = {d(x, V⁺) < 1 + (h + 1)s}. Ω̃\_h sei die Vereinigung der groben Kästen, die Ω\_h treffen; ein größeres Gebiet senkt die Energie nur. Man zerlegt Ω̃\_h in die feinen Kästen von V⁺ und die groben Kästen außerhalb. Die Neumann-Zerlegung und Lemma 6.3 für mehrere Teilchen geben Σ\_i L\_i ≥ Σ\_Q λ\_min(b\_Q) n\_Q 1{n\_Q ≥ 2} ≥ Σ\_Q λ\_min(b\_Q)(n\_Q − 1). Also ist die Innen-Energie ≥ −4j + c\_{b₁}(n\_{V⁺} − |V⁺|/b₁²) + c\_b(j − n\_{V⁺} − #grob(h)), mit j der Zahl der Innen-Teilchen. In V⁺ sind alle Teilchen innen.
3. **Außen.** Wie in Lemma A: E\_{N−j} ≥ E\_N + 4j − jμ̄.
4. **Festes h.** Zusammen ist

   ```text
   E(Φ) − E_N  ≥  (c_{b₁} − μ̄) E n_{V⁺} + (c_b − μ̄) E[Σ_{x∉V⁺} p_h(x)² n_x] − c_{b₁}|V⁺|/b₁² − c_b #grob(h) − (π²/(2s²)) E n_{Z_h⁺}
   ```

5. **Mitteln über h** mit der Dichte e^{−h}. Mit φ⁺(x) = e^{−(d(x,V⁺) − 1)₊/s} ist ∫ p\_h(x)² e^{−h} dh ≥ φ⁺(x) und ∫ 1{x ∈ Z\_h⁺} e^{−h} dh ≤ (1 + 2/s) e^{1 + 1/s} φ⁺(x) ≤ 2e² φ⁺(x). Der Koeffizient jedes Teilchens außerhalb von V⁺ ist damit ≥ (c\_b − μ̄ − C\_L/s²) φ⁺(x) ≥ 0 und wird weggelassen. Ω\_h liegt in einem Quadrat der Seite ≤ (2h + 5)s + 2 und wird von höchstens (2h + 5)²(s/b + 2)² groben Kästen getroffen; ∫(2h + 5)² e^{−h} dh = 53. ∎

*Bild.* Wer in V⁺ sitzt, zahlt je überzähligem Teilchen die große Energie c\_{b₁} der feinen Kästen. Der Fehler der Lokalisierung fällt nur in der Übergangszone an und wird dort von den groben Kästen getragen. Er geht nur als Zahl der groben Kästen ein, also als fester Energiebetrag c\_b N\_grob, der nicht von V abhängt.

## F.3 Lemma F2: Kippen auf der Skala R [S]

**Lemma F2.** Für g = e^{λ n\_χ}, λ ≥ 0, und Φ\_g = gψ/‖gψ‖ gilt

```text
E(Φ_g) − E_N  ≤  C_T λ² R^{−2} E_g[ n_{V″} ],        C_T = 2 e^{2λ/R}  ≤  2 e^{1/4}   (λ ≤ 1, R ≥ 8)
```

*Beweis.* Die Kippidentität (Lemma 6.2) gibt E(Φ\_g) − E\_N = Σ\_Kanten ψψ′(g − g′)²/⟨g²⟩. Ein Sprung ändert n\_χ um |Δ| ≤ 1/R, und nur, wenn das springende Teilchen in V″ sitzt. Also ist (g − g′)² ≤ min(g, g′)² λ² R^{−2} e^{2λ/R}. Mit ψψ′ min(g, g′)² ≤ ½(ψ²g² + ψ′²g′²) und höchstens 4 Sprüngen je Teilchen folgt die Behauptung. ∎

Gegenüber Lemma B (C\_K = 16e, Profil der Breite s) ist nur die Breite des Profils anders. Die Kosten der Kippung sind λ²/R² je Teilchen in V″; das ist bei kleinem R viel, und deshalb braucht man die feinen Kästen.

## F.4 Satz F3: obere Schwänze in einem Gebiet der Größe R [S]

**Satz F3.** Unter den Voraussetzungen von Lemma F1 sei 0 < λ₀ ≤ 1 und b₁ so gewählt, dass

```text
c_{b₁}  ≥  2μ̄  +  2 C_T λ₀² / R²                                                        (∗)
```

Dann gilt für alle 0 ≤ λ ≤ λ₀

```text
log E_ψ e^{2λ n_χ}  ≤  2λ N_F,        N_F  =  2 |V⁺| / b₁²  +  2 c_b N_grob / c_{b₁}
P( n_V ≥ t )  ≤  exp( −2λ₀ (t − N_F) )
```

*Beweis.* Lemma F1 für Φ\_g und Lemma F2, mit V″ ⊂ V⁺: (c\_{b₁} − μ̄ − C\_T λ²/R²) E\_g n\_{V⁺} ≤ c\_{b₁}|V⁺|/b₁² + c\_b N\_grob. Nach (∗) ist die Klammer ≥ c\_{b₁}/2, also E\_g n\_{V⁺} ≤ N\_F. Die Ableitung von log E e^{2λn\_χ} nach λ ist 2E\_g n\_χ ≤ 2E\_g n\_{V⁺}. Integrieren und Markov mit n\_V ≤ n\_χ. ∎

**Mit Zusatzpotential [S].** Für 0 ≤ J ≤ N und ein Potential 0 ≤ W ≤ w₀ mit Träger in V⁺ gilt Lemma F1 für H^W\_J mit c\_{b₁} − μ̄ − w₀ statt c\_{b₁} − μ̄ (Beweis wie Lemma A^W in satz\_3\_9 §11.3, mit Lemma 11.1 für den Außenteil). Für den Grundzustand Ψ^W von H^W\_J ist die linke Seite null, also

```text
E_{Ψ^W}[ n_{V⁺} ]  ≤  N_F        sofern        μ̄ + w₀ ≤ c_{b₁}/2
```

Ebenso gilt Satz F3 für Ψ^W, wenn in (∗) rechts 2w₀ dazukommt.

## F.5 Zahlen: die Skala √τ und die Skalen darunter

**Bausteine** (führende Ordnung für ρ → 0):

| Größe | Wert                               | Herkunft                                                                 |
|-------|------------------------------------|--------------------------------------------------------------------------|
| C\_T  | 2e^{1/4} ≈ 2,57                    | Lemma F2                                                                 |
| C\_E  | 53πH²K, also c\_b N\_grob ≤ C\_E ρ | c\_b = πHρ/ln(1/(Hρ)), s²/b² = HK ℓ\_ρ; 8·10⁵ (H = 17, K = 17) bis 3·10⁷ |
| C\_g  | 20                                 | \|V⁺\|/b₁² ≤ C\_g γ θ ℓ\_ρ für R ≥ 8b, wenn γρ/ℓ\_ρ ≤ c\_{b₁} ≤ 5γρ/ℓ\_ρ |
| γ     | 16πκ\_μ + 2C\_T λ₀²/θ              | Bedingung (∗) mit R² = θ ℓ\_ρ/ρ, μ̄ = 8πκ\_μ ρ/ln(1/(ρa²))                |

s ist hier nur die Lokalisierungsskala des Lemmas. Man darf das kleinste zulässige s nehmen (K = 17 wie in satz\_3\_9 §11), unabhängig von der Zellseite des Staffellaufs; dann ist C\_E ≈ 8·10⁵ bei H = 17.

Der Fehler der groben Kästen ist C\_E ρ, ohne Logarithmus. Die Energie der feinen Kästen ist c\_{b₁} ≈ γρ/ℓ\_ρ je Teilchen. Ihr Quotient ist die Zahl der Teilchen, die man nicht ausschließen kann: (C\_E/γ) ℓ\_ρ. Das wird klein, wenn γ groß ist, und γ wird groß, wenn θ klein gegen λ₀² ist.

**Auf der Skala R² = θ ℓ\_ρ/ρ:**

```text
N_F  ≤  [ 32π κ_μ C_g θ  +  4 C_g C_T λ₀²  +  C_E θ / (C_T λ₀²) ] · ln(1/ρ)
```

**Folgerung (Wahl von θ).** Sei ε ≤ 1. Mit λ₀² = ε/(24 C\_g C\_T) und

```text
θ  ≤  θ_F(ε)  =  ε² / (144 C_g C_E)
```

ist jeder der drei Summanden ≤ ε/6, also N\_F ≤ (ε/2) ln(1/ρ) und

```text
P( n_V ≥ ε ln(1/ρ) )  ≤  ρ^{λ₀ ε},        λ₀ ε  =  ε^{3/2} / (24 C_g C_T)^{1/2}  ≈  ε^{3/2} / 35
```

| ε    | θ\_F(ε) bei C\_E = 8·10⁵ | λ₀    | Exponent λ₀ε |
|------|--------------------------|-------|--------------|
| 1    | 4·10⁻¹⁰                  | 0,029 | 3·10⁻²       |
| 0,1  | 4·10⁻¹²                  | 0,009 | 9·10⁻⁴       |
| 0,01 | 4·10⁻¹⁴                  | 0,003 | 3·10⁻⁵       |

Gültig, sobald √τ ≥ 8b ist, also ln(1/ρ) ≥ 64/(Hθ).

**Skalenform.** Optimiert man λ bei festem R (λ\_R² = (C\_E θ\_R)^{1/2}/(2 C\_T C\_g^{1/2}) mit θ\_R = ρR²/ℓ\_ρ), so ist für 8b ≤ R und λ\_R ≤ 1

```text
N_F(R)  ≤  c_R · R · (ρ ln(1/ρ))^{1/2},        c_R = 4,1 (C_g C_E)^{1/2}   (≈ 1,7·10⁴ bei C_E = 8·10⁵)
```

- Die zertifizierbare Zahl wächst linear in R, nicht wie die Fläche. Im Verhältnis zur erlaubten Zahl ε ln(1/ρ) ist sie bei R = √τ gleich c\_R √θ/ε.
- Für R < 8b benutzt man die Schranke zu R = 8b: N\_F ≤ 8 c\_R (ln(1/ρ)/H)^{1/2}. Das wächst wie (ln(1/ρ))^{1/2}.
- Die Schwänze: P(n ≥ 2N\_F(R)) ≤ exp(−2λ\_R N\_F(R)), und 2λ\_R N\_F(R) ist von der Ordnung (C\_E ρR²)^{3/4} (ln(1/ρ))^{1/4}. Schon bei R = 8b ist das ≥ c (C\_E/H)^{3/4} (ln(1/ρ))^{1/4}.

## F.6 Folgerung F4: viele Zeiten [S, gegeben Lemma T3]

**Folgerung F4.** Seien V\_1, …, V\_n Gebiete derselben Größe R zu Zeiten t\_1 < … < t\_n mit Abständen ≥ t₀, und b₁, λ₀ wie in Satz F3. Sei λ ≤ λ₀ mit

```text
w₀  :=  λ/t₀ + 0,51 λ²/R²  ≤  C_T λ₀² / R²
```

Dann gilt

```text
log E exp( Σ_k λ n_{χ_k}(t_k) )  ≤  Σ_k λ (1 + 0,51 λ t₀/R²) N_F
P( n_{V_k}(t_k) ≥ t  für alle k )  ≤  exp( −λ n (t − (1 + 0,51 λ t₀/R²) N_F) )
```

*Beweis.* Wie Folgerung 11.2.

1. E[Π\_k e^{λn\_{χ\_k}(t\_k)}] = ⟨ψ, e^{A\_1} P\_1 e^{A\_2} ⋯ P\_{n−1} e^{A\_n} ψ⟩ mit A\_k = λ n\_{χ\_k} und P\_k = e^{−(t\_{k+1} − t\_k)(ℒ − ε\_N)}. Ist ein Abstand größer als t₀, spaltet man einen Faktor der Norm 1 ab; es genügt also der Abstand t₀.
2. Jedes e^{A\_k} wird halbiert. Cauchy–Schwarz für Operatornormen gibt ‖e^{A/2} P e^{A′/2}‖ ≤ ‖e^{A/2} P e^{A/2}‖^{1/2} ‖e^{A′/2} P e^{A′/2}‖^{1/2}.
3. Lemma T3 mit a = λχ/2: ‖e^{A/2} e^{−t₀ℒ} e^{A/2}‖ ≤ exp(−t₀ E₀(ℒ − ΣW₀)) mit W₀ = λχ/t₀ + Σ\_{y∼x}(cosh(λ(χ(x) − χ(y))/2) − 1) ≤ w₀ 1\_{V″}.
4. Hellmann–Feynman und Satz F3 mit Zusatzpotential (μ̄ + w₀ ≤ c\_{b₁}/2 folgt aus (∗) und der Bedingung an w₀): ε\_N − E₀(ℒ − ΣW₀) ≤ w₀ N\_F.
5. Die Ränder ‖e^{A\_1/2}ψ‖ und ‖e^{A\_n/2}ψ‖ schätzt Satz F3 zu einer Zeit ab. ∎

**Für feste Zeitgitter** (wie in der Fassung von Lemma P6 vom 2026-11-10; Lemma P6″ in F.12 wählt die Zwischenzeiten zufällig und braucht diese Schranke nicht). Dort sind die Zeiten kτ/j mit j ≤ j₁ = λ₁² + 1, also t₀ = τ/j₁. Bei R = √τ erlaubt die Bedingung λ ≤ 2λ₀²/j₁. Mit N\_F ≤ (ε/2) ln(1/ρ) wie in F.5 ist dann

```text
P( n_{V_k}(t_k) ≥ ε ln(1/ρ)  für alle k = 1..n )  ≤  ρ^{0,45 λ ε n},        λ = 2 λ₀² / j₁
```

Die Schranke ist multiplikativ in der Zahl der (Gebiet, Zeit)-Paare. Das ist die Form, die Satz D braucht. Bei kleineren R ist t₀/R² größer, und λ = λ\_R ist erlaubt.

Folgerung F4 gibt Schranken zu einzelnen Zeitpunkten. Für das Folgende ist die zeitgemittelte Fassung in F.8 bequemer; sie braucht Lemma T3 nicht und verträgt gemischte Skalen.

## F.7 Lemma F6: Potentialenergie unter anziehendem Zusatzpotential [S]

Die Ungleichung aus Lemma F1 beschränkt nicht nur Teilchenzahlen. Im Grundzustand mit anziehendem Zusatzpotential beschränkt sie unmittelbar die Potentialenergie, und zwar für mehrere Gebiete mit verschiedenen Kastengrößen zugleich.

**Lemma F6.** Unter den Voraussetzungen von Lemma F1 an b und s sei W ≥ 0 ein Potential auf Λ, 0 ≤ J ≤ N, und seien V\_1⁺, …, V\_m⁺ paarweise disjunkte Gebiete wie in F.1 (jedes eine Vereinigung grober Kästen in einem Quadrat der Seite ≤ 3s). W verschwinde außerhalb ihrer Vereinigung. Jedes V\_i⁺ sei in Quadrate Q zerlegt mit

```text
λ_min(b_Q)  ≥  2μ̄  +  2 sup_Q W
```

Dann gilt für jedes v ∈ [0, 1] im Grundzustand Ψ von H\_J − v Σ\_i W(x\_i):

```text
E_Ψ[ n_W ]  ≤  Σ_Q λ_min(b_Q)  +  m · c_b N_grob,        n_W = Σ_x W(x) n_x,   N_grob ≤ 53 (s/b + 2)²
```

*Beweis.*

1. Man lokalisiert wie in Lemma F1 um V⁺ = ∪ V\_i⁺ und zerlegt innen in die Quadrate Q und grobe Kästen. Jedes Innen-Teilchen im Quadrat Q hat zusätzlich −vW ≥ −sup\_Q W. Für den Außenteil gilt E₀(H^{vW}\_{J−j}) ≥ E₀(H^{vW}\_J) + 4j − jμ̄ nach Lemma 11.1 (satz\_3\_9 §11.2).
2. Wie in Lemma F1 folgt für jeden Zustand Φ, nach dem Mitteln über h:

   ```text
   ⟨Φ, H^{vW} Φ⟩ − E₀(H^{vW}_J)  ≥  Σ_Q ( λ_min(b_Q) − μ̄ − sup_Q W ) E_Φ[n_Q]  −  Σ_Q λ_min(b_Q)  −  m c_b N_grob
   ```

   Die Zahl der groben Kästen ist additiv, weil die Umgebung der Vereinigung in der Vereinigung der Umgebungen liegt.
3. Für Φ = Ψ ist die linke Seite null. Nach Voraussetzung ist λ\_min(b\_Q) − μ̄ − sup\_Q W ≥ λ\_min(b\_Q)/2 ≥ sup\_Q W. Also ist E\_Ψ[n\_W] ≤ Σ\_Q sup\_Q W · E\_Ψ[n\_Q] ≤ Σ\_Q λ\_min(b\_Q) + m c\_b N\_grob. ∎

*Bemerkung.* Die Gewichte passen von selbst: Wo das Potential stark ist, sind die Kästen fein und ihre Energie groß. Deshalb darf man Gebiete verschiedener Skalen in einer einzigen Ungleichung zusammenfassen.

## F.8 Satz F7: Raum-Zeit-Momente zeitgemittelter Teilchenzahlen [S]

Für ein Gebiet V der Größe R mit Rampe χ und ein Zeitfenster 𝒲 sei n̄(V, 𝒲) = |𝒲|^{−1} ∫\_𝒲 n\_χ(t) dt die zeitgemittelte Teilchenzahl.

**Satz F7.** Gegeben sei eine endliche Familie (V\_i, R\_i, 𝒲\_i, λ\_i), i ∈ 𝒜, mit λ\_i > 0. Zu jeder Zeit t seien die Gebiete V\_i⁺ mit t ∈ 𝒲\_i paarweise disjunkt. Die feinen Kastenseiten b\_{1,i} erfüllen

```text
c_{b_{1,i}}  ≥  2μ̄  +  2 λ_i / |𝒲_i|
```

Dann gilt unter dem stationären Grundzustands-Pfadmaß

```text
log E exp( Σ_i λ_i n̄(V_i, 𝒲_i) )  ≤  Σ_i λ_i N̄_i,        N̄_i  =  ( |𝒲_i| / λ_i ) · ( c_{b_{1,i}} |V_i⁺| / b_{1,i}²  +  c_b N_grob )
P( n̄(V_i, 𝒲_i) ≥ t_i  für alle i ∈ 𝒜 )  ≤  exp( −Σ_i λ_i (t_i − N̄_i) )
```

*Beweis.* Lemma 6.8 mit W\_t = Σ\_{i: t ∈ 𝒲\_i} (λ\_i/|𝒲\_i|) χ\_i gibt log E exp(∫ n\_{W\_t}(t) dt) ≤ ∫ [ε\_N − E₀(ℒ − ΣW\_t)] dt. Nach Hellmann–Feynman ist ε\_N − E₀(ℒ − ΣW\_t) = ∫₀¹ E\_{Ψ^{vW\_t}}[n\_{W\_t}] dv, und Lemma F6 beschränkt den Integranden für jedes v durch Σ\_{i: t ∈ 𝒲\_i} (c\_{b\_{1,i}} |V\_i⁺|/b\_{1,i}² + c\_b N\_grob). Integrieren über t gibt die Behauptung. ∎

- Die Schranke ist multiplikativ über die Familie. Die Gebiete dürfen verschiedene Skalen haben, und die Zeitfenster dürfen sich überlappen, solange gleichzeitig aktive Gebiete disjunkt sind.
- Lemma T3 und die Cauchy–Schwarz-Zerlegung aus Folgerung F4 werden nicht gebraucht.

**Zahlen.** Sei R² = θ\_R ℓ\_ρ/ρ und |𝒲| = ωR². Wählt man b₁ mit c\* ≤ c\_{b₁} ≤ 5c\*, c\* = 2μ̄ + 2λ/|𝒲|, so ist für R ≥ 8b

```text
N̄  ≤  [ 382 (λ + 8π κ_μ ω θ_R)² / (λ ω)  +  C_E ω θ_R / λ ] · ln(1/ρ)
```

Für θ\_R ≤ C\_E/(1528 (8πκ\_μ)²) (≈ 0,4 bei C\_E = 8·10⁵) und λ = ω (C\_E θ\_R/1528)^{1/2} folgt die Skalenform

```text
N̄(R)  ≤  c̄_R · R · (ρ ln(1/ρ))^{1/2},        c̄_R = 78 C_E^{1/2}   (≈ 7·10⁴ bei C_E = 8·10⁵),        unabhängig von ω
P( n̄ ≥ N̄(R) + u )  ≤  exp( −λ u ),        λ = ω R (ρ C_E / (1528 ln(1/ρ)))^{1/2}
```

Der Faktor 382 enthält den Spielraum 5 der Teilbarkeit im Quadrat; mit passendem b₁ wäre er 15. Für R < 8b benutzt man die Schranke zu R = 8b.

## F.9 Lemma P5 ohne (G3) [S, gegeben (K2′)]

**Lemma P5″.** X sei die Irrfahrt ab x (Rate 1 je Nachbar). Die Linien Y\_j seien feste rechtsstetige Bahnen auf [0, 2τ], zu jeder Zeit auf verschiedenen Plätzen. Sei 𝔅 = B(x, R\_G) die ℓ∞-Kugel um x, 𝔅′ = B(x, R\_G/2), τ ≥ 16A² und A τ^{1/2} ≤ R\_G/2. Jede Linie, die sich während [0, τ] in 𝔅′ aufhält, sei A-diffusiv im Sinn von (G2\_A). Dann gilt

```text
P_x( X trifft in [0, τ] eine Linie an einem Platz von 𝔅′ )  ≤  C e^{CA²} · 𝔏(x) / log₂(τ/A²)
𝔏(x)  =  ∫_0^{2τ} Σ_{y ∈ 𝔅} p_t(x, y) n_y(t) dt
```

*Beweis.*

1. Für die Linie j sei σ\_j die erste Zeit in [0, τ] mit X\_t = Y\_j(t) ∈ 𝔅′, und L\_j = ∫₀^{2τ} 1{X\_t = Y\_j(t) ∈ 𝔅} dt. Nach der starken Markov-Eigenschaft ist E[L\_j] ≥ E[1{σ\_j ≤ τ} g\_j(σ\_j)] mit g\_j(σ) = ∫₀^τ p\_u(Y\_j(σ), Y\_j(σ + u)) 1{Y\_j(σ + u) ∈ 𝔅} du.
2. In einem ruhigen Fenster W\_i ist |Y\_j(σ + u) − Y\_j(σ)| ≤ A 2^{i/2} ≤ A τ^{1/2} ≤ R\_G/2; die Linie bleibt also in 𝔅, wenn sie zur Zeit σ in 𝔅′ war. Wie in Schritt 2 von Lemma P5 folgt g\_j(σ) ≥ c e^{−CA²} log₂(τ/A²).
3. Vereinigungsschranke: P ≤ Σ\_j P(σ\_j ≤ τ) ≤ Σ\_j E[L\_j]/inf g\_j. Weil die Linien zu jeder Zeit auf verschiedenen Plätzen sitzen, ist Σ\_j E[L\_j] = Σ\_j ∫ p\_t(x, Y\_j(t)) 1{Y\_j(t) ∈ 𝔅} dt = 𝔏(x). ∎

- Schritt 3 von Lemma P5, der E[L\_j] über den Anfangsabstand und die schnellen Fenster abschätzt, wird nicht gebraucht. (G3), die Zahlen B\_j(x) und die Konstante C₁ entfallen. Eine Linie, die auf x zuläuft, ist in 𝔏(x) mit ihrem tatsächlichen Beitrag enthalten.
- (G2\_A) bleibt für den Nenner nötig, aber nur für Linien, die 𝔅′ besuchen.
- Dass X die Kugel 𝔅′ vor der Zeit τ verlässt, hat die Wahrscheinlichkeit ≤ 4 exp(−R\_G²/(18τ)) (Lemma F11a) und wird in Lemma P6a″ mitgezählt (F.12.3).
- Rückwärts in der Zeit gilt dasselbe mit der gespiegelten Größe; das braucht die zweite Hälfte in Lemma P6a.

## F.10 Lemma F8: 𝔏 ist klein, wenn die zeitgemittelte Dichte auf allen Skalen klein ist [S]

Das Lemma ist rein deterministisch: Es handelt von einer festen Raum-Zeit-Konfiguration von Linien. Wahrscheinlichkeiten kommen erst in F.11 vor.

### F.10.1 Voraussetzungen

- **Größen:** r ≥ 16 (Isolationsradius), β ≥ 1 mit r ≥ 12β, t\_r = r²/(16β), R₀ ≥ 8r mit t\_r ≤ R₀²/64, Skalen ℛ = {R₀ 2^j : 0 ≤ j ≤ J}, R\_max = R₀ 2^J, Zeithorizont T ≥ 1 mit R\_max² ≥ 8192 (1 + T), Kastenradius R\_G ≥ r, 𝔅 = B(x, R\_G).
- **Gitter:** Zu R ∈ ℛ gehören die Quadrate der Seite R auf dem Gitter der Weite R/2. Zugelassene Fensterlängen: für R > R₀ die Zweierpotenz Δ in (R²/32, R²/16]; für R = R₀ alle Zweierpotenzen Δ in [t\_r, R₀²/16].
- **Zeitbereich:** 𝒯 = [t\_a, t\_b] mit [t₀, t₀ + max(T, t\_r)] ⊂ 𝒯 und t\_b − t\_a ≥ R\_max²/8; in der Anwendung ist 𝒯 die Scheibe. Die Fenster der Länge Δ liegen auf zwei Zeitgittern der Weite Δ/2, eines von t\_a aufwärts und eines von t\_b abwärts: [t\_a + mΔ/2, t\_a + mΔ/2 + Δ] und [t\_b − mΔ/2 − Δ, t\_b − mΔ/2], m ≥ 0. Es zählen nur Fenster, die in 𝒯 liegen.
- **(H1) x gut:** Zur Zeit t₀ hat jede Linie den Abstand ≥ r von x.
- **(H2) Kurzzeit-Ruhe, das ist (G4):** Jede Linie, die sich während [t₀, t₀ + t\_r] in 𝔅 aufhält, bewegt sich in dieser Zeit um höchstens r/4 von ihrer Lage zur Zeit t₀.
- **(H3) zeitgemittelte Dichte, das ist (G1″):** Es gibt N₀ ≥ 0 und c̄ ≥ 0, sodass für jedes R ∈ ℛ, jedes Gitterquadrat Q der Seite R, das B(x, max(R\_G, R\_max) + r) trifft, und jedes Gitterfenster 𝒲 ⊂ 𝒯 zugelassener Länge Δ gilt

```text
∫_𝒲 n_Q(t) dt  ≤  Δ · N(R),        N(R) = N₀ + c̄ R
```

### F.10.2 Aussage

**Lemma F8 [S].** Unter (H1)–(H3) gilt für 𝔏(x) = ∫₀^T Σ\_{y∈𝔅} p\_u(x, y) n\_y(t₀ + u) du:

```text
𝔏(x)  ≤  1,1·10⁷ · c̄ (1 + T)^{1/2}                                                  (Hauptterm)
       +  5920 · (N₀ + c̄ R₀) · log₂(4(1 + T)/t_r)                                    (Zahl der Fenster)
       +  84 · log₂(t_r) · (N₀ + c̄ R₀) · e^{−9β/8}                                   (kurze Zeiten)
       +  n_G · (N₀ + c̄ R_max) · [ 666 v e^{−v} + (R_max²/(2 t_r)) e^{−R_max/128} ]    (ferne Schalen)

v = R_max² / (4096 (1 + T)),        n_G = ( ⌈(2R_G + 1)/R_max⌉ + 1 )²
```

Die Zahlenfaktoren kommen aus S₂ = Σ\_k â\_k 4^k ≤ 185 und S₃ = Σ\_k â\_k 8^k ≤ 4200 mit â\_k = exp(−min(4^k/32, 2^k 2^{1/2}/16)); das ist der Wert der Gewichte a\_{k,i} bei i = 0. Sie sind grob; im Gauß-Bereich allein wäre S₃ = 117.

### F.10.3 Beweis

**Schritt 1: Zerlegen in Zeitfenster und Schalen.** Sei I\_i = [2^i − 1, 2^{i+1} − 1) für i = 0, …, i\_T mit 2^{i\_T} ≤ 1 + T < 2^{i\_T + 1}, und ρ\_{k,i} = 2^k 2^{(i+1)/2}. Nach (K1) ist p\_u(x, y) ≤ (1 + u)^{−1} exp(−d²/(4(u + d))) mit d = |x − y|\_∞; der Exponent wächst in d und fällt in u. Für u ∈ I\_i ist (1 + u)^{−1} ≤ 2^{−i} und u < 2^{i+1}. Für d > ρ\_{k−1,i} ist der Exponent ≥ min(4^k/32, 2^k 2^{(i+1)/2}/16) (je nachdem, ob ρ\_{k−1,i} ≤ 2^{i+1} ist oder nicht). Also gilt für u ∈ I\_i

```text
Σ_{y∈𝔅} p_u(x, y) n_y(t₀ + u)  ≤  2^{−i} Σ_{k≥0} a_{k,i} · n( B(x, ρ_{k,i}) ∩ 𝔅 ; t₀ + u )
a_{0,i} = 1,        a_{k,i} = exp( −min(4^k/32, 2^k 2^{(i+1)/2}/16) )  ≤  â_k
```

Sei M\_{k,i} = 2^{−i} ∫\_{I\_i ∩ [0, T]} n(B(x, ρ\_{k,i}) ∩ 𝔅; t₀ + u) du (für i < i\_T das Zeitmittel über I\_i). Dann ist 𝔏(x) ≤ Σ\_i Σ\_k a\_{k,i} M\_{k,i}.

**Schritt 2: Überdeckung.** Eine Kugel B(x, ρ) liegt in einem Gitterquadrat der Seite R, sobald R ≥ 4ρ ist. Ein Zeitintervall [a, a + ℓ] ⊂ 𝒯 liegt in einem Gitterfenster der Länge Δ, das in 𝒯 liegt, sobald Δ ≥ 2ℓ ist: Das Fenster des Aufwärtsgitters mit dem größten Anfang f ≤ a enthält das Intervall, denn f + Δ > a + Δ/2 ≥ a + ℓ. Ragt es über t\_b hinaus, so ist a > t\_b − Δ. Dann nimmt man das Fenster des Abwärtsgitters mit dem kleinsten Ende e ≥ a + ℓ: Sein Anfang e − Δ ist < a + ℓ − Δ/2 ≤ a und ≥ a + ℓ − Δ > t\_b − 2Δ ≥ t\_a. Im Folgenden heißt „Gitterfenster“ immer ein solches Fenster in 𝒯; die Intervalle t₀ + (I\_i ∩ [0, T]) und [t₀, t₀ + t\_r] liegen nach Voraussetzung in 𝒯.

**Schritt 3: nahe Schalen in nicht kurzen Fenstern** (2^{i+1} > t\_r und 8ρ\_{k,i} ≤ R\_max). Sei R das kleinste Element von ℛ mit R ≥ 8ρ\_{k,i}.

- *R > R₀:* Dann ist R < 16ρ\_{k,i}. Die zugelassene Länge Δ erfüllt Δ > R²/32 ≥ 2ρ\_{k,i}² ≥ 4 · 2^i, also liegt t₀ + I\_i in einem Gitterfenster. Mit (H3) ist ∫\_{I\_i} n(B(x, ρ\_{k,i})) ≤ Δ N(R) ≤ (R²/16) N(R) ≤ 16 ρ\_{k,i}² N(16ρ\_{k,i}), also M\_{k,i} ≤ 32 · 4^k N(16ρ\_{k,i}).
- *R = R₀:* Dann ist 2^{i+1} ≤ R₀²/64, und Δ = 2^{i+1} ist zugelassen (≥ t\_r). Also M\_{k,i} ≤ 2N(R₀).
- *Beide Fälle:* M\_{k,i} ≤ 32 · 4^k (N₀ + c̄R₀ + 16 c̄ ρ\_{k,i}).

Summiert über k mit den Gewichten a\_{k,i} ≤ â\_k: Σ\_k a\_{k,i} M\_{k,i} ≤ 32 S₂ (N₀ + c̄R₀) + 512 S₃ c̄ 2^{(i+1)/2}. Die Zahl der nicht kurzen Fenster ist ≤ log₂(4(1 + T)/t\_r), und Σ\_i 2^{(i+1)/2} ≤ 3,42 · (2(1 + T))^{1/2}. Das gibt die ersten beiden Zeilen.

**Schritt 4: kurze Fenster** (2^{i+1} ≤ t\_r, alle Schalen). Für u ≤ t\_r gilt nach (H1) und (H2):

- Jede Linie in 𝔅 hat zur Zeit t₀ + u den Abstand ≥ 3r/4 von x. Es zählen also nur Plätze mit d ≥ 3r/4, und für die Schale k zählen Plätze mit d ≥ d\_k = max(ρ\_{k−1,i}, 3r/4).
- Jede Linie, die zur Zeit t₀ + u in B(x, ρ) liegt, liegt während ganz [t₀, t₀ + t\_r] in B(x, ρ + r/2). Also ist n(B(x, ρ) ∩ 𝔅; t₀ + u) ≤ t\_r^{−1} ∫ n(B(x, ρ + r/2); t) dt über dieses Intervall.
- B(x, ρ + r/2) wird von höchstens ((2ρ + r + 1)/R₀ + 2)² Gitterquadraten der Seite R₀ überdeckt, und [t₀, t₀ + t\_r] liegt in einem Gitterfenster der Länge Δ < 4t\_r (zugelassen wegen 4t\_r ≤ R₀²/16). Mit (H3) folgt n(B(x, ρ) ∩ 𝔅; t₀ + u) ≤ 4 ((2ρ + r + 1)/R₀ + 2)² N(R₀).

Sei k\_i die erste Schale mit ρ\_{k,i} ≥ 3r/4; es ist k\_i ≥ 1 und ρ\_{k\_i,i} < 3r/2. Für k = k\_i + m ist ρ\_{k,i} < 2^m · 3r/2 und d\_k ≥ (3r/4) 2^{(m−1)₊}. Wegen 2^{i+1} ≤ t\_r und r ≥ 12β ist der Exponent des Kerns ≥ min(2β d\_k²/r², d\_k/8) ≥ (9β/8) 2^{(m−1)₊}. Mit R₀ ≥ 8r ist der Überdeckungsfaktor ≤ 4 (0,375 · 2^m + 2,2)². Also

```text
Σ_{y∈𝔅} p_u(x, y) n_y(t₀ + u)  ≤  2^{−i} · 4 N(R₀) Σ_{m≥0} (0,375·2^m + 2,2)² e^{−(9β/8) 2^{(m−1)₊}}  ≤  2^{−i} · 84 N(R₀) e^{−9β/8}
```

Jedes kurze Fenster trägt damit ≤ 84 N(R₀) e^{−9β/8} bei, und es gibt höchstens log₂(t\_r) davon. Das ist die dritte Zeile.

**Schritt 5: ferne Schalen in nicht kurzen Fenstern** (8ρ\_{k,i} > R\_max). Wegen R\_max² ≥ 8192(1 + T) ist die erste ferne Schale k\_f ≥ 1, und für k = k\_f + m ist ρ\_{k−1,i} ≥ 2^m R\_max/16. Der Exponent ist ≥ 2^m E\_i mit E\_i = min(R\_max²/(2048 · 2^{i+1}), R\_max/128), und E\_i ≥ 1. Die Teilchenzahl in 𝔅 ist höchstens die Summe über n\_G Gitterquadrate der Seite R\_max, und t₀ + I\_i liegt in einem Gitterfenster der Länge ≤ R\_max²/16. Also ist M\_{k,i} ≤ 2^{−i} n\_G (R\_max²/16) N(R\_max) und

```text
Σ_{k fern} a_{k,i} M_{k,i}  ≤  2^{−i} n_G (R_max²/8) N(R_max) e^{−E_i}
```

Mit v\_i = R\_max²/(4096 · 2^i) ≥ v ≥ 2 ist 2^{−i} R\_max² e^{−R\_max²/(2048 · 2^{i+1})} = 4096 v\_i e^{−v\_i}, und Σ\_i v\_i e^{−v\_i} ≤ 1,3 v e^{−v}. Der zweite Zweig von E\_i gibt Σ\_i 2^{−i} R\_max² e^{−R\_max/128} ≤ (4R\_max²/t\_r) e^{−R\_max/128}. Das ist die vierte Zeile. ∎

### F.10.4 Folgerung F9: Anwendung [S, gegeben (G1″) und (G4)]

**Bedingungen an die Umgebung.** Sei β = β(ρ) = C\_β ln ln(1/ρ) mit C\_β ≥ 2 (Satz F11 verlangt später C\_β ≥ 300), t\_r = r²/(16β), R₀ = 8b, ℛ die Skalen 8b · 2^j bis R\_max mit s/16 < R\_max ≤ s/8, R\_G = s, und 𝒯 die Scheibe. In diesem Abschnitt sind s und K die Lokalisierungsskala aus F.5 und ihre Konstante (K = 17; in F.11 und F.12 heißen sie s\_F und K\_F). Dann ist θ\_R ≤ K/64 für alle Skalen, und die Skalenform aus F.8 gilt. Der Kasten vom Radius R\_G muss nur groß gegen √τ sein; mit R\_G = s hängt er nicht von D ab.

```text
(G1″)   (H3) mit   N(R) = N*(R) := 2 c̄_R R (ρ ln(1/ρ))^{1/2} + (ln(1/ρ))^{3/4},        c̄_R = 78 C_E^{1/2}   (Satz F7)
(G4)    (H2) für jede Zeit t₀ der Scheibe, vorwärts und rückwärts in der Zeit
```

**Folgerung F9.** Unter (G1″) und (G4) gilt für jeden zur Zeit t₀ guten Punkt x und jedes T mit t\_r ≤ T ≤ 2τ = 2θ ln(1/ρ)/ρ, für das [t₀, t₀ + T] in der Scheibe liegt,

```text
𝔏(x)  ≤  [ C_𝔏 (C_E θ)^{1/2}  +  ε_fern(θ)  +  o(1) ] · ln(1/ρ)        (ρ → 0)
C_𝔏 = 1,1·10⁷ · 2 · 2^{1/2} · 78  ≈  2,4·10⁹,        ε_fern(θ) = 666 · 35² · c̄_R K^{1/2} v e^{−v},   v ≥ K/(2,1·10⁶ θ)
```

*Beweis.* Einsetzen in Lemma F8 mit c̄ = 2c̄\_R (ρ ln(1/ρ))^{1/2} und N₀ = (ln(1/ρ))^{3/4}. Die Schranke von Lemma F8 wächst mit T (v e^{−v} fällt für v ≥ 1); es genügt also, T = 2τ einzusetzen.

1. **Voraussetzungen.** R₀ ≥ 8r heißt ζ ≤ H^{−1/2}. t\_r ≤ R₀²/64 = b² gilt wegen r ≤ b. R\_max² ≥ 8192(1 + T) heißt θ ≤ K/(4,2·10⁶). r ≥ 12β gilt für kleines ρ.
2. **Hauptterm.** c̄ (1 + T)^{1/2} = 2c̄\_R (2ρτ ln(1/ρ))^{1/2} (1 + o(1)) = 2 · 2^{1/2} c̄\_R θ^{1/2} ln(1/ρ).
3. **Zahl der Fenster.** c̄ R₀ = 16 c̄\_R (ln(1/ρ)/H)^{1/2} und 4(1 + T)/t\_r ≈ 128 θ β ln(1/ρ)/ζ². Die Zeile ist O((ln(1/ρ))^{3/4} ln ln(1/ρ)).
4. **Kurze Zeiten.** log₂(t\_r) ≤ 1,5 ln(1/ρ) und e^{−9β/8} = (ln(1/ρ))^{−9C\_β/8}. Mit C\_β ≥ 2 ist die Zeile O((ln(1/ρ))^{7/4 − 9/4}) = o(1).
5. **Ferne Schalen.** n\_G ≤ 35², N\*(R\_max) ≤ (c̄\_R K^{1/2}/4 + o(1)) ln(1/ρ), v ≥ K/(2,1·10⁶ θ), und v e^{−v} fällt in v. Der zweite Summand der Klammer geht mit ρ → 0 gegen 0, weil R\_max wie ρ^{−1/2} wächst. ∎

**Wahl von θ.** ε\_fern(θ) fällt für θ → 0 schneller als jede Potenz und hängt nicht von D ab. Mit

```text
θ  ≤  θ_P  :=  ε_P² / (16 C_𝔏² C_E)        und        ε_fern(θ_P) ≤ ε_P/4
```

ist 𝔏(x) ≤ (ε\_P/2 + o(1)) ln(1/ρ) für kleines ρ. Zusammen mit Lemma P5″ gilt dann die Treffschranke, die Lemma P6a″ braucht (F.12.3): P\_x(Treffer in 𝔅′) ≤ (1 + o(1))/(8C\_b). Die andere Hälfte des Spielraums 1/(4C\_b) aus F.0 bleibt für das Verlassen von 𝔅′.

**Reihenfolge der Konstanten, ohne Zirkel.**

1. K, H, also C\_E (satz\_3\_9; für das Lemma genügt K = 17).
2. A, also C\_P, C\_b und ε\_P (Anhang P, K).
3. θ = θ\_P(ε\_P). C₀, C₁ und b₀ kommen nicht mehr vor.
4. n = K/θ (hier mit dem K der Zellen); dann p₁, D\_c, D, λ₁, p\* und ζ in der Reihenfolge von F.12.6. Alle sind feste Zahlen.
5. β(ρ) = C\_β ln ln(1/ρ) wächst langsam; es geht nur in t\_r und damit in Terme o(ln(1/ρ)) ein.
6. Zuletzt ρ klein: σ\_ρ = C P\_treff/p\* → 0, weil p\* fest ist.

**Was sich in Lemma P6 sonst ändert,** steht in F.12. P6b und P6 zählen schlechte Zwischenpunkte. Zu einer festen Zeit beschränkt (G1″) diese Zahl nicht gut genug: Der Zusatz N₀ = (ln(1/ρ))^{3/4} je Quadrat der Seite R₀ ist dafür zu groß. Deshalb werden die Zwischenzeiten dort zufällig gewählt; dann zählt ein Zeitmittel auf der Skala des Teilschritts.

## F.11 Seltenheit der Bedingungen

Ab hier ist s die Zellseite und δ = s² = K ln(1/ρ)/ρ die Scheibendauer, wie überall im Projekt. Die Lokalisierungsskala der Lemmata F1 bis F8 heißt s\_F, mit s\_F² = K\_F ln(1/ρ)/ρ und K\_F = 17 ≤ K. Zu ihr gehören C\_E = 53πH²K\_F, R\_max ∈ (s\_F/16, s\_F/8] und R\_G = s\_F (F.10.4).

### F.11.1 Defekte Raum-Zeit-Zellen

- **Kasten.** Zur Raum-Zeit-Zelle (Q\_c, k), Zelle Q\_c in der Scheibe [t\_k, t\_{k+1}], gehört der Kasten 𝔎\_c = {x : d(x, Q\_c) ≤ R\_K} mit R\_K = D\_K s. D\_K ist eine feste Zahl; F.12.6 legt sie fest.
- **(G1″) im Kasten:** (H3) aus F.10.1 mit N = N\*, für jedes R ∈ ℛ, jedes Gitterquadrat der Seite R, das 𝔎\_c trifft, und jedes Fenster der beiden Zeitgitter der Scheibe (von t\_k aufwärts, von t\_{k+1} abwärts), das in der Scheibe liegt.
- **Zeitgitter für (G4).** Sei β₀ = C\_β ln ln(1/ρ) und N\_g die kleinste gerade Zahl ≥ 16β₀δ/r². Dann ist t\_r = δ/N\_g und β = r²/(16 t\_r) ≥ β₀; β weicht von β₀ um weniger als den Faktor 1 + 2/N\_g ab. Die Fenster sind G\_m = [t\_k + m t\_r, t\_k + (m + 1) t\_r], m = 0, …, N\_g − 1. Die Scheibenmitte ist ein Gitterpunkt.
- **(G4′) für ein Stück** (die Bahn Y einer Linie in der Scheibe): In jedem Fenster G\_m ist die Schwankung sup\_{u,u′ ∈ G\_m} |Y(u) − Y(u′)|\_∞ ≤ r/8.
- **(G4′) ⇒ (G4).** Seien t₀ und t₀ + u in der Scheibe, 0 ≤ u ≤ t\_r. Dann liegen beide im selben Fenster oder in zwei benachbarten Fenstern mit gemeinsamem Randpunkt g. Also ist |Y(t₀ + u) − Y(t₀)| ≤ |Y(t₀ + u) − Y(g)| + |Y(g) − Y(t₀)| ≤ r/4. Die Bedingung ist symmetrisch unter Zeitumkehr. (G4) gilt also zu jeder Zeit der Scheibe, vorwärts und rückwärts.
- **(G2\_A) für alle nötigen Horizonte.** Lemma P6 wendet Lemma P5″ auf Teilbrücken mit Treffhorizont τ\_h zwischen τ/(2J) und 3τ/4 an (J aus F.12.6). Verlangt wird deshalb: Für jedes σ der Scheibe und jedes i₁ mit τ/(8J) ≤ 2^{i₁} ≤ τ/2 und σ + 2^{i₁+1} ≤ t\_{k+1} ist mindestens die Hälfte der Fenster σ + W\_i, A² ≤ 2^i ≤ 2^{i₁}, ruhig; ebenso rückwärts. Lemma R (a) gilt für jeden Horizont. Die Vereinigung über die höchstens log₂(8J) Horizonte ändert seine Schranke nur um den festen Faktor log₂(8J) · (8J)^{c′(A)}.
- **Defektgründe.** Die Zelle (Q\_c, k) heißt (G1″)-defekt, wenn (G1″) im Kasten verletzt ist. Sie heißt (G4)-defekt, wenn ein Stück der Scheibe k, das 𝔎\_c besucht, (G4′) verletzt; ebenso für (G2\_A).

### F.11.2 Satz F10: (G1″) ist selten [S]

**Satz F10.** Sei m\_D = ⌈2D\_K⌉ + 3, D\_K ≥ 3 und ζ²H ≤ 1. Für jede Menge 𝒜 von Raum-Zeit-Zellen gilt unter dem stationären Grundzustands-Pfadmaß

```text
P( jede Zelle von 𝒜 ist (G1″)-defekt )  ≤  q₁^{|𝒜| / (4 m_D²)}
q₁  =  N_trip · exp( −c_q (ln(1/ρ))^{1/4} / β ),        N_trip ≤ 51 D_K² K² H β ζ^{−2} (ln(1/ρ))²,        c_q = ζ² (H C_E)^{1/2} / 5003
```

Für ρ → 0 geht q₁ gegen 0, denn (ln(1/ρ))^{1/4}/ln ln(1/ρ) wächst schneller als ln ln(1/ρ).

*Beweis.*

1. **Ein Tripel** (R, Q, 𝒲) mit |𝒲| = Δ. Für die Rampe χ um V = Q ist n\_Q ≤ n\_χ, also ∫\_𝒲 n\_Q dt ≤ Δ · n̄(Q, 𝒲). Die Skalenform von Satz F7 (F.8) gilt, weil θ\_R ≤ K\_F/64 < 0,4 ist; sie gibt N̄(R) ≤ c̄\_R R (ρ ln(1/ρ))^{1/2}, also N\*(R) ≥ N̄(R) + (ln(1/ρ))^{3/4}. Ist (H3) für das Tripel verletzt, so ist n̄ ≥ N̄(R) + (ln(1/ρ))^{3/4}.
2. **Exponent.** Mit λ = ωR (ρ C\_E/(1528 ln(1/ρ)))^{1/2} und ω = Δ/R² ist λ (ln(1/ρ))^{3/4} = (Δ/R) (ρ C\_E/1528)^{1/2} (ln(1/ρ))^{1/4}. Am kleinsten ist Δ/R bei R = R₀ = 8b und Δ = t\_r; für R > R₀ ist Δ/R > R/32 ≥ b/2. Dort ist Δ/R = t\_r/(8b) = ζ² H^{1/2}/(128 β ρ^{1/2}), also λ (ln(1/ρ))^{3/4} ≥ c\_q (ln(1/ρ))^{1/4}/β. (Es ist 128 · 1528^{1/2} = 5003.)
3. **Zahl der Tripel je Zelle.** Höchstens (5 D\_K s/R)² Quadrate der Seite R ≤ s/8 treffen 𝔎\_c. In der Scheibe liegen höchstens 4δ/Δ Fenster der Länge Δ (zwei Gitter der Weite Δ/2).
   - *R > R₀:* eine Länge Δ > R²/32, also höchstens 3200 D\_K² (s/R)⁴ Tripel. Über R = 16b · 2^j summiert sind das ≤ 0,053 D\_K² (KH ln(1/ρ))².
   - *R = R₀:* Die Längen sind Zweierpotenzen ≥ t\_r, zusammen höchstens 8δ/t\_r = 8N\_g Fenster, mit N\_g = 16βK ln(1/ρ)/ζ². Das gibt höchstens 50 D\_K² K² H β ζ^{−2} (ln(1/ρ))² Tripel.
4. **Ausdünnen.** Man wählt 𝒜′ ⊂ 𝒜 so, dass je zwei Zellen von 𝒜′ derselben Scheibe in mindestens einer Koordinate m\_D oder mehr Zellen auseinander liegen (auf dem Torus gemessen). Die gierige Auswahl gibt |𝒜′| ≥ |𝒜|/(2m\_D)². Für Tripel zu verschiedenen Zellen von 𝒜′ gilt dann:
   - *gleiche Scheibe:* Das Gebiet V⁺ eines Tripels liegt in B(Q\_c, R\_K + 2R\_max + b) ⊂ B(Q\_c, R\_K + s/2). Die Lücke zwischen zwei Zellen ist ≥ (m\_D − 1)s > 2R\_K + s. Also sind die Gebiete disjunkt.
   - *verschiedene Scheiben:* Die Fenster liegen in ihren Scheiben und überlappen höchstens in einem Zeitpunkt.
5. **Produkt.** Sind alle Zellen von 𝒜′ defekt, gibt es zu jeder ein verletztes Tripel. Für eine feste Zuordnung c ↦ i(c) erfüllt die Familie der Tripel die Voraussetzung von Satz F7 (gleichzeitig aktive Gebiete disjunkt), und der Satz gibt die Wahrscheinlichkeit ≤ Π\_c exp(−λ\_{i(c)} (ln(1/ρ))^{3/4}). Die Summe über die Zuordnungen ist das Produkt der Summen über die Tripel je Zelle, also ≤ q₁^{|𝒜′|}. ∎

- Der Satz ersetzt den Defektgrund D6. Die Rate je Zelle ist q₁^{1/(4m\_D²)}. Sie geht gegen 0, aber langsam.
- Die Fenster reichen nicht über die Scheibe hinaus. Das Ereignis liegt deshalb im Zeitbereich der Schleife, und die Übertragung auf µ\_ab (G.11.2) gilt unverändert.
- β wächst wie ln ln(1/ρ) (Review W4). Es steht hier im Exponenten gegen (ln(1/ρ))^{1/4} und in N\_trip als Faktor.

### F.11.3 Lemma F11a und Satz F11: (G4) ist selten

**Lemma F11a [S].** Y sei die freie Irrfahrt (Rate 1 je Nachbar) und 0 < a ≤ 2,2 t. Dann gilt

```text
P( sup_{u ≤ t} |Y_u − Y_0|_∞ ≥ a )  ≤  4 exp( −a² / (4,4 t) )
```

Für r ≥ 12β folgt: Die Schwankung von Y in einem Fenster der Länge t\_r = r²/(16β) ist mit Wahrscheinlichkeit ≤ 4 e^{−β/71} größer als r/8.

*Beweis.* Jede Koordinate springt mit Rate 1 nach links und mit Rate 1 nach rechts, und exp(ϑ(Y¹\_u − Y¹\_0) − 2u(cosh ϑ − 1)) ist ein Martingal. Doobs Ungleichung gibt P(sup\_{u≤t} (Y¹\_u − Y¹\_0) ≥ a) ≤ exp(−ϑa + 2t(cosh ϑ − 1)) ≤ exp(−ϑa + 1,1 t ϑ²) für 0 < ϑ ≤ 1, denn dort ist cosh ϑ − 1 ≤ 0,55 ϑ². Mit ϑ = a/(2,2t) ≤ 1 ist das exp(−a²/(4,4t)). Es gibt vier Richtungen. Zur zweiten Aussage: Ist die Schwankung größer als r/8, so ist sup\_u |Y\_u − Y\_0|\_∞ > r/16. Mit a = r/16 und t = t\_r ist a²/t = β/16 und ϑ = β/(2,2r) ≤ 1. ∎

**Satz F11 [S, gegeben Satz T2 (satz\_3\_9 §10) mit seinen Eingängen].** Sei C\_β ≥ 300 und m₄ = ⌈2D\_K + 2D⌉ + 4. Für jede Menge 𝒜 von Raum-Zeit-Zellen gilt

```text
P( in jeder Zelle von 𝒜 verletzt ein Stück ohne Makro-Fehler, das 𝔎_c besucht, (G4′) )  ≤  q₄^{|𝒜| / (4 m₄²)}
q₄  =  p₄^{1/2} · exp( C₄ ln(1/ρ) p₄^{1/3} ),        p₄  =  512π e^{1/2} e^{D²/2} K β ζ^{−2} (ln(1/ρ))^{1 − C_β/71}
```

Für ρ → 0 ist q₄ ≤ 2 p₄^{1/2} → 0.

*Beweis.*

1. **Ein Stück.** Ein Stück ohne Makro-Fehler von S nach E hat |S − E|\_∞ ≤ Ds. Auf der ersten Hälfte der Scheibe hat die Brücke bezüglich der freien Irrfahrt ab S die Dichte ≤ 8π e^{|S − E|²/(4δ)} ≤ 8π e^{D²/2} (K3, Schritt 1), auf der zweiten Hälfte bezüglich der rückwärts laufenden ab E. Jedes Fenster G\_m liegt in einer Hälfte, und die Schwankung ist symmetrisch unter Zeitumkehr. Lemma F11a und die Vereinigung über N\_g Fenster geben P\_{S→E}((G4′) verletzt) ≤ 8π e^{D²/2} · 4N\_g e^{−β/71} ≤ p₄.
2. **Ein Fach in Satz T2.** U\_c sei die Vereinigung der Zellen, die B(Q\_c, R\_K + Ds) treffen. Ein Stück ohne Makro-Fehler, das 𝔎\_c besucht, endet in U\_c. J\_c zähle die Stücke mit Ende in U\_c, die (G4′) verletzen und keinen Makro-Fehler haben. Das ist ein Fach wie R2 in §10.0, mit h = D. Satz T2 gilt mit jedem Gewicht w > 1 statt e: In §10.3 entwickelt man w^J = Π(1 + (w − 1) 1{…}), und Schritt 1 (§10.2) verlangt dann (w − 1) K\_b ≤ η\_b e^{−δM\_b} p\_b p\_b e^{c₁δΔ}; der Rest ist unverändert. Mit w − 1 = p₄^{−1/2} und η₄ = C p₄^{1/3} ist das erfüllt, denn η₄ e^{−δM₄} = η₄^{3/2}. Für Zellen c mit paarweise disjunkten U\_c folgt

   ```text
   log E w^{Σ_c J_c}  ≤  C C_a ρ Σ_c |U_c| · η₄ D²
   ```

   über mehrere Scheiben als Summe (§10.4).
3. **Ausdünnen und Markov.** Wie in Satz F10 wählt man 𝒜′ mit |𝒜′| ≥ |𝒜|/(2m₄)², sodass die U\_c in jeder Scheibe disjunkt sind. Wegen 1{J\_c ≥ 1 für alle c} ≤ w^{ΣJ\_c − |𝒜′|} und ρ|U\_c| ≤ (2D\_K + 2D + 3)² K ln(1/ρ) folgt die Behauptung mit C₄ = C C\_a (2D\_K + 2D + 3)² K D².
4. **Kleinheit.** Für C\_β ≥ 300 ist p₄ ≤ C β (ln(1/ρ))^{−3,2}, also ln(1/ρ) p₄^{1/3} → 0. Die Bedingung des Fachs, log(1/η₄) ≥ 4δμ̄ ≈ 32πK, gilt für kleines ρ, weil η₄ → 0. ∎

- (G4) tritt an die Stelle des Fachs R3. b₀ und Lemma R (b) werden nicht mehr gebraucht.
- Stücke mit Makro-Fehler, die 𝔎\_c besuchen, zählen zum Defektgrund D4, wie bei (G2\_A). Dafür muss D4 alle Stücke erfassen, die den Kasten besuchen, nicht nur die, die in ihm enden: Fächer j ≥ 1 zum Gebiet B(Q\_c, R\_K + 2D\_j s); die Summe Σ\_j e^{−κD\_j²} (D\_K + 2D\_j)² D\_j² konvergiert. In satz\_3\_9 §9 ist das nicht ausgeschrieben. Es betrifft (G2\_A) ebenso und ist kein neuer Punkt von (G4). *Nachtrag 2026-11-13:* Fächer nach der Reiseweite genügen dafür nicht; eine irreguläre Linie, die viele Zellen besucht, macht viele Kästen defekt. Gelöst in satz\_3\_9 §10.8: Lemma T4 (überlinearer Schwanz der Zahl besuchter Zellen), Lemma T5 (punktweise Kernschranke über Cauchy–Schwarz zur halben Zeit), Satz T2′ und Folgerung T6, mit C\_β ≥ 500; numerisch geprüft (pruef\_besucher.py).
- Die Bedingung log(1/η₄) ≥ 32πK heißt ln ln(1/ρ) ≳ 96πK/(C\_β/71 − 1). Das ist doppelt exponentiell in K; mit größerem C\_β wird es milder. Für den Existenzsatz ist es gleichgültig.

### F.11.4 Lemma F13: eine einzelne Linie [S, gegeben (K1), (K2′)]

In σ\_ρ = C P\_treff/p\* steht die Wahrscheinlichkeit P\_treff, dass eine freie Irrfahrt aus guter Lage ein bestimmtes Stück trifft. Bisher folgte sie aus Lemma P5 mit B(x) ≤ b₀, also aus (G3). Sie folgt auch ohne (G3):

**Lemma F13.** Sei x gut zur Zeit t₀. Die Linie Y erfülle (G4) bei t₀ und (G2\_A) mit Horizont τ zu jeder Zeit σ ∈ [t₀, t₀ + T\_h]. Dann gilt

```text
P_x( X trifft Y in [t₀, t₀ + T_h] )  ≤  C_P · [ ln( (1 + T_h + τ)/(1 + t_r) )  +  e^{−9β/8} ln(1 + t_r) ] / log₂(τ/A²)
```

Für T\_h ≤ δ ist die eckige Klammer ≤ ln(32Kβ ln(1/ρ)/ζ²) + o(1), also ist die Wahrscheinlichkeit ≤ C C\_P ln ln(1/ρ)/ln(1/ρ).

*Beweis.* Wie Lemma P5, Schritt 1 und 2, mit L = ∫₀^{T\_h+τ} 1{X\_t = Y(t₀ + t)} dt: Die Wahrscheinlichkeit ist ≤ E[L]/inf g, und g(σ) ≥ c e^{−CA²} log₂(τ/A²) nach (G2\_A). Der Zähler ist E[L] = ∫₀^{T\_h+τ} p\_t(x, Y(t₀ + t)) dt. Für t ≤ t\_r hat die Linie nach (G4) den Abstand ≥ 3r/4 von x, und (K1) gibt p\_t ≤ (1 + t)^{−1} e^{−9β/8} wie in Schritt 4 des Beweises von Lemma F8. Für t > t\_r genügt p\_t ≤ (1 + t)^{−1}. ∎

- Die Bahn der Linie nach der Zeit t\_r geht nicht ein. Auch eine Linie, die danach auf x zurast, kostet nur den Faktor ln(τ/t\_r) ~ ln ln(1/ρ), den schon die ruhende Linie kostet.
- L braucht die Linie bis zur Zeit t₀ + T\_h + τ. Für eine Brücke mit guten Endpunkten benutzt man das Lemma auf der ersten Hälfte vorwärts und auf der zweiten rückwärts (T\_h = δ/2), mit dem Dichtefaktor aus (W1) in F.12.2.
- Damit ist P\_treff ≤ C C\_P ln ln(1/ρ)/ln(1/ρ), ohne (G3) und ohne b₀.

## F.12 Lemma P6 mit den neuen Bedingungen [S, gegeben (K1), (K2′)]

Dieser Abschnitt ersetzt Lemma P6, P6a und P6b in Anhang P, P.7.5. Der Aufbau ist derselbe: kurze Brücke, einmaliges Teilen mittlerer Schritte, Ausnahmeereignis, Jensen. Neu sind drei Dinge:

- Die Treffschranke kommt aus Lemma P5″ und Folgerung F9 statt aus Folgerung P5′.
- Die Zwischenzeiten der Zerlegung werden zufällig gewählt. Dadurch ist die Zahl schlechter Zwischenpunkte ein Zeitmittel, und das beschränkt (G1″). Zu einer festen Zeit wäre (G1″) dafür zu schwach.
- Die Konstanten sind ausgeschrieben, und die Kern-Abschätzungen der Brücke („Gauß-artig“ in P.7.5) sind aus (K1), (K2) hergeleitet.

### F.12.1 Rahmen und Aussage

- **Brücke.** X ist die freie Brücke von S zur Zeit t\_a nach Y′ zur Zeit t\_b. [t\_a, t\_b] ist eine Scheibe, t\_b − t\_a = δ\_B = nτ mit ganzzahligem n ≥ 10⁵. Sei d = Y′ − S mit |d|\_∞ ≤ δ\_B, und γ\_n = |d|/(n τ^{1/2}) der normierte Vorschub je Teilintervall. |·| ohne Index ist die euklidische Norm.
- **Umgebung.** Feste Linien auf [t\_a, t\_b], zu jeder Zeit auf verschiedenen Plätzen. *Ausweichen* heißt X\_t ≠ Y\_j(t) für alle j und t. Ein Punkt u heißt *gut zur Zeit t*, wenn er zur Zeit t von allen Linien den Abstand > r hat.
- **Zahlen.**

  ```text
  λ₁ = max( 12 γ_n, (17 ln(352 n))^{1/2} ),        j₁ = ⌈λ₁²⌉,        J = 4 (λ₁² + 1),        R_K = λ₁ n τ^{1/2} + 3 s_F,        c₂ = 4·10⁻⁴
  ```

- **Voraussetzungen (U).**
  1. (G1″) für alle Gitterquadrate, die 𝔎 = B(S, R\_K) treffen, und alle Gitterfenster in [t\_a, t\_b] (F.11.1).
  2. (G4) und (G2\_A) (alle Horizonte, F.11.1) für jede Linie, die 𝔎 besucht.
  3. S ist gut zur Zeit t\_a, und Y′ ist gut zur Zeit t\_b.
  4. θ ≤ θ\_P (F.10.4), ζ ≤ ζ₀ (F.12.6), ρ klein genug.

**Lemma P6″.** Unter (U) gilt

```text
P_{S→Y′}( weicht aus )  ≥  p*  =  ½ exp( −C′ n ),        C′ = 9,3 · ( 1 + 520 e^{1,75 γ_n²} )
```

C′ hängt nur von γ\_n ab. C₀, C₁ und b₀ kommen nicht vor. *Bezeichnung (Review 2026-11-13, H5):* p\* heißt in diesem Anhang die Ausweichschranke von Lemma P6″. In Anhang M heißt sie p\_P (für allgemeine Brücken) bzw. p₁ (kurze Brücken); die Zugänglichkeitsschwelle p\* = e^{−δμ̄−κ} aus Anhang U ist etwas anderes.

Ist δ\_B/τ nicht ganzzahlig, nimmt man τ̃ = δ\_B/⌈δ\_B/τ⌉ ∈ (τ/2, τ] als Teilintervall; alles gilt dann mit θ̃ = θ τ̃/τ ≤ θ.

### F.12.2 Werkzeuge: der Kern der Brücke

Für eine Brücke der Dauer t von u nach u + d, mit t ≥ 1 und |d|\_∞ ≤ t, gilt:

- **(W1) Halbbrücke.** Auf [0, t/2] hat die Brücke bezüglich der freien Irrfahrt ab u die Dichte p\_{t/2}(X\_{t/2}, u + d)/p\_t(d) ≤ 8π e^{1/2} e^{λ²/4} mit λ = |d|/t^{1/2}. (Das ist K3, Schritt 1.)
- **(W2) Zuwachs.** Der Zuwachs Z über ein beliebiges Teilintervall der Länge Δ < t hat das Gesetz P(Z = z) = p\_Δ(z) p\_{t−Δ}(d − z)/p\_t(d), und

  ```text
  P(Z = z)  ≤  4π e^{1/2} · (1 + t)/(1 + t − Δ) · p_Δ(z) · exp( |d|² (|d|_∞ + |z|_∞)/(4t²)  +  |d| |z|/(2t) )
  ```

- **(W3) Randverteilung.** Zur Zeit a, mit b = t − a und m = u + (a/t) d, ist P(X\_a = y) = p\_a(y − u) p\_b(u + d − y)/p\_t(d), und

  ```text
  P(X_a = y)  ≤  4π e^{1/2} · (1 + t)/((1 + a)(1 + b)) · exp( −(t/(4ab)) |y − m|² + κ )
              κ = |y − u|² |y − u|_∞ / (4a²)  +  |u + d − y|² |u + d − y|_∞ / (4b²)
  P(X_a = y)  ≥  (4π)^{−2} e^{−1} · (1 + t)/((1 + a)(1 + b)) · exp( −(t/(4ab)) |y − m|² − |d|² |d|_∞/(4t²) )
              für a, b ≥ 1,  |y − u|_∞ ≤ a,  |u + d − y|_∞ ≤ b
  ```

*Beweis.* (W2): Das Gesetz folgt aus der Faltung Σ\_x p\_a(x) p\_{t−a−Δ}(d − z − x) = p\_{t−Δ}(d − z); die Zuwächse einer Brücke sind austauschbar. Für die Schranke nimmt man (K1) für p\_{t−Δ}(d − z) und (K2) für p\_t(d), dazu |d − z|² ≥ |d|² − 2|d||z|, |d − z|\_∞ ≤ |d|\_∞ + |z|\_∞ und 1/t − 1/(t + x) ≤ x/t². (W3): (K1) und (K2) für die drei Kerne und die Identität |y − u|²/a + |u + d − y|²/b = |d|²/t + (t/(ab)) |y − m|². ∎

*Konstanten seit 2026-11-13 mit (K2′) statt des scharfen (K2) (Anhang K, K.1): Jede Benutzung von (K2) kostet in 2D den Faktor e^{1/2}. Daher e^{1/2} in (W1), (W2) und der oberen Schranke von (W3), e^{−1} in der unteren, die (K2) zweimal benutzt. Alle Zahlen in F.12.3 bis F.12.6 sind entsprechend nachgerechnet; die Werte bis 2026-11-13 stehen jeweils in Klammern.*

### F.12.3 Lemma P6a″: kurze Brücke

**Lemma P6a″.** Sei τ/J ≤ τ′ ≤ 3τ/2 und [t, t + τ′] in der Scheibe. Sei u gut zur Zeit t, v gut zur Zeit t + τ′, |u − v| ≤ 3τ′^{1/2}, und B(u, 2s\_F) ∪ B(v, 2s\_F) ⊂ 𝔎. Dann weicht die Brücke von u nach v mit Wahrscheinlichkeit ≥ ½ aus.

*Beweis.*

1. Nach (W1) hat die erste Hälfte bezüglich der freien Irrfahrt ab u die Dichte ≤ C\_b := 8π e^{11/4} ≤ 394 (bis 2026-11-13: 8π e^{9/4} ≤ 239).
2. Die freie Irrfahrt verlässt 𝔅′ = B(u, s\_F/2) bis zur Zeit τ′/2 mit Wahrscheinlichkeit ≤ 4 exp(−(s\_F/2)²/(4,4 · 3τ/4)) = 4 e^{−K\_F/(13,2θ)} (Lemma F11a).
3. Sie trifft bis zur Zeit τ′/2 eine Linie an einem Platz von 𝔅′ mit Wahrscheinlichkeit ≤ C\_P 𝔏(u)/log₂(τ′/(2A²)). Das ist Lemma P5″ mit Treffhorizont τ′/2 und R\_G = s\_F; den Nenner sichert (G2\_A) für diesen Horizont. Folgerung F9 mit T = τ′ gibt 𝔏(u) ≤ (ε\_P/2 + o(1)) ln(1/ρ). Wegen log₂(τ′/(2A²)) = (1 + o(1)) ln(1/ρ)/ln 2 und ε\_P = 1/(4 ln 2 · C\_b C\_P) ist die Wahrscheinlichkeit ≤ (1 + o(1))/(8C\_b).
4. Die erste Hälfte der Brücke trifft also mit Wahrscheinlichkeit ≤ C\_b (1/(8C\_b) + 4e^{−K\_F/(13,2θ)} + o(1)) ≤ ¼ für kleines ρ. Die zweite Hälfte ist rückwärts gelesen eine Brücke ab v, und alle Bedingungen sind symmetrisch unter Zeitumkehr. Zusammen ≤ ½. ∎

### F.12.4 Lemma P6b″: mittlerer Schritt

**Lemma P6b″.** Sei τ/2 ≤ τ″ ≤ 3τ/2 und [t, t + τ″] in der Scheibe. Sei u gut zur Zeit t, v gut zur Zeit t + τ″, λ = |u − v|/τ″^{1/2} mit 3 < λ ≤ λ₁, und die 3s\_F-Umgebung der Strecke von u nach v liege in 𝔎. Sei j = ⌈λ²⌉ und

```text
ζ²  ≤  c₂^{j₁−1} θ^{1/2} / (2,0·10⁵ c̄_R j₁^{3/2})
```

Dann weicht die Brücke von u nach v mit Wahrscheinlichkeit ≥ ½ (c₂/2)^j ≥ exp(−9,3 (1 + λ²)) aus.

*Beweis.*

1. **Zufällige Zwischenzeiten.** Sei τ′ = τ″/j. Unabhängig von der Brücke seien V\_1, …, V\_{j−1} unabhängig und gleichverteilt auf [0, 1], und T\_i = t + iτ′ + V\_i τ′/2 für 0 < i < j, T\_0 = t, T\_j = t + τ″. Die Dauern Δ\_i = T\_{i+1} − T\_i liegen in [τ′/2, 3τ′/2] ⊂ [τ/J, 3τ/2]. Sei Q\_i = X\_{T\_i}. Gegeben die Zeiten und die Q\_i sind die Teilstücke unabhängige Brücken. Also ist P(weicht aus) = E[Π\_i q\_i], mit der Ausweichwahrscheinlichkeit q\_i des i-ten Teilstücks.
2. **Schlauch.** Sei m(t′) = u + ((t′ − t)/τ″)(v − u), m\_i = m(T\_i), und E\_klein das Ereignis |Q\_i − m\_i| ≤ ½ τ′^{1/2} für alle 0 < i < j. Gegeben die Zeiten und Q\_i ist Q\_{i+1} die Lage einer Brücke von Q\_i nach v der Dauer ϱ = t + τ″ − T\_i zur Zeit Δ\_i. Ihr Mittelpunkt m̃ = Q\_i + (Δ\_i/ϱ)(v − Q\_i) erfüllt m̃ − m\_{i+1} = (1 − Δ\_i/ϱ)(Q\_i − m\_i), also |m̃ − m\_{i+1}| ≤ ½ τ′^{1/2}. Für die (π/4) τ′ (1 − o(1)) Gitterpunkte y mit |y − m\_{i+1}| ≤ ½ τ′^{1/2} ist |y − m̃| ≤ τ′^{1/2}. Die untere Schranke in (W3) gibt mit ϱ/(Δ\_i(ϱ − Δ\_i)) = 1/Δ\_i + 1/(ϱ − Δ\_i) ≤ 4/τ′ für jeden dieser Punkte P(Q\_{i+1} = y | Q\_i) ≥ (4π)^{−2} (1 + 3τ′/2)^{−1} e^{−2−o(1)}. Also

   ```text
   P( |Q_{i+1} − m_{i+1}| ≤ ½ τ′^{1/2}  |  Q_i )  ≥  (1 − o(1)) · e^{−2}/(96π)  ≥  c₂,        P(E_klein)  ≥  c₂^{j−1}
   ```

3. **Teilschritte.** Es ist |m\_{i+1} − m\_i| = Δ\_i λ/τ″^{1/2} ≤ Δ\_i/τ′^{1/2}, weil j ≥ λ² ist. Auf E\_klein folgt |Q\_{i+1} − Q\_i| ≤ (Δ\_i/τ′ + 1) τ′^{1/2} ≤ 3Δ\_i^{1/2}, denn x² + 1 ≤ 3x für x = (Δ\_i/τ′)^{1/2} ∈ [0,71; 1,23].
4. **Schlechte Zwischenpunkte.** Gegeben T\_i = t′ ist nach der oberen Schranke in (W3) P(Q\_i = y) ≤ (12π e^{1/2} + o(1))/τ′ für |y − m(t′)| ≤ ½ τ′^{1/2}: Dort ist a = t′ − t ≥ τ′ und b ≥ τ′/2, also (1 + τ″)/((1 + a)(1 + b)) ≤ 1/a + 1/b ≤ 3/τ′, und κ = o(1). T\_i ist gleichverteilt auf einem Intervall I der Länge τ′/2, und in dieser Zeit bewegt sich m(t′) um höchstens ½ τ′^{1/2}. Ein schlechter Platz im Schlauch hat den Abstand ≤ r von einer Linie in der Kugel B̃ = B(m̄, τ′^{1/2} + r), m̄ = m(Anfang von I); jede Linie verdirbt (2r + 1)² Plätze. Also

   ```text
   P( Q_i schlecht zur Zeit T_i,  |Q_i − m_i| ≤ ½ τ′^{1/2} )  ≤  (2/τ′) · ((12π e^{1/2} + o(1))/τ′) · (2r + 1)² · ∫_I n(B̃; t′) dt′
   ```

   Sei R das kleinste Element von ℛ mit R ≥ 4(τ′^{1/2} + r). Dann liegt B̃ in einem Gitterquadrat der Seite R, es ist R₀ < R ≤ 8,1 τ′^{1/2} ≤ R\_max, und die zugelassene Fensterlänge ist Δ\_R > R²/32 ≥ τ′/2. Jede Hälfte von I (Länge τ′/4 ≤ Δ\_R/2) liegt in einem Gitterfenster. (G1″) gibt ∫\_I n(B̃) ≤ 2Δ\_R N\*(R) ≤ 8,2 τ′ N\*(8,1 τ′^{1/2}), und N\*(8,1 τ′^{1/2}) = (16,2 c̄\_R (θτ′/τ)^{1/2} + o(1)) ln(1/ρ). Mit (2r + 1)² = (4 + o(1)) ζ²/ρ, ln(1/ρ)/ρ = τ/θ und τ/τ′ ≤ 2j folgt

   ```text
   P( Q_i schlecht zur Zeit T_i,  |Q_i − m_i| ≤ ½ τ′^{1/2} )  ≤  9,4·10⁴ · ζ² c̄_R (j/θ)^{1/2} · (1 + o(1))
   ```

   Über i < j summiert ist das ≤ 1,0·10⁵ j^{3/2} ζ² c̄\_R θ^{−1/2} ≤ ½ c₂^{j−1} nach der Voraussetzung an ζ.
5. **Zusammen.** Auf E\_klein mit guten Zwischenpunkten erfüllt jedes Teilstück die Voraussetzungen von Lemma P6a″, also ist q\_i ≥ ½. Damit ist P(weicht aus) ≥ 2^{−j} (c₂^{j−1} − ½ c₂^{j−1}) ≥ ½ (c₂/2)^j. Wegen j ≤ λ² + 1 ist das ≥ exp(−(ln 2 + ln 5000)(1 + λ²)) ≥ e^{−9,3(1+λ²)}. ∎

*Zahl [N].* Die Schranke c₂ = 4·10⁻⁴ (bis 2026-11-13, mit dem scharfen (K2): 10⁻³) kommt aus den Vorfaktoren 4π in (K1), (K2′). Der exakte Wert der Wahrscheinlichkeit in Schritt 2 ist in den geprüften Lagen ≥ 0,039 (F.13).

### F.12.5 Beweis von Lemma P6″

1. **Zerlegen.** Unabhängig von der Brücke seien V\_1, …, V\_{n−1} unabhängig und gleichverteilt auf [0, 1], T\_k = t\_a + kτ + V\_k τ/2 für 0 < k < n, T\_0 = t\_a, T\_n = t\_b. Die Dauern Δ\_k = T\_{k+1} − T\_k liegen in [τ/2, 3τ/2]. Sei P\_k = X\_{T\_k} und λ\_k = |P\_{k+1} − P\_k|/Δ\_k^{1/2}. Wie in P6b″ ist P(weicht aus) = E[Π\_k q\_k].
2. **Große Schritte.** Nach (W2) mit t = δ\_B, |z|/δ\_B^{1/2} ≤ (1,5/n)^{1/2} |z|/Δ\_k^{1/2} und n ≥ 10⁵ hat der Zuwachs P\_{k+1} − P\_k bezüglich der freien Irrfahrt der Dauer Δ\_k für kleines ρ die Dichte ≤ 22 exp(0,63 γ\_n λ\_k) (bis 2026-11-13: 13); die Terme mit |d|/δ\_B = γ\_n/τ^{1/2} sind o(1). Für die freie Irrfahrt ist E e^{ϑ|Z¹|} ≤ 2 e^{1,1 Δϑ²} je Koordinate (ϑ ≤ 1). Die exponentielle Tschebyscheff-Ungleichung mit dem Exponenten λ₁/4,4 gibt

   ```text
   P( λ_k > λ₁ )  ≤  88 exp( −λ₁²/8,8 + 0,63 γ_n λ₁ )  ≤  88 e^{−λ₁²/16,4}  ≤  1/(4n)
   ```

   nach der Wahl von λ₁. Das Ereignis G₁ = {λ\_k ≤ λ₁ für alle k} hat also P(G₁) ≥ ¾. Ebenso ist E λ\_k² ≤ 22 (E\_frei λ⁴)^{1/2} (E\_frei e^{1,26 γ\_n λ})^{1/2} ≤ 260 e^{1,75 γ\_n²}, mit E\_frei λ⁴ ≤ 33.
3. **Lage.** Auf G₁ ist |P\_k − S| ≤ λ₁ Σ\_{i<k} Δ\_i^{1/2} ≤ λ₁ (k (T\_k − t\_a))^{1/2}, und ebenso |Y′ − P\_k| ≤ λ₁ ((n − k)(t\_b − T\_k))^{1/2}. Alle P\_k liegen in B(S, λ₁ n τ^{1/2}), und die 3s\_F-Umgebung aller Strecken von P\_k nach P\_{k+1} liegt in 𝔎.
4. **Schlechte Knoten.** Gegeben T\_k = t′ ist nach (W3) P(P\_k = y) ≤ (12π e^{1/2} + o(1))/τ für jedes y, das die beiden Ungleichungen aus Schritt 3 erfüllt: Es ist a = t′ − t\_a ≥ τ und b = t\_b − t′ ≥ τ/2, also 1/a + 1/b ≤ 3/τ, und κ ≤ λ₁³ n^{3/2}/τ^{1/2} = o(1). Die schlechten Plätze zählt man wie in P6b″, Schritt 4, mit dem Zeitmittel über das Intervall der Länge τ/2, auf dem T\_k gleichverteilt ist. Sei R ∈ ℛ mit 4τ^{1/2} ≤ R < 8τ^{1/2}. Die Kugel B(S, λ₁ n τ^{1/2} + r) wird von höchstens (2,1 λ₁ n τ^{1/2}/R)² Gitterquadraten einer Pflasterung überdeckt, und je Quadrat ist das Zeitintegral ≤ 2Δ\_R N\*(R) ≤ (R²/8) N\*(8τ^{1/2}). Also

   ```text
   P( P_k schlecht zur Zeit T_k,  G₁ )  ≤  (2/τ) · ((12π e^{1/2} + o(1))/τ) · (2r + 1)² · 0,56 λ₁² n² τ · N*(8τ^{1/2})  ≤  4,5·10³ · ζ² c̄_R λ₁² n² θ^{−1/2} · (1 + o(1))
   ```

   Über k < n summiert ist das ≤ ¼, sobald ζ² ≤ θ^{1/2}/(1,8·10⁴ c̄\_R λ₁² n³) ist. Das Ereignis G = G₁ ∩ {alle P\_k gut zur Zeit T\_k} hat dann P(G) ≥ ½.
5. **Je Schritt.** Auf G erfüllt jedes Teilstück die Voraussetzungen von Lemma P6a″ (λ\_k ≤ 3) oder von Lemma P6b″ (3 < λ\_k ≤ λ₁). In beiden Fällen ist q\_k ≥ e^{−9,3(1+λ\_k²)}.
6. **Jensen über die Schrittweiten.** E[1\_G Π\_k e^{−9,3(1+λ\_k²)}] ≥ P(G) exp(−9,3n − 9,3 E[Σ\_k λ\_k² | G]), und E[Σ\_k λ\_k² | G] ≤ E[Σ\_k λ\_k²]/P(G) ≤ 520 n e^{1,75 γ\_n²}. ∎

### F.12.6 Konstanten und Folgen

**Bedingungen an ζ** (das ist ζ₀ in (U)):

```text
ζ²  ≤  1/H                                                    (F.10.4: R₀ ≥ 8r)
ζ²  ≤  c₂^{j₁−1} θ^{1/2} / (2,0·10⁵ c̄_R j₁^{3/2})             (Lemma P6b″)
ζ²  ≤  θ^{1/2} / (1,8·10⁴ c̄_R λ₁² n³)                         (Lemma P6″, Schritt 4)
```

Die mittlere ist die schärfste. Mit λ₁² ≈ 17 ln(352n) ist c₂^{λ₁²} ≈ (352n)^{−133} (bis 2026-11-13: (208n)^{−117}): polynomial klein in n wie bisher, aber mit großem Exponenten. Mit dem exakten Wert 0,039 statt c₂ wäre der Exponent 55.

**Der Kasten.** Für δ\_B = δ ist R\_K ≤ D\_K s mit D\_K = λ₁ n^{1/2} + 3. Das ist die Zahl D\_K aus F.11.1. Sie ist viel größer als D, weil das Ausnahmeereignis G₁ nur die Schrittweiten begrenzt und nicht die Lage. Für den Existenzsatz stört das nicht: D\_K geht nur in m\_D, m₄ und N\_trip ein.

**Reihenfolge der Konstanten** (ersetzt Z.9, Schritt 2 und 4, und die Liste in F.10.4):

1. K, H (satz\_3\_9); K\_F = 17, also C\_E.
2. A (Regularität), also C\_P; C\_b = 8π e^{9/4}; ε\_P = 1/(4 ln 2 · C\_b C\_P).
3. θ ≤ θ\_P(ε\_P), so gewählt, dass n = K/θ ganzzahlig ist.
4. Kurze Brücken (|d| ≤ 2^{1/2} s, Lemma C): γ\_n ≤ (2/n)^{1/2}, also C′ ≤ 4900 und p₁ = ½ e^{−4900n} (bis 2026-11-13: 2500). Daraus D\_c (G.12.9) und D ≥ D\_c + 1.
5. Allgemeine Brücken (|d|\_∞ ≤ (D + 10)s): γ\_n ≤ 2^{1/2}(D + 10)/n^{1/2}. Daraus λ₁, j₁, J, C′, die Ausweichschranke p\* = p\_P (nicht die Zugänglichkeitsschwelle aus Anhang U), D\_K, m\_D und m₄.
6. ζ ≤ ζ₀, dazu die Bedingungen aus Isolation (satz\_3\_9 §12.2) und Lemma C.
7. C\_β ≥ 500 (Satz F11 allein braucht 300; die Besucher eines Kastens, satz\_3\_9 §10.8, Folgerung T6, brauchen 500). β(ρ) wächst wie ln ln(1/ρ) und geht nur in Terme o(ln(1/ρ)) und in die Raten q₁, q₄ ein.
8. Zuletzt ρ klein: σ\_ρ, q₁, q₄ → 0.

Kein Schritt greift auf einen späteren zurück. θ, n und p\* hängen nicht von ρ ab.

**Folgen für Lemma C (G.12.9).**

- Schritt 1 dort zählt die nicht isolierten Plätze zur Scheibenzeit t\_k. Dafür genügt die Dichte auf der Zellskala: In nicht defekten Zellen ist n\_Q ≤ C\_a m (Defektgrund D1). C₀ ist dort durch C\_a zu ersetzen, also η\_c = C (e^{−cD\_c²} + C\_a ζ² D\_c²)/(c₁ p₁).
- p₁ ist die Schranke von Lemma P6″ für |d| ≤ 2^{1/2} s. Sie hängt nicht von D\_c ab. Die Voraussetzung an die Umgebung ist (U) für den Kasten um Y\_m.
- Für das Treffen mit einem Stück der anderen Schleife tritt Lemma F13 an die Stelle von Folgerung P5′. Für die freie Rückwärts-Irrfahrt Q\_Y ab Y\_m deckt es die Treffer bis zur Zeit δ − τ. Den Rest behandelt man vom Anfang S′ aus: P\_{Q\_Y}(S′ = y, Treffer in der zweiten Hälfte) ≤ (1 + δ/2)^{−1} P\_y(Treffer in [0, δ/2]), denn der umgekehrte Weg ist eine Irrfahrt ab y, und p\_{δ/2} ≤ (1 + δ/2)^{−1}. Die Plätze y ∈ G(Y\_m) sind gut, und es gibt höchstens (2D\_c s + 1)² davon. Also ist P\_{Q\_Y}(Treffer) ≤ C D\_c² C\_P ln ln(1/ρ)/ln(1/ρ).

## F.13 Exakte Prüfung [N]

[pruef\_feinskala.py](pruef_feinskala.py), Ausgabe in ergebnisse/pruef\_feinskala.txt. Harte Bosonen auf 8×8 (N = 2, 3) und 12×12 (N = 2, 3), exakte Grundzustände, λ\_min(b) und μ̄ exakt.

| Prüfung                                                                                          | Fälle                                                         | Ergebnis                                                              |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------|
| gemischte Neumann-Zerlegung: ℒ\_N − Σ\_Q λ\_min(b\_Q) n\_Q 1{n\_Q ≥ 2} ≥ 0                       | b = 4 und 6, b₁ = 2 und 3, 12 Fälle                           | kleinster Eigenwert +0,019 bis +0,152                                 |
| Lemma F2                                                                                         | R = 1 und 2, λ = 0,5; 1; 2                                    | erfüllt, Spielraum Faktor 4 bis 300                                   |
| Lemma F1 bei festem h, mit abgezählten Kästen                                                    | 14 Geometrien, h = 0 bis 1,5, gekippte und zufällige Zustände | erfüllt, kleinster Abstand +0,72                                      |
| scharfe Zwischenstufe: E(Φ) − E\_N ≥ E[Σ\_Q λ\_min(b\_Q) n^in\_Q 1{n^in\_Q ≥ 2}] − μ̄ E[j] − F\_h | dieselben                                                     | erfüllt, kleinster Abstand +0,05 (bei Φ = ψ)                          |
| Lemma F6, scharfe Form im gestörten Grundzustand                                                 | 3 Systeme, W = wχ mit w = 0,02 bis 0,5                        | erfüllt, kleinster Abstand +0,05                                      |
| Lemma 6.8 für ein Zeitfenster: E exp(∫w n\_χ) ≤ exp(Δ(E₀(H) − E₀(H − w n\_χ)))                   | dieselben, Δ = 0,5 und 2                                      | erfüllt; Schranke 0,01 % bis 3 % über dem Moment                      |
| Lemma F8, Schalengewichte: p\_u(x, y) ≤ 2^{−i} a\_{k,i} mit dem exakten Kern; S₂, S₃             | i ≤ 17, k ≤ 13, je 5 Zeiten                                   | erfüllt (größtes Verhältnis 1,000 in Schale 0); S₂ = 184,6, S₃ = 4179 |
| Lemma F8, Überdeckung (Schritt 2 bis 4)                                                          | 28 800 zufällige Fälle                                        | kein Fehler                                                           |
| Lemma F8, Schalenformel (Schritt 1) und Kurzzeit-Schranke (Schritt 4) auf zufälligen Linien      | 400 schnelle Linien; 590 Linien mit (G4)                      | erfüllt (1,13 ≤ 375; 0,077 ≤ 97)                                      |
| Lemma P5″: P(Treffer) ≤ 𝔏/min g                                                                  | 12×12-Torus, 1 bis 3 Linien, diffusiv und heranlaufend        | erfüllt (z. B. 0,056 ≤ 0,106; 0,204 ≤ 0,319)                          |
| Lemma F11a (Doob), exakt mit Absorption bei ±a                                                   | 44 Fälle mit a ≤ 64; dazu β = 16 bis 400                      | erfüllt (größtes Verhältnis 0,35; bei β = 400: 0,0016 ≤ 0,0136)       |
| (G4′) ⇒ (G4); Überdeckung durch die zwei Zeitgitter                                              | 141 Zufallsbahnen; 20 000 Intervalle                          | kein Fehler                                                           |
| Brückenkern (W2), (W3) gegen den exakten Kern                                                    | 45 Fälle, Dauer 40 bis 2500                                   | erfüllt (Verhältnisse 0,08 und 0,01; untere Schranke mit Faktor 12,6) |
| Schlauch-Schritt in Lemma P6b″ und Randdichte der Brücke                                         | τ′ = 64 bis 1024, 1296 Lagen                                  | Wahrscheinlichkeit ≥ 0,039 (c₂ = 0,001); Randdichte ≤ 0,24/τ′         |

- Die abgezählte Form von Lemma F1 ist in so kleinen Systemen fast leer, weil der Abzug c\_{b₁}|V⁺|/b₁² alles überwiegt. Aussagekräftig sind die scharfen Zwischenstufen: Sie haben Spielraum von der Größe μ̄ und prüfen Vorzeichen und Faktoren der Lokalisierung, des Außenteils und der Zerlegung.
- Bei Lemma P5″ wird das Infimum von g nur an den Schrittgrenzen der Linien gesucht.
- Nebenbei: λ\_min(b) ≥ π/(2b² ln b) gilt auch für b = 2 und 3 (0,586 gegen 0,567; 0,176 gegen 0,159).
- Bei Lemma F8 sind die Bausteine geprüft, nicht die Endformel: Mit Faktoren wie 10⁷ ist sie in jedem rechenbaren Beispiel trivial erfüllt. Die Schalenformel aus Schritt 1 liegt in den Beispielen um den Faktor 300 bis 1000 über dem exakten 𝔏.
- Die Sätze F3, F7, F10, F11, Folgerung F9 und Lemma P6″ sind in erreichbaren Systemen nicht prüfbar: Sie werden erst für ln(1/ρ) ≥ 64/(Hθ) nichtleer. Geprüft sind ihre Bausteine. Die Doob-Schranke aus Lemma F11a ist erst ab β ≈ 100 kleiner als 1.

## F.14 Was offen bleibt

1. **K1 selbst.** Die drei Teile des Befunds sind beantwortet: Dichte unterhalb der Zellskala (F.2–F.8), kein Zirkel zwischen C₀ und θ (F.10.4, F.12.6), (G3) und C₁ entfallen (F.9–F.11). Lemma P6 ist mit den neuen Bedingungen bewiesen (F.12), und ihre Seltenheit steht in Satz F10 und Satz F11.
2. **Geerbt von Satz T2.** Satz F11 benutzt Satz T2 mit einem weiteren Fach und einem Gewicht w. Er gilt, soweit Satz T2 gilt (Eingänge in satz\_3\_9 §10.7, dazu Review W6). Dass D4 auch Stücke erfasst, die den Kasten nur durchlaufen, ist dort nicht ausgeschrieben (F.11.3, zweite Bemerkung).
3. **Gute Endpunkte.** Lemma P6″ verlangt, dass S und Y′ gut sind. Das war Befund K3 des Reviews (Lochstück j₀). Er ist in [anhang\_lochstueck.md](anhang_lochstueck.md) (Anhang L) beantwortet: Mit der Wählbarkeit über zwei Scheiben ist auch das Ende des Lochstücks isoliert. K2 (Satz P3 nur für feste Markenmengen) ist in [anhang\_unzugaenglich.md](anhang_unzugaenglich.md) (Anhang U) beantwortet; dort wird Lemma F13 für die Entkopplung gebraucht.
4. **Konstanten.** θ\_P ist von der Ordnung 10⁻²⁶ ε\_P², und ε\_P enthält e^{−CA²}. Damit ist n = K/θ riesig, ζ² von der Ordnung (352n)^{−133}, D\_K ≈ (17 n ln n)^{1/2}, und die Defektraten gehen nur sehr langsam gegen 0. Die Schwelle ρ\* wird nochmals viel kleiner als in G.12.8 geschätzt. Für eine vernünftige Schwelle bräuchte man eine scharfe Dichteschranke (Unter-Poisson, satz\_3\_9 §7), bessere Überdeckungen und ein Ausnahmeereignis, das auch die Lage der Brücke begrenzt.
5. **Eingearbeitet am 2026-11-12:** Anhang P (P.7.1 Bedingungen, P.7.3, P.7.5 mit Verweis auf die Beweise hier, Lemma P7), satz\_3\_9 (§9 D6 und D7, §10 Fach G4 statt R3, §12.4), Anhang K (K.4), Anhang Z (Satz Z, Z.3, Z.9), Anhang G (G.12.5, G.12.8, G.12.9), Tutorial §10 und README. Die Beweise stehen nur hier.
