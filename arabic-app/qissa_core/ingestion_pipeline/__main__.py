"""Ingest a treatise:  python -m qissa_core.ingestion_pipeline <manifest> --pdf-dir DIR [--out DIR] [--rules DIR]

Reads the printing's text layer, keeps the matn, and writes

* ``<out>/<id>-matn.txt``       the matn, a paragraph a page
* ``<out>/<id>.records.json``   the records mined from it (schema: records.schema.json)
* ``<rules>/<id>.cites.json``   which law rule is treated in which section, with the pages
                                where the rule's own vocabulary occurs
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path
from typing import Dict, List

from .pdf_layer import read_xml, to_xml
from .schema import validate
from .treatise import MatnExtractor, RecordMiner, SourceManifest, Treatise, records_json

HERE = Path(__file__).resolve().parents[2]


def find(pdf_dir: Path, name: str) -> Path:
    hits = sorted(pdf_dir.glob("*" + name))
    if not hits:
        raise SystemExit(f"no file ending in {name} under {pdf_dir}")
    return hits[0]


def ingest(manifest_path: Path, pdf_dir: Path, out: Path, rules: Path) -> Dict[str, object]:
    schema_dir = HERE / "content" / "rules" / "schema"
    raw = json.loads(manifest_path.read_text(encoding="utf-8"))
    problems = validate(raw, json.loads((schema_dir / "source.schema.json").read_text(encoding="utf-8")))
    if problems:
        raise SystemExit("manifest: " + "; ".join(problems[:5]))
    man = SourceManifest.load(manifest_path)
    with tempfile.TemporaryDirectory() as tmp:
        layers = [list(read_xml(to_xml(find(pdf_dir, name), Path(tmp)))) for name in man.files]
    extractor = MatnExtractor(man)
    pages = extractor.pages(layers)
    treatise = Treatise(man, pages)
    records = RecordMiner(treatise).records()
    head = (f"# {man.title['ar']} — {man.author['ar']}\n#\n"
            "# The matn only, extracted from the text layer of the owner's PDF by type size; the printing's\n"
            "# glyphs are folded to plain letters by the map in content/sources/" + man.id + ".json.\n"
            "# The modern introduction, running heads, footnotes, interlinear glosses and commentary sigla are NOT here.\n"
            f"# Status: {man.status} — spacing inside a few words and the vowel marks are the printing's own and\n"
            "# have not been collated against the page images. [ص N] is the page of the PDF.\n\n")
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{man.id}-matn.txt").write_text(
        head + "\n".join(f"[ص {p.number}]\n{p.text}\n" for p in pages), encoding="utf-8")
    doc = {"source": man.id, "status": man.status,
           "note": "Mined mechanically from the matn; raw until collated against the page images.",
           "records": records_json(records)}
    problems = validate(doc, json.loads((schema_dir / "records.schema.json").read_text(encoding="utf-8")))
    if problems:
        raise SystemExit("records: " + "; ".join(problems[:5]))
    (out / f"{man.id}.records.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    sections = {str(s["key"]): {"ar": s["ar"], "en": s["en"], "tr": s["tr"]} for s in man.sections}
    cites = {"source": {"id": man.id, "title": dict(man.title), "author": dict(man.author), "status": man.status},
             "sections": sections, "rules": treatise.cites(),
             "roles": {role: key for role, key in man.role_sections.items() if treatise.section(key)}}
    rules.mkdir(parents=True, exist_ok=True)
    (rules / f"{man.id}.cites.json").write_text(json.dumps(cites, ensure_ascii=False, indent=1), encoding="utf-8")
    kinds: Dict[str, int] = {}
    for r in records:
        kinds[r.kind] = kinds.get(r.kind, 0) + 1
    return {"pages": len(pages), "words": sum(len(p.text.split()) for p in pages), "sections": len(treatise.sections),
            "records": kinds, "rules_cited": len(cites["rules"]),  # type: ignore[arg-type]
            "unknown_glyphs": {f"{ord(k):04X}": v for k, v in extractor.unknown.items()}}


def main(argv: List[str]) -> int:
    ap = argparse.ArgumentParser(prog="python -m qissa_core.ingestion_pipeline")
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--pdf-dir", type=Path, required=True)
    ap.add_argument("--out", type=Path, default=HERE / "research" / "sources")
    ap.add_argument("--rules", type=Path, default=HERE / "content" / "rules")
    args = ap.parse_args(argv)
    print(json.dumps(ingest(args.manifest, args.pdf_dir, args.out, args.rules), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
