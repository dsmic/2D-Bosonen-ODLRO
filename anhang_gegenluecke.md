# Anhang G: Die Gegen-Lücke (Satz 5.2 ausgeschrieben)

> **Lesehinweis (2026-11-13, Review H1).** Gültig sind G.10 bis G.12 (Zeitschleife); G.0 bis G.9 beschreiben den verworfenen Weg über die Lücke und stehen nur als Vorgeschichte da. Wer neu liest, beginnt bei G.10. Der Stand der ganzen Beweiskette steht in [anhang\_zweites\_moment.md](anhang_zweites_moment.md), Z.12 und Z.13.

Teil 1, 2026-11-10. **Stand:** G.10 (Zeitschleife statt Lücke) und G.11 (Prüfung der offenen Punkte, Spiegel-Abweg) gehen G.0–G.9 vor. Gehört zu [tutorial\_beweis\_verduennt.md](tutorial_beweis_verduennt.md) §5 und §10, Punkt 1. Vorbild ist §9–§10 der OpenAI-Arbeit „A density-uniform condensate bound for dilute Bose gases“ (2026-09-27); Gleichungsnummern „OA (26)“ usw. beziehen sich dorthin. Kennzeichnung: [S] bewiesen, [B] Beweisskizze, [N] numerisch, [Lit] Literatur.

## Auf einer Seite

**Aussage (Satz G).** Für den zeitartigen Staffellauf aus Tutorial §5 gilt

```text
|ν|²  ≤  g̃⁻(T) · ∫ f̂² dΓ̂                                          (Cauchy–Schwarz)
∫ f̂² dΓ̂  ≤  C_end · e^{−T(E_{N+1} − E_N)} · C_Skelett                (zweites Moment über den Gegen-Zustand)
⇒  N₀/N  ≥  g⁻(T)  ≥  e^{Δ₂T} |ν|² / (C_end · C_Skelett)
```

Dabei ist g̃⁻(T) = g⁻(T) e^{−T(E\_{N−1} − E\_N)} die Lückenmasse pro Teilchen, Γ̂ = Γ\_T/N und f̂ = dν/dΓ̂. C\_Skelett beschränkt die exponentiellen Begegnungsmomente der Routen, C\_end hängt nicht von L, N oder ρ ab (G.8.3). **Bedingt:** Die zweite Zeile braucht das Übertragungs-Lemma G.8.4 (2.), und das ist offen. Das ist Satz 5.2 des Tutorials; die Masse der Gegen-Lücke wird dabei mitbeschränkt und tritt nicht mehr als Faktor auf.

**Idee in vier Schritten.**

1. **Dichte ausrechnen (G1).** ν entsteht aus dem geschlossenen Maß durch einen Austausch von Linienstücken. Weil jedes neue Stück aus seinem exakt normierten bedingten Gesetz gezogen wird, hat die Dichte f = dν/dΓ\_T eine geschlossene Form: einen Quotienten zweier bedingter Zustandssummen je Scheibe, mit N bzw. N − 1 Linien.
2. **Zweites Moment als Doppelsumme (G2).** ∫ f² dΓ\_T = ∫ f dν ist ein Mittel über zwei unabhängige Routen: R′ baut die Lücke, R wertet f aus.
3. **Gegen-Zustand B (G3).** Man vergleicht nicht mit dem geschlossenen Zustand, sondern mit B = „geschlossen plus eine zusätzliche Linie längs R“. Fern von Begegnungen stehen sich dann überall bedingte Zustandssummen mit gleicher Linienzahl und gleichem Rand gegenüber und kürzen sich *exakt*.
4. **Nahe Begegnungen (G4–G7).** Nur dort bleibt ein Faktor. Er ist beschränkt bei geteilten Teilchen und klein (≈ 1/ln(1/ρ)) bei nahen verschiedenen Brücken.

**Stand.**

| Schritt | Inhalt                                                    | Stand                                                 | Gegenstück bei OpenAI |
|---------|-----------------------------------------------------------|-------------------------------------------------------|-----------------------|
| G1      | Dichteformel                                              | [S], exakt geprüft                                    | OA §9.4, (26)         |
| G2      | zweites Moment als Doppelsumme                            | [S]                                                   | OA (27)               |
| G3      | Gegen-Zustand B, Zerlegung der Stücke, exakte Fernkürzung | [S]                                                   | OA §10.1, (28)        |
| G4      | Untergrenzen der beiden Nenner                            | [B], ausgeschrieben (G.6), Lemma P\* statt Jensen     | OA §10.2, (29)        |
| G5      | Wechselwirkungsgewicht im Gegen-Zustand wiederherstellen  | [B], ausgeschrieben (G.7)                             | OA §10.3, (29a)       |
| G6      | Auswahl und Nebenbedingungen bleiben erhalten             | [B], ausgeschrieben nach OA (G.5)                     | OA §10.4              |
| G7      | Summieren über Routen und Tupel, Endzellen                | [B], ausgeschrieben (G.8); offene Teilaussagen in G.9 | OA §10.5, Satz 7.3    |

**Was neu ist gegenüber OpenAI.**

- Die Teilchenzahl ändert sich: Die Lücke hat N − 1 Linien, der Gegen-Zustand N + 1. Daher kommt der Faktor e^{−Δ₂T}.
- Der Austausch ist ein *Löschen mit zyklischem Weiterreichen*: Je Scheibe gibt es ein Stück weniger. Bei OpenAI bleibt die Zahl der Pfade gleich, nur ein Endpunkt wird versetzt.
- Die Kosten naher verschiedener Brücken fallen in 2D nur wie 1/ln(1/ρ), nicht wie eine Potenz (Anhang zu den Stoßkosten, noch zu schreiben).
- Die Route wird Scheibe für Scheibe aus dem Skelett gebaut und hängt von der Endzelle des Lochstücks j₀ ab. j₀ darf nicht wählbar sein müssen, sonst fiele die Annahmewahrscheinlichkeit wie (1 − ε)^w (G.5.1).

## G.0 Rahmen

- **Weltlinien.** Raum-Zeit Λ × [0, β), periodisch in der Zeit. Gewicht: Lebesgue-Maß der Sprungzeiten, harter Kern. Z\_N(β) ist die Zustandssumme, P = Gewicht/Z\_N das geschlossene Maß. Alle Schranken sind gleichmäßig in β; am Ende β → ∞.
- **Lückenmaß Γ\_T.** Geschichten mit N − 1 Linien auf (0, T) und N Linien sonst. Bei (x, 0) endet eine Linie (Schwanz), bei (y, T) beginnt eine (Kopf). Γ\_T(dO) = Gewicht(O)/(M Z\_N). Seine Masse ist (1/(M Z\_N)) Tr(e^{−(β−T)H} B⁺ e^{−TH} B) mit B = Σ\_x b\_x; für β → ∞ ist das G̃⁻(T).
- **Gegen-Lückenmaß.** Ebenso mit N + 1 Linien auf (0, T): eine Linie beginnt bei (x, 0) und endet bei (y, T). Masse Ğ⁺(T) für β → ∞.
- **Scheiben und Stücke.** t\_k = kδ, k = 0, …, w, T = wδ. Jede Linie einer Geschichte zerfällt in Stücke, eines je Scheibe [t\_k, t\_{k+1}], mit Anfang S und Ende Y.
- **Zellen, wählbar, Schnitt.** Zellen sind Quadrate der Seite s. Ein Stück gehört zur Zelle seines Endes Y. Wann es *wählbar* ist, steht genau in G.5.1; die *Schnittbedingung* cut verlangt, dass ein Stück eine feste Umgebung (Radius R s) seines Endes nicht verlässt, wie cut\_R bei OpenAI. Wählbarkeit und cut hängen nur von Stücken derselben Scheibe in der Nähe ab. (Fassung 1 dieses Anhangs und das Tutorial verlangten „S und Y in derselben Zelle“; das ist zu eng, siehe G.5.1.)
- **Routen.** Ein *Skelett* γ = (γ₀, …, γ\_w) ist ein zufälliger Pfad benachbarter Zellen in Raum-Zeit, eine Zelle je Scheibengrenze (Tutorial §4, OA §8.1). Die *Route* R ist die daraus abgeleitete Folge von Sternpfaden P\_k = (c₀^k, …, c\_{m\_k}^k) verschiedener Zellen; wie sie von γ und von der Konfiguration abhängt, steht in G.5.1.

## G.1 Der Staffellauf

Gegeben sei eine geschlossene Geschichte C ~ P.

1. Wähle das Schwanz-Teilchen gleichverteilt unter den N Teilchen zur Zeit 0 (Gewicht 1/N); x sei sein Platz, a₀ seine Zelle. Ziehe das Skelett γ ab a₀.
2. Für k = 0, …, w − 1:
   - j₀ ist das Stück, das am Lochplatz h\_k beginnt (h₀ = x; sonst das Ende von j\_m der vorigen Scheibe). Es wird *nicht* ausgewählt und muss nicht wählbar sein. Seine Endzelle c₀ legt den Anfang des Sternpfads fest (G.5.1).
   - Für l = 1, …, m wähle j\_l gleichverteilt unter den wählbaren Stücken der Zelle c\_l. Gewicht 1/g\_{c\_l}(C); gibt es keines, wird verworfen.
   - Lösche das Stück von j₀. Ziehe neue Stücke („Brücken“) S\_l → Y\_{l−1}, l = 1, …, m, aus dem bedingten Gesetz bei festen übrigen Stücken der Scheibe, eingeschränkt durch cut: Dichte Gewicht/Z^{br}\_k.
   - Der neue Lochplatz ist h\_{k+1} = Y\_m.
3. Ausgabe ist O, eine Lücken-Geschichte mit Schwanz x und Kopf y = h\_w.

ν ist das Gesetz von O. Es ist ein Unterwahrscheinlichkeitsmaß; seine Masse |ν| ist die Annahmewahrscheinlichkeit.

In G1 steht π(R) dann für E\_γ[1{Sternpfade = P(Ĉ, γ)}], ausgewertet im hypothetischen Zustand Ĉ, genau wie h\_γ(Ĉ, I) in OA (26). Der Beweis von G1 ändert sich dadurch nicht, denn er braucht nur, dass Auswahl und Route Funktionen des geschlossenen Zustands und des Skeletts sind.

## G.2 Die Dichteformel

Für eine Lücken-Geschichte O und Rückwärtsdaten (R, h₁, …, h\_{w−1}, I₀, …, I\_{w−1}) sei:

- h\_k ein in O zur Zeit t\_k freier Platz in der Zelle a\_k, mit h₀ = x und h\_w = y;
- I\_k = (b₁, …, b\_m) ein Tupel verschiedener Stücke von O in Scheibe k mit S(b\_l) ∈ c\_l und Y(b\_l) ∈ c\_{l−1} (die Brücken);
- Ĉ der *hypothetische geschlossene Zustand*: O ohne die Brücken, dafür alte Stücke S\_l → Y\_l für l = 0, …, m mit S₀ = h\_k, S\_l = S(b\_l), Y\_l = Y(b\_{l+1}) und Y\_m = h\_{k+1};
- Z^{alt}\_k = ∫ 1\_cut · acc\_k · sel\_k(Ĉ) dW über die Geschichten der m + 1 alten Stücke bei festen übrigen Stücken von O, wobei sel\_k = Π\_{l≥1} 1{j\_l wählbar}/g\_{c\_l}(Ĉ);
- Z^{br}\_k = ∫ 1\_cut dW über die Geschichten der m Brücken bei denselben festen Stücken.

**Lemma G1 (Dichteformel) [S].**

```text
f(O) = dν/dΓ_T (O)  =  (M/N) · Σ_R π_{a₀}(R) 1{a_w = Zelle(y)} · Σ_{h₁…h_{w−1}} Π_{k=0}^{w−1} Σ_{I_k} Z^alt_k / Z^br_k
```

*Beweis.*

1. **Umkehrbarkeit.** Vorwärtsdaten (C, Schwanz-Teilchen, R, Tupel, neue Brücken) und Rückwärtsdaten (O, R, Lochplätze, Brücken-Tupel, alte Stücke) entsprechen einander eindeutig: O entsteht aus C durch Austausch der Stücke auf den Tupeln, und C entsteht aus O, indem man die Brücken durch die alten Stücke ersetzt. Dabei werden nur Stücke umbenannt; das Lebesgue-Maß der Sprungzeiten bleibt erhalten (Jacobi-Faktor 1, wie OA §9.4).
2. **Produktstruktur.** Nach Lemma 3.1 des Tutorials (Markov-Eigenschaft) zerfällt das Gewicht einer Geschichte in die Gewichte der Stücke mal den Indikator „kein Stoß“. Bei festen übrigen Stücken einer Scheibe hängt der Indikator nur von den Stücken dieser Scheibe ab. Also gilt Gewicht(C) = Gewicht(Rest) · Π\_k W(alte Stücke\_k) und Gewicht(O) = Gewicht(Rest) · Π\_k W(Brücken\_k), mit demselben Rest.
3. **Zusammensetzen.** ν(dO) ist die Summe über alle Rückwärtsdaten von (1/N) · π(R) · P(C) · Π\_k sel\_k · W(Brücken\_k)/Z^{br}\_k. Teilen durch Γ\_T(dO) = Gewicht(O)/(M Z\_N) gibt den Faktor M/N und je Scheibe sel\_k W(alte Stücke\_k)/Z^{br}\_k. Integrieren über die alten Stücke ergibt Z^{alt}\_k. ∎

**Exakte Prüfung [N]** ([pruef\_gegenluecke.py](pruef_gegenluecke.py)). Mini-System in diskreter Zeit: Ring mit 6 Plätzen, 3 Zellen zu je 2 Plätzen, N = 3. Die Zeit ist Trotter-zerlegt (gerade, dann ungerade Bindungen); Gewicht λ^{Sprünge} ist das diskrete Gegenstück zu „Gewicht 1 je Sprung“. 4 Schritte periodisch, Lücke über 2 Scheiben, Züge d ∈ {−1, 0, 1, 2}, also m bis 2. ν wurde durch vollständige Vorwärtsrechnung über alle 65 542 geschlossenen Geschichten bestimmt, f durch die Formel. Ergebnis: ν(O) = f(O) Γ(O) auf allen Lücken-Geschichten mit ν > 0, bis auf Rundungsfehler.

| N   | Schritte | λ    | geschlossene Geschichten | Lücken-Geschichten mit ν > 0 | größter relativer Fehler |
|-----|----------|------|--------------------------|------------------------------|--------------------------|
| 3   | 4        | 0,7  | 65 542                   | 175 233                      | 5·10⁻¹⁶                  |
| 3   | 4        | 0,35 | 65 542                   | 175 233                      | 6·10⁻¹⁶                  |
| 2   | 5        | 0,9  | 154 455                  | 86 676                       | 5·10⁻¹⁶                  |

## G.3 Das zweite Moment

**Lemma G2 [S].**

```text
∫ f² dΓ_T  =  ∫ f dν  =  (M/N) · E_C E_{R′, I′, Brücken} [ Σ_R π(R) Σ_{h, I} Π_k Z^alt_k(O) / Z^br_k(O) ]
```

Dabei entsteht O aus C längs R′ mit dem Tupel I′. Das ist das Gegenstück zu OA (27). Mit Lemma 5.1 des Tutorials folgt |ν|² ≤ |Γ\_T| ∫ f² dΓ\_T.

*Beweis.* f² dΓ = f dν nach Definition der Dichte; dann G1 einsetzen. ∎

**Zahlen im Mini-System [N].** |ν| = 0,1472, ∫ f² dΓ = 0,0482 und |Γ| = 1,1433 (Transfermatrix). Also ist |ν|²/∫ f² = 0,450 ≤ |Γ|, wie es sein muss. Cauchy–Schwarz verliert hier einen Faktor 2,5, weil das System winzig ist und die Routen sich ständig begegnen.

## G.4 Der Gegen-Zustand und die exakte Fernkürzung

Fest sei ein Summand von G2: Vorwärtstupel I′ längs R′ (erzeugt O aus C) und Rückwärtstupel I längs R (erzeugt Ĉ aus O). In jeder Scheibe zerlegt man die beteiligten Stücke wie OA §10.1:

```text
h = I ∩ I′  (geteilte Stücke)      d = h ∪ pred_I(h)      j = I \ d      l = I′ \ h      L = alle übrigen
```

Der **Gegen-Zustand B** ist stückweise erklärt:

| Zustand          | auf j                | auf l            | auf d  | auf L |
|------------------|----------------------|------------------|--------|-------|
| C (geschlossen)  | C\_j                 | C\_l             | C\_d   | C\_L  |
| O (Lücke)        | O\_j = C\_j          | O\_l neu gezogen | neu    | C\_L  |
| Ĉ (hypothetisch) | Ĉ\_j alt, integriert | Ĉ\_l = O\_l      | alt    | C\_L  |
| B (Gegen-Lücke)  | B\_j = Ĉ\_j          | B\_l = C\_l      | frisch | C\_L  |

Auf j hat Ĉ ein Stück mehr als O = C, auf l hat O eines weniger als C. Fern von den Begegnungen ist B also „C plus eine Linie längs R“: ein Element des Gegen-Lückenmaßes.

**Lemma G3 (Fernkürzung) [S].** Haben die Stücke auf j und auf l wegen cut keinen gemeinsamen Raum-Zeit-Bereich, dann gilt für die Integration über C\_j, C\_l, O\_l und Ĉ\_j bei festem Rest:

```text
∫ P(C) · [ W(O_l) / Z^br_{I′}(O) ] · [ sel(Ĉ) W(Ĉ_j) / Z^br_I(O) ]   =   ∫ P(B) · sel(B)      (auf j und l)
```

Die beiden Wechsel „gelöscht/neu gezogen“ heben sich also exakt gegen das Gewicht des Gegen-Zustands auf. Es bleibt kein Faktor, der mit der Länge der Route wächst.

*Beweis.*

1. **l-Teil.** Z^{br}\_{I′}(O) integriert die Brücken auf l bei festen übrigen Stücken. Die übrigen Stücke sind C\_L und C\_j = O\_j; Ĉ\_j kommt in diesem Nenner nicht vor. Integration über O\_l gibt ∫ W(O\_l)/Z^{br}\_{I′} = 1, sofern der Faktor sel(Ĉ) W(Ĉ\_j)/Z^{br}\_I(O) nicht von O\_l abhängt. Das ist der Fall, weil O\_l und die j-Stücke wegen cut nicht zusammenstoßen können und die Wählbarkeit lokal ist.
2. **j-Teil.** Z^{br}\_I(O) integriert die Brücken auf j bei festen übrigen Stücken; das sind C\_L und O\_l, und O\_l ist für j unsichtbar. Die Brücken auf j sind in O gerade die Stücke C\_j. Integration von P(C) ∝ W(C\_j) · (Rest) über C\_j bei festen Endpunkten gibt Z^{br}\_I · (Rest) und kürzt den Nenner.
3. **Übrig** bleibt W(C\_L) W(C\_l) sel(Ĉ) W(Ĉ\_j)/Z\_N. Das ist P(B) sel(B), denn B\_j = Ĉ\_j, B\_l = C\_l, B\_L = C\_L, und die Auswahl hängt nur von Stücken nahe der Zellen von R ab, die in Ĉ und B gleich sind. ∎

*Bemerkung.* Das ist das Gegenstück zu OA (28): Dort bleibt der Kernquotient K\_C K\_Ĉ/(K\_B K\_O) nur auf d. Neu ist bei uns nur, dass B eine Linie *mehr* hat als C. Daher vergleicht das zweite Moment die Lückenmasse mit der Gegen-Lückenmasse, und der Faktor e^{−Δ₂T} entsteht.

## G.5 Wählbarkeit, Route und ihre Stabilität (Schritt G6) [B, nach OA §10.4]

### G.5.1 Die genauen Definitionen

Beim Ausschreiben zeigte sich: Die vorläufigen Festlegungen des Tutorials (§5.2) sind zu eng, und zwar an zwei Stellen.

- **Wählbar heißt nicht „Anfang und Ende in derselben Zelle“.** Bei Scheibendauer δ ≈ s² wandert eine Linie in einer Scheibe etwa eine Zellseite weit. Dann wäre nur ein fester Bruchteil der Stücke wählbar. Der Vergleich in G.5.4 kostet aber je naher Begegnung den Kehrwert des wählbaren Anteils. Man braucht deshalb einen Anteil 1 − ε mit kleinem ε.
- **Das Stück am Loch darf nicht wählbar sein müssen.** j₀ wird nicht ausgewählt, sondern ist das Stück, das am Loch beginnt. Verlangt man seine Wählbarkeit, wird in jeder Scheibe mit Wahrscheinlichkeit etwa ε verworfen, und die Annahmewahrscheinlichkeit fällt wie (1 − ε)^w mit w ~ L/s Scheiben. Das wäre fatal. Fern von Begegnungen braucht man die Wählbarkeit von j₀ auch nicht, denn G3 gilt für jede Konfiguration. *Nachtrag 2026-11-12 (Review K3):* Ganz ohne Bedingung an j₀ geht es nicht: Sein Ende muss isoliert sein, und es darf nicht weit wandern. Beides erreicht man ohne Verwerfen, indem j\_m der Scheibe davor nur unter Stücken mit regulärer Fortsetzung gewählt wird (Wählbarkeit über zwei Scheiben, [anhang\_lochstueck.md](anhang_lochstueck.md), Anhang L).

Die genauen Festlegungen folgen OA §5:

- **Zelle eines Stücks:** die Zelle seines Endes Y. n\_Q ist die Zahl der Stücke mit Ende in Q.
- **Wählbar** ist ein Stück, wenn
  1. sein Anfang S unter den Anfängen und sein Ende Y unter den Enden den Abstand > r = ζρ^{−1/2} zu allen anderen haben (Isolation);
  2. es die Kugel vom Radius D s um sein Ende nicht verlässt (Makro-Bedingung);
  3. es in den ersten und letzten Zeitintervallen der Länge τ₀ innerhalb r/10 seines Anfangs bzw. Endes bleibt;
  4. seine Scores A⁻(S) und A⁺(Y) höchstens C₀ sind. A⁻(S) misst, zeitlich gewichtet, wie viele andere Linien kurz nach t\_k nahe bei S sind; A⁺(Y) ebenso kurz vor t\_{k+1} nahe bei Y (Gitter-Gegenstück zu OA (15)). *Nachtrag (satz\_3\_9\_dichteschranken.md §12.1):* Die Scores dienen bei OpenAI nur Jensen und werden bei uns nicht gebraucht; an ihre Stelle tritt die Güte der Zellumgebung (G1)–(G3) aus Anhang P.
- **Brauchbar** ist eine Zelle, wenn n\_Q ∈ [b₋m, b₊m] und mindestens (1 − ε) n\_Q ihrer Stücke wählbar sind. S(C) ist die Menge der unbrauchbaren Zellen.
- **Route aus dem Skelett.** Invariante: Das Loch liegt zur Zeit t\_k in der Zelle γ\_k. In Scheibe k ist c₀ die Endzelle von j₀; sie liegt im Abstand ≤ D + 1 von γ\_k, wenn j₀ die Makro-Bedingung erfüllt, sonst weiter weg. Der Sternpfad führt nach einer festen Regel von c₀ nach γ\_{k+1}, mit Umwegen um unbrauchbare Zellen wie OA §8.2. Weil j\_m in c\_m = γ\_{k+1} gewählt wird und das neue Loch am Ende von j\_m liegt, bleibt die Invariante erhalten. Ist j₀ weit gewandert, wird der Sternpfad länger; das wird wie ein Umweg behandelt (G.5.3). *Nachtrag 2026-11-12:* Mit den Regeln aus Anhang L ist j₀ immer regulär; dieser Fall tritt dann nicht ein, und c₀ liegt im Abstand ≤ D + 1 von γ\_k.

Die Route hängt damit von der Konfiguration nur über (i) die unbrauchbaren Zellen und (ii) die Endzellen der Stücke j₀ ab. Beides sind Endpunkt- bzw. Zelldaten. In jedem Vergleich unten sind sie fest.

### G.5.2 Konvention im Gegen-Zustand und Stabilität

**Zählung in B.** B hat fern von R′ in jeder Scheibe ein Stück mehr als C; dessen Ende liegt in c\_m, also zählt n\_Q(B) dort eins mehr. Die erste und die letzte Zelle (Schwanz- und Kopfzelle, beiden Routen gemeinsam) enthalten Anfang bzw. Ende der zusätzlichen Linie. Diese beiden Stücke werden in B für nicht wählbar erklärt, aber mitgezählt und in allen Scores berücksichtigt (wie die Ausnahme-Slot e in OA §10.4).

**Strengere Menge.** S₀(B) sind die unbrauchbaren Zellen von B mit den Tests von G.5.1. S₁(B) ⊇ S₀(B) entsteht mit der strengeren Schwelle C₀ − Δ\_A und dem strengeren Anteil 1 − ε/2, bei gleichem Zählintervall.

**Lemma G6.1 (Stabilität, OA Lemma 10.2) [B].** Bei festen Daten wie in G5 (L, B\_l = C\_l, B\_{j\\jn} = Ĉ\_{j\\jn}) gilt für jede Ersetzung von B\_{jn}, B\_d auf den Schnitten und jeden ursprünglichen Zeugen (C, Ĉ):

```text
S(C), S(Ĉ)  ⊆  S₁(B)
S(C) = S₀(B)   außerhalb des Abstands R* von P        (C und B unterscheiden sich nur auf den Stücken von I)
S(Ĉ) = S₀(B)   außerhalb des Abstands R* von P′       (Ĉ und B unterscheiden sich nur auf l, d, jn)
```

In den fernen Zellen stimmen auch alle einzelnen Wählbarkeiten und wählbaren Anzahlen überein.

*Beweisskizze* (wie OA).

- Alle geänderten Stücke erfüllen cut, liegen also innerhalb R s ihrer Enden, und ihre Enden liegen auf zwei Sternpfaden.
- Der Score eines ungeänderten Stücks ändert sich höchstens um Δ\_A, weil nur beschränkt viele geänderte Stücke in Reichweite sein können.
- Die Isolation ungeänderter Anfänge und Enden ändert sich nur bei beschränkt vielen Stücken je Zelle.
- Die Zahl n\_Q ändert sich höchstens um 1.
- Also ist die wählbare Anzahl im Zeugen mindestens die strengere Anzahl in B minus eine Konstante. Für großes m genügt das: (1 − ε/2) n\_Q − C ≥ (1 − ε) n\_Q.
- Fern von den geänderten Stücken ändert sich gar nichts.

*Neu gegenüber OA:* nur die Zählung +1 längs P, schon oben berücksichtigt.

### G.5.3 Listen der möglichen Routen

Wie OA (Lemma 10.3) zerlegt man S₁(B) in Komponenten (Nachbarschaftsabstand K\_b = 2R* + 10). *Brücken-Komponenten* sind solche, die beiden Skeletten nahe kommen; b\_tot ist ihre Gesamtgröße.

**Lemma G6.2 (Listen, OA Lemma 10.3) [B].** Zu B, γ, γ′ und den festen Endzellen der Stücke j₀ gibt es Listen möglicher Routen P, P′ mit:

- Für jeden Zeugen und jede Ersetzung stehen die tatsächlichen Routen P(Ĉ, γ) und P(C, γ′) auf den Listen.
- Es gibt höchstens 4^{b\_tot} Paare.
- Für jedes gelistete Paar gilt J ≤ J₀ + C(R*)(b\_tot + ℓ\_tot). Dabei zählt J₀ die Begegnungen der Skelette, und ℓ\_tot ist die Gesamtlänge der Sternpfad-Verlängerungen durch weit gewanderte Stücke j₀, soweit sie dem anderen Skelett nahe kommen.

*Beweisskizze.* Wie OA: Nicht-Brücken-Komponenten sind durch G6.1 exakt bestimmt, für Brücken-Komponenten werden alle Teilmengen geraten. Neu ist ℓ\_tot. Die Endzellen der j₀ sind Endpunktdaten und im Vergleich fest; eine Verlängerung erhöht J nur, wenn sie dem anderen Skelett nahe kommt, und wird dann wie ein Umweg gezählt.

### G.5.4 Gemeinsames Auswahlprodukt und integrierter Vergleich

Die Auswahlfaktoren der fernen Vorkommen (Wählbarkeit durch Anzahl, in B ausgewertet) haben nach G6.1 für alle Zeugen und alle Ersetzungen denselben Wert H\* (OA, „common far-choice product“). Für nahe Vorkommen schätzt man den Auswahlfaktor durch seinen größten Wert auf dem zulässigen Bereich ab, [(1 − ε) n\_Q]^{−1}.

**Lemma G6.3 (integrierter Kreuzvergleich, OA Lemma 10.4) [B].** Für feste Sternpfade, Tupel, Skelette und Endpunktdaten gilt

```text
I_{I,I′}  ≤  e^{C|h| + σ_ρ J} · 1_occ · Π_{nahe Vorkommen in Q} [(1 − ε) n_Q]^{−1} · ∫ W(B) 1_G H_F(B)
```

Dabei ist I\_{I,I′} das Integral des Summanden von G2 bei festen Daten, 1\_occ verlangt n\_Q ∈ [b₋m, b₊m] längs beider Routen, und σ\_ρ ist die Kostenrate naher verschiedener Brücken aus G4 und G5. In 2D gilt nur σ\_ρ ~ κ₂ P\_δ ~ 1/ln(1/ρ).

### G.5.5 Was daraus folgt

1. **Ein zusätzliches Dichte-Lemma ist nötig: „defekte Zellen sind selten“** (Gegenstück zu OA Satz 7.2). Für jede Menge U von Zellen soll P(alle Zellen von U defekt) ≤ q^{|U|} mit q → 0 für ρ → 0 gelten. Zutaten:
   - Zählschwänze: Satz 7.1 (a) und (b) des Tutorials.
   - Isolation: Satz 7.1 (c).
   - Scores: obere Schwänze und Lemma 6.8.
   - **Neu: Trajektorien.** Viele Stücke mit Verschiebung > D s sind selten. Im Grundzustands-Pfadmaß (Doob-Prozess) ist das nicht geschenkt, weil die Raten ψ(η′)/ψ(η) eine Drift enthalten. Möglicher Weg: Kippung mit der Sprungzahl in U, die nach Lemma 6.8 auf E₀(H − 4(e^θ − 1) n\_U) zurückgeht, dazu eine Abschätzung der Verschiebung durch die Sprungzahl. Das muss noch ausgearbeitet werden.
2. **Kosten je naher Begegnung.** Zum Faktor 1 + (e^C − 1)/n\_Q für geteilte Teilchen und e^{σ\_ρ} für nahe Brücken kommt (1 − ε)^{−1}, also κ₀ = 2ε + σ\_ρ wie OA §10.5. Die Bedingung des Beweises wird

```text
2ε  +  κ₂ P_δ  +  (e^C − 1)/(b₋ m)   <   α_max / 2
```

   ε muss also deutlich kleiner als α\_max/4 ≈ 0,02 sein. Das legt D (Makro-Bedingung) und ζ (Isolation) fest, beides feste Konstanten, unabhängig von ρ.
3. **Das Tutorial ist anzupassen:** §5.2 (Definition von wählbar, j₀ ohne Wählbarkeitsforderung), §8.1 (dritte Kostenart (1 − ε)^{−1}), §9.2 (Bedingung oben), §10 (zusätzliches Lemma zu defekten Zellen).

## G.6 Untergrenzen der beiden Nenner (Schritt G4) [B, nach OA §10.2]

### G.6.1 Aussage

Für G = j oder l und einen Zustand X sei Z[G, X] die Zustandssumme der Stücke von G mit Wahrscheinlichkeitsbrücken (freie Brücken, auf Masse 1 normiert, mit cut), wobei nur die Stöße innerhalb von G und mit L zählen; L ist fest. Die freien Brückenkerne sind herausgezogen wie in OA (28); sie kürzen sich auf j und l exakt und kosten auf d höchstens e^{C|h|}.

**Lemma G4 (OA (29)) [B].**

```text
Z^br_{I′}(O)  ≥  Z[l, O] · exp(−C(K) |h| − σ_ρ J)
Z^br_I(O)     ≥  Z[j, C] · exp(−C(K) |h| − σ_ρ J)
```

mit C(K) ≈ C₁ (K + 1) und σ\_ρ = C(R) e^{C₁(K+1)} P\_treff(r, s). Dabei ist P\_treff(r, s) die Wahrscheinlichkeit, dass sich zwei Stücke mit r-getrennten Endpunkten in einer Scheibe treffen; in 2D ist sie ≲ C ln(s/r)/ln(s/a) → 0 (G.6.3).

### G.6.2 Der Ersatz für Jensen beim harten Kern

OA schätzt die fehlenden Wechselwirkungen mit Jensen ab: E e^{−V} ≥ e^{−E V}. Beim harten Kern ist der Wechselwirkungsfaktor eine Indikatorfunktion „kein Stoß“, und Jensen ist nicht anwendbar (log 0). Zwei Ersatzwerkzeuge:

**(W1) Einpfad-Randdichte [S].** In einer normierten Gruppe von Stücken (Brücken mit cut, Stoßfreiheit untereinander und mit festen Stücken) hat jedes einzelne Stück, bedingt auf alle anderen, die Dichte

```text
1{weicht aus} / P_frei(weicht aus | andere)   ≤   1 / p*      bezüglich der freien Brücke mit cut
```

Das ist nur die Definition der bedingten Wahrscheinlichkeit; gemittelt über die anderen bleibt die Schranke. C₄ = 1/p\* ersetzt die Konstante C₄ aus OA §10.2.

**(W2) Ausweich-Untergrenze, Lemma P\* [B].** Eine freie Brücke mit cut, deren Endpunkte r-isoliert sind und deren Scores ≤ C₀ sind, weicht einer festen Umgebung mit höchstens C m Stücken in Reichweite mit Wahrscheinlichkeit

```text
P_frei(weicht aus)  ≥  p*  =  e^{−C₁ (K + 1)}
```

aus.

*Beweisweg (Zeitzerlegung):*

- **Teilintervalle der Länge τ ≈ ln(1/ρ)/(4πρ).** In dieser Zeit überstreicht die Relativbewegung zu den anderen Linien eine Fläche von etwa 2πτ/ln τ (2D-Wiener-Würstchen). Bei lokaler Dichte ≤ Cρ (Score) trifft sie also im Mittel höchstens 1/2 andere Linien. Es gibt n = δ/τ ≈ 4πK Teilintervalle.
- **Gute Lage** heißt: Abstand > r zu allen anderen Linien. Aus guter Lage trifft der Wanderer im Teilintervall mit Wahrscheinlichkeit ≤ 1/2 + o(1) eine Linie: die nächste nur mit ≈ ln(√τ/r)/ln(√τ/a) → 0, die übrigen nach der Vereinigungsschranke. Er endet mit Wahrscheinlichkeit ≥ 1 − Cζ² wieder in guter Lage, weil die Nähe anderer Linien nur einen Flächenanteil ~ ζ² ausmacht.
- **Markov-Eigenschaft:** P(weicht aus) ≥ (1/2 − Cζ² − o(1))^n ≥ e^{−C₁(K+1)}, mal einer Konstanten für cut und für den Brücken-Endpunkt.
- *Warnung:* Kürzere Teilintervalle (τ ~ r²) sind falsch gewählt. Dann ist n ≈ K ln(1/ρ), und die Schranke wird nur ρ^{cK}, zu schwach für σ\_ρ → 0.
- *Numerik:* §21 des Arbeitsdokuments misst P(ausweichen) ≈ exp(−2πm/ln 2δ) ≈ e^{−2πK}, passend zu dieser Form.

### G.6.3 Treffen zweier Stücke in 2D

Zwei Stücke derselben Scheibe, deren Anfänge und Enden jeweils den Abstand > r haben und die in den Randintervallen innerhalb r/10 ihrer Endpunkte bleiben (Wählbarkeit), können sich nur im Inneren der Scheibe treffen. Ihre Relativbewegung ist eine 2D-Irrfahrt, die aus dem Abstand ≥ r startet. Nach dem Potentialkern (Tutorial Übung 8.1) trifft sie den Ursprung vor Verlassen des Radius √δ ≈ s mit Wahrscheinlichkeit

```text
P_treff(r, s)  ≲  C · ln(s/r) / ln(s/a)
r = ζ ρ^{−1/2},   s² = K ln(1/ρ)/ρ    ⇒    P_treff  ≈  C · ln(K ln(1/ρ)/ζ²) / ln(1/ρ)  →  0
```

Das ist der kleine Parameter des 2D-Beweises. Er fällt nur wie ln ln(1/ρ)/ln(1/ρ), nicht wie eine Potenz.

### G.6.4 Beweisskizze von Lemma G4

Wie OA, mit (W1) und (W2) statt Jensen.

*Erste Ungleichung.*

1. Ziehe l aus seinem normierten Gruppengesetz (Stoßfreiheit in l und mit L), h unabhängig als freie Brücken mit cut.
2. Der Quotient zu Z[l, O] ist das Produkt der freien cut-Wahrscheinlichkeiten auf h mal der Wahrscheinlichkeit, dass keine der fehlenden Stoßarten eintritt: l gegen das feste j, l gegen das feste d \ h, h gegen alles.
3. **l gegen j:** Nach (W1) und G.6.3 ist die erwartete Zahl der Treffen ≤ C(R) J · P\_treff/p\* = σ\_ρ J. Die Zahl der nahen Paare ist ≤ C(R) J, weil Endzellen höchstens 2R + 5 entfernt sein können und je Route nur ein Stück pro Zelle gewählt wird. Man fasst nahe Paare zu räumlich getrennten Gruppen mit je beschränkt vielen Paaren zusammen; je Gruppe gibt die Vereinigungsschranke P(kein Treffen) ≥ 1 − σ\_ρ · (Gruppengröße) ≥ e^{−2σ\_ρ · (Gruppengröße)}, und die Gruppen sind bei fester Umgebung unabhängig.
4. **l gegen d \ h und h gegen alles:** (W2) für jedes der höchstens |d| ≤ 2|h| betroffenen Stücke gibt e^{−C₁(K+1)·2|h|}.

*Zweite Ungleichung:* ebenso, mit j aus seinem Gruppengesetz (Endpunkte von C, auf j gleich denen von O) und d als freie Brücken; die festen Stücke sind dann l. ∎

### G.6.5 Was das für den Beweis bedeutet

- **Für die Existenz genügt G4 in dieser groben Form.** C(K) ist eine feste Konstante. Sie geht nur in die Kosten geteilter Stücke ein, (e^{C(K)} − 1)/(b₋m) → 0. Auch σ\_ρ → 0 für ρ → 0 bei festem K.
- **Für eine vernünftige Schwelle ist die grobe Form schlecht:** σ\_ρ enthält e^{C₁K} = 1/p\*. Das ist genau die doppelt exponentielle Schwelle aus Tutorial §9.3, jetzt an der Stelle, an der sie entsteht.
- **Zwei Auswege**, beide schon bekannt:
  1. *Scharfes L2* (Tutorial §8.2): Der Umgebungsfaktor ist numerisch κ₂ ≈ e^{0,54K} statt e^{4πK}.
  2. *Kurze, „zugängliche“ Stücke* wie in der OpenAI-Arbeit zum Hartkugelgas bei T > 0 (§6–§7 dort): Man wählt Stücke, deren Ausweichwahrscheinlichkeit ≥ 0,9 ist, und braucht dann weder Jensen noch 1/p\*. In 2D verlangt das 2πK ≲ 0,1, also Zellen mit m = K ln(1/ρ) und K < 0,02. Das ist mit m → ∞ verträglich, aber nicht mit unseren Dichteschranken, die K ≥ 6 … 100 brauchen. Das ist wieder die Skalenspannung (Tutorial §9.3, offener Punkt „Skalen entkoppeln“).

## G.7 Wechselwirkungen im Gegen-Zustand wiederherstellen (Schritt G5) [B, nach OA §10.3]

**Wozu.** Nach G4 lässt man im Integranden von G2 alle Stoßbedingungen fallen, die nicht innerhalb der Gruppen j, l oder mit L wirken. Beim harten Kern ist das eine obere Abschätzung, weil man Indikatorfunktionen ≤ 1 weglässt (OA: „drop interaction costs by positivity“). Übrig bleibt ein Integral, in dem Ĉ\_j die Stücke von l nicht sieht. Der Gegen-Zustand B verlangt aber Stoßfreiheit zwischen allen Stücken. Diese fehlenden Bedingungen muss man zurückholen, und das darf nur an Begegnungen kosten.

**Feste und integrierte Daten** (wie OA §10.3). jn ⊆ j sind die Stücke, deren Endzelle höchstens 2R + 5 von einer Zelle von l entfernt ist; nur sie können wegen cut ein Stück von l treffen.

| Rolle                       | Stücke                                    |
|-----------------------------|-------------------------------------------|
| fest in beiden Integralen   | L, B\_l = C\_l, B\_{j \ jn} = Ĉ\_{j \ jn} |
| integriert im Original      | Ĉ\_jn, C\_j, O\_l, C\_d, Ĉ\_d, O\_h       |
| integriert im Gegen-Zustand | B\_jn, B\_d                               |

**Lemma G5 (OA (29a)) [B].**

```text
∫ 1_cut(jn) 1{jn stoßfrei mit j, L} dπ_jn   ≤   e^{C(K)|h| + σ_ρ J} · ∫ 1_cut(jn) 1_cut(d) 1{alle Paare außer L–L stoßfrei} dπ_jn dπ_d
```

Links fehlen die Bedingungen „jn trifft l nicht“ und alles, was d betrifft; rechts sind sie da.

*Beweisskizze.*

1. Ziehe jn aus seinem normierten Gruppengesetz bei festem j \ jn, und d unabhängig als freie Brücken mit cut.
2. Der Quotient rechts/links ist P\_frei(cut auf d) mal der Wahrscheinlichkeit, dass keine fehlende Stoßart eintritt.
3. **jn gegen l:** l ist fest und hat wählbare Endpunkte. Nach (W1) und G.6.3 kostet jedes der ≤ C(R) J nahen Paare höchstens P\_treff/p\*; zusammen e^{−2σ\_ρ J} wie in G.6.4.
4. **d gegen alles:** Bedingt auf jn ist die Umgebung jedes d-Stücks fest, mit beschränkten Scores; der Reihe nach angewandt gibt Lemma P\* (W2) je Stück p\*. Mit |d| ≤ 2|h| folgt e^{−2C₁(K+1)|h|}.
5. P\_frei(cut) ≥ c > 0 je Stück (OA Lemma 5.1). ∎

Neu gegenüber OA ist nur, dass Jensen durch (W1), (W2) und die Vereinigungsschranke ersetzt wird; Datenrollen und Ablauf sind dieselben.

## G.8 Summieren (Schritt G7) [B, nach OA §10.5]

### G.8.1 Über die Auswahl summieren

Mit G4–G6 ist jeder Summand von G2 bei festen Daten durch das Gewicht des Gegen-Zustands B mal Faktoren an Begegnungen beschränkt (Lemma G6.3). Man summiert zuerst über die Auswahl der Stücke bei festem B, zellweise wie OA §10.5:

| Zelle                        | Auswahl                                  | Schranke                       |
|------------------------------|------------------------------------------|--------------------------------|
| ferne Zelle (nur eine Route) | ein Stück                                | ≤ 1                            |
| nahe gemeinsame Zelle Q      | zwei unabhängige Stücke                  | 1 + (e^{C(K)} − 1)/n\_Q        |
| erste Zelle a (Schwanz)      | ein gemeinsames Stück                    | e^{C(K)}/n\_a                  |
| letzte Zelle b (Kopf)        | das Stück der einen Route ist festgelegt | [1 + (e^{C(K)} − 1)/n\_b]/n\_b |

Dazu kommt je nahem Vorkommen (1 − ε)^{−1} (G.5.4) und e^{σ\_ρ} (G4, G5). Mit n\_Q ≥ b₋m folgt je Paar von Sternpfad-Folgen

```text
≤  C / (n_a n_b) · e^{κ₀ J},        κ₀ = 2ε + σ_ρ + (e^{C(K)} − 1)/(b₋ m)
```

### G.8.2 Über die Routen summieren

Lemma G6.2 beschränkt die Zahl der möglichen Routenpaare und ihre Begegnungen: J ≤ J₀ + C(b\_tot + ℓ\_tot). Also

```text
Σ_{Routenpaare}  ≤  C/(n_a n_b) · e^{κ₀ J₀} · e^{C′ (b_tot + ℓ_tot)}
```

### G.8.3 Normierung (nachgerechnet, 2026-11-10) [B]

**Pro Teilchen normieren** (wie OA, dort ist das Zielmaß µ pro Teilchen normiert): Γ̂ = Γ\_T/N mit Masse g̃⁻(T) = G̃⁻(T)/N und f̂ = dν/dΓ̂ = N f. Cauchy–Schwarz lautet dann |ν|² ≤ g̃⁻ ∫ f̂² dΓ̂.

**Paarweise Dichten.** Für Schwanz x und Kopf y (Gitterplätze) sind die drei Maße von derselben Größenordnung 1/M²:

| Maß              | Gewicht je Paar (x, y), gemittelt | Herkunft                                                                                                                                                                                  |
|------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ν                | ≈ \|ν\|/M²                        | Schwanz: Teilchen gleichverteilt (1/N, besetzt mit Wahrscheinlichkeit ρ); Kopf: Zelle b mit p(b \| a) = 1/#Zellen, dann ein Teilchen der Zelle (1/n\_b, besetzt mit Wahrscheinlichkeit ρ) |
| Γ̂                | ≈ g̃⁻/M²                           | ⟨b\_y⁺(T) b\_x(0)⟩/(NM), für großes T ≈ ρ H̄² e^{−T(E\_{N−1} − E\_N)}/(NM)                                                                                                                 |
| ğ⁺\_{ab} je Paar | ≈ ğ̃⁺/M²                           | ebenso mit b\_y(T) b\_x⁺(0)                                                                                                                                                               |

Also ist f̂ von der Ordnung |ν|/g̃⁻, und der Vergleich in G.8.1 und G.8.2 betrifft nur Quotienten von Größen der Ordnung 1. Ein Faktor M, N oder L bleibt nicht übrig. Damit p(b | a) gleichverteilt sein kann, müssen alle Zellpaare zulässig sein: Die Route braucht w ≥ L/s Scheiben, also T ≳ L s (Tutorial §5.1).

**Endzellen.** Die Auswahlsummen der Tabelle in G.8.1 (erste Zelle e^{C}/n\_a, letzte Zelle [1 + (e^{C} − 1)/n\_b]/n\_b) heben sich gegen die Teilchenzahlen n\_a, n\_b der Schwanz- und Kopfwahl auf, genau wie m/(m²M) = 1/N bei OA.

**Kein 1/ρ-Verlust beim Einsetzen.** Im Übertragungs-Lemma (G.8.4, noch offen) tritt die Norm des Zustands a\*(1\_b)ψ\_N auf, also die Erwartung von a(1\_b) a\*(1\_b) = Σ\_{x,y∈b} b\_x b\_y⁺:

```text
⟨ Σ_{x,y∈b} b_x b_y⁺ ⟩  =  Σ_x (1 − ρ)  +  Σ_{x≠y} ρ₁(x, y)  ≤  s² + s⁴ ρ  ≤  2 s² m          (ρ₁(x,y) ≤ ρ nach Cauchy–Schwarz)
```

Damit wird die Konstante C s² m/(N M) = C/#Zellen², wie bei OA. Die naheliegende Operatorschranke a a\* ≤ |b|² = s⁴ würde dagegen s⁴/(NM) = 1/(ρ #Zellen²) geben, also einen Faktor 1/ρ verlieren. Im Kondensat erreicht die Operatornorm tatsächlich s⁴; man muss deshalb die Erwartung benutzen, nicht die Norm.

**Energiefaktoren.** Die Lebesgue-Gewichte enthalten je Teilchen und Zeiteinheit den Faktor der freien Bewegung. Deshalb sind G̃⁻ = G⁻ e^{−T(E\_{N−1} − E\_N)} und Ğ⁺ = G⁺ e^{−T(E\_{N+1} − E\_N)} einzeln exponentiell klein bzw. groß in T. Das Übertragungs-Lemma (in jeder der Formen von G.8.4) liefert den Faktor e^{−T(E\_{N+1} − E\_N)} mit, denn die Zeit [0, T] läuft im Sektor mit N + 1 Teilchen. Im Produkt bleibt nur e^{−Δ₂T}.

### G.8.4 Seltene Komponenten unter dem Gegen-Lückenmaß

Es bleibt E\_{γ,γ′}[e^{κ₀J₀} ∫ e^{C′(b\_tot + ℓ\_tot)} dĞ⁺\_{ab}]. Dafür braucht man:

1. **Defekte Zellen sind unter dem geschlossenen Maß selten:** P(U ⊆ defekt) ≤ q^{|U|}. Das ist das zusätzliche Dichte-Lemma aus G.5.5.
2. **Übertragung auf das Gegen-Lückenmaß — offen** (nachgeprüft 2026-11-10; die erste Fassung hielt das für eine direkte Übertragung von OA Satz 7.3, das stimmt nicht). Gebraucht wird für Defekt-Ereignisse E

```text
ğ⁺_{ab}(E)  ≤  (C / #Zellen²) · e^{−T(E_{N+1} − E_N)} · P(E)^θ          für ein festes θ > 0
```

   **Warum OAs Beweis nicht trägt.** OA schreibt das geöffnete Maß als Spur und teilt sie mit Hilbert–Schmidt-Cauchy–Schwarz in zwei Faktoren. Jeder Faktor setzt sich wieder zu einer *geschlossenen* Periode im *selben* Teilchenzahl-Sektor zusammen, und dort steht P(E). Bei uns läuft die Gegen-Lücke auf [0, T] im Sektor N + 1, sonst im Sektor N. Teilt man ebenso, sind beide Faktoren wieder Gegen-Lücken-Größen (eine Schleife von a nach a bzw. von b nach b), nicht das geschlossene Maß. Der Teilchenzahlwechsel, der die exakte Fernkürzung erst möglich macht (G3), verhindert hier den Trick.

   **Geprüfte Auswege.**

   - *(a) Kippen mit der Zusatzlinie:* ğ⁺(E) als Erwartung der Zustandssumme Z\_ℓ(ω) der Zusatzlinie im geschlossenen Maß, dann Cauchy–Schwarz. Das braucht E[Z\_ℓ²]/(E Z\_ℓ)², das zweite Moment eines gerichteten Polymers in 2+1 Dimensionen. Zwei Linien in derselben Umgebung sind schwach positiv gekoppelt; in 2D wächst das wie T^{cζ²}, also nicht gleichmäßig in L. Verworfen.
   - *(b) Relaxation:* Im endlichen System ist der durch Einsetzen eines Teilchens erzeugte Zustand nach langer Zeit punktweise ≤ 2 × Grundzustand (Perron). Das gibt ğ⁺(E) ≤ 4 ğ⁺\_{ab} P\_{N+1}(E) für Ereignisse weit weg von den Enden. Die nötigen Puffer sind aber Mischzeiten des ganzen Systems, und gerade an den Enden treffen sich beide Routen. Verworfen.
   - *(c) Hölder mit dem Einfügequotienten, aussichtsreich.* Im Grenzfall β → ∞ ist ğ⁺\_{ab}(E) ∝ ⟨φ\_b, U\_E φ\_a⟩ mit φ\_a = a\*(1\_a)ψ\_N. Schreibt man φ\_a = ψ\_{N+1} u\_a, so ist das e^{−TE\_{N+1}} E\_{N+1}[u\_b(ω\_T) 1\_E u\_a(ω\_0)] im stationären Prozess mit N + 1 Teilchen, und Hölder gibt

```text
ğ⁺_{ab}(E)  ≤  (1/(NM)) e^{−T(E_{N+1} − E_N)} · ‖u_a‖₄ ‖u_b‖₄ · P_{N+1}(E)^{1/2}
‖u_a‖₂ = ‖φ_a‖ = ⟨Σ_{x,y∈a} b_x b_y⁺⟩^{1/2}  ≤  (2 s² m)^{1/2}          (G.8.3)
```

     Es fehlt nur eine *umgekehrte Hölder-Ungleichung* ‖u\_a‖\_{2+η} ≤ C ‖u\_a‖₂ für den Einfügequotienten u\_a = (a\*(1\_a)ψ\_N)/ψ\_{N+1} im Grundzustand, für irgendein η > 0 (dann θ > 0). Das ist eine Ein-Zeit-Aussage über Grundzustände. Physikalisch ist sie plausibel: Im Jastrow-Bild ist ψ\_N(η \ x)/ψ\_{N+1}(η) ≈ 1/Π\_j f(x − x\_j) nur groß, wenn x einen nahen Nachbarn hat, und das ist selten. Streng ist sie offen. Möglicher Weg: φ\_a erfüllt H\_{N+1}φ\_a = E\_N φ\_a + [H, a\*(1\_a)]ψ\_N mit einer Quelle nur auf dem Rand der Zelle a; u\_a löst also eine Poisson-Gleichung des Doob-Generators. Höhere Integrierbarkeit (Gehring, Meyers) für solche Lösungen wäre das Werkzeug.

     **Numerik [N]** ([pruef\_einfuegequotient.py](pruef_einfuegequotient.py), exakte Grundzustände, 2026-11-10). R\_4 = ‖u\_a‖₄/‖u\_a‖₂ für den Grundzustand, verglichen mit der Gleichverteilung ohne Korrelationen (dort ist u\_a ∝ n\_a):

| L, N → N+1 | s   | ρ     | m    | R₄ Grundzustand | R₄ gleichverteilt | Verhältnis | max u/‖u‖₂ (Grundzustand / gleich) |
|------------|-----|-------|------|-----------------|-------------------|------------|------------------------------------|
| 6, 4 → 5   | 3   | 0,139 | 1,25 | 1,347           | 1,245             | 1,08       | 7,8 / 3,2                          |
| 8, 3 → 4   | 4   | 0,062 | 1,00 | 1,395           | 1,285             | 1,09       | 8,2 / 3,1                          |
| 8, 2 → 3   | 4   | 0,047 | 0,75 | 1,431           | 1,321             | 1,08       | 6,0 / 2,9                          |
| 10, 2 → 3  | 5   | 0,030 | 0,75 | 1,434           | 1,324             | 1,08       | 6,9 / 2,8                          |
| 12, 2 → 3  | 6   | 0,021 | 0,75 | 1,435           | 1,325             | 1,08       | 7,6 / 2,8                          |
| 12, 2 → 3  | 2   | 0,021 | 0,08 | 2,178           | 1,946             | 1,12       | 27,4 / 10,2                        |

     - Die umgekehrte Hölder-Ungleichung gilt in allen 15 Fällen mit kleinem Faktor: R₄ liegt nur 8–15 % über dem Wert ohne Korrelationen.
     - Bei fester Teilchenzahl je Zelle m hängt R₄ praktisch nicht von ρ ab (Zeilen mit m = 0,75). Für m = K ln(1/ρ) → ∞ ist daher R₄ → 1 wie bei Poisson-Statistik zu erwarten.
     - Der Schwanz existiert (Maximum 2–3-mal größer als ohne Korrelationen, eingesetztes Teilchen neben einem anderen), trägt aber kaum L⁴-Gewicht.
     - Vorbehalt: nur 3–5 Teilchen insgesamt. Der eigentliche Vielteilchen-Fall (viele Teilchen je Zelle) ist so nicht erreichbar.

     **Beweisansatz: Lemma J (Jastrow-Struktur des Einsetzens) [N + H].** Für eine (N+1)-Konfiguration η und x ∈ η sei G(x; η \ x) = Π\_{j} f(x − x\_j) mit der Paarfunktion f = min(1, a(·)/a\_R) (a der Potentialkern der 2D-Irrfahrt, Abschneideradius R). Vermutung:

```text
c₁ λ  ≤  ψ_N(η \ x) · G(x; η \ x) / ψ_{N+1}(η)  ≤  c₂ λ          für alle η und alle x ∈ η
```

     mit einer Normierungskonstante λ und festen c₂/c₁. *Folge:* u\_a(η) ≤ c₂λ Σ\_{x∈a∩η} 1/G(x; η \ x). Das ist eine *lokale* Funktion: 1/G ist nur groß, wenn x nahe Nachbarn hat. Ihre Momente unter ψ\_{N+1}² sind durch die Zellbesetzung (Satz 3.9 a) und die Statistik naher Paare (Satz 3.9 c) beschränkt. Das ergibt die umgekehrte Hölder-Ungleichung und damit das Übertragungs-Lemma, mit Konstanten, die von R und ρ, aber nicht von L abhängen.

     *Numerik* ([pruef\_unterloesung.py](pruef_unterloesung.py), exakte Grundzustände, alle Paare (η, x)), Quotient relativ zu seinem ψ²-gewichteten Mittel:

| L, N → N+1 | R   | mit Jastrow-Faktor: min – max | ohne (G = 1): min – max |
|------------|-----|-------------------------------|-------------------------|
| 6, 3 → 4   | 3   | 0,70 – 1,24                   | 0,70 – 2,93             |
| 8, 2 → 3   | 3   | 0,83 – 1,13                   | 0,80 – 2,54             |
| 8, 3 → 4   | 3   | 0,69 – 1,20                   | 0,72 – 3,85             |
| 8, 3 → 4   | 4   | 0,67 – 1,25                   | 0,72 – 3,85             |
| 10, 2 → 3  | 4   | 0,82 – 1,12                   | 0,81 – 2,94             |

     Also c₂/c₁ ≈ 1,4–1,9 in allen Fällen. Der Grundzustand hat bezüglich des Einsetzens fast exakt Jastrow-Struktur.

     *Was nicht geht:* Eine Jastrow-Einfügung als exakte Unterlösung, (H\_{N+1} − E\_{N+1})Φ̃ ≤ 0 punktweise, mit dem Vergleichsprinzip (e^{−tH} positivitätserhaltend ⇒ ψ\_{N+1} ≥ Φ̃/⟨ψ\_{N+1}, Φ̃⟩). Das ist numerisch auf 8–50 % des Gewichts verletzt (dieselbe Datei). Die Kreuzterme zwischen der Bewegung der übrigen Teilchen und dem Jastrow-Faktor haben kein Vorzeichen.

     *Möglicher Weg:* In Weltlinien ist ψ\_{N+1}(η)/ψ\_N(η \ x) die Zustandssumme einer zusätzlichen halbunendlichen Linie, die zur Zeit 0 bei x endet, gemittelt über die Vergangenheit der N übrigen Linien bei gegebener Gegenwart η \ x. Man zerlegt die Zeit in [−τ, 0] und (−∞, −τ]. Kurz vor 0 muss die Linie den nahen Nachbarn von x ausweichen; das gibt den Faktor G(x; η \ x), die 2D-Streufunktion. Der lange Teil soll von der Gegenwart nur um einen beschränkten Faktor abhängen. Dafür bräuchte man eine parabolische Harnack-Ungleichung für den Doob-Prozess auf Zeitskala τ; das ist der eigentlich offene Schritt.

     **Umformulierung: Überleben unter beweglichen Fallen [S für die Darstellung, H für die Folgerung].** Schreibt man ψ\_{N+1}(ζ ∪ y) = ψ\_N(ζ) Θ(ζ, y) für eine N-Konfiguration ζ und einen freien Platz y, dann ist Θ nach der Weltlinien-Darstellung (Linie durch y markieren, über die übrigen N Linien mitteln) die *renormierte Überlebenswahrscheinlichkeit* einer Irrfahrt unter beweglichen Fallen:

```text
Θ(ζ, y)  ∝  lim_{t→∞} e^{t (ε_{N+1} − ε_N)} · P_{ζ,y}( Wanderer trifft bis zur Zeit t keine der N Linien )
```

     Der Wanderer ist die freie Irrfahrt (Rate 1 je Nachbar) ab y. Die Fallen sind die N übrigen Teilchen unter ihrer Doob-Dynamik, gestartet in ζ; wegen Reversibilität ist die Zeitrichtung gleich. „Treffen“ heißt gleicher Platz zur gleichen Zeit. Die Abklingrate ε\_{N+1} − ε\_N ist die Einfügeenergie, also das chemische Potential (Lemma 3.5). Lemma J sagt dann: Das quasi-stationäre Überlebensprofil ist bis auf einen festen Faktor die 2D-Streufunktion G(y; ζ) der nahen Fallen. Das ist eine Aussage vom Typ „Irrfahrt unter beweglichen Fallen“ (Drewitz, Gärtner, Ramírez, Sun 2012; Athreya, Drewitz, Sun), dort allerdings für unabhängige Fallen und für das Abklingen, nicht für das Profil.

     *Beweisplan in zwei Zeitskalen [H]:*

     1. *Kurze Zeit τ ~ R²:* Der Wanderer muss den nahen Fallen entkommen. Weil die Fallen im verdünnten Gas in dieser Zeit kaum weiterlaufen, ist die Wahrscheinlichkeit ≍ G(y; ζ) (2D-Streuung, Potentialkern).
     2. *Lange Zeit:* Das restliche Überleben darf vom Start nur um einen festen Faktor abhängen. Dafür koppelt man zwei Starts, die sich nur nahe y unterscheiden. Die Wanderer treffen sich in 2D mit positiver Wahrscheinlichkeit, bevor sie weit laufen. Die Unterschiede der Fallen-Konfigurationen müssen unter der Doob-Dynamik „ausheilen“, das heißt lokal bleiben und verschwinden. Dieses Ausheilen lokaler Störungen im Vielteilchen-Doob-Prozess ist der offene Kern; im verdünnten Bereich wechselwirken die Fallen selten, was hilft.

     *Numerik zur Zeitskala* ([pruef\_harnack.py](pruef_harnack.py)): Entwickelt man das reine Einsetzen bzw. die Jastrow-Einfügung mit e^{−τ(H − E)}, ist das Verhältnis zu ψ\_{N+1} nach τ ≈ 2–4 bzw. τ ≈ 1–2 konstant (Schwankung 1,00), für L = 6 … 12. Das ist aber ein Endlichkeitseffekt: Die gleichmäßige Einfügung hat Impuls null, und kleine Systeme haben dort große Energielücken. Über Lokalität sagt dieser Test nichts aus. Aussagekräftig ist nur: Die Breite c₂/c₁ in Lemma J wächst nicht mit L, sie wird bei kleinerer Dichte sogar enger (1,8 bei ρ = 0,11; 1,4 bei ρ = 0,03).

     **Literatur zu Lemma J (Suche 2026-11-10) [Lit].**

     - *Irrfahrt unter beweglichen Fallen:* Drewitz, Gärtner, Ramírez, Sun, „Survival probability of a random walk among a Poisson system of moving traps“ (2012, arXiv 1010.3958): Das gequenchte Überleben fällt immer exponentiell, das gemittelte in d = 1, 2 subexponentiell; Werkzeug „Pascal-Prinzip“. Übersicht: Athreya, Drewitz, Sun (arXiv 1703.06617). Fallen, die selbst eine symmetrische Exklusion ausführen: Redig, J. Stat. Phys. 1994 (exponentielle obere Schranke). Untersucht werden dort Abklingraten, nicht das Profil Θ.
     - *Profil eines Hauptzustands per Kopplung:* Berger, Bouchot (arXiv 2408.15858) beweisen Regularität und Harnack-Ungleichungen für die erste Dirichlet-Eigenfunktion einer getöteten Irrfahrt über Feynman–Kac, Spiegelkopplung und Ruin-Abschätzungen. Das ist methodisch genau Schritt 2 unseres Plans, allerdings für ein festes Gebiet, nicht für bewegliche Fallen.
     - *Parabolische Harnack-Ungleichung in dynamischer Umgebung:* bewiesen für gleichmäßig elliptische bzw. balancierte zeitabhängige Leitfähigkeiten (Deuschel, Guo, arXiv 1710.05508; Dembo, Huang, Zheng, arXiv 1705.07534). Im entarteten Fall weicht man auf De-Giorgi-Iteration aus (Andres, Chiarini, Slowik, PTRF 2021). Getötete Wanderer unter harten beweglichen Hindernissen sind nicht abgedeckt.
     - *Vergleich mit unabhängigen Teilchen:* Liggetts Vergleichsungleichung (Interacting Particle Systems, Kap. VIII, Satz 1.7; Verallgemeinerung über Borcea–Brändén–Liggett) dominiert Erwartungen positiv definiter Funktionen unter der symmetrischen Exklusion durch unabhängige Irrfahrten. Unser Doob-Prozess ist keine symmetrische Exklusion (Raten ψ(η′)/ψ(η) statt 1), daher nicht direkt anwendbar; für Lemma P\* und Stoßschranken aber ein naheliegender Vergleich, falls sich eine Doob-Version beweisen lässt.
     - *Langsame Durchmischung:* Exklusionsartige Umgebungen sind wegen der Teilchenzahlerhaltung nicht „kegel-mischend“ (Avena, den Hollander, Redig; Avena, dos Santos, Völlering, arXiv 1102.1075). Für uns heißt das: Θ(ζ, y) erinnert sich an großräumige Dichteschwankungen von ζ. In 2D zerfällt deren Einfluss nur wie 1/t, integriert also logarithmisch.

     **Folgerung für die Formulierung.** Punktweise für *alle* ζ ist Lemma J wohl zu stark: Untypische Umgebungen mit großräumigem Dichteüberschuss verschieben Θ um einen Faktor, der mit dem Logarithmus der Systemgröße wachsen kann. Gebraucht wird aber nur die umgekehrte Hölder-Ungleichung, also Lemma J *in L^p* bzw. außerhalb seltener Ausnahmemengen. Der Einfluss großräumiger Dichteschwankungen ist dann exponentiell klein in ihrer Größe, und ihre Wahrscheinlichkeit steuern die Dichteschranken. Die richtige Zielaussage ist daher: log Θ(ζ, y) − log G(y; ζ) hat beschränkte exponentielle Momente unter ψ\_{N+1}², gleichmäßig in L.

     **Versuch an der Momentenform (2026-11-10 abends).**

     *Exakte Identitäten [S].* Θ ist die h-Funktion des getöteten Paares (Umgebung, Wanderer) zur Abklingrate μ = ε\_{N+1} − ε\_N:

```text
Θ(ζ, x)  =  e^{μt} E_{ζ,x}[ Θ(ζ_t, X_t) ; überlebt bis t ]                         für alle t ≥ 0
1/Θ(ζ, x)  =  E^Q_{ζ,x}[ 1/Θ(ζ_t, X_t) ] / ( e^{μt} P_{ζ,x}(überlebt bis t) )
```

     Dabei ist Q der auf ewiges Überleben bedingte Prozess; er ist genau der Doob-Prozess mit N + 1 Teilchen. Kleine Θ, also große Einfügequotienten, entstehen daher aus zwei Gründen. Entweder ist das kurzzeitige Überleben unwahrscheinlich (nahe Nachbarn); dafür hat man Lemma P\* und die 2D-Streuung. Oder der Q-Prozess landet aus dem Start (ζ, x) bevorzugt in Zuständen mit kleinem Θ; das ist eine Aussage über das Durchmischen des Doob-Prozesses mit N + 1 Teilchen.

     *Numerik [N]* ([pruef\_theta\_umgebung.py](pruef_theta_umgebung.py), Gewicht ψ\_N², x ein freier Platz): log(Θ/G) streut nur um 0,03–0,07 bei Ausreißern bis ±0,19. E[(Θ/G)^{−2}]·e^{2·Mittel} = 1,002–1,009. Eine Abhängigkeit von der Zahl der Teilchen jenseits der Jastrow-Reichweite ist nicht messbar (±0,005 bei 12×12, N = 2). Die Momentenform von Lemma J ist in diesen Systemen also sehr gut erfüllt, sogar besser als die punktweise Form.

     *Warum die Beweisversuche kreisen.* Jensen und Hölder in der h-Identität verschieben das Problem nur zu höheren Momenten oder zu E^Q[1/Θ\_t]. Eine Vor-Relaxation der Einfügung (die Zusatzlinie schon vor der Lücke starten) braucht wieder eine untere Schranke für ψ\_{N+1}. Bedingte Defekt-Schranken bei gegebenem Rand eines Raum-Zeit-Gebiets scheitern an der Teilchenzahlerhaltung: Der Rand legt die Zahl der Linien innen fest. Alle Wege brauchen dieselbe Zutat, eine **Durchmischungs- bzw. Entkopplungsabschätzung für den Grundzustands-Doob-Prozess** (gleichmäßig in L, zumindest im Mittel). Das ist der offene Kern des Übertragungs-Lemmas. In 2D ist er besonders heikel, weil die Dynamik die Teilchenzahl erhält und langsam (diffusiv) durchmischt.

     **Umbau-Versuch: das Mitteln unter dem Gegen-Lückenmaß vermeiden (2026-11-10 abends).**

     OA braucht das Mitteln unter dem geöffneten Maß aus zwei Gründen (OA §10.4–10.5):

     - **(i) Listen:** Die Rückwärts-Route hängt von den schlechten Zellen von Ĉ ab, die man aus B nicht kennt. Man rät Teilmengen der Brücken-Komponenten; das kostet 4^{b\_tot}.
     - **(ii) Umwege:** Umwege um Brücken-Komponenten erhöhen die Begegnungszahl, J ≤ J₀ + C b\_tot.

     *Zufällige Schwellen beseitigen (i) [B].* Die Tests „schlecht“ (Zahl, Anteil, Score) benutzen eine Schwelle, die gleichverteilt in einem Fenster gezogen wird, und zwar dieselbe für alle Zustände C, O, Ĉ, B. Fern von Begegnungen sind die Statistiken gleich, also auch die Urteile (exakt, wie G6.1). Nahe Begegnungen unterscheiden sich die Statistiken nur um ±1 Teilchen bzw. wenige Kennzeichen. Das Urteil kippt dann nur, wenn die Schwelle in diesen schmalen Bereich fällt, mit Wahrscheinlichkeit ≤ C/m je Zelle *über unsere eigene Zufälligkeit*, gleichmäßig in der Konfiguration. Die Rückwärts-Route ist damit bis auf einen Faktor e^{CJ/m} durch B bestimmt, ohne Raten und ohne Mitteln über die Umgebung. Das lohnt sich unabhängig vom Rest.

     *(ii) bleibt.* Umwege um Komponenten, die beiden Skeletten nahe kommen, kosten e^{κ₀ C b\_tot}, jetzt aber mit kleinem Koeffizienten κ₀C statt ln 4. Gebraucht wird also nur noch ein *schwacher* Schwanz: P\_B(Brücken-Komponente der Größe k) ≤ C e^{−ck} mit irgendeinem c > κ₀C. Das ist immer noch eine Aussage unter dem Gegen-Lückenmaß.

     *Was nicht geht:*

     - Das Ausgabemaß um die Route erweitern (Route mitnotieren): Dann fällt die Rückwärts-Route mit der Vorwärts-Route zusammen, und die Routen begegnen sich überall.
     - Ein geglätteter Bezugskern für die schlechten Mengen: Dann kostet *jede* Zelle der Route einen Faktor 1 + C/m. Das sind e^{CL/m}, nicht gleichmäßig in L.
     - Große Komponenten verwerfen (Größe > K): Die Annahmewahrscheinlichkeit fällt wie 1 − L(Cq)^K, also braucht man K ~ log L, und dann wachsen die Kosten je Begegnung mit L.

     Die exakte Fernkürzung erzwingt den Vergleich mit B (G3), und jede Abhängigkeit der Route von schlechten Zellen nahe Begegnungen führt dann auf ein Mittel unter B.

     **Polymer-Sicht auf den Rest [H].** Für den schwachen Schwanz genügt nach Hölder, dass die normierte Zustandssumme W/E W der Zusatzlinie (Weg von a nach b über die Zeit T in der Umgebung ω) für ein p > 1 in L^p beschränkt ist (schwache Unordnung):

```text
P_B(U schlecht)  ≤  ‖W/EW‖_p · P(U schlecht)^{1 − 1/p}  ≤  C q^{(1−1/p)|U|}
```

     Für gerichtete Polymere in 2+1 Dimensionen mit *unabhängiger* Unordnung gilt das nicht gleichmäßig in T (starke Unordnung für jedes β > 0, Lacoin 2010). Der Übergang tritt aber erst bei log T ~ 1/β² ein. Unsere Umgebung ist zudem keine unabhängige Unordnung, sondern ein Suprafluid: Langwellige Dichteschwankungen sind unterdrückt (S(k) ~ |k|). Ob das Var(log W) beschränkt hält, ist offen und **im Wurm messbar**: Testlinien in gespeicherte Weltlinien-Konfigurationen legen, W per dynamischer Programmierung in Raum-Zeit berechnen und E[W²]/(E W)² als Funktion von T verfolgen.

     *Einwand gegen die Polymer-Sicht [H, 2026-11-10].* E[W²] ist die Zustandssumme *zweier* unabhängiger Zusatzlinien in derselben Umgebung. Physikalisch sind das zwei Fremdteilchen in einem Bose-Gas (Bose-Polaronen). Ihre durch die Umgebung vermittelte Wechselwirkung ist anziehend, und in 2D bindet jede Anziehung (Bipolaron), wenn auch mit exponentiell kleiner Bindungsenergie b. Dann wächst E[W²]/(E W)² wie e^{bT}, mit T ~ Ls also nicht gleichmäßig in L. Das ist das 2+1-Gegenstück zur starken Unordnung. Die Polymer-Sicht trägt daher vermutlich nur, wenn man sie *lokalisiert*: Nur das Stück der Zusatzlinie nahe der Zellmenge U darf zählen. Diese Lokalisierung braucht aber wieder eine Entkopplung zwischen fernem Linienverlauf und lokaler Umgebung, also den offenen Kern von oben. Die Messung von E[W²]/(E W)² im Wurm würde das Bipolaron-Bild testen, aber keinen Beweis retten; sie ist zurückgestellt.
3. **Komponenten aufsummieren** wie OA: Entwicklung nach Brücken-Komponenten, Anwendung von 2. auf ihre Vereinigungen, geometrische Reihe. Ergebnis ∫ e^{C′b\_tot} dĞ⁺\_{ab} ≤ C(a, b) exp(ϑ(q) S\_{K\_b}) mit ϑ(q) → 0; S\_{K\_b} ist die Summe weicher Abstände der beiden Skelette. ℓ\_tot wird ebenso behandelt, mit den Trajektorien-Schranken aus dem Dichte-Lemma.
4. **Skelettmomente:** Cauchy–Schwarz trennt E e^{2κ₀J₀} (Budget: 2κ₀ ≤ α\_max) und E e^{2ϑ(q)S\_{K\_b}} (beschränkt nach OA (24)–(25) bzw. Lemma 8.1 dort).

### G.8.5 Ergebnis

```text
∫ f̂² dΓ̂  ≤  C_end · e^{−T(E_{N+1} − E_N)} · sup_{a,b} ( E e^{2κ₀ J₀} )^{1/2} ( E e^{2ϑ(q) S} )^{1/2}
```

Dabei hängt C\_end nicht von L, N oder ρ ab (G.8.3). Mit |ν|² ≤ g̃⁻ ∫ f̂² dΓ̂ und g̃⁻ = g⁻ e^{−T(E\_{N−1} − E\_N)} folgt Satz G in der Form

```text
g⁻(T)  =  G(T)/N  ≥  e^{Δ₂T} · |ν|² / (C_end · C_Skelett),        κ₀ = 2ε + σ_ρ + (e^{C(K)} − 1)/(b₋ m)  ≤  α_max / 2
```

Die Gegen-Lückenmasse G⁺ tritt dabei gar nicht mehr als Faktor auf; das Übertragungs-Lemma beschränkt sie mit. Mit Δ₂ ≥ 0 und N₀/N ≥ g⁻(T) (Lemma 3.2 des Tutorials) folgt N₀/N ≥ |ν|²/(C\_end C\_Skelett).

## G.9 Stand und was danach noch offen ist

Mit G.5–G.8 ist Satz G vollständig als Beweisskizze ausgeschrieben, Schritt für Schritt nach OA §10. Für die Existenz fehlen noch diese Teilaussagen:

| Teilaussage                                        | wo gebraucht | Stand                                                                                                                       | Weg                                                                                                                                                                                                                               |
|----------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lemma P\*: p\* ≥ e^{−C₁(K+1)}                      | G4, G5       | [B]                                                                                                                         | Zeitzerlegung (G.6.2)                                                                                                                                                                                                             |
| Defekte Zellen selten, einschließlich Trajektorien | G6, G7       | [B]; Teilstück Lemma T1 [S]                                                                                                 | [satz\_3\_9\_dichteschranken.md](satz_3_9_dichteschranken.md) §8: Lemma T1 (Eichtransformation), Satz T2 (gefärbter Operator, OA §6)                                                                                              |
| Übertragung auf das Gegen-Lückenmaß                | G7           | **offen**, neue Schwierigkeit                                                                                               | OAs Satz 7.3 trägt nicht (Teilchenzahlwechsel). Weg: Hölder mit dem Einfügequotienten; dieser folgt aus Lemma J (Jastrow-Struktur des Einsetzens, numerisch c₂/c₁ ≤ 1,9); offen ist eine parabolische Harnack-Ungleichung (G.8.4) |
| Normierung C\_end                                  | G7           | [B], nachgerechnet (G.8.3): unabhängig von L, N, ρ, sofern im Übertragungs-Lemma ρ₁ ≤ ρ statt der Operatornorm benutzt wird | Paarweise Dichten ν, Γ̂, ğ⁺ alle ~ 1/M²                                                                                                                                                                                            |
| Δ₂ ≥ 0 bzw. \|Δ₂\| T = O(1)                        | Satz G       | [N]                                                                                                                         | Tutorial §5.4                                                                                                                                                                                                                     |
| Skelette zwischen festen Endpunkten                | G7           | [Lit] + [B]                                                                                                                 | OA §8.1, Hartkugel-Arbeit bei T > 0 §8                                                                                                                                                                                            |

**Bedingung des Beweises:** κ₀ = 2ε + σ\_ρ + (e^{C(K)} − 1)/(b₋m) ≤ α\_max/2. Darin sind ε und K feste Konstanten, und σ\_ρ ≈ e^{C₁K} ln ln(1/ρ)/ln(1/ρ) sowie 1/(b₋m) gehen für ρ → 0 gegen 0.

## G.10 Umbau: Zeitschleife statt Lücke (2026-11-10 abends) [B]

**Befund in einem Satz.** Lässt man die Route nicht von der Zeit 0 zur Zeit T laufen, sondern *hinauf und wieder zurück zur Zeit 0*, dann ist der Gegen-Zustand B kein Gegen-Lückenmaß mehr. Er ist eine offene Konfiguration zu gleicher Zeit, im selben Teilchenzahl-Sektor. Damit gilt OpenAIs Übertragungs-Lemma (OA Satz 7.3) unverändert, und der offene Kern aus G.8.4 entfällt.

### G.10.1 Konstruktion

- **Ziel:** das Maß µ der offenen Konfigurationen zu gleicher Zeit. Der Schwanz liegt bei (x, 0), x ein gleichverteiltes Teilchen; der Kopf liegt bei (y, 0), y gleichverteilt. Seine Masse ist q₀ = N₀/N, genau wie bei OA. Lemma 2.1 (Einpunkt) und Lemma 3.2 (Monotonie von G) werden nicht mehr gebraucht.
- **Route = Zeitschleife.** Die Aufwärts-Hälfte U läuft von der Zelle von x zur Zeit 0 bis zu einer Wendezelle c zur Zeit T. Die Abwärts-Hälfte D läuft von c zur Zeit T bis zur Zelle von y zur Zeit 0. Beide Hälften sind zeitlich orientierte Pfade mit zwei räumlichen Querrichtungen (BPP-Skelette wie bisher).
- **Aufwärts:** der Staffellauf aus G.1. Das Loch wandert nach oben, die Lücke wächst, je Scheibe wird ein Stück gelöscht und Brücken werden neu gezogen.
- **Abwärts:** das Spiegelbild davon (genaue Festlegung in G.11.1). Je Scheibe wird ein neues Stück mit freiem Anfang *eingefügt*, dazu wird zyklisch umgestiegen; der Kopf steht danach eine Scheibe tiefer. Die Stücke stammen wieder aus exakt bedingten Gesetzen. *Achtung:* Ein Abweg, der den Kopf in seiner Zelle festhält (so in G.10.5 geprüft), ist falsch; ∫ f² wächst dann exponentiell in w (G.11.1).
- **Ergebnis O:** Unten endet die Linie bei (x, 0), oben beginnt eine bei (y, 0). Zu jeder Zeit t ∈ (0, T) fehlt längs U ein Linienstück, und längs D ist eines hinzugekommen. Die Linienzahl bleibt also überall N, und O ist eine offene Konfiguration zu gleicher Zeit.

### G.10.2 Linienzahlen im zweiten Moment

R′ baut O aus C, R wertet die Dichte aus. Zur Zeit t ∈ (0, T) gilt, gezählt relativ zu C:

| Zustand | nahe U′ (nur R′) | nahe D′ (nur R′) | nahe U (nur R) | nahe D (nur R) | Summe |
|---------|------------------|------------------|----------------|----------------|-------|
| C       | 0                | 0                | 0              | 0              | N     |
| O       | −1               | +1               | 0              | 0              | N     |
| Ĉ       | −1               | +1               | +1             | −1             | N     |
| B       | 0                | 0                | +1             | −1             | N     |

- **Wie bisher (G3):** Auf den Stücken nur von R′ ist Ĉ = O und B = C, auf denen nur von R ist B = Ĉ und O = C. Fern von Begegnungen stehen sich bedingte Zustandssummen mit gleicher Linienzahl und gleichem Rand gegenüber und kürzen sich exakt.
- **Neu:** B = C plus ein Stück längs U minus ein Stück längs D. Zu *jeder* Zeit hat B genau N Linien. Die beiden offenen Enden liegen bei der Zeit 0: Der Kopf liegt an einem frischen Punkt der Zelle von x, der Schwanz in der Zelle von y. B ist also die „umgekehrte Einfügung“ von OA (Kopf und Schwanz vertauscht), eine offene Konfiguration zu gleicher Zeit im Sektor N.
- **Folge:** Das Übertragungs-Lemma für B ist OA Satz 7.3: Beide Hilbert–Schmidt-Faktoren setzen sich zu einer geschlossenen Periode im selben Sektor zusammen. Beim harten Kern braucht man nur a\*(1\_a) a(1\_a) ≤ s² n\_a (Cauchy–Schwarz für Σ\_{x∈a} b\_x). Die Lemmata J, die umgekehrte Hölder-Ungleichung und die Durchmischung des Doob-Prozesses werden nicht gebraucht.
- **Nebenbei:** Es gibt keinen Faktor e^{−Δ₂T} mehr, also auch keine Bedingung an Δ₂.

### G.10.3 Begegnungen und Budget

Zwei unabhängige Schleifen begegnen sich auf vier Arten: U–U′, D–D′, U–D′ und D–U′. Jedes Paar besteht aus zwei unabhängigen, zeitlich orientierten Pfaden mit zwei räumlichen Querrichtungen. BPP liefert beschränkte exponentielle Begegnungsmomente für jedes Paar, also auch für die Summe (Hölder).

Die räumliche Verschiebung von x nach y verteilt sich auf 2T/δ Scheiben. *Korrektur (G.11.3):* Steile Hälften (T ≫ L s, Budget ≈ 0,05–0,07) brauchen eine Torus-Fassung von OAs Lemma 8.1. Für den Existenzsatz nimmt man OAs Bereich T ≈ L s/16 mit Drift ≤ 1 Zelle je Scheibe; das Budget ist dann kleiner, aber positiv.

**Gegenproben.**

- *1D:* Ein zeitlich orientierter Pfad hat nur eine räumliche Querrichtung, also gibt es keine beschränkten Begegnungen und keinen Schluss.
- *2D bei T > 0:* Die Zeit ist ein Kreis der Länge β, die Schleife hat höchstens die Höhe β/2, und die Begegnungen bleiben nicht gleichmäßig beschränkt.

Beides stimmt mit der Physik überein.

### G.10.4 Was sich am Beweis ändert

| Teil               | Zeitartige Lücke (G.0–G.9)                | Zeitschleife (G.10)                                                                  |
|--------------------|-------------------------------------------|--------------------------------------------------------------------------------------|
| Zielgröße          | G(T) mit Monotonie und Einpunkt-Kriterium | q₀ = N₀/N direkt (OA µ)                                                              |
| Gegen-Zustand B    | Gegen-Lücke, Sektor N + 1 auf [0, T]      | offene Konfiguration zu gleicher Zeit, Sektor N                                      |
| Übertragungs-Lemma | offen (G.8.4)                             | OA Satz 7.3                                                                          |
| Δ₂                 | nötig (≥ 0 nur numerisch)                 | entfällt                                                                             |
| Staffellauf        | nur Löschen                               | Löschen hinauf, Einfügen hinab                                                       |
| G1–G7              | ausgeschrieben                            | übertragen sich; neu: Einfüge-Hälfte (Zeitumkehr von G1), Begegnungen in vier Paaren |

**Was offen bleibt** (wie vorher, aber ohne den Kern): Lemma P\* (Ersatz für Jensen beim harten Kern, Zeitzerlegung), Satz T2 (gefärbte Operatoren), die Anpassung der Skelette an Schleifen, und für eine vernünftige Schwelle die Skalenspannung. Nach der Prüfung in G.11 kommen hinzu: der Spiegel-Abweg (behoben), orientierte Umwege und die Treffsumme als Voraussetzung von Lemma P\*.

### G.10.5 Exakte Prüfung am Mini-Ring [N]

*Nachtrag (G.11.1):* Der hier geprüfte Abweg hält den Kopf in seiner Zelle fest. Die Dichteformel ist richtig, aber das zweite Moment wächst mit dieser Fassung exponentiell in w. Der richtige Abweg ist das Spiegelbild des Aufwegs; seine Dichteformel ist in G.11.1 ebenso exakt geprüft.

[pruef\_zeitschleife.py](pruef_zeitschleife.py), Modell wie G.2 (Ring mit 6 Plätzen, 3 Zellen, Trotter-Zeit, Lücke über 2 Scheiben). Aufwärts läuft der Lösch-Staffellauf mit Querschritten. Abwärts wird je Scheibe ein Stück eingefügt; der neue Kopf ist ein gleichverteilter freier Platz der Zelle. Ziel ist das offene Maß zu gleicher Zeit µ(O) = W(O)/(N M Z\_N). Die Abwärts-Daten sind durch O bestimmt: Man verfolgt die Linie ab dem Kopf nach oben.

```text
f(O) = M · Σ_{Aufwärts-Daten} π Π_k sel_k Zalt_k/Zbr_k  ·  Π_k 1/(n_frei,k · Zein_k)
```

| N   | Schritte | λ   | offene Konfigurationen mit ν > 0 | größter relativer Fehler ν − fµ | \|ν\|²/∫f²dµ | q₀ = \|µ\| (Transfermatrix) |
|-----|----------|-----|----------------------------------|---------------------------------|--------------|-----------------------------|
| 3   | 4        | 0,7 | 177 477                          | 4,5·10⁻¹⁶                       | 0,154        | 0,671                       |
| 2   | 5        | 0,9 | 199 944                          | 5,6·10⁻¹⁶                       | 0,110        | 0,847                       |

Die Dichteformel der Zeitschleife ist exakt, einschließlich der Einfüge-Hälfte. Die Cauchy–Schwarz-Kette |ν|²/∫f²dµ ≤ q₀ = N₀/N ist erfüllt. Im Mini-System ist sie verlustreich, weil sich die Routen ständig begegnen. Die Fernkürzung mit dem neuen B ist am Mini-Ring nicht prüfbar (keine fernen Abschnitte); sie folgt wie G3 aus der Linienzahl-Tabelle G.10.2 und der Markov-Eigenschaft.

## G.11 Prüfung der offenen Punkte aus Tutorial §10 (2026-11-10 abends)

Jeder Punkt aus Tutorial §10 wurde gegen den OpenAI-Text (OA) und gegen die Zeitschleife geprüft. Ergebnis: ein echter Fehler in der ersten Fassung der Zeitschleife (A, behoben und exakt geprüft), eine gute Nachricht (B), zwei Stellen, an denen OAs Werkzeuge nicht wörtlich passen (C, D, beide mit Weg), und eine fehlende Voraussetzung (E).

| Befund | Inhalt                                                                     | Schwere                     | Stand                                                              |
|--------|----------------------------------------------------------------------------|-----------------------------|--------------------------------------------------------------------|
| A      | Der Abweg darf den Kopf nicht in seiner Zelle festhalten                   | Fehler, Schluss wäre falsch | behoben: Spiegel-Abweg, Dichteformel exakt geprüft [N]             |
| B      | OAs Übertragungs-Lemma (Satz 7.3) ist für eine Scheibe formuliert          | Lücke                       | geschlossen: Beweis trägt wörtlich über (0, T) [S nach OA]         |
| C      | Skelette: neue Begegnungen Aufweg gegen fremden Abweg; Steilheit und Torus | Lücke                       | Weg: OA Lemma 8.1 mit gespiegelter Zeit [S nach OA]; steil nur [B] |
| D      | Umwege: OAs Pfade sind räumlich, unsere Hälften zeitlich gerichtet         | Lücke                       | Weg: orientierte Umwege [B]                                        |
| E      | Lemma P\*: Treffschranke für eine feste Umgebungslinie fehlt               | Voraussetzung fehlte        | eigene Stücke: Anhang P [S]; umgehängte Brücken offen              |

### G.11.1 Befund A: Der Abweg muss seinen Weg verstecken

**Was falsch war.** Tutorial §5.3 und G.10.5 setzten den neuen Kopf gleichverteilt in die Zelle des alten Kopfes, ohne Querschritte. Dann läuft die eingefügte Linie in O eine feste Zellsäule entlang. Unter µ ist das selten: Eine Linie bleibt in einer Scheibe nur mit Wahrscheinlichkeit P(bleiben) in ihrer Zelle. Das gebaute Maß sitzt auf einer dünnen Menge, und ∫ f² dµ wächst je Scheibe mindestens um den Faktor 1/P(bleiben). Die Dichteformel war trotzdem richtig (G.10.5); sie sagt nichts über die Größe von ∫ f².

**Exakt für ein Teilchen [S + N]** ([pruef\_abwaerts\_einteilchen.py](pruef_abwaerts_einteilchen.py)). In stetiger Zeit mit Rate 1 je Nachbar und Zellen der Seite s gilt

```text
∫ f² dµ  =  Σ_z P_2T(z, z) · M · s^{−4w} · (V^w 1)(z),        V(h, h′) = 1 / P_δ(h, h′)   für h, h′ in der Zelle
```

Je Scheibe wächst ∫ f² also um λ\_max(V)/s⁴:

| s   | δ/s² | Faktor je Scheibe | ln Faktor | 1/P(bleiben) |
|-----|------|-------------------|-----------|--------------|
| 4   | 0,25 | 4,45              | 1,49      | 4,10         |
| 8   | 0,5  | 7,48              | 2,01      | 7,32         |
| 16  | 1    | 13,69             | 2,62      | 13,62        |

Zum Vergleich: Das ganze Budget je Begegnung ist α\_max ≈ 0,07.

**Abhilfe: der Spiegel-Abweg.** Je Scheibe, von oben nach unten:

1. Der Kopf steht oben bei Y₀ in der Zelle e₀. Man wählt einen Zug d der Route, also einen Sternpfad e₀, e₁, …, e\_m.
2. In jeder Zelle e\_l, l ≥ 1, wählt man ein wählbares Stück j\_l (Anfang und Ende in e\_l), gleichverteilt.
3. Neu gezogen werden gemeinsam, aus dem exakt normierten bedingten Gesetz: die Brücken j\_l: S\_l → Y\_{l−1} (Y\_l das alte Ende von j\_l) und ein neues Stück S′ → Y\_m mit **freiem Anfang** S′, summiert über alle freien Plätze.
4. Der neue Kopf ist S′. Ohne Querschritt (m = 0) wird nur das neue Stück eingefügt, und der Kopf wandert wie eine gewöhnliche Linie.

*Endgültige Wahl (G.12.1):* Statt des freien Anfangs in Schritt 3 wird S′ gleichverteilt unter den isolierten freien Plätzen der Zelle von Y\_m gewählt (Variante a), und jede Scheibe des Abwegs hat einen Querschritt. Grund: Die Ausweich-Untergrenze (Anhang P, Lemma P6) braucht feste, gute Endpunkte. Das Folgende gilt für beide Varianten. *Nachtrag 2026-11-11:* ersetzt durch Variante c (G.12.9), S′ aus dem bedingten Gesetz im Ball vom Radius D\_c s um Y\_m.

Rückwärts gelesen ist der Spiegel-Abweg ein Lösch-Staffellauf, der vom Kopf aus nach oben läuft, also dieselbe Art Schritt wie der Aufweg. Deshalb ist sein Weg in O versteckt: Welche Stücke eingefügt und welche umgehängt wurden, sieht man O nicht an. Im zweiten Moment sind D und D′ dann unabhängig, und die Linienzahl-Tabelle G.10.2 gilt wie dort. Sichtbar und beiden Schleifen gemeinsam ist nur das Kopfstück der untersten Scheibe (bei Zügen ohne Querschritt auch seine Fortsetzung); das ist ein Endzellen-Beitrag und geht in C\_end ein. Für ein Teilchen ist der Faktor je Scheibe genau 1, denn Σ\_{h′} K\_δ(h′, h) = e^{4δ} hängt nicht von h ab.

**Exakte Prüfung [N]** ([pruef\_zeitschleife\_spiegel.py](pruef_zeitschleife_spiegel.py), Ring mit 6 Plätzen und 3 Zellen, λ = 0,7, β = 4). Die Dichteformel des Spiegel-Abwegs ist

```text
f(O) = M Σ_{Abweg-Daten, alte Wege} Π_k π sel W(alt)/Z_neu  ·  Σ_{Aufweg-Daten} Π_k π sel Zalt/Zbr
```

Alle Kopf- und Lochplätze zwischen den Scheiben sind verdeckt und werden summiert. Weil Auf- und Abweg dieselben Scheiben ändern, steht die Aufweg-Summe innerhalb der Summe über die alten Wege des Abwegs.

| N   | w   | O mit ν > 0 | größter relativer Fehler ν − fµ |
|-----|-----|-------------|---------------------------------|
| 1   | 1   | 1 032       | 2,0·10⁻¹⁶                       |
| 1   | 2   | 1 536       | 4,0·10⁻¹⁶                       |
| 2   | 1   | 102 354     | 4,5·10⁻¹⁶                       |
| 2   | 2   | 133 104     | 7,3·10⁻¹⁶                       |

Ausbeute |ν|²/∫f² (die Untergrenze für |µ| = N₀/N), beide Abwege mit demselben Aufweg:

| N   | Abweg          | w = 1 | w = 2 | w = 3 | q₀ = \|µ\| |
|-----|----------------|-------|-------|-------|------------|
| 1   | Zelle (G.10.5) | 0,348 | 0,271 | 0,168 | 0,922      |
| 1   | Spiegel        | 0,611 | 0,835 | 0,907 | 0,922      |
| 2   | Zelle (G.10.5) | 0,319 | 0,234 | 0,143 | 0,817      |
| 2   | Spiegel        | 0,325 | 0,340 | 0,302 | 0,817      |

Mit dem eingeengten Abweg fällt die Ausbeute je Scheibe um den Faktor 0,6–0,8, mit dem Spiegel-Abweg nicht. Die Annahmewahrscheinlichkeit |ν| selbst fällt am Mini-Ring mit w, weil dort oft kein wählbares Teilchen für einen Querschritt da ist (Verwerfung). Die Ausbeute hängt davon nicht ab. Ergebnisse in ergebnisse/pruef\_zeitschleife\_spiegel\*.txt.

### G.11.2 Befund B: Übertragung über viele Scheiben

OA Satz 7.3 ist für ein „symmetric slab event“ formuliert, also für Ereignisse in einer einzigen Scheibe. OAs Route liegt ganz in einer Scheibe, unsere Schleife überstreicht w Scheiben. Der Beweis trägt aber wörtlich für ein symmetrisches Ereignis E auf den Weltlinien im ganzen Fenster (0, T):

1. Für das Bezugsmaß mit Kopf in der Zelle a und Schwanz in der Zelle b gilt µ\_ab(E) = (N M Z)^{−1} Spur(e^{−βH/2} a\*(1\_a) a(1\_b) U\_E) mit U\_E = K\_E e^{−(β/2 − T)H}. Dabei ist K\_E der getestete Kern des Fensters (0, T): die Summe der Weltlinien-Gewichte über (0, T), eingeschränkt auf E.
2. Gebraucht wird nur 0 ≤ K\_E ≤ e^{−TH} elementweise. Das gilt, weil alle Weltlinien-Gewichte ≥ 0 sind; in der Besetzungsbasis ist K\_E automatisch symmetrisch.
3. Hilbert–Schmidt-Cauchy–Schwarz wie bei OA, mit den Faktoren a(1\_a) e^{−βH/2} und a(1\_b) U\_E. Der zweite Faktor ist Spur(U\_E\* a\*(1\_b) a(1\_b) U\_E) ≤ s² Spur(U\_E\* n\_b U\_E) ≤ s² Spur(e^{−(β − T)H} n\_b K\_E) = s² Z E\_cl[n\_b(0) 1\_E]. Beim harten Kern gilt a\*(1\_b) a(1\_b) ≤ s² n\_b (Cauchy–Schwarz für Σ\_{x∈b} b\_x), ebenso für a, und E\_cl n\_b² ≤ C m² nach Satz 7.1. *Vermerk 2026-11-13 (Review H8):* Bis dahin stand hier n\_a; mit Kopf (Erzeugung) in a und Schwanz (Vernichtung) in b gehört n\_b in den getesteten Faktor. Am Ergebnis ändert das nichts.
4. Ergebnis: µ\_ab(E) ≤ (C/M²) P\_cl(E)^{1/4}. *Bezeichnung (2026-11-13):* M ist hier wie bei OA die Zahl der Zellen, M\_Z = |Λ|/s²; in Platz-Bezeichnung steht C s⁴/|Λ|² (Anhang M, M.9.2).

Die einzige Bedingung ist, dass E ganz auf einer Seite der Zeit 0 liegt. Das gilt, denn die Schleife liegt in [0, T]. **Stand:** [S], gegeben OA Satz 7.3.

### G.11.3 Befund C: Skelette für Schleifen

- **OAs Konstruktion ist schon eine Schleife.** OA §8.1 liest die zufällige Querabweichung bis zur Mitte vorwärts und danach rückwärts („the two halves deliberately use the same displacement variables“). Nimmt man die Zeit als erste Koordinate, sind die beiden Hälften genau U und D, mit der Wende in der Mitte. Innerhalb einer Schleife gilt U(t) − D(t) = (1 − t/w) · d, eine feste Verschiebung.
- **Neue Begegnungen.** Bei OA liegen die Zeitpunkte t und w − t an verschiedenen Orten. Bei uns sind sie dieselbe Zeit, und es gibt die Paarungen U–D′ und D–U′. Ihre Querdifferenz ist Z\_t − Z′\_t + s\_t mit einer festen Verschiebung s\_t (|s\_t| ≤ |d|).
- **OAs Beweis trägt.** Er benutzt nur, dass Z\_{t+k} gegeben die Vergangenheit eine Dichte ≤ C k^{−3/2} hat. Eine feste Verschiebung ändert daran nichts. Mit dem Test X\_t = min(1, 1{gleiche Hälfte nah} + 1{Gegenhälfte nah}) wird aus b₀ höchstens 2b₀, und Lemma 8.1 gilt für Schleifen mit halbiertem α. **Stand:** [S], gegeben OA Lemma 8.1.
- **Steilheit und Torus.** OAs w ist die Gesamtlänge der Schleife, bei uns W = 2w. OAs Beweis braucht, dass die Querabweichung nicht um den Torus läuft: W ≤ n/8 mit n = L/s Zellen, dann ist |Z| ≤ W/4. In diesem Bereich ist die Schleifenhöhe T = wδ ≈ L s/16, die Endpaare haben |d| ≤ W (ein fester Anteil υ ≈ 1/16 aller Paare, wie OAs „admissible pairs“), und je Scheibe kommen höchstens 1 Zelle Drift und 1/2 Zelle Zufallsgeschwindigkeit zusammen. Das Budget ist dann kleiner (Tutorial §4.3: schon bei Drift 0,5 nur etwa 0,004), aber positiv. **Für den Existenzsatz nimmt man diesen Bereich.**
- **Steile Schleifen (T ≫ L s)** brauchen eine Torus-Fassung: Die bedingte Dichte von Z modulo n ist ≤ C min(k^{−3/2}, n^{−2}), also b₀ ≤ C(R + 1)²(C + W/n²). Das bleibt beschränkt für n ≪ W ≤ n². [B], nur für eine bessere Schwelle.

### G.11.4 Befund D: Orientierte Umwege

OA §8.2 verwirft Konfigurationen mit einer Komponente schlechter Zellen der Größe ≥ n/4, füllt die übrigen Komponenten und führt den Pfad an ihrem Rand vorbei. OAs Pfade sind räumlich und dürfen in jede Richtung laufen. Unsere Hälften laufen in der Zeit nur in eine Richtung; innerhalb einer Scheibe darf die Route dagegen beliebig weit räumlich umsteigen (zyklisch längs eines räumlichen Pfades, wie OAs ganzer Staffellauf).

- **Was schiefgehen kann:** Eine Komponente, die zu einer Zeit ringförmig ist und sich später nach oben schließt („Kuppel“), fängt eine zeitlich gerichtete Route, die in ihren Innenraum geraten ist.
- **Ausweg:** vorausschauen. Jede Raum-Zeit-Komponente bekommt ihren um 1 vergrößerten umschreibenden Kasten; überlappende Kästen werden zusammengefasst. Die Route passiert einen Kasten so: In der Scheibe vor seiner Zeitspanne steigt sie räumlich bis außerhalb seiner räumlichen Projektion um, läuft außen senkrecht an ihm vorbei und steigt danach zurück. Außerhalb aller Kästen sind alle Zellen gut, also gibt es die nötigen wählbaren Teilchen.
- **Kosten:** Die Umweglänge ist ≤ C · Kastendurchmesser, und die Begegnungs-Buchführung geht wie bei OA über die Peierls-Summe der Komponentengrößen. Verworfen wird bei einer Komponente der Größe ≥ n/4; das Raum-Zeit-Zellgitter hat n² · 2w Zellen, also P(Verwerfen) ≤ C n² w p^{n/4} → 0.
- **Stand:** [B]. Rein geometrisch, neu gegenüber OA.

### G.11.5 Befund E: Die Voraussetzung von Lemma P\*

*Nachtrag:* Teilweise überholt durch [anhang\_ausweichen.md](anhang_ausweichen.md). Für die eigenen Stücke der Teilchen wird die Ausweich-Untergrenze Teil der Auswahl (zugängliche Teilchen), ihre Seltenheit ist bewiesen. Für umgehängte Brücken und neue Stücke bleibt Lemma P\* nötig (Anhang P, P.6); dafür ist die Treffsumme weiter ein Kandidat.

Die Skizze in G.6.2 schätzt im Teilintervall die Treffwahrscheinlichkeit jeder Umgebungslinie wie die eines ruhenden Punktes ab (≈ ln(√τ/d)/ln(√τ/a)). Für eine *feste* Umgebungslinie mit beliebiger Bahn folgt das nicht von selbst. Allgemein gilt nur, dass die mittlere gemeinsame Aufenthaltszeit ≤ C ln τ ist, und die Treffwahrscheinlichkeit kann größer sein als beim ruhenden Punkt.

- **Ausweg:** Die Treffsumme 𝒯\_k = max über gute Startpunkte von Σ\_j P\_frei(trifft die Linie j im Teilintervall k) hängt nur von der Umgebung ab. Man nimmt 𝒯\_k ≤ 1/4 in die Güte der Zelle auf.
- **Teilintervall:** τ = ln(1/ρ)/(8πC₀ρ). Dann ist der mittlere Wert von 𝒯\_k unter dem Grundzustands-Pfadmaß ≤ 1/8 (lokale Dichte ≤ C₀ρ, Linien wandern höchstens wie freie nach Lemma T1). Es gibt n ≈ 8πC₀K Teilintervalle, also p\* ≥ e^{−C₁(C₀)(K + 1)} wie behauptet.
- **Seltenheit:** 𝒯\_k > 1/4 ist ein Defekt-Ereignis auf Bahnen. Seine Seltenheit, gemeinsam über viele Zellen, gehört zum Defekt-Lemma (Tutorial §10, Punkt 3; Satz T2).
- Außerdem war in G.6.2 die lokale Dichte C₀ in der Wahl von τ vergessen. Sie verschiebt nur die Konstante C₁.
- **Stand:** [B], Voraussetzung jetzt ausdrücklich.

### G.11.6 Was sich nicht ändert, und Kleinigkeiten

- **Selbstbegegnungen** U–D derselben Schleife (bei kleinem |d| über die ganze Höhe) kosten im zweiten Moment nichts: Sie kürzen sich zwischen Ĉ/O und B/C wie alles fern von R′. Für die Annahme gilt die Regel „erst Aufweg, dann Abweg“; je Zelle und Scheibe ändern sich dabei höchstens m + 1 Stücke, die Wählbarkeit bleibt also bis auf O(1) erhalten.
- **Die Wende:** Die oberste Scheibe wird von beiden Hälften geändert. Die Dichteformel deckt das ab (Summe über die alten Wege, G.11.1).
- **C\_end:** Beide Enden liegen zur Zeit 0; das gemeinsame Kopfstück aus G.11.1 kommt hinzu. Die Rechnung aus G.8.3 überträgt sich.
- **Δ₂, Lemma J, Harnack, umgekehrte Hölder-Ungleichung:** werden nicht mehr gebraucht (G.10.2).

## G.12 Buchführung für die Zeitschleife (Tutorial §10, Punkt 1)

Stand 2026-11-10 spät abends. Hier wird Satz 5.2 für die Zeitschleife zusammengesetzt, Schritt für Schritt wie G.1–G.8 und OA §9–§10. Benutzt werden Anhang S (Skelette, orientierte Umwege), Anhang P (Ausweichen) und das Defekt-Lemma (satz\_3\_9\_dichteschranken.md §9–§12).

### G.12.0 Was sich gegenüber G.1–G.8 ändert

| Schritt                  | Lücke (G.1–G.8)                | Zeitschleife                                                                                                       |
|--------------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Ziel                     | Lückenmaß Γ\_T, dazu G(τ), Δ₂  | offenes Maß µ zu gleicher Zeit, \|µ\| = N₀/N                                                                       |
| G1 Dichteformel          | nur Löschen                    | Löschen hinauf, Spiegel-Einfügen hinab (G.12.2)                                                                    |
| G3 Fernkürzung           | Gruppen j (R) und l (R′)       | je Hälfte eine Gruppe, beim Abweg mit vertauschten Rollen von Normierer und altem Gewicht (G.12.4)                 |
| G4, G5 Nenner            | Lemma P\* (W1), (W2)           | eigene Stücke: Zugänglichkeit (Anhang U); umgehängte und neue Stücke: Lemma P6 unter (G1″), (G2\_A), (G4) (G.12.5) |
| G6 Wählbarkeit, Listen   | Scores; 4^{b\_tot}; ℓ\_tot     | keine Scores; Lokalität aus Lemma S2; ℓ\_tot entfällt (G.12.6, Anhang L)                                           |
| G7 Summieren, Normierung | Gegen-Lückenmaß (offen, G.8.4) | Bezugsmaß µ\_ab im selben Sektor, Übertragung nach G.11.2 (G.12.7)                                                 |

### G.12.1 Die Konstruktion, endgültig

- **Skelett:** OAs Skelett als Schleife, Gesamtlänge W = 2w ≤ n/8, Endzellen a (Zelle von x) und b mit |b − a|\_∞ ≤ W (Anhang S, S.1). Die Endzelle b wird gleichverteilt unter den zulässigen Zellen gewählt.
- **Umwege:** Lagen r\_k im Außenraum der Füllungen beider angrenzenden Scheiben (Anhang S, Lemma S2). Die Füllungen gehören zu den verdickten defekten Zellen aus Satz D, und D4 zählt fehlerhafte Stücke nach Anfangs- *und* Endzelle.
- **Auswahl, ohne Gruppe:** Die Umsteige-Teilchen j\_l werden gleichverteilt unter den wählbaren Stücken der Zelle gewählt. Wählbar heißt regulär⁺ (Tests 1 bis 3 aus G.5.1, dazu (G2\_A) und (G4′) für die eigene Bahn) und zugänglich: Die freie Brücke mit cut weicht allen anderen Stücken der Scheibe mit Wahrscheinlichkeit ≥ p\* aus ([anhang\_unzugaenglich.md](anhang_unzugaenglich.md), Anhang U). *Frühere Fassung (bis 2026-11-11):* eine nach OAH §7.2 zurückgehaltene Gruppe von M Teilchen je Zelle, Zugänglichkeit gegen die Stücke außerhalb der Gruppe. Damit hätten geteilte Teilchen 1/M statt 1/n\_Q gekostet, und die gemeinsame Seltenheit war nur für feste Marken bewiesen (Review W2 und K2).
- **Aufweg, Scheibe k:** j₀ ist das Stück am Loch. Es ist regulär (Isolation, Makro- und Randbedingung), weil j\_m der Scheibe davor nur unter Stücken mit regulärer Fortsetzung gewählt wird (Wählbarkeit über zwei Scheiben, Anhang L, Regel 1). Es endet also an einem isolierten Platz, höchstens D + 1 Zellen von r\_k. Umsteigen längs eines Sternpfads von seiner Endzelle nach r\_{k+1}, in jeder Scheibe mindestens einmal (m ≥ 1; ist die Endzelle schon r\_{k+1}, innerhalb der Zelle; Regel 2); Brücken aus dem exakt normierten bedingten Gesetz. In Scheibe 0 wird verworfen, wenn das Stück des Schwanz-Teilchens nicht regulär ist (Regel 3). *Frühere Fassung (bis 2026-11-11):* „Es beginnt in der guten Zelle r\_k, ist also nach D4 nicht weit gewandert.“ Das folgt nicht, denn eine gute Zelle darf einzelne Fehlgänger enthalten (Review K3).
- **Abweg, Scheibe k (Spiegel-Abweg, Variante c, G.12.9):** Querschritt in jeder Scheibe. Die Brücken j\_l und das neue Stück S′ → Y\_m werden gemeinsam aus dem exakt normierten bedingten Gesetz gezogen. Der Anfang S′ läuft dabei über die Plätze im Ball vom Radius D\_c s um Y\_m, die zur Zeit t\_k Abstand > r von allen Teilchen haben. (Bis 2026-11-10 Variante a: S′ gleichverteilt unter diesen Plätzen der Zelle von Y\_m, eigene Normierung je S′.)
- **Schwanz wie bei OA (seit 2026-11-13, [anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M.9.5):** Ein Hilfspunkt ξ gleichverteilt auf Λ bestimmt die Zelle a; verworfen wird, wenn ξ nicht gut ist. Das Schwanz-Teilchen wird gleichverteilt unter den Teilchen in a gewählt, deren Stück in Scheibe 0 regulär ist. Damit entfällt Regel 3 aus Anhang L. Die Dichte hat den Vorfaktor N s²/A und den Schwanzfaktor 1/g⁰\_a(Ĉ) (Lemma M14a). *Frühere Fassung:* Schwanz-Teilchen gleichverteilt unter allen N, Vorfaktor M.
- **Gezogene Stücke regulär (seit 2026-11-13, [anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M2):** Brücken und neue Stücke werden aus dem exakt normierten Gesetz gezogen, das zu cut und Ausweichen die Regularität (G2\_A) und (G4′) der eigenen Bahn hinzunimmt. Jede Untergrenze für einen Normierer verliert dadurch höchstens p\_irr → 0 (Lemma M2). Brauchbare Zellen erfüllen zusätzlich die Klausel (v): Kastenbedingungen (Anhang M, M1).
- **Verwerfen:** Komponente ≥ n/4, Endzelle in einer Füllung (Anhang S), Stück des Schwanz-Teilchens in Scheibe 0 nicht regulär (Anhang L, Regel 3), oder kein zugängliches Teilchen bzw. kein guter freier Platz (in guten Zellen ausgeschlossen).

### G.12.2 G1 für die Schleife [S]

```text
f(O) = dν/dµ (O)  =  M · Σ_{Abweg-Daten, alte Wege} Π_k π sel W(alt)/Z_neu,k  ·  Σ_{Aufweg-Daten} Π_k π sel Z^alt_k/Z^br_k
```

Mit Variante c ist Z\_neu,k = Σ\_{S′∈G(Y\_m)} Z(Brücken und S′ → Y\_m) (G.12.9); mit Variante a war es n\_gut,k · Z(Brücken und S′ → Y\_m), mit der Zahl n\_gut,k der zulässigen Anfangsplätze. Alle Kopf- und Lochplätze zwischen den Scheiben sind verdeckt und summiert. Beweis wie G1. Exakt geprüft am Mini-Ring (G.11.1; Variante a für w = 1, Fehler 2,2·10⁻¹⁶).

### G.12.3 G2 [S]

∫ f² dµ = ∫ f dν = Σ\_{R, R′} π(R) π(R′) ∫ f\_R dν\_{R′}, und |ν|² ≤ |µ| ∫ f² dµ mit |µ| = N₀/N (Tutorial Lemma 5.1, 3.2).

### G.12.4 G3 für die Schleife: Fernkürzung [S]

Fest sei ein Summand: R′ baut O aus C, R wertet f\_R(O) aus. In jeder Scheibe gibt es bis zu vier Gruppen von Stücken: die von R′ gezogenen (auf U′ Brücken, auf D′ Brücken und ein neues Stück) und die von R gezogenen.

**Lemma G3′ [S].** Liegen die Stücke von R und R′ in einer Scheibe wegen cut außer Reichweite voneinander, so gilt für die Integration über die beteiligten Stücke

```text
∫ P(C) · [Faktoren von R′] · [Faktoren von R]   =   ∫ P(B) · sel(B)
```

mit B = C plus Rückweg längs R, also +1 Linie längs U\_R und −1 Linie längs D\_R (Tabelle G.10.2).

*Beweis.*

1. **Teile von R′** (Aufweg und Abweg). R′ zieht seine Stücke aus normierten Gesetzen W/Z. Die Integration über diese Stücke gibt 1, sofern die Faktoren von R nicht von ihnen abhängen. Das gilt, weil sie außer Reichweite liegen und die Wählbarkeit lokal ist.
2. **Aufweg von R:** wie G3, j-Teil. Die Brücken von R sind in O = C die Stücke von C. Integration von P(C) ∝ W(C\_j) über sie kürzt Z^br, und es bleiben die alten Stücke Ĉ\_j: +1 Linie.
3. **Abweg von R:** mit vertauschten Rollen. Die *neuen* Stücke von R (Brücken und neues Stück) sind in O = C Stücke von C. Integration von P(C) über sie kürzt Z\_neu. Es bleibt W(alt), die alten Stücke ohne das neue Stück: −1 Linie.
4. **Auswahl:** Die Auswahlfaktoren beider Hälften von R werden im Zustand vor dem jeweiligen Schritt gezählt. Fern von R′ ist das der Zustand B. ∎

Ist R nahe bei R′, stehen in dieser Scheibe die Gruppen h, d, j, l wie in G.4, mit allen vier Paarungen; die Kosten dort behandeln G.12.5 bis G.12.7.

### G.12.5 G4 und G5: die Nenner nahe einer Begegnung [B, gegeben Lemma U4, Lemma P6]

Wie G.6.4 und G.7, mit zwei Sorten von Stücken:

| Sorte                           | Beispiel                                             | Ausweich-Untergrenze                                                                            |
|---------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| eigene Stücke                   | Stücke von C mit ihren Endpunkten (Gruppe j, d in C) | zugänglich: a ≥ p\* gegen alle anderen Stücke, also gegen jede Teilfamilie (Anhang U, Lemma U4) |
| umgehängte Brücken, neue Stücke | Gruppe l in O, d in O, neue Stücke des Abwegs        | Lemma P6, wenn (G1″), (G2\_A), (G4) gelten und die Endpunkte gut sind                           |

- **Gute Endpunkte:** Bei Brücken sind Anfang und Ende Endpunkte wählbarer (isolierter) Teilchen. Das gilt auch für die erste Brücke S₁ → Y₀ des Aufwegs, weil das Lochstück j₀ regulär und sein Ende Y₀ damit isoliert ist (Anhang L, Lemma L1). Beim neuen Stück ist S′ nach Konstruktion isoliert, und Y\_m ist das Ende des wählbaren j\_m. Für das neue Stück von Variante c tritt an die Stelle von Lemma P6 die über S′ gemittelte Schranke Lemma C (c) (G.12.9).
- **(G1″), (G2\_A), (G4)** (bis 2026-11-11: (G1)–(G3)): gelten im Kasten jeder brauchbaren Zelle, in jedem Zustand, der sich in höchstens n″ regulären Stücken vom Zeugen unterscheidet (Klausel (v) und Lemma M4 (3), [anhang\_buchfuehrung.md](anhang_buchfuehrung.md)). Bis 2026-11-12 stand hier „im Kasten jeder nicht defekten Zelle“; das reicht nicht, weil die Route nur unbrauchbare Zellen meidet. Selten sind die Verletzungen nach Satz F10 und Satz F11 ([anhang\_feinskala.md](anhang_feinskala.md)). Der Kasten hat den Radius D\_K s (Anhang F, F.12.6).
- **Ablauf wie G.6.4:** Die Dichte jedes bedingten Stück-Gesetzes bezüglich der freien Brücke ist ≤ 2/p\*. Die Treffwahrscheinlichkeit mit einem nahen Stück der anderen Schleife ist ≤ 2P\_treff/p\*, und P\_treff ≲ ln ln(1/ρ)/ln(1/ρ) folgt aus (G4) und (G2\_A) (Anhang F, Lemma F13). Die Gruppen-Vereinigungsschranke gibt e^{−σ\_ρ J} mit σ\_ρ = C e^{δμ̄ + κ} P\_treff → 0, und d-Stücke kosten je p\*.
- **Ergebnis:** G4 und G5 gelten wörtlich mit C(K) = δμ̄ + κ + C und σ\_ρ wie eben, für alle vier Paarungen U–U′, D–D′, U–D′, D–U′.

### G.12.6 G6: Wählbarkeit, Stabilität, Listen [B, nach OA §10.4]

- **Wählbarkeit:** Isolation, Makro- und Randbedingung, Regularität der eigenen Bahn ((G2\_A), (G4′)), Zugänglichkeit; keine Scores (satz\_3\_9 §12.1). Für j\_m im Aufweg zusätzlich: Die Fortsetzung in der Folgescheibe ist regulär (Anhang L). Brauchbare Zellen erfüllen dazu die Klauseln (iii) und (iv) aus Anhang L, L.1, und (v) aus Anhang M (Kastenbedingungen).
- **Zählung in B:** längs U\_R zählt n\_Q(B) eins mehr, längs D\_R eins weniger als C. In der ersten Zelle a und der letzten Zelle b liegen die offenen Enden von B; die betreffenden Stücke werden in B für nicht wählbar erklärt, aber mitgezählt (wie OAs Ausnahme-Slot).
- **Stabilität (G6.1):** gilt wie dort mit einer Toleranz von ±1 in der Zählung. Die Zugänglichkeit hängt von den Bahnen der Nachbarn ab und ändert sich um höchstens n′ P^{br}\_treff, wenn n′ Stücke in Reichweite umgehängt werden. Sie wird deshalb im Zeugen mit der Schwelle p\* und im Bezugszustand B mit 2p\* geprüft, so wie G.5.2 es für die Scores vorsah (Anhang U, Lemma U4). Die Tests sind lokal, und die geänderten Stücke liegen nach cut nahe den beiden Sternpfaden; das gelöschte Lochstück j₀ gehört dazu, weil es regulär ist. Die Anzeige „doppelt wählbar“ hängt von zwei Scheiben ab; der Begegnungsradius R\* ist deshalb um 2D + 4 größer zu nehmen (Anhang L, L.5).
- **Listen (G6.2):** Die Route hängt nach Lemma S2 (4) nur von den Stücken P\_k der Füllungen nahe dem Skelett ab, die Wege nur von den Füllungen längs der Strecken. Für Brücken-Komponenten (nahe beiden Skeletten) rät man, ob sie in S(C), S(Ĉ) oder S₁(B) liegen. Das gibt ≤ 4^{b\_tot} Routenpaare, und J ≤ J₀ + C(R\*) b\_tot.
- **ℓ\_tot entfällt:** j₀ ist in jedem Zeugen regulär (Anhang L, Lemma L1) und endet höchstens D + 1 Zellen von r\_k. Die Sternpfade sind also kürzer als D + |r\_{k+1} − r\_k| + 2. (Bis 2026-11-11 stand hier als Grund D4, nach Anfangszelle gezählt; das reicht nicht, Review K3.)

### G.12.7 G7: Summieren und Satz 5.2 [B]

*Lesehinweis (2026-11-14, Review 2026-11-13, H3):* Ausgeschrieben ist G7 in Anhang M (M.7 bis M.9). Dort gilt κ₀ = 3ε + 6σ + (e^{2C(K)} + 4)/(b₋m − 4) mit der Bedingung κ₀ ≤ α\_J (M.8.4) statt κ₀ = 10ε + … ≤ α/2, und die Annahme ist |ν| ≥ υ/2 − 5ζ² (Z.12; der Abzug ε von Regel 3 entfällt seit M.9.5). Die Zahlen unten sind der Stand vom 2026-11-12.

1. **Auswahl** (G.8.1): Je nahem gemeinsamen Vorkommen kostet es 1 + (e^{C(K)} − 1)/n\_Q für geteilte Teilchen, (1 − 2ε)^{−1} für die Auswahl und e^{σ\_ρ} für nahe verschiedene Stücke. Mit der Wählbarkeit über zwei Scheiben ist ein Vorkommen von j\_m auch dann nah, wenn die Begegnung in der Folgescheibe liegt; die Zahl der nahen Vorkommen verdoppelt sich dadurch höchstens (Anhang L, L.5). Zusammen e^{κ₀} je Begegnung mit

   ```text
   κ₀  =  10ε + σ_ρ + (e^{C(K)} − 1)/(b₋ m)        (bis 2026-11-11: 2ε statt 10ε)
   ```

   Die erste Zelle a (gemeinsamer Schwanz) trägt e^{C(K)}/n\_a bei. Die letzte Zelle b trägt das gemeinsame Kopfstück der untersten Scheibe bei. Mit Querschritt in jeder Scheibe setzt sich das Teilen je Scheibe nur mit Wahrscheinlichkeit ≤ C/m fort, und je geteilter Scheibe kostet das neue Stück höchstens 1/(c₁ p₁) (Lemma C (e), G.12.9). Also ist der Beitrag ≤ 2 für m ≥ 2C/(c₁ p₁). (Bis 2026-11-12 stand hier „≤ 1/(1 − η\_c) ≤ 2 je Scheibe, m ≥ 4C“, und für Variante a „≤ 14“. Das war die Rechnung für ein einzelnes Teilchen; bei vielen Teilchen bleibt je geteilter Scheibe der Kehrwert des Normierers stehen, Review W1.)
2. **Routen** (G.8.2): Σ ≤ C/(n\_a n\_b) · e^{κ₀ J₀} · e^{C′ b\_tot}.
3. **Seltene Komponenten unter B.** Die Faktoren e^{C′b\_tot} und die Indikatoren der Brücken-Komponenten sind Ereignisse auf (0, T) unter dem Bezugsmaß µ\_ab. Nach Satz D (zweite Zeile, Exponent 1/4 aus G.11.2) und Lemma S3 ist E\_{µ\_ab}[e^{C′ b\_tot} 1{…}] ≤ (C/M²) Σ\_k (C q^{1/4} e^{C′})^k. Für q klein genug ist das ≤ C/M².
4. **Skelette:** Lemma S1 gibt E e^{θJ₀} ≤ C für θ < α. Hölder trennt J₀ und b\_tot.
5. **Normierung** (G.8.3): Die paarweisen Dichten von ν und µ und das Gewicht von µ\_ab sind alle ~ 1/M². Kein Faktor M, N, L oder 1/ρ bleibt übrig; die Auswahlsummen der Endzellen heben sich gegen n\_a, n\_b. Einen Faktor e^{−Δ₂T} gibt es nicht mehr.
6. **Ergebnis (Satz 5.2):** Ist κ₀ ≤ α/2, so ist ∫ f² dµ ≤ C\_end · C\_S1 · C\_D mit Konstanten, die nicht von L, N oder ρ abhängen.

**Annahme |ν| ≥ a₀ > 0.** Verworfen wird bei einer großen Komponente oder einer Endzelle in einer Füllung (Anhang S, S.3: Wahrscheinlichkeit → 0), sonst nie: In guten Zellen gibt es zugängliche Teilchen mit regulärer Fortsetzung und isolierte freie Plätze (Anhang L, Lemma L2). Einmal, in Scheibe 0, wird außerdem verworfen, wenn das Stück des Schwanz-Teilchens nicht regulär ist; das kostet höchstens ε. Dazu kommt der Anteil υ ≈ 1/16 zulässiger Endzellen-Paare. Also |ν| ≥ υ/2 − ε für kleines ρ. *Nachtrag 2026-11-13 ([anhang\_zweites\_moment.md](anhang_zweites_moment.md), Z.12):* Seit dem Schwanz über ξ (Anhang M, M.9.5) wird auch verworfen, wenn ξ nicht gut ist; weil ξ gleichverteilt und von C unabhängig ist, hat das die Wahrscheinlichkeit ≤ ρ(2r + 1)² ≤ 5ζ². Also |ν| ≥ υ/2 − ε − 5ζ².

**Schluss.** N₀/N = |µ| ≥ |ν|²/∫ f² dµ ≥ (υ/2 − ε)²/(C\_end C\_S1 C\_D) =: c > 0 (seit M.9.5 und Z.12: |ν| ≥ υ/2 − 5ζ², ohne den Abzug ε, Review 2026-11-13, H8), sobald ρ so klein ist, dass κ₀ ≤ α/2 und q, σ\_ρ, 1/m klein genug sind.

### G.12.8 Stand

| Teil                                              | Stand                                                                                         |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------|
| G1, G2, G3′ (Dichte, zweites Moment, Fernkürzung) | [S]; G1 exakt geprüft                                                                         |
| G4, G5 (Nenner nahe Begegnungen)                  | [B]: Ablauf wie OA §10.2–10.3, Eingänge P3 [S], P6 [B]                                        |
| G6 (Stabilität, Listen)                           | [B]: wie OA §10.4, vereinfacht durch Lemma S2 und das reguläre Lochstück (Anhang L)           |
| G7 (Summieren, Normierung, Annahme)               | [B]: wie OA §10.5, mit S1 [S nach OA], Satz D, G.11.2 [S]                                     |
| Variante c des Abwegs (Anfang im Ball, G.12.9)    | Lemma C [S, gegeben P6]; Dichteformel exakt; Testmodell: Kosten je Scheibe → 1 mit dem Radius |

**Was noch fehlt, ehrlich gezählt:**

1. ~~Die Ausarbeitung der vier Gruppen in G4–G7 im Stil von OA §10.~~ Ausgeschrieben in [anhang\_zweites\_moment.md](anhang_zweites_moment.md) (Anhang Z), Schritt für Schritt nach OA §10.
2. Lemma P6 in den Einzelheiten (Rekursion für große Schritte, Wahl von ζ). *Nachtrag 2026-11-12:* ausgeschrieben mit den Bedingungen (G1″), (G2\_A), (G4) in Anhang F, F.12, samt der Seltenheit dieser Bedingungen (Satz F10, Satz F11). Offen bleibt die Voraussetzung guter Endpunkte (Review K3).
3. Die Eingänge mit Literaturstatus: Gitter-Wärmeleitungskern, BPP/Häggström–Mossel über OA Lemma 8.1.
4. ~~Eine Monte-Carlo-Prüfung der Ausbeute mit Variante a an einem System mit vielen Teilchen je Zelle (der Mini-Ring kann das nicht).~~ Testmodell auf dem 2D-Torus (Anhang Z, Z.11): Variante a ist bei kleinem m teuer (×3–4 je Scheibe), daraus Variante c (G.12.9).

Für eine vernünftige Schwelle kommen die Punkte aus Tutorial §10 „Nur für eine bessere Schwelle“ dazu. Das garantierte Budget α aus Lemma S1 ist klein (θ ≲ 10⁻³), also ist ρ\* noch kleiner als in Tutorial §9.3 geschätzt.

### G.12.9 Variante c: Anfang im Ball (2026-11-11)

**Anlass [N].** Im Testmodell auf dem 2D-Torus (Anhang Z, Z.11) wächst ∫f²dµ mit Variante a um ×3–4 je Scheibe, mit freiem Anfang gar nicht. Teuer ist die Beschränkung des Anfangs S′ auf die Zelle, nicht seine Verteilung darin: Das bedingte Gesetz auf der Zelle ist nicht billiger als die Gleichverteilung. Zieht man S′ aus dem bedingten Gesetz in einem Ball um Y\_m, fallen die Kosten mit dem Radius auf 1 (R = 1, 2, 3: Faktor 2,11; 1,17; 0,99 je Scheibe).

**Konstruktion (ersetzt Variante a).** Scheibe k des Abwegs, Sternpfad und Auswahl wie bisher. F seien alle Stücke der Scheibe außer den Brücken j\_l und dem neuen Stück. Mit

```text
G(Y_m)  =  { S′ :  S′ hat zur Zeit t_k Abstand > r von allen Linien,  |S′ − Y_m| ≤ D_c s }
```

werden Brücken, Anfang S′ und neues Stück gemeinsam gezogen:

```text
P(ω_br, S′, ω_neu)  =  1_{G(Y_m)}(S′) · W(ω_br) W(ω_neu) · 1{harter Kern untereinander und mit F} / Z_neu
Z_neu  =  Σ_{S′ ∈ G(Y_m)} Z(Brücken und S′ → Y_m | F)
```

- Der neue Kopf ist S′. Gegeben S′ ist das neue Stück eine Brücke mit festen Endpunkten.
- Variante a war: S′ gleichverteilt auf G(Y\_m) ∩ Zelle(Y\_m), eigene Normierung je S′.
- Der *freie Anfang* aus G.11.1 (Schritt 3) ist derselbe Ausdruck mit S′ über alle freien Plätze. Seine Zustandssumme heiße Z\_alle, und P\_c = Z\_neu/Z\_alle.

**Lemma C [S, gegeben Lemma P6 unter den Voraussetzungen von G.12.5].** Die Zellen im Abstand ≤ D\_c + D von Y\_m seien nicht defekt (zu lesen als: brauchbar einschließlich Klausel (v); nach der Verdickung gilt das im Abstand ≤ 2D + 2 vom Weg, [anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M.6.5), Y\_m sei gut zur Zeit t\_{k+1}, und c\_δ s² ≤ δ ≤ C\_δ s². Sei p₁ = ½ e^{−C′(n+1)} die Schranke aus Lemma P6 für Brücken der Länge ≤ s. Dann gilt mit Konstanten c₁, c, C, die nur von c\_δ und C\_δ abhängen:

- **(a) Masse:** 1 − P\_c ≤ η\_c := C (e^{−c D\_c²} + C\_a ζ² D\_c²)/(c₁ p₁).
- **(b) Vergleich mit dem freien Anfang:** Das Gesetz von Variante c hat bezüglich des freien Anfangs die Dichte 1\_G(S′)/P\_c. Ihr zweites Moment ist 1/P\_c ≤ 1/(1 − η\_c).
- **(c) Gemitteltes Stück-Gesetz:** Gegeben die Brücken hat (S′, ω\_neu) bezüglich der freien Rückwärts-Irrfahrt Q\_Y von Y\_m (Dauer δ, ihr Ort zur Zeit t\_k ist S′) die Dichte ≤ 1/(c₁ p₁).
- **(d) Kopfdichte:** P(S′ = y) ≤ C/(c₁ p₁ s²) für jeden Platz y.
- **(e) Geteilte Kopfscheibe (2026-11-12):** Haben in einer Scheibe des Abwegs die bauende und die auswertende Schleife dasselbe neue Stück, so bleibt im zweiten Moment für diese Scheibe der Faktor Σ\_S Z\_frei(S → Y\_m)/Z\_neu stehen, und er ist ≤ 1/(c₁ p₁).

*Beweis.*

1. **Untergrenze des Normierers.** Bei festen Brücken ist Z(S′ → Y\_m | F, Brücken) = a(S′) · Z\_frei(S′ → Y\_m), mit der Ausweichwahrscheinlichkeit a(S′) der freien Brücke vor F und den Brücken. Für S′ ∈ G mit |S′ − Y\_m| ≤ s sind beide Endpunkte gut, und Lemma P6 gibt a(S′) ≥ p₁. Nach (K2) ist p\_δ(S, Y\_m) ≥ c′/s² für |S − Y\_m| ≤ s. Davon sind höchstens C C\_a ζ² s² Plätze nicht isoliert: In den nicht defekten Zellen, die den Kreis vom Radius s + r treffen, liegen zur Zeit t\_k zusammen ≤ C C\_a ρ s² Linien (Defektgrund D1), jede sperrt ≤ (2r + 1)² Plätze, und r² = ζ²/ρ. Für kleines ζ bleibt also eine Masse ≥ c₁ des freien Kerns. Damit ist Z\_neu(Brücken) ≥ c₁ p₁ Σ\_S Z\_frei(S → Y\_m) für jede Lage der Brücken.
2. **(a):** 1 − P\_c ≤ (Z\_alle − Z\_neu)/Z\_neu. Im Zähler ist a ≤ 1, also zählt nur die freie Kernmasse außerhalb von G. Ferne Plätze (|S′ − Y\_m| > D\_c s) tragen nach (K1) ≤ C e^{−cD\_c²} bei. Nicht isolierte Plätze im Ball sind wie in Schritt 1 höchstens C C\_a ζ² D\_c² s² Stück, jeder mit p\_δ ≤ C/s². Weil Schritt 1 für jede Lage der Brücken gilt, überträgt sich das Verhältnis auf die Summe über die Brücken.
3. **(b):** Variante c ist der freie Anfang, eingeschränkt auf S′ ∈ G und neu normiert.
4. **(c), (d):** Gegeben die Brücken ist das Gewicht von (S′, ω\_neu) gleich 1\_G(S′) W(ω\_neu) 1{weicht aus}/Z\_neu ≤ W(ω\_neu)/(c₁ p₁ Σ\_S Z\_frei(S → Y\_m)). Das ist 1/(c₁ p₁) mal das Gewicht unter Q\_Y. Summiert über die Wege mit Anfang y folgt P(S′ = y) ≤ p\_δ(y, Y\_m)/(c₁ p₁) ≤ C/(c₁ p₁ s²) nach (K1).
5. **(e):** In ∫ f dν trägt die bauende Schleife R′ für die Scheibe die normierte Dichte ihrer gezogenen Stücke bei, W(neu)/Z\_neu, und die auswertende Schleife R den Faktor W(alt)/Z\_neu(O) der Dichteformel. In einer fernen Scheibe sind die neuen Stücke von R Stücke von C, und die Integration von P(C) über sie kürzt Z\_neu(O) (Lemma G3′). Ist das neue Stück dagegen beiden gemeinsam, so ist es das von R′ gezogene. Z\_neu(O) hängt von S′ und vom neuen Stück nicht ab, weil es über beide summiert; die Integration über das Gezogene gibt 1, und 1/Z\_neu(O) bleibt unintegriert stehen. Bezogen auf die freie Kernmasse ist das nach Schritt 1 höchstens 1/(c₁ p₁). Sind auch Brücken gemeinsam, kommen ihre Kosten e^{C(K)} je Stück aus G4 dazu. ∎

*Bemerkung zu (b) und (e) (Review W1).* (b) allein gibt die Kosten der geteilten Kopfscheibe nicht. Es vergleicht mit dem freien Anfang, und dessen eigene Kosten sind nur für ein Teilchen gleich 1 (G.11.1). Bei vielen Teilchen bleibt auch dort der Kehrwert des Normierers stehen, 1/A mit der Wahrscheinlichkeit A, dass die freie Rückwärts-Irrfahrt ab Y\_m allen Linien der Scheibe ausweicht. Typisch ist A ≈ e^{−2πK} (G.6.2), garantiert ist in guten Zellen A ≥ c₁ p₁. Das Testmodell sieht davon nur 1,07 bis 1,16 je Scheibe, weil dort m ≤ 3 ist und Ausweichen leicht fällt. Das ist dieselbe Größe e^{C(K)} wie bei jedem geteilten Stück (G.12.7); beim Kopfstück ist nur die Wahrscheinlichkeit des Teilens in der untersten Scheibe 1 statt 1/n\_Q.

*Bemerkung zu (c).* Ferne Anfänge brauchen kein eigenes Lemma P6. Das bedingte Gesetz gewichtet jeden Anfang S′ mit a(S′), und genau dieser Faktor steht im Nenner der Dichte des bedingten Stücks; über S′ gemittelt kürzt er sich. Nur die Untergrenze des Normierers braucht P6, und zwar nur für kurze Brücken. Deshalb hängt p₁ nicht von D\_c ab, und es gibt keinen Zirkel zwischen D\_c und D.

*Nachtrag 2026-11-12 (Review K1 und W1).* In Schritt 1 und 2 stand bis 2026-11-11 die Bedingung (G1) mit der Konstanten C₀. Gebraucht wird dort nur die Dichte auf der Zellskala zur Scheibenzeit t\_k, und die liefert Satz 3.9 (a) mit der Konstanten C\_a. Lemma P6 steht jetzt mit den Bedingungen (G1″), (G2\_A), (G4) in Anhang F, F.12; für kurze Brücken ist dort C′ ≤ 2500, unabhängig von D\_c. Folgerung P5′ ist durch Lemma F13 ersetzt (F.11.4, F.12.6).

**Was sich in G.12 ändert.**

- **G.12.2 (G1):** Z\_neu,k wie oben. Die Dichteformel bleibt exakt. Geprüft im Testmodell ([zeitschleife2d.py](zeitschleife2d.py), `--abweg ball`, Fehler ≤ 1,3·10⁻¹⁵); die Isolation schränkt G nur über Endpunkt-Daten weiter ein.
- **G.12.4 (G3′):** unverändert. Die Integration über das neue Stück von R summiert jetzt auch über S′ ∈ G(Y\_m) und ergibt genau Z\_neu. Die Normierer der Scheibe darunter hängen von S′ als Kopf ab; man integriert deshalb von der untersten Scheibe aufwärts, und jede Scheibe gibt 1.
- **G.12.5 (G4, G5):** Für das neue Stück ersetzt Lemma C (c) die Schranke 2/p\* aus Lemma P6. Die Treffwahrscheinlichkeit mit einem nahen Stück der anderen Schleife ist ≤ P\_{Q\_Y}(Treffer)/(c₁ p₁). Q\_Y ist eine freie Irrfahrt ab dem guten Punkt Y\_m, also gilt Lemma F13 (Anhang F, F.11.4; bis 2026-11-11: Folgerung P5′). Es deckt die Treffer bis zur Zeit δ − τ; die Treffer der zweiten Hälfte zählt man vom isolierten Anfang S′ aus, was den Faktor 2(2D\_c + 1)² kostet (F.12.6). Der Kopf S′ ist isoliert, also guter Endpunkt der Brücke j₁ der Scheibe darunter.
- **G.12.6 (G6):** G(Y\_m) hängt nur von den Linien zur Zeit t\_k im Abstand ≤ D\_c s + r von Y\_m ab, ist also lokal. Damit das neue Stück die Makro-Bedingung erfüllt, sei D ≥ D\_c + 1.
- **G.12.7 (G7), Punkt 1:** Je geteilter Kopfscheibe kostet das neue Stück höchstens 1/(c₁ p₁) (Lemma C (e)). Mit Querschritt setzt sich das Teilen je Scheibe nur mit Wahrscheinlichkeit ≤ C/m fort; der Beitrag ist ≤ 2 für m ≥ 2C/(c₁ p₁). Gegenüber dem freien Anfang kostet die Beschränkung auf den Ball zusätzlich höchstens 1/(1 − η\_c) ≤ 2 (Lemma C (b)), bei Variante a waren es bis zu 1/P(bleiben) ≤ 14.
- **C\_end:** Die Kopfdichte am unteren Ende ist ≤ C/(c₁ p₁ s²) auf ≤ (2D\_c + 1)² Zellen (Lemma C (d)), statt 1/n\_gut in einer Zelle. Beim Zurückgewinnen von µ\_ab (Anhang Z, Z.8) wird aus der Gleichheit eine Ungleichung mit dem Faktor C (2D\_c + 1)²/(c₁ p₁). Die zulässigen Endzellen-Paare verschieben sich dabei um ≤ D\_c Zellen; das ändert nur die Konstante.
- **Annahme |ν| ≥ υ/2:** unverändert. In guten Zellen enthält der Ball isolierte freie Plätze, also ist Z\_neu > 0.

**Reihenfolge der Konstanten (Anhang Z, Z.9).**

- In Schritt 2, nach A und θ (damit stehen n und p₁ fest; b₀ kommt nicht mehr vor): D\_c mit C e^{−cD\_c²} ≤ c₁ p₁/4, also D\_c² ≈ C′n/c. Danach D ≥ D\_c + 1.
- In Schritt 4 zusätzlich ζ² ≤ c₁ p₁/(4 C C\_a D\_c²).
- Dann ist η\_c ≤ ½.
- Die neue Bedingung an ζ ist exponentiell klein in n, also schärfer als die polynomiale aus Lemma P6. Für den Existenzsatz ist das gleichgültig, für die Schwelle kostet es.

**Bewertung.**

- **Existenzsatz:** Er hätte auch mit Variante a gestimmt. In beiden Varianten ist die Bedingung m ≥ C/(c₁ p₁) mit einer festen rechten Seite, und m wächst wie K ln(1/ρ).
- **Was Variante c bringt:** Sie nimmt der geteilten Kopfscheibe den Faktor 1/P(bleiben) (≤ 2 statt ≤ 14 im Vergleich zum freien Anfang). Der Faktor 1/(c₁ p₁) für das Ausweichen bleibt in jeder Variante (Lemma C (e)). Sie erklärt auch den Befund des Testmodells: Dort ist m ≤ 3, das Teilen setzt sich fast immer fort, und mit Variante a kostet jede Scheibe etwa 1/P(bleiben).
- **Ist der Querschritt noch nötig? Ja [N].** Vermutet war, dass mit Variante c der Abweg ganz ohne Route auskommt (nur Scheibe für Scheibe ein Stück mit Anfang im Ball einfügen). Das Testmodell widerlegt das (Anhang Z, Z.11, Test „nie Querschritt“). Ohne Querschritte wächst ∫f² um 1,22 je Scheibe (R = 3) und selbst mit freiem Anfang um 1,07–1,16, gleichbleibend über w, also exponentiell. Mit erlaubtem Querschritt sind es 0,99, mit Pflicht-Querschritt 1,13. Der Querschritt mischt den Kopf über die Zellen, und erst das versteckt den Weg des Abwegs ganz (Befund A). Für den Beweis bleibt es beim Querschritt in jeder Scheibe. Ein nur erlaubter Querschritt (Zug d = 0 mit Wahrscheinlichkeit p₀) ginge auch: Mit Variante c kostet eine geteilte Kopfscheibe ≤ 2, und die Reihe über die Fortsetzungen bleibt endlich, solange 2p₀² < 1.
