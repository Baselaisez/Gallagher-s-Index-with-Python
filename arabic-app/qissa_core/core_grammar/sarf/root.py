"""The root: three radicals and the class their weak letters put it in."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

from .orthography import fold


@dataclass(frozen=True)
class Root:
    """A triliteral root with folded radicals (every hamza is «ء»)."""

    f: str
    a: str
    l: str

    @classmethod
    def of(cls, text: str) -> "Root":
        rs = [ch for ch in fold(text).replace("ى", "ي") if "ء" <= ch <= "ي"]
        if len(rs) != 3:
            raise ValueError(f"a root has three radicals, got {text!r}")
        return cls(rs[0], rs[1], rs[2])

    @property
    def radicals(self) -> Tuple[str, str, str]:
        return (self.f, self.a, self.l)

    @property
    def key(self) -> str:
        return self.f + self.a + self.l

    @staticmethod
    def _weak(ch: str) -> bool:
        return ch in "وي"

    @property
    def is_lafif(self) -> bool:
        """Both the ʿayn and the lām weak (طوي): the ʿayn then stays sound."""
        return self._weak(self.a) and self._weak(self.l)

    def classes(self) -> List[str]:
        """Class keys, most specific first — the order overrides are tried in."""
        k: List[str] = []
        if self.a == self.l and not self._weak(self.a):
            k.append("doubled")
        if self._weak(self.l):
            k += ["naqis-w" if self.l == "و" else "naqis-y", "naqis"]
        if self._weak(self.a) and not self._weak(self.l):
            k += ["hollow-w" if self.a == "و" else "hollow-y", "hollow"]
        if self._weak(self.f):
            k += ["mithal-w" if self.f == "و" else "mithal-y", "mithal"]
        if self.l == "ء":
            k.append("mahmuz-l")
        if "ء" in self.radicals:
            k.append("mahmuz")
        return k or ["sahih"]

    def shown(self) -> str:
        return " ".join("أ" if r == "ء" else r for r in self.radicals)
