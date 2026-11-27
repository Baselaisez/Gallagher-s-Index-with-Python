"""lemmas.txt → lex.json for pkg_from_engine (run from arabic-app):  python3 tools/authoring/marah/mk_lex.py
Every form of the table becomes one lexicon row; a «=key» row copies the shipped entry; a new key may not collide with a shipped one."""
import json, glob, re, sys, unicodedata, pathlib
HERE = pathlib.Path(__file__).parent
N = lambda s: unicodedata.normalize("NFC", s or "")
G = {}
for f in sorted(glob.glob("content/samples/*/glossary.json")):
    if "/marah-al-arwah/" in f: continue
    for k, e in json.load(open(f, encoding="utf-8"))["entries"].items(): G.setdefault(k, e)
LX = {}; errs = []; new = 0; reuse = 0
cite = False
for ln, line in enumerate(open(HERE / "lemmas.txt", encoding="utf-8"), 1):
    line = line.rstrip("\n")
    if line.startswith("# ---"): cite = "the measures" in line
    if not line.strip() or line.startswith("#"): continue
    c = [x.strip() for x in line.split("|")]
    if len(c) != 7: errs.append(f"line {ln}: {len(c)} columns"); continue
    key, lemma, pos, root, en, tr, forms = c
    if key.startswith("="):
        key = key[1:]
        if key not in G: errs.append(f"line {ln}: no shipped key {key}"); continue
        e = dict(G[key]); e["key"] = key; reuse += 1
    else:
        if key in G and N(G[key].get("lemma")) != N(lemma): errs.append(f"line {ln}: key {key} is shipped as {G[key].get('lemma')}")
        if not (lemma and pos and en and tr): errs.append(f"line {ln}: incomplete row {key}")
        e = {"key": key, "lemma": N(lemma), "pos": pos, "gloss": {"en": en, "tr": tr}, "level": 5}
        if root: e["root"] = root
        new += 1
    for f in forms.split():
        f = N(f)
        if f in LX and LX[f]["key"] != key: errs.append(f"line {ln}: form {f} already → {LX[f]['key']}")
        LX[f] = dict(e, cite=True) if cite else e
json.dump(LX, open(HERE / "lex.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(LX)} forms; {new} new lemmas, {reuse} shipped lemmas reused; {len(errs)} problems")
for x in errs: print("  !", x)
sys.exit(1 if errs else 0)
