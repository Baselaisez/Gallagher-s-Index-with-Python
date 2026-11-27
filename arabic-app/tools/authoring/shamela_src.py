#!/usr/bin/env python3
"""shamela_src.py <pages dir> <out file> <header line> — the cached Shamela pages (p<N>.html) as one text in the house format:
=== p. <shamela page> (<printed page>) [<section>] ===, the matn's paragraphs, then «--- hashiya ---» and the notes. Verbatim."""
import re, html, sys, os
D, OUT, HEAD = sys.argv[1], sys.argv[2], sys.argv[3]
def txt(x):
    x = re.sub(r'<a [^>]*class="btn_tag[^>]*>.*?</a>', '', x, flags=re.S)
    x = re.sub(r'<br\s*/?>', '\n', x)
    x = html.unescape(re.sub(r'<[^>]+>', '', x))
    return re.sub(r'[ \t ]+', ' ', x).strip()
out = [HEAD, ""]; n = 0
pages = sorted((int(f[1:-5]) for f in os.listdir(D) if re.fullmatch(r'p\d+\.html', f)))
for p in pages:
    s = open(f"{D}/p{p}.html", encoding="utf-8", errors="ignore").read()
    m = re.search(r'<div class="nass[^"]*"[^>]*data-page-num="([^"]*)"[^>]*>(.*?)</div>\s*<div id="appended_pages">', s, re.S)
    if not m: continue
    t = re.search(r'<title>(.*?)</title>', s, re.S); t = html.unescape(t.group(1)) if t else ""
    parts = [x.strip() for x in t.split(" - ")]
    sec = parts[-2] if len(parts) >= 4 else ""
    vol = re.match(r'ج(\S+)', parts[0]) if parts else None
    pr = (vol.group(1) + ":" if vol else "") + m.group(1)
    body = m.group(2)
    hs = re.split(r'<hr[^>]*>', body, maxsplit=1)
    paras = [txt(x) for x in re.findall(r'<p[^>]*>(.*?)</p>', hs[0], re.S)]
    out.append(f"=== p. {p} ({pr}) [{sec}] ===")
    out += [x for x in paras if x]
    if len(hs) > 1:
        fn = [txt(x) for x in re.findall(r'<p[^>]*>(.*?)</p>', hs[1], re.S)]
        fn = [x for x in fn if x]
        if fn: out.append("--- hashiya ---"); out += fn
    out.append(""); n += 1
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print(n, "pages ->", OUT, os.path.getsize(OUT))
