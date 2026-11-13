"""The corpus lexicon: every verb the story packages recite, by root and bāb.

A Form I maṣdar and bāb are *recited* knowledge (samāʿī) — no rule computes
them — so the derivation engine asks this store, never guesses.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterator, Mapping, Optional, Set

from ..core_grammar.sarf.orthography import fold, letters_only

ROMAN: Mapping[str, int] = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "X": 10,
}


@dataclass(frozen=True)
class VerbEntry:
    """One recited verb: its key, dictionary form, glosses and attested nouns."""

    lex: str
    root: str            # three folded radicals, e.g. "قول"
    bab: int             # 1..10 (the verb form)
    lemma: str
    gloss: Mapping[str, str]
    masdar: Optional[str] = None
    ism_fail: Optional[str] = None
    ism_maful: Optional[str] = None


def root_key(root: str) -> str:
    """Fold a written root («ق و ل», «أ خ ذ») to its three bare radicals."""
    return "".join(ch for ch in fold(root) if "ء" <= ch <= "ي" or ch == "ى").replace("ى", "ي")


@dataclass
class Lexicon:
    """Verbs by root and bāb, plus the set of every root any entry names."""

    verbs: Dict[str, Dict[int, VerbEntry]] = field(default_factory=dict)
    roots: Set[str] = field(default_factory=set)

    @staticmethod
    def bab_of(form: Optional[str], wazn: Optional[str], babs: Mapping[str, Mapping[str, object]]) -> Optional[int]:
        """The bāb of a verb from its stated form, else from its māḍī template."""
        if form and form in ROMAN:
            return ROMAN[form]
        first = (wazn or "").split()
        if not first:
            return None
        shape = letters_only(first[0], keep_shadda=True)
        if shape == "فعل":
            return 1
        for key, bab in babs.items():
            if letters_only(str(bab["mazi"]), keep_shadda=True) == shape:
                return int(key)
        return None

    def add(self, entry: VerbEntry) -> None:
        """Keep one verb per (root, bāb): the alphabetically first key wins,
        so both interpreters choose the same entry whatever the load order."""
        slot = self.verbs.setdefault(entry.root, {})
        held = slot.get(entry.bab)
        if held is None or entry.lex < held.lex:
            slot[entry.bab] = entry

    def verb(self, root: str, bab: int) -> Optional[VerbEntry]:
        return self.verbs.get(root, {}).get(bab)

    def knows_root(self, root: str) -> bool:
        return root in self.verbs or root in self.roots

    def __iter__(self) -> Iterator[VerbEntry]:
        for slot in self.verbs.values():
            yield from slot.values()

    @classmethod
    def from_content(cls, content_dir: Path, babs: Mapping[str, Mapping[str, object]]) -> "Lexicon":
        """Load every package under ``content/samples`` (glossary + morphology)."""
        lex = cls()
        for pkg in sorted((content_dir / "samples").iterdir()):
            gpath, mpath = pkg / "glossary.json", pkg / "morphology.json"
            if not gpath.is_file():
                continue
            glossary = json.loads(gpath.read_text(encoding="utf-8"))
            entries = glossary.get("entries", glossary)
            if isinstance(entries, list):
                entries = {str(e.get("id") or e.get("lex")): e for e in entries}
            for e in entries.values():
                if isinstance(e, dict) and e.get("root"):
                    key = root_key(str(e["root"]))
                    if len(key) == 3:
                        lex.roots.add(key)
            if not mpath.is_file():
                continue
            verbs = json.loads(mpath.read_text(encoding="utf-8")).get("verbs", {})
            for name, m in verbs.items():
                e = entries.get(name)
                if not isinstance(e, dict) or not e.get("root"):
                    continue
                key = root_key(str(e["root"]))
                bab = cls.bab_of(e.get("form"), m.get("wazn"), babs)
                if len(key) != 3 or bab is None:
                    continue
                lex.add(VerbEntry(lex=name, root=key, bab=bab, lemma=str(e.get("lemma", "")),
                                  gloss=dict(e.get("gloss") or {}), masdar=m.get("masdar"),
                                  ism_fail=m.get("ismFail"), ism_maful=m.get("ismMaful")))
        return lex
