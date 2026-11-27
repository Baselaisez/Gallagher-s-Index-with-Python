#!/usr/bin/env python3
"""polish_pkg.py <package dir> [--write] — run the builder's LINE-LEVEL post-passes on a shipped engine-authored package.

A fresh engine pass re-reads the whole text on today's reader, and today's lexicon is not the one the book was authored
on (a verb added by a later book can capture an older book's noun — فَأَوَّلُهَا read as أَوَّلَ). The passes here need no
engine at all: they are functions of the authored lines of one sentence, so they can reach a shipped book without
re-deciding anything else in it.

  praise_khabar    the rafʿ noun after the praise parenthesis (اللهُ تَعَالَى وَاحِدٌ) is never its doer
  kana_dedupe      a sister of kāna whose noun is written keeps no hidden one beside it
  name_ma_khabar   the relative مَا right after its subject is the predicate

Without --write it only prints what would change."""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pkg_from_engine as B


def main():
    pkg = pathlib.Path(sys.argv[1]); write = "--write" in sys.argv
    report = {}; changed = 0; kana = 0
    for f in sorted((pkg / "chapters").glob("*.json"), key=lambda x: int(x.stem)):
        ch = json.load(open(f, encoding="utf-8")); before = json.dumps(ch, ensure_ascii=False, sort_keys=True)
        for sen in ch["sentences"]:
            toks = sen["tokens"]; old = [dict(t.get("irab") or {}) for t in toks]
            old_g = [list(t.get("grammar") or []) for t in toks]
            B.praise_khabar(toks, report); kana += B.kana_dedupe(toks); B.name_ma_khabar(toks, report)
            for i, t in enumerate(toks):
                if (t.get("irab") or {}) != old[i]:
                    changed += 1
                    print(f"{f.stem}:{sen['id']}:{i} {t['surface']['full']}\n   - {old[i].get('ar', '')}\n   + {t['irab']['ar']}")
        if write and json.dumps(ch, ensure_ascii=False, sort_keys=True) != before:
            json.dump(ch, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{pkg.name}: {changed} lines changed (after praise {report.get('praise_khabar', 0)}, left {report.get('praise_open', [])}; kāna {kana}; mā as khabar {report.get('ma_khabar', 0)})" + ("" if write else " — dry run"))


if __name__ == "__main__":
    main()
