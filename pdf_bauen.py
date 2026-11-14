#!/usr/bin/env python3
"""Baut die PDFs des Projekts.

  tutorial  tutorial_beweis_verduennt.md  →  tutorial_beweis_verduennt.pdf
  gesamt    beweis_gesamt_vorspann.md und alle Anhänge in der Reihenfolge des Lesewegs
            →  beweis_verduennt_gesamt.pdf (Arbeitsfassung zum Gegenlesen)
  bilanz    beweis_verlustbilanz.md  →  beweis_verlustbilanz.pdf (Beweisweg mit Verlustbilanz)

Kette: pandoc (Markdown → HTML, Bilder eingebettet) → Nachbearbeitung (Indizes _x, _{..} und Exponenten ^x, ^{..}
im Fließtext als <sub>/<sup>, Dateinamen geschützt) → Chrome headless (Druck nach PDF, Lesezeichen aus den
Überschriften). Absätze, die mit *Frühere Fassung* beginnen, werden grau gesetzt. Im Gesamtband zeigen Verweise
auf mitgedruckte Anhänge auf deren Anfang; andere Verweise auf lokale Dateien bleiben als Text stehen.

Aufruf: python3 pdf_bauen.py [tutorial] [gesamt] [bilanz]        (ohne Angabe: alle drei)
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
PANDOC = shutil.which('pandoc') or '/home/detlef/anaconda3/envs/NetKet/bin/pandoc'
CHROME = shutil.which('google-chrome') or shutil.which('chromium')

GESAMT = ['anhang_zweites_moment.md', 'anhang_buchfuehrung.md', 'satz_3_9_dichteschranken.md',
          'anhang_gegenluecke.md', 'anhang_feinskala.md', 'anhang_unzugaenglich.md', 'anhang_lochstueck.md',
          'anhang_einfuegen.md', 'anhang_schleifen.md', 'anhang_kern.md', 'anhang_ausweichen.md']

STIL = """
@page { size: A4; margin: 18mm 17mm 20mm 17mm;
  @bottom-center { content: counter(page) " / " counter(pages); font-family: "DejaVu Sans"; font-size: 8pt; color: #666; } }
html { font-family: "DejaVu Serif", "Noto Serif", serif; font-size: 10pt; line-height: 1.42; color: #111; }
body { margin: 0; }
h1 { font-family: "DejaVu Sans", sans-serif; font-size: 17pt; margin: 0 0 6pt; line-height: 1.25; }
h2 { font-family: "DejaVu Sans", sans-serif; font-size: 13pt; margin: 18pt 0 6pt; border-bottom: 0.6pt solid #999;
  padding-bottom: 2pt; break-after: avoid; }
h3 { font-family: "DejaVu Sans", sans-serif; font-size: 11pt; margin: 12pt 0 4pt; break-after: avoid; }
h4 { font-family: "DejaVu Sans", sans-serif; font-size: 10pt; margin: 10pt 0 3pt; break-after: avoid; }
h1 + p { color: #444; font-size: 9pt; }
p { margin: 4pt 0 6pt; text-align: left; orphans: 3; widows: 3; }
ul, ol { margin: 3pt 0 6pt; padding-left: 18pt; }
li { margin: 2pt 0; }
pre { font-family: "DejaVu Sans Mono", "Noto Mono", monospace; font-size: 7.9pt; line-height: 1.35; background: #f4f4f1;
  border-left: 2pt solid #b9b9b0; padding: 5pt 8pt; margin: 5pt 0 8pt; white-space: pre-wrap; break-inside: avoid; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.6pt; }
table { border-collapse: collapse; width: 100%; font-size: 8.3pt; line-height: 1.3; margin: 5pt 0 9pt; break-inside: auto; }
th, td { border: 0.5pt solid #bbb; padding: 2.5pt 4pt; vertical-align: top; text-align: left; }
th { background: #ecece6; font-family: "DejaVu Sans", sans-serif; font-weight: bold; }
tr { break-inside: avoid; }
strong { font-weight: bold; }
blockquote { margin: 5pt 0 8pt; padding: 3pt 8pt; border-left: 2pt solid #d0a060; background: #fbf6ec; }
img { display: block; max-width: 100%; margin: 8pt auto 2pt; break-inside: avoid; }
p:has(> img) { break-after: avoid; margin-bottom: 0; }
.alt, .alt * { color: #777 !important; }
.alt { border-left: 2pt solid #ddd; padding-left: 6pt; }
"""

STIL_GESAMT = """
h1 { break-before: page; }
header#title-block-header { margin: 30mm 0 10mm; }
header#title-block-header h1.title { font-size: 21pt; }
header#title-block-header p.subtitle { font-family: "DejaVu Sans", sans-serif; font-size: 12pt; color: #444; }
nav#TOC { font-family: "DejaVu Sans", sans-serif; font-size: 8.4pt; line-height: 1.3; }
nav#TOC ul { list-style: none; padding-left: 12pt; margin: 0; }
nav#TOC > ul { padding-left: 0; }
nav#TOC > ul > li { margin-top: 5pt; font-weight: bold; }
nav#TOC > ul > li li { font-weight: normal; margin: 0.5pt 0; }
nav#TOC a { color: #111; text-decoration: none; }
a { color: #1a4f8a; text-decoration: none; }
"""

FILTER = r"""
local ziele = {}
for z in string.gmatch(os.getenv('PDF_ZIELE') or '', '[^,]+') do ziele[z] = true end

function Link(el)
  if el.target:match('^https?://') or el.target:match('^#') then return el end
  local datei = el.target:match('^([^#]+%.md)')
  if datei and ziele[datei] then
    el.target = '#' .. (datei:gsub('%.md$', ''))
    return el
  end
  return el.content
end

local function alt(bl)
  local c = bl.content
  if #c > 0 and (c[1].t == 'Emph' or c[1].t == 'Strong') then
    if pandoc.utils.stringify(c[1]):match('^Frühere Fassung') then
      return pandoc.Div({bl}, pandoc.Attr('', {'alt'}))
    end
  end
end
Para = alt
Plain = alt
"""

DATEI = re.compile(r'\b[\w\-]+\.(?:py|md|json|txt|png|pdf)\b|\bsatz_3_9\b')


def nachbearbeiten(html):
    """Indizes und Exponenten im Fließtext als <sub>/<sup>; Formelblöcke ohne Skizzenzeichen enger."""
    teile = re.split(r'(<[^>]+>)', html)
    in_pre = 0

    def text(t):
        schutz = []

        def merke(m):
            schutz.append(m.group(0))
            return f'\x00{len(schutz) - 1}\x00'
        t = DATEI.sub(merke, t)
        alt = None
        while alt != t:
            alt = t
            t = re.sub(r'_\{([^{}]*)\}', r'<sub>\1</sub>', t)
            t = re.sub(r'\^\{([^{}]*)\}', r'<sup>\1</sup>', t)
        t = re.sub(r'(?<=[^\s_])_([A-Za-z0-9α-ωΑ-Ωϑ′]+)', r'<sub>\1</sub>', t)
        t = re.sub(r'(?<=[^\s^])\^([A-Za-z0-9α-ωΑ-Ωϑ′−]+)', r'<sup>\1</sup>', t)
        return re.sub(r'\x00(\d+)\x00', lambda m: schutz[int(m.group(1))], t)

    aus = []
    for s in teile:
        if s.startswith('<'):
            if re.match(r'<(pre|code)\b', s):
                in_pre += 1
            elif re.match(r'</(pre|code)>', s):
                in_pre -= 1
            aus.append(s)
        elif in_pre:
            zeilen = s.split('\n')
            if not any(c in s for c in '●○↖'):
                zeilen = [re.sub(r' {6,}', '     ', z) for z in zeilen]
            aus.append('\n'.join(zeilen))
        else:
            aus.append(text(s))
    return ''.join(aus)


def bauen(md_text, ziel_pdf, meta, stil, ziele=(), toc=False):
    with tempfile.TemporaryDirectory() as tmp:
        md = os.path.join(tmp, 'ein.md')
        css = os.path.join(tmp, 'stil.css')
        lua = os.path.join(tmp, 'filter.lua')
        roh = os.path.join(tmp, 'roh.html')
        html = os.path.join(tmp, 'seite.html')
        pdf = os.path.join(tmp, 'aus.pdf')
        open(md, 'w', encoding='utf-8').write(md_text)
        open(css, 'w', encoding='utf-8').write(stil)
        open(lua, 'w', encoding='utf-8').write(FILTER)
        befehl = [PANDOC, md, '-f',
                  'markdown-superscript-subscript-tex_math_dollars-raw_tex-raw_html-smart-citations-implicit_figures',
                  '-t', 'html5', '-s', '--embed-resources', f'--resource-path={HIER}', f'--lua-filter={lua}',
                  f'--css={css}', '--metadata', 'lang=de', '-o', roh]
        for k, v in meta.items():
            befehl += ['--metadata', f'{k}={v}']
        if toc:
            befehl += ['--toc', '--toc-depth=2']
        umg = dict(os.environ, PDF_ZIELE=','.join(ziele))
        subprocess.run(befehl, check=True, env=umg)
        open(html, 'w', encoding='utf-8').write(nachbearbeiten(open(roh, encoding='utf-8').read()))
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                        '--generate-pdf-document-outline', f'--print-to-pdf={pdf}', 'file://' + html],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=600)
        shutil.copy(pdf, ziel_pdf)
    print('geschrieben:', os.path.basename(ziel_pdf))


def tutorial():
    md = open(os.path.join(HIER, 'tutorial_beweis_verduennt.md'), encoding='utf-8').read()
    bauen(md, os.path.join(HIER, 'tutorial_beweis_verduennt.pdf'),
          {'pagetitle': 'Tutorial-Beweis verdünnte Bosonen'}, STIL)


def bilanz():
    md = open(os.path.join(HIER, 'beweis_verlustbilanz.md'), encoding='utf-8').read()
    bauen(md, os.path.join(HIER, 'beweis_verlustbilanz.pdf'), {'pagetitle': 'Beweisweg mit Verlustbilanz'}, STIL)


def gesamt():
    teile = [open(os.path.join(HIER, 'beweis_gesamt_vorspann.md'), encoding='utf-8').read()]
    for datei in GESAMT:
        zeilen = open(os.path.join(HIER, datei), encoding='utf-8').read().split('\n')
        assert zeilen[0].startswith('# '), datei
        zeilen[0] += ' {#' + datei[:-3] + '}'
        teile.append('\n'.join(zeilen))
    bauen('\n\n'.join(teile), os.path.join(HIER, 'beweis_verduennt_gesamt.pdf'),
          {'title': 'Kondensat im verdünnten 2D-Gitter-Bosegas: der Beweis mit allen Anhängen',
           'subtitle': 'Arbeitsfassung zum Gegenlesen', 'toc-title': 'Inhalt'},
          STIL + STIL_GESAMT, ziele=GESAMT, toc=True)


if __name__ == '__main__':
    wahl = sys.argv[1:] or ['tutorial', 'gesamt', 'bilanz']
    for w in wahl:
        {'tutorial': tutorial, 'gesamt': gesamt, 'bilanz': bilanz}[w]()
