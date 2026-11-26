"""Index al-Bakrī's «فصل المقال في شرح كتاب الأمثال» BY SCRIPT (v348-A) → content/rules/amthal_index.json.

Reads research/sources/fasl-al-maqal-bakri-src.txt (Shamela 1025, pp. 1–530; matn, then «--- hashiya ---»). Only the matn is read.
The book is Abū ʿUbayd's Kitāb al-amthāl with al-Bakrī's commentary: each entry opens «قال أبو عبيد» and quotes the proverb between
" … "; al-Bakrī's commentary follows after «ع:». A record per quoted proverb of an Abū ʿUbayd entry:
  n, mathal_ar (verbatim, as the e-text prints it), bab (the Shamela section = the book's bāb, and its heading), sub (the numbered
  «N - باب …» heading in force), page {shamela, printed}, entry (the entry number — proverbs quoted in one entry share it),
  au_words / bakri_words (the length of Abū ʿUbayd's and al-Bakrī's text for that entry), kind (narrative | note — by a marker count:
  people, a sequence of events, speech), markers, crossesPage, and `story` (the package that carries the tale, where one does).
Every `*_ar` string is a verbatim substring of the matn as the script reads it (page headers and the ḥāshiya removed).
Run: python3 tools/sources/amthal_index.py
"""
import json, re, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "research/sources/fasl-al-maqal-bakri-src.txt"
OUT = ROOT / "content/rules/amthal_index.json"
HEAD = re.compile(r"^=== p\. (\d+) \((\d+):(\d+)\) \[([^\]]*)\] ===$")

def matn():
    """the matn of every page joined by newlines, with (offset, shamela page, printed page, section) marks"""
    out, marks, keep, cur = [], [], False, None
    pos = 0
    for line in SRC.read_text(encoding="utf-8").split("\n"):
        m = HEAD.match(line)
        if m:
            cur = (int(m.group(1)), f"{m.group(2)}:{m.group(3)}", m.group(4)); keep = True
            marks.append((pos,) + cur); continue
        if line == "--- hashiya ---": keep = False; continue
        if keep and cur:
            out.append(line); pos += len(line) + 1
    return "\n".join(out), marks

def where(marks, off):
    lo = None
    for mk in marks:
        if mk[0] <= off: lo = mk
        else: break
    return lo

ENTRY = re.compile(r"قال أبو عبيد")
BAKRI = re.compile(r"(?:^|[\s>.؟])ع\s?:")
QUOTE = re.compile(r'"\s*([^"]{2,160}?)\s*"')
SUB = re.compile(r"([٠-٩]+)\s*-[\s؟]*(باب [^\n]*?)(?=\s*قال أبو عبيد|\n|$)")
NARR = re.compile(r"\b(?:فقال|فقالت|فلما|ولما|فأتى|فأتاه|فأتاها|فخرج|خرج|فبعث|بعث|فأخذ|أقبل|فأقبل|ثم|حتى|فجاء|جاء|فدخل|دخل|فسأل|سأل|فرأى|رأى|فقتل|قتل|فذهب|ذهب|فمر|مر|وكان|كان|فنزل|نزل|فركب|ركب)\b")
NOISE = re.compile(r"^[.،:؟]|^(?:وقال|قال|فقال|وذكر)\s")   # a quote mark paired across two quotations, not a proverb
WORD = re.compile(r"[ء-ي]+")
TASHKIL = re.compile("[ً-ْٰـ]")

# the proverb packages (tools/authoring/author_mathal_*.py): Shamela page of the entry → the record(s) whose tale the package carries
STORIES = {
    "mathal-sabaqa-al-sayf-al-adhal": (79, {"الحديث ذو شجون", "أسعد أم سعيد", "إن الحديث ذو شجون", "سبق السيف العذل"}),
    "mathal-ati-al-qaws-bariha": (310, {"أعط القوس باريها"}),
    "mathal-bi-khuffay-hunayn": (366, {"رجع فلان من حاجته بخفي حنين"}),
    "mathal-asa-al-ghuwayr-abusan": (436, {"عسى الغوير أبؤساً"}),
    "mathal-asmin-kalbaka-yakulka": (431, {"أسمن كلبك يأكلك"}),
    "mathal-kilahuma-wa-tamran": (122, {"كلاهما وتمرا"}),
    "mathal-istanwaqa-al-jamal": (202, {"قد استنوق الجمل", "استنوق الجمل"}),
    "mathal-arafatni-nasaaha-allah": (90, {"عرفتني نسأها الله"}),
    "mathal-al-maru-yajizu": (311, {"المرء يعجز لا المحالة"}),
    "mathal-wafaqa-shannun-tabaqah": (274, {"وافق شناً طبقه"}),
    "mathal-inda-al-sabah": (345, {"اتخذ الليل جملاً", "عند الصباح يحمد القوم السرى"}),
}

def words(s): return len(WORD.findall(TASHKIL.sub("", s)))

def build():
    text, marks = matn()
    starts = [m.start() for m in ENTRY.finditer(text)]
    sections = []                      # the Shamela sections with their first heading line
    for mk in marks:
        if not sections or sections[-1]["name"] != mk[3]: sections.append({"name": mk[3], "from": mk[1]})
    subs = [(m.start(), m.group(1), re.sub(r"\s+", " ", m.group(2)).strip()) for m in SUB.finditer(text)]
    recs, entries = [], 0
    for i, s in enumerate(starts):
        e = starts[i + 1] if i + 1 < len(starts) else len(text)
        seg = text[s:e]
        b = BAKRI.search(seg)
        au, bk = (seg[:b.start()], seg[b.end():]) if b else (seg, "")
        qs = [q for q in QUOTE.finditer(au) if not NOISE.match(q.group(1).strip())]
        mk = where(marks, s)
        if mk[3] in ("مقدمة التحقيق", "تحقيق الكتاب", "نسخ الكتاب", "منهجنا في التحقيق", "فصل المقال في شرح كتاب الأمثال"): continue
        entries += 1
        sub = None
        for so, num, title in subs:
            if so <= s: sub = {"n": num, "ar": title}
        narr = len(NARR.findall(TASHKIL.sub("", au[qs[0].end():] if qs else au))) + len(NARR.findall(bk))
        tale_w = words(bk) + (words(au[qs[-1].end():]) if qs else 0)
        kind = "narrative" if narr >= 6 and tale_w >= 60 else "note"
        for q in qs or [None]:
            ar = re.sub(r"\s+", " ", q.group(1)).strip() if q else None
            off = s + (q.start(1) if q else 0)
            p = where(marks, off)
            p_end = where(marks, s + (q.end(1) if q else 0))
            recs.append({"n": len(recs) + 1, "entry": entries, "mathal_ar": ar, "shape": "quoted" if q else "unquoted",
                         "head_ar": None if q else re.sub(r"\s+", " ", au[:90]).strip(),
                         "bab": p[3], "sub": sub, "page": {"shamela": p[1], "printed": p[2]}, "crossesPage": p_end[1] != p[1],
                         "au_words": words(au), "bakri_words": words(bk), "tale_words": tale_w, "markers": narr, "kind": kind, "kindBy": "markers"})
    return text, sections, recs

if __name__ == "__main__":
    text, sections, recs = build()
    c = collections.Counter(r["kind"] for r in recs if r["mathal_ar"])
    data = {"source": {"book": "فصل المقال في شرح كتاب الأمثال", "author": "أبو عبيد البكري (ت ٤٨٧)", "matn_of": "كتاب الأمثال لأبي عبيد القاسم بن سلام",
                       "edition": "تحقيق إحسان عباس وعبد المجيد عابدين، مؤسسة الرسالة ١٩٧١", "shamela": 1025,
                       "file": "research/sources/fasl-al-maqal-bakri-src.txt"},
            "how": "cut by script (tools/sources/amthal_index.py): one record per proverb quoted between \" \" in an entry that opens «قال أبو عبيد»; "
                   "al-Bakrī's commentary is what follows «ع:» up to the next entry. kind is a marker count (narrative verbs/particles ≥ 6 and ≥ 60 words of tale), "
                   "not a reading; the chosen stories were read whole.",
            "counts": {"entries": max(r["entry"] for r in recs), "records": len(recs), "quoted": sum(1 for r in recs if r["mathal_ar"]),
                       "unquoted": sum(1 for r in recs if not r["mathal_ar"]), "narrative": c["narrative"], "note": c["note"],
                       "babs": len({r["bab"] for r in recs})},
            "babs": [s for s in sections if s["name"].startswith("الباب")],
            "records": recs}
    for r in recs:                                  # the packages that carry a record's tale (authored, v348-A)
        for slug, (page, keys) in STORIES.items():
            if r["page"]["shamela"] == page and r["mathal_ar"] in keys: r["story"], r["kind"], r["kindBy"] = slug, "narrative", "read"
    linked = {r.get("story") for r in recs} - {None}
    assert linked == set(STORIES), ("every story package links to its proverb's record", set(STORIES) - linked)
    data["counts"]["withStory"] = sum(1 for r in recs if r.get("story"))
    c = collections.Counter(r["kind"] for r in recs if r["mathal_ar"])
    data["counts"]["narrative"], data["counts"]["note"] = c["narrative"], c["note"]
    OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(data["counts"])
