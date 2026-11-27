"""Arabic script as units: one letter with the marks it carries.

Inside the engine every hamza is the bare «ء» and «آ» is «ءَا»; the hamza
takes its seat again only when a built form is shown (:func:`seat`).
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import List, Optional

FATHA, DAMMA, KASRA = "َ", "ُ", "ِ"
SHORT = FATHA + DAMMA + KASRA
TANWIN = "ًٌٍ"
SUKUN, SHADDA = "ْ", "ّ"
WEAK = "وياى"
_MARK = re.compile("[ً-ْٰ]")


@dataclass
class Unit:
    """A letter, its marks, and — for a template slot — which radical it is."""

    c: str
    m: str = ""
    r: Optional[int] = None        # 0 fāʾ, 1 ʿayn, 2 lām
    origin: Optional[str] = None   # what an alif came from


def parse(text: str) -> List[Unit]:
    out: List[Unit] = []
    for ch in unicodedata.normalize("NFC", text or ""):
        if _MARK.match(ch):
            if out:
                out[-1].m += ch
        elif not ch.isspace():
            out.append(Unit(ch))
    return out


def norm_marks(marks: str) -> str:
    """One canonical order: the shadda first, then the vowel or tanwīn."""
    seen: List[str] = []
    for ch in marks or "":
        if ch not in seen:
            seen.append(ch)
    return "".join([c for c in seen if c == SHADDA] + [c for c in seen if c != SHADDA])


def join(units: List[Unit]) -> str:
    return "".join(u.c + norm_marks(u.m) for u in units)


def vowel(marks: str) -> str:
    for ch in marks or "":
        if ch in SHORT:
            return ch
    return ""


def is_short(marks: str) -> bool:
    """True for a short vowel — and for a letter left bare: a weak letter whose
    vowel was just carried away (naql) still counts as «moved in its origin»,
    which is what lets مُقْوَمٌ reach مُقَامٌ.  Only a WRITTEN sukūn is silent."""
    rest = (marks or "").replace(SHADDA, "")
    return rest == "" or rest[0] in SHORT


def is_sakin(unit: Unit) -> bool:
    return unit.m in ("", SUKUN)


def is_weak(ch: str) -> bool:
    return ch in "وي"


def fold(text: str) -> str:
    s = unicodedata.normalize("NFC", str(text or "")).replace("ـ", "")
    s = s.replace("آ", "ء" + FATHA + "ا")
    s = re.sub("[أإؤئ]", "ء", s)
    return s.replace("ٱ", "ا")


def letters_only(text: str, keep_shadda: bool = False) -> str:
    keep = "ء-ي" + (SHADDA if keep_shadda else "")
    return re.sub(f"[^{keep}]", "", fold(text))


def _any_vowel(marks: str) -> str:
    v = vowel(marks)
    if v:
        return v
    for t, s in zip(TANWIN, (FATHA, DAMMA, KASRA)):
        if t in (marks or ""):
            return s
    return ""


def seat(text: str) -> str:
    """Write each bare hamza on the seat the spelling rules give it."""
    u = parse(text)
    n = len(u)
    out: List[str] = []
    i = 0
    while i < n:
        x = u[i]
        if x.c != "ء":
            out.append(x.c + norm_marks(x.m))
            i += 1
            continue
        own = _any_vowel(x.m)
        p = u[i - 1] if i > 0 else None
        nx = u[i + 1] if i + 1 < n else None
        if p is None:
            pv = ""
        else:
            pv = vowel(p.m) or ("A" if p.c == "ا" else "U" if p.c == "و" and is_sakin(p)
                                else "I" if p.c == "ي" and is_sakin(p) else "")
        madd = own == FATHA and nx is not None and nx.c == "ا" and not nx.m and SHADDA not in x.m
        if i == 0:
            if madd:
                out.append("آ")
                i += 2
                continue
            c = "إ" if own == KASRA else "أ"
        elif i == n - 1:
            c = "ئ" if pv == KASRA else "ؤ" if pv == DAMMA else "أ" if pv == FATHA else "ء"
        elif own == KASRA or pv in (KASRA, "I"):
            c = "ئ"
        elif own == DAMMA or pv == DAMMA:
            c = "ؤ"
        elif madd:
            out.append("آ")
            i += 2
            continue
        elif pv in ("A", "U"):
            c = "ء"
        else:
            c = "أ"
        out.append(c + norm_marks(x.m))
        i += 1
    return "".join(out)
