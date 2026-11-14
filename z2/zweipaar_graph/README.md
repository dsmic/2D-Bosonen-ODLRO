# Zwei-Paar-Relativgraph des Stufe-A-Dimermodells

Begonnen 2026-11-08. Programm [two_pair_graph.py](two_pair_graph.py), Ergebnisse in [ergebnisse/](ergebnisse/). Kennzeichnung: **[A]** numerisch verifiziert für die gerechneten L, **[B]** mathematisch bewiesen (Argument unten), **[S, computergestützt]** endliche Rechnung, die wegen Lokalität für alle L ≥ L₀ und für ℤ² gilt.

## Ergebnis vorweg

- **E₂(L) = 4/7 exakt, für jedes L von 6 bis 1024** [A]; für ℤ² und alle L ≥ 12 [S, computergestützt].
- Grund: Die Drift ist ein Eigenvektor des Relativ-Generators, 𝓛\_rel d₂ = 7 d₂. Der Korrektor ist also exakt lokal, **h₂ = d₂/7**, getragen von denselben 16 Zuständen wie d₂.
- d₂ ≠ 0 nur in 16 Zuständen, alle gemischt orientiert (h,v bzw. v,h), |d₂| = ½, Mittenabstand (±½, ±2½) und (±2½, ±½). Das sind genau die Kontaktmotive des optimalen Korrektors aus [../beweis_box/README.md](../beweis_box/README.md) (dort −0,080 / +0,077 im Vielteilchensystem, hier ±1/14 = ±0,0714 für zwei Paare).
- Monopol 0 und Gesamtdipol 0. Über alle vier Orientierungssektoren summiert ist d̂₂(k) ≡ 0 für jedes k [B]; je Sektor ist der Dipol p\_x = ±4.
- Kontrolle gegen [../stufe_a.md](../stufe_a.md) §15: ρ\_s L²/t\_c = ¼⟨deg⟩ − 2E₂/|R| gibt 1,7843 / 1,8993 / 1,9403 für L = 6 / 8 / 10, wie die vollständige Aufzählung dort [A].

## Installation und Start

Umgebung: conda-Umgebung NetKet (Python 3.12, numpy 2.3, scipy 1.16, matplotlib 3.10). pyamg ist optional und wird benutzt, wenn installiert; nötig ist es nicht.

```bash
conda activate NetKet
cd paartransfer_analyse/z2/zweipaar_graph
python two_pair_graph.py selbsttest                      # 9 Tests, < 1 s
python -m pytest -q                                      # dieselben Tests über pytest
python two_pair_graph.py lauf --L 16 24 32 48 64 96 --jobs 6
python two_pair_graph.py lauf --L 128 256 512 1024 --jobs 4 --keine-bilder --lu-max 0 --out ergebnisse/erweitert
python two_pair_graph.py lauf --L 16 32 64 --gerade --out ergebnisse/gerade   # auch gerade Schritte (nicht Stufe A)
```

Optionen von `lauf`: `--jobs` (ein Prozess je L), `--rtol` (CG, Standard 1e-12), `--lu-max` (LU-Gegenprobe bis zu dieser Komponentengröße, Standard 200 000), `--gerade`, `--out`, `--keine-bilder`. Die lokale [pytest.ini](pytest.ini) verhindert, dass pytest eine NetKet-Warnungskonfiguration aus einem Elternverzeichnis liest.

## Vorprüfung der Übergangsdefinition

- **Eckschritt:** Bindung {u,v}, Pivot v (gemeinsamer Endpunkt), w = v + d mit d ⟂ (v − u), neue Bindung {v,w}. Je Paar zwei Pivots mal zwei Seiten, also vier Schritte, je einer in jede Diagonalrichtung der Bindungsmitte. Die vier Ziele sind verschieden. Der Rückschritt pivotiert um dasselbe v zurück auf u und ist der eindeutige Schritt der neuen Bindung mit diesem Ziel (Test 1).
- **Strom:** q\_x = (w\_x − u\_x)/2 in ungewrappten lokalen Koordinaten. Da u und w Diagonalnachbarn sind, ist **q\_x = ±½ für jeden Eckschritt, nie 0**. Die Angabe „0, ±½“ im Auftrag passt zu keiner einzelnen Schrittart: Gerade Schritte (u,v,w kollinear) geben q\_x ∈ {0, ±1}. Stufe A schließt gerade Schritte aus ([../stufe_a.md](../stufe_a.md) §3, §6); sie sind als Schalter `--gerade` vorhanden, Standard aus.
- **Berührungsverbot:** Torus-L1-Abstand > 1 für alle vier Endpunktpaare; schließt gleiche Plätze und Nachbarplätze aus, Diagonalnachbarn sind erlaubt. Das ist dieselbe Regel wie in stufe_a.md §2.
- **L ≥ 6 gerade:** Für kleinere L wickeln Sperrzonen um den Torus.

## Parametrisierung

- Bindung = (Anker a, Orientierung o); h: {a, a+e\_x}, v: {a, a+e\_y}.
- Zustand s = (α, r\_x, r\_y, β): Paar 1 mit Anker (0,0), Orientierung α; Paar 2 mit Anker r mod L, Orientierung β. Kodierung ((α L + r\_x) L + r\_y)·2 + β.
- **Markierte Paare.** Jeder physikalische Zwei-Paar-Zustand kommt zweimal vor, als (α, r, β) und (β, −r, α). Diese Wahl ist Absicht: Auf markierten Paaren wirkt die Translationsgruppe frei, der Relativgraph ist der exakte Quotient. Auf ungeordneten Paaren hätte sie Fixpunkte (α = β, 2r ≡ 0). Ein Sprung von Paar 1 wechselt α, einer von Paar 2 wechselt β; verschiedene Sprünge können daher nicht auf dieselbe Kante fallen (Multiplizität 1, Test 2).
- **Umrechnung auf die physikalische Steifigkeit (RK-Punkt):** |C\_voll| = |R| L²/2, Kanten ebenso, ⟨d, Λ⁻¹ d⟩\_voll = E₂ L²/2, also ρ\_s L²/t\_c = ¼⟨deg⟩ − 2 E₂/|R| (Test 6 gegen eine unabhängige Konstruktion auf dem vollen Torus).
- **Mittenabstand** m = Mitte(Paar 2) − Mitte(Paar 1) ∈ (½ℤ)², Minimalbild in [−L/2, L/2). Für Dipol und Bilder wird m benutzt. Für die Fourier-Transformierte braucht man keinen Repräsentanten: Mit k = 2πn/L ist e^{ik·m} wohldefiniert modulo L.
- Generator: (𝓛\_rel f)(s) = Σ\_{s′∼s} [f(s) − f(s′)] mit Multiplizität = Zahl der elementaren Sprünge s → s′.

## Automatische Tests

`python two_pair_graph.py selbsttest` (oder pytest). Alle [A], numerisch verifiziert für L ∈ {6, 8, 10, 12, 16, 24}; kein Beweis für andere L.

| Nr | Test                                    | Prüft                                                                                                                                 |
|----|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 1  | test\_schritte\_aus\_definition         | Schritte aus der Definition gegen eine Handtabelle; Pivot gemeinsam, senkrecht, vier verschiedene Ziele, q\_x = ±½, exakte Inverse     |
| 2  | test\_kanten\_eigenschaften             | Rückkante mit −q\_x für jede Kante, Generator symmetrisch, Multiplizität 1, keine fehlenden Ziele, Berührungsverbot nach jedem Sprung  |
| 3  | test\_paarzahl\_und\_einzelsprung       | In absoluten Koordinaten: zwei verschiedene Paare vorher und nachher, genau eines bewegt                                              |
| 4  | test\_komponentensummen\_und\_symmetrie | Σ\_C d₂ = 0 exakt (ganzzahlig) je Komponente; x-Spiegelung (d ↦ −d), y-Spiegelung, Paartausch sind Graph-Automorphismen               |
| 5  | test\_poisson\_und\_dirichlet           | CG-Residuum < 1e-10, LU-Gegenprobe, Poisson-Energie = Dirichlet-Form                                                                 |
| 6  | test\_voller\_torus                     | unabhängige Konstruktion auf dem vollen L×L-Torus (L = 6, 8, 10): gleiche Kantenmenge nach Quotient, Zählungen, Energie, ρ\_s wie §15 |
| 7  | test\_8x8\_zahlen                       | 6720 Konfigurationen, eine Komponente (stufe_a.md §5)                                                                                 |
| 8  | test\_drift\_lokal                      | Zahl, Radius und Dipol der Drift unabhängig von L; Fernfeld hat vollen Grad                                                           |
| 9  | test\_lokaler\_korrektor                | A d₂ = 0, Grad 7 auf dem Träger, h₂ = d₂/7, E₂ = 4/7, Sektor-Dipole ±4, d̂₂ über alle Sektoren null                                    |

## Was bewiesen ist [B]

1. **Komponentensummen.** Σ\_{s∈C} d₂(s) = Σ über die gerichteten Kanten in C von q\_x. Jede Kante s → s′ hat eine Rückkante s′ → s in derselben Komponente mit −q\_x (der Eckschritt ist umkehrbar, und das Ziel der Rückkante ist s selbst, also zulässig). Die Summe ist 0, für jede Komponente und jedes L.
2. **Endlicher Träger der Drift.** Jedes Paar hat vier Schritte mit q\_x = +½, +½, −½, −½, also ist d₂ = −Σ q\_x über die *gesperrten* Schritte. Ein Schritt ist nur gesperrt, wenn das andere Paar in seiner Sperrzone liegt (endliche Reichweite). Also ist d₂ = 0, sobald die Paare weit genug getrennt sind.
3. **Symmetrien und Sektorsumme.** x-Spiegelung (m\_x ↦ −m\_x, d ↦ −d), y-Spiegelung (d ↦ d) und Paartausch ((α, m, β) ↦ (β, −m, α), d ↦ d) sind Automorphismen des Graphen. Zusammengesetzt folgt d(β, m, α) = −d(α, m, β). Also verschwindet d₂ in den Sektoren (h,h), (v,v), und die Summe über die Sektoren ist für jedes m null. Damit ist d̂₂(k) ≡ 0 für alle k, nicht nur O(|k|).
4. **Poisson-Energie = Dirichlet-Form:** algebraisch, ⟨d, h⟩ = ⟨h, 𝓛 h⟩ = Σ\_{Kanten} (h(s) − h(s′))², sobald 𝓛 h = d.

**[S, computergestützt]: 𝓛\_rel d₂ = 7 d₂ auf ℤ² und für alle L ≥ 12.** Die Identität A d₂ = 0 (A = Adjazenz) und Grad 7 auf dem Träger betreffen nur Zustände mit |m|∞ ≤ 3,5 und deren Nachbarn. Für L ≥ 12 ist dort der Torusabstand der Endpunkte gleich dem ebenen Abstand. Die Nachbarschaftsstruktur ist also dieselbe wie auf ℤ², und die exakte, ganzzahlige Prüfung auf einem L ≥ 12 beweist die Identität für alle diese L und für ℤ². L = 6, 8, 10 sind zusätzlich direkt geprüft. Folge: h₂ = d₂/7, E₂ = |d₂|²/7 = 16·¼/7 = 4/7.

## Ergebnisse

Produktionslauf ([ergebnisse/zweipaar.csv](ergebnisse/zweipaar.csv)), Einheiten t\_c = 1, sechs Prozesse parallel, gesamt 2,0 s:

| L  | Zustände | Komp. | Übergänge | d₂ ≠ 0 | max Σ\_C | E₂         | CG-It. | ρ\_s L²    | ¼⟨deg⟩     |
|----|----------|-------|-----------|--------|----------|------------|--------|------------|------------|
| 16 | 978      | 1     | 7 744     | 16     | 0        | 0,57142857 | 1      | 1,97838154 | 1,97955010 |
| 24 | 2 258    | 1     | 17 984    | 16     | 0        | 0,57142857 | 1      | 1,99063647 | 1,99114260 |
| 32 | 4 050    | 1     | 32 320    | 16     | 0        | 0,57142857 | 1      | 1,99477954 | 1,99506173 |
| 48 | 9 170    | 1     | 73 280    | 16     | 0        | 0,57142857 | 1      | 1,99769434 | 1,99781897 |
| 64 | 16 338   | 1     | 130 624   | 16     | 0        | 0,57142857 | 1      | 1,99870591 | 1,99877586 |
| 96 | 36 818   | 1     | 294 464   | 16     | 0        | 0,57142857 | 1      | 1,99942575 | 1,99945679 |

In allen Läufen: fehlende Zielzustände 0, Asymmetrie 0, Multiplizität 1, Poisson gegen Dirichlet 5·10⁻¹⁵ relativ, CG-Residuum < 10⁻¹⁵, LU-Gegenprobe ≤ 3·10⁻¹⁵, Radius von Drift und Blockaden 2,5 (in |m|∞), außerhalb davon voller Grad 8.

Bilder in [ergebnisse/](ergebnisse/):

- `E2_gegen_L.png` und `E2_gegen_logL.png`: konstant.
- `E2_konvergenz.png`: relative Abweichung von E₂(96) auf Maschinengenauigkeit.
- `fourier_d2.png`: Sektor (h,v) längs e\_x wie |p\_x||k| mit p\_x = 4, längs e\_y exakt 0 (d ist ungerade in m\_x und hebt sich bei festem m\_y weg); Summe aller Sektoren auf Rundungsniveau.
- `drift_nahbereich.png`: d₂ in den vier Sektoren.
- `korrektor_nahbereich.png`: h₂ = d₂/7.
- `grad_komponenten_nahbereich.png`: Zahl erlaubter Sprünge im Nahbereich; eine einzige Komponente für alle L.

**Gerade Schritte (`--gerade`, nicht Stufe A)** [A]: E₂ = 1,451361 für L = 16, 32, 64, CG 16 Iterationen, Korrektor mit endlichem Träger (680 Zustände, Radius 10,5, ab L = 32 unverändert). Auch dort ist der Zwei-Paar-Korrektor exakt lokal, aber kein einfacher Eigenvektor.

## Laufzeit und Speicher (gemessen, i9, 24 Threads)

| L    | Zustände  | Übergänge  | Graph  | Komponenten | Poisson | Spitzen-RSS |
|------|-----------|------------|--------|-------------|---------|-------------|
| 96   | 36 818    | 294 464    | 0,05 s | 0,002 s     | 0,6 s   | 0,19 GB     |
| 256  | 262 098   | 2 096 704  | 0,9 s  | 0,06 s      | 0,10 s  | 0,31 GB     |
| 512  | 1 048 530 | 8 388 160  | 3,0 s  | 0,13 s      | 0,21 s  | 1,0 GB      |
| 1024 | 4 194 258 | 33 553 984 | 8,2 s  | 0,30 s      | 0,38 s  | 3,6 GB      |

- Bei L = 96 steckt die Poisson-Zeit in der LU-Gegenprobe (`--lu-max`); der erweiterte Lauf hat sie abgeschaltet.
- Komplexität: |R| ≈ 4L², Übergänge ≈ 8|R|, Graphaufbau und Komponenten O(L²). Bei d₂ als Eigenvektor genügt eine CG-Iteration, also O(L²). Für eine allgemeine Quelle braucht Jacobi-CG O(L) Iterationen (Konditionszahl ~ L²), also O(L³).
- Speicher ≈ 3,5 kB je Zustand, vor allem int64-Kantenarrays und die COO → CSR-Umwandlung. Mit 32 GB RAM also etwa 9·10⁶ Zustände, L ≈ 1500 in einem Prozess. Das ist extrapoliert, nicht gemessen; parallele Prozesse teilen sich den Speicher.

## Interpretation

- **Stützt die Zwei-Paar-Hypothese** (die Zwei-Paar-Quelle ist neutral, ihre H⁻¹-Energie bleibt beschränkt, der Korrektor ist lokal): ja, in der stärksten Form. Die Energie ist exakt L-unabhängig, der Korrektor h₂ = d₂/7 hat denselben endlichen Träger wie die Quelle, und die Quelle koppelt gar nicht an die langsame, sektorsymmetrische Mode (d̂₂ ≡ 0 nach Sektorsumme).
- **Widerlegt hätten sie:** wachsendes E₂(L), etwa ~log L (eine Monopolquelle in einer Komponente, nach [B] 1 ausgeschlossen); ein nichtverschwindender Gesamtdipol mit Fernfeldanteil; Komponenten, die den Nahbereich zerlegen. Nichts davon tritt auf.
- **Physikalisch:** Für zwei Paare ist der paramagnetische Abzug von der Steifigkeit exakt (8/7)/|R|, also O(L⁻²) bei fester Paarzahl. Das ist der Zwei-Körper-Anteil des Abzugs K − σ\_∞ im Vielteilchensystem, mit genau lokalisiertem Korrektor. Bei drei und mehr Paaren entstehen nach [../stufe_a.md](../stufe_a.md) §15 Reste, die nicht mehr in diesem Sinn exakt lokal sein müssen; dafür wäre das Programm auf drei Paare zu erweitern (Zustände ~ L⁴, für L ≤ 48 machbar).
- **Was die Zahlen nicht beweisen:** Aussagen über das Vielteilchensystem bei 7/8-Füllung oder über den thermodynamischen Limes mit endlicher Dichte. Bewiesen ist nur die Zwei-Paar-Aussage, für ℤ² und alle L ≥ 12, über die lokale Identität oben.

## 7/8-Füllung (2026-11-08)

Frage: Wie viel des Vielteilchen-Abzugs K − σ erklärt die Summe der exakten Zwei-Paar-Korrektoren f₂ = Σ\_{p<q} h₂(rel(p,q)) = d⁽²⁾/7, ohne Fitparameter? Dabei ist d⁽²⁾(D) = Σ\_{p<q} d₂(rel(p,q)) der Zweikörperanteil der Drift und R = d − d⁽²⁾ der Mehrkörperrest (Doppelblockaden).

### Exakt: 8×8-Torus, voller Konfigurationsgraph

[siebenachtel_8x8.py](siebenachtel_8x8.py) (pyamg-vorkonditioniertes CG, Ergebnisse [ergebnisse/siebenachtel_8x8.json](ergebnisse/siebenachtel_8x8.json)). P = 4 ist 7/8-Füllung; 8×8 ist die einzige 7/8-Torusgröße, die vollständig aufzählbar ist (12×12 hätte 9 Paare). Einheiten ρ\_s L²/t\_c, RK-Punkt.

| P | Konfigurationen | Komponenten     | ρ\_s L² (§15)     | ¼⟨deg⟩  | Abzug   | R ≠ 0   | f₂, λ = 1 | f₂, λ\*        | cos(f₂, h) |
|---|-----------------|-----------------|-------------------|---------|---------|---------|-----------|----------------|------------|
| 2 | 6 720           | 1               | 1,89932 (1,8993)  | 1,90476 | 0,00544 | 0       | 100,0 %   | 100,0 % (1,000) | 1,0000     |
| 3 | 188 288         | 1               | 2,68166 (2,6817)  | 2,69952 | 0,01786 | 0,34 %  | 94,3 %    | 94,4 % (1,033)  | 0,9716     |
| 4 | 3 075 264       | 33 (32 Säulen)  | 3,32796 (3,3279)  | 3,36712 | 0,03916 | 1,55 %  | 88,0 %    | 88,4 % (1,072)  | 0,9404     |

- „f₂, λ = 1“: Anteil des Abzugs, den der Paarsummen-Korrektor im Leitwertfunktional Q(f) = |C|⁻¹ Σ\_{D→D′} (Δx + f(D′) − f(D))² schließt; „λ\*“: mit optimaler Amplitude. cos: Winkel zum exakten Korrektor h in der Dirichlet-Metrik.
- Quellenenergien bei P = 4: ⟨d⁽²⁾, Λ⁻¹d⁽²⁾⟩ = 58 077, Rest 4 452, Kreuzterm −1 156, Summe 60 217 = E. Der Mehrkörperrest sitzt auf 1,55 % der Konfigurationen und trägt rund 7 % der Quellenenergie.
- Prüfungen: Komponentensummen exakt 0, Poisson gegen Dirichlet gleich, AMG-CG 9 Iterationen (Residuum ≤ 9·10⁻¹¹), alle ρ\_s-Werte wie die vollständige Aufzählung in §15. Laufzeit P = 4: 89 s, Spitzen-RSS 9,9 GB.

### Volumen: Torus L = 32 … 128, Monte Carlo

[siebenachtel_volumen.py](siebenachtel_volumen.py), Ergebnisse `ergebnisse/siebenachtel_volumen_L*.json`. Gleichgewichtsstichproben bei ρ\_b = 1/32 (Sampler und Akkumulation aus [../beweis_box/korrektor.py](../beweis_box/korrektor.py)). σ(F) = L⁻² E Σ\_m (Δx\_m + ∇\_m Φ\_F)². Der exakte Zwei-Paar-Korrektor ist in deren Motivbasis a = −1/14 bei (½, 2½) und +1/14 bei (2½, ½), sonst 0; das ist kein Fit. Abzug relativ zu σ\_∞ = 0,04971 (Green-Kubo, L = 64–256). Fehler aus 20 Blockmitteln. Jeder Wert σ(F) ist eine obere Schranke für σ\_∞ (Variationsprinzip), bis auf den Stichprobenfehler.

| L   | Proben | K                 | σ(a₂)             | λ\*           | K − σ(a₂)              | Anteil a₂     | Anteil λ\* a₂ | freie Zweikörpermotive (r ≤ 3) |
|-----|--------|-------------------|-------------------|---------------|------------------------|---------------|---------------|--------------------------------|
| 32  | 40 000 | 0,05063 ± 0,00001 | 0,05001 ± 0,00001 | 1,112 ± 0,003 | 0,000620 ± 0,000003    | 67,6 ± 1,2 %  | 68,3 ± 1,2 %  | 68,5 ± 1,2 %                   |
| 64  | 40 000 | 0,05053 ± 0,00001 | 0,04990 ± 0,00001 | 1,113 ± 0,001 | 0,000623 ± 0,000002    | 76,2 ± 1,1 %  | 77,0 ± 1,2 %  | 77,3 ± 1,2 %                   |
| 128 | 20 000 | 0,05051 ± 0,00000 | 0,04988 ± 0,00001 | 1,115 ± 0,002 | 0,000625 ± 0,000002    | 78,5 ± 1,1 %  | 79,4 ± 1,1 %  | 79,7 ± 1,1 %                   |

- Der geschlossene Betrag K − σ(a₂) ist von L unabhängig (0,000620–0,000625). Der Anteil steigt nur, weil K(L) im Nenner gegen den Volumenwert fällt; σ\_∞ stammt aus L ≥ 64. Bester Wert für das Volumen: **etwa 78 % des Abzugs aus dem exakten Zwei-Paar-Korrektor**.
- Freies Anpassen aller Zweikörpermotive bringt nur gut 1 Prozentpunkt mehr: Der exakte Zwei-Paar-Korrektor ist praktisch der optimale Zweikörperkorrektor auch bei 7/8. Optimale Amplitude λ\* ≈ 1,11, also etwa 11 % Verstärkung durch die Umgebung.
- Der Rest (≈ 21 %) ist Mehrkörperanteil; kompakte Dreikörpermotive heben die Schließung auf 92 % ([../beweis_box/korrektor3.py](../beweis_box/korrektor3.py)).
- Als Formel: σ ≈ K − (Zwei-Paar-Abzug) gibt σ = 0,04988 gegen σ\_∞ = 0,04971, also s = σ/K auf 0,3 % genau (0,9875 gegen 0,9844).
- Exakter 8×8-Fall (88 %) und Volumen (78 %) unterscheiden sich: Auf 8×8 gibt es nur 4 Paare, Mehrkörperlagen sind dort seltener.

Bewertung: [N]. Die Zwei-Paar-Identität 𝓛 d₂ = 7 d₂ ist bewiesen (oben); dass ihr Korrektor bei 7/8 rund vier Fünftel des Abzugs trägt, ist ein numerischer Befund, kein Satz.

## Dyson-Lieb-Simon-Kette mit exakter Suszeptibilität (2026-11-09)

[falk_bruch.py](falk_bruch.py) (Stufe A und harte Bosonen), [falk_bruch_8x8.py](falk_bruch_8x8.py) (erste Fassung, Stufe A). Ordnungsparameter A\_k = Paar- bzw. Bosonvernichter mit Impuls k, großkanonisch H − μN mit μ in der Mitte des Intervalls (E₀(N)−E₀(N−1), E₀(N+1)−E₀(N)). Exakt je k: g\_k = ½(⟨A†A⟩ + ⟨AA†⟩), Doppelkommutator c\_k, statische Suszeptibilität χ\_k (Gleichungslöser in den Sektoren N±1). Kette: Falk–Bruch g\_k ≤ ½√(c\_k χ\_k) und Summenregel Σ\_k g\_k = (N + Φ)/2, Φ = Zahl freier Plätze, also g₀ ≥ (N+Φ)/2 − Σ\_{k≠0} ½√(c\_k χ\_k). Das ist das Gerüst von Dyson–Lieb–Simon / Kennedy–Lieb–Shastry, mit dem exakten χ statt der Infrarotschranke, also der beste Fall [N].

| Modell                    | Gitter | N | Dichte je Objekt | n₀/N  | Spielraum je Mode | Kette garantiert von g₀ |
|---------------------------|--------|---|------------------|-------|-------------------|-------------------------|
| harte Bosonen             | 4×4    | 2 | 0,125            | 0,923 | 1,019             | 95 %                    |
| harte Bosonen             | 4×4    | 4 | 0,25             | 0,782 | 1,020             | 97 %                    |
| harte Bosonen             | 4×4    | 8 | 0,5              | 0,531 | 1,008             | 99 %                    |
| harte Bosonen             | 6×6    | 2 | 0,056            | 0,956 | 1,019             | 87 %                    |
| harte Bosonen             | 6×6    | 4 | 0,111            | 0,878 | 1,028             | 90 %                    |
| harte Bosonen             | 8×8    | 2 | 0,031            | 0,968 | 1,016             | 81 %                    |
| harte Bosonen             | 8×8    | 3 | 0,047            | –     | 1,021             | 82 %                    |
| Stufe A (x ≈ 9,4 %)       | 8×8    | 3 | 0,023            | 0,561 | 1,056             | **−2 %** (nichts)       |

- Der Spielraum je Mode ist klein (Cauchy–Schwarz fast scharf), wird aber über alle k ≠ 0 summiert, und die Summenregel enthält die Zahl freier Plätze Φ (Teilchen-hinzufügen-Seite), die mit dem Volumen wächst. Die Kette trägt nur, wenn Kondensat × Dichte deutlich größer ist als (Spielraum − 1) × (N + Φ)/2M.
- Harte Bosonen: Mit exaktem χ trägt die Kette auf allen gerechneten Gittern und Dichten (81–99 %). Fehlende Zutat ist dort allein eine Schranke für χ(k), die Infrarotschranke; sie kommt aus der Reflexionspositivität.
- Stufe A: Schon bei 3 Paaren auf 8×8 garantiert die Kette nichts, obwohl χ exakt ist: Spielraum je Mode 5,6 % (schlechteste Mode 0,67), kleines Kondensat × Dichte. Bei 7/8 und größerem L nur schlechter. **Der Weg über Falk–Bruch und Summenregel ist für Stufe A ausgeschlossen**, unabhängig davon, wie gut man χ kennt.

### Infrarotschranke abseits halber Füllung, harte Bosonen (2026-11-09)

[falk_bruch.py](falk_bruch.py) (prüft zusätzlich χ(k)·E(k) ≤ 1, E(k) = 4 − 2cos k\_x − 2cos k\_y, J = 1; aus der Gaußschen Dominanz von Dyson–Lieb–Simon mit S^x\_k = (b\_k + b\_{−k}†)/2 hergeleitet), [ir_integral.py](ir_integral.py) (Kette im unendlichen Volumen). [N]

1. **Infrarotschranke gilt numerisch bei allen Dichten**, auch wo die Reflexionspositivität sie nicht liefert (Feld ≠ 0: In der reellen (S¹, S³)-Darstellung koppelt μ an das imaginäre S², die Spiegelung kehrt sein Vorzeichen auf einer Hälfte um). Maximum von χ·E: halbe Füllung 0,42 (4×4); kleine Dichte 0,92 / 0,96 / 0,98 (ein Teilchen auf 4×4 / 6×6 / 8×8). Nie verletzt (4×4 alle N, 6×6 N ≤ 4, 8×8 N ≤ 3).
2. **Die Kette Falk–Bruch + Summenregel + Infrarotschranke scheitert im unendlichen Volumen trotzdem.** Exakt gilt c(k) = 8⟨b†b⟩\_nn − 8⟨(n−½)(n−½)⟩\_nn (cos k\_x + cos k\_y) + μ(2ρ − 1) (Residuum der Anpassung ≤ 5·10⁻¹³); damit g₀/M ≥ ½ − ½∫d²k/(2π)² √(c/E).

| Korrelationen aus | ρ    | 0,028  | 0,056  | 0,0625 | 0,083  | 0,111  | 0,125  | 0,25   | 0,375  | 0,4375 | 0,5     |
|-------------------|------|--------|--------|--------|--------|--------|--------|--------|--------|--------|---------|
| 4×4               |      |        |        | −0,039 |        |        | −0,038 | −0,024 | −0,007 | −0,002 | +0,0002 |
| 6×6               |      | −0,023 | −0,029 |        | −0,031 | −0,031 |        |        |        |        |         |

(μ in der Intervallmitte; am oberen Ende wenig besser.) Für ρ → 0 wird c = E, Integral 1, Schranke 0. Die Kette ist für 2D-harte Bosonen grundsätzlich auf der Kippe: bei halber Füllung knapp positiv (dort brauchten Kennedy–Lieb–Shastry zusätzliche Abschätzungen), sonst negativ. Endliche Gitter täuschen positive Werte vor: Der Integrand wächst wie 1/|k| bei k → 0, die Summe ohne k = 0 unterschätzt das um O(1/L).

**Folgerung:** Abseits halber Füllung fehlt nicht nur die Reflexionspositivität. Selbst mit Infrarotschranke trägt die Standardkette nicht; nötig wäre eine schärfere Ungleichung als Falk–Bruch mit Summenregel.
