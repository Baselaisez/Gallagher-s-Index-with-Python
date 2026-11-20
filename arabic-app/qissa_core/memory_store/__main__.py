"""Build (or grow) the memory:  python -m qissa_core.memory_store [--db PATH] [--summary PATH]"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import List

from ..core_grammar.sarf import Sarf
from .store import MemoryStore

HERE = Path(__file__).resolve().parents[2]


def main(argv: List[str]) -> int:
    ap = argparse.ArgumentParser(prog="python -m qissa_core.memory_store")
    ap.add_argument("--db", type=Path, default=HERE / "memory" / "qissa.sqlite")
    ap.add_argument("--summary", type=Path, default=HERE / "research" / "memory-summary.json")
    args = ap.parse_args(argv)
    content = HERE / "content"
    sarf = Sarf(content)
    store = MemoryStore(args.db)
    store.remember_law(sarf.law)
    store.remember_lexicon(sarf.lexicon)
    for cites in sorted((content / "rules").glob("*.cites.json")):
        doc = json.loads(cites.read_text(encoding="utf-8"))
        rec = HERE / "research" / "sources" / (doc["source"]["id"] + ".records.json")
        records = json.loads(rec.read_text(encoding="utf-8"))["records"] if rec.is_file() else []
        store.remember_source(doc, records)
    tend = content / "rules" / "masdar_tendencies.json"
    if tend.is_file():
        store.remember_tendencies(json.loads(tend.read_text(encoding="utf-8"))["rules"])
    learned = store.learn_corpus(content, sarf.analyzer)
    summary = {**store.summary(), **learned}
    store.close()
    args.summary.write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
