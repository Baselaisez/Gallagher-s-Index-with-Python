#!/usr/bin/env python3
"""pubsplit.py <reader.html> <outdir> — the artifact copy of the reader with its __DATA_START__…__DATA_END__ block
moved into outdir/data/d1.js (const STORIES = first packages), d2.js… (STORIES.push(...)), dN.js (GRAMMAR, models,
REF_GROUPS); each file < 15 MB; the page keeps everything else. The repository reader stays self-contained.
Publish with root=<outdir>, files={"data/d1.js": "data/d1.js", …}."""
import json,sys,os
src,out=sys.argv[1],sys.argv[2]
os.makedirs(os.path.join(out,"data"),exist_ok=True)
t=open(src,encoding="utf-8").read()
i=t.find("// __DATA_START__"); j=t.find("// __DATA_END__")
assert i>0 and j>i, "data markers missing"
seg=t[i:j]
s=seg.find("const STORIES = "); g=seg.find("\nconst GRAMMAR")
arr=json.loads(seg[s+len("const STORIES = "):g].rstrip().rstrip(";"))
rest=seg[g+1:]; head=seg[:s]
d=lambda o: json.dumps(o,ensure_ascii=False,separators=(",",":"))
files=[]; cur=[]; curb=0; LIM=15_000_000
for p in arr:
    b=len(d(p).encode())+2
    if cur and curb+b>LIM: files.append(cur); cur=[]; curb=0
    cur.append(p); curb+=b
files.append(cur)
names=[]
for k,chunk in enumerate(files):
    fn=f"data/d{k+1}.js"; names.append(fn)
    body=("const STORIES = " if k==0 else "STORIES.push(...")+d(chunk)+(";\n" if k==0 else ");\n")
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
