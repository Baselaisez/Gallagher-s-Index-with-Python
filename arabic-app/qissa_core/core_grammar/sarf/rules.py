"""The phonological rules (iʿlāl, ibdāl, idghām), one small class each.

Two ordered groups, as in the reader: the SHARED rules run first-match-wins
in a loop (the verb engine's table), then the NOUN rules run once each per
pass.  Every rule mutates the unit list in place and reports whether it
fired; the pipeline records the before/after of each firing.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Sequence

from .orthography import (DAMMA, FATHA, KASRA, SHADDA, SHORT, SUKUN, TANWIN, WEAK, Unit, is_sakin,
                          is_short, is_weak, vowel)
from .root import Root
from .wazn import Wazn


@dataclass
class Context:
    """What one derivation carries between rules."""

    root: Optional[Root] = None
    wazn: Optional[Wazn] = None
    pending: Optional[tuple] = None   # (dropped letter, index) for the harmony rule


class PhonologicalRule(ABC):
    """A rule of the ṣarf books: an id and one decision over the units."""

    id: str = ""
    pre: bool = False   # a noun rule that runs before the shared rules

    @abstractmethod
    def apply(self, u: List[Unit], ctx: Context) -> bool:
        """Mutate ``u`` and return True where the rule fires."""


def _set_vowel(unit: Unit, v: str) -> None:
    unit.m = "".join(ch for ch in unit.m if ch not in SHORT) + v


# ---- the shared rules (the reader's IlalEngine.RULES, same order) ----------

class Naql(PhonologicalRule):
    id = "naql"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        for i in range(1, len(u)):
            if not is_weak(u[i].c) or not is_short(u[i].m):
                continue
            p = u[i - 1]
            if is_weak(p.c) or not is_sakin(p) or p.m == "":
                continue   # only a SOUND, written sukūn receives the vowel
            p.m, u[i].m = vowel(u[i].m), ""
            return True
        return False


class QalbAlif(PhonologicalRule):
    id = "qalb-alif"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        for i in range(1, len(u)):
            if not is_weak(u[i].c) or not is_short(u[i].m) or vowel(u[i - 1].m) != FATHA:
                continue
            was_ya, last = u[i].c == "ي", i == len(u) - 1
            tail = "".join(ch for ch in u[i].m if ch not in SHORT)
            u[i] = Unit("ى" if was_ya and last else "ا", tail, origin=u[i].c)
            return True
        return False


class QalbWawYa(PhonologicalRule):
    id = "qalb-waw-ya"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        for i in range(len(u) - 1):
            if u[i].c == "و" and is_sakin(u[i]) and u[i + 1].c == "ي":
                u[i].c = "ي"
                return True
        return False


class QalbWawKasra(PhonologicalRule):
    id = "qalb-waw-kasra"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        for i in range(1, len(u)):
            if u[i].c == "و" and is_sakin(u[i]) and vowel(u[i - 1].m) == KASRA:
                u[i] = Unit("ي", "")
                return True
        return False


class QalbWawTarafiyya(PhonologicalRule):
    id = "qalb-waw-tarafiyya"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        i = len(u) - 1
        if i < 1 or u[i].c != "و" or vowel(u[i - 1].m) != KASRA:
            return False
        u[i].c = "ي"
        return True


class IdghamWeak(PhonologicalRule):
    id = "idgham"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        for i in range(len(u) - 1):
            if u[i].c != u[i + 1].c or not is_weak(u[i].c):
                continue
            if not is_sakin(u[i]) or is_sakin(u[i + 1]):
                continue
            u[i:i + 2] = [Unit(u[i].c, SHADDA + u[i + 1].m)]
            return True
        return False


class HadhfSakinayn(PhonologicalRule):
    id = "hadhf-sakinayn"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        for i in range(len(u) - 1):
            if not is_sakin(u[i]) or not is_sakin(u[i + 1]):
                continue
            a_w, b_w = u[i].c in WEAK, u[i + 1].c in WEAK
            if not a_w and not b_w:
                continue
            at = i + 1 if (a_w and b_w) else (i if a_w else i + 1)
            gone = u[at].origin or u[at].c
            tail = u[at].m.replace(SUKUN, "")
            del u[at]
            if tail and at < len(u):
                u[at].m += tail
            elif tail and u:
                u[-1].m += tail
            ctx.pending = (gone, at)
            return True
        return False


class Harmoniya(PhonologicalRule):
    id = "harmoniya"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        if ctx.pending is None:
            return False
        gone, idx = ctx.pending
        ctx.pending = None
        prev = u[idx - 1] if 0 < idx <= len(u) else None
        survived = prev is not None and is_weak(prev.c) and is_sakin(prev)
        seat = idx - 2 if survived else idx - 1
        near = prev.c if survived and prev is not None else gone
        want = DAMMA if near == "و" else KASRA if near == "ي" else ""
        if not want or seat < 0 or seat >= len(u) or vowel(u[seat].m) == want:
            return False
        _set_vowel(u[seat], want)
        return True


class Munasaba(PhonologicalRule):
    id = "munasaba"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        for i in range(1, len(u)):
            if u[i].c != "ي" or (not is_sakin(u[i]) and SHADDA not in u[i].m):
                continue
            if vowel(u[i - 1].m) != DAMMA:
                continue
            _set_vowel(u[i - 1], KASRA)
            return True
        return False


class HamzFail(PhonologicalRule):
    id = "hamz-fail"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        for i in range(1, len(u)):
            if is_weak(u[i].c) and is_short(u[i].m) and u[i - 1].c == "ا" and u[i - 1].m == "":
                u[i].c = "ء"
                return True
        return False


class HadhfManqus(PhonologicalRule):
    id = "hadhf-manqus"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        i = len(u) - 1
        if i < 1 or u[i].c != "ي" or SHADDA in u[i].m:
            return False
        if not any(t in u[i].m for t in "ٌٍ") or vowel(u[i - 1].m) != KASRA:
            return False
        del u[i]
        _set_vowel(u[-1], "ٍ")
        return True


SHARED: Sequence[PhonologicalRule] = (Naql(), QalbAlif(), QalbWawYa(), QalbWawKasra(), QalbWawTarafiyya(),
                                      IdghamWeak(), HadhfSakinayn(), Harmoniya(), Munasaba(), HamzFail(),
                                      HadhfManqus())


# ---- the noun rules (the reader's IshtiqaqEngine.POST, same order) ---------

class IbdalIftial(PhonologicalRule):
    id = "ibdal-iftial"
    pre = True

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        w, r = ctx.wazn, ctx.root
        if w is None or r is None or w.bab != 8 or len(u) < 3 or u[2].c != "ت" or u[1].c != r.f:
            return False
        if r.f in "صضطظ":
            u[2].c = "ط"
            return True
        if r.f in "دذز":
            u[2].c = "د"
            if r.f == "ذ":
                u[1].c = "د"
            return True
        return False


class IdghamMithlayn(PhonologicalRule):
    id = "idgham-mithlayn"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        r = ctx.root
        for i in range(len(u) - 2, -1, -1):
            a, b = u[i], u[i + 1]
            if a.c != b.c or a.c in "اويى" or SHADDA in a.m or SHADDA in b.m or is_sakin(b):
                continue
            if not is_sakin(a):
                if i == 0 or r is None or r.a != r.l or a.c != r.a:
                    continue   # two vowelled twins merge only as the root's own ʿayn and lām
                p = u[i - 1]
                if is_sakin(p) and p.c not in "اوي":
                    p.m = vowel(a.m)
            b.m = SHADDA + b.m
            del u[i]
            return True
        return False


class QalbMaqsur(PhonologicalRule):
    id = "qalb-maqsur"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        n = len(u)
        if (n >= 3 and u[-1].c == "ة" and is_weak(u[-2].c) and vowel(u[-2].m) == FATHA
                and SHADDA not in u[-2].m and vowel(u[-3].m) == FATHA):
            u[-2] = Unit("ا", "")
            return True
        if n < 2:
            return False
        x, p = u[-1], u[-2]
        if not is_weak(x.c) or is_sakin(x) or SHADDA in x.m or vowel(p.m) != FATHA:
            return False
        if any(t in x.m for t in TANWIN):
            p.m = p.m.replace(FATHA, "ً")
        u[-1] = Unit("ى", "")
        return True


class IdghamYa(PhonologicalRule):
    id = "idgham-ya"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        n = len(u)
        if n < 3:
            return False
        x, p = u[-1], u[-2]
        if (p.c != "ي" or not is_sakin(p) or not is_weak(x.c) or is_sakin(x) or SHADDA in x.m
                or vowel(u[-3].m) != KASRA):
            return False
        u[-2:] = [Unit("ي", SHADDA + x.m)]
        return True


class HamzTarafiyya(PhonologicalRule):
    id = "hamz-tarafiyya"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        if len(u) < 2:
            return False
        x, p = u[-1], u[-2]
        if not is_weak(x.c) or p.c != "ا" or p.m or SHADDA in x.m:
            return False
        x.c = "ء"
        return True


class QalbHamzaYa(PhonologicalRule):
    id = "qalb-hamza-ya"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        if len(u) < 2 or u[-1].c != "ء" or u[-2].c != "ء" or vowel(u[-2].m) != KASRA:
            return False
        u[-1].c = "ي"
        return True


class TashilHamza(PhonologicalRule):
    id = "tashil-hamza"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        for i in range(len(u) - 1):
            if u[i].c != "ء" or u[i + 1].c != "ء" or not is_sakin(u[i + 1]):
                continue
            v = vowel(u[i].m)
            if not v:
                continue
            u[i + 1] = Unit("ا" if v == FATHA else "ي" if v == KASRA else "و", "")
            return True
        return False


class QalbWawSakina(PhonologicalRule):
    id = "qalb-waw-sakina"

    def apply(self, u: List[Unit], ctx: Context) -> bool:
        for i in range(1, len(u)):
            if u[i].c == "و" and is_sakin(u[i]) and vowel(u[i - 1].m) == KASRA:
                u[i].c = "ي"
                return True
        return False


NOUN: Sequence[PhonologicalRule] = (IbdalIftial(), IdghamMithlayn(), QalbMaqsur(), IdghamYa(), HamzTarafiyya(),
                                    QalbHamzaYa(), TashilHamza(), QalbWawSakina())
