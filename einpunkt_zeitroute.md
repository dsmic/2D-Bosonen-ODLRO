# Einpunkt-Kriterium und zeitartige Routen

Begonnen 2026-11-09. Fortsetzung von [analyse\_familie267.md](analyse_familie267.md) §4 (offene Punkte 1 und 2), Teil von [weltlinien\_beweisobjekt.md](weltlinien_beweisobjekt.md). Kennzeichnung: [S] streng, [Lit] Literatur, [B] Beweisskizze, [N] numerisch, [H] Hypothese, [L] Lücke.

Kurz: Statt „Teilchen hier gegen Teilchen dort zur selben Zeit“ genügt ein Einpunkt-Vergleich: Bad um ein Teilchen gegen den Grundzustand mit einem Teilchen weniger. Er ist streng hinreichend, numerisch fast scharf, und in Weltlinien wird daraus eine Route in Zeitrichtung, deren Querrichtungen die beiden Raumrichtungen sind. Die Raum-Zeit ist dann ℤ³, und dort gibt es die Routen von Benjamini–Pemantle–Peres.

## 1. Einpunkt-Kriterium [S]

Bezeichnungen: Torus mit M Plätzen, ψ\_N > 0 Perron-Vektor (Grundzustand mit N Teilchen), ρ = N/M, b\_0 = M^{−1/2} Σ\_x b\_x, N₀ = ⟨b\_0⁺ b\_0⟩ (Besetzung von k = 0).

- **Faser bei x (Palm-Maß):** P\_x(S) = ψ\_N(S + x)² / ρ für (N−1)-Konfigurationen S ohne x. Normiert, weil Σ\_S ψ\_N(S + x)² = ⟨n\_x⟩ = ρ. Das ist das Bad, vom Teilchen bei x aus gesehen.
- **Vergleichsmaß:** Q(S) = ψ\_{N−1}(S)², der Grundzustand mit einem Teilchen weniger.

```text
H̄  :=  Σ_S √(P_x(S) Q(S))  =  Σ_{S ∌ x} ψ_N(S+x) ψ_{N−1}(S) / √ρ        (Affinität, unabhängig von x)

⟨ψ_{N−1} | b_0 | ψ_N⟩ = √N · H̄

N₀/N  ≥  H̄²                                  (Kondensatanteil)
ρ₁(x,y)/ρ  ≥  2 H̄² − 1     für alle x ≠ y     (punktweise, nützlich ab H̄² > 1/2)
```

Beweis. ψ\_{N−1} ist ein Einheitsvektor, also |⟨ψ\_{N−1}, b\_0 ψ\_N⟩|² ≤ |b\_0 ψ\_N|² = N₀. Die x-Summe in b\_0 gibt wegen Translationsinvarianz der Perron-Vektoren M gleiche Summanden. Punktweise: a\_x(S) = ψ\_N(S + x)/√ρ ist ein Einheitsvektor mit ⟨a\_x, a\_y⟩ = ρ₁(x,y)/ρ und ⟨a\_x, ψ\_{N−1}⟩ = H̄. Zerlegt man a\_x = H̄ ψ\_{N−1} + √(1 − H̄²) e\_x mit e\_x ⟂ ψ\_{N−1}, folgt ⟨a\_x, a\_y⟩ ≥ H̄² − (1 − H̄²). ∎

**Anschaulich.** Man nimmt bei x ein Teilchen heraus und fragt, ob der Rest wie der Grundzustand mit einem Teilchen weniger aussieht. Wenn ja (H̄ nicht klein), ist Kondensat da. Es gibt keinen zweiten Punkt y und keinen Abstand mehr, und die „Gleichzeitigkeit“ zweier Kopien (offener Punkt 1 in analyse\_familie267.md) tritt gar nicht auf.

**Prüfung am RK-Punkt.** ψ ist dort gleichverteilt, und es folgt H̄² = (M − N + 1)/M = N₀/N exakt.

## 2. Numerik: Das Kriterium verliert fast nichts [N]

Z₀ = N H̄² / N₀ ist das Quasiteilchengewicht bei k = 0. Exakt mit [einpunkt\_kriterium.py](einpunkt_kriterium.py):

| Modell     | L  | N  | ρ      | N₀/N    | H̄²      | Z₀      |
|------------|----|----|--------|---------|---------|---------|
| 2D         | 4  | 3  | 0,1875 | 0,85083 | 0,85041 | 0,99951 |
| 2D         | 4  | 4  | 0,25   | 0,78233 | 0,78143 | 0,99884 |
| 2D         | 4  | 8  | 0,5    | 0,53127 | 0,52776 | 0,99341 |
| 2D         | 5  | 5  | 0,2    | 0,79831 | 0,79735 | 0,99880 |
| 2D         | 6  | 4  | 0,111  | 0,87764 | 0,87723 | 0,99953 |
| 2D         | 6  | 6  | 0,167  | 0,80948 | 0,80850 | 0,99879 |
| 1D         | 8  | 2  | 0,25   | 0,78982 | 0,78982 | 1,00000 |
| 1D         | 16 | 4  | 0,25   | 0,60656 | 0,58929 | 0,97153 |
| 1D         | 28 | 7  | 0,25   | 0,48112 | 0,45548 | 0,94670 |
| 1D         | 8  | 4  | 0,5    | 0,53912 | 0,51977 | 0,96411 |
| 1D         | 16 | 8  | 0,5    | 0,39597 | 0,36840 | 0,93038 |
| 1D         | 24 | 12 | 0,5    | 0,32900 | 0,30093 | 0,91469 |
| Stufe A    | 8  | 3  | 0,0234 | 0,56108 | 0,54988 | 0,98003 |
| Stufe A    | 8  | 4  | 0,0312 | 0,35655 | 0,35119 | 0,98496 |

- **2D:** Z₀ ≈ 0,9988 bei ρ ≈ 0,17–0,25, praktisch unabhängig von L = 4, 5, 6. H̄² ist also gleich N₀/N bis auf 0,1 %. Die Worm-Werte für N₀/N bei großen L gelten damit auch für H̄².
- **1D:** H̄² fällt wie L^{−0,46…0,50}. Das passt zu Tonks (harte Bosonen in 1D, Exponent 1/(2K) = 1/2). Z₀ fällt nur langsam.
- **Stufe A (8×8):** Z₀ ≈ 0,98.

Aufrufe: `python einpunkt_kriterium.py --modell bosonen --L 6 --N 4 5 6`, `--modell bosonen1d --L 8 12 16 20 24 28 --rho 0.25`, `--modell stufe_a --L 8 --N 2 3 4`.

## 3. Weltlinien: halbunendliche Lücke und Route in Zeitrichtung

**Lücken-Green-Funktion [S].** G(τ) = ⟨b\_0 ψ\_N | e^{−τ(H\_{N−1} − E\_0(N−1))} | b\_0 ψ\_N⟩ ist vollständig monoton in τ:

```text
N₀ = G(0)  ≥  G(τ)  ↓  G(∞) = |⟨ψ_{N−1}|b_0|ψ_N⟩|² = N H̄²
```

Im Wurm ist G(τ) das Gewicht der Konfigurationen mit einer **Lücke der Länge τ**: Kopf und Schwanz liegen τ auseinander, über den räumlichen Abstand summiert. Eine Schranke „eine Lücke beliebiger Länge kostet nur O(1)“ ist also dasselbe wie H̄ ≥ c. Als Zustandssummen geschrieben: H̄ = Z\_halb / √(Z\_voll Z\_leer). Die Linie durch (x, 0) endet dort, läuft ganz durch, oder fehlt.

**Geometrie [B].** Die Lücke läuft in Zeitrichtung nach oben (oder unten). Ihre Querrichtungen sind die beiden **Raum**richtungen. Bei T = 0 ist die Raum-Zeit eines 2D-Gitters ℤ² × ℤ ≅ ℤ³, und Routen mit gemeinsamem Start ins Unendliche sind genau die Situation des ursprünglichen Satzes von Benjamini–Pemantle–Peres: ℤ³ hat Zufallspfade mit exponentiellen Schnittschwänzen (EIT), ℤ² nicht [Lit].

| Fall      | Raum-Zeit der Route         | EIT?                                 | H̄ (numerisch)     | Physik      |
|-----------|-----------------------------|--------------------------------------|-------------------|-------------|
| 2D, T = 0 | ℤ² × ℤ ≅ ℤ³                 | ja (BPP)                             | ≈ √(N₀/N), stabil | ODLRO       |
| 1D, T = 0 | ℤ × ℤ ≅ ℤ²                  | nein (BPP)                           | → 0 wie L^{−1/4}  | kein ODLRO  |
| 2D, T > 0 | ℤ² × [0, β], Platte         | nein (Keile: Häggström–Mossel) [Lit] | —                 | kein ODLRO  |

Das ist die saubere Form von „imaginäre Zeit als zweite Querrichtung“ (analyse\_familie267.md §4). Die Route schreitet jetzt in τ voran, beide Querrichtungen sind räumlich, und die Rolle der Zeit ist eindeutig.

## 4. Zeitartiger Staffellauf: Skizze und Lücken

**Mechanismus [B].** Bei ununterscheidbaren Bosonen ist nicht festgelegt, *welche* Linie während der Lücke fehlt; nur (N−1)-Geschichte und Enden zählen. Für den Beweis wählt man den Verlauf:

- Die herausgenommene Strecke folgt einer physikalischen Linie. Das kostet nichts, sie wandert aber nur diffusiv (Abstand ~ √τ).
- Wo zwei Linien benachbart sind, **steigt sie um**. Ein eingefügter Sprung verbindet das untere Stück der einen mit dem oberen Stück der anderen. Das ist eine lokale Änderung mit O(1)-Kosten.
- Durch gezieltes Umsteigen lässt sich die Strecke längs einer vorgegebenen Route steuern, auch superdiffusiv. Nötig ist das: Zwei diffusive Strecken mit 2 Querrichtungen begegnen sich ~ Σ 1/τ mal (logarithmisch divergent). Bei Querschwankung τ^{3/4} wie bei BPP sind es ~ Σ τ^{−3/2}, also endlich viele.

**Bausteine.**

1. **Raum-Zeit-Markov-Eigenschaft [S].** Das Gitter-Weltlinienmaß hat ein Gewicht aus Nächstnachbar-Faktoren: Sprünge, harter Kern und e^{∫D} mit D = Zahl erlaubter Sprünge als Paarsumme. Gegeben die Konfiguration auf dem Rand eines Raum-Zeit-Blocks, ist das Innere vom Äußeren unabhängig. Das ersetzt Satz 6.2 des Preprints (exakte bedingte Produktstruktur), und zwar **ohne** Beschränkung auf kurze Zeitfenster.
2. **Löschen und Umsteigen in einer Zelle [L].** Gegenstück zu Satz 5.3: Kosten und Erfolgswahrscheinlichkeit pro Raum-Zeit-Zelle. Hier geht die Verdünnung ein. Zellen müssen groß gegen den Teilchenabstand sein, damit Linien zum Umsteigen da sind.
3. **Aufhebung fern von Begegnungen [L].** Gegenstück zu Lemma 8.3, über Baustein 1 und bedingt normierte lokale Faktoren.
4. **Routen [Lit].** EIT-Pfade in ℤ³ (BPP), dazu Umwege um schlechte Zellen mit Peierls-Schranke in Raum-Zeit.
5. **Normierung durch das chemische Potential [L], neu gegenüber dem Preprint.** Eine Lücke der Länge τ kostet im Mittel e^{−(E\_0(N−1) − E\_0(N))τ}. Die lokalen Faktoren müssen diese Normierung zellweise tragen. Im Preprint bleibt die Teilchenzahl beim Staffellauf erhalten. Weiter in §8: Die Selbstvarianz hebt sich auf; nötig ist dann eine Dekorrelationsschranke oder eine exakt normierte Variante.

**Warnung: ganze Linien vergleichen genügt nicht [S + H].** Auf Pfadebene ist das Bad unter P\_x gleich Q, gekippt mit W\_x(ω)/E\_Q W\_x. Dabei ist W\_x die Zustandssumme einer zusätzlichen Linie durch (x, 0) im Bad ω, also ein gerichtetes Polymer in einer Raum-Zeit-Umgebung [S]. Daraus folgt H̄ ≥ E\_Q √(W/EW) ≥ (E W² / (E W)²)^{−1/2} [S]. Aber zwei unabhängige Kopien der physikalischen Linie begegnen sich wie zwei Irrfahrten in ℤ², also rekurrent. Das zweite Moment divergiert vermutlich, und wahrscheinlich geht sogar E √(W/EW) → 0, analog zur starken Unordnung gerichteter Polymere in 2+1 Dimensionen [H]. Pfadebene und Zeitscheibe sind verschieden: Erst die frei gewählten, superdiffusiven Routen machen das Argument möglich. Das ist dieselbe Lehre wie im Preprint.

## 5. Gegenprobe: Starrheit des Punktprozesses |ψ|²

H̄ misst, ob man dem Rest ansieht, dass bei x ein Teilchen fehlt. P\_x ist dabei das Palm-Maß, und es ist zugleich das invariante Maß des Prozesses „Umgebung vom markierten Teilchen aus gesehen“ (Kipnis–Varadhan) [S].

**Obstruktion [S].** Für jede Statistik F, etwa linear F(S) = Σ\_{s∈S} φ(s), mit Mittelwertdifferenz δ = E\_Q F − E\_P F und Streuungen σ\_P, σ\_Q gilt:

```text
H(P, Q)  ≤  2 (σ_P + σ_Q) / |δ|
```

Beweis: Tschebyschow auf der Menge {F ≤ Mitte}, dazu √(P(A)Q(A)) ≤ √Q(A).

Mit φ ≈ 1 um x herum, langsam abfallend, ist |δ| ≈ 1 (Korrelationsloch, Summenregel bei fester Teilchenzahl). Dazu gilt σ² ≈ ∫ |φ̂(k)|² S(k) dk.

| Fall                                  | S(k) klein k | beste σ²                                         | Folge                     | Physik                                      |
|---------------------------------------|--------------|--------------------------------------------------|---------------------------|---------------------------------------------|
| 1D, Phononen                          | ~ \|k\|      | → 0 wie 1/log R (Log-Profil)                     | starr, H̄ → 0             | kein ODLRO                                  |
| 2D, Phononen                          | ~ \|k\|      | ≥ const (H^{1/2}-Kapazität einer Kugel in 2D > 0) | keine Obstruktion         | ODLRO                                       |
| 2D, Coulomb-Plasma (\|Laughlin\|²)    | ~ k²         | → 0 (Log-Profil, Dirichlet-Energie)              | starr, H̄ → 0             | nur algebraisch (Girvin–MacDonald) [Lit]    |
| 3D, Phononen                          | ~ \|k\|      | wächst                                           | keine Obstruktion         | BEC                                         |

Die Zählung ist dieselbe wie bei den Routen. S ~ |k| in d Dimensionen ist die Spur eines masselosen Feldes in d + 1 Dimensionen (H^{1/2}(ℝ^d) = Spur von H¹(ℝ^{d+1})). Starr bedeutet, dass das Fehlen eines Teilchens von weit weg erkennbar ist. Das ist genau dann der Fall, wenn die Raum-Zeit-Kapazität verschwindet, also d + 1 ≤ 2.

Literatur zur Starrheit [Lit, Details noch prüfen]: Ghosh–Peres (Ginibre und Nullstellen der Gaußschen analytischen Funktion sind zahlstarr), Ghosh (Sinus-Prozess starr), Ghosh–Lebowitz (Starrheit superhomogener Punktfelder in d ≤ 2), Holroyd–Soo (Einfüge- und Löschtoleranz).

**Einordnung.** Ziel ist „Löschtoleranz in Affinität“: Palm-Maß und (N−1)-Grundzustand sind gleichmäßig nicht singulär. Starrheit ist das Gegenteil und erklärt, *warum* es in 1D und beim Laughlin-Plasma scheitert. Der Satz selbst ist die schwere Richtung.

## 6. Bilanz

- **Gewonnen:**
    - Offener Punkt 1 (Gleichzeitigkeit) ist erledigt [S].
    - Die Zielgröße H̄ ist streng hinreichend und numerisch fast scharf (Z₀ ≈ 0,999 in 2D).
    - Die Raum-Zeit ist ℤ³, BPP ist direkt anwendbar.
    - Die Markov-Eigenschaft in Raum-Zeit ersetzt die Kurzzeit-Produktstruktur [S].
    - Die Starrheits-Gegenprobe erklärt 1D und Laughlin.
- **Offen [L]:**
    - Bausteine 2, 3 und 5.
    - Verdünnungsabschätzungen in 2D.
    - Das Kriterium selbst gilt für alle Dichten; nur der Staffellauf-Beweis braucht Verdünnung (kleine ρ, über Teilchen ↔ Loch auch ρ nahe 1). Stufe A bei 7/8 bleibt außerhalb.

## 7. Nächste Schritte

1. Baustein 2 als Lemma für kleine ρ formulieren: eine Raum-Zeit-Zelle, Löschen und Umsteigen, bedingt auf den Rand (Baustein 1).
2. Numerik [N], nach Ende der laufenden Wurm-Läufe: G(τ) bei k = 0 im Wurm messen (Zeitabstand Kopf–Schwanz, Erweiterung K2) für L = 16, 32. Das liefert H̄² direkt bei großen L und den Abfall von N₀/N nach H̄². **Stand 2026-11-10:** hist\_tau im Wurm eingebaut und gegen exakt geprüft (χ² = 18 bei 15 Freiheitsgraden). Die Läufe L = 16/32, ρ = 1/16 und 1/8 starten automatisch nach Runde 1 (siehe README).
3. Baustein 5 klären: Lässt sich die Normierung e^{−μτ} in bedingt normierte Zellfaktoren zerlegen? Erst am RK-Punkt (H̄ exakt bekannt), dann bei kleinem ρ.
4. Den früheren Schritt „Ersetzungserfolg gegen ρ, mit und ohne t′“ (analyse\_familie267.md §6.3) als „Umsteige-Erfolg pro Zelle“ in Schritt 1 aufnehmen.

## 8. Kostenbilanz: Selbstvarianz hebt sich auf, Kreuzterme bleiben (2026-11-10)

**Problem (Baustein 5).** Beim Preprint ist jeder lokale Faktor ein Quotient bedingter Wahrscheinlichkeiten *desselben* Systems, mit bedingtem Mittel genau 1. Bei uns ändert die Lücke die Teilchenzahl. Der Löschfaktor einer Zelle hängt von der Umgebung ab, etwa über die Zahl der Nachbarn der gelöschten Linie. Sein Produkt längs einer Route der Länge n hat eine Log-Varianz ~ n, und das sieht zunächst tödlich aus.

**Rechnung [B, Gauß-Näherung].** ν entsteht aus P durch Staffellauf längs einer Zufallsroute R, also dν/dP = E\_R[Π\_{c∈R} f\_c]. Lemma 8.1 braucht nur das Verhältnis

```text
m² / C_P  =  (E_R E_P Π_{c∈R} f_c)²  /  E_{R1,R2} E_P[ Π_{c∈R1} f_c · Π_{c∈R2} f_c ]
```

Mit log f\_c gaußisch, Kovarianz K(c, c′), gilt:

```text
Zähler   ~  exp( Σ_{c,c′∈R1} K + Σ_{c,c′∈R2} K ) · exp(2 Σ log-Mittel)
Nenner   ~  exp( Σ_{c,c′∈R1} K + Σ_{c,c′∈R2} K + 2 Σ_{c∈R1, c′∈R2} K ) · exp(2 Σ log-Mittel)
m²/C_P   ~  1 / E_{R1,R2} exp( 2 Σ_{c∈R1, c′∈R2} K(c, c′) )
```

Die Selbstterme (Varianz ~ n) kürzen sich vollständig. Das gilt, solange die Routen gerichtet sind, also nicht zu sich selbst zurückkehren; dann ist Σ\_{R1×R1} K für alle Routen gleich bis auf O(1). Übrig bleiben nur **Kreuzterme zwischen zwei unabhängigen Routen**: Kontakt (gemeinsame Zellen) und Fernkorrelation.

**Exponentenbedingung [B].** Route mit Querschwankung ~ s^α in q Querrichtungen, lokale Kosten mit Kovarianz ~ R^{−a} in Raum-Zeit:

```text
Kontakt:           Σ_s P(|X1(s) − X2(s)| ≤ 1)   ~  Σ_s s^{−qα}          endlich  ⇔  qα > 1
Fernkorrelation:   Σ_s Σ_{s′} R(s,s′)^{−a}       ~  Σ_s s^{−α(a−1)}      endlich  ⇔  α(a−1) > 1
Phononen bei T = 0, d Raumdimensionen:  a = d + 1 (Dichtekorrelation in Raum-Zeit),  q = d
→ beide Bedingungen werden zu  α · d > 1
```

| d (T = 0)      | physikalische Linien (α = 1/2) | gewählte Routen (α ≤ 1)       | Kondensat |
|----------------|--------------------------------|-------------------------------|-----------|
| 1              | divergent                      | divergent (bräuchte α > 1)    | nein      |
| 2              | **grenzwertig** (logarithmisch) | endlich für α > 1/2, z. B. 3/4 | ja        |
| 3              | endlich                        | endlich                       | ja        |

**Folgerungen.**

- Die Polymer-Warnung aus §4 ist der Fall α = 1/2 derselben Formel: In 2D ist er genau grenzwertig. Superdiffusive Routen (Umsteigen) sind also nötig und auch hinreichend, und zwar für Kontakt *und* Fernkorrelation zugleich.
- In 3D bei T = 0 würden schon die physikalischen Linien genügen. Dort könnte der Polymer-Ansatz H̄ ≥ (E W²/(E W)²)^{−1/2} direkt tragen (L²-Bereich gerichteter Polymere in d ≥ 3). Das ist nicht unser Ziel, aber ein Hinweis, dass die Schranke vernünftig ist.
- Baustein 5 ist damit **kein grundsätzliches Hindernis**. Er macht aber aus der exakten Aufhebung des Preprints eine näherungsweise: Gebraucht wird eine **Dekorrelationsschranke** |Cov| ≲ R^{−a} mit a > 1 + 1/α (für α = 3/4: a > 7/3) für lokale Funktionale des Weltlinienensembles. Physikalisch ist a = 3 [H]. Streng ist das eine Aussage über Phononen-Korrelationen bei T = 0 und für sich schwer [L].
- **Ausweg gesucht [L]:** ein Staffellauf, dessen Zellfaktoren *exakt* bedingt normiert sind, trotz Änderung der Teilchenzahl. Dann bräuchte man keine Dekorrelation, sondern nur Kontaktzählung (BPP). Kandidat: Die Lücke wird nicht gelöscht, sondern in jeder Zelle aus dem bedingten (N−1)-Gesetz neu gezogen. Der Faktor ist dann ein Quotient bedingter Zustandssummen Z^{(N−1)}/Z^{(N)} des Zellrands, dessen Schwankung wieder Kreuzterme gibt. Noch nicht klar, ob das besser ist.

**Teleskop-Variante [S + H].** Wegen der Monotonie gilt log(N H̄²/N₀) = Σ\_T log(G(T+1)/G(T)). Jeder Quotient ist ein Erwartungswert im Ensemble mit Lücke der Länge T, nämlich der Kosten, die Lücke am Kopf um eine Einheit zu verlängern. Das ist ein Produkt von *Erwartungswerten*, nicht der Erwartungswert eines Produkts, und es entsteht keine Varianzanhäufung. Gebraucht wird 1 − G(T+1)/G(T) ≲ T^{−1−ε}: Der Kopf spürt den Schwanz im Zeitabstand T nur summierbar schwach. Spektral heißt das, dass das Anregungsgewicht im Entnahmespektrum bei k = 0 nahe ε = 0 schwach genug ist. Das ist eine Relaxationsaussage. Sie ist nicht offensichtlich leichter, aber ohne Routen formuliert, also ein zweiter Zugang.

## 9. Literatur-Nachtrag (2026-11-10, nach Regel 5 der Beweissuch-Lehren)

**Neue OpenAI-Preprints derselben Familie [Lit, ungeprüfte Downloads, nur Einleitung und Kernabschnitte gelesen].** Das Repository github.com/openai/math hat inzwischen rund 750 Preprints. Für uns einschlägig:

| Preprint (Datum)                                                        | Aussage                                                                                     | für uns                                                                 |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| A density-uniform condensate bound for dilute Bose gases (2026-09-27)   | 3D, beschränktes Potential: Kondensatanteil q₀ ≥ c gleichmäßig in kleiner Dichte und 0 ≤ T ≤ ρ² | misst direkt k = 0; **„reverse insertion“** löst das Längenproblem       |
| BEC at positive temperature in the dilute hard-sphere gas (2026-10-05)   | 3D harte Kugeln, BEC bei T > 0                                                              | dieselbe Maschinerie, thermische Zeitscheibe                            |
| Quantum depletion (hard spheres; bounded potentials) (2026-10-05)        | Bogoliubov-Verarmung 8/(3√π) √(ρa³) streng, 3D                                               | zeigt, wie weit die Methode trägt                                       |
| Planar XY (mehrere, 2026-09/10)                                          | BKT-Universalität, kritische Exponenten, klassisch 2D                                       | 2D bei T > 0 (kein ODLRO), nicht unser Fall                             |

**Wie die dichte-uniforme Schranke vorgeht (§1.2, §9, §10 dort).**

- **Größe:** Ein Endpunkt eines Weges wird durch einen gleichverteilten Raumpunkt z ersetzt. Das ergibt ein positives Maß μ mit Masse q₀ (Besetzung der konstanten Mode).
- **Konstruktion:** ν entsteht durch einen Staffellauf längs eines zufälligen Zellpfades. Je Zelle wird ein Teilchen ausgewählt, die Startpunkte werden zyklisch weitergereicht, und die gewählten Brücken werden aus ihrem *exakt normierten* bedingten Gesetz neu gezogen.
- **Ergebnis:** Cauchy–Schwarz gibt a² ≤ q₀ ∫ f² dμ.
- **Der entscheidende Satz dort:** „Estimating both changes against the original closed configuration would incur a cost proportional to their lengths. Instead, a reverse insertion supplies a baseline in which contributions far from encounters cancel.“
- **Rückwärts-Zustand B:** Er öffnet das *letzte* Label der Route am anderen Ende. Auf den nicht geteilten Stücken j = I \ (geteilt ∪ Vorgänger) und l = I′ \ geteilt gilt C\_j = O\_j, B\_j = Ĉ\_j, B\_l = C\_l, Ĉ\_l = O\_l. Die bedingten Normierer kürzen sich exakt; Kosten bleiben nur bei geteilten Labels (≤ e^{C|h|}) und bei nahen verschiedenen Brücken (→ 0 mit der Verdünnung).
- **Teilchenzahl:** Diese Konstruktion erhält sie, weil nur ein Ende versetzt wird.

**Folgerung für §8 [H].** Die „reverse insertion“ ist genau der gesuchte Ausweg *im teilchenzahlerhaltenden Fall*. Damit ist exakte Aufhebung ohne Dekorrelationsschranke möglich. Offen ist, ob die Buchführung auch für die Lücke trägt, also für den zeitartigen, teilchenzahländernden Fall. Prüfauftrag: die Tabelle aus §10.1 dort für „Linie vorhanden gegen fehlend“ längs zweier Zeitrouten nachrechnen. Wenn sich auf j und l je ein Faktor „mit Lücke“ und einer „ohne Lücke“ mit gleichem Rand gegenüberstehen, kürzt sich auch die Normierung durch das chemische Potential exakt, und Baustein 5 entfällt.

**Abstammung der Methode [Lit].** Ein Werkzeug für d ≥ 3, das nicht aus der Physik kommt:

- Benjamini–Pemantle–Peres (Ann. Probab. 1998, arXiv math/9701227): ein Maß auf *orientierten* Pfaden in ℤ³ mit exponentiellem Schwanz der Schnittzahl. Zwei gleichverteilte orientierte Pfade schneiden sich dagegen unendlich oft.
- Häggström–Mossel (Ann. Probab. 1998): Pfade mit geringer Vorhersagbarkeit, hierarchische Drift; Vorbild der dyadischen Geschwindigkeiten im Preprint.
- Abbe–Massoulié–Montanari–Sly–Srivastava, Group synchronization on grids (Math. Stat. Learn. 2018, arXiv 1706.08561): schwache Rekonstruktion für d ≥ 3 bei kleinem Rauschen, für kontinuierliche Gruppen in d = 2 unmöglich.
- Garban–Spencer, Continuous symmetry breaking along the Nishimori line (arXiv 2109.01617): kontinuierliche Symmetriebrechung für S¹-, SU(n)- und SO(n)-Spins in d ≥ 3 ohne Reflexionspositivität, über AMMSS plus Nishimori-Eichinvarianz.

**Einordnung.** Die Methode ist „Synchronisation durch Pfadmittel“ und von Natur aus ein Werkzeug für d ≥ 3. Unser Problem (Quanten-2D bei T = 0) ist in Raum-Zeit ein *klassisches* 3D-Problem. Ein Argument vom Garban–Spencer-Typ in Raum-Zeit ist daher die natürliche Fortsetzung, und das ist genau das zeitartige Programm dieses Dokuments. Anders als bei Garban–Spencer fehlt eine Eichinvarianz, die das Rauschen kontrolliert; ihre Rolle übernehmen bei uns die exakte Positivität (Perron) und die Verdünnung.

**Weitere Punkte [Lit].**

- **Gerichtete Polymere in 2+1 Dimensionen:** Sie sind marginal. Der Übergang schwach–stark liegt auf der feineren Skala β = β̂/√R\_N mit β̂\_c = 1, wo die L²-Norm explodiert (Caravenna–Sun–Zygouras, AAP 2017). Das passt zu „physikalische Linien grenzwertig“ in §8.
- **Starrheit:** Ghosh–Lebowitz (J. Stat. Phys. 166, 2017, arXiv 1601.04216) geben hinreichende Bedingungen für Zahlstarrheit in d = 1, 2 über den Abfall der Korrelationen; Übersicht arXiv 1608.07496. Die genaue 2D-Bedingung ist noch nachzulesen.
- **Harte Bosonen abseits halber Füllung:** Die Suche fand keinen strengen 2D-Beweis. Frühere strenge ODLRO-Resultate gibt es nur bei halber Füllung (Grundzustand d ≥ 2, T > 0 in d ≥ 3), siehe die Einleitung von cond-mat/0011334. Tasaki–Watanabe (arXiv 2105.10692) zeigen: ODLRO erzwingt eine verschwindende Ladungslücke.

## 10. Reverse insertion für die Lücke: Gegen-Lücke als Bezug [B]

Übertragung von §10.1 der dichte-uniformen Schranke auf den zeitartigen, teilchenzahländernden Fall.

**Zustände.**

- C ist geschlossen (N Linien).
- O ist die Hin-Änderung: Längs der Route R′ wird in jeder Zelle ein Linienstück gelöscht und aus dem exakt normierten bedingten (N−1)-Gesetz neu gezogen, zusammen mit dem Umsteigen an den Zellgrenzen. Das ergibt eine Lücke.
- Die Dichte f(O) wird mit einer unabhängigen Route R ausgewertet. Ihr hypothetischer geschlossener Zustand ist Ĉ = O mit wieder eingefügter Linie längs R.

Die naheliegende Wahl „B = Lücke längs R“ passt nicht: Auf j hätte B lokal N−1 Linien, Ĉ aber N+1. Richtig ist die **Gegen-Lücke**:

| Zustand | längs R \ R′ (j)     | längs R′ \ R (l)     | sonst |
|---------|----------------------|----------------------|-------|
| C       | N                    | N                    | N     |
| O       | N (= C)              | N − 1 (Lücke)        | N     |
| Ĉ       | N + 1 (O + Linie)    | N − 1 (= O)          | N     |
| B       | N + 1 (C + Linie)    | N (= C)              | N     |

Wie im Preprint gilt C\_j = O\_j, B\_j = Ĉ\_j, B\_l = C\_l, Ĉ\_l = O\_l. Fern von Begegnungen sind auch die Ränder der Zellen gleich. Deshalb stehen sich auf j und l bedingte Zustandssummen mit *gleicher* Teilchenzahl und *gleichem* Rand gegenüber und kürzen sich exakt. Die Normierung durch das chemische Potential (Baustein 5) taucht damit gar nicht als schwankender Faktor auf. Es bleiben:

1. Kosten auf geteilten und nahen Zellen: Löschen und Einfügen in derselben Zelle, lokal beschränkt bei Verdünnung, ≤ e^{C·J} mit J = Zahl der nahen Begegnungen. Mit BPP-Routen in ℤ³ hat das ein beschränktes exponentielles Moment.
2. Die globale Bilanz, nachgerechnet unten: Sie fällt günstig aus.

**Globale Bilanz [B] (2026-11-10, korrigiert die erste Fassung).** Normierung wie im Preprint: Der Kopf der Lücke wird mit der *normierten* Gleichverteilung dz/V integriert, μ hat die Masse G̃⁻(T). Das ist die Lücken-Green-Funktion bei k = 0 ohne Abzug von E₀(N−1), pro Teilchen normiert. ν ist das Bild des geschlossenen Wahrscheinlichkeitsmaßes unter dem Staffellauf längs R′, mit Masse a (Annahmewahrscheinlichkeit).

- **Dichte.** f\_R(O) = Z^{+1}\_R(∂O)/Z^{0}\_R(∂O) mal Auswahl- und Routenfaktoren. Das ist das Verhältnis der bedingten Zustandssummen im Schlauch um R mit einer zusätzlichen Linie und ohne, bei festem Rand aus O. Grund: Jedes O mit N−1 Linien je Zeitscheibe entsteht aus einem geschlossenen Ĉ = O + Linie längs R, und der Löschkern ist exakt bedingt normiert.
- **Fernanteil exakt.** Liegt R fern von R′, ist O = C im Schlauch um R und auf dessen Rand. Dann gilt:

```text
E_C[ f_R(O) ]  =  Σ_{C außen} W(C_außen) Z^{+1}_R(∂C) / Z   =   Masse der Gegen-Lücke längs R   (=: Ğ⁺_R)
```

- **Zweites Moment.** ∫ f² dμ = ∫ f dν ≲ E\_{R,R′}[ Ğ⁺\_R · e^{C·J(R,R′)} ]. Die nahen und geteilten Zellen liefern e^{C·J} (Baustein 2).
- **Zusammen:**

```text
a²  ≤  G̃⁻(T) · Ğ⁺(T) · E[e^{CJ}]  =  G⁻(T) G⁺(T) · e^{−Δ₂ T} · E[e^{CJ}]
Δ₂ = E₀(N+1) + E₀(N−1) − 2E₀(N) ≈ 1/(κM) ≥ 0,    G^± = mit Abzug der Grundzustandsenergien, G⁺ ≤ G⁺(0) ≤ 1
⇒  G⁻(T) ≥ a² / E[e^{CJ}]     ⇒     N₀/N ≥ G⁻(T)   (Monotonie, §3)
```

**Folgerungen.**

- Der Restfaktor e^{−Δ₂T} steht auf der *guten* Seite. Eine Bedingung T ≪ κM ist nicht nötig. Selbst bei Δ₂ < 0 kostete er nur e^{O(T/M)}.
- Nebenbei folgt dieselbe Schranke für die Hinzufüge-Seite G⁺; das Argument ist symmetrisch.
- **Wahl von T.** Wie im Preprint muss der Kopf wie dz/V verteilt sein, sonst wird f groß. Die Route führt deshalb von der Zelle des Schwanzes (Zeit 0) zur Zelle eines unabhängig gleichverteilten Punktes z (Zeit T). Mit T ~ L ist sie zeitartig mit räumlichem Versatz ~ L, ein orientierter BPP-Pfad in ℤ³ zwischen zwei Endpunkten. Die Wahl T ~ L^{4/3} aus der ersten Fassung ist unnötig.
- **Gegenprobe 1D:** Dieselbe Rechnung braucht beschränkte Begegnungsmomente orientierter Pfade der Länge ~L in ℤ². Die gibt es nicht (Σ s^{−α} wächst), also folgt nichts, wie es sein muss. Für festes T wäre die Begegnungszahl auch in 1D beschränkt, aber dann ist der Kopf nicht gleichverteilt, und f explodiert. Dieser Fehlschluss lag nahe und ist hiermit ausgeschlossen.
- E\_R[(Ğ⁺\_R)²] ≲ (Ğ⁺)² braucht noch eine Rechtfertigung: Gegen-Lücken-Massen längs verschiedener Routen gleicher Länge sind vergleichbar (Translationsinvarianz, lokale Kosten) [L, klein].

**Stand.** Baustein 5 ist damit auf Beweisskizzen-Niveau ohne Dekorrelationsschranke erledigt. Die tragenden offenen Punkte sind Baustein 2 (lokale Konstante C für Löschen, Einfügen und Umsteigen in derselben Zelle; Peierls-Schranke für schlechte Zellen bei kleinem ρ) und Baustein 3 in der Form „Fernanteil exakt“, also die genaue Schlauch- und Randbuchführung.

## 11. Numerik: Begegnungen der Skelette (2026-11-10) [N]

[skelett\_begegnungen.py](skelett_begegnungen.py) baut die Skelette der dichte-uniformen Arbeit (§8.1 dort) nach. Die erste Koordinate ist bei uns die imaginäre Zeit, die Querrichtungen sind räumlich. Gezählt wird J = Zahl der Zeiten, zu denen zwei unabhängige Skelette mit gleichen Endpunkten höchstens R = 1 Zelle auseinander liegen, für beide Hälften. α\_max ist die Schwanzrate aus P(J ≥ n) ~ e^{−α\_max n}; E e^{αJ} ist genau für α < α\_max beschränkt. Je Punkt 20 000 Paare.

Skala 1 (Normierung des Preprints, Querschritt |v| ≤ ½):

| Fall                        | E J bei w = 64 / 256 / 1024 / 4096 / 16384 | Verhalten               | α\_max bei großem w |
|-----------------------------|--------------------------------------------|-------------------------|---------------------|
| 2 Querrichtungen, dyadisch  | 50 / 75 / 83 / 86 / 85                     | beschränkt              | 0,012, stabil       |
| 2 Querrichtungen, diffusiv  | 32 / 54 / 77 / 101 / 124                   | ~ log w (marginal)      | → 0                 |
| 1 Querrichtung, dyadisch    | 57 / 127 / 225 / 363 / 548                 | ~ w^{0,30} (Theorie ¼)  | → 0                 |
| 1 Querrichtung, diffusiv    | 45 / 109 / 238 / 499 / 1036                | ~ w^{0,52} (Theorie ½)  | → 0                 |

Skala 8 (Querschritte × 8, also 8 Raumzellen je Zeitschritt):

| Fall                        | E J bei w = 64 / 256 / 1024 / 4096 / 16384 | α\_max              |
|-----------------------------|--------------------------------------------|---------------------|
| 2 Querrichtungen, dyadisch  | 6,9 / 6,9 / 6,9 / 6,9 / 6,8                | 0,17, stabil        |
| 1 Querrichtung, dyadisch    | 16 / 25 / 36 / 52 / 76                     | 0,16 → 0,017        |

**Lesart.**

- Die Zählung aus §3 und §8 ist bestätigt. Mit zwei Querrichtungen (2D bei T = 0, Route in Zeitrichtung) bleibt J beschränkt, mit einer (1D, oder räumliche Routen in 2D) wächst es wie eine Potenz. Physikalische, also diffusive Linien sind in 2D genau marginal.
- **α\_max ist das Budget für Baustein 2:** Die lokalen Kosten G je Begegnung (geteiltes Label, nahe verschiedene Brücken, Löschen und Einfügen in derselben Zelle) müssen log G < α\_max erfüllen. Bei Skala 1 sind das nur ≈ 1,2 % Mehrkosten je Begegnung, bei Skala 8 schon ≈ 18 %. Fast alle Begegnungen liegen an den beiden gemeinsamen Endpunkten.
- **Die Skala ist bei uns frei:** Raumzellen je Zeitschritt ist eine Wahl der Zellgeometrie. Eine längere Zeitzelle δ lässt die Linien weiter wandern (~ √δ), große Querschritte kosten also nicht automatisch mehr Umsteigen. Der Preis sind mehr Linienstücke je Zelle. Ob das die lokalen Kosten senkt oder hebt, muss die Messung in Baustein 2 zeigen [L].
- **Nächste Messung (Baustein 2):** Kosten von Löschen, Einfügen und Umsteigen je Raum-Zeit-Zelle aus Wurm-Schnappschüssen, als Funktion von ρ, Zellgröße s und Zeitlänge δ. Verglichen wird mit dem Budget α\_max(Skala).

## 12. Gleichzeitige „lokale“ Einfügekosten sind global (2026-11-10) [S + N]

Versuch einer billigen Vorstufe zu Baustein 2 mit [lokale\_einfuegung.py](lokale_einfuegung.py): relative Varianz G − 1 des Einfügeverhältnisses f\_c(S) = Σ\_{x∈c} ψ\_N(S+x)/ψ\_{N−1}(S) unter Q = ψ\_{N−1}², für Zellen c aus s×s Plätzen. Dazu analog die Löschseite unter ψ\_N².

**Identität [S].** Mit u\_c = Σ\_{x∈c} b\_x ψ\_N gilt |u\_c|² = Σ\_{x,y∈c} ρ₁(x,y) und ⟨ψ\_{N−1}, u\_c⟩ = |c| √ρ H̄ (Translationsinvarianz). Also:

```text
G_ein(c) = Σ_{x,y∈c} ρ₁(x,y) / (|c|² ρ H̄²),        ein Platz:  G_ein − 1 = 1/H̄² − 1,        c = alles:  G_ein = 1/Z₀
G_los(c) = Σ_{x,y∈c} ⟨b_x b_y⁺⟩_{N−1} / (|c|² ρ H̄²),   ein Platz:  ≈ (1 − ρ)/(ρ H̄²)   (der Term „1/m“)
```

Numerisch bestätigt: 6×6 mit N = 4 gibt 1/0,87723 − 1 = 0,1400 (gemessen 0,1400), 1D mit L = 24 und N = 6 gibt 1,0426 (gemessen 1,0426).

| Fall               | ρ     | G\_ein − 1 bei s = 1 / 2 / 3       | G\_los − 1 bei s = 1 / 2 / 3 |
|--------------------|-------|------------------------------------|------------------------------|
| 2D 6×6, N = 4      | 0,111 | 0,140 / 0,077 / 0,039              | 8,4 / 1,96 / 0,75            |
| 2D 6×6, N = 6      | 0,167 | 0,237 / 0,119 / 0,059              | 5,4 / 1,29 / 0,51            |
| 1D L = 16, N = 4   | 0,25  | 0,70 / 0,62 / (s = 4) 0,44         | 4,5 / 2,4 / (s = 4) 1,2      |
| 1D L = 24, N = 6   | 0,25  | 1,04 / 0,94 / (s = 4) 0,72         | 5,5 / 3,0 / (s = 4) 1,7      |

**Lehre.** Der gleichzeitige Vergleich mit dem (N−1)-Grundzustand ist *nicht lokal*: Er enthält die globale Affinität H̄ und wächst deshalb in 1D mit L. Echte lokale Kosten für Baustein 2 müssen **auf den Rand einer Raum-Zeit-Zelle bedingt** sein, also Quotienten Z^{±1}\\_c(∂)/Z^{0}\\_c(∂) bei festem Rand (Markov-Eigenschaft, Baustein 1). Diese hängen nur vom Rand ab. Die Messung braucht deshalb zuerst die genaue Konstruktion des Staffellaufs (welche Linienstücke, wie umgestiegen wird, was zum Rand gehört), erst dann ist die Größe wohldefiniert. Der Löschterm ~ 1/m (m = Teilchen je Zelle) ist dagegen echt lokal und verlangt Zellen mit m ≳ 1/α\_max Teilchen.

**Nächster Schritt (Theorie vor Messung).** Den zeitartigen Staffellauf auf dem Gitter genau aufschreiben, analog zu §9 der dichte-uniformen Arbeit: Grundgesetz, Annahme, Auswahl eines Linienstücks je Raum-Zeit-Zelle, exakt normierter bedingter Vorschlag, Gegen-Lücken-Zustand. Danach die Randquotienten mit einer Transfermatrix auf kleinen Kästen (Weg 1) messen, mit Rändern aus Wurm-Konfigurationen.

## 13. Gitterkonstruktion des zeitartigen Staffellaufs (2026-11-10) [B, Lücken markiert]

Analog zu §9 der dichte-uniformen Arbeit, für harte Bosonen auf (ℤ/Lℤ)², H = −A, Zielgröße G⁻(T) mit gleichverteiltem Schwanz und Kopf (k = 0, §3).

### 13.1 Weltlinienmaß und Markov-Eigenschaft [S]

- **Gewicht.** Dyson-Entwicklung von e^{βA}: Eine Konfiguration ist eine Besetzungsgeschichte (η\_τ) mit Sprüngen zwischen Nachbarn, periodisch in τ. Ihr Gewicht ist das Lebesgue-Maß der Sprungzeiten, Gewicht 1 je Sprung, ohne Diagonalterm. Der harte Kern steckt in der Definition. Markierte Linien sind durch die Sprünge wohldefiniert, denn jeder Sprung bewegt genau ein Teilchen.
- **Markov-Eigenschaft.** Gegeben die Konfiguration außerhalb eines Raum-Zeit-Gebiets R ist das Innere gleichverteilt (Lebesgue) über die mit den Randdaten verträglichen Geschichten. Randdaten sind die Besetzung auf Boden und Deckel sowie die Sprünge über den räumlichen Rand. Die Normierung Z\_R(∂) ist ein Matrixelement der Kasten-Zeitentwicklung mit eingefügten Randsprüngen; für kleine Kästen ist es exakt berechenbar.
- **Lücke.** Ein Linienstück fehlt zwischen dem Schwanz (Linie endet bei (y, 0)) und dem Kopf (Linie beginnt bei (z, T)). μ ist das Maß dieser Konfigurationen, normiert wie das geschlossene Maß P, mit Kopf und Schwanz gleichverteilt (Hilfspunkte wie im Preprint).

### 13.2 Skalen

| Größe           | Wahl            | Rolle                                                              |
|-----------------|-----------------|--------------------------------------------------------------------|
| r               | ρ^{−1/2}        | mittlerer Teilchenabstand                                          |
| Zeitscheibe δ   | κ r²            | in δ wandert eine Linie ~ √κ r, also etwa einen Abstand             |
| Zelle           | s = λ r, Seite  | enthält m ≈ λ² Teilchen                                             |
| Route           | Pfad in ℤ² × ℤ  | eine Zeitscheibe je Schritt; je Scheibe ein Sternpfad aus höchstens 5 Zellen (BPP-Skelett, §11) |
| Länge           | w ~ L/s Scheiben | der Kopf muss eine gleichverteilte Zelle erreichen (§10)          |

### 13.3 Ein Schritt in Scheibe k

Gegeben sind der Sternpfad c₀ = B\_k, c₁, …, c\_m = B\_{k+1} der Route in Scheibe k (m = 0, …, 4) und je Zelle ein **wählbares** Teilchen j\_l in c\_l. Wählbar heißt: Anfang S\_j und Ende Y\_j seines Stücks liegen in c\_l, das Stück verlässt eine Umgebung der Zelle nicht, und die Endpunkte sind von anderen Teilchen getrennt. Dann:

- **Löschen.** Das Stück von j₀ wird gelöscht. Das Loch steht am Boden bei S\_{j₀} und ist identisch mit dem Loch, das die vorige Scheibe am Deckel hinterlässt. Deshalb ist j₀ das letzte Label der vorigen Scheibe.
- **Zyklisch verschieben.** Für l = 1, …, m wird das Stück von j\_l neu gezogen, als Brücke von S\_{j\_l} nach Y\_{j\_{l−1}}, aus dem *exakt normierten bedingten Gesetz* bei festgehaltenem Rest (13.1).
- **Ergebnis.** Am Boden fehlt S\_{j₀}, am Deckel fehlt Y\_{j\_m} ∈ B\_{k+1}. Das Loch ist eine Zelle weitergewandert.
- **Ohne Querschritt** (m = 0) wird nur j₀ gelöscht: Das Loch fährt auf der Linie mit.

Der Schwanz ist S\_{j₀} in Scheibe 0, der Kopf Y\_{j\_m} in der letzten Scheibe. Das definiert ν. Die Dichte f = dν/dμ und ihr zweites Moment werden mit dem Gegen-Lücken-Bezug aus §10 gerechnet. Fern von Begegnungen kürzen sich die bedingten Normierer exakt.

### 13.4 Kosten je Begegnung, und wo 2D anders ist als 3D

Begegnen sich zwei unabhängige Routen in einer Zelle, entstehen zwei Kosten:

1. **Geteiltes Label.** Beide wählen dasselbe Teilchen, mit Wahrscheinlichkeit ~ 1/m ≈ λ^{−2}. Das ist der echt lokale 1/m-Term aus §12.
2. **Stoß verschiedener Brücken.** Zwei neu gezogene Brücken der Dauer δ, deren Enden etwa einen Teilchenabstand auseinander liegen, treffen sich. In 3D ist das eine Wahrscheinlichkeit ~ (Reichweite/Abstand), klein durch Verdünnung. **In 2D sind zwei Irrfahrten marginal rekurrent:** Die Trefferwahrscheinlichkeit innerhalb der Zeit δ bei Startabstand d ist ≈ log(√δ/d)/log(√δ/a). Mit √δ ~ λ r und d ~ r ergibt das ≈ log λ / log(1/√ρ).

```text
Kosten je Begegnung  ≈  C₁ / λ²  +  C₂ · log λ / log(1/ρ)       (2D)
Budget:  log(1 + Kosten) < α_max                                  (§11: α_max ≈ 0,012 bei Skala 1)
⇒  λ groß fest wählen, dann ρ < exp(−C₂ log λ / α_max) klein genug
```

**Deutung [H].** Der kleine Parameter in 2D ist g\_eff = 1/log(1/ρ), genau die effektive Kopplung des verdünnten 2D-Bose-Gases (Schick; Lieb–Yngvason: E/N ≈ 4πρ/|ln ρa²|). Ein Beweis auf diesem Weg ergäbe ODLRO für ρ < ρ\* mit sehr kleinem, aber positivem ρ\*, über Teilchen ↔ Loch auch für 1 − ρ < ρ\*. Das ist die übliche Form solcher Sätze; auch die Preprints haben winzige Schwellen.

**Größenordnung [Lit + B].** Nach Dvoretzky–Erdős besucht eine 2D-Irrfahrt in der Zeit t etwa πt/log t verschiedene Plätze. Eine Brücke der Dauer δ = κ/ρ trifft deshalb im Mittel etwa

```text
ρ · π(2δ) / log(2δ)  =  2πκ / log(2κ/ρ)
```

andere Linien (Relativbewegung, doppelte Rate). Die Zahl ist nicht potenzartig, sondern nur logarithmisch klein. Beispiele mit κ = 1: ρ = 10⁻³ gibt ≈ 0,83, ρ = 10⁻¹⁰ gibt ≈ 0,27.

- **Kleineres κ hilft nicht:** Die Zellen müssen Teilchen enthalten, also s ≳ r, und eine Brücke muss etwa s weit kommen, also κ ≳ 1.
- **Was in die Kreuzterme eingeht**, ist nur die Wechselwirkung zweier Brücken *verschiedener* Routen in derselben Zelle. Stöße mit der übrigen Umgebung stecken in den exakt normierten Normierern und kürzen sich. Auch dieser Term ist ~ 1/log(1/ρ).
- **Budget:** Mit dem Budget α\_max ≈ 0,012 der Preprint-Skelette wäre die Schwelle astronomisch klein (log(1/ρ\*) von der Ordnung einige Hundert). Für einen Existenzsatz genügt das. Für eine physikalisch sinnvolle Schwelle müsste das Budget durch bessere Skelette oder bessere Zählung der Begegnungen deutlich größer werden.
- **1D zum Vergleich:** Zwei Irrfahrten treffen sich mit Wahrscheinlichkeit O(1), es gibt keinen kleinen Parameter, und dazu divergiert die Begegnungszahl (§11). Zweifaches Scheitern, wie es sein muss.

### 13.5 Offene Lemmata

- **[L1] Wählbarkeit.** Eine Zelle hat mit hoher Wahrscheinlichkeit ≳ λ²/2 wählbare Teilchen. Die Peierls-Schranke P(alle Zellen von A schlecht) ≤ p^{|A|} in Raum-Zeit braucht Schranken für lokale Dichteschwankungen im Grundzustand, entsprechend Abschnitt 4 des Preprints.
- **[L2] Stoßkosten.** Bedingte Normierer Z\_I sind beschränkt, und die Kreuzterme naher Brücken kosten ≤ C log λ/log(1/ρ). Das ist das 2D-Gegenstück zu Satz 5.3 und der Kern des verdünnten Teils.
- **[L3] Buchführung** der Gegen-Lücke mit Sternpfaden und Umwegen um schlechte Zellen, wie in §10 der dichte-uniformen Arbeit.
- **[L4] Umwege** um schlechte Komponenten in Raum-Zeit. Das ist Geometrie, Übertragung von §8.2 dort.

### 13.6 Was sich jetzt messen lässt (Regel 7)

- Die Trefferwahrscheinlichkeit einer neu gezogenen Brücke mit den übrigen Linien als Funktion von ρ bei festem κ und λ. Erwartet wird ein Abfall wie 1/log(1/ρ), nicht wie eine Potenz. Das geht zuerst mit unabhängigen Irrfahrten (freies Gas), dann mit Wurm-Konfigurationen.
- Die Verteilung der Zahl wählbarer Teilchen je Zelle aus Wurm-Konfigurationen (L1).
- Randquotienten Z\_I(∂) mit der Transfermatrix auf kleinen Kästen (L2).

## 14. Budget je Zellpaar und die Wahl der Route (2026-11-10) [N]

Der Zähler aus §11 zählt nur nahe Basispunkte. Die Kosten fallen aber je nahem **Zellpaar** der beiden Sternpfade an. [skelett\_budget.py](skelett_budget.py) zählt J\_A = Σ\_t #{(c, c′) ∈ Seg₁(t) × Seg₂(t) : |c − c′|\_∞ ≤ 1}. Variiert werden der dyadische Exponent β (Gewichte 2^{−ℓβ}, Querschwankung ~ t^{1−β}, Preprint β = ¼), die Skala A (Querzellen je Zeitscheibe) und eine gemeinsame Drift D (Querzellen je Schritt, mal A). Es sind 20 000 Paare je Punkt, w = 2048 (w-unabhängig, §11).

| D         | β = ⅛: A = 1 / 4 / 8 / 16       | β = ¼: A = 1 / 4 / 8 / 16       | β = ½: A = 1 / 8 / 32    |
|-----------|---------------------------------|---------------------------------|--------------------------|
| 0         | 0,009 / 0,029 / 0,043 / 0,046   | 0,011 / 0,033 / 0,044 / 0,046   | 0,008 / 0,034 / 0,038    |
| 0,02      | – / 0,026 / 0,040 / 0,040       | – / 0,030 / 0,043 / 0,046       | –                        |
| 0,05      | – / 0,025 / 0,026 / 0,028       | – / 0,029 / 0,034 / 0,036       | –                        |
| 0,1       | – / 0,016 / 0,015 / 0,015       | – / 0,022 / 0,023 / 0,022       | –                        |
| 0,2       | – / 0,008 / 0,009 / 0,007       | – / 0,012 / 0,011 / 0,011       | –                        |
| 0,5       | 0,003 / 0,003 / 0,003 / 0,003   | 0,004 / 0,004 / 0,004 / 0,004   | 0,003 / 0,004 / 0,004    |

**Lesart.**

- **Drift kostet.** Laufen zwei nahe Routen in dieselbe Richtung, überdecken sich ihre Sternpfade der Länge nach, und die Zahl naher Zellpaare je Schritt wächst mit A·D.
- **Zeitartige Routen dürfen steil sein.** Die Lücke darf beliebig lang sein: G⁻ ist monoton, und der Restfaktor in §10 ist günstig. Man wählt also w ≫ (Versatz)/A, also D ≲ 0,02. Das ist ein echter Vorteil gegenüber räumlichen Routen, deren Länge der Abstand der Endpunkte festlegt.
- **Bestes Budget:** α\_max ≈ 0,046 bei β = ¼, A ≈ 16, D ≈ 0, also etwa das Vierfache des Preprint-Skeletts (A = 1: 0,011) und das Zehnfache bei Drift 0,5. Größeres A bringt ab etwa 16 nichts mehr, β um ¼ ist gut.
- **Schwelle.** Mit Kosten je Paar ≈ C₁/λ² + C₂ log λ / log(1/ρ) (§13.4) und Budget 0,046 braucht man log(1/ρ\*) ≳ 20 · C₂ log λ, also eine Größenordnung von einigen Zehn bis Hundert. Das bleibt astronomisch klein. Es ist ein Existenzsatz, weit weg von den numerisch sicheren Dichten (ρ = 1/16 hat n₀ ≈ 0,75). Der logarithmisch kleine Parameter der 2D-Physik lässt kaum mehr zu.

## 15. Skizze zu L2: Stoßkosten in 2D [B]

**Bedingtes Gesetz einer neu gezogenen Brücke.** Halten wir alle anderen Linien fest, so ist das Stück von j eine freie Brücke von S nach E der Dauer δ, bedingt auf das Vermeiden der besetzten Raum-Zeit-Punkte Occ der anderen. Die freie Brücke ist eine Irrfahrt in stetiger Zeit, Rate 1 je Nachbar, wegen Gewicht 1 je Sprung. Im harten Kern auf dem Gitter heißt „Stoß“: zur selben Zeit am selben Platz. Es geht also um Treffen in Raum-Zeit, nicht um Schnitte der Bahnen als Mengen; letztere wären in 2D fast sicher, Schnittexponent 5/4.

Zu zeigen sind drei Dinge:

1. **Normierer [B].** P\_Brücke(Occ vermeiden) ≥ 1 − ε(ρ) für wählbare Endpunkte (Abstand ≥ ζ r zu den anderen) und für Umgebungen mit beschränktem „Score“, entsprechend dem Score im Preprint. Grundlage ist die 2D-Treffwahrscheinlichkeit: Die Relativbewegung zweier Teilchen ist eine 2D-Irrfahrt, und bei Startabstand d trifft sie 0 innerhalb der Zeit δ mit Wahrscheinlichkeit ≈ log(√δ/d)/log(√δ). Mit d ≥ ζ r und √δ = √κ r gibt das ≈ 2 log(√κ/ζ)/log(1/ρ) je Nachbar. Etwa κ Nachbarn sind in Reichweite, also ε(ρ) ≈ C κ log(√κ/ζ)/log(1/ρ). Für eine *feste*, nicht zufällige Nachbarbahn γ geht das über Aufenthaltszeiten: P(Treffen) ≤ E[L]/E[L | Treffen] mit L = ∫ 1{X\\_t = γ(t)} dt. Der Zähler ist ~ log(δ/d²), der Nenner ~ log δ, solange γ beschränkt viele Sprünge je Zeiteinheit hat (Score).
2. **Einpfad-Randdichte.** Die bedingte Dichte relativ zur freien Brücke ist ≤ 1/(1 − ε). Das ersetzt den Jensen-Schritt des Preprints, der bei hartem Kern versagt, weil log 0 auftritt.
3. **Kreuzterm naher Brücken verschiedener Routen.** Zwei Brücken in derselben oder einer benachbarten Zelle, beide aus exakt normierten Gesetzen, treffen sich mit Wahrscheinlichkeit ≲ C log(λ√κ/ζ)/log(1/ρ). Das sind die Kosten je Zellpaar in §13.4 und §14.

**Was fehlt [L].**

- **Score-Schranke** (exponentielle Momente für „zu viele Nachbarn“ und „zu sprunghafte Nachbarbahnen“) unter dem Grundzustandsmaß. Auf dem Gitter ist n\_S ≤ |S| trivial, nötig ist aber E e^{n\_S} ≤ e^{Cρ|S|}, also eine Großabweichungsschranke der lokalen Dichte im Grundzustand. Das ist L1 und das eigentlich analytische Stück, entsprechend den Energie- und Entropieabschätzungen in §3–4 des Preprints.
- **Die 2D-Treff-Asymptotik** mit expliziten Konstanten für Brücken (statt freier Irrfahrten) und für bewegte Ziele [Lit: Lawler, Green-Funktion in 2D]. Das ist Standard, aber Arbeit.

**Einordnung.** L2 ist auf dem Gitter in 2D eher *leichter* als im 3D-Kontinuum: keine Streulänge, kein Sobolev-Apparat, der harte Kern ist ein Platz. Der Preis ist der nur logarithmisch kleine Parameter. Das eigentlich schwere Stück ist L1, die lokalen Dichteschranken im Grundzustand.

## 16. L1: Dichteschranken im Grundzustand, Gitterfassung (2026-11-10)

**Ziel (scharf).** Für Vereinigungen U von Zellen der Seite s mit s² ≥ K ln(1/ρ)/ρ und φ\_U(x) = e^{−d(x,U)/s}:

```text
log E_{ψ²} e^{λ n_{φU}}  ≤  C λ ρ |U|        (0 ≤ λ ≤ 1)
```

Das ist das Gegenstück zu (11) der dichte-uniformen Arbeit, dort bei T ≤ ρ² gezeigt und auf T = 0 übertragen. Bei uns geht es direkt bei T = 0, ohne Entropieterme.

**Grundidentität [S].** Auf dem Gitter gilt H + 4N = Σ\_i L\_i. Dabei ist L\_i der freie Graph-Laplace-Operator des Teilchens i, und die Wellenfunktion verschwindet auf der Stoßmenge (Doppelbesetzung). Der harte Kern ist also eine Dirichlet-Bedingung im Konfigurationsraum. Der Term 2N\_nn in H = L\_Token − 4N + 2N\_nn ist genau der Beitrag der Kanten in die Stoßmenge. Das ist die Gitterfassung von „−Δ mit harten Kugeln“.

**Vier Bausteine.**

| Teil | Inhalt | Stand |
|------|--------|-------|
| L1a | Kippidentität: für diagonales g > 0 gilt ⟨gψ, Hgψ⟩ − E₀⟨ψ, g²ψ⟩ = Σ\_Kanten ψψ′(g − g′)²; mit G = λ n\_φ höchstens C λ² s^{−2} E\_g n\_φ | [S] Identität, [B] Schranke |
| L1b | IMS mit zwei Farben auf dem Gitter: p = cos θ, q = sin θ, 1 − p\_x p\_y − q\_x q\_y ≤ (θ\_x − θ\_y)²/2 ≤ C/s². Die zweifarbige Einbettung ist eine Isometrie; das Bild verletzt den harten Kern nicht, also gilt die Energie ≥ E^{in}\_j + E^{out}\_{N−j} mit Fehler C s^{−2} E n\_Übergang | [B] |
| L1c | Zellenschranke: Kasten der Seite b, ein Dirichlet-Punkt (der Partner): λ\_min ≥ c/(b² ln b). Durch Paaren ⌊j/2⌋ ≥ j/3 gilt im Kasten E ≥ −4j + (c/3)/(b² ln b) · n\_Q 1{n\_Q ≥ 2} | [N] c ≈ 1,66 (Ecke, b ≤ 128, vermutlich → π/2); [B] über die 2D-Punktkapazität |
| L1d | **Scharfe Einfügeschranke:** E\_k − E\_{k−1} ≤ −4 + C\* ρ/ln(1/ρ), über einen korrelierten Versuchszustand (Jastrow mit der 2D-Nullenergie-Streulösung bis R ~ ρ^{−1/2}, Dyson bzw. Lieb–Yngvason) | [B], Arbeit |

Numerik zu L1c: [zellschranke\_punkt.py](zellschranke_punkt.py); min\_y λ · b² ln b = 1,76 / 1,74 / 1,71 / 1,69 / 1,67 / 1,66 für b = 4 … 128. In der Mitte geht der Wert gegen 2π.

**Zusammensetzen (wie Lemma 4.2 dort).** Kästen der Seite b = D₀^{−1/2} in U, D₀ = Hρ. Bewegt man j Teilchen nach U, so kostet das mindestens

```text
[ c H ρ / ln(1/(Hρ))  −  C* ρ / ln(1/ρ)  −  C/s² ] · j   −   c H² ρ² |U| / ln(1/(Hρ))
```

Bei großem H ist die Klammer ≥ (cH/4) ρ/ln(1/ρ), sofern s² ≳ ln(1/ρ)/ρ. Mit L1a folgt E\_g n\_φU ≤ C H ρ|U| gleichmäßig in λ ∈ [0, 1], und durch Integration in λ die Zielschranke.

**Die 2D-Falle [B].** Mit der groben Born-Schranke E\_k − E\_{k−1} ≤ −4 + Cρ (unkorreliert einfügen) statt L1d müsste D₀ ≈ ρ ln(1/ρ) sein. Daraus würde nur E n\_U ≤ C ρ ln(1/ρ) |U| folgen, und dieser Faktor ln(1/ρ) fräße in L2 genau den kleinen Parameter 1/ln(1/ρ): Die Nachbarzahl wäre nur bis ~ κ ln(1/ρ) kontrolliert. In 3D tritt das nicht auf, weil dort Born und der wahre Wert dieselbe Ordnung ρ haben. Die korrelierte Einfügeschranke L1d ist also in 2D **unverzichtbar**. Sie entspricht physikalisch der 2D-Kopplung g\_eff = 1/ln(1/ρ).

**Nächste Schritte.**

1. L1d ausarbeiten: Versuchszustand ψ\_k ∝ F · b₀⁺ψ\_{k−1} mit Jastrow-Faktor F = Π\_j f(x\_new − x\_j), f die Gitter-Streulösung, f(0) = 0, f = 1 ab R. Abzuschätzen sind die kinetischen Kreuzterme mit den alten Teilchen und Dreierüberlappungen. Das ist der Upper-bound-Teil von Lieb–Yngvason, auf das Gitter übertragen; die Gitter-Streulänge lässt sich numerisch bestimmen.
2. L1b sauber aufschreiben (Fock-Raum-Lokalisierung nach Dereziński–Gérard bzw. Lewin, Gitterfassung).
3. Numerik: die Gitter-Streulänge a\_Gitter und den Vergleich von μ + 4 aus den Wurm-Läufen mit 4π ρ/ln(1/(ρ a²)) bzw. mit dem Born-Wert.

### 16.1 Gitter-Streulänge und chemisches Potential [S + N]

Die Nullenergie-Streulösung auf ℤ² mit f(0) = 0 ist der Potentialkern der einfachen Irrfahrt: a(x) = (2/π)(ln|x| + γ + (3/2) ln 2) + O(|x|^{−2}). Daraus folgt die **Gitter-Streulänge a = e^{−γ} 2^{−3/2} ≈ 0,1985** (Gitterabstand 1, kinetischer Operator L = −Δ\_Gitter, also ħ²/2m = 1). Vergleich mit den μ-Werten aus Runde 1:

| ρ      | μ + 4 gemessen | 8πρ / ln(1/(ρa²)) (Lieb–Yngvason, führend) | Born 8ρ | gemessen / LY |
|--------|----------------|--------------------------------------------|---------|---------------|
| 0,0645 | 0,329          | 0,271                                      | 0,516   | 1,21          |
| 0,1298 | 0,770          | 0,618                                      | 1,038   | 1,25          |
| 0,2559 | 1,769          | 1,403                                      | 2,047   | 1,26          |

- Der Überschuss von etwa 20 % gegenüber der führenden Ordnung passt zur bekannten nächsten Ordnung (Fournais et al. 2024: Faktor 1 + Y ln Y + 2,8 Y mit Y = 1/ln(1/ρa²), also ≈ 1,17 bei ρ = 0,0645).
- Born liegt um den Faktor ≈ ln(1/(ρa²))/π darüber. Dieser Faktor wächst logarithmisch und ist die Falle aus §16.

### 16.2 L1d über eine exakte Identität und einen Bootstrap [B]

**Identität [S].** Die alten Teilchen sind im Grundzustand ψ\_{k−1}, das neue ist gleichverteilt: Ψ₀ = ψ\_{k−1} ⊗ 1. Das ist ein positiver Eigenvektor des Operators, in dem neu–alt-Stöße erlaubt sind. Mit dem Jastrow-Faktor F = Π\_j f(x\_neu − x\_j), 0 ≤ f ≤ 1, f(0) = 0, verschwindet FΨ₀ auf neu–alt-Stößen. Die Kippidentität (L1a) ist exakt:

```text
E_k − E_{k−1} + 4  ≤  Σ_{Kanten} Ψ₀Ψ₀′ (F − F′)² / ⟨Ψ₀, F² Ψ₀⟩
```

Verteilte Teilchen genügen als Versuchszustand. Der Grundzustand mit hartem Kern und markierten Teilchen ist positiv und eindeutig, also symmetrisch.

**Abschätzung.** f\_R(x) = min(1, a(x)/a(R)) mit R = ε ρ^{−1/2}.

- *Sprünge alter Teilchen* ändern nur einen Faktor. Mit ψψ′ ≤ (ψ² + ψ′²)/2 ergibt das (k−1)/M · D(f\_R). Dabei ist D(f\_R) = Σ\_Kanten (Δf\_R)² = 4/a(R) ≈ 2π/ln(R/a), die Dirichlet-Energie bzw. Kapazität (Green-Identität mit L a = 4δ₀, wie im Kontinuum ∫|∇ ln(r/a)|²/ln²(R/a) = 2π/ln(R/a)).
- *Sprünge des neuen Teilchens* ändern alle Faktoren. Es gilt |ΔF| ≤ Σ\_j |Δf\_j|; der Mehrfachterm braucht die Paardichte der alten Teilchen im Radius R.
- *Normierung* ⟨F²⟩ ≥ 1 − (Dichte · Fläche, in der f < 1 ist).

Ergebnis: μ + 4 ≲ 2ρ D(f\_R)(1 + Überlapp) ≈ 4πρ/ln(R/a) = 8πρ/ln(R²/a²). Mit R² ~ 1/ρ ist das der Lieb–Yngvason-Wert 8πρ/ln(1/(ρa²)) bis auf O(1) im Logarithmus, sofern die Paardichte im Radius R durch C(ρ R²)² beschränkt ist.

**Zirkel und Bootstrap (überholt durch §16.4: Mit dem Nächster-Nachbar-Jastrow nach Dyson entfällt der Mehrfachterm, und es braucht keine Dichte-Information).**

- *Zirkel:* L1d braucht Paardichten des wahren Grundzustands, also L1.
- *Schritt 1:* Mit Born gilt E\_k − E\_{k−1} ≤ −4 + 8ρ(1 + o(1)). Daraus folgt L1 mit Verlust: log E e^{λ n\_U} ≤ C λ ρ ln(1/ρ) |U|. Insbesondere sind Paardichten auf Skala R durch C (ρ ln(1/ρ) R²)² beschränkt.
- *Schritt 2:* Mit R = ρ^{−1/2}/ln(1/ρ) sind die Überlappterme klein, während ln(R/a) = ½ ln(1/(ρa²)) − ln ln(1/ρ) ≈ ½ ln(1/ρ) bleibt. Damit gilt L1d scharf bis auf einen Faktor (1 + O(ln ln/ln)).
- *Schritt 3:* L1 scharf.

Offen [L]: die Gitterfassung der Fock-Raum-Lokalisierung (L1b) und das saubere Ausrechnen der Überlappterme. Beides sind Standardtechniken, aber Arbeit.

### 16.3 L1d numerisch: Die korrelierte Einfügung ist fast scharf [N]

[l1d\_einfuegen.py](l1d_einfuegen.py) wertet die exakte Schranke aus §16.2 mit dem exakten ψ\_{k−1} aus und vergleicht mit dem wahren μ = E\_k − E\_{k−1}. Der Potentialkern ist numerisch berechnet; a(2,0) = 1,4535 = 4 − 8/π ist der bekannte exakte Wert.

| Gitter | k | ρ     | μ + 4 wahr | Born           | f\_R, R = 3      | bestes Paarprofil |
|--------|---|-------|------------|----------------|------------------|-------------------|
| 6×6    | 2 | 0,056 | 0,1595     | 0,2286 (+43 %) | 0,1657 (+3,9 %)  | 0,1595 (exakt)    |
| 6×6    | 3 | 0,083 | 0,3332     | 0,4627 (+39 %) | 0,3453 (+3,6 %)  | 0,3333 (+0,03 %)  |
| 6×6    | 4 | 0,111 | 0,5193     | 0,7017 (+35 %) | 0,5370 (+3,4 %)  | 0,5198 (+0,1 %)   |
| 8×8    | 2 | 0,031 | 0,0798     | 0,1270 (+59 %) | 0,0823 (+3,1 %)  | 0,0798 (exakt)    |
| 8×8    | 3 | 0,047 | 0,1660     | 0,2560 (+54 %) | 0,1705 (+2,7 %)  | 0,1661 (+0,06 %)  |
| 8×8    | 4 | 0,062 | 0,2578     | 0,3868 (+50 %) | 0,2643 (+2,5 %)  | 0,2581 (+0,1 %)   |

- **Born** liegt zu hoch, und zwar umso mehr, je kleiner ρ ist (35 % → 59 %). Das ist der logarithmische Faktor der 2D-Falle aus §16.
- **Die Streulösung f\_R** (Potentialkern, abgeschnitten bei R = 3, ohne jede Anpassung) liegt nur 2,5–4 % über dem wahren Wert.
- **Das beste Paarprofil** ist auf 0,1 % scharf. Bei k = 2 ist es exakt, da der Zweiteilchen-Grundzustand eine reine Paarfunktion ist.

Für den Beweis heißt das: L1d ist nicht nur richtig, sondern mit dem einfachsten Profil nahezu optimal. Die Überlappterme, die der Bootstrap kontrollieren muss, sind numerisch klein (wenige Prozent). Es bleibt, sie streng abzuschätzen.

### 16.4 L1d streng: Einfügeschranke mit Dysons Nächster-Nachbar-Jastrow [S]

**Lemma (L1d).** Sei f: Torus → [0, 1] mit f(0) = 0 und gleichen Kantensummen in x- und y-Richtung (z. B. gitter-symmetrisch), ρ′ = (k−1)/M, D(f) = Σ\_Kanten (f(z) − f(z′))², S(f) = Σ\_z (1 − f(z)²), und ρ′S(f) < 1. Dann gilt für die Grundzustandsenergien der harten Bosonen, auch mit beliebigem anziehendem Außenpotential −W ≤ 0:

```text
E_k − E_{k−1} + 4  ≤  2ρ′ D(f) / (1 − ρ′ S(f))
```

**Beweis.**

1. *Markierte Fassung.* K\_k = Σ\_i L\_i auf markierten Konfigurationen ohne Doppelbesetzung (Dirichlet auf der Stoßmenge), also K\_k = 4k − A. Der Grundzustand ist positiv und eindeutig, also symmetrisch, also bosonisch: ε\_k := E\_k + 4k.
2. *Gelockerter Operator.* K\_rel = K\_{k−1} ⊗ 1 + 1 ⊗ L\_neu auf Paaren (η, x), wobei nur die alten Teilchen einander ausschließen. Ψ₀ = ψ\_{k−1} ⊗ 1 erfüllt K\_rel Ψ₀ = ε\_{k−1} Ψ₀, ψ\_{k−1} > 0.
3. *Grundzustandssubstitution.* Für reelles G gilt ⟨GΨ₀, K\_rel GΨ₀⟩ = ε\_{k−1} ‖GΨ₀‖² + Σ\_{Kanten von K\_rel} Ψ₀Ψ₀′ (G − G′)².
4. *Versuchsfaktor.* F(η, x) = min\_j f(x − x\_j) verschwindet bei neu–alt-Stößen. Deshalb gilt ⟨FΨ₀, K\_k FΨ₀⟩ = ⟨FΨ₀, K\_rel FΨ₀⟩. Ein Außenpotential −W wirkt auf das neue Teilchen mit ⟨FΨ₀, −W FΨ₀⟩ ≤ 0 und darf weggelassen werden. Es folgt ε\_k ≤ ε\_{k−1} + N/Z.
5. *Nenner.* Aus 1 − min\_j f\_j² ≤ Σ\_j (1 − f\_j²) folgt Z = Σ\_{η,x} ψ² F² ≥ M − (k−1) S(f) (bei ‖ψ‖ = 1).
6. *Sprünge des neuen Teilchens.* |min\_j a\_j − min\_j b\_j| ≤ max\_j |a\_j − b\_j|, also (ΔF)² ≤ Σ\_j (Δf\_j)². Summiert über x ~ x′ ergibt das ≤ Σ\_η ψ² (k−1) D(f) = (k−1) D(f).
7. *Sprünge eines alten Teilchens j.* Nur der j-te Term im Minimum ändert sich, also (ΔF)² ≤ (f(x − x\_j) − f(x − x\_j′))². Die Summe über x ist die Kantensumme D\_e der Sprungrichtung e. Mit ψψ′ ≥ 0 und Σ\_{Kanten in Richtung e} ψψ′ = ¼⟨ψ, A\_{k−1}ψ⟩ ≤ k − 1 je Richtung (Gittersymmetrie von ψ) ist der Beitrag ≤ (k−1)(D\_x + D\_y) = (k−1) D(f).
8. Insgesamt N ≤ 2(k−1) D(f) und Z ≥ M(1 − ρ′S). ∎

Das Lemma braucht **keine** Dichte-Information über ψ\_{k−1}, nur dessen Positivität. Der Zirkel aus §16.2 kam allein vom Produkt-Jastrow, bei dem ein Sprung des neuen Teilchens alle Faktoren ändert.

**Auswertung mit f\_R = min(1, a(z)/a\_R)**, Potentialkern a, a\_R = (2/π)(ln R + γ + 1,5 ln 2):

- Asymptotisch D(f\_R) ≈ 4/a\_R ≈ 2π/ln(R/a) (Green-Identität mit L a = 4δ₀) und S(f\_R) ≈ 2R²/a\_R ≈ πR²/ln(R/a).
- Mit R = 1/(t√ρ) und t ~ √ln optimiert:

```text
E_k − E_{k−1} + 4  ≤  8πρ / ln(1/(ρa²)) · (1 + O(ln ln(1/ρ) / ln(1/ρ)))      (a = 0,1985)
```

Das ist die Lieb–Yngvason-Ordnung, also scharf in führender Ordnung. Die Asymptotik des Potentialkerns mit Fehlerschranke ist Standard [Lit: Fukai–Uchiyama, Kozma–Schreiber; Lawler–Limic].

Numerisch mit [l1d\_schranke.py](l1d_schranke.py), unendliches Gitter, optimales R:

| ρ     | strenge Schranke | LY 8πρ/ln(1/ρa²) | streng/LY | Born/LY | R\_opt |
|-------|------------------|------------------|-----------|---------|--------|
| 10⁻¹  | 0,812            | 0,454            | 1,79      | 1,76    | 1,5    |
| 10⁻²  | 0,0481           | 0,0321           | 1,50      | 2,50    | 3,9    |
| 10⁻³  | 3,37·10⁻³        | 2,48·10⁻³        | 1,36      | 3,23    | 13     |
| 10⁻⁴  | 2,59·10⁻⁴        | 2,02·10⁻⁴        | 1,28      | 3,96    | 42     |
| 10⁻⁶  | 1,76·10⁻⁶        | 1,47·10⁻⁶        | 1,19      | 5,43    | 414    |
| 10⁻⁸  | 1,34·10⁻⁸        | 1,16·10⁻⁸        | 1,16      | 6,89    | ≥ 3000 |

Auf den kleinen Tori (R < L/2) liegt die strenge Schranke 2–22 % über dem wahren μ + 4 (6×6 und 8×8, k = 2 … 4), stets darüber und stets unter Born.

**Folge für L1.** Die Klammer in §16 wird [c H ρ/ln(1/(Hρ)) − 8πρ(1 + o(1))/ln(1/(ρa²)) − C/s²]. Mit H > 8π/c (c aus L1c, numerisch ≈ π/2, also H ≳ 16) ist sie positiv. Damit fehlen für L1 noch:

- **L1b**, die zweifarbige Lokalisierung auf dem Gitter,
- **L1c streng** (Punktkapazität im Kasten),
- **das Zusammensetzen** wie in Lemma 4.2 des Preprints.

### 16.5 L1c und L1b streng, Zusammensetzen [S bzw. B]

**L1c (Zellenschranke) [S].** Q sei ein b×b-Kasten mit Neumann-Graph-Laplace L\_Q (nur innere Kanten), y ∈ Q, f: Q → ℝ mit f(y) = 0. Dann gilt:

```text
⟨f, L_Q f⟩ ≥ ‖f‖² / (1/λ₂ + b² R_y),     λ₂ = 2 − 2cos(π/b),
R_y = effektiver Widerstand von y zur Gleichverteilung = Σ_{(p,q)≠0} φ_pq(y)² / λ_pq   (Cosinus-Basis)
```

*Beweis.* Mit f̄ als Mittelwert gilt ‖f‖² = ‖f − f̄‖² + b² f̄². Poincaré im Neumann-Kasten gibt ‖f − f̄‖² ≤ ⟨f, L\_Q f⟩/λ₂. Für jeden Einheitsfluss θ von y zur Gleichverteilung ist f̄ = f̄ − f(y) = ⟨θ, ∇f⟩. Cauchy–Schwarz und Thomson (Minimum der Flussenergie = R\_y) geben f̄² ≤ R\_y ⟨f, L\_Q f⟩. ∎

*Zahlen* ([l1c\_widerstand.py](l1c_widerstand.py), exakt über die Eigenbasis):

- Das Maximum über y liegt in der Ecke, mit R\_Ecke = (2/π) ln b − 0,1820 (konvergiert ab b ≈ 32; bei b = 4 −0,168). In der Mitte ist R = (1/(2π)) ln b + 0,0488.
- Da 1/(λ₂b²) ≤ 0,107 < 0,168 gilt, folgt **λ\_min(b, y) ≥ π/(2 b² ln b) für alle y und b ≥ 4**. Gezeigt ist das exakt für b ≤ 512; für alle b fehlt nur die Standard-Asymptotik der Neumann-Green-Funktion mit Restglied.
- Die Schranke liegt 4 % unter dem wahren Eigenwert (c = 1,60 gegen 1,66 bei b = 128).

*Mehrere Teilchen.* Neumann-Zerlegung: Lässt man Kanten zwischen Kästen weg, bleiben nur nichtnegative Kantenterme übrig, die Dirichlet-Terme der Stoßmenge eingeschlossen. Danach paart man die Teilchen eines Kastens (⌊n/2⌋ ≥ n/3) und benutzt für jedes Paar den Laplace-Operator eines Partners bei festgehaltenem anderen; die Wellenfunktion verschwindet am Platz des anderen. Ergebnis:

```text
Σ_i L_i  ≥  (π / (6 b² ln b)) · Σ_Q n_Q 1{n_Q ≥ 2}
```

**L1b (Lokalisierung mit zwei Farben) [S].** Sei p = cos θ, q = sin θ: Λ → [0, 1]. Die Abbildung U „jedes Teilchen bei x wird mit Amplitude p(x) innen, q(x) außen gefärbt“ ist eine Isometrie vom Hartkern-Fock-Raum in Hartkern ⊗ Hartkern. Im Bild sitzen nie zwei Teilchen auf einem Platz, gleich welcher Farbe. Direkt nachgerechnet:

```text
⟨Φ, HΦ⟩ = ⟨UΦ, (H_innen + H_außen) UΦ⟩ − Σ_{η~η′} Φ(η)Φ(η′) (1 − cos(θ_x − θ_y))
```

Dabei ist x → y der Sprung der Kante η ~ η′.

- Der Fehler ist ≤ ½ max(Δθ)² · Σ |ΦΦ′| ≤ 4 max(Δθ)² · E\_Φ[n\_Übergangszone].
- H\_innen + H\_außen erhält die Zahl j der Innen-Teilchen und lässt Stöße zwischen den Farben zu. Diese Lockerung kann die Energie nur senken, also ist ⟨UΦ, …⟩ ≥ Σ\_j w\_j (E^{innen}\_j(Ω) + E\_{N−j}(Λ)).
- w\_j ist die Verteilung der Innen-Zahl; jedes Teilchen wird unabhängig mit Wahrscheinlichkeit p(x)² innen gefärbt.

Bei T = 0 entfallen alle Entropieterme des Preprints. ∎

**Kippschranke (L1a ausgeführt) [S].** Für g = e^{λ n\_φ}, φ = e^{−d(·,U)/s} und 0 ≤ λ ≤ 1:

```text
E(gψ/‖gψ‖) − E_N = Σ_{Kanten} ψψ′(g − g′)² / ⟨g²⟩ ≤ C λ² s^{−2} E_g[n_φ]
```

Das folgt aus |Δφ| ≤ (e^{1/s} − 1) φ und ψψ′g² ≤ ½(ψ²g² + ψ′²g′²) e^{2λ/s}.

**Zusammensetzen (wie Lemma 4.2 dort) [B].** Kästen der Seite b = D₀^{−1/2} in der Vergrößerung Ω\_h von U, gemittelt über h mit Dichte e^{−h}. Innen gilt E^{innen}\_j ≥ −4j + c\_b (j − #Kästen) mit c\_b = (π/3) D₀/ln(1/D₀). Außen gilt nach L1d E\_{N−j} ≥ E\_N + 4j − j μ\* mit μ\* = 8πρ(1 + o(1))/ln(1/(ρa²)). Zusammen mit L1b und der Kippschranke:

```text
(c_b − μ* − C/s²) · E_g n_φU  ≤  c_b · C D₀ |U|
```

Mit D₀ = Hρ, H ≳ 50 (dann c\_b ≥ 2μ\*) und s² ≳ ln(1/ρ)/ρ folgt E\_g n\_φU ≤ C H ρ |U| gleichmäßig in λ, also

```text
log E e^{2λ n_φU} ≤ C λ ρ |U|        (L1, scharf, ohne Logarithmus-Verlust)
```

**Noch offen für den vollständigen verdünnten Teil (Gegenstücke zu Lemma 4.3 und 4.4 des Preprints):**

- **Untere Schwänze.** Zellen mit zu wenigen Teilchen sind selten. Über negative Kippungen und die Gitterfassung von (5): ε\_j/j ist nichtfallend, mit ε\_j = E\_j + 4j [S]. Beweis: Die (j−1)-Randverteilung hat weniger Dirichlet-Bedingungen, also ε\_{j−1} ≤ ((j−1)/j) ε\_j. Dazu kommt ε\_N ≥ c ρ N/ln(1/ρ) aus L1c.
- **Isolation** auf kürzerer Skala: wählbare Endpunkte sind getrennt.

### 16.6 Untere Schwänze und Isolation (Gegenstücke zu Lemma 4.3 und 4.4) [B, Zutaten S]

**Zutaten [S].**

1. *ε\_j/j ist nichtfallend* (ε\_j = E\_j + 4j). Die (j−1)-Randverteilung des j-Grundzustands Φ zerfällt in die bedingten Zustände Φ(·, z), z = Platz des herausgenommenen Teilchens. Jeder davon ist ein zulässiger (j−1)-Hartkernzustand, und seine Kantenterme stimmen mit denen in Φ überein: Ein Sprung auf z ergibt in beiden Fällen den Term Φ², weil Φ dort ohnehin verschwindet. Also ε\_{j−1} ≤ ((j−1)/j) ε\_j. Exakt geprüft auf 6×6: ε\_j/j = 0; 0,080; 0,164; 0,253; 0,346; 0,442.
2. *ε\_N ≥ (π/16) ρN/ln(4/ρ)* für N ≥ 4, sobald Kästen der Seite (4/ρ)^{1/2} in den Torus passen. Das folgt aus L1c, weil Σ n\_Q 1{n\_Q ≥ 2} ≥ N − #Kästen ≥ 3N/4. Die Schranke ist richtig, aber etwa 40-fach zu schwach (grobe Paarung). Für die Ordnung genügt sie.
3. *Folglich ε\_{N+k} − ε\_N ≥ k ε\_N/N ≥ c₁ ρ k/ln(1/ρ)* (Hinzufügen kostet). Zusammen mit L1d gilt ε\_N − ε\_{N−j} ≤ j μ\*, μ\* ≈ 8πρ/ln(1/ρa²) (Herausnehmen bringt höchstens). **Beide sind von der Ordnung ρ/ln(1/ρ).** Mit der Born-Schranke statt L1d wäre der zweite Wert um ln(1/ρ) zu groß, und das Argument bräche.

**Untere Schwänze [B].** Behauptung: Für jede Vereinigung U von u Zellen gilt P(n\_Q < 2b₋ m für alle Q ⊂ U) ≤ C e^{−c m u}.

- *Lokalisieren* mit p = 1 auf den inneren Teilkästen jeder Zelle (wie im Preprint).
- *Im Sektor mit j Innen-Teilchen* fügt man dem Außen-Zustand k = ηρ|U| Teilchen hinzu, im Hartkern-Grundzustand der inneren Teilkästen. Diese sind frei von Außen-Teilchen, weil dort q = 0 ist. Das kostet höchstens k·C/s² + C k²/(|U| ln(1/(ηρ))) (Dirichlet-Kasten plus L1d im Kasten).
- *Mit Zutat 3:*

```text
ε(σ) − ε_N  ≥  c₁ ρ k/ln − μ* E j − C k/s² − C k²/(|U| ln) − C s^{−2} E n_φ
            ≥  c′ ρ²|U| / ln(1/ρ)  −  C (ρ/ln(1/ρ)) E_σ n_φ          (η klein, s² ≥ K ln(1/ρ)/ρ)
```

- *Negative Kippung* G = −λ n\_φ: Die Kippschranke gibt höchstens C λ² s^{−2} E\_g n\_φ ≤ C (ρ/(K ln)) E\_g n\_φ. Also E\_g n\_φ ≥ c″ ρ|U| für alle λ ∈ [0, 1]; **die Logarithmen kürzen sich**.
- Integration gibt E e^{−2 n\_φ} ≤ e^{−2c″ρ|U|}, und Markov mit kleinem b₋ liefert die Behauptung. Bei T = 0 entfällt der Entropieterm des Preprints samt Differentialungleichung.

**Isolation [B].** Ein Teilchen heißt nicht isoliert, wenn ein anderes im Abstand r = ζ ρ^{−1/2} liegt. Wie Lemma 4.4 dort: Q = Σ\_χ (n\_χ − 1)\_+ über feine Kästen der Seite r, mit reservierter Ballungsenergie c\_r E Q. Nach L1c ist c\_r = π/(6 r² ln r) ≈ (π/3) ρ/(ζ² ln(1/ρ)). Kippung λ Q mit λ ≤ λ₀ ~ ζ. Daraus folgt E\_g Q ≤ C ζ² ρ |S|, wieder mit gekürzten Logarithmen, und

```text
P(#nicht isoliert in S ≥ k′) ≤ exp(C λ₀ ζ² ρ|S| − λ₀ k′)
```

**Strukturbefund.** In der gesamten Familie L1 (obere und untere Schwänze, Isolation) ist jede Energieskala von der Ordnung ρ/ln(1/ρ), und in allen Verhältnissen kürzt sich der Logarithmus. Der kleine Parameter 1/ln(1/ρ) überlebt nur in L2 (Stoßkosten) und bestimmt dort die Schwelle ρ\*. Möglich ist das nur dank der scharfen Einfügeschranke L1d.

**Stand des verdünnten Teils.**

| Lemma | Inhalt                                    | Stand                         |
|-------|-------------------------------------------|-------------------------------|
| L1    | obere Schwänze                            | [S]-Zutaten, Zusammensetzen [B] |
| L1    | untere Schwänze, Isolation                | [S]-Zutaten, Zusammensetzen [B] |
| L2    | Stoßkosten ≲ C log λ/ln(1/ρ)              | [B] (§15)                     |
| L3    | Buchführung der Gegen-Lücke mit Sternpfaden | [B] (§10, §13)              |
| L4    | Umwege um schlechte Komponenten           | offen, Geometrie              |

## 17. L4: Umwege um schlechte Zellen in Raum-Zeit (2026-11-10)

**Geometrie [Lit/S].** Wie §8.2 der dichte-uniformen Arbeit, jetzt im Zellgitter ℤ² × ℤ (Raum × Zeitscheiben) = ℤ³:

- Komponenten schlechter Zellen werden „gefüllt“ (endliche Löcher hinzugenommen).
- Der Außenrand einer zusammenhängenden Menge ist über Diagonalnachbarn zusammenhängend (Timár, in jeder Dimension).
- Jede getroffene Komponente T wird genau einmal auf ihrem Außenrand umgangen, mit ≤ 6|T| Umwegzellen, danach chronologische Schleifentilgung.
- Löscht man nicht getroffene Komponenten, ändert sich nichts. Komponenten der Größe ≥ n/4 führen zur Verwerfung; das ist selten nach Peierls.

Das überträgt sich wörtlich.

**Neue Schwierigkeit: Peierls in Raum-Zeit.** Der Preprint braucht P(alle Zellen von A schlecht) ≤ q^{|A|} nur innerhalb *einer* kurzen Zeitscheibe. Unsere Route läuft durch viele Scheiben. Ereignisse zu verschiedenen Zeiten sind korreliert, und weil Phononen langsam abklingen, gibt es keine gleichmäßige Durchmischung.

**Ausweg [S + B].** Exponentielle Momente zeitabhängiger Funktionale über Feynman–Kac und Operatornormen:

```text
log E_ψ[ exp ∫ W(η_t, t) dt ]  ≤  ∫ [ E₀(H) − E₀(H − W_t) ] dt
```

Begründung [S]: E\_ψ[e^{∫W}] = ⟨ψ, T exp(−∫(H − E₀ − W\_t) dt) ψ⟩, und jeder Faktor hat die Norm e^{−dt(E₀(H − W\_t) − E₀)}.

- Die rechte Seite ist die Energieabsenkung durch ein *anziehendes* Außenpotential auf den betroffenen Zellen. Für sie gilt die Einzeitmaschinerie von L1 mit Außenpotential [B]. L1d gilt gleichmäßig in anziehenden Potentialen (§16.4), und der Preprint führt −W genau deshalb in (6) und (9) mit.
- Ergebnis: E₀(H) − E₀(H − w 1\_U) ≤ C w ρ|U|, sofern w unter der Ballungsskala ~ ρ/ln(1/ρ) bleibt. Mit Scheibendauer δ ~ κ/ρ heißt das λ ≲ κ/ln(1/ρ) im exponentiellen Moment.
- Die Peierls-Schranke q = e^{−c λ m} ist klein, sobald die Zellen m ≳ ln(1/ρ) Teilchen enthalten, was ohnehin gefordert ist (§16).
- Schlechtheit wird über Scheibenmittel oder Scheibenmaxima definiert, sodass ∫W dt die Ereignisse dominiert.

**Numerik [N]** ([skelett\_umwege.py](skelett_umwege.py), A = 16, β = ¼, w = 2048, je 20 000 Paare). Beide Routen sehen dieselben schlechten Zellen (Dichte q) und werden deterministisch auf dieselbe nächste gute Randzelle gelenkt. Das ist eine vereinfachte, scheibenweise Form der Außenrand-Umwege.

| Persistenz τ\_p (Scheiben) | q = 0 | q = 0,03 | q = 0,1 | q = 0,2 | q = 0,3 |
|----------------------------|-------|----------|---------|---------|---------|
| 1 (unabhängig): E J / α\_max | 20,2 / 0,042 | 19,9 / 0,049 | 19,6 / 0,049 | 19,4 / 0,049 | 19,1 / 0,051 |
| 16                         | –     | 19,8 / 0,049 | 19,7 / 0,047 | 19,5 / 0,050 | –       |
| 256                        | –     | 19,8 / 0,046 | 20,1 / 0,046 | 19,5 / 0,048 | –       |

- **Umwege kosten kein Budget**, auch nicht bei 30 % schlechten Zellen und auch nicht bei Schläuchen über 256 Scheiben. Die Routen ziehen superdiffusiv quer und passieren Schläuche schnell. Sind zwei Routen am selben Schlauch, sind sie ohnehin nahe und schon gezählt.
- **Vorbehalt:** Volle 3D-Außenrand-Umwege großer, in der Zeit langgestreckter Komponenten sind damit nicht getestet. Diese sind nach der Raum-Zeit-Peierls-Schranke exponentiell selten in ihrer Größe.

**Stand L4:** Geometrie [Lit/S], Raum-Zeit-Peierls [S]-Identität plus [B], Numerik unbedenklich.

## 18. L2 numerisch: Treffwahrscheinlichkeit in 2D [N + S]

Die Relativbewegung zweier Teilchen ist eine 2D-Irrfahrt mit Rate 2 je Nachbar, mit Kern p\_t(x) = e^{−8t} I\_{x₁}(4t) I\_{x₂}(4t). Mit exponentieller Dauer (Mittel δ) ist die Treffwahrscheinlichkeit exakt g(d)/g(0), mit g = ∫ e^{−t/δ} p\_t dt [S]. Sie wird mit [l2\_treffen.py](l2_treffen.py) über Quadratur berechnet. Gewählt sind d = r = ρ^{−1/2} und δ = κ r²:

| κ   | P bei r = 4 / 16 / 64 / 256       | P·ln(1/ρ) bei r = 256 | Fit P ≈ A/(ln r + B) | Grenzwert 2A |
|-----|-----------------------------------|-----------------------|----------------------|--------------|
| 0,5 | 0,137 / 0,094 / 0,072 / 0,058     | 0,64                  | A = 0,42             | 0,84         |
| 1   | 0,190 / 0,135 / 0,105 / 0,086     | 0,95                  | A = 0,66, B = 2,1    | 1,32         |
| 2   | 0,244 / 0,178 / 0,140 / 0,116     | 1,29                  | –                    | ≈ 1,8        |
| 4   | 0,296 / 0,221 / 0,177 / 0,147     | 1,63                  | A = 1,22, B = 2,8    | 2,44         |

- Die Form C(κ)/ln(1/ρ) aus §15 ist bestätigt, mit C ≈ ln κ + 1,3, wie die Asymptotik ½ ln κ + const im Zähler erwartet.
- **Die Konvergenz ist langsam:** B ≈ 2 im Nenner. Selbst bei r = 256, also ρ = 1,5·10⁻⁵, treffen sich zwei Teilchen in der Zeit δ = r² noch mit Wahrscheinlichkeit ≈ 0,09.
- **Schwelle grob:** Eine Brückenpaarung je Begegnung und Budget α\_max ≈ 0,046 erfordern 0,66/(ln r + 2,1) < 0,046, also ln r > 12, r > 2·10⁵, ρ < 3·10⁻¹¹. Weitere Faktoren (mehrere Brückenpaare je Begegnung, log λ, Teilchenwahl) drücken ρ\* weiter. Das bestätigt die Einschätzung „Existenzsatz mit astronomisch kleiner Schwelle“ quantitativ.
- **Was L2 streng noch braucht:** die gleiche Schranke für Brücken statt freier Irrfahrten (fester Endpunkt; bis auf Konstanten gleich, da der Endpunkt im Abstand ~ √δ liegt), für feste und nicht zufällige Nachbarbahnen mit beschränktem Score (Aufenthaltszeit-Argument, §15), und die Kreuzterme zweier exakt normierter Brücken.

## 19. Budget-Hebel: weiche Kosten und Endbereiche (2026-11-10) [N]

[skelett\_budget2.py](skelett_budget2.py): β = ¼, D = 0, w = 2048, je 20 000 Paare.

- *Weiche Kosten* gewichten Zellpaare im Sup-Abstand 0/1/2/3 mit w = 1 / 0,45 / 0,18 / 0,08. Das ist die Treffwahrscheinlichkeit relativ zu „gleiche Zelle“, aus der Bessel-Rechnung mit Zellseite ≈ √δ: P(0,5√δ) = 0,196, P(√δ) = 0,105, P(2√δ) = 0,038, P(3√δ) = 0,016.
- *Endbereich ausgelassen* heißt: gezählt werden nur Zeiten t ≥ t₀ von beiden Enden aus.

| A  | t₀  | hart: E J | hart: α\_max | weich: E J | weich: α\_max |
|----|-----|-----------|--------------|------------|---------------|
| 4  | 0   | 31,2      | 0,032        | 26,0       | 0,045         |
| 4  | 128 | 2,7       | 0,038        | 2,9        | 0,043         |
| 8  | 0   | 22,8      | 0,043        | 18,8       | 0,058         |
| 8  | 128 | 1,3       | 0,058        | 1,3        | 0,080         |
| 16 | 0   | 20,1      | 0,049        | 17,1       | 0,064         |
| 16 | 8   | 3,4       | 0,052        | 3,6        | 0,064         |
| 16 | 32  | 1,7       | 0,069        | 1,8        | 0,070         |
| 16 | 128 | 0,76      | 0,072        | 0,77       | 0,090         |

**Befund.**

- Weiche Kosten bringen etwa 30 % Budget (0,049 → 0,064 bei A = 16).
- Der *Mittelwert* von J kommt fast ganz von den gemeinsamen Endpunkten (20 → 0,8 ohne Endbereich). Der *Schwanz* aber nicht: Seine Rate steigt ohne Endbereich nur auf 0,07–0,09. Er kommt von „klebrigen“ Wiederbegegnungen im Inneren. Treffen sich zwei Routen, bleiben sie mit exponentiell fallender Wahrscheinlichkeit eine Weile beisammen, weil die Querschübe je Schritt klein gegen den Begegnungsradius sind.
- **Für diese Routenfamilie liegt das Budget bei etwa 0,05–0,09** je Zellpaar mit Kosten „gleiche Zelle“.

**Folgen für die Schwelle.**

- Die Kosten je Paar sind ≈ 1/m + P\_Treffen mit P\_Treffen ≈ 0,66/(ln r + 2,1) bei κ = 1 (§18). Bei Budget 0,07 braucht man ln r ≳ 7,3, also r ≳ 1500 und ρ ≲ 4·10⁻⁷. Das ist besser als die 3·10⁻¹¹ aus §18, aber vor weiteren Faktoren (mehrere Brücken je Begegnung, Auswahl, Wählbarkeit).
- Für physikalische Dichten (ρ = 1/16, ln r ≈ 1,4) müsste das Budget bei 0,2 oder mehr liegen, also 3- bis 10-mal höher. Die Kopplung g\_eff ≈ 1/ln(1/ρa²) ≈ 0,17 ist dort nicht klein. Mit einer *störungsartigen* Zählung (Kosten je Begegnung gegen Budget) ist das nach diesen Zahlen nicht zu erwarten.
- **Strategische Lage:** Der Staffellauf-Beweis führt realistisch zu einem Existenzsatz mit sehr kleinem ρ\*, eventuell um einige Größenordnungen verbesserbar (Budget-Hebel: weiche Kosten, Skelette mit schnellerem Auseinanderlaufen nach Begegnungen). Mittlere Dichten bräuchten eine nicht-störungsartige Idee.
- **Für L2 heißt das:** Die Aussage sollte mit weichen Abstandsgewichten formuliert werden, also Kosten ~ Treffwahrscheinlichkeit im Abstand d statt Indikator d ≤ 1.

### 19.1 Kurzzeit-Rauschen: Beharrlichkeit trennt, Rauschen verklebt [N]

Variante mit Gewicht b₀ auf der kürzesten Skala ([skelett\_budget2.py](skelett_budget2.py) --b0). Weiche Zählung, β = ¼, D = 0:

| b₀  | A = 16, ganz: E J / α\_max | A = 16, innen (t₀ = 128): E J / α\_max | A = 32, innen: α\_max |
|-----|----------------------------|----------------------------------------|-----------------------|
| 0   | 14,8 / 0,071               | 0,60 / 0,106                           | 0,108                 |
| 0,25 | 15,0 / 0,069              | 0,65 / 0,102                           | 0,115                 |
| 1   | 17,1 / 0,061               | 0,76 / 0,089                           | –                     |
| 2   | 22,1 / 0,049               | 1,14 / 0,069                           | –                     |
| 4   | 31,7 / 0,034               | 2,57 / 0,045                           | –                     |
| 16  | 55,1 / 0,021               | 7,95 / 0,022                           | –                     |

- **Gegen die Vermutung:** Größere Kurzzeit-Schübe *verschlechtern* das Budget. Rauschen auf kurzen Skalen macht die Routen dort diffusiv, und diffusiv ist in 2D genau marginal, also häufigere Wiederbegegnungen. Was die Routen trennt, ist die Beharrlichkeit der großen Skalen.
- **Bestes Budget dieser Familie:** α\_max ≈ 0,07 für die ganze Route, ≈ 0,11 im Inneren (b₀ = 0, A = 16–32, weiche Kosten). Die gemeinsamen Endpunkte begrenzen den Rest; ein „Auffächern“ der Endbereiche könnte den inneren Wert annähern.
- **Was das für ρ\* heißt:** Ein Paar in derselben Zelle trifft sich mit P\_δ ≈ 1,23/(ln √δ + 2,1), also P ≈ 0,2 bei √δ ≈ 64 Gitterabständen. Allein P\_δ < 0,1 bzw. < 0,07 verlangt √δ = λ r ≳ 3·10⁴ bzw. 5·10⁶. Mit λ ~ 10 sind das ρ\* ~ 10⁻⁷ bzw. 4·10⁻¹², vor κ₂, Teilchenwahl und weiteren Faktoren (§20). Die Schwelle hängt also extrem an den Konstanten in L2.

## 20. L2 mit weichen Gewichten: Aussage und Beweisgerüst (2026-11-10) [B, Teile S]

**Rahmen.** Scheibe k, Routen R und R′ mit Sternpfaden. In jeder Zelle c\_l (l ≥ 1) einer Route wird genau eine Brücke neu gezogen (Label j\_l, von S\_{j\_l} nach Y\_{j\_{l−1}}). In c₀ wird das Stück von j₀ gelöscht. Im zweiten Moment mit Gegen-Lücken-Bezug (§10) entstehen Kosten nur bei Zellpaaren (c, c′) ∈ Stern\_k(R) × Stern\_k(R′) mit kleinem Sup-Abstand d. Dort stehen sich die bedingten Normierer nicht mehr unabhängig gegenüber.

**Lemma L2 (Ziel).** Für jedes solche Paar erfüllt der Kreuzfaktor F(c, c′), bedingt auf Umgebung und Routen,

```text
E[F(c, c′) | …]  ≤  1 + κ₂ · w(d) · ( 1/m_e + P_δ )
w(0..3) = 1, 0,45, 0,18, 0,08 (darüber Gauß-artig klein),   P_δ = sup über wählbare Endpunkte der Treffwahrscheinlichkeit
zweier Brücken in derselben Zelle,   m_e = Zahl wählbarer Teilchen je Zelle (≥ b₋ m nach L1)
```

**Folge.** Der Gesamtkreuzfaktor ist ≤ exp(κ₂ (1/m\_e + P\_δ) · J\_weich). Bedingung des Beweises:

```text
κ₂ · (1/m_e + P_δ)  <  α_max^{weich}  ≈ 0,07   (ganze Route; ≈ 0,11 im Inneren, §19.1)
```

**Beweisgerüst.**

1. *Exakte bedingte Gesetze je Zelle* (Markov-Eigenschaft, §13.1) [S].
2. *Einpfad-Randdichte:* Die bedingte Dichte einer neu gezogenen Brücke ist ≤ (1 − ε)^{−1} mal die der freien Brücke. Das gilt bei wählbaren Endpunkten und beschränktem Score, ε ≈ C κ/ln(1/ρ) (§15) [B].
3. *Zwei Brücken verschiedener Routen, verschiedene Labels:* Der Kreuzfaktor ist ein Quotient von Vermeidungswahrscheinlichkeiten (gemeinsam gegen einzeln), also |F − 1| ≤ P(Treffen)/(1 − ε)². P(Treffen) bei Endpunktabstand ~ d·s und Dauer δ ~ s² ist für freie Irrfahrten exakt berechenbar (§18, Bessel) [S]. Für Brücken gilt es bis auf Konstanten, weil die Endpunkte im Abstand ~ √δ liegen [B]. Daraus kommen die Gewichte w(d).
4. *Geteiltes Label:* Wahrscheinlichkeit ≤ 1/m\_e bei gleichverteilter Wahl; Kosten ≤ e^{C}, Quotient der Brückenkerne wie (28) im Preprint, da alle Versätze ≤ C s bei δ ~ s² [B].
5. *Löschzelle gegen Brücke:* Fehlt in c₀ das Stück von j₀ der einen Route, so ändert das die Umgebung der Brücke der anderen. Die Kosten sind von derselben Ordnung wie in 3, weil nur das Fehlen statt eines Treffens zählt [B].

**Zahlen zur Konstante.**

- P\_δ ≈ 0,2 bei √δ ≈ 64 Gitterabständen und fällt wie A/(ln √δ + B) (§18, Zähler bei Abstand 0,5√δ).
- 1/m\_e ≲ 0,05 schon bei 20 wählbaren Teilchen je Zelle.
- Fit an §18 (Abstand 0,5√δ, κ = 1): P\_δ ≈ 1,23/(ln √δ + 2,1).
- Mit κ₂ ≈ 2 und Budget 0,07 braucht man P\_δ ≲ 0,03, also ln √δ ≳ 39 und √δ ~ 10¹⁷ Gitterabstände. Mit κ₂ = 1 und Budget 0,11 (Endbereiche aufgefächert) genügt P\_δ ≲ 0,06, also ln √δ ≳ 18 und √δ ~ 10⁸.
- Wegen ρ = (λ/√δ)² mit λ ~ 10 ergibt das ρ\* ~ 10⁻¹⁴ (günstiger Fall) bis 10⁻³²: Die Schwelle hängt extrem an κ₂ und am Budget.
- κ₂ bestimmt ρ\* exponentiell. Als Nächstes sollte κ₂ numerisch gemessen werden: Kreuzfaktoren zweier neu gezogener Brücken in Wurm-Umgebungen.

**Offen [L]:**
- die Score-Schranken (aus L1) für Schritt 2,
- Brücken statt freier Irrfahrten mit expliziter Konstante in Schritt 3,
- die Löschzellen in Schritt 5,
- die Gaußsche Abschneidung der Gewichte für d ≥ 4.

## 21. κ₂ gemessen: Die Umgebung verstärkt nicht, aber Worst-Case-Schranken wären katastrophal (2026-11-10) [N]

[l2\_kappa.py](l2_kappa.py): zwei Teststücke mit Start gleichverteilt in derselben Zelle (Seite s), Dauer δ = s², Umgebung als freies Gas der Dichte ρ in 3×3 Zellen, m = ρ s² Teilchen je Zelle. Je Punkt 20 000 Proben.

| m   | ρ      | s  | P(Treffen) frei | P(beide weichen aus) | P(Treffen \| beide weichen aus) | κ\_Umgebung     |
|-----|--------|----|-----------------|----------------------|---------------------------------|-----------------|
| 0,5 | 0,05   | 3  | 0,519           | 0,085                | 0,550 ± 0,012                   | 1,06            |
| 0,5 | 0,0125 | 6  | 0,455           | 0,114                | 0,467 ± 0,010                   | 1,03            |
| 1   | 0,05   | 4  | 0,487           | 0,016                | 0,497 ± 0,028                   | 1,02            |
| 1   | 0,0125 | 9  | 0,418           | 0,0097               | 0,477 ± 0,036                   | 1,14            |
| 2   | 0,05   | 6  | 0,454           | 10⁻⁴                 | (zu wenig Ereignisse)           | –               |
| 10  | 0,0125 | 28 | 0,345           | 0                    | –                               | –               |

**Befunde.**

1. **Das Bedingen auf „der Umgebung ausweichen“ verstärkt die Kreuzkosten kaum.** κ\_Umgebung liegt bei 1,0–1,15, wo es messbar ist. Numerisch gilt also κ₂ ≈ 1 bis auf den Unterschied Brücke gegen Irrfahrt und den Term für geteilte Labels.
2. **Die Ausweichwahrscheinlichkeit eines einzelnen Stücks ist winzig:** P(ausweichen) ≈ exp(−2πm/ln(2δ)). Mit m ~ K ln(1/ρ) (aus L1) und ln δ ≈ ln(1/ρ) ist das die feste Konstante p\* ≈ e^{−2πK}, wie im 3D-Preprint (dort ρ a s² = a K²). Für die Exaktheit ist das unerheblich, die Normierung ist exakt.
3. **Gefahr für die Schwelle:** Ein Beweis, der die bedingte Dichte grob durch 1/p\* mal die freie abschätzt (Einpfad-Randdichte), bekäme κ₂ ~ p\*^{−2} = e^{4πK}. Im 3D-Preprint schadet das nicht, weil die Kreuzkosten dort wie eine Potenz r^{−1/2} fallen. In 2D fallen sie nur wie 1/ln(1/ρ), und die Bedingung κ₂ P\_δ < α\_max würde ln(1/ρ\*) ~ e^{4πK}/α\_max erzwingen, also eine doppelt exponentiell kleine Schwelle.
4. **Absolute Größe:** Zwei Stücke in derselben Zelle treffen sich bei s ≤ 28 mit P ≈ 0,35–0,5, weit über dem Budget. Die nötigen Zellgrößen sind astronomisch (§20).

**Folgerung für L2 [L].** Für eine vernünftige Schwelle braucht L2 eine *scharfe* Form: Die Kreuzkosten zweier exakt bedingter Stücke sind ≤ (1 + o(1)) mal die freien Kreuzkosten, ohne den Faktor 1/p\*². Kandidaten:
- eine Korrelationsungleichung (FKG bzw. Harris) für Ausweichereignisse in Raum-Zeit,
- ein Vergleich über die Doob-Transformation, da beide Stücke im *selben* Umgebungsmaß bedingt werden.

Numerisch ist die scharfe Form gut belegt (κ\_Umgebung ≈ 1). Streng ist sie offen. Mit Worst-Case-Konstanten bleibt nur ein Existenzsatz mit doppelt exponentiell kleinem ρ\*.

### 21.1 Die 2D-Spannung zwischen den Skalen [B/L]

- **L1 (Dichteschranken)** braucht Zellen mit m ≥ K\_L1 ln(1/ρ) Teilchen, K\_L1 = C/c groß. Dabei ist C die Konstante der Lokalisierungskosten und c die der Ballungsschranke.
- **Der Staffellauf** zieht Stücke neu, die eine Zelle überspannen (δ ~ s²). Ein solches Stück stößt im Mittel mit 2πm/ln(2δ) ≈ 2π K anderen zusammen, also gilt p\* ≈ e^{−2πK}. Damit Worst-Case-Faktoren 1/p\*² erträglich bleiben, müsste K ≲ 0,3 sein.
- **Geteilte Labels** kosten ~ 1/m. Das verlangt viele Teilchen je Zelle (m → ∞), was mit m ~ K ln(1/ρ) noch geht.
- **Kurze Sprünge** (Stücke der Dauer ~ r², Kette über Nachbarteilchen) machen p\* ≈ 1. Dann gibt es aber nur O(1) Kandidaten je Sprung, und die Wahrscheinlichkeit eines geteilten Labels bleibt O(1).
- **In 3D** tritt die Spannung nicht auf: Dort ist die Stoßzahl eines zellüberspannenden Stücks ρ a s² = a K² fest, die Kreuzkosten fallen wie r^{−1/2}, und Konstanten spielen für die Schwelle kaum eine Rolle.

**Damit ist der zentrale offene Punkt des verdünnten 2D-Beweises benannt:** Man braucht entweder

1. **ein scharfes L2:** Kreuzkosten exakt bedingter Stücke ≤ (1 + o(1)) × frei, ohne 1/p\*². Numerisch spricht κ\_Umgebung ≈ 1 dafür. Dann ist großes K unschädlich. Oder
2. **zwei Skalen:** grobe Zellen für L1 (Statistik, Peierls), feine Zellen mit m ≈ K′ ln(1/ρ), K′ klein, für den Staffellauf. Dafür muss Peierls auch für Mengen feiner Zellen gelten, bei glatter Abschneidung auf der groben Skala. Das ist offen.

Ohne eines davon bleibt nur ein Existenzsatz mit doppelt exponentiell kleinem ρ\*.

## 22. Scharfes L2: Doob-Verhältnis exakt gerechnet (2026-11-10) [S + N]

**Identität [S].** Zwei Stücke werden unabhängig in derselben festen Umgebung auf „Ausweichen“ bedingt. Ihre bedingten Randverteilungen sind p^h\_i = p\_i · r\_i mit dem Doob-Verhältnis

```text
r_i(x, t) = g_i(x, t) · h(x, t) / Z_i
g_i = P(bis t ausgewichen, bei x),   h = P(ab (x, t) auszuweichen),   Z_i = P(ausweichen) = p*
```

Für die gemeinsame Aufenthaltszeit L gilt exakt κ\_L := E[L | beide weichen aus]/E[L frei] = E\_w[r₁ r₂], mit w = freie Treffpunktverteilung. Der Worst-Case benutzt r ≤ 1/Z, also κ\_L ≤ 1/Z².

**Exakte Rechnung** ([l2\_doob.py](l2_doob.py)): g und h aus Einteilchen-Dynamik vorwärts und rückwärts in fester Umgebung (freies Gas, Dichte ρ, Torus 3s × 3s, Dauer ~ s²), je 12 Umgebungen.

| ρ      | m | s  | K = m/ln(1/ρ) | κ\_L Median / Mittel / Max | Z (Median) | 1/Z² (Median) |
|--------|---|----|---------------|----------------------------|------------|---------------|
| 0,05   | 1 | 4  | 0,33          | 1,20 / 1,25 / 1,70         | 0,36       | 7,6           |
| 0,05   | 2 | 6  | 0,67          | 1,41 / 1,46 / 2,07         | 0,021      | 2·10³         |
| 0,05   | 4 | 9  | 1,34          | 1,58 / 1,83 / 3,90         | 9·10⁻⁴     | 1·10⁶         |
| 0,05   | 8 | 13 | 2,67          | 2,31 / 2,45 / 5,39         | 5·10⁻⁷     | 4·10¹²        |
| 0,0125 | 1 | 9  | 0,23          | 1,15 / 1,17 / 1,42         | 0,20       | 25            |
| 0,0125 | 2 | 13 | 0,46          | 1,23 / 1,45 / 2,43         | 0,058      | 3·10²         |
| 0,0125 | 4 | 18 | 0,91          | 1,65 / 1,64 / 2,12         | 3·10⁻³     | 9·10⁴         |
| 0,0125 | 8 | 25 | 1,83          | 1,94 / 2,37 / 4,28         | 1,5·10⁻⁵   | 5·10⁹         |

**Befunde.**

1. **Der Worst-Case ist völlig unrealistisch:** κ\_L bleibt bei 1,2–2,4, während 1/Z² bis 10¹² geht. Der globale Ausweichfaktor kürzt sich im Verhältnis r.
2. **Gesetz:** ln κ\_L ≈ 0,27 · m/ln s, bei m = 8: 0,83 (s = 13) und 0,66 (s = 25), das Verhältnis ist das von ln s. Jedes Hindernis in Reichweite erzeugt eine logarithmische Delle in r, und ihre zweiten Momente addieren sich im Exponenten: ln κ ≈ Σ\_Hindernisse c/ln δ.
3. **Mit m = K ln(1/ρ) und ln s ≈ ½ ln(1/ρ): κ₂ ≈ e^{0,54 K}**, eine feste Konstante. Der Worst-Case wäre e^{≈ 4πK}, also im Exponenten etwa 25-mal schlechter. Die frühere Erwartung κ − 1 ~ K/ln(1/ρ) war zu optimistisch: Die Dellen sind einzeln klein, aber es sind ~ m viele.

**Folgen für die Schwelle.**

- Kosten je Begegnung ≈ (e^C − 1)/m + e^{0,54K} · C′/ln(1/ρ). Beide Terme gehen für ρ → 0 bei festem K gegen null, also gibt es **keinen doppelt exponentiellen Einbruch**, sofern die scharfe Form bewiesen wird.
- ln(1/ρ\*) ≈ e^{0,54 K} · C′/α\_max. Bei K = 3 ist das ≈ 5 · 1,2/0,07 ≈ 90, also ρ\* ~ e^{−90}. Bei K = 10 sind es ≈ 220 · 17 ≈ 4000. **Die Schwelle hängt also vor allem an der L1-Konstante K = K\_L1**, und es lohnt sich, sie klein zu halten (Lokalisierungs- gegen Ballungskonstante).

**Zu beweisen (scharfes L2) [L].** E\_w[r₁ r₂] ≤ exp(Σ\_j ε\_j), Summe über die Hindernisse in Reichweite, ε\_j ≲ c/ln δ je Hindernis. Ansätze:
- Produktstruktur des Doob-Verhältnisses für dünne Hindernisse (Einschluss–Ausschluss bzw. Clusterentwicklung für die Ausweichwahrscheinlichkeiten),
- Gaußscher Vergleich der logarithmischen Dellen,
- direkt über die Green-Funktion mit Dirichlet-Punkten.

Die Numerik gibt das Ziel genau vor: c ≈ 0,27 je Hindernis in Einheiten von 1/ln s.

## 23. Scharfes L2: Rückführung auf ein Stück, Literatur, Beweisweg (2026-11-10)

**Verkleben [S].** Aus κ\_L = Σ p¹p² r¹r² / Σ p¹p² folgt exakt

```text
κ_L = P_L(A¹ ∩ A²) / ( P(A¹) P(A²) )
```

P\_L ist das mit der gemeinsamen Aufenthaltszeit L gewichtete Paargesetz. Unter P\_L sind die Stücke um einen zufälligen Treffzeitpunkt verklebt und müssen dort denselben Fallen nur einmal ausweichen. Das erklärt ln κ ≈ Trefferrate × Klebezeit ≈ c m/ln δ (§22). Die gemessenen Werte entsprechen einer Klebezeit von etwa 9 % der Dauer.

**Rückführung auf ein Stück [N].** Cauchy–Schwarz gibt κ\_L ≤ √(E\_w[(r¹)²] E\_w[(r²)²]). Exakt nachgerechnet ([l2\_doob.py](l2_doob.py)) liegt diese Schranke im Median nur 0–8 % über κ\_L (ρ = 0,05 und 0,0125, m = 1 … 8). Das scharfe L2 ist damit im Wesentlichen eine Aussage über **ein** Stück: die gewichtete χ²-Abweichung seiner bedingten Aufenthaltsverteilung von der freien,

```text
1 + χ²_u = Σ_x p_u(x) r(x,u)²  =  P(A¹ ∩ A² | zwei Kopien mit gemeinsamem Start und gemeinsamem Punkt zur Zeit u) / P(A)²
```

Das ist wieder eine Verklebe-Darstellung, jetzt mit Kopien desselben Stücks.

**Literatur [Lit].**

- Drewitz, Gärtner, Ramírez, Sun, *Survival probability of a random walk among a Poisson system of moving traps* (arXiv 1010.3958): Annealed fällt die Überlebenswahrscheinlichkeit in d = 2 wie exp(−c ν t/log t), dieselbe 2D-Form wie unser e^{−2πm/ln δ}. Quenched (feste Fallen) fällt sie exponentiell. Werkzeug ist das „Pascal-Prinzip“: Stillstehen maximiert das annealed Überleben.
- Athreya, Drewitz, Sun, *Random walk among mobile/immobile traps: a short review* (arXiv 1703.06617), und *Subdiffusivity … on ℤ* (arXiv 1603.01709): Pfadmaß des auf Überleben bedingten Wanderers.
- Athreya, Drewitz, Sun 2024, *An invariance principle for a random walk among moving traps via thermodynamic formalism* (arXiv 2401.10179).

Unser κ ist dort eine Frage nach zwei Kopien in derselben Fallen-Umgebung.

**Beweisweg über die Poisson-Formel [S + B].** Für Poisson-Fallen (Dichte ν, unabhängige Irrfahrten) ist die Umgebungsmittelung exakt:

```text
E_Umg[1_{A¹} 1_{A²}] = exp(−ν Σ_y P_y(Falle trifft X¹ oder X²))
⇒ E_Umg[1_{A¹} 1_{A²}] / (E_Umg 1_{A¹} · E_Umg 1_{A²}) = exp(ν · V₂(X¹, X²)),   V₂ = Σ_y P_y(Falle trifft beide)
```

V₂ ist das *gemeinsame Fangvolumen* der beiden Pfade, eine rein geometrische Größe ohne Umgebung. Für Pfade, die eine Zeit τ verklebt sind, ist V₂ ~ 2πτ/ln τ (2D-Wiener-Würstchen), also ν V₂ ~ c m/ln δ, genau die gemessene Form.

Plan für einen Beweis des scharfen L2:

1. **Geometrie:** E[exp(ν V₂)] unter der Verklebe-Verteilung beschränken, mit Schnittvolumina zweier 2D-Wiener-Würstchen und Klebezeiten der Relativbewegung (2D-Lokalzeit am Ursprung).
2. **Von Poisson zum Grundzustand:** Die Umgebung ist bei uns kein Poisson-Feld, sondern die übrigen Teilchen. Die exponentiellen Momente linearer Statistiken (L1 mit Raum-Zeit-Erweiterung, §17) sollen die Poisson-Formel durch eine Ungleichung ersetzen: E\_Umg[exp(Σ\_Fallen φ)] ≤ exp(C ρ ∫(e^{φ} − 1)) für die nötigen φ.
3. **Annealed statt quenched:** Im zweiten Moment des Staffellaufs wird ohnehin über die Umgebung gemittelt. Zu prüfen ist, ob dort die *annealed* Kreuzgröße genügt. Dann ersetzt Schritt 1 die quenched Schranke.

Damit wäre das scharfe L2 auf zwei klar umrissene Teilaufgaben reduziert: Geometrie zweier Würstchen und Poisson-Vergleich über L1.

## 24. Quenched oder annealed? Das richtige Ziel ist eine Momentenschranke (2026-11-10) [N + B]

**Was der Beweis braucht.** Im zweiten Moment des Staffellaufs ist jeder lokale Faktor *für die gegebene Umgebung* exakt normiert. Deshalb erscheint die quenched Verstärkung κ\_q(Umg) = P(A¹A² | Umg)/(P(A¹ | Umg) P(A² | Umg)), gemittelt über die Umgebung und multipliziert über die Begegnungen: E\_Umg[Π\_i κ\_q(i)]. Die annealed Poisson-Formel aus §23 beschreibt dagegen das Verhältnis der Mittelwerte. Sie ist ein Leitfaden, aber nicht direkt die gebrauchte Größe.

**Pfadweise lineare Schranke? Nein [N].** [l2\_linear.py](l2_linear.py), ρ = 0,0125, je 150 Umgebungen: ln κ\_q korreliert mit der Zahl der nahen Umgebungsteilchen nur schwach (0,38 / 0,26 / 0,12 für m = 2 / 4 / 8), mit Resten bis 0,5–0,9 über der Regressionsgeraden. κ\_q hängt an der Feingeometrie, vor allem daran, welche Teilchen früh nahe am Start sind.

**Momente über die Umgebung [N]:**

| m | s  | ln E κ | ln E κ²/2 | ln E κ³/3 | ln E κ⁴/4 | ln κ: Median / 90 % / 99 % |
|---|----|--------|-----------|-----------|-----------|----------------------------|
| 2 | 13 | 0,31   | 0,34      | 0,36      | 0,39      | 0,27 / 0,58 / 0,81         |
| 4 | 18 | 0,50   | 0,54      | 0,57      | 0,60      | 0,46 / 0,82 / 1,05         |
| 8 | 25 | 0,82   | 0,88      | 0,94      | 1,00      | 0,75 / 1,24 / 1,49         |

- **Leichte Schwänze, fast log-normal mit kleiner Varianz:** ln E κ^q/q wächst nur langsam mit q. Var(ln κ) ≈ 0,05–0,1.
- ln E κ ≈ 0,1 m bei s = 13–25, verträglich mit ln κ ≈ 0,27 m/ln s (§22).

**Neues Ziel für das scharfe L2 (Momentform) [B].**

```text
E_Umg[ κ_q^p ]  ≤  exp( p · c(p) · m / ln s ),      c(p) mäßig wachsend (numerisch c(1) ≈ 0,27 … 0,33, c(4) ≈ 0,35 … 0,4)
```

Für Produkte über viele Begegnungen:

- *Ferne Begegnungen:* Entkopplung über die Raum-Zeit-Exponentialmomente aus L1 (§17). Die Umgebungen weit entfernter Zellen sind nahezu unabhängig.
- *Nahe Begegnungen* (verklebte Strecken über mehrere Scheiben): Die Kosten addieren sich je Scheibe; das ist schon in der Zählung J enthalten.

**Weg zum Beweis der Momentform:**

1. *Verklebe-Darstellung* (§23) je Umgebung.
2. *Poisson-Vergleich:* Für Poisson-Fallen ist E\_Umg[P(A¹A² | Umg)] exakt exp(−ν V\_∪). Die quenched Normierer P(A^i | Umg) im Nenner werden über Jensen bzw. Positivität aus den Umgebungsmomenten nach unten abgeschätzt, also log-konvexe Mittelung.
3. *Grundzustand statt Poisson* über L1.

Offen [L]: Schritt 2 sauber, weil der Nenner quenched ist, und die Geometrie des gemeinsamen Fangvolumens (Schnitt zweier 2D-Wiener-Würstchen unter der Verklebe-Verteilung).

## 25. Scharfes L2: Lokalisierung und Produkt über die Fallen (2026-11-10) [N + B]

**Lokalisierung [N]** ([l2\_lokal.py](l2_lokal.py), ρ = 0,0125, je 30 Umgebungen). Berücksichtigt man nur Fallen, deren Bahn irgendwann im Sup-Abstand < D von der Startzelle ist:

| D       | s/8   | s/4   | s/2  | s    | 1,5 s | alle  |
|---------|-------|-------|------|------|-------|-------|
| m = 4: mittleres ln κ\_L | −0,14 | −0,11 | 0,06 | 0,40 | 0,43 | 0,43 |
| m = 8: mittleres ln κ\_L | −0,11 | −0,02 | 0,18 | 0,75 | 0,78 | 0,78 |

- Bei D = s sind 93–96 % erreicht, bei 1,5 s alles. Die mittlere Abweichung zwischen D = s und „alle“ ist 0,03. **Fallen jenseits der Reichweite √δ ~ s spielen keine Rolle.**
- *Vorzeichen:* Sehr nahe Fallen allein machen κ < 1, sie drängen die Stücke auseinander. Fallen in mittlerem Abstand machen κ > 1, sie sperren beide in dieselbe freie Gegend.

**Produkt über die Fallen [N]** ([l2\_additiv.py](l2_additiv.py)): Verglichen werden ln κ(alle Fallen in Reichweite) und Σ\_j ln κ(nur Falle j). Je 20 Umgebungen, ρ = 0,0125:

| m | Fallen in Reichweite | ln κ(alle) | Σ\_j ln κ(Falle j) | Korrelation | Differenz Mittel / Max | subadditiv |
|---|----------------------|------------|--------------------|-------------|------------------------|------------|
| 2 | 19                   | 0,291      | 0,325              | 0,95        | −0,034 / +0,17         | 65 %       |
| 4 | 36                   | 0,544      | 0,548              | 0,57        | −0,004 / +0,81         | 65 %       |
| 8 | 67                   | 0,728      | 0,826              | 0,73        | −0,098 / +0,29         | 80 %       |

- **Im Mittel über die Umgebungen gilt die Produktvermutung**; die Summe der Einzelfallen liegt sogar leicht darüber (subadditiv im Mittel).
- **Pfadweise nicht:** Die Abweichung D = ln κ(alle) − Σ\_j ln κ(j) schwankt, mit Ausreißern bis +0,8. Positive D entstehen, wenn Fallen zusammenwirken, etwa als Korridor, der beide Stücke gemeinsam einsperrt (Paareffekt).

**Beweisstruktur für das scharfe L2 [B].**

1. **Lokalisierung:** Nur Fallen in Reichweite ~ √δ zählen. Ferne Fallen ändern das Doob-Verhältnis nur um Harnack-Faktoren nahe 1 [B, 2D-Harnack für Irrfahrten mit spärlichen Fallen].
2. **Additivität im Mittel:** ln κ\_q(Umg) = Σ\_j ln κ(γ\_j) + D(Umg), mit E D ≤ 0 numerisch. Gebraucht wird nur eine Exponentialmoment-Schranke für den positiven Teil von D. Mit Hölder gilt E κ ≤ (E Π\_j κ(γ\_j)^p)^{1/p} (E e^{qD})^{1/q}. Der erste Faktor ist nach Campbell exakt exp(ν ∫(κ₁^p − 1)/p); der zweite ist ein Paareffekt zweiter Ordnung (Mayer-artig: Fallenpaare, die gemeinsam einsperren) [L, Kernpunkt].
3. **Campbell-Formel:** Für Poisson-Fallen gilt exakt E\_Umg[Π\_j κ(γ\_j)] = exp(ν ∫ (κ₁(γ) − 1) dγ).
4. **Eine Falle, zwei Stücke:** κ₁(γ) − 1 = Cov(Ausweichen¹, Ausweichen²)/P(Ausweichen)² ≈ P(Falle trifft beide verklebten Stücke). Das Integral ist das gemeinsame Fangvolumen aus §23, also ν ∫(κ₁ − 1) ≈ ν E[V₂] ≲ c m/ln δ [B, 2D-Treffwahrscheinlichkeiten].
5. **Vom Poisson-Feld zum Grundzustand** über die exponentiellen Momente aus L1 (§17) [B].

Bemerkenswert: Über 2 und 3 wird der quenched Mittelwert zur selben geometrischen Größe wie die annealed Poisson-Formel (§23). Die quenched Normierung kostet also nur den Additivitätsfehler.

## 26. Eine Falle, zwei Stücke: Campbell-Exponent über Fangvolumina (2026-11-10) [S + B]

**Bezeichnungen.** H^i = {Falle trifft Stück i}, P\_L = das mit der gemeinsamen Aufenthaltszeit gewichtete, also verklebte Paargesetz, P = frei. Für eine Falle γ gilt

```text
κ₁(γ) − 1 = [ P_L(H¹H²) − P(H¹)P(H²) − (P_L(H¹) − P(H¹)) − (P_L(H²) − P(H²)) ] / [ (1 − P(H¹)) (1 − P(H²)) ]
```

**Summe über das Poisson-Feld [S].** Der Startpunkt y der Falle wird summiert, der Fallenpfad gemittelt. Jede Wahrscheinlichkeit wird dabei zu einem Fangvolumen:

| Summe Σ\_y E\_γ[·] | ist gleich |
|--------------------|------------|
| P\_L(H¹H²)        | E\_{P\_L}[V₂(X¹, X²)], gemeinsames Fangvolumen der verklebten Stücke |
| P(H¹)P(H²)        | E\_{P⊗P}[V₂(X¹, X²)], gemeinsames Fangvolumen unabhängiger Stücke |
| P\_L(H^i), P(H^i) | E\_{P\_L}[V(X^i)] bzw. E\_P[V(X^i)], Fangvolumen eines Stücks |

Dabei ist V(X) = Σ\_y P\_y(Falle trifft X) und V₂ = Σ\_y P\_y(Falle trifft beide). Bis auf den Nenner (s. u.) gilt also

```text
Φ = ν Σ_y E_γ[κ₁ − 1]  ≈  ν { E_{P_L} V₂ − E_{P⊗P} V₂ }  −  ν Σ_i { E_{P_L} V(X^i) − E_P V(X^i) }
     („Verkleben lässt dieselbe Falle beide treffen“)        („verklebte Stücke sind etwas anders geformt“)
```

Reine Pfadgeometrie, keine Umgebung.

**Grobe Schranke [B].**

- *Nenner:* Wählbarkeit hält Fallen am Start mindestens ζr entfernt. Dann ist P(H^i) ≤ 1 − c(ζ) und der Nenner ≥ c(ζ)².
- *V₂ ≤ V₁ trivial:* Wer beide trifft, trifft das erste.
- *2D-Würstchen:* E V(X) ≈ 2π ν⁻¹ · νδ/ln δ, also ν E V ≈ 2π m/ln δ (Dvoretzky–Erdős bzw. Le Gall; Relativbewegung von Falle und Stück).
- *Formunterschied:* |E\_{P\_L} V − E\_P V| ≤ C · δ/ln δ, weil das Gewichten mit der Aufenthaltszeit die Pfadform nur beschränkt ändert.

```text
Φ ≤ C(ζ) · m / ln δ        also bei m = K ln(1/ρ):   Φ ≤ C(ζ) K
```

Damit ist das Ein-Fallen-Lemma in grober Form auf klassische 2D-Würstchen-Asymptotik zurückgeführt.

**Scharfe Konstante [H].** V₂ für verklebte Stücke ist ≈ V₁ mal den Anteil g der Fangereignisse, bei denen das zweite Stück noch in Log-Reichweite ist (Klebeanteil). Das ergibt Φ ≈ 2π g m/ln δ = π g m/ln s. Mit g ≈ 0,09 folgt Φ ≈ 0,28 m/ln s, genau das gemessene Gesetz ln κ ≈ 0,27 m/ln s (§22). Die grobe Schranke verliert also einen Faktor ~1/g ≈ 11 im Exponenten. Die Schwelle hängt davon über e^{Φ} ab, also lohnt sich die scharfe Form später.

### 26.1 Campbell-Exponent numerisch [N]

[l2\_einefalle.py](l2_einefalle.py): je 200 Einzelfallen mit gleichverteiltem Startpunkt. Φ = ν · Volumen · E[κ₁ − 1] ist für Poisson-Fallen exakt ln E\_Umg[Π\_j κ(γ\_j)].

| ρ      | m | s  | Φ           | Φ · ln s/m | Anteil Fallen mit κ₁ < 1 | gemessen: ln E κ / E Σ ln κ\_j (§24, §25) |
|--------|---|----|-------------|------------|--------------------------|-------------------------------------------|
| 0,05   | 4 | 9  | 0,68 ± 0,14 | 0,38       | 22 %                     | –                                         |
| 0,0125 | 2 | 13 | 0,38 ± 0,07 | 0,48       | 20 %                     | 0,31 / 0,33                               |
| 0,0125 | 4 | 18 | 0,62 ± 0,11 | 0,45       | 20 %                     | 0,50 / 0,55                               |
| 0,0125 | 8 | 25 | 1,36 ± 0,19 | 0,55       | 20 %                     | 0,82 / 0,83                               |
| 0,003  | 2 | 26 | 0,32 ± 0,05 | 0,53       | 20 %                     | –                                         |

- **Skalierung bestätigt:** Φ ≈ 0,5 · m/ln s über ρ = 0,05 … 0,003. Bei m = K ln(1/ρ) und ln s ≈ ½ ln(1/ρ) ist das Φ ≈ K.
- **Ordnung wie erwartet:** Φ ≥ E Σ ln κ\_j (Jensen) ≥ ln E κ im Mittel (Subadditivität, §25). Der Weg über Campbell verliert etwa einen Faktor 2 im Exponenten (Φ ≈ K gegen ln E κ ≈ 0,54 K). Das ist annehmbar.
- Etwa 20 % der Einzelfallen haben κ₁ < 1, das sind die nahen Fallen, die die Stücke auseinanderdrängen.

**Stand des scharfen L2.**

| Schritt | Inhalt | Stand |
|---------|--------|-------|
| 1 | Lokalisierung (nur Fallen in Reichweite √δ) | [N] eindeutig, [B] über Harnack |
| 2 | Additivität im Mittel, Paarfehler D | [N] im Mittel erfüllt; Exponentialmoment von D offen [L] |
| 3 | Campbell | [S] |
| 4 | Eine Falle: Φ ≤ C(ζ) m/ln δ (grob), Φ ≈ 0,5 m/ln s (numerisch) | [B] über V₂ ≤ V₁ und 2D-Würstchen |
| 5 | Poisson → Grundzustand | [B] über L1 |

## 27. Der Paarfehler D (2026-11-10) [N + B]

**Messung** ([l2\_paare.py](l2_paare.py), ρ = 0,0125). Verglichen werden D = ln κ(alle) − Σ\_j ln κ(j) und D₂ = Σ\_{j<k, nah} u₂(j,k) mit u₂(j,k) = ln κ(j,k) − ln κ(j) − ln κ(k):

| m | Umgebungen | Paare je Umgebung | Korrelation D/D₂ | Streuung D | Streuung D − D₂ | größtes u₂ | Mittel D / D₂ |
|---|------------|-------------------|------------------|------------|-----------------|------------|---------------|
| 2 | 15         | 66–276            | 0,88             | 0,149      | 0,072           | ≤ 0,10     | +0,02 / +0,04 |
| 4 | 6          | 325–861           | 0,85             | 0,162      | 0,176           | ≤ 0,08     | −0,06 / −0,03 |

**Befunde.**

- **D ist im Wesentlichen ein Paareffekt.** Bei m = 2 halbiert die Paarsumme die Streuung des Rests. Bei m = 4 überschießt D₂ (Werte bis ±0,4 gegen D bis ±0,34): Dort wirken schon Dreiergruppen mit umgekehrtem Vorzeichen.
- **Jeder einzelne Paarbeitrag ist klein** (|u₂| ≤ 0,1, meist ≤ 0,05). D entsteht aus Hunderten kleiner Beiträge beider Vorzeichen, mit Mittel ≈ 0 und Streuung ≈ 0,15. Zusammen mit §25: In 41 Umgebungen liegt D zwischen −0,34 und +0,81.

**Beweisweg ohne Konvergenz einer Clusterentwicklung [B + Lit].** Bei m ≳ 4 konvergiert die Clusterentwicklung nur knapp: Die Gesamtkopplung einer Falle an die übrigen in Reichweite ist ~ 30 · 0,02 ≈ 0,6. Besser ist **Konzentration für Funktionale eines Poisson-Prozesses**:

- **Hinzufüge-Kosten** von D für eine neue Falle γ: D\_γD = [ln κ(Γ ∪ γ) − ln κ(Γ)] − ln κ(γ). Das ist genau die Wechselwirkung von γ mit den vorhandenen Fallen, also Σ\_k u₂(γ, k) + höhere Ordnungen, und damit klein.
- **Ungleichung:** Eine modifizierte logarithmische Sobolev-Ungleichung bzw. Bennett-Ungleichung für Poisson-Prozesse (L. Wu, *A new modified logarithmic Sobolev inequality for Poisson point processes and several applications*, PTRF 118 (2000) 427–438; S. Bachmann, G. Peccati, *Concentration bounds for geometric Poisson functionals: logarithmic Sobolev inequalities revisited*, EJP 21 (2016), arXiv 1504.03138; dort Herbst-Argument mit Hinzufüge-Kosten) gibt E e^{q(D − E D)} ≤ exp(V · ψ(qβ)), mit β = sup |D\_γD| und V = ν ∫ (D\_γD)² dγ. Numerisch ist V ~ 30 · 0,05² ≈ 0,08, also gilt E e^{qD} ≈ e^{q E D} (1 + O(q² · 0,04)).
- **Mittelwert:** E D lässt sich über die Mecke-Formel durch Integrale der Paar- und höheren Beiträge ausdrücken. Numerisch ist E D ≈ 0 oder negativ. Eine Schranke |E D| ≤ C (Kopplung)² genügt.

**Stand des scharfen L2.**

| Schritt | Inhalt | Stand |
|---------|--------|-------|
| 1 | Lokalisierung | [N], [B] Harnack |
| 2 | Additivität im Mittel; Paarfehler D über Poisson-Konzentration | [N]; [B] mit [Lit] Wu, Bachmann–Peccati |
| 3 | Campbell | [S] |
| 4 | Eine Falle über Fangvolumina | [B], [N] Φ ≈ 0,5 m/ln s |
| 5 | Poisson → Grundzustand | [B] über L1 |

Damit hat jeder Schritt des scharfen L2 einen konkreten Beweisweg. Was bleibt, ist Ausschreiben mit Konstanten, kein offener Mechanismus mehr.

## 28. Woher die Konstante K kommt, und wie man sie klein macht (2026-11-10) [B + N]

K tritt in L1 als Mindestzellgröße s² ≥ K ln(1/ρ)/ρ auf, also m ≥ K ln(1/ρ) Teilchen je Zelle. Ist die Staffellaufzelle gleich der L1-Zelle, gilt κ₂ ≈ e^{0,54 K} (§22). K geht damit exponentiell in die Schwelle ein.

**Konstanten eingesetzt.**

- **Obere Schwänze (§16.5):** Ballungskosten c\_b = (π/3) Hρ/ln(1/(Hρ)) gegen μ\* ≈ 8πρ/ln(1/(ρa²)) verlangen H ≈ 50. Lokalisierungs- und Kippkosten (π² + 4)/s² ≤ c\_b/4 verlangen dann s² ≳ (53/H) ln(1/ρ)/ρ, also **K ≈ 1**. Unkritisch. *Korrektur 2026-11-10 (satz\_3\_9\_dichteschranken.md):* Mit den expliziten Konstanten C\_L = π²e² ≈ 73 und C\_K = 16e ≈ 44 statt (π² + 4) wird K\_a ≈ 445/H ≈ 6–9.
- **Untere Schwänze (§16.6):** Gewinn c₁ρ/ln(1/ρ) je hinzugefügtem Teilchen mit der strengen Untergrenze c₁ = π/16 ≈ 0,2. Sie ist etwa 40-fach zu schwach gegen Lieb–Yngvason 4π. Dagegen stehen die Dirichlet-Kosten der eingefügten Teilchen (~ 30/s² bei großzügigem Teilkasten) und Lokalisierungskosten der Übergangszone bei kleinem Einfügeanteil η. Ergebnis: **K ~ 10³**. Das ist der Engpass, und mit κ₂ ≈ e^{0,54K} wäre die Schwelle wieder doppelt exponentiell klein.

**Hebel 1: bessere strenge Energie-Untergrenze [N + B].** [l1\_kastenenergie.py](l1_kastenenergie.py) rechnet die exakte Hartkern-Grundenergie e\_b(n) im b×b-Neumann-Kasten:

| b  | e\_b(2) · b² ln b | Fit 4π ln b/(ln b + 1,77) | e\_b(3)/e\_b(2) |
|----|-------------------|---------------------------|-----------------|
| 4  | 5,465             | 5,52                      | 3,19            |
| 6  | 6,306             | 6,32                      | 3,17            |
| 8  | 6,776             | 6,79                      | 3,16            |
| 10 | 7,088             | 7,11                      | –               |
| 12 | 7,316             | 7,34                      | –               |
| 16 | 7,634             | 7,67                      | –               |
| 20 | 7,853             | 7,90                      | –               |
| 24 | 8,017             | 8,07                      | –               |

Exakte Eigenwerte ([l1\_kasten2.py](l1_kasten2.py), LOBPCG mit Mehrgitter-Vorkonditionierer, bis Dimension 1,7·10⁵). Ein freier Fit A ln b/(ln b + c) ergibt A ≈ 12,2 ≈ 0,97 · 4π und c ≈ 1,67. Der Grenzwert ist also **4π**, der Zweiteilchen-Wert mit doppelter Relativbewegung. Die Paarungsschranke (π/2, ein festes Teilchen in der Ecke) ist 8-fach zu schwach.

- Zwei *bewegliche* Teilchen kosten das 3,5- bis 4-Fache der Paarungsschranke, weil die Relativbewegung doppelt schnell ist und der Ecken-Ungünstigst-Fall wegfällt.
- e(3)/e(2) ≈ 3,2 ≈ C(3,2): Die Energie im Kasten ist nahezu paar-additiv, also quadratisch in n.
- **Streng ohne Weiteres** [S]: Σ\_i L\_i = (n−1)^{−1} Σ\_{i<j}(L\_i + L\_j) gibt e\_b(n) ≥ (n/2) e\_b(2). Mit e\_b(2) ≈ 4π/(b²(ln b + 1,7)) und optimierter Kastengröße (ρb² ≈ 2) folgt c₁ → π statt π/16, also **K um den Faktor ~16 kleiner** (nur noch Faktor 4 unter Lieb–Yngvason). Für große b braucht e\_b(2) eine strenge Untergrenze (Relativkoordinate mit doppeltem Laplace-Operator und Punktkapazität), numerisch ist sie bis b = 24 belegt.
- **Mit quadratischer Abhängigkeit** e\_b(n) ≥ C(n,2) e\_b(2)(1 − o(1)) (Dyson-Lemma auf dem Gitter, wie bei Lieb–Yngvason; numerisch e(3)/e(2) ≈ 3,2 ≈ C(3,2)) folgt c₁ → 4π, die Lieb–Yngvason-Konstante. K sinkt dann um den Faktor ~60, also K ~ 15–30.

**Bewertung.** Selbst K ~ 15–30 gibt κ₂ ≈ e^{8}–e^{16}. Die bloße Verbesserung der Konstanten reicht nicht für eine vernünftige Schwelle, solange Staffellaufzelle und L1-Zelle gleich sind.

**Hebel 2: die Skalen entkoppeln (§21.1).** Kleine Staffellaufzellen (K\_r ~ 1, κ₂ ≈ e^{0,5}) und große L1-Zellen. Dafür braucht man untere Schwänze auf der *feinen* Skala ohne Gradientenkosten. Kandidat ist ein **Feynman–Kac-Lochargument** wie in §17: P(Zelle während einer Scheibe leer) ≤ exp(−δ · ΔE\_Loch), mit ΔE\_Loch = E₀(Gitter ohne Zelle) − E₀(Gitter). Das gilt auf jeder Skala, mehrzeitig und für viele Löcher zugleich (Peierls). Physikalisch ist ΔE\_Loch ≥ Druck × Fläche ~ 2πρ² s²/ln, also δ ΔE ~ 2π K\_r² ln(1/ρ) und P ≤ ρ^{2πK\_r²}.

Für den Beweis braucht man aber obere und untere Energieschranken mit *gleicher* Konstante (Lieb–Yngvason scharf auf beiden Seiten), weil ΔE eine Differenz ist. Die obere hat L1d bereits (asymptotisch scharf). Die untere wäre das Gitter-Dyson-Lemma.

**Folgerung.** Der eigentliche analytische Engpass der Schwelle ist eine **scharfe untere Schranke für die Energie je Teilchen** auf dem Gitter, E/N ≥ 4πρ/ln(1/ρa²) · (1 − o(1)). Das ist das Gegenstück zu Lieb–Yngvason 2D (Kontinuum, 2001). Mit ihr werden beide Hebel wirksam: K klein in L1, und Lochkosten auf feiner Skala.

## 29. Diskretes Dyson-Lemma und der Weg zur scharfen Energie-Untergrenze (2026-11-10)

**Lemma (diskretes Dyson-Lemma) [S].** B sei ein Gitterbereich, 0 ∈ B, S ⊂ B eine Zielmenge („Schale“), θ der Einheitsstrom von 0 nach S, mit S geerdet und Einheitswiderständen, und μ seine Austrittsverteilung auf S (gleich der Treffverteilung der Irrfahrt von 0). Für jedes f: B → ℝ mit f(0) = 0 gilt

```text
Σ_{Kanten in B} (f(x) − f(x′))²  ≥  Σ_{y∈S} U(y) f(y)²,      U = μ / R_eff(0 ↔ S),      Σ_y U(y) = 1/R_eff(0 ↔ S)
```

*Beweis.* Der Strom ist kreisfrei und zerfällt in ein Wahrscheinlichkeitsmaß auf Pfaden P von 0 nach S mit P(e ∈ P) = θ\_e. Längs P gilt f(Ende) = Σ\_{e∈P} ∇\_e f. Cauchy–Schwarz mit den Gewichten θ\_e gibt f(Ende)² ≤ (Σ\_{e∈P} (∇\_e f)²/θ\_e)(Σ\_{e∈P} θ\_e). Für den Strom ist Σ\_{e∈P} θ\_e der Potentialabfall längs P, für jeden Pfad gleich R\_eff. Mitteln über P (Endpunkt verteilt nach μ) ergibt Σ μ f² ≤ R\_eff Σ\_e θ\_e (∇\_e f)²/θ\_e ≤ R\_eff Σ\_Kanten (∇f)². ∎

Anders als im Kontinuum (Dyson 1957; Lieb–Yngvason) braucht man keine Sternförmigkeit von B. Jeder Bereich mit einem Strom geht, also auch Nächster-Nachbar-Zellen beliebiger Form. Es ist dasselbe Werkzeug wie in L1c (Thomson plus Cauchy–Schwarz).

**Konstante [N]** ([l1\_dyson\_reff.py](l1_dyson_reff.py)): Für die Schale „Euklid-Abstand ≥ R“ gilt R\_eff ≈ (1/2π) ln(R/a) mit der Gitter-Streulänge a = e^{−γ} 2^{−3/2}:

| R               | 2      | 8      | 32     | 128    |
|-----------------|--------|--------|--------|--------|
| R\_eff           | 0,3750 | 0,5927 | 0,8105 | 1,0300 |
| (1/2π) ln(R/a)  | 0,3677 | 0,5883 | 0,8089 | 1,0296 |

Das Gewicht des weichen Potentials ist also 1/R\_eff ≈ 2π/ln(R/a), genau die Lieb–Yngvason-Konstante. Für zwei bewegliche Teilchen (Relativkoordinate, doppelter Laplace-Operator) verdoppelt es sich auf 4π, wie die Kastenrechnung in §28 zeigt.

**Weg zur scharfen Untergrenze E/N ≥ 4πρ/ln(1/ρa²)(1 − o(1)) (nach Lieb–Yngvason 2D, J. Stat. Phys. 103, 2001) [B].**

1. *Viele Teilchen:* Für Teilchen i und festgehaltene übrige ist f(x) = Ψ(…, x\_i = x, …) null an allen anderen Teilchen. Das Lemma wird in der Nächster-Nachbar-Zelle des jeweils nächsten Partners angewandt, mit Strom vom Partner zur Grenze der Zelle bzw. zum Radius R. Ein Bruchteil 1 − ε der kinetischen Energie wird so zu einem weichen Paarpotential Σ\_i (2π/ln(R/a)) U(Abstand zum nächsten Nachbarn) [B; der Strom in beliebig geformten Zellen ist auf dem Gitter kein Problem].
2. *Kästen und Temple:* Neumann-Kästen der Seite ℓ mit dem Restanteil ε der kinetischen Energie (Lücke 2 − 2 cos(π/ℓ) ≈ π²/ℓ², explizit). In jedem Kasten liefert die Temple-Ungleichung mit dem weichen Potential als Störung E ≥ n(n−1)/ℓ² · (2π/ln(R/a)) · (1 − Fehler). Paarzahl n(n−1) gibt 2 · 2π = 4π je Teilchen und Dichte.
3. *Verteilen der Teilchen* auf die Kästen über Konvexität bzw. Superadditivität, dann ℓ, R, ε optimieren. Im Kontinuum ergibt das den Fehler O(ln^{−1/5}).

**Was das bringt.**

- **Konstante K (§28):** c₁ → 4π statt π/16, also K etwa 60-fach kleiner (K ~ 15–30).
- **Lochargument (§28, Hebel 2):** Hier bleibt eine Schwierigkeit. Die Lochkosten sind lokal (~ Druck × Fläche ~ ρ m\_Loch/ln), die Fehler der Energieschranken aber ~ ρ m\_Bereich/ln · ln^{−1/5}. Die Differenz trägt nur bei lokaler Fassung beider Schranken und sehr kleinem ln^{−1/5}, also wieder sehr kleinem ρ. Der Gewinn für die Skalenentkopplung ist damit fraglich [L].

### 29.1 Lochenergien exakt (kleine Tori) [N]

[l1\_loch.py](l1_loch.py): ΔE = E₀(N; Torus ohne h×h-Block) − E₀(N; Torus), dazu ΔE(λ) für ein weiches Potential λ auf dem Block.

| Loch       | ΔE/ρ, 8×8, N = 2 / 3 / 4 | ΔE/ρ, 10×10, N = 2 / 3 | erwartete Teilchen im Block (8×8, N = 4) |
|------------|--------------------------|------------------------|------------------------------------------|
| 1 Platz    | 2,68 / 2,80 / 2,90       | 2,46 / 2,55            | 0,06                                     |
| 2×2        | 5,46 / 5,84 / 6,20       | 4,66 / 4,94            | 0,25                                     |
| 3×3        | 9,43 / 10,2 / 10,9       | 7,43 / 7,98            | 0,56                                     |
| 4×4        | 15,9 / 17,2 / 18,5       | 11,4 / 12,3            | 1,0                                      |
| 5×5        | –                        | 17,4 / 18,8            | –                                        |

- **Kleine Löcher:** ΔE ≈ ρ · Kapazität(Loch). Ein einzelner Platz kostet ρ · 2,5–2,9, verträglich mit der Punktkapazität 2π/ln(R/a) und einer schwachen Abhängigkeit von L (2,68 → 2,46 von L = 8 auf 10). Das ist das Bild „das Kondensat muss auf dem Loch verschwinden“.
- **Große Löcher** sind auf diesen Tori von der Kompression dominiert (ein 4×4-Loch nimmt 25 % des 8×8-Torus weg). ΔE/ρ wächst dort wie h², etwa 0,9 je erwartetem Teilchen im Loch, viel mehr als das chemische Potential (μ + 4 ≈ 0,26). Für die Asymptotik ist das unbrauchbar.
- **Weich:** ΔE(λ) ist konkav. Bei kleinem λ gilt ΔE ≈ λ⟨n\_Block⟩ (z. B. 0,095 gegen 0,100), dann sättigt es zum harten Wert.

**Folgerung.** Für das Feynman–Kac-Lochargument auf der Skala der Staffellaufzellen braucht man ΔE im thermodynamischen Limes. Kleine Tori geben es nicht her. Messbar wäre es im Wurm: Die Wahrscheinlichkeit, dass ein Bereich eine Zeit τ lang leer bleibt, fällt wie e^{−τ ΔE}. Das ließe sich in den Weltlinien-Konfigurationen direkt zählen; der Wurm braucht dafür eine kleine Erweiterung.

## 30. Scharfe Energie-Untergrenze auf dem Gitter (nach Lieb–Yngvason 2D) (2026-11-10) [B, Kernlemma S]

**Satz (Ziel).** Harte Bosonen auf (ℤ/Lℤ)², N = ρL², ε\_N = E\_N + 4N (Grundenergie von Σ\_i L\_i mit Dirichlet auf der Stoßmenge), Y = 1/ln(1/(ρa²)), a = e^{−γ}2^{−3/2}. Dann gilt für kleines ρ, gleichmäßig in L:

```text
ε_N / N  ≥  4πρ Y · (1 − C Y^{1/5})
```

Zusammen mit L1d (obere Schranke 8πρY für das chemische Potential, also 4πρY für ε\_N/N) ist das die Gitterfassung von Lieb–Yngvason 2D (J. Stat. Phys. 103, 2001). Der Exponent 1/5 stammt von dort; auf dem Gitter ist er nicht verbessert.

**Schritt A: Dyson für viele Teilchen [B, Kernlemma S].** Halte alle Teilchen außer i fest, f(x) = Ψ(…, x\_i = x, …). f verschwindet an allen x\_j, j ≠ i.

- Zerlege das Gitter in Nächster-Nachbar-Zellen V\_j (Punkte, deren nächstes Teilchen unter den übrigen j ist; feste Regel bei Gleichstand).
- In jeder Zelle wende das diskrete Dyson-Lemma (§29) an, mit Quelle x\_j und Ziel S\_j = (Punkte von V\_j im Abstand ≥ R) ∪ (Rand von V\_j). Die Kantenmengen der Zellen sind disjunkt, also gilt Σ\_alle Kanten (∇f)² ≥ Σ\_j Σ\_{y∈S\_j} U\_j(y) f(y)².
- Gewicht von U\_j: 1/R\_eff(x\_j ↔ S\_j) ≥ 1/R\_eff(x\_j ↔ Kreis R) ≈ 2π/ln(R/a), weil mehr geerdete Ziele den Widerstand nur senken.
- Mit einem Bruchteil ε der kinetischen Energie in Reserve folgt:

```text
Σ_i L_i  ≥  ε Σ_i L_i  +  (1 − ε) W,      W(X) = Σ_i Σ_{j≠i} U_j(x_i; übrige)   („weiches Nächster-Nachbar-Potential“)
```

*Gitter-Vorteil:* Im Kontinuum braucht das Dyson-Lemma sternförmige Bereiche, und Lieb–Yngvason müssen die Voronoi-Zellen eigens behandeln. Hier genügt ein Strom in beliebig geformten Zellen.

**Schritt B: Kästen und Temple [B].**

- Neumann-Kästen Q der Seite ℓ: Kanten zwischen Kästen weglassen, alle weggelassenen Terme sind ≥ 0. Schritt A wird *innerhalb* jedes Kastens ausgeführt.
- Danach darf der harte Kern im Kasten wegfallen; das senkt das Infimum nur. Es bleibt ε T\_Q + (1 − ε) W\_Q auf dem vollen Raum, mit T\_Q = Σ\_i L\_i^{Q, Neumann}. Der Grundzustand von T\_Q ist die Konstante φ₀; die Lücke ist ε(2 − 2cos(π/ℓ)) ≈ επ²/ℓ², explizit.
- Temple-Ungleichung mit φ₀: E₀ ≥ ⟨W′⟩ − (⟨W′²⟩ − ⟨W′⟩²)/(επ²/ℓ² − ⟨W′⟩), mit W′ = (1−ε) W\_Q.
- Im gleichverteilten Zustand gilt ⟨W\_Q⟩ = n(n−1)/ℓ² · 2π/ln(R/a) · (1 − O(nR²/ℓ²)): Jedes Teilchen hat mit Dichte (n−1)/ℓ² einen Nachbarn, und das Gewicht je Nachbar ist 2π/ln(R/a). Zähle i und j: Paarzahl n(n−1), also 4π je Teilchen und Dichte.
- *Bedingungen:* ⟨W′⟩ ≪ επ²/ℓ², also n² ≪ ε ln(R/a). Temple-Korrektur ⟨W²⟩/(ε/ℓ²) ≪ ⟨W⟩, mit max U ~ 1/(R ln) bei auf 2πR Punkte verteiltem μ, also n ℓ²/(R ε ln) ≪ 1. Und a ≪ R ≪ ℓ.

**Schritt C: Teilchen auf die Kästen verteilen [B].**

- Für n ≤ n\_max gilt e(n, ℓ) ≥ (1 − δ) n(n−1)/ℓ² · 4π/ln(1/(ρa²)) mit ln(R/a) ≈ ½ ln(1/(ρa²)) bei R = ρ^{−1/2} Y^{c}.
- Für größere n: Superadditivität (Gruppen aufteilen), ε\_j/j nichtfallend (§16.6).
- Konvexität in n: Gleichverteilung ist am ungünstigsten. Daraus folgt ε\_N/N ≥ 4πρY(1 − 1/(ρℓ²) − δ − ε).
- Optimieren mit ρℓ² ~ Y^{−1/5}, ε ~ Y^{1/5} (wie bei Lieb–Yngvason) gibt den Fehler C Y^{1/5}.

**Was zu tun bleibt, damit es [S] wird.**

1. Schritt A sauber: Gleichstände, Zellen am Kastenrand, Zellen mit Nachbarn näher als 2R. Dort wird das Gewicht nur größer, aber der Ort von U rückt näher; das geht in ⟨W⟩ als O(nR²/ℓ²) ein.
2. ⟨W\_Q⟩ und ⟨W\_Q²⟩ im gleichverteilten Zustand explizit berechnen: Kombinatorik plus Treffverteilung μ auf der Schale, numerisch prüfbar.
3. Die Optimierung mit allen Konstanten durchrechnen.

**Folgen.**

- c₁ = 4π(1 − CY^{1/5}) statt π/16. K aus den unteren Schwänzen (§28) sinkt etwa 60-fach, für sehr kleines ρ sogar bis auf den Faktor (1 − CY^{1/5})^{−1}.
- Mit der oberen Schranke aus L1d ist der Satz asymptotisch scharf. Damit ist die Grundzustandsenergie des 2D-Gitter-Bosegases in führender Ordnung streng bestimmt: E/N + 4 = 4πρ/ln(1/(ρa²))(1 + o(1)), mit der Gitter-Streulänge a = e^{−γ}2^{−3/2}. Unsere Literatursuche (§16) fand dafür keine Gitterfassung.

### 30.1 Numerische Prüfung der Kette Dyson → weiches Potential → Temple (n = 2) [N]

[l1\_dyson\_kette.py](l1_dyson_kette.py): b×b-Neumann-Kasten mit zwei Teilchen. Dyson-Potential U\_x mit Ziel „Abstand ≥ R“, W(x₁, x₂) = U\_{x₂}(x₁) + U\_{x₁}(x₂).

| b  | e\_b(2) exakt | λ\_min(εT + (1−ε)W), bestes R, ε | Anteil | ⟨W′⟩ (gleichverteilt) | ε · Lücke (ε = 0,2 / 0,5) |
|----|--------------|----------------------------------|--------|-----------------------|---------------------------|
| 6  | 0,0978       | 0,0443 (R = 2, ε = 0,5)          | 45 %   | 0,053                 | 0,054 / 0,134             |
| 8  | 0,0509       | 0,0249 (R = 3, ε = 0,2)          | 49 %   | 0,040                 | 0,030 / 0,076             |
| 10 | 0,0308       | 0,0155 (R = 4, ε = 0,2)          | 50 %   | 0,024                 | 0,020 / 0,049             |
| 12 | 0,0204       | 0,0101 (R = 2, ε = 0,5)          | 49 %   | 0,016                 | 0,014 / 0,034             |

- **Die Dyson-Ungleichung gilt in allen 24 Fällen.** Das weiche Ersatzproblem behält 36–50 % der wahren Energie. Der Verlust kommt vom Faktor (1 − ε) und daher, dass die Wellenfunktion der Schale des weichen Potentials ausweicht.
- **Temple ist hier nicht anwendbar:** ⟨W′⟩ ist von derselben Größe wie die Lücke ε · (2 − 2cos π/b). Es braucht n² ≪ ε ln(R/a), bei ln(R/a) ≈ 3 unmöglich. Die Temple-Werte sind negativ oder nicht definiert.

**Folgerung.**

- Der Lieb–Yngvason-Weg (§30) ist eine **rein asymptotische** Aussage (Y → 0, Fehler Y^{1/5}). Für die Konstante c₁ bei realistisch kleinem, aber nicht astronomisch kleinem ρ hilft er nicht.
- **Praktisch besser:** rechnergestützte strenge Untergrenzen. Über die Neumann-Zerlegung gilt streng ε\_N ≥ Σ\_Q e\_b(n\_Q), und die Kastenenergien e\_b(n) für n ≤ 3, b ≤ 24 sind exakt berechenbar; streng würde das mit Intervallarithmetik bzw. Temple für die Matrix selbst. Mit linearer Paarung gibt das c₁ ≈ π, mit Dreiteilchen-Kästen etwas mehr.
- **Für K (§28) heißt das:** realistisch c₁ ≈ π, also K etwa 16-fach kleiner (K ~ 60), nicht 60-fach. Asymptotisch für Y → 0 wird es 4π.
