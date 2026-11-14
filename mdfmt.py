#!/usr/bin/env python3
"""Markdown im Stil des iPad-Editors prüfen und Tabellen auffüllen.

Aufruf: python3 mdfmt.py datei.md [weitere.md] [--schreiben]
- Tabellen: Spalten auf gleiche Breite auffüllen; Breite = Codepunkte ohne kombinierende Zeichen (μ̄, Γ̂ zählen 1).
  Ohne --schreiben wird nur gemeldet. Nur auf Dateien mit --schreiben anwenden, deren Tabellen man selbst geändert hat.
- Prüfungen: Unterstriche ohne Backslash im Fließtext, ungerade Zahl einzelner Sterne, Liste ohne Leerzeile davor.
"""
import re, sys, unicodedata

def breite(t):
    """Codepunkte ohne kombinierende Zeichen (so füllt der iPad-Editor auf)."""
    return sum(1 for c in t if not unicodedata.combining(c))

def ljust(t, w):
    return t + ' ' * (w - breite(t))

def zellen(zeile):
    inner = zeile.strip()
    assert inner.startswith('|') and inner.endswith('|'), zeile
    return [c.strip() for c in re.split(r'(?<!\\)\|', inner[1:-1])]

def pad_tabellen(lines):
    out, i, geaendert = [], 0, 0
    fence = False
    while i < len(lines):
        if lines[i].lstrip().startswith('```'):
            fence = not fence
        if not fence and lines[i].startswith('|'):
            j = i
            while j < len(lines) and lines[j].startswith('|'):
                j += 1
            rows = [zellen(l) for l in lines[i:j]]
            ncol = max(len(r) for r in rows)
            if not all(len(r) == ncol for r in rows):          # uneinheitliche Tabelle: nicht anfassen
                print(f'Zeile {i + 1}: Tabelle mit ungleichen Spaltenzahlen, unverändert gelassen')
                out += lines[i:j]
                i = j
                continue
            sep = [k for k, r in enumerate(rows) if all(re.fullmatch(r':?-+:?', c) for c in r)]
            w = [max(breite(r[c]) for k, r in enumerate(rows) if k not in sep) for c in range(ncol)]
            w = [max(x, 3) for x in w]
            neu = []
            for k, r in enumerate(rows):
                if k in sep:
                    neu.append('|' + '|'.join('-' * (w[c] + 2) for c in range(ncol)) + '|')
                else:
                    neu.append('| ' + ' | '.join(ljust(r[c], w[c]) for c in range(ncol)) + ' |')
            geaendert += sum(a != b for a, b in zip(neu, lines[i:j]))
            out += neu
            i = j
        else:
            out.append(lines[i]); i += 1
    return out, geaendert

def pruefe(lines, name):
    fence = False
    probleme = 0
    for nr, l in enumerate(lines, 1):
        if l.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        t = re.sub(r'`[^`]*`', '', l)                 # Inline-Code
        t = re.sub(r'\]\([^)]*\)', ']', t)            # Linkziele
        for m in re.finditer(r'(?<!\\)_', t):
            probleme += 1
            print(f'{name}:{nr}: Unterstrich ohne \\: …{t[max(0, m.start() - 25):m.start() + 15]}…')
        t2 = t.replace('\\*', '')
        t2 = re.sub(r'\*\*', '', t2)
        if t2.count('*') % 2:
            probleme += 1
            print(f'{name}:{nr}: ungerade Zahl einzelner Sterne: {l[:90]}')
        if re.match(r'\s*(- |\d+\. )', l) and nr >= 2:
            v = lines[nr - 2]
            if v.strip() and not re.match(r'\s*(- |\d+\. )', v) and not v.lstrip().startswith('```') and not v.startswith('   ') and not v.startswith('  '):
                probleme += 1
                print(f'{name}:{nr}: Liste ohne Leerzeile davor: {l[:70]}')
    if fence:
        probleme += 1
        print(f'{name}: Codeblock nicht geschlossen')
    return probleme

if __name__ == '__main__':
    schreiben = '--schreiben' in sys.argv
    nur_ab = None
    for fn in [a for a in sys.argv[1:] if not a.startswith('--')]:
        s = open(fn, encoding='utf-8').read()
        lines = s.split('\n')
        neu, g = pad_tabellen(lines)
        pr = pruefe(neu, fn.split('/')[-1])
        print(f'{fn.split("/")[-1]}: {g} Tabellenzeilen neu aufgefüllt, {pr} Auffälligkeiten')
        if schreiben and g:
            open(fn, 'w', encoding='utf-8').write('\n'.join(neu))
