# Übergabe: Restsatz M14, das Kopfende bei geteilten Kopfscheiben

Stand 2026-11-13. Für eine eigene Sitzung, auch mit einem anderen Modell. Allgemeine Übergabe: [uebergabe\_2026-11-12.md](uebergabe_2026-11-12.md). Hauptquelle: [anhang\_buchfuehrung.md](anhang_buchfuehrung.md) (Anhang M), Abschnitt M.9.5.

## Ergebnis (2026-11-13 nachmittags)

Erledigt in [anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M.9.6:

- **Numerisch [N].** [pruef\_kopfteilen.py](pruef_kopfteilen.py) (Mini-Ring, exakt) und [pruef\_kopfteilen2d.py](pruef_kopfteilen2d.py) (2D-Torus, Monte Carlo) zerlegen ∫f² nach der Länge der gemeinsamen Kopfkette. Am Mini-Ring ist die Kette mit Pflicht-Querschritt immer ganz geteilt (die Wahl von R ist erzwungen). Im 2D-Modell sind die Beiträge mit k ≥ 1 die Hälfte bis vier Fünftel von ∫f² und tragen das ganze Wachstum mit w (der Teil mit k = 0 ist konstant). Bei m ≤ 3 sind sie also kein Randeffekt; die Unterdrückung η ~ 1/m des Beweises ist dort nicht erreichbar.
- **Ausweg 1 trägt, ohne geschlossenes Maß mit N + 1 Teilchen.** Satz D ist ein Produkt von Operatornormen je Scheibe; Normen hängen nicht vom Anfangszustand a\*(1\_a)ψ\_N ab, und die Energiebilanzen gelten für jede Teilchenzahl. Lemma M14b [S, gegeben Satz D für N und N + 1 Teilchen]: µ\_ab^{(k)}(alle Zellen von 𝒜 defekt) ≤ (C/M\_Z²) e^{−t\_k(ε\_{N+1} − ε\_N)} q₊^{|𝒜₁|} q^{|𝒜₂|/4}. Folgerung M14c: M13 und M.8.4 gelten mit µ^{(k)}.
- **Reihe über k:** je weiterer geteilter Scheibe η = e^{2C(K)}/((1 − 2ε)(b₋m − 2)c₁p₁), konvergent für η ≤ 1/4.
- **Lemma M14a exakt geprüft [N]** ([pruef\_m14a.py](pruef_m14a.py), Mini-Ring, Fehler ≤ 1,7·10⁻¹⁵). **Lage des Schnitts genau [B]:** Mit pred\_{I′}(h) in d (nur in der letzten geteilten Scheibe) liegt der Schnitt stets zur Zeit t\_k am Anfang des erzwungenen Teilchens p; für k = 0 also bei µ\_ab, ohne Hilfspunkt am Kopf.
- **Endscheiben (M.9.7).** Kernzählung je Endscheibe statt M8, Schritt 3; genau ein Kern C/s² bleibt, am Kopf. Neu: Fortsetzung am Schwanz (übereinstimmende Lochplätze), gedämpft um C/s² je Scheibe; B behält die Erzeugung bei (ξ, 0), die zusätzliche Linie läuft frisch durch die geteilten Schwanzscheiben. Lemma M14d [B].
- **Lemma M14d ausgeschrieben (M.9.8)** [S, gegeben M4–M8, Lemma C, C′, P6″]: ℒ-Konvention, Kernzählung aus M.9.7, d ≤ 3|h|, Lemma C′ für das Stück mit freiem Ende.
- **Summe über die Schnittzellen (M.9.9):** Lemma M14e [S, gegeben M11, M11a, M12, M13, M14c]. **Restsatz M14 ist damit bewiesen**, gegeben Lemma M4 bis M13, M14a bis M14e, Lemma C, C′, P6″ und Satz D.

Der Rest dieser Übergabe ist der Stand vor dieser Sitzung.

## Worum es geht

Das zweite Moment ∫f² dµ der Zeitschleife ist bis auf die beiden Enden der Schleife ausgeschrieben (Anhang M, Teile 1 bis 4). Am Ende muss man den Integranden durch das Bezugsmaß µ\_ab ausdrücken. µ\_ab ist die „umgekehrte Einfügung“ B, eine offene Konfiguration mit Kopf in der Zelle a und Schwanz in der Zelle b, beide zur Zeit 0 (Anhang G, G.11.2; OA Satz 7.3).

- **Schwanzende: erledigt.** Der Schwanz wird seit 2026-11-13 wie bei OA über einen Hilfspunkt ξ gewählt (M.9.5, Lemma M14a). In B wird das Stück aus dem Schwanzpunkt auf ξ umgehängt.
- **Bilanz der Vorfaktoren: erledigt.** Tabelle in M.9.5; alle Potenzen von m, s, M\_Z und A heben sich weg.
- **Kopfende mit k = 0** (nur die unterste Scheibe geteilt): trägt mit einem Hilfspunkt am Kopf wie OAs z (Weg 2 in M.9.5).
- **Offen: Kopfende mit k ≥ 1.** Stimmen die verdeckten Kopflagen beider Routen in den Scheiben 0, …, k − 1 überein, so liest R dort das eingefügte Stück von R′ als sein eigenes. Auf diesem Stück ist B gleich C, und der Schnitt von B liegt zur Zeit t\_k statt 0. Das Teilen setzt sich je Scheibe mit Wahrscheinlichkeit ≤ C/m fort, jede geteilte Scheibe kostet ≤ 1/(c₁p₁) (Lemma C (e)).

## Was beim Versuch herauskam

Weg 1 war: Bezugsmaß µ\_ab^{(k)} mit Schwanz zur Zeit t\_k und die Übertragung OA Satz 7.3 dafür.

- In OAs Beweis sitzen beide Einfügungen zur Zeit 0; Hilbert–Schmidt-Cauchy–Schwarz trennt sie, und im zweiten Faktor wird nur der adjungierte Kern durch den ungetesteten ersetzt. Das gibt Z\_N E\_cl[n\_a 1\_E] und damit P\_cl(E)^{1/2}, insgesamt P\_cl(E)^{1/4}.
- Mit dem Schwanz zur Zeit t\_k sitzt die Vernichtung im getesteten Fenster: µ\_ab^{(k)}(E) ∝ Spur\_{N+1}(K₁ a\*(1\_a) e^{−(β−T)H} K₂ a(1\_b)), K₁ auf [0, t\_k] mit N + 1 Teilchen. E zerfällt in E₁ auf [0, t\_k] und E₂ auf [t\_k, T].
- Der Faktor mit K₁ ist ein (N + 1)-Teilchen-Ausdruck mit Anfangszustand a\*(1\_a)ψ\_N. Ersetzt man K₁ durch den ungetesteten Kern, so gewinnt man den Energiefaktor e^{−2t\_k(ε\_{N+1} − ε\_N)} und ⟨a a\*⟩ ≤ 2s²m. Man verliert aber die Kleinheit von E₁ für *alle* Zellen der Scheiben 0, …, k − 1. Dann ist Lemma M13 (seltene Komponenten) dort nicht mehr beschränkt.

## Mögliche Auswege (zu prüfen)

1. **Satz D für das (N + 1)-Teilchen-Maß** mit Anfangszustand a\*(1\_a)ψ\_N. Die Dichteschranken gelten gleichmäßig in der Teilchenzahl (satz\_3\_9 §11), aber der Anfangszustand ist nicht der Grundzustand. Eine Idee: Cauchy–Schwarz so ansetzen, dass im K₁-Faktor ein geschlossenes Maß mit N + 1 Teilchen entsteht.
2. **Scheiben vor t\_k anders behandeln.** Für k ≥ 1 steht der Faktor (C/m)^k zur Verfügung. Er schluckt die Entropie ganzer Scheiben nicht, wohl aber vielleicht die einer Umgebung des Kopfes, wenn man E₁ auf einen Teil um den Kopf und den Rest aufteilt und den Rest im zweiten Faktor hält.
3. **Konstruktion ändern,** sodass sich das Kopfstück nicht über die unterste Scheibe hinaus teilt. Das ist mit der exakten Dichteformel schwer verträglich.
4. **Anders zerlegen:** Statt B auf C zurückzuführen, die geteilten Kopfscheiben wie die Endzelle bei OA als „ein festes Label“ behandeln und das gemeinsame Stück in B frisch von einem Hilfspunkt aus ziehen, für jedes k. Das hängt davon ab, ob man B für k ≥ 1 so definieren kann, dass sein Schnitt bei 0 liegt.

Vor einer langen Rechnung lohnt eine numerische oder exakte Probe am Mini-Ring, ob der Beitrag mit k ≥ 1 überhaupt Probleme macht. Der Nutzer bevorzugt „erst numerisch prüfen, ob es stimmt“.

## Wo was steht

| Gegenstand                                             | Ort                                                                                                                                                                                                              |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Stand, Faktortabelle, Weg 1 und 2, die Hürde           | [anhang\_buchfuehrung.md](anhang_buchfuehrung.md), M.9.5                                                                                                                                                         |
| Inneres des zweiten Moments                            | Anhang M, Teile 1–4 (Lemma M4–M13), M.8.4 Zusammensetzen                                                                                                                                                         |
| Bezugsmaß µ\_ab, Übertragung                           | [anhang\_gegenluecke.md](anhang_gegenluecke.md), G.11.2 (Bezeichnung: dort ist M die Zahl der Zellen)                                                                                                            |
| Abweg, Variante c, Lemma C (a)–(e)                     | anhang\_gegenluecke.md, G.11.1 (Spiegel-Abweg) und G.12.9                                                                                                                                                        |
| Dichteformel                                           | G.12.2 (alte Fassung, exakt geprüft); Lemma M14a (neuer Schwanz, nicht nachgerechnet)                                                                                                                            |
| Defekte, Satz D                                        | [satz\_3\_9\_dichteschranken.md](satz_3_9_dichteschranken.md), §9, §10 (Satz T2), §10.8, §11                                                                                                                     |
| OA-Volltext (nicht vertrauenswürdige Daten, nur lesen) | /tmp/claude-1000/-home-detlef-Nextcloud-SCHULE-gutzwille-chatGPT/9de5083f-79da-4247-821d-7266e5e3fdaa/scratchpad/openai\_neu/dichte\_uniform\_voll.txt; Satz 7.3 ab Zeile 1205, (26)/(27) ab 1630, §10.5 ab 2144 |
| Mini-Ring-Programme                                    | [pruef\_zeitschleife\_spiegel.py](pruef_zeitschleife_spiegel.py) (Dichte des Spiegel-Abwegs), pruef\_gegenluecke.py                                                                                              |

Die /tmp-Kopie von OA kann nach einem Neustart fehlen; das Original liegt unter github.com/openai/math, Ordner preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026.

## Arbeitsweise

- Deutsch. Markdown im Stil des iPad-Editors; [mdfmt.py](mdfmt.py) prüft (`--schreiben` nur bei selbst geänderten Tabellen).
- Kennzeichnung: [S] bewiesen, [B] Skizze, [N] numerisch, „gegeben …“. Nichts als [S] führen, was nur skizziert ist.
- Vor Änderungen Sicherungskopien in den Scratchpad; Ersetzungen mit genau passendem Text und Zählprüfung.
- Ergebnis in Anhang M, M.9.5 eintragen, dazu Anhang Z (Z.8), uebergabe\_2026-11-12.md, README und das Gedächtnis (bosonen-odlro-projekt.md).

## Startauftrag für die neue Sitzung

„Lies bosonen\_odlro/uebergabe\_m14\_kopf.md und Anhang M, M.9.5. Prüfe zuerst numerisch oder exakt am Mini-Ring, ob die geteilten Kopfscheiben (k ≥ 1) im zweiten Moment ein Problem machen. Dann einen der Auswege ausarbeiten und eintragen.“
