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
BODY_KEYS=("chapters","morph","glossary","course351","about"); BODY_LIM=int(os.environ.get("QISSA_BODY_LIM","2500000"))   # (v351-I) course351: the Iẓhār course rides in its story's body
# (v354-S) about: a story's provenance text (0.9 MB raw / ~0.2 MB gzip of the core for 102 stories) is read only by openAbout, which waits
# for that story's body (bodyGate341) — it rides in the body slice; BODY341.KEYS lists it, so its stub traps a door read (__bodyMiss341)
def hname(prefix,text): return f"data/{prefix}-{hashlib.sha256(text.encode()).hexdigest()[:10]}.js"
meta=[{k:v for k,v in p.items() if k not in BODY_KEYS} for p in arr]
bodies=[]; cur=[]; curb=0
for p in arr:
    b={k:p[k] for k in BODY_KEYS if k in p}; n=len(d(b).encode())
    if cur and curb+n>BODY_LIM: bodies.append(cur); cur=[]; curb=0
    cur.append((p["id"],b)); curb+=n
if cur: bodies.append(cur)
# (v354-S) two tables no door reads ride in the LAST body slice, declared before its arrival call: ALFIYYA_JSON (130 KB, read only by a
# grammar note's Elfiye card and its round — openRef waits for every body) and AMTHAL (the proverbs' index, 0.3 MB, which no screen reads).
# `var`, so a re-run slice cannot throw; Alfiyya352.data tests `typeof` and caches nothing before BODY341.ready() — 0.4 MB raw / 67 KB gzip
# off the core; QISSA_NO_LATE354=1 keeps them in the core
late=""
if os.environ.get("QISSA_NO_LATE354") != "1":
    for nm in ("ALFIYYA_JSON","AMTHAL"):
        k=rest.find("\nconst "+nm+" = ")
        if k<0: continue
        e=rest.find("\n",k+1); line=rest[k+1:e if e>=0 else len(rest)]
        if not line.endswith(";"): continue
        late+="var"+line[len("const"):]+"\n"; rest=rest[:k]+rest[k+1+len(line):]
body_list=[]
for k,chunk in enumerate(bodies):
    text=(late if k==len(bodies)-1 else "")+"__qissaBodies341("+jp({i:b for i,b in chunk})+");\n"
    fn=hname(f"b{k+1}",text); open(os.path.join(out,fn),"w",encoding="utf-8").write(text)
    body_list.append([fn,[i for i,_ in chunk]])
# (v350-S) THE GRAMMAR TABLES' BODIES AFTER THE DOOR. GRAMMAR was 1.0 MB of the core's 1.6 MB gzip and CATECHISM 0.17 MB; the door reads
# of them only ids, titles, groups, levels, the rule of the day's book lines (an example that cites a book, and a note's first own example)
# and a question's id. The core keeps exactly that ("light"); the rest (a note's explanation, question, mistakes, plain text and its whole
# examples list; a question's text, answer, Arabic and notes) rides in data/g1-<hash>.js, which the shell (BODY341) fetches FIRST after
# the door and merges into the same objects in their original key order. Until it is in, BODY341.ready() is false, so every door that
# reads the corpus (search, games, Atölye, deck, progress, a word's sheet, a grammar note, a story) waits exactly as for a story body.
# A smoke check proves the door reads no missing field and that the merged tables equal the repository reader's.
G_HEAVY=("explanation","question","mistakes","plain")
C_KEEP=("n","id","story","chapter","verified","src","kind")
gsplit=None
def _cut(text, name):
    k=text.find("const "+name+" = ")
    if k<0: return None
    e=text.find("\n",k); line=text[k:e if e>=0 else len(text)]
    if not line.endswith(";"): return None
    return k, k+len(line), json.loads(line[len("const "+name+" = "):-1])
cg=_cut(rest,"GRAMMAR"); cc=_cut(rest,"CATECHISM")
if cg and cc and os.environ.get("QISSA_NO_GSPLIT") != "1":
    G=cg[2]; C=cc[2]; gl={}; gh={}
    for gid,g in G.items():
        l={}; h={}
        for k,v in g.items():
            if k in G_HEAVY: h[k]=v
            elif k=="examples" and isinstance(v,list):
                own=[False]; keep=[x for x in v if (isinstance(x,dict) and x.get("cite")) or (not own[0] and not own.__setitem__(0,True))]
                l[k]=keep
                if len(keep)<len(v): h[k]=v
            else: l[k]=v
        gl[gid]=l
        if h: h["__o"]=list(g.keys()); gh[gid]=h
    cl=[]; ch=[]
    for bi,b in enumerate(C):
        b2={k:v for k,v in b.items() if k!="items"}; its=[]
        for ii,it in enumerate(b.get("items") or []):
            l={k:v for k,v in it.items() if k in C_KEEP}; h={k:v for k,v in it.items() if k not in C_KEEP}
            its.append(l)
            if h: h["__o"]=list(it.keys()); ch.append([bi,ii,h])
        if "items" in b: b2["items"]=its
        if list(b2.keys())!=list(b.keys()): b2={k:b2[k] for k in b.keys()}
        cl.append(b2)
    parts=sorted([(cg[0],cg[1],"const GRAMMAR = "+jp(gl)+";"),(cc[0],cc[1],"const CATECHISM = "+jp(cl)+";")],reverse=True)
    for a,z,s in parts: rest=rest[:a]+s+rest[z:]
    gtext="__qissaGrammar350("+jp({"g":gh,"c":ch})+");\n"
    gsplit=hname("g1",gtext); open(os.path.join(out,gsplit),"w",encoding="utf-8").write(gtext)
core_text=head+"const STORIES = "+jp(meta)+";\n"+rest
core=hname("d1",core_text); open(os.path.join(out,core),"w",encoding="utf-8").write(core_text)
names=[core]+([gsplit] if gsplit else [])+[b[0] for b in body_list]
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
loader=("<script>(function(){var L="+json.dumps([core])+";window.__qissaSlices341={core:L,"+("grammar:"+json.dumps(gsplit)+"," if gsplit else "")+"bodies:"+json.dumps(body_list,ensure_ascii=False)+"};"
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
