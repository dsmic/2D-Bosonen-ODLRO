# Anhang P: Ausweichen beim harten Kern (zugängliche Teilchen statt Lemma P\*)

Stand 2026-11-10 abends; P.7 am 2026-11-12 an [anhang\_feinskala.md](anhang_feinskala.md) (Anhang F) angepasst, als Antwort auf Befund K1 in [review\_2026-11-11.md](review_2026-11-11.md); P.1 und P.4 am selben Tag an [anhang\_unzugaenglich.md](anhang_unzugaenglich.md) (Anhang U, Antwort auf K2 und W2: keine zurückgehaltene Gruppe mehr). Gehört zu [tutorial\_beweis\_verduennt.md](tutorial_beweis_verduennt.md) §10, Punkte 1, 3 und 4, und ersetzt [anhang\_gegenluecke.md](anhang_gegenluecke.md) G.6.2 (W2) sowie G.11.5. Vorbild ist §7 der OpenAI-Arbeit zum Hartkugelgas bei T > 0 (OAH), dort „accessible labels“. Kennzeichnung: [S] bewiesen, [B] Beweisskizze, [N] numerisch.

## Auf einer Seite

- **Problem.** OpenAI schätzt fehlende Wechselwirkungen mit Jensen ab, E e^{−V} ≥ e^{−EV}. Beim harten Kern ist der Faktor eine Indikatorfunktion, und Jensen gibt nichts. Die Ersatzskizze G.6.2 (Zeitzerlegung) brauchte eine Untergrenze für *jede* feste Umgebung. Die gilt so nicht: Eine Umgebungslinie, die auf den Startpunkt zuläuft, hebt die Treffwahrscheinlichkeit von ≈ ln ln(1/ρ)/ln(1/ρ) auf ≈ 1/2 (G.11.5).
- **Ausweg wie bei OAH.** Die Ausweich-Untergrenze wird Teil der Auswahl: Nur **zugängliche** Teilchen werden zum Umsteigen benutzt, also solche, deren freie Brücke allen anderen Stücken der Scheibe mit Wahrscheinlichkeit ≥ p\* ausweicht. Zu zeigen ist dann nur, dass unzugängliche Teilchen selten sind, gemeinsam über viele Zellen. Anders als bei OAH gibt es keine zurückgehaltene Gruppe (Anhang U).
- **Neu gegenüber OAH:** OAH zeigt die Seltenheit mit einer Vereinigungsschranke über Hindernisse; das geht dort, weil die Stücke kurz sind und die Erfolgswahrscheinlichkeit ≥ 0,9 ist. Bei uns ist sie typisch e^{−2πK}. Wir benutzen stattdessen eine exakte Kippidentität (Lemma P1) und eine Spektralschranke (Lemma P2).
- **Ergebnis für feste Marken (Lemma P1, P2) [S]:** P(alle Teilchen einer festen Menge A von Marken sind unzugänglich) ≤ e^{−κ|A|}, mit p\* = e^{−δμ̄ − κ} ≈ e^{−8πK − κ}.
- **Ergebnis für die Stücke der Zellen (Satz P3 in der Fassung von Anhang U) [S, gegeben Satz T2 §10.3–§10.6 und Lemma F13]:** P(in allen Zellen von 𝒜 sind mindestens (ε/4) b₋ m reguläre Stücke unzugänglich) ≤ e^{−k₀|𝒜|}, mit κ = κ\_U fest und k₀ → ∞ für ρ → 0. Die Fassung bis 2026-11-11 behauptete das für „jede aus dem offengelegten Datum bestimmte Menge“; bewiesen war es nur für feste Marken (Review K2).
- **Reichweite (Nachtrag, 20:20):** Satz P3 gilt für Stücke, die im Gibbs-Maß wirklich vorkommen, also für das *eigene* Stück eines Teilchens zwischen seinen Endpunkten. Das deckt den zweiten Nenner von G4 (Z[j, C]). Der Staffellauf zieht aber auch Brücken mit **umgehängten** Endpunkten (S\_l → Y\_{l−1}) und im Abweg neue Stücke. Für sie, im ersten Nenner von G4 (Z[l, O]), gibt es keine Kippidentität (P.6). Dort bleibt eine Ausweich-Untergrenze unter Umgebungsbedingungen nötig, also Lemma P\* für umgehängte Brücken. Sie ist in P.7 und Anhang F bewiesen: Lemma P5″ (Treffschranke über die gemeinsame Aufenthaltszeit), Lemma F8 (Dichte in Raum-Zeit) und Lemma P6 (Zeitzerlegung der Brücke), gegeben die Schranken des Gitterkerns; die Seltenheit der Gütebedingungen steht in Satz F10, Satz F11 und Satz D.

| Teil                                   | Stand                                                     | Prüfung                                |
|----------------------------------------|-----------------------------------------------------------|----------------------------------------|
| P1 Kippidentität                       | [S]                                                       | –                                      |
| P2 Spektralschranke Z(A frei)/Z\_N     | [S]                                                       | pruef\_zugaenglich.py, exakt [N]       |
| P3 gemeinsame Seltenheit über Zellen   | [S, gegeben Satz T2 und Lemma F13] (Anhang U, Satz U)     | Bausteine: pruef\_unzugaenglich.py [N] |
| eigene Stücke (zweiter Nenner von G4)  | [S]                                                       | Anhang U, Lemma U4 (Randschranke)      |
| umgehängte Brücken (erster Nenner)     | P5″, P6 [S] (Anhang F); Seltenheit: Satz F10, F11, Satz D | P.7, Anhang F; pruef\_feinskala.py [N] |
| neue Stücke des Abwegs (erster Nenner) | Lemma C (G.12.9) mit P6 für kurze Brücken                 | zeitschleife2d.py [N]                  |

## P.1 Rahmen

- **Scheibe k**, Dauer δ. Für ein Stück i ist B\_i das Gesetz der freien Brücke zwischen seinen Endpunkten (Rate 1 je Nachbar).
- **Ausweichwahrscheinlichkeit:** Für eine Familie F fester Stücke ist a\_i(F) = B\_i(cut und weicht F aus). In Lemma P1 und P2 unten steht dieselbe Größe ohne cut; sie ist höchstens um η\_D = B\_i(cut verletzt) ≤ e^{−cD²} größer, und die Beweise sind dieselben.
- **Umgebung:** F\_i^{alle} sind alle anderen Stücke der Scheibe.

**Definition (Fassung vom 2026-11-12, Anhang U).** Ein Stück i heißt **zugänglich**, wenn a\_i(F\_i^{alle}) ≥ p\*, und **streng zugänglich**, wenn a\_i(F\_i^{alle}) ≥ 2p\*, mit

```text
p*  =  exp( −δ μ̄ − κ ),        μ̄ = max_{j ≤ N} (ε_j − ε_{j−1}),        κ = κ_U  (Anhang U, U.5)
```

Nach Lemma 6.5 ist δμ̄ ≤ 8πK(1 + o(1)), also p\* ≈ e^{−8πK−κ}. Das ist die Form e^{−C₁(K+1)} aus G.6.1, jetzt mit expliziter Konstante.

- **Monotonie:** Wer allen anderen Stücken ausweicht, weicht jeder Teilfamilie aus. Ein zugängliches Stück hat also a\_i(F′) ≥ p\* für jedes F′ ⊂ F\_i^{alle}.
- **Zwei Schwellen:** Die Zugänglichkeit hängt von den Bahnen der Nachbarn ab. Hängt der Staffellauf wenige Stücke in Reichweite um, ändert sich a\_i höchstens um n′ P^{br}\_treff → 0 (Lemma U4). Deshalb wird im Zeugen mit p\* und im Bezugszustand mit 2p\* geprüft, wie OpenAI es bei den Scores tut.

*Frühere Fassung (bis 2026-11-11), nach OAH §7.* Aus einem offengelegten Datum (Endpunkte, Wählbarkeits-Anzeigen, Zuteilung) wurde je Zelle eine Gruppe I von höchstens M Teilchen zurückgehalten; F waren die Stücke außerhalb von I, und i ∈ I hieß zugänglich, wenn a\_i(F) ≥ p\*. Das hat zwei Mängel (Review K2 und W2): Die gemeinsame Seltenheit war nur für feste Marken bewiesen, und mit einer Gruppe von M Teilchen kosten geteilte Teilchen 1/M statt 1/n\_Q. Die Gruppe ist ersatzlos gestrichen; was sie bei OAH leistet, leisten hier die Monotonie und die Route, die die Zahl der geänderten Stücke in Reichweite begrenzt (Anhang U, U.0).

## P.2 Lemma P1: Kippidentität für Stücke

**Lemma P1 [S].** Sei A eine *feste* Menge von Marken (Teilchen und Scheibe), verteilt auf eine oder mehrere Scheiben, und F die Familie aller Stücke außerhalb von A. Unzugänglich heißt hier a\_i(F) < p\*. Z\_N^{A frei} sei die Zustandssumme, in der die Stücke von A in ihren Scheiben mit niemandem wechselwirken (kein harter Kern, keine Bedingung C\_i). Dann gilt

```text
P( alle i ∈ A sind unzugänglich )  ≤  (p*)^{|A|} · Z_N^{A frei} / Z_N
```

*Beweis.*

1. **Zerlegen.** Das Gewicht einer geschlossenen Geschichte ist W\_außen · W(F) · Π\_{i∈A} W(ω\_i) · 1{harter Kern}. Integriert man die Stücke von A aus, bleibt W\_außen · W(F) · Π\_{i∈A} Z\_i^{frei} · Ξ\_A(F) mit Ξ\_A(F) = B\_A(alle Stücke von A weichen F und einander aus).
2. **Abschätzen auf dem Ereignis.** Lässt man die Stöße der Stücke von A untereinander weg, so wird Ξ\_A(F) ≤ Π\_{i∈A} a\_i(F), weil B\_A ein Produktmaß ist. Auf dem Ereignis ist jeder Faktor a\_i(F) < p\*.
3. **Zurücksummieren.** Σ W\_außen · W(F) · Π\_{i∈A} Z\_i^{frei} ist genau Z\_N^{A frei}: Die Stücke von A sind freie Brücken ohne jede Bedingung. Teilen durch Z\_N gibt die Behauptung. ∎

*Bemerkung.* Für ein einzelnes Teilchen gilt sogar die Gleichung E[1/a\_i(F)] = Z\_N^{i frei}/Z\_N (ohne cut), und für eine Menge A ebenso E[1/Ξ\_A(F)] = Z\_N^{A frei}/Z\_N. Beides ist am Mini-Ring exakt geprüft ([pruef\_unzugaenglich.py](pruef_unzugaenglich.py), Anhang U, U.8). Wichtig ist die Einschränkung auf *feste* Marken: Für die Stücke, die gerade in einer Zelle sitzen, braucht man zusätzlich die Summe über die Markenmengen (Satz U). Die Umgebung ist unter dem Grundzustands-Pfadmaß um den Faktor a\_i gekippt; deshalb sind Umgebungen mit kleinem a\_i selten.

## P.3 Lemma P2: Spektralschranke

**Lemma P2 [S].** Für β → ∞ bei festem L, und |A\_k| freien Stücken in Scheibe k, gilt

```text
Z_N^{A frei} / Z_N  ≤  Π_k exp( δ (ε_N − ε_{N−|A_k|}) )  ≤  exp( |A| δ μ̄ )
```

*Beweis.*

1. **Markierte Teilchen.** Man schreibt alles im Raum markierter Teilchen. Nach Lemma 6.1 ist der Grundzustand der markierten Hartkern-Teilchen der bosonische ψ\_N mit Energie E\_N. Für β → ∞ ist Z\_N^{A frei}/Z\_N = ⟨ψ\_N, Π\_k P\_hk e^{−δ(H\_rel,k − E\_N)} P\_hk ⋯ ψ\_N⟩, mit den Projektionen P\_hk auf stoßfreie Konfigurationen an den Scheibenrändern und e^{−t(H − E\_N)} dazwischen.
2. **Normen.** H\_rel,k lässt die Teilchen aus A\_k frei springen; die übrigen sind untereinander hart. Seine Grundenergie ist E\_{N−|A\_k|} − 4|A\_k| (freie Teilchen haben −4). Alle Faktoren haben Norm ≤ 1 bis auf e^{−δ(H\_rel,k − E\_N)} mit Norm e^{δ(E\_N − E\_{N−|A\_k|} + 4|A\_k|)} = e^{δ(ε\_N − ε\_{N−|A\_k|})}.
3. **Teleskop.** ε\_N − ε\_{N−j} = Σ (ε\_l − ε\_{l−1}) ≤ j μ̄. ∎

**Zahlen [N]** ([pruef\_zugaenglich.py](pruef_zugaenglich.py), exakt im Raum markierter Teilchen):

| L   | N   | \|A\| | ε\_N − ε\_{N−\|A\|} | R(δ = 4) | Schranke e^{4Δε} | R(δ = 32) | Schranke e^{32Δε} |
|-----|-----|-------|---------------------|----------|------------------|-----------|-------------------|
| 4   | 3   | 1     | 0,905               | 31,7     | 37,3             | 3,20·10¹² | 3,76·10¹²         |
| 4   | 3   | 2     | 1,335               | 165      | 209              | 2,85·10¹⁸ | 3,61·10¹⁸         |
| 5   | 3   | 1     | 0,521               | 7,17     | 8,04             | 1,55·10⁷  | 1,74·10⁷          |
| 6   | 3   | 1     | 0,333               | 3,47     | 3,79             | 3,90·10⁴  | 4,27·10⁴          |
| 6   | 3   | 2     | 0,493               | 6,29     | 7,17             | 6,15·10⁶  | 7,02·10⁶          |

Die Schranke gilt überall und ist scharf bis auf den Überlapp-Faktor 0,85–0,95.

## P.4 Satz P3: Unzugängliche Teilchen sind selten

**Für feste Marken [S].** Für jede feste Menge A von Marken gilt nach Lemma P1 und Lemma P2

```text
P( alle i ∈ A sind unzugänglich gegen die Stücke außerhalb von A )  ≤  ( p* e^{δ μ̄} )^{|A|}  =  e^{−κ |A|}
```

**Satz P3 (Fassung vom 2026-11-12; in Anhang U: Satz U und Folgerung) [S, gegeben satz\_3\_9 §10.3–§10.6 und Lemma F13].** X\_{Q,k} sei die Zahl der Stücke der Scheibe k mit Ende in Q, die regulär⁺, aber nicht streng zugänglich sind (regulär⁺: Tests 1 bis 3 aus G.5.1, dazu (G2\_A) und (G4′) für die eigene Bahn). Sei k₀ ≥ 1 ganz mit k₀ (2R + 2D + 3)² P^{br}\_treff ≤ p\*. Dann gilt für jede Menge 𝒜 von Raum-Zeit-Zellen

```text
E[ Π_{(Q,k)∈𝒜} ( X_{Q,k} über k₀ ) ]  ≤  ( C_U m e^{−κ} / k₀ )^{k₀ |𝒜|},        C_U = 12 e⁵ C_a (2D + 7)²
P( X_{Q,k} ≥ (ε/4) b₋ m  für alle (Q,k) ∈ 𝒜 )  ≤  e^{−k₀ |𝒜|}        für  κ ≥ κ_U = ln( 48 e⁶ C_a (2D + 7)² / (ε b₋) )
```

*Beweisweg* (ausgeführt in Anhang U).

1. Das Binomialmoment ist die Zahl der Markenmengen mit k₀ unzugänglichen Stücken je Zelle.
2. **Entkoppeln (Lemma U1).** Solche Stücke könnten einander blockieren. Weil zwei reguläre Stücke sich nur mit Wahrscheinlichkeit P^{br}\_treff → 0 treffen und höchstens k₀ (2R + 2D + 3)² markierte Stücke in Reichweite sind, ist jedes auch gegen die unmarkierten Stücke allein unzugänglich, mit Schwelle 3p\*.
3. **Kippen (Lemma U2).** Für die feste Markenmenge gibt die Kippidentität den Faktor 3p\* je Stück; die markierten Stücke werden freie Brücken.
4. **Summe über die Markenmengen (Lemma U3).** Sie wird wie in Satz T2 von einem gefärbten Operator getragen. Seine Norm kostet e^{δμ̄} je markiertem Stück und, über die Dichteschranke Satz 3.9 (a^W), den Faktor C\_a m (2D + 7)² je Zelle.
5. Markov mit (X über k₀) ≥ (x/k₀)^{k₀}; der Faktor m^{k₀} hebt sich weg.

**Folgerungen.**

- **Defektgrund D5:** Eine Raum-Zeit-Zelle ist D5-defekt, wenn X\_{Q,k} ≥ (ε/4) b₋ m ist. Die Rate ist e^{−k₀}; sie geht für ρ → 0 gegen 0, weil k₀ wie ln(1/ρ)/ln ln(1/ρ) wachsen darf. Das ist eine Eingangsgröße der Peierls-Schranke (Anhang S, S.3) und des Defekt-Lemmas (Satz D).
- **(W2) für eigene Stücke (Lemma U4):** Für ein zugängliches Stück i ist die Dichte seines bedingten Gesetzes bezüglich B\_i höchstens 2/p\*, in jedem normierten Gesetz, in dem i beliebigen anderen Stücken der Konfiguration und höchstens n′ neu gezogenen regulären Stücken ausweichen muss, sobald n′ P^{br}\_treff ≤ p\*/2 ist. Das ist (W1) aus G.6.2 mit garantiertem p\*, für Stücke mit ihren eigenen Endpunkten. Für umgehängte Brücken gilt das nicht (P.6).
- **Konstante:** σ\_ρ = C e^{δμ̄ + κ} P\_treff → 0 für ρ → 0 bei festem K, wie in G.6.

*Frühere Fassung (bis 2026-11-11).* „Für jede aus dem offengelegten Datum bestimmte Menge A ⊂ I gilt P(alle i ∈ A unzugänglich) ≤ e^{−κ|A|}“, mit den Folgerungen P(mehr als εM der Gruppe unzugänglich) ≤ 2^M e^{−κεM} je Zelle und (2^M e^{−κεM})^{|𝒜|} gemeinsam. Der Beweis (Lemma P1 und P2) deckt nur feste Marken.

**Was die Auswahl jetzt verlangt.** Die Umsteige-Teilchen j\_l (Aufweg und Abweg) werden gleichverteilt unter den wählbaren Stücken der Zelle gewählt; wählbar heißt regulär⁺ und zugänglich, für j\_m im Aufweg dazu mit regulärer Fortsetzung (Anhang L). In guten Zellen sind das mindestens (1 − 2ε) n\_Q Stücke. Für ihre *eigenen* Stücke ist die Stoßwahrscheinlichkeit mit einem festen Stück der anderen Schleife ≤ 2P\_treff/p\*. Für die umgehängten Brücken fehlt diese Schranke (P.6).

## P.5 Was sich am Beweisplan ändert

| vorher                                                    | jetzt                                                                         |
|-----------------------------------------------------------|-------------------------------------------------------------------------------|
| Lemma P\*: deterministische Untergrenze für jede Umgebung | für eigene Stücke: Zugänglichkeit als Teil der Auswahl                        |
| Beweis durch Zeitzerlegung, Lücke bei festen Linien       | Seltenheit durch Kippidentität, Entkopplung und gefärbten Operator (Anhang U) |
| Konstante C₁ unbestimmt                                   | p\* = e^{−δμ̄−κ}, δμ̄ ≈ 8πK                                                     |
| umgehängte Brücken                                        | weiter offen: Lemma P\* für sie (P.6)                                         |

## P.6 Offen: umgehängte Brücken und neue Stücke

**Wo es gebraucht wird.** In G4 (OA (29)) stehen zwei Nenner. Der zweite, Z[j, C], gehört zu Stücken des geschlossenen Zustands mit ihren eigenen Endpunkten; dafür reicht Satz P3. Der erste, Z[l, O], gehört zu den Brücken, die der Staffellauf gezogen hat: im Aufweg j\_l: S\_l → Y\_{l−1}, im Abweg dazu das neue Stück. Um die zusätzlichen Hindernisse nahe einer Begegnung abzuschätzen, braucht man die Dichte ihres bedingten Gesetzes bezüglich der freien Brücke, also ihre Ausweichwahrscheinlichkeit a(S\_l → Y\_{l−1}; F) vor der Umgebung.

**Warum die Kippidentität hier nicht greift.** Die Endpunkte S\_l und Y\_{l−1} gehören zu zwei verschiedenen Teilchen in Nachbarzellen. Unter dem Gibbs-Maß ist die Umgebung mit den Ausweichwahrscheinlichkeiten der *eigenen* Stücke gekippt, a(S\_l → Y\_l) · a(S\_{l−1} → Y\_{l−1}). Eine Umgebung, in der die gekreuzte Brücke schlecht ausweicht, die eigenen aber gut, wird dadurch nicht unterdrückt. Auch das bosonische Summieren über Paarungen hilft nicht direkt, denn der ungekreuzte Summand bleibt unkontrolliert. Dasselbe gilt für das neue Stück des Abwegs; mit freiem Anfang gibt es nicht einmal ein festes Stück, mit dem man vergleichen könnte.

**Was OpenAI tut.** Mit weichem Potential (OA) gibt Jensen eine Schranke für beliebige Endpunkte. Im Hartkugelgas (OAH) wird über frische Mittelpunkte u umgeleitet, und Zugänglichkeit heißt „für fast alle u gelingt es mit Wahrscheinlichkeit ≥ 0,9“. Die Seltenheit folgt dort aus einer Vereinigungsschranke über Hindernisse. Das geht, weil die Stücke kurz sind. Bei uns ist die typische Erfolgswahrscheinlichkeit e^{−2πK}, und die Vereinigungsschranke versagt.

**Was bleibt: Lemma P\* für umgehängte Brücken.** Für wählbare Endpunkte in Nachbarzellen und eine Umgebung, die eine ausdrückliche Gütebedingung erfüllt, gilt a ≥ p\*; die Gütebedingung versagt selten, gemeinsam über viele Zellen. Kandidaten für die Gütebedingung:

1. **Treffsumme** wie in G.11.5, mit Zeitzerlegung. Der Knackpunkt: Die Zeitzerlegung braucht den schlechtesten guten Startpunkt jedes Teilintervalls, die Seltenheit lässt sich aber nur für gemittelte Größen leicht zeigen.
2. **Diffusive Regularität** der nahen Umgebungslinien, |ΔY| ≤ A√h + B auf allen Skalen h ≤ τ. Sie schließt „heranrasende“ Linien aus; eine Linie, die höchstens diffusiv heranläuft, hebt die Treffwahrscheinlichkeit nur um ≈ ln A/ln τ. Offen sind die Treffschranke für bewegte reguläre Ziele in 2D und die gemeinsame Seltenheit der Regularitätsverletzung (Lemma T1 gibt Exponentialmomente der Verschiebungen).

**Neue Stücke des Abwegs.** Weg (a): Anfang gleichverteilt in der Zelle von Y\_m, eigene Normierung je Anfang, Querschritt in jeder Scheibe. Die Dichteformel dieser Variante ist am Mini-Ring exakt (w = 1, Fehler 2,2·10⁻¹⁶; ergebnisse/pruef\_zeitschleife\_spiegel\_varianten.txt). Das neue Stück ist dann eine Brücke mit festen, aber „fremden“ Endpunkten und fällt unter dasselbe Lemma P\*. Ein Anfang dicht neben dem Anfang von j\_m (lokales Harnack-Argument) wäre leichter abzuschätzen. Er hinterlässt aber eine Spur in O, ein ungewöhnlich enges Paar je Scheibe. Damit würde der Abweg sichtbar, wie in Befund A.

**Prüfung der Ausbeute.** Am Mini-Ring nicht möglich: Mit 2 Teilchen auf 3 Zellen fehlt für den erzwungenen Querschritt fast immer ein wählbares Teilchen, und ν sitzt künstlich auf einer dünnen Menge.

*Nachtrag 2026-11-11: Variante c.* Das Testmodell auf dem 2D-Torus (Anhang Z, Z.11) zeigt, dass Weg (a) teuer ist: Die Beschränkung des Anfangs auf die Zelle kostet je Scheibe etwa 1/P(bleiben). Ersetzt durch Variante c ([anhang\_gegenluecke.md](anhang_gegenluecke.md) G.12.9): S′ wird gemeinsam mit den Brücken aus dem bedingten Gesetz gezogen, auf den isolierten freien Plätzen im Ball vom Radius D\_c s um Y\_m. Für das neue Stück braucht man dann kein Lemma P\* mit festem Anfang mehr. Lemma C (c) gibt für das über S′ gemittelte Gesetz die Dichte ≤ 1/(c₁ p₁) bezüglich der freien Rückwärts-Irrfahrt von Y\_m, denn die Ausweichwahrscheinlichkeit a(S′) kürzt sich zwischen Gewicht und bedingter Dichte. Lemma P6 wird nur noch für die Untergrenze des Normierers gebraucht, und zwar für kurze Brücken (Länge ≤ s), mit p₁ = ½ e^{−C′(n+1)}.

## P.7 Lemma P\* bei umgehängten Brücken: diffusive Regularität

### P.7.1 Rahmen

- **Wanderer:** X ist die Irrfahrt auf ℤ² in stetiger Zeit, Rate 1 je Nachbar (die freie Bewegung eines Teilchens unter H = −A), Start x. p\_t(x, y) = P\_x(X\_t = y).
- **Ziel:** Y ist eine feste rechtsstetige Bahn auf [0, 2τ] mit endlich vielen Sprüngen. *Treffer* heißt X\_t = Y\_t für ein t; in stetiger Zeit springen X und Y fast sicher nie gleichzeitig.
- **Kern-Schranken** (jede Koordinate ist eine unabhängige Irrfahrt mit Rate 2, p\_t = Π e^{−2t} I\_k(2t)); mit expliziten Konstanten c = 1/4, C = 1 in (K1) und c = e^{−1/2}/(4π), C = 1/4 in (K2′) (seit 2026-11-13; das scharfe (K2) mit c = 1/(4π) ist nur [N], Anhang K) bewiesen und exakt geprüft in [anhang\_kern.md](anhang_kern.md):

  ```text
  (K1)  p_t(x, y)  ≤  C (1 + t)^{−1} exp( −c |x − y|² / (t + |x − y|) )                für alle t ≥ 0
  (K2)  p_t(x, y)  ≥  c (1 + t)^{−1} exp( −C |x − y|² / t )                          für t ≥ 1, |x − y| ≤ t
  ```

- **Dyadische Fenster:** W\_{−1} = [0, 1] und W\_i = [2^i, 2^{i+1}] für i ≥ 0.

**Gütebedingungen** (Fassung vom 2026-11-12; genaue Form und Beweise in Anhang F, F.10.1, F.10.4 und F.11.1).

- **(G1″) Zeitgemittelte Dichte auf allen Skalen:** Für jede Skala R = 8b · 2^j ≤ R\_max (R\_max ≈ s\_F/8, s\_F die Lokalisierungsskala), jedes Gitterquadrat Q der Seite R und jedes Gitterfenster 𝒲 der Scheibe mit zugelassener Länge Δ ist ∫\_𝒲 n\_Q(t) dt ≤ Δ · N\*(R), mit N\*(R) = 2c̄\_R R (ρ ln(1/ρ))^{1/2} + (ln(1/ρ))^{3/4}. Zugelassen sind Δ zwischen R²/32 und R²/16, auf der kleinsten Skala alle Zweierpotenzen ab t\_r.
- **(G2\_A) Diffusiv nach jedem Zeitpunkt:** Für eine Bahn Y und eine Zeit σ heißt das Fenster W\_i mit A² ≤ 2^i ≤ τ/2 *ruhig*, wenn sup\_{u ∈ W\_i} |Y\_{σ+u} − Y\_σ| ≤ A 2^{i/2}. Y heißt *A-diffusiv auf [0, τ]*, wenn für jedes σ ∈ [0, τ] mindestens die Hälfte dieser Fenster ruhig ist. Lemma P6 braucht das für alle dyadischen Horizonte zwischen τ/(8J) und τ/2 statt nur für τ/2, vorwärts und rückwärts (F.11.1).
- **(G4) Kurzzeit-Ruhe:** Jede Linie bewegt sich in jeder Zeitspanne der Länge t\_r = r²/(16β) um höchstens r/4 (im ℓ∞-Abstand), mit β = C\_β ln ln(1/ρ). Geprüft wird die Gitterfassung (G4′): Schwankung ≤ r/8 in jedem Fenster eines Zeitgitters der Weite t\_r.

*Frühere Fassung (bis 2026-11-11).* Statt (G1″) und (G4) standen hier (G1) (jede Kreisscheibe vom Radius R ≥ r enthält zur Zeit 0 höchstens C₀ρπR² + C₀ Linien) und (G3) (für jeden guten Start höchstens C₁C₀(ρτ + 1) schnelle Fenster, über alle Linien gezählt). (G1) war auf der Skala √τ nicht durch Satz 3.9 (a) gedeckt, C₀ und θ waren zirkulär gekoppelt, und (G3) verlangte ein festes C₁, das die Regularitätsschranke nicht hergibt (Review K1). Die schnellen Fenster kommen nur noch in Lemma P5 vor, das für Lemma P6 nicht mehr gebraucht wird:

- **Schnelle Fenster:** Für einen Start x mit d = |x − Y\_0| ≥ 1 heißt ein Fenster W (W\_{−1}, oder W\_i mit 2^{i+1} ≤ d²) *schnell*, wenn inf\_{t∈W} |x − Y\_t| < d/2. B(x) ist die Zahl der schnellen Fenster.

### P.7.2 Lemma P5: Treffen eines bewegten Ziels

**Lemma P5 [S, gegeben (K1), (K2)].** Sei A ≥ 1, τ ≥ 16A² und Y A-diffusiv auf [0, τ]. Dann gilt für jeden Start x mit d = |x − Y\_0| ≥ 1

```text
P_x( X trifft Y in [0, τ] )  ≤  C e^{C A²} · ( φ(d²/τ) + B(x) ) / log₂(τ/A²)
φ(v) = 1 + ln(1/v)  für v ≤ 1,        φ(v) = e^{−c v}  für v > 1
```

Die Konstanten hängen nicht von x, d, τ, A oder der Bahn ab.

*Beweis.*

1. **Quotient.** σ\_H = inf{t : X\_t = Y\_t} ist eine Stoppzeit für X, weil Y fest ist; auf {σ\_H ≤ τ} ist X\_{σ\_H} = Y\_{σ\_H}. Sei L = ∫₀^{2τ} 1{X\_t = Y\_t} dt und g(σ) = ∫₀^τ p\_u(Y\_σ, Y\_{σ+u}) du. Nach der starken Markov-Eigenschaft ist

   ```text
   E[L]  ≥  E[ 1{σ_H ≤ τ} · ∫_{σ_H}^{σ_H+τ} 1{X_t = Y_t} dt ]  =  E[ 1{σ_H ≤ τ} g(σ_H) ]  ≥  P(σ_H ≤ τ) · inf_{σ ≤ τ} g(σ)
   ```

2. **Nenner.** Sei σ ≤ τ und W\_i ruhig, also 2^i ≥ A². Für u ∈ W\_i ist |Y\_{σ+u} − Y\_σ| ≤ A 2^{i/2} ≤ A√u ≤ u, und (K2) gibt p\_u(Y\_σ, Y\_{σ+u}) ≥ c(1 + u)^{−1} e^{−CA²}. Über W\_i integriert ist das ≥ c e^{−CA²} ln(3/2). Es gibt mindestens log₂(τ/A²) − 2 ≥ ½ log₂(τ/A²) Fenster mit A² ≤ 2^i ≤ τ/2 (wegen τ ≥ 16A²), davon die Hälfte ruhig; sie liegen in [0, τ]. Also ist g(σ) ≥ c e^{−CA²} log₂(τ/A²).
3. **Zähler.** E[L] = ∫₀^{2τ} p\_t(x, Y\_t) dt, aufgeteilt in Fenster.
   - *Schnelle Fenster:* Mit (K1) ohne Exponentialfaktor trägt jedes höchstens ∫\_W C(1 + t)^{−1} dt ≤ C bei, zusammen ≤ C B(x).
   - *Übrige Fenster unterhalb von d²:* Dort ist |x − Y\_t| ≥ d/2, und (K1) gibt den Integranden ≤ C(1 + t)^{−1} e^{−cd²/(4t+2d)}. Für t ≤ d/2 ist der Exponent ≥ cd/4, Beitrag ≤ C e^{−cd/4} ln(1 + d) ≤ C. Für d/2 ≤ t ≤ d² ist 4t + 2d ≤ 8t; mit v = d²/t wird der Beitrag ≤ C ∫₁^∞ v^{−1} e^{−cv/8} dv ≤ C.
   - *Zeiten t ≥ d²* (nur falls d² ≤ 2τ): ≤ ∫\_{d²}^{2τ} C(1 + t)^{−1} dt ≤ C(1 + ln(2τ/d²)).
   - *Fernes Ziel, d² > 2τ:* Alle Fenster liegen unterhalb von d². Man teilt den Exponenten in zwei Hälften; die eine ist ≤ e^{−c′d²/τ}, die andere integriert sich wie oben zu einer Konstanten.

   Zusammen: E[L] ≤ C(φ(d²/τ) + B(x)).
4. **Zusammensetzen:** P(σ\_H ≤ τ) ≤ E[L]/inf g. ∎

**Was die Bedingungen leisten.** (G2) sichert den Nenner: Nach jedem möglichen Treffer bleibt das Ziel auf genügend vielen Skalen in Reichweite des Wanderers. Dadurch entsteht der Faktor log τ, der das 2D-Treffen klein macht. Der Zähler ist die erwartete gemeinsame Aufenthaltszeit E[L]. In der Form oben wird er über den Anfangsabstand und die schnellen Fenster abgeschätzt: Nur Fenster, in denen das Ziel schneller als diffusiv herankommt, kosten mehr als üblich. Für viele Linien ist es besser, E[L] nicht je Linie abzuschätzen, sondern über die Linien zu summieren (P.7.3).

### P.7.3 Viele Linien: Lemma P5″ und die Dichte in Raum-Zeit

Fassung vom 2026-11-12. Beweise in Anhang F, F.9 und F.10.

**Lemma P5″ [S, gegeben (K2)].** X sei die Irrfahrt ab x. Die Linien Y\_j seien feste rechtsstetige Bahnen auf [0, 2τ], zu jeder Zeit auf verschiedenen Plätzen. Sei 𝔅 = B(x, R\_G) die ℓ∞-Kugel um x, 𝔅′ = B(x, R\_G/2), τ ≥ 16A² und A√τ ≤ R\_G/2. Jede Linie, die sich während [0, τ] in 𝔅′ aufhält, sei A-diffusiv. Dann gilt

```text
P_x( X trifft in [0, τ] eine Linie an einem Platz von 𝔅′ )  ≤  C e^{CA²} · 𝔏(x) / log₂(τ/A²)
𝔏(x)  =  ∫_0^{2τ} Σ_{y ∈ 𝔅} p_t(x, y) n_y(t) dt
```

- Der Beweis ist Schritt 1 und 2 von Lemma P5, über die Linien summiert. Weil die Linien zu jeder Zeit auf verschiedenen Plätzen sitzen, ist die Summe der Zähler E[L\_j] gleich 𝔏(x).
- 𝔏(x) ist eine reine Dichtegröße in Raum-Zeit. Die Bahnen einzelner Linien kommen nicht vor; eine Linie, die auf x zuläuft, ist mit ihrem tatsächlichen Beitrag enthalten. Deshalb entfallen (G3) und C₁.

**Folgerung F9 [S, gegeben (G1″) und (G4)].** Für jeden zur Zeit t₀ guten Punkt x und jedes T ≤ 2τ, τ = θ ln(1/ρ)/ρ, gilt

```text
𝔏(x)  ≤  [ C_𝔏 (C_E θ)^{1/2}  +  ε_fern(θ)  +  o(1) ] · ln(1/ρ),        C_𝔏 ≈ 2,4·10⁹
```

Dahinter steht das deterministische Lemma F8: Ist die zeitgemittelte Teilchenzahl in Gitterquadraten aller Skalen klein, so ist 𝔏 klein. ε\_fern(θ) fällt für θ → 0 schneller als jede Potenz.

**Anwendung (Eingang für P6).** Sei C\_P = C e^{CA²} die Konstante aus Lemma P5″, C\_b = 8π e^{11/4} und ε\_P = 1/(4 ln 2 · C\_b C\_P). Für

```text
θ  ≤  θ_P  =  ε_P² / (16 C_𝔏² C_E)        (und ε_fern(θ_P) ≤ ε_P/4)
```

ist 𝔏(x) ≤ (ε\_P/2 + o(1)) ln(1/ρ), also

```text
P_x( Treffer im Teilintervall an einem Platz von 𝔅′ )  ≤  (1 + o(1)) / (8 C_b)        (ρ → 0)
```

C₀ und C₁ kommen nicht mehr vor, und es gibt keinen Zirkel: A bestimmt ε\_P, ε\_P bestimmt θ.

**Eine einzelne Linie (Lemma F13, F.11.4) [S].** Ist x gut zur Zeit t₀ und erfüllt die Linie Y (G4) und (G2\_A), so trifft X sie bis zur Zeit t₀ + T\_h ≤ t₀ + δ mit Wahrscheinlichkeit ≤ C e^{CA²} ln(32Kβ ln(1/ρ)/ζ²)/log₂(τ/A²), also ≲ ln ln(1/ρ)/ln(1/ρ). Das ist P\_treff in σ\_ρ; es braucht weder (G3) noch b₀.

*Frühere Fassung (Folgerung P5′).* Aus der Vereinigungsschranke über die Linien, mit (G1) zur Startzeit: P ≤ C e^{CA²} (C₀ρτ + C₀(log₂(2√τ/r))² + Σ\_j B\_j(x))/log₂(τ/A²). Die Folgerung ist richtig, aber ihre Voraussetzungen (G1) auf der Skala √τ und Σ\_j B\_j ≤ C₁C₀(ρτ + 1) waren nicht gesichert (Review K1).

### P.7.4 Zahlen [N]

[pruef\_treffen\_bewegt.py](pruef_treffen_bewegt.py), faule Irrfahrt, τ = 6000, d = 12, Ausbreitung √(pτ) = 49:

| Zielbahn                                                    | P(Treffer)          |
|-------------------------------------------------------------|---------------------|
| ruhend                                                      | 0,231               |
| diffusiv heranlaufend, A = 1                                | 0,406               |
| diffusiv heranlaufend, A = 2                                | 0,495               |
| diffusiv heranlaufend, A = 4                                | 0,601               |
| ballistisch heranrasend, Geschwindigkeit 1                  | 0,643               |
| unabhängige Irrfahrt (60 Bahnen): Mittel, Streuung, Maximum | 0,255; 0,083; 0,435 |

Ein Irrfahrt-Ziel, wie es eine typische Umgebungslinie ist, verhält sich im Mittel wie ein ruhendes, mit mäßiger Streuung. Je Verdopplung von A steigt die Treffwahrscheinlichkeit um etwa 0,1. Das passt zur Form von P5: ein Zusatz der Ordnung (Konstante + ln A)/ln √τ, hier mit ln √τ ≈ 3,9. Im Beweis ist ln √τ ≈ ½ ln(1/ρ), und der Zusatz verschwindet für jedes feste A.

### P.7.5 Die übrigen Schritte

Fassung vom 2026-11-12. Hier stehen die Aussagen und der Beweisweg; die Beweise stehen in Anhang F, F.12 (dort heißen die Lemmata P6″, P6a″, P6b″). Gegenüber der Fassung vom 2026-11-10 sind (G1) und (G3) durch (G1″) und (G4) ersetzt, die Zwischenzeiten der Zerlegung sind zufällig, und die Konstanten sind ausgeschrieben.

Ein Punkt u heißt **gut zur Zeit t**, wenn er zur Zeit t Abstand > r von allen Linien hat. Für eine Brücke der Dauer τ′ von u nach v heißt λ = |u − v|/√τ′ ihr **normierter Schritt**.

**Lemma P6 (P\* für umgehängte Brücken) [S, gegeben (K1), (K2)].**

*Voraussetzungen.*

- Die Brücke läuft von S nach Y′ über eine Scheibe der Dauer nτ, mit τ = θ ln(1/ρ)/ρ und ganzzahligem n. γ\_n = |S − Y′|/(n√τ) ist der normierte Vorschub je Teilintervall. Für |S − Y′|\_∞ ≤ (D + 10)s und n = K/θ ist γ\_n ≤ √2 (D + 10)/√n.
- Die Gütebedingungen (G1″), (G2\_A), (G4) gelten auf der ganzen Scheibe im Kasten 𝔎 = B(S, R\_K), (G2\_A) und (G4) vorwärts und rückwärts. Dabei ist R\_K = λ₁ n √τ + 3s\_F mit λ₁ = max(12γ\_n, (17 ln(208n))^{1/2}).
- S und Y′ sind zu ihren Zeiten gut.
- θ ≤ θ\_P (P.7.3), ζ ≤ ζ₀ (unten), ρ klein genug.

*Aussage.* Die freie Brücke von S nach Y′ weicht der Umgebung mit Wahrscheinlichkeit

```text
P_{S→Y′}(weicht aus)  ≥  p*  =  ½ exp( −C′ n ),        C′ = 9,3 · ( 1 + 520 e^{1,75 γ_n²} )
```

aus. C′ hängt nur von γ\_n ab. C₀, C₁ und b₀ kommen nicht mehr vor.

**Lemma P6a (kurze Brücke; F.12.3) [S].** Sei τ/J ≤ τ′ ≤ 3τ/2 mit J = 4(λ₁² + 1), u gut zur Zeit t, v gut zur Zeit t + τ′ und |u − v| ≤ 3√τ′. Dann weicht die Brücke von u nach v mit Wahrscheinlichkeit ≥ ½ aus.

*Beweisweg.* Auf jeder Hälfte hat die Brücke bezüglich der freien Irrfahrt die Dichte ≤ C\_b = 8π e^{11/4}. Die freie Irrfahrt trifft nach Lemma P5″ und Folgerung F9 mit Wahrscheinlichkeit ≤ (1 + o(1))/(8C\_b), und sie verlässt den Kasten B(u, s\_F/2) mit Wahrscheinlichkeit ≤ 4 e^{−K\_F/(13,2θ)}.

**Lemma P6b (mittlerer Schritt; F.12.4) [S].** Sei τ/2 ≤ τ″ ≤ 3τ/2, u gut zur Zeit t, v gut zur Zeit t + τ″, 3 < λ ≤ λ₁ und j = ⌈λ²⌉. Dann weicht die Brücke mit Wahrscheinlichkeit ≥ ½ (c₂/2)^j ≥ exp(−8,3 (1 + λ²)) aus, mit c₂ = 10⁻³.

*Beweisweg.*

1. Man teilt in j Teilstücke an zufälligen Zwischenzeiten T\_i = t + iτ′ + V\_i τ′/2, mit τ′ = τ″/j und V\_i unabhängig und gleichverteilt auf [0, 1].
2. Die Brücke bleibt an allen Zwischenzeiten mit Wahrscheinlichkeit ≥ c₂^{j−1} im Schlauch der Breite ½√τ′ um die gerade Verbindung. Dann ist jeder Teilschritt höchstens das Dreifache der Wurzel seiner Dauer.
3. Ein Zwischenpunkt im Schlauch ist mit Wahrscheinlichkeit ≤ 9,4·10⁴ ζ² c̄\_R (j/θ)^{1/2} schlecht. Seine Dichte ist ≤ 12π/τ′, und weil T\_i zufällig ist, zählt das Zeitmittel der Linien in einer Kugel vom Radius √τ′; das beschränkt (G1″). Zu einer festen Zeit wäre (G1″) dafür zu schwach.
4. Auf den Teilstücken gilt P6a.

*Beweisweg von Lemma P6.*

1. **Zerlegen** an zufälligen Zeiten T\_k = kτ + V\_k τ/2. P\_k sind die Lagen der Brücke, λ\_k die normierten Schritte, und P(weicht aus) = E[Π\_k q(P\_k, P\_{k+1})].
2. **Ausnahmeereignis** G: alle λ\_k ≤ λ₁ und alle P\_k gut. Der Zuwachs der Brücke hat bezüglich der freien Irrfahrt die Dichte ≤ 22 e^{0,63 γ\_n λ} (aus (K1), (K2)); das gibt P(λ\_k > λ₁) ≤ 1/(4n). Schlechte Knoten haben zusammen die Wahrscheinlichkeit ≤ ¼, wieder über das Zeitmittel aus (G1″). Also P(G) ≥ ½.
3. **Je Schritt:** Auf G ist q ≥ e^{−9,3(1+λ\_k²)}, nach P6a für λ\_k ≤ 3 und nach P6b sonst.
4. **Jensen über die Schrittweiten,** mit E λ\_k² ≤ 150 e^{1,75 γ\_n²}. ∎

**Wahl von ζ.** ζ₀ ist durch drei Bedingungen bestimmt (F.12.6): ζ² ≤ 1/H, ζ² ≤ c₂^{j₁−1} θ^{1/2}/(2,0·10⁵ c̄\_R j₁^{3/2}) mit j₁ = ⌈λ₁²⌉, und ζ² ≤ θ^{1/2}/(1,1·10⁴ c̄\_R λ₁² n³). Die mittlere ist die schärfste, etwa (208n)^{−117}: polynomial klein in n wie bisher, aber mit großem Exponenten. Das ist eine feste Zahl, sobald K, A und damit θ und n feststehen. Das passt zur Reihenfolge der Konstanten in Anhang Z (Z.9: ζ nach ε, b₋ und n).

**Keine Rekursion nötig.** Schritte über λ₁ sind so selten, dass man sie dem Ausnahmeereignis zuschlägt, und Schritte bis λ₁ teilt man genau einmal. Die kürzesten Teilstücke haben die Dauer ≥ τ/J. Lemma P5″ passt auf sie, weil τ ~ ln(1/ρ)/ρ wächst und J fest ist.

**Lemma P7 (Seltenheit der Gütebedingungen).**

- (G1″) versagt selten, gemeinsam über viele Zellen: Satz F10 (F.11.2), aus den Raum-Zeit-Momenten zeitgemittelter Teilchenzahlen (Satz F7). [S]
- (G2): An einer festen Stelle σ und in einem festen Fenster ist das Fenster für eine Linie mit Wahrscheinlichkeit ≤ 2e^{−A²/c} unruhig; Lemma T1 gibt für markierte Teilchen dieselben Exponentialmomente der Verschiebung wie für freie. Damit mehr als die Hälfte der Fenster unruhig ist, braucht es über disjunkte Zeitfenster (Markov-Eigenschaft) eine große Abweichung der Ordnung (Ce^{−A²/c})^{½ log₂ τ} = τ^{−c(A)} mit c(A) > 2 für großes A. Die Vereinigung über σ (τ Stellen nach Diskretisierung, mit leicht vergrößertem A), über die Horizonte und über die Linien im Kasten bleibt klein. Ausgeschrieben in Lemma R (a) (Anhang K, K.4).
- (G4): Für die freie Irrfahrt ist die Schwankung in einem Fenster der Länge t\_r mit Wahrscheinlichkeit ≤ 4e^{−β/71} größer als r/8 (Lemma F11a). Für die Linien im Kasten gibt das ein Fach in Satz T2 (Satz F11, mit C\_β ≥ 300); es ersetzt das Fach R3. [S, gegeben Satz T2]
- Gemeinsam über viele Zellen geht das ins Defekt-Lemma ([satz\_3\_9\_dichteschranken.md](satz_3_9_dichteschranken.md) §9, Gründe D6 und D7).
- **Kalibrierung [N]** ([pruef\_regularitaet.py](pruef_regularitaet.py)): Für die Irrfahrt mit Rate 1 je Nachbar versagt (G2) irgendwo in [0, 4096] mit Wahrscheinlichkeit 0,42 (A = 5), 0,03 (A = 6), 0 (A = 8). Also A ≈ 6–8.

**Stand.** Lemma P5″, Lemma F8 und Folgerung F9 ersetzen Folgerung P5′. Lemma P6 ist mit den Bedingungen (G1″), (G2\_A), (G4) bewiesen, gegeben die Kern-Schranken: Zerlegung der Brücke an zufälligen Zeiten, Hälftenvergleich mit freien Irrfahrten (P6a), einmaliges Teilen mittlerer Schritte (P6b), Ausnahmeereignis für sehr große Schritte und schlechte Zwischenpunkte, Jensen über die Schrittweiten. ζ muss polynomial klein in n = K/θ sein. Die Seltenheit der Bedingungen steht in Satz F10 und Satz F11. Lemma P6 setzt gute Endpunkte der Brücke voraus. Im Abweg sind sie nach Konstruktion da; im Aufweg liefert sie die Wählbarkeit über zwei Scheiben, auch für die Brücke S₁ → Y₀ am Lochstück ([anhang\_lochstueck.md](anhang_lochstueck.md), Anhang L, Antwort auf Befund K3 des Reviews).
