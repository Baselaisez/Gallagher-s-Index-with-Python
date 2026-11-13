"""The teacher's memory: one SQLite file that only ever grows.

It remembers the law (patterns and rules), what the lexicon recites (verbs),
what each treatise says and where (citations, records), what the corpus
ATTESTS (a derived noun met in a story, with its root and wazn), and the
tendencies the learning layer was allowed to promote.  Everything is an
upsert: building twice changes nothing; building after new content adds.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple, Union

from ..core_grammar.sarf.analyzer import Analyzer
from ..orthography import seat
from ..core_grammar.sarf.wazn import LawTable
from .lexicon import Lexicon, root_key

_SCHEMA = """
CREATE TABLE IF NOT EXISTS pattern (id TEXT PRIMARY KEY, bab INTEGER, role TEXT, tpl TEXT);
CREATE TABLE IF NOT EXISTS rule (id TEXT PRIMARY KEY, ar TEXT, en TEXT, tr TEXT);
CREATE TABLE IF NOT EXISTS verb (lex TEXT PRIMARY KEY, root TEXT, bab INTEGER, lemma TEXT, en TEXT, tr TEXT,
                                 masdar TEXT, ism_fail TEXT, ism_maful TEXT);
CREATE TABLE IF NOT EXISTS source (id TEXT PRIMARY KEY, title TEXT, author TEXT, status TEXT);
CREATE TABLE IF NOT EXISTS citation (rule TEXT, source TEXT, section TEXT, pages TEXT, PRIMARY KEY (rule, source, section));
CREATE TABLE IF NOT EXISTS record (id TEXT PRIMARY KEY, source TEXT, section TEXT, page INTEGER, kind TEXT,
                                   text TEXT, question TEXT, answer TEXT, status TEXT);
CREATE TABLE IF NOT EXISTS attestation (word TEXT, root TEXT, pattern TEXT, package TEXT, count INTEGER,
                                        PRIMARY KEY (word, root, pattern, package));
CREATE TABLE IF NOT EXISTS tendency (id TEXT PRIMARY KEY, condition TEXT, shape TEXT, support INTEGER,
                                     confidence REAL, status TEXT);
CREATE INDEX IF NOT EXISTS attestation_root ON attestation (root);
"""


class MemoryStore:
    """A thin, typed face over the SQLite file."""

    def __init__(self, path: Union[Path, str] = ":memory:") -> None:
        if isinstance(path, Path):
            path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(str(path))
        self.db.executescript(_SCHEMA)

    def close(self) -> None:
        self.db.commit()
        self.db.close()

    # -- remembering -------------------------------------------------------
    def remember_law(self, law: LawTable) -> None:
        self.db.executemany("INSERT OR REPLACE INTO pattern VALUES (?,?,?,?)",
                            [(p.id, p.bab, p.roles[0], p.tpl) for p in law.patterns])
        self.db.executemany("INSERT OR REPLACE INTO rule VALUES (?,?,?,?)",
                            [(rid, r.get("ar", ""), r.get("en", ""), r.get("tr", "")) for rid, r in law.rules.items()])

    def remember_lexicon(self, lexicon: Lexicon) -> None:
        self.db.executemany(
            "INSERT OR REPLACE INTO verb VALUES (?,?,?,?,?,?,?,?,?)",
            [(v.lex, v.root, v.bab, v.lemma, v.gloss.get("en", ""), v.gloss.get("tr", ""), v.masdar, v.ism_fail,
              v.ism_maful) for v in lexicon])

    def remember_source(self, cites: Mapping[str, object], records: Sequence[Mapping[str, object]] = ()) -> None:
        src: Mapping[str, object] = cites["source"]  # type: ignore[assignment]
        title: Mapping[str, str] = src["title"]      # type: ignore[assignment]
        author: Mapping[str, str] = src["author"]    # type: ignore[assignment]
        self.db.execute("INSERT OR REPLACE INTO source VALUES (?,?,?,?)",
                        (src["id"], title.get("ar", ""), author.get("ar", ""), src.get("status", "")))
        rules: Mapping[str, Sequence[Mapping[str, object]]] = cites.get("rules", {})  # type: ignore[assignment]
        for rule, places in rules.items():
            for place in places:
                self.db.execute("INSERT OR REPLACE INTO citation VALUES (?,?,?,?)",
                                (rule, place["source"], place["section"], json.dumps(place["pages"])))
        self.db.executemany(
            "INSERT OR REPLACE INTO record VALUES (?,?,?,?,?,?,?,?,?)",
            [(r["id"], r["source"], r["section"], r["page"], r["kind"], r["text"], r.get("question", ""),
              r.get("answer", ""), r["status"]) for r in records])

    def attest(self, word: str, root: str, pattern: str, package: str, count: int = 1) -> None:
        self.db.execute(
            "INSERT INTO attestation VALUES (?,?,?,?,?) ON CONFLICT (word, root, pattern, package) "
            "DO UPDATE SET count = excluded.count", (word, root, pattern, package, count))

    def remember_tendencies(self, rules: Iterable[Mapping[str, object]]) -> None:
        for r in rules:
            cond = json.dumps(r["if"], ensure_ascii=False, sort_keys=True)
            self.db.execute("INSERT OR REPLACE INTO tendency VALUES (?,?,?,?,?,?)",
                            (cond + "→" + str(r["then"]), cond, r["then"], r["support"], r["confidence"], "induced"))

    # -- learning from the corpus ---------------------------------------------
    @staticmethod
    def _noun_tokens(package: Path) -> Iterator[Tuple[str, str]]:
        """(written word, the glossary's root) for every token that has no verb paradigm."""
        gpath = package / "glossary.json"
        if not gpath.is_file():
            return
        glossary = json.loads(gpath.read_text(encoding="utf-8"))
        entries = glossary.get("entries", glossary)
        if isinstance(entries, list):
            entries = {str(e.get("id") or e.get("lex")): e for e in entries}
        mpath = package / "morphology.json"
        verbs = json.loads(mpath.read_text(encoding="utf-8")).get("verbs", {}) if mpath.is_file() else {}
        for chapter in sorted((package / "chapters").glob("*.json")):
            doc = json.loads(chapter.read_text(encoding="utf-8"))
            for sentence in doc.get("sentences", []):
                for tok in sentence.get("tokens", []):
                    e = entries.get(tok.get("lex"))
                    if not isinstance(e, dict) or tok.get("lex") in verbs or tok.get("segments") or not e.get("root"):
                        continue
                    if "prop" in str(e.get("pos", "")) or "name" in str(e.get("pos", "")):
                        continue
                    yield str((tok.get("surface") or {}).get("full", "")), root_key(str(e["root"]))

    def learn_corpus(self, content_dir: Path, analyzer: Analyzer, packages: Optional[Sequence[str]] = None) -> Dict[str, int]:
        """Read every plain noun of the packages; where the engine rebuilds it from the
        root the glossary itself states, remember the attestation."""
        seen = kept = 0
        memo: Dict[str, Optional[Tuple[str, str]]] = {}
        for package in sorted((content_dir / "samples").iterdir()):
            if packages is not None and package.name not in packages:
                continue
            counts: Dict[Tuple[str, str, str], int] = {}
            for word, root in self._noun_tokens(package):
                seen += 1
                if word not in memo:
                    r = analyzer.read(word)
                    memo[word] = (r.root.key, r.wazn.id) if r and r.confidence == "verb" and r.full else None
                hit = memo[word]
                if hit and hit[0] == root:
                    key = (seat(word), hit[0], hit[1])
                    counts[key] = counts.get(key, 0) + 1
            for (word, root, pattern), n in counts.items():
                self.attest(word, root, pattern, package.name, n)
                kept += n
        self.db.commit()
        return {"noun_tokens": seen, "attested": kept}

    # -- asking ------------------------------------------------------------
    def pattern_counts(self) -> List[Tuple[str, int]]:
        return [(str(a), int(b)) for a, b in self.db.execute(
            "SELECT pattern, SUM(count) FROM attestation GROUP BY pattern ORDER BY 2 DESC")]

    def attested_family(self, root: str) -> List[Tuple[str, str, int]]:
        return [(str(a), str(b), int(c)) for a, b, c in self.db.execute(
            "SELECT word, pattern, SUM(count) FROM attestation WHERE root = ? GROUP BY word, pattern ORDER BY 3 DESC",
            (root_key(root),))]

    def citations(self, rule: str) -> List[Tuple[str, str, List[int]]]:
        return [(str(a), str(b), json.loads(c)) for a, b, c in self.db.execute(
            "SELECT source, section, pages FROM citation WHERE rule = ?", (rule,))]

    def summary(self) -> Dict[str, object]:
        one = lambda q: int(self.db.execute(q).fetchone()[0] or 0)   # noqa: E731
        return {"patterns": one("SELECT COUNT(*) FROM pattern"), "rules": one("SELECT COUNT(*) FROM rule"),
                "verbs": one("SELECT COUNT(*) FROM verb"), "sources": one("SELECT COUNT(*) FROM source"),
                "citations": one("SELECT COUNT(*) FROM citation"), "records": one("SELECT COUNT(*) FROM record"),
                "attested_forms": one("SELECT COUNT(*) FROM (SELECT DISTINCT word, root, pattern FROM attestation)"),
                "attested_tokens": one("SELECT SUM(count) FROM attestation"),
                "roots_attested": one("SELECT COUNT(DISTINCT root) FROM attestation"),
                "tendencies": one("SELECT COUNT(*) FROM tendency"), "by_pattern": self.pattern_counts()[:12]}
