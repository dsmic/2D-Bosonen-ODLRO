# Anhang U: Unzugängliche Stücke sind selten, ohne zurückgehaltene Gruppe

Stand 2026-11-12. Antwort auf die Befunde K2 und W2 in [review\_2026-11-11.md](review_2026-11-11.md). Gehört zu [anhang\_ausweichen.md](anhang_ausweichen.md) P.1–P.5 (Satz P3), zu [satz\_3\_9\_dichteschranken.md](satz_3_9_dichteschranken.md) §9 (Defektgrund D5) und §10 (Satz T2), zu [anhang\_gegenluecke.md](anhang_gegenluecke.md) G.12.1 und zu [anhang\_zweites\_moment.md](anhang_zweites_moment.md) Z.3, Z.5, Z.9. Benutzt Lemma F13 aus [anhang\_feinskala.md](anhang_feinskala.md) und die Regeln aus [anhang\_lochstueck.md](anhang_lochstueck.md). Kennzeichnung: [S] bewiesen, [B] Beweisskizze, [N] numerisch. Die Änderungen sind am 2026-11-12 eingearbeitet (U.9).

## Auf einer Seite

- **Problem (K2).** Satz P3 sagte: Für jede aus dem offengelegten Datum bestimmte Menge A von Gruppenteilchen ist P(alle unzugänglich) ≤ e^{−κ|A|}. Bewiesen war das nur für eine feste Menge von Marken (Lemma P2 lässt bestimmte Teilchen frei springen). Welche Teilchen in einer Zelle sitzen, hängt aber von der Konfiguration ab. Summiert man über alle Markenmengen, entsteht ein Faktor (N über |A|).
- **Problem (W2).** Die Umsteige-Teilchen sollten aus einer zurückgehaltenen Gruppe von M Teilchen je Zelle kommen. Die Kosten geteilter Teilchen wurden aber mit 1/n\_Q gerechnet, n\_Q ~ m. Beides zugleich geht nicht, und die Gruppe kam in Dichteformel und zweitem Moment nicht vor.
- **Abhilfe 1: keine Gruppe, starke Zugänglichkeit.** Ein Stück heißt zugänglich, wenn seine freie Brücke *allen* anderen Stücken der Scheibe mit Wahrscheinlichkeit ≥ p\* ausweicht. Das ist eine Eigenschaft der Konfiguration; eine Gruppe und ein offengelegtes Datum braucht man dafür nicht. Gewählt wird unter allen wählbaren Stücken der Zelle, also unter etwa n\_Q Stücken. Damit stimmen die Kosten 1/n\_Q.
- **Abhilfe 2: Zählen mit Binomialmomenten (Satz U).** Für die Zahl X\_Q der regulären, aber unzugänglichen Stücke einer Zelle gilt E[Π\_Q (X\_Q über k₀)] ≤ (C\_U m e^{−κ}/k₀)^{k₀|𝒜|}. Die Summe über die Markenmengen ist darin enthalten: Sie wird, wie in Satz T2, von einem gefärbten Operator getragen, und die Dichteschranke liefert den Faktor m^{k₀} je Zelle, der gegen die Zahl der Auswahlen (n\_Q über k₀) aufgeht.
- **Der neue Schritt (Lemma U1).** Stark unzugängliche Stücke können einander blockieren, und dann zählt die Kippidentität nicht für jedes einen Faktor p\*. Weil zwei reguläre Stücke sich nur mit Wahrscheinlichkeit P\_treff → 0 treffen, sind bei beschränkt vielen markierten Stücken je Zelle alle auch gegen die *unmarkierten* allein unzugänglich, mit Schwelle 3p\* statt 2p\*. Danach faktorisiert alles.
- **Ergebnis.** P(in allen Zellen von 𝒜 sind mindestens (ε/4) b₋ m Stücke unzugänglich) ≤ e^{−k₀|𝒜|}, mit κ = κ\_U fest und k₀ ~ ln(1/ρ)/ln ln(1/ρ) → ∞. Die Rate von D5 geht also mit ρ gegen 0; bisher war sie nur eine feste kleine Zahl.
- **Preis.** Die Zugänglichkeit hängt jetzt von den Bahnen der Nachbarn ab und ändert sich, wenn der Staffellauf Stücke umhängt. Die Stabilität (Z.5) braucht deshalb zwei Schwellen, p\* im Zeugen und 2p\* im Bezugszustand, wie OpenAI bei den Scores (Lemma U4). Die Gruppengröße M entfällt als Konstante.

| Teil                                                      | Stand                               | Prüfung                            |
|-----------------------------------------------------------|-------------------------------------|------------------------------------|
| Lemma U1 (Entkopplung)                                    | [S, gegeben Lemma F13]              | pruef\_unzugaenglich.py, exakt [N] |
| Lemma U2 (Kippidentität für feste Markenmengen, Kernform) | [S]                                 | pruef\_unzugaenglich.py, exakt [N] |
| Lemma U3 (gefärbter Operator für einen vorgegebenen Kern) | [S, gegeben satz\_3\_9 §10.3–§10.6] | –                                  |
| Satz U (Binomialmomente, viele Zellen und Scheiben)       | [S, gegeben U1–U3]                  | –                                  |
| Lemma U4 (Monotonie, Randschranke, zwei Schwellen)        | [S, gegeben Lemma F13]              | –                                  |
| Folgen für Auswahl, Stabilität und Konstanten (U.7)       | [B], wie G.12.5–G.12.7 und Anhang Z | –                                  |

## U.0 Die beiden Befunde

**K2.** Lemma P1 (Kippidentität) und Lemma P2 (Spektralschranke) gelten für eine feste Menge A von Marken: P(alle i ∈ A unzugänglich) ≤ (p\*)^{|A|} Z^{A frei}/Z\_N ≤ e^{−κ|A|}. Für den Defektgrund D5 braucht man aber eine Aussage über „die Teilchen der Zelle Q“. Das sind von der Konfiguration abhängige Marken, und der Kern, der zu einer solchen Menge gehört, ist kein Produkt der Operatoren aus Lemma P2. Für ein einzelnes festes Teilchen stimmt alles: E[1/a\_i] ≤ e^{δμ̄}.

**W2.** Mit einer Gruppe von M Teilchen je Zelle teilen zwei Schleifen ein Teilchen mit Wahrscheinlichkeit ~ 1/M, nicht 1/m. Das Gerüst von Anhang Z folgt aber OA §10 (keine Gruppen), und die Gruppe war nur aus der Hartkugel-Arbeit (OAH §7) übernommen. Dort hat sie zwei Aufgaben: Sie macht die Zugänglichkeit zu einer Eigenschaft des festgehaltenen Rests, und sie begrenzt die Zahl der möglichen Stoßpartner unter den nicht festgehaltenen Stücken auf CM. Bei uns begrenzt schon die Route die Zahl der geänderten Stücke in Reichweite (je Route ein gewähltes Stück je Zelle). Die erste Aufgabe übernimmt die Monotonie: Wer allen Stücken ausweicht, weicht jeder Teilfamilie aus.

## U.1 Definitionen

Alles bezieht sich auf eine Scheibe k der Dauer δ. B\_i ist das Gesetz der freien Brücke zwischen den Endpunkten S\_i, E\_i des Stücks i. Für eine Familie F fester Stücke ist

```text
a_i(F)  =  B_i( cut und weicht F aus )
```

mit cut wie in G.0: Das Stück verlässt die Kugel vom Radius Rs um sein Ende nicht, R ≥ D. In Anhang P, P.1, stand a\_i für die Ausweichwahrscheinlichkeit ohne cut; sie ist höchstens um η\_D = B\_i(cut verletzt) größer. Mit cut hängt a\_i(F) nur von den Stücken von F ab, die die Kugel vom Radius Rs um E\_i betreten; erfüllt ein solches Stück die Makro-Bedingung, liegt sein Ende höchstens (R + D)s von E\_i. Das macht die Zugänglichkeit lokal, wie die Fernkürzung und das gemeinsame Fern-Auswahlprodukt es brauchen.

- **Regulär⁺** heißt ein Stück, wenn es regulär ist (Tests 1 bis 3 aus G.5.1: beide Endpunkte isoliert, Makro-Bedingung mit Radius Ds, Randintervalle) und seine Bahn (G2\_A) und (G4′) erfüllt (Anhang F, F.11.1). Das sind Eigenschaften des Stücks selbst und der Endpunkte der anderen.
- **Zugänglich** heißt ein Stück i, wenn a\_i(F\_i^{alle}) ≥ p\*, mit der Familie F\_i^{alle} aller anderen Stücke der Scheibe und p\* = e^{−δμ̄−κ}. **Streng zugänglich** heißt es, wenn a\_i(F\_i^{alle}) ≥ 2p\*.
- **Wählbar** ist ein Stück, das regulär⁺ und zugänglich ist. Gewählt wird gleichverteilt unter den wählbaren Stücken der Zelle; für j\_m im Aufweg unter denen mit regulärer Fortsetzung (Anhang L). Eine zurückgehaltene Gruppe gibt es nicht.
- **Zählgröße:** X\_{Q,k} ist die Zahl der Stücke der Scheibe k mit Ende in Q, die regulär⁺, aber nicht streng zugänglich sind.
- **Defektgrund D5** für die Raum-Zeit-Zelle (Q, k): X\_{Q,k} ≥ (ε/4) b₋ m.
- **Treffwahrscheinlichkeit.** P^{br}\_treff ist das Supremum von B\_i(trifft ω) über alle regulären⁺ Stücke i und alle festen Bahnen ω mit (G2\_A) und (G4′), deren Endpunkte zu beiden Zeiten den Abstand > r von denen von i haben. Nach Lemma F13 und der Halbbrücken-Dichte (W1) aus F.12.2 ist

  ```text
  P^br_treff  ≤  16π e^{1/2} e^{D²/2} · C_P · ( ln(32 K β ln(1/ρ)/ζ²) + o(1) ) / log₂(τ/A²)   →  0        (ρ → 0)
  ```

**Bedingung an k₀.** Die ganze Zahl k₀ ≥ 1 erfüllt

```text
k₀ (2R + 2D + 3)² · P^br_treff  ≤  p*
```

Für ρ → 0 darf k₀ wie ln(1/ρ)/ln ln(1/ρ) wachsen. Die Bedingung an D aus P.1 (η\_D ≤ p\*/2) wird nicht mehr gebraucht, weil cut schon in a\_i steht.

## U.2 Lemma U1: Entkopplung [S, gegeben Lemma F13]

**Lemma U1.** Sei A eine Menge von Stücken einer Scheibe. Alle seien regulär⁺, und in jeder Zelle mögen höchstens k₀ von ihnen enden. Sei q₀ > 0 und a\_i(F\_i^{alle}) < q₀ für jedes i ∈ A. Dann gilt für jedes i ∈ A

```text
a_i(F_{A^c})  <  q₀ + p*
```

wobei F\_{A^c} die Familie der Stücke außerhalb von A ist.

*Beweis.* Es ist F\_i^{alle} = F\_{A^c} ∪ (A \ {i}). Eine Brücke, die F\_{A^c} ausweicht, weicht entweder auch allen Stücken von A \ {i} aus oder trifft eines davon:

```text
a_i(F_{A^c})  ≤  a_i(F_i^alle)  +  Σ_{j ∈ A, j ≠ i} B_i( cut und trifft ω_j )
```

- *Nahe Stücke* (|E\_i − E\_j|\_∞ ≤ (R + D)s): Ihre Enden liegen in höchstens (2R + 2D + 3)² Zellen, es sind also höchstens k₀ (2R + 2D + 3)² Stück. Jedes ist regulär⁺, und die Endpunkte von i und j sind getrennt (Test 1). Also ist jeder Summand ≤ P^{br}\_treff, zusammen ≤ p\*.
- *Ferne Stücke* (|E\_i − E\_j|\_∞ > (R + D)s): ω\_j bleibt in der Kugel vom Radius Ds um E\_j, und die Brücke von i mit cut bleibt in der Kugel vom Radius Rs um E\_i. Sie können sich nicht treffen. ∎

**Warum man das braucht.** Zwei Stücke können einander blockieren. In einem kleinen Modell sieht man das deutlich (U.8): Dort sind Paare, in denen beide Stücke gegen alle anderen unzugänglich sind, häufiger als Paare, in denen beide gegen den Rest ohne das Paar unzugänglich sind. Die Kippidentität zählt aber nur die zweite Sorte mit einem Faktor je Stück. Im Beweisbereich ist die gegenseitige Blockade durch P^{br}\_treff → 0 beschränkt, solange nur beschränkt viele markierte Stücke in Reichweite sind. Deshalb arbeitet Satz U mit Binomialmomenten fester Ordnung k₀ und nicht mit Exponentialmomenten.

## U.3 Lemma U2: Kippidentität für feste Markenmengen [S]

Das ist Lemma P1 aus Anhang P, als Ungleichung zwischen Scheibenkernen geschrieben und mit Endpunkt-Bedingungen.

**Lemma U2.** Seien x und x′ Konfigurationen der N markierten Teilchen zu den Zeiten t\_k und t\_{k+1}, A eine feste Menge von Marken, q ∈ (0, 1] und U eine Menge von Plätzen. Dann gilt

```text
Σ_{Geschichten von x nach x′}  Gewicht · Π_{i∈A} 1{ E_i ∈ U,  |S_i − E_i|_∞ ≤ Ds,  cut_i,  a_i(F_{A^c}) < q }
        ≤  q^{|A|} · [e^{−δ ℒ_{A^c}}](x_{A^c}, x′_{A^c}) · Π_{i∈A} p_δ(x_i, x′_i) 1{ x′_i ∈ U,  |x_i − x′_i|_∞ ≤ Ds }
```

Rechts steht der Hartkern-Kern der Teilchen außerhalb von A und für jedes i ∈ A der freie Kern, ohne jede Wechselwirkung.

*Beweis.* Das Gewicht einer Geschichte ist das Produkt der Gewichte der Stücke mal der Anzeige „kein Stoß“. Man lässt alle Stöße weg, an denen ein Stück von A beteiligt ist, außer dem Ausweichen jedes i ∈ A vor F\_{A^c}. Bei festem F\_{A^c} sind die Stücke von A dann unabhängig, und die Summe über die Bahnen von i mit cut gibt p\_δ(x\_i, x′\_i) a\_i(F\_{A^c}). Die Anzeige a\_i(F\_{A^c}) < q hängt nur von F\_{A^c} und den Endpunkten ab; auf ihr ist der Faktor < q. Die Summe über F\_{A^c} gibt den Hartkern-Kern. ∎

- Für eine feste Menge A und U = Λ folgt daraus nach dem Mitteln über die Ränder Lemma P1 (dort ohne cut; der Beweis ist derselbe).
- Ohne die Anzeigen und ohne cut gilt Gleichheit im Mittel: E[Σ 1/Ξ\_A(F\_{A^c})] = Σ Z^{A frei}/Z\_N, mit der gemeinsamen Ausweichwahrscheinlichkeit Ξ\_A der Stücke von A vor F\_{A^c} und voreinander. Das ist in U.8 exakt geprüft, für einzelne Stücke und für Paare.

## U.4 Lemma U3: gefärbter Operator für einen vorgegebenen Kern [S, gegeben satz\_3\_9 §10.3–§10.6]

Satz T2 zählt Stücke, die einen Fehler ihrer eigenen Bahn haben. Sein Beweis benutzt von diesem Fehler nur eine Schranke für den Kern eines markierten Stücks. In dieser Form:

**Lemma U3.** Sei U eine Zellvereinigung, p eine Abschneidefunktion mit p = 1 auf {d(x, U) ≤ Ds}, p = 0 außerhalb von {d(x, U) ≤ (D + 2)s} und |p(x) − p(y)| ≤ 1/s über jede Kante. Sei 0 < η ≤ 1. Für eine Menge A von Marken sei

```text
K^A_η(x, x′)  =  [e^{−δ ℒ_{A^c}}](x_{A^c}, x′_{A^c}) · Π_{i∈A}  η e^{−δμ̄ − 4} · p(x_i) p(x′_i) p_δ(x_i, x′_i)
```

Dann gilt im stationären Pfadmaß des Grundzustands

```text
e^{δ ε_N} ⟨ψ, Σ_A K^A_η ψ⟩  ≤  exp( 4 C_a ρ (2D + 7)² |U| · η )
```

Für mehrere Scheiben, jede mit eigenem U und η, gilt das Produkt der Schranken.

*Beweis.* Wie satz\_3\_9 §10.3–§10.6, mit einer markierten Farbe.

1. **Operator.** Σ\_A K^A\_η ist der Kern von T = Ṽ\* e^{−δℋ} Ṽ mit der Einbettung ṽf = (f, √η p f). Teilchen der Grundfarbe haben L\_i und den harten Kern. Ein markiertes Teilchen lebt auf ℓ²(Λ), hat den freien Operator L (c₁ = 1, kein Dirichlet-Rand) und die Lücke M = μ̄ + 4/δ, und wechselwirkt mit niemandem. Der Dirichlet-Rand aus §10.0 wird nicht gebraucht: Die Abschneidefunktion p lokalisiert die Endpunkte, und die kinetische Energie eines markierten Teilchens ist auch auf dem Torus ≥ 0.
2. **Einschub.** Mit a = ½ log(1 + ηp²) ist Ṽ = e^A Ũ mit einer Isometrie Ũ, und Lemma T3 gibt ‖T‖ ≤ exp(−δ E₀(ℋ̃)) mit W₀(x) = 2a(x)/δ + Σ\_{y∼x}(cosh(a(x) − a(y)) − 1). Es ist a ≤ η/2 und |a(x) − a(y)| ≤ η/s, also W₀ ≤ (η + 2,2 η²)/δ ≤ 3,2 η/δ wegen s² = δ.
3. **Energiebilanz.** Auf dem Sektor mit J Teilchen der Grundfarbe ist ℋ̃ ≥ E₀(ℒ\_J − ΣW₀) + (N − J)(M − ‖W₀‖\_∞) und ε\_J ≥ ε\_N − (N − J) μ̄. Wegen M ≥ μ̄ + ‖W₀‖\_∞ fallen die Sektorterme weg. W₀ verschwindet außerhalb einer Zellvereinigung B mit |B| ≤ (2D + 7)² |U|, und der Dichte-Eingang (Satz 3.9 (a^W), gleichmäßig in J) gibt ε\_J − E₀(ℒ\_J − ΣW₀) ≤ (3,2 η/δ) C\_a ρ |B|.
4. **Grundzustand und viele Scheiben:** e^{δε\_N}⟨ψ, Tψ⟩ ≤ e^{δε\_N}‖T‖, und über mehrere Scheiben das Produkt der Normen (§10.4). ∎

## U.5 Satz U: Binomialmomente der Zahl unzugänglicher Stücke

**Satz U [S, gegeben Lemma U1–U3].** Sei 𝒜 eine endliche Menge von Raum-Zeit-Zellen, k₀ wie in U.1 und m ≥ k₀/(4C\_a). Dann gilt unter dem stationären Pfadmaß des Grundzustands

```text
E[ Π_{(Q,k)∈𝒜}  ( X_{Q,k} über k₀ ) ]  ≤  ( C_U m e^{−κ} / k₀ )^{k₀ |𝒜|},        C_U = 12 e⁵ C_a (2D + 7)²
```

und für jede ganze Zahl x ≥ k₀

```text
P( X_{Q,k} ≥ x  für alle (Q,k) ∈ 𝒜 )  ≤  ( C_U m e^{−κ} / x )^{k₀ |𝒜|}
```

*Beweis.* Zuerst für eine Scheibe; U sei die Vereinigung der Zellen von 𝒜 und K = k₀|𝒜|.

1. **Binomialmoment als Summe über Markenmengen.** Π\_Q (X\_Q über k₀) ist die Zahl der Mengen A von Stücken, die in jeder Zelle Q ∈ 𝒜 genau k₀ Stücke mit Ende in Q enthalten, alle regulär⁺ und nicht streng zugänglich.
2. **Entkoppeln.** Für eine solche Menge gibt Lemma U1 mit q₀ = 2p\*: a\_i(F\_{A^c}) < 3p\* für jedes i ∈ A. Außerdem ist E\_i ∈ U, |S\_i − E\_i|\_∞ ≤ Ds, und das Stück erfüllt cut (Makro-Bedingung, R ≥ D).
3. **Kippen.** Nach Lemma U2 mit q = 3p\* ist der Beitrag von A zum getesteten Scheibenkern elementweise ≤ dem Kern rechts in Lemma U2. Summiert man über alle Mengen A mit |A| = K (nicht nur die mit genau k₀ je Zelle), wird die Schranke nur größer.
4. **Erzeugende Funktion.** Für z > 0 sei η = 3 e⁴ z e^{−κ}; dann ist z · 3p\* p\_δ(S, E) 1{E ∈ U, |S − E|\_∞ ≤ Ds} ≤ η e^{−δμ̄−4} p(E) p(S) p\_δ(S, E), weil p\* e^{δμ̄} = e^{−κ} ist und p auf den Trägern gleich 1. Die Summe aus Schritt 3 ist also höchstens z^{−K} mal dem Anteil von Σ\_A K^A\_η mit |A| = K. Alle Anteile sind ≥ 0, und Lemma U3 gibt

   ```text
   E[ Π_Q (X_Q über k₀) ]  ≤  z^{−K} · exp( 12 e⁴ C_a (2D + 7)² m |𝒜| · z e^{−κ} )        für η ≤ 1
   ```

5. **Optimieren.** Mit z = k₀ e^{κ}/(12 e⁴ C\_a (2D + 7)² m) ist η = k₀/(4 C\_a (2D + 7)² m) ≤ 1, und die rechte Seite ist (C\_U m e^{−κ}/k₀)^K.
6. **Markov.** Aus X ≥ x ≥ k₀ folgt (X über k₀) ≥ (x über k₀) ≥ (x/k₀)^{k₀}.
7. **Viele Scheiben.** Die Schritte 1 bis 3 gelten in jeder Scheibe für sich, weil Zugänglichkeit nur Stücke derselben Scheibe betrifft. Der getestete Kern des ganzen Fensters ist das Produkt der Scheibenkerne, und Lemma U3 gibt das Produkt der Schranken. Man wählt in jeder Scheibe dasselbe z. ∎

**Folgerung (D5).** Sei

```text
κ  ≥  κ_U  :=  ln( 4 e C_U / (ε b₋) )  =  ln( 48 e⁶ C_a (2D + 7)² / (ε b₋) )
```

Dann gilt für jede Menge 𝒜 von Raum-Zeit-Zellen

```text
P( in jeder Zelle von 𝒜 sind mindestens (ε/4) b₋ m reguläre⁺ Stücke nicht streng zugänglich )  ≤  e^{−k₀ |𝒜|}
```

- Die Summe über die Markenmengen kostet nichts mehr: Der Faktor (C\_U m)^{k₀} aus der Dichteschranke geht gegen (x über k₀) ~ (ε b₋ m/(4k₀))^{k₀} auf, und m fällt heraus.
- κ\_U ist eine feste Zahl. Sie hängt logarithmisch von D ab; eine Bedingung an D entsteht hier nicht.
- Die Rate von D5 ist e^{−k₀} mit k₀ ~ p\* ln(1/ρ)/ln ln(1/ρ). Sie geht für ρ → 0 gegen 0. Die frühere Schranke (2^M e^{−κεM})^{|𝒜|} war eine feste kleine Zahl und verlangte κ > (ln 2)/ε + 1.
- Die Schranke hat die Normform je Scheibe, die Satz D zum Mischen der Defektgründe braucht (satz\_3\_9 §9.3).

## U.6 Lemma U4: Monotonie, Randschranke und zwei Schwellen [S, gegeben Lemma F13]

**Lemma U4.** Sei i ein reguläres⁺ Stück.

1. **Monotonie.** Aus F′ ⊂ F folgt a\_i(F′) ≥ a\_i(F).
2. **Wenige Stücke ändern wenig.** Entsteht F′ aus F, indem man höchstens n′ Stücke hinzufügt und beliebig viele wegnimmt, und sind die hinzugefügten Bahnen regulär im Sinn von (G2\_A) und (G4′) mit Endpunkten im Abstand > r von denen von i, so ist a\_i(F′) ≥ a\_i(F) − n′ P^{br}\_treff.
3. **Randschranke.** Sei i zugänglich. In einem normierten Gesetz, in dem das Stück i eine freie Brücke mit cut ist, bedingt darauf, einer Familie F″ auszuweichen, die aus beliebigen anderen Stücken der Konfiguration und höchstens n′ weiteren Bahnen wie in Punkt 2 besteht, hat i bezüglich B\_i die Dichte

   ```text
   ≤  1 / ( p* − n′ P^br_treff )  ≤  2/p*        sobald  n′ P^br_treff ≤ p*/2
   ```

4. **Zwei Schwellen.** Zwei Zustände mögen sich in höchstens n′ Stücken in Reichweite von i unterscheiden, alle wie in Punkt 2, und es sei n′ P^{br}\_treff ≤ p\*. Ist i im einen Zustand streng zugänglich, so ist es im anderen zugänglich.

*Beweis.* (1) Weniger Hindernisse. (2) Wegnehmen erhöht a\_i nach (1); jedes hinzugefügte Stück senkt a\_i höchstens um die Wahrscheinlichkeit, es zu treffen. (3) Die Dichte ist 1{…}/a\_i(F″), und a\_i(F″) ≥ a\_i(F\_i^{alle}) − n′ P^{br}\_treff nach (1) und (2). (4) Nach (2), in beiden Richtungen angewandt, ist |a\_i − a\_i′| ≤ n′ P^{br}\_treff ≤ p\*. ∎

**Wozu.**

- Punkt 3 ist die Ein-Stück-Randschranke aus Z.3 für Stücke mit ihren eigenen Endpunkten. Sie brauchte bisher die Gruppe: Zugänglichkeit bezog sich auf den festgehaltenen Rest F, und das Ausweichen vor anderen Gruppenstücken war nicht ausgeschrieben (Review H7). Jetzt deckt die starke Zugänglichkeit jede Teilfamilie, und die wenigen neu gezogenen Stücke in Reichweite kosten n′ P^{br}\_treff.
- Punkt 4 ersetzt die exakte Invarianz, die die Gruppe gab („der Staffellauf ändert nur Gruppenstücke, F bleibt fest“). Die Zahl n′ der geänderten Stücke in Reichweite ist durch die Routen beschränkt, n′ ≤ C(R\*), und P^{br}\_treff → 0.

## U.7 Was sich ändert [B]

1. **Auswahl (G.12.1, Z.0).** Keine Gruppe und kein offengelegtes Datum. Die Umsteige-Teilchen werden gleichverteilt unter den wählbaren Stücken der Zelle gewählt, wählbar = regulär⁺ und zugänglich. In guten Zellen sind das mindestens (1 − ε) n\_Q Stücke, für j\_m mindestens (1 − 2ε) n\_Q (Lemma L2).
2. **Kosten geteilter Teilchen (W2).** Zwei Schleifen wählen in einer Zelle dasselbe Stück mit Wahrscheinlichkeit ≤ 1/((1 − 2ε) n\_Q). Der Beitrag (e^{C(K)} − 1)/(b₋ m) in κ₀ und die Kopfstück-Reihe mit C/m in G.12.7 und Z.8 stimmen damit; eine Bedingung M ≳ e^{C(K)}/α gibt es nicht.
3. **Defektgrund D5** wie in U.1, mit der Rate e^{−k₀} aus der Folgerung.
4. **Stabilität (Z.5).** Zugänglichkeit im Zeugen (C, Ĉ) mit der Schwelle p\*, im Bezugszustand B und in Satz D mit 2p\*. Nach Lemma U4 (4) ist ein in B streng zugängliches, ungeändertes Stück in jedem Zeugen zugänglich. Die Zahl der wählbaren Stücke im Zeugen ist also mindestens die strenge Zahl in B minus die beschränkt vielen Stücke, deren Regularität sich ändert. Fern von allen geänderten Stücken stimmen die Ausweichwahrscheinlichkeiten genau überein, weil a\_i mit cut nur von Stücken abhängt, die die Kugel vom Radius Rs um E\_i betreten.
5. **Nenner (Z.3).** Für Stücke mit ihren eigenen Endpunkten gilt die Randschranke 2/p\* nach Lemma U4 (3), für umgehängte Brücken nach Lemma P6 wie bisher.
6. **Konstanten (Z.9).** κ = κ\_U. Die Gruppengröße M und die Bedingung „2^M e^{−κεM} klein“ entfallen. C(K) = δμ̄ + κ\_U + C bleibt eine feste Zahl, und σ\_ρ = C e^{δμ̄+κ\_U} P\_treff → 0.

## U.8 Exakte Prüfung [N]

[pruef\_unzugaenglich.py](pruef_unzugaenglich.py), Ausgabe in ergebnisse/pruef\_unzugaenglich.txt. Mini-Ring wie in G.2 (6 Plätze, Trotter-Zeit, periodisch), eine Scheibe aus zwei Schritten; alle geschlossenen Geschichten werden aufgezählt, die rechten Seiten kommen aus Transfermatrizen.

| N   | λ    | E[Σ 1/a\_p] gegen Σ Z^{p frei}[a > 0]/Z | E[Σ 1/Ξ\_A] gegen Σ Z^{A frei}[Ξ > 0]/Z (Paare) | Kippungleichung, q = 0,3 bis 0,9 | Entkopplung  |
|-----|------|-----------------------------------------|-------------------------------------------------|----------------------------------|--------------|
| 3   | 0,7  | 4,13406 = 4,13406 (Fehler 6·10⁻¹³)      | 5,57722 = 5,57722 (3·10⁻¹³)                     | erfüllt                          | nie verletzt |
| 4   | 0,7  | 6,67383 = 6,67383 (2·10⁻¹³)             | 16,36090 = 16,36090 (1·10⁻¹³)                   | erfüllt                          | nie verletzt |
| 2   | 0,9  | 2,53849 = 2,53849 (1·10⁻¹³)             | 1,55420 = 1,55420 (6·10⁻¹⁴)                     | erfüllt                          | nie verletzt |
| 3   | 0,35 | 3,32535 = 3,32535 (2·10⁻¹³)             | 3,66772 = 3,66772 (7·10⁻¹⁴)                     | erfüllt                          | nie verletzt |

- Geprüft ist Lemma U2 in der scharfen Form: Die Identität für einzelne Stücke und für Paare stimmt auf 13 Stellen. In Trotter-Zeit gibt es Umgebungen, denen eine Brücke gar nicht ausweichen kann; sie sind rechts ausgenommen. In stetiger Zeit gibt es sie nicht.
- Die Kippungleichung E[#Paare, beide mit a(F\_{A^c}) < q] ≤ q² Σ Z^{A frei}/Z\_N gilt in allen Fällen.
- Lemma U1 ist eine Ungleichung je Geschichte und nie verletzt. Wie nötig es ist, zeigt das Modell auch: Bei N = 3, λ = 0,7 und q = 0,5 ist die erwartete Zahl der Paare, in denen beide Stücke gegen *alle* anderen unzugänglich sind, 0,053; gegen den Rest ohne das Paar sind es nur 0,006. Die Stücke blockieren einander (größte Treffwahrscheinlichkeit 0,67). Im Beweisbereich ist diese Wahrscheinlichkeit P^{br}\_treff → 0.
- Nicht prüfbar sind Lemma U3 und Satz U selbst; sie sind erst für m ≫ k₀ nichtleer. Lemma U3 ist Satz T2 mit einem anderen Kern; dessen Einschub ist in pruef\_lipschitz.py exakt geprüft.

## U.9 Was offen bleibt, und was eingearbeitet ist

1. **K2 und W2** sind damit beantwortet: Die gemeinsame Seltenheit unzugänglicher Stücke gilt für die Stücke der Zellen selbst, nicht nur für feste Marken, und die Gruppe entfällt.
2. **Geerbt von Satz T2.** Lemma U3 benutzt Lemma T3 (Gitter-Einschub) und den Dichte-Eingang Satz 3.9 (a^W); beide sind [S]. Die Gauß-Vergleiche und die Lokalisierung aus §10.2, die Satz T2 selbst braucht, kommen hier nicht vor.
3. **Stufe der Buchführung.** U.7 ist eine Skizze auf dem Stand von Anhang Z. Die zwei Schwellen in Z.5 und die Lesart mit cut sind nicht Zeile für Zeile durch das zweite Moment verfolgt.
4. **Konstanten.** κ\_U enthält ln(C\_a D²/(ε b₋)) und ist mit dem riesigen D aus Anhang F groß; p\* = e^{−δμ̄−κ\_U} bleibt eine feste Zahl. Für eine Schwelle ist das so unbrauchbar wie der Rest.
5. **Eingearbeitet am 2026-11-12:** Anhang P (P.1, P.2, P.4, P.5), satz\_3\_9 (§9.1, §9.2, §9.3, §9.5, §12.4), Anhang G (G.12.0, G.12.1, G.12.5, G.12.6), Anhang Z (Satz Z, Z.0, Z.3, Z.5, Z.9, Z.10), Anhang L (L.1, L.3, L.7), Anhang F (F.14), Tutorial §10, README und Review.
