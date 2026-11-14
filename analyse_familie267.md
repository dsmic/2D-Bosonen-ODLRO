# Analyse: „Ground-state condensation in the dilute hard-sphere gas“ (OpenAI, Familie 267)

Begonnen 2026-11-09. Teil von [weltlinien\_beweisobjekt.md](weltlinien_beweisobjekt.md). Kennzeichnung: [S] streng, [Lit] Literatur, [B] Beweisskizze, [N] numerisch, [H] Hypothese, [L] Lücke.

Quelle: [paper.pdf](https://github.com/openai/math/blob/main/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/paper.pdf) (53 S., 2026-09-24), erzeugt von einem internen OpenAI-Modell, laut Repository in Lean formalisiert (`HardSphere.lean`). Gelesen: Einleitung, Abschnitte 2–8 in den tragenden Aussagen; Beweise der Abschätzungen nur stellenweise. Abschnitts- und Lemmanummern beziehen sich auf das Preprint.

## 1. Aussage

Harte Kugeln (Radius a) im 3D-Torus, T = 0, feste Dichte ρ mit ρa³ < ε₀. Dann gilt für jeden Grundzustand im thermodynamischen Limes B(Ψ) ≥ c₀ > 0, mit c₀ unabhängig von ρa³ (Satz 1.1). Bisher galt das als großes offenes Problem (Solovej 2025).

## 2. Beweisaufbau in acht Schritten

1. **Betrag statt Wellenfunktion (§2, §9).** Φ = |Ψ| ist wieder Grundzustand; erst B(Φ) wird abgeschätzt, dann werden die Phasen zurückgeholt. *Für uns entfällt §9:* Auf dem Gitter ist H\_A stoquastisch und ψ > 0 eindeutig (Perron).
2. **Unser Kriterium als Affinität (8.2–8.3).** Für Zellen v, w: P\_vw = Teilchen in v mit Bad Y (dazu ein Hilfspunkt gleichverteilt in w), Q\_vw = dasselbe Bad mit Teilchen in w. Exakt gilt B(Φ) = V^{−2} Σ\_{v,w} H(P\_vw, Q\_vw) mit der Affinität H(P, Q) = ∫√(pq). Das ist das Faserkriterium aus [weltlinien\_beweisobjekt.md](weltlinien_beweisobjekt.md) §3 A, über Zellen gemittelt.
3. **Gemeinsames Maß (Lemma 8.1).** Gibt es ein Maß ν der Masse m mit ∫(dν/dP)² dP ≤ C\_P und ∫(dν/dQ)² dQ ≤ C\_Q, so ist H(P, Q) ≥ m²/√(C\_P C\_Q). Man muss also nur ein ν bauen, das beiden Seiten ähnlich genug ist (zweite Momente der Likelihood-Quotienten).
4. **Stationäres Weltlinienmaß (Lemma 4.1).** Brownsche Pfade auf [0, 2t] mit Gewicht e^{2tE} Φ(Anfang) Φ(Ende) und harter Vermeidung. Jede Zeitscheibe hat die Verteilung Φ²; bei festen Enden ist es ein Produkt von Brücken, bedingt auf Vermeidung. Das ist unser Wurm-Ensemble auf einem **kurzen** Zeitfenster; t ist klein und fest.
5. **Lokale Ersetzung (Satz 5.3, Korollar 5.5).** Die Bahn eines Teilchens wird bei festen Enden durch eine Brücke ersetzt, deren Mitte in der Nachbarzelle liegt. Die Wahrscheinlichkeit, dabei andere Bahnen zu treffen, ist ≲ α t/D + D^{−1/4} (D = Teilchen pro Zelle). **Hier geht die Verdünnung ein:** Fast jede Ersetzung gelingt.
6. **Gruppen und schlechte Zellen (§6).** Je Zelle werden disjunkte Gruppen beweglicher Teilchen gebildet. Bei festgehaltener Umgebung ist die bedingte Verteilung ein exakt bekanntes Produkt (Satz 6.2). Zellen ohne genug bewegliche Teilchen sind selten, mit Peierls-Schranke P(A ⊂ schlecht) ≤ p^{|A|} (Satz 6.3).
7. **Zufällige Routen (§7).** Von v nach w führt eine zufällige Gitterroute aus „unvorhersagbaren Pfaden“ nach Benjamini–Pemantle–Peres. Sie schreitet in Richtung 1 voran und schwankt in Richtung 2 und 3; um schlechte Cluster weicht sie über deren Außenrand aus (Kesten/Timár). Zwei unabhängige Routen haben exponentiell beschränkte Begegnungsmomente E e^{κJ} ≤ C (Satz 7.1).
8. **Staffellauf und Aufhebung (§8).** Längs der Route übernimmt je Zelle ein anderes Teilchen die Markierung. In Kopie 1 liegt seine Mitte in der eigenen Zelle, in Kopie 2 in der nächsten, und nach Entfernen der Markierung bleibt dasselbe Bad. Der Likelihood-Quotient ist ein Produkt lokaler Faktoren. Im zweiten Moment über zwei unabhängige Routen heben sich die Normierungen weit voneinander entfernter Stücke exakt auf; Kosten entstehen nur bei Begegnungen (Lemma 8.3: ≤ G^{|S∩T|}(1−χ)^{−2(…)}). Mit Schritt 7 folgt H(P\_vw, Q\_vw) ≥ const für einen festen Anteil der Zellpaare und damit B(Φ) ≥ c\* (Satz 8.4).

**Kern in einem Satz:** Man vergleicht „Teilchen hier“ mit „Teilchen dort“ bei gleichem Bad über eine Kette lokaler Umbauten. Die Kosten der Kette werden nicht entlang der Länge bezahlt, sondern nur dort, wo sich zwei unabhängig gewählte Ketten begegnen.

## 3. Wo die Dimension 3 eingeht

| Stelle                                   | Rolle                                            | wesentlich?                         |
|------------------------------------------|--------------------------------------------------|-------------------------------------|
| Routen-Skelett, zwei Querrichtungen (§7) | beschränkte Begegnungen zweier Routen            | **ja, das ist der Kern**            |
| Gauß-Dichten s^{−3/2} (Lemma 5.1)        | Stoßwahrscheinlichkeit der Ersetzung             | technisch; in 2D s^{−1}, logarithmisch |
| Energie- und Einfügelemmata (§3)         | Streulänge, Entfernungsenergie harter Kugeln     | technisch; 2D-Verdünnung ist logarithmisch |
| Mikrowürfel, Füllen (§9)                 | Phasen zurückholen                               | entfällt auf dem Gitter             |

**Dimensionszählung [B].** Das Skelett schwankt quer superdiffusiv, im Abstand s vom Routenende um etwa s^{3/4} (Mehrskalensumme mit Gewichten 2^{−ℓ/4}). Zwei Routen mit gleichen Enden kommen sich dort mit Wahrscheinlichkeit ~ (R/s^{α})^{q} nahe, q = Zahl der Querrichtungen:

```text
erwartete Begegnungen  ~  Σ_s s^{−qα}      konvergiert  ⇔  qα > 1
q = 2 (3D): α = 3/4 genügt.     q = 1 (2D): nötig wäre α > 1, unmöglich für Gitterpfade (Steigung beschränkt).
```

In 2D gibt es deshalb keine Routen mit beschränkten Begegnungen. Bei gemeinsamem Start ist bekannt, dass ℤ² keine exponentiellen Schnittschwänze erlaubt (Benjamini–Pemantle–Peres) [Lit].

## 4. Die imaginäre Zeit als zweite Querrichtung [H]

Bei T = 0 hat das Weltlinien-Ensemble eine unbeschränkte Zeitrichtung. Eine Route in Raum-Zeit (2 + 1) mit Querrichtungen „y“ und „τ“ hätte q = 2. Die Zählung passt genau zur bekannten Physik:

| Fall          | Querrichtungen der Route                           | q             | Routen-Argument | Physik                       |
|---------------|----------------------------------------------------|---------------|-----------------|------------------------------|
| 3D, T > 0     | 2 Raumrichtungen                                   | 2             | trägt (Preprint) | BEC                          |
| 2D, T = 0     | 1 Raum + Zeit (unbeschränkt)                       | 2             | **trägt?**      | ODLRO (numerisch sicher)     |
| 2D, T > 0     | 1 Raum + Zeit (Länge β, für s ≫ β^{4/3} wirkungslos) | effektiv 1  | scheitert       | kein ODLRO (Hohenberg)       |
| 1D, T = 0     | nur Zeit                                           | 1             | scheitert       | kein ODLRO                   |

Dieselbe Zählung ist der Grund, warum die Infrarotkette ∫E^{−1/2} in 2D bei T = 0 endlich ist und bei T > 0 nicht.

**Offene Punkte der Übertragung [L]:**

1. **Gleichzeitigkeit.** B(Φ) vergleicht zwei Konfigurationen zur selben Zeit. Die Kopien müssen bei τ = 0 bis auf die Markierung übereinstimmen und dürfen sich nur in einer Raum-Zeit-Röhre längs der Route unterscheiden. Dazu muss die exakte bedingte Verteilung (Satz 6.2) von kurzen auf lange Zeitfenster erweitert werden. **Erledigt (2026-11-09):** Das Einpunkt-Kriterium N₀/N ≥ H̄² vergleicht die Faser mit dem (N−1)-Grundzustand, ohne zweite Kopie. Die Route läuft dann in Zeitrichtung mit zwei räumlichen Querrichtungen (Raum-Zeit ℤ³). Die Raum-Zeit-Markov-Eigenschaft ersetzt Satz 6.2 ohne Zeitbeschränkung. Siehe [einpunkt\_zeitroute.md](einpunkt_zeitroute.md).
2. **Staffelschritt in Zeitrichtung.** Ein Schritt in τ ist nicht dasselbe wie ein Schritt im Raum. Die Markierung kann längs einer Weltlinie „mitfahren“ (kostenlos), driftet dabei aber diffusiv im Raum. Man braucht einen Zeitschritt mit kontrolliertem Likelihood-Quotienten und muss prüfen, dass Lemma 8.3 (Aufhebung fern der Begegnungen) erhalten bleibt.
3. **Anisotropie.** Raum und Zeit skalieren erst über die Schallgeschwindigkeit gleich (τ ~ r/c), und bei kleiner Dichte ist c klein. Die Querschwankung in τ muss im Skelett passend gewählt werden.
4. **Verdünnung in 2D.** Die Energie- und Stoßlemmata (§3, §5) brauchen 2D-Gegenstücke mit logarithmischer Kopplung. Auf dem Gitter mit kleinem ρ sollte das einfacher sein als im Kontinuum.
5. **Reichweite.** Die Methode braucht Verdünnung (Schritt 5). Selbst bei Erfolg wären nur kleine ρ erfasst, über Teilchen ↔ Loch auch ρ nahe 1. Mittlere Dichten und Stufe A bei 7/8 (Ausschlussanteil 23ρ\_b ≈ 0,72, also dicht) blieben offen.

## 5. Ersetzt eine Diagonale (t′) die dritte Dimension?

**Nein, für die Zählung nicht [B].** Diagonale Sprünge sind Abkürzungen in derselben Ebene. Die Querkoordinate einer Route bleibt eindimensional, ihre Schwankung bleibt höchstens linear (α ≤ 1), und Σ s^{−α} divergiert weiter. Ein zweites Argument: Könnte ein Term endlicher Reichweite die dritte Richtung ersetzen, dann trüge das Argument auch in 2D bei T > 0. Dort schließt der Satz von Hohenberg bzw. Mermin–Wagner ODLRO für jede endliche Reichweite aus, also auch mit t′.

**Lokal kann t′ aber helfen [H]:**

- Mehr Wege für die lokale Ersetzung, also höhere Erfolgswahrscheinlichkeit in Schritt 5.
- Bessere Perkolation freier Plätze: Mit Diagonalnachbarn liegt die Schwelle der Platzperkolation bei ≈ 0,407 statt 0,593 [Lit]. Umwege um blockierte Gebiete (Schritt 7, Thomson-Flüsse, eingefrorener Hintergrund) werden leichter.
- Für Bosonen bleibt t′ mit passendem Vorzeichen stoquastisch. Bei Fermionen bzw. im t-J-Modell bringt t′ Dreiecke und damit Vorzeichenstruktur ins Spiel; seine Rolle dort (Supraleitung gegen Streifen) ist Physik, keine Dimensionsfrage.

## 6. Nächste Schritte

1. Gitterfassung der Schritte 2–8 für 2D-Bosonen bei kleinem ρ mit **räumlichen** Routen aufschreiben. Erwartet: Alles überträgt sich bis auf Satz 7.1, wo die Begegnungen wie Σ s^{−α} divergieren. Das kontrolliert, dass wirklich nur die Zählung fehlt.
2. Raum-Zeit-Staffellauf konstruieren: Zeitschritt definieren, Satz 6.2 auf lange Fenster erweitern, Lemma 8.3 prüfen (offene Punkte 1–3). **Begonnen:** [einpunkt\_zeitroute.md](einpunkt_zeitroute.md), mit Umsteigen zwischen Linien als Zeitschritt und fünf Bausteinen, davon zwei [S] bzw. [Lit].
3. Numerik [N], billig: Erfolgswahrscheinlichkeit der lokalen Ersetzung (Schritt 5) auf dem 2D-Gitter als Funktion von ρ und t, mit und ohne t′. Das zeigt, bis zu welcher Dichte der Verdünnungsteil realistisch ist.
4. Familie 271 (Ferromagnet) unter derselben Frage lesen. Dort geht d ≥ 3 über Transienz der Wärmeleitung ein, also wieder eine Dimensionszählung.
