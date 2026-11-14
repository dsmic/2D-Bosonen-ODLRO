# Anhang K: Kern-Schranken und Regularität der freien Irrfahrt

Stand 2026-11-10 nachts; K.4 am 2026-11-12 angepasst: (G3), das Fach R3 und b₀ entfallen ([anhang\_feinskala.md](anhang_feinskala.md), Anhang F). Schließt die Literatur-Eingänge von Anhang P (K1, K2), Satz T2 (Brückenmaximum, Schlauch) und Lemma S1 (BPP über OA Lemma 8.1), dazu die Seltenheit der Regularitätsverletzung (Fächer R2, R3 in Satz T2). Kennzeichnung: [S] bewiesen, [Lit] zitiert, [N] numerisch.

## Auf einer Seite

| Aussage                                 | Inhalt                                                                                      | Stand                                                        |
|-----------------------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| (K1) obere Gauß-Schranke                | p\_t(x) ≤ (1+t)^{−1} exp(−\|x\|²/(4(t + \|x\|\_∞)))                                         | [S] (Lemma K0, K1, ohne Literatur)                           |
| (K2) untere Gauß-Schranke               | p\_t(x) ≥ (4π)^{−1}(1+t)^{−1} exp(−\|x\|²/(4t)) für t ≥ 1, \|x\|\_∞ ≤ t                     | [N] scharf; bewiesen ist (K2′) mit e^{−1/2} mehr (Lemma K2′) |
| K3 Brückenmaximum                       | Schwankung ≥ h√t mit Wahrscheinlichkeit ≤ C e^{Cλ²} e^{−h²/C}                               | [S], gegeben (K1), (K2′)                                     |
| K4 Schlauch                             | Brücke bleibt im Schlauch der Breite a√t mit Wahrscheinlichkeit ≥ q\*(a, λ)                 | [S], gegeben (K2′)                                           |
| Lemma S1 ohne Literatur                 | OAs Beweis von Lemma 8.1 ist elementar                                                      | [S]                                                          |
| Lemma R Regularität der freien Irrfahrt | (G2\_A) versagt mit ≤ C τ^{1−c′(A)}, c′(A) ≥ cA − C; B\* hat doppelt-exponentielle Schwänze | [S], gegeben K3                                              |

## K.1 Der Kern in Produktform

Die Irrfahrt auf ℤ² in stetiger Zeit mit Rate 1 je Nachbar besteht aus zwei unabhängigen Koordinaten. Jede springt mit Rate 1 nach links und mit Rate 1 nach rechts. Also

```text
p_t(x) = q_t(x₁) q_t(x₂),        q_t(k) = e^{−2t} I_|k|(2t)
```

mit der modifizierten Bessel-Funktion I\_k.

*Neufassung 2026-11-13.* Bausteine und (K1) sind jetzt elementar bewiesen, ohne Literatur. Für die untere Schranke gibt es zwei Fassungen: (K2′) mit dem Faktor e^{−1/4} je Koordinate ist bewiesen; das scharfe (K2) ist nur numerisch gesichert. Die frühere Begründung von Schritt 1 war falsch (siehe unten, „Frühere Fassung“).

**Lemma K0 (Bausteine) [S].** Mit z = 2t und r\_j = I\_j(z)/I\_{j−1}(z), j ≥ 1:

1. **Rekursion:** I\_{j−1}(z) − I\_{j+1}(z) = (2j/z) I\_j(z), also 1/r\_j = 2j/z + r\_{j+1}.
2. **Log-Konkavität:** q\_t(k)² ≥ q\_t(k − 1) q\_t(k + 1) für alle k, also r\_{j+1} ≤ r\_j.
3. **Quotienten:** ℓ\_j := z/(j + √(j² + z²)) ≤ r\_j ≤ Ũ\_j := z/(j − 1 + √((j + 1)² + z²)).
4. **Mittelpunkt:** q\_t(0) ≤ Q(t) := min(e^{−2t + t²}, √π/(4√t)) für alle t > 0, und q\_t(0) ≥ (4πt)^{−1/2} für t ≥ 1.

*Beweis.*

1. Aus der Reihe I\_j(z) = Σ\_m (z/2)^{2m+j}/(m! (m+j)!) durch Verschieben des Index in I\_{j+1}: Die Glieder mit gleicher Potenz unterscheiden sich um den Faktor (m + j) − m = j.
2. Jede Koordinate springt mit Rate 1 nach rechts und mit Rate 1 nach links, ist also eine Differenz P₁ − P₂ zweier unabhängiger Poisson(t)-Größen. Daraus folgt q\_t(k) = e^{−2t} Σ\_m t^{2m+k}/(m! (m+k)!) = e^{−2t} I\_k(2t). Die Poisson-Gewichte sind log-konkav, denn ihr Quotient (n + 1)/n ist ≥ 1. Für eine log-konkave Folge a ohne innere Nullen gilt a\_{x+p} a\_{x+q} ≥ a\_x a\_{x+p+q} für p, q ≥ 0, weil die Quotienten a\_{n+1}/a\_n nicht wachsen. Also hat die Toeplitz-Matrix (a\_{i−j}) nur nichtnegative 2×2-Minoren. Nach Cauchy–Binet gilt das auch für das Produkt zweier solcher Matrizen, also für die Toeplitz-Matrix der Faltung c. Ihr Minor mit benachbarten Zeilen und Spalten ist c\_n² − c\_{n−1} c\_{n+1}.
3. Nach 1 und 2 ist 1/r\_j = 2j/z + r\_{j+1} ≤ 2j/z + r\_j, also r\_j² + (2j/z) r\_j − 1 ≥ 0 und r\_j ≥ √(1 + j²/z²) − j/z = ℓ\_j. Andererseits ist 1/r\_j ≥ 2j/z + ℓ\_{j+1} = 2j/z + (√((j+1)² + z²) − (j + 1))/z = (j − 1 + √((j+1)² + z²))/z.
4. I₀(z) = Σ (z/2)^{2m}/(m!)² ≤ Σ (z²/4)^m/m! = e^{z²/4} gibt die erste Schranke. Für die zweite schreibt man q\_t(0) = (1/π) ∫\_0^π e^{−2t(1 − cos θ)} dθ und benutzt 1 − cos θ ≥ 2θ²/π² auf [0, π]. Für die untere Schranke gilt 1 − cos θ ≤ θ²/2 − θ⁴/24 + θ⁶/720 ≤ θ²/2 − θ⁴/30 auf [0; 2,4], also e^{−2t(1−cos θ)} ≥ e^{−tθ²} (1 + tθ⁴/15). Über [0, ∞) integriert gibt das (4πt)^{−1/2} (1 + 1/(20t)). Der Rest über [2,4; ∞) ist für t ≥ 1 kleiner als der Gewinn (4πt)^{−1/2}/(20t); bei t = 1 ist er ≈ 0,001 gegen 0,014, und er fällt wie e^{−5,76t}. ∎

**Lemma K1 [S, gegeben Lemma K0].** Für alle t ≥ 0 und k ∈ ℤ gilt

```text
q_t(k)  ≤  (1 + t)^{−1/2} exp( −k² / (4(t + |k|)) )
```

*Beweis.* Nach Lemma K0 ist log q\_t(k) ≤ log Q(t) + Σ\_{j≤|k|} log Ũ\_j.

1. **k = 0:** Für t ≤ 1 ist −2t + t² + ½ ln(1 + t) ≤ t(t − 3/2) ≤ 0. Für t ≥ π/(16 − π) ist √π/(4√t) ≤ (1 + t)^{−1/2}.
2. **t ≥ 1, k ≥ 1:** Es ist −log Ũ\_j ≥ asinh((j − 1)/z) ≥ (j − 1)/(z + j − 1), und die Summe über j ≤ k ist ≥ k(k − 1)/(2(2t + k)). Ferner ist log(Q(t) √(1 + t)) ≤ log(√(2π)/4) ≤ −0,467. Es bleibt k²/(4(t + k)) − k(k − 1)/(2(2t + k)) = k(4t + 4k − 2k²)/((4t + 2k)(4t + 4k)) ≤ 0,467. Für k ≥ 1 + √(1 + 2t) ist die linke Seite ≤ 0, sonst ≤ k/(4t + 2k) ≤ (1 + √(1 + 2t))/(4t + 2 + 2√(1 + 2t)) ≤ 0,29.
3. **t < 1, k = 1:** Ũ₁ = z/√(4 + z²) ≤ t, also q\_t(1) ≤ t e^{−2t + t²} ≤ t e^{−t} ≤ 1/e, und die rechte Seite ist ≥ 2^{−1/2} e^{−1/4} ≥ 0,55.
4. **t < 1, k ≥ 2:** Ũ\_j ≤ z/(2j) ≤ 1/j, also q\_t(k) ≤ q\_t(1)/k! ≤ 0,368/k!. Die rechte Seite ist ≥ 2^{−1/2} e^{−k/4}, und 0,368 e^{k/4}/k! ≤ 0,31 < 2^{−1/2} für k ≥ 2. ∎

**Lemma K2′ [S, gegeben Lemma K0].** Für t ≥ 1 und |k| ≤ t gilt

```text
q_t(k)  ≥  e^{−1/4} (4π)^{−1/2} (1 + t)^{−1/2} exp( −k² / (4t) )
```

*Beweis.* Nach Lemma K0 ist q\_t(k) ≥ (4πt)^{−1/2} Π\_{j≤|k|} ℓ\_j und −log ℓ\_j = asinh(j/z) ≤ j/z. Die Summe ist ≤ k(k + 1)/(4t) ≤ k²/(4t) + 1/4 für |k| ≤ t, und (4πt)^{−1/2} ≥ (4π(1 + t))^{−1/2}. ∎

**Lemma K2 (scharf) [N].** Für t ≥ 1 und |k| ≤ t gilt q\_t(k) ≥ (4π)^{−1/2} (1 + t)^{−1/2} exp(−k²/(4t)). Die Konstante ist der Grenzwert bei k = 0, t → ∞, also scharf. Numerisch geprüft (Tabelle unten). Ein vollständiger Beweis fehlt: Weder der frühere Beweisweg noch die schärfere Quotienten-Schranke von Segura (2011), r\_j ≥ z/(j − ½ + √((j + ½)² + z²)), reichen. Die Kette q\_t(0) Π\_j r\_j mit dieser Schranke verfehlt die Konstante bei t ≈ 58, k = 24 um 0,1 % ([pruef\_bessel.py](pruef_bessel.py), Teil h). Das Projekt benutzt seit 2026-11-13 überall (K2′) statt (K2); die Zahlenwerte sind umgestellt (K.5).

*Frühere Fassung (bis 2026-11-13), Schritt 1:* „√z e^{−z} I₀(z) wächst monoton gegen 1/√(2π).“ Das ist falsch. Die Funktion steigt bis z ≈ 0,79 auf 0,469 und fällt dann von oben gegen 1/√(2π) = 0,3989 (pruef\_bessel.py, Teil a). Die benutzte Folgerung q\_t(0) ≥ (4πt)^{−1/2} für t ≥ 1 stimmt trotzdem (Lemma K0, Punkt 4). Schritt 3 („≥ −k²/(4t) − 1/4“) gab nur (K2′), nicht das scharfe (K2).

Ohne explizite Konstanten gelten beide Gauß-Schranken auch nach Delmotte (1999) [Lit]: parabolische Harnack-Ungleichung und Gauß-Schranken für Markov-Ketten auf Graphen mit Volumenverdopplung und Poincaré-Ungleichung, was für ℤ² gilt.

**Exakte Prüfung [N]** ([pruef\_kernschranken.py](pruef_kernschranken.py)): q\_t(k) = e^{−2t}I\_k(2t) auf einem Gitter t ∈ [0,05; 10⁵], |k| ≤ 30t + 30. In den tiefen Schwänzen wird die gleichmäßige Debye-Asymptotik benutzt.

| Schranke | Konstante im Exponenten | nötiger Vorfaktor         | Bemerkung                                                                |
|----------|-------------------------|---------------------------|--------------------------------------------------------------------------|
| (K1), 1D | c₁ = 1/4                | C₁ = 0,93 (≤ 1 mit t = 0) | c₁ = 0,3 versagt: 1/4 ist die Gauß-Rate, scharf                          |
| (K2), 1D | C₂ = 1/4                | c₂ = 0,2821 = 1/√(4π)     | Infimum bei k = 0, t → ∞; bei \|k\| = t ist die Cramér-Rate 0,2452 < 1/4 |

**In 2D** multiplizieren sich die Schranken. Wegen x\_i²/(t + |x\_i|) ≥ x\_i²/(t + |x|\_∞) folgen

```text
(K1)  p_t(x)  ≤  (1 + t)^{−1} exp( −|x|² / (4(t + |x|_∞)) )
(K2)  p_t(x)  ≥  (4π)^{−1} (1 + t)^{−1} exp( −|x|² / (4t) )        für t ≥ 1, |x|_∞ ≤ t
```

Das sind die Schranken, die Anhang P (Lemma P5, P6) und Satz T2 benutzen, mit c = 1/4, C = 1 und c = 1/(4π), C = 1/4. *Seit 2026-11-13* benutzt das Projekt statt des scharfen (K2) die bewiesene Fassung (K2′) mit c = e^{−1/2}/(4π) (K.1, K.5).

## K.2 Brückenmaximum und Schlauch

Für eine Brücke der Dauer t von u nach v sei Δ\_s = X\_s − (u + (s/t)(v − u)) ihre Schwankung um die gerade Verbindung, und λ = |u − v|/√t.

**Lemma K3 (Brückenmaximum) [S, gegeben (K1), (K2′)].** Für 1 ≤ λ√t ≤ t gilt P(sup\_s |Δ\_s| ≥ h√t) ≤ C e^{Cλ²} e^{−h²/C}.

*Beweis.*

1. Auf [0, t/2] hat die Brücke bezüglich der freien Irrfahrt ab u die Dichte p\_{t/2}(X\_{t/2}, v)/p\_t(u, v) ≤ 4π e^{1/2} e^{λ²/4} · 2 nach (K1), (K2′) (bis 2026-11-13 ohne e^{1/2}, mit dem scharfen (K2)).
2. Für die freie Irrfahrt ist e^{θ·(X\_s − u)} · e^{−2s(cosh θ − 1)} je Koordinate ein Martingal. Doobs Ungleichung und die Wahl θ = h/(4√t) geben P(sup\_{s≤t/2} |X\_s − u|\_∞ ≥ h√t/2) ≤ 4 e^{−h²/C}.
3. Die Gerade weicht auf [0, t/2] um höchstens λ√t/2 von u ab; das schluckt der Faktor e^{Cλ²}.
4. Die zweite Hälfte ist rückwärts gelesen eine Brücke von v aus; dieselbe Schranke. ∎

**Lemma K4 (Schlauch) [S, gegeben (K2′) und K3].** Für jedes a > 0 und λ ≤ λ₀ gibt es q\*(a, λ₀) > 0 mit P(sup\_s |Δ\_s| ≤ a√t) ≥ q\* für alle t ≥ t₀(a).

*Beweis.* Man zerlegt [0, t] in j = j(a) gleiche Teile, mit j so groß, dass auf jedem Teil die Schwankung mit Wahrscheinlichkeit ≥ ½ unter a√t/2 bleibt (K3 mit Dauer t/j). Man verlangt, dass die Brücke an den j − 1 Knoten im Abstand ≤ a√t/4 von der Geraden liegt. Nach (K2) hat jeder Knoten, gegeben den vorigen, mindestens Wahrscheinlichkeit c(a, j, λ₀) > 0, dort zu landen. Das ergibt q\* ≥ (c/2)^j. ∎

In Satz T2 (§10.2, Lokalisierung) ist das die Aussage „eine Irrfahrt der Dauer c₁δ bleibt mit Wahrscheinlichkeit ≥ q\* im Schlauch“, für die Brücke von S nach E (OA (18) benutzt genau die Brücke).

## K.3 Lemma S1 braucht keine Literatur

Lemma S1 (Anhang S) überträgt OA Lemma 8.1. OAs Beweis ist in sich vollständig und elementar. Er benutzt nur:

1. unabhängige, auf [−1, 1] gleichverteilte Variablen in dyadischen Blöcken;
2. die Beobachtung, dass ein unbenutzter Block der Länge ≥ k/4 einen gleichverteilten Summanden der Breite ≥ c k^{3/4} beiträgt, also je Koordinate eine Dichte ≤ C k^{−3/4} und für zwei unabhängige Koordinaten ≤ C k^{−3/2};
3. die Entwicklung e^{θΣX} = Π(1 + (e^{θX} − 1)) mit geordneten Tupeln.

Die Zitate auf Benjamini–Pemantle–Peres und Häggström–Mossel bei OA sind Herkunftsangaben, keine Beweiseingänge. Lemma S1 ist damit [S].

## K.4 Lemma R: Regularität der freien Irrfahrt

Y sei die freie Irrfahrt (Rate 1 je Nachbar) auf [0, 2τ]. (G2\_A) und B wie in Anhang P, P.7.1.

**Lemma R (a) [S].** Es gibt c, C mit

```text
P( (G2_A) versagt auf [0, τ] )  ≤  C(A) τ^{1 − c′(A)} + 2τ e^{−A/C},        c′(A) ≥ cA − C
```

*Beweis.*

1. **Feste Stelle σ ∈ ℤ.** Mit T\_0 = [0, 1] und T\_j = [2^{j−1}, 2^j] seien V\_j = sup\_{u∈T\_j} |Y\_{σ+u} − Y\_{σ+2^{j−1}}|\_∞ / 2^{j/2} (V\_0 mit Startpunkt σ). Die V\_j hängen von disjunkten Zeitintervallen ab und sind unabhängig. Nach K3 (für die freie Irrfahrt, Schritt 2) ist E e^{V\_j} ≤ C\_V gleichmäßig in j.
2. **Unruhiges Fenster.** Für W\_i = [2^i, 2^{i+1}] ist sup\_{u∈W\_i} |Y\_{σ+u} − Y\_σ| ≤ Σ\_{j≤i+1} 2^{j/2} V\_j. Ist W\_i unruhig, gilt also Σ\_{j≤i+1} 2^{(j−i)/2} V\_j > A.
3. **Viele unruhige Fenster.** Summiert über die unruhigen i: A · #unruhig < Σ\_i Σ\_{j≤i+1} 2^{(j−i)/2} V\_j ≤ C\_g Σ\_{j≤J} V\_j, mit C\_g = Σ\_{m≥−1} 2^{−m/2} ≈ 4,83 und J = log₂(2τ). Sind mindestens N\_w/2 der N\_w ≥ log₂(τ/A²) − 2 Fenster unruhig, ist Σ\_j V\_j ≥ A N\_w/(2C\_g).
4. **Exponentielle Tschebyscheff-Ungleichung:** P(Σ\_{j≤J} V\_j ≥ A N\_w/(2C\_g)) ≤ C\_V^{J+1} e^{−A N\_w/(2C\_g)} ≤ C(A) τ^{−c′(A)} mit c′(A) = (A/(2C\_g) − ln C\_V)/ln 2.
5. **Alle σ.** Die Vereinigung über σ ∈ {0, …, τ} gibt den Faktor τ + 1. Für nicht ganzzahlige σ verschieben sich die Fenster um < 1. Hat jedes Einheitsintervall höchstens b = A/2 Sprünge (sonst Wahrscheinlichkeit ≤ 2τ e^{−A/C}, Poisson-Schwanz), ändern sich die Verschiebungen um ≤ A/2, und man wendet Schritt 1–4 mit A/2 an. ∎

**Lemma R (b) [S].** Mit β = sup\_{t ≤ 2τ} |Y\_t − Y\_0|\_∞²/max(t, 1) ist B\* ≤ 1 + log₂(4β) und

```text
P( B* ≥ b )  ≤  P( β ≥ 2^{b−3} )  ≤  C log₂(2τ) · exp(−c 2^{b})
```

*Beweis.* β ≥ v verlangt für ein dyadisches t ≤ 2τ, dass sup\_{u≤2t} |Y\_u − Y\_0| ≥ √(vt). Nach Schritt 2 im Beweis von K3 hat das je Skala Wahrscheinlichkeit ≤ C e^{−cv}. Die Vereinigung über log₂(2τ) Skalen ergibt die Behauptung. ∎

**Für Brücken** (das Fach R2 in Satz T2, früher auch R3, betrifft Stücke mit festen Endpunkten): Die Dichte der Brücke bezüglich der freien Irrfahrt ist auf jeder Hälfte ≤ C e^{Cλ²} (K3, Schritt 1). Also gelten (a) und (b) für Brücken mit einem festen Faktor.

**Folgen für die Konstanten.**

- In Satz T2 ist η\_{R2} = (C τ^{1−c′(A)})^{2/3}. Die Bedingung δM\_{R2} ≳ 16πK verlangt (c′(A) − 1) ln τ ≳ 48πK. Das ist für jedes feste A > A₀ = (C + 1)/c erfüllt, sobald ρ klein genug ist.
- Lemma P6 braucht (G2\_A) für alle dyadischen Horizonte zwischen τ/(8J) und τ/2 (Anhang F, F.11.1). (a) gilt für jeden Horizont τ″, mit τ″ statt τ in der großen Abweichung. Die Vereinigung über die höchstens log₂(8J) Horizonte kostet den festen Faktor log₂(8J) · (8J)^{c′(A)}.
- (b) wird seit 2026-11-12 nicht mehr gebraucht. (G3) und das Fach R3 sind durch die Kurzzeit-Bedingung (G4) ersetzt (Anhang F, F.11.3: Lemma F11a und Satz F11). Damit entfallen b₀ und C₁ = b₀ + 1. An ihre Stelle tritt die Schwelle β = C\_β ln ln(1/ρ) in t\_r = r²/(16β). Sie wächst ebenfalls langsam mit ρ, geht aber nur in Terme o(ln(1/ρ)) und in die Defektraten ein; θ, n = K/θ und p\* hängen nicht mehr von ρ ab. P\_treff ~ ln ln(1/ρ)/ln(1/ρ) folgt aus (G4) und (G2\_A) allein (Lemma F13), und σ\_ρ = C P\_treff/p\* geht gegen 0.
- *Frühere Fassung:* Bei R3 wuchs der Faktor log₂(2τ) mit ln(1/ρ). Also musste 2^{b₀} ≳ C ln ln(1/ρ) + 32πK sein, b₀ wuchs wie log₂ ln ln(1/ρ), und mit ihm C₁, 1/θ und n. Dass C₁ = b₀ + 1 in (G3) genügt, folgt aus R3 allein nicht (Review K1, Teil 3).

**Zahlen [N]** ([pruef\_regularitaet.py](pruef_regularitaet.py)): Für τ = 4096 versagt (G2\_A) mit Wahrscheinlichkeit 0,95; 0,42; 0,03; 0 bei A = 4, 5, 6, 8. Bei τ = 16384 (200 Bahnen) sind es 0,67; 0,06; 0 bei A = 5, 6, 7 (ergebnisse/pruef\_regularitaet\_16384.txt). Bei τ = 65536 (150 Bahnen) sind es 0,107; 0,020; 0 bei A = 6, 7, 8 (ergebnisse/pruef\_regularitaet\_65536.txt). Für A ≤ 7 wächst die Versagenswahrscheinlichkeit also noch mit τ, wie (a) mit c′(A) < 1 vorhersagt; A = 8 versagt bei keinem der drei τ. Die Schranke in der früheren Bedingung (G3) bleibt stabil: B ≤ 8,4 im Maximum bei allen τ (99 %-Wert 7,95 bzw. 8,23).

## K.5 Was damit geschlossen ist

- **Anhang P:** (K1), (K2′) in P5 und P6 mit expliziten Konstanten (in Anhang P als (K2) in allgemeiner Form c(1 + t)^{−1}e^{−C|x−y|²/t} geschrieben, das deckt (K2′)).
- **Satz T2:** Gauß-Vergleich der Kerne in §10.2 (K1, K2′), Brückenmaximum (K3), Schlauch (K4), Seltenheit des Fachs R2 (Lemma R (a)). Das Fach G4, das R3 ersetzt, steht in Anhang F (Lemma F11a).
- **Lemma S1:** ohne Literatur-Eingang.

*Stand 2026-11-13:* (K1) und (K2′) sind elementar bewiesen (K.1, Lemma K0, K1, K2′), ohne Literatur. Das scharfe (K2) ist nur numerisch gesichert [N]. Alle Stellen, an denen (K2) eingeht, sind auf (K2′) umgestellt, mit dem Faktor e^{1/2} je Benutzung in 2D: Anhang F, (W1)–(W3), P6a″ (C\_b ≤ 394), P6b″ (c₂ = 4·10⁻⁴, e^{−9,3(1+λ²)}, ζ-Bedingung mit 2,0·10⁵), P6″ (C′ = 9,3(1 + 520e^{1,75γ\_n²}), λ₁ mit 352n, ζ-Bedingung mit 1,8·10⁴), F.12.6 (C′ ≤ 4900, (352n)^{−133}), Satz F11 (p₄ mit 512πe^{1/2}); Anhang U (P^{br}\_treff mit 16πe^{1/2}); Anhang P (P.7.5, C\_b); K3 (Schritt 1); Anhang M (Lemma M2, M8, C(K), C′(K) mit 4πe^{(Λ²+1)/2}); satz\_3\_9 §10.8 (Lemma T5 mit 119c₁); Anhang Z, Z.9 (C′ ≤ 4900). Allgemeine Konstanten C, c (Lemma P5, P5″, F13, K4, Lemma C, Satz T2 Schritt 1) ändern nur ihren Wert. [pruef\_feinskala.py](pruef_feinskala.py) besteht mit den neuen Schwellen. Frühere Fassung: „Offen bleibt als Literatur nur Schritt 1 und 2 in K.1 …, beides Standard.“ Schritt 1 war dabei falsch begründet (K.1, „Frühere Fassung“).
