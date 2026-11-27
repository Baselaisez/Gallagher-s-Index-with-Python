#!/usr/bin/env python3
"""v358-A — the Alfiyya and Ibn ʿAqīl as a COURSE: content/rules/alfiyya_course.json, built from files that already exist.

  python3 tools/alfiyya_course.py            # assemble, run the page half (tools/alfiyya_course_probe.js), write
  python3 tools/alfiyya_course.py --no-prove # reuse tools/.alfcourse-cache.json (the page half's last answers)

Sources (nothing typed that a file holds): content/rules/toc_ibn_aqil.json (the bābs, the verses, the commentary units, the shawāhid),
content/rules/alfiyya.json (Ibn ʿAqīl's ruling sentence per verse, the renderings en / tr where they exist), content/rules/coverage_ibn_aqil.json
(the rule statements, their status and the printed probes the engines prove), research/sources/sharh-ibn-aqil-src.txt (the editor's printed
iʿrāb of a shāhid, «الاعراب:», cited as his). One UNIT per bāb in the book's order: a bāb of < 6 verses takes the next small ones with it, a bāb
of > 30 verses is two units cut at a commentary unit. The questions come only from proved material:
  r — «which role?» on the book's own example as printed: the role Illa346.read finds on the ENGINE's line (an applied row, its printed probe
      proved); the options are roles of the same family (Illa346.famOf) none of whose patterns is on that line; a line giving a second
      reading («او / وقيل / ويجوز»), a probe proved only by OUR vowels, and a probe that names a bare case are never asked;
  h — «complete the verse»: the second hemistich among three of the same unit (received text);
  v — «which verse rules this?»: an applied row's printed example whose page lies in exactly ONE commentary unit and that unit has ONE verse;
  s — «söylenir mi?»: the forbidden-form rows' «لا تقول X» (a form qualified by «على أن / تريد» — meaning-bound — left out; the editor's
      leaked note A284.1 left out) and the applied rows whose ruling allows «يجوز … فتقول X».
"""
import json, re, sys, subprocess, hashlib, os
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
R = lambda f: json.loads((ROOT / f).read_text(encoding="utf-8"))
toc, led, alf = R("content/rules/toc_ibn_aqil.json"), R("content/rules/coverage_ibn_aqil.json"), R("content/rules/alfiyya.json")
SRC = (ROOT / "research/sources/sharh-ibn-aqil-src.txt").read_text(encoding="utf-8")
CACHE = ROOT / "tools/.alfcourse-cache.json"
OUT = ROOT / "content/rules/alfiyya_course.json"
AV = {v["n"]: v for v in alf}

def H(s):
    s = re.sub(r"[ً-ْٰـ]", "", s or "")
    return s.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ٱ", "ا").replace("ى", "ي").replace("ة", "ه")
def clean(s): return re.sub(r"[ \t]+", " ", re.sub(r"\s*\([٠-٩]+\)\s*", " ", s or "")).strip()   # = Alfiyya352.clean
def halves(ar):
    c = clean(ar); m = re.split(r"\s*\.\.\.\s+", c, maxsplit=1)
    return m if len(m) == 2 and m[0] and m[1] else None
GENERIC = {"معرب", "مبني", "مرفوع", "منصوب", "مجرور", "مجزوم", "مضارع", "نصب", "هي"}
def loose(rx): return all(a.strip("()^$ ") in GENERIC for a in rx.split("|"))

# ── units
babs = [b for b in toc["babs"] if b["verses"]]   # the editor's appendix «تكملة» has no verse of the Alfiyya
groups, i = [], 0
while i < len(babs):
    g = [babs[i]]; nv = len(babs[i]["verses"]); i += 1
    while nv < 6 and i < len(babs) and len(babs[i]["verses"]) < 12:
        g.append(babs[i]); nv += len(babs[i]["verses"]); i += 1
    groups.append(g)
units = []   # each: parts = [(bab, [toc units])], part (0 / 1 / 2)
for g in groups:
    if len(g) == 1 and len(g[0]["verses"]) > 30:
        b = g[0]; us = b["units"]; tot = sum(len(u["verses"]) for u in us); acc = 0; k = 0
        while k < len(us) and acc + len(us[k]["verses"]) <= tot / 2: acc += len(us[k]["verses"]); k += 1
        k = max(1, k)
        units.append({"parts": [(b, us[:k])], "half": 1}); units.append({"parts": [(b, us[k:])], "half": 2})
    else:
        units.append({"parts": [(b, b["units"]) for b in g], "half": 0})

def page_units(sp):   # every commentary unit (book-wide) whose page span holds sp
    return [(b, u) for b in babs for u in b["units"] if u["from"] <= sp <= u["to"]]
def verses_at(bab, sp):   # the verse(s) of the commentary unit of this bāb that a page belongs to (the last one starting at or before it)
    us = [u for u in bab["units"] if u["from"] <= sp]
    return (us[-1]["verses"] if us else bab["units"][0]["verses"]) if bab["units"] else []
def in_part(bab, tus, sp):   # a split bāb: the first half holds the pages before the second half's first commentary unit
    us = bab["units"]
    if len(tus) == len(us): return True
    if tus[0] is us[0]: return sp < us[len(tus)]["from"]
    return sp >= tus[0]["from"]

E = led["entries"]; byb = {}
for e in E: byb.setdefault(e["bab"], []).append(e)

# ── the unit's grammar notes: the notes an Elfiye card of its verses already sits on (alfiyya.json), then the naḥw / ṣarf notes whose
# commentary-link topics meet the topics of the unit's ledger rows (content/rules/commentary_links.json — aqil_alfiyya.py's join); ≤ 4
LINKS = R("content/rules/commentary_links.json")["links"]
NOTE_T = {x["topic"][5:]: set(x["topics"]) for x in LINKS if x["topic"].startswith("note:") and (ROOT / "content/grammar" / (x["topic"][5:] + ".json")).exists()}
def note_level(g):
    try: return json.loads((ROOT / "content/grammar" / (g + ".json")).read_text(encoding="utf-8")).get("level") or 0
    except Exception: return 0
def unit_notes(U):
    tops = {}; out = []
    for b, tus in U["parts"]:
        for tu in tus:
            for n in tu["verses"]:
                for g in (AV.get(n) or {}).get("notes") or []:
                    if g not in out and g in NOTE_T: out.append(g)
        for e in byb.get(b["bab"], []):
            if in_part(b, tus, e["shamela"]):
                for t in e.get("topics") or []: tops[t] = tops.get(t, 0) + 1
    tk = set(tops)
    cand = sorted((g for g, ts in NOTE_T.items() if ts & tk and g not in out), key=lambda g: (-sum(tops.get(t, 0) for t in NOTE_T[g] & tk), len(NOTE_T[g]), g))
    return (out + cand)[:4]
for U in units: U["notes"] = unit_notes(U)

# ── the page half's input
probes, pkey = [], {}
for e in E:
    if e["status"] != "applied" or e.get("warn"): continue
    for k, p in enumerate(e.get("probes") or []):
        if not p.get("ok"): continue   # proved only by our vowels (or not at all): never shown, never asked
        q = {"s": p["s"], "w": p["w"], "re": p["re"]} if p.get("w") else {"s": p["s"], "any": p["any"]}
        pkey[(e["id"], k)] = len(probes); probes.append(q)
corpus_in = []
for ui, U in enumerate(units):
    rx = []
    for b, tus in U["parts"]:
        for e in byb.get(b["bab"], []):
            if e["status"] != "applied" or not in_part(b, tus, e["shamela"]): continue
            for p in e.get("probes") or []:
                r0 = p.get("re") or p.get("any")
                if (p.get("ok") or p.get("svok")) and r0 and not loose(r0) and H(r0) not in rx: rx.append(H(r0))   # the ruling's wording (a vowelled proof's regex too: only the corpus is shown)
    corpus_in.append({"u": "U%02d" % (ui + 1), "re": rx, "notes": U["notes"]})
topics_all = sorted({t for e in E for t in e.get("topics") or []})
inp = {"probes": probes, "corpus": corpus_in, "topics": topics_all}
sig = hashlib.sha256(json.dumps(inp, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]
if "--no-prove" in sys.argv and CACHE.exists():
    got = json.loads(CACHE.read_text(encoding="utf-8"))
    if got.get("sig") != sig: print("warning: the cache was made for other input (sig %s, now %s)" % (got.get("sig"), sig))
else:
    tmp_in, tmp_out = ROOT / "tools/.alfcourse-in.json", ROOT / "tools/.alfcourse-out.json"
    tmp_in.write_text(json.dumps(inp, ensure_ascii=False), encoding="utf-8")
    subprocess.run(["node", str(ROOT / "tools/alfiyya_course_probe.js"), str(tmp_in), str(tmp_out)], check=True)
    got = json.loads(tmp_out.read_text(encoding="utf-8")); got["sig"] = sig
    CACHE.write_text(json.dumps(got, ensure_ascii=False), encoding="utf-8"); tmp_in.unlink(); tmp_out.unlink()
PR, CORP, TOP = got["probes"], got["corpus"], got["topics"]

# ── the editor's printed iʿrāb of a shāhid: the first «الاعراب:» after the bayt, before the next bayt, to the line's end
def editor_irab(sh, nxt_ar):
    j = SRC.find(sh["ar"]);
    if j < 0: return None
    k = SRC.find("الاعراب:", j, j + 4000)
    if k < 0: return None
    if nxt_ar:
        jn = SRC.find(nxt_ar, j + 1)
        if 0 <= jn < k: return None
    end = SRC.find("\n", k); end = len(SRC) if end < 0 else end
    t = SRC[k:end]
    for stop in ("الشاهد فيه", " ="):
        z = t.find(stop)
        if z > 0: t = t[:z]
    t = t.rstrip(" ،=")
    if len(t) > 700:   # cut at a word boundary; shown with «…»
        t = t[:700]; t = t[:t.rfind(" ")]
    return t if len(t) > 20 else None

# ── «söylenir mi?»
STOP = r"(?=\s(?:كما|لأن|لئلا|على|تريد|وظاهر|بل|أو|وتقع|لأنه|فلا|وكالمصادر|وكذلك|ولا|وفى|وفي)(?:\s|$)|[.:،]|$)"
TAIL = {"وإنما", "بقطع", "ولا", "وقد", "وهو", "وهي", "لأن", "كما", "ومنه"}   # a cut that ran into the commentary: the form is not shown
EDITOR_ROWS = {"A284.1", "A285.1"}   # the editor's footnote (منحة الجليل) leaked into the ledger's lines: not Ibn ʿAqīl's ruling
def forbidden(e):
    out = []
    for m in re.finditer(r"(?:^|\s)(?:ف|و)?لا تقول\s+(.+?)" + STOP, e["ar"]):
        out.append((m.group(1).strip(), m.end()))
        pos = m.end()
        while True:
            m2 = re.match(r"\s+ولا\s+(?!تقول|يجوز|توسطها)(.+?)" + STOP, e["ar"][pos:])
            if not m2: break
            out.append((m2.group(1).strip(), pos + m2.end())); pos += m2.end()
    keep = []
    for x, end in out:
        after = e["ar"][end:end + 12]
        if re.match(r"\s*(على أن|تريد)", after): continue   # meaning-bound: the form alone is not what the book forbids
        if 1 <= len(x.split()) <= 7 and x in e["ar"] and x.split()[-1] not in TAIL: keep.append(x)
    return keep
def allowed(e):
    if e["id"] in EDITOR_ROWS or e["status"] != "applied" or not re.search(r"(^|\s)[وف]?يجوز\s", e["ar"]) or re.search(r"لا يجوز|لم يجز|يمتنع|لا تقول", e["ar"]): return []
    out = []
    for x in e["ex"]:
        z = e["ar"].find(x)
        if z > 0 and re.search(r"(?:^|\s)[وف]?تقول:?\s*$", e["ar"][max(0, z - 8):z]) and any(p.get("ok") and p["s"] == x for p in e.get("probes") or []) and x.split()[-1] not in TAIL: out.append(x)
    return out

course = {"about": "built by tools/alfiyya_course.py (v358-A) from toc_ibn_aqil.json, alfiyya.json, coverage_ibn_aqil.json and the source's editor notes; "
          "Arabic verbatim; e = the engine's line on the printed example, t = its own words for the role (only t is shown: the rest of a line on unvowelled letters — the part of speech, an estimated sign — is a guess that moves with the page's state)", "babs": [], "verses": {}, "units": [], "skipped": {}}
SK = course["skipped"]
def skip(k): SK[k] = SK.get(k, 0) + 1
bab_ix = {}
for ui, U in enumerate(units):
    uid = "U%02d" % (ui + 1); vs = []; vgroups = []; rul = []; exs = []; qs = []; sh_out = []; tops = {}
    for b, tus in U["parts"]:
        if b["bab"] not in bab_ix: bab_ix[b["bab"]] = len(course["babs"]); course["babs"].append(b["bab"])
        for tu in tus:
            g = [n for n in tu["verses"]]
            vs += g; v0 = AV.get(g[0]) or {}
            vgroups.append({"v": g, "r": v0.get("rule_ar") or "", "rp": v0.get("rule_page") or v0.get("page"), "rs": v0.get("rule_sp") or v0.get("sp")})
        ents = [e for e in byb.get(b["bab"], []) if in_part(b, tus, e["shamela"])]
        for e in ents:
            st = {"applied": "a", "not-automatable": "n", "open": "o", "noted": "d"}[e["status"]] if not e.get("warn") else "w"
            rul.append({"id": e["id"], "ar": e["ar"], "st": st, "p": e["page"]})
            for t in e.get("topics") or []: tops[t] = tops.get(t, 0) + 1
            if e["status"] != "applied":
                if e.get("probes"): skip("not applied (⚠ / open / n-a): no example, no question")
                continue
            for k, p in enumerate(e.get("probes") or []):
                if not p.get("ok"):
                    skip("proved only by our vowels (sv): never shown, never asked" if p.get("svok") else "probe not proved"); continue
                r = PR[pkey[(e["id"], k)]]
                if not r.get("ok"): skip("the page half no longer proves it"); continue
                vn = verses_at(b, e["shamela"])
                if not p.get("w"): skip("a construction probe (the book names no word): the engine's word may not be the book's — not shown, not asked"); continue
                if r.get("clash"): skip("the engine's line contradicts itself (a noun's role on «فعل»): not shown"); continue
                if not any(x["s"] == p["s"] and x["w"] == r["w"] for x in exs):
                    if r.get("role") and r.get("t") and r.get("keyOk"): exs.append({"id": e["id"], "s": p["s"], "w": r["w"], "i": r["i"], "role": r["role"], "t": r["t"], "e": r["e"], "v": vn})
                    else: skip("example: the line's role is not the one the ruling names (or no role words): not shown")
                rx = p.get("re") or p.get("any")
                why = None
                if loose(rx): why = "the probe names a bare case / verb kind: shown, not asked"
                elif e.get("offered") or p.get("offered") or r.get("off"): why = "the line gives a second reading (او / وقيل / ويجوز): not asked"
                elif not r.get("role"): why = "no role read on the line (a particle / verb kind): not asked"
                elif not r.get("keyOk"): why = "the ruling's words on the line do not name the line's role (a construction, not a role): not asked"
                elif len(r.get("sibs") or []) < 2: why = "fewer than two siblings in the role's family: not asked"
                if why: skip(why); continue
                qid = "r:%s:%d" % (e["id"], k)
                if any(q["k"] == "r" and q["s"] == p["s"] and q["w"] == r["w"] for q in qs): continue
                sb = r["sibs"]; h0 = int(hashlib.md5(qid.encode()).hexdigest(), 16) % len(sb)   # three siblings, rotated by the question's id
                if not r.get("t"): skip("no role words on the line: not asked"); continue
                qs.append({"k": "r", "id": qid, "s": p["s"], "w": r["w"], "i": r["i"], "t": r["t"], "e": r["e"], "key": r["role"], "opts": (sb[h0:] + sb[:h0])[:3], "v": vn})
            # v — the example → its verse, only where the page lies in ONE commentary unit and that unit has ONE verse
            pu = page_units(e["shamela"])
            if len(pu) == 1 and len(pu[0][1]["verses"]) == 1 and pu[0][0] is b and any(p.get("ok") for p in e.get("probes") or []):
                s0 = next(p["s"] for p in e["probes"] if p.get("ok")); n = pu[0][1]["verses"][0]
                pool = [m for m in (x["n"] for x in b["verses"]) if m != n and (AV.get(m) or {}).get("rule_ar") != (AV.get(n) or {}).get("rule_ar")]
                pool.sort(key=lambda m: (abs(m - n), m))
                if len(pool) >= 3 and not any(q["k"] == "v" and q["s"] == s0 for q in qs):
                    qs.append({"k": "v", "id": "v:" + e["id"], "s": s0, "n": n, "opts": pool[:3]})
            elif e["status"] == "applied": skip("v: the page is not tied to ONE verse")
            for x in allowed(e): qs.append({"k": "s", "id": "s:%s:%s" % (e["id"], x), "ar": x, "said": True, "v": verses_at(b, e["shamela"]), "src": e["id"]})
        for e in ents:
            if e["status"] == "not-automatable" and "forbidden form" in (e.get("reason") or "") and e["id"] not in EDITOR_ROWS:
                for x in forbidden(e): qs.append({"k": "s", "id": "s:%s:%s" % (e["id"], x), "ar": x, "said": False, "v": verses_at(b, e["shamela"]), "src": e["id"]})
        shs = [s for s in b["shawahid"] if U["half"] == 0 or in_part(b, tus, s["sp"])]
        allsh = b["shawahid"]
        for s in shs:
            if len(sh_out) >= 2: break
            nx = allsh[allsh.index(s) + 1]["ar"] if allsh.index(s) + 1 < len(allsh) else None
            t = editor_irab(s, nx)
            if t: sh_out.append({"ar": s["ar"], "n": s.get("n"), "sp": s["sp"], "irab": t})
    # h — complete the verse: three other verses of the unit, the nearest first, their second halves all different
    for n in vs:
        hv = halves(AV[n]["ar"]) if n in AV else None
        if not hv: skip("h: the verse line has no « ... » between its halves"); continue
        pool = sorted((m for m in vs if m != n and halves(AV[m]["ar"]) and halves(AV[m]["ar"])[1] != hv[1]), key=lambda m: (abs(m - n), m))
        if len(pool) < 3: skip("h: fewer than three other verses in the unit"); continue
        qs.append({"k": "h", "id": "h:%d" % n, "n": n, "opts": pool[:3]})
    for n in vs:
        v = AV[n]; course["verses"][str(n)] = {k: v[k] for k in ("ar", "page", "sp", "en", "tr") if v.get(k)}
    ars = [x["ar"] for x in rul]
    for g in vgroups:
        if g["r"] in ars: g["ri"] = ars.index(g["r"]); del g["r"]   # the same sentence is one of the bāb's rulings: point at it
    tt = U["notes"]
    lv = min([note_level(g) for g in tt if note_level(g)] or [4])
    title = [b["bab"] for b, _ in U["parts"]]
    course["units"].append({"id": uid, "b": [bab_ix[t] for t in title], "half": U["half"], "lv": lv, "vg": vgroups, "rul": rul, "ex": exs,
                            "sh": sh_out, "topics": tt, "corpus": CORP.get(uid, []), "q": qs})
cnt = {"units": len(course["units"]), "verses": len(course["verses"]), "rulings": sum(len(u["rul"]) for u in course["units"]),
       "examples": sum(len(u["ex"]) for u in course["units"]), "shawahid_irab": sum(len(u["sh"]) for u in course["units"]),
       "corpus": sum(len(u["corpus"]) for u in course["units"]), "units_no_corpus": sum(1 for u in course["units"] if not u["corpus"])}
for k in "rhvs": cnt["q_" + k] = sum(1 for u in course["units"] for q in u["q"] if q["k"] == k)
cnt["q_s_said"] = sum(1 for u in course["units"] for q in u["q"] if q["k"] == "s" and q["said"])
course["counts"] = cnt
OUT.write_text(json.dumps(course, ensure_ascii=False, indent=0), encoding="utf-8")
raw = json.dumps({k: course[k] for k in ("babs", "verses", "units", "counts")}, ensure_ascii=False, separators=(",", ":")).encode()
import gzip
print(json.dumps(cnt, ensure_ascii=False)); print("skipped", json.dumps(SK, ensure_ascii=False)); print("bytes raw %d gzip %d" % (len(raw), len(gzip.compress(raw, 9))))
