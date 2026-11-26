"""(v352-A) Ibn ʿAqīl's Sharḥ on the Alfiyya — the shared reading of research/sources/sharh-ibn-aqil-src.txt.

Every page header reads `=== p. <shamela page> (<vol>:<printed page>) [<section>] ===`; a page is its matn, then «--- hashiya ---»
(volumes 1–2: the editor Muḥyī al-Dīn ʿAbd al-Ḥamīd's «منحة الجليل»). Nothing here rewrites a received line: every cut is a
verbatim substring of the file (`ar` fields are checked by the smoke check «v352-A …»).

The naẓm is told from the prose by script:
  * a matn line with « ... » between two hemistichs (< 140 characters), or a hemistich line followed by a line opening «... »;
  * a SHĀHID when it opens with the edition's number «١٢ - », when the number stands alone on the line before, when it follows a
    shāhid line directly (a shāhid of several verses), or when the prose before it ends with «:» (كقوله: / قول الشاعر:) — except
    «المراد بقوله:» / «أشار بقوله:» / «قال المصنف …:» which introduce the Alfiyya's own verse;
  * otherwise a verse of the ALFIYYA (in vols 1–2 it carries the editor's footnote mark, whose note is its iʿrāb).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "research/sources/sharh-ibn-aqil-src.txt"
REL = "research/sources/sharh-ibn-aqil-src.txt"
HDR = re.compile(r"^=== p\. (\d+) \((\d+):(\d+)\) \[(.*)\] ===$", re.M)
HASH = "\n--- hashiya ---\n"
A2L = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
_DIA = re.compile("[ً-ٰٟـۖ-ۭ]")
FN = re.compile(r"\s*\([٠-٩]+\)\s*")   # the editor's footnote marks inside a matn line


def norm(s):
    s = _DIA.sub("", s or "")
    s = re.sub("[أإآٱ]", "ا", s).replace("ى", "ي").replace("ة", "ه").replace("ؤ", "و").replace("ئ", "ي")
    return s


def text():
    return SRC.read_text(encoding="utf-8")


def pages(t=None):
    t = t or text()
    ms = list(HDR.finditer(t))
    out = []
    for i, m in enumerate(ms):
        s = m.end() + 1
        e = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        h = t.find(HASH, s, e)
        out.append({"sp": int(m.group(1)), "vol": int(m.group(2)), "pp": int(m.group(3)), "sec": m.group(4).strip(),
                    "start": s, "end": e, "matn_end": h if h != -1 else e})
    # a volume's first page is headed by the volume's name: it opens the next page's bāb
    for i in range(len(out) - 2, 0, -1):
        if out[i]["sec"].startswith("المجلد") and not out[i + 1]["sec"].startswith("المجلد"):
            out[i]["sec"] = out[i + 1]["sec"]
    return t, out


# the editor's / index pages and the volume title pages: not the sharḥ's bābs
NOT_BAB = {"المجلد الأول", "المجلد الثاني", "المجلد الثالث", "المجلد الرابع", "مقدمة الطبعة الثانية", "مقدمة المحقق",
           "الفهارس", "فهرس"}


def matn_lines(t, ps):
    """[(page, offset, line)] — every line of every page's matn, with its file offset."""
    rows = []
    for p in ps:
        off = p["start"]
        for ln in t[p["start"]:p["matn_end"]].split("\n"):
            rows.append((p, off, ln))
            off += len(ln) + 1
    return rows


def rhymes(v):
    """the Alfiyya is rajaz muzdawij: both hemistichs of a verse end on one rhyme letter — a shāhid's verse mostly does not."""
    a, _, b = bare(norm(v)).partition(" ... ")
    a, b = re.sub("[^ء-ي]", "", a), re.sub("[^ء-ي]", "", b)
    a = re.sub("[اي]$", "", a) if len(a) > 2 else a
    b = re.sub("[اي]$", "", b) if len(b) > 2 else b
    return a[-1:] == b[-1:]


def _isv(ln):
    return " ... " in ln and len(ln) < 140


# read by hand: verses the rules above take for the Alfiyya's and that are a shāhid's (the second verse of a numbered shāhid that
# happens to rhyme within itself, a verse brought by «قال المصنف ويحتمل أن يكون منه قوله:», al-Nābigha al-Jaʿdī's verse in the
# taṣrīf). Matched on the verse's opening words.
SHAHID_BY_HAND = ("وماذا تبتغي الشعراء", "وحلت سواد القلب", "أبحنا حيهم قتلا", "إذا بكيت قبلتني", "تنتهض الرعدة",
                  "فمن يك لم يثأر")


def classify(rows):
    """per row: None (prose) | 'alf' | 'alf-half' (the first hemistich of a split verse) | 'shahid' | 'shahid+'.
    Returns the list and, for 'alf', the verse text (the row, or the two rows joined for a split verse)."""
    cls = [None] * len(rows)
    for i, (p, off, ln) in enumerate(rows):
        nxt = rows[i + 1][2] if i + 1 < len(rows) else ""
        if not _isv(ln):
            if ln.startswith("... ") and i and cls[i - 1] == "alf-half":
                cls[i] = "alf"
            elif nxt.startswith("... ") and len(ln) < 80 and ln.strip():
                cls[i] = "alf-half"
            continue
        j = i - 1
        while j >= 0 and not rows[j][2].strip():
            j -= 1
        prev = rows[j][2].strip() if j >= 0 else ""
        if re.match(r"^[٠-٩]+\s*-", ln) or re.match(r"^[٠-٩]+\s*-?$", prev) or re.search(r"[٠-٩]+\s*-$", prev):
            c = "shahid"
        elif FN.search(ln) and p["vol"] <= 2:
            c = "alf"
        elif j >= 0 and cls[j] in ("shahid", "shahid+") and not rhymes(ln):
            c = "shahid+"
        elif prev.endswith(":"):
            c = "alf" if re.search(r"(المراد|اشار|أشار) بقوله:$|^قال المصنف", prev) and "الكافية" not in prev else "shahid"
        else:
            c = "alf"
        if c == "alf" and ln.startswith(SHAHID_BY_HAND):
            c = "shahid+"
        cls[i] = c
    return cls


def verse_text(rows, cls, i):
    """the verse as printed, footnote marks cut off at its end only (a mark inside stays: the text is the file's)."""
    if cls[i] == "alf" and rows[i][2].startswith("... ") and i and cls[i - 1] == "alf-half":
        return rows[i - 1][2].strip() + "\n" + rows[i][2].strip(), rows[i - 1][1]
    return rows[i][2].strip(), rows[i][1]


def bare(v):
    """a verse for display / matching: footnote marks removed (the parts between are verbatim substrings)."""
    return re.sub(r"\s+", " ", FN.sub(" ", v)).strip()


def babs(ps):
    """[{bab, pages:[...]}] in book order; a section recurring later (none in this file) would open a new bāb."""
    out = []
    for p in ps:
        if not out or out[-1]["bab"] != p["sec"]:
            out.append({"bab": p["sec"], "pages": []})
        out[-1]["pages"].append(p)
    return out


def sentences(s):
    """prose → sentences at «.» / line ends; offsets kept relative to s."""
    out, k = [], 0
    for m in re.finditer(r"[^.\n]+[.]?", s):
        seg = m.group(0)
        if seg.strip():
            a = m.start() + (len(seg) - len(seg.lstrip()))
            out.append((a, seg.strip()))
    return out


if __name__ == "__main__":
    t, ps = pages()
    rows = matn_lines(t, ps)
    cls = classify(rows)
    from collections import Counter
    print(Counter(c for c in cls if c))
    sys.exit(0)
