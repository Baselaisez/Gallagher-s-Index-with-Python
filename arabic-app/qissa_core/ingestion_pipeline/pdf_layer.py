"""The text layer of a PDF as positioned runs (through poppler's ``pdftohtml -xml``).

A printed treatise mixes the classical matn with a modern apparatus on the
same page; they differ by TYPE SIZE, so the layer is read as runs that keep
their size and position, and the caller keeps only the size it wants.
"""

from __future__ import annotations

import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterator, List, Tuple

_FONT = re.compile(r'<fontspec id="(\d+)" size="(\d+)"')
_PAGE = re.compile(r'<page number="(\d+)"[^>]*>(.*?)</page>', re.S)
_TEXT = re.compile(r'<text top="(\d+)" left="(\d+)" width="(\d+)" height="(\d+)" font="(\d+)">(.*?)</text>', re.S)
_TAG = re.compile(r"<[^>]+>")
_ENTITIES = (("&#34;", '"'), ("&quot;", '"'), ("&lt;", "<"), ("&gt;", ">"), ("&amp;", "&"))


@dataclass(frozen=True)
class Run:
    """One run of glyphs as the PDF stores it (visual order)."""

    top: int
    left: int
    width: int
    size: int
    text: str


def to_xml(pdf: Path, out_dir: Path) -> Path:
    """Run poppler on ``pdf`` and return the XML it writes."""
    stem = out_dir / pdf.stem
    subprocess.run(["pdftohtml", "-xml", "-i", "-q", str(pdf), str(stem)], check=True)
    return stem.with_suffix(".xml")


def read_xml(xml: Path) -> Iterator[Tuple[int, List[Run]]]:
    """(page number, runs) for every page of a poppler XML file."""
    text = xml.read_text(encoding="utf-8", errors="replace")
    sizes: Dict[str, int] = {fid: int(size) for fid, size in _FONT.findall(text)}
    for pm in _PAGE.finditer(text):
        runs: List[Run] = []
        for m in _TEXT.finditer(pm.group(2)):
            raw = _TAG.sub("", m.group(6))
            for ent, ch in _ENTITIES:
                raw = raw.replace(ent, ch)
            runs.append(Run(int(m.group(1)), int(m.group(2)), int(m.group(3)), sizes.get(m.group(5), 0), raw))
        yield int(pm.group(1)), runs


def read_pdf(pdf: Path) -> List[Tuple[int, List[Run]]]:
    with tempfile.TemporaryDirectory() as tmp:
        return list(read_xml(to_xml(pdf, Path(tmp))))
