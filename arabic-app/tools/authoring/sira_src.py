#!/usr/bin/env python3
"""sira_src.py <cache dir> [<out file>] — build research/sources/al-sira-al-nabawiyya-nadwi-src.txt (v359-S) from the cached
Shamela pages of book 9914 (p1.html … pN.html, one per Shamela page, fetched one at a time and never altered). Run with
`python3 -I`.

al-Nadwī, «السيرة النبوية» (Abū al-Ḥasan ʿAlī al-Ḥasanī al-Nadwī, 1333–1420 AH), Dār Ibn Kathīr, 12th ed. 2004, notes by
Sayyid ʿAbd al-Mājid al-Ghawrī. The text is Shamela's, unchanged except that HTML is stripped and runs of spaces are folded.
Each page, in the house format:
    === p. <shamela page> (<printed page>) [<section heading>] ===
    <the matn's paragraphs>
    --- hashiya ---
    <the editor's notes, if the page has any — another man's work: NEVER authored>
The printed page is the title's «ص N» (the book is one volume). Pages not yet in the cache are listed on stdout, so the
file can be rebuilt when the download is complete.
"""
import sys, re, html, os

D = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../research/sources/al-sira-al-nabawiyya-nadwi-src.txt')
HEAD = ('al-Nadwī, «السيرة النبوية» لأبي الحسن علي الحسني الندوي (١٣٣٣–١٤٢٠ هـ)، دار ابن كثير، ط ١٢، ٢٠٠٤، '
        'تعليق سيد عبد الماجد الغوري — Shamela book 9914, https://shamela.ws/book/9914')


def clean(x):
    x = re.sub(r'<a href="#p\d+" class="btn_tag[^>]*>.*?</a>', '', x, flags=re.S)
    x = re.sub(r'<br\s*/?>', '\n', x); x = re.sub(r'<[^>]+>', '', x); x = html.unescape(x).replace('\xa0', ' ')
    return '\n'.join(re.sub(r'[ \t]+', ' ', l).strip() for l in x.split('\n')).strip()


pages = sorted(int(m.group(1)) for f in os.listdir(D) for m in [re.match(r'p(\d+)\.html$', f)] if m)
LAST = pages[-1] if pages else 0
out = ['# ' + HEAD, '# Shamela pages 1-%d as Shamela gives them; matn first, then «--- hashiya ---» (the editor\'s notes, never authored).' % LAST,
       '# Header: === p. <shamela page> (<printed page>) [<section>] ===. Built by tools/authoring/sira_src.py.', '']
miss = []
for p in range(1, LAST + 1):
    f = os.path.join(D, 'p%d.html' % p)
    if not os.path.exists(f): miss.append(p); continue
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<div class="nass[^"]*"[^>]*>(.*?)</div>', s, re.S)
    if not m: miss.append(p); continue
    t = re.search(r'<title>(.*?)</title>', s, re.S); title = html.unescape(t.group(1)) if t else ''
    pp = re.search(r'ص\s*(\d+)', title); printed = pp.group(1) if pp else '?'
    parts_t = [x.strip() for x in title.split(' - ')]
    sec = parts_t[-2] if len(parts_t) >= 3 and 'المكتبة الشاملة' in parts_t[-1] else ''
    body = m.group(1); parts = body.split('<hr>', 1)
    matn = [clean(x) for x in re.findall(r'<p(?: [^>]*)?>(.*?)</p>', parts[0], re.S)]
    ham = [clean(x) for x in re.findall(r'<p class="hamesh">(.*?)</p>', parts[1], re.S)] if len(parts) > 1 else []
    out.append('=== p. %d (%s)%s ===' % (p, printed, (' [' + sec + ']') if sec else ''))
    out += [x for x in matn if x]
    if any(ham): out.append('--- hashiya ---'); out += [x for x in ham if x]
    out.append('')
open(OUT, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(os.path.basename(OUT), 'pages', LAST, 'missing', miss[:10], len(miss), 'bytes', os.path.getsize(OUT))
