# Anhang Z: Das zweite Moment der Zeitschleife (nach OA §10)

Stand 2026-11-10 spät abends; Z.3 und Z.9 am 2026-11-12 an [anhang\_feinskala.md](anhang_feinskala.md) (Anhang F) angepasst, Z.0, Z.5, Z.8 und Z.9 an [anhang\_lochstueck.md](anhang_lochstueck.md) (Anhang L), Z.0, Z.3, Z.5 und Z.9 an [anhang\_unzugaenglich.md](anhang_unzugaenglich.md) (Anhang U). Ausarbeitung von Schritt G4–G7 aus [anhang\_gegenluecke.md](anhang_gegenluecke.md) G.12 für die Zeitschleife, eng nach OA §10 („Cross comparison in the slab“) der OpenAI-Arbeit „A density-uniform condensate bound for dilute Bose gases“. Die Nummern in Klammern verweisen auf OA, damit man die Formalisierung dort später wiederverwenden kann. Benutzt werden [anhang\_schleifen.md](anhang_schleifen.md) (S1–S3), [anhang\_ausweichen.md](anhang_ausweichen.md) (P3, P5, P6) und [satz\_3\_9\_dichteschranken.md](satz_3_9_dichteschranken.md) §9–§12 (Satz D). Kennzeichnung: [S] bewiesen; [S nach OA] bewiesen mit einem OA-Schritt, der samt Beweis nachgelesen und dessen Übertragung geprüft ist; [B nach OA] Beweisskizze nach dem genannten OA-Schritt, Übertragung nicht Zeile für Zeile geprüft; [B] Beweisskizze. Bis 2026-11-11 trugen auch Z.2, Z.5, Z.6 und Z.8 „[S nach OA]“ (Review W3).

## Auf einer Seite

**Satz Z (OA Proposition 10.1) [S nach OA bis auf zwei Sonderfälle an den Enden der Schleife (Anhang M, M.9.10) [B]; Kette in Z.12].** Nach Festlegung der Abschneidekonstanten (D, ε, ζ, κ, A, θ, C\_β) gibt es C < ∞ mit ∫ f² dµ ≤ C für alle hinreichend kleinen ρ und alle L ≥ L₀(ρ) = c\_L s(ρ), ohne Teilbarkeitsbedingung (Z.13; c\_L = max(16, 2R\*″ + 2), bis 2026-11-13: L ≥ 16 s(ρ)). Mit |ν| ≥ υ/2 − 5ζ² ≥ υ/4 (Z.12) folgt N₀/N ≥ υ²/(16C). Beliebige Seitenlängen über die Pflasterung in Z.13. *Bis 2026-11-13:* [B, Gerüst vollständig] und |ν| ≥ υ/2.

**Ablauf** (wie OA):

1. Je Scheibe eine Tabelle der vier Zustände C, O, Ĉ, B und die Gruppen h, d, j, l, L (Z.1).
2. Kernfaktoren nur auf d (Z.2, OA (28)).
3. Zwei Nenner-Schranken nahe Begegnungen, mit Ausweich-Untergrenzen statt Jensen (Z.3, OA (29)).
4. Wechselwirkungen in B zurückholen (Z.4, OA (29a)).
5. Nebenbedingungen verfolgen: Stabilität, Listen, gemeinsames Fern-Auswahlprodukt (Z.5, OA Lemma 10.2–10.3).
6. Integrierter Kreuzvergleich (Z.6, OA Lemma 10.4) und Defektschranke unter µ\_ab (Z.7, OA (33)).
7. Summieren über Auswahl, Routen und seltene Komponenten (Z.8, OA §10.5).

| Schritt                  | Gegenstück bei OA | was neu ist                                                                                                    | Stand                                                                                                 |
|--------------------------|-------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Z.1 Zustände und Gruppen | §10.1             | je Scheibe; Linienzahl ±1 in B; Selbstbegegnungen                                                              | [S]                                                                                                   |
| Z.2 Kernfaktoren         | (28)              | Gitterkern, Stücke mit Dauer δ                                                                                 | [S, gegeben (K1), (K2′)] (Anhang M, Lemma M8)                                                         |
| Z.3 Nenner               | (29)              | Ausweich-Untergrenzen statt Jensen                                                                             | [S, gegeben Lemma P6″, Lemma C (c), Lemma F13, Lemma M4] (Anhang M, Folgerung M6)                     |
| Z.4 Zurückholen          | (29a)             | ebenso                                                                                                         | [S] wie Z.3 (Anhang M, Folgerung M7)                                                                  |
| Z.5 Nebenbedingungen     | Lemma 10.2, 10.3  | Wählbarkeit ohne Scores, über zwei Scheiben; zwei Schwellen der Zugänglichkeit; orientierte Umwege; ℓ\_tot = 0 | Stabilität [S] (Anhang M, Lemma M4); Listen [S] (Lemma M11, M11a, M12)                                |
| Z.6 Kreuzvergleich       | Lemma 10.4        | –                                                                                                              | [S, gegeben M4, M6–M8, G3′] (Anhang M, Lemma M9)                                                      |
| Z.7 Defekte unter µ\_ab  | (33)              | über viele Scheiben (G.11.2)                                                                                   | [S]                                                                                                   |
| Z.8 Summieren            | §10.5, (34)       | Endzellen der Schleife; weiches Begegnungsmaß für Schleifen                                                    | Auswahl [S] (Anhang M, Lemma M10); Endzellen [S, gegeben Satz D] (Lemma M14a–e); Skelette [S nach OA] |

**Zum Stand „nach OA“ (Review W3).** OA hat ein beschränktes, weiches Potential, eine einzige Scheibe, eine feste Zahl von Pfaden und benutzt Jensen und Scores. Hier gibt es den harten Kern, w Scheiben, Löschen und Einfügen, zeitlich gerichtete Hälften, keine Scores, dafür Zugänglichkeit mit zwei Schwellen (Anhang U) und Wählbarkeit über zwei Scheiben (Anhang L). Die Schritte Z.2, Z.5, Z.6 und Z.8 folgen OAs Beweisen; ob sie sich Zeile für Zeile übertragen, war bis 2026-11-12 nicht geprüft. *Seit 2026-11-13* sind sie in Anhang M für dieses Modell ausgeschrieben und bewiesen (Lemma M1 bis M14e), ohne Rückgriff auf OAs Beweise; die Kette steht in Z.12. Geprüft sind zwei OA-Aussagen samt Beweis und ihre Übertragung: Proposition 7.3 (hier G.11.2 und Z.7) und Lemma 8.1 (hier Lemma S1). Weder OA noch die Hartkugel-Arbeit bei positiver Temperatur (OAH) sind in Lean formalisiert; formalisiert ist nach dem Stand des Repositories vom 2026-10-07 nur die Grundzustandsarbeit zum Hartkugelgas.

## Z.0 Ausgangspunkt: die Dichte und ihr zweites Moment (OA (26), (27))

- **Konstruktion:** wie G.12.1. Aufweg: Löschen mit Umsteigen längs der Lagen r\_0, …, r\_w aus Lemma S2. Im Aufweg wird in jeder Scheibe umgestiegen, und j\_m wird unter den Stücken mit regulärer Fortsetzung gewählt (Wählbarkeit über zwei Scheiben, Anhang L); dadurch ist das Lochstück j₀ jeder Scheibe regulär. Abweg: Spiegel-Abweg, Variante c (Anfang des neuen Stücks aus dem bedingten Gesetz im Ball vom Radius D\_c s um Y\_m, G.12.9), mit Querschritt in jeder Scheibe. Die Umsteige-Teilchen werden gleichverteilt unter den wählbaren Stücken der Zelle gewählt, mit Gewicht h\_γ(C, I) wie OA §9.2. Wählbar heißt regulär⁺ und zugänglich gegen alle anderen Stücke der Scheibe; eine zurückgehaltene Gruppe gibt es nicht (Anhang U).
- **Dichte (OA (26)):** G.12.2, exakt geprüft. Je Scheibe stehen im Nenner die Normierer Z^{br}\_k (Aufweg) und Z\_{neu,k} (Abweg) der gezogenen Stücke, im Zähler das Gewicht der alten Stücke des hypothetischen geschlossenen Zustands Ĉ und die Auswahlgewichte in Ĉ. Das Auswahlgewicht von j\_m hängt auch von der Folgescheibe ab; die Formel bleibt exakt (Anhang L, Lemma L3, am Mini-Ring geprüft).
- **Zweites Moment (OA (27)):** ∫ f² dµ = ∫ f dν. Ausgeschrieben ist das ein Integral über die geschlossenen Pfade C, die von R′ gezogenen Stücke (in O) und die hypothetischen alten Stücke von R (in Ĉ), mit den Faktoren beider Konstruktionen. Alle Integranden sind ≥ 0; Tonelli erlaubt jede Integrationsreihenfolge.

## Z.1 Die vier Zustände und die Gruppen (OA §10.1)

**Scheibenweise.** Nach Lemma 3.1 des Tutorials zerfällt das Weltlinien-Gewicht bei festen Konfigurationen an den Scheibenrändern in ein Produkt über Scheiben. Jeder Schritt der Konstruktion ändert nur Stücke seiner Scheibe. Deshalb kann man alle Vergleiche Scheibe für Scheibe führen. Die Ränder sind dabei fest, außer an den offenen Enden und am Loch bzw. Kopf, deren Lagen zu den Rückwärtsdaten gehören.

**Zustände in Scheibe k.** R′ baut O aus C, R wertet die Dichte in O aus.

| Zustand | was in Scheibe k gegenüber C geändert ist                                                        | Linien in Scheibe k |
|---------|--------------------------------------------------------------------------------------------------|---------------------|
| C       | nichts                                                                                           | N                   |
| O       | Schritte von R′: auf U′ ein Stück gelöscht und Brücken; auf D′ Brücken und ein neues Stück       | N                   |
| Ĉ       | O, dazu die Schritte von R rückgängig: auf U ein altes Stück mehr, auf D das neue Stück entfernt | N                   |
| B       | C, dazu die Schritte von R rückgängig: +1 Stück längs U, −1 Stück längs D                        | N                   |

Liegen U und D in derselben Scheibe (Schleife steil oder nahe der Wende), so stehen beide Änderungen; die Gesamtzahl bleibt N.

**Gruppen (OA (h, d, j, l, L)).** In Scheibe k sei I die Menge der Stücke, die R ändert (Brücken, neue Stücke und die zugehörigen alten Stücke), und I′ die von R′. Dann

```text
h = I ∩ I′  (geteilt),      d = h ∪ pred_I(h),      j = I \ d,      l = I′ \ h,      L = alle übrigen
```

mit pred\_I dem zyklischen Vorgänger in der Umsteigekette von R. Es gilt |d| ≤ 2|h|.

- **Begegnungen:** J zählt die Zellen der Route von R im Abstand ≤ R\* von der Route von R′ und umgekehrt, über alle Scheiben und alle vier Paarungen U–U′, D–D′, U–D′, D–U′.
- **Feste und integrierte Pfade** (wie OA): Auf j ist C = O, und B hat die alten Stücke Ĉ\_j. Auf l ist B = C, und Ĉ = O. Auf d wird B frisch gezogen. L bleibt fest.

**Lemma Z.1 (Fernkürzung, je Scheibe) [S].** Auf einer Scheibe mit h = ∅ und ohne Stück von j in Reichweite eines Stücks von l gilt die exakte Kürzung von G3′. Das gilt auch, wenn U\_R und D\_R in derselben Scheibe wirken (Selbstbegegnung).

*Beweis.* G.12.4 für jede Hälfte. Bei einer Selbstbegegnung integriert man zuerst über die neuen Stücke des Abwegs von R; das kürzt Z\_neu und lässt W(alt) stehen. Danach integriert man über die Brücken des Aufwegs, die jetzt Stücke des Zustands nach dem Rückgängigmachen des Abwegs sind; das kürzt Z^{br}. Die Reihenfolge entspricht der Zeitordnung der Konstruktion (erst Aufweg, dann Abweg) rückwärts. ∎

## Z.2 Kernfaktoren (OA (28)) [B nach OA]

*Seit 2026-11-13 bewiesen:* Lemma M8 [S, gegeben (K1), (K2′)] in [anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M.6.4, mit der Schranke (4πe^{(Λ²+1)/2})^{6|h|}, Λ = D + 2 (mit dem scharfen (K2) wäre es 4πe^{Λ²/2}). Der Text unten ist die frühere Skizze.

Man zieht von jedem Stück den freien Kern seines Endpunktpaares heraus, p\_δ(S, E) mit der Gitter-Irrfahrt. Gezogene Stücke kürzen sich gegen ihre Normierer. Übrig bleibt nur auf d

```text
K_C(d) K_Ĉ(d) / ( K_B(d) K_O(d) )  ≤  e^{C|h|}
```

denn alle beteiligten Endpunkte liegen nach Wählbarkeit und Sternnachbarschaft im Abstand ≤ (D + 10)s, und der Gitterkern ist dort nach (K1), (K2) aus Anhang P bis auf feste Faktoren gleich groß.

## Z.3 Die zwei Nenner (OA (29))

*Seit 2026-11-13 bewiesen:* Folgerung M6 [S, gegeben Lemma P6″, Lemma C (c), Lemma F13, Lemma M4] in [anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M.6.2, aus dem Vergleichslemma M5. Lemma P6″ trägt dort alle Stücke, auch die mit eigenen Endpunkten; die Randschranke über die Zugänglichkeit und die Gruppierung naher Paare werden nicht gebraucht. Konstanten: p = ½ min(p\_P, c₁p₁) statt e^{−C(K)}, σ = 2n\_R² P\_T/p statt σ\_ρ. Der Text unten ist die frühere Skizze.

Für G = j oder l sei Z[G, X] das Integral der Indikatorfunktion „die Stücke von G weichen einander und L aus“ gegen die freien Brücken mit cut, bei festem L.

**Ein-Stück-Randschranke (Ersatz für OAs Jensen-Schritt).** In den normierten Gruppengesetzen hat jedes einzelne Stück, bedingt auf alle anderen, bezüglich seiner freien Brücke die Dichte ≤ 2/p\*. Das gilt:

- für Stücke mit ihren eigenen Endpunkten in C (die Gruppe j mit den Endpunkten von C, die auf j gleich denen von O sind): Sie sind zugänglich gegen alle anderen Stücke, also gegen jede Teilfamilie, und die beschränkt vielen neu gezogenen Stücke in Reichweite kosten höchstens n′ P^{br}\_treff ≤ p\*/2 (Anhang U, Lemma U4 (3));
- für umgehängte Brücken und neue Stücke (die Gruppe l mit den Endpunkten von O, und j in B): Anhang P, Lemma P6, wenn die Zellen ihrer Endpunkte brauchbar sind und die Endpunkte isoliert. Die Gütebedingungen (G1″), (G2\_A), (G4) im Kasten um die Brücke gelten dann in jedem Zustand, der sich in höchstens n″ regulären Stücken unterscheidet (Klausel (v), Lemma M4 (3), [anhang\_buchfuehrung.md](anhang_buchfuehrung.md)). Bis 2026-11-12 stand hier „wenn die Zellen ihrer Endpunkte nicht defekt sind“; das deckt die Zellen der Route nicht.

**Lemma Z.3 [B, gegeben P3, P6].**

```text
Z_{I′}(O)  ≥  Z[l, O] · exp( −C(K)|h| − σ_ρ J )
Z_I(O)     ≥  Z[j, C] · exp( −C(K)|h| − σ_ρ J ),        C(K) = δμ̄ + κ + C,   σ_ρ = C e^{δμ̄+κ} P_treff → 0
```

*Beweis* (wie OA, Jensen ersetzt durch die Randschranke und die Vereinigungsschranke).

1. **Erste Ungleichung.** Ziehe l aus seinem normierten Gruppengesetz und h unabhängig als freie Brücken mit cut. Der Quotient zu Z[l, O] ist das Produkt der cut-Wahrscheinlichkeiten auf h mal der Wahrscheinlichkeit, dass keine der fehlenden Stoßarten eintritt: l gegen das feste j, l gegen d \ h, h gegen alles.
2. **l gegen j:** Die Endpunkte sind getrennt (Wählbarkeit), in den Randintervallen bleiben die Stücke in ihren kleinen Kugeln, und danach trifft ein l-Stück ein festes j-Stück mit Wahrscheinlichkeit ≤ (2/p\*) P\_treff. Es gibt höchstens C(R) J solche Paare. Fasst man nahe Paare zu räumlich getrennten Gruppen zusammen, gibt die Vereinigungsschranke je Gruppe 1 − σ\_ρ · (Gruppengröße) ≥ e^{−2σ\_ρ·(Gruppengröße)}.
3. **h und d \ h:** Je Stück eine Ausweich-Untergrenze p\*/2 (Lemma P6 bzw. Lemma U4), zusammen e^{−C(K)|h|}.
4. **Zweite Ungleichung:** ebenso, mit j aus seinem Gruppengesetz und d als freie Brücken; das feste Gegenüber ist l. ∎

## Z.4 Wechselwirkungen in B zurückholen (OA (29a)) [B]

*Seit 2026-11-13 bewiesen:* Folgerung M7 in [anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M.6.3, mit p^{−|d|} e^{σJ\_k} als Faktor. Der Text unten ist die frühere Skizze.

jn ⊆ j seien die Stücke, deren Endzelle höchstens 2R + 5 von einer Zelle von l entfernt ist; nur sie können wegen cut ein Stück von l treffen.

| Rolle                       | Pfade                                 |
|-----------------------------|---------------------------------------|
| fest in beiden Integralen   | L, B\_l = C\_l, B\_{j\jn} = Ĉ\_{j\jn} |
| integriert im Original      | Ĉ\_jn, C\_j, O\_l, C\_d, Ĉ\_d, O\_h   |
| integriert im Bezugszustand | B\_jn, B\_d                           |

```text
∫ 1_cut(jn) 1{jn weicht j\jn und L aus} dπ_jn  ≤  e^{C(K)|h| + σ_ρ J} · ∫ 1_cut(jn) 1_cut(d) 1{alle Paare außer L–L weichen aus} dπ_jn dπ_d
```

*Beweis.* Wie Lemma Z.3: jn aus seinem Gruppengesetz mit festem j \ jn, d unabhängig als freie Brücken mit cut. Die fehlenden Stoßarten sind jn gegen l (Vereinigungsschranke, σ\_ρ J) und alles, was d betrifft (Ausweich-Untergrenzen, C(K)|d| ≤ 2C(K)|h|). Die Randschranke gilt auch für die teilweise festgehaltene Gruppe, denn nur beschränkt viele feste oder integrierte j-Stücke liegen in Reichweite. ∎

## Z.5 Nebenbedingungen verfolgen (OA §10.4) [B nach OA]

**Zählweise in B.** Die Zählung n\_Q(B) folgt den Stück-Enden in B: längs U\_R eins mehr, längs D\_R eins weniger als in C. Die beiden Stücke an den offenen Enden von B (Kopf in a, Schwanz in b) werden mitgezählt, aber für nicht wählbar erklärt (OAs Ausnahme-Slot e). S₀(B) sind die unbrauchbaren Zellen von B, S₁(B) ⊇ S₀(B) die mit dem strengeren Anteil 1 − ε/2 bei gleichem Zählintervall.

| Menge             | Zählintervall      | Ausfallanteil | Isolation, Makro, Rand, Regularität                           | Schwelle der Zugänglichkeit |
|-------------------|--------------------|---------------|---------------------------------------------------------------|-----------------------------|
| S(C), S(Ĉ), S₀(B) | [b₋m, b₊m]         | > ε           | wie G.12.1, dazu Klausel (v) mit N\* − n″                     | p\*                         |
| S₁(B)             | [b₋m + 2, b₊m − 2] | > ε/2         | dieselben Tests, (G1″) mit N\* − 2n″                          | 2p\*                        |
| defekt (Satz D)   | [2b₋m, b₊m/2]      | ≥ ε/4         | dieselben Tests, mit tatsächlichen Enden, (G1″) mit N\* − 3n″ | 2p\*                        |

**Lemma Z.5 (Stabilität, OA Lemma 10.2) [B nach OA; ersetzt durch Lemma M4, [S, gegeben Lemma U4], Anhang M].** Für jede Ersetzung von B\_jn, B\_d mit cut und jeden Zeugen (C, Ĉ) gilt S(C), S(Ĉ) ⊆ S₁(B). Im Abstand > R\* von der Route von R gilt S(C) = S₀(B), im Abstand > R\* von der Route von R′ gilt S(Ĉ) = S₀(B), samt aller einzelnen Wählbarkeiten.

*Beweis* (wie OA, ohne den Score-Teil).

- C unterscheidet sich von B nur auf den Stücken von R, Ĉ nur auf l, d, jn. Alle geänderten Stücke erfüllen cut und liegen nahe den beiden Routen.
- Die Isolation ungeänderter Anfänge und Enden ändert sich nur bei beschränkt vielen Stücken je Zelle. Die Ausweichwahrscheinlichkeit a\_i eines ungeänderten Stücks ändert sich nur, wenn ein geändertes Stück in seiner Reichweite liegt, und dann um höchstens n′ P^{br}\_treff ≤ p\*; n′ ≤ C(R\*) ist die Zahl der geänderten Stücke in Reichweite (Anhang U, Lemma U4). Das kann viele Stücke einer Zelle betreffen. Deshalb prüft S₁(B) die Zugänglichkeit mit der Schwelle 2p\*: Ein in B streng zugängliches Stück ist in jedem Zeugen zugänglich. (Bis 2026-11-11 stand hier, die Zugänglichkeit ändere sich nur bei beschränkt vielen Stücken je Zelle. Das galt für die Fassung mit zurückgehaltener Gruppe.)
- Die Zählung ändert sich um höchstens 1.
- Also ist die wählbare Anzahl im Zeugen ≥ (1 − ε/2)n\_Q − C ≥ (1 − ε)n\_Q für großes m.
- Fern von den geänderten Stücken ist alles gleich. ∎

**Listen (OA Lemma 10.3) [B nach OA; seit 2026-11-13 Lemma M11 und M12, [S, gegeben Lemma S2 und M4], Anhang M, M.8].** Dort sind es ≤ e^{4b\_tot} Routenpaare und J ≤ C\_J(J₀″ + b\_tot), mit b\_tot aus Klumpen am Skelett und den Komponenten auf *einer* Strecke je Scheibe. Der Text dieses Absatzes ist die frühere Skizze. Man zerlegt S₁(B) in Komponenten im Nachbarschaftsabstand K\_b = 2R\* + 10. *Brücken-Komponenten* liegen im Abstand ≤ R\* + 2 von beiden Skeletten (als Raum-Zeit-Mengen); b\_tot ist ihre Gesamtgröße. Für jede Route rät man auf Brücken-Komponenten die schlechte Teilmenge, auf den übrigen nimmt man den Schnitt mit S₀(B). Dann führt man die orientierte Umweg-Konstruktion (Lemma S2) aus.

- Jeder Zeuge steht auf der Liste: Lemma S2 (4) (Lokalität) ersetzt OAs „deletion invariance“ in Lemma 8.2.
- Es gibt höchstens 4^{b\_tot} Paare, und für jedes gilt J ≤ J₀ + C(R\*) b\_tot.
- **Kein Zusatzterm ℓ\_tot:** Das Lochstück j₀ ist in jedem Zeugen regulär, weil j\_m der Scheibe davor nur unter Stücken mit regulärer Fortsetzung gewählt wird (Anhang L, Lemma L1). Es endet höchstens D + 1 Zellen von r\_k. (Bis 2026-11-11 stand hier als Grund „j₀ beginnt in einer guten Zelle“ und D4; das reicht nicht, Review K3.)

**Gemeinsames Fern-Auswahlprodukt (OA).** Die Auswahlfaktoren der fernen Vorkommen, in B ausgewertet, haben nach Lemma Z.5 für alle Zeugen und alle Ersetzungen denselben Wert H\*. Für nahe Vorkommen schätzt man den Auswahlfaktor durch [(1 − 2ε)n\_Q]^{−1} ab (Lemma L2). Ein Vorkommen von j\_m im Aufweg ist auch dann nah, wenn die Begegnung in der Folgescheibe liegt; mit dem um 2D + 4 vergrößerten R\* sind alle übrigen Vorkommen fern im bisherigen Sinn (Anhang L, L.5).

## Z.6 Integrierter Kreuzvergleich (OA Lemma 10.4) [B nach OA, gegeben Z.3, Z.4]

*Seit 2026-11-13 bewiesen:* Lemma M9 [S, gegeben Lemma M4, M6–M8 und G3′] in [anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M.7.1, mit dem Faktor [(1 − 2ε)(n\_c(B) − 2)]^{−1} je nahem Vorkommen und 1\_G als Verträglichkeit. Der Text unten ist die frühere Skizze.

Für feste Routen, Tupel, Skelette und Endpunktdaten sei I\_{I,I′} das Integral eines Summanden des zweiten Moments. Dann gilt

```text
I_{I,I′}  ≤  e^{C(K)|h| + σ_ρ J} · 1_occ · Π_{nahe Vorkommen in Q} [(1 − 2ε) n_Q]^{−1} · ∫ W(B) 1_G H_F(B)
```

*Beweis* wörtlich wie OA: auf jeder zulässigen Faser mit Z.2–Z.5, das gemeinsame Fern-Auswahlprodukt vor dem Weglassen der Nebenbedingungen herausziehen, auf unzulässigen Fasern ist der Beitrag 0.

## Z.7 Defekte unter dem Bezugsmaß (OA (33)) [S]

Für jede vorgegebene Menge U von Raum-Zeit-Zellen gilt

```text
µ_ab( U ⊆ S₁(B) )  ≤  C M^{−2} q^{|U|/4}
```

*Beweis.* S₁(B) wird mit der Ausnahme-Konvention gezählt. Ersetzt man an den beiden offenen Enden das Ausnahme-Ende durch das tatsächliche, ändern sich Zählungen um höchstens 1 und nur beschränkt viele Isolationsflaggen (Packung). Also ist jede Zelle von S₁(B) defekt im Sinn von Satz D (Ausfallanteil ≥ ε/4 für großes m). Satz D, zweite Zeile, gibt die Behauptung; das ist die Übertragung aus G.11.2 für Ereignisse über alle Scheiben der Schleife.

## Z.8 Summieren (OA §10.5)

**Auswahl summieren [B nach OA; seit 2026-11-13 Lemma M10, [S, gegeben Lemma M9], Anhang M, M.7.2].** Dort zählt J die nahen Vorkommen, und κ₀ = 3ε + 6σ + (e^{2C(K)} + 4)/(b₋m − 4) je Vorkommen; die Bedingung lautet κ₀ ≤ α\_J = α(R\*″)/(4C\_J) (Anhang M, M.8.4). Der Text dieses Absatzes ist die frühere Skizze. Man summiert Z.6 über die Tupel bei festem B. Ferne Vorkommen kosten ≤ 1, nahe je (1 − 2ε)^{−1}; je Begegnung gibt es höchstens zwei nahe Vorkommen je Route (Anhang L, L.5), zusammen also ≤ (1 − 2ε)^{−4} ≤ e^{10ε}. Dazu kommen die zellweisen Summen:

| Zelle                          | Wahl                                                      | Schranke                       |
|--------------------------------|-----------------------------------------------------------|--------------------------------|
| gewöhnliche gemeinsame Zelle Q | zwei unabhängige Teilchen                                 | 1 + (e^{C(K)} − 1)/n\_Q        |
| erste Zelle a (Schwanz)        | ein gemeinsames Teilchen, der Schwanz x                   | e^{C(K)}/n\_a                  |
| letzte Zelle b (Kopf)          | gemeinsames unterstes neues Stück ab y; ein Teilchen j\_m | [1 + (e^{C(K)} − 1)/n\_b]/n\_b |

Die Endzellen-Summen kosten zusätzlich das Teilen des Kopfstücks über weitere Scheiben. Mit Querschritt in jeder Scheibe setzt es sich je Scheibe nur mit Wahrscheinlichkeit ≤ C/m fort. Je geteilter Scheibe kostet das neue Stück höchstens 1/(c₁ p₁) (Lemma C (e), G.12.9: Der Kehrwert des Normierers bleibt stehen), also zusammen ein Faktor ≤ 1/(1 − C/(c₁ p₁ m)) ≤ 2 für m ≥ 2C/(c₁ p₁). (Bis 2026-11-12 stand hier ≤ 2 je Scheibe und m ≥ 4C; das war die Rechnung für ein Teilchen, Review W1.) *Nachtrag 2026-11-13 (Anhang M, M.9.6):* Bei k ≥ 1 übereinstimmenden verdeckten Kopflagen liegt der Schnitt des Bezugszustands B zur Zeit t\_k, und B hat auf [0, t\_k) N + 1 Linien. Das Bezugsmaß µ\_ab^{(k)} behält trotzdem die Defekt-Kleinheit in allen Scheiben (Lemma M14b [S, gegeben Satz D für N und N + 1 Teilchen]), weil Satz D ein Produkt von Operatornormen je Scheibe ist. Die Reihe über k ist ≤ 2 für (1 − 2ε)(b₋m − 2) c₁p₁ ≥ 4e^{2C(K)}. Auch am Schwanz kann sich das Teilen fortsetzen (übereinstimmende verdeckte Lochplätze); jede solche Scheibe kostet einen Kern C/s², die Reihe ist also ebenfalls beschränkt (Anhang M, M.9.7). Die Schritte von Lemma M9 für die Endscheiben stehen als Lemma M14d in Anhang M, M.9.8 [S, gegeben Lemma M4 bis M8, Lemma C und P6″]. Mit n\_Q ≥ b₋m folgt je Tupelpaar

```text
≤  C/(n_a n_b) · e^{κ₀ J},        κ₀  =  10ε + σ_ρ + (e^{C(K)} − 1)/(b₋ m)        (bis 2026-11-11: 2ε)
```

*Veraltet (Review 2026-11-13, H3):* Gültig ist κ₀ = 3ε + 6σ + (e^{2C(K)} + 4)/(b₋m − 4) mit der Bedingung κ₀ ≤ α\_J (Anhang M, M.7.2 und M.8.4); J zählt dort die nahen Vorkommen.

und nach den Listen ≤ C/(n\_a n\_b) · e^{κ₀ J₀ + C′ b\_tot}.

**Bezugsmaß zurückgewinnen [B nach OA, mit Lemma C (d)]** (Stand und Restsatz M14 in [anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M.9; seit 2026-11-13 dort bewiesen, M.9.5 bis M.9.9, gegeben Satz D und die Lemmata von Anhang M; „C/M²“ in Z.7 und hier ist mit M\_Z = M/s², der Zahl der Zellen, zu lesen)**.** Der Vorfaktor M aus der Dichte und die Gewichte 1/n\_a und 1/n\_b ergeben zusammen mit der Verteilung des Kopfes µ\_ab, mit Schwanz in a und Kopf in b wie in der Tabelle oben, wie m/(m²M) = 1/N bei OA. Benennung einheitlich wie in G.11.2 und Anhang M: µ\_ab hat die Erzeugung (den Kopf von B) in a und die Vernichtung (den Schwanz von B) in b; a ist die Zelle des Schwanzes von O, b die seines Kopfes (Review H8). Bei Variante a war der Kopf in seiner Zelle gleichverteilt, und es galt Gleichheit. Bei Variante c hat der Kopf die Dichte ≤ C/(c₁ p₁ s²) auf den ≤ (2D\_c + 1)² Zellen im Ball um Y\_m (Lemma C (d)). Man summiert über diese Zellen b′ und erhält eine Ungleichung mit µ\_{ab′} und dem Faktor C (2D\_c + 1)²/(c₁ p₁). Die zulässigen Endzellen-Paare verschieben sich dabei um ≤ D\_c Zellen; das ändert nur die Konstante. Also

```text
∫ f² dµ  ≤  C Σ_{(a,b) zulässig} E_{γ,γ′}[ e^{κ₀ J₀} ∫ e^{C′ b_tot} dµ_ab ]        (OA (34))
```

**Seltene Komponenten [B nach OA, gegeben Z.7; seit 2026-11-13 Lemma M13, [S, gegeben Z.7], Anhang M, M.8.3].** Der Text dieses Absatzes ist die frühere Skizze. Wie OA: Man entwickelt das Produkt über die Brücken-Komponenten mit Faktoren 1 + (e^{C′|T|} − 1). Jede zulässige Sammlung disjunkter zusammenhängender Mengen T, die beiden Skeletten nahe liegt, hat nach Z.7 das Gewicht ≤ C M^{−2} Π (e^{C′} q^{1/4})^{|T|}. Wurzelt man die Mengen an Skelettpunkten, folgt

```text
∫ e^{C′ b_tot} dµ_ab  ≤  C M^{−2} exp( ϑ(q) S_{K_b} ),        ϑ(q) → 0 für q → 0
```

mit dem weichen Begegnungsmaß S\_{K\_b} = Σ\_{z∈γ} e^{−d(z,γ′)/K\_b} der beiden Skelette.

**Skelette [S nach OA].** Lemma S1 gibt E e^{θJ₀} ≤ C für θ < α. Dasselbe gilt für das weiche Maß: E e^{ξ S\_{K\_b}} ≤ C(K\_b) für ξ klein (OA (25)); der Beweis von Lemma S1 deckt mit dem Test X\_u = e^{−|Z\_u − Z′\_u + s|/(CK\_b)} auch diesen Fall, mit den festen Verschiebungen s ∈ {0, ±s\_u}. Hölder trennt die beiden Faktoren.

**Schluss** (ausgeschrieben in Anhang M, M.8.4, bis auf die Endzellen und das Bezugsmaß; dort lautet die Bedingung κ₀ ≤ α\_J)**.** Ist κ₀ ≤ α/2 und ϑ(q) ≤ ξ/2, so ist die Summe über zulässige Paare (a, b) mit ihrem Gewicht ≤ C, also ∫ f² dµ ≤ C. Alle Konstanten hängen nur von K, D, ε, ζ, κ, A, θ, C\_β ab, nicht von L, N oder ρ. ∎

## Z.9 Reihenfolge der Konstanten

1. K (Zellen, Satz 3.9) und daraus μ̄δ ≈ 8πK.
2. A ≈ 6–8 (Regularität), also C\_P und ε\_P; dann θ ≤ θ\_P(ε\_P) und n = K/θ (Anhang F, F.10.4 und F.12.6). θ hängt weder von einer Dichtekonstanten C₀ noch von b₀ ab; beide kommen nicht mehr vor. Mit n steht p₁ = ½ e^{−C′(n+1)} für kurze Brücken fest (C′ ≤ 4900 mit (K2′); bis 2026-11-13: 2500); dann D\_c mit C e^{−cD\_c²} ≤ c₁ p₁/4 (Ball des Abwegs, G.12.9), also D\_c² ≈ C′n/c, und D ≥ D\_c + 1 mit D² ≳ 32πK/κ (Satz T2). Danach λ₁, p\* und der Kastenradius D\_K für allgemeine Brücken (F.12.6). Dann der cut-Radius R mit η\_R ≤ min(p\_P, c₁p₁)/4, also R − (D + 2) ≳ (C′n)^{1/2} (Bedingung (B1), Anhang M, M.6.5).
3. ε klein gegen α\_J/6 (Auswahl je nahem Vorkommen, κ₀ = 3ε + 6σ + …, Anhang M, M.7.2, mit α\_J = α(R\*″)/(4C\_J), C\_J = 12D + 138 (bis 2026-11-13 abends 12D + 90, Anhang S, W2 des Reviews) und R\*″ = R\* + D′ + 1 + 2(Δ + D + 9), M.8.2 und M.8.4; bis 2026-11-13: α/40 mit J als Zahl der Begegnungen; bis 2026-11-11: α/8). Danach κ = κ\_U = ln(48 e⁶ C\_a (2D + 7)²/(ε b₋)) für die Zugänglichkeit (Anhang U, U.5), also p\* = e^{−δμ̄−κ\_U} und C(K) = δμ̄ + κ\_U + C. Eine Gruppengröße M gibt es nicht mehr (bis 2026-11-11: M groß, 2^M e^{−κεM} klein).
4. ζ klein, abhängig von ε, b₋, D und n = K/θ (Isolation, getrennt gezählt: ζ² ≤ εb₋/(768 (2D + 3)² C\_iso), Anhang L, Klausel (iii); Lemma P6: ζ² ≲ (208n)^{−117}, Anhang F, F.12.6), dazu ζ² ≤ c₁ p₁/(4 C C\_a D\_c²) (Lemma C (a), damit η\_c ≤ ½). Die letzte Bedingung ist exponentiell klein in n; für die Existenz gleichgültig, für die Schwelle teuer.
5. R\* = Δ + D\_K + R + 2D + 6 (Anhang M, M4: deckt alle Reichweiten, auch die Kästen vom Radius D\_K s und die Wählbarkeit über zwei Scheiben) und R\*″ = R\* + D′ + 1 + 2(Δ + D + 9) (M.8.2); dann α = α(R\*″) aus Lemma S1 und ξ für das weiche Maß. (K\_b = 2R\* + 10 aus der früheren Fassung wird in Anhang M nicht mehr benutzt; Komponenten sind Kanten-Komponenten, das weiche Maß ist S mit e^{−d/7}, M.8.3.) **Rückkopplung (Review 2026-11-13, H2).** α hängt über R\*″ von D ab, und ε aus Schritt 3 von α: D → γ\_n = 2^{1/2}(D + 10)/n^{1/2} → C′ = 9,3(1 + 520 e^{1,75γ\_n²}) → p\_P → R (Bedingung (B1), R − Λ ≳ (C′n)^{1/2}) → R\*″ → α → ε. Für die Rate von D4 braucht man weiter D² ≳ ln(C\_a/(b₋ε))/κ (satz\_3\_9 §8.5). Bis 2026-11-13 stand hier, das vertrage sich, „weil sie in ε nur logarithmisch ist“; das reicht nicht, denn ε ist selbst exponentiell klein in D²/n. Richtig ist: ln R\*″ = 0,875 γ\_n² + O(ln n) = 1,75 (D + 10)²/n + O(ln n), also ln(1/ε) = 2 ln R\*″ + O(ln D) ≤ 3,5 (D + 10)²/n + O(ln n), und die Bedingung lautet D² ≳ 3,5 (D + 10)²/(nκ) + O(ln n)/κ. Sie ist für großes D erfüllbar, sobald **nκ ≥ 8**: Dann ist die rechte Seite ≤ 0,44 (D + 10)² + O(ln n)/κ ≤ D² für D ≥ 40 + O((ln n/κ)^{1/2}). Wegen n ≥ 10⁵ (F.12.1) gilt nκ ≥ 8 für jedes κ ≥ 10⁻⁴; hier ist κ = κ\_U ≥ 1. Der Kreis schließt sich also, aber aus diesem Grund. **r\_∗ (Review H2 (b)).** Die Konstante r\_∗ des Randfachs ∗ in Satz T2 (Z.12) wird nach ε gewählt: r\_∗ ≳ 64πK (Satz T2) und C C\_a e^{−r\_∗/2} D² ≤ εb₋ (Rate von D4). r ≥ 20 r\_∗ gilt dann für kleines ρ; τ₀ = r²/(440 r\_∗) kommt nur in Test 3 vor, also entsteht kein weiterer Kreis.
6. C\_β ≥ 500 (Satz F11; seit 2026-11-13 wegen der Besucher eines Kastens, satz\_3\_9 §10.8: bisher 300). Die Schwelle β = C\_β ln ln(1/ρ) wächst langsam mit ρ, geht aber nur in Terme o(ln(1/ρ)) und in die Defektraten ein.
7. Zuletzt ρ klein: σ\_ρ, 1/m, q → 0, c(A) ln τ ≳ 32πK, ln ln(1/ρ) ≳ 96πK/(C\_β/71 − 1). Aus Anhang M (Stand 2026-11-14, Review H3): (a) κ₀ = 3ε + 6σ + (e^{2C(K)} + 4)/(b₋m − 4) ≤ α\_J (M.8.4), mit 3ε ≤ α\_J/2 aus Schritt 3; (b) η = e^{2C′(K)}/((1 − 2ε)(b₋m − 2)) ≤ 1/4 für die geteilten Kopfscheiben (M.9.8; die Form mit C(K) und c₁p₁ in M.9.6 ist darin enthalten, weil p ≤ c₁p₁/2, und m ≥ 2C/(c₁p₁) aus Z.8 ebenso); (c) C e^{C′(K)} e^{δμ̄} ≤ s²/2 für den späten Anfang am Schwanz (M.9.11; bis 2026-11-13: s² ≥ 2C e^{2C′(K)}); (d) q klein genug für Lemma M13 mit C₂ ≤ 4 + κ₀C\_J + 7 + 7 ≤ 19 (Schnittzelle M14e und Erzeugungszelle M.9.11). Dabei sind C(K) = 6 ln(4πe^{(Λ²+1)/2}) + 5 ln(1/p), C′(K) = 8 ln(4πe^{(Λ²+1)/2}) + 7 ln(1/p) und Λ = (9/8)(D + 4) (Lemma M14f). Für die Sonderfälle in M.9.10 [B] käme η ≤ e^{−C″(K)} hinzu.

**Was fest ist und was mit ρ wächst (Review W4).** Fest heißt: unabhängig von ρ, L und N, in der Reihenfolge oben gewählt.

| feste Größe                    | Bedeutung                                                         | bestimmt durch                                   |
|--------------------------------|-------------------------------------------------------------------|--------------------------------------------------|
| K, H; K\_F = 17                | Zellbesetzung m = K ln(1/ρ); Kastenseite 1/b² = Hρ; Lokalisierung | Dichteschranken (satz\_3\_9 §3, §11)             |
| C\_a, b₋, b₊, C\_E             | Dichtekonstanten                                                  | K, H                                             |
| A; C\_P, C\_b, ε\_P            | Regularität; Konstanten von Lemma P5″ und P6a                     | Lemma R; Anhang F                                |
| θ, n = K/θ                     | Teilintervall τ = θ ln(1/ρ)/ρ und ihre Zahl je Scheibe            | θ ≤ θ\_P(ε\_P)                                   |
| p₁, D\_c, D                    | kurze Brücken, Ball des Abwegs, Makro-Radius                      | n (G.12.9)                                       |
| λ₁, j₁, J, C′, D\_K, m\_D, m₄  | Lemma P6 für allgemeine Brücken; Kasten des Defekts               | n, D (F.12.6)                                    |
| R\*, R\*″, α, ξ                | Begegnungsradien, Budget der Skelette (K\_b nicht mehr benutzt)   | D, D\_K (Anhang M, M4; Lemma S1)                 |
| ε, ε₁                          | Ausfallanteile                                                    | ε ≤ α\_J/6; ε₁ = ε/(12 (2D + 3)²)                |
| κ\_U, p\* = e^{−δμ̄−κ\_U}, C(K) | Zugänglichkeit; δμ̄ → 8πK ist beschränkt                           | D, ε (Anhang U)                                  |
| ζ                              | Isolationsradius r = ζ ρ^{−1/2}                                   | ε, D, n (Schritt 4)                              |
| C\_β                           | Kurzzeit-Schwelle                                                 | ≥ 500 (Satz F11; Folgerung T6, satz\_3\_9 §10.8) |

| Größe, die von ρ abhängt                       | Verhalten für ρ → 0                             | wo sie eingeht                                                                                |
|------------------------------------------------|-------------------------------------------------|-----------------------------------------------------------------------------------------------|
| m = K ln(1/ρ)                                  | → ∞                                             | Zellbesetzung; Kosten geteilter Teilchen (e^{C(K)} − 1)/(b₋m)                                 |
| s, δ = s², τ, r, b                             | Skalen, wachsen wie ρ^{−1/2} bzw. ρ^{−1}        | überall; nur Verhältnisse zählen                                                              |
| β = C\_β ln ln(1/ρ)                            | → ∞, langsam                                    | t\_r = r²/(16β); nur in Termen o(ln(1/ρ)) von 𝔏 und in den Raten q₁, q₄                       |
| N\_g = 16βK ln(1/ρ)/ζ², N\_trip ≲ β (ln(1/ρ))² | → ∞                                             | Zahl der Fenster und Tripel je Zelle; stehen gegen e^{−β/71} und exp(−c\_q (ln(1/ρ))^{1/4}/β) |
| P\_treff, P^{br}\_treff                        | ~ ln ln(1/ρ)/ln(1/ρ) → 0                        | σ\_ρ; Entkopplung (Lemma U1); zwei Schwellen (Lemma U4)                                       |
| k₀ ~ p\* ln(1/ρ)/ln ln(1/ρ)                    | → ∞                                             | Rate von D5: e^{−k₀}                                                                          |
| σ\_ρ = C e^{δμ̄+κ\_U} P\_treff                  | → 0                                             | κ₀                                                                                            |
| Raten D1, D4; D2; D7 mit (G2)                  | e^{−cm}; e^{−cζK (ln(1/ρ))^{1/2}}; Potenz von ρ | q                                                                                             |
| Raten D5; D6; D7 mit (G4)                      | e^{−k₀}; q₁^{1/(4m\_D²)}; q₄^{1/(4m₄²)}         | q; die letzten beiden gehen sehr langsam gegen 0                                              |
| q = 7 · max (Rate)^{1/7}, ϑ(q)                 | → 0                                             | Summe über seltene Komponenten (Z.8)                                                          |
| κ₀ = 3ε + 6σ + (e^{2C(K)} + 4)/(b₋m − 4)       | → 3ε                                            | Bedingung κ₀ ≤ α\_J (M.8.4)                                                                   |

**Die Bedingungen des Beweises mit diesen Abhängigkeiten.**

1. **κ₀ ≤ α\_J** (bis 2026-11-13: κ₀ = 10ε + σ\_ρ + … ≤ α/2). Der feste Anteil ist 3ε ≤ α\_J/2 nach der Wahl von ε. Die beiden anderen Summanden gehen gegen 0 (σ = 12 n\_loc P\_T/p wie σ\_ρ): σ\_ρ wie ln ln(1/ρ)/ln(1/ρ) mit dem festen Vorfaktor C e^{δμ̄+κ\_U}, der letzte wie 1/ln(1/ρ) mit dem festen Vorfaktor (e^{C(K)} − 1)/(b₋K).
2. **ϑ(q) ≤ ξ/2.** q geht gegen 0, weil jede Ein-Grund-Rate es tut. Am langsamsten sind D6 und D7 mit (G4); ihre Exponenten 1/(4m\_D²) und 1/(4m₄²) sind fest, aber winzig.
3. **Bedingungen der Form „alle Objekte im Kasten erfüllen …“.** Ein Kasten enthält ~ D\_K² m → ∞ Linien, also muss die Einzelwahrscheinlichkeit mit ρ verschwinden. Das ist der Fall bei (G2\_A) (Potenz von ρ je Linie), bei (G4′) (p₄ → 0 wegen C\_β ≥ 500; bis 2026-11-13: 300) und bei (G1″) (je Tripel exp(−c\_q (ln(1/ρ))^{1/4}/β)). Alle übrigen Tests sind Anteilsbedingungen (Isolation, Fehlgänger, Zugänglichkeit) oder werden durch die Auswahl gesichert (Lochstück, Anhang L); „kein Fehlgänger im Kasten“ wird nirgends verlangt.
4. **Nichts im Exponenten wächst.** θ, n, p₁, C′, λ₁, κ\_U und damit p\* und C(K) sind fest. Mit ρ wachsen nur β und k₀. β steht nur in Termen o(ln(1/ρ)) und in Defektraten, und ein größeres k₀ verbessert die Rate von D5. Die Größe b₀, die in der Fassung bis 2026-11-11 wie log₂ ln ln(1/ρ) wachsen musste und trotzdem als fest behandelt wurde, kommt nicht mehr vor (Anhang F).

## Z.10 Was offen bleibt

- **Review vom 2026-11-11** ([review\_2026-11-11.md](review_2026-11-11.md)): K1 (Gütebedingungen unterhalb der Zellskala) ist in Anhang F beantwortet und am 2026-11-12 hier eingearbeitet. K3 (Lochstück j₀, gute Endpunkte) ist in Anhang L beantwortet und ebenfalls eingearbeitet. K2 (Satz P3 nur für feste Marken) und W2 (Gruppe gegen Kosten 1/n\_Q) sind in Anhang U beantwortet und eingearbeitet: keine zurückgehaltene Gruppe, Zugänglichkeit gegen alle anderen Stücke, zwei Schwellen in der Stabilität. W3 (Kennzeichnung „nach OA“), W4 (Tabelle in Z.9) und W7 (Satz für L ≥ 16 s) sind ebenfalls erledigt. W1 ist erledigt: Eine geteilte Kopfscheibe kostet höchstens 1/(c₁ p₁) (Lemma C (e), G.12.9), und die Verdickung in Anhang S ist D′ = 2D + 2. W5 ist am 2026-11-13 erledigt: λ\_min(b) ≥ π/(2b² (ln b + 3,6)) für alle b (Tutorial Lemma 6.3a). W6 ist ebenfalls am 2026-11-13 erledigt: Einfügen im Dirichlet-Quadrat und glatte Innenzahl ([anhang\_einfuegen.md](anhang_einfuegen.md), Anhang E); b₋ ist dabei etwa 6- bis 8-mal kleiner geworden und geht hier nur als feste positive Konstante ein.
- **Buchführung, Teil 1 (2026-11-13)** in [anhang\_buchfuehrung.md](anhang_buchfuehrung.md) (Anhang M): Inventar der Tests; vier Korrekturen (Kastenbedingungen als Klausel (v) der Brauchbarkeit, gezogene Stücke regulär, Stufen für (G1″) und Zählintervall, R\* explizit); Lemma M4 (Stabilität) [S, gegeben Lemma U4] ersetzt Lemma Z.5. Offen: Z.2–Z.4, Z.6, Z.8 ausschreiben, Listen; in Satz D der Grund D4 für Stücke, die einen Kasten nur durchlaufen.
- ~~Lemma P6 in den Einzelheiten~~: erledigt (Anhang P, P.7.5: P6a, P6b, keine Rekursion nötig, ζ polynomial klein in n).
- ~~Literatur-Eingänge~~: erledigt in [anhang\_kern.md](anhang_kern.md): (K1), (K2) mit expliziten Konstanten (bis auf Standard-Bessel-Ungleichungen), Brückenmaximum K3, Schlauch K4; Lemma S1 braucht keine Literatur.
- ~~Seltenheit der Regularitätsverletzung~~: erledigt, Lemma R in [anhang\_kern.md](anhang_kern.md).
- ~~**Numerische Prüfung der Ausbeute** mit Variante a~~ erledigt in Z.11 (Ergebnis: Variante c ersetzt Variante a). Zur Geschichte: Prüfung mit Variante a an einem System mit vielen Teilchen je Zelle. Stand 2026-11-10: Monte-Carlo-Programm [pruef\_zeitschleife\_mc.py](pruef_zeitschleife_mc.py) gegen exakte Werte geprüft; im Testmodell (eine Scheibe = ein Trotter-Schritt) wird aber fast alles verworfen, weil Brücken die Nachbarzelle nicht erreichen. Auch mit Scheiben aus 4 Halbschritten und Zellen aus 3 Plätzen (Ring mit 12 Plätzen) beherrschen Verwerfungen alles. Aussagekräftig wird der Test erst mit einer Konstruktion ohne Verwerfung (die Umwege nachgebildet: Züge nur unter den ausführbaren, normiert und in der Dichteformel mitgeführt) und langen Scheiben mit Normierern per dynamischer Programmierung (ergebnisse/pruef\_zeitschleife\_mc.txt). Fortsetzung in Z.11.

## Z.11 Testmodell auf dem 2D-Torus (Stand 2026-11-10, Nachtlauf läuft)

**Programm [N]:** [zeitschleife2d.py](zeitschleife2d.py). Harte Bosonen auf dem Lx×Ly-Torus, Trotter-Zeit mit vier Bindungsklassen, Scheiben aus S Halbschritten, Zellen cx×cy.

- Züge werden nur unter den ausführbaren gezogen. Ausführbar hängt nur von Endpunkten ab (wählbare Stücke vorhanden, bei Variante a ein freier Platz in der Zielzelle). Die Normierung steht in der Dichteformel mit.
- `--zuege alle` erlaubt Züge in jede Zelle; das ersetzt im kleinen Modell die Umwege um leere Zellen.
- `--locker` heißt wählbar = Ende in der Zelle. Das ist die Festlegung von G.5.1 (ein Stück gehört zur Zelle seines Endes), also beweistreu.
- Dichte f = dν/dµ exakt als dynamische Programmierung über die Scheiben, Zustand (Kopf, Loch); Aufweg-Faktor als Matrix Φ[S0, Yo] mit numpy-Propagatoren für ein und zwei markierte Teilchen.
- Ziehen von C exakt: periodisch per Transfermatrix oder Grundzustand per Doob-Transformation.

**Exaktprüfung [N]:** ν = fµ durch vollständige Aufzählung, Vorwärtszweige über den unabhängigen langsamen beweger. Größter relativer Fehler ≤ 1,1·10⁻¹⁵ in allen Fällen: 4×2 (N = 2, 3; w = 1, 2), 6×2 (N = 2, 3), 4×4 (N = 2), alle vier Abweg-Varianten, mit und ohne Querschritt, `--locker`, `--zuege alle`. Der MC-Modus trifft die exakten Werte (E[f] = 5,503 ± 0,020 gegen 5,524).

**Befund bei m ≈ 1 Teilchen je Zelle [N]** (4×4, N = 4, Zellen 2×2, S = 8, Grundzustand, je 600 Proben; ergebnisse/zs2d\_diag/):

| Abweg                                       | ∫f²dµ bei w = 1 | w = 2 | w = 3 |
|---------------------------------------------|-----------------|-------|-------|
| frei (idealer Spiegel, nicht zellgebunden)  | 2,3             | 3,0   | 3,3   |
| Variante a (festzelle, Querschritt, locker) | 6,3             | 24,9  | 83    |
| festzelle, locker, ohne Pflicht-Querschritt | 5,8             | 16,8  | 23,4  |
| festzelle, Anfang und Ende in der Zelle     | 10,6            | 40,8  | 183   |
| zelle (alter eingeengter Abweg)             | 9,4 (N = 6)     | 30,5  | 36,8  |

- Der freie Spiegel bleibt beschränkt (Faktor je Scheibe 1,29, dann 1,11).
- Die zellgebundenen Varianten wachsen bei m ≈ 1 um den Faktor 3–4 je Scheibe.
- Das widerspricht dem Beweis nicht. In Z.8 kostet jede gemeinsame Zelle 1 + (e^{C(K)} − 1)/n\_Q, und das Kopfstück setzt sich nur mit Wahrscheinlichkeit ≤ C/m fort. Im kleinen Modell ist jede Scheibe gemeinsam (nur 4 Zellen), und n\_Q ≈ 1. Der Gesetz-der-großen-Zahlen-Effekt der Summe über die Stücke einer Zelle fehlt dann ganz.

**Nachtlauf 2026-11-10/11 [N]:** Gitter und Dichte fest (6×4, N = 6, ρ = 1/4, S = 8, Grundzustand), Zellgröße wachsend: m = 1 (Zellen 2×2), 1,5 (3×2), 3 (6×2). Varianten a, festzelle locker, frei, zelle; w = 1 bis 4; 48 Läufe à 1,75 h (4000 bis 10⁶ Proben). Skript [zs2d\_nacht.sh](zs2d_nacht.sh), Auswertung [auswertung\_zs2d\_nacht.py](auswertung_zs2d_nacht.py), Zahlen in ergebnisse/zs2d\_nacht\_auswertung.txt.

Wachstumsfaktor von ∫f²dµ je Scheibe (geometrisches Mittel über w = 1 bis 4):

| Abweg                                       | m = 1 | m = 1,5 | m = 3 |
|---------------------------------------------|-------|---------|-------|
| frei (Anfang aus dem bedingten Gesetz)      | 1,00  | 1,04    | 1,14  |
| festzelle locker (ohne Pflicht-Querschritt) | 2,22  | 2,14    | 1,93  |
| Variante a                                  | ≈ 3,4 | ≈ 4–5   | 2,85  |
| zelle (alter eingeengter Abweg)             | 4,37  | 4,01    | 2,86  |

Bei Variante a sind m = 1, w = 4 und m = 1,5, w = 3 und 4 von Einzelproben beherrscht (größte Probe 26–68 % von Σf). *Vermerk 2026-11-13 (Review H4):* Das gilt für alle 25 der 112 Zeilen von ergebnisse/zs2d\_nacht\_auswertung.txt mit max/Σf ≥ 0,05; ihre Mittelwerte sind untere Schätzungen. Betroffen sind die zellgebundenen Varianten (Variante a, zellgewicht, festzelle) und der Ball mit R = 1 und 2, jeweils bei w = 2 bis 4. Nicht betroffen sind die Zeilen „frei“ und „Ball R = 3“, auf denen die Folgerung für Variante c beruht. Angegeben sind deshalb für m = 1 die Faktoren aus w = 1 → 2 → 3 (3,36; 3,37) und für m = 1,5 der Bereich (4,0 bei w = 1 → 2).

Was der Lauf zeigt:

- **Die Schleife selbst ist gesund.** Mit dem Spiegel-Abweg und Anfang aus dem exakt bedingten Gesetz bleibt ∫f²dµ über vier Scheiben konstant (m = 1: 2,10; 2,08; 1,99; 2,07). Aufweg-Relais, Spiegel-Abweg und Buchführung erzeugen also kein exponentielles Wachstum.
- **Variante a ist im kleinen Modell nicht besser als der alte Abweg.** Beide wachsen um den Faktor 3–4 je Scheibe. Die Kosten zerlegen sich: gleichverteilter Anfang in der Zelle statt bedingtem Gesetz etwa ×2 je Scheibe (frei → festzelle locker), Pflicht-Querschritt nochmals ×1,5–2,5 (festzelle locker → a).
- **Die Vorhersage „Faktor − 1 ~ 1/m“ lässt sich hier nicht prüfen.** (F − 1)·m ist für Variante a 4,2; 5,9; 5,5, also grob konstant. Der alte Abweg zelle, der nach Befund A gar nicht von m profitieren sollte, fällt aber genauso (3,4; 4,5; 5,6). Größere Zellen erhöhen zugleich m und die Wahrscheinlichkeit, in der Zelle zu bleiben; beides ist bei fester Dichte nicht zu trennen.
- **Der Beweis-Bereich ist weit weg.** Z.8 braucht m ≫ 14C (Kopfstück-Teilen ≤ 1/(1 − 14C/m)) und κ₀ = 2ε + σ\_ρ + (e^{C(K)} − 1)/(b₋m) klein. Im Modell ist m ≤ 3 und σ\_ρ von der Ordnung 1. Ein Widerspruch zu Satz Z folgt daraus nicht, eine Bestätigung von Variante a aber auch nicht.

**Gegenprobe „zellgewicht“ (2026-11-11, [zs2d\_zellgewicht.sh](zs2d_zellgewicht.sh)) [N]:** Vermutet war, dass der gleichverteilte Anfang die Kosten macht. Neue Variante: Anfang aus dem bedingten Gesetz ∝ Z(S′ → Y\_m | übrige Stücke), aber nur unter den freien Plätzen der Zielzelle. Exakt geprüft (Fehler ≤ 1,2·10⁻¹⁵), dann je Lauf 18 min am selben System.

| Abweg (Anfang des neuen Stücks)                  | m = 1 | m = 3 |
|--------------------------------------------------|-------|-------|
| frei: bedingtes Gesetz, alle freien Plätze       | 1,00  | 1,14  |
| festzelle locker: gleichverteilt in der Zelle    | 2,22  | 1,93  |
| zellgewicht: bedingtes Gesetz in der Zelle       | 2,88  | 3,51  |
| Variante a: gleichverteilt + Pflicht-Querschritt | ≈ 3,4 | 2,85  |
| zellgewicht + Pflicht-Querschritt                | 4,25  | 3,54  |

- **Die Vermutung ist widerlegt.** Das bedingte Gesetz in der Zelle ist nicht besser als die Gleichverteilung, eher schlechter.
- **Teuer ist die Beschränkung auf die Zelle, nicht die Verteilung darin.** Der Aufweg ist in allen Varianten derselbe. Ohne Beschränkung (frei) kostet eine Scheibe fast nichts, obwohl sich im kleinen Modell beide Kopien in jeder Scheibe begegnen. Also kosten Aufweg-Brücken und Spiegel-Buchführung je Begegnung fast nichts; die Kosten ×2–4 kommen aus dem eingeschränkten Anfang des neuen Stücks.

**Deutung [H]:** Im kleinen Modell ist jede Scheibe eine Begegnung der beiden Kopien; gemessen wird also der Faktor Λ je Begegnung. Im Beweis kosten ferne Scheiben ≤ 1, aber Begegnungen müssen fast nichts kosten: Λ = e^{κ₀} mit κ₀ ≤ α/2 (Budget θ ≲ 10⁻³). Für Variante a soll das über (e^{C(K)} − 1)/n\_Q geschehen, braucht also n\_Q ≫ e^{C(K)}. Die Daten bei m = 1–3 zeigen für die zellgebundenen Varianten keinen Abfall wie 1/m.

**Neuer Vorschlag [H]:** Anfang aus dem bedingten Gesetz auf isolierten freien Plätzen im Ball vom Radius D s um Y\_m, nicht in der Zelle. Die Kosten sind dann von der Art 1/P(Anfang im Ball) − 1 ~ e^{−cD²}, klein ohne großes m. Die Lokalität bleibt auf der Skala D s, auf der die Makro-Bedingung ohnehin arbeitet. Der Normierer ist von der Art der Zugänglichkeit in Anhang P. Prüfbar im kleinen Modell mit einem Radius R statt der Zelle: Λ(R) sollte mit R gegen 1 gehen.

**Test „ball“ (2026-11-11, [zs2d\_ball.sh](zs2d_ball.sh)) [N]:** `--abweg ball --radius R`: Anfang aus dem bedingten Gesetz unter den freien Plätzen im Torus-Manhattan-Abstand ≤ R von Y\_m. Exakt geprüft (Fehler ≤ 1,3·10⁻¹⁵; für großes R identisch mit frei). System m = 1 (6×4, N = 6, Zellen 2×2), je Lauf 15 min. Zum Vergleich P(R) = Wahrscheinlichkeit, dass der Anfang eines freien Teilchens bei gegebenem Ende im Ball liegt (gleiche Scheibe S = 8).

| R         | P(R)  | 1/P(R) − 1 | Λ ohne Pflicht-Querschritt | Λ mit Pflicht-Querschritt |
|-----------|-------|------------|----------------------------|---------------------------|
| 1         | 0,292 | 2,42       | 2,11                       | 2,77                      |
| 2         | 0,627 | 0,60       | 1,17                       | 1,36                      |
| 3         | 0,878 | 0,14       | 0,99                       | 1,13                      |
| ∞         | 1     | 0          | 1,00 (frei)                | –                         |
| Zelle 2×2 | –     | –          | 2,88 (zellgewicht)         | 4,25                      |

- **Die Vorhersage trifft zu.** Λ − 1 fällt mit R rasch auf 0, sogar schneller als 1/P(R) − 1 (Faktor 0,3–0,5 darunter). Schon bei P(R) ≈ 0,9 kostet die Scheibe nichts mehr messbar.
- Der Ball mit R = 1 (5 Plätze) ist besser als die Zelle 2×2 (4 Plätze), weil er um Y\_m zentriert ist: Y\_m liegt nie am Rand.
- Der Pflicht-Querschritt kostet zusätzlich, bei R = 3 nur noch ×1,13.

**Test „nie Querschritt“ (2026-11-11, [zs2d\_nie\_quer.sh](zs2d_nie_quer.sh)) [N]:** Abweg ganz ohne Route (`--nie_quer`: nur Zug d = 0, also Scheibe für Scheibe nur ein neues Stück einfügen). Exakt geprüft (Fehler ≤ 9·10⁻¹⁶), je Lauf 15 min, 50 000 bis 150 000 Proben. Faktor Λ je Scheibe:

| Anfang des neuen Stücks | ohne Route, m = 1 | ohne Route, m = 3 | Querschritt erlaubt, m = 1 | Pflicht-Querschritt, m = 1 |
|-------------------------|-------------------|-------------------|----------------------------|----------------------------|
| Ball R = 1              | 4,72              | –                 | 2,11                       | 2,77                       |
| Ball R = 2              | 1,83              | –                 | 1,17                       | 1,36                       |
| Ball R = 3              | 1,22              | 1,32              | 0,99                       | 1,13                       |
| frei                    | 1,07              | 1,16              | 1,00                       | –                          |
| Zelle (alter Abweg)     | 4,37              | 2,86              | –                          | –                          |

- **Ohne Route wächst ∫f² stetig**, auch mit freiem Anfang (1,07 bzw. 1,16 je Scheibe, über w = 1 bis 4 gleichbleibend, also exponentiell). Der Abweg versteckt seinen Weg ohne Querschritte nicht vollständig; ein schwacher Rest von Befund A bleibt.
- **Am billigsten ist der Ball mit erlaubtem, nicht erzwungenem Querschritt** (R = 3: 0,99), vor dem Pflicht-Querschritt (1,13) und dem Abweg ohne Route (1,22).
- **Die Route bleibt also nötig.** Der Querschritt mischt den Kopf über die Zellen; das Einfügen allein reicht nicht.

**Folgerung für den Beweis (umgesetzt in G.12.9):** Variante a ist durch Variante c ersetzt: S′ aus dem bedingten Gesetz ∝ Z(S′ → Y\_m | übrige Stücke) auf den isolierten freien Plätzen im Ball vom Radius D\_c s um Y\_m. Lemma C [S, gegeben P6]: Eine geteilte Kopfscheibe kostet ≤ 1/(1 − η\_c) ≤ 2 statt ≤ 14, und die Bedingung 14C/m < 1 wird zu m ≥ 4C. Das über S′ gemittelte Gesetz des neuen Stücks hat eine beschränkte Dichte bezüglich der freien Rückwärts-Irrfahrt; Lemma P6 wird nur für kurze Brücken gebraucht. Der Querschritt bleibt (Test „nie Querschritt“ oben).


Alles Übrige folgt OA §10 Schritt für Schritt. Die Unterschiede sind in der Tabelle oben vollständig aufgezählt.

## Z.12 Die Kette der Voraussetzungen von Satz Z (2026-11-13)

Mit Restsatz M14 (Anhang M, M.9.5 bis M.9.9) hat jeder Schritt Z.1 bis Z.8 eine Aussage mit Beweis. Hier wird die ganze Kette der „gegeben …“ bis zu den Eingängen verfolgt, und daraus die Kennzeichnung von Satz Z bestimmt. Geprüft ist die Kette der Kennzeichnungen und ihre Vollständigkeit, nicht jeder Beweis neu.

**Die Bausteine.**

| Baustein                                         | Ort                                     | Stand                                                          | stützt sich auf                                       |
|--------------------------------------------------|-----------------------------------------|----------------------------------------------------------------|-------------------------------------------------------|
| Konstruktion, Dichteformel                       | G.12.1, G.12.2, Lemma L3, Lemma M14a    | [S], exakt geprüft [N]                                         | Tutorial Lemma 3.1, 5.1                               |
| zweites Moment, Zustände, Fernkürzung            | G.12.3, Z.1, Lemma G3′                  | [S]                                                            | –                                                     |
| Z.2 Kernfaktoren                                 | Lemma M8                                | [S]                                                            | (K1), (K2′)                                           |
| Z.3, Z.4 Nenner                                  | Lemma M5, Folgerung M6, M7              | [S]                                                            | Lemma P6″, Lemma C (c), Lemma F13, Lemma M4           |
| Z.5 Stabilität                                   | Lemma M1 bis M4                         | [S]                                                            | Lemma U4, Lemma M2 (Lemma R, F11a)                    |
| Listen, J                                        | Lemma M11, M11a, M12                    | [S]                                                            | Lemma S2, M4                                          |
| Z.6 Kreuzvergleich                               | Lemma M9                                | [S]                                                            | M4, M6 bis M8, G3′                                    |
| Z.7 Defekte unter dem Bezugsmaß                  | Z.7, Lemma M14b                         | [S]                                                            | Satz D, G.11.2                                        |
| Z.8 Auswahl, seltene Komponenten, Zusammensetzen | Lemma M10, M13, M.8.4                   | [S]                                                            | Z.7, Lemma S1 (auch weiches Maß)                      |
| Z.8 Endzellen                                    | Lemma M14a bis M14f, M14b′              | [S] im Regelfall; zwei Sonderfälle [B] (M.9.10)                | Satz D für N − 1, N, N + 1, Lemma C, P6″              |
| Skelette                                         | Lemma S1, S2, S3                        | S1, S2 [S nach OA], S3 [S]                                     | OA Lemma 8.1, 8.2 (nachgelesen); Satz D               |
| Ausweichen                                       | Lemma P6″, F13, U4, C, C′               | [S]                                                            | (K1), (K2′)                                           |
| Satz D, alle Gründe                              | satz\_3\_9 §9 bis §12, Anhang E, F, U   | [S]                                                            | Satz T2, Satz 3.9 (a^W), (c), Anhang E                |
| Übertragung auf µ\_ab                            | G.11.2                                  | [S nach OA]                                                    | OA Satz 7.3 (nachgelesen)                             |
| Satz T2, T2′ (gefärbter Operator)                | satz\_3\_9 §10                          | [S, gegeben die Eingänge in §10.7]                             | Gitterkern, Lemma R, F11a, Fach ∗, §11, Lemma 6.5, T3 |
| Gitterkern (K1) bis (K4), Lemma R                | Anhang K                                | (K1), (K2′) [S] ohne Literatur; scharfes (K2) [N] (2026-11-13) | Anhang K, K.1, K.5; pruef\_bessel.py                  |
| Fach ∗ (Randintervalle) in Satz T2               | satz\_3\_9 §10.0, §10.2                 | bisher [B]; hier geschlossen, [S, gegeben Lemma F11a]          | unten                                                 |
| Tutorial-Lemmata                                 | Lemma 3.1, 3.2, 5.1, 6.1, 6.5, 6.6, 6.8 | [S]                                                            | –                                                     |
| Annahme \|ν\| ≥ υ/2 − 5ζ²                        | G.12.7, ergänzt unten                   | bisher [B]; hier [S, gegeben Lemma S3 und L2]                  | unten                                                 |

**Zwei Lücken, die die Durchsicht gezeigt hat, und ihre Schließung.**

- **Fach ∗ in Satz T2.** Die Randintervall-Bedingung der Wählbarkeit (G.5.1, Test 3: in den ersten und letzten Zeitintervallen der Länge τ₀ innerhalb r/10 von Anfang bzw. Ende bleiben) hatte als Fach ∗ in Satz T2 die Kleinheit e^{−κr\_∗} nur behauptet, und τ₀ war nirgends festgelegt. Man setzt τ₀ = r²/(440 r\_∗). Nach Lemma F11a (Anhang F) verlässt die freie Irrfahrt die Kugel vom Radius r/10 in der Zeit τ₀ mit Wahrscheinlichkeit ≤ 4 exp(−(r/10)²/(4,4 τ₀)) = 4e^{−r\_∗}; die Voraussetzung r/10 ≤ 2,2 τ₀ heißt r ≥ 20 r\_∗ und gilt für kleines ρ, ebenso τ₀ ≤ δ/2 wegen r² = ζ²/ρ ≪ s². Für die Brücke kostet das wie bei den Fächern R2 und G4 einen festen Faktor (satz\_3\_9 §10.2). Mit beiden Enden ist die Fehlerwahrscheinlichkeit ≤ C e^{−r\_∗} ≤ c η\_∗^{3/2} für η\_∗ = e^{−r\_∗/2} und r\_∗ groß. Die Bedingung von Satz T2 wird zu r\_∗ ≳ 64πK, eine feste Zahl.
- **Annahme mit dem neuen Schwanz.** Seit M.9.5 wird außerdem verworfen, wenn ξ nicht gut ist. Weil ξ gleichverteilt und von C unabhängig ist, ist die Wahrscheinlichkeit dafür höchstens das Mittel über ξ der Zahl der Teilchen im Abstand ≤ r, also N(2r + 1)²/M = ρ(2r + 1)² ≤ 5ζ² für kleines ρ (r² = ζ²/ρ). Eine Dichteschranke braucht man dafür nicht. Ein Schwanz-Kandidat fehlt nur in unbrauchbaren Zellen; die Endzelle a liegt nach dem Verwerfen von S.3 nicht in einer Füllung. Mit den übrigen Gründen aus G.12.7 (Anhang S, Lemma S3; Anhang L, Lemma L2) gilt |ν| ≥ υ/2 − 5ζ² für kleines ρ. (Bis 2026-11-14 stand hier υ/2 − ε − 5ζ²; der Abzug ε stammte von Regel 3 aus Anhang L, dem Verwerfen bei irregulärem Schwanzstück, die seit M.9.5 entfällt, weil das Schwanzstück regulär gewählt wird. Review 2026-11-13, H8.)

**Was nicht in der Kette steht, aber für die Aussage zählt.**

- **Pflasterung.** Die Konstruktion braucht Zellen, die den Torus pflastern. Ist L kein Vielfaches einer zulässigen Zellseite (s² im festen Bereich um K ln(1/ρ)/ρ), braucht man Zellen mit Seiten zwischen s und 2s. Das ist im Tutorial (§0.1) nur als Hinweis notiert und nicht nachgerechnet. *Nachtrag:* ausgeführt in Z.13.
- **Konstanten.** Die Reihenfolge Z.9 deckt die neuen Bedingungen aus Anhang M ab, ergänzt in Punkt 7: η ≤ 1/4 mit C′(K) (M.9.8), s² ≥ 2C e^{2C′(K)} für die Fortsetzung am Schwanz (M.9.7) und q klein genug für Lemma M13 mit C₂ ≤ 12 (M.9.9). Alle sind von der Form „fest gegen ρ → 0“.

**Urteil.** Satz Z ist bewiesen, gegeben

1. die Schranken für Bessel-Quotienten im Gitterkern (Literatur, Standard; ohne explizite Konstanten auch Delmotte 1999). *Seit 2026-11-13 entfällt dieser Eingang:* (K1) und (K2′) sind elementar bewiesen, und alle Stellen sind auf (K2′) umgestellt (Anhang K, K.5). Satz Z ist damit [S nach OA] ohne Literatur. Der frühere Beweisweg hatte in Schritt 1 eine falsche Begründung,
2. zwei OA-Schritte, die samt Beweis nachgelesen und deren Übertragung geprüft ist (OA Satz 7.3 in G.11.2, OA Lemma 8.1 in Lemma S1),

und zwar für Seitenlängen L, die ein Vielfaches einer zulässigen Zellseite sind. Kennzeichnung nach der Regel dieses Anhangs: **[S nach OA, gegeben die Bessel-Quotienten [Lit]]** (seit 2026-11-13: **[S nach OA]** ohne Literatur, siehe Punkt 1), für allgemeines L mit der Pflasterung als offenem Punkt [B]. *Nachtrag 2026-11-13:* Die Pflasterung ist in Z.13 ausgeführt; dort ist auch L₀ = c\_L s(ρ) festgelegt. Satz Z gilt damit für alle L ≥ L₀(ρ). Numerisch gestützt, aber nicht gebraucht, sind die exakten Prüfungen der Dichteformeln und der Bausteine (Mini-Ring, Testmodell).

*Nachtrag 2026-11-14 (zweites Review, [review\_2026-11-13.md](review_2026-11-13.md)):* W2 (Lemma S2 jetzt OAs Konstruktion wörtlich), W1 (später Anfang am Schwanz, Lemma M14b′, M.9.11) und W3 im Regelfall (Lage des Schnitts, Lemma M14f, M.9.10) sind erledigt. Zwei Sonderfälle an den Enden der Schleife sind nur skizziert [B]: Teilen der Kopfkette bis zur Wende (k\_H = w) und Kopf- und Schwanzende in derselben Scheibe mit gemeinsamen Stücken. Die Kennzeichnung von Satz Z ist deshalb **[S nach OA bis auf diese Sonderfälle [B]]**. Beide betreffen Selbstbegegnungen der auswertenden Schleife an ihren Enden und ändern nach dem Plan in M.9.10 nur Konstanten.

*Nachtrag 2026-11-13 (beim Nachziehen des Tutorials):* Lemma S2 benutzt in Schritt 3 außerdem den Randzusammenhang aus OA Lemma 8.2. OA beweist ihn selbst mit einem kurzen Paritätsargument nach Timár; der Beweis ist nachgelesen und überträgt sich wörtlich. Das ist ein dritter OA-Schritt neben Satz 7.3 und Lemma 8.1. An der Kennzeichnung [S nach OA] ändert sich nichts; S2 ist in der Tabelle entsprechend umgestellt. *Nachtrag (Review 2026-11-13, W2):* Die damalige Fassung von S2 war nicht OAs Konstruktion (gemeinsame Füllung, Kantenwege) und trug nicht; seit 2026-11-13 abends ist S.2 OAs Konstruktion wörtlich (Füllung je Kanten-Komponente, Sternpfade am Außenrand). Folge in Anhang M: C\_J = 12D + 138.

## Z.13 Pflasterung und Systemgröße (2026-11-13)

Z.12 lässt für Satz Z zwei Punkte offen, die nicht in der Kette der Lemmata stehen: Seitenlängen L, die kein Vielfaches der Zellseite sind (Tutorial §0.1: „im Einzelnen nicht nachgerechnet“), und die untere Schranke L₀(ρ). Beide werden hier erledigt.

**Die Pflasterung.** s = s(ρ) sei die Zellseite aus Satz 3.9, **als ganze Zahl** gewählt: s = ⌈(K ln(1/ρ)/ρ)^{1/2}⌉ (s ≥ 16 für kleines ρ; die Zellbesetzung m = ρs² ändert sich dadurch um einen Faktor 1 + O(1/s), Review 2026-11-13, H4). n = ⌊L/s⌋. Jede Koordinatenachse wird ausgeglichen geteilt: L = nq + r mit q = ⌊L/n⌋ und 0 ≤ r < n, also r Abschnitte der Länge q + 1 und n − r der Länge q. Die Zellen sind die Produkte zweier Abschnitte. Für n ≥ 16 gilt dann

- **(P1)** Jede Zellseite liegt in [s, 9s/8]: q ≥ s, und q + 1 ≤ L/n + 1 < s(n + 1)/n + 1 ≤ 17s/16 + 1 ≤ 9s/8. Also s² ≤ |Q| ≤ (81/64) s².
- **(P2)** Die Zellen bilden genau den Zellgraphen (ℤ/nℤ)² der bisherigen Fassung.
- **(P3)** Gitter feinerer Skalen werden ebenso gebildet: Kästen der Seite b (Lemma A), der Seite 2r (Isolation, §12.2) und Quadrate der Skalen R aus Anhang F, je mit ⌊L/b⌋, ⌊L/(2r)⌋ bzw. ⌊L/R⌋ Abschnitten je Achse. Sie sind Rechtecke mit Seiten b oder b + 1 usw.

Numerisch geprüft ([pruef\_pflasterung.py](pruef_pflasterung.py), ergebnisse/pruef\_pflasterung.txt): In 20 000 Zufallsfällen (16 ≤ s < 400, 16s ≤ L < 200s) liegen alle Zellseiten in [s, 9s/8].

**Lemma 6.3b (Kästen als Rechtecke) [S].** Sei Q ein Rechteck mit Seiten b und b′ ∈ {b, b + 1}, b ≥ 2, mit Neumann-Laplace-Operator L\_Q. Dann gilt Lemma 6.3 mit |Q| statt b² und λ₂ = 2 − 2cos(π/b′), und für alle y ∈ Q

```text
R_y  ≤  (2/π) ln b + 3,4,        λ_min(Q)  ≥  π / ( 2 |Q| (ln b + 5,8) )
```

*Beweis.* Lemma 6.3: Die drei Schritte benutzen nur den Mittelwert, die Spektrallücke und das Thomson-Prinzip; die Lücke ist die der längeren Seite. Für R\_y wie Lemma 6.3a in der Kosinus-Eigenbasis, jetzt mit x\_p = πp/(2b), y\_q = πq/(2b′), φ\_p² ≤ 2/b und ψ\_q² ≤ 2/b′:

1. R\_y ≤ (bb′)^{−1} [Σ\_{p,q≥1} 1/(sin² x\_p + sin² y\_q) + ½ Σ\_p 1/sin² x\_p + ½ Σ\_q 1/sin² y\_q].
2. Wie dort ist 1/(sin² x + sin² y) ≤ 1/(x² + y²) + π²/12. Wegen b′ ≥ b ist x\_p² + y\_q² ≥ (π/(2b′))² (p² + q²), und die Gittersumme über p ≤ b − 1, q ≤ b′ − 1 ist ≤ ½ + (π/2) ln(√2 b′). Mit b′/b ≤ 1 + 1/b und ln b′ ≤ ln b + 1/b gibt das ≤ (2/π) ln b + 0,43 + 0,83 + 0,92.
3. Achsen: (2bb′)^{−1} [(4b²/π²)(π²/6) + (4b′²/π²)(π²/6)] + π²/24 ≤ ⅓(b/b′ + b′/b) + 0,42 ≤ 1,13.
4. Zusammen R\_y ≤ (2/π) ln b + 3,31. Mit 1/λ₂ ≤ b′²/π² + π²/48 ≤ 0,23 |Q| gibt Lemma 6.3 λ\_min ≥ 1/(|Q| ((2/π) ln b + 3,63)) ≥ π/(2|Q|(ln b + 5,8)). ∎

*Prüfung [N].* Das Maximum von R\_y über alle y (b ≤ 128, sonst in der Ecke) liegt für Rechtecke b × (b + 1) höchstens 0,003 über dem des Quadrats, bei b = 1024 bei 4,23 gegen die Schranke 7,81; die λ-Schranke hält mit Faktor ≥ 1,87. Die Konstante 5,8 statt 3,6 ändert nichts: In Kapitel 7 ist ln b = ½ ln(1/(Hρ)), und additive Konstanten verschwinden für ρ → 0 gegen ln b.

**Wo die Zellen eingehen, und was die Pflasterung ändert.**

| Stelle                                                  | braucht                                                    | mit der Pflasterung                                                                        |
|---------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Lemma A, Satz 3.9 (a), (a^W) (satz\_3\_9 §1, §11)       | Neumann-Kästen der Seite b über Ω\_h, ihre Zahl            | Rechtecke nach (P3), Lemma 6.3b; c\_b mit (b + 1)² und ln b + 5,8, C\_V × 81/64            |
| Satz 3.9 (b), Anhang E                                  | einzelne Dirichlet-Quadrate im Gebiet, Fläche \|U\| ≥ u s² | keine: die Quadrate werden gepackt, nicht gepflastert                                      |
| Isolation, Satz 3.9 (c) (§12.2)                         | Kästen der Seite 2r mit Versatz, Lemma 3.3                 | Rechtecke 2r bzw. 2r + 1; „im selben Kasten für ≥ ¼ der Versätze“ bleibt, alle Seiten ≥ 2r |
| Anhang F (Gitterquadrate aller Skalen, F1, F2, F7, F10) | Quadratgitter je Skala, Lokalisierung, Kastenenergie       | ausgeglichene Gitter nach (P3), Lemma 6.3b; Ausdünnen gierig auf dem Torus                 |
| Satz T2, T2′, Satz U, Lemma R, F11                      | Gebiete nach Abstand, Flächen, Zellmengen U                | nur Flächen: \|U\| ≤ (81/64) u s²                                                          |
| Zählintervall [b₋m, b₊m], m = ρs²                       | E n\_Q = ρ\|Q\| von der Ordnung m                          | ρ\|Q\| ∈ [m, (81/64) m]; b₊ um den Faktor 81/64 größer wählen                              |
| Lemma C, Variante c                                     | c\_δ s² ≤ δ ≤ C\_δ s², Ball vom Radius D\_c s              | δ = s² wie bisher; Bälle in Plätzen gemessen                                               |
| Skelette, Umwege, Listen (Anhang S, M11)                | Zellgraph (ℤ/nℤ)²                                          | unverändert nach (P2)                                                                      |
| Zählungen n″, n\_loc, J, Reg (Anhang M)                 | Zellen in Bällen, Abstände in Zellen                       | unverändert; Plätze ↔ Zellen mit Seiten in [s, 9s/8]                                       |
| Dichteformel, Bilanz (M14a, M.9.5)                      | s² = Fläche der Zelle von ξ, M\_Z = Zahl der Zellen        | s² wird \|Q\_a\| (exakt in der Formel), M\_Z = n²; Bilanz mit Faktoren (81/64)^k           |
| Gitterkern (K1) bis (K4) auf dem Torus                  | Kern auf ℤ²                                                | Torus-Kern = Summe über Bilder, Zusatz ≤ e^{−cn} für δ = s²                                |
| Kernquotienten Lemma M2, M8, M14d (Λ)                   | Endpunktabstände ≤ Λs                                      | Λ = (9/8)(D + 4) statt D + 2 (Zellseiten ≤ 9s/8; Paarung nach Lemma M14f), Review H4, W3   |

Jede Zeile ändert nur feste Konstanten um feste Faktoren; keine Bedingung der Reihenfolge Z.9 wird dadurch verletzt, denn alle sind von der Form „fest gegen ρ → 0“.

**Systemgröße.** Bisher stand L ≥ 16 s(ρ); die 16 kommt allein aus dem Skelett (W ≤ n/8, Anhang S). Die lokalen Argumente benutzen aber feste Umgebungen größerer Reichweite: Kästen vom Radius D\_K s (D6, D7, Lemma P6″), den Begegnungsradius R\*″ = R\*₂ + 2ℓ⁰ (Anhang M, M.8.2) und Brücken bis (D + 10)s. Bei n = 16 reicht ein Kasten vom Radius D\_K s um den Torus, sobald D\_K > 8. Ob jedes lokale Argument das verträgt, ist nicht geprüft. Deshalb wird verlangt

```text
L  ≥  L₀(ρ)  =  c_L s(ρ),        c_L  =  max( 16, 2R*″ + 2 )
```

*Ist die Erhöhung nötig? (Review 2026-11-13, H4, Punkt 7 der Übergabe):* ja. D\_K ≥ 12γ\_n n^{1/2} + 3 ≈ 17(D + 10) und R ≳ (C′n)^{1/2} sind viel größer als 8; bei 16 Zellen je Achse gäbe es keine fernen Zellen im Sinn von Lemma M4, und die Kästen von Lemma P6″ überlappten sich selbst. Dann liegt jede dieser Umgebungen (Radius ≤ R\*″ Zellen; R\*″ ≥ R\* = Δ + D\_K + R + 2D + 6 deckt die Kästen und die Brücken) ohne Selbstüberlappung im Torus, und alle lokalen Argumente sind wörtlich die der Ebene. Die zufälligen Bereiche Reg aus M.8.0 dürfen größer sein; sie gehen nur als obere Schranken ein. c\_L ist eine feste Zahl, abhängig von K, D, D\_K, R und ε; der Satz bleibt einer für alle L ≥ c · s(ρ). Der elementar behandelte Bereich kleiner Systeme (Tutorial §0.1) ändert sich nicht, der unbehandelte Zwischenbereich (Review W7) wird um den Faktor (c\_L/16)² in N größer.

**Ergebnis.** Satz Z gilt für alle L ≥ L₀(ρ) = c\_L s(ρ), ohne Teilbarkeitsbedingung. Kennzeichnung: [S nach OA] (seit 2026-11-13 ohne Literatur-Eingang: (K1), (K2′) elementar, Anhang K; bis dahin gegeben die Bessel-Quotienten [Lit]). Die Pflasterung ist [S] im Sinn einer Durchsicht: Lemma 6.3b ist bewiesen, und die Tabelle führt jede Stelle auf, an der die Zellform eingeht, mit dem Grund, warum sich nur Konstanten ändern.
