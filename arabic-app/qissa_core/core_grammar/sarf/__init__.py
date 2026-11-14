"""Ṣarf: build a derived noun from root + wazn, read one back, deduce its meaning."""

from pathlib import Path
from typing import Optional

from ...memory_store.lexicon import Lexicon
from .analyzer import Analyzer, Reading
from .deducer import Meaning, SemanticDeducer
from .derivation import Derivation, Deriver, Step
from .orthography import fold, seat
from .root import Root
from .rules import PhonologicalRule
from .wazn import LawTable, Wazn

CONTENT_DIR = Path(__file__).resolve().parents[3] / "content"


class Sarf:
    """The three verbs of the engine behind one object: build, read, deduce."""

    def __init__(self, content_dir: Optional[Path] = None) -> None:
        root = content_dir or CONTENT_DIR
        self.law = LawTable.load(root / "rules" / "ishtiqaq.json")
        self.lexicon = Lexicon.from_content(root, self.law.babs)
        self.deriver = Deriver()
        self.analyzer = Analyzer(self.law, self.lexicon, self.deriver)
        self.deducer = SemanticDeducer(self.law)
        self._wazn = self.law.by_id()

    def build(self, root: str, pattern: str) -> Derivation:
        return self.deriver.derive(Root.of(root), self._wazn[pattern])

    def read(self, word: str) -> Optional[Reading]:
        return self.analyzer.read(word)

    def meaning(self, word: str) -> Optional[Meaning]:
        reading = self.read(word)
        return self.deducer.deduce(reading) if reading else None


__all__ = ["Analyzer", "Derivation", "Deriver", "LawTable", "Meaning", "PhonologicalRule", "Reading", "Root",
           "Sarf", "SemanticDeducer", "Step", "Wazn", "fold", "seat"]
