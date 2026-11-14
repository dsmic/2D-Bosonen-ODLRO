# Z2.1: Stufe A, Definition, Satz, Formfaktor

Teil von [z2_plan.md](z2_plan.md). Ergebnis vorweg: Stufe A ist exakt stoquastisch in einer Eichung, die genau der
d-Wellen-Formfaktor ist. Entscheidungspunkt E1: **d-Welle**.

## 1. Gitter und Bausteine

- $L\times L$-Quadratgitter, periodisch, $L$ gerade. Plätze $s=x+Ly$; gerade Plätze ($x+y$ gerade) und ungerade.
- Néel-Zustand $|N\rangle$: ↑ auf geraden, ↓ auf ungeraden Plätzen (ein einzelner Fock-Zustand).
- Bindungen $b=\{u,v\}$ zwischen Nachbarn, Orientierung h (waagerecht) oder v (senkrecht).
- Singulett-Paaroperator $\Delta_b=c_{u\uparrow}c_{v\downarrow}-c_{u\downarrow}c_{v\uparrow}$ (symmetrisch in $u,v$).

## 2. Hilbertraum

- Konfiguration $D$: Menge von Bindungen, die sich *nicht berühren* (kein Platz einer Bindung ist gleich einem Platz
  oder Nachbar eines Platzes einer anderen).
- Basiszustand $|D\rangle:=\prod_{b\in D}\Delta_b|N\rangle$.
  - Wohldefiniert: Die $\Delta_b$ sind Produkte von zwei Fermionoperatoren und vertauschen miteinander (P1).
  - Normiert: Auf $|N\rangle$ überlebt von $\Delta_b$ genau ein Term, $\Delta_b|N\rangle$ ist ein Fock-Zustand.
  - Orthogonal: Verschiedene $D$ haben verschiedene Lochmengen.
- Spins außerhalb der Paare: fest im Néel-Zustand. Paardichte $n_D=x/2$ pro Platz bei Lochdotierung $x$.

## 3. Hamiltonoperator

Herleitung aus t-J in zweiter Ordnung in $t$ (Feshbach), mit genau einer Einschränkung: Als Zwischenzustände
zählen nur die *diagonalen* (Löcher im Abstand $\sqrt2$), nicht die geraden (Abstand 2). Das ist die Einschränkung
aus dem Auswahlsatz ([../auswahl_durch_interferenz.md](../auswahl_durch_interferenz.md)): Ohne die geraden
Zwischenzustände ist das Netz ausgeglichen; für ein einzelnes Paar bei $k=0$ ändert das die Energie nicht.

- **Eckschritt** $b=\{u,v\}\to b'=\{v,w\}$ mit rechtem Winkel bei $v$: Das Loch auf $v$ springt nach $w$, das Loch auf $u$
  folgt nach $v$. Der Spin von $w$ landet auf $u$ (gleiches Untergitter), der Néel-Zustand bleibt erhalten.
  Jedes Paar hat vier Eckschritte, einen über jeden diagonalen Zwischenzustand.
- **Erlaubt**, wenn $D\setminus\{b\}\cup\{b'\}$ wieder berührungsfrei ist. Der Zwischenplatz $w$ ist dann automatisch frei.
- **Amplitude** $t_c=t^2/(E_d-E)$, Ising-Abschätzung $E_d-E\approx\tfrac32J$, hier als Konstante genommen.
- **Diagonale:** konstant pro Paar. Die vier diagonalen Zwischenzustände sind bei berührungsfreien Konfigurationen
  immer verfügbar, und die Ising-Energie berührungsfreier Paare ist additiv.

In der physikalischen Basis $|D\rangle$:
$$H_A=\epsilon_0N_D+t_c\sum_{D\to D'\ \text{Eckschritt}}\big(|D'\rangle\langle D|+\mathrm{h.c.}\big),\qquad t_c>0 .$$
Das *positive* Vorzeichen ist das Ergebnis von P3 (§4).

## 4. Die Lemmata

**P1 (Vertauschbarkeit).** $\Delta_b\Delta_{b'}=\Delta_{b'}\Delta_b$; ein Paarschritt (vier Fermionoperatoren) hat in Gegenwart
anderer Paare dasselbe Matrixelement wie allein. *Beweis:* Vorbeiziehen von vier Fermionoperatoren gibt $(-1)^4$. □

**P3 (Vorzeichen der Folgeschritte).** Für jeden Folgeschritt (Ecke oder gerade) ist
$$A(b\to b')=\langle N|\Delta_{b'}^\dagger H_tH_t\,\Delta_b|N\rangle<0,$$
also $\langle b'|H_{\rm eff}|b\rangle=-A/(E_d-E)>0$.
*Herleitung:* Holon-Algebra in der Slave-Fermion-Darstellung gibt im geordneten Lochbasis-Zustand das Vorzeichen
$\operatorname{sgn}(v-u)\operatorname{sgn}(w-v)$; die Umrechnung auf die Singulettbasis liefert für jeden Schritt den Faktor
$-1$ ([../paartransfer_vorzeichen.md](../paartransfer_vorzeichen.md) §4.3,
[../zweite_quantisierung.md](../zweite_quantisierung.md)). Da $A$ ein geschlossener Prozess ist (Start und Ende
$|N\rangle$), hängt es nicht von der Fermion-Ordnung ab.
*Numerische Prüfung* ([check_p3.py](check_p3.py), direkte Fermion-Algebra mit Jordan-Wigner):

| Test | Ergebnis |
|---|---|
| $L=4$, alle Bindungen, alle Folgeschritte | Ecke: 128-mal $A<0$; gerade: 64-mal $A<0$; keine Ausnahme |
| $L=6$, ebenso (inkl. Schritte über den Rand) | Ecke: 288-mal $A<0$; gerade: 144-mal $A<0$ |
| $L=8$, Paar $b_1$ bewegt, zweites Paar $b_2$ an drei Positionen (auch nah, ohne Berührung) | in allen Fällen dasselbe Vorzeichen wie ohne $b_2$ (P1) |

Folge: Im Netz aller Folgeschritte haben Schleifen $W=(-1)^{\text{Länge}}$. Ungerade Schleifen (Dreiecke aus einem
geraden und zwei Eckschritten) sind frustriert; das ist die Lochstatistik (K−).

## 5. Satz A

**Satz.** Mit der Eichung $|D\rangle\mapsto(-1)^{N_v(D)}|D\rangle$ ($N_v$ = Zahl senkrechter Paare) hat $H_A$ nur die
Nebendiagonalelemente $-t_c$, ist also stoquastisch.
*Beweis:* Jeder Eckschritt wechselt die Orientierung eines Paares (h↔v), ändert $N_v$ also um $\pm1$; das kehrt das
positive Vorzeichen aus P3 um. Andere Paare beeinflussen das Matrixelement nicht (P1). □

**Folgerungen** (bei Irreduzibilität, also wenn die Eckschritte alle Konfigurationen verbinden). Bei 7/8-Füllung
($x=1/8$) ist $n_D=1/16$ pro Platz. Schon die einfache Anordnung „waagerechte Paare mit Periode 3 in jeder zweiten
Reihe“ erreicht $n_D=1/6$; die Paardichte liegt also bei höchstens etwa 40 % der dichtesten Packung, der Paarabstand
bei etwa 4 Gitterkonstanten.

**Vollständige Aufzählung** ([check_irreduzibel.py](check_irreduzibel.py)):

| System | Konfigurationen | Komponenten |
|---|---|---|
| 8×8, 2 Paare | 6 720 | 1 |
| 8×8, 3 Paare | 188 288 | 1 |
| 8×8, 4 Paare (7/8-Füllung) | 3 075 264 | 1 große (3 075 232) + 32 eingefrorene Einzelkonfigurationen |
| 4×4, 2 Paare (7/8) | 160 | 1 große (144) + 16 eingefrorene |

Die eingefrorenen Konfigurationen sind **Säulen, die sich um den Torus schließen**: vier parallele Paare im
Abstand 2 übereinander (bzw. nebeneinander), jedes blockiert vom nächsten. 8×8: 16 waagerechte und 16 senkrechte
Säulen. Das ist ein Effekt der periodischen Ränder; im unendlichen Gitter kann das Ende jeder Säule sich bewegen.

**Satz (8×8, 4 Paare, computergestützt).** Der Grundzustand von $H_A$ ist eindeutig, liegt in der großen Komponente
und ist dort in der d-Eichung positiv.
*Beweis:* Die eingefrorenen Zustände sind Eigenzustände mit Energie $4\epsilon_0$ ohne kinetischen Anteil. Auf der
großen, zusammenhängenden Komponente liefert Perron-Frobenius einen eindeutigen, positiven tiefsten Zustand mit
Energie $4\epsilon_0-t_c\lambda_{\max}<4\epsilon_0$. □
Das ist ein vollständiger Beweis für genau dieses endliche System (unter der Voraussetzung, dass Modell und Code
stimmen), nicht für andere Größen. Größere Tori haben zusätzlich Komponenten „umlaufende Säule + bewegliche
Paare“; auch dort tragen die Säulenpaare keine kinetische Energie.

Auf 4×4 ist Stufe A wegen des Berührungsverbots fast dicht gepackt; für Stufe A sind mindestens 8×8 nötig.
- Der Grundzustand ist in der Eichung positiv, in der physikalischen Basis also $\propto(-1)^{N_v(D)}$: Jedes Paar trägt
  den Formfaktor $f(\text{h})=+1$, $f(\text{v})=-1$. **Das ist $d_{x^2-y^2}$.**
- $\langle\Delta_d^\dagger(b)\Delta_d(b')\rangle\ge0$ für $\Delta_d(b)=f(b)\Delta_b$; die Impulsverteilung der d-Paare ist bei $k=0$
  maximal. Kondensieren die Paare, dann als gleichförmige d-Welle.
- In dieser Eichung ist $H_A$ ein Hardcore-Bosonenmodell auf dem *Mittelgitter* (Bindungsmitten; um 45° gedrehtes
  Quadratgitter mit Abstand $1/\sqrt2$), mit Nachbarhüpfen $-t_c$ und erweitertem Ausschluss (Berührungsverbot).
  Ein einzelnes Paar: $E(\mathbf k)=\epsilon_0-4t_c\cos\frac{k_x}2\cos\frac{k_y}2$, Minimum bei $k=0$.

Für Stufe A gilt damit exakt: $\sigma_2\equiv1$ (mit d-Formfaktor). Paar-ODLRO ist dort *genau* die Frage (B), ob
dieses Bosonenmodell kondensiert.

## 6. Was Stufe A weglässt (Modellabstand)

- gerade Folgeschritte und gerade Zwischenzustände (frustrieren, K−);
- Spindynamik (J⊥), Stufe B;
- ausgedehnte Paare, Stufe C (laut 4×4-ED bei $J/t=0{,}4$ nur ≈ 29 % Nachbarpaare);
- sich berührende Paare (Ising-Anziehung, Konkurrenz mit Phasenseparation; Überzähligkeit);
- Abhängigkeit der Zwischenenergie von der Umgebung ($t_c$ konstant gesetzt);
- nicht folgekonforme Prozesse (Domino, Pivot), Aufbrechen von Paaren.

## 7. Nächster Schritt (Z2.2)

Stufe A ist jetzt ein Standardproblem: Hardcore-Bosonen auf dem Mittelgitter mit erweitertem Ausschluss.
- Exakte Diagonalisierung kleiner Systeme (z. B. $L=6,8$ mit wenigen Paaren): Grundzustand positiv in der Eichung
  (Kontrolle von Satz A), Paarkorrelation über den Abstand, Kondensatanteil.
- Erwartung: Suprafluid bei kleiner Dichte, Kristall nahe dichtester Packung. Interessant wird es erst mit den
  Zusätzen aus §6.

## 8. RK-Punkt von Stufe A

**Satz (RK-Identität).** Sei $\mathcal C$ die Menge der berührungsfreien $P$-Paar-Konfigurationen, $A$ ihre Adjazenzmatrix
bezüglich Eckschritten (nach §3 symmetrisch, 0/1), $B(D)\in\{0,\dots,4P\}$ die Zahl der *blockierten* Eckschritte von $D$
(jedes Paar hat vier, jeder ist erlaubt oder blockiert). In der d-Eichung ist $H_A=\epsilon_0P-t_cA$. Mit
$\Lambda=\mathrm{Deg}-A\ge0$ (Graph-Laplace-Operator, $\mathrm{Deg}(D)=4P-B(D)$) gilt
$$H_A-t_c\,B=(\epsilon_0-4t_c)P+t_c\Lambda .$$
Der Grundzustand von $H_{RK}:=H_A-t_cB$ hat also die Energie $(\epsilon_0-4t_c)P$ und ist auf jeder Zusammenhangskomponente von
$\mathcal C$ die **Gleichverteilung** $\sum_D|D\rangle$ in der d-Eichung, in der physikalischen Basis
$\sum_D(-1)^{N_v(D)}|D\rangle$.
*Beweis.* $x^T\Lambda x=\sum_{D\sim D'}(x_D-x_{D'})^2$, Kern = lokal konstante Funktionen; $\mathrm{Deg}=4P-B$ ist die Definition von $B$. □

**Folgerungen** (rigoros, einzige Annahme: Satz A und die Zählung vier Eckschritte pro Paar).
1. $(\epsilon_0-4t_c)P\le E_0(H_A)\le(\epsilon_0-4t_c)P+t_c\langle B\rangle_{\rm gleich}$. Die untere Schranke ist die triviale
   Gershgorin-Schranke; neu ist, dass die obere Schranke ein *klassischer* Erwartungswert im Gas berührungsfreier Bindungen ist.
2. $H_{RK}$ unterscheidet sich von $H_A$ um $t_cB\ge0$ (Attraktion für blockierte Konfigurationen). Der RK-Zustand ist
   nicht der Grundzustand von $H_A$; Korrelationen des RK-Zustands sind die einer klassischen Gleichverteilung.

**Numerik** ([schraeg/rk_check.py](schraeg/rk_check.py) exakt, [schraeg/rk_mc.py](schraeg/rk_mc.py) Monte Carlo), 8×8,
Einheiten $t_c$, volle Aufzählung:

| Paare | Konfig. | $\max\lvert\Lambda\mathbf 1\rvert$ | $E_{RK}$ | $E_0(H_A)$ | $\langle B\rangle/P$ gleich (exakt / MC) | $(E_0-E_{RK})/P$ | $n_0$ RK (MC) | $n_0$ Stufe A (ED) |
|---|---|---|---|---|---|---|---|---|
| 2 | 6 720 | 0 | −8 | −7,8128 | 0,1905 / 0,189 | 0,094 | 0,82 | 0,75 |
| 3 | 188 288 | 0 | −12 | −11,3463 | 0,4006 / 0,402 | 0,218 | 0,66 | 0,56 |
| 4 | 3 075 264 | 0 | −16 | −14,5852 | 0,6329 / 0,634 | 0,354 | 0,51 | 0,36 |

Bei 4 Paaren hat $H_{RK}$ 33 entartete Grundzustände (die 32 eingefrorenen Säulen haben $B=4P$, Energie ebenfalls
$(\epsilon_0-4t_c)P$); der relevante ist die Gleichverteilung auf der großen Komponente. Die Schranken aus Folgerung 1 gelten
in allen Fällen, $E_0-E_{RK}$ liegt bei 49–56 % des oberen Abstands.

**Einordnung.**
- Numerisch beobachtet (3 Fälle, nicht bewiesen): $n_0^{RK}>n_0^{A}$; die Abweichung wächst mit der Dichte (0,07 → 0,10 → 0,15).
  Das Berührungsverbot allein (RK) lässt mehr Kohärenz als die echte Dynamik von $H_A$.
- Das RK-Resultat sagt *nichts Rigoroses* über ODLRO von $H_A$ selbst; es ist ein Vergleichspunkt. Für den RK-Zustand
  selbst ist Paar-ODLRO bewiesen, für $\rho_b<1/23$, also auch bei 7/8-Füllung (§10).
- $n_0$ (RK) ist der Rayleigh-Quotient des gleichförmigen Vektors zur Paardichtematrix (MC), gleich $\lambda_{\max}/n$ unter
  der Annahme, dass der gleichförmige Vektor der Perron-Vektor ist (Translations- und Drehsymmetrie; nicht eigens geprüft).
  Exakt durch Aufzählung ([check_rk_odlro.py](check_rk_odlro.py)): 0,8203 / 0,6573 / 0,5123; nach §10 ist es in jedem Fall
  eine untere Schranke für $\lambda_{\max}/n$.

## 9. Satz: Nachbarkohärenz, gleichmäßig in der Gittergröße

**Satz.** Sei $\psi_0$ ein Grundzustand von $H_A$ mit $P$ Paaren auf einem Torus mit $2N$ Bindungen, $\rho_b=P/2N$. Dann gilt für die
Paarkohärenz zwischen Bindungen, die durch einen Eckschritt verbunden sind (in der d-Eichung
$\langle A\rangle_0=\sum_{D\sim D'}\psi_0(D)\psi_0(D')$, physikalisch die Summe der d-Paarkorrelationen
$\langle\Delta_d^\dagger(b')\Delta_d(b)\rangle$ über rechtwinklig benachbarte Bindungen):
$$4\;\ge\;\frac{\langle A\rangle_0}{P}\;\ge\;4-\frac{\langle B\rangle_{\rm gleich}}{P}\;\ge\;4-\frac{20\,(P-1)}{2N-23(P-1)}
\;\xrightarrow{N\to\infty}\;4-\frac{20\,\rho_b}{1-23\rho_b}.$$
Bei 7/8-Füllung ($\rho_b=1/32$) ist die rechte Seite $4-2{,}22=1{,}78>0$, unabhängig von der Gittergröße. Die Schranke ist
nichttrivial für $\rho_b<1/28$.

*Beweis.*
1. *Energie.* In der d-Eichung ist $H_A=\epsilon_0P-t_cA$, also $\langle A\rangle_0=(\epsilon_0P-E_0)/t_c$. Mit der oberen Schranke aus §8,
   $E_0\le(\epsilon_0-4t_c)P+t_c\langle B\rangle_{\rm gleich}$ (Gleichverteilung als Versuchszustand), folgt die mittlere Ungleichung.
   Die linke folgt aus $\langle A\rangle_0\le\lambda_{\max}(A)\le\max_D\mathrm{Deg}(D)\le4P$.
2. *Blockierte Schritte.* Ein Eckschritt $b\to b'$ ist blockiert, wenn ein anderes Paar auf einer Bindung der Menge
   $Z(b\to b')=\mathrm{Konflikt}(b')\setminus(\mathrm{Konflikt}(b)\cup\{b\})$ sitzt. Abzählung: $|Z|=5$ für jeden der vier Eckschritte,
   $|\mathrm{Konflikt}(b)|=22$. Mit der Vereinigungsschranke
   $\langle B\rangle\le\sum_b P(b\in D)\sum_{4\ \text{Schritte}}\sum_{c\in Z}P(c\in D\mid b\in D)$.
3. *Umsetz-Argument.* Sei $\mathcal C_b$ die Menge der Konfigurationen mit einem Paar auf $b$ und $n_c$ die Zahl derer, die zusätzlich
   $c$ enthalten. Nimmt man aus einer solchen Konfiguration das Paar auf $c$ heraus, hat es mindestens
   $F=2N-23(P-1)$ erlaubte Plätze (jedes der übrigen $P-1$ Paare sperrt höchstens 23 Bindungen). Jede Zielkonfiguration in
   $\mathcal C_b$ entsteht so aus höchstens $P-1$ Ausgangskonfigurationen (welches Paar wurde bewegt). Also
   $n_c\,F\le(P-1)\,|\mathcal C_b|$, d.h. $P(c\in D\mid b\in D)\le(P-1)/F$.
4. Zusammen $\langle B\rangle/P\le4\cdot5\cdot(P-1)/F$. □

**Vergleich mit der exakten Diagonalisierung (8×8, Einheiten $t_c$, Werte aus §8):**

| Paare | $\langle A\rangle_0/P$ exakt | Schranke mit $\langle B\rangle$ exakt | Schranke aus der Zählung |
|---|---|---|---|
| 2 | 3,906 | 3,810 | 3,810 (hier exakt: das zweite Paar ist gleichverteilt auf 105 Plätze) |
| 3 | 3,782 | 3,599 | 3,512 |
| 4 | 3,646 | 3,367 | 2,983 |

**Einordnung.**
- Das ist ein echter Satz über den Grundzustand von Stufe A, gleichmäßig in der Gittergröße: Die kurzreichweitige
  d-Paarkohärenz ist bei 7/8-Füllung mindestens 1,78 von höchstens 4 pro Paar. Er braucht nur die RK-Identität und eine Zählung.
- Er sagt nichts über große Abstände. ODLRO verlangt, diese Kohärenz auf beliebige Abstände zu übertragen; das ist der offene Schritt.
- Für Stufe B (mit Spindynamik) überträgt sich das nicht direkt: Ein Versuchszustand mit guter Paarbewegung muss auch die
  Spinenergie gut treffen, und deren Fehler wächst mit $N$, die kinetische Energie der Paare nur mit $P$.

## 10. Satz: Paar-ODLRO am RK-Punkt

**Rahmen** wie in §8 und §9: Torus mit $2N$ Bindungen, $\mathcal C$ die berührungsfreien Konfigurationen mit $P$ Paaren,
$\rho_b=P/2N$, $X(b)=\{b\}\cup\mathrm{Konflikt}(b)$ mit $|X(b)|=23$. In der d-Eichung sei $T_{b\leftarrow b'}$ das Umsetzen eines
Paares von $b'$ nach $b$ im Modellraum: $T_{b\leftarrow b'}|D\rangle=|D\setminus\{b'\}\cup\{b\}\rangle$, falls $b'\in D$ und das Ergebnis in $\mathcal C$
liegt (für $b=b'$ also $|D\rangle$), sonst $0$. Die Paardichtematrix ist $\rho_1(b,b')=\langle T_{b\leftarrow b'}\rangle$. In der physikalischen
Basis trägt sie den Faktor $f(b)f(b')$, ist also die d-Paarkorrelation aus §5. Die Eichung ist diagonal-unitär, $\lambda_{\max}(\rho_1)$
ist eichinvariant. ODLRO im Sinn von Penrose-Onsager und Yang heißt: $\lambda_{\max}(\rho_1)\ge n_0P$ mit $n_0>0$ unabhängig von $N$.

**Satz.** Sei $\psi_{RK}=|\mathcal C|^{-1/2}\sum_{D\in\mathcal C}|D\rangle$ (d-Eichung), nach §8 ein Grundzustand von $H_{RK}=H_A-t_cB$, und
$u=(2N)^{-1/2}(1,\dots,1)$ die gleichförmige Mode (physikalisch die d-Welle bei $k=0$). Dann gilt für die Besetzung dieser Mode
$$N_0=\langle u|\rho_1|u\rangle\;\ge\;P\Big(1-\frac{23\,(P-1)}{2N}\Big),\qquad\text{also}\qquad
n_0=\frac{\lambda_{\max}(\rho_1)}{P}\;\ge\;1-\frac{23\,(P-1)}{2N}\;\xrightarrow{N\to\infty}\;1-23\rho_b .$$
Für $\rho_b<1/23$, also Lochdotierung $x=4\rho_b<17\,\%$, hat $\psi_{RK}$ Paar-ODLRO in der d-Welle bei $k=0$, gleichmäßig in der
Gittergröße. Bei 7/8-Füllung ($\rho_b=1/32$) ist $n_0\ge1-23/32=0{,}28$.

*Beweis.*
1. *Abzählen.* Alle Amplituden von $\psi_{RK}$ sind $|\mathcal C|^{-1/2}$. Also ist
   $\sum_{b,b'}\rho_1(b,b')=|\mathcal C|^{-1}\cdot\#\{(D,b',b):D\in\mathcal C,\ b'\in D,\ D\setminus\{b'\}\cup\{b\}\in\mathcal C\}
   =|\mathcal C|^{-1}\sum_{D\in\mathcal C}\sum_{p\in D}f(D\setminus\{p\})$, wobei $f(E)=\#\{b:E\cup\{b\}\in\mathcal C\}=2N-\big|\bigcup_{q\in E}X(q)\big|$
   die Zahl der Plätze ist, auf die das herausgenommene Paar zurück darf (der alte eingeschlossen).
2. *Freie Plätze.* $\big|\bigcup_{q\in E}X(q)\big|\le23\,|E|=23(P-1)$, also $f\ge2N-23(P-1)$ für jede Konfiguration.
3. Mit $\sum_D\sum_{p\in D}1=P|\mathcal C|$ folgt $N_0=\frac1{2N}\sum_{b,b'}\rho_1(b,b')\ge\frac{P\,(2N-23(P-1))}{2N}$, und
   $\lambda_{\max}\ge\langle u|\rho_1|u\rangle$. □

Der Beweis braucht keine Translationssymmetrie, nur $|X(b)|\le23$. Er gilt für die Gleichverteilung über *ganz* $\mathcal C$
(einschließlich eingefrorener Säulen): $T_{b\leftarrow b'}$ verbindet auch verschiedene Zusammenhangskomponenten, deshalb ist
die Gleichverteilung über nur eine Komponente nicht direkt abgedeckt. Die eingefrorenen Konfigurationen haben verschwindendes
Gewicht (8×8, 4 Paare: 32 von 3 075 264).

**Zusatz (punktweise).** $\rho_1(r,0)/\rho_b=P\big(X(r)\cap(D\setminus\{0\})=\emptyset\mid0\in D\big)\ge1-23(P-1)/F$ mit $F=2N-23(P-1)$
(Vereinigungsschranke und §9 Schritt 3), gleichmäßig in $r$. Im Grenzfall $1-23\rho_b/(1-23\rho_b)$; das ist nur für
$\rho_b<1/46$ ($x<8{,}7\,\%$) nichttrivial. Bei 7/8-Füllung trägt nur die gemittelte Form des Satzes.

**Prüfung durch vollständige Aufzählung** ([check_rk_odlro.py](check_rk_odlro.py), 8×8):

| Paare | $\rho_b$ | $n_0$ RK exakt | Schranke $1-23(P-1)/2N$ | $\min f$ / $F$ | $\rho_1(r,0)/\rho_b$, $r=(L/2,L/2)$ | punktweise Schranke | $n_0$ Stufe A (ED) |
|---|---|---|---|---|---|---|---|
| 2 | 1/64 | 0,8203 | 0,8203 | 105 / 105 | 0,7810 | 0,7810 | 0,75 |
| 3 | 3/128 | 0,6573 | 0,6406 | 82 / 82 | 0,5971 | 0,4390 | 0,56 |
| 4 | 1/32 | 0,5123 | 0,4609 | 59 / 59 | 0,4419 | $<0$ | 0,36 |

Die Schranke für die freien Plätze wird in allen drei Fällen angenommen ($\min f=F$). Sie lässt sich also ohne Information
über die *typische* Lage der Paare nicht verbessern; bei zwei Paaren ist der Satz exakt.

**Einordnung.**
- **Bewiesen:** Ein Modell aus der Familie von Stufe A hat in einem Grundzustand Paar-ODLRO in der d-Welle, gleichmäßig in
  der Gittergröße und bei 7/8-Füllung. Dieses Modell ist $H_{RK}=H_A-t_cB$, also Stufe A plus eine Anziehung $t_c$ für jeden
  blockierten Eckschritt; die wirkt zwischen Paaren, die sich nahe kommen, ohne sich zu berühren. Die Arbeit steckt in der
  RK-Identität (§8), der Rest ist eine Zeile Zählung.
- **Das ist der leichte Fall.** Am RK-Punkt ist der Grundzustand eine klassische Gleichverteilung; Kohärenz heißt dann nur,
  dass ein Paar umsetzbar ist, und das ist bei kleiner Dichte automatisch. Für bosonische RK-Zustände ist das vermutlich
  bekannt (nicht geprüft).
- **Für $H_A$ folgt nichts.** Auf 8×8 mit 4 Paaren liegt $n_0$ von Stufe A (0,36) sogar unter der RK-Schranke (0,46). Die
  Anziehung $t_cB$ erhöht die Kohärenz, und $H_A$ ist vom RK-Punkt um die Abstoßung $+t_cB$ entfernt.
- **Offen:** ODLRO entlang $H(\lambda)=H_{RK}+\lambda\,t_cB$ für $\lambda\in(0,1]$. Der Laplace-Operator $\Lambda$ auf dem
  Konfigurationsgraphen hat keine Lücke gleichmäßig in $N$ (Paarbewegung ist diffusiv), deshalb trägt keine Störungstheorie. Für
  $\lambda=1$ liefert der Weltlinien-Wurm ein Kosterlitz-Thouless-Suprafluid mit $T_{KT}\approx0{,}07\,t_c$
  ([weltlinien/README.md](weltlinien/README.md)). Das passt zu ODLRO bei $T=0$, ist aber kein Beweis.
- **Lean:** Der Kern ist endliche Kombinatorik (Schritt 1–3). Das ist ein guter erster Kandidat, sobald formalisiert wird.

## 11. Satz: Obere Schranke für die Phasensteifigkeit

**Rahmen.** Verdrillung $\varphi$ in $x$-Richtung: Jeder Eckschritt verschiebt die Paarmitte um $\Delta x=\pm\tfrac12$ und erhält die Phase
$e^{i\varphi\Delta x/L}$, also $H(\varphi)=\epsilon_0P-t_cA(\varphi)$ mit $A(\varphi)=\sum_{D\to D'}e^{i\varphi\Delta x/L}|D'\rangle\langle D|$ (d-Eichung, Paar als Boson
der Ladung 1). $F(\varphi)=-T\ln\mathrm{Tr}\,e^{-\beta H(\varphi)}$, kanonisch oder großkanonisch; Steifigkeit $\rho_s=\partial^2_\varphi F|_{\varphi=0}$, also
$F(\varphi)-F(0)=\tfrac12\rho_s\varphi^2+O(\varphi^4)$. Bei $T=0$ entsprechend mit $E_0(\varphi)$.

**Satz.** Für jedes $T\ge0$, jede Gittergröße und jede Paarzahl gilt
$$0\;\le\;\rho_s\;\le\;\frac{t_c\,\langle A\rangle}{4L^2}\;\le\;t_c\,\frac{P}{N}\;=\;t_c\,\frac x2 ,$$
bei 7/8-Füllung also $\rho_s\le0{,}0625\,t_c$. In Weltlinien-Größen ($\rho_s=T\langle W_x^2\rangle$ nach Pollock-Ceperley,
$t_c\langle A\rangle=T\langle K\rangle$ mit der Kinkzahl $K$) heißt das
$$\langle W_x^2\rangle\;\le\;\frac{\langle K\rangle}{4L^2}.$$

*Beweis.*
1. *Obere Schranke.* Gibbs-Variationsprinzip: $F(\varphi)\le F(0)+\mathrm{Tr}\big[\rho_0\,(H(\varphi)-H(0))\big]$ mit $\rho_0=e^{-\beta H(0)}/Z$ (bei
   $T=0$: $E_0(\varphi)\le\langle\psi_0|H(\varphi)|\psi_0\rangle$). In der d-Eichung ist $\rho_0$ reell symmetrisch, und zu jedem Schritt $D\to D'$
   gehört der Rückschritt mit $-\Delta x$. Also
   $\mathrm{Tr}[\rho_0(H(\varphi)-H(0))]=t_c\sum_{D\to D'}\rho_0(D,D')\,\big(1-\cos\tfrac{\varphi\Delta x}L\big)=t_c\big(1-\cos\tfrac{\varphi}{2L}\big)\langle A\rangle$,
   weil *alle* Eckschritte $|\Delta x|=\tfrac12$ haben. Vergleich der $\varphi^2$-Terme gibt $\rho_s\le t_c\langle A\rangle/(4L^2)$.
2. $\langle A\rangle\le\lambda_{\max}(A)\le\max_D\mathrm{Deg}(D)\le4P$.
3. *Untere Schranke.* $H(0)$ ist stoquastisch; in der Pfadentwicklung von $e^{-\beta H(\varphi)}$ trägt jeder Pfad dasselbe positive Gewicht
   wie bei $\varphi=0$ mal eine Phase, also $Z(\varphi)\le Z(0)$ und $F(\varphi)\ge F(0)$. □

**Bemerkungen.**
- Die Differenz zur Schranke ist der paramagnetische Strom-Strom-Beitrag. Die Schranke ist erreicht, wenn er verschwindet
  (ein freies Teilchen bei $T=0$).
- Exakte Werte bei endlichem $T$ (vollständige Diagonalisierung, [weltlinien/exakt.py](weltlinien/exakt.py)): 6×6, 2 Paare,
  $\beta=12$: $\langle W_x^2\rangle=0{,}6133$ gegen Schranke $0{,}6229$ (98,5 %); 8×8, 2 Paare, $\beta=12{,}5$: $0{,}3400$ gegen $0{,}3807$ (89,3 %).
- **Bei $T=0$ ist die Schranke fast gesättigt** ([ed_steifigkeit.py](ed_steifigkeit.py): Grundzustand und paramagnetischer Abzug
  $2L^{-2}\langle K\psi_0|(H-E_0)^{-1}|K\psi_0\rangle$, gegen echte Verdrillung geprüft):

  | System | $E_0$ | Schranke $\langle A\rangle/4L^2$ | $\rho_s$ exakt | Verhältnis |
  |---|---|---|---|---|
  | 6×6, 2 Paare | −7,47625 | 0,051918 | 0,051879 | 0,9992 |
  | 8×8, 2 Paare | −7,81282 | 0,030519 | 0,030512 | 0,9998 |
  | 8×8, 3 Paare | −11,34630 | 0,044321 | 0,044284 | 0,9991 |
  | 8×8, 4 Paare (7/8) | −14,58520 | 0,056973 | 0,056878 | 0,9983 |

  Der Grundzustand trägt praktisch keinen paramagnetischen Strom: Die Steifigkeit ist die kinetische Energie der Paare, wie
  bei einem galileiinvarianten Suprafluid ($\rho_s=n/m$ bei $T=0$). Die Abzüge wachsen erst bei endlichem $T$ (thermisch
  angeregte Stromzustände).
- Die Steifigkeit der Elektronenladung ist $4\rho_s$, weil ein Paar die Ladung 2 trägt; für Kosterlitz-Thouless zählt die Phase des
  Paarfeldes, also $\rho_s$ wie oben.
- Die Schranke gilt unverändert für $H_{RK}$ und $H(\lambda)$ aus §10 (Diagonalterme fallen heraus) und großkanonisch.
- **Folgerung für $T_{KT}$ (nicht rigoros):** Mit der Kosterlitz-Thouless-Beziehung $T_{KT}=\tfrac\pi2\rho_s(T_{KT}^-)$ (Renormierungsgruppe)
  folgt $T_{KT}\le\tfrac\pi8t_c\langle A\rangle_{T_{KT}}/L^2\le\tfrac\pi4\,x\,t_c$, bei 7/8-Füllung $\le0{,}098\,t_c$; mit dem gemessenen
  $\langle A\rangle/4P\approx0{,}91$ etwa $0{,}089\,t_c$. Der Wurm liefert $T_{KT}\approx0{,}07\,t_c$, also etwa 80 % davon.
- **Als Test der Numerik:** Die Ungleichung $\langle W_x^2\rangle\le\langle K\rangle/4L^2$ muss jeder korrekte Weltlinien-Lauf erfüllen, Lauf für
  Lauf. Siehe [weltlinien/README.md](weltlinien/README.md) für den Befund bei den Produktionsläufen.

## 12. Satz: Keine lokalen Einfrierungen; Irreduzibilität auf $\mathbb Z^2$

**Bezeichnungen.** Für eine Diagonalrichtung $s\in\{(\pm1,\pm1)\}$ sei $\sigma(b)=s\cdot x_b$ die Koordinate der Bindungsmitte längs $s$.
Jede Bindung hat genau einen Eckschritt mit Verschiebung $\parallel s$; er erhöht $\sigma$ um 1 (§3: die vier Eckschritte zeigen in
die vier Diagonalrichtungen). Er ist blockiert, wenn ein anderes Paar in
$Z(b\to b')=\mathrm{Konflikt}(b')\setminus(\mathrm{Konflikt}(b)\cup\{b\})$ sitzt (§9).

**Lemma (vorderstes Paar).** Alle fünf Bindungen in $Z$ des Eckschritts in Richtung $s$ haben $\sigma(c)-\sigma(b)\in\{2,3\}$.

*Beweis.* Beispiel $b=\{(0,0),(1,0)\}$, $s=(1,1)$: Drehpunkt $(1,0)$, $w=(1,1)$, $b'=\{(1,0),(1,1)\}$. Die Zone von $b'$ (beide Plätze und ihre
Nachbarn) enthält gegenüber der Zone von $b$ genau die zwei neuen Plätze $w+e_x=(2,1)$ und $w+e_y=(1,2)$. Blockierend sind die
Bindungen an diesen Plätzen, deren anderer Platz nicht in der Zone von $b$ liegt: $\{(2,1),(3,1)\}$, $\{(2,1),(2,2)\}$, $\{(1,2),(0,2)\}$,
$\{(1,2),(2,2)\}$, $\{(1,2),(1,3)\}$ mit $\sigma=3{,}5;\,3{,}5;\,2{,}5;\,3{,}5;\,3{,}5$ gegen $\sigma(b)=0{,}5$. Allgemein: Die neuen Zonenplätze liegen
auf der Platzhöhe $\sigma(b)+\tfrac52$, jede Bindung an ihnen hat also Mittenhöhe $\ge\sigma(b)+2$. Die übrigen Fälle folgen durch Spiegelung
und Drehung (numerisch für beide Orientierungen und alle vier Richtungen bestätigt). □

**Folgerung.** Ein Paar mit maximalem $\sigma$ kann immer in Richtung $s$ ziehen, und danach ist es *eindeutig* vorderstes Paar,
kann also beliebig weiter ziehen.

**Satz (Irreduzibilität auf $\mathbb Z^2$).** Für jede Paarzahl $P$ ist der Graph der berührungsfreien $P$-Paar-Konfigurationen auf
$\mathbb Z^2$ unter Eckschritten zusammenhängend.

*Beweis.* Wähle $s=(1,1)$, $G=4$ und eine Höhe $S$ über allen vorkommenden $\sigma$. Normalform $\mathcal N_S$: Paare auf den Höhen
$S,S-G,\dots,S-(P-1)G$, jedes mit Querkoordinate $\tau=s^\perp\cdot x=\tfrac12$.
1. *Heben.* Das vorderste Paar zieht nach dem Lemma bis zur Höhe $S$. Dann das vorderste der übrigen bis $S-G$: Seine blockierenden
   Bindungen liegen auf Höhen $\sigma+2,\sigma+3$; das schon gehobene Paar ist mindestens $G=4$ darüber, alle anderen liegen nicht höher.
   Induktiv stehen alle Paare auf den Höhen von $\mathcal N_S$.
2. *Querverschieben.* Die Eckschritte mit $s\cdot\Delta x=0$ ändern $\tau$ um $\pm1$ und lassen $\sigma$ fest; ihre blockierenden Bindungen liegen
   (gleiche Rechnung, gedreht) höchstens 2 in $\sigma$ entfernt. Bei Höhenabständen $4$ blockiert also kein anderes Paar; jedes Paar
   läuft einzeln auf $\tau=\tfrac12$.
3. Zwei Konfigurationen erreichen mit gemeinsamem $S$ dieselbe Normalform; Eckschritte sind umkehrbar. □

**Satz (Torus: Blockaden wickeln sich um).** Auf dem $L\times L$-Torus sei $D$ eine Konfiguration, in der *kein* Paar in Richtung $s$
ziehen kann. Dann gibt es zu jedem Paar $p$ ein Paar $q$ mit $\sigma(q)-\sigma(p)\in\{2,3\}\pmod L$ und Querabstand $\le2$; die
Kette $p\to q\to\dots$ läuft also um den Torus und enthält mindestens $L/3$ Paare.

*Beweis.* Unmittelbar aus dem Lemma (die Zonen sind lokal, für $L\ge8$ wickeln sie sich nicht). □

**Einordnung.**
- Auf dem unendlichen Gitter gibt es keine eingefrorenen oder getrennten Sektoren. Alle Hindernisse für die Ergodizität auf
  dem Torus sind topologisch: Ketten, die sich um den Torus schließen, wie die Säulen auf 8×8 (§5).
- **Offen:** Irreduzibilität der "großen Komponente" auf dem Torus bei fester Dichte und damit die Eindeutigkeit des
  Grundzustands für jedes $L$. Das Heben braucht freien Platz, den der Torus bei fester Dichte nicht bietet.

## 13. Satz: Kein Paar-ODLRO bei $T>0$ (nach Koma und Tasaki)

**Satz.** Für $H_A$ (ebenso $H_{RK}$, $H(\lambda)$, kanonisch oder großkanonisch) gilt bei jeder Temperatur $T>0$ für große $|r|$,
gleichmäßig in der Gittergröße,
$$|\rho_1(r,0)|=|\langle T_{r\leftarrow0}\rangle|\;\le\;C\,|r|^{-\eta(T)},\qquad\eta(T)=\frac{T}{2\pi t_c}\big(1+O(T/t_c)\big).$$
Insbesondere ist $\lambda_{\max}(\rho_1)\le\sum_r|\rho_1(r,0)|=O(L^{2-\eta})=o(P)$: kein ODLRO bei $T>0$.

*Beweis* (Methode von Koma und Tasaki [KT], dort für Hubbard-Modelle; sie braucht nur die globale U(1)-Symmetrie und
Sprünge endlicher Reichweite, keine Vorzeichenfreiheit).
1. *Imaginäre Eichdrehung.* $G=\prod_m e^{-\varphi_mn_m}$ mit reeller Funktion $\varphi$ auf dem Mittelgitter. $G$ ist diagonal, erhält also den
   Modellraum. Es gilt $\mathrm{Tr}[T_{r\leftarrow0}e^{-\beta H}]=\mathrm{Tr}[GT_{r\leftarrow0}G^{-1}e^{-\beta GHG^{-1}}]$ mit
   $GT_{r\leftarrow0}G^{-1}=e^{-(\varphi_r-\varphi_0)}T_{r\leftarrow0}$ und $GHG^{-1}=H+U+iP$, wobei
   $U=-t_c\sum_e(\cosh\Delta_e-1)\,T_e$ und $P$ hermitesch sind ($e$ = Kante des Mittelgitters, $\Delta_e$ = Differenz von $\varphi$ längs $e$,
   $T_e$ = Umsetzen über $e$ in beide Richtungen, $\|T_e\|\le1$). Diagonalterme bleiben unverändert.
2. *Spurungleichungen* (Schwarz, Golden-Symanzik-Thompson, wie in [KT] Gl. (14)–(16)):
   $|\mathrm{Tr}[GT_{r\leftarrow0}G^{-1}e^{-\beta GHG^{-1}}]|\le e^{-(\varphi_r-\varphi_0)}\,\mathrm{Tr}\,e^{-\beta(H+U)}\le e^{-(\varphi_r-\varphi_0)}\,e^{\beta\|U\|}\,Z$.
3. *Wahl von $\varphi$.* $-\Delta\varphi=q(\delta_r-\delta_0)$ auf dem Mittelgitter (Kanten = Eckschritte). Dann ist $\varphi_r-\varphi_0=qR(0,r)$ mit dem
   Widerstand $R(0,r)=\tfrac1\pi\ln|r|+O(1)$, und $\sum_e\Delta_e^2=q^2R$. Mit $\cosh x-1\le g\,x^2$ ($g\to\tfrac12$ für kleine $q$) wird
   $\|U\|\le t_c\,g\,q^2R$.
4. Zusammen $|\rho_1(r,0)|\le\exp\{-R(0,r)\,[q-\beta t_cg\,q^2]\}$; das Optimum $q=T/t_c$ gibt den Exponenten $R\,T/(2t_c)$. □

**Einordnung.**
- Das gilt auch für Stufe B und B+ (Spinaustausch vertauscht mit $G$, alle Paarprozesse haben endliche Reichweite); Vorzeichen
  spielen keine Rolle. Für das volle t-J-Modell haben Koma und Tasaki es selbst gezeigt ([KT], Fußnote 10).
- Die Schranke ist schwach: Bei $T_{KT}\approx0{,}07\,t_c$ ist $\eta\approx0{,}011$, der wahre Wert ist $\tfrac14$. Spinwellen geben
  $\eta=T/(2\pi\rho_s)$; der Satz hat $t_c$ an der Stelle von $\rho_s\approx0{,}056\,t_c$, weil er $\|T_e\|\le1$ auf jeder Kante ansetzt, auch
  dort, wo kein Paar ist.
- Damit ist die Lage sauber: Bei $T>0$ höchstens algebraische Ordnung (Kosterlitz-Thouless), ODLRO höchstens bei $T=0$. Die
  Wurm-Rechnung misst deshalb $T_{KT}$, nicht eine Kondensat-Temperatur.

[KT] T. Koma, H. Tasaki, *Decay of superconducting and magnetic correlations in one- and two-dimensional Hubbard models*,
Phys. Rev. Lett. 68, 3248 (1992), arXiv:cond-mat/9709068 (gelesen 2026-10-20).

## 14. Satz: Steifigkeit als Leitwert des Konfigurationsgraphen

**Rahmen.** $H=V-t_cA$ auf einer Zusammenhangskomponente $\mathcal C_0$ ($V$ beliebig diagonal, also $H_A$, $H_{RK}$, $H(\lambda)$),
Grundzustand $\psi_0>0$ auf $\mathcal C_0$ (Perron-Frobenius), nicht entartet. Verdrillung wie in §11, jeder Eckschritt hat
$\Delta x=\pm\tfrac12$. Summen $\sum_{D\to D'}$ laufen über geordnete Eckschritte, $c(D,D')=\psi_0(D)\psi_0(D')$.

**Satz (Leitwertdarstellung).**
$$\rho_s=\frac{t_c}{L^2}\;\min_f\sum_{D\to D'}\psi_0(D)\psi_0(D')\,\big(\Delta x(D\to D')+f(D')-f(D)\big)^2 .$$
Die Steifigkeit ist der effektive Leitwert des Konfigurationsgraphen mit Kantenleitwerten $t_c\psi_0\psi_0$ in "Windungsrichtung".

*Beweis.* Zweite Ordnung (§11, [ed_steifigkeit.py](ed_steifigkeit.py)):
$\rho_s=\frac{t_c\langle A\rangle}{4L^2}-\frac{2t_c^2}{L^2}\langle K\psi_0|(H-E_0)^{-1}|K\psi_0\rangle$ mit $K=\sum_{D\to D'}\Delta x\,|D'\rangle\langle D|$. Für $u=\psi_0f$ gilt die
Grundzustandsidentität $\langle u|H-E_0|u\rangle=\tfrac{t_c}2\sum_{D\to D'}c\,(f(D')-f(D))^2$ (aus $H\psi_0=E_0\psi_0$) und
$\sum_{D\to D'}c\,\Delta x\,(f(D')-f(D))=2\langle u|K\psi_0\rangle$ (Antisymmetrie von $\Delta x$). Also ist die Summe im Satz
$Q(f)=\tfrac14\langle A\rangle+4\langle u|K\psi_0\rangle+\tfrac2{t_c}\langle u|H-E_0|u\rangle$, mit Minimum bei $u=-t_c(H-E_0)^{-1}K\psi_0$ und Wert
$\tfrac14\langle A\rangle-2t_c\langle K\psi_0|(H-E_0)^{-1}|K\psi_0\rangle$. □

Numerisch bestätigt (direkte Minimierung über $f$, [ed_steifigkeit_rk.py](ed_steifigkeit_rk.py)): 0,051879 / 0,030512 / 0,044284 für
6×6 (2 Paare), 8×8 (2 und 3 Paare), gleich den Werten aus §11.

**Klassische Lesart.** Die Doob-Transformation macht aus $H-E_0$ den Generator eines reversiblen Markov-Prozesses auf $\mathcal C_0$
(Raten $t_c\psi_0(D')/\psi_0(D)$, stationäres Maß $\psi_0^2$; das ist der Prozess der Diffusions-Monte-Carlo-Rechnung mit Führung $\psi_0$).
Dann ist $\rho_sL^2$ die Varianzrate der Gesamtverschiebung aller Paare, also eine kollektive Diffusionskonstante
(Kipnis-Varadhan).

**Folgerungen.**
1. *Obere Schranke:* $f=0$ gibt §11.
2. *Untere Schranke über Flüsse (Thomson):* Für jeden antisymmetrischen, quellenfreien Fluss $\theta$ ($\sum_{D'}\theta(D\to D')=0$ für alle
   $D$) ist $\rho_s\ge\frac{t_c}{L^2}\big(\sum\theta\Delta x\big)^2/\sum\theta^2/c$ (Cauchy-Schwarz; $\sum\theta\,(f(D')-f(D))=0$). Gleichheit für den
   optimalen Strom $\theta^*=c(\Delta x+\nabla f^*)$.
3. *Drift-Form:* Ist $F$ ein antisymmetrischer Fluss mit denselben Quellen wie $c\,\Delta x$, also
   $\sum_{D'}F(D\to D')=\sum_{D'}c\,\Delta x(D\to D')$ für alle $D$, dann
   $$\rho_s\;\ge\;\frac{t_c}{L^2}\Big(\tfrac14\langle A\rangle-\sum_{D\to D'}F^2/c\Big)$$
   (quadratische Ergänzung $c(\nabla f)^2+2F\nabla f\ge-F^2/c$). Die Quellen von $c\Delta x$ sind die *Drift*: wie unausgeglichen die
   erlaubten Schritte einer Konfiguration in $x$ sind. Ist die Drift überall null (Gradientensystem), dann ist $F=0$ erlaubt und
   §11 ist exakt.

## 15. Steifigkeit am RK-Punkt (Programm)

Am RK-Punkt ist $\psi_0$ die Gleichverteilung, $c=1/|\mathcal C|$, und die Quellen sind $d(D)/|\mathcal C|$ mit der Drift
$d(D)=\sum_{\text{erlaubte Schritte}}\Delta x$. Mit einem Fluss $\tilde F$, $\sum_{D'}\tilde F(D\to D')=d(D)$, gibt §14 Folgerung 3
$$\rho_s^{RK}\;\ge\;\frac{t_c}{L^2}\Big(\tfrac14\langle A\rangle_{\rm gleich}-\big\langle\textstyle\sum_{D'}\tilde F(D\to D')^2\big\rangle_{\rm gleich}\Big).$$
Der erste Term ist nach §9 mindestens $P\,(1-5(P-1)/F)$. Gebraucht wird ein Fluss, der die Drift mit kleiner Energie abführt.

**Exakt (8×8, 6×6, [ed_steifigkeit_rk.py](ed_steifigkeit_rk.py)):**

| System | Drift $\ne0$ | $\langle A\rangle/4L^2$ | $\rho_s^{RK}$ | Verhältnis |
|---|---|---|---|---|
| 6×6, 2 Paare | 16 % | 0,049887 | 0,049563 | 0,9935 |
| 8×8, 2 Paare | 7,6 % | 0,029762 | 0,029677 | 0,9971 |
| 8×8, 3 Paare | 21 % | 0,042180 | 0,041901 | 0,9934 |

Der paramagnetische Abzug ist klein und wächst etwa wie die Zahl der Paarkontakte, $\propto(P-1)/2N$.

**Lemma (Struktur der Drift, zwei Paare; vollständige Aufzählung).** Für ein waagerechtes Paar $p$ und ein zweites Paar $q$ ist die
Drift nur in 8 Relativlagen ungleich null, alle mit $q$ senkrecht: $r=(\mp2{,}5,\mp0{,}5)$, $(\mp2{,}5,\pm0{,}5)$ (Drift $\mp\tfrac12$, ein
Schritt von $q$ zu $p$ hin blockiert) und $r=(\mp0{,}5,\mp2{,}5)$, $(\mp0{,}5,\pm2{,}5)$ (Drift $\pm\tfrac12$, ein Schritt von $p$ blockiert).
Jeweils genau *ein* Schritt ist einseitig blockiert, die Blockade ist dort nicht gegenseitig. Die 8 Lagen bilden vier Dipole
$(+\tfrac12,-\tfrac12)$, deren Enden sich um $(2,\pm2)$ unterscheiden; ein Weg von 4 Eckschritten von $q$ verbindet sie, ohne $p$ zu
berühren (von Hand geprüft für den Dipol $r=(-0{,}5,-2{,}5)\to(-2{,}5,-0{,}5)$).

**Beweisplan für kleine Dichte.**
1. Zwei-Körper-Fluss: Je Dipol $\tfrac12$ Einheit längs des 4-Schritt-Wegs, Energie $\le4\cdot2\cdot\tfrac14=2$ pro Dipol. Das führt die
   Zwei-Körper-Drift exakt ab.
2. Viel-Körper-Korrekturen: (a) Ein Schritt kann von zwei Paaren zugleich blockiert sein (zwei berührungsfreie Paare passen in
   dieselbe Zone $Z$), dann zählt die Zwei-Körper-Summe doppelt. (b) Ein drittes Paar kann den 4-Schritt-Weg versperren. Beides
   verlangt drei Paare in einem Gebiet fester Größe, Wahrscheinlichkeit $O(\rho_b^2)$ je Paar. Für diese Fälle braucht man Ersatzwege
   (anderer Dipolweg, Bewegung von $p$ statt $q$, Umwege), deren Länge im Mittel beschränkt ist.
3. Ergebnis wäre $\rho_s^{RK}\ge t_c\frac PN\big(1-C_1\rho_b-C_2\rho_b^2\big)$ mit expliziten Konstanten, gleichmäßig in $L$.

**Offen:** Schritt 2 vollständig, also eine Konstruktion, die *jede* Konfiguration abdeckt und deren mittlere Energie beschränkt
bleibt. Das ist die bekannte Schwierigkeit nicht-gradienter Gittergase (Varadhan), hier aber in einer elementaren, abzählbaren
Form. Ob das bis 7/8-Füllung trägt, ist offen; die Zahlen (Abzug unter 1 %) sprechen dafür, dass die Konstanten klein sind.

**Expliziter Fluss (2026-10-21, [fluss_rk.py](fluss_rk.py)).** Zwei-Körper-Fluss wie oben: Aus jeder Quell-Lage läuft $q$ in vier
Eckschritten $(-\tfrac12,\pm\tfrac12)$ zur Senken-Lage, Fluss $\tfrac12$. Bei mehr Paaren entfallen Wege, die ein drittes Paar versperrt; der Rest
$R=d-\mathrm{div}F_2$ wird hier noch mit dem energieminimalen Fluss abgeführt (numerisch, keine explizite Konstruktion). Einheiten
$\rho_s^{RK}L^2/t_c$:

| System | Dipol-Quellen | versperrt | $R\ne0$ | Energie $F_2$ | Energie gesamt | Schranke | exakt | $\tfrac14\langle A\rangle$ |
|---|---|---|---|---|---|---|---|---|
| 6×6, 2 Paare | 144 | 0 | 0 | 0,1633 | 0,1633 | 1,6327 | 1,7843 | 1,7959 |
| 8×8, 2 Paare | 256 | 0 | 0 | 0,0762 | 0,0762 | 1,8286 | 1,8993 | 1,9048 |
| 10×10, 2 Paare | 400 | 0 | 0 | 0,0452 | 0,0452 | 1,8983 | 1,9403 | 1,9435 |
| 8×8, 3 Paare | 22 272 | 18 % | 4,2 % | 0,1985 | 0,2019 | 2,4976 | 2,6817 | 2,6995 |
| 10×10, 3 Paare | 63 600 | 10 % | 1,3 % | 0,1267 | 0,1277 | 2,6971 | 2,8146 | 2,8249 |
| 8×8, 4 Paare (7/8) | 752 640 | 36 % | 15 % | 0,3312 | 0,3452 | 3,0219 | 3,3279 | 3,3671 |

**Satz (zwei Paare).** Für $P=2$ sind die Quellen des Zwei-Körper-Flusses exakt die Drift (geprüft auf 6×6, 8×8, 10×10; die Lagen
und Wege sind lokal, also gilt das für jedes $L\ge6$). Damit ist $\rho_s^{RK}L^2/t_c\ge\tfrac14\langle A\rangle-(\text{Anteil der Konfigurationen mit
Drift})$ rigoros (jeder Weg trägt Energie $2\cdot4\cdot\tfrac14=2$ und verbindet zwei Konfigurationen mit Drift).

**Befund für mehr Paare.** Der Rest ist lokal (drei Paare dicht beieinander) und billig: 1–4 % der Fluss-Energie. Selbst bei
7/8-Füllung liegt die Schranke bei 91 % des exakten Werts. Der Abstand zum Optimum (Faktor 6–14 in der Energie) kommt daher, dass
der Fluss jeden Dipol über einen einzigen Weg führt; mehrere parallele Wege (etwa $p$ statt $q$ bewegen) halbieren die Energie je
Verdopplung.

**Was für einen vollständigen Beweis fehlt:** den Rest explizit abführen. Das ist eine endliche Fallanalyse der Drei-Paar-Lagen
(Ersatzwege, wenn der Dipolweg versperrt ist; doppelt blockierte Schritte), mit einem Rest, der vier Paare dicht beieinander
braucht, usw. Bei kleiner Dichte schließt diese Hierarchie (jede Stufe kostet einen Faktor $\rho_b$); bei 7/8-Füllung zeigen die
Zahlen, dass schon die zweite Stufe klein ist. Zusammen mit einer schärferen Abzählung als der Umsetz-Schranke aus §9 (die bei
7/8-Füllung zu grob ist) ergäbe das $\rho_s^{RK}\ge c\,t_cP/N$ gleichmäßig in $L$.

**Drei-Körper-Rest im Einzelnen (8×8, 3 Paare, [fluss_rk3.py](fluss_rk3.py)).**
- *Ketten:* Jede Senke hat zwei mögliche Quellen (q oder p zurückbewegen). Quellen und Senken bilden daher Ketten: das Dipolpaar
  $(p,q)$ um $\Delta=(-2,\pm2)$ verschoben, das dritte Paar $r$ fest. Weit weg von $r$ passen die q-Wege lückenlos aneinander. Ein
  Ersatzweg "p statt q" bei versperrtem Weg verschlimmert den Rest (Senken doppelt oder gar nicht bedient), weil die Zuordnung
  längs der Kette konsistent sein muss.
- *Unterbrochene Ketten:* 4096 verwaiste Quellen. Für 72 % liegt die verwaiste Senke auf derselben Kette hinter $r$, und der
  kürzeste Umweg um $r$ hat **in allen Fällen 12 Eckschritte** (Energie 6). Für 28 % findet die einfache Kettensuche keinen Partner
  (noch zu klären).
- *Doppelblockaden:* 640 Konfigurationen (0,34 %), bis auf Translation **18 Klassen**, Abweichung von der Dipolsumme $\pm\tfrac12$ oder $\pm1$.
- Nach den Umwegen Rest in 1,2 % statt 4,2 % der Konfigurationen. Schranke mit expliziten Umwegen 2,401 (mit numerischem Restfluss
  statt Umwegen 2,498; exakt 2,682): Die Umwege sind teuer, aber die Schranke bleibt deutlich positiv.

**Einschätzung.** Der Drei-Körper-Teil ist eine endliche, aber nicht kleine Fallanalyse: Kettenunterbrechungen (ein Umwegtyp
gefunden, ein Teil noch offen) und 18 Doppelblockade-Klassen. Am saubersten wäre ein computergestützter Beweis: alle lokalen
Drei-Paar-Lagen bis auf Translation auf $\mathbb Z^2$ aufzählen, für jede einen Fluss per Suche bauen und die Quellen prüfen; dann ein
Abzählargument, dass Vier-Paar-Reste um einen Faktor $\rho_b$ seltener sind.

**Drei-Körper-Tabelle auf $\mathbb Z^2$ (2026-10-21, [fluss_z2.py](fluss_z2.py), computergestützt).** Drei Paare auf $\mathbb Z^2$ bis auf
Translation (Quotientengraph; Flüsse darauf heben sich zu translationsinvarianten Flüssen). Für jede Konfiguration lokal: Drift $d$,
Quellen des Zwei-Körper-Flusses $F_2$ (nur freie Dipolwege), Rest $R=d-\mathrm{div}F_2$.

| Fenster (Durchmesser) | Konfigurationen | Klassen mit $R\ne0$ | $\sum R$ | Energie des Restflusses im Fenster |
|---|---|---|---|---|
| ≤ 6 | 12 482 | 122 | 0 | 10,505 |
| ≤ 7 | 25 006 | 122 | 0 | 10,476 |
| ≤ 8 | 44 758 | 122 | 0 | 10,469 |
| ≤ 9 | 73 970 | 122 | 0 | 10,467 |

- **Endlich:** genau 122 Klassen, Werte $\pm\tfrac12$ (je 60) und $\pm1$ (je eine), unabhängig vom Fenster.
- **Kompakt:** Durchmesser der Rest-Klassen 2 bis 4,5.
- **Neutral, aus Symmetrie:** $R$ ist ungerade unter der Spiegelung $x\to-x$ ($R(\mathcal R_xD)=-R(D)$, geprüft für alle Klassen), also
  $\sum R=0$. Die Drift ist ungerade; mit dem antisymmetrisierten Fluss $F_2'=\tfrac12(F_2-\mathcal R_xF_2)$ ist jeder Rest auf jeder
  Stufe ungerade, die Neutralität also eingebaut (und die Zwei-Körper-Energie halbiert sich, weil $-x$- und $+x$-Wege disjunkt
  sind). Für $F_2$ selbst ist der Rest schon ungerade.
- **Billig:** Der energieminimale Restfluss im Fenster hat Energie $\approx10{,}47$ (Summe über alle Klassen). Grob geschätzt trägt
  das relativ zum Diamagnet-Term $\sim\rho_b^2\cdot E_3/2\approx0{,}5\,\%$ bei 7/8-Füllung bei.

**Beweisaufbau für $\rho_s^{RK}\ge c\,t_cP/N$ bei kleiner Dichte.**
1. §14: Steifigkeit $\ge$ Diamagnet $-$ Energie eines Flusses mit Quellen gleich der Drift.
2. Zwei-Körper: exakter Dipolfluss (Lemma oben), Energie $\le1$ je Dipolzustand.
3. Stufe $k$: Der Rest ist auf zusammenhängenden $k$-Paar-Clustern getragen und ungerade, also neutral. Nach Satz 12
   (Irreduzibilität auf $\mathbb Z^2$) gibt es zu jedem endlichen neutralen Rest einen endlichen Fluss. Für $k=3$ explizit: 122
   Klassen, Fenster 6, Energie 10,5.
4. Abzählen: $k$-Cluster haben die Dichte $O(\rho_b^{k-1})$ je Paar.

**Offen:** (a) Die Fenster der Stufe-$k$-Flüsse beschränkt halten. Die Hebekonstruktion von Satz 12 bewegt Paare weit, das ließe die
Fenster mit $k$ wachsen und die Abzählung divergieren. Nötig sind lokale Reparaturen in festen Fenstern; gedrängte Cluster, für die
das nicht geht, müssen als seltene Ausnahme gezählt werden. (b) Kreuzterme zwischen den Stufen (über $2ab\le\epsilon a^2+b^2/\epsilon$
harmlos). (c) Für 7/8-Füllung eine schärfere Abzählung als §9.

**Vier-Paar-Stufe auf $\mathbb Z^2$ (2026-10-21, [fluss_z2_4.py](fluss_z2_4.py)).** $F_3$ = energieminimaler Fluss im Drei-Paar-Fenster,
gehoben auf vier Paare (nur die in $D$ erlaubten Züge), Zwei-Körper-Fluss symmetrisiert. Rest $R_4=d-\mathrm{div}F_2'-\mathrm{div}F_3$:

| $F_3$-Fenster | Energie $F_3$ | Vier-Paar-Fenster | Konfigurationen | $R_4\ne0$ | ungerade | Komponenten | Energie $F_4$ |
|---|---|---|---|---|---|---|---|
| ≤ 8 | 10,469 | ≤ 5 | 51 780 | 42 590 | ja | 1 | 32,05 |
| ≤ 5 | 10,658 | ≤ 6,5 | 433 898 | 101 378 | ja | 1 | 30,16 |

- Neutralität und Abführbarkeit tragen auch auf Stufe 4: $R_4$ ist exakt ungerade, der Fenstergraph zusammenhängend, $F_4$ existiert.
- Der Energiezuwachs je Stufe ist etwa ein Faktor 3; mit dem Dichtefaktor $\rho_b$ je Stufe sind die Beiträge ab Stufe 4 bei 7/8-Füllung
  im Promillebereich.
- **Aber:** $R_4$ ist nicht kompakt im Sinn der Stufe 3. Der energieminimale $F_3$ verteilt sich über das ganze Drei-Paar-Fenster, und
  ein viertes Paar in Reichweite (≈ 3) irgendeiner dieser Lagen erzeugt Rest. Der Träger von $R_k$ wächst so um die Reichweite je
  Stufe, die Fenster wachsen linear in $k$, und eine naive Clusterabzählung divergiert (Lage des nächsten Paares $\sim k^2$ Möglichkeiten).

**Folgerung für den Beweis.** Die Flüsse der Stufen $\ge3$ müssen *wegartig* und *nahe am Cluster* bleiben wie die Dipolwege: Rest-Knoten
paarweise über kurze Wege verbinden, deren Lagen höchstens $O(1)$ von den Paaren des Clusters abweichen. Dann braucht ein weiteres Paar
nur in fester Reichweite der Cluster-*Paare* zu liegen (Gittertier-Abzählung $C^k$), und die Reihe konvergiert für kleine $\rho_b$.
Gedrängte, lokal eingefrorene Cluster, für die das nicht geht, sind als seltene Ausnahme mit großem Fenster zu zählen. Das ist der
nächste technische Schritt; die Zahlen zeigen, dass er quantitativ unkritisch ist, aber für die Strenge nötig.

**Wegartige Flüsse: die Hierarchie bleibt lokal (2026-10-21, [fluss_z2_wege.py](fluss_z2_wege.py),
[fluss_z2_stufe4.py](fluss_z2_stufe4.py), [fluss_z2_stufe5.py](fluss_z2_stufe5.py)).** Statt des energieminimalen Flusses werden die
Rest-Einheiten ($\pm\tfrac12$) per Zuordnung minimaler Gesamtweglänge gepaart und über kürzeste Wege verbunden.

| Stufe | Rest-Klassen | Einheiten | Weglängen | Energie | Fluss trägt | Durchmesser Träger | Abstand zum nächsten Paar |
|---|---|---|---|---|---|---|---|
| 3 | 122 | 62 | 1–5 (meist 2) | 85 | 187 Lagen, Durchmesser ≤ 4,5 | ≤ 4,5 | |
| 4 | 900 | 485 | 1–6 | 954 | 1782 Lagen | ≤ 6,0 (Fenster 6,5 und 7,5 gleich) | ≤ 4 |
| 5 | 8314 | | | | | ≤ 9 (abklingend) | ≤ 4 |

- Alle Flüsse haben exakt die gewünschten Quellen ($|\mathrm{div}F_k-R_k|=0$); alle Einheiten der Stufen 3 und 4 finden Partner in höchstens
  5 bzw. 6 Schritten.
- **Kompakt:** Der Vier-Paar-Rest ändert sich nicht, wenn das Fenster von 6,5 auf 7,5 wächst (900 Klassen). Für Stufe 5: Bei einem
  fünften Paar im Abstand 6–9 ist $R_5=0$ in allen 20 000 Stichproben.
- **Clusterstruktur:** In jedem Rest-Träger hat jedes Paar einen Nachbarn im Abstand ≤ 4, auf allen Stufen. Das ist die Struktur, die
  eine Gittertier-Abzählung ($\le C^k$ Klassen) braucht.
- **Wachstum:** Klassen ×7–9, Energie ×11 je Stufe; mit dem Dichtefaktor $\rho_b\approx1/32$ je Stufe fallen die Beiträge bei 7/8-Füllung
  um etwa 0,3 je Stufe.
- Der wegartige $F_3$, $F_4$ ist nicht spiegelsymmetrisch gebaut, deshalb ist $R_5$ nicht mehr ungerade (die Summe ist trotzdem 0). Mit
  $F_k'=\tfrac12(F_k-\mathcal R_xF_k)$ bleibt die Neutralität auf jeder Stufe eingebaut.

**Stand des Beweises.** Numerisch ist die Hierarchie bis Stufe 5 lokal und konvergent. Für einen Beweis fehlt ein Lemma, das für
*jede* Stufe garantiert, dass die Rest-Einheiten innerhalb beschränkter Weglänge gepaart werden können (bis Stufe 4 reichen 6 Schritte),
und die zugehörige Abzählung $\#\text{Klassen}_k\le C^k$, $E_k\le C'^k$; dann konvergiert die Reihe für $\rho_b<1/(CC')$.

## 16. Satz: Schranke durch eingefrorene Umgebungen

**Satz.** Rahmen wie §14 ($H=V-t_cA$ stoquastisch, $\psi_0>0$ normiert). Für eine Konfiguration $E$ von $P-1$ Paaren sei
$G_E=\{b:E\cup\{b\}\in\mathcal C\}$ der freie Bereich für ein weiteres Paar, mit Eckschritten als Kanten und Leitwerten
$c_E(b,b')=\psi_0(E\cup b)\,\psi_0(E\cup b')$, und $\sigma_E=\min_f\sum_{b\to b'}c_E\,(\Delta x+f(b')-f(b))^2$ sein Windungsleitwert (ein Paar
bewegt sich, alle anderen sind eingefroren). Dann
$$\rho_s\;\ge\;\frac{t_c}{L^2}\sum_E\sigma_E .$$
Am RK-Punkt ($\psi_0=|\mathcal C|^{-1/2}$): $\rho_s^{RK}L^2/t_c\ge\frac1{|\mathcal C|}\sum_E\sigma_E^{(1)}=P\,\langle\sigma^{(1)}_E\rangle/\langle|G_E|\rangle$ mit den ungewichteten
Leitwerten $\sigma^{(1)}_E$ und Mitteln über die gleichverteilten $(P-1)$-Konfigurationen.

*Beweis.* Für jedes $E$ ist der optimale Strom $i_E=c_E(\Delta x+\nabla f_E^*)$ auf $G_E$ quellenfrei (Euler-Lagrange), mit
$\sum i_E\Delta x=\sum i_E^2/c_E=\sigma_E$. Setze $\theta(D\to D')=i_{D\setminus p}(b_p\to b_p')$, wenn der Schritt $D\to D'$ das Paar $p$ bewegt. Die
Kanten von $D$ sind genau die Kanten der Netze $G_{D\setminus p}$ an $b_p$, also $\mathrm{div}\,\theta(D)=\sum_p\mathrm{div}\,i_{D\setminus p}(b_p)=0$ (Kirchhoff). Mit
$\sum_D\sum_{p\in D}=\sum_E\sum_{b\in G_E}$ ist $\sum\theta\Delta x=\sum\theta^2/c=\sum_E\sigma_E$, und Thomson (§14 Folgerung 2) gibt die Behauptung. □

Der Fluss $\theta$ ist von selbst quellenfrei; Drift, Dipole und Paarungen (§15) braucht dieser Weg nicht.

**Zahlen (8×8, [einfrieren.py](einfrieren.py)), Einheiten $\rho_sL^2/t_c$:**

| Paare | Schranke RK | exakt RK | Schranke $H_A$ | exakt $H_A$ |
|---|---|---|---|---|
| 1 | 1,000 | 1,000 | 1,000 | 1,000 |
| 2 | 1,589 (84 %) | 1,899 | 1,322 (68 %) | 1,953 |
| 3 | 1,755 (65 %) | 2,682 | 1,339 (47 %) | 2,834 |
| 4 (7/8) | 1,495 (45 %) | 3,328 | 0,286 (8 %) | 3,640 |

Die Schranke ignoriert kollektive Bewegung und wird mit der Dichte schwächer; für $H_A$ bei 7/8-Füllung fast wertlos (dort trägt die
Korrelation in $\psi_0$, die das Einfrieren zerstört). Für kleine Dichte ist sie dagegen der einfachste Weg zu einem Satz.

**Folgerung (RK, kleine Dichte; Beweisskizze).** Es gibt $\rho_0>0$ und $c>0$ mit $\rho_s^{RK}\ge c\,t_cP/N$ für $\rho_b\le\rho_0$, gleichmäßig in $L$.
1. *Mehrpunkt-Schranke:* Wiederholtes Umsetz-Argument (§9 Schritt 3) gibt $P(b_1,\dots,b_k\in E)\le\rho'^k$ mit $\rho'=(P-1)/(2N-23(P-1))$.
2. *Peierls:* Eine Bindung ist gesperrt, wenn ein Paar in ihrer Zone (23 Bindungen) sitzt. Ein Weg quer zur Windungsrichtung (Länge
   $n\ge L$) mit $\ge\delta n$ gesperrten Bindungen braucht $\ge\delta n/23$ besetzte Bindungen in Abstand $\le2$ vom Weg; Wahrscheinlichkeit
   $\le C^n(C'\rho')^{\delta n/23}$, summierbar über alle Wege für kleines $\rho'$.
3. *Menger:* Die Zahl knotendisjunkter Windungskreise in $G_E$ ist der kleinste Schnitt; nach 2 ist jeder Querweg zu mindestens
   $1-\delta$ frei, also gibt es mit großer Wahrscheinlichkeit $m\ge aL$ solche Kreise.
4. *Thomson auf $G_E$:* Einheitsfluss auf $m$ knotendisjunkten Windungskreisen (Gesamtlänge $\le2N$) gibt $\sigma_E^{(1)}\ge(2mL)^2/(2\cdot2N)\ge a^2L^2$.
5. Mit $\langle|G_E|\rangle\le2N$: $\rho_s^{RK}L^2/t_c\ge P\,a^2L^2/(2\cdot2N)\cdot(1-o(1))$, also $\rho_s^{RK}\ge\tfrac{a^2}4\,t_cP/N$.
Zusammen mit §10 hätte der RK-Zustand bei kleiner Dichte rigoros ODLRO *und* Phasensteifigkeit. Die Konstanten wären klein ($\rho_0$ weit
unter 7/8-Füllung); für 7/8-Füllung bleibt der Weg über §15 (Hierarchie mit kurzen Wegen), der dort 91–96 % des exakten Werts erreicht.

**Wie weit trägt §16? Perkolation des freien Bereichs ([perkolation_frei.py](perkolation_frei.py), RK-Stichproben per Monte Carlo,
ein Paar herausgenommen, ungewichteter Windungsleitwert):**

| Lochdotierung $x$ | 2 % | 4 % | 6 % | 8 % | 10 % | 12,5 % (7/8) |
|---|---|---|---|---|---|---|
| $\sigma_E/\lvert G_E\rvert$, $L=24\to48$ | 0,86 → 0,86 | 0,70 → 0,69 | 0,51 → 0,53 | 0,40 → 0,31 | 0,26 → 0,18 | 0,077 → 0,034 |
| freier Anteil | 0,89 | 0,78 | 0,68 | 0,59 | 0,50 | 0,40 |

Bei 7/8-Füllung fällt der Leitwert wie $\approx1{,}6/L$ (L = 16/24/32/48: 0,093/0,077/0,051/0,034; viele Stichproben ohne Windungsweg): Der
freie Bereich perkoliert nicht. Die Schwelle liegt bei einem freien Anteil um 0,6 (Quadratgitter-Perkolation ≈ 0,59), also bei
$x\approx7\,\%$. **Der Weg über eingefrorene Umgebungen trägt bis etwa $x\approx6$–$7\,\%$, nicht bei 7/8-Füllung.** Dasselbe gilt für jede
Variante mit endlich vielen gemeinsam beweglichen Paaren in eingefrorener Umgebung: Ein Windungsweg der Länge $L$ muss durch den ganzen
eingefrorenen Rest. Bei 7/8-Füllung ist die Steifigkeit also wesentlich kollektiv; dafür bleibt §15.

## 17. Vorprüfung: Spektrallücke und Leitfähigkeit am RK-Punkt bei 7/8-Füllung (2026-11-03)

**Idee (Weg zum Beweis von $\rho_s^{RK}>0$ bei 7/8).** $H_{RK}-E_0=t_c\Lambda$ ist der Generator des klassischen Dimer-Ausschlussprozesses (Rate $t_c$ je erlaubtem Eckschritt, stationär die Gleichverteilung). Kette: (1) starke räumliche Durchmischung des Dimergases, weil $z\approx0{,}078<\lambda_c(22)=0{,}139$ (Weitz; Aktivität streng eingeschachtelt in Baustein 2, `../stufe_a_tkt`); (2) Spektrallücke $\ge c/L^2$ der kanonischen Dynamik; (3) Lücke $\Rightarrow$ Leitfähigkeit: mit einem lokalen Korrektor als Testfunktion $\mathrm{gap}_L\le Dk^2(1+o(1))$, $k=2\pi/L$, also $\rho_s^{RK}=2t_c\chi D\ge2t_c\chi\,c/(4\pi^2)-o(1)$ mit der Kompressibilität $\chi$. Offen ist vor allem (2): Für harte, ausgedehnte Teilchen mit blockierten Sprüngen gibt es keinen Satz (Lu-Yau, Cancrini-Martinelli setzen beschränkte Wechselwirkungen bzw. positive Raten voraus; Spohn-Yau vergleichen mit dem einfachen Ausschlussprozess, das geht hier nicht). Für Doppelblockaden und einseitige Blockaden (waagrecht gegen senkrecht) gibt es auch keinen driftfreien Teilgraphen, also keine Abkürzung über §14 Folgerung 3 mit $F=0$.

**Numerik** ([rk_luecke_exakt.py](rk_luecke_exakt.py) exakt, [rk_dynamik.py](rk_dynamik.py) kinetisches Monte Carlo, $\rho_b=1/32$; Ergebnisse in `ergebnisse_rk/`):

| $L$ | Paare | Lücke $\cdot L^2$ | $s_{RK}=\rho_s^{RK}/K_{RK}$ | $K_{RK}/t_c$ |
|---|---|---|---|---|
| 8 | 4 | 26,6 exakt (MC 27,5) | 0,988 exakt (MC 0,99 ± 0,01) | 0,0526 |
| 16 | 16 | 32,0 | 0,99 ± 0,01 | 0,0510 |
| 32 | 64 | 33,4 / 33,5 (zwei Seeds) | 0,99 ± 0,01 | 0,0506 |
| 64 | 256 | 33,5 | 1,00 ± 0,02 | 0,0505 |

- Lücke aus der Abklingrate der Dichtemode $k=2\pi/L$ (exakt auf 8×8: 0,4159, doppelt entartet; MC 0,429). Diffusiv mit $D\approx0{,}85\,t_c$; für ein freies Paar $D=0{,}5$, die Abstoßung erhöht die kollektive Diffusion (8×8 exakt: 0,49 / 0,55 / 0,61 / 0,67 für 1–4 Paare).
- $s_{RK}$ aus der Varianzrate der Gesamtverschiebung (Kipnis-Varadhan: $\lim\mathrm{Var}\,X(t)/t=Q$, §14), relativ zu $\langle A\rangle/4$ bei $\tau\to0$. Kein Abfall mit $L$.
- Einstein-Relation: $\chi=\rho_s^{RK}/(2t_cD)\approx0{,}47\,n$, plausibel für ein Gas harter Teilchen bei dieser Dichte.

**Folgerung.** Die Behauptung $\rho_s^{RK}\ge c\,t_c\,n$ bei 7/8-Füllung ist numerisch sehr robust, und Schritt (3) wäre in der Schranke praktisch verlustfrei. Der Beweis steht und fällt mit der Lücke $\ge c/L^2$ für die Dimer-Ausschlussdynamik.

**Literatur zur Kette (2026-11-03).**
- Lu-Yau / Cancrini-Martinelli (Lücke $\sim L^{-2}$ für Kawasaki-Dynamik unter starker Durchmischung, [mp_arc 99-275](https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=99-275)): verlangen beschränkte Potentiale und Raten $\ge c_m>0$; harte Wechselwirkung und blockierte Sprünge sind ausgeschlossen.
- Cancrini-Martinelli-Roberto-Toninelli, Kinetically constrained lattice gases (CMP 2010): Kob-Andersen-Modell (Bernoulli-Maß, Sprung nur bei genug leeren Nachbarn), Lücke $\sim L^{-2}$ bis auf $(\log L)^4$ bei jeder Dichte, mit Randquellen; Technik: Renormierung, Hilfs-Glauber-Dynamik mit langreichweitigen Bedingungen, Pfadargumente. Für nicht-kooperative Modelle (bewegliche endliche Cluster) Standardtechnik, dort auch positive Selbstdiffusion (Bertini-Toninelli 2004).
- **Statischer Schritt gelöst:** Davies-Perkins ([arXiv:2102.04984](https://arxiv.org/abs/2102.04984)): kritische Dichte für unabhängige Mengen fester Größe in Graphen vom Maximalgrad $\Delta$, $\alpha_c(\Delta)=\lambda_c(\Delta)/(1+(\Delta+1)\lambda_c(\Delta))$ (Besetzung von $K_{\Delta+1}$ bei $\lambda_c$). Jain-Michelen-Pham-Vuong ([arXiv:2305.06198](https://arxiv.org/abs/2305.06198)): Die Down-up-Kette (ein zufälliges Teilchen entfernen, an einem zufälligen Knoten einsetzen, falls erlaubt) mischt für $k\le(1-\delta)\alpha_c(\Delta)n$ in $O_{\delta,\Delta}(k\log n)$, Poincaré-Konstante $\Omega_{\delta,\Delta}(1/k)$ (aus einer Zusammenfassung von Abschnitt 3.4, nicht wörtlich geprüft), Log-Sobolev $\Omega(1/n)$ für $k\ge cn$.
- **Anwendung:** Paarkonfigurationen sind die unabhängigen Mengen fester Größe $P$ des Konfliktgraphen (Grad 22, $n=2N$ Bindungen). $\lambda_c(22)=21^{21}/20^{22}=0{,}13929$, $\alpha_c(22)=0{,}033135$; bei 7/8-Füllung $\rho_b=1/32=0{,}943\,\alpha_c$, also $\delta=5{,}7\,\%$. Die Fernsprung-Dynamik für genau unser kanonisches Gleichmaß hat damit eine Lücke $\ge c$ (je Paar Rate 1) [Lit].

**Beweisplan bei 7/8 (RK).**
1. [Lit] Lücke der Fernsprung-Dynamik $\ge c(\delta,22)$ (Jain-Michelen-Pham-Vuong).
2. [zu zeigen, computergestützt] Lemma vom beweglichen Cluster: Eine leere Box (Seite $\ell$ plus Rand) lässt sich bei jeder Außenkonfiguration durch Eckschritte um eine Gitterlänge verschieben und kann ein angrenzendes Paar mitnehmen. Hinweis: §12 (vorderstes Paar).
3. [zu zeigen] Vergleich der Dirichlet-Formen, $\mathcal E_{\rm Fern}\le C L^2\mathcal E_{\rm Eck}$ auf der Hauptkomponente, über Pfade durch bewegliche Cluster; deren Dichte ist nach unten beschränkt (endliche Energie: Box leer mit bedingter Wahrscheinlichkeit $\ge(1+\lambda)^{-|B|}$). Schwierig: Kosten ungünstiger Konfigurationen und die eingefrorenen Komponenten des Torus.
4. [Standard] Lücke $\ge c/L^2$ $\Rightarrow$ $\rho_s^{RK}\ge2t_c\chi c/(4\pi^2)-o(1)$, $\chi>0$ aus endlicher Energie.

**Schritt 3 genauer (2026-11-03).**
- Rahmen nach Bertini-Toninelli ([arXiv:cond-mat/0304694](https://arxiv.org/abs/cond-mat/0304694)): offene Box der Seite $\ell$ mit Reservoiren am Rand (Glauber-Züge mit Rate $1/\ell$), Vergleich mit der vollen Glauber-Dynamik statt mit Fernsprüngen; auch dort ist die Lücke $\sim\ell^{-2}$ bei fester Teilchenzahl nur für $N<\ell/3$ bewiesen.
- Statischer Schritt dann: Glauber-Dynamik des Hard-Core-Gases mischt in $O(n\log n)$ für $\lambda<(1-\delta)\lambda_c(\Delta)$ auf jedem Graphen vom Grad $\le\Delta$ (Chen-Liu-Vigoda, [arXiv:2011.02075](https://arxiv.org/abs/2011.02075)); bei uns $z\approx0{,}078=0{,}56\,\lambda_c(22)$, gleichmäßig in der Randbedingung [Lit].
- Pfadlemma (Bertini-Toninelli Lemma 3.2): Kosten eines Flips bei $x$ $\le A\{\ell\sum_{\rm Schlauch}\mathcal E_{\rm Eck}+\sum_{\rm Rand}\mathcal E_{\rm Glauber}\}$. Dort trägt ein endlicher Lochhaufen, am Rand erzeugt, den Flip zu $x$; jeder Schritt ist für jede Konfiguration erlaubt, Information und Maßverzerrung bleiben beschränkt. Das benutzt, dass beim Produktmaß der Inhalt vor dem Haufen beliebig hinter ihn gesetzt werden darf.
- **Kern [L]:** Für harte Dimere fehlt dieses Lemma. (1) Einen ganzen Schlauch leeren geht für jede Konfiguration (vorderstes Paar, §12: diagonal vom nahen Schlauchrand weg in leeren Raum ziehen; $\eta$ und $\eta^x$ führen auf dieselbe Konfiguration), löscht aber den Inhalt von $\sim\ell$ Paaren, also Vielfachheit $e^{c\ell}$. (2) Ein endlicher Haufen setzt den Inhalt hinter sich, und dort kann er mit den hinteren Nachbarn kollidieren (Verschieben, Spiegeln, volles Band: alle scheitern im schlechtesten Fall).
- Auswege: (a) Haufen mit Fracht (bis zu $K$ Paare mitnehmen, hinten absetzen, sobald Platz ist), am Rechner zu testen; (b) Renormierung wie Cancrini-Martinelli-Roberto-Toninelli (Fernsprung nur, wenn gute Blöcke einen Transportweg bereitstellen), dort aber mehrfach Produktstruktur benutzt.

**Test Haufen mit Fracht (2026-11-03, [rk_haufen_test.py](rk_haufen_test.py), $L=64$, je 20 Lagen; `ergebnisse_rk/haufen_test.json`).** Schlauch der Höhe $h$, Haufen der Breite $w$ wie bei Bertini-Toninelli vom Rand bis zum Ende geschoben, Inhalt dahinter um $w$ verschoben; gezählt werden verschobene Paare, die mit festen Paaren außerhalb kollidieren, und ob ein verträglicher Ersatzplatz im Abstand $\le2$ existiert (sonst Fracht). Bewegungen im Haufen nicht simuliert.

| Lage | $\rho_b$ | Kollisionen je Spalte | lokal repariert | Fracht am Ende |
|---|---|---|---|---|
| Gleichgewicht (7/8) | 0,031 | 0,043–0,053 (alle $h$, $w$) | alle | 0 |
| Gleichgewicht | 0,045 | 0,06–0,19 ($L=48$) | fast alle | ≤ 0,3 |
| zufällig gesättigt | 0,081 | 0,50–0,88 | fast alle | ≤ 1,4 |

- Die Kollisionen sitzen an den beiden Schlauchseiten (Rate je Spalte unabhängig von $h$ und $w$). Fracht ist kein Problem, Ersatzplätze gibt es fast immer.
- **Das Problem ist die Information:** Jede Reparatur ist eine Wahl unter $\sim50$ Ersatzplätzen. Bei 7/8-Füllung sind das typisch $\approx0{,}05\cdot\ln50\approx0{,}2$ nats je Spalte, im dicht gepackten Fall $\approx3$ nats je Spalte. Die Vielfachheit der Abbildung $\eta\mapsto\eta_i$ wächst also wie $e^{c\ell}$, und das Pfadlemma braucht sie gleichmäßig beschränkt. **Weg (a) scheidet damit aus**, nicht an der Machbarkeit, sondern an der Information.
- Bleibt Weg (b): eine eingeschränkte Hilfsdynamik (Glauber-Flip nur, wenn ein Transportweg ohne Kollision existiert) und deren Poincaré-Ungleichung über Renormierung (Cancrini-Martinelli-Roberto-Toninelli), übertragen vom Produktmaß auf das Hard-Core-Maß mit starker Durchmischung.

**Numerischer Abschluss von Schritt 3 (2026-11-03) [N].** [rk_numerik.py](rk_numerik.py) (Prüfungen 1-3, [rk_numerik_kette.sh](rk_numerik_kette.sh)), [rk_aufloesung.py](rk_aufloesung.py) (Prüfung 4); $\rho_b=1/32$, Ergebnisse in `ergebnisse_rk/num_L*.json`, `aufloesung_L128*.json`.

1. *Steifigkeit direkt* (Kipnis-Varadhan, ohne Umweg über die Lücke): $s_{RK}=\rho_s^{RK}/K_{RK}$ = 1,06 / 0,87 ($L=32$), 1,02 / 0,98 (64), 1,01 / 0,99 (128), 0,95 (256), je ±5–7 %; mit den früheren Läufen $1{,}00\pm0{,}03$ ohne Trend in $L$. Stromzuwächse nach einer Zeiteinheit unkorreliert ($|C_J(1)/C_J(0)|<0{,}01$), kein Langzeitschwanz.
2. *Einstein-Relation*: $Q$ aus $2DPS(k_{\min})$ gegen $Q$ direkt, Verhältnis 0,93 / 1,12 / 0,95 / 1,01 / 0,98 / 1,06 / 1,13, also $1{,}03\pm0{,}03$; $D\approx0{,}86$–$0{,}89$, $S(k\to0)\approx0{,}45$–$0{,}47$.
3. *Langsamste Mode*: Dichtemode 1/e-Zeit 30 / 119 / 462 / 1500 für $L$ = 32 / 64 / 128 / 256, also $L^2/(4\pi^2D)$; Orientierung ($N_h-N_v$, $k=0$ und $2\pi/L$) 0,64 und blockierte Schritte $B$ 6,4, beide unabhängig von $L$, $C_B$ bei Verzögerung 100 ≈ 0. Nichts ist langsamer als die Dichtemode (auf 8×8 exakt: Lücke = Dichtemode).
4. *Schlimmster Fall*: Quadrat der Seite $R$ in einer Gleichgewichtslage ($L=128$, je 4 Lagen) dicht gepackt, Zerfall des Überschusses. Zufällig gesättigt ($\rho_b\approx0{,}08$): $\tau_{1/e}/R^2$ = 0,069 / 0,078 / 0,078 / 0,080 / 0,073 für $R$ = 12 / 16 / 24 / 32 / 48. Geordneter Kristall (waagrechte Paare im Raster 3×2, $\rho_b=1/12$, 75–96 % aller Schritte blockiert, innen keiner erlaubt): 0,078 / 0,075 / 0,100 / 0,062 für $R$ = 16 / 24 / 32 / 48. Diffusiv, keine glasartige Verlangsamung.

**Bewertung.** Die Behauptung $\rho_s^{RK}\ge c\,t_c\,n$ bei 7/8-Füllung gleichmäßig in $L$ ist numerisch von vier unabhängigen Seiten gestützt ($s_{RK}=1{,}00\pm0{,}03$ bis $L=256$; Lücke diffusiv und gleich der Dichtemode; auch maximal blockierte Gebiete lösen sich diffusiv auf). Formal bleibt sie [N]; der Beweis von Schritt 3 (Weg b) ist offen.

## 18. Schritt 4: Aus der Lücke folgt eine positive Leitfähigkeit (bedingter Satz, offene Box, 2026-11-03)

**Vorbemerkung.** Allein aus einer globalen Lücke folgt keine untere Schranke für einen Leitwert: Auf einem Expander, auf dem $\Delta x$ fast ein Gradient ist, ist die Lücke groß und der Leitwert fast null. Es braucht Lokalität und Homogenität. Die erste Fassung dieses Abschnitts arbeitete auf dem Torus mit exakter Translationsinvarianz; dort fehlen für das kanonische Maß Abfall der Korrelationen und Gleichwertigkeit der Ensembles (die bekannten Beweise setzen beschränkte Wechselwirkungen voraus), und die eingefrorenen Komponenten verlangen die offene Irreduzibilität aus §12. In der offenen Box mit Reservoiren (Rahmen wie Bertini-Toninelli) ist das stationäre Maß großkanonisch, und für genau dieses Hard-Core-Maß ist die starke räumliche Durchmischung bewiesen (Weitz). Das Ergebnis ist eine untere Schranke für die Leitfähigkeit des unendlichen Systems (Varadhan, Green-Kubo).

**Rahmen.**
- Box $\Lambda_\ell=\{0,\dots,\ell-1\}^2$, Paare auf Bindungen mit beiden Plätzen in $\Lambda_\ell$, außerhalb leer. Großkanonisches Maß $\mu_\ell(D)\propto z^{\lvert D\rvert}$ auf den verträglichen Konfigurationen, $z=z^*$ die Aktivität zur Dichte $\rho_b=1/32$, $z^*\in[0{,}0765;0{,}0792]$ (Baustein 2, `../stufe_a_tkt`).
- Dynamik: Eckschritte mit Rate 1 (Ziel in der Box und verträglich); an jeder Randbindung (ein Platz auf dem Rand) Erzeugen mit Rate $\tfrac1\ell\tfrac z{1+z}$, falls verträglich, und Vernichten mit Rate $\tfrac1\ell\tfrac1{1+z}$. Reversibel bezüglich $\mu_\ell$; Dirichlet-Form $\mathcal E_\ell$, Lücke $\gamma_\ell$.
- Unendliches Volumen: $\mu$ das Gibbs-Maß zu $z^*$ (eindeutig, da $z^*<\lambda_c(22)=0{,}1393$). Lokale Funktionen $F^x,F^y$ (abhängig von den Bindungen im Abstand $\le r$ vom Ursprung, $F^y$ die Drehung von $F^x$, $F^x$ gerade unter $y\to-y$), $\Phi^{x,y}=\sum_u\tau_uF^{x,y}$; $W_0(F)$ = Summe von $(\Delta x+\nabla_m\Phi^x)^2$ über die geordneten Schritte $m$ der Paare in der Ursprungszelle; $\sigma_\infty(F)=\mu(W_0(F))$, $\sigma_\infty=\inf_F\sigma_\infty(F)$, $\rho_s^{RK}(\infty):=t_c\sigma_\infty$.

**Eingänge.**
- (W) [Lit, für den harten Kern bewiesen]: Weitz (STOC 2006): starke räumliche Durchmischung des Hard-Core-Modells auf jedem Graphen vom Grad $\le\Delta$ für $\lambda<\lambda_c(\Delta)$; hier Konfliktgraph der Box, Grad $\le22$. Daraus (i) Eindeutigkeit von $\mu$ und $\lvert\mu_\ell(f)-\mu(f)\rvert\le C_fe^{-d/\xi}$ für lokales $f$ im Abstand $d$ vom Rand; (ii) $\sum_u\lvert\mathrm{Cov}_{\mu_\ell}(f,\tau_ug)\rvert\le C_{f,g}$ gleichmäßig in $\ell$.
- (L$'$) [N]: $\gamma_\ell\ge c'/\ell^2$ für alle $\ell$. Exakt $\gamma_\ell\ell^2$ = 5,70 / 6,31 / 6,62 ($\ell$ = 4 / 5 / 6, vollständige Aufzählung, bis 349 511 Konfigurationen); kinetisches Monte Carlo 6,82 / 6,97 / 6,98 / 7,05 / 7,25 / 7,04 ($\ell$ = 8 / 12 / 16 / 24 / 32 / 48), auf $\ell\le6$ gegen die exakten Werte auf 2–3 %; langsamste Mode ist die Teilchenzahl ([rk_box.py](rk_box.py), `ergebnisse_rk/box_*.json`). Vorsichtig $c'=6{,}6$.

**Lemma 18.1 (Irreduzibilität, streng).** Von jeder verträglichen Konfiguration in $\Lambda_\ell$ ist die leere erreichbar, und umgekehrt.

*Beweis.* Richtung $s=(1,1)$. Das Paar mit größtem $\sigma=s\cdot x$ kann nach dem Lemma vom vordersten Paar (§12) in Richtung $s$ ziehen: Die blockierenden Bindungen liegen auf Höhe $\sigma+2,\sigma+3$, dort ist kein Paar, außerhalb der Box ohnehin nicht. Es zieht, bis seine Bindung einen Platz auf dem oberen oder rechten Rand hat, und wird dort vernichtet. Induktion über die Paarzahl; alle Züge sind umkehrbar. □

**Satz 18.2 (bedingt).** Unter (W) und (L$'$) gilt für jedes lokale $F$
$$\sigma_\infty(F)\;\ge\;\frac{c'\kappa}{\pi^2},\qquad\kappa=\tfrac16\,(1+z^*)^{-22}\,\frac{z^*}{(1+z^*)^2}\;\ge\;0{,}00205,$$
also $\rho_s^{RK}(\infty)\ge t_c\,c'\kappa/\pi^2$.

*Beweis.* $\psi(x,y)=\sin\frac{\pi(x+1/2)}\ell\,\sin\frac{\pi(y+1/2)}\ell$ auf den Bindungsmitten, $g=\sum_p\psi(x_p)+\sum_u\big(\partial_x\psi(u)\,\tau_uF^x+\partial_y\psi(u)\,\tau_uF^y\big)$.
1. *Zuwachs.* Für einen Eckschritt $m$ mit Mitte $\bar x$: $g(D')-g(D)=\partial_x\psi(\bar x)(\Delta x+\nabla_m\Phi^x)+\partial_y\psi(\bar x)(\Delta y+\nabla_m\Phi^y)+\varepsilon_m$, $\lvert\varepsilon_m\rvert\le C_F\ell^{-2}$ (Taylor, $\lvert\nabla^2\psi\rvert\le\pi^2/\ell^2$, Lokalität von $F$).
2. *Volumenterm der Dirichlet-Form.* Nach (W)(i) ist der Erwartungswert von $(\Delta x+\nabla_m\Phi^x)^2$ für Schritte an einem Ort im Abstand $d$ vom Rand gleich dem Volumenwert bis auf $C_Fe^{-d/\xi}$; der Mischterm verschwindet im Volumen wegen der Spiegelsymmetrie $y\to-y$. Mit $\sum_u\lvert\nabla\psi(u)\rvert^2=\tfrac{\pi^2}2(1+O(1/\ell))$ folgt $\le\tfrac{\pi^2}4\sigma_\infty(F)+O_F(\xi/\ell)$.
3. *Reservoirterm.* Auf Randbindungen ist $\lvert\psi\rvert\le\pi/\ell$, bei $O(\ell)$ Randbindungen mit Rate $1/\ell$ also $O_F(\ell^{-2})$.
4. *Varianz, ohne Grenzübergang.* $I$ = waagrechte Bindungen an den Plätzen $(3i,2j)$, paarweise verträglich, Dichte $1/6$ je Platz. Gegeben alle Bindungen außerhalb von $I$, sind die Besetzungen in $I$ unabhängig; $b\in I$ ist frei mit Wahrscheinlichkeit $\ge(1+z)^{-22}$ (endliche Energie: jede der 22 Nachbarbindungen bedingt leer mit Wahrscheinlichkeit $\ge1/(1+z)$) und dann besetzt mit $z/(1+z)$. Also $\mathrm{Var}\big(\sum_p\psi(x_p)\big)\ge\sum_{b\in I}\psi(x_b)^2(1+z)^{-22}\tfrac z{(1+z)^2}=\kappa\tfrac{\ell^2}4(1+O(1/\ell))$. Der Korrekturteil hat nach (W)(ii) Varianz $\le\pi^2C_F$, also $\mathrm{Var}\,g\ge\kappa\tfrac{\ell^2}4(1-O_F(1/\ell))$.
5. *Poincaré.* $\mathrm{Var}\,g\le\mathcal E_\ell(g)/\gamma_\ell$ und (L$'$): $\tfrac{c'}{\ell^2}\kappa\tfrac{\ell^2}4(1-o(1))\le\tfrac{\pi^2}4\sigma_\infty(F)+o(1)$; $\ell\to\infty$ gibt die Behauptung. □

**Folgerung (Zahlen).** Mit $c'=6{,}6$ [N] und $\kappa\ge0{,}00205$ [S]: $\rho_s^{RK}(\infty)\ge0{,}0014\,t_c$. Mit der gemessenen Kompressibilität $\chi=nS(0)\approx0{,}0288$ statt $\kappa$: $\ge0{,}019\,t_c$. Gemessen sind $0{,}050\,t_c$; die Box-Fassung verliert einen Faktor $\approx2{,}5$, weil die langsamste Mode der Box durch die Reservoire begrenzt ist ($\gamma\ell^2\approx7$ statt $2\pi^2D\approx17$ für eine reine Dirichlet-Mode).

**Stand der Kette.**
- Streng: Lemma 18.1; Satz 18.2 unter (W) [Lit, für den harten Kern bewiesen] und (L$'$); Lemma zur Varianz ohne Grenzübergang.
- Numerisch: (L$'$); unabhängig davon auf dem Torus $\rho_s^{RK}(L)/K_{RK}=1{,}00\pm0{,}03$ bis $L=256$ (§17).
- Offen [L]: die Identifikation von $\rho_s^{RK}(\infty)=t_c\sigma_\infty$ mit dem Grenzwert der Torus-Steifigkeit. Die Ungleichung $\limsup_L\rho_s^{RK}(L)\le t_c\sigma_\infty$ folgt aus §14 mit $f=\Phi_F$, braucht aber die lokale Konvergenz der kanonischen Torusmaße; die umgekehrte Richtung ist die hydrodynamische Identifikation. $\sigma_\infty$ selbst ist die Green-Kubo-Leitfähigkeit des unendlichen Systems, die übliche Definition der Volumen-Leitfähigkeit eines Gittergases (Spohn, Varadhan). Die Steifigkeit der KT-Physik ist dagegen die Torus-Steifigkeit (verdrillte Randbedingung); dass beide gleich sind, ist genau die offene Identifikation. (Stand 2026-11-04: bedingt bewiesen unter (C), §19.) Für uns ist die Richtung $\liminf_L\rho_s^{RK}(L)\ge t_c\sigma_\infty$ die nötige, und gerade sie ist die schwere: Der Minimierer auf dem Torus darf nichtlokal sein. Bewiesen ist die Gleichheit in Modellen, in denen die Nicht-Gradienten-Methode greift (Varadhan 1994, Quastel 1992; Lücke $O(\ell^{-2})$ in kanonischen Boxen gleichmäßig in der Teilchenzahl und Charakterisierung der geschlossenen Formen). Hier fehlt schon der erste Eingang, weil kanonische Boxen bei hoher Dichte eingefrorene Konfigurationen haben (§17, Prüfung 4). Für Modelle mit entarteten Raten gibt es Varianten (Gonçalves-Landim-Toninelli 2009), für harte Dimere ausgeführt ist keine. Numerisch spricht nichts für einen Unterschied [N]: $\rho_s^{RK}(L)/K_{RK}$ ist von $L=16$ bis 256 konstant ($1{,}00\pm0{,}03$), und die Einstein-Relation $Q=2DPS(k_{\min})$ verknüpft den Torus-Leitwert auf jeder Größe mit der hydrodynamischen Diffusion ($1{,}03\pm0{,}03$, §17, Prüfung 2).

## 19. Schritt 5 bedingt: Identifikation unter gleichmäßiger Green-Kubo-Konvergenz (2026-11-04)

Zusammenfassung mit Beweis im PDF [beweis_rk/stand_beweis_rk.pdf](beweis_rk/stand_beweis_rk.pdf) (§7.1).

**Bild.** ODLRO heißt globale Phasenkohärenz (nebendiagonal); die Steifigkeit ist der Koeffizient der *lokalen* Gradientenenergie $\tfrac12\rho_s\int(\nabla\theta)^2$. Auf dem Torus ist die Verdrillung ein gleichmäßiger Gradient, also ist der Torus-Leitwert die lokale Dichte, solange die Verdrillungsenergie das Integral dieser Dichte ist. Hindernis wäre eine nichtlokale, (näherungsweise) erhaltene Größe, an die der Strom koppelt (Windungs- oder Flusssektoren dicht gepackter Dimere, Zahl der Streifen in t-J). Am RK-Punkt ist ODLRO $\langle T_{b\leftarrow b'}\rangle$ ein Produkt lokaler Faktoren des freien Volumens: langreichweitig, aber nicht nichtlokal gebunden.

**Rahmen.** Großkanonischer Torus $\mu_L\propto(z^*)^{|D|}$ (alle Paarzahlen), Eckschritt-Dynamik (Paarzahl erhalten), Generator $-\Lambda$; Drift $d=\sum_xd_x$; $c_L(t)=L^{-2}\mu_L(d\,e^{-t\Lambda}d)\ge0$, fallend. Großkanonischer Torus-Leitwert $G_L$ (gewichtetes Mittel der Leitwerte aus §14), in Green-Kubo-Form $G_L/t_c=\tfrac14\mu_L(A_0)-2\int_0^\infty c_L\,dt$ ($d$ hat auf jeder Komponente Mittel 0).

**Annahme (C).** $\varepsilon(T):=\sup_L\int_T^\infty c_L(t)\,dt\to0$ für $T\to\infty$. Spektral: verletzt genau dann, wenn Moden mit in $L$ verschwindender Rate einen endlichen Anteil von $L^{-2}\langle d,\Lambda^{-1}d\rangle$ tragen. Hydrodynamisch erwartet: Langzeitschwanz $\sim t^{-2}$ in 2D, $\varepsilon(T)\sim1/T$ [B].

**Satz 19.1 (bedingt).** Unter (C) gilt $\lim_LG_L=t_c\sigma_\infty$.
*Beweisgang.* (1) Weitz-SSM gilt für jeden Graphen vom Grad $\le22$, also auf dem Torus: Kovarianzabfall und $\mu_L(f)\to\mu(f)$ [Lit]. (2) Endliche Ausbreitung (Liggett): $e^{-t\Lambda}d_y$ ist bis auf $Ce^{-R}$ lokal im Radius $R\ge C't$ [Lit]. (3) Für festes $t$: $c_L(t)=\sum_y\mu_L(d_0e^{-t\Lambda}d_y)\to c_\infty(t)$, beschränkt durch $c_L(0)$. (4) (C) und Fatou für den Schwanz: $\lim G_L/t_c=\tfrac14\mu(A_0)-2\int_0^\infty c_\infty=\sigma_{GK}$. (5) $\sigma_{GK}=\sigma_\infty$ (Resolvente, lokale Funktionen als Kern; Spohn 1991 Teil II Kap. 2) [Lit, für den harten Kern nicht eigens nachgerechnet]. □

**Bemerkungen.**
- (C) ist von der Positivität logisch unabhängig. Mit (W), (L$'$), (C): $\lim G_L\ge0{,}0014\,t_c$.
- Quantitativ ersetzte (C) sogar (L$'$): $G_L/t_c\ge\tfrac14\mu_L(A_0)-2Tc_L(0)-2\varepsilon(T)$, $c_L(0)$ lokal und mit der Clusterentwicklung aus Baustein 2 abschätzbar [B].
- Kanonisch bei fester Dichte: braucht Stetigkeit in der Dichte gleichmäßig in $L$ [H]; eingefrorene Komponenten (Ketten um den Torus, §12) haben großkanonisch exponentiell kleines Gewicht [B].
- Numerisch [N]: $\mathrm{Var}\,X(\tau)/\tau$ flach von $\tau=1$ bis 300–1000 auf ±5 % ($L=64$–256), $C_J(t)/C_J(0)$ für $t\ge1$ im Rauschen (±0,01), ganzer Green-Kubo-Abzug auf 8×8 exakt 1,2 % von $K_{RK}$. Ein echter Test bräuchte $c_L(t)$ mit kleinerem Fehler bis $t\sim L^2$.
- Gleiche Struktur wie Streifen gegen d-Welle in t-J: Streifen sind diagonale Ordnung mit nichtlokaler, fast erhaltener Größe und verletzen (C); in Stufe A am RK-Punkt schließt SSM sie streng aus.

## 20. Übertrag auf Stufe B und B+ (2026-11-04)

Im PDF [beweis_rk/stand_beweis_rk.pdf](beweis_rk/stand_beweis_rk.pdf) §8, mit Tabelle Schritt für Schritt.

**Satz 20.1 (RK-Punkt von B).** Mit der Diagonale, die $H_B=t_c\Lambda_{\rm Paar}+\tfrac J2\Lambda_{\rm Spin}$ macht, ist der Grundzustand die Gleichverteilung über Paar- und Spinkonfigurationen (Marshall-Eichung), und die Ladungssteifigkeit ist auf jedem Torus gleich $\rho_s^{RK}(L)$ von Stufe A.
*Beweis.* Leitwertform §14 auf $(D,\sigma)$; die Verdrillung koppelt nur an Paarschritte. Zahl der Spinkonfigurationen unabhängig von $D$, Raten und $\Delta x$ unabhängig von $\sigma$, Eckschritte bilden $\sigma$ bijektiv ab. Jensen für $\bar f(D)=\mathbb E_\sigma f(D,\sigma)$; Austauschschritte haben $\Delta x=0$. □
Der Spinteil wird dabei nach Untergitterdrehung zum Heisenberg-Ferromagneten $J\sum(\tfrac14-\mathbf S_i\cdot\mathbf S_j)$: unphysikalisch, für die Ladung ohne Belang.

**Satz 20.2 (Monotonie).** Zusätzliche Schritte mit symmetrischen Raten bei gleichem stationärem Maß vergrößern Dirichlet-Form, Lücke, Torus-Leitwert und $\sigma_\infty(F)$ (Rayleigh-Monotonie). □
Für $|B+|$ (B+ mit $-|\cdot|$ statt aller Nebendiagonalelemente) folgt am RK-Punkt, sofern Raten und Sperrregel der zusätzlichen Paarschritte nicht von den Spins abhängen [B]: Lücke $\ge$ die von A, $\sigma_\infty\ge\sigma_\infty^A\ge0{,}0014\,t_c$ unter (W), (L$'$).

**Einordnung.**
- An den RK-Punkten: B bringt für die Ladung nichts Neues, $|B+|$ liegt darüber; der Satz für A ist untere Schranke für alle drei RK-Fassungen.
- Physikalische Grundzustände: B wie A (Leitwertform ja, Gewichte unbekannt, kein SSM für $\psi_0^2$). B+ ist frustriert und nicht stoquastisch (`satz_b_herleitung.md` §7): keine Leitwertform, nicht einmal $\rho_s\ge0$ gesichert; die diamagnetische obere Schranke bleibt.
- Nutzen von B: Der Wurm misst für stoquastische Grundzustände die Quantenfassung von (C) und von „Leitwert = Leitfähigkeit“: $\rho_T(q\to0)$ aus der transversalen Antwort gegen $\rho_s$ aus der Windung. Gemessen für $H_A$ bei $T=0{,}04\,t_c$, $L=16$–48 (`../stufe_a_tkt/auswertung_nb5.py`) [N]: $\rho_T(q)/K$ bei gleichem $q$ unabhängig von $L$; Grenzwert $q\to0$ 0,975–0,988 gegen Windung 0,995 ± 0,008, also Übereinstimmung auf 1–2 %.

## 21. Box-Fassung des ganzen Beweises (2026-11-04)

Eigenes Verzeichnis [beweis_box/](beweis_box/README.md), Dokument [beweis_box/beweis_box.pdf](beweis_box/beweis_box.pdf). Alle Schritte in der offenen Box mit Paarreservoiren; Schritt 5 über die Volumensteifigkeit $\rho_s^{\rm Vol}=t_c\sigma_\infty$ mit dem Haken (KT-Sprung gilt für die renormierte Steifigkeit; $\rho_s^{\rm Box}\le\rho_s^{\rm Vol}$ ist die leichte Richtung [S], Gleichheit braucht Lokalität (C$_{\rm Box}$)).
- Neu streng: Steifigkeit der Box über Phasenkontakte (geschlossene Box: null, Eichung), Leitwertform der Box, leichte Richtung $\limsup\rho_s^{\rm Box}\le\rho_s^{\rm Vol}$ unter (W) ohne kanonisches Maß.
- Neu numerisch: Mit starken Kontakten (Rate 1) ist die Lücke $\gamma\ell^2\to2\pi^2D\approx17$ (Dirichlet-Mode), Satz 18.2 damit fast scharf: $\rho_s^{\rm Vol}\ge0{,}0031\,t_c$ ($c'=15$, $\kappa$), $\ge0{,}044\,t_c$ mit $\chi$. Ohm in der Box: $\rho_s^{\rm Box}(\ell)\to0{,}04965$, auf 0,1 % die Volumensteifigkeit $0{,}04971\pm0{,}00001$ (Torus als Näherung des unendlichen Volumens, Green-Kubo); transversale Antwort stetig bei $q\to0$.

## 22. Varianzschranke über Blöcke (2026-11-04)

[beweis_box/varianz_cluster.py](beweis_box/varianz_cluster.py), im PDF der Box-Fassung Lemma 6.1. Gilt ebenso für Satz 18.2 hier.
- Exakt $P(b\text{ frei})=\tfrac{1+z}z\rho_b$ (DLR) statt $(1+z)^{-22}$: $\kappa\ge\rho_b/(6(1+z^*))=0{,}0048$.
- Blöcke $a\times b$ mit einer leeren Platzreihe dazwischen, gegeben alles außerhalb unabhängig; $c=\min_{A,z}\mathrm{Var}(N_A)/E(N_A)$ über alle Teilmengen (Zeta-Transformation) und $z\in[0{,}0765;0{,}0792]$ (Monotonie von $Z_1/Z_0$ und $Z_2/Z_1$ auf Teilintervallen) [S, computergestützt, Gleitkomma]. $4\times4$: $c=0{,}5623$, $\kappa\ge0{,}01686$, das 8,2-Fache der alten Schranke, Faktor 1,7 unter $\chi$.
- Folge: $\rho_s^{\rm Vol}\ge0{,}0113\,t_c$ (schwache Kontakte, $c'=6{,}6$), $\ge0{,}0256\,t_c$ (starke Kontakte, $c'=15$); gemessen 0,0497.
- Minimum jedes Mal beim ganzen Block; bliebe das so [H], gäben $6\times6$-Blöcke 0,0202 und sehr große Blöcke $\chi$.
- Nachtrag (2026-11-04, [beweis_box/varianz_realisierbar.py](beweis_box/varianz_realisierbar.py)): Es genügt das Minimum über die vorkommenden $A=C\setminus B(\eta)$ ($\eta$ unabhängige Menge des Rings um den Block); damit Blöcke bis $6\times6$ [S, computergestützt]. In allen ist der ganze Block der schlechteste Fall (Abstand zum nächsten Muster schrumpft bis 0,0007; allgemein über Graphen falsch). $6\times6$: $c=0{,}5227$, $\kappa\ge0{,}01999$, Faktor 1,4 unter $\chi$; $\rho_s^{\rm Vol}\ge0{,}0134\,t_c$ (schwach) bzw. $\ge0{,}0304\,t_c$ (stark), 61 % des gemessenen Werts.

## 23. Basisfall einer Renormierung für (L$'$) (2026-11-04)

Vorprüfung, ob ein Weg wie Cancrini–Martinelli trägt ([beweis_box/basisfall.py](beweis_box/basisfall.py), [beweis_box/basisfall_mc.py](beweis_box/basisfall_mc.py); README dort).
- Freier Rand: kanonische Eckschritt-Dynamik zusammenhängend bis $N=3$ ($4\times4$), $2$ ($5\times5$), $4$ ($6\times6$, $8\times4$); Lücken 0,08–0,35 [N, exakt].
- Gleichmäßig über alle Randmuster: nein (5×5, $N=3,4$: 37 % zusammenhängend, Lücken bis 0,004) [N, exakt]. Ein gleichmäßiger Basisfall ist ausgeschlossen.
- Gewichtet mit dem Gleichgewicht: schlechte Blöcke 0,4 % / 0,15 % / 0,03 % (4×4 / 5×5 / 6×6), mit der Blockgröße fallend [N]. Also Renormierung mit guten Blöcken (CMRT, GLT) [B, H].

## 24. Struktur für die Analysis: schlechte Blöcke und lokaler Korrektor (2026-11-04)

README in [beweis_box/](beweis_box/README.md).
- Schlechte Blöcke sind Randartefakte (eingesperrte Paare am Rand, kleine Komponenten); Befreiungsradius stets ≤ 2, also lokal prüfbare Definition „gut“ [N, B].
- Optimaler Zweikörper-Korrektor: nur gemischt orientierte Paare (gleich orientierte heben sich exakt weg), getragen von den Kontaktlagen (½, 2½) und (2½, ½) mit entgegengesetzten Vorzeichen (d-Welle); schließt 77 % von $K-\sigma_\infty$, Rest dreikörperartig [N].
- Nachtrag: Dreikörpermotive (kompakt, ≤ 3,5) heben den Anteil auf 92 % ($\sigma=0{,}04978$). Große Stichproben: schlechte Blöcke 0,36 / 0,17 / 0,006 % (4×4 / 5×5 / 6×6), alle mit Radius ≤ 2 befreit; mit Rand 2 keiner von 500 000 schlecht [N].

## 25. Erste Lemmata für die Renormierung (Versuch, 2026-11-04)

**Lemma A (Drift als Kontaktsumme) [S].** Die vier Eckschritte eines Paares haben $\Delta x=\pm\tfrac12$, je zwei von jedem Vorzeichen, also $\sum_k\Delta x_k=0$. Damit ist die Drift
$$d(D)=\sum_p\sum_{k\ \rm erlaubt}\Delta x_k=-\sum_p\sum_k\Delta x_k\,\mathbf 1[D\cap Z_k(p)\ne\emptyset],$$
mit $Z_k(p)=X(b_k')\setminus X(b_p)$ der Sperrzone des Schritts $k$ (5 Bindungen, §12). Zerlegt nach der Zahl der sperrenden Paare: $d=d^{(2)}+d^{(\ge3)}$ mit
$$d^{(2)}=\sum_{p\ne q}w(p,q),\qquad w(p,q)=-\sum_k\Delta x_k\,\mathbf 1[q\in Z_k(p)],$$
und $d^{(\ge3)}$ nur aus Schritten, die von mindestens zwei Paaren zugleich gesperrt sind (in einer Sperrzone gibt es verträgliche Paare von Bindungen, etwa $\{(2,1),(3,1)\}$ und $\{(1,2),(0,2)\}$ im Beispiel von §12).
1. $w(p,q)\ne0$ nur, wenn $q$ in einer Sperrzone von $p$ liegt (Kontaktlagen).
2. Für gleich orientierte $p,q$ gilt $w(p,q)+w(q,p)=0$. *Beweis:* Die Punktspiegelung durch die Mitte zwischen den Bindungsmitten von $p$ und $q$ vertauscht die beiden Bindungen (sie erhält die Orientierung), bildet den Schritt $k$ von $p$ auf einen Schritt $k'$ von $q$ mit $\Delta x_{k'}=-\Delta x_k$ ab und $Z_k(p)$ auf $Z_{k'}(q)$. □ Im Zweikörperanteil bleiben also nur gemischt orientierte Paare.
3. Die gemischten Kontaktlagen sind genau die senkrechten Bindungen der Sperrzonen: für $p$ waagrecht bei $(0,0)$–$(1,0)$ und den Schritt nach $(1,1)$ die Versätze $(1\tfrac12,1\tfrac12)$ und $(\tfrac12,2\tfrac12)$, mit Spiegelbildern; für senkrechtes $p$ gedreht $(2\tfrac12,\tfrac12)$. Das sind die Motive des optimalen Korrektors (§24: $(\tfrac12,2\tfrac12)$ mit $-0{,}080$, $(2\tfrac12,\tfrac12)$ mit $+0{,}077$, $(1\tfrac12,1\tfrac12)$ klein). Die d-Wellen-Vorzeichen kommen aus der Drehung um $90^\circ$, die H und V vertauscht.

Folge: Der Korrektor muss im Wesentlichen die Poisson-Gleichung für eine explizite, lokale Zweikörper-Quelle lösen; numerisch tragen Zweikörpermotive 78 %, kompakte Dreikörpermotive weitere 14 %.

**Lemma B (schlechte Blöcke selten), Versuch [S, computergestützt].** Mit der DLR-Schranke $P(S\ \text{besetzt})\le p^{|S|}$, $p=z/(1+z)\le0{,}0734$, und Vereinigung über alle schlechten Paare (Blockkonfiguration, Ringkonfiguration): $P(\text{schlecht})\le0{,}18$ (4×4), $\le0{,}23$ (5×5) ([beweis_box/schranke_schlecht.py](beweis_box/schranke_schlecht.py)); gemessen 0,0036 und 0,0017. Gute Blöcke also streng $\ge77\,\%$. Verbesserungen: (a) Peierls-Summe nur über minimale Sperrmotive (das Ereignis „Komponente von $I$ hat höchstens $s_0$ Elemente“ ist monoton in $B$); (b) schärfere gemeinsame Besetzungsschranken statt $p$ ($\rho_b=0{,}031$ ist um 2,4 kleiner, je Bindung des Motivs) über die Baumrekursion aus Baustein 2.

**Lemma C (Lücke der Hauptkomponente) [S, computergestützt, Gleitkomma].** Für alle vorkommenden Randmuster der 5×5-Box und $N\le4$ hat die größte Komponente der kanonischen Eckschritt-Dynamik die Lücke $\ge0{,}0039$ (4×4: $\ge0{,}017$) ([beweis_box/basisfall.py](beweis_box/basisfall.py)); gewichtet ist sie fast immer $\ge0{,}03$.

**Was fehlt [L].** Der Mehrskalenschritt (grobe Austauschdynamik zwischen guten Blöcken, Behandlung schlechter Gebiete), eine scharfe Fassung von Lemma B, und für (C) die geschlossenen Formen.
- Nachtrag Lemma B (2026-11-04): Peierls-Summe nur über minimale Zeugen $(I,\eta_0)$ (schlecht, aber kein $\eta_0\setminus\{e\}$ schlecht; jede schlechte Realisierung enthält einen, ohne Monotonie): $P(\text{schlecht})\le0{,}076$ (4×4), $\le0{,}066$ (5×5) [S, computergestützt, Gleitkomma], gemessen 0,0036 / 0,0017. Größter Beitrag: ein eingesperrtes Paar mit zwei Sperrern von außen. Der Restverlust steckt in $p=z/(1+z)$ je Bindung statt $\approx\rho_b$; nächster Hebel: gemeinsame Besetzungsschranken über die Baumrekursion (Baustein 2).
- Nachtrag Lemma B, scharf (2026-11-04, [beweis_box/schranke_baum.py](beweis_box/schranke_baum.py)): In der Peierls-Summe über minimale Zeugen statt $p^{|S|}$ das Produkt $\prod_iP(s_i\ \text{besetzt}\mid s_{<i}\ \text{besetzt})$, jeder Faktor streng nach oben durch die Baumrekursion aus Baustein 2 (`strenge_schranke._rek`, Graph ohne die Sperrzonen $X(s_j)$, Intervallrechnung in $z\in[0{,}0765;0{,}0792]$, nach außen gerundet). Ergebnis [S, computergestützt]: $P(\text{schlecht})\le0{,}0073$ (4×4, $D=5$), $\le0{,}0054$ (5×5, $D=4$); gemessen 0,0036 / 0,0017. Gute 5×5-Blöcke also streng $\ge99{,}46\,\%$.

## 26. Mehrskalenschritt für (L$'$): Plan nach Cancrini–Martinelli–Roberto–Toninelli (2026-11-04)

**Literatur [Lit]** (CMP 297 (2010), §4 und §6 gelesen). Hauptsatz: Lücke des Kob–Andersen-Gases in der Box mit Quellen $\gtrsim L^{-2}(\log L)^{-4}$. Für *nicht-kooperative* Modelle genügt nach den Autoren der einfache Weg: Poincaré-Ungleichung für eine Hilfs-Glauber-Dynamik (beim Produktmaß trivial), dann Transport der Glauber-Züge zum Rand über Pfadargumente. Die schwere Maschinerie (renormiertes Modell AKG, Tausch ganzer Blockinhalte $T_e$, Rahmen) brauchen sie nur für das kooperative KA-Modell; dort ist das Blockmaß wieder ein Produkt, sonst wäre $T_e$ nicht maßerhaltend.

**Unser Fall [B, H].** Nach §24–25 ist das Dimer-Gas bei 7/8 nicht-kooperativ: schlechte Stellen endlich, Befreiungsradius $\le2$, gute 5×5-Blöcke streng $\ge99{,}46\,\%$. Plan:
1. *Glauber-Poincaré mit Nebenbedingung* für das Hard-Core-Maß: $\mathrm{Var}(f)\le C\sum_x\mu[c_x\,\mathrm{Var}_x(f)]$, $c_x$ = es gibt einen Pfad guter Blöcke von $x$ zum Rand. Eingänge: Glauber-Mischen unter SSM (Chen–Liu–Vigoda) [Lit], $P(c_x=0)$ klein aus Lemma B und Peierls; zu zeigen: Übertragung der beschränkten Glauber-Ungleichung auf das Gibbs-Maß mit lokaler Nebenbedingung [L].
2. *Pfadargument über gute Blöcke*: Ein Glauber-Zug bei $x$ wird realisiert, indem ein Paar vom Rand-Reservoir Block für Block nach $x$ getragen wird; in jedem guten Block wird der übrige Inhalt danach exakt wiederhergestellt (Hauptkomponente zusammenhängend, Lemma C). Anders als beim Lochhaufen (§17) wird nichts verschoben, die Information je Block bleibt beschränkt. Kosten: Pfadlänge $\sim\ell/\ell_0$, Engpass beschränkt, also $\gamma_\ell\ge\gamma_{\rm aux}/(C\ell^2)$.
3. *Neues Lemma, berechenbar* (nächster Schritt): Transport durch gute Blöcke: In der Vereinigung zweier benachbarter guter Blöcke kann ein am Eingang hinzugefügtes Paar zum Ausgang gebracht werden, mit dem Rest wiederhergestellt; Wahrscheinlichkeit wie Lemma B streng nach unten.
- Transportlemma numerisch (2026-11-04, [beweis_box/transport_mc.py](beweis_box/transport_mc.py), je 40 000 Gleichgewichtslagen) [N]: Transport = Rest innerhalb der Hauptkomponente umordnen, Paar in der Eingangszone (zwei linke Spalten) zufügen, in derselben Komponente mit $N+1$ Paaren zur Ausgangszone tragen, Rest zurückstellen. Gelingt in 99,997 % (6×6; ein Fall nicht in der Hauptkomponente, kein echter Transportfehler), 99,57 % (7×5), 95,7 % (8×4, zu schmal). Nächster Schritt: strenge untere Schranke wie Lemma B (minimale Zeugen und Baumrekursion), braucht eine schnellere Ringaufzählung.
- Transportlemma streng (2026-11-04, [beweis_box/transport_streng.py](beweis_box/transport_streng.py)) [S, computergestützt]: Peierls-Summe über minimale Zeugen $(I,\eta_0)$ (schlecht bei $B(\eta_0)$, bei keinem $B(\eta_0\setminus e)$) mit $p^{N+|\eta_0|}$, dazu $P(N>n_{\max})\le\#\{|I|=n_{\max}+1\}\,p^{n_{\max}+1}$. 6×6, $n_{\max}=6$: $P(\text{Transport scheitert})\le0{,}0066$ (Zeugen 0,0062 aus $1{,}05\cdot10^9$ Zeugen, Rest 0,0004); gemessen $\approx3\cdot10^{-5}$. Beiträge vor allem $N=3$–$5$; bei $N\ge5$ scheitert der Transport meist, weil kein weiteres Paar passt, nicht an getrennten Komponenten. Schärfer mit Baumrekursions-Faktoren statt $p$ (wie Lemma B), dann wohl $<10^{-3}$.
- Transportlemma scharf (2026-11-04, [beweis_box/transport_baum.py](beweis_box/transport_baum.py)) [S, computergestützt]: Gewicht $\prod_iP(s_i\mid s_{<i}\ \text{besetzt})$ (erst $\eta_0$, dann $I$), jeder Faktor aus der Teleskop-Rekursion von Baustein 2 mit drei Knotenzuständen: bekannt sind $N(s)$ und alles außerhalb $A=\bigcup_tX(t)$ ($t$ in Region und Ring, $W\subseteq A$ immer), alle übrigen unbekannt; ein unbekanntes Kind gibt den Faktor $[1/(1+c_{\max}),1]$. Der Faktor hängt dann nur von $(s,W\cap N(s))$ ab (22 Bit) und wird tabelliert (54 201 Rekursionen, $D=4$). Isolierte Bindung: $0{,}0430$ statt $p=0{,}0734$ (voll bekannt $0{,}0364$). Ergebnis 6×6, $n_{\max}=6$: $P(\text{Transport scheitert})\le4{,}8\cdot10^{-4}$, gute 6×6-Regionen also streng $\ge99{,}95\,\%$ (gemessen $\approx3\cdot10^{-5}$).

## 27. Mehrskalenschritt: Gerüst und die eigentliche Lücke (2026-11-04)

**Bedingte Transportschranke [S, computergestützt]** ([beweis_box/transport_baum.py](beweis_box/transport_baum.py) `--bedingt --puffer w`): gleichmäßig in jeder Konfiguration $\xi$ außerhalb von $P=$ Region $\cup$ Ring $\cup$ Puffer (Abstand $\le w$ im Konfliktgraphen; außerhalb sicher entfernt, von $\xi$ sperrbare Knoten unbekannt): $\sup_\xi P(\text{Transport 6×6 scheitert}\mid\xi)\le6{,}1\cdot10^{-4}$ ($w=1$, $|P|=264$), $\le5{,}0\cdot10^{-4}$ ($w=2$, $|P|=424$); ohne Bedingung $4{,}8\cdot10^{-4}$. Ohne Puffer ist die Schranke viel schlechter (4×4: 0,21 statt 0,059), weil leeres Außen die äußeren Ringbindungen wirklich öfter besetzt.

**Gerüst für (L$'$), starke Kontakte.**
1. Glauber-Poincaré gleichmäßig in $\ell$: $\mathrm{Var}(f)\le C_G\sum_b\mu[\mathrm{Var}_b f]$ für das Hard-Core-Maß auf jedem Graphen vom Grad 22 bei $z<\lambda_c(22)$ [Lit: Chen–Liu–Vigoda 2021, spektrale Unabhängigkeit; alternativ Weitz-SSM + Dyer–Sinclair–Vigoda–Weitz 2004].
2. Pfadvergleich (kanonische Pfade): jeder Glauber-Zug bei $b$ als Pfad der offenen Dynamik, Paar vom Rand durch gute Regionen nach $b$ tragen, Rest je Region wiederhergestellt. Last je Übergang $\sim\ell\cdot\ell$, also $\gamma_\ell\ge c/\ell^2$, *wenn* jeder Pfad gut ist.
3. Die Lücke [L, B]: Kanonische Pfade brauchen das Maximum der Last über alle Übergänge. Liegt $b$ in einem großen schlechten Cluster $R$ ($k$ Blöcke), muss der Pfad $R$ umbauen; die Last solcher Übergänge ist $\sim Z_R\approx23^k$ (Zustandssumme eines 6×6-Blocks $\approx23$) und unbeschränkt, weil solche Cluster (selten, aber) vorkommen. Die Wahrscheinlichkeit $\varepsilon$ hilft im Maximum nicht. Ausweg wie bei CMRT: eine *eingeschränkte* Glauber-Poincaré-Ungleichung $\mathrm{Var}(f)\le C\sum_b\mu[c_b\,\mathrm{Var}_bf]$, $c_b=1$ wenn ein guter Weg zum Rand existiert. Für Produktmaße ist das CMRT 2008 (nicht-kooperative KCM haben positive Lücke, Bisektion); für ein Gibbs-Maß mit SSM ist mir kein Satz bekannt (Literatursuche 2026-11-04: nichts; Caputo nennt nicht-Produkt-Fälle ausdrücklich schwierig). Das ist der analytische Kern.
4. Perkolation guter Blöcke: aus der bedingten Schranke nach Liggett–Schonmann–Stacey (1997) Dominanz eines Bernoulli-Feldes, aber mit Verlust $\varepsilon^{1/\Delta}$ ($\Delta\approx20$ Nachbarblöcke mit überlappendem $P$): zu schwach. Besser: gemeinsame Zeugensummen für Blockcluster direkt mit den Baumfaktoren [B, berechenbar].
5. Für die Verkettung nötig: ein *verkettbares* Transportlemma (Paar wartet im Eingang, gehört dabei zum Ring der nächsten Region; Rest exakt wiederhergestellt, solange das Paar in der Region ist). Das bisher berechnete Kriterium (Paar kommt „von außen“, Rest vorher umgeordnet) ist dafür noch nicht genau das Richtige [L, berechenbar].

**Ideen für 3 [H].** (a) Bisektion nach CMRT mit SSM-Fehlertermen: Bedingen auf eine Hälfte ändert das Maß der anderen nur um $e^{-d/\xi}$ in Abstand $d$; Fehler über die Skalen summierbar? (b) Zwei Skalen: Block-Poincaré mit großen Blöcken (SSM, [Lit] Martinelli–Olivieri) und in jedem Block die eingeschränkte Ungleichung bedingt auf das Außen, wo das bedingte Maß wieder Hard-Core mit SSM ist. (c) Gewichtete Pfade (Pfadlänge statt Maximum über Peierls mitteln): geht für kanonische Pfade nicht direkt, aber für den Vergleich über Martingale/Lu–Yau vielleicht.

**Bisektion nach CMRT 2008 (§4, Satz 4.2) für ein Gibbs-Maß [B, Entwurf, 2026-11-05].** Hilfsmodell: Blöcke $x$ mit Inhalt $\omega_x$, Zug „Block $x$ neu aus $\mu(\cdot\mid\omega_{x^c})$ ziehen, falls die orientierten Nachbarn gut sind“, $D_\Lambda(f)=\sum_x\mu[c_x\mathrm{Var}_x f]$. Das Produktmaß geht an drei Stellen ein:
- (P1) Lemma 4.1, Monotonie der Lücke im Volumen ($\mathrm{Var}_V=\mathrm{Var}_\Lambda$ für Funktionen auf $V$). Gebraucht, um von der unregelmäßigen Menge $B_\Gamma$ auf $\Lambda_1$ zu gehen. *Ersatz:* Induktion gleich über alle Teilmengen $V$ von Rechtecken aus $F_k$ und alle Randbedingungen, $\gamma_k:=\sup_{V,\tau}\mathrm{gap}^{-1}$. Die Bisektion teilt $V=V\cap\Lambda_1\cup V\cap\Lambda_2$, $B_\Gamma\subseteq\Lambda_1$ ist dann selbst zulässig. Monotonie wird nicht mehr gebraucht.
- (P2) Satz 4.5, Lücke der Zweiblock-Dynamik $\ge1-\sqrt{\varepsilon}$: nutzt $\pi_1\pi_2f=0$ für disjunkte Blöcke (Unabhängigkeit). Beim Gibbs-Maß sind benachbarte disjunkte Blöcke stark korreliert. *Ersatz:* überlappende Blöcke $A_1=B_1\cup I$ (bedingt erneuert) und $A_2=\Lambda_2\supseteq I\cup J$ (immer), Überlapp $I$ der Breite $\sim\delta_k/2$, die Bedingung $c_1$ = „$J$-gut“ auf einem Streifen $J\subseteq\Lambda_2\setminus I$ rechts von $I$, also messbar bezüglich $A_1^c$ (bleibt beim Erneuern von $A_1$ fest). Unbedingter Teil: Zweiblock-Ungleichung mit Überlapp unter SSM [Lit, Martinelli–Olivieri]. Bedingter Teil: $\mathrm{Var}^\tau_{A_1}(g)$ für $g$ auf $B_1$ hängt von $\tau$ nur über $1\pm C|B_1|e^{-m\delta}$ ab (SSM, Radon-Nikodym), also $\mu[(1-c_1)\mathrm{Var}_{A_1}g]\le\varepsilon(1+\eta)^2\mu[\mathrm{Var}_{A_1}g]$ und Absorption. Ergebnis: Faktor $1+O(\varepsilon_k)+O(l_k^2e^{-m\delta_k})$ je Skala, Produkt konvergent ($\delta_k\sim\sqrt{l_k}$).
- (P3) Gl. (4.3), $\mu(\omega_I)=\mu(\omega_{I\setminus I_\Gamma})\mu(\omega_{I_\Gamma})$: *Ersatz:* DLR. Das Ereignis $\{\Pi_\omega=\Gamma\}$ hängt nicht von $\omega_{J_\Gamma}$ ab (Behauptung 4.7, rein geometrisch), Mittelung über $\omega_{J_\Gamma}$ mit der bedingten Verteilung und Konvexität gibt $\le\mathrm{Var}_{B_\Gamma}(f)$. Behauptung 4.6 (Bedingungen in $B_\Gamma$ wie mit gutem Rand) ist rein geometrisch.

Damit scheint die Bisektion für ein Gibbs-Maß mit SSM für alle Teilgraphen (Weitz) zu tragen; das muss sorgfältig nachgerechnet werden [L, Schreibarbeit].

**Quantitativer Engpass [B].** $\varepsilon_k=P(\text{schlechter Cluster durchquert }J)$ muss in $\delta_k$ exponentiell fallen. Mit der bedingten Blockschranke und grober Behandlung der Abhängigkeit (Teilmenge paarweise getrennter Blöcke, $\ge k/9$ eines $*$-Pfades der Länge $k$) braucht Peierls $8\,\varepsilon^{1/9}<1$, also $\varepsilon\lesssim10^{-8}$; wir haben $5\cdot10^{-4}$. Auswege: (i) gemeinsame minimale Zeugen für ganze Cluster schlechter Blöcke mit Baumfaktoren (berechenbar, Hauptaufwand); (ii) zweistufige Renormierung.

**Verkettbares Transportlemma, Monte Carlo** ([beweis_box/transport_kette_mc.py](beweis_box/transport_kette_mc.py), 40 000 Lagen) [N]: feste Tore (waagrechte Bindungen über den Regionsrand): nur 68,0 % gut (17,4 % kein Transport, 14,7 % kein freies Eingangstor; Einfügen 83 %). Überlappende Regionen (Ausgangszone = Eingangszone der nächsten, Bedingung für *jedes* gültige Eingangspaar, Rest exakt zurück): 89,1 % gut, 5,3 % kein Transport, 5,6 % kein freier Eingang; Einfügen 94 %. Ein 6 breiter Gang ist zu schmal: zwei Paare verriegeln einen 2×6-Streifen. Folgerung: gerade Gänge tragen nicht, das Pfadargument braucht 2D-Wege um schlechte Stellen, also genau die eingeschränkte Ungleichung oben.

**Gibbs-Bisektion ausgeschrieben (2026-11-05)** [B], [beweis_box/bisektion_gibbs.pdf](beweis_box/bisektion_gibbs.pdf): Satz: unter (S) SSM in Radon-Nikodym-Form (aus Weitz über die Kettenregel), (P) $\mu_V^\tau(\text{alle }y\in Y\text{ schlecht})\le\hat\varepsilon^{|Y|}$ und (E) leerer Block gut hat die eingeschränkte Blockdynamik (Block neu ziehen, wenn die NO-Nachbarn gut sind) eine Lücke unabhängig von $V$ und $\tau$, falls $8\hat\varepsilon<1$. Zweiblock-Lemma mit Überlapp: Eigenwerte $\ge1-s_0$, $s_0=\max\{2\sqrt\varepsilon,\sqrt{(16\eta_1+24\eta_2)/3}\}$ ($\eta$ = SSM-Fehler über die Überlappbreite; für $\eta=0$ genau CMRT). Blöcke = Fenster $10\times10$ (Region 6×6 und Ring), dann gilt (P) für beliebige, auch benachbarte Blöcke mit der bedingten Schranke ohne Puffer: $\hat\varepsilon\le0{,}0020$ [S, computergestützt], also $8\hat\varepsilon\le0{,}016$. Offen [L]: Vergleich der Hilfsdynamik (ändert die Paarzahl eines Blocks) mit der echten Dynamik (Paare nur vom Rand); CMRT 2010 nutzen dafür den Tausch von Blockinhalten (Produktmaß).

## 28. Vergleichsschritt und ein kürzerer Weg: Thomson statt Lücke (2026-11-05)

**Zerlegung (a) trägt nicht [B].** Die Hilfsdynamik ändert die Paarzahl eines Blocks; zerlegt man $\mathrm{Var}_x$ in den kanonischen Teil und den Teil der Paarzahl, bleibt der zweite nichtlokal (Paare kommen nur vom Rand). Jede lokale Kompensation ist wertlos: In einem geschlossenen Block ist die Drift der inneren Züge exakt $L_x\tilde X$ ($\tilde X$ = Summe der $x$-Koordinaten), also ein Gradient; die kompensierende Strömung hebt den ganzen Strom auf (das ist die Eichung der geschlossenen Box). Ein lokaler Vergleich Hilfsdynamik → echte Dynamik bräuchte eine erhaltende Hilfsdynamik (Block-Kawasaki mit Bedingung, Gibbs-Maß), also genau das schwere Problem von CMRT 2010 ohne Produktmaß.

**Thomson-Weg [B].** Ziel ist nicht die Lücke, sondern $\rho_s^{\rm Vol}>0$. Dafür:
1. $\rho_s^{\rm Vol}\ge\limsup_\ell\rho_s^{\rm Box}(\ell)$ [S] (leichte Richtung, beweis_box Satz 3.2, unter (W), für $r\le1$).
2. Leitwertform der Box + Thomson (§14 Folgerung 2): für jeden quellenfreien Fluss $\theta$ auf dem Konfigurationsgraphen der Box (Eckschritte und Reservoirschritte) ist $\rho_s^{\rm Box}/t_c\ge\ell^{-2}(\sum\theta\Delta)^2/\sum\theta^2/(\mu q)$.
3. Fluss aus Durchquerungen: zu jeder Konfiguration $D$ Wege guter Blöcke von links nach rechts; je Weg ein Zyklus im Konfigurationsraum (Paar am linken Rand erzeugen, Block für Block tragen, Rest jeweils exakt zurück, rechts vernichten), Netto-$\Delta\approx\ell$.
- Entscheidender Unterschied zur Lücke: Thomson braucht nur die *mittlere* Energie $\sum_e\mu(e)R_e^2$, nicht die maximale Last, und $\theta$ muss nicht jede Konfiguration bedienen. Konfigurationen ohne gute Wege tragen einfach keinen Fluss; seltene teure Stellen zählen mit ihrem Gewicht. Das Max-Last-Problem (§27, Punkt 3) und die ganze Lückenmaschinerie (L$'$), $\kappa$, Bisektion, Vergleich entfallen.
- Skalierung: $\sim\ell/h$ disjunkte Durchquerungen (Menger) mit beschränkter Vielfachheit je Kante gibt $\sum\theta\Delta\sim\ell^2/h$, Energie $\sim\ell^2/h$, also $\rho_s^{\rm Box}/t_c\ge c/h$ unabhängig von $\ell$, mit *expliziter* Konstante.

**Was dafür nötig ist.**
- (T1) Ein fensterlokales Gütekriterium, das verkettbaren Transport in alle Richtungen (auch Abbiegen) und die Übergabe an Nachbarn garantiert.
- (T2) Strenge Schranke $P(\text{schlecht}\mid\text{Außen})$ klein, über Zeugensummen mit Baumfaktoren (Werkzeug vorhanden).
- (T3) Viele disjunkte Durchquerungen guter Blöcke (Menger, Peierls über duale Pfade mit überwiegend schlechten Blöcken).
- (T4) Beschränkte Vielfachheit: Wegfamilie aus dem Gütefeld, das sich zwischen $D$ und Zwischenzuständen nur lokal ändert.
- Engpass: (T1)+(T2). Mit 6×6-Regionen gelingt die verkettete Übergabe nur zu 89 % [N] (§27); für Peierls mit Abhängigkeit bräuchte man streng $\lesssim1\,\%$ Ausfall. Größere Regionen sprengen die 62-Bit-Masken (8×6 hat 82 Bindungen).

**Übergabe-Diagnose, Monte Carlo (2026-11-05, je 1000 Lagen, [beweis_box/transport_kette_mc.py](beweis_box/transport_kette_mc.py) `--zone k --nur_ueberlapp`) [N].**

| Region | Zone | gut (∀e∃f) | kein Transport | kein Eingang | voll verbunden |
|--------|------|------------|----------------|--------------|----------------|
| 6×6    | 2    | 88,6 %     | 5,2 %          | 6,2 %        | 88,6 %         |
| 5×7    | 2    | 92,8 %     | 3,7 %          | 3,5 %        | 91,9 %         |
| 4×9    | 2    | 96,0 %     | 2,6 %          | 1,4 %        | 89,2 %         |
| 6×6    | 3    | 97,2 %     | 1,4 %          | 1,4 %        | 96,9 %         |

Breitere Zonen (3 Spalten, Regionen um 3 versetzt) helfen am meisten; höhere Gänge helfen für die Geradeausfahrt, nicht für „voll verbunden“.

**Die Peierls-Wand kehrt zurück [B].** Für (T3) braucht man Abschätzungen $P(\text{alle Knoten eines Pfades schlecht})$. Die bedingte Schranke gilt pro *Fenster* (Region ∪ Ring); überlappen die Fenster benachbarter Knoten (bei versetzten Regionen um bis zu 3 Knoten), so bleibt nach grober Auswahl getrennter Fenster nur $n/49$ eines Pfades, und Peierls verlangt $\varepsilon\lesssim8^{-49}$. In der Bisektion ging das mit disjunkten Fenstern ($8\hat\varepsilon<1$, $\hat\varepsilon=0{,}002$), weil dort nur ein Einzelfenster-Ereignis nötig war. Die Übergabe zwischen Nachbarn hängt aber zwingend von zwei Fenstern ab. Auswege [H]: (i) Kantenereignisse auf zwei Fenstern, unabhängige Teilmenge $\ge n/7$ eines dualen Pfades, also $\varepsilon_{\rm Kante}\lesssim5\cdot10^{-4}$ (streng); (ii) gemeinsame Zeugensummen für ganze Pfade schlechter Knoten statt Auswahl getrennter Fenster; (iii) Übergabe lockern (Überlappinhalt darf umgeordnet übergeben werden, die nächste Region stellt ihn wieder her).

**Lockere Übergabe, Monte Carlo (2026-11-05, [beweis_box/uebergabe_mc.py](beweis_box/uebergabe_mc.py), 6×6, Überlapp 3 Spalten, 40 000 Kanten) [N].** Übergabezustand: Original außerhalb der Bindungen mit beiden Plätzen im Überlapp, dort ein beliebiger Inhalt mit einem Paar mehr; Kante gut, wenn der Zustand in der Hauptkomponente beider Regionen liegt (verkettbar, da die Überlappzonen disjunkt sind). Ausfall $4{,}2\cdot10^{-3}$ (streng, ein Eingangspaar ∃: 3,9 %), verteilt über $N=2$–$5$, vor allem 3–4. Ziel wären $\approx3\cdot10^{-5}$: es fehlen gut zwei Größenordnungen.

**Schluss (2026-11-05).** (L$'$) bzw. $\rho_s>0$ bleibt eine numerisch sehr gut gestützte Annahme. Der offene Kern ist genau eingegrenzt: entweder der Vergleich Hilfsdynamik → echte Dynamik (Gibbs-Bisektion steht, [B]) oder für den Thomson-Weg eine verkettbare Übergabe mit Ausfall $\lesssim10^{-4}$, was größere Regionen (Masken über 62 Bit) verlangt. Stand im PDF [beweis_box/beweis_box.pdf](beweis_box/beweis_box.pdf), Abschnitt „Auf dem Weg zu (L$'$)“.

**Größere Regionen (2026-11-05, [beweis_box/uebergabe_gross_mc.py](beweis_box/uebergabe_gross_mc.py), gepackte Indizes statt Bitmasken, je 40 000 Kanten) [N].** Lockere Übergabe: 8×6 mit Überlapp 4: Ausfall $4{,}0\cdot10^{-4}$ (16), streng 1,3 %; 6×8 mit Überlapp 3: $3{,}3\cdot10^{-4}$ (13), streng 1,3 % (6×6: $4{,}2\cdot10^{-3}$). Je Größenschritt etwa Faktor 10; für das Ziel $\approx3\cdot10^{-5}$ bräuchte man etwa 8×8. Die strenge Zeugensumme ist bei dieser Größe mit unserer Ringaufzählung nicht machbar (6×6: Ring 76 Bindungen, $2{,}5\cdot10^8$ Ringkonfigurationen; 8×8: Ring ≈ 100 Bindungen).

**8×8 abgebrochen (2026-11-06) [N].** 20 Prozesse, 3,6 h: nur 1405 Kanten (≈190 s je Probe wegen dichter Proben mit 7–8 Paaren, bis 16 GB je Prozess, Speicher voll), kein lockerer Ausfall, streng 0,14 %. Für eine Aussage auf dem Niveau \cdot10^{-5}$ bräuchte man $\sim10^5$ Proben, also Tausende Prozessstunden: nicht sinnvoll.

## 29. Driftfreie Einschränkung von Stufe A? (2026-11-06)

**Frage.** Eine driftfreie Dynamik (Gradient) gäbe $\rho_s=K$ exakt (§14 Folgerung 3, $F=0$) und damit ein strenges $T_{KT}$ ohne Lücke. LP ([gradient_lp.py](gradient_lp.py)): Rate je Eckschritt als Funktion des lokalen Umfelds (Belegung der zweiten Schale um alte und neue Bindung, für Hin- und Rückzug gleich, Gleichverteilung bleibt stationär), Drift in jeder Konfiguration null, $K$ maximal.

**Ergebnis [N].** Torus 10×10 und 12×12:
- Bis 3 Paare: zulässig, nur durch Absenken (Raten $\le1$, freie Züge 1) $K_{\rm neu}/K_{\rm alt}=0{,}982$ (89 von 6068 Mustern auf 0).
- Mit 4 Paaren: unzulässig bei freien Zügen auf 1, auch mit Raten bis 10. Dürfen auch freie Züge sinken: Optimum $K_{\rm neu}/K_{\rm alt}=0{,}0002$, praktisch alles auf 0 (Innere-Punkte-Verfahren, 79 540 Muster, 374 898 Zeilen).

**Schluss [B].** Eine driftfreie Einschränkung mit lokalen Regeln gibt es nicht; das bestätigt das Argument mit dichten Klumpen (Drift im Inneren eines Klumpens lässt sich lokal nicht ausgleichen). Ein strenges $T_{KT}$ über eine Gradient-Variante von Stufe A ist damit nicht zu haben.

## 30. Forschungsbericht: Großwerkzeuge für untere Transportschranken (2026-11-08)

[transport_forschungsbericht.md](transport_forschungsbericht.md). Literaturprüfung (CMRT, Martinelli–Shapira–Toninelli, Shapira, Kawasaki unter Mischung, Bauerschmidt–Bodineau–Dagallier, Nichtgradient, Homogenisierung). Ergebnis: Für die Lücke passt kein Satz; für σ\_∞ > 0 lässt sich Shapiras Beweis von D > 0 für Kob–Andersen (Grobgitter, Variationsformel, Irrfahrt auf Perkolationsclustern) übertragen, wenn man das Produktmaß durch die DLR-Faktorisierung auf festen Stützbindungen ersetzt. Neu streng: Eine Stützbindung ist gleichmäßig im Außen mit Wahrscheinlichkeit ≥ 0,303 frei ([stuetzbindung_frei.py](stuetzbindung_frei.py)), über der Schwelle 0,196 der Platzperkolation bis zum 4. Nachbarn. Offen: Perkolation der Transportkanten (Lemma S7) und das wörtliche Nachrechnen von Shapira §4.

## 31. Zwei-Paar-Relativgraph: exakt lokaler Korrektor (2026-11-08)

[zweipaar_graph/README.md](zweipaar_graph/README.md), Programm [zweipaar_graph/two_pair_graph.py](zweipaar_graph/two_pair_graph.py) (9 automatische Tests, unabhängige Kontrolle auf dem vollen Torus, Steifigkeit gegen §15 bestätigt). Ergebnis: Die Zwei-Paar-Drift d₂ ist Eigenvektor des Relativ-Generators, 𝓛 d₂ = 7 d₂ [S, computergestützt, für ℤ² und alle L ≥ 12], also h₂ = d₂/7 und E₂ = 4/7 exakt für jedes L. Träger: 16 gemischt orientierte Kontaktlagen (±½, ±2½), (±2½, ±½), dieselben Motive wie der Korrektor in §24. Über die Orientierungssektoren summiert ist d̂₂(k) ≡ 0 [B, Symmetrie], die Quelle koppelt nicht an die Diffusionsmode. Paramagnetischer Abzug für zwei Paare exakt (8/7)/|R|. 7/8-Füllung: Der Paarsummen-Korrektor Σ h₂ schließt exakt auf 8×8 (4 Paare, pyamg) 88 % des paramagnetischen Abzugs, im Volumen (MC, L = 64–128) etwa 78 % ohne Fitparameter; freie Zweikörpermotive nur 1 Prozentpunkt mehr [N].

## 32. ODLRO als Teilnahmezahl der bedingten Ein-Paar-Wellenfunktion (2026-11-09)

Anlass: Prüfung eines ChatGPT-Verlaufs zu ODLRO harter Bosonen ([odlro_chatgpt_pruefung.md](odlro_chatgpt_pruefung.md)). **Satz [S, Identität]:** Σ\_{b,b′} ρ₁ = Σ\_E S\_E² mit S\_E = Σ\_{b∈G\_E} ψ(E∪b), also (1 − 23(P−1)/2N)⟨F⟩\_w ≤ n₀ ≤ ⟨F⟩\_w, F\_E = Teilnahmezahl von b ↦ ψ(E∪b) auf dem freien Raum G\_E. ODLRO ⇔ ⟨F⟩\_w bleibt positiv; RK: F ≡ 1 (§10). Exakt 8×8 für H\_A [N] ([zweipaar_graph/odlro_teilnahme_8x8.py](zweipaar_graph/odlro_teilnahme_8x8.py)): ⟨F⟩\_w = 0,92 / 0,86 / 0,73 für 2 / 3 / 4 Paare, min\_E F\_E = 0,65 bei 7/8, während die punktweise Harnack-Konstante max/min ψ(E∪·) bis 116 reicht. Zielaussage für einen Beweis daher ⟨F⟩\_w ≥ c, nicht Harnack. Die Fourierform von „Ansatz A“ ist in Stufe A genau Satz §9.

**Nachtrag §32: F im Volumen, Jastrow-VMC (2026-11-09)** ([../stufe_a_tkt/odlro_vmc.py](../stufe_a_tkt/odlro_vmc.py), Daten `../stufe_a_tkt/daten/odlro_vmc_*.json`). Schätzer: D aus ψ², ein Paar gleichverteilt entfernen (Gewicht w\_E/P exakt). Geprüft: Translationsgeometrie = direkter Aufbau; MC = exakte Aufzählung desselben Jastrow-Zustands auf 8×8 (⟨F⟩ 0,7717, n₀ 0,3779); Jastrow R\_h = 4 überschätzt den exakten H\_A-Grundzustand auf 8×8 um 6 % (F 0,772 gegen 0,728, n₀ 0,378 gegen 0,357). Werte ⟨F⟩\_w / n₀, 2000 Proben, Fehler ≤ 0,0015:

| R\_h       | L = 16        | 32            | 64            | 128           |
|------------|---------------|---------------|---------------|---------------|
| RK (u = 0) | 1 / 0,427     | 1 / 0,407     | 1 / 0,402     | 1 / 0,401     |
| 4          | 0,707 / 0,272 | 0,680 / 0,244 | 0,671 / 0,236 | 0,669 / 0,235 |
| 7          | 0,631 / 0,244 | 0,562 / 0,203 | 0,543 / 0,192 | 0,539 / 0,190 |
| 15         |               | 0,496 / 0,179 | 0,450 / 0,159 | 0,441 / 0,155 |
| 20         |               |               | 0,432 / 0,153 | 0,416 / 0,146 |
| 25         |               |               | 0,423 / 0,149 | 0,401 / 0,141 |
| 30         |               |               |               | 0,389 / 0,137 |

- Bei festem R\_h konvergiert F in L, sobald L ≳ 4–8 R\_h; auch das 1 %-Quantil von F\_E bleibt beschränkt (0,65 / 0,44 / 0,27 für R\_h = 4 / 7 / 15 bei L = 128). Kein Infrarot-Zusammenbruch im Versuchszustand [N].
- F fällt mit der Reichweite langsam, etwas langsamer als 1/ln R\_h (F·ln(R\_h/1,6) = 0,99 → 1,14 für R\_h = 15 → 30). Die Energie legt R\_h nicht fest (flach für 15–25, Baustein 3). Im energetisch guten Bereich ist ⟨F⟩ ≈ 0,40–0,44, also n₀ ≈ 0,14–0,16 im Volumen [N, Versuchszustand].
- **RK im Volumen [B]:** n₀ = ⟨|G\_E|⟩\_w/2N → P\_μ(X(b) leer) = ρ\_b/z\* (DLR), mit z\* ∈ [0,0765; 0,0792] aus Baustein 2 also n₀^RK ∈ [0,395; 0,409], MC 0,4009. Schärfer als die Schranke 0,28 aus §10; offen ist nur die Ensemble-Äquivalenz (kanonischer Torus → Gibbs-Maß).
- Grenze: F ist hier eine Eigenschaft des Versuchszustands und hängt vor allem vom langreichweitigen Teil der Korrelationen ab, den die Energie kaum bestimmt. Für den wahren Grundzustand entscheidet das erst eine direkte Messung, etwa G(L/2) aus Wurm-Läufen (wurm_nb4, Kopf-Schwanz-Histogramm) bei T → 0 [L].
- **Wahrer Grundzustand, Wurm [N] (2026-11-09):** g(r)/g(0) aus den vorhandenen Tief-T-Läufen (T = 0,04/0,055, L ≤ 32, temperaturunabhängig) gibt n₀(H\_A, 7/8) ≈ 0,10 ± 0,01, zwei Schätzer (Plateau-Extrapolation, Profil n₀ + a(1/r + 1/(L−r))) übereinstimmend ([weltlinien/README.md](weltlinien/README.md), [weltlinien/auswertung_null.py](weltlinien/auswertung_null.py)). Also ODLRO bei T = 0 numerisch klar, rund ein Viertel des RK-Werts; der Jastrow-Zustand überschätzt n₀ um etwa die Hälfte. Läufe bei T = 0,02 mit L = 32/48/64 (fertig 2026-11-10): Plateau g(L/2)/g(0) = 0,104 ± 0,008 (L = 48) und 0,101 ± 0,010 (L = 64), Extrapolation n₀ + a/L 0,08 ± 0,02, Profil-Fit 0,10–0,12; zusammen n₀ ≈ 0,09 ± 0,02, verträglich mit 0,10 und klar von null weg. Der thermische Abfall r^{−η} (η ≈ 0,06) ist bis L = 64 nicht sichtbar.
- **Herkunft (2026-11-09):** Der Fall F ≡ 1 ist die Näherung von Penrose und Onsager (Phys. Rev. 104, 576 (1956), Gl. (32)–(35)): Feynmans Grundzustand konstant und positiv auf allen erlaubten Hartkugel-Konfigurationen, Kondensatanteil = Dichte/Aktivität des klassischen Hartkugelgases (Helium: 8 %). n₀^RK = ρ\_b/z\* ist die Gitterfassung dieser Formel, Satz §10 ihre strenge Untergrenze. ⟨F⟩ misst die Abweichung des wahren Grundzustands davon. Die Identität Σρ₁ = Σ\_E |Σ\_b φ\_E(b)|² gilt für jede Wellenfunktion; erst die Positivität (d-Eichung) macht F zu einem reinen Maß der Amplitudenverteilung ohne Vorzeichenauslöschung.
- **Stufe B [B] (2026-11-09):** Positivität gilt nach Satz B ([stufe_b_ergebnisse.md](stufe_b_ergebnisse.md)) für H\_B bei jedem t\_c/J, nicht nur am RK-Punkt (dort ist zusätzlich der Grundzustand exakt bekannt, §20). Das Kriterium überträgt sich: Σ\_{b,b′} ρ₁ = ‖Qψ‖² mit Q = Σ\_b Δ\_d(b); die Umgebung E umfasst P−1 Paare und alle Spins, G\_E die Plätze, auf die das Paar passt und deren Spins antiparallel sind; in der Marshall-Eichung sind die Singulett-Matrixelemente ≥ 0, also keine Auslöschung, und n₀ = ⟨F|G\_E|/2N⟩\_w gilt sinngemäß. Matrixelemente noch nicht einzeln nachgerechnet. Erst B+ verliert die Positivität.
- **RK-Punkt als kritischer Punkt [S/B] (2026-11-09):** Für harte Bosonen ist H\_RK = J(Deg − A) = −2J Σ(S\_x·S\_y − ¼), der Heisenberg-Ferromagnet (Bosonen mit Nächstnachbar-Anziehung V = −2J); Grundzustand = voll polarisiertes Multiplett = Gleichverteilung je Teilchenzahl, ODLRO exakt mit n₀ = (M−N+1)/M, die S²-Identität des ChatGPT-Verlaufs ist dort gesättigt. Am RK-Punkt (harte Bosonen wie Stufe A, §8) ist E₀ linear in der Teilchenzahl: chemisches Potential dichteunabhängig, Kompressibilität unendlich, Grenze zur Phasenseparation, Anregungen ω ∝ k² (z = 2, gemessene Lücke ≈ Dk², §17). Im Phononenbild verschwinden dann die Quantenfluktuationen der Phase (⟨|θ\_k|²⟩ = 1/(2√(κρ\_s) k) → 0): daher F = 1 und der maximale Penrose-Onsager-Wert. Abseits davon (H\_A) endliches κ, Schall mit c = √(ρ\_s/κ), F < 1, n₀ = 0,10; und Störungstheorie um RK startet an einem lückenlosen kritischen Punkt (§10, Baustein 3).
- **Dyson-Lieb-Simon-Kette ohne Reflexionspositivität, Test [N] (2026-11-09):** mit exakter Suszeptibilität χ(k) ([zweipaar_graph/falk_bruch.py](zweipaar_graph/falk_bruch.py), README dort). Harte Bosonen 4×4–8×8: trägt (garantiert 81–99 % von g₀), fehlende Zutat nur die Infrarotschranke. Stufe A 8×8 mit 3 Paaren: garantiert nichts (−2 %), Spielraum je Mode 5,6 % gegen 2 % bei Bosonen; damit für Stufe A ausgeschlossen, unabhängig von χ.
- **Harte Bosonen, Infrarotschranke [N] (2026-11-09):** χ(k)·E(k) ≤ 1 gilt numerisch bei allen Dichten (4×4–8×8), auch ohne Reflexionspositivität; aber die Kette Falk–Bruch + Summenregel + Infrarotschranke ist im unendlichen Volumen nur bei halber Füllung (knapp) positiv und sonst negativ (−0,02 bis −0,04 je Platz). Abseits halber Füllung fehlt also mehr als die Reflexionspositivität ([zweipaar_graph/README.md](zweipaar_graph/README.md), [zweipaar_graph/ir_integral.py](zweipaar_graph/ir_integral.py)).
- **Einseitige Kette [N] (2026-11-09):** Für harte Bosonen ergeben (I) χ⁻(k) ≤ ρ/E(k) und (II) c⁻(k) ≤ Cρ mit C < 2,42 streng ODLRO in 2D (Kette n\_k ≤ √(c⁻χ⁻), Summenregel, J = ∫E^{−1/2} = 0,643); bei kleiner und mittlerer Dichte numerisch mit Abstand erfüllt, (I) in 1D verletzt (Fermi-See-Löcher). Für Stufe A bei 7/8 (8×8) sind beide weit verletzt (8,2 und 6,0; nötig Produkt < 2,4), die Kette mit exakten Werten je k ist aber scharf (0,344 gegen 0,357). Details [../bosonen_odlro/README.md](../bosonen_odlro/README.md).
- **Spektrum des Herausnehmens, Normierung von (I) [N/H] (2026-11-09):** Bei Stufe A (8×8, P = 3) liegt das Maximum von (I) beim kleinsten k: sauberes Phonon (Z = 0,998, ε\_h = 1,44·E), aber n\_k/ρ\_b = 9,8. Bei P = 4 (7/8) ebenso (Z = 0,97, n\_k/ρ\_b = 12,5). Absolut ist χ⁻E = 0,16 (P = 3) bzw. 0,26 (7/8), wie in 1D (0,14–0,18) und nahe dem Bogoliubov-Wert 1/4 bzw. f₀/(4f\_s) (Josephson). Im Phononbereich hängt χ⁻E nicht von der Dichte ab. (I) mit ρ auf der rechten Seite ist deshalb falsch normiert und bei kleiner Dichte im Volumen verletzt; Stufe A ist nur wegen ρ\_b ≈ 0,03 auffällig. Nötig sind k-abhängige Schranken (Kennedy–Lieb–Shastry-artig); Details [../bosonen\_odlro/README.md](../bosonen_odlro/README.md).
