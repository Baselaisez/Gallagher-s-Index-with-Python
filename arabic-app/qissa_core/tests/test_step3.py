"""Unit tests of Step 3: schemas, the treatise pipeline, the memory store, rule induction."""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from typing import List, Tuple

from qissa_core.core_grammar.sarf import Root, Sarf
from qissa_core.ingestion_pipeline.pdf_layer import Run
from qissa_core.ingestion_pipeline.schema import check_file, validate
from qissa_core.ingestion_pipeline.treatise import MatnExtractor, Page, RecordMiner, SourceManifest, Treatise
from qissa_core.memory_store.store import MemoryStore
from qissa_core.ml_engine.induction import MasdarInducer, PromotionGate, Tendency, shape_of

APP = Path(__file__).resolve().parents[2]
CONTENT = APP / "content"
SCHEMA = CONTENT / "rules" / "schema"


def manifest(**over: object) -> SourceManifest:
    base = dict(id="demo", title={"ar": "", "en": "", "tr": ""}, author={"ar": "", "en": "", "tr": ""}, files=["a.pdf"],
                matn_size=33, header_size=27, first_matn_page=1, glyphs={"": "َ", "": "به"},
                opaque_ranges=[(0xF100, 0xF2FF)], opaque_mark="", rule_sections={"naql": ["two"]},
                rule_terms={"naql": ["نقل"]}, role_sections={}, last_matn_page=99,
                sections=[{"key": "one", "start": 1, "ar": "", "en": "", "tr": ""},
                          {"key": "two", "start": 2, "ar": "", "en": "", "tr": ""}],
                status="raw-unreviewed", rights="")
    base.update(over)
    return SourceManifest(**base)  # type: ignore[arg-type]


class SchemaTests(unittest.TestCase):
    def test_law_table_conforms(self) -> None:
        self.assertEqual(check_file(CONTENT / "rules" / "ishtiqaq.json", SCHEMA / "law_table.schema.json"), [])

    def test_a_broken_table_is_named(self) -> None:
        schema = json.loads((SCHEMA / "law_table.schema.json").read_text(encoding="utf-8"))
        table = json.loads((CONTENT / "rules" / "ishtiqaq.json").read_text(encoding="utf-8"))
        table["patterns"][0]["bab"] = "one"
        del table["patterns"][1]["tpl"]
        table["patterns"][2]["colour"] = "red"
        errors = validate(table, schema)
        self.assertTrue(any("patterns[0].bab" in e for e in errors))
        self.assertTrue(any("missing «tpl»" in e for e in errors))
        self.assertTrue(any("unknown key «colour»" in e for e in errors))

    def test_every_source_manifest_conforms(self) -> None:
        for path in sorted((CONTENT / "sources").glob("*.json")):
            with self.subTest(source=path.name):
                self.assertEqual(check_file(path, SCHEMA / "source.schema.json"), [])


class TreatiseTests(unittest.TestCase):
    def test_glyphs_fold_to_letters_in_reading_order(self) -> None:
        ex = MatnExtractor(manifest())
        # the PDF stores a run right-to-left as it is SEEN: the last letter first
        self.assertEqual(ex.fold("ﻠﻋﺍ"), "اعلَ")
        self.assertEqual(ex.fold("ﻢﺍﻮﺟ"), "جوابهم")
        self.assertEqual(ex.fold(""), "")           # the display face of a heading is not text
        ex.fold("")
        self.assertEqual(ex.unknown, {"": 1})              # an unmapped glyph is counted, never guessed

    def test_lines_and_the_file_seam(self) -> None:
        ex = MatnExtractor(manifest())
        p1 = [Run(10, 300, 40, 33, "ﻢﻟﻋ"), Run(10, 200, 40, 33, "ﻦﻣ"), Run(50, 300, 40, 23, "x")]
        layers: List[List[Tuple[int, List[Run]]]] = [[(1, p1)], [(1, p1), (2, p1)]]
        pages = ex.pages(layers)
        self.assertEqual([p.number for p in pages], [1, 2])      # the repeated seam page is kept once
        self.assertEqual(pages[0].lines, ("علم من",))            # only the matn's type size, right to left

    def test_sections_records_and_citations(self) -> None:
        man = manifest()
        pages = [Page(1, "", ("الصحيح هو الذي ليس فيه حرف علة، نحو: ضرب.",)),
                 Page(2, "", ("فإن قيل: لم نقلت الحركة؟ قلنا: للثقل. ثم يقال: قول.",))]
        t = Treatise(man, pages)
        self.assertEqual([s.key for s in t.sections], ["one", "two"])
        recs = RecordMiner(t).records()
        self.assertEqual([r.kind for r in recs], ["definition", "qa", "statement"])
        self.assertEqual((recs[1].question, recs[1].answer), ("لم نقلت الحركة؟", "للثقل."))
        self.assertEqual(recs[0].examples, ("ضرب",))
        self.assertEqual(t.cites(), {"naql": [{"source": "demo", "section": "two", "pages": [2]}]})

    def test_the_ingested_files_are_whole(self) -> None:
        law = json.loads((CONTENT / "rules" / "ishtiqaq.json").read_text(encoding="utf-8"))
        for path in sorted((CONTENT / "rules").glob("*.cites.json")):
            cites = json.loads(path.read_text(encoding="utf-8"))
            man = json.loads((CONTENT / "sources" / (cites["source"]["id"] + ".json")).read_text(encoding="utf-8"))
            keys = {s["key"] for s in man["sections"]}
            self.assertGreaterEqual(len(cites["rules"]), 10)
            for rule, places in cites["rules"].items():
                self.assertIn(rule, law["rules"])
                for place in places:
                    self.assertIn(place["section"], keys)
                    self.assertTrue(place["pages"], rule)        # a citation stands on pages, never on a guess
            for role, key in cites["roles"].items():
                self.assertIn(role, law["roles"])
                self.assertIn(key, keys)
            records = APP / "research" / "sources" / (cites["source"]["id"] + ".records.json")
            if records.is_file():
                self.assertEqual(check_file(records, SCHEMA / "records.schema.json"), [])


class MemoryTests(unittest.TestCase):
    sarf: Sarf

    @classmethod
    def setUpClass(cls) -> None:
        cls.sarf = Sarf(CONTENT)

    def test_the_store_grows_and_never_doubles(self) -> None:
        store = MemoryStore()
        store.remember_law(self.sarf.law)
        store.remember_lexicon(self.sarf.lexicon)
        for path in sorted((CONTENT / "rules").glob("*.cites.json")):
            store.remember_source(json.loads(path.read_text(encoding="utf-8")))
        first = store.learn_corpus(CONTENT, self.sarf.analyzer, packages=["adam-wa-iblis"])
        one = store.summary()
        again = store.learn_corpus(CONTENT, self.sarf.analyzer, packages=["adam-wa-iblis"])
        self.assertEqual(first, again)
        self.assertEqual(one, store.summary())                   # a second build changes nothing
        self.assertGreater(one["attested_tokens"], 3)
        self.assertEqual(one["patterns"], len(self.sarf.law.patterns))
        self.assertTrue(store.citations("naql"))
        more = store.learn_corpus(CONTENT, self.sarf.analyzer, packages=["habil-wa-qabil"])
        self.assertGreater(store.summary()["attested_tokens"], one["attested_tokens"])   # new content adds
        self.assertGreater(more["attested"], 0)
        root = store.db.execute("SELECT root FROM attestation LIMIT 1").fetchone()[0]
        self.assertTrue(store.attested_family(root))


class InductionTests(unittest.TestCase):
    sarf: Sarf

    @classmethod
    def setUpClass(cls) -> None:
        cls.sarf = Sarf(CONTENT)

    def test_shape_of(self) -> None:
        cases = [("قَوْل", "قول", "فَعْل"), ("دُخُول", "دخل", "فُعُول"), ("قِيَام", "قوم", "فِعَال"),
                 ("بَقَاء", "بقي", "فَعَال"), ("كِفَايَة", "كفي", "فِعَالَة"), ("عُلُوّ", "علو", "فُعُول")]
        for form, root, shape in cases:
            with self.subTest(form=form):
                self.assertEqual(shape_of(form, Root.of(root)), shape)
        self.assertIsNone(shape_of("عِدَة", Root.of("وعد")))

    def test_the_gate(self) -> None:
        gate = PromotionGate()
        cond = frozenset({("mazi", "a")})
        self.assertIsNone(gate.kind(Tendency(cond, "x", 11, 11), 0.1))          # too few verbs
        self.assertEqual(gate.kind(Tendency(cond, "x", 40, 30), 0.5), "majority")
        self.assertEqual(gate.kind(Tendency(cond, "x", 40, 16), 0.1), "plurality")
        self.assertIsNone(gate.kind(Tendency(cond, "x", 40, 16), 0.3))          # common everywhere: no lift
        parent = Tendency(cond, "x", 40, 30)
        child = Tendency(cond | {("class", "sahih")}, "x", 30, 23)
        self.assertFalse(gate.admits(child, [parent], 0.5))                      # says nothing its parent did not

    def test_induction_on_the_corpus(self) -> None:
        inducer = MasdarInducer()
        examples = inducer.examples(self.sarf.lexicon)
        self.assertGreater(len(examples), 400)
        inducer.fit(examples)
        gate = inducer.gate
        for r in inducer.rules:
            self.assertGreaterEqual(r.support, gate.min_support)
            self.assertGreaterEqual(r.confidence, gate.min_plurality)
        shapes = {r.shape for r in inducer.rules}
        self.assertIn("فَعْل", shapes)        # the transitive فَعَلَ
        self.assertIn("فَعَل", shapes)        # the intransitive فَعِلَ
        self.assertIn("فُعُول", shapes)       # the intransitive فَعَلَ
        cv = inducer.cross_validate(examples)
        self.assertGreater(cv["accuracy"], cv["baseline"])
        self.assertEqual(inducer.predict({"mazi": "i", "mudari": "a", "transitive": "no", "class": "sahih"})[0], "فَعَل")

    def test_the_written_tendencies_are_this_fit(self) -> None:
        path = CONTENT / "rules" / "masdar_tendencies.json"
        inducer = MasdarInducer()
        examples = inducer.examples(self.sarf.lexicon)
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), inducer.fit(examples).as_json(examples))


if __name__ == "__main__":
    unittest.main()
