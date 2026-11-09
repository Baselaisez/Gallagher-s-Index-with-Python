#!/usr/bin/env python3
"""pubsplit.py <reader.html> <outdir> — the artifact copy of the reader with its __DATA_START__…__DATA_END__ block moved
into outdir/data/d1.js (const STORIES = first packages), d2.js… (STORIES.push(...)), dN.js (GRAMMAR, models, REF_GROUPS, the
ready call); each file < 15 MB; the page keeps everything else. The repository reader stays self-contained.
(wave 127) reads either a literal or a JSON.parse("…") embedding and writes literals; the data scripts follow the code script,
so the page's skeleton library paints before they parse. Publish with root=<outdir>, files={"data/d1.js": "data/d1.js", …}."""
import json,sys,os
src,out=sys.argv[1],sys.argv[2]
os.makedirs(os.path.join(out,"data"),exist_ok=True)
t=open(src,encoding="utf-8").read()
i=t.find("// __DATA_START__"); j=t.find("// __DATA_END__")
assert i>0 and j>i, "data markers missing"
seg=t[i:j]
s=seg.find("const STORIES = "); g=seg.find("\nconst GRAMMAR")
lit=seg[s+len("const STORIES = "):g].rstrip().rstrip(";")
if lit.startswith("JSON.parse("): arr=json.loads(json.loads(lit[len("JSON.parse("):-1]))
else: arr=json.loads(lit)
rest=seg[g+1:]; head=seg[:s]
d=lambda o: json.dumps(o,ensure_ascii=False,separators=(",",":"))
def jp(o):   # an object literal: Chromium parses it faster than JSON.parse("…") of the same data (wave 127 measurement)
    return d(o).replace("</","<\\/")
files=[]; cur=[]; curb=0; LIM=13_000_000
for p in arr:
    b=len(d(p).encode())+2
    if cur and curb+b>LIM: files.append(cur); cur=[]; curb=0
    cur.append(p); curb+=b
files.append(cur)
names=[]
for k,chunk in enumerate(files):
    fn=f"data/d{k+1}.js"; names.append(fn)
    body=("const STORIES = "+jp(chunk)+";\n") if k==0 else ("STORIES.push(..."+jp(chunk)+");\n")
    open(os.path.join(out,fn),"w",encoding="utf-8").write((head if k==0 else "")+body)
fn=f"data/d{len(files)+1}.js"; names.append(fn)
open(os.path.join(out,fn),"w",encoding="utf-8").write(rest)
tags="".join(f'<script src="{n}"></script>' for n in names)
page=t[:i]+"// data served from data/*.js for the hosted copy — the repository reader keeps it inline\n</script>"+tags+"<script>\n"+t[j:]
name=os.path.basename(src)
open(os.path.join(out,name),"w",encoding="utf-8").write(page)
for n in names: print(n, os.path.getsize(os.path.join(out,n)))
print("page", name, os.path.getsize(os.path.join(out,name)), "packages per file", [len(c) for c in files])
print("files=" + json.dumps({n:n for n in names}))
