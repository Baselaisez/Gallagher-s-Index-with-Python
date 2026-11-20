"""A treatise from its printed pages: matn only → sections → rule records.

The pipeline is deliberately modest and inspectable:

1. ``MatnExtractor`` keeps the runs set in the matn's type size, puts them
   back in reading order and folds the printer's glyphs to plain letters
   (a per-source glyph map names every private glyph the printing uses).
2. ``Treatise`` groups the pages into sections by the running head.
3. ``RecordMiner`` cuts each section into records a later step can cite or
   teach from: a question with its answer («فإن قيل … قلنا …»), a
   definition, a statement with its examples («نحو: …»).

Nothing here judges the Arabic.  A record is raw until a reviewer collates
it against the page image; its ``status`` says so.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from .pdf_layer import Run

_MARK = "[ً-ْٰ]"
_PUA = re.compile("[-]")


@dataclass(frozen=True)
class SourceManifest:
    """content/sources/<id>.json — what a printing is and how to read it."""

    id: str
    title: Mapping[str, str]
    author: Mapping[str, str]
    files: Sequence[str]
    matn_size: int
    header_size: int
    first_matn_page: int
    glyphs: Mapping[str, str]
    opaque_ranges: Sequence[Tuple[int, int]]     # glyph ranges that cannot be read (a Quran font)
    opaque_mark: str
    rule_sections: Mapping[str, Sequence[str]]   # law-rule id → the section keys that treat it
    rule_terms: Mapping[str, Sequence[str]]      # law-rule id → words its treatment uses
    role_sections: Mapping[str, str]             # law role → the section that treats it
    sections: Sequence[Mapping[str, object]]     # in order: {key, start (page), ar, en, tr}
    last_matn_page: int
    status: str
    rights: str

    @classmethod
    def load(cls, path: Path) -> "SourceManifest":
        raw = json.loads(path.read_text(encoding="utf-8"))
        return cls(id=raw["id"], title=raw["title"], author=raw["author"], files=raw["files"],
                   matn_size=int(raw["matn_size"]), header_size=int(raw["header_size"]),
                   first_matn_page=int(raw["first_matn_page"]),
                   glyphs={chr(int(k, 16)): v for k, v in raw["glyphs"].items()},
                   opaque_ranges=[(int(a, 16), int(b, 16)) for a, b in raw.get("opaque_ranges", [])],
                   opaque_mark=raw.get("opaque_mark", "﴿…﴾"), rule_sections=raw.get("rule_sections", {}),
                   rule_terms=raw.get("rule_terms", {}), role_sections=raw.get("role_sections", {}),
                   sections=raw.get("sections", []),
                   last_matn_page=int(raw.get("last_matn_page", 10 ** 6)),
                   status=raw["status"], rights=raw["rights"])


@dataclass(frozen=True)
class Page:
    number: int          # the page of the whole printing, continuous across files
    header: str
    lines: Tuple[str, ...]

    @property
    def text(self) -> str:
        return " ".join(self.lines)


class MatnExtractor:
    """Runs of one type size → clean lines in reading order."""

    def __init__(self, manifest: SourceManifest) -> None:
        self.m = manifest
        self.unknown: Dict[str, int] = {}

    def _opaque(self, ch: str) -> bool:
        return any(a <= ord(ch) <= b for a, b in self.m.opaque_ranges)

    def fold(self, visual: str) -> str:
        """A run in visual order → logical order, presentation forms folded,
        every private glyph replaced by the letters the manifest gives it."""
        out: List[str] = []
        opaque = False
        for ch in reversed(visual):
            if self._opaque(ch):
                if not opaque:
                    out.append(self.m.opaque_mark)
                opaque = True
                continue
            opaque = False
            if ch in self.m.glyphs:
                out.append(self.m.glyphs[ch])
            elif _PUA.match(ch):
                self.unknown[ch] = self.unknown.get(ch, 0) + 1
            else:
                out.append(unicodedata.normalize("NFKC", ch))
        return "".join(out)

    @staticmethod
    def clean(line: str) -> str:
        line = re.sub(r"\.{3,}", "", line).replace("ـ", "")
        line = line.replace("1⁄2", "«").replace("1⁄4", "»").replace("االله", "الله")
        line = re.sub(r"\s+(" + _MARK + ")", r"\1", line)
        line = re.sub(r"\s+([،؛:.؟!»])", r"\1", line)
        line = re.sub(r"«\s+", "«", line)
        return re.sub(r"\s+", " ", line).strip()

    def lines(self, runs: Iterable[Run], size: int) -> List[str]:
        rows: Dict[int, List[Run]] = {}
        for r in runs:
            if r.size == size:
                rows.setdefault(r.top, []).append(r)
        out: List[str] = []
        for top in sorted(rows):
            seg = sorted(rows[top], key=lambda r: -r.left)
            text = ""
            for k, r in enumerate(seg):
                if k and not r.text.isspace():
                    prev = seg[k - 1]
                    if prev.left - (r.left + r.width) > 6 and not text.endswith(" "):
                        text += " "
                text += self.fold(r.text)
            text = self.clean(text)
            if text:
                out.append(text)
        return out

    def pages(self, files: Sequence[List[Tuple[int, List[Run]]]]) -> List[Page]:
        """Every matn page of the printing; a page repeated at a file seam is kept once."""
        pages: List[Page] = []
        number = 0
        for index, layer in enumerate(files):
            for local, runs in layer:
                lines = tuple(self.lines(runs, self.m.matn_size))
                if index and local == 1 and pages and lines == pages[-1].lines:
                    continue   # the seam: the second file opens on the first file's last page
                number += 1
                if number < self.m.first_matn_page or number > self.m.last_matn_page or not lines:
                    continue
                header = " ".join(self.lines(runs, self.m.header_size))
                pages.append(Page(number, header, lines))
        return pages


@dataclass(frozen=True)
class Record:
    """One citable unit of a treatise."""

    id: str
    source: str
    section: str
    page: int
    kind: str                    # "qa" | "definition" | "statement"
    text: str
    question: str = ""
    answer: str = ""
    examples: Tuple[str, ...] = ()
    status: str = "raw-unreviewed"


@dataclass
class Section:
    key: str
    pages: List[Page] = field(default_factory=list)

    @property
    def text(self) -> str:
        return " ".join(p.text for p in self.pages)


class Treatise:
    """The matn as sections.  A section starts on the page its manifest entry names
    (the printing sets its headings in a display face that cannot be read as text,
    so the manifest states the page and the title, checked against the matn's own words)."""

    def __init__(self, manifest: SourceManifest, pages: Sequence[Page]) -> None:
        self.manifest = manifest
        self.pages = list(pages)
        self.sections: List[Section] = []
        current: Optional[Section] = None
        for p in self.pages:
            key = self.section_of(p.number)
            if current is None or current.key != key:
                current = Section(key)
                self.sections.append(current)
            current.pages.append(p)

    def section_of(self, page: int) -> str:
        key = "front"
        for spec in self.manifest.sections:
            if int(spec["start"]) <= page:   # type: ignore[call-overload]
                key = str(spec["key"])
        return key

    def section(self, key: str) -> Optional[Section]:
        merged = Section(key)
        for s in self.sections:
            if s.key == key:
                merged.pages.extend(s.pages)
        return merged if merged.pages else None

    def cites(self) -> Dict[str, List[Dict[str, object]]]:
        """For each law rule the manifest places in a section: the pages of that
        section where the rule's own vocabulary actually occurs (evidence, not a guess)."""
        out: Dict[str, List[Dict[str, object]]] = {}
        for rule, keys in self.manifest.rule_sections.items():
            terms = self.manifest.rule_terms.get(rule, [])
            for key in keys:
                sec = self.section(key)
                if sec is None:
                    continue
                pages = [p.number for p in sec.pages
                         if any(t in re.sub(_MARK, "", p.text) for t in terms)] if terms else []
                if terms and not pages:
                    continue
                out.setdefault(rule, []).append({"source": self.manifest.id, "section": key, "pages": pages})
        return out


def _loose(phrase: str) -> str:
    """A regex for ``phrase`` that lets any vowel marks stand between its letters."""
    return "".join(re.escape(ch) + (_MARK + "*" if not ch.isspace() else "") if not ch.isspace() else r"\s+"
                   for ch in phrase)


class RecordMiner:
    """Sections → records.  Rule-based and order-preserving: first the author's own
    objections with their answers («فإن قيل … قلنا …»), then what is left, a sentence at a time."""

    _ASK = re.compile(_loose("فإن قيل") + r"\s*:?")
    _ANSWER = re.compile(_loose("قلنا") + r"\s*:?")
    _EX = re.compile(r"(?:" + _loose("نحو") + "|" + _loose("مثل") + r")\s*:?\s*([^.؛،]+)")
    _DEF = re.compile(r"(?:" + _loose("هو") + "|" + _loose("هي") + r")\s+(?:" + _loose("الذي") + "|" + _loose("التي")
                      + "|" + _loose("اسم") + "|" + _loose("ما") + r")(?=\s)")

    def __init__(self, treatise: Treatise) -> None:
        self.t = treatise

    @staticmethod
    def _page_at(starts: Sequence[Tuple[int, int]], pos: int) -> int:
        page = starts[0][1]
        for offset, number in starts:
            if offset <= pos:
                page = number
        return page

    def _spans(self, text: str) -> List[Tuple[int, int, str]]:
        """(start, end, kind) over a section's text: each objection runs to the end of
        its answer's sentence (or to the next objection); the rest is cut at full stops."""
        spans: List[Tuple[int, int, str]] = []
        asks = [m.start() for m in self._ASK.finditer(text)]
        cursor = 0
        for i, start in enumerate(asks):
            limit = asks[i + 1] if i + 1 < len(asks) else len(text)
            ans = self._ANSWER.search(text, start, limit)
            end = limit
            if ans:
                stop = re.compile(r"[.؟]").search(text, ans.end(), limit)
                end = stop.end() if stop else limit
            if cursor < start:
                spans.append((cursor, start, "plain"))
            spans.append((start, end, "qa" if ans else "plain"))
            cursor = end
        if cursor < len(text):
            spans.append((cursor, len(text), "plain"))
        return spans

    def records(self) -> List[Record]:
        recs: List[Record] = []
        count: Dict[int, int] = {}
        man = self.t.manifest

        def add(page: int, section: str, kind: str, text: str, q: str = "", a: str = "") -> None:
            text = text.strip()
            if len(text) < 8:
                return
            count[page] = count.get(page, 0) + 1
            examples = tuple(e.strip() for e in self._EX.findall(text))
            recs.append(Record(f"{man.id}:p{page}:{count[page]}", man.id, section, page, kind, text, q, a, examples))

        for sec in self.t.sections:
            starts: List[Tuple[int, int]] = []
            text = ""
            for p in sec.pages:
                starts.append((len(text), p.number))
                text += p.text + " "
            for start, end, kind in self._spans(text):
                chunk = text[start:end]
                if kind == "qa":
                    ask, ans = self._ASK.search(chunk), self._ANSWER.search(chunk)
                    assert ask and ans
                    add(self._page_at(starts, start), sec.key, "qa", chunk,
                        chunk[ask.end():ans.start()].strip(" :"), chunk[ans.end():].strip(" :"))
                    continue
                offset = start
                for part in re.split(r"(?<=[.؟])\s+", chunk):
                    if part.strip():
                        kind2 = "definition" if self._DEF.search(part) else "statement"
                        add(self._page_at(starts, offset), sec.key, kind2, part)
                    offset += len(part) + 1
        return recs


def records_json(records: Sequence[Record]) -> List[Dict[str, object]]:
    return [{k: (list(v) if isinstance(v, tuple) else v) for k, v in asdict(r).items()} for r in records]
