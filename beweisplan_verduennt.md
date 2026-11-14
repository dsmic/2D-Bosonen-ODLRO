# Beweisplan: Kondensat für verdünnte harte Bosonen in 2D bei T = 0

> **Überholt (Vermerk 2026-11-13, Review H1).** Dieser Plan beschreibt den zeitartigen Staffellauf mit Lücke, Gegen-Lücke und Δ₂. Er ist seit Anhang G, G.10, durch die Zeitschleife ersetzt. Gültig ist die Zeitschleife: [tutorial\_beweis\_verduennt.md](tutorial_beweis_verduennt.md) §10, [anhang\_gegenluecke.md](anhang_gegenluecke.md) G.10 bis G.12, [anhang\_zweites\_moment.md](anhang_zweites_moment.md) (Anhang Z, Stand der Beweiskette in Z.12 und Z.13) und [anhang\_buchfuehrung.md](anhang_buchfuehrung.md) (Anhang M).

Stand 2026-11-10. Zusammenfassung von [einpunkt\_zeitroute.md](einpunkt_zeitroute.md) §1–§17, dort mit allen Herleitungen. Kennzeichnung: [S] streng, [Lit] Literatur, [B] Beweisskizze, [N] numerisch, [L] Lücke.

## Ziel

**Satz (angestrebt).** Harte Bosonen auf (ℤ/Lℤ)², H = −Σ\_{⟨xy⟩}(b\_x⁺b\_y + h.c.). Es gibt ρ\* > 0 und c > 0, sodass für 0 < ρ < ρ\* und für 1 − ρ < ρ\* der Grundzustand mit N = ρL² Teilchen N₀/N ≥ c erfüllt, gleichmäßig in L ≥ L₀(ρ) (genauer Geltungsbereich: Tutorial §0.1, Fassung vom 2026-11-12). Insbesondere hat er ODLRO.

- **Teilchen-Loch [S]:** b ↔ b⁺ lässt H unverändert, und für x ≠ y ist ⟨b\_x⁺b\_y⟩ gleich der entsprechenden Lochkorrelation. Der Fall 1 − ρ < ρ\* folgt also aus dem Fall ρ < ρ\*.
- **Reichweite:** ρ\* ist nach heutigem Stand astronomisch klein (log(1/ρ\*) von der Ordnung 10²). Es ist ein Existenzsatz. Mittlere Dichten und Stufe A bei 7/8 sind nicht erfasst.

## Die Idee in Bildern

1. **Ein Punkt statt zwei.** Man nimmt bei x ein Teilchen heraus und fragt, ob der Rest wie der Grundzustand mit einem Teilchen weniger aussieht. Wenn ja, ist Kondensat da.
2. **Die Frage wird zur Lücke in Raum-Zeit.** In Weltlinien fehlt ein Stück Linie, eine Lücke. Sie darf beliebig lang sein, denn G(τ) fällt monoton. Man muss zeigen: Eine lange Lücke kostet nur O(1).
3. **Staffellauf in der Zeit.** Die Lücke wird Scheibe für Scheibe durch Raum-Zeit getragen. Je Scheibe wird ein Linienstück gelöscht, und wenige Nachbarstücke werden neu gezogen, sodass das Loch eine Zelle weiterrückt.
4. **Zufällige Routen, zweites Moment.** Längs einer festen Route würden sich die Kosten multiplizieren. Mittelt man über zufällige Routen, bleiben nur Kosten dort, wo sich zwei unabhängige Routen begegnen.
5. **Zwei Querrichtungen.** In Raum-Zeit ℤ² × ℤ ≅ ℤ³ hat eine zeitartige Route zwei räumliche Querrichtungen. Benjamini–Pemantle–Peres: Dann begegnen sich zwei Routen nur endlich oft. In 1D (ℤ²) nicht, deshalb kein Kondensat dort.
6. **Gegen-Lücke als Bezug.** Damit sich die teilchenzahländernden Kosten fern von Begegnungen exakt wegheben, vergleicht man mit einer zusätzlichen Linie längs der zweiten Route.
7. **Verdünnung macht Begegnungen billig.** In 2D nur logarithmisch: Der kleine Parameter ist 1/ln(1/ρ), die effektive Kopplung des 2D-Bose-Gases.

## Aufbau und Abhängigkeiten

```text
                       Satz: N₀/N ≥ c für ρ < ρ*
                                   ▲
              Schritt 1: N₀/N ≥ G⁻(T)/N ≥ H̄²   (Einpunkt + Monotonie)
                                   ▲
       Schritt 2: G⁻(T) ≥ a² / E[e^{C·J}]   (Lemma 8.1, Staffellauf, Gegen-Lücke)
          ▲                 ▲                    ▲                    ▲
   Routen/Budget       Kosten je Begegnung   Buchführung L3      Umwege L4
   (BPP, α_max)        C/λ² + C log λ/ln(1/ρ)       │            (Timár, Raum-Zeit-
                            ▲          ▲            │             Peierls)
                         L2 Stöße   L1 Dichte ──────┴───────────────┘
                                     ▲
                    L1a Kippen · L1b Lokalisierung · L1c Zelle · L1d Einfügen
```

## Schritte und Lemmata

| Nr. | Aussage | Stand | Ort |
|-----|---------|-------|-----|
| 0 | Weltlinienmaß: Gewicht 1 je Sprung; Markov-Eigenschaft in Raum-Zeit; H + 4N = Σ L\_i mit Dirichlet auf der Stoßmenge | [S] | §13.1, §16 |
| 1a | N₀/N ≥ H̄², H̄ = Affinität(Faser bei x, ψ\_{N−1}²); punktweise ρ₁/ρ ≥ 2H̄² − 1 | [S] | §1 |
| 1b | G⁻(τ) vollständig monoton: N₀ ≥ G⁻(τ) ↓ N H̄² | [S] | §3 |
| 2a | Lemma 8.1 (Preprint): gemeinsames Maß ν, H ≥ m²/√(C\_P C\_Q) | [Lit] | Preprint |
| 2b | Zeitartiger Staffellauf auf dem Gitter: Loch-Träger löschen, Sternpfad zyklisch neu ziehen, exakt normiert | [B] | §13 |
| 2c | Gegen-Lücke als Bezug: fern von Begegnungen exakte Aufhebung; globaler Restfaktor e^{−Δ₂T} günstig; a² ≤ G⁻G⁺ E[e^{CJ}] | [B] | §10 |
| 3 | Skelette in ℤ³ (BPP, Häggström–Mossel), steil (Drift D ≈ 0), A ≈ 16, β = ¼: Budget α\_max ≈ 0,046 je Zellpaar | [Lit] + [N] | §11, §14 |
| L1a | Kippidentität ⟨gψ, Hgψ⟩ − E₀⟨g²⟩ = Σ ψψ′(g − g′)²; Kippschranke C λ² s^{−2} E\_g n\_φ | [S] | §16, §16.5 |
| L1b | Lokalisierung mit zwei Farben auf dem Gitter, Fehler Σ ΦΦ′(1 − cos Δθ) | [S] | §16.5 |
| L1c | Zellenschranke λ\_min(b, y) ≥ π/(2b² ln b) für b ≥ 4 (Poincaré + Thomson); n Teilchen im Kasten ≥ (π/(2b² ln b)) n 1{n ≥ 2} (ohne Paarung, Fassung 2) | [S] (b ≤ 512 exakt, sonst Standard-Asymptotik) | §16.5 |
| L1d | Einfügen: E\_k − E\_{k−1} + 4 ≤ 2ρ′D(f)/(1 − ρ′S(f)) (Dyson, nächster Nachbar), asymptotisch ≤ 8πρ/ln(1/ρa²)·(1 + o(1)), auch mit anziehendem Potential | [S] | §16.4 |
| L1 | Obere Schwänze log E e^{λn\_U} ≤ Cλρ|U|; untere Schwänze ≤ Ce^{−cmu}; Isolation | Zutaten [S] (u. a. ε\_j/j nichtfallend), Zusammensetzen [B] | §16.5, §16.6 |
| L2 | Kreuzfaktor je Zellpaar ≤ 1 + κ₂ w(d)(1/m\_e + P\_δ) mit weichen Gewichten w; Bedingung κ₂(1/m\_e + P\_δ) < α\_max^{weich} ≈ 0,07 | [B], Teile [S] | §15, §20 |
| L3 | Buchführung der Gegen-Lücke mit Sternpfaden, Auswahl- und Wählbarkeitsgewichten (wie §10 des Preprints) | [B] | §10, §13 |
| L4 | Umwege: Timár in ℤ³ [Lit]; Raum-Zeit-Peierls über log E e^{∫W} ≤ ∫[E₀(H) − E₀(H − W\_t)] [S] plus L1 mit Potential [B]; geteilte Umwege kosten kein Budget [N] | gemischt | §17 |

## Reihenfolge der Konstanten

1. Skelett: β = ¼, Skala A ≈ 16, Drift D ≤ 0,02, Begegnungsradius R = 1 ⇒ Budget α\_max ≈ 0,046 (gleichmäßig in der Länge).
2. Zellgeometrie: Zellseite s = λ ρ^{−1/2} mit λ² ≳ ln(1/ρ) (genug Teilchen je Zelle, L1), Scheibendauer δ = κ/ρ mit κ ~ 1.
3. Ballungsparameter H ≈ 17–25 (L1, aus L1c gegen L1d; vorher 50 mit Paarung), Lokalisierungsbreite K, Isolationsskala ζ.
4. Wählbarkeit: Schwellen b₋, b₊, Score-Schranken; Peierls-Parameter q klein.
5. Dichteschwelle: Kosten je Zellpaar ≈ C₁/λ² + C₂ log λ/ln(1/ρ) < α\_max ⇒ ln(1/ρ\*) ≳ C₂ log λ/α\_max. Mit weichen Kosten (α\_max bis ≈ 0,07–0,09, §19) grob ρ\* ≲ 4·10⁻⁷ vor weiteren Faktoren.

## Numerische Belege

| Aussage | Befund | Ort |
|---------|--------|-----|
| Einpunkt-Kriterium fast scharf | Z₀ = N H̄²/N₀ ≈ 0,999 in 2D (L = 4, 5, 6); 1D: H̄² ~ L^{−1/2} | §2 |
| Kondensat bei kleinem ρ | n₀ ≈ 0,75 (ρ = 1/16), 0,72 (1/8); n\_k ∝ 1/k; χE ≈ Josephson | README, Runde 1 |
| Dimensionszählung | Begegnungen beschränkt mit 2 Querrichtungen, wachsend wie w^{1/4} bzw. w^{1/2} mit einer | §11 |
| Budget und Drift | α\_max 0,046 (D = 0) bis 0,004 (D = 0,5) | §14 |
| L1c | min\_y λ · b² ln b = 1,66 (b = 128) → π/2; Schranke 4 % darunter | §16.5 |
| L1d | strenge Schranke 1,16–1,79 × Lieb–Yngvason; Born 1,76–6,9 × (wachsend) | §16.4 |
| μ aus dem Wurm | 1,21–1,26 × Lieb–Yngvason führend (passt zur 2. Ordnung) | §16.1 |
| Umwege | geteilte Umwege, auch zeitlich persistente, ändern α\_max nicht | §17 |
| Budget-Hebel | weiche Abstandsgewichte +30 % (α\_max 0,064); Schwanz kommt von klebrigen Wiederbegegnungen im Inneren, Budget dieser Routenfamilie ≈ 0,05–0,09 | §19 |
| Kurzzeit-Rauschen | b₀ = 0 (kein Rauschen auf Stufe 0) am besten: α\_max 0,071 ganz, ≈ 0,11 innen; mehr Rauschen verschlechtert (2D marginal) | §19.1 |
| κ₂ (Umgebung) | κ\_Umgebung ≈ 1,0–1,15: Bedingen auf Ausweichen verstärkt die Kreuzkosten kaum; P(ausweichen) ≈ e^{−2πm/ln 2δ} winzig, Worst-Case-Faktor 1/p\*² wäre katastrophal | §21 |
| Doob-Verhältnis (scharfes L2) | κ\_L = E[r₁r₂] exakt 1,2–2,4 statt 1/Z² bis 10¹²; ln κ ≈ 0,27 m/ln s, also κ₂ ≈ e^{0,54K}; Schwelle ln(1/ρ\*) ≈ e^{0,54K}·C′/α\_max (K = 3: ~90) | §22 |
| Rückführung auf ein Stück | Cauchy–Schwarz κ\_L ≤ √(E\_w r₁² E\_w r₂²) nur 0–8 % über κ\_L; Poisson-Formel: annealed Verhältnis = exp(ν V₂), V₂ gemeinsames Fangvolumen | §23 |
| quenched-Momente | ln κ\_q nicht linear in der Teilchenzahl, aber leichte Schwänze: ln E κ^q/q = 0,31…0,39 (m = 2), 0,82…1,00 (m = 8); Ziel: Momentform E κ\_q^p ≤ exp(p c(p) m/ln s) | §24 |
| Lokalisierung und Produkt | Fallen jenseits ~√δ irrelevant; ln κ ≈ Σ\_j ln κ(Falle j) im Mittel (Differenz −0,03 … −0,10), pfadweise Ausreißer bis +0,8 → Campbell plus Paarfehler | §25 |
| Eine Falle (Campbell) | Φ = ln E Π κ(γ\_j) über Fangvolumina; grob Φ ≤ C(ζ) m/ln δ (V₂ ≤ V₁, 2D-Würstchen); numerisch Φ ≈ 0,5 m/ln s ≈ K | §26 |
| Paarfehler D | D ≈ Paarsumme (Korrelation 0,85–0,88), Einzelpaare |u₂| ≤ 0,1, Streuung ≈ 0,15; Beweisweg: Poisson-Konzentration (Wu; Bachmann–Peccati) mit kleinen Hinzufüge-Kosten | §27 |
| Konstante K (§28) | untere Schwänze treiben K auf ~10³ (Energie-Untergrenze π/16 zu schwach); exakt e\_b(2) → 4π/(b² ln b) (bis b = 24); linear streng c₁ → π (K/16), mit Gitter-Dyson-Lemma 4π (K ~ 15–30); für vernünftige Schwelle zusätzlich Skalen entkoppeln | §28 |
| Diskretes Dyson-Lemma | Σ(∇f)² ≥ Σ U f², Gewicht 1/R\_eff ≈ 2π/ln(R/a), Beweis über Stromzerlegung, keine Sternförmigkeit nötig [S]; R\_eff numerisch auf 0,04–2 %; Weg zu E/N ≥ 4πρ/ln(1/ρa²)(1 − o(1)) nach Lieb–Yngvason [B] | §29 |
| Gitter-Lieb–Yngvason | ε\_N/N ≥ 4πρY(1 − CY^{1/5}): Dyson für viele Teilchen in beliebigen Nachbarzellen (Strom), Neumann-Kästen mit Temple, Verteilung über Konvexität; mit L1d asymptotisch scharf | §30 |
| L2 Treffen | P ≈ 0,66/(ln r + 2,1) bei κ = 1 (exakter Bessel-Kern), also C(κ)/ln(1/ρ) mit langsamer Konvergenz | §18 |

## Offene Punkte nach Priorität

0. **Zentraler offener Punkt (§21.1, §22, §28): 2D-Spannung zwischen den Skalen; analytischer Kern ist eine scharfe Gitter-Untergrenze E/N ≥ 4πρ/ln(1/ρa²)(1 − o(1)) (Gitter-Dyson-Lemma).** Mit scharfem L2 (numerisch κ₂ ≈ e^{0,54K} statt e^{4πK}) bleibt sie eine feste Konstante; zu beweisen ist E\_w[r₁r₂] ≤ exp(Σ\_j c/ln δ). Die Schwelle hängt dann vor allem an der L1-Konstante K. Beweisweg (§23): annealed Poisson-Formel exp(ν V₂) mit gemeinsamem Fangvolumen V₂, dann Vergleich Poisson gegen Grundzustand über L1.
1. **L2 scharf (§21):** Kreuzkosten exakt bedingter Stücke ≤ (1 + o(1)) × frei, ohne Faktor 1/p\*² (Korrelationsungleichung oder Doob-Vergleich); sonst nur doppelt exponentiell kleines ρ\*. Außerdem **L2 streng:** 2D-Treffwahrscheinlichkeiten für Brücken und bewegte Ziele mit expliziten Konstanten; Score-Schranken. Das ist der einzige Ort des kleinen Parameters.
2. **L1 zusammensetzen** (obere und untere Schwänze, Isolation) mit allen Konstanten ausschreiben; dazu L1 mit anziehendem Potential für L4.
3. **L3 Buchführung** vollständig, analog §9–§10 des Preprints: Annahme, Auswahl, Normierer, Kreuzterme.
4. **Umwege:** volle 3D-Außenrand-Umwege, nicht nur scheibenweise; Verwerfung großer Komponenten.
5. **Budget vergrößern:** bessere Skelette oder bessere Zählung, um ρ\* in einen weniger absurden Bereich zu bringen.
6. **Numerisch offen:** Z₀ bei L = 16, 32 aus G(τ) (Läufe bis 2026-11-10 21:45).
