# Zu diesem Band

Stand 2026-11-14. Dieser Band ist eine **Arbeitsfassung zum Gegenlesen**, keine Darstellung zum Lernen. Er setzt die Anhänge des Projekts unverändert hintereinander, in der Reihenfolge des Lesewegs aus uebergabe\_review\_2026-11-13.md. Ziel ist, dass Fehler auffallen. Einführung, Bezeichnungen und die Lemmata aus Kap. 3, 5 und 6 stehen im Tutorial (tutorial\_beweis\_verduennt.pdf). Verweise auf andere Anhänge sind anklickbar, und die Lesezeichen des PDF folgen den Überschriften. Gebaut mit pdf\_bauen.py.

**Was bewiesen wird.** Satz Z (Anhang Z): Nach Festlegung der Abschneidekonstanten gibt es C < ∞ mit ∫ f² dµ ≤ C für alle hinreichend kleinen ρ und alle L ≥ L₀(ρ) = c\_L s(ρ). Mit |ν| ≥ υ/4 folgt N₀/N ≥ υ²/(16C). Kennzeichnung [S nach OA] bis auf zwei Sonderfälle an den Enden der Schleife (Anhang M, M.9.10) [B]. Die Kette aller Voraussetzungen steht in Z.12, die Reihenfolge der Konstanten in Z.9.

**Kennzeichnung.** [S] bewiesen. [S nach OA] bewiesen mit einem Schritt der OpenAI-Arbeit (OA), dessen Beweis nachgelesen und dessen Übertragung geprüft ist: OA Satz 7.3 (G.11.2), Lemma 8.1 (Lemma S1), Lemma 8.2 (Lemma S2). [B] Beweisskizze. [N] numerisch. [Lit] Literatur. „Gegeben …“ nennt die Eingänge eines Beweises.

**Was zum Beweis gehört und was nicht.** Die Anhänge sind über mehrere Tage gewachsen. Ältere Fassungen sind stehen geblieben und markiert.

- Absätze, die mit *Frühere Fassung* beginnen, sind grau gesetzt. Sie gehören nicht zum Beweis.
- In Anhang Z tragen Z.2 bis Z.8 Vermerke „Seit 2026-11-13 bewiesen“ bzw. „seit 2026-11-13 Lemma M…“. Der Text danach („die frühere Skizze“) ist durch Anhang M ersetzt. Z.10 ist Geschichte, Z.11 ein Testmodell.
- In Anhang M ist M.9.4 (der offene Restsatz) durch M.9.6 bis M.9.11 erledigt; die Fortsetzung am Schwanz aus M.9.7 („Frühere Abhilfe“) ist durch den späten Anfang in M.9.11 ersetzt, Lemma C′ wird nicht mehr gebraucht. M.5 am Ende ist eine Abhakliste.
- In satz\_3\_9 ist §4 (untere Schwänze) durch Anhang E ersetzt, §5 (Isolation [B]) durch §12.2 und §8 (Satz 3.9 d) durch Satz D in §9. §6 und §7 sind Bilanz und Vermutung.
- In Anhang G sind G.0 bis G.9 die Vorgeschichte (Lücke statt Zeitschleife). Gültig bleiben die Festlegungen, auf die G.10 bis G.12 und die anderen Anhänge verweisen, vor allem G.5.1 (Wählbarkeit), G.2 (Dichteformel) und G.4 (Fernkürzung).
- In Anhang P ist P.6 („Offen“) durch P.7 und Anhang F beantwortet.

**Wo man am genauesten hinsehen sollte.** Die zweite Durchsicht (review\_2026-11-13.md) ist eingearbeitet; neu und noch von niemandem gegengelesen sind seitdem Anhang S, S.2 (OAs Umwegkonstruktion), M.9.10 (Lemma M14f und die Sonderfälle) und M.9.11 (später Anfang, Lemma M14b′). Die ältere Liste steht in uebergabe\_review\_2026-11-13.md: Lemma M14b (später Schnitt), die Lage des Schnitts, die Fortsetzung am Schwanz, die Kernzählung an den Enden und Lemma M14d, Lemma M14e, die Kette Z.12, die Pflasterung Z.13 und die Reihenfolge der Konstanten Z.9. Auffälligkeiten am besten mit Seitenzahl und Abschnittsnummer notieren.

| Teil             | Datei                          | Inhalt                                                                      |
|------------------|--------------------------------|-----------------------------------------------------------------------------|
| Anhang Z         | anhang\_zweites\_moment.md     | Satz Z, Ablauf, Konstanten (Z.9), Kette (Z.12), Pflasterung (Z.13)          |
| Anhang M         | anhang\_buchfuehrung.md        | Beweise zu Z.2 bis Z.8: Lemma M1 bis M14e                                   |
| Satz 3.9, Satz D | satz\_3\_9\_dichteschranken.md | Dichteschranken, Defekt-Lemma, Satz T2, Besucher eines Kastens (§10.8)      |
| Anhang G         | anhang\_gegenluecke.md         | Zeitschleife: Konstruktion (G.12.1), Übertragung (G.11.2), Lemma C (G.12.9) |
| Anhang F         | anhang\_feinskala.md           | Gütebedingungen unterhalb der Zellskala, Lemma P6″, Lemma F13               |
| Anhang U         | anhang\_unzugaenglich.md       | Zugänglichkeit ohne zurückgehaltene Gruppe, Satz U, Lemma U4                |
| Anhang L         | anhang\_lochstueck.md          | Lochstück j₀, Wählbarkeit über zwei Scheiben                                |
| Anhang E         | anhang\_einfuegen.md           | Einfügen im Dirichlet-Quadrat, untere Schwänze                              |
| Anhang S         | anhang\_schleifen.md           | Skelette (S1), orientierte Umwege (S2), Schwänze der Abweichung (S3)        |
| Anhang K         | anhang\_kern.md                | Gitterkern (K1), (K2′), Brückenmaximum, Schlauch, Lemma R                   |
| Anhang P         | anhang\_ausweichen.md          | Ausweichen beim harten Kern, Satz P3, Lemma P5″, P6                         |
