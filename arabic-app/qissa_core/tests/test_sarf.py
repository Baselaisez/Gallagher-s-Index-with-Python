"""Unit tests of the ṣarf engine against the shared, hand-verified fixtures."""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from typing import Any, Dict, List

from qissa_core.core_grammar.sarf import Root, Sarf, seat
from qissa_core.core_grammar.sarf.analyzer import alternatives, plain
from qissa_core.core_grammar.sarf.deducer import Turkish, ottoman
from qissa_core.core_grammar.sarf.orthography import join, parse
from qissa_core.core_grammar.sarf.rules import (Context, HadhfManqus, HamzFail, IdghamMithlayn, Naql,
                                                 QalbAlif)

CONTENT = Path(__file__).resolve().parents[2] / "content"


def fixtures() -> List[Dict[str, Any]]:
    return json.loads((CONTENT / "rules" / "ishtiqaq_fixtures.json").read_text(encoding="utf-8"))["fixtures"]


class RuleTests(unittest.TestCase):
    """Each rule alone, on the textbook example it is taught with."""

    def run_rule(self, rule: Any, text: str, root: str = "") -> str:
        u = parse(text)
        rule.apply(u, Context(root=Root.of(root) if root else None))
        return join(u)

    def assertSame(self, got: str, want: str) -> None:
        """Equal once both spellings write their marks in the one canonical order."""
        self.assertEqual(got, join(parse(want)))

    def test_qalb_alif(self) -> None:
        self.assertEqual(self.run_rule(QalbAlif(), "قَوَلَ"), "قَالَ")
        self.assertEqual(self.run_rule(QalbAlif(), "بَيَعَ"), "بَاعَ")

    def test_naql(self) -> None:
        self.assertEqual(self.run_rule(Naql(), "يَقْوُلُ"), "يَقُولُ")
        self.assertEqual(self.run_rule(Naql(), "يَبْيِعُ"), "يَبِيعُ")

    def test_hamz_fail(self) -> None:
        self.assertEqual(seat(self.run_rule(HamzFail(), "قَاوِلٌ")), "قَائِلٌ")

    def test_manqus(self) -> None:
        self.assertEqual(self.run_rule(HadhfManqus(), "رَامِيٌ"), "رَامٍ")

    def test_idgham(self) -> None:
        self.assertSame(self.run_rule(IdghamMithlayn(), "مَادِدٌ", "مدد"), "مَادٌّ")
        self.assertSame(self.run_rule(IdghamMithlayn(), "مُحْبِبٌ", "حبب"), "مُحِبٌّ")
        self.assertSame(self.run_rule(IdghamMithlayn(), "مُسْتَتِرٌ", "ستر"), "مُسْتَتِرٌ")


class RootTests(unittest.TestCase):
    def test_classes(self) -> None:
        self.assertEqual(Root.of("ق ت ل").classes(), ["sahih"])
        self.assertIn("hollow-w", Root.of("ق و ل").classes())
        self.assertIn("naqis-y", Root.of("ر م ي").classes())
        self.assertIn("doubled", Root.of("م د د").classes())
        self.assertIn("mithal-w", Root.of("و ع د").classes())
        self.assertIn("mahmuz", Root.of("أ خ ذ").classes())
        self.assertTrue(Root.of("ط و ي").is_lafif)

    def test_three_radicals(self) -> None:
        with self.assertRaises(ValueError):
            Root.of("ق ل")


class EngineTests(unittest.TestCase):
    sarf: Sarf

    @classmethod
    def setUpClass(cls) -> None:
        cls.sarf = Sarf(CONTENT)

    def test_law_table_is_whole(self) -> None:
        law = self.sarf.law
        for p in law.patterns:
            for o in p.over.values():
                self.assertIn(o.why, law.why, p.id)
            for r in p.roles:
                self.assertIn(r, law.roles, p.id)
            self.assertIn(str(p.bab), law.babs, p.id)
        self.assertEqual(len({p.id for p in law.patterns}), len(law.patterns))

    def test_build(self) -> None:
        for fx in fixtures():
            with self.subTest(word=fx["word"]):
                d = self.sarf.build(fx["root"], fx["pattern"])
                self.assertEqual(seat(d.asl), fx["asl"])
                self.assertEqual(seat(d.out), fx["out"])
                self.assertEqual(d.rule_ids, fx["steps"])

    def test_every_rule_has_its_sentence(self) -> None:
        law = self.sarf.law
        for fx in fixtures():
            for rid in fx["steps"]:
                if rid.startswith("qiyas-"):
                    self.assertIn(rid[len("qiyas-"):], law.why)
                else:
                    self.assertIn(rid, law.rules)

    def test_read(self) -> None:
        for fx in fixtures():
            with self.subTest(word=fx["word"]):
                r = self.sarf.read(fx["word"])
                self.assertIsNotNone(r)
                assert r is not None
                self.assertEqual(r.root.shown(), fx["root"])
                self.assertEqual(r.wazn.id, fx["pattern"])

    def test_read_through_clitics(self) -> None:
        for word, root, pattern in [("وَالْمُعَلِّمُونَ", "ع ل م", "fail-2"), ("لِلْمُؤْمِنِينَ", "أ م ن", "fail-4"),
                                    ("كَاتِبُهُمْ", "ك ت ب", "fail-1"), ("الرَّامِي", "ر م ي", "fail-1"),
                                    ("الْمُصْطَفَى", "ص ف و", "maful-8"), ("بِالْمَعْرُوفِ", "ع ر ف", "maful-1")]:
            with self.subTest(word=word):
                r = self.sarf.read(word)
                assert r is not None
                self.assertEqual((r.root.shown(), r.wazn.id), (root, pattern))

    def test_nothing_is_invented(self) -> None:
        # a plain noun on no wazn of the table, and a maṣdar shape its verb does not recite
        for word in ("بَيْتٌ", "لِسَانُهُ", "رَجُلٌ", "بَنِي"):
            with self.subTest(word=word):
                self.assertIsNone(self.sarf.read(word))

    def test_deduction(self) -> None:
        for fx in fixtures():
            if "en" not in fx:
                continue
            with self.subTest(word=fx["word"]):
                m = self.sarf.meaning(fx["word"])
                assert m is not None
                self.assertEqual(m.en, fx["en"])
                self.assertEqual(m.tr, fx["tr"])

    def test_the_brief_examples(self) -> None:
        qatil, qail = self.sarf.meaning("قَاتِلٌ"), self.sarf.meaning("قَائِلٌ")
        assert qatil is not None and qail is not None
        self.assertEqual(qatil.tr, "öldüren / katl eden")
        self.assertEqual(qail.tr, "diyen / kavl eden")
        self.assertEqual(self.sarf.build("ق و ل", "fail-1").rule_ids, ["hamz-fail"])

    def test_calibration_on_the_corpus(self) -> None:
        """The stories are the calibration set: rebuild every recited participle and
        every regular maṣdar, and hold the agreement above the measured floor."""
        ok = total = 0
        by_kind = {"fail": "ism_fail", "maful": "ism_maful", "masdar": "masdar"}
        for v in self.sarf.lexicon:
            root = Root.of(v.root)
            for kind, attr in by_kind.items():
                book = getattr(v, attr)
                if not book or (kind == "masdar" and v.bab == 1):
                    continue
                pats = [p for p in self.sarf.law.patterns if p.bab == v.bab and p.id.startswith(kind + "-")]
                if not pats:
                    continue
                total += 1
                built = {plain(self.sarf.deriver.derive(root, p).out) for p in pats}
                if any(plain(a) in built for a in alternatives(book)):
                    ok += 1
        self.assertGreater(total, 2500)
        self.assertGreaterEqual(ok / total, 0.985, f"{ok}/{total}")


class TurkishTests(unittest.TestCase):
    def test_suffixes(self) -> None:
        self.assertEqual(Turkish.active("öldür"), "öldüren")
        self.assertEqual(Turkish.active("de"), "diyen")
        self.assertEqual(Turkish.active("vaat et"), "vaat eden")
        self.assertEqual(Turkish.active("şükret"), "şükreden")
        self.assertEqual(Turkish.active("öğret"), "öğreten")
        self.assertEqual(Turkish.passive("yaz"), "yazılan")
        self.assertEqual(Turkish.passive("bil"), "bilinen")
        self.assertEqual(Turkish.passive("söyle"), "söylenen")
        self.assertEqual(Turkish.verbal_noun("oku"), "okuma")

    def test_ottoman(self) -> None:
        self.assertEqual(ottoman("قَتْل"), "katl")
        self.assertEqual(ottoman("قَوْل"), "kavl")
        self.assertEqual(ottoman("تَعْلِيم"), "ta'lîm")
        self.assertEqual(ottoman("اِسْتِغْفَار"), "istigfâr")


if __name__ == "__main__":
    unittest.main()
