"""(v352-U) shared reading of the two uṣūl books received 2026-11-26 — Ibn Jinnī's al-Khaṣāʾiṣ and al-Suyūṭī's al-Iqtirāḥ, page-marked
Shamela texts in research/sources. Same header grammar as tools/ilal/common.py; nothing here rewrites a received line — `pages()`
hands back offsets, so every cut downstream is a verbatim substring of the source file. In al-Iqtirāḥ «--- hashiya ---» is the
modern editor's «الإصباح» and is never read as al-Suyūṭī's: every reader here stops at `matn_end`."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ilal"))
from common import HASH, HDR, ROOT, SRC, norm  # noqa: E402,F401

BOOKS = {
    "khasais": {"file": "al-khasais-ibn-jinni-src.txt", "ar": "الخصائص", "en": "Ibn Jinnī, al-Khaṣāʾiṣ",
                "tr": "İbn Cinnî, el-Hasâis", "short_en": "Ibn Jinnī", "short_tr": "İbn Cinnî", "shamela": 9986},
    "iqtirah": {"file": "al-iqtirah-suyuti-src.txt", "ar": "الاقتراح في أصول النحو", "en": "al-Suyūṭī, al-Iqtirāḥ",
                "tr": "Süyûtî, el-İktirâh", "short_en": "al-Suyūṭī", "short_tr": "Süyûtî", "shamela": 14246},
}


def text(book):
    return (SRC / BOOKS[book]["file"]).read_text(encoding="utf-8")


def pages(book):
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


def matn_lines(book):
    """[(page dict, line text, offset)] over the matn only."""
    t, ps = pages(book)
    out = []
    for p in ps:
        off = p["start"]
        for ln in t[p["start"]:p["matn_end"]].split("\n"):
            out.append((p, ln, off))
            off += len(ln) + 1
    return t, ps, out


AR_DIG = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")


def on_page(book, sp, ar, t=None, ps=None):
    """True when `ar` is a verbatim substring of Shamela page `sp`'s matn (never the editor's hashiya)."""
    if t is None:
        t, ps = pages(book)
    p = next((q for q in ps if q["sp"] == sp), None)
    return bool(p) and ar in t[p["start"]:p["matn_end"]]
