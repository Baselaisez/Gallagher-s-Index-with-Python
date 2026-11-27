#!/usr/bin/env python3
"""tabaqat_src.py [cache dir] [out file] — build research/sources/tabaqat-ibn-sad-src.txt from the cached Shamela pages of
book 1686, «الطبقات الكبرى» لابن سعد (ت ٢٣٠ هـ), ط دار الكتب العلمية ١٩٩٠، تحقيق محمد عبد القادر عطا (v358-T).

Run with `python3 -I` (the cached html is downloaded data). Re-runnable while the pages are still arriving: it takes every
page present, in Shamela order, and lists the gaps. The text is Shamela's, unchanged, except that HTML is stripped and runs of
spaces are folded (the converter of tools/sources/shamela_src.py, with the book's sections named). Each page:
    === p. <shamela page> (<vol>:<printed page>) [<section>] ===
    <the matn's paragraphs>
    --- hashiya ---
    <the editor's notes, if the page has any>
Sections by Shamela page: مقدمة التحقيق 1 · السيرة النبوية 15 · الصحابة 687 · التابعون 1431 · النساء 2670.
"""
import sys, re, html, os, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
D = sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-0/-home-user-Gallagher-s-Index-with-Python/612c64cf-e6b9-547d-9c53-f32b7b6377b6/scratchpad/newsrc/dl/1686"
OUT = sys.argv[2] if len(sys.argv) > 2 else str(ROOT / "research/sources/tabaqat-ibn-sad-src.txt")
SECTIONS = [(1, "مقدمة التحقيق"), (15, "السيرة النبوية"), (687, "الصحابة"), (1431, "التابعون"), (2670, "النساء")]
def section(p): return [n for a, n in SECTIONS if p >= a][-1]
def clean(x):
    x = re.sub(r'<a href="#p\d+" class="btn_tag[^>]*>.*?</a>', '', x, flags=re.S)
    x = re.sub(r'<br\s*/?>', '\n', x); x = re.sub(r'<[^>]+>', '', x); x = html.unescape(x).replace('\xa0', ' ')
    return '\n'.join(re.sub(r'[ \t]+', ' ', l).strip() for l in x.split('\n')).strip()
pages = sorted(int(m.group(1)) for f in os.listdir(D) for m in [re.match(r'p(\d+)\.html$', f)] if m)
LAST = pages[-1] if pages else 0
out = ['# «الطبقات الكبرى» لابن سعد (ت ٢٣٠ هـ)، ط دار الكتب العلمية، بيروت ١٩٩٠، تحقيق محمد عبد القادر عطا — Shamela book 1686 (https://shamela.ws/book/1686).',
       '# Shamela pages 1-%d as Shamela gives them, unvowelled except where the e-text vowels (the Qurʾān); matn first, then «--- hashiya ---».' % LAST,
       '# Header: === p. <shamela page> (<vol>:<printed page>) [<section>] ===. Built by tools/authoring/tabaqat_src.py (python3 -I).', '']
miss, bad = [], []
have = set(pages)
for p in range(1, LAST + 1):
    if p not in have: miss.append(p); continue
    s = open(os.path.join(D, 'p%d.html' % p), encoding='utf-8').read()
    m = re.search(r'<div class="nass[^"]*" data-page-id="(\d+)" data-page-num="(\d+)">(.*?)</div>\s*<div id="appended_pages">', s, re.S)
    if not m: bad.append(p); continue
    t = re.search(r'<title>(.*?)</title>', s, re.S); title = html.unescape(t.group(1)) if t else ''
    v = re.search(r'ج\s*(\d+)\s*-\s*ص', title); vol = v.group(1) if v else '1'
    body = m.group(3); parts = body.split('<hr>', 1)
    matn = [clean(x) for x in re.findall(r'<p(?: [^>]*)?>(.*?)</p>', parts[0], re.S)]
    ham = [clean(x) for x in re.findall(r'<p class="hamesh">(.*?)</p>', parts[1], re.S)] if len(parts) > 1 else []
    out.append('=== p. %d (%s:%s) [%s] ===' % (p, vol, m.group(2), section(p)))
    out += [x for x in matn if x]
    if any(ham): out.append('--- hashiya ---'); out += [x for x in ham if x]
    out.append('')
open(OUT, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(os.path.basename(OUT), 'last page', LAST, 'missing', len(miss), miss[:10], 'unparsed', bad[:10], 'bytes', os.path.getsize(OUT))
