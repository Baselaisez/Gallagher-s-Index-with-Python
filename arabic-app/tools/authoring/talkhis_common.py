# -*- coding: utf-8 -*-
"""Shared helpers for the Talkhis authoring scripts (ch55 onward): the token
builder, the glossary/morphology lookups across every package, the frame
builders (majaz, istiara, kinaya, badi) and the write-out that adds the
chapter, the manifest entry, the glossary and the notes."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PKG = ROOT / "content/samples/talkhis-al-miftah"
GR = ROOT / "content/grammar"
DIA = re.compile("[ً-ٰ]")
def bare(s): return DIA.sub("", s).replace("ـ", "")
def tok(full, lex, pos, grammar, ar, en, tr, punct=None, segments=None):
    t = {"surface": {"full": full, "smart": full, "bare": bare(full)}, "lex": lex, "pos": pos}
    if grammar: t["grammar"] = grammar
    t["irab"] = {"ar": ar, "en": en, "tr": tr}
    if segments: t["segments"] = segments
    if punct: t["punctAfter"] = punct
    return t
def seg(form, lex, pos): return {"form": form, "lex": lex, "pos": pos}
def g(lemma, root, pos, en, tr, level, plural=None, form=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    if form: e["form"] = form
    return e
_GL = None
def _all_gloss():
    global _GL
    if _GL is None:
        _GL = {}
        for p in sorted((ROOT / "content/samples").iterdir()):
            gp = p / "glossary.json"
            if gp.exists():
                for k, v in json.loads(gp.read_text(encoding="utf-8"))["entries"].items():
                    _GL.setdefault(k, v)
    return _GL
def find_gloss(key):
    d = _all_gloss()
    if key in d: return d[key]
    raise KeyError(key)
def has_gloss(key): return key in _all_gloss()
_has_gloss = has_gloss
def G(key, lemma, root, pos, en, tr, level, plural=None, form=None):
    """Reuse the entry a package already owns under this key (its lemma must be
    the same word) or build a new one — a key is a global claim."""
    if has_gloss(key):
        e = find_gloss(key)
        a = bare(e["lemma"]).split(" ")[0].replace("ال", "", 1) if bare(e["lemma"]).startswith("ال") else bare(e["lemma"]).split(" ")[0]
        b = bare(lemma).split(" ")[0].replace("ال", "", 1) if bare(lemma).startswith("ال") else bare(lemma).split(" ")[0]
        assert a == b, f"key {key} already means {e['lemma']}, not {lemma}"
        return e
    return g(lemma, root, pos, en, tr, level, plural, form)
def _key_word(lemma):
    w = bare(lemma).split("(")[0].strip().split(" ")[0]
    return w[2:] if w.startswith("ال") and len(w) > 3 else w
def find_morph(key):
    for p in sorted((ROOT / "content/samples").iterdir()):
        gp = p / "morphology.json"
        if gp.exists():
            d = json.loads(gp.read_text(encoding="utf-8"))["verbs"]
            if key in d: return d[key]
    raise KeyError(key)
def has_morph(key):
    try: find_morph(key); return True
    except KeyError: return False
def mj(word, kind, alaqa=None, haqiqa=None, murad=None, qarina=None, istiara=None):
    f = {"word": word, "kind": kind}
    if alaqa: f["alaqa"] = alaqa
    if haqiqa: f["haqiqa"] = haqiqa
    if murad: f["murad"] = murad
    if qarina is not None: f["qarina"] = qarina
    if istiara: f["istiara"] = istiara
    return f
def ist(lafz, ends=None, jami=None, hissi=None, seat=None, mulaim=None, minhu=None, lahu=None):
    d = {"lafz": lafz}
    if ends: d["ends"] = ends
    if jami: d["jami"] = jami
    if hissi: d["hissi"] = hissi
    if seat: d["qarinaSeat"] = seat
    if mulaim: d["mulaim"] = mulaim
    if minhu: d["mulaimMinhu"] = minhu
    if lahu: d["mulaimLahu"] = lahu
    return d
def kn(span, kind, lazim, sub=None, wasait=None, sakkaki=None, tasrih=None, head=None, mawsuf=None):
    """An authored KINAYA frame: the said (span of token indexes), the kind by
    what is sought (sifa / mawsuf / nisba), the meant (lazim), the rungs the mind
    climbs (wasait — zero for a qariba), Sakkaki's name, whether the wording
    carries a pronoun (the tasrih inside طَوِيلُ النِّجَادِ)."""
    f = {"span": list(span), "kind": kind, "lazim": lazim}
    if sub: f["sub"] = sub
    if wasait is not None: f["wasait"] = wasait
    if sakkaki: f["sakkaki"] = sakkaki
    if tasrih is not None: f["tasrih"] = tasrih
    if head is not None: f["head"] = head
    if mawsuf is not None: f["mawsuf"] = mawsuf
    return f
def bd(kind, pair, sub=None, cls=None):
    """An authored BADIʿ frame: the figure, the two token indexes it joins."""
    f = {"kind": kind, "pair": list(pair)}
    if sub: f["sub"] = sub
    if cls: f["class"] = cls
    return f
R_EN = " (Restored: the source carries this step only in Turkish.)"
R_TR = " (Geri yazım: kaynak bu adımı yalnız Türkçe taşır.)"
def kaq(tag, full="كَقَوْلِهِ", who="pron-3ms", punct=":"):
    pr = {"pron-3ms": "هِ", "pron-3mp": "هِمْ", "pron-2ms": "كَ", "pron-1p": "نَا"}[who]
    return tok(full, "qawl", "noun", [tag, "huruf-jarr", "idafa-definiteness"],
               "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ؛ قَوْلِ مَجْرُورٌ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.",
               "«as in the saying» — the kaf of «for instance», a wall: no likening.", "«sözü gibi» — «meselâ» kâfı, duvar: benzetme değil.",
               segments=[seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun"), seg(pr, who, "pron")], punct=punct)
def kawa(tag, full="وَكَقَوْلِهِ", who="pron-3ms"):
    t = kaq(tag, full, who, ":"); t["segments"].insert(0, seg("وَ", "wa", "conj")); return t
def taala(tag, punct=":"):
    return tok("تَعَالَى", "taala", "verb", [tag], "فِعْلٌ مَاضٍ جَامِدٌ فِي مَعْنَى الدُّعَاءِ — لَا يَجْرِي عَلَى اللهِ إِلَّا مَاضِيًا.",
               "«exalted is He» — the frozen mazi of praise.", "«teâlâ» — duâ mânâsında donmuş mâzî.", punct=punct)
def saw(tag, punct=":"):
    return tok("ﷺ", "salla-allahu", "part", [tag], "جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«peace be upon him» — a parenthetical prayer.", "«sallallâhu aleyhi ve sellem» — mu'terize dua.", punct=punct)
def write_out(n, S, title, add_en, add_tr, marker, gloss_add, notes=(), related=()):
    man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
    (PKG / f"chapters/{n}.json").write_text(json.dumps({"chapter": n, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
    if not any(c["n"] == n for c in man["chapters"]):
        man["chapters"].append({"n": n, "title": title})
    man["chapters"].sort(key=lambda c: c["n"])
    man["version"] = f"0.{n}.0"
    if marker not in man["attribution"]["en"]:
        man["attribution"]["en"] += add_en
        man["attribution"]["tr"] += add_tr
    (PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
    gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
    other = {}
    for p in (ROOT / "content/samples").iterdir():
        if p.name == PKG.name or not (p / "glossary.json").exists(): continue
        for k, v in json.loads((p / "glossary.json").read_text(encoding="utf-8"))["entries"].items():
            other.setdefault(k, set()).add(bare(v["lemma"]).split(" ")[0])
    for k, v in gloss_add.items():
        if k in gl["entries"]:
            assert _key_word(gl["entries"][k]["lemma"]) == _key_word(v["lemma"]), f"key {k} already means {gl['entries'][k]['lemma']}"
            continue
        if k in other:
            assert bare(v["lemma"]).split(" ")[0] in other[k], f"key {k} means something else elsewhere: {other[k]}"
        gl["entries"][k] = v
    (PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
    for nt in notes:
        (GR / f"{nt['id']}.json").write_text(json.dumps(nt, ensure_ascii=False, indent=1), encoding="utf-8")
    for nid, add in related:
        fp = GR / f"{nid}.json"
        if not fp.exists(): continue
        w = json.loads(fp.read_text(encoding="utf-8")); ch = False
        for a in add:
            if a not in w.get("relatedNotes", []): w.setdefault("relatedNotes", []).append(a); ch = True
        if ch: fp.write_text(json.dumps(w, ensure_ascii=False, indent=1), encoding="utf-8")
def put_morph(mo, key, e):
    if key not in mo["verbs"]: mo["verbs"][key] = e
def report(n, S, gloss_add, notes):
    def cnt(k): return sum(len(x[k]) if isinstance(x.get(k), list) else (1 if x.get(k) else 0) for x in S)
    print(f"talkhis ch{n}:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(gloss_add),
          "; notes", [nt["id"] for nt in notes], "; majaz", cnt("majaz"), "tashbih", cnt("tashbih"), "kinaya", cnt("kinaya"), "badi", cnt("badi"))

_has_morph = has_morph
