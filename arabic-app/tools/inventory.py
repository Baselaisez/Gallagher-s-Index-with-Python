#!/usr/bin/env python3
"""v356-G — NOTHING IS LOST: one inventory of everything the app holds, and a guard that it only grows.

    python3 tools/inventory.py --write        refresh content/inventory.json (the developer's step after adding content)
    python3 tools/inventory.py --check        rebuild and compare with the committed file; exit 1 on anything REMOVED
    python3 tools/inventory.py --diff         a readable report of added / removed / changed (exit 0)
    python3 tools/inventory.py --selftest     three in-memory bites (a sentence, an engine rule row, a game) must each fail
    options: --files-only (the tree only: stories, notes, catechism, rule tables — release.py's non-browser gate)
             --page-json F (the in-page half already read, e.g. by the smoke suite on its open page) --json (one JSON line)

What it holds (content/inventory.json, sorted, deterministic):
  stories    per package (content/samples + content/user-uploads): shelf, level, chapters, sentences, tokens and three hashes —
             text (every token's surface.full in order: the received text and its vowels), irab (ar/en/tr lines, the Turkish
             from content/i18n/irab-tr.json as the build adds it), gloss (translations, glossary, morphology); totals per shelf.
  notes      content/grammar: id → examples, hash.   catechism: book → item ids.
  rules      content/rules/*.json: per file its hash and its record lists ({n, ids}); statuses and ledger counts are kept as
             information (a row moving open → applied is progress, not loss).
  engines    read from the BUILT page by tools/inventory_probe.js: every class, and every class's UPPER-CASE static table
             (RULES, GATES, SEAT, …) with its row ids.
  features   games (GameFactory.CATALOGUE), labs (LAB_TOOLS), shelves (LIB_SOURCES), the word sheet's tabs, the Today card's
             steps, Settings' sections, ui() keys per language, the qissa-* storage keys the code names (Backup carries them all).
  page       the built page's STORIES / GRAMMAR / CATECHISM / ILAL must equal the tree (a build that dropped something fails).
  hosted     tools/pubsplit.py into a temp folder: every story (its body, same text hash), note (merged examples), catechism item,
             reason, data table and feature id is reachable in the split copy; the slices' names and sizes. The folder is removed.

How the guard decides (compare): anything REMOVED fails, named (a package, a fallen chapter/sentence/token count, a note, an
example, a catechism item, a rule row or table, an engine class or one of its rule ids, a game, a lab, a shelf, a tab, a step, a
section, a string key, a storage key, a reason, a verse). A story's TEXT hash that changed fails unless the package is named in a
NEW line of content/inventory-accepted.jsonl ({date, what, why, by}; `what` starts with the package id) — that also covers its
counts. A changed irab / gloss hash passes and is counted. Anything ADDED passes and is listed. Lines of the accepted file already
folded in by the last --write are spent (inventory["accepted_lines"]); a fresh --write absorbs every accepted change.
"""
import copy, hashlib, json, os, re, shutil, subprocess, sys, tempfile, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INV = ROOT / "content/inventory.json"
ACC = ROOT / "content/inventory-accepted.jsonl"
PAGE = Path(os.environ.get("SMOKE_READER") or ROOT / "prototype/reader.html")
COLLECTIONS = [ROOT / "content/samples", ROOT / "content/user-uploads"]
FILE_SECTIONS = ("stories", "notes", "catechism", "rules")


def H(x):
    return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]


def jload(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


# ---------------------------------------------------------------- the tree
def irab_tr():
    p = ROOT / "content/i18n/irab-tr.json"
    return jload(p).get("entries", {}) if p.is_file() else {}


def load_pkg(pkg):
    m = jload(pkg / "manifest.json")
    chs = [jload(pkg / "chapters" / f"{c['n']}.json") for c in m["chapters"]]
    g = jload(pkg / "glossary.json") if (pkg / "glossary.json").is_file() else {}
    mo = jload(pkg / "morphology.json") if (pkg / "morphology.json").is_file() else {}
    return {"manifest": m, "chapters": chs, "glossary": g, "morphology": mo}


def story_entry(d, tr):
    """counts and the three hashes of one package (d = load_pkg's dict; also used on in-memory copies by --selftest)."""
    text, irab, gl = [], [], []
    ns = nt = 0
    for ch in d["chapters"]:
        ct, ci = [], []
        for s in ch["sentences"]:
            ns += 1; nt += len(s["tokens"])
            ct.append([t["surface"]["full"] for t in s["tokens"]])
            ir = []
            for t in s["tokens"]:
                i = dict(t.get("irab") or {})
                if i.get("en") and not i.get("tr") and tr.get(i["en"]):
                    i["tr"] = tr[i["en"]]
                ir.append(i)
            ci.append(ir); gl.append(s.get("translation"))
        text.append(ct); irab.append(ci)
    return {"level": d["manifest"].get("level"), "chapters": len(d["chapters"]), "sentences": ns, "tokens": nt,
            "text": H(text), "irab": H(irab), "gloss": H([gl, d["glossary"], d["morphology"]])}


def packages():
    out = []
    for c in COLLECTIONS:
        if c.is_dir():
            out += sorted(p for p in c.iterdir() if (p / "manifest.json").is_file())
    return out


def ids_of(lst):
    """a record list → {n, ids} or {n}. ids: the first of id / key / n / name / entry that every row carries and that is
    unique (else the first every row carries), or the strings themselves."""
    if not lst:
        return {"n": 0}
    sc = lambda v: isinstance(v, (str, int)) and not isinstance(v, bool)
    if all(isinstance(r, dict) for r in lst):
        keys = [k for k in ("id", "key", "n", "name", "entry") if all(sc(r.get(k)) for r in lst)]
        if not keys:
            return {"n": len(lst)}
        k = next((k for k in keys if len({r[k] for r in lst}) == len(lst)), keys[0])
        ids = [str(r[k])[:60] for r in lst]
    elif all(sc(r) for r in lst):
        ids = [str(r)[:60] for r in lst]
    else:
        return {"n": len(lst)}
    return {"n": len(lst), "ids": sorted(set(ids))}


INFO_KEYS = ("counts", "status", "built_by", "about", "how", "note")


def rule_file(p):
    d = jload(p)
    e = {"hash": H(d), "lists": {}}
    if isinstance(d, list):
        e["lists"]["(rows)"] = ids_of(d)
        rows = d
    else:
        rows = []
        for k, v in sorted(d.items()):
            if k in INFO_KEYS:
                continue
            if isinstance(v, list) and v:
                e["lists"][k] = ids_of(v)
                if all(isinstance(r, dict) for r in v):
                    rows += v
            elif isinstance(v, dict) and (len(v) >= 4 or (len(v) >= 2 and all(isinstance(x, (dict, list)) for x in v.values()))):
                e["lists"][k] = {"n": len(v), "ids": sorted(str(x)[:60] for x in v)}
        if isinstance(d.get("counts"), dict):
            e["counts"] = d["counts"]
    st = {}
    for r in rows:
        if isinstance(r, dict) and isinstance(r.get("status"), str):
            st[r["status"]] = st.get(r["status"], 0) + 1
    if st:
        e["status"] = st
    return e


def files_side():
    tr = irab_tr()
    stories = {}
    for pkg in packages():
        d = load_pkg(pkg)
        stories[d["manifest"]["id"]] = story_entry(d, tr)
    notes = {}
    for f in sorted((ROOT / "content/grammar").glob("*.json")):
        g = jload(f)
        notes[g.get("id", f.stem)] = {"examples": len(g.get("examples") or []), "hash": H(g)}
    cat = {}
    for f in sorted((ROOT / "content/catechism").glob("*.json")):
        b = jload(f)
        cat[b.get("book", f.stem)] = ids_of(b.get("items") or [])
    rules = {}
    for f in sorted((ROOT / "content/rules").glob("*.json")):
        rules[f.name] = rule_file(f)
    return {"stories": stories, "notes": notes, "catechism": cat, "rules": rules}


# ---------------------------------------------------------------- the built page
def data_block(text):
    i, j = text.find("// __DATA_START__"), text.find("// __DATA_END__")
    assert i > 0 and j > i, "data markers missing in the page"
    return i, j


def const_line(seg, name, kw="const"):
    k = seg.find("\n" + kw + " " + name + " = ")
    if k < 0:
        return None
    e = seg.find("\n", k + 1)
    line = seg[k + 1:e if e >= 0 else len(seg)].rstrip()
    lit = line[len(kw + " " + name + " = "):].rstrip(";")
    if lit.startswith("JSON.parse("):
        return json.loads(json.loads(lit[len("JSON.parse("):-1]))
    return json.loads(lit)


def page_story(s):
    chs = s.get("chapters") or []
    if isinstance(chs, str):   # the build ships a long story's chapters as one JSON string, parsed on open
        chs = json.loads(chs)
    text = [[[t["s"]["full"] for t in sen["tokens"]] for sen in ch["sentences"]] for ch in chs]
    return {"chapters": len(text), "sentences": sum(len(c) for c in text), "tokens": sum(len(x) for c in text for x in c), "text": H(text)}


def page_tables(seg):
    """the data tables a page (or a split copy's core) carries: GRAMMAR ids/examples, CATECHISM items, ILAL reason ids."""
    out = {}
    g = const_line(seg, "GRAMMAR")
    out["notes"] = {k: len(v.get("examples") or []) for k, v in (g or {}).items()}
    c = const_line(seg, "CATECHISM") or []
    out["catechism"] = {b.get("book"): ids_of(b.get("items") or [])["n"] for b in c}
    il = const_line(seg, "ILAL") or const_line(seg, "ILAL", "var") or {}
    out["reasons"] = sorted(r["id"] for r in il.get("reasons", []))
    out["consts"] = sorted(set(re.findall(r"^(?:const|var) ([A-Z][A-Z0-9_]*) = ", seg, re.M)))
    return out


CLASS_RX = re.compile(r"^\s*class ([A-Za-z_$][\w$]*)", re.M)


def code_scan(code):
    """features read from the page's CODE by pattern: classes, the word sheet's tabs, the Today steps, Settings' sections,
    the qissa-* storage keys the code names."""
    out = {"classes": sorted(set(CLASS_RX.findall(code)))}
    out["tabs"] = sorted(set(re.findall(r'tabB\("(\w+)"', code)))
    out["today"] = sorted(set(re.findall(r'\{ id: "(\w+)", label: U\.', code)))
    i = code.find("function openDoorSettings340(")
    body = code[i:code.find("sheetInner.querySelectorAll", i)] if i >= 0 else ""
    out["settings"] = sorted(set(re.findall(r'class="set-group"><span class="ls-lbl">\$\{U\.(\w+)\}', body)) |
                             set(re.findall(r'\$\{(\w+)\.(?:settingsHtml|html)\(\)\}', body)))
    out["storage"] = sorted(set(k.rstrip("-:") for k in re.findall(r'["\'`](qissa-[a-z0-9][a-z0-9_:-]*)', code) if len(k.rstrip("-:")) > 6))
    return out


def page_side(probe):
    text = PAGE.read_text(encoding="utf-8")
    i, j = data_block(text)
    seg = text[i:j]
    stories = {s["id"]: page_story(s) for s in const_line(seg, "STORIES")}
    code = text[text.find("<script>"):i]
    sc = code_scan(code)
    tables = page_tables(seg)
    feats = {"games": probe.get("games", []), "labs": probe.get("labs", []), "shelves": probe.get("shelves", []),
             "tabs": sc["tabs"], "today": sc["today"], "settings": sc["settings"], "storage": sc["storage"],
             "ui": {lang: {"n": len(k), "ids": k} for lang, k in sorted(probe.get("ui", {}).items())}}
    engines = {"classes": sorted(set(probe.get("classes", [])) | set(sc["classes"])), "tables": probe.get("tables", {})}
    return text, seg, stories, tables, feats, engines, sc


def hosted_side(text, page_stories, tables, feats, engines):
    """pubsplit into a temp folder and prove everything is reachable there; the folder is removed."""
    tmp = tempfile.mkdtemp(prefix="inv356-")
    try:
        src = Path(tmp) / "reader.html"
        src.write_text(text, encoding="utf-8")
        out = Path(tmp) / "out"
        r = subprocess.run([sys.executable, str(ROOT / "tools/pubsplit.py"), str(src), str(out)], capture_output=True, text=True)
        if r.returncode:
            return {"error": "pubsplit failed: " + (r.stderr or r.stdout)[-300:]}
        files = json.loads(r.stdout.strip().splitlines()[-1][len("files="):])
        slices = {n: (out / n).stat().st_size for n in files}
        slices["reader.html"] = (out / "reader.html").stat().st_size
        core_name = next(n for n in files if n.startswith("data/d1-"))
        core = (out / core_name).read_text(encoding="utf-8")
        core = "\n" + core
        meta = const_line(core, "STORIES")
        bodies, late = {}, ""
        for n in files:
            if re.match(r"data/b\d+-", n):
                t = (out / n).read_text(encoding="utf-8")
                k = t.find("__qissaBodies341(")
                late += t[:k]
                bodies.update(json.loads(t[k + len("__qissaBodies341("):t.rindex(");")]))
        st = {}
        for m in meta:
            b = bodies.get(m["id"])
            st[m["id"]] = page_story(dict(m, **(b or {}))) if b else None
        ct = page_tables(core)
        gn = next((n for n in files if n.startswith("data/g1-")), None)
        if gn:   # merge the grammar slice the way BODY341 does: heavy fields back into the same notes / items
            gt = (out / gn).read_text(encoding="utf-8")
            gj = json.loads(gt[gt.find("(") + 1:gt.rindex(");")])
            for k, h in gj.get("g", {}).items():
                if "examples" in h:
                    ct["notes"][k] = len(h["examples"])
        lt = page_tables("\n" + late)
        consts = set(ct["consts"]) | set(lt["consts"])
        app = (out / "app.js").read_text(encoding="utf-8")
        asc = code_scan(app)
        miss = []
        for sid, s in page_stories.items():
            if st.get(sid) is None:
                miss.append("story " + sid + (" (no body)" if sid in st else ""))
            elif st[sid] != s:
                miss.append("story " + sid + " differs")
        for k, n in tables["notes"].items():
            if ct["notes"].get(k) != n:
                miss.append(f"note {k} examples {ct['notes'].get(k)}≠{n}")
        for k, n in tables["catechism"].items():
            if ct["catechism"].get(k) != n:
                miss.append(f"catechism {k}")
        for r_ in sorted(set(tables["reasons"]) - set(ct["reasons"] or lt["reasons"])):
            miss.append("reason " + r_)
        for c in sorted(set(tables["consts"]) - consts):
            miss.append("table " + c)
        for c in sorted(set(engines["classes"]) - set(asc["classes"])):
            miss.append("class " + c)
        for sec in ("tabs", "today", "settings", "storage"):
            for x in sorted(set(feats[sec]) - set(asc[sec])):
                miss.append(sec + " " + x)
        for sec in ("games", "labs", "shelves"):
            for x in feats[sec]:
                if '"' + x + '"' not in app:
                    miss.append(sec + " " + x)
        return {"missing": miss, "stories": len([s for s in st.values() if s]), "slices": dict(sorted(slices.items()))}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def run_probe():
    tmp = tempfile.mkdtemp(prefix="inv356p-")
    try:
        o = Path(tmp) / "p.json"
        env = dict(os.environ)
        env.setdefault("NODE_PATH", "/opt/node-tools/node_modules")
        r = subprocess.run(["node", str(ROOT / "tools/inventory_prove.js"), str(o)], env=env, capture_output=True, text=True)
        if r.returncode:
            sys.exit("inventory: the in-page probe failed: " + (r.stderr or r.stdout)[-400:])
        return jload(o)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------- build
def build(files_only=False, probe=None, hosted=True):
    inv = {"inventory": "v356-G — what the app holds; generated by tools/inventory.py --write, guarded by --check"}
    inv.update(files_side())
    if files_only:
        return inv
    if probe is None:
        probe = run_probe()
    text, seg, pst, tables, feats, engines, sc = page_side(probe)
    shelf = probe.get("shelfOf", {})
    for sid, s in inv["stories"].items():
        s["shelf"] = shelf.get(sid, "")
    mism = []
    for sid, s in inv["stories"].items():
        p = pst.get(sid)
        if not p:
            mism.append("story " + sid + " is not in the built page")
        elif any(p[k] != s[k] for k in ("chapters", "sentences", "tokens", "text")):
            mism.append("story " + sid + " in the built page differs from the tree (rebuild?)")
    for nid, n in inv["notes"].items():
        if tables["notes"].get(nid) is None:
            mism.append("note " + nid + " is not in the built page")
        elif tables["notes"][nid] < n["examples"]:
            mism.append(f"note {nid}: the built page has {tables['notes'][nid]} examples, the tree {n['examples']}")
    for b, c in inv["catechism"].items():
        if tables["catechism"].get(b, -1) < c["n"]:
            mism.append("catechism " + b + " is short in the built page")
    il = {r["id"] for r in jload(ROOT / "content/rules/ilal.json").get("reasons", [])} if (ROOT / "content/rules/ilal.json").is_file() else set()
    for r_ in sorted(il - set(tables["reasons"])):
        mism.append("reason " + r_ + " is not in the built page")
    inv["page"] = {"mismatch": mism, "stories": len(pst), "consts": tables["consts"]}
    inv["engines"] = engines
    inv["features"] = feats
    if hosted:
        inv["hosted"] = hosted_side(text, pst, tables, feats, engines)
    tot = {}
    for s in inv["stories"].values():
        for key in ("(all)", s.get("shelf") or "(none)"):
            t = tot.setdefault(key, {"stories": 0, "chapters": 0, "sentences": 0, "tokens": 0})
            t["stories"] += 1
            for k in ("chapters", "sentences", "tokens"):
                t[k] += s[k]
    inv["totals"] = dict(sorted(tot.items()))
    inv["accepted_lines"] = len(accepted())
    return inv


def accepted():
    if not ACC.is_file():
        return []
    out = []
    for ln in ACC.read_text(encoding="utf-8").splitlines():
        if ln.strip():
            out.append(json.loads(ln))
    return out


# ---------------------------------------------------------------- compare
SKIP = {"hash", "text", "irab", "gloss", "level", "shelf", "counts", "status", "slices", "mismatch", "missing", "totals",
        "inventory", "accepted_lines"}


def atoms(o, path="", out=None):
    """flatten an inventory into guarded atoms: path → set of ids, or path → a count."""
    out = {} if out is None else out
    if isinstance(o, dict):
        if "ids" in o:
            out[path] = ("set", set(o["ids"]))
        if "n" in o and isinstance(o["n"], int):
            out[path + "#n"] = ("n", o["n"])
        for k, v in o.items():
            if k in ("ids", "n") or k in SKIP:
                continue
            p = path + "/" + k if path else k
            if isinstance(v, dict):
                out[p] = ("set", set(x for x in v if x not in SKIP and x not in ("ids", "n")))
                atoms(v, p, out)
            elif isinstance(v, list) and all(isinstance(x, str) for x in v):
                out[p] = ("set", set(v))
            elif isinstance(v, int) and not isinstance(v, bool):
                out[p] = ("n", v)
    return out


def compare(old, new, acc_new=()):
    """→ {ok, removed[], added[], changed_text[], accepted[], irab_changed, gloss_changed, problems[]}"""
    secs = [k for k in new if k not in ("inventory", "accepted_lines", "totals")]
    o = {k: old[k] for k in secs if k in old}
    n = {k: new[k] for k in secs}
    acc_ids = [str(a.get("what", "")) for a in acc_new]
    is_acc = lambda sid: any(w == sid or w.startswith(sid + ":") or w.startswith(sid + " ") for w in acc_ids)
    ao, an = atoms(o), atoms(n)
    removed, added, accd = [], [], []
    for p, (kind, v) in sorted(ao.items()):
        story = re.match(r"stories/([^/]+)/(chapters|sentences|tokens)$", p)
        if p not in an:   # a missing child is named once, by its parent's set of keys
            if "/" not in p:
                removed.append(p)
            continue
        w = an[p][1]
        if kind == "set":
            gone = sorted(v - w)
            if gone:
                removed.append(p + ": " + ", ".join(gone[:12]) + (f" … (+{len(gone) - 12})" if len(gone) > 12 else ""))
            new_ = sorted(w - v)
            if new_:
                added.append(p + ": " + ", ".join(new_[:8]) + (f" … (+{len(new_) - 8})" if len(new_) > 8 else ""))
        else:
            sp = p[:-2] if p.endswith("#n") else None
            if sp in ao and sp in an and ao[sp][0] == "set" and ao[sp][1] != an[sp][1]:
                continue   # its ids already said it
            q = p[:-2] if p.endswith("#n") else p
            if story and w != v and is_acc(story.group(1)):
                accd.append(f"{q} {v}→{w}")
            elif w < v:
                removed.append(f"{q} {v}→{w}")
            elif w > v:
                added.append(f"{q} {v}→{w}")
    changed_text, irab_c, gloss_c = [], 0, 0
    for sid, s in n.get("stories", {}).items():
        os_ = o.get("stories", {}).get(sid)
        if not os_:
            continue
        if os_.get("text") != s["text"]:
            (accd if is_acc(sid) else changed_text).append(sid + " (text)")
        irab_c += os_.get("irab") != s["irab"]
        gloss_c += os_.get("gloss") != s["gloss"]
    problems = list(n.get("page", {}).get("mismatch", [])) + ["hosted copy: " + m for m in n.get("hosted", {}).get("missing", [])]
    if n.get("hosted", {}).get("error"):
        problems.append("hosted copy: " + n["hosted"]["error"])
    return {"ok": not (removed or changed_text or problems), "removed": removed, "changed_text": changed_text, "problems": problems,
            "added": added, "accepted": accd, "irab_changed": irab_c, "gloss_changed": gloss_c}


def dump(inv):
    """one key per line, each leaf list of ids on ONE line: small, and a diff still names what moved."""
    def w(o, ind):
        if isinstance(o, dict) and o:
            pad = "\n" + " " * (ind + 1)
            return "{" + ",".join(pad + json.dumps(k, ensure_ascii=False) + ": " + w(o[k], ind + 1) for k in sorted(o)) + "\n" + " " * ind + "}"
        return json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(", ", ": ") if isinstance(o, (list, dict)) else None)
    return w(inv, 0) + "\n"


def report(r, full=True):
    L = []
    for k, lbl in (("removed", "REMOVED"), ("changed_text", "TEXT CHANGED (not in content/inventory-accepted.jsonl)"),
                   ("problems", "NOT REACHABLE"), ("accepted", "accepted changes"), ("added", "added")):
        if r[k]:
            L.append(f"{lbl} ({len(r[k])}):")
            L += ["  - " + x for x in (r[k] if full else r[k][:20])]
    L.append(f"irab hashes changed: {r['irab_changed']}; translation/glossary hashes changed: {r['gloss_changed']}")
    L.append("OK — nothing is lost" if r["ok"] else "FAIL — something the app held is gone (see above); if deliberate, record it and run --write")
    return "\n".join(L)


# ---------------------------------------------------------------- self-test
def selftest(probe=None):
    """three bites on in-memory copies; no file is touched."""
    if probe is None:
        probe = run_probe()
    base = build(probe=probe, hosted=False)
    out = []
    # 1. one sentence out of a package (through the same story code path)
    pkg = next(p for p in packages() if p.name == "ashab-al-fil") if (ROOT / "content/samples/ashab-al-fil").is_dir() else packages()[0]
    d = load_pkg(pkg)
    d2 = copy.deepcopy(d)
    d2["chapters"][0]["sentences"].pop()
    inv1 = copy.deepcopy(base)
    sid = d["manifest"]["id"]
    inv1["stories"][sid] = dict(story_entry(d2, irab_tr()), shelf=base["stories"][sid]["shelf"])
    r1 = compare(base, inv1)
    out.append(("sentence", sid, r1))
    # 2. one rule row out of an engine table
    p2 = copy.deepcopy(probe)
    rows = p2["tables"]["Nahw342Engine"]["RULES"]
    gone = rows["ids"].pop(0); rows["n"] -= 1
    r2 = compare(base, build_from(base, p2))
    out.append(("engine rule", "Nahw342Engine.RULES " + gone, r2))
    # 3. one game out of the registry
    p3 = copy.deepcopy(probe)
    g = p3["games"].pop()
    r3 = compare(base, build_from(base, p3))
    out.append(("game", g, r3))
    res = []
    ok = True
    for what, name, r in out:
        key = name.split()[-1] if what != "sentence" else sid
        bit = (not r["ok"]) and any(key in x for x in r["removed"] + r["changed_text"])
        ok &= bit
        res.append({"bite": what, "name": name, "failed_as_it_must": bit, "said": (r["removed"] + r["changed_text"])[:3]})
    clean = compare(base, base)
    ok &= clean["ok"]
    return ok, res


def build_from(base, probe):
    """the page-side sections rebuilt from an (altered) probe; the tree sections reused."""
    inv = copy.deepcopy(base)
    feats = inv["features"]
    for k in ("games", "labs", "shelves"):
        feats[k] = probe.get(k, [])
    feats["ui"] = {lang: {"n": len(k), "ids": k} for lang, k in sorted(probe.get("ui", {}).items())}
    inv["engines"]["tables"] = probe["tables"]
    return inv


# ---------------------------------------------------------------- main
def main(argv):
    t0 = time.time()
    a = set(x for x in argv if x.startswith("--"))
    pj = argv[argv.index("--page-json") + 1] if "--page-json" in argv else None
    probe = jload(pj) if pj else None
    fo = "--files-only" in a
    as_json = "--json" in a
    if "--selftest" in a:
        ok, res = selftest(probe)
        print(json.dumps({"ok": ok, "bites": res, "ms": int((time.time() - t0) * 1000)}, ensure_ascii=False, indent=None if as_json else 1))
        return 0 if ok else 1
    new = build(files_only=fo, probe=probe)
    if "--write" in a:
        if fo:
            sys.exit("inventory: --write needs the page (drop --files-only)")
        old = jload(INV) if INV.is_file() else {}
        r = compare(old, new) if old else None
        INV.write_text(dump(new), encoding="utf-8")
        print(f"wrote {INV.relative_to(ROOT)} ({INV.stat().st_size // 1024} KB)")
        if r:
            print(report(r, full=False))
        bad = new.get("page", {}).get("mismatch") or new.get("hosted", {}).get("missing")
        return 1 if bad else 0
    if not INV.is_file():
        sys.exit("inventory: content/inventory.json is missing — run python3 tools/inventory.py --write")
    old = jload(INV)
    acc = accepted()
    spent = old.get("accepted_lines", 0)
    r = compare(old, new, acc[spent:])
    if len(acc) < spent:
        r["removed"].append(f"content/inventory-accepted.jsonl: {spent - len(acc)} recorded line(s) gone")
        r["ok"] = False
    r["ms"] = int((time.time() - t0) * 1000)
    if as_json:
        print(json.dumps(r, ensure_ascii=False))
    else:
        print(report(r, full=True))
        print(f"({r['ms']} ms{', files only' if fo else ''})")
    if "--diff" in a:
        return 0
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
