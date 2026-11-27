"""Induce and write the maṣdar tendencies:  python -m qissa_core.ml_engine"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from ..core_grammar.sarf import Sarf
from .induction import MasdarInducer

HERE = Path(__file__).resolve().parents[2]


def main() -> int:
    sarf = Sarf(HERE / "content")
    inducer = MasdarInducer()
    examples = inducer.examples(sarf.lexicon)
    doc = inducer.fit(examples).as_json(examples)
    (HERE / "content" / "rules" / "masdar_tendencies.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in doc.items() if k != "note"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
