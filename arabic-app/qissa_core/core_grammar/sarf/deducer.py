"""DEDUCE: the meaning of a derived noun from its root's verb and its wazn's role.

قَتَلَ «to kill» + فَاعِل → قَاتِل «one who kills / öldüren — katl eden»:
nothing is looked up for قَاتِل itself.  Where only the bare verb is known,
the bāb's own function carries the rest and the gloss says so; where the
root is unknown, only the structure is stated.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Tuple

from ...memory_store.lexicon import VerbEntry
from .analyzer import Reading
from .orthography import DAMMA, FATHA, KASRA, SHADDA, fold, is_sakin, is_weak, parse, vowel
from .wazn import LawTable

_TR_VOWELS = "aeıioöuüâîû"
_OSM = {"ء": "'", "ب": "b", "ت": "t", "ث": "s", "ج": "c", "ح": "h", "خ": "h", "د": "d", "ذ": "z", "ر": "r",
        "ز": "z", "س": "s", "ش": "ş", "ص": "s", "ض": "z", "ط": "t", "ظ": "z", "ع": "'", "غ": "g", "ف": "f",
        "ق": "k", "ك": "k", "ل": "l", "م": "m", "ن": "n", "ه": "h", "و": "v", "ي": "y"}


@dataclass(frozen=True)
class Meaning:
    """A deduced gloss in both languages, and how far it can be trusted."""

    role: str
    en: str
    tr: str
    structural: bool = False   # True where no verb gloss could be composed


def sense(gloss: Mapping[str, str], lang: str) -> str:
    """The first sense of a glossary line, its brackets and article shed."""
    t = re.sub(r"\([^)]*\)", "", str(gloss.get(lang) or gloss.get("en") or "")).strip()
    t = re.split(r"[;,]|\s[—–-]\s", t)[0].strip()
    t = re.sub(r"[!?…]+$", "", t)
    return re.sub(r"^(a|an|the) ", "", t, flags=re.I).strip()


class English:
    """Just enough English morphology for a verb gloss."""

    def __init__(self, irregular: Mapping[str, List[str]]) -> None:
        self.irregular = irregular

    @classmethod
    def load(cls) -> "English":
        path = Path(__file__).resolve().parents[2] / "data" / "en_irregular.json"
        return cls(json.loads(path.read_text(encoding="utf-8")))

    @staticmethod
    def _one_vowel_group(v: str) -> bool:
        return len(re.findall(r"[aeiou]+", v)) == 1

    def past(self, stem: str) -> str:
        w = stem.split(" ")
        v = w[0]
        if v in self.irregular:
            p = self.irregular[v][0]
        elif v.endswith("e"):
            p = v + "d"
        elif re.search(r"[^aeiou]y$", v):
            p = v[:-1] + "ied"
        elif re.search(r"[^aeiou][aeiou][^aeiouwxy]$", v) and self._one_vowel_group(v):
            p = v + v[-1] + "ed"
        else:
            p = v + "ed"
        return " ".join([p] + w[1:])

    def participle(self, stem: str) -> str:
        w = stem.split(" ")
        v = w[0]
        return " ".join([self.irregular[v][1] if v in self.irregular else self.past(v)] + w[1:])

    @staticmethod
    def third(stem: str) -> str:
        w = stem.split(" ")
        v = w[0]
        if re.search(r"(s|sh|ch|x|z|o)$", v):
            s = v + "es"
        elif re.search(r"[^aeiou]y$", v):
            s = v[:-1] + "ies"
        elif v == "have":
            s = "has"
        else:
            s = v + "s"
        return " ".join([s] + w[1:])

    def gerund(self, stem: str) -> str:
        w = stem.split(" ")
        v = w[0]
        if v.endswith("ie"):
            g = v[:-2] + "ying"
        elif re.search(r"[^e]e$", v) and v != "be":
            g = v[:-1] + "ing"
        elif re.search(r"[^aeiou][aeiou][^aeiouwxy]$", v) and self._one_vowel_group(v):
            g = v + v[-1] + "ing"
        else:
            g = v + "ing"
        return " ".join([g] + w[1:])


class Turkish:
    """Vowel harmony and the three suffixes a derived noun needs."""

    @staticmethod
    def harmony(stem: str) -> Tuple[str, str]:
        """(the narrow vowel, the open vowel) the stem's last vowel calls for."""
        vs = [c for c in stem if c in _TR_VOWELS] or ["e"]
        v = vs[-1]
        narrow = "ı" if v in "aıâ" else "u" if v in "ouû" else "ü" if v in "öü" else "i"
        return narrow, ("a" if v in "aıouâû" else "e")

    @staticmethod
    def split(stem: str) -> Tuple[str, str]:
        w = stem.split(" ")
        return " ".join(w[:-1]), w[-1]

    @staticmethod
    def compound(v: str) -> bool:
        """küfret-, şükret-, affet-: a fused «etmek» (its t softens)."""
        return bool(re.search(r"[^aeıioöuü]{2}et$", v)) and not v.endswith("öğret")

    @classmethod
    def soften(cls, v: str) -> str:
        return v[:-1] + "d" if (v in ("et", "git", "güt", "tat", "dit") or cls.compound(v)) else v

    @classmethod
    def active(cls, stem: str) -> str:
        head, v = cls.split(stem)
        _, a = cls.harmony(v)
        base = "diy" if v == "de" else "yiy" if v == "ye" else v + "y" if v[-1] in "aeıioöuü" else cls.soften(v)
        return (head + " " if head else "") + base + ("an" if a == "a" else "en")

    @classmethod
    def passive(cls, stem: str) -> str:
        head, v = cls.split(stem)
        i, a = cls.harmony(v)
        base = v + "n" if v[-1] in "aeıioöuü" else v + i + "n" if v.endswith("l") else cls.soften(v) + i + "l"
        return (head + " " if head else "") + base + ("an" if a == "a" else "en")

    @classmethod
    def verbal_noun(cls, stem: str) -> str:
        head, v = cls.split(stem)
        return (head + " " if head else "") + v + ("ma" if cls.harmony(v)[1] == "a" else "me")


def ottoman(masdar: Optional[str]) -> str:
    """The old Turkish reading of a maṣdar (قَتْل → katl): a transliteration by rule."""
    first = re.split(r"\s*[/،,]\s*", str(masdar or ""))[0]
    u = parse(fold(first))
    if len(u) < 2:
        return ""
    back, hard = "قصضطظعغخح", "قصضطظ"
    s = ""
    for i, x in enumerate(u):
        nx = u[i + 1] if i + 1 < len(u) else None
        p = u[i - 1] if i > 0 else None
        v = vowel(x.m)
        if x.c == "ا":
            if i == 0 and v:
                s += "e" if v == FATHA else "i" if v == KASRA else "ü"
            continue
        if x.c == "ة":
            s += "t"
            continue
        if x.c == "ى":
            continue
        if p is not None and is_weak(x.c) and is_sakin(x) and (
                (x.c == "و" and vowel(p.m) == DAMMA) or (x.c == "ي" and vowel(p.m) == KASRA)):
            continue
        c = _OSM.get(x.c, "")
        s += c + c if SHADDA in x.m else c
        if not v:
            continue
        long = nx is not None and is_sakin(nx) and (
            (v == FATHA and nx.c in "اى") or (v == DAMMA and nx.c == "و") or (v == KASRA and nx.c == "ي"))
        bk = x.c in back or (nx is not None and not long and is_sakin(nx) and nx.c in back)
        if v == FATHA:
            s += "â" if long else ("a" if bk else "e")
        elif v == KASRA:
            s += "î" if long else ("ı" if x.c in hard else "i")
        else:
            dark = (x.c in back and x.c != "ح") or (nx is not None and nx.c in back + "ء" and nx.c != "ح")
            s += "û" if long else ("u" if dark else "ü")
    return re.sub(r"'$", "", re.sub(r"^'", "", s))


class SemanticDeducer:
    """Composes the EN/TR meaning of a reading from the law table's roles."""

    def __init__(self, law: LawTable, english: Optional[English] = None) -> None:
        self.law = law
        self.en = english or English.load()

    def _name(self, role: str, lang: str) -> str:
        return str(self.law.roles.get(role, {}).get(lang, role)).split(" — ")[0]

    def deduce(self, reading: Reading) -> Meaning:
        role = reading.wazn.roles[0]
        bab: Mapping[str, object] = self.law.babs.get(str(reading.wazn.bab), {})
        root = reading.root.shown()
        verb: Optional[VerbEntry] = reading.verb
        src = verb or reading.verb1
        if src is None or not src.gloss:
            return Meaning(role, f"{self._name(role, 'en')} of the root {root}",
                           f"{root} kökünden {self._name(role, 'tr')}", structural=True)
        en = re.sub(r"\s+", " ", re.sub(r"^to ", "", sense(src.gloss, "en")))
        tr_inf = sense(src.gloss, "tr")
        tr = re.sub(r"\s+", " ", re.sub(r"(mek|mak)$", "", tr_inf))
        if verb is None:   # only the bare verb is known: the bāb's function carries the rest
            name: Mapping[str, str] = bab.get("name", {})  # type: ignore[assignment]
            fn: Mapping[str, str] = bab.get("sense", {})   # type: ignore[assignment]
            return Meaning(role,
                           f"{self._name(role, 'en')} of {name.get('en', 'Form ' + str(reading.wazn.bab))} "
                           f"from «to {en}» — {fn.get('en', '')}",
                           f"«{tr_inf}» fiilinin {name.get('tr', '')}ndan {self._name(role, 'tr')} — {fn.get('tr', '')}",
                           structural=True)
        be = en.startswith("be ")
        adj = re.sub(r"^be ", "", en)
        pres = "is " + adj if be else self.en.third(en)
        ing = "being " + adj if be else self.en.gerund(en)
        pp = self.en.participle(en)
        english: Dict[str, str] = {
            "ism-fail": f"one who {pres}", "ism-maful": f"made {adj}" if be else f"one {pp}",
            "mubalagha": f"one who {pres} much",
            "sifa": adj if be else f"one who {pres} by nature — or one {pp}",
            "makan": f"place or time of {ing}", "alat": f"tool for {ing}",
            "tafdil": f"more {adj}" if be else f"more {ing}", "masdar": ing}
        out_en = english.get(role, en)
        if not re.search(r"(mek|mak)$", tr_inf):
            return Meaning(role, out_en, f"{self._name(role, 'tr')}: {tr_inf}")
        act, pas, noun = Turkish.active(tr), Turkish.passive(tr), Turkish.verbal_noun(tr)
        turkish: Dict[str, str] = {
            "ism-fail": act, "ism-maful": pas, "mubalagha": "çok " + act,
            "sifa": re.sub(r" ol$", "", tr) if tr.endswith(" ol") else f"{act} (kalıcı vasıf) — ya da {pas}",
            "makan": noun + " yeri ya da zamanı", "alat": noun + " aleti", "tafdil": "daha çok " + act,
            "masdar": noun}
        out_tr = turkish.get(role, tr)
        osm = ottoman(verb.masdar) if verb.masdar else ""
        plain_verb = not re.search(r"(^| )(et|ol|eyle|kıl)$", tr) and not Turkish.compound(Turkish.split(tr)[1])
        if osm and plain_verb and role in ("ism-fail", "ism-maful", "mubalagha"):
            out_tr += " / " + ("çok " if role == "mubalagha" else "") + osm + (
                " edilen" if role == "ism-maful" else " eden")
        return Meaning(role, out_en, out_tr)
