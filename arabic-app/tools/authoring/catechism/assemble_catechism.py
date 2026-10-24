# -*- coding: utf-8 -*-
"""Assemble the catechism banks (wave 64): tools/authoring/catechism/<prefix>_qa_*.py (ITEMS lists) -> content/catechism/<book>.json.
Run from anywhere; paths are __file__-relative. Every note id must exist in content/grammar; an item with no surviving note fails the run.
Each item: id, n, q{en,tr}, a{en,tr}, ar[], notes[] (must exist in content/grammar), story/chapter (kept only when the item's
Arabic is found in that story's package, or the item names a chapter whose text carries it)."""
import importlib.util, json, re, glob, os, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]   # arabic-app
OUT = ROOT / "content/catechism"
def bare(s): return re.sub(r"[ً-ْٰـ]", "", s).replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ٱ", "ا")
GR = {p.stem for p in (ROOT / "content/grammar").glob("*.json")}
def chapters(story):
    out = {}
    for f in glob.glob(str(ROOT / f"content/samples/{story}/chapters/*.json")):
        n = int(os.path.basename(f)[:-5]); d = json.load(open(f, encoding="utf-8"))
        out[n] = " ".join(bare((t.get("s") or t.get("surface"))["full"]) for sn in d["sentences"] for t in sn["tokens"])
    return out
def assemble(book, story, title, source, prefix=None):
    items = []
    for f in sorted(HERE.glob(f"{prefix or book}_qa_*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); items += m.ITEMS
    chs = chapters(story) if story else {}
    bad = []; found = 0
    for it in items:
        it["id"] = f"{book}-q{it['n']}"
        for k in ("q", "a"):
            if not (it[k].get("en") and it[k].get("tr")): bad.append((it["id"], k))
        missing = [n for n in it.get("notes", []) if n not in GR]
        if missing: bad.append((it["id"], "notes:" + ",".join(missing)))
        it["notes"] = [n for n in it.get("notes", []) if n in GR] or []
        if not it["notes"]: bad.append((it["id"], "no note"))
        hit = None
        for a in it.get("ar", []):
            b = bare(a).split("،")[0].strip()
            words = b.split()
            probe = " ".join(words[:4]) if len(words) >= 4 else b
            for n, t in sorted(chs.items()):
                if probe and probe in t: hit = n; break
            if hit: break
        if hit: it["story"] = story; it["chapter"] = hit; found += 1
        else: it.pop("story", None); it.pop("chapter", None)
    out = {"book": book, "title": title, "source": source, "items": items}
    OUT.mkdir(exist_ok=True); (OUT / f"{book}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(book, "items", len(items), "anchored to a chapter", found, "problems", bad)
    if bad: sys.exit(f"{book}: unresolved items")
assemble("kafiya-turkce", "al-kafiya", {"ar": "سُؤَالَاتُ الْكَافِيَةِ", "en": "Questions on al-Kāfiya", "tr": "Kâfiye Soru-Cevapları"}, "research/sources/kafiya-turkce-sual-cevap.txt", prefix="kafiya")

assemble("mansubat", None, {"ar": "سُؤَالَاتُ الْمَنْصُوبَاتِ", "en": "Questions on the manṣūbāt", "tr": "Mansûbât Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="mansubat")

assemble("majrurat", "al-kafiya", {"ar": "سُؤَالَاتُ الْمَجْرُورَاتِ", "en": "Questions on the majrūrāt", "tr": "Mecrûrât Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="majrurat")
assemble("tawabi", "al-kafiya", {"ar": "سُؤَالَاتُ التَّوَابِعِ", "en": "Questions on the tawābiʿ", "tr": "Tevâbi' Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="tawabi")
assemble("mabni", "al-kafiya", {"ar": "سُؤَالَاتُ الْمَبْنِيَّاتِ وَالْأَسْمَاءِ", "en": "Questions on the built nouns and the noun's kinds", "tr": "Mebnîler ve İsim Kısımları Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="mabni")
assemble("fil", "al-kafiya", {"ar": "سُؤَالَاتُ الْفِعْلِ", "en": "Questions on the verb", "tr": "Fiil Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="fil")
assemble("harf", "al-kafiya", {"ar": "سُؤَالَاتُ الْحَرْفِ", "en": "Questions on the particle", "tr": "Harf Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="harf")
