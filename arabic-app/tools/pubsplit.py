#!/usr/bin/env python3
"""pubsplit.py <reader.html> <outdir> — the artifact copy of the reader: app.js (the code, wave 150) + data/d1–dN.js, the page keeps
the catalog and the skeleton and a loader that inserts the data scripts after one frame. Its __DATA_START__…__DATA_END__ block moved
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
# (v341-S) THE DOOR BEFORE THE BODIES. d1 (the core) carries every story's catalog fields and the tables after them, and calls the
# shell; the bodies (chapters, morph, glossary) ride in slices of about BODY_LIM bytes, a few stories each, named by a hash of
# their content (data/b<k>-<hash>.js), so a new build re-downloads only the slices whose stories changed. The page's loader
# inserts the core after one frame; the shell (BODY341) fetches the bodies after the door, the tapped story's slice first.
import hashlib
BODY_KEYS=("chapters","morph","glossary"); BODY_LIM=int(os.environ.get("QISSA_BODY_LIM","2500000"))
def hname(prefix,text): return f"data/{prefix}-{hashlib.sha256(text.encode()).hexdigest()[:10]}.js"
meta=[{k:v for k,v in p.items() if k not in BODY_KEYS} for p in arr]
bodies=[]; cur=[]; curb=0
for p in arr:
    b={k:p[k] for k in BODY_KEYS if k in p}; n=len(d(b).encode())
    if cur and curb+n>BODY_LIM: bodies.append(cur); cur=[]; curb=0
    cur.append((p["id"],b)); curb+=n
if cur: bodies.append(cur)
body_list=[]
for k,chunk in enumerate(bodies):
    text="__qissaBodies341("+jp({i:b for i,b in chunk})+");\n"
    fn=hname(f"b{k+1}",text); open(os.path.join(out,fn),"w",encoding="utf-8").write(text)
    body_list.append([fn,[i for i,_ in chunk]])
core_text=head+"const STORIES = "+jp(meta)+";\n"+rest
core=hname("d1",core_text); open(os.path.join(out,core),"w",encoding="utf-8").write(core_text)
names=[core]+[b[0] for b in body_list]
tags="".join(f'<script src="{n}"></script>' for n in [core])
page=t[:i]+"// data served from data/*.js for the hosted copy — the repository reader keeps it inline\n</script>"+tags+"<script>\n"+t[j:]
# (wave 150) the CODE leaves the page too: an external classic script is compiled off the main thread as it streams in, and
# its bytecode is kept in the browser's code cache from the second visit on, while an inline script of 3.9 MB is re-parsed
# on every launch. Measured at 4× CPU through route interception: boot 2.5–3.3 s → 1.8 s, the longest task 847 → 210 ms.
# The page keeps the CATALOG and the skeleton inline; app.js is the first script of the body; the data scripts are inserted
# by a loader after ONE FRAME, in order (async=false keeps insertion order), so the skeleton shelf is on screen before the
# first data file parses — on every host, file:// included.
cs=page.find("<script>"); ce=page.find("</script>", cs)
code=page[cs+len("<script>"):ce]
cat_i=code.find("// __CATALOG_START__"); cat_j=code.find("// __CATALOG_END__")
assert cat_i>=0 and cat_j>cat_i, "catalog markers"
catalog=code[cat_i:cat_j+len("// __CATALOG_END__")]
app=code[:cat_i]+code[cat_j+len("// __CATALOG_END__"):]
open(os.path.join(out,"app.js"),"w",encoding="utf-8").write(app)
data_names=list(names)
loader=("<script>(function(){var L="+json.dumps([core])+";window.__qissaSlices341={core:L,bodies:"+json.dumps(body_list,ensure_ascii=False)+"};"
        "function go(){L.forEach(function(n){var s=document.createElement('script');s.src=n;s.async=false;document.body.appendChild(s);});}"
        "if(window.requestAnimationFrame)requestAnimationFrame(function(){setTimeout(go,0);});else go();})();</script>")
page=page[:cs]+"<script>\n"+catalog+"\n</script><script src=\"app.js\"></script>"+loader+page[ce+len("</script>"):]
page=page.replace(tags,"<!-- data/*.js are loaded by the loader above: "+" ".join(data_names)+" -->")
names.insert(0,"app.js")
name=os.path.basename(src)
open(os.path.join(out,name),"w",encoding="utf-8").write(page)
for n in names: print(n, os.path.getsize(os.path.join(out,n)))
print("page", name, os.path.getsize(os.path.join(out,name)), "body slices", len(body_list), "stories per slice", [len(c) for c in bodies])
print("files=" + json.dumps({n:n for n in names}))
