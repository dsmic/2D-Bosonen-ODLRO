# Anhang S: Geometrie der Zeitschleifen (Skelette und orientierte Umwege)

Stand 2026-11-10 abends; S.0 und S.2 am 2026-11-12 an [anhang\_lochstueck.md](anhang_lochstueck.md) (Anhang L, Lochstück j₀) angepasst. Gehört zu [tutorial\_beweis\_verduennt.md](tutorial_beweis_verduennt.md) §4, §9.1 und §10, Punkte 2 und 5. Vorbild ist §8 der OpenAI-Arbeit „A density-uniform condensate bound for dilute Bose gases“ (OA). Kennzeichnung: [S] bewiesen, [S nach OA] bewiesen unter Verwendung eines OA-Lemmas, [B] Beweisskizze, [N] numerisch. Benutzt werden zwei OA-Lemmata. Lemma 8.1 ist samt Beweis nachgelesen (Review W3), der Beweis ist elementar (Anhang K, K.3), und die Übertragung auf Schleifen ist in S.1 ausgeschrieben. Lemma 8.2 liefert in S.2 die Konstruktion der Umwege und den Randzusammenhang (Paritätsbeweis nach Timár, nachgelesen am 2026-11-13; bis dahin war das hier übersehen, und S.2 benutzte eine abgewandelte Konstruktion, die nicht trug, Review 2026-11-13, W2). OA ist nicht in Lean formalisiert.

## Auf einer Seite

- **Lemma S1 (Begegnungen von Schleifen-Skeletten) [S nach OA].** OAs Skelett aus §8.1 ist schon eine Schleife, wenn man die erste Koordinate als Zeit liest. Zwei unabhängige Schleifen haben beschränkte exponentielle Begegnungsmomente, einschließlich der neuen Paarungen Aufweg gegen fremden Abweg.
- **Lemma S2 (orientierte Umwege) [S nach OA]** (Konstruktion und Randzusammenhang aus OA Lemma 8.2; seit 2026-11-13 abends wörtlich OAs Konstruktion, Review 2026-11-13, W2). Die Lage der Schleife zur Zeit t\_k liegt außerhalb der Füllungen beider angrenzenden Scheiben. Innerhalb einer Scheibe umläuft der Weg wie bei OA die äußersten Füllungen auf ihrem Außenrand, als Sternpfad. Dann gibt es den Weg immer, keine Komponente kann die Schleife einfangen, und die Abweichung vom Skelett hat exponentielle Schwänze.
- **Was bleibt:** die Begegnungen der *tatsächlichen* Schleifen (Skelett plus Umweg) im zweiten Moment aufzusummieren. Das ist OAs Argument aus §10.5 und gehört zur Buchführung von Satz 5.2 (Tutorial §10, Punkt 1).

| Teil                                  | Stand                                        | Gegenstück bei OA | Prüfung                                    |
|---------------------------------------|----------------------------------------------|-------------------|--------------------------------------------|
| S1 Skelett-Begegnungen für Schleifen  | [S nach OA]                                  | Lemma 8.1         | pruef\_schleifen\_geometrie.py, Teil 1 [N] |
| S2 orientierte Umwege                 | [S nach OA]                                  | Lemma 8.2         | pruef\_schleifen\_geometrie.py, Teil 2 [N] |
| S3 Schwänze der Abweichung            | [S], gegeben die gemeinsame Peierls-Schranke | §8.2 Schluss      | Teil 2 [N]                                 |
| Summieren mit den tatsächlichen Wegen | [B]                                          | §10.5             | –                                          |

## S.0 Rahmen

- **Zellen:** n = L/s Zellen je Richtung, Zellgitter Λ\_n = (ℤ/nℤ)². Scheibe k ist das Zeitintervall (t\_k, t\_{k+1}) der Länge δ.
- **Schleife:** Endzellen a (Zelle von x) und b (Zelle von y), beide zur Zeit 0. Die Aufwärts-Hälfte U hat Lagen r\_0 = a, r\_1, …, r\_w zu den Zeiten t\_0, …, t\_w; die Abwärts-Hälfte D hat Lagen r′\_w, …, r′\_0 = b, mit r′\_w = r\_w (Wende). W = 2w ist die Gesamtlänge.
- **Was der Staffellauf von einer Lage verlangt:** In Scheibe k steigt das Loch von der Zelle, in der das Stück j₀ endet, zyklisch bis zur Zelle r\_{k+1} um. Alle dabei benutzten Zellen müssen in Scheibe k brauchbar sein. j₀ beginnt bei r\_k. Es ist regulär, weil j\_m der Scheibe davor nur unter Stücken mit regulärer Fortsetzung gewählt wird (Anhang L, Lemma L1), und endet deshalb höchstens D + 1 Zellen entfernt. (Bis 2026-11-11 stand hier: „ist die Umgebung von r\_k in Scheibe k gut, endet es höchstens D Zellen entfernt“. Das folgt nicht, denn eine gute Zelle darf einzelne Fehlgänger enthalten; Review K3.)
- **Schlechte Zellen:** 𝔅 ⊂ Λ\_n × ℤ ist die Menge der Raum-Zeit-Zellen, die in ihrer Scheibe nicht brauchbar sind (brauchbar einschließlich der Klauseln (iii) und (iv) aus Anhang L, L.1), *räumlich verdickt* um D′ = 2D + 2 (bis 2026-11-12: D + 2; der größere Wert nimmt den Ball des Abwegs auf, Review W1): Ist (c, k) roh schlecht, gelten alle (c′, k) mit |c′ − c|\_∞ ≤ D′ als schlecht. 𝔅\_k ist der Schnitt mit Scheibe k.

## S.1 Lemma S1: Begegnungen von Schleifen-Skeletten

**Skelett (OA §8.1 wörtlich).** Für q = 1, 2 seien U^{(q)}\_{ℓ,j} unabhängig und gleichverteilt auf [−1, 1], c\_vel = (1 − 2^{−1/4})/2 und

```text
v_i^{(q)} = c_vel Σ_{ℓ≥0} 2^{−ℓ/4} U^{(q)}_{ℓ, ⌊(i−1)/2^ℓ⌋},        Z_t^{(q)} = Σ_{i=1}^{t} v_i^{(q)},        |v_i| ≤ 1/2
```

**Als Schleife gelesen.** Mit dem Fortschritt σ ∈ {0, …, W} und der gehobenen Verschiebung d = b − a ist die Grundlage

```text
Zeit(σ) = min(σ, W − σ),        Lage(σ) = a + ⌊σ d/W + Z_{min(σ, W−σ)}⌋
```

Die Lagen mit σ ≤ w bilden U, die mit σ ≥ w bilden D. Zwischen zwei Grundlagen wird wie bei OA mit höchstens zwei Schritten je Koordinate verbunden. Zur selben Zeit u liegen U und D derselben Schleife um die feste Verschiebung (1 − u/w) d auseinander; an der Wende u = w treffen sie sich.

**Zulässig** heißt: W ≤ n/8 und |d|\_∞ ≤ W. Das sind OAs „admissible pairs“ mit OAs w = W. Ein fester Anteil υ ≈ 1/16 aller Endpaare (a, b) ist zulässig, und man beschränkt µ von unten durch seine Einschränkung auf diese Paare.

**Lemma S1 [S nach OA].** Seien R, R′ zwei unabhängige Schleifen-Skelette mit denselben zulässigen Endzellen, R\* ≥ 1, und

```text
J = Σ_{u=0}^{w}  Σ_{A ∈ {U, D}, B ∈ {U′, D′}}  1{ d_∞(A(u), B(u)) ≤ R* }
```

Dann gibt es absolute Konstanten c > 0 und C < ∞ mit E e^{αJ} ≤ C für α = c/(1 + R\*)², gleichmäßig in n, W und den zulässigen Paaren.

*Beweis.*

1. **Kein Herumlaufen.** Für u ≤ w ist |Z\_u| ≤ u/2 ≤ W/4 ≤ n/32 und |(1 − 2u/W) d| ≤ W ≤ n/8. Alle Differenzen unten sind also kleiner als n/2, und der Torus-Abstand ist der gehobene Abstand.
2. **Zurückführen auf Z − Z′.** Die linearen Anteile sind beiden Schleifen gemeinsam. Bis auf Rundung (höchstens 1 je Koordinate) gilt

   ```text
   U(u) − U′(u) = D(u) − D′(u) = Z_u − Z′_u,        U(u) − D′(u) = Z_u − Z′_u + s_u,        D(u) − U′(u) = Z_u − Z′_u − s_u
   ```

   mit der festen Verschiebung s\_u = (2u/W − 1) d. Also ist J ≤ 4 Σ\_u X\_u mit X\_u = min(1, Σ\_{s ∈ {0, s\_u, −s\_u}} 1{|Z\_u − Z′\_u + s|\_∞ ≤ R\* + 1}). Bei OA kommt nur s = 0 vor, weil dort die Zeiten u und W − u an verschiedenen Orten liegen.
3. **Bedingte Dichte (OA).** F\_t enthält alle Variablen von R′ und die bis zur Zeit t benutzten von R. Für t + k ≤ w enthält das Intervall (t, t + k] einen unbenutzten dyadischen Block der Länge ≥ k/4. Er trägt einen gleichverteilten Summanden der Breite ≥ c k^{3/4} bei, je Koordinate unabhängig. Also hat Z\_{t+k} gegeben F\_t eine Dichte ≤ C k^{−3/2}. Diese Schranke sieht eine feste Verschiebung nicht. Deshalb gilt

   ```text
   E[ X_{t+k} | F_t ]  ≤  min(1, 3 C (2R* + 3)² k^{−3/2}),        E[ Σ_{u>t} X_u | F_t ]  ≤  b₀ = C′ (1 + R*)²
   ```

4. **Exponentielles Moment (OA).** Ausmultiplizieren von e^{θΣX\_u} = Π(1 + (e^{θX\_u} − 1)), mit e^{θx} − 1 ≤ (e^θ − 1)x für 0 ≤ x ≤ 1 und der Schranke aus Schritt 3 auf geordneten Tupeln, ergibt E e^{θΣX\_u} ≤ Σ\_j [(e^θ − 1)(b₀ + 1)]^j. Mit θ = 4α klein genug gegen 1/(b₀ + 1) folgt die Behauptung. ∎

**Der einzige Unterschied zu OA** ist der Test X\_u mit drei statt einer Verschiebung. Dadurch wird b₀ höchstens dreimal so groß, und α schrumpft um einen festen Faktor.

**Zahlen [N]** ([pruef\_schleifen\_geometrie.py](pruef_schleifen_geometrie.py), Teil 1; R\* = 1, 4000 Paare):

| W    | d            | E J gleiche Hälften | E J Gegenhälften | E e^{0,005J} | J 99 % | J 99,9 % |
|------|--------------|---------------------|------------------|--------------|--------|----------|
| 64   | (32, 16)     | 43,6                | 1,8              | 1,26         | 71     | 71       |
| 256  | (128, 64)    | 63,4                | 0,6              | 1,42         | 212    | 252      |
| 1024 | (512, 256)   | 74,8                | 0,2              | 1,55         | 302    | 400      |
| 4096 | (2048, 1024) | 81,6                | 0,07             | 1,67         | 370    | 562      |
| 4096 | (0, 0)       | 81,4                | 81,4             | 4,45         | 768    | 1064     |

- Der Mittelwert ist beschränkt (Abstand der Zuwächse fällt wie W^{−1/2}).
- Die Gegenhälften spielen für d ≠ 0 kaum eine Rolle; für d = 0 fallen U und D zusammen und verdoppeln J.
- **Das Budget ist klein.** Die Skelette trennen sich erst nach etwa 30 Schritten, weil c\_vel ≈ 0,08 klein ist. Rechnet man OAs Konstante aus, ist b₀ ≈ 600 für R\* = 1. Garantiert ist also nur θ ≲ 10⁻³, und bei θ = 0,005 wächst E e^{θJ} im gerechneten Bereich noch langsam mit W. Für den Existenzsatz genügt jedes positive α. Für eine vernünftige Schwelle wäre ein Skelett mit größerer Geschwindigkeit besser (längere Umsteigeketten je Scheibe gegen schnellere Trennung).
- **Torus:** Ohne die Bedingung W ≤ n/8 kommen etwa 9 W/n² Begegnungen hinzu (Zeile n = 64 in ergebnisse/pruef\_schleifen\_geometrie\_teil1.txt). Steile Schleifen mit n ≪ W ≤ n² bleiben also beschränkt, brauchen aber eine Torus-Fassung von Schritt 3 [B].

## S.2 Lemma S2: Orientierte Umwege

OA §8.2 führt einen räumlichen Pfad, der in jede Richtung laufen darf, am Außenrand gefüllter Komponenten vorbei. Unsere Hälften laufen in der Zeit nur in eine Richtung. Eine Komponente, die zu einer Zeit ein Ring ist und sich später schließt, könnte eine Schleife einfangen, die in ihr Inneres geraten ist. Die folgende Konstruktion schaut genau eine Scheibe voraus und verhindert das.

**Komponenten und Füllungen (wie OA §8.2, wörtlich).** Komponenten von 𝔅\_k sind die Komponenten bezüglich Nachbarschaft über Kanten. Eine Komponente T mit weniger als n/4 Zellen hebt sich zu einer endlichen zusammenhängenden Menge in ℤ²; einfache Kreise in T sind zu kurz, um den Torus zu umlaufen. Ihre **Füllung** F(T) ist T zusammen mit den endlichen Kanten-Komponenten ihres Komplements in ℤ², auf den Torus zurückprojiziert. Sie liegt im umschreibenden Kasten von T, also ist diam F(T) ≤ |T|. F\_k ist die Vereinigung der Füllungen aller Komponenten von 𝔅\_k und E\_k = Λ\_n \ F\_k. Eine Füllung heißt *äußerst*, wenn sie in keiner anderen liegt. Der *Außenrand* ∂F(T) ist die Menge der Zellen außerhalb von F(T) mit einem Kantennachbarn in F(T).

Aus dem Beweis von OA Lemma 8.2 (nachgelesen; er ist für ein beliebiges kubisches Zellgitter geschrieben und gilt für das ebene Zellgitter einer Scheibe wörtlich) werden drei Tatsachen benutzt:

- **(F1)** Eine Kante von F(T) in sein Äußeres beginnt in T.
- **(F2)** Die Füllungen zweier verschiedener Komponenten sind ineinander geschachtelt oder disjunkt und nicht über eine Kante benachbart.
- **(F3)** ∂F(T) hat höchstens 6|T| Zellen und ist im Sterngraph (Schritte der ℓ∞-Länge 1) zusammenhängend. Der Beweis ist ein Paritätsargument im Zyklenraum nach Timár.

Für eine äußerste Füllung liegt ∂F(T) in E\_k: Läge eine Randzelle x in einer Füllung F(T′), so wären F(T′) und F(T) nach (F2) geschachtelt, und wegen x ∉ F(T) läge F(T) in F(T′). Das widerspricht „äußerst“. Insbesondere ist x nicht schlecht, denn eine schlechte Zelle liegt in der Füllung ihrer Komponente.

**Strecke.** Zu zwei Zellen x, y sei σ(x, y) ein fest gewählter Kantenweg von x nach y im umschreibenden Kasten der beiden, etwa die Gitternäherung der geraden Strecke. Er hat |x − y|₁ ≤ 2 d\_∞(x, y) Schritte.

**Konstruktion.** Sei b\_0, …, b\_w die Grundlage einer Hälfte, also b\_k die Skelettlage zur Zeit t\_k. Mit A\_k = E\_{k−1} ∩ E\_k (A\_0 = E\_0) setzt man

```text
r_k  =  der Punkt von A_k mit kleinstem Abstand d_∞ zu b_k        (feste Regel bei Gleichstand)
Weg in Scheibe k  =  OAs Umwegverfahren in Scheibe k auf σ(r_k, r_{k+1}), danach chronologische Schleifenlöschung
```

Das **Umwegverfahren** (OA §8.2): Man durchläuft σ = σ(r\_k, r\_{k+1}). Betritt σ eine äußerste Füllung F(T) der Scheibe k, so ersetzt man das Stück vom letzten Punkt vor dem Eintritt bis zum ersten Punkt nach dem *letzten* Besuch von F(T) durch einen fest gewählten Sternpfad auf ∂F(T), und läuft von dort weiter.

**Verwerfen**, wie bei OA: wenn eine Komponente einer Scheibe ≥ n/4 Zellen hat, oder wenn a oder b zur Zeit 0 in F\_0 liegt.

**Lemma S2 [S nach OA].** Nach Verwerfen gilt für jede Hälfte:

1. **Gültig:** Alle r\_k existieren und liegen in E\_{k−1} ∩ E\_k, sind also in den Scheiben k − 1 und k gut. Der Weg in Scheibe k ist ein einfacher Sternpfad von r\_k nach r\_{k+1}, und alle seine Zellen liegen in E\_k, sind also in Scheibe k gut.
2. **Abweichung:** Ist b\_k ∉ A\_k, sei P\_k(b\_k) das über Kanten zusammenhängende Stück von F\_{k−1} ∪ F\_k, das b\_k enthält. Dann ist d\_∞(r\_k, b\_k) ≤ diam P\_k(b\_k) + 1.
3. **Weglänge und Lage:** Der Weg in Scheibe k hat höchstens 2 d\_∞(r\_k, r\_{k+1}) + Σ 6|T| Zellen. Summiert wird über die Komponenten T von 𝔅\_k, die σ(r\_k, r\_{k+1}) trifft. Jede Zelle des Wegs liegt auf σ(r\_k, r\_{k+1}) oder auf ∂F(T) für eine solche Komponente, also höchstens |T| + 1 Zellen von σ entfernt.
4. **Lokal:** Entfernt man ganze schlechte Komponenten, die weder zu einem Stück P\_k(b\_k) beitragen noch von einer der Strecken σ(r\_k, r\_{k+1}) getroffen werden, ändert sich die Schleife nicht.

*Beweis.*

1. A\_k ist nicht leer, denn F\_{k−1} ∪ F\_k ist klein gegen Λ\_n; also gibt es r\_k. Weil r\_{k+1} ∈ A\_{k+1} ⊂ E\_k ist, beginnt und endet σ außerhalb aller Füllungen der Scheibe k. Betritt σ eine äußerste Füllung F(T), so liegt der Punkt davor außerhalb und ist Kantennachbar, liegt also auf ∂F(T); ebenso der erste Punkt nach dem letzten Besuch. Nach (F3) verbindet sie ein Sternpfad auf ∂F(T), und ∂F(T) ⊂ E\_k. Die nicht ersetzten Punkte von σ liegen außerhalb aller äußersten Füllungen, also außerhalb aller Füllungen. Jede Komponente wird höchstens einmal umlaufen (Regel des letzten Besuchs), und die Schleifenlöschung entfernt nur Punkte. Das ist OA Lemma 8.2 für die Scheibe k.
2. P = P\_k(b\_k) ist ein maximales über Kanten zusammenhängendes Stück. Ein Kantennachbar außerhalb von P liegt nicht in F\_{k−1} ∪ F\_k, sonst gehörte er zu P. Geht man von b\_k geradeaus, verlässt man P nach höchstens diam P + 1 Schritten und landet in A\_k.
3. σ hat höchstens 2 d\_∞(r\_k, r\_{k+1}) Schritte. Jede umlaufene Füllung F(T) wird von σ über eine Kante betreten, die nach (F1) in T endet; T wird also von σ getroffen. Sie ersetzt ein Stück von σ durch höchstens |∂F(T)| ≤ 6|T| Zellen. Randzellen sind Kantennachbarn von F(T), und F(T) trifft σ und hat Durchmesser ≤ |T|.
4. r\_k hängt nur von P\_k(b\_k) ab. Der Weg hängt nur von den äußersten Füllungen ab, die σ betritt, und diese gehören nach Schritt 3 zu Komponenten, die σ trifft (OAs „deletion invariance“). ∎

*Zur Kennzeichnung und Geschichte.* Bis 2026-11-13 abends stand hier eine abgewandelte Konstruktion: eine gemeinsame Füllung von ganz 𝔅\_k (alle endlichen Komponenten des Komplements von 𝔅\_k) und ein kürzester Kantenweg in E\_k, mit der Behauptung, E\_k sei über Kanten zusammenhängend. Das trug nicht (Review 2026-11-13, W2). Schlechte Zellen, die sich nur an Ecken berühren, sind lauter Komponenten der Größe 1. Ein diagonaler Ring aus solchen Zellen wurde als Ganzes gefüllt, und Weglänge und Lokalität hingen dann von Komponenten ab, die die Strecke nicht treffen. Eine diagonale Kette um den Torus machte E\_k unzusammenhängend. Jetzt ist die Konstruktion die von OA: Füllung je Komponente und Sternpfade. Ein Ring, der nur über Ecken zusammenhängt, hält einen Sternpfad nicht auf. Ein Zusammenhang von E\_k wird nicht mehr gebraucht. Die Kennzeichnung [S nach OA] gilt, weil Schritt 1 und 3 OA Lemma 8.2 samt Beweis benutzen ((F1) bis (F3), Paritätsbeweis nach Timár, Proc. AMS 141, 2013). Gegenüber der alten Fassung ist die Schranke der Weglänge doppelt so groß (Kantenweg statt d\_∞); das ändert in Anhang M nur die Konstante C\_J (M.8.2).

**Warum nichts einfangen kann.** Die Lage r\_k liegt zur Zeit t\_k *auch* außerhalb der Füllung der folgenden Scheibe. Schließt sich ein Ring (eine über Kanten zusammenhängende Komponente) in Scheibe k zu einer Kuppel, ist sein Inneres in seiner Füllung, also in F\_k, und die Schleife steht schon zur Zeit t\_k außerhalb. Innerhalb einer Scheibe darf sie beliebig weit räumlich umsteigen, deshalb reicht dieser eine Schritt Vorausschau.

**Was der Staffellauf braucht.** Wegen der Verdickung um D′ = 2D + 2 sind alle Zellen im Abstand ≤ 2D + 2 vom Weg in Scheibe k roh gut. Für den Abweg mit Variante c (G.12.9) heißt das: Der neue Kopf S′ liegt höchstens D\_c ≤ D − 1 Zellen neben der Lage, Lemma C verlangt nicht defekte Zellen im Abstand ≤ D\_c + D ≤ 2D − 1 von Y\_m, und die Umsteigekette der nächsten Scheibe führt von der Zelle von S′ durch roh gute Zellen zum Weg. Das Stück j₀ beginnt bei r\_k, ist regulär (Anhang L, Lemma L1) und endet höchstens D + 1 Zellen entfernt; von dort führt eine Umsteigekette durch roh gute Zellen zum Weg und auf ihm nach r\_{k+1}. In r\_{k+1} gibt es genug Stücke mit regulärer Fortsetzung für die Wahl von j\_m: r\_{k+1} liegt nach Lemma S2 (1) auch in der Scheibe k + 1 außerhalb der Füllung, und Lemma L2 gibt den Vorrat (1 − 2ε) n\_Q.

**Zahlen [N], alte Fassung** (Teil 2, gemeinsame Füllung und kürzester Kantenweg, wie bis 2026-11-13 abends; n = 48, 96 Scheiben, schlechte Zellen unabhängig mit Wahrscheinlichkeit p, dazu 20 Kuppeln mit Radius 2–4, je 40 Skelette):

| p    | Kuppeln | ungültige Wege | P(Abw ≥ 1) | P(Abw ≥ 2) | P(Abw ≥ 4) | größte Abw | mittlerer Mehrweg |
|------|---------|----------------|------------|------------|------------|------------|-------------------|
| 0,01 | 0       | 0              | 0,021      | 0          | 0          | 1          | 0,03              |
| 0,03 | 0       | 0              | 0,059      | 0          | 0          | 1          | 0,05              |
| 0,06 | 0       | 0              | 0,118      | 0          | 0          | 1          | 0,11              |
| 0,03 | 20      | 0              | 0,064      | 0,0026     | 0          | 3          | 0,06              |
| 0,06 | 20      | 0              | 0,119      | 0,0063     | 0          | 3          | 0,08              |

**Zahlen [N], jetzige Fassung** ([pruef\_schleifen\_geometrie.py](pruef_schleifen_geometrie.py), Teil 3, ergebnisse/pruef\_schleifen\_geometrie\_teil3.txt; OAs Umwegverfahren mit Füllung je Kanten-Komponente; sonst wie Teil 2, dazu diagonale Ringe |a| + |b| = r mit r = 3–7 über 20 Scheiben, deren Zellen sich nur an Ecken berühren). „Fehler“ zählt Wege, bei denen ein Außenrand nicht sternzusammenhängend war, in einer Füllung lag, oder der Weg E\_k verließ.

| p    | Kuppeln | diagonale Ringe | Fehler | Länge über der Schranke aus S2 (3) | P(Abw ≥ 1) | P(Abw ≥ 2) | größte Abw | mittlerer Mehrweg |
|------|---------|-----------------|--------|------------------------------------|------------|------------|------------|-------------------|
| 0,01 | 0       | 0               | 0      | 0                                  | 0,020      | 0          | 1          | 0,02              |
| 0,03 | 0       | 0               | 0      | 0                                  | 0,045      | 0          | 1          | 0,05              |
| 0,06 | 0       | 0               | 0      | 0                                  | 0,108      | 0          | 1          | 0,07              |
| 0,03 | 20      | 0               | 0      | 0                                  | 0,101      | 0,012      | 3          | 0,06              |
| 0,06 | 20      | 0               | 0      | 0                                  | 0,141      | 0,009      | 4          | 0,10              |
| 0,03 | 0       | 40              | 0      | 0                                  | 0,104      | 0          | 1          | 0,04              |
| 0,06 | 20      | 40              | 0      | 0                                  | 0,175      | 0,028      | 4          | 0,08              |

Einzeln das Gegenbeispiel aus W2: Ein diagonaler Ring aus 32 Zellen der Größe 1 wird nicht gefüllt; eine Strecke von innen nach außen trifft eine Ringzelle, und der Weg hat die Länge d\_∞ = 18, ohne Umlauf um den Ring.

## S.3 Schwänze der Abweichung

**Eingang.** Die gemeinsame Peierls-Schranke für schlechte Zellen (Tutorial Satz 7.1 mit Lemma 6.8 und dem Defekt-Lemma; Tutorial §10, Punkt 3): Für jede Menge 𝒜 von Raum-Zeit-Zellen ist P(alle Zellen von 𝒜 sind roh schlecht) ≤ q^{|𝒜|}. Nach der Verdickung um D′ braucht eine verdickt schlechte Menge 𝒜 mindestens |𝒜|/(2D′ + 1)² roh schlechte Zellen, und es gilt eine Schranke derselben Form mit q′ = (C(D′) q)^{1/(2D′+1)²}.

**Lemma S3 [S, gegeben den Eingang].** Für jede Zelle c und Scheibe k ist P(diam P\_k(c) ≥ ℓ) ≤ C (C q′)^{ℓ/8}.

*Beweis.*

1. **Innerhalb einer Scheibe ketten Füllungen nicht.** Nach OA (Beweis von Lemma 8.2) sind die Füllungen zweier getrennter Komponenten derselben Scheibe entweder ineinander geschachtelt oder disjunkt und nicht benachbart. Die Stücke von F\_k allein sind also die Füllungen der äußersten Komponenten, und jede hat Durchmesser ≤ |T|.
2. **Über zwei Scheiben** ist P\_k(c) eine zusammenhängende Vereinigung äußerster Füllungen aus den Scheiben k − 1 und k. Je zwei sich schneidende oder berührende Füllungen verbindet man; der so entstehende Überlappungsgraph wechselt zwischen den beiden Scheiben.
3. **Kette.** Ist diam P ≥ ℓ, liegt ein Punkt von P im Abstand ≥ ℓ/2 von c. Ein kürzester Weg T₁, …, T\_j im Überlappungsgraphen von der Füllung, die c enthält, zu diesem Punkt hat Σ\_i (|T\_i| + 1) ≥ ℓ/2, also Σ\_i |T\_i| ≥ ℓ/4.
4. **Zählen.** Gegeben T\_i, liegt T\_{i+1} im Abstand ≤ |T\_{i+1}| + 1 von der Füllung von T\_i, also im umschreibenden Kasten von T\_i vergrößert um |T\_{i+1}| + 1. Für einen Wurzelpunkt von T\_{i+1} gibt es höchstens C(|T\_i| + |T\_{i+1}|)² Möglichkeiten, für seine Form höchstens C^{|T\_{i+1}|}. Die Komponenten sind paarweise disjunkte Mengen von Raum-Zeit-Zellen, also hat die Kette die Wahrscheinlichkeit ≤ q′^{Σ|T\_i|}.
5. **Summe.** Jedes |T\_i| kommt in höchstens zwei polynomialen Faktoren vor; mit |T|⁴ ≤ C 2^{|T|} schluckt man sie. Die Summe über alle Ketten mit Σ|T\_i| ≥ ℓ/4 ist ≤ C (C q′)^{ℓ/8}. ∎

**Verwerfen ist selten.** Eine Komponente mit ≥ n/4 Zellen in einer der 2w + 1 Scheiben hat die Wahrscheinlichkeit ≤ C n² w (C q′)^{n/4} → 0. Dass a oder b in F\_0 liegt, hat die Wahrscheinlichkeit ≤ Σ\_j C j³ (C q′)^j, klein für kleines q′.

## S.4 Was noch fehlt

- **Summieren mit den tatsächlichen Wegen [B].** Im zweiten Moment begegnen sich die tatsächlichen Schleifen, nicht die Skelette. Ihre Begegnungen sind höchstens die der Skelette mit vergrößertem Radius, plus Beiträge der Stücke P\_k und der umlaufenen Füllungen nahe beider Skelette. OA erledigt das in §10.5 mit der Lokalität (Lemma S2, 4) und der Schranke für vorgegebene schlechte Mengen unter dem Bezugsmaß (Satz 7.2 und 7.3 dort, bei uns G.11.2). Das gehört zur Buchführung von Satz 5.2 (Tutorial §10, Punkt 1) und wird dort ausgeschrieben.
- **Abwärts-Hälfte:** Sie benutzt dieselben Füllungen und dieselbe Regel, mit der Zeit rückwärts gelesen. An der Wende ist r′\_w = r\_w, weil beide Hälften dieselbe Grundlage und dieselbe Regel benutzen.
- **Steile Schleifen** (nur Schwelle): Torus-Fassung von S1, Schritt 3.
