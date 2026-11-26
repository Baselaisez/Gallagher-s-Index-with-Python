"""(v348-F) shared reading of the three commentaries received 2026-11-26 — page-marked Shamela texts in research/sources.

Every page header reads `=== p. <shamela page> (<vol>:<printed page>) [<section>] ===`; a page's text is its matn, then
«--- hashiya ---» and the editor's footnotes. Nothing here rewrites a received line: `pages()` hands back the raw text of each
page with its offset in the file, so every cut made downstream is a verbatim substring."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "research/sources"

BOOKS = {
    "shaykhzade": {"file": "sharh-qawaid-al-irab-shaykhzade-src.txt", "ar": "شرح قواعد الإعراب لشيخ زاده",
                   "en": "Shaykhzāde, Sharḥ Qawāʿid al-Iʿrāb", "tr": "Şeyhzâde, Şerhu Kavâidi'l-İ'râb", "short_tr": "Şeyhzâde",
                   "short_en": "Shaykhzāde", "shamela": 19236},
    "ibn-malik": {"file": "sharh-al-kafiya-al-shafiya-ibn-malik-src.txt", "ar": "شرح الكافية الشافية لابن مالك",
                  "en": "Ibn Mālik, Sharḥ al-Kāfiya al-Shāfiya", "tr": "İbn Mâlik, Şerhu'l-Kâfiyeti'ş-Şâfiye", "short_tr": "İbn Mâlik",
                  "short_en": "Ibn Mālik", "shamela": None},
    "radi": {"file": "sharh-al-shafiya-radi-src.txt", "ar": "شرح شافية ابن الحاجب للرضي",
             "en": "al-Raḍī, Sharḥ al-Shāfiya", "tr": "Radî, Şerhu'ş-Şâfiye", "short_tr": "Radî", "short_en": "al-Raḍī",
             "shamela": None},
}

HDR = re.compile(r"^=== p\. (\d+) \((\d+):(\d+)\) \[(.*)\] ===$", re.M)
HASH = "\n--- hashiya ---\n"
_DIA = re.compile("[ً-ٰٟـۖ-ۭ]")


def norm(s):
    """letters only, for matching — never for output: diacritics and tatweel out, the alif / yāʾ / tāʾ marbūṭa forms folded."""
    s = _DIA.sub("", s or "")
    s = re.sub("[أإآٱ]", "ا", s).replace("ى", "ي").replace("ة", "ه").replace("ؤ", "و").replace("ئ", "ي")
    return s


def text(book):
    return (SRC / BOOKS[book]["file"]).read_text(encoding="utf-8")


def pages(book):
    """[{sp, vol, pp, sec, start, end, matn_end}] — start/end are offsets of the page body in the file; matn_end stops before
    the footnotes."""
    t = text(book)
    ms = list(HDR.finditer(t))
    out = []
    for i, m in enumerate(ms):
        s = m.end() + 1
        e = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        h = t.find(HASH, s, e)
        out.append({"sp": int(m.group(1)), "vol": int(m.group(2)), "pp": int(m.group(3)), "sec": m.group(4).strip(),
                    "start": s, "end": e, "matn_end": h if h != -1 else e})
    return t, out
