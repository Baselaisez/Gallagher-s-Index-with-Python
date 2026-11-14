# -*- coding: utf-8 -*-
"""Assemble the catechism banks (wave 64, extended in wave 65): tools/authoring/catechism/<prefix>_qa_*.py (ITEMS lists)
-> content/catechism/<book>.json. Run from anywhere; paths are __file__-relative.

Each item: id, n, q{en,tr}, a{en,tr}, ar[], notes[] (every id must exist in content/grammar — an item with no surviving note fails
the run), story/chapter (kept only when the item's Arabic is found in that story's package by a four-word probe).

Wave 65 — the Arabic is the matn's BY CONSTRUCTION: after anchoring, every `ar` string whose bare letters are found as a
contiguous run of tokens in the anchored chapter is REPLACED by that run's own vowelled forms (`verified` counts them), so the
bank can never carry a vowelling the reviewed text does not. A string the chapter does not carry whole is kept as authored
and listed in the report; the smoke suite reads `verified` and holds a floor on it. A bank also declares its Elo `area`
(nahw by default; balagha for the Talkhīṣ and ʿalāqa sheets) so the game credits the right discipline."""
import importlib.util, json, re, glob, os, sys, pathlib, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]   # arabic-app
OUT = ROOT / "content/catechism"
def N(s): return unicodedata.normalize("NFC", s)
def bare(s): return re.sub(r"[ً-ْٰـ]", "", s).replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ٱ", "ا")
GR = {p.stem for p in (ROOT / "content/grammar").glob("*.json")}
def chapters(story):
    """{chapter n: (bare token list, full token list)} for every chapter of the story."""
    out = {}
    for f in glob.glob(str(ROOT / f"content/samples/{story}/chapters/*.json")):
        n = int(os.path.basename(f)[:-5]); d = json.load(open(f, encoding="utf-8"))
        fulls = [N((t.get("s") or t.get("surface"))["full"]) for sn in d["sentences"] for t in sn["tokens"]]
        out[n] = ([bare(x) for x in fulls], fulls)
    return out
def find_run(words, bares):
    """index of the first token run whose bare forms equal `words`, else -1"""
    k = len(words)
    if not k: return -1
    for i in range(len(bares) - k + 1):
        if bares[i] == words[0] and bares[i:i + k] == words: return i
    return -1
def assemble(book, story, title, source, prefix=None, area="nahw", anchor_from=1):
    items = []
    for f in sorted(HERE.glob(f"{prefix or book}_qa_*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); items += m.ITEMS
    chs = chapters(story) if story else {}
    bad = []; found = 0; verified = 0; kept = []
    for it in items:
        it["id"] = f"{book}-q{it['n']}"
        for k in ("q", "a"):
            if not (it[k].get("en") and it[k].get("tr")): bad.append((it["id"], k))
        missing = [n for n in it.get("notes", []) if n not in GR]
        if missing: bad.append((it["id"], "notes:" + ",".join(missing)))
        it["notes"] = [n for n in it.get("notes", []) if n in GR] or []
        if not it["notes"]: bad.append((it["id"], "no note"))
        it["ar"] = [N(a) for a in it.get("ar", [])]
        hit = None
        # the probe is a TOKEN RUN (the first four words, or all of a shorter string), never a substring — a bare
        # «لفظ» must not anchor inside «اللفظ»; chapters from `anchor_from` are searched first (the ʿalāqa sheet
        # belongs to the bayān fann, not to the maʿānī chapter that happens to quote the same āya)
        for a in it["ar"]:
            words = bare(a).split("،")[0].split()[:4]
            for n, (bs, _) in sorted(chs.items(), key=lambda kv: (kv[0] < anchor_from, kv[0])):
                if words and find_run(words, bs) >= 0: hit = n; break
            if hit: break
        if hit:
            it["story"] = story; it["chapter"] = hit; found += 1
            bs, fs = chs[hit]; v = 0; new = []
            for a in it["ar"]:
                i = find_run(bare(a).split(), bs)
                if i >= 0: new.append(" ".join(fs[i:i + len(bare(a).split())])); v += 1
                else: new.append(a); kept.append((it["id"], a[:40]))
            it["ar"] = new; it["verified"] = v; verified += 1 if v else 0
        else: it.pop("story", None); it.pop("chapter", None)
    out = {"book": book, "title": title, "source": source, "area": area, "items": items}
    OUT.mkdir(exist_ok=True); (OUT / f"{book}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(book, "items", len(items), "anchored", found, "verified", verified, "kept-as-authored", len(kept), "problems", bad)
    for k in kept: print("   kept", k[0], k[1])
    if bad: sys.exit(f"{book}: unresolved items")
assemble("kafiya-turkce", "al-kafiya", {"ar": "سُؤَالَاتُ الْكَافِيَةِ", "en": "Questions on al-Kāfiya", "tr": "Kâfiye Soru-Cevapları"}, "research/sources/kafiya-turkce-sual-cevap.txt", prefix="kafiya")

assemble("mansubat", None, {"ar": "سُؤَالَاتُ الْمَنْصُوبَاتِ", "en": "Questions on the manṣūbāt", "tr": "Mansûbât Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="mansubat")

assemble("majrurat", "al-kafiya", {"ar": "سُؤَالَاتُ الْمَجْرُورَاتِ", "en": "Questions on the majrūrāt", "tr": "Mecrûrât Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="majrurat")
assemble("tawabi", "al-kafiya", {"ar": "سُؤَالَاتُ التَّوَابِعِ", "en": "Questions on the tawābiʿ", "tr": "Tevâbi' Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="tawabi")
assemble("mabni", "al-kafiya", {"ar": "سُؤَالَاتُ الْمَبْنِيَّاتِ وَالْأَسْمَاءِ", "en": "Questions on the built nouns and the noun's kinds", "tr": "Mebnîler ve İsim Kısımları Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="mabni")
assemble("fil", "al-kafiya", {"ar": "سُؤَالَاتُ الْفِعْلِ", "en": "Questions on the verb", "tr": "Fiil Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="fil")
assemble("harf", "al-kafiya", {"ar": "سُؤَالَاتُ الْحَرْفِ", "en": "Questions on the particle", "tr": "Harf Soru-Cevapları"}, "research/sources/mensubat.txt", prefix="harf")
# wave 65 — the Iẓhār Q&A (Ottoman notebook, three bābs), the Talkhīṣ badīʿ sheet and the ʿalāqa sheet
assemble("izhar-amil", "izhar-al-asrar", {"ar": "سُؤَالَاتُ الْإِظْهَارِ: الْعَامِلُ", "en": "Questions on the Iẓhār: the governor", "tr": "İzhâr Soru-Cevapları: Âmil"}, "research/sources/izhar-sual-cevap.txt", prefix="izhar1")
assemble("izhar-mamul", "izhar-al-asrar", {"ar": "سُؤَالَاتُ الْإِظْهَارِ: الْمَعْمُولُ", "en": "Questions on the Iẓhār: the governed word", "tr": "İzhâr Soru-Cevapları: Ma'mûl"}, "research/sources/izhar-sual-cevap.txt", prefix="izhar2")
assemble("izhar-irab", "izhar-al-asrar", {"ar": "سُؤَالَاتُ الْإِظْهَارِ: الْإِعْرَابُ", "en": "Questions on the Iẓhār: the iʿrāb", "tr": "İzhâr Soru-Cevapları: İ'rab"}, "research/sources/izhar-sual-cevap.txt", prefix="izhar3")
assemble("badi", "talkhis-al-miftah", {"ar": "سُؤَالَاتُ الْبَدِيعِ", "en": "Questions on the badīʿ", "tr": "Bedî' Soru-Cevapları"}, "research/sources/talkhis-al-miftah-balagha.txt", prefix="badi", area="balagha")
assemble("alaka", "talkhis-al-miftah", {"ar": "سُؤَالَاتُ الْعَلَاقَةِ", "en": "Questions on the ʿalāqa", "tr": "Alâka Soru-Cevapları"}, "research/sources/alaka-suallar.txt", prefix="alaka", area="balagha", anchor_from=46)
# wave 66 — Molla Jāmī's sual-cevap on his sharḥ of the Kāfiya
assemble("jami", "al-kafiya", {"ar": "سُؤَالَاتُ مُلَّا جَامِي", "en": "Molla Jāmī's questions on al-Kāfiya", "tr": "Molla Câmî Soru-Cevapları"}, "research/sources/molla-cami-sual-cevap.txt", prefix="jami")
