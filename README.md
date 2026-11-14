# ODLRO harter Bosonen im 2D-Grundzustand abseits halber Füllung

Begonnen 2026-11-09. Kennzeichnung wie in [z2/stufe_a.md](z2/stufe_a.md): [S] streng, [Lit] Literatur, [B] Beweisskizze, [N] numerisch, [H] Hypothese, [L] Lücke.

## Ziel

Ein strenger Beweis: Der Grundzustand harter Bosonen auf ℤ² mit Nächstnachbar-Hüpfen, H = −J Σ(b_x†b_y + h.c.), hat bei jeder Dichte 0 < ρ < 1 ODLRO. Bewiesen ist das nur bei ρ = ½ [Lit]; sonst ist es offen und gilt als großes Problem der mathematischen Physik. Die Numerik spricht eindeutig für die Aussage [N].

Harte Bosonen sind das Versuchsfeld für Stufe A: Der schwierige Kern (Kohärenz über große Abstände im wechselwirkenden Grundzustand) ist derselbe, alles andere ist einfacher. Siehe [z2/stufe_a.md](z2/stufe_a.md) §32 und [z2/odlro_chatgpt_pruefung.md](z2/odlro_chatgpt_pruefung.md).

## Ausgangslage

- [Lit] ρ = ½: Kennedy–Lieb–Shastry 1988 (XY-Modell, Grundzustandsordnung, d ≥ 2), Kubo–Kishi 1988; Aizenman–Lieb–Seiringer–Solovej–Yngvason 2004 (Gitter-Bosegas, halbe Füllung „dictated by our method of proof“). Methode: Reflexionspositivität → Infrarotschranke → Falk–Bruch + Summenregel.
- [B] Warum nur ρ = ½: Für die Reflexionspositivität muss das XY-Modell in die reelle (S¹, S³)-Ebene gedreht werden; μ koppelt dann an das imaginäre S², und die Spiegelung (mit komplexer Konjugation) kehrt sein Vorzeichen auf einer Hälfte um.
- [N] Unsere Befunde (2026-11-09, [z2/zweipaar_graph/README.md](z2/zweipaar_graph/README.md)):
  1. Die Infrarotschranke χ(k)·E(k) ≤ 1 gilt numerisch bei allen Dichten (4×4–8×8, max. 0,98 bei kleinster Dichte), auch ohne Reflexionspositivität.
  2. Die Kette Falk–Bruch + Summenregel + Infrarotschranke ist im unendlichen Volumen nur bei ρ = ½ knapp positiv (+0,0002 je Platz) und sonst negativ (−0,02 bis −0,04). Für ρ → 0 wird c(k) = E(k), die Schranke genau 0.
  3. Also fehlen abseits ρ = ½ zwei Dinge: eine Infrarotschranke ohne Reflexionspositivität und eine schärfere Ungleichungskette.

## Werkzeuge

- [gitter_bosonen.py](gitter_bosonen.py): Quadratgitter im Format von `z2/weltlinien/gitter.py`; der Wurm ([z2/weltlinien/wurm_nb4.py](z2/weltlinien/wurm_nb4.py)) wird unverändert importiert (leere Ausschlusslisten = harte Bosonen).
- [scan_bos.py](scan_bos.py): Wurm-Treiber, großkanonisch, μ auf Zieldichte eingeregelt (`--rho`) oder fest (`--mu`). Misst E, N, Windung, g(r) bei r = 0, (L/2, 0), (L/2, L/2), volle Histogramme gleichzeitig (`hist_eq`) und zeitintegriert (`hist_all`, ω = 0).
- [pruef_exakt.py](pruef_exakt.py): exakte großkanonische Werte bei endlicher Temperatur (volle Diagonalisierung, L = 4).
- Exakte T = 0-Rechnungen und Kettentests: [z2/zweipaar_graph/falk_bruch.py](z2/zweipaar_graph/falk_bruch.py), [z2/zweipaar_graph/ir_integral.py](z2/zweipaar_graph/ir_integral.py).

## Prüfung des Wurms (4×4, β = 4, μ = −2,3, zwei Seeds à 7 min) [N]

| Größe       | Wurm Seed 1        | Wurm Seed 2        | exakt    |
|-------------|--------------------|--------------------|----------|
| ρ           | 0,25182 ± 0,00011  | 0,25170 ± 0,00018  | 0,25185  |
| E_kin/M     | −0,82441 ± 0,00043 | −0,82394 ± 0,00068 | −0,82470 |
| g(L/2, 0)   | 0,18852 ± 0,00070  | 0,18788 ± 0,00053  | 0,18921  |
| g(L/2, L/2) | 0,17767 ± 0,00080  | 0,17826 ± 0,00091  | 0,17777  |
| g(0)        | 0,24562 ± 0,00103  | 0,24535 ± 0,00093  | 0,25185  |

- Alles stimmt bis auf g(0): Die gleichzeitige Korrelation am selben Platz wird wegen des endlichen Zeitfensters (w = 0,05) systematisch 2,5 % zu klein gemessen; bei r ≠ 0 ist der Effekt ≤ 0,5 %.
- **Regel:** g(r) durch die gemessene Dichte ρ normieren (g(0) = ⟨n⟩ = ρ exakt), nicht durch das gemessene g(0). Damit g(L/2,0)/ρ = 0,749 (exakt 0,751), g(L/2,L/2)/ρ = 0,706 (exakt 0,706).
- Rückwirkung auf Stufe A: n₀ war um 1–3 % zu hoch; mit ρ normiert n₀ ≈ 0,095–0,100 ([z2/weltlinien/auswertung_null.py](z2/weltlinien/auswertung_null.py) gibt beide Werte aus).

## Programm

**Phase 1, Numerik (Wurm), Dichten ρ = 1/16, 1/8, 1/4, 3/8, ½, L = 8–48, T ≪ Lückenskala (β ≳ L):**

1. Kondensat n₀(ρ) aus g(r)/ρ (Plateau und Profil n₀ + a(1/r + 1/(L−r)), wie bei Stufe A), Steifigkeit aus der Windung, Schallgeschwindigkeit aus a/n₀ = c/(4πρ\_s) als Konsistenzprobe.
2. **Infrarotschranke bei großem L:** χ(k) aus `hist_all` (Eichung der Normierung gegen exakt auf 4×4), Prüfung χ(k)·E(k) ≤ 1 bis L = 48, besonders bei kleinem ρ, wo sie knapp ist.
3. Doppelkommutator c(k) im unendlichen Volumen: ⟨b†b⟩\_nn aus der Energie, ⟨n n⟩\_nn als neue Messung.

**Phase 2, Abschätzungen suchen:**

- (a) Kennedy–Lieb–Shastry lesen: Welche zusätzlichen Abschätzungen machen die Kette bei ρ = ½ in 2D tragfähig? Tragen sie mit angenommener Infrarotschranke auch bei ρ ≠ ½ (mit den Daten aus Phase 1 prüfbar)?
- (b) Infrarotschranke ohne Reflexionspositivität: Sie ist numerisch bei allen Dichten erfüllt und für ρ → 0 scharf (freies Teilchen). Kandidaten: Weltlinien-/Schleifendarstellung mit Korrelationsungleichungen, Monotonie in μ, Vergleich mit dem freien Gas.
- (c) Andere Ketten als Falk–Bruch + Summenregel, etwa mit Steifigkeit und Kompressibilität (Phononenstruktur) statt der nackten Summenregel.

**Phase 3:** Was in Phase 2 mit Spielraum trägt, als Satz ausschreiben, mit genau benannten Annahmen.

## Phase 2, erste Befunde (2026-11-09)

**Wie Kennedy–Lieb–Shastry bei ρ = ½ schließen** [Lit, nach der Übersicht Björnberg–Ueltschi, arXiv:2204.12896, §3–4]: zwei sich ergänzende Ungleichungen, beide mit Infrarotschranke und der Nachbarkorrelation α:

- (A) Summenregel: ⅓S(S+1) > ½ I √α, I = (2π)⁻ᵈ ∫ √(ε(k+π)/ε(k)) dᵈk (2D: I = 1,393); trägt bei kleinem α.
- (B) Nachbarkorrelation: √α/(1 − J₂/J₁) > ½ Ĩ, Ĩ = Integral mit Faktor (Σcos k_i/d)₊ (2D: Ĩ = 0,6468); trägt bei großem α.
- Bei Spin ½ in 2D überlappen die Bereiche (XY-Modell und Anisotropien nahe XY); für den isotropen Heisenberg-Antiferromagneten nicht.

**Warum ρ = ½ für diese Methode besonders ist, unabhängig von der Reflexionspositivität** [S, Identität]: Für harte Bosonen gilt m_k = ⟨A_kA_k†⟩ = n_k + 1 − 2ρ (aus b_x b_x† = 1 − n_x und b_y†b_x = b_x b_y† für x ≠ y), also

```text
g_k = ½(n_k + m_k) = n_k + ½(1 − 2ρ)
```

Falk–Bruch schätzt die symmetrische Größe g_k ab. Abseits ρ = ½ trägt sie in jeder Mode den flachen Untergrund ½(1−2ρ); die Kette muss n_k ~ ρ auf einem Untergrund ~½ auflösen, mit typisch 1–3 % Cauchy-Schwarz-Spielraum je Mode. Bei ρ = ½ verschwindet der Untergrund. Das erklärt die negativen Werte der Kette im unendlichen Volumen bei ρ < ½ (siehe oben).

**Einseitige Kette** [N]: n_k ≤ √(c⁻(k) χ⁻(k)) mit c⁻ = ⟨A†(H−E₀+μ)A⟩, χ⁻ = ⟨A†(H−E₀+μ)⁻¹A⟩ (nur Entfernungsseite) ist auf 4×4 praktisch exakt (n₀ garantiert 100 / 100 / 100 / 99 % bei ρ = 1/8, 1/4, 3/8, 1/2). Für c⁻ und χ⁻ fehlen aber a-priori-Schranken: c⁻ ist nicht lokal, χ⁻ wird von der Infrarotschranke nur über χ⁻ ≤ χ erfasst, und das ist bei kleiner Dichte grob.

**Präzisierte Lücke [L]:** Abseits halber Füllung braucht man eine a-priori-Schranke, die nicht symmetrisch in A ↔ A† ist (eine „einseitige Infrarotschranke“), oder eine Summenregel ohne Untergrund. Die symmetrische Dyson–Lieb–Simon-Struktur zahlt den Untergrund ½(1−2ρ) mit; das ist neben der fehlenden Reflexionspositivität das zweite, ebenso grundsätzliche Hindernis.

## Zwei einseitige Ungleichungen als Beweisziel (2026-11-09)

Kanonisch, ohne μ (für k ≠ 0 steht A_kψ\_N senkrecht auf dem (N−1)-Grundzustand, Impuls 0):

```text
χ⁻(k) = ⟨ψ_N| A_k† (H_{N−1} − E₀(N−1))⁻¹ A_k |ψ_N⟩,    c⁻(k) = ⟨ψ_N| A_k† (H_{N−1} − E₀(N−1)) A_k |ψ_N⟩
(I)   χ⁻(k) ≤ ρ / E(k)          (einseitige Infrarotschranke; mit Teilchen-Loch-Symmetrie folgt χ ≤ 1/E)
(II)  c⁻(k) ≤ C ρ,  C < 1/J² = 2,42,   J = ∫d²k/(2π)² E^(−1/2) = 0,6428
⇒  n_k ≤ √(c⁻χ⁻) ≤ ρ √(C/E(k)),   n₀/N ≥ 1 − √C·J        [S, gegeben (I) und (II)]
```

In 1D divergiert J logarithmisch; die Kette kann dort nichts beweisen (richtig, Lenard). Zahlen [N] ([z2/zweipaar_graph/falk_bruch.py](z2/zweipaar_graph/falk_bruch.py), Logs in `z2/zweipaar_graph/ergebnisse/einseitig/`):

| Fall                | ρ                     | max χ⁻E/ρ          | max χ⁺E/(1−ρ)      | C = max c⁻/ρ       |
|---------------------|-----------------------|--------------------|--------------------|--------------------|
| 2D 4×4              | 1/8 … 1/2             | 0,19 … 0,42        | 0,94 … 0,42        | 0,48 … 2,62        |
| 2D 6×6              | 0,056 / 0,083 / 0,111 | 0,24 / 0,36 / 0,43 | 0,97 / 0,96 / 0,95 | 0,28 / 0,55 / 0,80 |
| 2D 8×8              | 0,031                 | 0,31               | 0,98               | 0,21               |
| 1D L = 16 / 24 / 32 | 0,125                 | 0,98 / 1,06 / 1,14 | 0,89 / 0,90 / 0,90 | 0,33 / 0,50 / 0,59 |
| 1D L = 16 / 24      | 0,25                  | 0,61 / 0,63        | 0,82 / 0,82        | 1,13 / 1,28        |

- 2D: beide Ungleichungen mit großem Abstand; die Kette garantiert auf 4×4 n₀/N ≥ 55 / 25 / 8 % bei ρ = 1/8, 1/4, 3/8 (bei ½ nicht; dort trägt die symmetrische Kette).
- 1D: (I) wird bei ρ = 1/8 verletzt und die Verletzung wächst mit L. Ursache: Harte Bosonen in 1D sind freie Fermionen; Herausnehmen erzeugt ein Loch im Fermi-See, und Lochanregungen mit beliebig kleiner Energie gibt es für alle |k| < 2πρ. Genau dort ist χ⁻E/ρ ≈ 1 (Profil), oberhalb fällt es steil ab. (II) bleibt in 1D moderat.
- Folgerung: (I) ist keine dimensionsunabhängige, rein lokale Ungleichung. Ein Beweis muss etwas typisch Zweidimensionales benutzen: das Fehlen eines weichen Kontinuums von Lochanregungen bei endlichem k. Physikalisch heißt das, dass Herausnehmen im Wesentlichen ein einzelnes Quasiteilchen erzeugt (Bogoliubov-Bild). Das liegt näher am Kern des Problems als erhofft. (II) wirkt dagegen generisch.

**Übertrag auf Stufe A bei 7/8 [N] (2026-11-09,** [z2/zweipaar_graph/einseitig_stufe_a.py](z2/zweipaar_graph/einseitig_stufe_a.py)**):** Paare auf dem Mittelgitter, freie Paardispersion E(k) = 4 − 4cos(k_x/2)cos(k_y/2), J_A = 0,6428. 8×8, exakt:

| P       | ρ\_b  | n₀/P  | (I) max χ⁻E/ρ\_b | (II) C | 1 − √C·J_A | Kette mit exakten c⁻, χ⁻ je k |
|---------|-------|-------|------------------|--------|------------|-------------------------------|
| 2       | 0,016 | 0,752 | 7,4              | 2,3    | +0,03      | 0,752                         |
| 3       | 0,023 | 0,561 | 6,8              | 4,3    | −0,34      | 0,557                         |
| 4 (7/8) | 0,031 | 0,357 | 8,2              | 6,0    | −0,57      | 0,344                         |

Die Cauchy-Schwarz-Kette ist auch hier fast scharf, aber mit einheitlichen Konstanten bräuchte man (I-Faktor)·C < 2,4; bei 7/8 ist es ≈ 49. Stufe A bei 7/8 ist stark korreliert (Verarmung 64 %); Herausnehmen eines Paares mit großem k ist viel weicher als frei. Die Zielungleichungen passen zu harten Bosonen bei kleiner und mittlerer Dichte, nicht zu Stufe A bei 7/8; dort müsste die Verarmung je k einzeln abgeschätzt werden. Die Methode wird deshalb zuerst an den Bosonen entwickelt.

## Eichung χ(k) aus dem Wurm (2026-11-09) [N]

[pruef_chi.py](pruef_chi.py): exakte Duhamel-Suszeptibilität χ(k) = β(A_k†, A_k)\_D bei β = 4, μ = −2,3 auf 4×4 gegen das zeitintegrierte Histogramm `hist_all` (zwei Seeds). Ergebnis:

```text
χ(k) = Σ_r e^{−ik·r} hist_all(r) / (Σ nZ · K),    K = 2 C_w M β = 0,2   (gemessen 0,2005 / 0,2003, Streuung je k ≤ 0,9 %)
```

Mit C_w = 1/(10 M β) (Voreinstellung) ist K = 0,2 unabhängig von L und β. Die Infrarotschranke gilt auch bei endlicher Temperatur (Duhamel-Form): χ·E ≤ 0,65 auf 4×4, β = 4. Für die einseitigen Größen χ⁻, χ⁺ müsste der Wurm das Histogramm zusätzlich nach der Zeitordnung der Enden trennen (vernichtendes Ende früher oder später); das ist noch nicht eingebaut.

## Spektrum des Herausnehmens; (I) ist falsch normiert (2026-11-09)

[z2/zweipaar_graph/spektral_entfernen.py](z2/zweipaar_graph/spektral_entfernen.py): Lanczos-Spektrum von u_k = A_kψ im Sektor N−1 (exakt). Gibt niedrigste Anregung ε\_min mit Gewicht Z, harmonisches Mittel ε\_h = n_k/χ⁻ und χ⁻E/ρ je k [N].

- 2D: ε\_min/E fällt bis 0,63, aber nur bei großem k, wo Z ≈ 0,03 und n_k winzig ist. Das gewichtete ε\_h/E ist ≥ 0,69. Bei kleinem und mittlerem k ist Z = 0,84–1 (ein Quasiteilchen).
- Korrektur zur 1D-Zeile oben: Die dort mit L wachsende Verletzung kam von μ in der Intervallmitte. Kanonisch ist (I) bei ρ = 1/8 etwa 1,4 und stabil (L = 24: 1,44; L = 32: 1,42). Ursache ist die große Verarmung n_k/ρ = 1,5–3,7 bei kleinen k (Quasi-Kondensat), nicht Fermi-See-Löcher bei großem k (dort Z → 0, aber n_k klein).
- Stufe A, 8×8, P = 3 / 4: Maximum von (I) beim kleinsten k ≠ 0, dort sauberes Phonon (Z = 0,998 / 0,969, ε\_h = 1,44 / 1,52·E), aber n_k/ρ\_b = 9,8 / 12,5. Das Minimum von ε\_h/E (0,08 / 0,14) liegt bei großem k (E ≈ 7–8), wo n_k/ρ\_b ≤ 0,01 ist; harmlos.

Absolutwert χ⁻E (nicht durch ρ geteilt) beim kleinsten k ≠ 0:

| Modell         | L            | ρ                  | χ⁻E                   | χ⁻E/ρ              |
|----------------|--------------|--------------------|-----------------------|--------------------|
| 1D             | 16 / 24 / 32 | 0,125              | 0,184 / 0,169 / 0,155 | 1,47 / 1,35 / 1,24 |
| 1D             | 24           | 0,25               | 0,140                 | 0,56               |
| 2D             | 4            | 0,125 / 0,25 / 0,5 | 0,027 / 0,096 / 0,230 | 0,21 / 0,38 / 0,46 |
| 2D             | 6            | 0,056 / 0,111      | 0,014 / 0,052         | 0,26 / 0,47        |
| 2D             | 8            | 0,031              | 0,010                 | 0,33               |
| Stufe A, P = 3 | 8            | 0,023              | 0,158                 | 6,76               |
| Stufe A, P = 4 | 8            | 0,031 (7/8)        | 0,256                 | 8,20               |

**Befund [H]:** Im Phononbereich (k unterhalb des Heilungsimpulses) hängt χ⁻E nicht von der Dichte ab:

```text
Bogoliubov:      χ⁻(k) = v_k²/ω_k  →  1/(4E(k))            (k → 0, unabhängig von ρ und g)
hydrodynamisch:  χ⁻(k)E(k) → f₀/(4 f_s)                     (f₀ Kondensat-, f_s Superfluidanteil; Josephson-Relation)
```

1D (0,14–0,18) und Stufe A (0,16 / 0,26) liegen in dieser Größenordnung; bei 7/8 trifft Stufe A den Bogoliubov-Wert 1/4. Die 2D-Gitter bis 8×8 erreichen den Phononbereich bei kleiner Dichte nicht, weil ihr kleinstes k zu groß ist; daher die kleinen Werte.

**Folgerung:** (I) in der Form χ⁻E ≤ ρ ist falsch normiert. Im thermodynamischen Limes muss (I) bei kleiner Dichte (ρ ≲ f₀/(4f_s)) für k unterhalb des Heilungsimpulses verletzt sein [H]. Die Aussage „beide Ungleichungen in 2D mit großem Abstand“ oben ist ein Effekt kleiner Gitter. Die Stufe-A-Werte 6,8–8,2 sind 0,16/ρ\_b: nur die kleine Paardichte, nichts Exotisches.

- Eine Kette mit k-unabhängigen Konstanten kann bei kleiner Dichte grundsätzlich nicht tragen. Im Phononbereich gilt c⁻ ≈ gρ/2 und χ⁻ ≈ 1/(4E), die Kette verlangte also g·J²/8 < ρ. ODLRO folgt trotzdem, weil der Phononbereich klein ist (Fläche ∝ gρ).
- Ein Beweis braucht k-abhängige Schranken, ähnlich den zwei Ungleichungen von Kennedy–Lieb–Shastry. Bei kleinem k: χ⁻E ≤ a mit a = O(1). Bei großem k: Herausnehmen ist nicht zu billig, und n_k ist klein.
- Bei ρ = ½ ist (I) gleichwertig zur bewiesenen Infrarotschranke (χ⁺ = χ⁻ durch Teilchen-Loch-Symmetrie, also χ⁻E ≤ ½) [B].
- Teilchen-Loch-Symmetrie (ρ ↔ 1−ρ) hilft nicht: Bei ρ = 7/8 steckt das verdünnte Lochproblem im flachen Untergrund n_k = n_k^Loch + 2ρ − 1.
- Kein Zirkelschluss: Der Kondensatanteil steht im Zähler einer oberen Schranke und darf durch f₀ ≤ 1 ersetzt werden. Übrig bleibt eine untere Schranke für die Steifigkeit, die logisch schwächer ist als ODLRO (1D hat Steifigkeit ohne ODLRO), aber ebenfalls unbewiesen. Die bekannte strenge Ungleichung (Bogoliubov, Hohenberg 1967) gibt χ nur nach **unten** (mit der kinetischen Energie statt der Steifigkeit). Die Richtung nach oben ist der Josephson-Teil und als Ungleichung nicht verfügbar [L].
- Prüfbar im thermodynamischen Limes: Runde 1 des Wurms (L = 32, ρ = 1/16, β = 64; kleinstes k = 2π/32 liegt im Phononbereich). Erwartet wird n_k/ρ deutlich > 1 beim kleinsten k (Bogoliubov-Abschätzung etwa 3–6), gegen 0,25 auf 6×6.

## Weltlinien-Ensemble als Beweisobjekt (2026-11-09)

[weltlinien_beweisobjekt.md](weltlinien_beweisobjekt.md): ODLRO als Aussage über den Perron-Vektor des Token-Graphen und über offene Wege (Wurm); Wörterbuch Physik ↔ Graph, Literaturkarte, Kandidaten-Lemmata K1–K4. Exakte Identitäten geprüft mit [pruef_identitaeten.py](pruef_identitaeten.py) [N].

## Einpunkt-Kriterium und zeitartige Routen (2026-11-09)

*Überholt (Vermerk 2026-11-13, Review H1):* Dieser Abschnitt und „Beweisplan“ beschreiben den verworfenen Weg über die Lücke. Gültig ist die Zeitschleife: [tutorial_beweis_verduennt.md](tutorial_beweis_verduennt.md) §10, [anhang_gegenluecke.md](anhang_gegenluecke.md) G.10 bis G.12, [anhang_zweites_moment.md](anhang_zweites_moment.md) (Anhang Z, Stand der Beweiskette in Z.12 und Z.13) und [anhang_buchfuehrung.md](anhang_buchfuehrung.md) (Anhang M).

[einpunkt_zeitroute.md](einpunkt_zeitroute.md): N₀/N ≥ H̄² mit H̄ = Affinität zwischen Faser (Bad um ein Teilchen) und (N−1)-Grundzustand [S]; punktweise ρ₁(x,y)/ρ ≥ 2H̄² − 1. Exakt mit [einpunkt_kriterium.py](einpunkt_kriterium.py) [N]: in 2D ist Z₀ = N H̄²/N₀ ≈ 0,999 (L = 4, 5, 6), in 1D fällt H̄² wie L^{−1/2}. Weltlinien: Lücke in Zeitrichtung, Querrichtungen räumlich, Raum-Zeit ℤ³ (BPP-Routen). Gegenprobe über Starrheit des Punktprozesses |ψ|² (1D und Laughlin starr, 2D-Phononen nicht).

## Lücken-Green-Funktion G(τ) im Wurm (2026-11-10)

- `wurm_nb4.py` misst jetzt zusätzlich `hist_tau`: den Zeitabstand vom vernichtenden zum erzeugenden Ende (Länge der Lücke), über alle Verschiebungen summiert (k = 0). Kanonisch werden nur Konfigurationen mit n Teilchen außerhalb der Lücke gezählt. Die Kette ist unverändert, weil Messungen keine Zufallszahlen ziehen.
- Geprüft mit [pruef_gtau.py](pruef_gtau.py) gegen die exakte kanonische G(τ) = Tr[e^{−(β−τ)H_N} b₀⁺ e^{−τH\_{N−1}} b₀]/Z (4×4, N = 4, β = 4): χ² = 18,2 bei 15 Freiheitsgraden, Prüfzähler der Teilchenzahl-Abkürzung 0. Mit μ = E₀(N) − E₀(N−1) ist e^{−μτ}G(τ) flach bis auf 0,1 % (Z₀ = 0,9988).
- Produktion: [scan_gtau.py](scan_gtau.py) über [gtau_start.sh](gtau_start.sh), startet automatisch nach `ergebnisse/runde1.done`. Es sind 6 Prozesse mit nice 0, je 12 h: L = 16 (β = 32) mit ρ = 1/16 und 1/8, L = 32 (β = 64) mit ρ = 1/16 und 1/8 (je 2 Seeds). μ wird aus Runde 1 übernommen. Fertigmeldung `ergebnisse/gtau.done`.
- Auswertung ([auswertung_gtau.py](auswertung_gtau.py), Läufe fertig 2026-11-10 21:43, ergebnisse/auswertung_gtau_final.txt): Z₀ = 1,001 ± 0,003 (L = 16, ρ = 1/16), 1,000 ± 0,004 (L = 16, ρ = 1/8), 0,983 ± 0,011 (L = 32, ρ = 1/16, zwei Seeds gemittelt). Bei L = 32, ρ = 1/8 zu wenige Blöcke (49 bzw. 58) für eine Aussage. Das Einpunkt-Kriterium verliert also auch bei L = 32 höchstens wenige Prozent. Für den Beweis ist das seit der Zeitschleife nur noch Hintergrund.

## Begegnungen der Skelette (2026-11-10)

[skelett_begegnungen.py](skelett_begegnungen.py), Ergebnisse in [einpunkt_zeitroute.md](einpunkt_zeitroute.md) §11 und `ergebnisse/skelett_*.log`. Mit zwei Querrichtungen ist die Begegnungszahl beschränkt (E J ≈ 85 bei Skala 1, ≈ 6,9 bei Skala 8, unabhängig von w bis 16384). Mit einer Querrichtung wächst sie wie w^{1/4} (dyadisch) bzw. w^{1/2} (diffusiv); diffusiv mit zwei Querrichtungen wächst sie wie log w. Das Budget für lokale Kosten je Begegnung ist α\_max ≈ 0,012 (Skala 1) bzw. 0,17 (Skala 8).

## Runde 1 ausgewertet (2026-11-10, je 16 h, [auswertung_runde1.py](auswertung_runde1.py))

Die χ-Eichung ist gegen exakt geprüft (4×4, Abweichung < 1 %). n₀ grob = g(L/2,0)/ρ, mit Extrapolation n₀ + a/L aus L = 16 und 32.

| ρ      | n₀ (L = 16 / 32 / extrapoliert) | f_s = ρ\_s/ρ | n_k/ρ beim kleinsten k (L = 32) | χE beim kleinsten k | Josephson n₀/(2ρ\_s) | μ + 4 |
|--------|---------------------------------|--------------|---------------------------------|---------------------|----------------------|-------|
| 0,0649 | 0,831 / 0,790 / ≈ 0,75          | 0,963        | 9,05                            | 0,464               | 0,410                | 0,332 |
| 0,1298 | 0,743 / 0,729 / ≈ 0,72          | 0,908        | 8,40                            | 0,432               | 0,401                | 0,771 |
| 0,2559 | – / 0,599 / –                   | 0,795        | 6,56                            | 0,332               | 0,377                | 1,769 |
| 0,5000 | – / 0,391 / –                   | 0,545        | 4,56                            | 0,368               | 0,358                | 4,000 |

- **n_k ∝ 1/k im Phononbereich:** Von L = 16 auf 32 verdoppelt sich n_k/ρ beim kleinsten k (3,4 → 9,1 bei ρ = 1/16).
- **χE beim kleinsten k liegt nahe der Josephson-Erwartung n₀/(2ρ\_s):** 0,46 gegen 0,41 bei ρ = 1/16; 0,37 gegen 0,36 bei ρ = ½. Bei größeren k ist die Fourier-Summe verrauscht (vereinzelt n_k < 0).
- **Ungleichung (I) χ⁻E ≤ ρ ist bei ρ = 1/16 verletzt, wie vorhergesagt.** Bogoliubov-Anteil bei k = 2π/32, mit c² = ρ\_s/κ, κ = Δρ/Δμ ≈ 0,148: χ⁻/χ = v²/(u² + v²) ≈ 0,23. Damit ist χ⁻E ≈ 0,11 > ρ = 0,065. Bei ρ = 1/8 liegt es an der Grenze, bei ρ ≥ ¼ gilt (I). Für k → 0 wird χ⁻/χ → ½ und die Verletzung bei kleinem ρ größer (§ „Spektrum des Herausnehmens“).
- **μ + 4 liegt 21–26 % über Lieb–Yngvason in führender Ordnung**, passend zur nächsten Ordnung (einpunkt_zeitroute.md §16.1).
- **Die G(τ)-Läufe laufen seit 09:41** (6 Prozesse, nice 0, 12 h, Fertigmeldung `ergebnisse/gtau.done` gegen 21:45).

## Beweisplan (2026-11-10)

*Überholt (Vermerk 2026-11-13, Review H1):* siehe den Vermerk bei „Einpunkt-Kriterium“; der hier beschriebene Plan ist durch die Zeitschleife ersetzt.

[beweisplan_verduennt.md](beweisplan_verduennt.md) fasst den zeitartigen Staffellauf-Beweis für verdünnte 2D-Bosonen zusammen: Ziel, Bilder, Abhängigkeiten, Lemmata mit Status, Reihenfolge der Konstanten, numerische Belege und offene Punkte.

## Lochkosten im Wurm (2026-11-10)

[scan_leer.py](scan_leer.py) misst im Z-Sektor die Wahrscheinlichkeit P(τ), dass ein h×h-Block eine Zeit τ lang leer bleibt, über alle Blocklagen gemittelt. Für großes τ erwartet man −ln P ≈ c₀ + τ ΔE, mit ΔE der Lochenergie im thermodynamischen Limes (Feynman–Kac-Lochargument, einpunkt_zeitroute.md §28–§29).

- **Kurztest** (L = 16, ρ = 1/16): Die Blockbesetzung stimmt exakt. P(leer) ist 0,75 bzw. 0,27 (Poisson: 0,77 bzw. 0,35), also gleichmäßiger als Poisson. Für den 4×4-Block ist ΔE ≈ 0,68.
- **Läufe** über [leer_start.sh](leer_start.sh), seit 2026-11-10 ≈ 13:50: 8 Prozesse, nice 0, je 8 h. L = 32, β = 64; ρ = 1/16 mit h = 4, 6, 8 und ρ = 1/8 mit h = 3, 4, 6, je 4 Seeds. Fertigmeldung `ergebnisse/leer.done`.
- **Ergebnis** ([auswertung_leer.py](auswertung_leer.py), ergebnisse/auswertung_leer_final.txt): Lochenergie je verdrängtem Teilchen ΔE/(ρh²) = 0,75 (h = 4), 0,65 (h = 6) bei ρ = 1/16; 1,40 (h = 3), 1,23 (h = 4) bei ρ = 1/8. Für h = 8 (ρ = 1/16, P(leer) = 10⁻³, nur 7 Punkte) und h = 6 (ρ = 1/8) reicht die Statistik nicht. Der Wert je Teilchen fällt mit h, wie ein Randbeitrag ∝ h es verlangt.

## Manuskript und Gitter-Energiesatz (2026-11-10)

- [manuskript_verduennt.md](manuskript_verduennt.md): geordnete Fassung des Beweisprogramms. Hauptsatz (bedingt), Lemmata mit Status, strenge Beweise der [S]-Teile, Konstantenreihenfolge, offene Punkte, Skript-Anhang.
- [gitter_lieb_yngvason.md](gitter_lieb_yngvason.md): Grundenergie des verdünnten 2D-Gitter-Bosegases, ε\_N/N = 4πρY(1 + o(1)) mit der Gitter-Streulänge a = e^{−γ}2^{−3/2}. Obere Schranke [S] über Dysons Nächster-Nachbar-Jastrow, untere [B] über das diskrete Dyson-Lemma (Strom statt Sternförmigkeit) und Temple.
- [tutorial_beweis_verduennt.md](tutorial_beweis_verduennt.md): der ganze Beweis als Tutorial (Bild, Aussage, Beweis, Zahlen, Übungen mit Lösungen; ehrlicher Stand je Schritt). Rechenübungen in [tutorial_uebungen.py](tutorial_uebungen.py). Dabei gefunden: Zellenschranke für mehrere Teilchen ohne Paarung, Faktor 3 (H ≈ 17–25, C_a ≈ 2–3·10³). Fassung 2 (2026-11-10): Kap. 3–5 auf die Zeitschleife umgestellt (Kondensat als Masse offener Konfigurationen, |µ| = N₀/N; Aufweg Löschen, Abweg Einfügen; Bezug B im selben Sektor); Kap. 2 und die Lücke G(τ) nur noch Hintergrund. Abbildungen 1–6 aus [abbildungen_tutorial.py](abbildungen_tutorial.py).
- [anhang_gegenluecke.md](anhang_gegenluecke.md): Satz 5.2 (Gegen-Lücke) ausgeschrieben, Teil 1. Dichteformel G1, zweites Moment G2, exakte Fernkürzung G3 [S]; G1 exakt geprüft mit [pruef_gegenluecke.py](pruef_gegenluecke.py) (Mini-Ring, vollständige Aufzählung, Fehler 5·10⁻¹⁶). G4–G7 als Beweisskizze nach OA §10.2–10.5 (Jensen beim harten Kern durch Einpfad-Randdichte und Ausweich-Untergrenze p\* ersetzt; Übertragung auf das Gegen-Lückenmaß nach OA Satz 7.3). Offene Teilaussagen in G.9.
- **Zeitschleife (Anhang G.10):** Route hinauf und zurück zur Zeit 0, Gegen-Zustand im selben Sektor, Übertragungs-Lemma = OA Satz 7.3. Dichteformel exakt geprüft mit [pruef_zeitschleife.py](pruef_zeitschleife.py) (177 477 bzw. 199 944 offene Konfigurationen, Fehler ≤ 5,6·10⁻¹⁶).
- **Prüfung der offenen Punkte (Anhang G.11, 2026-11-10 abends):** Der Abweg aus G.10.5 (Kopf in seiner Zelle festgehalten) ist falsch, ∫f² wächst je Scheibe um 4,5–14 ([pruef_abwaerts_einteilchen.py](pruef_abwaerts_einteilchen.py), exakt für N = 1). Richtig ist der Spiegel-Abweg (freier Anfang, zyklisches Umsteigen); Dichteformel exakt geprüft und Ausbeute stabil in w mit [pruef_zeitschleife_spiegel.py](pruef_zeitschleife_spiegel.py) (Fehler ≤ 7,3·10⁻¹⁶). Außerdem: OA Satz 7.3 trägt über viele Scheiben; OA Lemma 8.1 trägt für Schleifen (T ≈ L s/16); orientierte Umwege und die Treffsumme in Lemma P\* sind neu zu zeigen.
- [anhang_schleifen.md](anhang_schleifen.md) (Anhang S): Geometrie der Zeitschleifen. Lemma S1 = OA Lemma 8.1 für Schleifen (Gegenhälften-Begegnungen mit fester Verschiebung), Lemma S2 orientierte Umwege (Lage im Außenraum der Füllungen beider angrenzenden Scheiben), Lemma S3 Schwänze. Numerik: [pruef_schleifen_geometrie.py](pruef_schleifen_geometrie.py), ergebnisse/pruef_schleifen_geometrie_teil1/2.txt.
- [anhang_ausweichen.md](anhang_ausweichen.md) (Anhang P): Lemma P\* für die eigenen Stücke der Teilchen ersetzt durch zugängliche Teilchen (wie OA-Hartkugel §7.3). Kippidentität P1, Spektralschranke P2 (Z(A frei)/Z_N ≤ e^{δ(ε\_N−ε\_{N−|A|})}, exakt geprüft mit [pruef_zugaenglich.py](pruef_zugaenglich.py)), Satz P3: P(A unzugänglich) ≤ e^{−κ|A|}, p\* = e^{−δμ̄−κ}. Offen: Ausweich-Untergrenze für umgehängte Brücken S_l → Y\_{l−1} und neue Stücke des Abwegs (P.6), der eigentliche Ersatz für Jensen.
- [satz_3_9_dichteschranken.md](satz_3_9_dichteschranken.md) §9: Defekt-Lemma Satz D für die Zeitschleife (sieben Gründe D1–D7, Normform je Scheibe, Mischen, Übertragung auf µ\_ab mit Exponent 1/4). Rest: Satz T2 (auch mehrskalig). Kalibrierung der Regularität mit [pruef_regularitaet.py](pruef_regularitaet.py): A ≈ 6–8. Treffschranke bewegter Ziele: [pruef_treffen_bewegt.py](pruef_treffen_bewegt.py).
- [satz_3_9_dichteschranken.md](satz_3_9_dichteschranken.md) §10: Satz T2 ausgeschrieben (Gitter, Grundzustand): Fächer makro/Rand/R2/R3, gefärbter Operator, E e^J ≤ e^{δε\_N}‖T‖, Gitter-Einschub Lemma T3 mit W₀ = 2a/δ + c₁Σ(cosh Δa − 1), exakt geprüft mit [pruef_lipschitz.py](pruef_lipschitz.py) (48 Fälle). Offener Eingang: Satz 3.9 (a) mit schwachem anziehendem Potential, gleichmäßig in J ≤ N.
- [satz_3_9_dichteschranken.md](satz_3_9_dichteschranken.md) §11: Dichte-Eingang Satz 3.9 (a^W) mit anziehendem Potential, gleichmäßig in J ≤ N [S]; Lemma 11.1 (Einfügen mit Potential ≤ μ̄) exakt geprüft mit [pruef_einfuegen_potential.py](pruef_einfuegen_potential.py); Folgerung 11.2 für viele Zeiten über Lemma T3.
- [satz_3_9_dichteschranken.md](satz_3_9_dichteschranken.md) §12: Punkt 3 geschlossen. Scores entfallen (dienen bei OA nur Jensen); Isolation Satz 3.9 (c) [S] über Paarzählung Q in verschobenen 2r-Kästen (μ̄/λ\_min(2r) ≈ 32κ\_μζ²); untere Schwänze über viele Zeiten [S] über Lemma 12.1 (abstoßendes Potential, Minimum-Argument) und Lemma T3 mit negativem A.
- [anhang_gegenluecke.md](anhang_gegenluecke.md) G.12: Buchführung für die Zeitschleife (Punkt 1). Konstruktion endgültig (Spiegel-Abweg Variante a: Anfang gleichverteilt unter isolierten freien Plätzen der Zelle, Querschritt je Scheibe); G1–G3′ [S]; G4–G7 [B] mit P3/P6, S1–S3, Satz D, G.11.2; Annahme |ν| ≥ υ/2; Schluss N₀/N ≥ c. Rest: Ausarbeitung im Stil OA §10, Details P6, MC-Prüfung der Ausbeute.
- [anhang_zweites_moment.md](anhang_zweites_moment.md) (Anhang Z): zweites Moment der Zeitschleife, Schritt für Schritt nach OA §10 mit OA-Nummern als Anker: Zustände und Gruppen je Scheibe (Selbstbegegnungen kürzen sich), Kernfaktoren, zwei Nenner über P3/P6, Zurückholen, Stabilität ohne Scores, Listen über Lemma S2, Kreuzvergleich, Defekte unter µ\_ab, Summieren mit Endzellen der Schleife, Reihenfolge der Konstanten. Satz Z: ∫f²dµ ≤ C.
- Anhang P, P.7.5: Lemma P6 vollständig (P6a kurze Brücke q ≥ ½ über Hälftenvergleich und P5′; P6b mittlerer Schritt einmal teilen; sehr große Schritte und schlechte Zwischenpunkte ins Ausnahmeereignis; Jensen über Schrittweiten; ζ² ≤ n^{−C}/C₀).
- [pruef_zeitschleife_mc.py](pruef_zeitschleife_mc.py): Monte Carlo für die Ausbeute (C exakt per Transfermatrix, Konstruktion zufällig, f exakt); gegen Aufzählung validiert. Option --locker (Wählbarkeit = Ende in der Zelle) auch in pruef_zeitschleife_spiegel.py, Dichteformel exakt. Im Testmodell (eine Scheibe = ein Trotter-Schritt) zu viele Verwerfungen; braucht mehrschrittige Scheiben (ergebnisse/pruef_zeitschleife_mc.txt).
- [anhang_kern.md](anhang_kern.md) (Anhang K): Kern-Schranken (K1) p_t(x) ≤ (1+t)^{−1}e^{−|x|²/(4(t+|x|∞))}, (K2) p_t(x) ≥ (4π)^{−1}(1+t)^{−1}e^{−|x|²/(4t)} mit Konstanten, exakt geprüft ([pruef_kernschranken.py](pruef_kernschranken.py)); Brückenmaximum K3, Schlauch K4; Lemma S1 ohne Literatur; Lemma R (Regularität der freien Irrfahrt: (G2_A) versagt mit ≤ Cτ^{1−c′(A)}, B\* doppelt-exponentiell; b₀ wächst wie log ln ln(1/ρ), harmlos).
- [satz_3_9_dichteschranken.md](satz_3_9_dichteschranken.md) §8: Satz 3.9 (d) defekte Zellen selten. Lemma T1 [S]: markiertes Teilchen im Grundzustandsprozess wandert höchstens wie eine freie Irrfahrt, E e^{θΔx} ≤ e^{2δ(cosh θ−1)} (Eichtransformation + numerischer Wertebereich), exakt geprüft mit [pruef_markiert.py](pruef_markiert.py). Satz T2 (Zahl der Fehlgänger, gefärbter Operator nach OA §6) [B].
- [pruef_einfuegequotient.py](pruef_einfuegequotient.py): umgekehrte Hölder-Ungleichung für den Einfügequotienten u_a = a\*(1_a)ψ\_N/ψ\_{N+1} (Übertragungs-Lemma, Anhang G.8.4 c). Exakt auf Tori 6–12: ‖u‖₄/‖u‖₂ nur 8–15 % über der Gleichverteilung, bei festem m unabhängig von ρ.
- [pruef_unterloesung.py](pruef_unterloesung.py): Lemma J (Jastrow-Struktur des Einsetzens): ψ\_N(η\\x)·Π f(x−x_j)/ψ\_{N+1}(η) punktweise im Bereich 0,67–1,25 × Mittel (ohne Jastrow-Faktor bis 3,9×). Exakte Jastrow-Unterlösung scheitert. Anhang G.8.4.
- [zeitschleife2d.py](zeitschleife2d.py): Testmodell der Zeitschleife auf dem 2D-Torus ohne Verwerfung durch leere Zellen (Züge nur unter den ausführbaren, Normierung in der Dichteformel; `--zuege alle` als Umweg-Ersatz; `--locker` = Wählbarkeit nach G.5.1). Dichte f exakt per DP über die Scheiben, numpy-Propagatoren für ein und zwei markierte Teilchen. ν = fµ exakt geprüft (Fehler ≤ 1,1·10⁻¹⁵, alle Varianten). Befund bei m ≈ 1 Teilchen je Zelle: freier Spiegel ∫f² beschränkt, zellgebundene Varianten ×3–4 je Scheibe, wie Z.8 für n_Q ≈ 1 erwarten lässt. Nachtlauf [zs2d_nacht.sh](zs2d_nacht.sh) (6×4, N = 6, m = 1; 1,5; 3) prüft die Vorhersage „Faktor − 1 ~ 1/m“. Anhang Z, Z.11.
- Nachtlauf zeitschleife2d (2026-11-11, [auswertung_zs2d_nacht.py](auswertung_zs2d_nacht.py), ergebnisse/zs2d_nacht_auswertung.txt): freier Spiegel ∫f²dµ über w = 1–4 konstant (Schleife gesund); Variante a im kleinen Modell ×3–4 je Scheibe wie der alte Abweg; Kosten: gleichverteilter Anfang ≈ ×2, Pflicht-Querschritt ×1,5–2,5. m-Abhängigkeit mit Zellgröße vermengt, Vorhersage aus Z.8 hier nicht prüfbar. Vorschlag: Anfang aus dem bedingten Gesetz auf freien Plätzen der Zelle. Anhang Z, Z.11.
- Gegenprobe zellgewicht (2026-11-11, [zs2d_zellgewicht.sh](zs2d_zellgewicht.sh)): Anfang aus dem bedingten Gesetz, aber auf die Zelle beschränkt, ist nicht besser als gleichverteilt (×2,9/×3,5 je Scheibe bei m = 1/3). Teuer ist die Beschränkung auf die Zelle; ohne sie (frei) kostet die Scheibe fast nichts. Neuer Vorschlag: bedingtes Gesetz im Ball vom Radius D s um Y_m. Anhang Z, Z.11.
- Test ball (2026-11-11, [zs2d_ball.sh](zs2d_ball.sh)): Anfang aus dem bedingten Gesetz im Ball vom Radius R um Y_m. Λ je Scheibe: R = 1: 2,11; R = 2: 1,17; R = 3: 0,99 (frei 1,00); fällt schneller als 1/P(R) − 1. Vorschlag „Variante c“ für den Beweis: Ball vom Radius D s statt Zelle; Kopfscheibe kostet ≈ 1/P(Ball) statt ≤ 14. Anhang Z, Z.11.
- [anhang_gegenluecke.md](anhang_gegenluecke.md) G.12.9 (2026-11-11): Variante c des Abwegs, Anfang S′ aus dem bedingten Gesetz im Ball vom Radius D_c s um Y_m (isolierte Plätze). Lemma C [S, gegeben P6]: Masse außerhalb ≤ η\_c, geteilte Kopfscheibe ≤ 1/(1 − η\_c) ≤ 2 statt ≤ 14, gemitteltes Stück-Gesetz mit Dichte ≤ 1/(c₁p₁) bezüglich der freien Rückwärts-Irrfahrt (P6 nur für kurze Brücken nötig), Kopfdichte ≤ C/(c₁p₁s²). G.12.1/2/5/7/8 angepasst. Neu: D ≥ D_c + 1, ζ² ≤ c₁p₁/(4CC₀D_c²). Offen [H]: ob der Querschritt entfallen kann.
- Test nie Querschritt (2026-11-11, [zs2d_nie_quer.sh](zs2d_nie_quer.sh)): Abweg ohne Route (nur Einfügen) wächst stetig (Ball R = 3: 1,22 je Scheibe; frei: 1,07–1,16). Mit erlaubtem Querschritt 0,99, mit Pflicht-Querschritt 1,13. Die Route bleibt nötig (G.12.9, Anhang Z, Z.11).
- Variante c nachgezogen (2026-11-11): Anhang Z (Z.0, Z.8 Kopfstück und Rückgewinnung von µ\_ab als Ungleichung mit Faktor C(2D_c+1)²/(c₁p₁), Z.9 D_c in Schritt 2 und ζ-Bedingung in Schritt 4, Z.10, Z.11), Anhang P (P.6 Nachtrag, Tabelle), Tutorial §4.1, §5.3 (neuer Absatz „Warum der Anfang im Ball“), §5.4, §10, Programmtabelle; PDF neu (28 Seiten).
- [review_2026-11-11.md](review_2026-11-11.md) (2026-11-11): unabhängiges Review des Beweisprogramms. Kritische Befunde: K1 (die Gütebedingungen (G1)–(G3) aus Anhang P sind unterhalb der Zellskala nicht gedeckt), K2 (Satz P3 gilt nur für feste Markenmengen), K3 (Lochstück j₀, gute Endpunkte); dazu W1–W7 und H1–H9. K1, K2 und K3 sind beantwortet und eingearbeitet (die nächsten drei Punkte), ebenso W2. W1, W3, W4 und W7 sind ebenfalls erledigt (die letzten beiden Punkte dieser Liste). W5 ist am 2026-11-13 erledigt (Tutorial Lemma 6.3a, Zellenschranke für alle b); W6 am selben Tag mit Anhang E; offen sind die H-Punkte (außer H7).
- [anhang_feinskala.md](anhang_feinskala.md) (Anhang F, 2026-11-11 und 12): Antwort auf K1. Dichteschranken unterhalb der Zellskala über zweiskalige Lokalisierung (Lemma F1, F2, Satz F3); Raum-Zeit-Momente zeitgemittelter Teilchenzahlen (Lemma F6, Satz F7); Lemma P5″ mit der gemeinsamen Aufenthaltszeit 𝔏 statt (G3); deterministisches Lemma F8 und Folgerung F9 (𝔏 ≤ ε\_P ln(1/ρ) für θ ≤ θ\_P ≈ 10⁻²⁶ ε\_P²); Seltenheit der neuen Bedingungen (G1″) und (G4) gemeinsam über viele Zellen (Satz F10; Lemma F11a und Satz F11 über ein Fach in Satz T2); Lemma F13 (P_treff ohne (G3)); Lemma P6 neu mit zufälligen Zwischenzeiten (F.12). C₀, C₁ und b₀ entfallen, und die Konstanten haben keinen Zirkel mehr. Bausteine exakt geprüft mit [pruef_feinskala.py](pruef_feinskala.py) (ergebnisse/pruef_feinskala.txt). Eingearbeitet am 2026-11-12 in Anhang P (P.7), satz_3_9 §9–§12 (D6, D7, Fach G4 statt R3), Anhang K (K.4), Anhang Z (Z.3, Z.9, Z.10), Anhang G (G.12.5, G.12.8, G.12.9) und Tutorial §10. Die Konstanten taugen nicht für eine Schwelle (ζ² ~ (208n)^{−117} mit n = K/θ); für den Existenzsatz ist das gleichgültig.
- [anhang_lochstueck.md](anhang_lochstueck.md) (Anhang L, 2026-11-12): Antwort auf K3. Das Lochstück j₀ des Aufwegs wird nicht gewählt, und „beginnt in einer guten Zelle“ sichert weder ein isoliertes Ende noch, dass es nicht weit wandert. Abhilfe ohne Verwerfen: Wählbarkeit über zwei Scheiben (j_m nur unter Stücken mit regulärer Fortsetzung), Umstieg in jeder Scheibe (notfalls innerhalb der Zelle), einmaliges Verwerfen in Scheibe 0. Lemma L1 (j₀ regulär, alle Brücken mit guten Endpunkten), Lemma L2 (Vorrat ≥ (1 − 2ε) n_Q), Lemma L3 (Dichteformel mit gekoppelten Scheiben), exakt geprüft mit [pruef_lochstueck.py](pruef_lochstueck.py) (Mini-Ring, N = 2 bis 4, w = 2 und 3, Fehler ≤ 7,5·10⁻¹⁶; ergebnisse/pruef_lochstueck.txt). Folgen: κ₀ = 10ε + … statt 2ε + …, R\* um 2D + 4 größer, ζ² ≤ εb₋/(768 (2D + 3)² C_iso), |ν| ≥ υ/2 − ε. Eingearbeitet in Anhang G (G.5.1, G.12.1, G.12.5–G.12.7), Anhang Z (Z.0, Z.5, Z.8, Z.9), Anhang S (S.0, S.2), satz_3_9 (§9.1, §12.2) und Tutorial (§5.2, §8, §9, §10). Abb. 5 des Tutorials und das PDF sind nicht neu erzeugt.
- [anhang_unzugaenglich.md](anhang_unzugaenglich.md) (Anhang U, 2026-11-12): Antwort auf K2 und W2. Satz P3 war nur für feste Marken bewiesen, gebraucht wird er für die Stücke, die gerade in einer Zelle sitzen; und die aus der Hartkugel-Arbeit übernommene Gruppe von M Teilchen je Zelle passte nicht zu den Kosten 1/n_Q. Jetzt: keine Gruppe; ein Stück ist zugänglich, wenn seine freie Brücke (mit cut) *allen* anderen Stücken der Scheibe mit Wahrscheinlichkeit ≥ p\* ausweicht. Lemma U1 (Entkopplung: beschränkt viele markierte Stücke blockieren einander nur um k₀ (2R + 2D + 3)² P_treff ≤ p\*), Lemma U2 (Kippidentität für feste Marken als Kernungleichung), Lemma U3 (Satz T2 für einen vorgegebenen Kern, markierte Farbe auf dem Torus, Konstanten explizit), Satz U: E[Π\_Q (X_Q über k₀)] ≤ (C_U m e^{−κ}/k₀)^{k₀|𝒜|}, also P(in allen Zellen von 𝒜 mindestens (ε/4) b₋ m unzugängliche Stücke) ≤ e^{−k₀|𝒜|} mit κ\_U = ln(48 e⁶ C_a (2D + 7)²/(ε b₋)) und k₀ ~ ln(1/ρ)/ln ln(1/ρ). Lemma U4 (Monotonie, Randschranke 2/p\*, zwei Schwellen p\* und 2p\* für die Stabilität). Kippidentität für Stücke und Paare exakt geprüft mit [pruef_unzugaenglich.py](pruef_unzugaenglich.py) (Mini-Ring, vier Parametersätze, Fehler ≤ 6·10⁻¹³; ergebnisse/pruef_unzugaenglich.txt). Eingearbeitet in Anhang P (P.1, P.2, P.4), satz_3_9 (§9, §12.4), Anhang G (G.12.0, G.12.1, G.12.5, G.12.6), Anhang Z (Z.0, Z.3, Z.5, Z.9, Z.10), Anhang L und Tutorial §10. Die Gruppengröße M entfällt als Konstante.
- Review W3, W4, W7 (2026-11-12): (W3) In Anhang Z heißen Z.2, Z.5, Z.6, Z.8 jetzt [B nach OA]; „[S nach OA]“ nur noch für Lemma S1 und G.11.2, deren OA-Vorlagen samt Beweis nachgelesen sind. (W4) Anhang Z, Z.9: Tabellen der festen und der von ρ abhängigen Größen; mit ρ wachsen nur m, β ~ ln ln(1/ρ) und k₀; κ₀ → 10ε. (W7) Der Satz gilt für L ≥ L₀(ρ) = 16 s(ρ); für N ≤ (π/(5κ\_μ)) ln(1/(ρa²)) folgt N₀/N ≥ 1/2 elementar aus ε\_N ≥ ε\_min(L)(N − N₀); dazwischen ist er nicht bewiesen (Tutorial §0.1).
- Review W1 (2026-11-12): Lemma C (e) in G.12.9. Eine von beiden Schleifen geteilte Kopfscheibe kostet im zweiten Moment den Kehrwert des Normierers, bezogen auf die freie Kernmasse ≤ 1/(c₁p₁); die frühere Zahl „≤ 2“ galt nur für ein Teilchen (typisch ist e^{2πK}). Die Reihe konvergiert für m ≥ 2C/(c₁p₁). Verdickung in Anhang S jetzt D′ = 2D + 2 (Ball des Abwegs). Angepasst: G.12.7, G.12.9, Z.8, Z.9, S.0, S.2.
- [anhang_einfuegen.md](anhang_einfuegen.md) (Anhang E, 2026-11-13): Antwort auf W6. Einfügen harter Bosonen im Dirichlet-Quadrat (Lemma E1, Dichte zählt mit max φ²), Produktzustand (Lemma E2), Energieungleichung mit glatter Innenzahl S_U (Lemma E3), untere Schwänze zu einer Zeit (Satz E) und zu vielen Zeiten (Folgerung E4 = Folgerung 12.2). b₋ = c₃″/8, etwa 6- bis 8-mal kleiner als vorher. Prüfung: [pruef_einfuegen.py](pruef_einfuegen.py).
- [anhang_buchfuehrung.md](anhang_buchfuehrung.md) (Anhang M, Teile 1–5, 2026-11-13): Buchführung im zweiten Moment. Inventar aller Tests mit Reichweite und Stufen; Korrekturen: Kastenbedingungen als Klausel (v) der Brauchbarkeit, gezogene Brücken und neue Stücke regulär (Lemma M2), Stufen für (G1″) (Lemma M3), R\* explizit; Lemma M4 (Stabilität) ersetzt Lemma Z.5. Teil 2: die Nenner Z.2–Z.4 aus einem Vergleichslemma (Lemma M5) mit Lemma P6″ für alle Stücke. Teil 3: Z.6 (Lemma M9) und das Summieren über die Auswahl (Lemma M10). Teil 4: Listen, J und seltene Komponenten (Lemma M11–M13); offen nur noch Endzellen und Bezugsmaß (Teil 5: Stand, Bezeichnungskorrektur, Restsatz M14). Besucher eines Kastens (D4/D7): satz_3_9 §10.8, Lemma T4, T5, Satz T2′, Folgerung T6, mit C\_β ≥ 500; Prüfung [pruef_besucher.py](pruef_besucher.py).
- [uebergabe_m14_kopf.md](uebergabe_m14_kopf.md) (2026-11-13): Übergabe für den letzten offenen Punkt des zweiten Moments, das Kopfende bei geteilten Kopfscheiben (Restsatz M14).
- Restsatz M14, geteilte Kopfscheiben (2026-11-13, [anhang_buchfuehrung.md](anhang_buchfuehrung.md), M.9.6): Bei k ≥ 1 geteilten verdeckten Kopflagen liegt der Schnitt von B zur Zeit t_k. Lemma M14b [S, gegeben Satz D für N und N + 1 Teilchen]: Das Bezugsmaß µ\_ab^{(k)} behält die Defekt-Kleinheit in allen Scheiben, weil Satz D ein Produkt von Operatornormen je Scheibe ist (unabhängig vom Anfangszustand a\*(1_a)ψ\_N). Die Reihe über k konvergiert für (1 − 2ε)(b₋m − 2)c₁p₁ ≥ 4e^{2C(K)}. Prüfung [N]: [pruef_kopfteilen.py](pruef_kopfteilen.py) (Mini-Ring, exakt: Kette bei Pflicht-Querschritt immer ganz geteilt) und [pruef_kopfteilen2d.py](pruef_kopfteilen2d.py) mit [kopfteilen2d_start.sh](kopfteilen2d_start.sh) (2D-Torus: Beiträge mit k ≥ 1 die Hälfte bis vier Fünftel von ∫f², sie tragen das ganze Wachstum mit w; ergebnisse/kopfteilen2d/). Lemma M14a am Mini-Ring exakt nachgerechnet ([pruef_m14a.py](pruef_m14a.py), Fehler ≤ 1,7·10⁻¹⁵, ergebnisse/pruef_m14a.txt); Lage des Schnitts genau (mit pred\_{I′}(h) in d stets zur Zeit t_k, für k = 0 ohne Hilfspunkt). Endscheiben in M.9.7: Kernzählung je Endscheibe (genau ein Kern C/s², am Kopf), Fortsetzung am Schwanz über übereinstimmende Lochplätze (in M.9.5 übersehen, gedämpft um C/s² je Scheibe), Lemma M14d [B]; Prüfung [kopfteilen2d_schwanz_start.sh](kopfteilen2d_schwanz_start.sh), ergebnisse/kopfteilen2d_schwanz/ (Schwanz 8–21 %, Kopf 44–61 %). Lemma M14d (M.9.8) schreibt die Schritte von M9 für die Endscheiben aus [S, gegeben M4–M8, Lemma C, C′, P6″]; Lemma M14e (M.9.9) erledigt die Summe über die Schnittzellen; Restsatz M14 ist damit bewiesen, gegeben die Lemmata von Anhang M, Lemma C, C′, P6″ und Satz D.
- Kette der Voraussetzungen von Satz Z (2026-11-13, [anhang_zweites_moment.md](anhang_zweites_moment.md), Z.12): Tabelle aller Bausteine bis zu den Eingängen. Urteil: Satz Z ist [S nach OA, gegeben die Bessel-Quotienten im Gitterkern [Lit\]\] (seit 2026-11-13: [S nach OA] ohne Literatur; Anhang K, K.1 mit Lemma K0, K1, K2′, alle Stellen auf (K2′) umgestellt; Prüfung [pruef_bessel.py](pruef_bessel.py)), für Seitenlängen L, die ein Vielfaches einer zulässigen Zellseite sind; für allgemeines L fehlt die Pflasterung [B]. Dabei geschlossen: das Randfach ∗ in Satz T2 (τ₀ festgelegt, Lemma F11a) und die Annahme mit dem neuen Schwanz (|ν| ≥ υ/2 − ε − 5ζ²). Satz D in satz_3_9 §9.2 ebenso neu gekennzeichnet, die Eingangstabelle §10.7 nachgeführt.
- Pflasterung und Systemgröße (2026-11-13, [anhang_zweites_moment.md](anhang_zweites_moment.md), Z.13): ausgeglichene Teilung jeder Achse in n = ⌊L/s⌋ Abschnitte, Zellseiten in [s, 9s/8], Zellgraph (ℤ/nℤ)² unverändert; Lemma 6.3b (Neumann-Kästen als Rechtecke b × (b + 1): R_y ≤ (2/π) ln b + 3,4, λ\_min ≥ π/(2|Q|(ln b + 5,8))) [S], geprüft mit [pruef_pflasterung.py](pruef_pflasterung.py); Tabelle aller Stellen, an denen die Zellform eingeht. L₀ = c_L s(ρ) mit c_L = max(16, 2R\*″ + 2) statt 16 s(ρ), weil die festen lokalen Umgebungen sonst um den Torus reichen können. **Satz Z gilt damit für alle L ≥ L₀(ρ)** [S nach OA, gegeben die Bessel-Quotienten im Gitterkern [Lit\]\].
- Review-Hinweise H1–H9 erledigt (2026-11-13; Stand in [review_2026-11-11.md](review_2026-11-11.md), §3.3): überholte Dokumente markiert, Tutorial-Zahlen (2.3, 9.3), Lemma 6.1, Lemma A, G.11.2, schwere Schwänze im Nachtlauf, ergebnisse/pruef_markiert.txt.
- [uebergabe_review_2026-11-13.md](uebergabe_review_2026-11-13.md): Übergabe an eine zweite unabhängige Durchsicht (Review-Chat), mit den acht am genauesten zu prüfenden Punkten, Leseweg und Startauftrag.
- [uebergabe_2026-11-12.md](uebergabe_2026-11-12.md): Stand der Review-Arbeit für die nächste Sitzung (erledigt: K1–K3, W1–W7; offen: Buchführung im zweiten Moment, Pflasterung, H-Punkte). [mdfmt.py](mdfmt.py): Prüfung des Markdown-Stils und Auffüllen von Tabellen.
- Tutorial nachgezogen und PDF neu gebaut (2026-11-13 abends): §0.1 mit L₀ = c_L s, §0.2 neuer Stand (Beweis für L ≥ L₀ geschlossen, [S nach OA], Tabelle mit Beweisorten), Satz 5.2 und 7.1 [S], Kap. 8 und 9.1, Kap. 10 (offen nur unabhängige Durchsicht und Zwischenbereich W7), Anhang C mit den neuen Prüfprogrammen; Abbildung 5 zeigt den Umstieg in der Zelle. [tutorial_beweis_verduennt.pdf](tutorial_beweis_verduennt.pdf), 30 Seiten (pandoc → HTML → Chrome headless). Dabei gefunden: Lemma S2 benutzt OA Lemma 8.2 (Randzusammenhang, Paritätsbeweis nach Timár), also [S nach OA]; nachgetragen in Anhang S und Z.12.
- Gesamtband zum Gegenlesen (2026-11-13 abends): [beweis_verduennt_gesamt.pdf](beweis_verduennt_gesamt.pdf), 171 Seiten, alle Anhänge unverändert in der Reihenfolge des Lesewegs (Z, M, satz_3_9, G, F, U, L, E, S, K, P), mit Vorspann [beweis_gesamt_vorspann.md](beweis_gesamt_vorspann.md) (was bewiesen wird, Kennzeichnung, welche Abschnitte überholt sind), Inhaltsverzeichnis, PDF-Lesezeichen, anklickbaren Verweisen zwischen den Anhängen und grau gesetzten „Frühere Fassung“-Absätzen. Bau beider PDFs: [pdf_bauen.py](pdf_bauen.py) (`python3 pdf_bauen.py [tutorial] [gesamt]`; pandoc → HTML → Chrome headless). In Anhang S den Kopfsatz zu den OA-Lemmata nachgezogen (8.1 und 8.2).
- Beweisweg mit Verlustbilanz (2026-11-13 abends): [beweis_verlustbilanz.md](beweis_verlustbilanz.md) bzw. .pdf (6 Seiten). Je Schritt bewiesene Konstante gegen wahren/numerischen Wert; Verlusttreppe A Physik (ρ\* ≥ 1/16, N₀/N ≈ 0,75) → B Methode mit wahren Konstanten (ln(1/ρ\*) ≈ 10⁹) → C Buchführung des Beweises mit wahren Eingängen (≈ 10¹⁰⁶⁴) → D Beweis (ln ln(1/ρ\*) ≈ 10³⁹, c ≈ exp(−10³⁹), c_L ≈ 10²⁰). Hauptverlust: Ausweich-Untergrenze p₁ = ½e^{−4900n} mit n = K/θ\_P ≈ 10³⁴ (θ\_P ≈ 10⁻³² wegen C\_𝔏 ≈ 2,4·10⁹ in Lemma F8), daraus auch D, D_K, R\*″ ≈ 10²⁰ und α ≈ 10⁻⁴². Schätzungen [H] mit C_P = 1: [verlustbilanz_zahlen.py](verlustbilanz_zahlen.py), ergebnisse/verlustbilanz_zahlen.txt. Bau: `python3 pdf_bauen.py bilanz`.
- Zweites Review eingearbeitet (2026-11-14, [review_2026-11-13.md](review_2026-11-13.md), Stand der Bearbeitung je Befund): W2 Lemma S2 jetzt OAs Umwegkonstruktion wörtlich (Füllung je Kanten-Komponente, Sternpfade am Außenrand, (F1)–(F3) aus OA Lemma 8.2; Weglänge 2d\_∞ + Σ6|T|, C_J = 12D + 138; pruef_schleifen_geometrie.py Teil 3, auch diagonale Ringe); W3 Lemma M14f [S] (Anhang M, M.9.10: Lage des Schnitts, Fassung von B als Verschiebung längs der Kette von R mit Korrektur am Kopf, Abstände ≤ D + 4 Zellen, begründet auch M8 Schritt 4; Λ = (9/8)(D + 4)); W1 später Anfang am Schwanz (M.9.11: B = C in geteilten Schwanzscheiben, Erzeugung an isoliertem freiem Platz nahe dem gemeinsamen Lochplatz, Bezugsmaß µ^{(k_T,k_H)}, Lemma M14b′ mit Sektor N ± 1, Energiefaktor e^{δμ̄} je Scheibe bei N − 1; Lemma C′ entfällt); H2/H3 Z.9 neu (Rückkopplung D → … → ε mit nκ ≥ 8, r\_∗, κ₀ ≤ α\_J, η-Bedingung einmal, C e^{C′(K)}e^{δμ̄} ≤ s²/2); H1, H4–H8 erledigt (Lemma 9.0 scheibenweise Defekte, Sektoren N − 1, N, N + 1, s ganzzahlig, (K2′)-Kennzeichnungen, p\*-Bezeichnung, |ν| ≥ υ/2 − 5ζ²). Offen: zwei Sonderfälle an den Enden der Schleife [B] (Teilen bis zur Wende, H9; Kopf- und Schwanzende in derselben Scheibe). Satz Z: [S nach OA bis auf diese Sonderfälle]. Tutorial §0.2, §10 und Satz 5.2 nachgezogen.