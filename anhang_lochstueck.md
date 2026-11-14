# Anhang L: Das Lochstück j₀ (Wählbarkeit über zwei Scheiben)

Stand 2026-11-12. Antwort auf Befund K3 in [review\_2026-11-11.md](review_2026-11-11.md). Gehört zu [anhang\_gegenluecke.md](anhang_gegenluecke.md) G.5.1, G.12.1 und G.12.5–G.12.7, zu [anhang\_zweites\_moment.md](anhang_zweites_moment.md) Z.5 und Z.8 und zu [anhang\_schleifen.md](anhang_schleifen.md) S.0 und S.2. Bezeichnungen wie dort. Kennzeichnung: [S] bewiesen, [B] Beweisskizze, [N] numerisch. Die Änderungen sind am 2026-11-12 in diese Dokumente eingearbeitet (L.7).

## Auf einer Seite

- **Problem (K3).** Im Aufweg ist j₀ das Stück, das am Loch beginnt, also die Fortsetzung der Linie von j\_m aus der Scheibe davor. Es wird nicht gewählt. Der Beweis benutzte trotzdem drei Eigenschaften von j₀: Es wandert nicht weit (der Sternpfad beginnt nahe r\_k, „ℓ\_tot entfällt“), es bleibt nahe der Route (Lokalität aller geänderten Stücke), und sein Ende Y₀ ist isoliert (guter Endpunkt der ersten Brücke S₁ → Y₀ für Lemma P6). Begründet war das mit „j₀ beginnt in einer guten Zelle“. Eine gute Zelle darf aber bis zum Anteil ε Stücke enthalten, die einen Test verfehlen, und j₀ kann eines davon sein.
- **Warum man nicht einfach verwirft.** Das geschieht je Scheibe mit Wahrscheinlichkeit von der Ordnung e^{−cD²} (zu weit gewandert) und πζ² (Ende nicht isoliert). Über w ~ L/s Scheiben fiele die Annahme wie (1 − ε)^w (G.5.1).
- **Abhilfe: eine Scheibe vorausschauen.** Der Aufweg läuft in der Zeit vorwärts, und die Folgescheibe des geschlossenen Zustands C ist bekannt. j\_m wird nur unter Stücken gewählt, deren Fortsetzung in der Folgescheibe regulär ist (Isolation, Makro- und Randbedingung). Dann ist das nächste Lochstück regulär, ohne dass seinetwegen je verworfen wird. Dazu kommen zwei kleine Regeln: In jeder Scheibe wird umgestiegen, damit jedes Lochstück die Fortsetzung eines gewählten Stücks ist; und in Scheibe 0 wird einmal verworfen, wenn das Stück des Schwanz-Teilchens nicht regulär ist.
- **Ergebnis.** j₀ ist in jeder Scheibe regulär, im geschlossenen Zustand und in jedem hypothetischen Zustand der Dichteformel (Lemma L1). In guten Zellen bleiben mindestens (1 − 2ε) n\_Q Kandidaten (Lemma L2). Die Dichteformel bleibt exakt; die Auswahlgewichte koppeln benachbarte Scheiben (Lemma L3, am Mini-Ring exakt geprüft). „ℓ\_tot entfällt“ und „gute Endpunkte“ gelten damit (L.5).
- **Preis.** Die Kosten je Begegnung steigen von 2ε auf 10ε, der Begegnungsradius R\* wächst um 2D + 4, ζ muss um einen Faktor der Ordnung 1/D kleiner sein, und die Annahme sinkt einmalig um höchstens ε. Für den Existenzsatz ist das gleichgültig.
- **Nicht berührt:** der Abweg (dort sind alle Enden nach Konstruktion gut). Die Befunde K2 und W2 zur Gruppe sind getrennt beantwortet, in [anhang\_unzugaenglich.md](anhang_unzugaenglich.md) (Anhang U): Die zurückgehaltene Gruppe entfällt.

| Teil                                                    | Stand                                 | Prüfung                            |
|---------------------------------------------------------|---------------------------------------|------------------------------------|
| Lemma L1 (j₀ regulär, gute Endpunkte, kein Verwerfen)   | [S]                                   | pruef\_lochstueck.py (Zusicherung) |
| Lemma L2 (Vorrat doppelt wählbarer Stücke)              | [S]                                   | –                                  |
| Seltenheit der neuen Klauseln (iii), (iv)               | [S, gegeben Satz 3.9 (c) und Satz T2] | –                                  |
| Lemma L3 (Dichteformel mit gekoppelten Scheiben)        | [S]                                   | pruef\_lochstueck.py, exakt [N]    |
| Buchführung im zweiten Moment (Fernkürzung, κ₀, Listen) | [B], wie G.12.5–G.12.7 und Anhang Z   | –                                  |

## L.0 Der Befund im Einzelnen

**Die Konstruktion bisher** (G.1, G.12.1). In Scheibe k des Aufwegs liegt das Loch bei h\_k in der Zelle r\_k. j₀ ist das Stück von C, das bei h\_k beginnt; es endet bei Y₀ in der Zelle c₀. Längs eines Sternpfads c₀, c₁, …, c\_m = r\_{k+1} werden Stücke j\_l (l ≥ 1) gewählt. j₀ wird gelöscht, und die Brücken S\_l → Y\_{l−1} werden neu gezogen. Das neue Loch ist h\_{k+1} = Y\_m, das Ende von j\_m. Das Lochstück der nächsten Scheibe ist also die Fortsetzung von j\_m, oder bei m = 0 die Fortsetzung von j₀ selbst.

**Wo j₀ gebraucht wird.**

| Eigenschaft von j₀                | Stelle im Beweis                                                                |
|-----------------------------------|---------------------------------------------------------------------------------|
| endet höchstens D Zellen von r\_k | Sternpfad, „ℓ\_tot entfällt“ (G.12.6, Z.5), „Was der Staffellauf braucht“ (S.2) |
| bleibt in der Kugel um sein Ende  | alle geänderten Stücke liegen nahe den Routen (Stabilität Z.5, Fernkürzung)     |
| Ende Y₀ isoliert                  | guter Endpunkt der Brücke S₁ → Y₀ (Lemma P6, G.12.5, Z.3)                       |

**Warum es nicht folgte.** Eine Zelle ist brauchbar, wenn höchstens der Anteil ε ihrer Stücke einen Test verfehlt. Bei m = K ln(1/ρ) Stücken je Zelle und festem D enthält für ρ → 0 fast jede Zelle einzelne Fehlgänger; „kein Fehlgänger in der Zelle“ kann man also nicht verlangen. Ob j₀ zu den schlechten Stücken gehört, entscheidet sich in jeder Scheibe neu.

## L.1 Die neue Regel

**Begriffe.** Die Tests 1 bis 3 aus G.5.1 betreffen ein einzelnes Stück in seiner Scheibe.

- Ein Stück heißt **regulär**, wenn (1) sein Anfang unter den Anfängen und sein Ende unter den Enden den Abstand > r zu allen anderen haben, (2) es die Kugel vom Radius Ds um sein Ende nicht verlässt und (3) es in den Randintervallen innerhalb r/10 seines Anfangs bzw. Endes bleibt. *Wählbar* ist ein reguläres Stück, das auch die übrigen Bedingungen der Auswahl erfüllt: Regularität der eigenen Bahn ((G2\_A), (G4′)) und Zugänglichkeit (Anhang U, U.1).
- Die **Fortsetzung** eines Stücks der Scheibe k ist das Stück derselben Linie in der Scheibe k + 1. Es beginnt am Ende des ersten.
- Ein Stück der Scheibe k heißt **doppelt wählbar**, wenn es wählbar ist und seine Fortsetzung regulär ist. Zugänglich muss die Fortsetzung nicht sein.

**Regeln für den Aufweg** (sie ersetzen die Sätze über j₀ in G.1, G.5.1 und G.12.1).

1. **Zwei Scheiben.** In jeder Scheibe k ≤ w − 2 wird j\_m gleichverteilt unter den *doppelt* wählbaren Kandidaten der Zelle c\_m = r\_{k+1} gewählt. Für l < m und in der obersten Scheibe k = w − 1 bleibt es bei „wählbar“.
2. **Umstieg in jeder Scheibe.** Es ist immer m ≥ 1. Ist c₀ = r\_{k+1}, so wird innerhalb der Zelle umgestiegen: m = 1, c₁ = c₀, und j₁ ≠ j₀.
3. **Erste Scheibe.** Das Schwanz-Teilchen wird wie bisher gleichverteilt unter allen N Teilchen gewählt. Ist sein Stück in Scheibe 0 nicht regulär, wird verworfen. *Seit 2026-11-13 entfällt diese Regel:* Der Schwanz wird wie bei OA über einen Hilfspunkt und unter den Teilchen mit regulärem Stück gewählt ([anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M.9.5).

**Brauchbare Zellen.** Zur Definition aus G.5.1 (Zählintervall, Anteil ≥ 1 − ε der Stücke mit Ende in Q wählbar) kommen zwei Klauseln für die Zelle Q in der Scheibe k:

- **(iii) Isolation, getrennt gezählt:** Höchstens ε₁ b₋ m der Teilchen in Q sind zur Zeit t\_k nicht isoliert, und ebenso zur Zeit t\_{k+1}. Dabei ist ε₁ = ε/(12 (2D + 3)²).
- **(iv) Zählung nach der Anfangszelle:** Höchstens der Anteil ε/4 der Stücke mit *Anfang* in Q verfehlt die Makro- oder die Randbedingung.
- **(v) Kastenbedingungen** (seit 2026-11-13, [anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M1): Im Kasten vom Radius D\_K s gilt (G1″) mit der Schwelle der Stufe, und jede Linie, die den Kasten besucht, erfüllt (G2\_A) und (G4′).

Für die drei Stufen aus Z.5 (unbrauchbar in C und Ĉ, strenger in B, defekt in Satz D) gelten für (iii) und (iv) dieselben Verhältnisse 1 : ½ : ¼ wie für den Anteil ε.

## L.2 Lemma L1: was die Regel liefert [S]

**Lemma L1.** Die Konstruktion mit den Regeln 1 bis 3 sei nicht verworfen worden. Dann gilt in jeder Scheibe k des Aufwegs, im geschlossenen Zustand C:

1. j₀ ist regulär.
2. Der Lochplatz h\_k hat zur Zeit t\_k den Abstand > r von allen anderen Teilchen, und das Ende Y₀ von j₀ hat ihn zur Zeit t\_{k+1}.
3. j₀ verlässt die Kugel vom Radius Ds um Y₀ nicht. Die Zelle c₀ liegt höchstens D + 1 Zellen von r\_k.
4. Jede Brücke S\_l → Y\_{l−1}, l = 1, …, m, hat zwei Endpunkte, die zu ihrer Zeit den Abstand > r von allen anderen Teilchen haben.
5. Nach der Scheibe 0 wird wegen j₀ nie verworfen.

Dasselbe gilt im hypothetischen geschlossenen Zustand Ĉ jedes Summanden der Dichteformel.

*Beweis.*

1. Für k = 0 ist das Regel 3. Für k ≥ 1 ist j₀ die Fortsetzung von j\_m der Scheibe k − 1 (Regel 2: m ≥ 1), und j\_m war doppelt wählbar (Regel 1).
2. Das ist Test 1 für j₀. Für k ≥ 1 ist h\_k außerdem das Ende des wählbaren Stücks j\_m der Scheibe davor.
3. Das ist Test 2. h\_k liegt in r\_k und |h\_k − Y₀|\_∞ ≤ Ds.
4. S\_l ist der Anfang des wählbaren Stücks j\_l, also isoliert. Y\_{l−1} ist für l ≥ 2 das Ende des wählbaren Stücks j\_{l−1} und für l = 1 das Ende Y₀ von j₀; beide sind isoliert.
5. Die Regularität von j₀ ist durch die Wahl gesichert, nicht durch eine Prüfung.

Im Zustand Ĉ: Das Auswahlgewicht sel⁺ der Dichteformel (L.4) enthält die Anzeigen „j\_l wählbar“, „j\_m doppelt wählbar“ und in Scheibe 0 „j₀ regulär“, ausgewertet in Ĉ. Auf dem Träger jedes Summanden gelten also dieselben Aussagen in Ĉ. ∎

**Was damit begründet ist.**

- Der Sternpfad beginnt in einer Zelle im Abstand ≤ D + 1 von r\_k. Seine Länge ist höchstens D + 2 plus die Weglänge aus Lemma S2. Einen Zusatzterm ℓ\_tot gibt es nicht.
- Alle geänderten Stücke, auch das gelöschte j₀, liegen in der Kugel vom Radius Ds um ihr Ende. Die Lokalität, die Stabilität (Z.5) und Fernkürzung brauchen, gilt für j₀ wie für die gewählten Stücke.
- Lemma P6 verlangt gute Endpunkte der Brücke. Für alle Brücken des Aufwegs sind sie da, auch für S₁ → Y₀.

## L.3 Lemma L2: der Vorrat [S]

**Lemma L2.** Die Zelle Q sei in der Scheibe k brauchbar, und alle Zellen im Abstand ≤ D + 1 von Q seien in der Scheibe k + 1 brauchbar, jeweils mit den Klauseln (iii) und (iv). Sei n = n\_Q die Zahl der Stücke der Scheibe k mit Ende in Q. Dann gilt:

```text
#{ Stücke mit Ende in Q, deren Fortsetzung nicht regulär ist, obwohl ihr Ende isoliert ist }  ≤  (ε/3) n
#{ Stücke mit Ende in Q, die wählbar sind und eine reguläre Fortsetzung haben }              ≥  (1 − 2ε) n
```

*Beweis.* Die Fortsetzungen sind genau die Stücke der Scheibe k + 1 mit Anfang in Q; es sind n. Eine Fortsetzung ist aus einem von drei Gründen nicht regulär:

1. *Ihr Anfang ist nicht isoliert.* Der Anfang ist das Ende des Stücks der Scheibe k. Dann ist schon dieses Stück nicht wählbar und zählt zu den höchstens εn nicht wählbaren.
2. *Sie verfehlt die Makro- oder die Randbedingung.* Nach Klausel (iv) für (Q, k + 1) sind das höchstens (ε/4) n.
3. *Sie erfüllt die Makro-Bedingung, aber ihr Ende ist nicht isoliert.* Dann liegt ihr Ende in einer Zelle Q′ im Abstand ≤ D + 1 von Q. Nach Klausel (iii) für (Q′, k + 1) enthält jede solche Zelle höchstens ε₁ b₋ m nicht isolierte Enden. Zusammen sind das höchstens (2D + 3)² ε₁ b₋ m = (ε/12) b₋ m ≤ (ε/12) n.

Die erste Zeile ist (ε/4 + ε/12) n = (ε/3) n. Die zweite folgt mit den höchstens εn nicht wählbaren Stücken der Scheibe k. ∎

**Anwendung.** Nach Lemma S2 (1) ist die Lage r\_{k+1} in den Scheiben k und k + 1 gut, und wegen der Verdickung um D′ ≥ D + 2 (Anhang S) sind alle Zellen im Abstand ≤ D + 2 in beiden Scheiben roh gut. Lemma L2 gilt also für Q = r\_{k+1}: Für j\_m gibt es mindestens (1 − 2ε) n\_Q doppelt wählbare Stücke. Für den Umstieg innerhalb der Zelle (Regel 2) braucht man eines davon außer j₀; das gibt es für großes m.

**Keine Gruppe.** Seit der Fassung von Anhang U gibt es keine zurückgehaltene Gruppe mehr: j\_m wird unter allen wählbaren Stücken der Zelle mit regulärer Fortsetzung gewählt. Unter den Stücken mit Ende in Q sind höchstens εn nicht wählbar (einschließlich der unzugänglichen) und nach Lemma L2 höchstens (ε/3)n weitere ohne reguläre Fortsetzung. (Die erste Fassung dieses Abschnitts bildete die Gruppe unter den Stücken mit regulärer Fortsetzung.)

**Seltenheit der Klauseln [S, gegeben Satz 3.9 (c) und Satz T2].**

- *Klausel (iii).* Das ist der Defektgrund D2 mit dem Anteil ε₁ statt ε/4. Satz 3.9 (c) (satz\_3\_9 §12.2) gibt für u solche Zellen die Schranke exp(−λ₀ m u (ε₁b₋/32 − C\_iso ζ²)), wenn die Defektstufe ε₁/4 ist. Der Exponent ist positiv für

  ```text
  ζ²  ≤  ε₁ b₋ / (64 C_iso)  =  ε b₋ / (768 (2D + 3)² C_iso)
  ```

  Das ist die Bedingung ζ² < εb₋/(64C\_iso) aus §12.2, verschärft um den Faktor 12 (2D + 3)². ζ wird nach D und ε gewählt (Z.9), also entsteht kein Zirkel.
- *Klausel (iv).* Satz T2 zählt fehlerhafte Stücke mit *Ende* in U. Das stationäre Pfadmaß des Grundzustands ist invariant unter der Zeitumkehr einer Scheibe (H ist reell symmetrisch). Unter ihr wird aus einem Stück mit Anfang in U eines mit Ende in U, die Randintervalle tauschen die Rollen, und „verlässt die Kugel vom Radius Ds um sein Ende“ wird zu „um seinen Anfang“. Ein Stück, das die Kugel vom Radius Ds um sein Ende verlässt, verlässt auch die Kugel vom Radius Ds/2 um seinen Anfang. Satz T2 mit D/2 statt D gilt also für die Zählung nach der Anfangszelle. Dass D4 nach Anfangs- und Endzelle zählt, steht schon in G.12.1; hier ist die Begründung.

## L.4 Lemma L3: die Dichteformel [S]

Mit den neuen Regeln hängt das Auswahlgewicht von j\_m in Scheibe k von Stücken der Scheibe k + 1 ab. Sei

```text
sel⁺_k(Ĉ)  =  Π_{l<m} 1{j_l wählbar} / g_{c_l}(Ĉ)  ·  1{j_m doppelt wählbar} / g⁺_{c_m}(Ĉ)        (k ≤ w − 2)
```

mit der Zahl g⁺\_{c\_m}(Ĉ) der doppelt wählbaren Kandidaten der Zelle c\_m im Zustand Ĉ (ohne j₀); für k = w − 1 ist sel⁺ = sel wie bisher, und für k = 0 kommt der Faktor 1{j₀ regulär} dazu.

**Lemma L3.** Die Dichteformel (Lemma G1, für die Schleife G.12.2) gilt mit den Regeln 1 bis 3, wenn man den Aufweg-Faktor so liest:

```text
Aufweg-Faktor  =  Σ_{Aufweg-Daten}  ∫  Π_k  π · sel⁺_k(Ĉ) · 1_cut · W(alte Stücke_k) / Z^br_k
```

Das Integral läuft über die alten Stücke aller Scheiben gemeinsam. Es zerfällt nicht mehr in ein Produkt Π\_k Z^{alt}\_k/Z^{br}\_k, weil g⁺ und die Anzeige „doppelt wählbar“ die alten Stücke benachbarter Scheiben koppeln.

*Beweis.* Der Beweis von Lemma G1 benutzt von der Auswahl nur, dass ihre Gewichte Funktionen des geschlossenen Zustands und des Skeletts sind (G.1, letzter Absatz). Das gilt weiter: Die Anzeigen der Folgescheibe sind Funktionen von C. Umkehrbarkeit und Produktstruktur der Gewichte (Schritte 1 und 2 dort) bleiben wörtlich. In Schritt 3 steht je Summand der Faktor Π\_k sel⁺\_k(C) W(Brücken\_k)/Z^{br}\_k; nach dem Teilen durch das Zielmaß bleibt Π\_k sel⁺\_k(Ĉ) W(alte Stücke\_k)/Z^{br}\_k, und man integriert über die alten Stücke. Regel 2 ändert nur die Menge der Sternpfade, Regel 3 fügt eine Anzeige hinzu. ∎

**Exakte Prüfung [N]** ([pruef\_lochstueck.py](pruef_lochstueck.py), Ausgabe in ergebnisse/pruef\_lochstueck.txt). Modell wie in G.2: Ring mit 6 Plätzen und 3 Zellen, Trotter-Zeit, Aufweg über w Scheiben, Ziel ist das Lückenmaß. Regulär heißt dort „Anfang und Ende in derselben Zelle“. Die Züge sind d ∈ {−1, 0, 1, 2}; d = 0 ist der Umstieg innerhalb der Zelle. ν entsteht durch vollständige Vorwärtsrechnung über alle geschlossenen Geschichten, f aus der Formel mit gekoppelten Scheiben.

| N   | w   | λ   | Lücken-Geschichten mit ν > 0 | größter relativer Fehler ν − fΓ | \|ν\|   |
|-----|-----|-----|------------------------------|---------------------------------|---------|
| 3   | 2   | 0,7 | 45 588                       | 5,0·10⁻¹⁶                       | 0,033   |
| 3   | 3   | 0,7 | 16 863                       | 5,0·10⁻¹⁶                       | 0,0066  |
| 4   | 2   | 0,7 | 52 032                       | 5,7·10⁻¹⁶                       | 0,083   |
| 4   | 3   | 0,9 | 43 752                       | 7,5·10⁻¹⁶                       | 0,019   |
| 2   | 3   | 0,9 | 54                           | 6,5·10⁻¹⁶                       | 0,00016 |

- Die Formel ist exakt, auch über drei Scheiben (zwei Kopplungen) und mit Umstiegen innerhalb der Zelle.
- Im Programm steht die Zusicherung, dass das Lochstück jeder Scheibe k ≥ 1 regulär ist. Sie wird nie verletzt.
- Die Masse |ν| ist am Mini-Ring klein. Das liegt am Modell: Eine Zelle hat 2 Plätze, und für den Pflicht-Umstieg fehlt meist ein Kandidat (59–78 % der Masse; weitere 17–41 % fallen in Scheibe 0 weg, weil das Stück des Schwanz-Teilchens die Zelle wechselt). Über die Ausbeute im Beweisbereich sagt das nichts; dort gibt Lemma L2 den Vorrat.

## L.5 Was sich im zweiten Moment ändert [B]

Der Ablauf von G.12.4–G.12.7 und Anhang Z bleibt. Fünf Stellen ändern sich.

1. **Reichweite der Auswahlgewichte.** Das Gewicht von j\_m in Scheibe k hängt jetzt auch von den Stücken der Scheibe k + 1 ab, die in r\_{k+1} beginnen, und von der Isolation ihrer Enden. Diese Stücke liegen im Abstand ≤ D + 1 von r\_{k+1}, und die Route von R beginnt in Scheibe k + 1 in einer Zelle im Abstand ≤ D + 1 von r\_{k+1} (Lemma L1). Vergrößert man den Begegnungsradius R\* um 2D + 4, so hängen die Auswahlgewichte von R in den Scheiben k − 1 und k nur von Stücken der Scheibe k ab, die innerhalb von R\* der Route von R in Scheibe k liegen.
2. **Fernkürzung (G.12.4, Lemma Z.1).** Mit dem größeren R\* gilt sie scheibenweise wie bisher. Liegt in Scheibe k kein Stück von R′ in Reichweite, so hängen die Faktoren von R nicht von den Stücken ab, die R′ dort zieht; die Stücke der anderen Scheiben sind beim Integrieren fest.
3. **Nahe Vorkommen.** Ein Vorkommen von j\_m in (r\_{k+1}, k) heißt nah, wenn die andere Route in Scheibe k *oder* in Scheibe k + 1 in Reichweite ist. Jede Scheibe mit einer Begegnung bringt so je Route höchstens ein weiteres nahes Vorkommen; ihre Zahl verdoppelt sich höchstens. Für ein nahes Vorkommen ist das Auswahlgewicht ≤ [(1 − 2ε) n\_Q]^{−1} nach Lemma L2 (bisher [(1 − ε) n\_Q]^{−1}). Je Begegnung kostet die Auswahl also höchstens (1 − 2ε)^{−4} ≤ e^{10ε} für ε ≤ 1/10, statt (1 − ε)^{−2}:

   ```text
   κ₀  =  10 ε  +  σ_ρ  +  (e^{C(K)} − 1) / (b₋ m)
   ```

   Ferne Vorkommen werden wie bisher in B ausgewertet und haben für alle Zeugen denselben Wert.
4. **Stabilität und Listen (Z.5).** Die Klauseln (iii) und (iv) sind Zählungen je Zelle und Scheibe. Sie ändern sich zwischen den Zuständen C, Ĉ und B nur um beschränkt viele Stücke je Zelle, wie die bisherigen Zählungen; die drei Stufen fangen das auf. Die einzelnen Anzeigen „doppelt wählbar“ stimmen überein, sobald in beiden Scheiben kein geändertes Stück in Reichweite ist. In den Listen entfällt ℓ\_tot: In jedem Zeugen ist j₀ regulär (Lemma L1), also ist die Endzelle c₀ ein Endpunkt-Datum im Abstand ≤ D + 1 von r\_k.
5. **Nenner nahe Begegnungen (G.12.5, Z.3).** Die Voraussetzung „gute Endpunkte“ von Lemma P6 gilt für alle Brücken des Aufwegs und für die alten Stücke längs R im Bezugszustand B, einschließlich des Lochstücks. Der Fall „Y₀ nicht isoliert“, für den eine Untergrenze ganz fehlte, kommt nicht mehr vor.

Die Bedingung des Beweises bleibt κ₀ ≤ α/2. Sie verlangt jetzt ε ≤ α/40 statt ε ≤ α/8, und α = c/(1 + R\*)² wird durch das größere R\* um einen festen Faktor kleiner.

## L.6 Die Annahme

Verworfen wird wie bisher bei einer großen Komponente oder einer Endzelle in einer Füllung (Anhang S), dazu einmal in Scheibe 0, wenn das Stück des Schwanz-Teilchens nicht regulär ist. Liegt die Zelle a außerhalb der Füllungen, so sind höchstens (ε/2) n der Stücke mit Anfang in a nicht regulär (wie im Beweis von Lemma L2, dazu ε₁ n für nicht isolierte Anfänge). Das Schwanz-Teilchen ist gleichverteilt, also ist die zusätzliche Verwerfung höchstens ε, und

```text
|ν|  ≥  υ/2 − ε
```

In den Scheiben k ≥ 1 gibt es wegen j₀ keine Verwerfung, und der Pflicht-Umstieg findet in guten Zellen immer einen Kandidaten (Lemma L2). Die Annahme hängt also weiter nicht von w ab.

## L.7 Was offen bleibt, und was eingearbeitet ist

1. **K3 selbst** ist damit beantwortet: j₀ ist regulär, „ℓ\_tot entfällt“ ist begründet, und alle Brücken haben gute Endpunkte.
2. **Stufe der Buchführung.** L.5 ist eine Beweisskizze auf dem Stand von G.12.5–G.12.7 und Anhang Z ([B] bzw. [B nach OA]). Die drei Stufen der Klauseln (iii) und (iv) in den Zuständen C, Ĉ, B sind nicht einzeln ausgeschrieben.
3. **Gruppe.** K2 und W2 des Reviews sind in Anhang U beantwortet: Die zurückgehaltene Gruppe entfällt, und gewählt wird unter allen wählbaren Stücken der Zelle.
4. **Abbildung 5 des Tutorials** zeigt in Scheibe 1 noch einen Schritt ohne Umstieg. Die Bildunterschrift weist darauf hin; das Bild ist nicht neu gezeichnet.
5. **Eingearbeitet am 2026-11-12:** Anhang G (G.5.1 Nachtrag, G.12.1, G.12.5, G.12.6, G.12.7), Anhang Z (Z.0, Z.5, Z.8, Z.9, Z.10), Anhang S (S.0, S.2), satz\_3\_9 (§9.1, §12.2), Tutorial (§5.2, §10), Anhang P und F (Verweise), README und Review.
