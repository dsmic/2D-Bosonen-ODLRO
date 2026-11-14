# Beweisweg mit Verlustbilanz

Stand 2026-11-13. Ein grober Weg durch den Beweis. Zu jedem Schritt steht, was bewiesen ist, was wahr ist (numerisch, aus der Literatur oder heuristisch) und wie weit beides auseinanderliegt. Nicht alles hier ist bewiesen; es geht um Größenordnungen. Den Beweis selbst enthalten das Tutorial (tutorial\_beweis\_verduennt.pdf) und der Gesamtband (beweis\_verduennt\_gesamt.pdf).

## 0. Lesart

- **Kennzeichnung:** [S] bewiesen, [N] numerisch, [Lit] Literatur, [H] Heuristik oder Schätzung. Die Spalte „bewiesen“ nennt die Konstante des Beweises. Die Zahlen, die *daraus* folgen (Schwelle, Kondensatanteil), sind Schätzungen [H]: Ich habe die Formeln der Anhänge ausgewertet, aber nicht jede Bedingung einzeln nachverfolgt.
- **Günstige Annahme:** Konstanten, die der Beweis nur als „C“ angibt, setze ich auf 1. Das betrifft vor allem C\_P = C e^{CA²} aus Lemma P5″. Mit C\_P ≈ e^{A²} bei A = 6–8 würden die großen Zahlen in Abschnitt 3.5 und 4 noch um den Faktor 10³¹ bis 10⁵⁶ größer.
- **Rechnung:** [verlustbilanz\_zahlen.py](verlustbilanz_zahlen.py), Ausgabe in ergebnisse/verlustbilanz\_zahlen.txt. Fehler um einige Größenordnungen *im Exponenten* ändern das Bild nicht.
- **Bezeichnungen:** Zellen der Seite s mit m = ρs² = K ln(1/ρ) Teilchen im Mittel; Y = 1/ln(1/(ρa²)) mit der Gitter-Streulänge a ≈ 0,1985; eine Zeitscheibe hat die Dauer δ ≈ s².

## 1. Auf einen Blick

| Größe                | bewiesen                                 | wahr bzw. gemessen                                                                           | Abstand               |
|----------------------|------------------------------------------|----------------------------------------------------------------------------------------------|-----------------------|
| Kondensatanteil N₀/N | ≥ c mit c ≈ exp(−10³⁹) [H aus der Kette] | ≈ 0,75 bei ρ = 1/16 (L = 32: 0,790) [N]; → 1 − 1/ln(1/(ρa²)) für ρ → 0 [Lit]                 | Faktor exp(10³⁹)      |
| Dichteschwelle ρ\*   | ρ\* ≈ exp(−exp(10³⁹)) [H aus der Kette]  | Kondensat bei allen gerechneten Dichten (ρ ≈ 0,02 bis 0,19) [N]; erwartet für alle 0 < ρ < 1 | dreifach exponentiell |
| Systemgröße          | L ≥ L₀ = c\_L s(ρ) mit c\_L ≈ 10²⁰ [H]   | keine Mindestgröße; schon 4×4 bis 32×32 zeigen N₀/N = 0,79–0,89 [N]                          | Faktor 10²⁰ in L/s    |

Die 2D-Bogoliubov-Verarmung 1/ln(1/(ρa²)) ist bei ρ = 1/16 etwa 0,17, also N₀/N ≈ 0,83. Gemessen sind 0,75 bis 0,79; die führende Ordnung trifft also schon dort ungefähr.

### Die Verlusttreppe

Von der Physik bis zum Beweis geht es über vier Stufen. Jede Stufe setzt etwas Gröberes ein.

| Stufe                                      | was eingesetzt ist                                                                     | Schwelle                | Kondensatanteil   |
|--------------------------------------------|----------------------------------------------------------------------------------------|-------------------------|-------------------|
| A Physik                                   | –                                                                                      | ρ\* ≥ 1/16 gemessen     | ≈ 0,75 [N]        |
| B Methode mit wahren Konstanten            | Stoßkosten κ₂ ≈ e^{0,54K}, c₁ = 4π, Budget α = 0,07, K = 25 (Tutorial §9.3)            | ln(1/ρ\*) ≈ 10⁹ [H]     | nicht abgeschätzt |
| C Buchführung des Beweises, wahre Eingänge | Ausweichen p ≈ e^{−2πK}, Radius D ≈ 3, b₋ ≈ 0,2, K = 25, aber die Formeln aus Anhang M | ln(1/ρ\*) ≈ 10¹⁰⁶⁴ [H]  | ≈ 10⁻⁷⁶³ [H]      |
| D Beweis mit seinen Konstanten             | p₁ = ½e^{−4900n} mit n ≈ 10³⁴, D ≈ 10¹⁹, K = 100                                       | ln ln(1/ρ\*) ≈ 10³⁹ [H] | ≈ exp(−10³⁹) [H]  |

- **A → B: die Grenze der Methode in 2D.** Der kleine Parameter ist nur 1/ln(1/ρ). Jede Begegnung zweier Schleifen kostet etwa κ₂ (1/(2b₋m) + P\_δ) mit P\_δ ≈ 2,5/ln(1/ρ), und das muss unter dem Budget α liegen. Mit κ₂ ≈ e^{0,54K} ≈ 7·10⁵ braucht man ln(1/ρ) ≈ 10⁹. Diesen Verlust hat jeder Beweis auf diesem Weg, auch mit optimalen Konstanten.
- **B → C: die Buchführung.** Der Beweis rechnet je nahem Stück nicht mit dem Doob-Verhältnis κ₂, sondern mit dem Kehrwert 1/p der Ausweich-Wahrscheinlichkeit. An den Enden der Schleife geht das bis zur 14. Potenz ein (Bedingung η ≤ 1/4 in Anhang M, M.9.8). Mit dem wahren p ≈ e^{−2πK} sind das schon e^{2C′(K)} ≈ 10¹⁰⁶³.
- **C → D: die Ausweich-Untergrenze.** Bewiesen ist p nur über eine Zerlegung der Scheibe in n Teilintervalle mit je e^{−4900}, und n ist riesig, weil die Dichtegröße 𝔏 grob abgeschätzt ist (Abschnitt 3.5). Daraus wird ρ\* dreifach exponentiell klein.

## 2. Der Beweisweg in acht Schritten

1. **Kondensat als Masse offener Konfigurationen** (Tutorial Kap. 3): N₀/N = |µ|.
2. **Bauen statt messen** (Kap. 5.4): N₀/N ≥ |ν|²/∫ f² dµ, mit dem gebauten Maß ν.
3. **Zellen und Dichteschranken** (Kap. 6, 7; satz\_3\_9, Anhang E): Jede Zelle hat genug und nicht zu viele Teilchen, mit exponentiell kleinen Ausnahmen.
4. **Zufällige Schleifen mit wenigen Begegnungen** (Kap. 4, Anhang S): E e^{θJ} ≤ C für die Zahl J der Begegnungen.
5. **Ausweichen** (Anhang P, F, U; Lemma C): Neu gezogene Stücke weichen allen anderen Linien mit Wahrscheinlichkeit ≥ p aus.
6. **Kosten je Begegnung** (Kap. 8, Anhang M): Fern von Begegnungen kürzt sich alles exakt; nahe kostet es einen festen Faktor, der durch m geteilt wird.
7. **Seltene Defekte** (Satz D, satz\_3\_9 §9–§12): Schlechte Zellen sind selten, auch unter dem Bezugsmaß.
8. **Zusammensetzen** (Anhang Z, Z.9): ∫ f² dµ ≤ C, sobald ρ klein genug ist.

## 3. Die Schritte mit ihren Verlusten

### 3.1 Kondensat als offene Konfiguration

Exakt, ohne Verlust (Lemma 3.2 [S]). Auch das Einpunkt-Kriterium (Kap. 2, nur Hintergrund) verliert praktisch nichts: Z₀ = N H̄²/N₀ = 0,9988–0,9997 auf exakt gerechneten Systemen [N].

### 3.2 Bauen statt messen

| Größe                  | bewiesen                                                   | wahr bzw. gemessen                                                                        | Abstand          |
|------------------------|------------------------------------------------------------|-------------------------------------------------------------------------------------------|------------------|
| zulässige Endpaare     | Anteil υ ≈ 1/16 (Endpaare mit Abstand ≤ W, OAs Bereich)    | die Kondensat-Korrelation ist für alle Paare gleich groß                                  | Faktor 16        |
| Annahme \|ν\|          | ≥ υ/4 (Z.12)                                               | nicht gemessen; in guten Zellen fast immer                                                | Faktor ≈ 4       |
| zusammen \|ν\|²        | ≥ υ²/16 ≈ 2,4·10⁻⁴                                         | –                                                                                         | Faktor ≈ 4·10³   |
| zweites Moment ∫ f² dµ | ≤ C e^{2C(K)} (4D\_c + 3)²/υ (Anhang M, M.9.5) ≈ exp(10³⁹) | 2 bis 3 im Testmodell (Anfang aus dem bedingten Gesetz), Zuwachs 1,00–1,14 je Scheibe [N] | Faktor exp(10³⁹) |

Selbst mit ∫ f² dµ = 1 gäbe die Konstruktion nur N₀/N ≥ 2,4·10⁻⁴. Der eigentliche Verlust steckt aber im Faktor e^{2C(K)} der beiden Endzellen (Abschnitt 3.6).

### 3.3 Zellen und Dichteschranken

| Größe                                         | bewiesen                                                         | wahr bzw. gemessen                                                    | Abstand                  |
|-----------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------------|--------------------------|
| Energie je Teilchen ε\_N/N ≥ c₁ρY             | c₁ = 3π/16 ≈ 0,59 [S]; π mit exakten Kastenenergien [S, Rechner] | c₁ = 4π ≈ 12,6 (Lieb–Yngvason) [Lit]                                  | Faktor 21 bzw. 4         |
| chemisches Potential μ̄ ≤ κ\_μ 8πρY            | κ\_μ → 1 [S], scharf                                             | κ\_μ = 1,2–1,8 bei endlichem ρ [N]                                    | kein Verlust für ρ → 0   |
| Dyson-Lemma 6.4                               | R\_eff = (1/2π) ln(R/a)                                          | bis auf 0,04 % (R = 128) [N]                                          | kein Verlust             |
| Zellenschranke λ\_min(b)                      | ≥ π/(2b² (ln b + 3,6)) [S]                                       | ≈ π/(2b² (ln b − 0,13)) [N, b ≤ 512]                                  | Faktor 1–2               |
| obere Schwänze: log E e^{2λn} ≤ 2λC\_a ρ\|U\| | C\_a ≈ 2–3·10³ [S]                                               | E n\_U = ρ\|U\| exakt; unter-Poisson, ungekippt Var/E = 0,37–0,86 [N] | Faktor 10³ im Exponenten |
| untere Schwänze: Rate b₋                      | 4,7·10⁻⁷ (c₁ = 3π/16), 1,2·10⁻⁵ (π), 2,8·10⁻⁴ (4π) (Anhang E)    | ≈ 0,2 nach Poisson-Vergleich [H]; unter-Poisson eher besser           | Faktor 10³–10⁶           |
| Zellkonstante K                               | 25 (mit c₁ = 4π) bis 540 (c₁ = 3π/16)                            | einige Teilchen je Zelle genügen, K ≈ 1 [H]                           | Faktor 25–540 in m       |
| Isolationsradius ζ ρ^{−1/2}                   | ζ² ≈ (352n)^{−133} ≈ 10⁻⁴⁸⁰⁰ (Anhang F, F.12.6) [H]              | ζ ≈ 0,1–0,3 genügt [H]                                                | Faktor 10²⁴⁰⁰ in ζ       |

Woher die großen Zahlen kommen: Lokalisierung und Kippen kosten C\_L ≈ 73 und C\_K ≈ 44 je Teilchen und 1/s², das Einfügen im Dirichlet-Quadrat ≈ 79/s². Sie stehen gegen die winzige Energieskala ρY. Bei b₋ kommt dazu, dass der Gewinn je eingefügtem Teilchen nur ε\_N/N ist, halb so groß wie das chemische Potential, gegen das er antritt (satz\_3\_9 §6). Für die Schwelle wiegen diese Verluste wenig: Sie gehen nur in K und in Vorfaktoren ein. Teuer wird K erst über das Ausweichen, wo es im Exponenten steht.

### 3.4 Schleifen und Budget

| Größe                                    | bewiesen                                                              | wahr bzw. gemessen                                                        | Abstand       |
|------------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------|---------------|
| Budget der Routenfamilie                 | jedes α > 0 genügt (Lemma S1)                                         | α\_max ≈ 0,046 (harte Kosten), 0,07 (weiche) [N]; mit Drift 0,5 nur 0,004 | –             |
| Skelett mit Begegnungsradius R\* = 1     | θ ≲ 10⁻³ (b₀ ≈ 600) [S nach OA]                                       | θ = 0,005 trägt noch: E e^{0,005J} = 1,26–1,67 bis W = 4096 [N]           | Faktor ≥ 5    |
| Begegnungsradius R\*″ des Beweises       | R\*″ = R\* + D′ + … mit R\* = Δ + D\_K + R + 2D + 6 ≈ 10²⁰ Zellen [H] | Linien entkoppeln nach 1–3 Zellen [H]                                     | Faktor ≈ 10¹⁹ |
| Budget im Beweis α(R\*″) ∝ 1/(1 + R\*″)² | ≈ 10⁻⁴² [H]                                                           | ≈ 0,05 [N]                                                                | Faktor 10⁴⁰   |

Der Radius ist so groß, weil der Kasten eines Defekts (D\_K ≈ λ₁ n^{1/2}) und der Ball des Abwegs (D\_c ≈ (C′n)^{1/2}) mit der Zahl n der Teilintervalle wachsen, also mit der Ausweich-Untergrenze aus 3.5. Derselbe Radius bestimmt die Mindestgröße L₀ = c\_L s mit c\_L = 2R\*″ + 2.

### 3.5 Ausweichen: der Hauptverlust

Ein neu gezogenes Stück muss allen anderen Linien der Scheibe ausweichen. Die Nenner der Dichte sind solche Ausweich-Wahrscheinlichkeiten, und der Beweis braucht Untergrenzen.

| Stück                                      | bewiesen                                                      | wahr bzw. gemessen                                           | Abstand im Exponenten |
|--------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------|-----------------------|
| eigenes Stück eines zugänglichen Teilchens | p\* = e^{−δμ̄−κ\_U} ≈ e^{−8πK−κ\_U}, κ\_U ≈ 260 (Anhang U) [S] | ≈ e^{−2πK}: ein Stück trifft im Mittel ≈ 2πK Linien [H]      | Faktor 4 (+ κ\_U)     |
| neues Stück des Abwegs, kurze Brücke       | p₁ = ½ e^{−4900(n+1)}, n = K/θ ≈ 10³⁴ (Anhang F, F.12.6) [S]  | ≈ e^{−2πK} (G.6.2) [H]; Testmodell: 1,07–1,16 je Scheibe [N] | Faktor ≈ 10³⁵         |
| umgehängte Brücke                          | p\_P = ½ e^{−C′K/θ}, ebenso klein [S]                         | wie oben                                                     | Faktor ≈ 10³⁵         |

**Warum n so groß ist.** Lemma P6 zerlegt die Brücke an zufälligen Zeiten in n Teilintervalle der Dauer τ = θ ln(1/ρ)/ρ. Jedes Teilintervall kostet höchstens e^{−C′} mit C′ ≤ 4900, das Produkt also e^{−C′n}. Das verliert zweimal:

1. **Konstante je Teilintervall.** Wahr ist je Teilintervall etwa e^{−2πK/n}, also fast 1. Der Beweis zahlt e^{−4900}. Schon mit einem vernünftigen θ (≈ 2·10⁻⁴, siehe 2.) gibt das im Exponenten den Faktor 4900/(2πθ) ≈ 4·10⁶.
2. **θ muss winzig sein.** Je Teilintervall darf die Trefferwahrscheinlichkeit höchstens 1/(8C\_b) sein (C\_b = 8πe^{11/4} ≈ 393). Dafür muss die Raum-Zeit-Dichtegröße 𝔏 ≤ ε\_P ln(1/ρ)/2 sein, mit ε\_P = 1/(4 ln 2 · C\_b C\_P) ≈ 9·10⁻⁴. Wahr ist im Mittel 𝔏 ≈ 2θ ln(1/ρ); dafür genügte θ ≈ ε\_P/4 ≈ 2·10⁻⁴. Bewiesen ist nur 𝔏 ≤ C\_𝔏 (C\_E θ)^{1/2} ln(1/ρ) mit C\_𝔏 ≈ 2,4·10⁹ (Lemma F8, deterministisch) und C\_E ≈ 8·10⁵. Daraus θ\_P = ε\_P²/(16 C\_𝔏² C\_E) ≈ 10⁻³², also n = K/θ\_P ≈ 10³³ bis 10³⁵. Das ist ein Faktor 10²⁸ gegen das wahre θ.

Mit (K2′) statt des scharfen (K2) verdoppelt sich C′ (2500 → 4900). Das ist dagegen eine Kleinigkeit.

### 3.6 Kosten je Begegnung

| Größe                                          | bewiesen                                                           | wahr bzw. gemessen                                        | Abstand                         |
|------------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------|---------------------------------|
| Stoß zweier neuer Stücke                       | P\_treff ≲ C\_P ln(32Kβ ln(1/ρ)/ζ²)/log₂(τ/A²) ≈ 8·10³/ln(1/ρ) [H] | P\_δ ≈ 1,23/(ln √δ + 2,1) ≈ 2,5/ln(1/ρ) [N, exakter Kern] | Faktor ≈ 3·10³                  |
| Bedingen auf die Umgebung (Doob-Verhältnis κ₂) | im Beweis ersetzt durch 1/p je nahem Stück, e^{C(K)} ~ p^{−5}      | κ = 1,2–2,4 exakt (kleine Systeme), ln κ₂ ≈ 0,54K [N]     | Faktor e^{C(K)} statt e^{0,54K} |
| geteiltes Teilchen                             | Wahrscheinlichkeit ≤ 1/(b₋m) mit b₋ ≈ 10⁻⁵                         | ≈ 1/m [H]                                                 | Faktor 1/b₋ ≈ 10⁵               |
| Auswahl an nahen Vorkommen                     | (1 − 2ε)^{−1} je Vorkommen                                         | –                                                         | klein                           |
| Endzellen der Schleife                         | e^{C(K)}/n\_a am Schwanz, 1/(c₁p₁) je geteilter Kopfscheibe        | Testmodell: ∫ f² wächst um 1,00–1,14 je Scheibe [N]       | Faktor e^{2C(K)} ≈ exp(10³⁹)    |

C(K) = 6 ln(4π e^{(Λ²+1)/2}) + 5 ln(1/p) mit Λ = D + 2 (Anhang M, M.6). Beide Summanden sind im Beweis riesig: ln(1/p) ≈ 4900n ≈ 4·10³⁷, und Λ² ≈ D\_c² ≈ 2·10³⁸ (Kernfaktor e^{Λ²/2} für Endpunkte im Abstand ≤ Λs). Wahr laufen die Stücke etwa eine Zellseite weit, und der Kernfaktor wäre von der Ordnung 1.

### 3.7 Seltene Defekte

| Größe                                     | bewiesen                                                      | wahr bzw. gemessen                               | Abstand                       |
|-------------------------------------------|---------------------------------------------------------------|--------------------------------------------------|-------------------------------|
| Besucher eines Kastens (satz\_3\_9 §10.8) | P(N ≥ v) ≤ C exp(−0,2 (v/9 − 1)²) [S]: 0,89 bei v = 16        | 1,4·10⁻⁴ bei v = 16 (s = 16, freie Irrfahrt) [N] | Schranke 10⁻⁴ erst bei v ≈ 70 |
| Kurzzeit-Schwelle C\_β                    | ≥ 500 (Folgerung T6)                                          | –                                                | –                             |
| Raten D6, D7 (zeitgemittelte Dichte)      | q₁^{1/(4m\_D²)} mit m\_D ≈ 2D\_K ≈ 10¹⁹: Exponent ≈ 10⁻³⁸ [H] | e^{−cm} wie für die Teilchenzahl [H]             | verlangt ln(1/ρ) ≳ 10¹⁵³      |
| Peierls-Parameter q                       | q = 7 · max(Rate)^{1/7} → 0                                   | –                                                | –                             |

Diese Verluste sind riesig, legen ρ\* aber nicht fest: ln(1/ρ) ≳ 10¹⁵³ ist harmlos gegen die Bedingung aus 3.8.

### 3.8 Zusammensetzen: welche Bedingung ρ\* festlegt

Die Bedingungen an ρ stehen in Anhang Z, Z.9, Punkt 7. Die schärfste ist die Fortsetzung des Teilens an den Enden der Schleife (Anhang M, M.9.6 und M.9.8):

```text
η  =  e^{2C′(K)} / ((1 − 2ε)(b₋m − 2))  ≤  1/4,        C′(K) = 8 ln(4π e^{(Λ²+1)/2}) + 7 ln(1/p)
also   ln m  ≳  2C′(K)
```

| Stufe                      | ln(1/p)   | Λ²       | 2C′(K) | Folge                 |
|----------------------------|-----------|----------|--------|-----------------------|
| C (wahre Eingänge, K = 25) | 2πK ≈ 157 | ≈ 25     | ≈ 2450 | ln(1/ρ\*) ≈ 10¹⁰⁶⁴    |
| D (Beweis, K = 25)         | 1,1·10³⁷  | 4,4·10³⁷ | 5·10³⁸ | ln ln(1/ρ\*) ≈ 5·10³⁸ |
| D (Beweis, K = 100)        | 4,4·10³⁷  | 1,8·10³⁸ | 2·10³⁹ | ln ln(1/ρ\*) ≈ 2·10³⁹ |
| D (Beweis, K = 540)        | 2,4·10³⁸  | 9,6·10³⁸ | 10⁴⁰   | ln ln(1/ρ\*) ≈ 10⁴⁰   |

Der Kondensatanteil folgt aus ∫ f² dµ ≤ C e^{2C(K)} (4D\_c + 3)²/υ, also c ≈ υ³ e^{−2C(K)}/(16 C (4D\_c + 3)²) ≈ exp(−10³⁹) auf Stufe D und ≈ 10⁻⁷⁶³ auf Stufe C.

Alle anderen Bedingungen sind schwächer: geteilte Teilchen und Auswahl (κ₀ ≤ α\_J verlangt m ≳ e^{C(K)}/(b₋ α\_J), also ln m ≳ C(K) + 160), die Defektraten (ln(1/ρ) ≳ 10¹⁵³), die Isolation (ρ ≲ ζ² ≈ 10⁻⁴⁸⁰⁰) und σ\_ρ → 0 (ln(1/ρ) ≫ e^{8πK + κ\_U}).

## 4. Wo man am meisten gewinnen würde

Nach Wirkung auf die Schwelle geordnet. Keiner dieser Punkte ist für den Existenzsatz nötig.

1. **Ausweich-Untergrenze für ganze Scheiben** (Stufe D → C). Eine Schranke p ≥ e^{−CK} mit fester Konstante, ohne Zerlegung in n Teilintervalle, oder eine Zerlegung mit Kosten nahe 1 je Teilintervall. Dazu eine bessere Schranke für 𝔏 als Lemma F8 (Mittelwert statt Wurzel, ohne C\_𝔏 ≈ 2,4·10⁹). Das macht ρ\* von dreifach zu doppelt exponentiell, und D, D\_K, R\*″ und L₀ würden zu festen, mäßigen Zahlen.
2. **Kosten an den Enden mit dem Doob-Verhältnis statt 1/p** (Stufe C → B). Je nahem Stück e^{0,54K} statt p^{−5}, und an den Enden keine 14. Potenz. Das brächte ln(1/ρ\*) von 10¹⁰⁶⁴ auf etwa 10⁹ bis 10²⁷. Der Beweisweg dafür (Satz 6.2 im Manuskript) ist nur skizziert.
3. **Lokalität.** Ein Begegnungsradius von wenigen Zellen statt 10²⁰ gäbe ein Budget α ≈ 0,05 statt 10⁻⁴² und eine Mindestgröße L₀ ≈ 16 s.
4. **Dichteschranken schärfen.** Unter-Poisson (Var\_g ≤ E\_g, numerisch in allen 48 Fällen) beseitigt C\_a ≈ 10³; c₁ → 4π und Lemma 6.6 mit μ statt ε/N vergrößern b₋ um einen Faktor 20 bis 600, je nach Ausgangspunkt, und senken K auf ≈ 25.
5. **Bessere Skelette.** Schnellere Trennung (c\_vel ≈ 0,08 ist klein) vergrößert α\_max über 0,07.
6. **Die Grenze der Methode** (Stufe B → A). Der kleine Parameter bleibt 1/ln(1/ρ), und die Stoßkosten wachsen exponentiell in K. Zwei getrennte Skalen, grob für die Statistik und fein für den Staffellauf, würden das lösen (Tutorial §9.3). Ohne eine neue Idee bleibt ρ\* auch dann bei e^{−10⁹}.

## 5. Woher die Zahlen kommen

| Zahl                                         | Quelle                                                          |
|----------------------------------------------|-----------------------------------------------------------------|
| N₀/N bei ρ = 1/16, Z₀, kleine Systeme        | Tutorial §2.3, README (Wurm Runde 1), tutorial\_uebungen.py     |
| c₁, μ̄, C\_a, b₋, K, Unter-Poisson            | satz\_3\_9 §0, §3, §6, §7; Anhang E; Tutorial §7.3, §7.4        |
| Lemma 6.3a, Dyson-Lemma                      | Tutorial §6.3, §6.4; l1c\_widerstand.py, l1\_dyson\_reff.py     |
| Budget, Skelette                             | Tutorial §4.3; Anhang S (pruef\_schleifen\_geometrie.py)        |
| P\_δ, κ, κ₂                                  | Tutorial §8 (l2\_treffen.py, l2\_doob.py)                       |
| p\*, κ\_U; p₁, C′, θ\_P, C\_𝔏, C\_E, ζ, D\_K | Anhang U (U.5); Anhang F (F.10.4, F.11, F.12.6); Anhang P (P.7) |
| C(K), C′(K), η, Endzellen                    | Anhang M (M.6, M.9.5–M.9.8); Anhang Z (Z.9)                     |
| Testmodell ∫ f²                              | Anhang Z, Z.11; Anhang G, G.12.9 (Bemerkung zu (b) und (e))     |
| Besucher                                     | satz\_3\_9 §10.8; ergebnisse/pruef\_besucher\_s16.txt           |
| 2D-Bogoliubov-Verarmung 1/ln(1/(ρa²))        | Schick 1971, führende Ordnung [Lit]                             |
| alle abgeleiteten Größenordnungen            | verlustbilanz\_zahlen.py, ergebnisse/verlustbilanz\_zahlen.txt  |

## 6. Zum Vergleich: OpenAIs Beweis in 3D

Ganz grob, alles Schätzungen [H]. Die 3D-Zeilen stützen sich auf OA, Abschnitt 2 (Skalen) und Abschnitt 11 (Wahl der Konstanten); die 2D-Zeilen auf die Abschnitte oben.

|                                                    | OA, 3D (weiches, beschränktes Potential)                                                                                                                                         | wir, 2D (Gitter, harter Kern)                                                                               |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Wahrheit                                           | Kondensat bei allen kleinen Dichten; Verarmung ≈ (8/(3√π)) (ρa³)^{1/2} [Lit]; numerisch noch bei ρa³ ~ 1                                                                         | Kondensat bei allen gerechneten Dichten (bis ρ ≈ 0,19), N₀/N ≈ 0,75 bei ρ = 1/16; Verarmung ≈ 1/ln(1/(ρa²)) |
| kleiner Parameter der Methode                      | Potenzen von ρ: 1/m ~ ρ^{1/2} (OA: m ≍ ρ^{−1/2}), r^{−1/2} ~ ρ^{1/6}                                                                                                             | nur 1/ln(1/ρ)                                                                                               |
| Methode mit wahren Konstanten                      | ρ\*a³ grob 10⁻⁵ bis 10⁻¹⁴                                                                                                                                                        | ln(1/ρ\*) ≈ 10⁹, also ρ\* ≈ e^{−10⁹}                                                                        |
| Beweis mit seinen Konstanten                       | von OA nicht ausgerechnet; nach Bauart ρ\* ≈ exp(−6 C\_v) mit einer festen Zahl C\_v; für C\_v zwischen 10² und 10⁴ ist ρ\*a³ ≈ 10^{−300} bis 10^{−30000} (einfach exponentiell) | ln ln(1/ρ\*) ≈ 10³⁹ (dreifach exponentiell)                                                                 |
| Abstand Beweis zur Wahrheit, gemessen in ln(1/ρ\*) | ein fester Faktor, etwa C\_v                                                                                                                                                     | Faktor ≈ exp(10³⁹)                                                                                          |

**Warum 3D so viel besser ist.** Bei OA sind alle kleinen Größen Potenzen der Dichte, und die großen festen Konstanten stehen nur als Vorfaktor davor. OA sagt das in §11 selbst: „Fixed conditional bridge bounds may be large, but the encounter terms they multiply contain r^{−1/2} or m^{−1}“. Eine große Konstante C kostet dort nur ρ\* ~ e^{−6C}. Bei uns ist der kleine Parameter logarithmisch; dieselbe Konstante kostet ln(1/ρ\*) ~ e^{C}, also einen Exponenten mehr. Das ist der Schritt A → B der Verlusttreppe (ρ\* ≥ 1/16 gegen e^{−10⁹}).

**Warum unser Beweis noch einen Exponenten mehr verliert.** Der harte Kern verlangt Untergrenzen für das Ausweichen. OA hat ein beschränktes Potential und kommt mit Jensen aus, das gibt eine feste Konstante. Unsere Untergrenze p₁ = ½e^{−4900n} mit n ≈ 10³⁴ (Abschnitt 3.5) macht aus dem Faktor e^{C} den Faktor exp(10³⁸). Das ist der Schritt C → D.

Die 3D-Zahlen für ρ\* sind eine eigene Schätzung, nicht die von OA; OA gibt nur an, dass ρ\* von festen Konstanten abhängt, und rechnet sie nicht aus.
