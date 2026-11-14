"""READ: analysis by synthesis.

A written word is peeled into every stem its clitics allow; each stem is
laid against the inverse templates (what the BUILDER makes of each root
class with unknown radicals); every root that fits is rebuilt on its wazn,
and only a rebuild that lands on the written word, vowel for vowel, is kept.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple

from ...memory_store.lexicon import Lexicon, VerbEntry
from .derivation import Derivation, Deriver
from .orthography import SHADDA, SUKUN, Unit, fold, is_sakin, join, norm_marks, parse, vowel
from .root import Root
from .wazn import LawTable, Wazn

_X, _Y, _Z = "", "", ""
_PRIOR = {"ism-fail": 0.5, "ism-maful": 0.45, "masdar": 0.4, "mubalagha": 0.3, "sifa": 0.3, "tafdil": 0.3,
          "makan": 0.1, "alat": 0.0}
_ENCLITICS = ("هما", "هم", "هن", "ها", "ه", "كما", "كم", "كن", "ك", "نا", "ي")
_NUMBER = (("تان", "fd"), ("تين", "fd"), ("ات", "fp"), ("ون", "mp"), ("ين", "mp"), ("ان", "md"), ("ة", "f"))


@dataclass(frozen=True)
class Stem:
    """One reading of a word's clitics: what is left, and what was peeled."""

    units: Tuple[Unit, ...]
    pre: str = ""
    suf: str = ""
    definite: bool = False


@dataclass(frozen=True)
class Reading:
    """One (root, wazn) whose rebuild is the written word."""

    root: Root
    wazn: Wazn
    derivation: Derivation
    stem: Stem
    confidence: str          # "verb" (the bāb's verb is recited) | "root" | "shape"
    full: bool               # every vowel the rules give was written
    score: float
    verb: Optional[VerbEntry] = None
    verb1: Optional[VerbEntry] = None


def _letters(text: str) -> List[str]:
    out = [u.c for u in parse(text)]
    if out and out[-1] == "ى":
        out[-1] = "ا"
    return out


def _clean(marks: str) -> str:
    return norm_marks((marks or "").replace(SUKUN, ""))


def plain(text: str) -> str:
    """A form with the case ending and the waṣl kasra set aside, for comparison."""
    u = parse(fold(text))
    if u and u[0].c == "ا":
        u[0].m = ""
    out: List[str] = []
    for i, x in enumerate(u):
        if i == len(u) - 1:
            out.append(("ا" if x.c == "ى" else x.c) + (SHADDA if SHADDA in x.m else ""))
        else:
            out.append(x.c + _clean(x.m).replace("ً", "َ"))
    return "".join(out)


def alternatives(text: Optional[str]) -> List[str]:
    """The forms a lexicon cell lists («إِخْطَاء / خَطَأ»), notes shed."""
    import re

    parts = re.split(r"\s*[/،,]\s*|\s+أَوْ\s+", str(text or ""))
    out: List[str] = []
    for p in parts:
        p = re.sub(r"\(.*?\)", "", p).strip()
        if p:
            out.append(p.split()[0])
    return out


class Analyzer:
    """The inverse reader over one law table and one lexicon."""

    def __init__(self, law: LawTable, lexicon: Lexicon, deriver: Optional[Deriver] = None) -> None:
        self.law = law
        self.lexicon = lexicon
        self.deriver = deriver or Deriver()
        self._inverse: Optional[Dict[int, List[Tuple[Wazn, Root, List[str]]]]] = None

    # -- the inverse templates ---------------------------------------------
    @staticmethod
    def _variants(bab: int) -> List[Root]:
        v = [(_X, _Y, _Z), (_X, "و", _Z), (_X, "ي", _Z), (_X, _Y, "و"), (_X, _Y, "ي"), ("و", _Y, _Z),
             ("ي", _Y, _Z), (_X, _Y, _Y), (_X, "و", "ي"), (_X, "ي", "ي"), ("و", _Y, "ي"), ("ء", _Y, _Z),
             ("ء", _Y, "ي"), ("ء", _Y, "و"), ("ء", _Y, _Y), (_X, "ي", "ء"), (_X, "و", "ء")]
        if bab == 8:
            for f in "صضطظدذزت":
                v += [(f, _Y, _Z), (f, _Y, "و"), (f, _Y, "ي"), (f, _Y, _Y), (f, "و", _Z), (f, "ي", _Z)]
        return [Root(*t) for t in v]

    def inverse(self) -> Dict[int, List[Tuple[Wazn, Root, List[str]]]]:
        if self._inverse is not None:
            return self._inverse
        table: Dict[int, List[Tuple[Wazn, Root, List[str]]]] = {}
        seen = set()
        scratch = Deriver()   # placeholder roots stay out of the real memo
        for wazn in self.law.patterns:
            for var in self._variants(wazn.bab):
                d = scratch.derive(var, wazn)
                for form in (d.out, d.full):
                    if not form:
                        continue
                    sk = _letters(form)
                    key = (wazn.id, "".join(sk), var.key)
                    if key in seen:
                        continue
                    seen.add(key)
                    table.setdefault(len(sk), []).append((wazn, var, sk))
        self._inverse = table
        return table

    # -- one stem against one built form -------------------------------------
    @staticmethod
    def compare(stem: Sequence[Unit], form: str) -> Optional[Tuple[int, int]]:
        """(vowels confirmed, vowels the form carries), or None on any clash."""
        built = parse(form)
        n = len(built)
        if len(stem) != n:
            return None
        ev = need = 0
        bare_twin = False
        for i in range(n):
            a, b = stem[i].c, built[i].c
            if i == n - 1:
                a = "ا" if a == "ى" else a
                b = "ا" if b == "ى" else b
            if a != b:
                return None
            mi, mv = _clean(stem[i].m), _clean(built[i].m)
            if i == n - 1:
                if mi and (SHADDA in mi) != (SHADDA in mv):
                    return None
                bare_twin = not mi and SHADDA in mv
                continue
            if i == n - 2 and built[n - 1].c == "ى":
                mv = mv.replace("ً", "َ")
            if mv:
                need += 1
            if not mi:
                continue
            if mi.replace("ً", "َ") != mv:
                return None
            ev += 1
        if bare_twin and ev > 0:
            return None   # a vowelled word writes its final shadda: بَنِي is not بَنِيٌّ
        return ev, need

    # -- the clitics a noun wears ---------------------------------------------
    @staticmethod
    def stems(word: str) -> List[Stem]:
        u0 = parse(fold(word))
        heads: List[Tuple[List[Unit], str, str, bool]] = [(u0, "", "", False)]   # units, pre, jarr, definite
        if len(u0) > 3 and u0[0].c in "وف" and u0[0].m in ("", "َ"):
            heads.append((u0[1:], u0[0].c, "", False))
        for units, pre, _jarr, _d in list(heads):
            x = units[0]
            if len(units) > 3 and ((x.c in "بل" and x.m in ("", "ِ")) or (x.c == "ك" and x.m in ("", "َ"))):
                heads.append((units[1:], pre + x.c, x.c, False))
        for units, pre, jarr, _d in list(heads):
            rest: Optional[List[Unit]] = None
            if len(units) > 4 and units[0].c == "ا" and units[1].c == "ل" and is_sakin(units[1]):
                rest = units[2:]
            elif jarr == "ل" and len(units) > 3 and units[0].c == "ل" and is_sakin(units[0]):
                rest = units[1:]
            if rest:
                rest = list(rest)
                if SHADDA in rest[0].m:
                    rest[0] = Unit(rest[0].c, rest[0].m.replace(SHADDA, ""))
                heads.append((rest, pre + "ال", jarr, True))
        out: List[Stem] = []
        seen = set()

        def push(units: Sequence[Unit], pre: str, definite: bool, suf: str) -> None:
            if len(units) < 3:
                return
            key = (pre, "".join(x.c for x in units), ",".join(x.m for x in units), suf)
            if key in seen:
                return
            seen.add(key)
            out.append(Stem(tuple(units), pre, suf, definite))

        for units, pre, _jarr, definite in heads:
            tails: List[Tuple[List[Unit], str]] = [(list(units), "")]
            s = "".join(x.c for x in units)
            if not definite:
                for e in _ENCLITICS:
                    if s.endswith(e) and len(units) - len(e) >= 3:
                        b = list(units[:len(units) - len(e)])
                        tails.append((b, "+" + e))
                        z = b[-1]
                        if z.c == "ت" and len(b) > 3 and vowel(b[-2].m) != "ِ":
                            tails.append((b[:-1], "f+" + e))
                        if z.c in "وي" and is_sakin(z) and len(b) > 3:
                            tails.append((b[:-1], "mp+" + e))
            for tu, suf in tails:
                push(tu, pre, definite, suf)
                if suf:
                    continue
                s2 = "".join(x.c for x in tu)
                for e, tag in _NUMBER:
                    if s2.endswith(e) and len(tu) - len(e) >= 3:
                        push(tu[:len(tu) - len(e)], pre, definite, tag)
        return out

    def recites(self, book: Optional[str], built: str) -> bool:
        b = plain(built)
        return any(plain(a) == b for a in alternatives(book))

    # -- the reader ---------------------------------------------------------------
    def analyze(self, word: str) -> List[Reading]:
        inverse = self.inverse()
        found: Dict[Tuple[str, str], Reading] = {}
        for st in self.stems(word):
            lt = _letters(join(list(st.units)))
            for wazn, var, sk in inverse.get(len(lt), []):
                bind: Dict[str, str] = {}
                ok = True
                for s, ch in zip(sk, lt):
                    if _X <= s <= _Z:
                        if bind.setdefault(s, ch) != ch:
                            ok = False
                            break
                    elif s != ch:
                        ok = False
                        break
                if not ok:
                    continue
                rs = [bind.get(x, x) for x in var.radicals]
                if any(x in "اىةآ" or x >= "" for x in rs) or rs[0] == rs[1]:
                    continue
                root = Root(*rs)
                key = (root.key, wazn.id)
                if key in found and found[key].stem.pre == "":
                    continue
                d = self.deriver.derive(root, wazn)
                m = self.compare(st.units, d.out)
                if m and d.full:   # the reduced manqūṣ stands bare or under the sound plural only
                    if st.suf and not st.suf.startswith("mp"):
                        m = None
                    elif not st.suf:
                        z = st.units[-1].m.replace(SUKUN, "")
                        if z and z != "ٍ":
                            m = None
                if not m and d.full:
                    m = self.compare(st.units, d.full)
                if not m:
                    continue
                ev, need = m
                full = ev >= need
                if wazn.vowelled and not full:
                    continue
                own = self.lexicon.verb(root.key, wazn.bab)
                if wazn.sama and not (own and self.recites(own.masdar, d.out)):
                    continue   # a Form I maṣdar is recited, never computed
                has_verb = root.key in self.lexicon.verbs
                conf = "verb" if own else "root" if self.lexicon.knows_root(root.key) else "shape"
                if conf == "shape" and (not full or any(c in st.pre.replace("ال", "") for c in "بلك")):
                    continue
                if wazn.needs_verb and not own:
                    continue
                score = ((6 if own else 3 if has_verb else 2 if conf == "root" else 0) + (2 if full else 0)
                         + ev * 0.1 - (0.5 if st.pre else 0) - (0.3 if st.suf else 0)
                         - (0.5 if wazn.vowelled else 0) + _PRIOR.get(wazn.roles[0], 0)
                         - (0.2 if root.f == "ي" else 0) - wazn.bab * 0.01)
                prev = found.get(key)
                if prev and prev.score >= score:
                    continue
                found[key] = Reading(root=root, wazn=wazn, derivation=d, stem=st, confidence=conf, full=full,
                                     score=score, verb=own, verb1=self.lexicon.verb(root.key, 1))
        return sorted(found.values(), key=lambda r: -r.score)

    def read(self, word: str) -> Optional[Reading]:
        readings = self.analyze(word)
        return readings[0] if readings else None
