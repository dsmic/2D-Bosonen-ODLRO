# Weltlinien-Ensemble als Beweisobjekt

Begonnen 2026-11-09. Teil von [README.md](README.md). Kennzeichnung: [S] streng, [Lit] Literatur, [B] Beweisskizze, [N] numerisch, [H] Hypothese, [L] Lücke.

Zweck: ODLRO harter Bosonen als Aussage über einen Graphen und über Pfade in diesem Graphen formulieren, also in der Sprache der Kombinatorik und Wahrscheinlichkeitstheorie. Der Wurm tastet genau dieses Objekt ab; jedes Hilfslemma lässt sich damit numerisch testen, bevor man es zu beweisen versucht.

Literaturangaben in §6 stammen aus dem Gedächtnis und sind vor Verwendung nachzuprüfen.

## 1. Das Modell als Graph

Λ = ℤ\_L² (Torus), M = L², N Teilchen, ρ = N/M, Hüpfamplitude t = 1.

```text
Token-Graph F_N(Λ):  Ecken  η ⊂ Λ mit |η| = N
                     Kanten η ~ η'  ⇔  η' = η − {x} + {y},  x ∈ η, y ∉ η, x ~ y Nachbarn in Λ
H_A = −A(F_N)        (harte Bosonen mit Nächstnachbar-Hüpfen, kanonisch)
```

- [S] Alle Nichtdiagonalelemente von H\_A sind ≤ 0 (keine Vorzeichen, Bosonen). Der Grundzustand ist der Perron-Vektor ψ > 0 von A(F\_N) mit Eigenwert λ\_N; E₀(N) = −λ\_N.
- [Lit] Der Token-Graph eines zusammenhängenden Graphen ist zusammenhängend (Fabila-Monroy u. a. 2012), also ist ψ eindeutig.
- [S] Für gerades L ist F\_N bipartit (jeder Sprung ändert die Parität von Σ(x₁ + x₂)). Daher hat A auch den Eigenwert −λ\_N; mit kontinuierlicher Zeit (e^{βA}) stört das nicht.
- [S] Teilchen-Loch: η ↦ Λ ∖ η ist ein Isomorphismus F\_N ≅ F\_{M−N}, und ⟨b\_x†b\_y⟩ für Teilchen ist ⟨h\_y†h\_x⟩ für Löcher (x ≠ y). ODLRO bei ρ ⇔ ODLRO bei 1 − ρ.

## 2. Weltlinien und Wurm

**Weltlinien [S].** Dyson-Entwicklung:

```text
Z_β = Tr e^{βA} = Σ_n β^n/n! · W_n,    W_n = Anzahl geschlossener Wege der Länge n in F_N
```

Ein geschlossener Weg in F\_N ist ein Bild in Raum × imaginärer Zeit [0, β): N Linien, die zu zufälligen Zeiten (Rate 1 je erlaubter Kante) auf leere Nachbarplätze springen, sich nie berühren (harter Kern) und bei β wieder die Startmenge besetzen. Weil nur die Menge zurückkehren muss, verbinden sich die Linien zu Zyklen um die Zeitrichtung (Feynman).

**Wurm [S].** Mit S für (N−1)-Mengen:

```text
⟨b_x† b_y⟩_β = Σ_{S ∌ x,y} (e^{βA})_{S+y, S+x} / Z_β   →(β → ∞)→   ρ₁(x, y) = Σ_{S ∌ x,y} ψ(S+x) ψ(S+y)
```

Zähler: Wege von S+x nach S+y, also N−1 geschlossene Linien und eine offene Linie von (x, 0) nach (y, β). Das ist der Wurm; sein Kopf-Schwanz-Histogramm misst genau dieses Verhältnis. Der Grenzwert folgt aus Perron–Frobenius (Lücke > 0 bei endlichem L).

- [N] Geprüft auf 4×4, N = 4, β = 12: Weltlinienformel und Perron-Formel stimmen auf 14 Stellen überein ([pruef\_identitaeten.py](pruef_identitaeten.py)).

**Zeitgeordneter Wurm [S].** Liegt das vernichtende Ende früher, fehlt der Weltlinie ein Stück (Lücke, Herausnehmen). Liegt es später, ist ein Stück zu viel da (Zusatzstück, Hinzufügen). Für die Lücke mit Impuls k:

```text
G_k(τ) = ⟨ψ| b_k† e^{−τ(H − E₀(N−1))} b_k |ψ⟩ = Σ_m |⟨m|b_k|ψ⟩|² e^{−τ(E_m − E₀(N−1))},    τ ≥ 0
n_k = G_k(0),    χ⁻(k) = ∫₀^∞ G_k(τ) dτ = n_k / ε_h(k)
```

G\_k ist vollständig monoton (Mischung fallender Exponentialfunktionen). Die einseitigen Größen aus [README.md](README.md) sind also Zeitprofile der Lücke: n\_k ist ihre Häufigkeit, ε\_h ihre mittlere Heilungsrate.

## 3. Das Ziel in drei gleichwertigen Formen

**Ziel.** Für 0 < ρ < 1 gibt es c(ρ) > 0 mit liminf N₀/N ≥ c(ρ) für L → ∞, N/L² → ρ, wobei N₀ = ‖b₀ψ‖², b₀ = M^{−1/2} Σ\_x b\_x. Bewiesen nur bei ρ = ½ (Kennedy–Lieb–Shastry 1988) [Lit].

**(A) Fasern [S].** Jede (N−1)-Menge S bestimmt eine Faser: die bedingte Ein-Teilchen-Wellenfunktion φ\_S(x) = ψ(S + x) auf der Leerstellenmenge V\_S = Λ ∖ S (|V\_S| = M − N + 1). Mit Gewicht w\_S = Σ\_x φ\_S(x)² und Teilnahmezahl F\_S = (Σ\_x φ\_S(x))² / (|V\_S| w\_S) gilt exakt

```text
N₀/N = (1 − ρ + 1/M) · ⟨F⟩_w,     ⟨F⟩_w = Σ_S w_S F_S / Σ_S w_S
```

ODLRO heißt: Die bedingte Wellenfunktion eines Teilchens ist im w-Mittel über einen festen Bruchteil der Leerstellen ausgebreitet. Für Stufe A ist das das Kriterium aus [z2/stufe\_a.md](z2/stufe_a.md) §32; bei Bosonen gilt es als Gleichung, ohne den Faktor 1 − 23ρ\_b.

- [N] 4×4, N = 4: beide Seiten 0,78233 (14 Stellen).

**(B) Pfade [S].** N₀/N = lim\_{β→∞} (1/(NM)) Σ\_{x,y} Σ\_S (e^{βA})\_{S+y,S+x} / Z\_β: Der Anteil offener Wege, deren Enden beliebig weit getrennt sind, ist nicht klein.

**(C) Markiertes Teilchen und Kollisionsmenge [S].** Der markierte Graph P hat die Ecken (S, x) mit x ∉ S. Kanten: x springt (S fest) oder ein Teilchen aus S springt auf einen leeren Platz ≠ x (x fest). P ist der Produktgraph F\_{N−1} □ Λ ohne die Kollisionsmenge C = {(S, x) : x ∈ S}. Ψ(S, x) = ψ(S + x) ist der Perron-Vektor von P, und

```text
N₀ = (1/M) Σ_S ( Σ_x Ψ(S, x) )²     (Anteil von Ψ, der im markierten Teilchen konstant ist)
```

Ohne Kollisionsmenge wäre der Perron-Vektor ψ\_{N−1} ⊗ konstant und N₀/N = 1. **ODLRO heißt: Das Herausschneiden der Kollisionsmenge verbiegt den Perron-Vektor des Produktgraphen nur zu einem festen Bruchteil.** Das ist eine Frage der spektralen Graphentheorie.

## 4. Was die Graphsprache sofort zeigt

**4.1 Naive Schranke und das Infrarotproblem [S].** Sei Φ = ψ\_{N−1} ⊗ M^{−1/2} der Perron-Vektor von G = F\_{N−1} □ Λ mit Eigenwert λ\_{N−1} + 4 und Spektrallücke γ. Ψ (auf C durch 0 fortgesetzt) erfüllt ⟨Ψ, A\_G Ψ⟩ = λ\_N ‖Ψ‖², also γ ‖Ψ\_⊥‖² ≤ (λ\_{N−1} + 4 − λ\_N) ‖Ψ‖². Mit N₀ ≥ ⟨Φ, Ψ⟩² (Cauchy–Schwarz) folgt

```text
N₀/N ≥ 1 − (4 + λ_{N−1} − λ_N) / γ
```

Der Zähler ist der Wechselwirkungsanteil des chemischen Potentials, von der Ordnung ρ, und bleibt im Volumen endlich. Die Lücke γ ≤ 2 − 2cos(2π/L) ≈ (2π/L)² verschwindet. Die Schranke ist also im Volumen wertlos. Das ist das Infrarotproblem in Graphsprache: Das Herausschneiden kostet endliche Energie, und langwellige Verbiegungen sind fast umsonst. Auf 4×4, N = 4: Kosten 1,41, γ ≤ 2 [N].

**4.2 Modenaufgelöste Identität [S].** Zerlegt man das markierte Teilchen nach Impulsen, ist ‖P\_k Ψ‖² = n\_k, und

```text
Σ_k E(k) n_k = 4N − λ_N      (kinetische Energie über der Bandunterkante; E(k) = 4 − 2cos kx − 2cos ky)
```

[N] 4×4, N = 4: 2,74831 auf beiden Seiten. Energie allein begrenzt Σ\_{k≠0} n\_k in keiner Dimension, denn alles Gewicht könnte beim kleinsten k sitzen. Man braucht Schranken für jedes n\_k einzeln, Größenordnung n\_k ≲ 1/|k| bei kleinem k. Das sind die einseitigen Ungleichungen aus [README.md](README.md), mit k-abhängiger Form.

**4.3 RK-Punkt = Exklusionsprozess [S].** H\_RK = Deg − A ist der Laplace-Operator von F\_N, also minus der Generator des symmetrischen Exklusionsprozesses (Teilchen springen mit Rate 1 auf leere Nachbarplätze). Der Grundzustand ist konstant, N₀/N = (M − N + 1)/M ([N] 4×4: 0,8125). Die Spektrallücke ist gleich der Ein-Teilchen-Lücke (Caputo–Liggett–Richthammer 2010, Aldous-Vermutung) [Lit]. Wegen Deg = 4N − 2N\_nn (N\_nn = besetzte Nachbarpaare) gilt die Feynman–Kac-Formel

```text
(e^{βA})_{η',η} = e^{4Nβ} · E_η[ exp(−2 ∫₀^β N_nn(η_s) ds) ; η_β = η' ]      (η_s Exklusionsprozess)
```

**H\_A ist also der Exklusionsprozess, umgewichtet mit dem Faktor e^{−2∫N\_nn}:** Zeit mit Nachbarkontakten wird bestraft. Außerdem ist ψ² reversibel für den Sprungprozess mit Raten ψ(η′)/ψ(η) (Doob-Transformation) [S]; ψ² ist die stationäre Verteilung des entsprechend konditionierten Exklusionsprozesses. Solche konditionierten Prozesse sind in der Statistik seltener Trajektorien untersucht, etwa Hyperuniformität bei Bias zu hoher Aktivität (Jack–Thompson–Sollich 2015) [Lit]. Hyperuniform heißt S(k) → 0 wie |k|, wie es Feynman für Suprafluide erwartet.

**4.4 1D: kein Überholen [Lit].** In 1D können sich nicht kollidierende Linien nicht überholen. Übergangsgewichte sind Determinanten (Karlin–McGregor 1959, Lindström–Gessel–Viennot), ψ = |Slater-Determinante| (Girardeau 1960). Es gibt keinen Platztausch außer kollektivem Weiterrücken, also keine Austauschzyklen und kein ODLRO. In 2D können Linien umeinander herumlaufen; das ist Feynmans Austausch.

**4.5 Eingefrorener Hintergrund reicht nie [S/H].** Aus A ψ = λψ folgt für die Fasern

```text
λ φ_S(x) = Σ_{x'~x, x' ∈ V_S} φ_S(x')  +  Σ_{s ∈ S} Σ_{s'~s, s' ∈ V_S, s' ≠ x} φ_{S−s+s'}(x)
           (markiertes Teilchen hüpft)      (Umgebung bewegt sich: Kopplung der Fasern)
```

Ohne den zweiten Term wäre φ\_S der Perron-Vektor des Hüpfens auf V\_S. Bei Leerstellendichte 1 − ρ < 0,593 (Platzperkolation, also ρ > 0,407) zerfällt V\_S in endliche Inseln und F\_S → 0 [H]; heuristisch, weil S nach ψ² verteilt ist und nicht unabhängig. Darunter lokalisiert der Perron-Vektor im größten hindernisfreien Gebiet (Lifschitz) [H]. **Die Ausbreitung kommt also ganz aus der Kopplung der Fasern: Ein Teilchen in eingefrorener Umgebung bleibt gefangen, erst das Ausweichen der anderen macht es beweglich.** Das ist dieselbe Grenze wie bei der Thomson-Schranke mit festem Hintergrund für Stufe A (scheitert bei 7/8: freie Dichte 0,395 < 0,593).

**4.6 Zyklen: Vorsicht bei T = 0 [S].** Mit Etiketten auf den Teilchen induziert jeder geschlossene Weg eine Permutation π. Ist der Graph der etikettierten Konfigurationen zusammenhängend, so ist sein Perron-Vektor unter Umetikettierung invariant. Dann ist das Gewicht jeder Permutation für β → ∞ proportional zu Σ\_η Φ(πη)Φ(η) = const, π wird also **gleichverteilt**. (Mit nur einem Loch sind auf bipartiten Graphen nur gerade Permutationen erreichbar, Wilson 1974 [Lit].) Bei endlichem L und T = 0 trägt die Zyklenstatistik also keine Information. Feynman-Zyklen sind eine Aussage bei T > 0 mit L → ∞ zuerst, und in 2D gibt es bei T > 0 kein ODLRO. Der Test „n₀ = Anteil in makroskopischen Zyklen“ aus dem Chat vom 2026-11-09 ist deshalb für T = 0 falsch gestellt und wird nicht verfolgt. Das richtige Objekt bei T = 0 ist der offene Weg (§2, §3 B).

## 5. Wörterbuch

| Physik                               | Graph / Pfade                                                                 |
|--------------------------------------|-------------------------------------------------------------------------------|
| H\_A = −Σ(b†b + h.c.), kanonisch     | −A(F\_N), Token-Graph des Torus                                                |
| Grundzustand                         | Perron-Vektor ψ                                                               |
| ρ₁(x, y)                             | offene Wege S+x → S+y / geschlossene Wege (Wurm)                              |
| n₀ (Kondensat)                       | mittlere Teilnahmezahl der Fasern; Verbiegung durch die Kollisionsmenge       |
| n\_k, χ⁻(k)                          | Häufigkeit und Lebensdauer einer Lücke mit Impuls k in einer Weltlinie        |
| chemisches Potential                 | 4 + λ\_{N−1} − λ\_N = Kosten des Herausschneidens der Kollisionsmenge          |
| RK-Punkt                             | Laplace von F\_N, symmetrischer Exklusionsprozess, ψ konstant                 |
| H\_A abseits RK                      | Exklusionsprozess mit Gewicht e^{−2∫N\_nn}; ψ² = konditionierter Prozess       |
| Teilchen ↔ Loch                      | F\_N ≅ F\_{M−N}                                                               |
| 1D (kein ODLRO)                      | Linien können sich nicht überholen; Determinanten                             |
| 2D (ODLRO)                           | Linien laufen umeinander; Austausch                                           |
| Infrarotproblem                      | Lücke des Produktgraphen ~ 1/L², Kosten O(ρ)                                  |
| fester Hintergrund                   | Ein-Teilchen-Hüpfen auf V\_S, perkoliert bei hoher Dichte nicht               |

## 6. Literaturkarte [Lit, aus dem Gedächtnis, prüfen]

| Objekt                                   | bewiesen                                    | Methode                        | Quelle                                                   |
|------------------------------------------|---------------------------------------------|--------------------------------|----------------------------------------------------------|
| XY-Modell Spin ½, ρ = ½, T = 0, d ≥ 2    | ODLRO                                       | Reflexionspositivität          | Kennedy–Lieb–Shastry 1988                                |
| ideales Bosegas                          | Kondensat = Anteil in unendlichen Zyklen    | explizit                       | Süto 1993, 2002; Ueltschi 2006 (PRL 97, 170601)          |
| Heisenberg-Ferromagnet ↔ Vertauschung    | Darstellung, Druckschranken                 | Pfadintegral                   | Tóth 1993                                                |
| Antiferromagnet, Schleifen               | Darstellung                                 | Pfadintegral                   | Aizenman–Nachtergaele 1994                               |
| Schleifenfamilie inkl. XY                | Darstellung; lange Schleifen nur mit RP     | Pfadintegral + Dyson–Lieb–Simon | Ueltschi 2013; Goldschmidt–Ueltschi–Windridge 2011       |
| Vertauschungsprozess, vollständiger Graph | makroskopische Zyklen, Poisson–Dirichlet   | Kopplung, Kombinatorik         | Schramm 2005                                             |
| Vertauschungsprozess, Bäume              | unendliche Zyklen                           | Kombinatorik                   | Angel 2003; Hammond 2013, 2015                           |
| Vertauschungsprozess auf ℤ^d             | **offen** (Tóths Vermutung)                 | –                              | –                                                        |
| Exklusionsprozess, Spektrallücke         | gleich Ein-Teilchen-Lücke                   | Oktopus-Ungleichung            | Caputo–Liggett–Richthammer 2010                          |
| Token-Graphen                            | Zusammenhang, Spektren                      | Graphentheorie                 | Fabila-Monroy u. a. 2012; Audenaert u. a. 2007; Dalfó u. a. 2021 |
| Ising, Zufallsströme                     | Schaltlemma, scharfe Übergänge              | Umverdrahtung                  | Aizenman 1982; Aizenman–Duminil-Copin–Sidoravicius 2015; Björnberg–Grimmett 2009 (Quanten-Ising) |
| verdünntes Bosegas, Kontinuum            | BEC nur in Skalierungslimites (Stand bis 2025) | Analysis                    | Lieb–Seiringer 2002 und Folgearbeiten                    |
| **harte Kugeln 3D, T = 0, feste kleine Dichte** | **BEC in jedem Grundzustand, thermodynamischer Limes** (Preprint, KI) | Φ = \|Ψ\|, Vergleich Φ(x,Y) ↔ Φ(y,Y) längs zufälliger Routen, Begegnungsmomente | OpenAI 2026-09-24, Familie 267 |
| **Heisenberg-Ferromagnet, d ≥ 3, T > 0** | **spontane Magnetisierung ≥ S/4** (Preprint, KI) | Zyklen mit Pins, stabile Polynome, Rückkehr eines Wegs, Nash, Flüsse; **ohne RP** | OpenAI 2026-09-24, Familie 271 |
| No-go-Ungleichungen                      | n\_k nach unten, kein BEC in 1D / T > 0     | Bogoliubov-Ungleichung         | Hohenberg 1967; Pitaevskii–Stringari 1991                |

Bilanz (Stand bis 2025): Rein kombinatorische Beweise langer Zyklen gab es auf Bäumen und dem vollständigen Graphen, wo Wege selten zu sich zurückfinden; auf ℤ^d benutzte jedes Ergebnis Reflexionspositivität.

**Nachtrag 2026-11-09:** Zwei Preprints aus der OpenAI-Sammlung ([github.com/openai/math](https://github.com/openai/math), von einem internen Modell erzeugt, laut Repository in Lean formalisiert, unabhängige Begutachtung nicht gefunden) beweisen Ordnung auf Gittern bzw. im Kontinuum **ohne Reflexionspositivität**, beide in der Pfaddarstellung:

- Familie 271, „Spontaneous magnetization in the quantum Heisenberg ferromagnet“: d ≥ 3, T > 0, jeder Spin. In Bosonensprache (§1.4 dort) ist das Modell harte Bosonen mit Nachbaranziehung bei ½, also unser **RK-Modell** (§4.3). Bei T = 0 ist dieser Fall für uns trivial; neu ist die Methode: Randzyklen werden „festgesteckt“ (Pins), gezeigt wird, dass ein innerer Zyklus fast nie am Rand vorbeikommt. Werkzeuge: Negativabhängigkeit des Exklusionsprozesses (stabile Polynome, Borcea–Brändén–Liggett), eine Determinanten-Identität für die Rückkehr eines Wegs, Nash-Ungleichung, Flüsse um blockierte Gebiete (vgl. unsere Thomson-Flüsse).
- Familie 267, „Ground-state condensation in the dilute hard-sphere gas“: 3D, T = 0, feste kleine Dichte, thermodynamischer Limes. Der Beweis arbeitet mit Φ = |Ψ| und B(Φ) = L^{−3} ∫ Φ(x,Y) Φ(y,Y) dx dy dY, also **genau unserem Faserkriterium (§3 A)**. Φ(x,Y) und Φ(y,Y) werden längs zufälliger Zellrouten verglichen; der Doob-Prozess mit Randverteilung Φ² liefert die lokalen Ersetzungen; die Kosten bleiben auf Begegnungen zweier unabhängiger Routen beschränkt.
- **Wo d = 3 eingeht:** Die Routen (Benjamini–Pemantle–Peres, „unvorhersagbare Pfade“) schreiten in einer Richtung voran und schwanken in **zwei** Querrichtungen; nur dann haben die Begegnungen zweier Routen exponentielle Schranken. In 2D gibt es nur eine Querrichtung, und Routen treffen sich zu oft. Beim Ferromagneten geht d ≥ 3 über Transienz der Wärmeleitung ein.
- **Folgerung für uns [H]:** Bei T = 0 in 2D steht die imaginäre Zeit als dritte Richtung zur Verfügung (2 + 1). Ob Routen in Raum-Zeit statt im Raum die fehlende Querrichtung liefern können, ist die naheliegende Frage. Beide Methoden brauchen Verdünnung bzw. eine Sonderstruktur; mittlere Dichten bleiben auch dann offen.

**Nachtrag 2026-11-10.** Weitere OpenAI-Preprints derselben Familie (dichte-uniforme Kondensatschranke mit „reverse insertion“, BEC bei T > 0, Bogoliubov-Verarmung) und die Abstammung der Methode (Benjamini–Pemantle–Peres, Häggström–Mossel, Gruppensynchronisation nach Abbe et al., Garban–Spencer) stehen in [einpunkt\_zeitroute.md](einpunkt_zeitroute.md) §9.

## 7. Kandidaten-Lemmata und Tests

| Nr. | Aussage                                                                                                 | Art                       | Test                                                                                      |
|-----|---------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|
| K1  | Faser-Delokalisierung: ⟨F⟩\_w ≥ c(ρ) gleichmäßig in L; lokal: w-Anteil der Fasern mit F\_S ≥ δ ist ≥ ε | gleichwertig zum Ziel     | exakt für L ≤ 6 (Bosonen, neu), Jastrow-VMC für großes L wie `odlro_vmc.py`              |
| K2  | Lücken mit großem Impuls heilen schnell: ε\_h(k) ≥ b·E(k) für \|k\| ≥ k₁; bei kleinem k χ⁻E ≤ a = O(1) | zwei getrennte Schranken  | Wurm mit zeitgeordnetem, zeitaufgelöstem Histogramm (Erweiterung nötig)                   |
| K3  | Infrarotform: n\_k·\|k\| bleibt bei kleinem k gleichmäßig in L beschränkt, Konstante nahe Bogoliubov     | Struktur der Verbiegung   | Wurm Runde 1 (L = 16, 32; `hist_eq` gibt n\_k direkt), keine neuen Läufe                 |
| K4  | Umgewichtung schwach bei kleiner Dichte: N₀(H\_A)/N₀(RK) → 1 für ρ → 0                                  | Störung um RK [H]         | exakt und Wurm über ρ; Vorsicht: RK ist kritisch (κ = ∞, §32)                             |

## 8. Mögliche Beweisideen in dieser Sprache [H]

1. **Perron-Störung mit Modenauflösung.** §4.1 scheitert, weil eine einzige Lücke γ alle Moden behandelt. Gebraucht wird: Das Herausschneiden von C verbiegt Ψ in der Mode k höchstens um ~ 1/|k| (K3). Das ist Graphentheorie (Dirichlet-Problem auf G ∖ C, Kapazität von C), aber mit Fernwirkung.
2. **Umverdrahtung.** Die Züge des Wurms sind lokale Umverdrahtungen von Wegen. Beim Ising-Modell macht das Schaltlemma daraus Ungleichungen; für U(1)-Symmetrie und Bosonen ist mir kein Analogon bekannt [L].
3. **Werkzeuge der Teilchensysteme.** Exklusionsprozess mit Feynman–Kac-Gewicht (§4.3): Oktopus-Ungleichung (Caputo–Liggett–Richthammer), Doob-Transformation, große Abweichungen.
4. **Routen in Raum-Zeit (nach Familie 267).** Faserkriterium direkt angreifen: Φ(x,Y) gegen Φ(y,Y) längs zufälliger Routen vergleichen, mit dem Doob-Prozess (§4.3) als Lieferant lokaler Ersetzungen. Die dritte Routenrichtung müsste die imaginäre Zeit sein. Zuerst bei kleiner Dichte auf dem Gitter. Ausgearbeitet in [analyse\_familie267.md](analyse_familie267.md): Dimensionszählung (Begegnungen ~ Σ s^{−qα}, q Querrichtungen), Konsistenz mit 1D/2D/3D und T > 0, offene Punkte; t′ ersetzt die dritte Richtung nicht. Weitergeführt in [einpunkt\_zeitroute.md](einpunkt_zeitroute.md): Einpunkt-Kriterium N₀/N ≥ H̄² (Faser gegen (N−1)-Grundzustand) [S], numerisch fast scharf; Route in Zeitrichtung, Raum-Zeit ℤ³, BPP direkt anwendbar.
5. **Warnung „falsche Richtung“.** Die natürlichen Ungleichungen (Bogoliubov, Hohenberg, Pitaevskii–Stringari) begrenzen n\_k nach **unten** und beweisen Abwesenheit von Ordnung. Für Ordnung braucht man Schranken nach oben. Reflexionspositivität ist der einzige bekannte Mechanismus dafür, und genau sie fehlt bei ρ ≠ ½. Hier liegt die eigentliche Lücke [L].

## 9. Nächste Schritte

1. K3 sofort nach Ende der Wurm-Runde 1 (`ergebnisse/runde1.done`): n\_k bei kleinem k für L = 16 und 32 vergleichen.
2. K1 für Bosonen exakt (L = 4, 6) und mit Jastrow-VMC: Verteilung von F\_S, nicht nur das Mittel.
3. Wurm-Erweiterung für K2: Histogramm nach Zeitordnung und Zeitabstand der Enden trennen.
4. Die beiden OpenAI-Preprints (Familien 267, 271) im Detail lesen, mit der Frage, ob die dritte Raumrichtung durch die imaginäre Zeit ersetzt werden kann. Zuerst 267 (Grundzustand, T = 0, unser Kriterium).
5. Literatur prüfen, zuerst Ueltschi 2013 (genauer Satz über lange Schleifen), Caputo–Liggett–Richthammer (Oktopus-Ungleichung), Jack–Thompson–Sollich 2015.
