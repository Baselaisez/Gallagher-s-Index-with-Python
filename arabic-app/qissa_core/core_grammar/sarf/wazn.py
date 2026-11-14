"""The wazn (pattern) and the law table that lists every one of them."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Tuple

from .orthography import Unit, fold, parse
from .root import Root


@dataclass(frozen=True)
class Override:
    """What a root class takes instead of the plain template, and why."""

    tpl: str
    why: str


@dataclass(frozen=True)
class Wazn:
    """One pattern of the law table: a template over ف ع ل and its role."""

    id: str
    bab: int
    roles: Tuple[str, ...]
    tpl: str
    vowelled: bool = False     # believed only where every vowel is written
    sound_ayn: bool = False    # the ʿayn is never weakened on this shape
    sama: bool = False         # a recited (samāʿī) shape: the lexicon must attest it
    needs_verb: bool = False   # believed only where the bāb's verb is known
    over: Mapping[str, Override] = field(default_factory=dict)

    def template_for(self, root: Root) -> Tuple[str, Optional[str]]:
        for cls in root.classes():
            if cls in self.over:
                return self.over[cls].tpl, self.over[cls].why
        return self.tpl, None

    @staticmethod
    def fill(tpl: str, root: Root) -> List[Unit]:
        """Seat the radicals in the template, tagging each with its position."""
        units = parse(fold(tpl))
        for u in units:
            i = "فعل".find(u.c)
            if i >= 0:
                u.c, u.r = root.radicals[i], i
        return units


@dataclass
class LawTable:
    """content/rules/ishtiqaq.json, typed."""

    patterns: List[Wazn]
    roles: Mapping[str, Mapping[str, str]]
    babs: Mapping[str, Mapping[str, object]]
    why: Mapping[str, Mapping[str, str]]
    rules: Mapping[str, Mapping[str, str]]

    @classmethod
    def load(cls, path: Path) -> "LawTable":
        raw = json.loads(path.read_text(encoding="utf-8"))
        pats = [Wazn(id=p["id"], bab=int(p["bab"]), roles=tuple(p["roles"]), tpl=p["tpl"],
                     vowelled=bool(p.get("vowelled")), sound_ayn=bool(p.get("sound_ayn")),
                     sama=bool(p.get("sama")), needs_verb=bool(p.get("needs_verb")),
                     over={k: Override(v["tpl"], v["why"]) for k, v in (p.get("over") or {}).items()})
                for p in raw["patterns"]]
        return cls(patterns=pats, roles=raw["roles"], babs=raw["babs"], why=raw.get("why", {}),
                   rules=raw.get("rules", {}))

    def by_id(self) -> Dict[str, Wazn]:
        return {p.id: p for p in self.patterns}
