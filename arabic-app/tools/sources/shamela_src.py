#!/usr/bin/env python3
"""shamela_src.py <cache dir> <out file> <last page> <header line> — build a research/sources text from cached Shamela
pages (p1.html … pN.html, one per Shamela page, fetched one at a time and never altered). Run with `python3 -I`.
The text is Shamela's, unchanged except that HTML is stripped and runs of spaces are folded. Each page:
    === p. <shamela page> (<vol>:<printed page>) [<section heading>] ===
    <the matn's paragraphs>
    --- hashiya ---
    <the editor's notes, if the page has any>
"""
import sys, re, html, os
D, OUT, LAST, HEAD = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
def clean(x):
    x = re.sub(r'<a href="#p\d+" class="btn_tag[^>]*>.*?</a>', '', x, flags=re.S)
    x = re.sub(r'<br\s*/?>', '\n', x); x = re.sub(r'<[^>]+>', '', x); x = html.unescape(x).replace(' ', ' ')
    return '\n'.join(re.sub(r'[ \t]+', ' ', l).strip() for l in x.split('\n')).strip()
out = ['# ' + HEAD, '# Shamela pages 1-%d as Shamela gives them; matn first, then «--- hashiya ---».' % LAST,
       '# Header: === p. <shamela page> (<vol>:<printed page>) [<section>] ===. Built by tools/sources/shamela_src.py.', '']
miss = []
for p in range(1, LAST + 1):
    f = os.path.join(D, 'p%d.html' % p)
    if not os.path.exists(f): miss.append(p); continue
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<div class="nass[^"]*" data-page-id="(\d+)" data-page-num="(\d+)">(.*?)</div>\s*<div id="appended_pages">', s, re.S)
    if not m: miss.append(p); continue
    t = re.search(r'<title>(.*?)</title>', s, re.S); title = html.unescape(t.group(1)) if t else ''
    v = re.search(r'ج\s*(\d+)\s*-\s*ص', title); vol = v.group(1) if v else '1'
    parts_t = [x.strip() for x in title.split(' - ')]
    sec = parts_t[-2] if len(parts_t) >= 3 and 'المكتبة الشاملة' in parts_t[-1] else ''
    body = m.group(3); parts = body.split('<hr>', 1)
    matn = [clean(x) for x in re.findall(r'<p(?: [^>]*)?>(.*?)</p>', parts[0], re.S)]
    ham = [clean(x) for x in re.findall(r'<p class="hamesh">(.*?)</p>', parts[1], re.S)] if len(parts) > 1 else []
    out.append('=== p. %d (%s:%s)%s ===' % (p, vol, m.group(2), (' [' + sec + ']') if sec else ''))
    out += [x for x in matn if x]
    if any(ham): out.append('--- hashiya ---'); out += [x for x in ham if x]
    out.append('')
open(OUT, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(os.path.basename(OUT), 'pages', LAST, 'missing', miss[:10], len(miss), 'bytes', os.path.getsize(OUT))
