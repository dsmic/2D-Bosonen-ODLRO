# Anhang M: Buchführung im zweiten Moment

Stand 2026-11-13. Teil 1 (M.1–M.4): Inventar der Tests, vier Korrekturen, Stabilität. Teil 2 (M.6): die Nenner Z.2–Z.4. Teil 3 (M.7): Z.6 und die Auswahlsummen aus Z.8. Teil 4 (M.8): Listen, J und seltene Komponenten; dabei die Korrektur der Zählungen je Scheibe. Teil 5 (M.9): Endzellen und Bezugsmaß, mit dem späten Schnitt bei geteilten Kopfscheiben (M.9.6). Ausgangspunkt ist [anhang\_zweites\_moment.md](anhang_zweites_moment.md) (Anhang Z), Z.2 bis Z.8; dort sind die Schritte Beweisskizzen nach OA §10. Dieser Anhang geht sie mit den Begriffen durch, die seit dem Review dazugekommen sind: Anhang F (Kästen vom Radius D\_K s), Anhang L (Wählbarkeit über zwei Scheiben), Anhang U (zwei Schwellen der Zugänglichkeit) und Anhang E (b₋).

## Auf einer Seite

- **Vorgehen.** Zuerst wird für jeden Test, der über „brauchbar“, „wählbar“ oder „defekt“ entscheidet, festgehalten, wovon er abhängt, wie weit er reicht und wie er sich zwischen den Zuständen C, Ĉ und B ändert (M.1, M.2). Daraus folgen vier Korrekturen (M.3) und das Stabilitätslemma M4 [S], das Lemma Z.5 ersetzt (M.4).
- **M1, Kastenbedingungen.** Lemma P6 verlangt (G1″), (G2\_A) und (G4) im Kasten um jede Brücke. In Anhang Z und G.12.5 steht dafür „gilt im Kasten jeder nicht defekten Zelle“. Die Zellen der Route sind aber nur brauchbar, nicht unbedingt nicht defekt. Korrektur: Die Kastenbedingungen werden Klausel (v) der Brauchbarkeit.
- **M2, reguläre Brücken.** Lemma U4 (2) bis (4) und die Stabilität von D7 setzen voraus, dass hinzugefügte Bahnen (G2\_A) und (G4′) erfüllen. Gezogene Brücken und neue Stücke tun das bisher nicht sicher. Korrektur: Sie werden aus dem bedingten Gesetz *mit* dieser Regularität gezogen. Das kostet in jeder Untergrenze nur p\_irr → 0 (Lemma M2).
- **M3, Stufen.** (G1″) und das Zählintervall brauchen wie die Zugänglichkeit drei Stufen (Zeuge, B, defekt). Satz F10 verträgt die abgesenkte Schwelle (Lemma M3).
- **M4, Begegnungsradius.** R\* war nirgends festgelegt. Er muss alle Reichweiten decken, also auch D\_K: R\* = Δ + D\_K + R + 2D + 6. Damit wird α = c/(1 + R\*)² kleiner; die Reihenfolge der Konstanten verträgt das.
- **Lemma M4 (Stabilität) [S, gegeben Lemma U4 und M1–M3].** S(C) ∪ S(Ĉ) ⊆ S₁(B) ⊆ defekt; fern der Routen stimmen alle Anzeigen überein; an jeder brauchbaren Zelle gelten die Voraussetzungen von Lemma P6 in jedem Zustand, der sich in höchstens n″ regulären Linien unterscheidet.
- **Teil 2, die Nenner (M.6).** Z.2–Z.4 folgen aus einem Vergleichslemma (Lemma M5 [S]) mit Lemma P6″ für *alle* Stücke: Folgerung M6 (Z.3), M7 (Z.4) [S, gegeben Lemma P6″, Lemma C (c), Lemma F13, Lemma M4] und Lemma M8 (Z.2) [S, gegeben (K1), (K2)]. Die Konstanten: C(K) = 6 ln(4πe^{(Λ²+1)/2}) + 4 ln(1/p), σ = 12 n\_loc P\_T/p → 0. Neu ist eine Bedingung an den cut-Radius R.
- **Teil 3 (M.7).** Lemma M9 (= Z.6) [S, gegeben M4, M6–M8, G3′] und Lemma M10 (Auswahl summieren) [S, gegeben M9]. J zählt jetzt die nahen Vorkommen; je Vorkommen κ₀ = 3ε + 6σ + (e^{2C(K)} + 4)/(b₋m − 4).
- **Teil 4 (M.8).** Lemma M11 (Listen: ≤ e^{4b\_tot} Routenpaare), M12 (J ≤ C\_J(J₀″ + b\_tot)) und M13 (seltene Komponenten: E\_{µ\_ab} e^{C₂b\_tot} ≤ (C/M²) e^{ϑS}), alle [S, gegeben Lemma S2, M4 bzw. Z.7]. b\_tot zählt je Scheibe den Klumpen am Skelett und die Komponenten auf *einer* Strecke; über die ganze Umgebung zu zählen, ließe die Peierls-Summe versagen. Bedingung jetzt κ₀ ≤ α\_J = α(R\*″)/(4C\_J), also ε ≤ α\_J/6.
- **Korrektur (Teil 4):** Eine Route ändert je Scheibe *nicht* beschränkt viele Stücke, denn der Weg um eine große Komponente ist lang. M1, M4 und M6 zählen jetzt lokal (je Routenzelle, je Kasten), und Lemma M5 nimmt die Bedingungen einzeln hinzu.
- **Teil 5 (M.9).** Endzellen und Bezugsmaß: OAs Vorlage (§10.5) nachgelesen; Bezeichnung korrigiert (OAs M ist die Zahl der Zellen, hier M\_Z = M/s²); unsere Enden sind anders gebaut (Schwanz unter allen N, Kopf aus Variante c, Vorfaktor M). Restsatz M14: Schwanz jetzt wie OA (Hilfspunkt ξ, M.9.5), Dichte Lemma M14a [S], Bilanz der Vorfaktoren vollständig (alle Potenzen von m, s, M\_Z, A heben sich weg, Ergebnis C e^{2C(K)}(4D\_c + 3)²/υ); [B nach OA] bleibt der Vergleich in den beiden Endscheiben.
- **Geteilte Kopfscheiben (M.9.6).** Bei k ≥ 1 liegt der Schnitt von B zur Zeit t\_k, auf [0, t\_k) hat B also N + 1 Linien. Lemma M14b [S, gegeben Satz D für N und N + 1 Teilchen]: Das Bezugsmaß µ\_ab^{(k)} erfüllt Z.7 in derselben Form, mit voller Defekt-Kleinheit auch vor t\_k. Grund: Satz D ist ein Produkt von Operatornormen je Scheibe und hängt deshalb nicht vom Anfangszustand a\*(1\_a)ψ\_N ab. Die Reihe über k konvergiert für (1 − 2ε)(b₋m − 2)c₁p₁ ≥ 4e^{2C(K)}. Numerisch [N]: Im 2D-Testmodell sind die Beiträge mit k ≥ 1 die Hälfte bis vier Fünftel von ∫f² und tragen das ganze Wachstum mit w; der Teil mit k = 0 ist über w konstant.
- **Lemma M14a exakt geprüft [N]** (pruef\_m14a.py, Fehler ≤ 1,7·10⁻¹⁵). Lage des Schnitts: mit pred\_{I′}(h) in d liegt er stets zur Zeit t\_k am Anfang des erzwungenen Teilchens p, für k = 0 also zur Zeit 0, ohne Hilfspunkt am Kopf. Seit 2026-11-13 abends Lemma M14f [S] (M.9.10): Bilanz, das Stück am Ende Y\_0^R, die Fassung von B als Verschiebung längs der Kette von R mit einer Korrektur am Kopf, Abstände ≤ D + 4 Zellen, Λ = (9/8)(D + 4); dieselbe Verschiebung begründet M8, Schritt 4. Zwei Sonderfälle (Teilen bis zur Wende, Kopf- und Schwanzende in derselben Scheibe) [B].
- **Endscheiben (M.9.7).** Auch am Schwanz kann sich das Teilen fortsetzen (übereinstimmende verdeckte Lochplätze); M.9.5 hatte das nicht. Abhilfe: Die zusätzliche Linie von B läuft ab ξ frisch durch die geteilten Schwanzscheiben, die Erzeugung bleibt bei (ξ, 0). Die Kernzählung je Endscheibe ersetzt M8, Schritt 3: Insgesamt bleibt genau ein Kern C/s² am Kopf (das Stück von p, das B fehlt), jede weitere geteilte Schwanzscheibe kostet einen Kern C/s², jede weitere Kopfscheibe keinen. Lemma M14d [B]. Numerisch [N]: Fortsetzung am Schwanz 8–21 % gegen 44–61 % am Kopf; die Dämpfung C/s² ist auf kleinen Tori nicht prüfbar.
- **Lemma M14d ausgeschrieben (M.9.8)** [S, gegeben Lemma M4 bis M8, Lemma C, C′ und P6″]: die Schritte von M9 in den Endscheiben, mit ℒ-Konvention (keine Faktoren e^{4δ}), Kernzählung aus M.9.7, d ≤ 3|h| und Lemma C′ (Stück mit freiem Ende, Zeitumkehr von Lemma C). Ergebnis: Faktor e^{C′(K)|h|} s^{−2(1 + k\_T)} mit C′(K) = 8 ln(4πe^{(Λ²+1)/2}) + 7 ln(1/p). Die Summe über die Zelle des Schnitts ist Lemma M14e (M.9.9): Der Schnitt liegt in Reg\_{k\_H}, und 1{d ≤ ℓ} ≤ e^{ℓ − d} führt auf M13 mit C₂ + 7. **Restsatz M14 ist damit bewiesen**, gegeben Lemma M4 bis M13, M14a bis M14e, Lemma C, C′, P6″ und Satz D für N und N + 1 Teilchen.
- **Später Anfang am Schwanz (M.9.11, 2026-11-14, Review 2026-11-13, W1).** In den geteilten Schwanzscheiben ist B = C; die Erzeugung liegt zur Zeit t\_{k\_T} an einem isolierten freien Platz P höchstens eine Zellseite vom gemeinsamen Lochplatz. Bezugsmaß µ^{(k\_T, k\_H)} mit Sektor N ± 1 dazwischen, Lemma M14b′ [S, gegeben Satz D für N − 1, N, N + 1]; im Sektor N − 1 ein Energiefaktor e^{δμ̄} je Scheibe, den die Kerne C/s² schlucken. Die Summe über P bringt s², die erste geteilte Schwanzscheibe nimmt es mit ihrem Kern zurück. Lemma C′ wird nicht mehr gebraucht.
- **Noch offen in Anhang M:** die beiden Sonderfälle in M.9.10 [B] (Teilen bis zur Wende; Kopf- und Schwanzende in derselben Scheibe). Bis 2026-11-13 stand hier: nichts mehr. Der Grund D4 für Stücke, die einen Kasten nur durchlaufen, ist in satz\_3\_9 §10.8 erledigt (Tabelle M.5).

## M.1 Was sich zwischen den Zuständen ändert [S]

Bezeichnungen wie Z.1: R′ baut O aus C, R wertet die Dichte in O aus, Ĉ ist O mit den Schritten von R rückgängig, B ist C mit den Schritten von R rückgängig. Ein Stück heißt *geändert*, wenn es in den beiden verglichenen Zuständen verschieden ist.

**Lemma M1.** Sei Δ = R + D + 2. Eine *Routenzelle* ist eine Zelle, in der eine Hälfte einer Route in Scheibe k umsteigt.

1. **Zahl, lokal gezählt.** Je Routenzelle ändert eine Route höchstens 6 Stücke (je Hälfte das alte Stück, die Brücke, die dort endet, und im Abweg das neue Stück). Die Zahl der Routenzellen einer Scheibe ist *nicht* beschränkt: Um eine große schlechte Komponente kann der Weg lang werden (Lemma S2 (3)). In einem ℓ∞-Ball vom Radius ϱ Zellen ändern beide Routen in einer Scheibe zusammen höchstens n(ϱ) = 12(2ϱ + 2Δ + 1)² Stücke. C und B unterscheiden sich nur in den Stücken von R, Ĉ und B nur in denen von R′. Mit n″ = n(D\_K + R + 1), der größten Reichweite der Tabelle M.2, unterscheiden sich je zwei der Zustände C, O, Ĉ, B in jeder Reichweite eines Tests und in jedem Kasten in höchstens n″ Stücken.
2. **Lage.** Jedes geänderte Stück liegt im ℓ∞-Ball vom Radius Δ s um die Routenzelle, in der es gewählt oder gezogen wird.
3. **Art.** Jedes geänderte Stück ist ein wählbares altes Stück (also regulär⁺), eine Brücke oder ein neues Stück. Die Endpunkte geänderter Stücke sind Endpunkte wählbarer Stücke oder der Kopf S′; alle sind isoliert.
4. **Endpunkte.** Zu den Zeiten t\_k unterscheiden sich die Teilchenmengen zweier Zustände nur am Loch und am Kopf, je Route und Zeit in höchstens einem Platz. Diese Plätze sind isoliert. Also ändern sich Zählungen n\_Q um höchstens 2 und Isolationsanzeigen anderer Teilchen gar nicht.

*Beweis.* (1) Ein Sternpfad besteht aus verschiedenen Zellen (G.0), also gibt es je Zelle und Hälfte höchstens einen Umstieg. Stücke in einem Ball vom Radius ϱ gehören nach (2) zu Routenzellen im Ball vom Radius ϱ + Δ, davon gibt es je Scheibe höchstens (2ϱ + 2Δ + 1)². (2) Alte Stücke bleiben nach der Makro-Bedingung im Ball vom Radius Ds um ihr Ende, Brücken und neue Stücke nach cut im Ball vom Radius Rs, R ≥ D, und S′ liegt im Ball vom Radius D\_c s ≤ Ds um Y\_m. (3) Gewählt wird nur unter wählbaren Stücken; S′ ist nach Konstruktion isoliert. (4) Brücken verbinden vorhandene Endpunkte; neu oder weg sind nur das Loch und der Kopf. Ein isolierter Platz hat im Abstand r kein anderes Teilchen, also ändert sein Hinzufügen oder Entfernen keine andere Isolationsanzeige. ∎

## M.2 Inventar der Tests

Reichweite heißt: Ein geändertes Stück kann den Test einer Raum-Zeit-Zelle (Q, k) nur ändern, wenn es in Scheibe k (bzw. k + 1, wo angegeben) näher als so viele Zellen an Q liegt.

| Test                                       | hängt ab von                                      | Reichweite            | Änderung zwischen den Zuständen (M1)                 | Stufen Zeuge / B / defekt                       |
|--------------------------------------------|---------------------------------------------------|-----------------------|------------------------------------------------------|-------------------------------------------------|
| Zählintervall n\_Q zu t\_k, t\_{k+1}       | Endpunkten                                        | 1                     | ≤ 2                                                  | [b₋m, b₊m] / [b₋m + 2, b₊m − 2] / [2b₋m, b₊m/2] |
| Isolation (Test 1), Klausel (iii)          | Endpunkten im Abstand r                           | 1                     | keine (M1 (4))                                       | ε₁b₋m / ε₁b₋m/2 / ε₁b₋m/4                       |
| Makro, Rand (Tests 2, 3), Klausel (iv)     | der eigenen Bahn                                  | 0                     | nur geänderte Stücke, ≤ n″                           | ε/4 / ε/8 / ε/16                                |
| (G2\_A), (G4′) der eigenen Bahn            | der eigenen Bahn                                  | 0                     | nur geänderte Stücke; nach M2 regulär                | gleich                                          |
| Zugänglichkeit a\_i(F\_i^{alle})           | Bahnen im Ball vom Radius Rs um E\_i              | R + 1                 | ≤ n″ P^{br}\_treff + p\_irr (Lemma U4 (2), M2)       | p\* / 2p\* / 2p\*                               |
| Ausfallanteil (nicht wählbar)              | allem oben                                        | R + 1                 | ≤ n″ + 4 Stücke (dazu die Ausnahme-Enden von B)      | ε / ε/2 / ε/4                                   |
| doppelt wählbar (Auswahl von j\_m)         | dazu der Fortsetzung in Scheibe k + 1             | R + 1, auch in k + 1  | wie oben                                             | nur Auswahlgewicht                              |
| (G1″) im Kasten (D6)                       | Zahlen in Gitterquadraten, die den Kasten treffen | D\_K + 1              | Zeitmittel um ≤ n″                                   | N\* − n″ / N\* − 2n″ / N\* − 3n″ (M3)           |
| (G2\_A), (G4′) aller Linien im Kasten (D7) | Bahnen, die den Kasten besuchen                   | D\_K + 1              | keine, wenn alle geänderten Stücke regulär sind (M2) | gleich                                          |
| Route (Füllungen, Lemma S2)                | S(·) der Zellen nahe dem Skelett                  | über die Listen (Z.5) | durch Raten auf Brücken-Komponenten                  | –                                               |

## M.3 Vier Korrekturen

**M1: Die Kastenbedingungen gehören zur Brauchbarkeit.** Zu den Klauseln (i)–(iv) einer brauchbaren Raum-Zeit-Zelle (G.5.1, Anhang L, L.1) kommt:

- **(v)** Im Kasten 𝔎\_c vom Radius D\_K s gilt (G1″) mit der Schwelle der Stufe, und jede Linie, die 𝔎\_c in der Scheibe besucht, erfüllt (G2\_A) und (G4′).

Bisher stand an dieser Stelle (G.12.5, Z.3): „gelten im Kasten jeder nicht defekten Zelle“. Das reicht nicht, denn die Route meidet nur unbrauchbare Zellen, und brauchbar ist schwächer als nicht defekt. Satz D bleibt gültig, weil D6 und D7 schon Defektgründe sind; mit (v) liegt jede Zelle, die (v) verletzt, in S(C) und in S₁(B), und sie ist defekt (M3).

**M2: Gezogene Stücke sind regulär.** Brücken und neue Stücke werden aus dem exakt normierten Gesetz gezogen, das zu cut und Ausweichen die Regularität (G2\_A) und (G4′) der eigenen Bahn hinzunimmt. Die Dichteformel (G.12.2, Lemma L3) bleibt exakt, denn die Normierer enthalten dieselbe Bedingung; die Fernkürzung (G.12.4) ebenso.

**Lemma M2 (Brücken sind fast immer regulär) [S, gegeben Lemma R (a), Lemma F11a, (W1)].** Für die freie Brücke einer Scheibe zwischen S und E mit λ = |E − S|/δ^{1/2} ≤ Λ gilt (für die Stücke der Konstruktion ist Λ = (9/8)(D + 4), wie in Lemma M8; bis 2026-11-13 abends D + 2)

```text
P( die Brücke verletzt (G2_A) oder (G4′) )  ≤  p_irr  =  16π e^{1/2} e^{Λ²/4} · ( p_A + 4 N_g e^{−β/70,4} )
```

mit p\_A der Schranke aus Lemma R (a) für (G2\_A) auf einer halben Scheibe (alle Horizonte, F.11.1). Für C\_β ≥ 300 geht p\_irr gegen 0.

*Beweis.* Nach (W1) hat die erste Hälfte der Brücke bezüglich der freien Irrfahrt die Dichte ≤ 8πe^{λ²/4}, die zweite rückwärts ebenso. Für die freie Irrfahrt gibt Lemma R (a) die Schranke p\_A. Verletzt eine Bahn (G4′) im Fenster G, so ist sup\_{u ≤ t\_r} |Y(g + u) − Y(g)|\_∞ ≥ r/16 für den Anfang g des Fensters; Lemma F11a mit a = r/16, t = t\_r = r²/(16β) gibt 4 exp(−a²/(4,4 t)) = 4e^{−β/70,4}. Vereinigung über die N\_g Fenster und die beiden Hälften. Mit β = C\_β ln ln(1/ρ) ist N\_g e^{−β/70,4} ≲ β ln(1/ρ) (ln(1/ρ))^{−C\_β/70,4} → 0. ∎

*Folgen.* Jede Untergrenze für einen Normierer verliert höchstens p\_irr: Lemma P6 gibt p₁ − p\_irr ≥ p₁/2, die Randschranke aus Lemma U4 (3) wird 1/(p\* − n″P^{br}\_treff − p\_irr) ≤ 2/p\* für n″P^{br}\_treff + p\_irr ≤ p\*/2, und Lemma C (c), (d) behält seine Form mit c₁p₁/2. Alle Bedingungen sind von der Form „p\_irr klein gegen eine feste Zahl“ und gelten für kleines ρ.

**M3: Stufen für (G1″) und das Zählintervall.** Die Stufen stehen in der Tabelle M.2. Für (G1″) braucht Satz D die abgesenkte Schwelle.

**Lemma M3 [S].** Satz F10 gilt mit N\*(R) − 3n″ statt N\*(R) und c\_q/2 statt c\_q, sobald (ln(1/ρ))^{3/4} ≥ 6n″.

*Beweis.* In Schritt 1 des Beweises von Satz F10 heißt „verletzt“ jetzt n̄ ≥ N̄(R) + (ln(1/ρ))^{3/4} − 3n″ ≥ N̄(R) + ½ (ln(1/ρ))^{3/4}. Schritt 2 gibt dann den Exponenten λ · ½ (ln(1/ρ))^{3/4}; alles Übrige bleibt. ∎

**M4: Der Begegnungsradius.** Eine Zelle heißt *fern* von der Route von R, wenn sie in den Scheiben k − 1, k, k + 1 mehr als R\* Zellen von r\_{k−1}, r\_k, r\_{k+1} entfernt ist. Gewählt wird

```text
R*  =  Δ_R + D_K + R + 2D + 6
```

Dann liegt jedes von R geänderte Stück weiter als jede Reichweite der Tabelle M.2 von einer fernen Zelle entfernt, auch für die Auswahl über zwei Scheiben (Anhang L, L.5: 2D + 4). *Reihenfolge (Z.9):* D\_K steht nach n und D fest (F.12.6), R\* danach, dann α = c/(1 + R\*)² (Lemma S1), dann ε ≤ α/40. Weil D\_K ≫ D, ist α jetzt viel kleiner; für die Existenz ist das gleichgültig. Bisher (bis 2026-11-12) hieß es nur „R\* aus D“.

## M.4 Lemma M4: Stabilität [S, gegeben Lemma U4 und M1–M3]

S(X) sind die unbrauchbaren Raum-Zeit-Zellen des Zustands X mit den Schwellen der Stufe „Zeuge“, S₀(B) dieselben für B, S₁(B) die mit den Schwellen der Stufe „B“. B wird mit der Ausnahme-Konvention gezählt (Z.5): Die beiden Stücke an den offenen Enden sind nicht wählbar, aber gezählt. „Defekt“ ist Satz D mit den tatsächlichen Enden und den Schwellen der dritten Stufe.

**Lemma M4.** Seien m und ρ so, dass (ε/2) b₋ m ≥ n″ + 5, ε₁ b₋ m ≥ 8, b₋ m ≥ 4, n″ P^{br}\_treff + p\_irr ≤ p\* und (ln(1/ρ))^{3/4} ≥ 6n″. Dann gilt für jeden Zeugen (C, Ĉ) zu B:

1. **Einschluss.** S(C) ∪ S(Ĉ) ⊆ S₁(B) ⊆ {defekte Zellen}.
2. **Fern.** Für jede Zelle fern von der Route von R stimmen in C und B alle Tests überein, samt der Anzeigen „wählbar“ und „doppelt wählbar“ und der Auswahlgewichte; ebenso für Ĉ und B fern von der Route von R′.
3. **Voraussetzungen von Lemma P6.** Ist (Q, k) ∉ S(C), und unterscheidet sich ein Zustand X von C in Scheibe k nur in regulären Stücken, im Kasten von (Q, k) in höchstens n″ davon, so gilt im Kasten von (Q, k) in X die Bedingung (G1″) mit N\*, und jede Linie von X im Kasten erfüllt (G2\_A) und (G4′). Ebenso mit Ĉ statt C.

*Beweis.* Zu 1, für C (für Ĉ ebenso, mit R′ statt R): Sei (Q, k) ∉ S₁(B). Dann ist (Q, k) ∉ S(C), Test für Test.

- **Zählintervall:** n\_Q(C) und n\_Q(B) unterscheiden sich um ≤ 2 (M1 (4)), und [b₋m + 2, b₊m − 2] ± 2 ⊆ [b₋m, b₊m].
- **(iii):** Isolationsanzeigen sind gleich (M1 (4)); die Ausnahme-Enden ändern die Zahl um ≤ 2 ≤ ε₁b₋m/4.
- **Ausfallanteil:** Ein Stück mit Ende in Q, das in B wählbar mit Schwelle 2p\* und kein Ausnahme-Ende ist und das R nicht ändert, ist in C wählbar: Regularität und Isolation sind gleich, und nach Lemma U4 (4) ist es zugänglich, weil höchstens n″ geänderte, nach M2 reguläre Stücke mit isolierten Endpunkten in seiner Reichweite liegen. Also ist die Zahl der nicht wählbaren Stücke in C höchstens (ε/2) n\_Q(B) + n″ + 4 ≤ ε n\_Q(C).
- **(iv):** Nur geänderte Stücke können ihre Makro- oder Randanzeige ändern, ≤ n″ ≤ (ε/8) b₋m.
- **(v):** Die Zeitmittel in jedem Gitterquadrat ändern sich um ≤ n″, also folgt (G1″) mit N\* − n″ in C aus N\* − 2n″ in B. Jede Linie von C im Kasten ist eine Linie von B oder ein geändertes Stück; beide erfüllen (G2\_A) und (G4′) (B nach (v), geänderte Stücke nach M1 (3) und M2).

Für S₁(B) ⊆ defekt: Ersetzt man die Ausnahme-Enden durch die tatsächlichen, ändern sich höchstens zwei Stücke und ihre Endpunkte; jede Klausel der Stufe „B“ geht mit diesem Spielraum in die der Stufe „defekt“ über, für (G1″) nach Lemma M3.

Zu 2: Nach M1 (2) liegt jedes geänderte Stück im Ball vom Radius Δ s um die Routenzelle, nach M4 also außerhalb jeder Reichweite der Tabelle. Zugänglichkeit hängt mit cut nur von Stücken im Ball vom Radius Rs um E\_i ab (Anhang U, U.1); Kästen haben den Radius D\_K s; die Fortsetzung liegt in der Scheibe k + 1, die die Definition von „fern“ mit erfasst.

Zu 3: Im Kasten unterscheiden sich X und C in höchstens n″ Stücken (M1 (1)); die Zeitmittel ändern sich also um ≤ n″, also gilt (G1″) mit N\* aus N\* − n″. Linien im Kasten sind Linien von C (nach (v) regulär) oder eines der n″ regulären Stücke. ∎

*Was das ersetzt.* Lemma Z.5 [B nach OA] mit „Die Zählung ändert sich um höchstens 1“ und gleichem Zählintervall in S(C) und S₁(B); G.12.5 mit „gilt im Kasten jeder nicht defekten Zelle“; Z.3 mit derselben Formulierung. Punkt 3 gibt Z.3 genau die Voraussetzungen, die Lemma P6 verlangt.

## M.6 Teil 2: die Nenner (Z.2, Z.3, Z.4)

Stand 2026-11-13. Die drei Schritte laufen auf ein einziges Vergleichslemma hinaus (Lemma M5). Lemma P6 trägt dabei *alle* Stücke, auch die mit ihren eigenen Endpunkten; die Randschranke über die Zugänglichkeit (Lemma U4 (3)) wird in Z.3 nicht mehr gebraucht. Möglich ist das, weil Lemma M4 (3) die Voraussetzungen von Lemma P6 an jeder brauchbaren Zelle sichert.

### M.6.0 Bezeichnungen und Bedingungen

- **Bezugsgesetze.** Für ein Stück mit festen Endpunkten (S, E) ist ϖ\_i die freie Brücke der Dauer δ. Für das neue Stück eines Abwegs ist ϖ\_i = Q\_Y, die freie Rückwärts-Irrfahrt ab Y\_m; im Integranden steht dann zusätzlich 1{S′ ∈ G(Y\_m)} (G.12.9).
- **Normierer.** Für eine Menge G integrierter Stücke und eine Familie F fester Stücke derselben Scheibe sei

  ```text
  Z(G | F)  =  ∫ Π_{i∈G} dϖ_i  Π_{i∈G} 1{cut_i, reg_i}  ·  1{ die Stücke von G sind stoßfrei untereinander und mit F }
  ```

  mit reg = (G2\_A) und (G4′) der eigenen Bahn (M2). Z[l, O] aus Z.3 ist Z(l | L), Z[j, C] ist Z(j | L).
- **Untergrenze.** p\_P = ½ e^{−C′n} ist die Schranke von Lemma P6″ für Brücken mit |d|\_∞ ≤ (D + 10)s (F.12.6, Schritt 5); in Anhang F heißt sie p\*. Hier bleibt p\* die Schwelle der Zugänglichkeit aus Anhang U. p₁ und c₁ sind die Größen aus Lemma C (G.12.9). Sei

  ```text
  p  =  ½ min(p_P, c₁ p₁)
  (B1)  η_R  =  sup_i ϖ_i(cut verletzt)  ≤  min(p_P, c₁p₁)/4        (Bedingung an den cut-Radius R)
  (B2)  p_irr  ≤  min(p_P, c₁p₁)/4                                    (Lemma M2; gilt für kleines ρ)
  ```

- **Treffschranke.** P\_T = max(P^{br}\_treff, P^{neu}\_treff) mit P^{br}\_treff aus Anhang U, U.1 (Lemma F13 mit (W1)) und P^{neu}\_treff ≤ C D\_c² C\_P ln ln(1/ρ)/ln(1/ρ) für das neue Stück (F.12.6, Folgen für Lemma C). Beide gehen gegen 0.
- **Nahe Vorkommen.** J\_k ist die Zahl der nahen Vorkommen in Scheibe k, J = Σ\_k J\_k (genauer M.7.0). Jedes Stück einer Route, das ein Stück der anderen treffen kann, gehört zu einer Routenzelle, die ein nahes Vorkommen ist.
- **Lokale Paarzahl.** Ein Stück kann wegen cut nur Stücke treffen, deren Routenzelle höchstens 2Δ + 1 Zellen von seiner entfernt ist; das sind höchstens n\_loc = 6(4Δ + 3)² Stücke der anderen Route.

### M.6.1 Lemma M5: Vergleich zweier Normierer [S]

**Lemma M5.** Sei G = A ⊔ H, F eine stoßfreie Familie fester Stücke und F\_N ⊆ F. Für jedes i ∈ G und jede stoßfreie Familie X, die aus F, aus Stücken von G \ {i} mit cut und reg oder aus Teilen davon besteht, gelte

```text
(P)  ϖ_i( cut, reg, stoßfrei mit X )  ≥  p
(T)  ϖ_a( trifft f )  ≤  P_T        für a ∈ A und f ∈ F_N
```

N(a) sei die Zahl der f ∈ F\_N, die a wegen cut überhaupt treffen kann, und N\_P = Σ\_a N(a). Ist N(a) P\_T ≤ p/2 für alle a ∈ A, so gilt

```text
Z(G | F)  ≥  Z(A | F \ F_N) · p^{|H|} · exp( −2 N_P P_T / p )
```

*Beweis.*

1. **H der Reihe nach.** Nach Fubini ist Z(G | F) = ∫ Π\_{a∈A} dϖ\_a 1{A mit cut, reg, stoßfrei untereinander und mit F} · Z(H | F ∪ A). Auf diesem Ereignis ist F ∪ A stoßfrei. Man integriert die Stücke von H nacheinander; das jeweils nächste muss F, A und den schon gezogenen ausweichen, und nach (P) hat das die Masse ≥ p. Also Z(G | F) ≥ p^{|H|} Z(A | F).
2. **A gegen F\_N, eine Bedingung nach der anderen.** Sei A = {a₁, …, a\_r} und Z\_i das Integral von Z(A | F \ F\_N) mit den zusätzlichen Bedingungen „a\_j stoßfrei mit F\_N“ für j ≤ i; Z\_r = Z(A | F). Dann ist Z\_i/Z\_{i−1} = π^{(i−1)}(a\_i stoßfrei mit F\_N) mit dem normierten Gesetz π^{(i−1)} zu Z\_{i−1}. Dessen Bedingungen betreffen a\_i nur über (F \ F\_N) ∪ (A \ {a\_i}). Gegeben die übrigen Stücke hat a\_i also bezüglich ϖ\_{a\_i} die Dichte 1{cut, reg, stoßfrei mit (F \ F\_N) ∪ (A \ {a\_i})} geteilt durch die Masse dieses Ereignisses, und die Masse ist nach (P) ≥ p. Mit (T) ist π^{(i−1)}(a\_i trifft F\_N) ≤ N(a\_i) P\_T/p ≤ ½, also Z\_i/Z\_{i−1} ≥ 1 − N(a\_i) P\_T/p ≥ exp(−2N(a\_i) P\_T/p). Das Produkt über i gibt den Faktor. ∎

*Bis Teil 2 stand hier die Vereinigungsschranke über alle Paare auf einmal; sie brauchte N\_P P\_T ≤ p/2 für die ganze Scheibe. Das ist falsch, wenn der Weg einer Scheibe lang ist (M1 (1)). Die Fassung oben braucht die Kleinheit nur je Stück.*

### M.6.2 Folgerung M6 (Z.3, OA (29)) [S, gegeben Lemma P6″, Lemma C (c), Lemma F13 und Lemma M4]

**Folgerung M6.** In jeder Scheibe k gilt mit σ = 12 n\_loc P\_T/p, sobald n\_loc P\_T ≤ p/2:

```text
Z_{I′}(O)  ≥  Z[l, O] · p^{|h|} · e^{−σ J_k}
Z_I(O)     ≥  Z[j, C] · p^{|d|} · e^{−σ J_k}        (|d| ≤ 2|h|)
```

*Beweis.* Lemma M5, einmal mit A = l, H = h, F = O \ I′ = L ∪ j ∪ (d \ h), F\_N = j ∪ (d \ h); einmal mit A = j, H = d, F = O \ I = L ∪ l, F\_N = l. Zu prüfen sind (P), (T) und die Zahl der Paare.

- **(P).** Die Umgebung X unterscheidet sich von C (erste Zeile; die Route von R′ meidet S(C)) bzw. von Ĉ (zweite Zeile; die Route von R meidet S(Ĉ)) nur in regulären Stücken (M1, M2), im Kasten jeder Brücke in höchstens n″ davon; weggelassene Stücke zählen mit. Der Anfang jeder Brücke liegt höchstens D + 1 Zellen neben einer Routenzelle, nach der Verdickung um D′ = 2D + 2 (Anhang S, S.0) also in einer brauchbaren Zelle, und der Kasten B(S, R\_K) von Lemma P6″ liegt in deren Kasten vom Radius D\_K s. Nach Lemma M4 (3) gilt dort (U) aus F.12.1; die Endpunkte sind gut (M1 (3)), und |d|\_∞ ≤ (D + 2)s. Lemma P6″ gibt Ausweichen mit Wahrscheinlichkeit ≥ p\_P, Lemma C (c) für das neue Stück ≥ c₁p₁. Abzüglich cut und reg nach (B1), (B2) bleibt ≥ 2p − ½ min(p\_P, c₁p₁) = p.
- **(T).** Die Stücke von F\_N sind regulär (wählbare alte Stücke oder nach M2 gezogene) und haben isolierte Endpunkte, die von denen von a mehr als r entfernt sind. Also gilt die Definition von P^{br}\_treff bzw. die Schranke für Q\_Y.
- **Paare.** Ein Stück von A und eines von F\_N gehören zu verschiedenen Routen. N(a) ≤ n\_loc, und N(a) > 0 nur für Stücke, deren Routenzelle ein nahes Vorkommen ist; je Routenzelle gibt es höchstens 6 Stücke. Also N\_P ≤ 6 n\_loc J\_k, und Lemma M5 gibt den Faktor exp(−12 n\_loc P\_T J\_k/p) = e^{−σ J\_k}. ∎

*Gegenüber Z.3.* Dort stand exp(−C(K)|h| − σ\_ρ J) mit C(K) = δμ̄ + κ + C und σ\_ρ = C e^{δμ̄+κ} P\_treff, die Randschranke 2/p\* über die Zugänglichkeit für Stücke mit eigenen Endpunkten und eine Gruppierung naher Paare. Jetzt ist C(K) durch ln(1/p) ersetzt; das ist größer (p\_P ≈ e^{−C′K/θ}), aber fest. Die Gruppierung entfällt, weil Lemma M5 die Bedingungen einzeln hinzunimmt.

### M.6.3 Folgerung M7 (Z.4, OA (29a)) [S, gegeben wie M6]

**Folgerung M7.** Mit jn ⊆ j wie in Z.4 und den freien Gesetzen ϖ:

```text
Z( jn | L ∪ (j \ jn) )  ≤  p^{−|d|} e^{σ J_k} · Z( jn ∪ d | L ∪ (j \ jn) ∪ C_l )
```

Links stehen nur die Stoßbedingungen von jn mit j \ jn und L, rechts alle außer L–L. Das ist die Ungleichung von Z.4.

*Beweis.* Lemma M5 mit A = jn, H = d, F = L ∪ (j \ jn) ∪ C\_l, F\_N = C\_l. Die Umgebungen unterscheiden sich von Ĉ in höchstens n″ regulären Stücken (B unterscheidet sich von Ĉ nur in den Stücken von R′, und d wird frisch gezogen); C\_l sind wählbare alte Stücke von R′. Sonst wie M6. ∎

### M.6.4 Lemma M8 (Z.2, OA (28)) [S, gegeben (K1), (K2′)]

**Lemma M8.** Schreibt man das Gewicht jedes Stücks als W = e^{4δ} p\_δ(S, E) ϖ\_{S,E}, so heben sich im Summanden von Lemma G2 bzw. G.12.3 alle Faktoren e^{4δ} und alle Kerne gegen die des Bezugszustands B weg, außer den Kernen auf d. Dort bleibt

```text
K_C(d) K_Ĉ(d) / ( K_B(d) K_O(d) )  ≤  ( 4π e^{(Λ²+1)/2} )^{6|h|},        Λ = (9/8)(D + 4)
```

*Beweis.*

1. **Kerne aus den gezogenen Stücken.** Die Endpunkte der von R′ gezogenen Stücke stehen fest, also ist Z\_{I′}(O) = K\_O(I′) · Z(I′ | ·) und W(O\_{I′}) = K\_O(I′) ϖ(O\_{I′}); der Quotient ist kernfrei. Ebenso für Z\_I(O) mit K\_O(I) und für die alten Stücke von R mit K\_Ĉ. Beim neuen Stück eines Abwegs steht statt eines Kerns die Rückwärts-Irrfahrt Q\_Y, deren Gesamtmasse über S′ summiert 1 ist.
2. **Was übrig bleibt.** Im Zähler stehen die Kerne von C (aus P(C)) und die der alten Stücke von Ĉ, im Nenner die der Stücke von O auf I und, nach Umschreiben auf P(B), die von B. Nach der Tabelle in G.4 ist auf L, j und l jeweils eines der Zählerpaare gleich einem der Nennerpaare (C\_j = O\_j und Ĉ\_j = B\_j; C\_l = B\_l und l ∉ I). Es bleiben nur die Positionen von d.
3. **e^{4δ}.** Die Stückzahlen erfüllen #C + #Ĉ = #O + #B in jeder Scheibe, denn Ĉ entsteht aus O wie B aus C. Die Faktoren e^{4δ} heben sich also weg.
4. **Schranke.** Alle Endpunktpaare auf d haben |x|\_∞ ≤ Λs (M1 (2); die frische Paarung von B ist die Verschiebung längs der Kette von R, Abstand ≤ D + 2 Zellen, an der letzten geteilten Kopfscheibe ≤ D + 4, Lemma M14f (4)), und δ = s² ≥ 1. Λ = (9/8)(D + 4) deckt die Zellseiten bis 9s/8 aus der Pflasterung (Z.13); bis 2026-11-13 abends stand hier D + 2. Nach (K1) und (K2′) ist (4π)^{−1} e^{−1/2} (1 + δ)^{−1} e^{−Λ²/2} ≤ p\_δ(x) ≤ (1 + δ)^{−1}, also unterscheiden sich je zwei Kerne höchstens um den Faktor 4π e^{(Λ²+1)/2}. Im Quotienten stehen oben und unten gleich viele Kerne, höchstens 2|d| + 2 ≤ 6|h| (die zusätzliche Linie von Ĉ und B gegenüber O und C). ∎

### M.6.5 Zusammen

Mit Lemma M8, Folgerung M6 und M7 gilt der integrierte Kreuzvergleich Z.6 mit

```text
e^{C(K)|h| + 6σ J},        C(K)  =  6 ln(4π e^{(Λ²+1)/2}) + 5 ln(1/p),        σ  =  12 n_loc P_T / p  →  0
```

statt C(K) = δμ̄ + κ + C und σ\_ρ = C e^{δμ̄+κ} P\_treff. Der Exponent 5 von 1/p kommt aus |h| (M6, erste Zeile), |d| ≤ 2|h| (M6, zweite Zeile) und |d| ≤ 2|h| (M7); der Faktor 6 vor σ aus vier Normierern und zwei Anwendungen von M7 je Scheibe (M.7.1). Beide Größen sind fest bzw. gehen gegen 0; κ₀ steht in M.7.2.

**Neue Bedingungen.** (B1) an den cut-Radius: η\_R ≤ C e^{CΛ²} e^{−(R−Λ)²/C} (Brückenmaximum K3) muss ≤ min(p\_P, c₁p₁)/4 sein, also R − Λ ≳ (C′n)^{1/2}. R wird nach n, D\_c und D gewählt und vor R\*; das passt in die Reihenfolge von Z.9. (B2) und n\_loc P\_T ≤ p/2 gelten für kleines ρ.

**Lemma C (G.12.9).** Seine Voraussetzung „Die Zellen im Abstand ≤ D\_c + D von Y\_m seien nicht defekt“ ist wie in M1 zu lesen: brauchbar einschließlich Klausel (v). Nach der Verdickung (Anhang S, S.2) gilt das für alle Zellen im Abstand ≤ 2D + 2 vom Weg.

## M.7 Teil 3: der integrierte Kreuzvergleich (Z.6) und die Auswahlsummen (Z.8, erster Teil)

Stand 2026-11-13.

### M.7.0 Nahe Vorkommen und J

Ein *Vorkommen* ist eine Auswahl einer Route: eine Zelle c\_l in Scheibe k, in der ein Stück gewählt wird. Es heißt *nah*, wenn die Zelle nicht fern von der anderen Route ist (M4: in den Scheiben k − 1, k, k + 1 höchstens R\* Zellen von ihr entfernt), sonst *fern*. Ab hier ist

```text
J  =  Zahl der nahen Vorkommen beider Routen,        J_k  =  ihre Zahl in Scheibe k
```

Bisher zählte J die Begegnungszellen einer Scheibe. Die neue Zählung erfasst die Begegnungen über zwei Scheiben aus Anhang L, L.5, ohne eigene Regel. Folgerung M6 und M7 sind mit diesem J\_k formuliert. Wie J durch die Begegnungen der Skelette und die Brücken-Komponenten beschränkt wird, steht in Teil 4 (Lemma M12).

### M.7.1 Lemma M9 (integrierter Kreuzvergleich, OA Lemma 10.4) [S, gegeben Lemma M4, M6, M7, M8 und G3′]

Fest seien die Skelette, die Routen P, P′, die Tupel I, I′ und die verdeckten Daten (Loch- und Kopfplätze), außer den Köpfen S′ der Abwege: Sie gehören zum neuen Stück und werden mit ihm integriert (Bezugsgesetz Q\_Y). I\_{I,I′} sei das Integral des Summanden von G.12.3 über die übrigen Stücke.

**Lemma M9.**

```text
I_{I,I′}  ≤  e^{C(K)|h| + 6σJ} · 1_occ(B) · Π_{nahe Vorkommen v} [ (1 − 2ε)(n_{c(v)}(B) − 2) ]^{−1} · ∫ W(B) 1_G(B) H_F(B)
```

mit C(K) = 6 ln(4πe^{(Λ²+1)/2}) + 5 ln(1/p) und σ = 12 n\_loc P\_T/p aus M.6. Dabei ist

- 1\_occ(B) = 1{n\_c(B) ∈ [b₋m − 2, b₊m + 2] für alle Zellen beider Routen};
- 1\_G(B) = 1{P und P′ sind mit B verträglich}, das heißt: Es gibt einen Zeugen und eine Ersetzung der integrierten Stücke von B, für die P(Ĉ, γ) = P und P(C, γ′) = P′;
- H\_F(B) das Produkt der Auswahlfaktoren 1{wählbar}/g\_c der fernen Vorkommen, in B ausgewertet.

*Beweis.* Das Gewicht zerfällt nach Lemma 3.1 des Tutorials in Scheiben, sobald die Auswahlfaktoren durch Größen ersetzt sind, die nicht mehr von den integrierten Stücken abhängen (Schritt 1). Fern von allen Begegnungen gilt die exakte Kürzung G3′. In jeder Scheibe mit Begegnung geht man so vor:

1. **Auswahl und Route.** Ein fernes Vorkommen hat in C bzw. Ĉ denselben Faktor wie in B, für jeden Wert der integrierten Stücke (Lemma M4 (2)); das Produkt dieser Faktoren ist H\_F(B). Ein nahes Vorkommen liegt in einer brauchbaren Zelle des Zeugen. Dort gibt es mindestens (1 − 2ε) n\_c(X) doppelt wählbare Kandidaten (Lemma L2), und n\_c(X) ≥ n\_c(B) − 2 (M1 (4)). Also ist 1{wählbar}/g ≤ 1{cut, reg} · [(1 − 2ε)(n\_c(B) − 2)]^{−1}; die Indikatoren cut und reg bleiben stehen, weil wählbare Stücke regulär⁺ sind. Die Routenindikatoren sind ≤ 1 und auf jedem zulässigen Wert ≤ 1\_G(B), ebenso 1{Zellen brauchbar} ≤ 1\_occ(B). Lemma M4 gilt dabei für jede Ersetzung von B\_jn, B\_d mit cut und reg, weil diese Stücke wie die anderen geänderten Stücke regulär sind und isolierte Endpunkte haben.
2. **Kerne** (Lemma M8): Alle Gewichte werden als Kern mal Brückengesetz geschrieben. Es bleibt der Kernquotient auf d, ≤ e^{6 ln(4πe^{(Λ²+1)/2}) |h|}.
3. **Nenner** (Folgerung M6, für jede der höchstens vier Gruppen der Scheibe, Auf- und Abweg beider Routen): 1/Z\_{I′}(O) ≤ p^{−|h|} e^{σJ\_k}/Z[l, O] und 1/Z\_I(O) ≤ p^{−|d|} e^{σJ\_k}/Z[j, C]. Über die Gruppen summiert sind die Exponenten |h| und |d| ≤ 2|h|.
4. **Weglassen.** Alle Stoßbedingungen außer l–l, l–L (in O), j–j, j–L (in C), l–l, l–L (in C) und j–j, j–L (in Ĉ) werden weggelassen; das vergrößert das Integral.
5. **Integrieren.** O\_l gegen 1/Z[l, O] gibt 1, denn Z[l, O] = Z(l | L) ist genau dieses Integral. C\_j gibt Z(j | L) = Z[j, C], das den Nenner kürzt; auf j stehen cut und reg, weil die Brücken von R sie nach M2 erfüllen. Die Stücke C\_d, Ĉ\_d und O\_h geben je ≤ 1.
6. **Zurückholen** (Folgerung M7): Übrig sind C\_l = B\_l und Ĉ\_j = B\_j mit ihren eigenen Stoßbedingungen und denen mit L. Für j \ jn ist das Ausweichen vor l nach cut automatisch. Für jn gibt M7 den Faktor p^{−|d|} e^{σJ\_k} und stellt alle Bedingungen von B her, mit frisch gezogenem B\_d. Das Ergebnis ist das Gewicht W(B) auf dieser Scheibe.
7. **Zusammen:** je Scheibe e^{C(K)|h\_k|} und höchstens sechs Faktoren e^{σJ\_k} (vier aus Schritt 3, zwei aus Schritt 6). ∎

*Gegenüber Z.6.* Dort stand „Beweis wörtlich wie OA“ und der Faktor [(1 − 2ε) n\_Q]^{−1}. Neu sind die Zählung n\_c(B) − 2 (die Zeugen zählen um bis zu 2 anders), die Indikatoren cut und reg, die in Schritt 5 und 6 gebraucht werden, und 1\_G als Verträglichkeit statt als Liste. Die Listen (Zahl der verträglichen Routenpaare) braucht erst Z.8.

### M.7.2 Lemma M10 (Auswahl summieren, OA §10.5) [S, gegeben Lemma M9]

**Lemma M10.** Bei festem B, festen Skeletten und festen verträglichen Routen P, P′ gilt für die Summe über die Tupel, ohne die beiden Endzellen a und b,

```text
Σ_{I, I′}  e^{C(K)|h| + 6σJ} · Π_{nahe v} [ (1 − 2ε)(n_{c(v)}(B) − 2) ]^{−1} · H_F(B)   ≤   e^{κ₀ J}
κ₀  =  3ε  +  6σ  +  (e^{2C(K)} + 4) / (b₋m − 4)        (ε ≤ 1/10)
```

*Beweis.*

1. **Tupel als Auswahl in B.** Die Stücke, die R in Ĉ wählt, sind Stücke von B (B\_j = Ĉ\_j, auf d frisch), und die Stücke, die R′ in C wählt, sind auf l Stücke von B (B\_l = C\_l). Bei festem B ist ein Tupelpaar also eine Wahl von Stücken von B in den Zellen der Vorkommen. Mit Ende in der Zelle c stehen höchstens n\_c(B) + 2 Stücke zur Wahl.
2. **Ferne Vorkommen.** Der Faktor in H\_F(B) ist 1{wählbar in B}/g\_c(B). Die Summe über die Wahl ist genau 1.
3. **Nahe Vorkommen.** Die Summe über die Wahl ist ≤ (n + 2)/((1 − 2ε)(n − 2)) mit n = n\_c(B) ≥ b₋m − 2 (wegen 1\_occ), also ≤ (1 − 2ε)^{−1}(1 + 4/(n − 2)) ≤ exp(2,5ε + 4/(b₋m − 4)).
4. **Geteilte Stücke.** Ein Stück von h ist eine Brücke, die beide Routen haben; ihr Anfang ist der Anfang eines Stücks, das beide in derselben Zelle gewählt haben (Endpunkte zur Zeit t\_k bezeichnen Teilchen eindeutig). Jede solche gemeinsame Wahl gibt höchstens zwei Stücke von h. Schreibt man den Faktor als Π (1 + (e^{2C(K)} − 1) 1{gemeinsame Wahl}), so kostet jede Zelle mit nahen Vorkommen beider Routen in der Doppelsumme über die beiden Wahlen höchstens 1 + (e^{2C(K)} − 1)/(n + 2) ≤ exp((e^{2C(K)} − 1)/(b₋m − 4)). Man rechnet das einem der beiden nahen Vorkommen zu.
5. **Zusammen** je nahem Vorkommen höchstens exp(2,5ε + 6σ + (e^{2C(K)} + 3)/(b₋m − 4)) ≤ e^{κ₀}. ∎

*Gegenüber Z.8.* Dort stand je Begegnung (1 − 2ε)^{−4} ≤ e^{10ε}, weil J die Begegnungen zählte und je Begegnung bis zu vier nahe Vorkommen auftreten. Mit J als Zahl der nahen Vorkommen ist der Anteil 2,5ε je Vorkommen; die Bedingung an κ₀ steht in Teil 4 (M.8.4).

### M.7.3 Was von Z.8 noch fehlt

- **Endzellen a und b:** gemeinsamer Schwanz (e^{C(K)}/n\_a) und das Teilen des Kopfstücks über mehrere Scheiben (Lemma C (e), Faktor ≤ 2 für m ≥ 2C/(c₁p₁)). Die Rechnung steht in Z.8; sie ist mit M9 und M10 verträglich, ausgeschrieben ist sie nicht.
- **Listen** (OA Lemma 10.3), **seltene Komponenten** mit Z.7 und **Skelette** mit Lemma S1: jetzt Teil 4, Lemma M11–M13 und M.8.4.
- **Bezugsmaß** µ\_ab mit Lemma C (d): offen.

## M.8 Teil 4: Listen, die Zahl J und seltene Komponenten (Z.8, zweiter Teil)

Stand 2026-11-13. Hier zeigt sich eine Feinheit der Umweg-Regel aus Lemma S2: Liegt das Skelett in einem großen gefüllten Klumpen, so hängt die Lage r\_k vom ganzen Klumpen ab und die Strecke von r\_k nach r\_{k+1} von einer flächigen Umgebung. Zählt man alle schlechten Komponenten dieser Umgebung, versagt die Peierls-Summe: Ein Klumpen der Größe p kostet nur q^p, die Fläche um ihn enthält aber etwa q p² schlechte Zellen. Deshalb zählt b\_tot unten nur die Komponenten auf *einer* Strecke, mit dem Maximum über die möglichen Strecken.

### M.8.0 Die Größen eines Skeletts in einer Scheibe

𝔅₁ ist S₁(B), räumlich verdickt um D′ (Anhang S, S.0). Komponenten sind je Scheibe über Kanten zusammenhängend; F(T) ist die Füllung der einzelnen Komponente T, und diam F(T) ≤ |T| (Anhang S, S.2). F\_k(𝔅) ist die Vereinigung der Füllungen aller Komponenten von 𝔅 in Scheibe k (seit 2026-11-13 abends wie OA, Review 2026-11-13, W2; bis dahin die gemeinsame Füllung von ganz 𝔅\_k). Für eine Hälfte eines Skeletts mit den Grundlagen b\_k sei, mit F\_k = F\_k(𝔅₁):

- **Klumpen.** P\_k ist das Stück von F\_{k−1} ∪ F\_k, das b\_k enthält (leer, wenn b\_k außerhalb liegt), und p\_k die Summe der |T| über die Komponenten, deren Füllungen P\_k bilden. ϱ\_k = 2p\_k + 1 ≥ diam P\_k + 1.
- **Strecken.** Seg\_k ist die Menge der Strecken σ(x, y) (fest gewählte Kantenwege, Anhang S, S.2) mit |x − b\_k|\_∞ ≤ ϱ\_k und |y − b\_{k+1}|\_∞ ≤ ϱ\_{k+1}; ist p\_k = 0, so ist nur x = b\_k zugelassen, ebenso für y.
- **Masse auf der Strecke.** s\_k ist das Maximum über Seg\_k der Summe der |T| über die Komponenten von 𝔅₁ in Scheibe k, deren Füllung die Strecke trifft. (Das schließt die Komponenten ein, die die Strecke selbst trifft, und ist damit eine obere Schranke für die Summe in Lemma S2 (3).)
- **Masse und Bereich.** β\_k = p\_k + p\_{k+1} + s\_k, summiert über beide Hälften. W\_k ist die Vereinigung der Komponenten, die zu p\_k, p\_{k+1} oder zu s\_k für irgendeine Strecke beitragen. Reg\_k ist der ℓ∞-Ball um b\_k vom Radius ℓ\_k = ℓ⁰ + 4p\_k + 4p\_{k+1} + 7s\_k ≤ ℓ⁰ + 7β\_k mit ℓ⁰ = Δ + D + 9.

**Lemma M11a (Lage und Abhängigkeit) [S, gegeben Lemma S2].** Sei 𝔅 ⊆ 𝔅₁ eine beliebige schlechte Menge (etwa 𝔅(C) oder 𝔅(Ĉ)). Dann liegt die Route einer Hälfte in Scheibe k, samt Umsteigeketten und geänderten Stücken, in Reg\_k, und W\_k ⊆ Reg\_k. Bei festen Endpunktdaten hängt sie nur von 𝔅 ∩ W\_k ab.

*Beweis.*

1. **Füllungen sind monoton.** Jede Komponente T von 𝔅 liegt in einer Komponente T₁ von 𝔅₁, und F(T) ⊆ F(T₁): Liegt x in einer endlichen Komponente des Komplements von T und nicht in T₁, so ist seine Komponente im Komplement von T₁ darin enthalten, also endlich. Also ist F\_k(𝔅) ⊆ F\_k(𝔅₁), und jede Füllung von 𝔅 liegt in der Füllung einer Komponente von 𝔅₁.
2. **Lage.** Das Stück P\_k(𝔅) mit b\_k liegt in P\_k, also ist |r\_k − b\_k| ≤ ϱ\_k (Lemma S2 (2)), ebenso für r\_{k+1}. Die Strecke σ(r\_k, r\_{k+1}) liegt in Seg\_k und im umschreibenden Kasten von r\_k und r\_{k+1}, also im Abstand ≤ 2 + ϱ\_k + ϱ\_{k+1} von b\_k (|b\_{k+1} − b\_k|\_∞ ≤ 2). Nach S2 (3) liegt jede Wegzelle höchstens s\_k + 1 Zellen von der Strecke entfernt, also höchstens 3 + ϱ\_k + ϱ\_{k+1} + s\_k von b\_k. Mit dem Stück j₀ (Ende ≤ D + 1 Zellen von r\_k), den Ketten und den geänderten Stücken (Δ, M1 (2)) folgt die Lage. (Bis 2026-11-13 abends lief dieser Schritt über die Weglänge; mit dem Kantenweg wäre sie doppelt so groß, die Lage ändert sich nicht.) Jede Komponente in W\_k liegt höchstens 2 + ϱ\_k + ϱ\_{k+1} + s\_k von b\_k entfernt.
3. **Abhängigkeit.** r\_k hängt nur von P\_k(𝔅) ab, und dessen Komponenten liegen in Komponenten, die P\_k bilden. Der Weg hängt nur von den Komponenten von 𝔅 ab, die die Strecke trifft (S2 (4)); jede liegt in einer Komponente von 𝔅₁, die die Strecke trifft, also in W\_k. ∎

### M.8.1 Lemma M11 (Listen, OA Lemma 10.3) [S, gegeben Lemma S2 und M4]

Eine Scheibe k heißt *nah*, wenn Reg\_k einer Hälfte des einen Skeletts von Reg\_{k′} einer Hälfte des anderen für ein k′ ∈ {k − 1, k, k + 1} höchstens R\*₂ = R\* + D′ + 1 Zellen entfernt ist. Sei

```text
b_tot  =  Σ_{k nah} ( β_k(γ) + β_k(γ′) )
```

**Lemma M11.** Bei festem B, festen Skeletten und festen Endpunktdaten gibt es höchstens e^{4 b\_tot} verträgliche Routenpaare (P, P′).

*Beweis.*

1. **Was B festlegt.** 𝔅(C) ⊆ 𝔅₁, und 𝔅(C) stimmt mit 𝔅₀(B) (S₀(B) verdickt) auf allen Zellen überein, die weiter als R\* + D′ von der Route von R entfernt sind (Lemma M4 (1), (2), dazu die Verdickung). Die Route von R liegt in ∪ Reg(γ) (Lemma M11a mit 𝔅(Ĉ) ⊆ 𝔅₁).
2. **Ferne Scheiben.** Ist k nicht nah, so liegt W\_k(γ′) ⊆ Reg\_k(γ′) weiter als R\*₂ von Reg(γ) in den Scheiben k − 1, k, k + 1. Dort ist 𝔅(C) = 𝔅₀(B), also ist die Route von R′ in Scheibe k nach M11a durch B bestimmt.
3. **Nahe Scheiben.** Die Route von R′ in Scheibe k ist durch r′\_k, r′\_{k+1} und 𝔅(C) auf den Komponenten bestimmt, deren Füllung die Strecke trifft. Für r′\_k gibt es eine Möglichkeit, wenn p′\_k = 0, sonst höchstens (4p′\_k + 3)² ≤ e^{4p′\_k}; ebenso für r′\_{k+1}. Auf den Komponenten der Strecke hat 𝔅(C) höchstens 2^{s′\_k} Möglichkeiten. Zusammen ≤ e^{4β′\_k}. Ebenso für R mit 𝔅(Ĉ). ∎

### M.8.2 Lemma M12 (die Zahl J) [S, gegeben Lemma M11a]

J₀″ sei die Zahl der Paare (Scheibe k, Paar von Hälften), für die die Grundlagen höchstens R\*″ = R\*₂ + 2ℓ⁰ Zellen auseinander liegen, für ein k′ ∈ {k − 1, k, k + 1}.

**Lemma M12.** Für jedes verträgliche Routenpaar gilt J ≤ C\_J (J₀″ + b\_tot) mit C\_J = 12D + 138 (bis 2026-11-13 abends: 12D + 90, mit der Weglänge d\_∞ statt 2d\_∞ aus der alten Fassung von Lemma S2).

*Beweis.* Nahe Vorkommen sind Routenzellen in nahen Scheiben. Eine Hälfte hat in Scheibe k nach Lemma S2 (3) höchstens 2(2 + ϱ\_k + ϱ\_{k+1}) + 6s\_k + 1 = 9 + 4p\_k + 4p\_{k+1} + 6s\_k Weg- und D + 2 Kettenzellen, also ≤ 6β\_k + D + 11. In einer nahen Scheibe gibt es damit höchstens 6(β\_k(γ) + β\_k(γ′)) + 4(D + 11) nahe Vorkommen. Ist eine Scheibe nah, aber β in ihr und in den Nachbarscheiben null, so haben die Bereiche den Radius ℓ⁰, und die Grundlagen liegen höchstens R\*″ auseinander; solche Scheiben zählt J₀″. Jede andere nahe Scheibe hat in ihrem Fenster eine nahe Scheibe mit β > 0; davon gibt es höchstens b\_tot, also höchstens 3 b\_tot solche Scheiben. Zusammen J ≤ 4(D + 11)(J₀″ + 3b\_tot) + 6b\_tot ≤ C\_J (J₀″ + b\_tot). ∎

### M.8.3 Lemma M13 (seltene Komponenten) [S, gegeben Z.7]

Sei d\_k der kleinste Abstand der Grundlage b\_k (einer Hälfte von γ) zu den Grundlagen von γ′ in den Scheiben k − 1, k, k + 1, und

```text
S  =  Σ_{k, Hälften}  e^{−d_k / 7}        (weiches Begegnungsmaß der Skelette)
```

**Lemma M13.** Zu C₂ ≥ 0 gibt es q₀ > 0 und ϑ(q) → 0 (q → 0), sodass für q ≤ q₀ und feste Skelette gilt

```text
E_{µ_ab}[ e^{C₂ b_tot} ]  ≤  (C/M_Z²) · exp( ϑ(q) S )        (M_Z = M/s² Zellen, M.9.2)
```

*Beweis.*

1. **Abstand.** Ist k nah, so ist d\_k ≤ R\*″ + 7 M\_k mit M\_k = Σ der β beider Skelette über die Scheiben k − 1, k, k + 1, denn Reg hat den Radius ≤ ℓ⁰ + 7β.
2. **Entwickeln.** e^{C₂ b\_tot} ≤ Π\_k (1 + (e^{C₂ M\_k} − 1) 1{M\_k ≥ max(1, (d\_k − R\*″)/7)}). Ausmultipliziert ist das eine Summe über Mengen K′ von Scheiben, je mit dem Produkt der Klammerterme.
3. **Strukturen.** M\_k > 0 verlangt schlechte Komponenten: Klumpen (eine Kette sich berührender Füllungen mit einer Füllung, die b\_k enthält, wie in Anhang S, S.3, Schritt 3 und 4) und die Komponenten auf einer Strecke aus Seg\_k. Man schätzt e^{C₂ s\_k} durch die Summe über die höchstens e^{4(p\_k + p\_{k+1})} Strecken ab. Auf einer festen Strecke (Kantenweg mit ≤ 2(2 + ϱ\_k + ϱ\_{k+1}) Schritten) wählt man die Ankerzellen (≤ 2^{Länge}) und die Formen (≤ 11^{|T|} zusammenhängende Mengen mit gegebener Zelle). Ketten der Gesamtgröße p gibt es ≤ C^p (S.3, Schritt 4 und 5). Also gibt es zu gegebener Masse M höchstens C₉^M Strukturen.
4. **Wahrscheinlichkeit.** Eine verdickte Komponente T enthält ≥ |T|/(2D′ + 1)² rohe Zellen von S₁(B); verschiedene Komponenten sind disjunkt. Jede Komponente kommt in höchstens 36 der Strukturen vor (drei Scheiben im Fenster, zwei Scheiben je Klumpen, zwei Hälften, zwei Skelette). Nach Z.7 ist die Wahrscheinlichkeit, dass alle gewählten Strukturen schlecht sind, ≤ (C/M²) Π\_{k∈K′} q₃^{M\_k} mit q₃ = q^{1/(144 (2D′+1)²)}.
5. **Summe.** Mit x = C₉ e^{C₂} q₃ ≤ e^{−1} trägt jede Scheibe k ∈ K′ höchstens ϑ\_k = Σ\_{M ≥ max(1, (d\_k − R\*″)/7)} x^M ≤ 2x · e^{1 + R\*″/7} e^{−d\_k/7} bei. Die Summe über K′ ist Π\_k (1 + ϑ\_k) ≤ exp(Σ\_k ϑ\_k) = exp(ϑ(q) S) mit ϑ(q) = 2x e^{1 + R\*″/7}. Der Vorfaktor C/M² steht nur einmal. ∎

### M.8.4 Zusammensetzen (Z.8 ohne die Endzellen) [S, gegeben M9–M13 und Lemma S1 mit dem weichen Maß]

Für feste Endzellen (a, b) und feste Skelette gibt Lemma M9 mit M10 für jedes verträgliche Routenpaar die Schranke e^{κ₀ J} ∫ W(B) 1\_G; die Summe über die Routenpaare steht unter dem Integral. Mit M11 und M12 ist sie

```text
≤  e^{κ₀ C_J J₀″} · ∫ e^{(4 + κ₀ C_J) b_tot} dµ_ab   ≤   (C/M_Z²) · e^{κ₀ C_J J₀″ + ϑ(q) S}
```

nach M13 mit C₂ = 4 + κ₀C\_J ≤ 5. Hölder über die Skelette und Lemma S1 (für J₀″ mit dem Radius R\*″, für S mit K = 7; OA (25)) geben E\_{γ,γ′}[…] ≤ C, sobald

```text
κ₀  ≤  α_J  :=  α(R*″) / (4 C_J)        und        2 ϑ(q)  ≤  ξ
```

Mit κ₀ = 3ε + 6σ + (e^{2C(K)} + 4)/(b₋m − 4) heißt das: ε ≤ α\_J/6, und σ, 1/m, q klein, also ρ klein.

*Was offen bleibt:* die Endzellen a und b und das Zurückgewinnen des Bezugsmaßes, also die Rechnung Σ\_{(a,b)} (Vorfaktoren) · C/M\_Z² ≤ C mit Lemma C (d), (e). Stand und Restsatz in M.9.

## M.9 Teil 5: Endzellen und Bezugsmaß (Z.8, Rest): Stand und offener Restsatz

Stand 2026-11-13. Grundlage ist OA §10.5 („Summing the comparison“, „Recovering the reverse insertion“), im Volltext nachgelesen.

### M.9.1 Die Vorlage bei OA

1. **Labelsummen je Zelle.** Gewöhnliche gemeinsame Zelle 1 + (e^C − 1)/n\_Q; erste Zelle a: ein gemeinsames Label, e^C/n\_a; letzte Zelle b: das Label des ersten Tupels ist festgelegt, [1 + (e^C − 1)/n\_b]/n\_b. Zusammen (C/m²) e^{κ₀J}.
2. **Hilfspunkt.** Der Hilfspunkt z in b kommt sonst nicht mehr vor; sein Integral gibt 1/M (bei OA ist M die Zahl der Zellen).
3. **Vorfaktor.** Mit dem Vorfaktor m der Dichte ist m/(m²M) = 1/N.
4. **Bezugsmaß.** Summe über das letzte Label und Integral über den Hilfspunkt x in a geben *genau* µ\_ab. Nach OA Satz 7.3 ist µ\_ab ≤ C/M², und es gibt höchstens M² geordnete Zellpaare.

### M.9.2 Korrektur der Bezeichnung [S]

Bei OA ist M die Zahl der Zellen und V das Volumen. In diesem Projekt ist M = |Λ| die Zahl der Plätze. Z.7, G.11.2 und Lemma M13 haben „C/M²“ von OA übernommen. Zu lesen ist das als C/M\_Z² mit der Zahl der Zellen M\_Z = M/s², also C s⁴/M² in Platz-Bezeichnung. Probe mit G.11.2, Schritt 3: µ\_ab(Ω) ≤ (NM)^{−1} ⟨a\*(1\_a) a(1\_b)⟩ ≤ (NM)^{−1} s² C m = C s⁴/M². Die Zahl der geordneten Zellpaare ist M\_Z², das Produkt also eine Konstante wie bei OA.

### M.9.3 Wo unsere Enden anders sind

| Ende                 | OA                                                                    | hier                                                                                       |
|----------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Schwanz (Zelle a)    | Hilfspunkt x gleichverteilt im Volumen, dann ein wählbares Label in a | Schwanz-Teilchen gleichverteilt unter allen N; verworfen, wenn sein Stück nicht regulär    |
| Kopf (Zelle b)       | Hilfspunkt z gleichverteilt im Volumen ist der neue innere Endpunkt   | Kopf S′ des Abwegs in der untersten Scheibe, aus dem bedingten Gesetz im Ball (Variante c) |
| Vorfaktor der Dichte | m                                                                     | M (G.12.2, exakt geprüft)                                                                  |
| Teilen am Kopf       | ein festes Label                                                      | geteilte Kopfscheiben, je ≤ 1/(c₁p₁), Fortsetzung je Scheibe mit Wahrscheinlichkeit ≤ C/m  |

**Bewiesen sind:** die Kopfdichte P(S′ = y) ≤ C/(c₁p₁s²) (Lemma C (d)); die Kosten einer geteilten Kopfscheibe ≤ 1/(c₁p₁) (Lemma C (e)); am Schwanz ist das Gesetz unseres Schwanz-Teilchens auf brauchbaren Zellen bis auf den Faktor g\_a/m ∈ [(1 − ε) b₋, b₊] dasselbe wie das von OA (Zelle mit Wahrscheinlichkeit s²/M, dann ein wählbares Label mit 1/g\_a).

### M.9.4 Der offene Restsatz [B nach OA]

*Nachtrag 2026-11-13:* bewiesen in M.9.5 bis M.9.9 (Lemma M14a bis M14e), gegeben die Lemmata von Anhang M, Lemma C, C′, P6″ und Satz D.

**Restsatz M14.** Für jedes zulässige Endzellenpaar und feste Skelette ist die Summe der End-Vorfaktoren (Vorfaktor der Dichte, Wahl des Schwanzes, Labelsummen in a und b, Verteilung des Kopfes und geteilte Kopfscheiben) höchstens C mal das Gewicht, mit dem µ\_{ab′} in M.8.4 eingeht, summiert über die ≤ (2D\_c + 1)² Zellen b′ im Ball um die Endzelle.

Zu zeigen ist dafür:

1. die Gleichung „Vorfaktor × Endsummen × Hilfsintegral = 1/N“ in unserer Bezeichnung. Der Vorfaktor ist M statt m, und statt des Hilfspunkts z gibt es den Kopf aus Variante c;
2. dass sich das Teilen des Kopfstücks je Scheibe nur mit Wahrscheinlichkeit ≤ C/m fortsetzt; das steht in G.12.7 nur als Behauptung.

**Vorschlag.** Den Schwanz wie bei OA wählen: Hilfspunkt x gleichverteilt im Volumen, das Schwanz-Teilchen gleichverteilt unter den wählbaren Stücken der Zelle von x. Dann überträgt sich die Schwanzseite von OAs Rechnung wörtlich, und Regel 3 aus Anhang L (Verwerfen bei irregulärem Schwanzstück) wird überflüssig, weil wählbare Stücke regulär sind. Eigene Rechnung braucht dann nur noch die Kopfseite, mit Lemma C (d) und (e) an der Stelle von OAs Hilfspunkt z.

### M.9.5 Der Schwanz wie bei OA, und die Rechnung (2026-11-13)

**Änderung der Konstruktion.** Basis ist C ~ P zusammen mit einem Hilfspunkt ξ, gleichverteilt auf Λ; a ist die Zelle von ξ. Verworfen wird, wenn ξ zur Zeit 0 nicht gut ist (ein Teilchen im Abstand ≤ r) oder wenn a keinen Schwanz-Kandidaten hat. Das Schwanz-Teilchen wird gleichverteilt unter den g⁰\_a(C) Teilchen gewählt, die zur Zeit 0 in a sitzen und deren Stück in Scheibe 0 regulär ist. Alles Übrige bleibt. Regel 3 aus Anhang L (Verwerfen bei irregulärem Schwanzstück) entfällt, weil das Schwanzstück jetzt regulär gewählt wird. In brauchbaren Zellen ist g⁰\_a ≥ (1 − ε/2) n\_a(0) nach den Klauseln (iii) und (iv).

**Erweitertes Zielmaß.** µ̃(dO, dξ) = µ(dO) · s^{−2} 1{ξ in der Zelle des Schwanzes}, mit derselben Masse N₀/N. ν̃ ist das Gesetz von (O, ξ) und f̃ = dν̃/dµ̃. Weil f = E[f̃ | O], ist ∫f² dµ ≤ ∫f̃² dµ̃ (Jensen); OA hält den Hilfspunkt ebenso als Koordinate fest.

**Lemma M14a (Dichte) [S].** Mit der Zahl A der zulässigen Endzellen zu a gilt

```text
f̃(O, ξ)  =  (N s² / A) · Σ_R  (1/g⁰_a(Ĉ)) · π(γ | a, b) · Π sel(Ĉ) · Π W(alt)/Z
```

*Beweis.* Wie G1 und G.12.2. In ν̃ stehen für die Enden (1/M) (Hilfspunkt), 1/g⁰\_a(C) (Schwanz) und 1/A (Endzelle), in µ̃ steht W(O)/(NMZ\_N) · s^{−2}. Der Quotient der Vorfaktoren ist N s²/A, und der Schwanzfaktor wird wie alle Auswahlfaktoren im hypothetischen Zustand Ĉ ausgewertet. ∎

*Nachtrag 2026-11-13: exakt nachgerechnet [N]* ([pruef\_m14a.py](pruef_m14a.py), aus pruef\_zeitschleife\_spiegel.py, Ausgaben in ergebnisse/pruef\_m14a.txt). Am Mini-Ring gilt ν̃ = f̃ µ̃ mit größtem relativem Fehler 1,7·10⁻¹⁵, für N = 1 bis 3, w = 1 und 2, mit und ohne Pflicht-Querschritt, Isolationsradius r = 0 und 1, bis 2,4 Millionen Paare (O, ξ). Regulär heißt dort: Das Stück beginnt und endet in derselben Zelle. Ausgeschrieben gehören zur Formel die Indikatoren 1{ξ gut} (hängt nur von O ab) und 1{Schwanzstück in Ĉ regulär}; oben stecken sie in 1/g⁰\_a(Ĉ) und in der Annahme.

**Die Faktoren an den Enden.** Im zweiten Moment ∫f̃ dν̃ stehen außer den Faktoren des Inneren (Lemma M9–M13):

| Faktor                                       | Herkunft                                                                                             | Größe                       |
|----------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------|
| N s²/A                                       | Vorfaktor von f̃ (Lemma M14a)                                                                         | N s²/A                      |
| 1/A                                          | Endzelle b′ von R′                                                                                   | Summe über b′: ≤ A Terme    |
| (1/M) Σ\_ξ                                   | Hilfspunkt; wird zum neuen Anfang (Kopf) von B in a                                                  | geht in N µ\_ab ein (unten) |
| Σ\_x (1/g⁰(C))(1/g⁰(Ĉ)) e^{C(K)}             | gemeinsames Schwanz-Label beider Routen                                                              | ≤ 2e^{C(K)}/((1 − ε) b₋m)   |
| 1/g\_b(Ĉ), das Label j\_m von R in Scheibe 0 | durch O festgelegt (die Linie von O durch den Kopf), also nicht summiert; R′ wählt dasselbe Teilchen | ≤ 2e^{C(K)}/((1 − 2ε) b₋m)  |
| p\_δ(y, Y) des Kopfstücks von R              | R normiert über alle Anfänge (Q\_Y), sein Stück hat den festen Anfang y                              | ≤ C/s² nach (K1)            |
| geteilte Kopfscheiben darüber                | Lemma C (e) je Scheibe ≤ 1/(c₁p₁), Fortsetzung nur bei gemeinsamer Wahl (Lemma M10)                  | ≤ 2                         |
| Σ\_b                                         | Endzelle von R liegt ≤ D\_c + 1 Zellen von der Zelle von y, diese ≤ D\_c von b′                      | ≤ (4D\_c + 3)² Terme        |

**Rechnung.** Mit (1/M) Σ\_ξ ∫ W(B)/Z\_N = (1/M) · NM · µ\_ab = N µ\_ab (B mit Kopf ξ in a und Schwanz in der Zelle b) ergibt das Produkt der Vorfaktoren

```text
(N s²/A) · (1/A) · (C e^{C(K)}/m) · (C e^{C(K)}/m) · (C/s²) · N  =  C e^{2C(K)} (N/m)² / A²  =  C e^{2C(K)} M_Z² / A²  ≤  C e^{2C(K)} / υ²
```

wegen N/m = M\_Z und A ≥ υ M\_Z. Die Summe über a, b′ und b hat höchstens M\_Z · A · (4D\_c + 3)² Glieder, und jedes ist nach M.8.4 höchstens (C/M\_Z²) · E[…] ≤ C/M\_Z². Zusammen ist ∫f̃² dµ̃ ≤ C e^{2C(K)} (4D\_c + 3)²/υ, eine Konstante. Alle Potenzen von m, s, M\_Z und A heben sich weg.

**Stand [B nach OA, Größen und Rechnung geprüft].** Die Bilanz der Vorfaktoren ist vollständig, und jeder Faktor hat eine benannte Quelle. Nicht ausgeschrieben ist der Vergleich in den beiden Endscheiben im Stil von Lemma M9:

- **Schwanz:** Das Stück von R aus x wird in B auf den Hilfspunkt ξ umgehängt und frisch gezogen. Das kostet wie ein Stück von d den Faktor 1/p, dazu den Kernquotienten aus M8.
- **Kopf:** B fehlt die Linie längs D. Es ist zu zeigen, dass das Kopfstück und das festgelegte Label genau die beiden letzten Zeilen der Tabelle liefern.

Das ist dieselbe Technik wie M5–M9, aber mit der Endgeometrie von B. Wenn es dort klemmt, dann bei der genauen Lage des Schwanzes von B in b.

**Die Schwierigkeit am Kopf, genauer.** B ist C mit den Schritten von R rückgängig und hat längs D eine Linie weniger als C. Fern von R′ ist die Linie, die R in O als eingefügt liest, eine Linie von C; B fehlt sie. Unten fallen aber die Abwege beider Routen zusammen: Die Linie von O ab dem Kopf y ist das neue Stück von R′, und R liest sie als sein eigenes. In C gibt es dort keine Linie, denn y ist in C frei. Also ist B auf dem gemeinsamen Stück gleich C, und die fehlende Linie beginnt erst dort, wo die beiden Abwege auseinandergehen, zur Zeit t\_k mit k ≥ 1. B hat dann seinen Schwanz zur Zeit t\_k und nicht zur Zeit 0. µ\_ab (OA, G.11.2) setzt beide offenen Enden auf dieselbe Zeit.

Zwei mögliche Wege:

1. **Bezugsmaß mit Schwanz zur Zeit t\_k.** µ\_ab mit dem Schwanz zur Zeit t\_k definieren und die Übertragung G.11.2 dafür beweisen. Der Hilbert–Schmidt-Schluss bekommt dann den Faktor e^{−t\_k H} zwischen den Enden. Die Fortsetzung des Teilens kostet je Scheibe ≤ C/m (Lemma M10), die Summe über k ist also beschränkt.
2. **Gemeinsames Kopfstück auflösen.** B auch am Kopf umhängen wie am Schwanz: Das gemeinsame Kopfstück von R wird in B durch ein frisch gezogenes Stück ab einem zweiten Hilfspunkt in b ersetzt. Dann liegt der Schwanz von B zur Zeit 0, wie bei OA mit dem Hilfspunkt z. Dafür müsste die Konstruktion am Kopf einen Hilfspunkt bekommen, oder man vergleicht mit Lemma C (d) gegen einen gleichverteilten Punkt im Ball.

Der zweite Weg liegt näher an OA und ändert nur B, nicht die Konstruktion, wenn Lemma C (d) als Vergleich genügt.

**Weg 2 geprüft (2026-11-13): trägt allein nicht.** Stimmen die verdeckten Kopflagen von R und R′ zur Zeit t\_1 überein, so beginnt das neue Stück von R in Scheibe 1 am selben Punkt wie das von R′. R liest dann die Linie von O ab diesem Punkt, also wieder das eingefügte Stück von R′. Das Teilen setzt sich so über die Scheiben 0, …, k − 1 fort, mit Wahrscheinlichkeit ≤ C/m je Scheibe (Lemma M10). Auf diesem ganzen Stück ist B gleich C, und der Schnitt von B liegt zur Zeit t\_k. Ein Hilfspunkt am Kopf wie OAs z erledigt nur den Fall k = 0; OA hat eine einzige Scheibe und kennt die Fortsetzung nicht.

**Also Weg 1, mit diesem Plan.**

1. **Bezugsmaß µ\_ab^{(k)}:** offene Konfigurationen B mit dem Kopf (Anfang der zusätzlichen Linie) zur Zeit 0 in a und dem Schwanz (Ende der fehlenden Linie) zur Zeit t\_k in b. In Operatoren ist das (NMZ\_N)^{−1} Spur(e^{−(β−t\_k)H} a\*(1\_a) e^{−t\_k H} a(1\_b) …); zwischen 0 und t\_k läuft der Sektor mit N + 1 Teilchen.
2. **Übertragung (wie G.11.2):** Der Hilbert–Schmidt-Schluss trennt die beiden Einfügungen wie bisher; e^{−t\_k H} ist nach Abzug von e^{−t\_k ε\_N} eine Kontraktion. Zu erwarten ist µ\_ab^{(k)}(E) ≤ (C/M\_Z²) e^{−t\_k (ε\_{N+1} − ε\_N)} P\_cl(E)^{1/4}. Der Energiefaktor hilft, denn ε\_{N+1} − ε\_N ≥ ε\_N/N ≥ c₁ρY > 0 (Lemma 6.6).
3. **Summe über k:** Jede weitere geteilte Kopfscheibe kostet ≤ 1/(c₁p₁) (Lemma C (e)) und tritt mit Wahrscheinlichkeit ≤ C/m ein. Die Reihe Σ\_k (C/(c₁p₁ m))^k ist für m ≥ 2C/(c₁p₁) höchstens 2, wie schon in Z.8 angesetzt.
4. **Bilanz:** Die Tabelle oben gilt für jedes k, mit der Kopfzelle b in Scheibe k statt 0.

Zu prüfen ist vor allem Schritt 2: dass der Beweis von OA Satz 7.3 die Zeitverschiebung zwischen den beiden Enden verträgt.

**Schritt 2 versucht (2026-11-13): eine weitere Hürde.** OAs Beweis (Volltext nachgelesen) schreibt µ\_ab(E) als Spur mit beiden Einfügungen zur Zeit 0 und dem getesteten Kern danach. Hilbert–Schmidt-Cauchy–Schwarz trennt die Einfügungen. Im zweiten Faktor ersetzt man nur den adjungierten Kern durch den ungetesteten; das gibt Z\_N E\_cl[n\_a 1\_E] und damit P\_cl(E)^{1/2}. Mit dem Schwanz zur Zeit t\_k sitzt die Vernichtung a(1\_b) *im* getesteten Fenster:

```text
µ_ab^{(k)}(E)  ∝  Spur_{N+1}( K₁ a*(1_a) e^{−(β−T)H} K₂ a(1_b) ),        K₁ auf [0, t_k] mit N + 1 Teilchen,  K₂ auf [t_k, T]
```

E zerfällt in E₁ auf [0, t\_k] und E₂ auf [t\_k, T], weil Defekte scheibenweise erklärt sind. Cauchy–Schwarz trennt wieder. Der Faktor mit K₁ ist ein (N + 1)-Teilchen-Ausdruck mit dem Anfangszustand a\*(1\_a)ψ\_N und nicht das geschlossene N-Teilchen-Maß. Ersetzt man dort den Kern durch den ungetesteten, gewinnt man den Energiefaktor e^{−2t\_k(ε\_{N+1} − ε\_N)} und ⟨a a\*⟩ ≤ 2s²m (G.8.3). Man verliert aber die Kleinheit von E₁, und zwar für *alle* Zellen der Scheiben 0, …, k − 1, nicht nur am Kopf. Dann ist die Summe über seltene Komponenten (Lemma M13) in diesen Scheiben nicht mehr beschränkt.

**Mögliche Auswege** (nicht ausgeführt):

1. Satz D für das (N + 1)-Teilchen-Maß mit Anfangszustand a\*(1\_a)ψ\_N. Die Dichteschranken gelten gleichmäßig in der Teilchenzahl (§11), aber der Anfangszustand ist nicht der Grundzustand.
2. Für k ≥ 1 in den Scheiben 0, …, k − 1 auf die Kleinheit verzichten und die Komponenten dort anders beschränken. Für k ≥ 1 steht der Faktor (C/m)^k zur Verfügung, aber die Entropie ganzer Scheiben schluckt ihn nicht.
3. Die Konstruktion so ändern, dass sich das Kopfstück nicht über die unterste Scheibe hinaus teilt, etwa indem R′ in Scheibe 1 nie dasselbe Teilchen wählt wie das, das R lesen würde. Das ist mit der Dichteformel schwer verträglich.

**Stand:** Restsatz M14 bleibt [B nach OA]. Die Faktorbilanz ist geprüft, der Schwanz ist erledigt (Hilfspunkt), offen ist allein der Kopf bei geteilten Kopfscheiben (k ≥ 1). Für k = 0 trägt Weg 2 (Hilfspunkt am Kopf). Die Dichteformel Lemma M14a ist mit dem neuen Schwanz noch nicht am Mini-Ring nachgerechnet; G.12.2 war es für den alten. *Nachtrag 2026-11-13:* Die Hürde bei k ≥ 1 ist in M.9.6 beseitigt (Ausweg 1, Lemma M14b).

### M.9.6 Der späte Schnitt: Satz D in Normform trägt (2026-11-13)

Zählweise wie in M.9.5 und der Übergabe: k ist die Zahl der übereinstimmenden verdeckten Kopflagen. Geteilt sind dann die neuen Stücke der Scheiben 0, …, k, und der Schnitt von B liegt zur Zeit t\_k. Die Prüfprogramme geben K = k + 1 aus, die Länge der gemeinsamen Kopfkette.

**Erst geprüft: Machen die Beiträge mit k ≥ 1 ein Problem? [N]**

Zerlegt wird ∫f² dµ = ∫f dν nach k. ν wird nach den Kopflagen H′ der bauenden Route R′ aufgeteilt, f(O) nach den verdeckten Kopflagen H der auswertenden Route R. K(H, H′) ist die Zahl der übereinstimmenden Kopflagen von unten; die Kopflage zur Zeit 0 ist der Kopf y und stimmt immer überein, die zur Zeit t\_w ist die Wende.

- **Mini-Ring** ([pruef\_kopfteilen.py](pruef_kopfteilen.py), abgeleitet aus pruef\_zeitschleife\_spiegel.py, exakt, Dichteformel dabei mit Fehler ≤ 10⁻¹⁵): Mit einem Teilchen und mit Pflicht-Querschritt ist die Kopfkette immer ganz geteilt (K = w + 1). Dort gibt es je Zelle fast nie mehr als ein wählbares Stück, die Wahl von R ist also erzwungen. Ohne Pflicht-Querschritt (N = 2, w = 2) sind die Anteile 0,16, 0,22 und 0,62 für K = 1, 2, 3. Der Mini-Ring kann die Unterdrückung durch 1/m also nicht zeigen (ergebnisse/pruef\_kopfteilen.txt).
- **Testmodell auf dem 2D-Torus** ([pruef\_kopfteilen2d.py](pruef_kopfteilen2d.py), Monte Carlo wie zeitschleife2d.py, Variante c mit Radius 3 und Pflicht-Querschritt, Grundzustand, S = 8, Läufe mit [kopfteilen2d\_start.sh](kopfteilen2d_start.sh), Ausgaben in ergebnisse/kopfteilen2d/): f exakt je Probe, die Zerlegung wird gegen f geprüft (Fehler ≤ 2·10⁻¹⁵).

| System                 | m    | w   | Proben | ∫f²dµ       | Teil mit k = 0 | Anteil k ≥ 1 | A(K) für K = 1, 2, … (letzte: Teilen bis zur Wende) |
|------------------------|------|-----|--------|-------------|----------------|--------------|-----------------------------------------------------|
| 4×4, Zellen 2×2, N = 4 | 1,00 | 3   | 6093   | 2,00 ± 0,03 | 0,90 ± 0,01    | 0,55 ± 0,01  | 0,90 / 0,55 / 0,32 / 0,23                           |
| 6×4, Zellen 2×2, N = 6 | 1,00 | 2   | 2895   | 3,33 ± 0,12 | 1,69 ± 0,07    | 0,49 ± 0,02  | 1,69 / 1,01 / 0,62                                  |
| 6×4, Zellen 2×2, N = 6 | 1,00 | 3   | 707    | 3,42 ± 0,25 | 1,51 ± 0,10    | 0,56 ± 0,03  | 1,51 / 1,04 / 0,54 / 0,32                           |
| 6×4, Zellen 2×2, N = 6 | 1,00 | 4   | 1064   | 4,10 ± 0,38 | 1,69 ± 0,12    | 0,59 ± 0,03  | 1,69 / 1,04 / 0,80 / 0,37 / 0,20                    |
| 4×4, Zellen 2×2, N = 6 | 1,50 | 3   | 3411   | 2,24 ± 0,10 | 1,12 ± 0,03    | 0,50 ± 0,01  | 1,12 / 0,63 / 0,32 / 0,18                           |
| 6×4, Zellen 3×2, N = 6 | 1,50 | 2   | 2891   | 3,96 ± 0,13 | 1,80 ± 0,06    | 0,54 ± 0,02  | 1,80 / 1,30 / 0,86                                  |
| 6×4, Zellen 3×2, N = 6 | 1,50 | 3   | 812    | 5,02 ± 0,35 | 2,05 ± 0,16    | 0,59 ± 0,03  | 2,05 / 1,29 / 1,10 / 0,58                           |
| 6×4, Zellen 3×2, N = 6 | 1,50 | 4   | 1226   | 6,41 ± 1,23 | 2,40 ± 0,46    | 0,63 ± 0,07  | 2,40 / 1,64 / 0,96 / 0,92 / 0,48                    |
| 4×4, Zellen 2×2, N = 8 | 2,00 | 3   | 2648   | 0,83 ± 0,04 | 0,37 ± 0,02    | 0,55 ± 0,02  | 0,37 / 0,24 / 0,14 / 0,08                           |
| 6×4, Zellen 6×2, N = 6 | 3,00 | 2   | 5998   | 4,63 ± 0,16 | 1,88 ± 0,06    | 0,59 ± 0,01  | 1,88 / 1,14 / 1,61                                  |
| 6×4, Zellen 6×2, N = 6 | 3,00 | 3   | 2312   | 6,34 ± 0,52 | 1,77 ± 0,12    | 0,72 ± 0,02  | 1,77 / 1,89 / 1,28 / 1,40                           |
| 6×4, Zellen 6×2, N = 6 | 3,00 | 4   | 2132   | 8,48 ± 0,61 | 1,70 ± 0,11    | 0,80 ± 0,01  | 1,70 / 1,86 / 2,23 / 1,05 / 1,63                    |

Statistische Fehler: Standardfehler des Mittels; A(K) ist der Beitrag mit genau K gemeinsamen Kopflagen, absolut.

- **Größe.** Die Beiträge mit k ≥ 1 machen bei m = 1 bis 3 die Hälfte bis vier Fünftel von ∫f² aus.
- **Wo das Wachstum mit w sitzt.** Der Teil mit k = 0 ist über w im Rahmen der Fehler konstant (m = 1: 1,69; 1,51; 1,69). Das Wachstum von ∫f² mit w, das Z.11 im kleinen Modell gesehen hat, steckt in den geteilten Kopfketten.
- **Abfall mit K.** Mit vier oder sechs Zellen fällt A(K) geometrisch, mit dem Quotienten 0,5 bis 0,8 je Scheibe, im Mittel etwa 0,6. Am 4×4-Torus ändert er sich von m = 1 bis m = 2 nicht. Die Reihe über K bleibt dann beschränkt, und das Wachstum mit w ist ihr Auffüllen (m = 1: 3,33; 3,42; 4,10, Grenzwert grob 1,7/(1 − 0,6) ≈ 4). Mit nur zwei Zellen (m = 3) führt der Pflicht-Querschritt beide Routen in dieselbe Zelle; dort fällt A(K) nicht, und ∫f² wächst etwa linear in w.
- **Kein Abfall wie 1/m sichtbar.** Bei m ≤ 3 ist das wie in Z.11 nicht zu erwarten. Gebremst wird die Fortsetzung im Modell vor allem durch verschiedene Routen, nicht durch die Wahl unter vielen Stücken.
- **Folgerung.** Die Beiträge mit k ≥ 1 sind kein Randeffekt, und weglassen kann man sie nicht. Im Beweis muss jede weitere geteilte Scheibe einen kleinen Faktor η ~ 1/m tragen, denn auf die Routen ist kein Verlass (nahe der Kopfzelle laufen beide Skelette zusammen), und das Bezugsmaß muss die Defekt-Kleinheit auch vor t\_k behalten. Beides leistet das Folgende. Die Bedingung an m liegt weit außerhalb dessen, was das Modell erreicht.

**Der Ausweg: Satz D ist eine Normschranke.** Alle Ein-Grund-Schranken von Satz D sind als Produkte von Operatornormen je Scheibe bewiesen: satz\_3\_9 §9.3, Schritte 1 und 2; §10.4 für D4 und D7; Folgerung 11.2 und §12.3 für D1; §12.2 für D2; Satz F7 mit Lemma 6.8 für D6; Satz U, Schritt 7, für D5. Eine Normschranke hängt nicht vom Anfangszustand ab. Den Grundzustand braucht der Beweis nur an den beiden Zeiträndern, wo die Kippungen zu einer Zeit abgeschätzt werden. Die Energiebilanzen (§10.6, §11, §12.2, §12.3, Anhang F, F.8, Anhang U, U.5) sind für jede Teilchenzahl geführt, also auch für N + 1. Damit trägt Ausweg 1 der Übergabe, und zwar ohne ein geschlossenes Maß mit N + 1 Teilchen.

**Bezugsmaß mit spätem Schnitt.** Grundzustandsform wie in satz\_3\_9 §10.4: ψ = ψ\_N ≥ 0 ist der normierte Grundzustand von ℒ\_N = H + 4N mit der Energie ε\_N; ε\_{N+1} ist die Grundenergie mit N + 1 Teilchen. Für 0 ≤ k ≤ w, Zellen a, b und ein Ereignis E auf den Bahnen des Fensters (0, T) sei

```text
µ_ab^{(k)}(E)  =  (N M)^{−1} e^{T ε_N} ⟨ψ, K^E_{[t_k, T]} a(1_b) K^E_{[0, t_k]} a*(1_a) ψ⟩
```

Dabei ist K^E\_{[s, t]} der getestete Kern (Weltliniengewichte auf [s, t], auf E eingeschränkt), auf [0, t\_k] im Sektor N + 1. µ\_ab^{(0)} ist µ\_ab aus G.11.2 in Grundzustandsform. Die Zustände B aus M.9.5 mit k übereinstimmenden Kopflagen haben genau dieses Gewicht: eine zusätzliche Linie ab (ξ, 0) in a, das Ende einer Linie zur Zeit t\_k in der Zelle b des Schnitts, auf [0, t\_k) also N + 1 Linien.

**Lage des Schnitts, genau (2026-11-13) [B]; seit 2026-11-13 abends Lemma M14f [S] in M.9.10.** Sei s = k die letzte Scheibe mit gemeinsamem neuen Stück ν und p = j\_m das Teilchen über dem Ende Y\_m von ν; beide Routen haben p, denn O legt es fest. Unterhalb von t\_s sind die Stücke beider Routen dieselben, dort ist B bis auf Umbenennung gleich C. In Scheibe s trennen sich die Ketten. Zählt man die Endpunkte der Stücke von B in Scheibe s gegen C, so fehlt oben das Ende Y\_0^R (dort beginnt in Scheibe s + 1 das neue Stück von R, das B nicht hat), und unten muss ein Anfang fehlen. Man nimmt in Scheibe s

```text
d  =  h ∪ pred_I(h) ∪ pred_{I′}(h)        (bei OA und in M9: h ∪ pred_I(h))
```

lässt den Anfang S\_m von p weg und zieht die übrigen Stücke von d frisch, mit den Enden, die nach j, l und L noch fehlen; darunter ist Y\_m. Dann ist B konsistent, und die Linie von B, die von unten bei (S\_m, t\_s) ankommt, endet dort. Der Schnitt liegt also zur Zeit t\_s = t\_k an einem Platz, der Anfang eines wählbaren Stücks und damit isoliert ist, höchstens D + D\_c + 1 Zellen von der Kopflage zur Zeit t\_k (|S\_m − Y\_m| ≤ Ds, |Y\_m − S′| ≤ D\_c s). Für k = 0 ist das die Zeit 0, also µ\_ab^{(0)} = µ\_ab; einen Hilfspunkt am Kopf (Weg 2) braucht man nicht.

*Warum pred\_{I′}(h).* Mit d = h ∪ pred\_I(h) allein geht es nicht immer. Wählt R in Scheibe s nur p und R′ eine längere Kette, so ist q′ = pred\_{I′}(p) ein Stück von l mit B = C, und sein Ende ist das O-Ende von p, also Y\_0^R. Dann endet in B eine Linie bei (Y\_0^R, t\_{s+1}), der Schnitt läge zur Zeit t\_{s+1}. Lemma M14b deckt auch diesen Fall; mit q′ in d bleibt aber die Zählung der Übergabe (Schnitt zur Zeit t\_k). Der Preis: In dieser einen Scheibe ist |d| ≤ 3|h| statt 2|h|. In Folgerung M6, M7 und Lemma M10 kostet das dort e^{3C(K)} statt e^{2C(K)} je gemeinsamer Wahl, einen festen Faktor.

**Lemma M14b (Übertragung mit spätem Schnitt) [S, gegeben die Ein-Grund-Schranken von Satz D (§12.4) für N und für N + 1 Teilchen; dass sie für N + 1 mit denselben Konstanten gelten, steht in satz\_3\_9 §9.3, Schritt 6].** Sei 1 ≤ k ≤ w, 𝒜 eine Menge von Raum-Zeit-Zellen des Fensters, 𝒜₁ ihr Teil in den Scheiben 0, …, k − 1 und 𝒜₂ der Rest. Dann gilt

```text
µ_ab^{(k)}( alle Zellen von 𝒜 defekt )  ≤  (C/M_Z²) · e^{−t_k (ε_{N+1} − ε_N)} · q₊^{|𝒜₁|} · q^{|𝒜₂|/4}
```

mit q aus Satz D und einer Rate q₊(ρ) → 0, die wie q aus den Ein-Grund-Schranken entsteht. Insbesondere gilt Z.7 für µ^{(k)} in derselben Form, mit max(q, q₊⁴) statt q.

*Beweis.*

1. **Zerlegen zur Zeit t\_k.** Defekte sind scheibenweise erklärt (satz\_3\_9, Lemma 9.0). Also ist {alle Zellen von 𝒜 defekt} = E₁ ∩ E₂; E₁ hängt nur von den Bahnen auf [0, t\_k] ab, mit den Enden zur Zeit t\_k vor der Vernichtung, und E₂ nur von denen auf [t\_k, T]. Mit den elementweise nichtnegativen Vektoren χ = a\*(1\_b) (K₂^{E₂})\* ψ und φ = a\*(1\_a) ψ ist µ\_ab^{(k)}(E) = (NM)^{−1} e^{Tε\_N} ⟨χ, K₁^{E₁} φ⟩. Für F ≥ 0 auf den Bahnen von [0, t\_k] ist ν(F) = ⟨χ, K₁^F φ⟩ ein positives Maß.
2. **Mischen der Gründe** wie §9.3, Schritt 3: 𝒜₁ wird nach dem ersten zutreffenden Grund in höchstens 7 Teile 𝒜₁^g zerlegt (≤ 7^{|𝒜₁|} Zerlegungen), und Hölder für ν mit Exponent 7 gibt ν(Π\_g 1\_{E^g}) ≤ Π\_g ν(1\_{E^g})^{1/7}; für nicht benutzte Gründe steht ν(1)^{1/7}, und ν(1) hat nach Schritt 3 bis 5 (ohne Kippung) denselben Vorfaktor.
3. **Ein Grund.** Exponential-Markov wie in Satz D: 1\_{E^g} ≤ e^{−λ\_g θ\_g |𝒜₁^g|} e^{λ\_g N\_g}. (Für D5 läuft das über Binomialmomente, Satz U, und für D6 über Ausdünnen und die Summe über Zuordnungen, Satz F10. Auch das sind elementweise Majorisierungen durch Produkte nichtnegativer Scheibenoperatoren, und der Rest des Schritts gilt wörtlich; Review 2026-11-13, H1 (c).) Der Beweis von Satz D majorisiert den mit e^{λ\_g N\_g} getesteten Kern elementweise durch R\_t · T\_{k−1} ⋯ T\_0 · R\_0. Die T\_j sind die gekippten bzw. gefärbten Scheibenoperatoren; R\_0 und R\_t sind die diagonalen Randhälften der Kippung zu den Zeiten 0 und t\_k. Sie gibt es nur bei den Gründen mit Zählungen zu festen Zeiten, D1 und D2; D6 ist zeitgemittelt (Lemma 6.8), D4, D5 und D7 sind gefärbte Operatoren, dort ist R\_0 = R\_t = 1. Nach den Energiebilanzen gilt im Sektor N + 1 ‖T\_j‖ ≤ e^{−δ ε\_{N+1}} e^{c\_g |𝒜₁^g ∩ Scheibe j|}. Also ist ν(1\_{E^g}) ≤ e^{−(λ\_g θ\_g − c\_g) |𝒜₁^g|} e^{−t\_k ε\_{N+1}} ‖R\_t χ‖ ‖R\_0 φ‖.
4. **Rand zur Zeit 0.** Ein zusätzliches Teilchen ändert jede Zählgröße A der Kippung um höchstens λ, also e^{A/2} a\*(1\_a) ≤ e^{λ/2} a\*(1\_a) e^{A/2} elementweise. Mit a(1\_a) a\*(1\_a) ≤ s² (n\_a + 1) (harte Bosonen, G.8.3) folgt ‖R\_0 φ‖² ≤ e^{λ} s² E\_ψ[(n\_a + 1) e^{A}] ≤ C s² m e^{c|𝒜₁|}, mit Hölder und Satz 3.9 (a), (b) bzw. (c) zu einer Zeit.
5. **Rand zur Zeit t\_k, der geschlossene Faktor.** Ebenso ist ‖R\_t χ‖² ≤ e^{λ} s² ⟨(K₂^{E₂})\* ψ, (n\_b + 1) e^{A} (K₂^{E₂})\* ψ⟩. Ersetzt man einen der beiden Kerne durch den ungetesteten e^{−(T−t\_k)ℒ\_N} (alles ≥ 0, wie bei OA), so wird das ≤ e^{λ} s² e^{−2(T−t\_k)ε\_N} E\_cl[(n\_b(t\_k) + 1) e^{A(t\_k)} 1\_{E₂}]. Hölder mit (E\_cl(n\_b + 1)⁴)^{1/4} (E\_cl e^{4A})^{1/4} P\_cl(E₂)^{1/2} und Satz 3.9 zu einer Zeit (λ\_g notfalls kleiner als in Satz D) geben ≤ C s² m e^{c|𝒜₁|} e^{−2(T−t\_k)ε\_N} P\_cl(E₂)^{1/2}, und P\_cl(E₂) ≤ q^{|𝒜₂|} nach Satz D, erste Zeile.
6. **Zusammen.** Die Zeitfaktoren geben e^{Tε\_N} e^{−(T−t\_k)ε\_N} e^{−t\_k ε\_{N+1}} = e^{−t\_k(ε\_{N+1} − ε\_N)}, die Vorfaktoren (NM)^{−1} C s² m = C s⁴/M² = C/M\_Z² (M.9.2). Für λ\_g θ\_g groß gegen c\_g + c entsteht wie in §9.3, Schritt 4, die Rate q₊ → 0; die 7^{|𝒜₁|} Zerlegungen stecken darin. ∎

*Warum der Versuch in M.9.5 scheiterte.* Dort wurde im Faktor mit K₁ der getestete Kern durch den ungetesteten ersetzt, wie OA es für das geschlossene Maß tun muss; das kostet E₁. Hier bleibt K₁ getestet, und die Kleinheit kommt aus den Normen. Der Anfangszustand a\*(1\_a)ψ\_N geht nur über die Ein-Zeit-Schranke am Rand ein, im Kern ‖a\*(1\_a)ψ\_N‖² ≤ 2s²m. Den Energiefaktor e^{−t\_k(ε\_{N+1} − ε\_N)} ≤ 1 (Lemma 6.6 des Tutorials) braucht man nicht.

**Folgerung M14c [S, gegeben Lemma M14b].** Lemma M13 und das Zusammensetzen M.8.4 gelten wörtlich mit µ\_ab^{(k)} statt µ\_ab. Der Beweis von M13 benutzt vom Bezugsmaß nur Z.7, und Lemma M14b gibt Z.7 für µ^{(k)} in derselben Form. Lemma M4 und M11 bleiben gültig: B mit spätem Schnitt hat wie bisher zwei Ausnahme-Enden (den Kopf ξ zur Zeit 0 und den Schnitt zur Zeit t\_k), und die Ausnahme-Konvention behandelt beide wie in M4.

**Bilanz für k ≥ 1 [B nach OA, wie für k = 0].** Gegenüber k = 0 kommen je weiterer geteilter Kopfscheibe j = 1, …, k hinzu:

| Faktor                        | Herkunft                                                                                                  | Größe                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------|
| Label j\_m von R in Scheibe j | durch O festgelegt (die Linie von O über dem Ende des gemeinsamen neuen Stücks), also nicht summiert; M10 | ≤ e^{2C(K)}/((1 − 2ε)(b₋m − 2))              |
| Kehrwert des Normierers       | Lemma C (e)                                                                                               | ≤ 1/(c₁p₁)                                   |
| Bezugsmaß                     | µ\_{a b\_k}^{(k)} statt µ\_ab (Lemma M14b, Folgerung M14c)                                                | dieselbe Schranke (C/M\_Z²) e^{ϑS}           |
| Zelle b\_k des Schnitts       | liegt auf der Route von R in Scheibe k, also in Reg\_k (Lemma M11a)                                       | ersetzt durch Lemma M14e: ≤ 9 e^{ℓ⁰}, C₂ + 7 |

Zur letzten Zeile: Man summiert über b\_k mit 1{b\_k ∈ Reg\_j} ≤ e^{ℓ\_j − d(b\_k, b\_j)} und ℓ\_j ≤ ℓ⁰ + 7β\_j; die β\_j der geteilten Scheiben gehören zu b\_tot, weil beide Skelette dort nah sind. Mit η = e^{2C(K)}/((1 − 2ε)(b₋m − 2) c₁p₁) ist der Beitrag aller k ≥ 0 zusammen höchstens C e^{ℓ⁰} Σ\_k (k + 1) η^k mal der Schranke für k = 0, und Σ\_k (k + 1) η^k = (1 − η)^{−2} ≤ 2 für η ≤ 1/4. Das ersetzt in der Tabelle von M.9.5 die Zeile „geteilte Kopfscheiben darüber ≤ 2“ und in M.9.5, Weg 1, Schritt 3 die Begründung. Die Bedingung (1 − 2ε)(b₋m − 2) c₁p₁ ≥ 4e^{2C(K)} ist von derselben Art wie m ≥ 2C/(c₁p₁) aus Z.8 und gilt für kleines ρ.

**Stand von Restsatz M14 [B nach OA].** Die Hürde bei k ≥ 1 ist beseitigt: Das Bezugsmaß mit spätem Schnitt behält die Defekt-Kleinheit in allen Scheiben (Lemma M14b [S, gegeben Satz D]), und die Reihe über k konvergiert. Offen bleibt dasselbe wie für k = 0: der Vergleich in den beiden Endscheiben, im Stil von Lemma M9 ausgeschrieben (Schwanz: Umhängen auf ξ wie bei OA mit dessen Hilfspunkt x; Kopf: festgelegtes Label, Kopfstück, die frisch gezogene Gruppe d der letzten geteilten Scheibe). Die Faktoren dieses Vergleichs stehen in den Tabellen von M.9.5 und oben, jeder mit Quelle. Für k = 0 liegt der Schnitt zur Zeit 0 (Lage des Schnitts, oben), also µ\_ab^{(0)} = µ\_ab ohne Hilfspunkt am Kopf. Die Dichteformel Lemma M14a ist am Mini-Ring exakt nachgerechnet (Nachtrag in M.9.5). *Nachtrag:* Die Abweichungen der Endscheiben von M9 stehen vollständig in M.9.7, dort auch die Fortsetzung am Schwanz.

### M.9.7 Der Vergleich in den Endscheiben (2026-11-13)

Hier werden die Abweichungen der Endscheiben von Lemma M9 vollständig aufgezählt, für jede Zahl geteilter Scheiben an beiden Enden. Dabei kommt eine Lücke von M.9.5 ans Licht: Auch am Schwanz kann sich das Teilen fortsetzen.

**Was an den Enden anders ist als in M9.** Lemma M9 benutzt in jeder Scheibe zweierlei. Erstens gilt #C + #Ĉ = #O + #B für die Zahl der Stücke, und die Kerne heben sich bis auf d paarweise weg (Lemma M8, Schritte 2 und 3). Zweitens wird B auf d frisch gezogen, mit Endpunkten, die C, Ĉ und O vorgeben. An den Enden gilt beides nicht wörtlich. Das neue Stück ν eines Abwegs hat in O keinen Kern, sondern die Rückwärts-Irrfahrt Q\_Y mit Gesamtmasse 1 (M8, Schritt 1), und B hat an seinen beiden offenen Enden ein Stück mehr oder weniger. Alles andere in M9 gilt unverändert: Lemma M4 bis M7, Lemma C (c) und (e) für ν, Lemma P6″.

**Fortsetzung am Schwanz.** Im Aufweg ist der Lochplatz h\_{j+1} zur Zeit t\_{j+1} für R verdeckt und wird über die freien Plätze summiert (G.12.2), mit dem Kern des alten Stücks, das dort endet. Stimmt er mit dem Lochplatz h′\_{j+1} von R′ überein, so beginnt in Scheibe j + 1 das gelöschte Stück beider Routen am selben Platz, und das Teilen setzt sich fort. k\_T sei die Zahl der übereinstimmenden verdeckten Lochplätze. Ist k\_T ≥ 1, so liefe die zusätzliche Linie von B, die bei (ξ, 0) beginnt und der Route von R folgt, durch (h′\_1, t\_1), wo auch C eine Linie hat. M.9.5 hatte nur k\_T = 0 betrachtet.

*Frühere Abhilfe (bis 2026-11-13; trug nicht, Review 2026-11-13, W1; ersetzt durch den späten Anfang in M.9.11).* In den Scheiben 0, …, k\_T − 1 ist B = C bis auf Umbenennung, dazu ein frisch gezogenes Stück der zusätzlichen Linie: Sie beginnt bei (ξ, 0) und endet zur Zeit t\_{k\_T} an einem isolierten freien Platz P, über den summiert wird. In Scheibe k\_T wird B auf d frisch gezogen, mit P statt des gemeinsamen Lochplatzes als zusätzlichem Anfang. So bleibt die Erzeugung von B für jedes k\_T bei (ξ, 0), und das Bezugsmaß ist weiter µ\_ab^{(k\_H)} aus M.9.6 mit der Zahl k\_H der geteilten Kopflagen; Lemma M14b deckt es. Das frische Stück braucht in Lemma M5 die Untergrenze (P). Ein Stück mit festem Anfang und freiem Ende ist das zeitlich gespiegelte neue Stück von Variante c; Lemma C (c) gibt die Dichte ≤ 1/(c₁p₁) bezüglich der freien Irrfahrt ab ξ bzw. ab dem vorigen P.

**Stückzahlen und Kerne in den Endscheiben.** Gezählt wird in der Umgebung des jeweiligen Endes, n = Zahl der Stücke von C dort. „Kerne übrig“ ist die Zahl der Kerne mit festen Endpunkten im Zähler (aus C und Ĉ) minus der im Nenner (aus O und B). ν und die frischen Stücke mit freiem Ende tragen keinen Kern, sondern die Masse 1. Jeder übrige Kern ist nach (K1) ≤ C/s². Die Faktoren e^{4δ} gleichen genau die zusätzliche Linie von B auf [0, t\_{k\_H}) aus (M14b, Zeitfaktoren).

| Scheibe                                                | #C  | #Ĉ  | #O                  | #B                        | Kerne übrig | Faktor                                   |
|--------------------------------------------------------|-----|-----|---------------------|---------------------------|-------------|------------------------------------------|
| Schwanz, Teilen endet (Scheibe k\_T)                   | n   | n   | n − 1               | n + 1 (Stück ab ξ bzw. P) | 0           | Kernquotient, 1/p nach Lemma P6″ (M.9.5) |
| Schwanz, Teilen setzt sich fort (Scheiben < k\_T)      | n   | n   | n − 1               | n + 1 (freies Ende)       | 1           | ≤ C e^{C(K)}/(c₁p₁ s²) je Scheibe        |
| Kopf, voll geteilt (Scheiben < k\_H)                   | n   | n   | n + 1 (ν ohne Kern) | n (B = C)                 | 0           | Lemma C (e), erzwungenes Label (M.9.6)   |
| Kopf, letzte geteilte Scheibe (k\_H, Schnitt bei S\_m) | n   | n   | n + 1 (ν ohne Kern) | n − 1                     | 1           | ≤ C/s², dazu e^{3C(K)}/(c₁p₁) (M.9.6)    |

Die erste und die letzte Zeile sind die Enden, die es immer gibt (k\_T = 0 und k\_H = 0 eingeschlossen). Insgesamt bleibt also genau ein Kern C/s², und zwar am Kopf: Das Stück von p in der letzten geteilten Scheibe steht in C und in Ĉ, aber nicht in B. Das ist der Faktor „p\_δ(y, Y) ≤ C/s²“ der Tabelle in M.9.5, dort nur dem Kopfstück zugeschrieben. Jede weitere geteilte Schwanzscheibe kostet einen weiteren Kern C/s², jede weitere geteilte Kopfscheibe keinen. Deshalb ist die Fortsetzung am Kopf nur um die erzwungene Wahl gedämpft (C/m), die am Schwanz zusätzlich um C/s².

**Lemma M14d (Vergleich in den Endscheiben) [S, ausgeschrieben in M.9.8; hier die Kurzform].** Fest seien Skelette, Routen, Tupel und verdeckte Daten mit k\_H geteilten Kopflagen und k\_T geteilten Lochplätzen. Dann gilt die Schranke von Lemma M9 mit dem Bezugszustand B von oben (Erzeugung bei (ξ, 0), Schnitt bei (S\_m, t\_{k\_H})), und zu den Faktoren von M9 kommen nur die der Tabelle hinzu:

```text
I_{I,I′}  ≤  [M9-Faktoren] · Φ_end · (C/s²) · ( C e^{C(K)}/(c₁p₁ s²) )^{k_T} · (1/(c₁p₁))^{k_H + 1} · e^{3C(K)} · ∫ W(B) 1_G H_F(B)
```

*Hinweis (Review 2026-11-13, H7):* Das ist die Kurzform. In der ausgeschriebenen Fassung (M.9.8) steckt der Faktor 1/(c₁p₁) je geteilter Kopfscheibe in p^{−|d|} (p ≤ c₁p₁/2); hier und dort zusammen wäre er doppelt gezählt, was nur schadlos zu groß ist. Maßgeblich ist M.9.8, für k\_T ≥ 1 mit M.9.11.

Φ\_end steht für die festen Endfaktoren aus M.9.5 (Kernquotient ξ statt x, 1/p für das Stück ab ξ). Die Label-Faktoren der erzwungenen Wahl je geteilter Kopfscheibe stehen in M10 und in der Bilanz von M.9.6.

*Beweis (Gang).* Scheibe für Scheibe wie M9, Schritte 1 bis 7. Die Gruppen sind die von M9, in der letzten geteilten Kopfscheibe mit d = h ∪ pred\_I(h) ∪ pred\_{I′}(h) (M.9.6). In den voll geteilten Scheiben beider Enden ist B = C auf dem gemeinsamen Stück, am Schwanz dazu das frische Stück der zusätzlichen Linie. Nach Integration der von R′ gezogenen Stücke bleibt dort am Kopf der Quotient Z^{alt}/Z\_neu (Lemma C (e), für die Kette Lemma M8), am Schwanz ein überzähliger Kern. In der Scheibe, in der das Teilen endet, wird B auf d frisch gezogen. Am Schwanz gehört dazu das Stück ab ξ bzw. P; seine Endpunkte sind isoliert (ξ gut, P isoliert nach Wahl, sonst Endpunkte wählbarer Stücke), also gilt (P) in Lemma M5 mit Lemma P6″. Am Kopf fällt das Stück von p weg (Schnitt bei S\_m). Die Kerne zählt die Tabelle statt M8, Schritt 3. Lemma M4 gilt mit den beiden offenen Enden als Ausnahme-Enden, die frischen Stücke sind regulär mit isolierten Endpunkten wie alle geänderten Stücke. Das Bezugsmaß ist µ\_ab^{(k\_H)}; Lemma M14b ersetzt Z.7 in M13. ∎

**Summe über k\_H und k\_T** (für k\_T ≥ 1 ersetzt durch die Bilanz in M.9.11). Mit η aus M.9.6 ist die Summe höchstens Σ\_{k\_H} (k\_H + 1) η^{k\_H} · Σ\_{k\_T} (C e^{C(K)}/(c₁p₁ s²))^{k\_T} mal der Schranke für k\_H = k\_T = 0. Wegen s² = m/ρ → ∞ ist die zweite Reihe ≤ 2 für kleines ρ. Die Lage von P geht über das frische Stück in µ\_ab^{(k\_H)} ein und braucht keine eigene Summe.

**Prüfung [N]** (pruef\_kopfteilen2d.py, jetzt auch mit den Lochplätzen; Läufe [kopfteilen2d\_schwanz\_start.sh](kopfteilen2d_schwanz_start.sh), ergebnisse/kopfteilen2d\_schwanz/): Anteil von ∫f², bei dem sich das Teilen über Scheibe 0 hinaus fortsetzt, am Kopf und am Schwanz, gegen die Zahl s² der Plätze je Zelle (w = 2).

| System     | s²  | S   | m    | Proben | ∫f²dµ | Kopf: Anteil K ≥ 2 | Schwanz: Anteil K\_T ≥ 2 |
|------------|-----|-----|------|--------|-------|--------------------|--------------------------|
| 4×4, N = 4 | 4   | 4   | 1,00 | 55934  | 0,85  | 0,614 ± 0,003      | 0,104 ± 0,006            |
| 4×4, N = 4 | 4   | 8   | 1,00 | 10203  | 1,92  | 0,499 ± 0,005      | 0,095 ± 0,008            |
| 6×4, N = 6 | 4   | 8   | 1,00 | 2508   | 3,23  | 0,518 ± 0,014      | 0,079 ± 0,030            |
| 4×4, N = 6 | 4   | 8   | 1,50 | 5965   | 2,53  | 0,436 ± 0,009      | 0,141 ± 0,017            |
| 4×4, N = 8 | 4   | 8   | 2,00 | 5349   | 1,81  | 0,496 ± 0,015      | 0,214 ± 0,028            |
| 6×4, N = 6 | 6   | 8   | 1,50 | 3042   | 3,70  | 0,532 ± 0,018      | 0,085 ± 0,030            |
| 4×4, N = 4 | 8   | 8   | 2,00 | 16657  | 1,92  | 0,576 ± 0,005      | 0,108 ± 0,007            |
| 6×4, N = 6 | 12  | 8   | 3,00 | 4619   | 4,56  | 0,595 ± 0,014      | 0,097 ± 0,028            |
| 4×4, N = 4 | 4   | 12  | 1,00 | 1044   | 1,77  | 0,468 ± 0,017      | 0,096 ± 0,024            |
| 4×4, N = 4 | 4   | 16  | 1,00 | 55     | 1,59  | 0,497 ± 0,115      | 0,102 ± 0,155            |

- **Schwanz seltener als Kopf.** Über Scheibe 0 hinaus setzt sich das Teilen am Schwanz in 8 bis 21 % von ∫f² fort, am Kopf in 44 bis 61 %.
- **Mechanismus sichtbar, Dämpfung nicht.** Die Fortsetzung am Schwanz wächst mit der Dichte (4×4: 0,10; 0,14; 0,21 für N = 4, 6, 8) und ist von der Größe 1/(Zahl der freien Plätze) (1/12, 1/10, 1/8): Sie ist ein Treffer auf einen bestimmten Platz, die am Kopf eine gemeinsame Wahl. Von der Zellgröße (s² = 4 bis 12) und der Scheibendauer (S = 4 bis 16) hängt sie nicht ab. Auf so kleinen Tori überdeckt die Irrfahrt einer Scheibe schon fast alle freien Plätze, der Kern ist flach, und die Dämpfung C/(1 + δ) mit δ = s² kann dort nur sättigen. Die Vorhersage C/s² selbst ist im Modell nicht prüfbar.
- **Vorsicht beim Wiederholen.** Läufe mit S ≥ 16 brauchen sehr viel Speicher; der Lauf mit S = 16 kam in 20 min nur auf 55 Proben, und einer mit S = 24 hat am 2026-11-13 den Rechner an den Speicherrand gebracht (OOM). Nicht mit S > 12 starten.

**Stand von Restsatz M14.** Alle Faktoren an beiden Enden haben jetzt eine Herkunft, einschließlich der Fortsetzung am Schwanz, die in M.9.5 fehlte, und des einzelnen Kerns C/s², dessen Ort die Tabelle angibt. Die Schritte von M9 für die Endscheiben stehen in M.9.8 (Lemma M14d mit Beweis); dort auch der Stand.

### M.9.8 Lemma M14d ausgeschrieben (2026-11-13)

Hier stehen die Schritte von Lemma M9 für die Endscheiben, in derselben Reihenfolge. Bezeichnungen wie in M9 und M.9.6, M.9.7: k\_H geteilte Kopflagen, k\_T geteilte Lochplätze, B der Bezugszustand mit Erzeugung bei (ξ, 0) und Schnitt bei (S\_m, t\_{k\_H}).

**Konvention.** Gerechnet wird mit ℒ = H + 4N (Grundenergie ε\_N, wie satz\_3\_9 §10.0). Dann hat jedes Stück das Gewicht W = p\_δ(S, E) ϖ\_{S,E} ohne Faktor e^{4δ}, und die zusätzliche Linie von B auf [0, t\_{k\_H}) geht nur in die Normierung von µ\_ab^{(k\_H)} ein (Lemma M14b, Zeitfaktoren). Schritt 3 von Lemma M8 (Ausgleich der Faktoren e^{4δ}) entfällt damit.

**Lemma C′ (Stück mit freiem Ende) [S, gegeben Lemma C].** *Seit M.9.11 (später Anfang am Schwanz) nicht mehr gebraucht; es bleibt als Hilfssatz stehen.* Sei Z ein isolierter Platz zur Zeit t\_j in einer brauchbaren Umgebung und G′(Z) die Menge der Plätze im Abstand ≤ D\_c s von Z, die zur Zeit t\_{j+1} von allen Linien den Abstand > r haben. Q′\_Z sei die freie Vorwärts-Irrfahrt ab Z über die Dauer δ. Für jede Familie F fester Stücke, die die Voraussetzungen von Lemma C erfüllt, gilt

```text
Q′_Z( Ende in G′(Z), cut, reg, stoßfrei mit F )  ≥  c₁p₁ − p_irr − η_R  ≥  2p
```

*Beweis.* In stetiger Zeit mit symmetrischem Hüpfen ist das Gewicht einer Scheibe bei festen Endpunkten invariant unter Zeitumkehr, ebenso der harte Kern, cut und reg. Die Spiegelung t ↦ t\_j + t\_{j+1} − t führt Q′\_Z in Q\_Y mit Y = Z über und G′(Z) in G(Y). Schritt 1 des Beweises von Lemma C gibt dann die Masse ≥ c₁p₁; cut und reg kosten nach (B1), (B2) höchstens η\_R + p\_irr ≤ c₁p₁/2. ∎

**Lemma M14d [S, gegeben Lemma M4 bis M8, Lemma C, C′, Lemma P6″ und Lemma M14f; in den Sonderfällen von M.9.10 [B]].** Fest seien Skelette, Routen, Tupel und die verdeckten Daten außer den Köpfen S′ der Abwege. I\_{I,I′} sei wie in M9 das Integral des Summanden über die übrigen Stücke, jetzt auch in den Endscheiben. Dann gilt

```text
I_{I,I′}  ≤  e^{C′(K)|h| + 6σJ} · s^{−2(1 + k_T)} · 1_occ(B) · Π_{nahe Vorkommen v} [ (1 − 2ε)(n_{c(v)}(B) − 2) ]^{−1} · ∫ W(B) 1_G(B) H_F(B)
C′(K)  =  8 ln(4π e^{(Λ²+1)/2}) + 7 ln(1/p)
```

Das Integral läuft über alle Stücke von B, auch über die Erzeugung P ∈ G\_P am Schwanz (M.9.11; bis 2026-11-13: über die freien Enden P der frischen Stücke). In den Scheiben, die kein Ende enthalten, ist das Lemma M9 selbst.

*Beweis.* Scheibe für Scheibe. In jeder Endscheibe sind die Gruppen die von M9 mit zwei Ergänzungen: In der letzten geteilten Kopfscheibe ist d = h ∪ pred\_I(h) ∪ pred\_{I′}(h) (M.9.6), und in den Schwanzscheiben 0, …, k\_T gehört zu d das Stück von B, das an der Erzeugung bzw. am vorigen freien Ende P beginnt. In jeder Endscheibe ist h ≠ ∅ (gemeinsames ν am Kopf, gemeinsames gelöschtes Stück am Schwanz), also |d| ≤ 3|h|.

1. **Auswahl und Route.** Wie M9, Schritt 1. Dazu kommen das Schwanz-Label 1/g⁰\_a(Ĉ) und am Kopf die durch O festgelegten Labels von R. Beide sind nahe Vorkommen und werden wie dort durch [(1 − 2ε)(n\_c(B) − 2)]^{−1} beschränkt; g⁰\_a zählt die Teilchen mit regulärem Stück; in brauchbaren Zellen ist g⁰\_a ≥ (1 − ε/2) n\_a (M.9.5), und n\_a(Ĉ) ≥ n\_a(B) − 2 (M1 (4)), also g⁰\_a(Ĉ) ≥ (1 − 2ε)(n\_a(B) − 2). Dass die Labels am Kopf nicht summiert werden, geht erst in die Auswahlsumme (M10) ein. Der Indikator 1{ξ gut} ist ≤ 1.
2. **Kerne.** Wie Lemma M8, Schritte 1 und 2, mit der Zählung der Tabelle in M.9.7 statt Schritt 3. Das neue Stück ν in O und die frischen Stücke mit freiem Ende in B tragen keinen Kern; ihre Bezugsgesetze Q\_Y und Q′\_Z haben die Masse 1. Übrig bleiben im Zähler 1 + k\_T Kerne mit festen Endpunkten (einer in der letzten geteilten Kopfscheibe, einer je fortgesetzter Schwanzscheibe), jeder ≤ (1 + δ)^{−1} ≤ s^{−2} nach (K1) mit C = 1. Die übrigen Kerne stehen paarweise in Zähler und Nenner, höchstens 2|d| + 2 ≤ 8|h| je Seite, mit Endpunkten im Abstand ≤ Λs (am Schwanz liegt ξ in der Zelle von x). Wie in M8, Schritt 4, gibt das (4πe^{(Λ²+1)/2})^{8|h|}.
3. **Nenner.** Folgerung M6 in jeder Endscheibe mit diesen Gruppen. Die Bedingung (P) von Lemma M5 gilt für Stücke mit festen guten Endpunkten nach Lemma P6″ wie im Beweis von M6, für ν nach Lemma C (c), für das Stück ab ξ nach Lemma P6″ (ξ ist gut, a ist brauchbar) und für die Stücke mit freiem Ende nach Lemma C′. Die Exponenten sind |h| und |d|.
4. **Weglassen.** Wie M9, Schritt 4.
5. **Integrieren.** Wie M9, Schritt 5. Am Schwanz hat das gemeinsame gelöschte Stück keine Version in O; seine Versionen in C und Ĉ geben je ≤ 1. Am Kopf gibt O\_h einschließlich ν (Gesetz Q\_Y) ≤ 1.
6. **Zurückholen.** Folgerung M7 mit H = d. Die frischen Stücke von B auf d bekommen die Endpunkte, die die Zählung in M.9.6 und M.9.7 verlangt (am Kopf die Fassung aus Lemma M14f (3)): am Schwanz einen zusätzlichen Anfang (ξ bzw. P) und in den fortgesetzten Scheiben ein freies Ende in G′, am Kopf fehlt der Anfang S\_m. In jeder Scheibe stimmen die Anfänge und Enden von B mit denen der Nachbarscheiben überein (dort nachgezählt). Faktor p^{−|d|} e^{σJ\_k}.
7. **Stabilität.** Lemma M4 gilt für B mit zwei Ergänzungen: Die beiden offenen Enden sind Ausnahme-Enden wie in Z.5 (gezählt, nicht wählbar), und je Endscheibe ist höchstens ein Stück mehr geändert als in M1 (das frische Stück am Schwanz). Mit n″ + 1 statt n″ in den Bedingungen von M4 bleibt der Beweis wörtlich; alle diese Bedingungen haben Spielraum für ρ klein.
8. **Zusammen.** Je Endscheibe die Exponenten |h| (M6, erste Zeile), |d| (M6, zweite Zeile) und |d| (M7), also ≤ 7|h| Faktoren 1/p, dazu (4πe^{(Λ²+1)/2})^{8|h|} aus Schritt 2 und sechs Faktoren e^{σJ\_k}. Das gibt e^{C′(K)|h|}. Die übrigen Kerne geben s^{−2(1 + k\_T)}. ∎

**Was daraus für Restsatz M14 folgt.**

- **Bilanz.** Der Kern s^{−2} am Kopf ist der Faktor „p\_δ(y, Y) ≤ C/s²“ der Tabelle in M.9.5. Die Ausweich- und Kernfaktoren der Endscheiben stecken in e^{C′(K)|h|} und ersetzen „Φ\_end“ aus M.9.7. Die Labels: Am Schwanz summiert R′ über x mit 1/g⁰\_a(C), R hat 1/g⁰\_a(Ĉ) (Schritt 1); die Summe über x gibt die Zeile „gemeinsames Schwanz-Label“ der Tabelle in M.9.5, mit C′(K) statt C(K). Am Kopf gibt jedes festgelegte Label einen Faktor 1/g ohne Summe (M.9.6).
- **Reihen.** Je weiterer geteilter Kopfscheibe η = e^{2C′(K)}/((1 − 2ε)(b₋m − 2)), je weiterer geteilter Schwanzscheibe s^{−2} e^{2C′(K)} (mit spätem Anfang: C e^{C′(K)} e^{δμ̄}/s², und die erste geteilte Schwanzscheibe kostet eine Konstante, M.9.11). Der Faktor 1/(c₁p₁) aus Lemma C (e), mit dem M.9.6 rechnete, steckt hier in p^{−|d|}, denn p ≤ c₁p₁/2. Beide Reihen sind ≤ 2 für kleines ρ.
- **Bezugsmaß.** ∫W(B) … ist ein Integral unter µ\_ab^{(k\_H)} (Lemma M14b), für k\_T ≥ 1 unter µ^{(k\_T, k\_H)} (Lemma M14b′, M.9.11); Folgerung M14c gibt M13 dafür.

**Stand.** Lemma M14d [S, gegeben Lemma M4 bis M8, Lemma C, C′, P6″ und M14f; Sonderfälle M.9.10 [B]]. Restsatz M14 ist damit bewiesen (im Regelfall), gegeben diese Lemmata, Lemma M14a bis M14c und Satz D, bis auf die Summe über die Zelle des Schnitts; die steht in M.9.9 (Lemma M14e).

### M.9.9 Lemma M14e: Summe über die Schnittzelle (2026-11-13)

In M.8.4 hat B seine Vernichtung in einer festen Zelle b, und die Routen werden unter dem Integral summiert. Tatsächlich liegt die Vernichtung am Anfang S\_m des erzwungenen Teilchens p in der letzten geteilten Kopfscheibe k\_H (M.9.6), also in einer Zelle z, die von den Routen abhängt. Hier wird die Summe über z ausgeschrieben; sie ersetzt die letzte Zeile der Bilanztabelle in M.9.6.

**Lemma M14e [S, gegeben Lemma M11, M11a, M12, M13 und Folgerung M14c].** Seien a, b, die Skelette γ, γ′ und k\_H fest, und b\_{k\_H} die Grundlage der Abweg-Hälfte von γ in Scheibe k\_H (M.8.0; Review 2026-11-13, H7). Dann gilt für die Summe über alle verträglichen Routenpaare

```text
(N M Z_N)^{−1} Σ_{(P, P′)} e^{κ₀ J} ∫ W(B) 1_G(B)  ≤  C_z e^{ℓ⁰} · e^{κ₀ C_J J₀″} · max_z E_{µ_az^{(k_H)}}[ e^{(C₂ + 7) b_tot} ]  ≤  (C/M_Z²) · e^{κ₀ C_J J₀″ + ϑ′(q) S}
```

mit C₂ = 4 + κ₀C\_J aus M.8.4, C\_z = Σ\_z e^{−d(z, b\_{k\_H})} ≤ 9 (Summe über alle Zellen z, ℓ∞-Abstand) und ϑ′ aus Lemma M13 mit C₂ + 7 statt C₂.

*Beweis.*

1. **Nach der Schnittzelle zerlegen.** Jeder Zustand B hat genau eine Vernichtung, in der Zelle z(B). Ein Routenpaar ist mit B nur verträglich, wenn S\_m der Platz dieser Vernichtung ist. Also ist die Summe über die Routenpaare unter dem Integral eine Summe über die mit B verträglichen Paare, und das Integral zerfällt in die Teile Ω\_{az} = {B : Erzeugung in a, Vernichtung in z}. Auf Ω\_{az} ist (NMZ\_N)^{−1} W(B) das Maß µ\_{az}^{(k\_H)}.
2. **Lage.** p ist ein Stück der Route von R in Scheibe k\_H, das R ändert. Nach Lemma M11a (mit 𝔅(Ĉ) ⊆ 𝔅₁) liegt es in Reg\_{k\_H}, also d(z, b\_{k\_H}) ≤ ℓ\_{k\_H} ≤ ℓ⁰ + 7β\_{k\_H}. In Scheibe k\_H haben beide Routen ν und p gemeinsam; die Scheibe ist also nah (M.8.1), und β\_{k\_H} ≤ b\_tot. Damit ist 1{B verträglich} ≤ e^{ℓ⁰ + 7 b\_tot − d(z, b\_{k\_H})}.
3. **Routen und J.** Wie in M.8.4: Bei festem B gibt es höchstens e^{4b\_tot} verträgliche Routenpaare (Lemma M11), und J ≤ C\_J(J₀″ + b\_tot) (Lemma M12). Mit Schritt 2 ist der Integrand auf Ω\_{az} höchstens e^{ℓ⁰ − d(z, b\_{k\_H})} e^{κ₀C\_J J₀″} e^{(C₂ + 7) b\_tot}.
4. **Seltene Komponenten.** Lemma M13 gilt für µ\_{az}^{(k\_H)} gleichmäßig in z (Folgerung M14c), mit C₂ + 7 statt C₂: E[e^{(C₂ + 7) b\_tot}] ≤ (C/M\_Z²) e^{ϑ′(q) S}.
5. **Summe über z.** Auf dem ℓ∞-Zellgitter gibt es höchstens 8r Zellen im Abstand r ≥ 1, also Σ\_z e^{−d(z, b\_{k\_H})} ≤ 1 + Σ\_{r≥1} 8r e^{−r} = 1 + 8e^{−1}/(1 − e^{−1})² < 9. ∎

*Folgen.*

- **M.8.4** gilt damit wörtlich mit der wandernden Schnittzelle, mit dem zusätzlichen Faktor C\_z e^{ℓ⁰} und C₂ ≤ 12 statt ≤ 5 in Lemma M13; q wird entsprechend kleiner gewählt.
- **M.9.6, Bilanztabelle, letzte Zeile:** Statt „Summe ≤ C(k + 1) e^{ℓ⁰}, C₂ in M13 um 7 größer“ gilt der Faktor C\_z e^{ℓ⁰} ≤ 9 e^{ℓ⁰}, unabhängig von k\_H; es zählt nur Reg\_{k\_H}, nicht die Bereiche der Scheiben darunter.
- **Rechnung von M.9.5:** Für jedes Glied (a, b′, b) tritt an die Stelle von „(C/M\_Z²) nach M.8.4“ die Schranke von Lemma M14e. Die Summe über a, b′ und b und alle Potenzen von m, s, M\_Z und A bleiben, wie sie sind.
- **Schwanz:** Die Erzeugung liegt immer bei ξ in a (M.9.7); dort gibt es keine eigene Summe.

**Stand von Restsatz M14.** Bewiesen, gegeben Lemma M4 bis M13, Lemma M14a bis M14f, Lemma C, C′ und P6″ sowie Satz D für N und N + 1 Teilchen, im Regelfall; die beiden Sonderfälle in M.9.10 (Teilen bis zur Wende, Kopf- und Schwanzende in derselben Scheibe) sind [B]. Am Mini-Ring exakt nachgerechnet ist die Dichteformel Lemma M14a; die Kernzählung der Enden und die Fortsetzung des Teilens sind im 2D-Testmodell gesehen, aber nicht in der Größe, auf die es im Beweis ankommt (m ≤ 3).

### M.9.10 Lage des Schnitts als Lemma, Abstände und Sonderfälle (2026-11-13 abends, Review 2026-11-13, W3)

M.9.6 führte die Lage des Schnitts nur als [B], obwohl M14d und M14e darauf bauen. Hier steht sie als Lemma, mit einer ausdrücklichen Fassung von B in der letzten geteilten Kopfscheibe.

**Bezeichnungen.** s = k\_H ist die letzte geteilte Kopfscheibe. Beide Routen haben dort dasselbe neue Stück ν (von S′ zur Zeit t\_s nach Y\_m zur Zeit t\_{s+1}) und dasselbe Teilchen p über Y\_m, denn O legt die Linie über Y\_m fest. Die Kopflagen zur Zeit t\_{s+1} sind verschieden: Y\_0^R ≠ Y′\_0. Die Kette von R in Scheibe s ist j\_1^R, …, j\_m^R = p (m ≥ 1, Querschritt in jeder Scheibe), die von R′ ist j′\_1, …, j′\_{m′} = p. R liest in O die Brücke von j\_i^R mit Ende Y\_{i−1}^R; ihre Ĉ-Fassung endet bei Y\_i^R (Y\_0^R ist die verdeckte Kopflage). Für R′ endet die C-Fassung von j′\_l bei Y′\_l und die O-Fassung bei Y′\_{l−1}. Zyklischer Vorgänger am Kopf: pred\_I(j\_1^R) = pred\_{I′}(j′\_1) = ν. Gruppen wie in M8, Schritt 2: h von beiden Routen geändert, j nur von R, l nur von R′, L von keiner. In B tragen L und l die C-Fassung, j die Ĉ-Fassung, d wird frisch gezogen. Ein wählbares Stück beginnt höchstens D Zellen von seinem Ende in seiner Kettenzelle, und benachbarte Kettenzellen liegen höchstens 2 Zellen auseinander.

**Lemma M14f (Lage des Schnitts) [S].** Sei 0 ≤ s = k\_H ≤ w − 1, und die Stücke, die die beiden Abwege in Scheibe s ändern, seien von denen der Aufwege in Scheibe s verschieden (Regelfall; zu den übrigen Fällen unten). Sei d = h ∪ pred\_I(h) ∪ pred\_{I′}(h). Dann gilt:

1. **Bilanz.** Am Kopf hat B in Scheibe s zur Zeit t\_s die Anfänge von C und zur Zeit t\_{s+1} die Enden von C außer Y\_0^R.
2. **Das Stück am Ende Y\_0^R.** Sei q₀ das Stück von C mit Ende Y\_0^R. Ist j\_1^R ∈ j, so ist q₀ = j\_1^R. Ist j\_1^R ∈ h, so ist j\_1^R = j′\_l mit l ≥ 2 und q₀ = j′\_{l−1} = pred\_{I′}(j\_1^R) ∈ d. Andere Fälle gibt es nicht. In beiden Fällen endet in B kein Stück aus j ∪ l ∪ L bei Y\_0^R.
3. **Konsistenz und Schnitt.** Die festen Stücke (j mit der Ĉ-Fassung, l und L mit der C-Fassung) belegen in B verschiedene Enden außer Y\_0^R. Für d bleiben die |d| C-Anfänge seiner Stücke und |d| − 1 Enden. Lässt man S\_m weg und paart den Rest, so ist B mit den Nachbarscheiben konsistent, und die Linie von B, die bei (S\_m, t\_s) von unten ankommt, endet dort. S\_m ist isoliert und liegt höchstens D + D\_c + 1 Zellen von der Kopflage S′ zur Zeit t\_s.
4. **Abstände.** Es gibt eine Paarung in 3, in der jedes frische Stück einen Anfang und ein Ende im ℓ∞-Abstand ≤ D + 4 Zellen verbindet, also ≤ Λs mit Λ = (9/8)(D + 4) (Zellseiten ≤ 9s/8 nach Z.13).

*Beweis von 1 bis 3.*

1. Unterhalb von t\_s stimmen die Kopfketten beider Routen überein, und B ist dort am Kopf bis auf Umbenennung gleich C (M.9.6). Oberhalb von t\_{s+1} fehlt B gegenüber C die eingefügte Linie von R. Sie läuft durch (Y\_0^R, t\_{s+1}), denn dort beginnt das neue Stück von R in Scheibe s + 1. In C ist Y\_0^R zur Zeit t\_{s+1} besetzt, nämlich von q₀ (Schritt 2).
2. j\_1^R wird von R geändert, liegt also in h ∪ j. Ist j\_1^R ∈ j, so ändert R′ das Stück nicht; seine C-Fassung ist die O-Fassung und endet bei Y\_0^R. Ist j\_1^R ∈ h, so ist j\_1^R = j′\_l, und Y\_0^R ist sein O-Ende Y′\_{l−1}. Für l = 1 wäre das Y′\_0, also eine gemeinsame Kopflage zur Zeit t\_{s+1}, und s wäre nicht die letzte geteilte Scheibe. Also ist l ≥ 2, und Y′\_{l−1} ist das C-Ende von j′\_{l−1}. Wegen des harten Kerns endet nur ein Stück von C bei Y\_0^R. Feste Stücke enden in B nicht bei Y\_0^R: Stücke aus l und L tragen ihre C-Fassung und sind nicht q₀ (im Fall j ist q₀ ∈ j, im Fall h ist q₀ ∈ d). Stücke aus j tragen die Ĉ-Fassung, und in Ĉ ist Y\_0^R zur Zeit t\_{s+1} frei, weil Ĉ die eingefügte Linie von R nicht hat.
3. Die festen Stücke tragen Fassungen von C bzw. Ĉ; dass sie in B verschiedene Enden belegen, ist die Kettenbuchführung von M9 (Schritt 6), und nach 2 ist keines davon Y\_0^R. Ihre Anfänge sind C-Anfänge, denn auch die Ĉ-Fassungen behalten die Anfänge. Nach 1 hat Scheibe s in B so viele Anfänge wie C Stücke und ein Ende weniger; für d bleiben also |d| Anfänge und |d| − 1 Enden. Welcher Anfang wegfällt, darf man wählen, solange er zu d gehört, und p ∈ h ⊆ d, denn beide Routen ändern p. Fällt S\_m weg, so setzt sich die Linie von B, die bei (S\_m, t\_s) ankommt, in Scheibe s nicht fort. S\_m ist Anfang eines wählbaren Stücks, also isoliert (M1 (3)); |S\_m − Y\_m| ≤ D Zellen und |Y\_m − S′| ≤ D\_c + 1. ∎

*Beweis von 4.* Die **Verschiebung längs der Kette von R** setzt j\_i^R (1 ≤ i ≤ m − 1) auf das C-Ende von j\_{i+1}^R und lässt alle anderen Stücke in ihrer C-Fassung.

- **Was sie tut.** Sie benutzt nur die C-Enden von j\_2^R, …, j\_m^R = p; frei wird das C-Ende von j\_1^R, und weil p wegfällt, auch S\_m. Für j\_i^R ∈ j liegt der Nachfolger nicht in h (sonst wäre j\_i^R = pred\_I(j\_{i+1}^R) ∈ d), also ist sein C-Ende sein O-Ende Y\_i^R, und j\_i^R bekommt genau seine Ĉ-Fassung, wie für j verlangt. Stücke aus l und L bleiben, wie sie sind.
- **Länge.** Liegt j\_{i+1}^R in j, ist das neue Ende Y\_i^R, höchstens D Zellen vom Anfang. Ist j\_{i+1}^R = j′\_l ∈ h, ist es Y′\_l; der Anfang liegt höchstens D Zellen von Y\_i^R = Y′\_{l−1}, und Y′\_{l−1}, Y′\_l liegen in benachbarten Kettenzellen von R′. Also ≤ D + 2.
- **Korrektur am Kopf.** Nach 1 muss statt des C-Endes von j\_1^R das Ende Y\_0^R frei werden. Im Fall j\_1^R ∈ j sind beide gleich (q₀ = j\_1^R), es ist nichts zu tun. Im Fall j\_1^R = j′\_l ∈ h ist das C-Ende von j\_1^R gleich Y′\_l und q₀ = j′\_{l−1}. Liegt q₀ nicht in der Kette von R, setzt man q₀ auf Y′\_l (benachbarte Kettenzelle von R′, ≤ D + 2); dann ist Y\_0^R frei. Liegt q₀ in der Kette von R, etwa q₀ = j\_{i₀}^R mit i₀ ≥ 2, so hat die Verschiebung j\_{i₀−1}^R auf das C-Ende von q₀ gesetzt, also auf Y\_0^R. Man setzt j\_{i₀−1}^R stattdessen auf Y′\_l; das ist erlaubt, denn j\_{i₀−1}^R = pred\_I(q₀) ∈ d (q₀ liegt in beiden Ketten, also in h). Sein Anfang liegt höchstens D Zellen von Y\_{i₀−1}^R, dem O-Ende von q₀ = j′\_{l−1}, also Y′\_{l−2}, und Y′\_l liegt zwei Kettenzellen von R′ weiter. Also ≤ D + 4.
- **Ergebnis.** In allen Fällen hat Scheibe s die Anfänge von C ohne S\_m und die Enden von C ohne Y\_0^R, jedes Stück von B verbindet Anfang und Ende im Abstand ≤ D + 4 Zellen, und außerhalb von d stimmt die Fassung mit der von 3 überein. ∎

*Für die inneren Scheiben* (Lemma M8, Schritt 4) ist die frische Paarung von B auf d dieselbe Verschiebung längs der Kette von R, ohne Korrektur am Kopf; die Abstände sind dort ≤ D + 2 Zellen. Das ist die genaue Begründung für „alle Endpunktpaare auf d haben |x|\_∞ ≤ Λs“, die M8 nur über die Lage der Stücke (M1 (2)) gab. Ein erster Versuch am 2026-11-13 abends, die Paarung am Kopf als einen einzigen alternierenden Weg zu schreiben, der bei q₀ beginnt, scheiterte am Fall q₀ in der Kette von R; daher die Korrektur oben.

**Folgen.**

- **M.9.6:** Die Lage des Schnitts ist damit [S]; d = h ∪ pred\_I(h) ∪ pred\_{I′}(h) bleibt. Lemma M14d, Schritt 6, benutzt die Fassung aus Teil 4 (Verschiebung längs der Kette von R mit der Korrektur am Kopf).
- **Λ.** Lemma M2, M8 und M14d rechnen mit Λ = (9/8)(D + 4) statt D + 2: Zellseiten bis 9s/8 nach der Pflasterung (Review 2026-11-13, H4) und D + 4 Zellen aus Teil 4. Es ändern sich nur C(K) und C′(K) über Λ².

**Sonderfälle [B].**

1. **Teilen bis zur Wende (k\_H = w).** Dann stimmen auch die Kopflagen zur Zeit t\_w überein, also die Wendepunkte beider Routen und damit die obersten Lochplätze ihrer Aufwege. In Scheibe w − 1 treffen Aufweg und Abweg jeder Route zusammen (Selbstbegegnung, Z.1), und der Schnitt liegt zur Zeit t\_w = T. Das Bezugsmaß ist µ\_ab^{(w)} aus Lemma M14b (dort ist k = w zugelassen). Plan: In Scheibe w − 1 legt man die Gruppen beider Hälften beider Routen zu einem d zusammen (|d| ≤ C|h| mit fester Zahl C) und setzt die Fassung von B durch zwei alternierende Wege wie in Teil 3 zusammen, einen längs des Abwegs, einen längs des Aufwegs. Das kostet e^{C″(K)|h|} mit einem festen C″(K), und der Beitrag trägt den Faktor η^w aus der Fortsetzung. Für η ≤ e^{−C″(K)} ist er höchstens so groß wie der des Regelfalls. Nicht ausgeschrieben ist, dass sich die beiden Wege konsistent zusammensetzen.
2. **Kopf- und Schwanzende in derselben Scheibe.** In den Scheiben 0, …, min(k\_H, k\_T) können die Endgruppen am Kopf (Abweg von R) und am Schwanz (Aufweg von R) gemeinsame Stücke haben, wenn sich die beiden Hälften von R dort nahe kommen. Das ist eine Selbstbegegnung von R wie in Z.1. Die Änderungen der Endpunktmengen sind additiv: am Schwanz ein Anfang mehr (ξ bzw. P) und ein Ende mehr (der verdeckte Lochplatz), am Kopf ein Anfang weniger (S\_m) und ein Ende weniger (Y\_0^R). Plan wie in 1: d als Vereinigung beider Endgruppen, Fassung von B durch die beiden alternierenden Wege; teilen sich die Wege ein Stück, legt man es nach d und paart dort neu. Kosten e^{C″(K)|h|}, fester Faktor.

Die Sonderfälle ändern die Struktur der Schranke nicht, nur Konstanten. Ausgeschrieben sind sie nicht. **Stand:** Lemma M14f [S]; Lemma M14d und Restsatz M14 sind [S] im Regelfall und [B] in den beiden Sonderfällen.

### M.9.11 Später Anfang am Schwanz (2026-11-14, Review 2026-11-13, W1)

**Befund.** In der Fassung von M.9.7 lief die zusätzliche Linie von B in den geteilten Schwanzscheiben frisch ab ξ, und ihr freies Ende P\_{j+1} lag im Ball um das *vorige* freie Ende. Damit war weder die brauchbare Umgebung gesichert, die Lemma C′ verlangt, noch der Abstand ≤ Λs zum gemeinsamen Lochplatz in Scheibe k\_T, und die Konstanten von Lemma P6″ wuchsen mit k\_T. Abhilfe ist der späte Anfang, spiegelbildlich zum späten Schnitt am Kopf (Vorschlag des Reviews).

**Bezeichnungen.** k\_T ≥ 1 ist die Zahl der übereinstimmenden verdeckten Lochplätze h\_1, …, h\_{k\_T}. In den Scheiben 0, …, k\_T löschen beide Routen dasselbe Stück: in Scheibe 0 das Schwanzstück ab x, in Scheibe j ≥ 1 das Stück ab dem gemeinsamen Lochplatz h\_j. In Scheibe k\_T trennen sich die Ketten, denn die Lochplätze zur Zeit t\_{k\_T+1} sind verschieden. q\_{k\_T} sei das gemeinsam gelöschte Stück von Scheibe k\_T und E\_q sein C-Ende.

**Neue Fassung von B.**

1. **Scheiben 0, …, k\_T − 1:** B = C bis auf Umbenennung, ohne zusätzliche Linie. Der Hilfspunkt ξ wird nicht zur Erzeugung von B.
2. **Scheibe k\_T:** Die Erzeugung von B liegt zur Zeit t\_{k\_T} an einem Platz P aus

   ```text
   G_P  =  { P : |P − h_{k_T}|_∞ ≤ s,  P zur Zeit t_{k_T} frei und im Abstand > r von allen Teilchen }
   ```

   Das Stück von B ab P ist die umgehängte Fassung von q\_{k\_T}: Es beginnt bei P statt bei h\_{k\_T} und endet bei E\_q; es gehört zu d und wird frisch gezogen. Alles Übrige in Scheibe k\_T ist wie im ungeteilten Fall mit ξ an der Stelle von P. Summiert wird über P ∈ G\_P.
3. **Darüber:** wie bisher; die zusätzliche Linie folgt der Route von R.

Für k\_T = 0 ist das die alte Fassung mit P = ξ in Scheibe 0. G\_P ist nicht leer: h\_{k\_T} liegt auf der Route von R, also in einer brauchbaren Zelle, und dort gibt es isolierte freie Plätze (Anhang L, Lemma L2).

**Was das behebt.**

- **Umgebung.** P liegt höchstens eine Zellseite von h\_{k\_T}, also an der Route. Nach der Verdickung um D′ = 2D + 2 ist die Umgebung brauchbar (Anhang S, S.0). Lemma C′ wird nicht mehr gebraucht; das Stück ab P hat zwei feste, isolierte Endpunkte (P und E\_q, das Ende eines wählbaren Stücks), und Lemma P6″ gibt die Bedingung (P) von Lemma M5 wie für das Stück ab ξ.
- **Abstand.** |P − E\_q|\_∞ ≤ |P − h\_{k\_T}| + |h\_{k\_T} − E\_q| ≤ (1 + D + 1) Zellen, also ≤ Λs mit Λ = (9/8)(D + 4).
- **Gleichmäßigkeit in k\_T.** Kein Abstand und keine Konstante hängt mehr von k\_T ab.

**Bezugsmaß mit spätem Anfang und spätem Schnitt.** Für 0 ≤ k\_T, k\_H ≤ w, Zellen c, b und ein Ereignis E auf den Bahnen des Fensters sei, mit t₁ = min(t\_{k\_T}, t\_{k\_H}) und t₂ = max(t\_{k\_T}, t\_{k\_H}),

```text
µ_cb^{(k_T, k_H)}(E)  =  (N M)^{−1} e^{T ε_N} ⟨ψ, K^E_{[t₂, T]} X₂ K^E_{[t₁, t₂]} X₁ K^E_{[0, t₁]} ψ⟩
```

mit X = a\*(1\_c) zur Zeit t\_{k\_T} und X = a(1\_b) zur Zeit t\_{k\_H} (bei k\_T = k\_H beide zur selben Zeit, erst a\*). Auf (t₁, t₂) liegt der Sektor N + 1 (k\_T < k\_H) bzw. N − 1 (k\_T > k\_H). Für k\_T = 0 ist das µ\_cb^{(k\_H)} aus M.9.6. Die Zustände B mit k\_T und k\_H geteilten Lagen und Erzeugung bei P ∈ c haben genau dieses Gewicht.

**Lemma M14b′ (Übertragung mit spätem Anfang) [S, gegeben die Ein-Grund-Schranken von Satz D für N − 1, N und N + 1 Teilchen].** Sei 𝒜 eine Menge von Raum-Zeit-Zellen des Fensters, 𝒜₀, 𝒜₁, 𝒜₂ ihre Teile in den Zeitfenstern [0, t₁], [t₁, t₂], [t₂, T]. Dann gilt

```text
µ_cb^{(k_T, k_H)}( alle Zellen von 𝒜 defekt )  ≤  (C/M_Z²) · e^{δ μ̄ (k_T − k_H)₊} · q^{|𝒜₀|/4} · q₊^{|𝒜₁|} · q^{|𝒜₂|/4}
```

*Beweis.* Wie Lemma M14b, mit zwei Schnitten statt einem. Zerlegt wird {alle Zellen von 𝒜 defekt} = E₀ ∩ E₁ ∩ E₂ nach den drei Fenstern; das geht, weil Defekte scheibenweise erklärt sind und t₁, t₂ Scheibengrenzen sind. Mit χ = X₂\*(K₂^{E₂})\*ψ und φ = X₁ K₀^{E₀} ψ, beide elementweise ≥ 0, ist ν(F) = ⟨χ, K₁^F φ⟩ ein positives Maß, und Schritt 2 und 3 von M14b geben für das mittlere Fenster ν(1\_{E₁}) ≤ q₊^{|𝒜₁|} e^{−(t₂ − t₁) ε\_{N±1}} ‖R χ‖ ‖R φ‖. Die beiden Randfaktoren werden wie in M14b, Schritt 5, behandelt, jetzt an beiden Seiten: ‖Rφ‖² ≤ e^{λ} s² ⟨K₀^{E₀}ψ, (n\_c + 1) e^{A} K₀^{E₀}ψ⟩, und Ersetzen eines der beiden Kerne durch den ungetesteten gibt ≤ C s² m e^{c|𝒜₁|} e^{−2t₁ε\_N} P\_cl(E₀)^{1/2}; ebenso ‖Rχ‖² mit P\_cl(E₂)^{1/2}. Im Sektor N − 1 ist ‖a(1\_b)ψ‖² ≤ E n\_b ≤ C s² m, und die Ungleichung e^{A/2} a(1\_b) ≤ e^{λ/2} a(1\_b) e^{A/2} gilt wie für a\*. Die Zeitfaktoren geben e^{Tε\_N} e^{−t₁ε\_N} e^{−(t₂ − t₁)ε\_{N±1}} e^{−(T − t₂)ε\_N} = e^{−(t₂ − t₁)(ε\_{N±1} − ε\_N)}. Für N + 1 ist das ≤ 1; für N − 1 ist es e^{(t₂ − t₁)(ε\_N − ε\_{N−1})} ≤ e^{δμ̄ (k\_T − k\_H)}, weil ε\_N − ε\_{N−1} ≤ μ̄ (Lemma 6.5). Die Vorfaktoren sind wie in M14b C/M\_Z². ∎

Die Ein-Grund-Schranken für N − 1 Teilchen sind die für J ≤ N aus satz\_3\_9 §11 und §12 (Satz 3.9 (a^W) ist für 0 ≤ J ≤ N formuliert); für N + 1 siehe §9.3, Schritt 6. Folgerung M14c gilt wörtlich für µ^{(k\_T, k\_H)}.

**Kerne und Bilanz.** Die Tabelle in M.9.7 gilt mit zwei Änderungen. In den Scheiben < k\_T ist #B = n (B = C) statt n + 1; der übrige Kern ist derselbe, das C-Stück, das beide Routen löschen und R in Ĉ zurückholt: ≤ C/s² je Scheibe. In Scheibe k\_T ist das Stück ab P ein Stück von B mit festen Endpunkten; die Bilanz der Kerne ist dort 0 wie bisher. Neu ist die Verbuchung von ξ und P:

| k\_T | Hilfspunkt ξ                       | Erzeugung von B                                     | zusammen                         |
|------|------------------------------------|-----------------------------------------------------|----------------------------------|
| 0    | (1/M) Σ\_ξ wird zur Erzeugung in a | in µ\_ab enthalten                                  | N µ\_ab (wie M.9.5)              |
| ≥ 1  | (1/M) Σ\_{ξ ∈ a} 1 ≤ s²/M          | Σ\_{P ∈ G\_P} in µ\_cb^{(k\_T, k\_H)}, ≤ 9 Zellen c | ≤ N s² Σ\_c µ\_cb^{(k\_T, k\_H)} |

Gegenüber k\_T = 0 kommt also der Faktor s² hinzu. Ihn gleicht der übrige Kern der ersten geteilten Schwanzscheibe aus (C/s²); jede weitere geteilte Schwanzscheibe kostet einen weiteren Kern. Mit den Ausweich- und Kernfaktoren der Endscheiben (Lemma M14d, e^{C′(K)|h|}) und dem Energiefaktor aus M14b′ ist der Beitrag mit k\_T ≥ 1 höchstens

```text
9 e^{ℓ⁰+1} · Σ_{k_T ≥ 1}  C e^{C′(K)} e^{δμ̄} · ( C e^{C′(K)} e^{δμ̄} / s² )^{k_T − 1}   mal der Schranke für k_T = 0
```

Der Faktor 9 e^{ℓ⁰+1} ist die Summe über die Zelle c von P wie in Lemma M14e: h\_{k\_T} liegt auf der Route von R in Scheibe k\_T, also in Reg\_{k\_T} (Lemma M11a), und 1{c nahe h\_{k\_T}} ≤ e^{ℓ⁰ + 7β − d(c, b\_{k\_T}) + 1}; Lemma M13 läuft dann mit C₂ + 14 statt C₂ + 7 (q entsprechend kleiner). Die Reihe ist für C e^{C′(K)} e^{δμ̄} ≤ s²/2 höchstens 2 C e^{C′(K)} e^{δμ̄}, eine feste Zahl; das gilt für kleines ρ, weil s² = K ln(1/ρ)/ρ → ∞ und δμ̄ → 8πK beschränkt ist. Der Beitrag mit k\_T ≥ 1 ist also nicht klein, aber beschränkt, und ∫f̃² dµ̃ bleibt eine Konstante.

**Lemma M14d mit spätem Anfang [S, gegeben Lemma M4 bis M8, Lemma C, P6″ und M14f].** Lemma M14d gilt mit dieser Fassung von B, mit drei Änderungen im Beweis: In Schritt 3 hat das Stück ab P feste, isolierte Endpunkte in brauchbarer Umgebung, (P) gilt nach Lemma P6″; Lemma C′ entfällt. In Schritt 6 bekommt B am Schwanz den zusätzlichen Anfang ξ (k\_T = 0) bzw. P (Scheibe k\_T); in den Scheiben < k\_T ist B = C. Das Integral läuft über P ∈ G\_P statt über freie Enden, und das Bezugsmaß ist µ^{(k\_T, k\_H)} (Lemma M14b′). Die Schranke s^{−2(1 + k\_T)} für die übrigen Kerne bleibt.

**Stand.** W1 ist damit behoben: Restsatz M14 gilt mit spätem Anfang am Schwanz, gegeben Lemma M14b′ statt M14b. Die beiden Sonderfälle aus M.9.10 bleiben [B]; der späte Anfang ändert an ihnen nichts Wesentliches (Kopf- und Schwanzende in derselben Scheibe heißt jetzt: k\_T = k\_H mit Erzeugung und Vernichtung nahe beieinander).

## M.5 Was als Nächstes kommt

| Schritt                 | Stand nach Teil 1                                                                                                                          | was zu tun ist                                 |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| Z.2 Kernfaktoren        | [S, gegeben (K1), (K2′)] (Lemma M8, Teil 2)                                                                                                | erledigt                                       |
| Z.3, Z.4 Nenner         | [S, gegeben Lemma P6″, Lemma C (c), Lemma F13, Lemma M4] (Lemma M5, Folgerung M6, M7, Teil 2)                                              | erledigt; Bedingung (B1) an R in Z.9 eintragen |
| Z.5 Stabilität          | [S, gegeben Lemma U4 und M1–M3] (Lemma M4)                                                                                                 | Listen: erledigt in Teil 4 (Lemma M11)         |
| Z.6 Kreuzvergleich      | [S, gegeben M4, M6–M8, G3′] (Lemma M9, Teil 3)                                                                                             | erledigt                                       |
| Z.7 Defekte unter µ\_ab | [S]                                                                                                                                        | mit Lemma M3 und Klausel (v) unverändert       |
| Z.8 Summieren           | Auswahl, Listen, J, seltene Komponenten [S] (Lemma M10–M13); Endzellen [S, gegeben M4–M13, C, C′, P6″, Satz D] (Lemma M14a–e, M.9.5–M.9.9) | erledigt (M.9.9)                               |
| Satz D, D4              | Besucher eines Kastens [S, gegeben Satz T2] (satz\_3\_9 §10.8, C\_β ≥ 500)                                                                 | erledigt                                       |
| Konstruktion (G.12.1)   | geändert: gezogene Stücke regulär (M2); Klausel (v) (M1)                                                                                   | in G.12.1, G.12.5, Z.3, Z.5 eingetragen        |
