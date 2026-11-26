# build research/sources/insaf-ibn-al-anbari-src.txt from the cached Shamela pages (run with python3 -I)
import sys, re, html, os
D, OUT, LAST = sys.argv[1], sys.argv[2], int(sys.argv[3])
def clean(x):
    x = re.sub(r'<a href="#p\d+" class="btn_tag[^>]*>.*?</a>', '', x, flags=re.S)
    x = re.sub(r'<br\s*/?>', '\n', x); x = re.sub(r'<[^>]+>', '', x); x = html.unescape(x)
    x = x.replace(' ', ' ')
    return '\n'.join(re.sub(r'[ \t]+', ' ', l).strip() for l in x.split('\n')).strip()
out = ["# al-Insaf fi masa'il al-khilaf — Ibn al-Anbari (d. 577), with M. Muhyi al-Din Abd al-Hamid's hashiya «al-Intisaf min al-Insaf».",
       "# Shamela book 7362 (al-Maktaba al-Asriyya, 1st ed. 1424/2003), pages 1-%d as Shamela gives them; matn first, then «--- hashiya ---»." % LAST,
       "# Header: === p. <shamela page> (<vol>:<printed page>) ===. Text is Shamela's, unchanged except HTML stripped and whitespace folded.", ""]
miss = []
for p in range(1, LAST + 1):
    f = os.path.join(D, 'p%d.html' % p)
    if not os.path.exists(f): miss.append(p); continue
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<div class="nass[^"]*" data-page-id="(\d+)" data-page-num="(\d+)">(.*?)</div>\s*<div id="appended_pages">', s, re.S)
    if not m: miss.append(p); continue
    body = m.group(3)
    parts = body.split('<hr>', 1)
    matn = [clean(x) for x in re.findall(r'<p(?: [^>]*)?>(.*?)</p>', parts[0], re.S)]
    ham = [clean(x) for x in re.findall(r'<p class="hamesh">(.*?)</p>', parts[1], re.S)] if len(parts) > 1 else []
    vol = 1 if p < 338 else 2
    out.append('=== p. %d (%d:%s) ===' % (p, vol, m.group(2)))
    out += [x for x in matn if x]
    if any(ham): out.append('--- hashiya ---'); out += [x for x in ham if x]
    out.append('')
open(OUT, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('pages', LAST, 'missing', miss)
