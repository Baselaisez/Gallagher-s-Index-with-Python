#!/usr/bin/env python3
"""Audit the grammar registry against the canonical madrasah lists.

The Ottoman awamil/ma'mul tables transcribed in research/sources/ are the
curriculum's own inventory of governors and governed positions: twenty huruf
jarr, eight sisters of inna, fifteen jawazim, the nine qiyasi and two ma'nevi
governors, the thirteen mansubat, and so on. The registry in content/grammar/
teaches these piecemeal, one note per topic, and nothing else says how much of
the canonical inventory the notes actually reach.

This tool hardcodes the canonical lists (each with the source file it was
transcribed from), maps every item to the registry note id(s) that teach it,
and prints a coverage report. Items with no honest mapping are printed as TODO
— a gap is information, not an error, so the exit code is 0 either way. The
one thing treated as a bug is a mapping that points at a note id which does
not exist on disk: with --strict that exits 1, because a typo in this file
would silently overstate coverage.

The mapping is deliberately conservative: an item counts as covered only when
a note names the item and its behaviour (e.g. لَنْ is covered because
an-masdariyya lists all four nasb particles; مُذْ is TODO because no note
names it, even though huruf-jarr covers the class).

Usage:
    python3 tools/check_canon.py            # coverage report
    python3 tools/check_canon.py --strict   # exit 1 on mapped ids missing from disk
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAMMAR_DIR = ROOT / "content" / "grammar"

# Each list: (source file in research/sources/, list title, items).
# Each item: (canonical name as the table gives it, [note ids that teach it]).
# An empty id list means TODO — no registry note teaches the item yet.
# Names are quoted from the transcription; where the transcription's spelling
# is an artifact of the OCR/typing (خلى for خَلَا, كيمه for كَيْ), the
# standard form is added in parentheses so the report stays readable.

CANON = [
    # -- research/sources/amil-tablolari-turkce.txt -------------------------
    ("amil-tablolari-turkce.txt", "Harf-i cerler (20)", [
        ("ب", ["huruf-jarr"]),
        ("من", ["huruf-jarr"]),
        ("الى", ["huruf-jarr"]),
        ("عن", ["huruf-jarr"]),
        ("على", ["huruf-jarr"]),
        ("لام", ["huruf-jarr"]),
        ("فى", ["huruf-jarr"]),
        ("كف (كَـ)", ["huruf-jarr"]),
        ("حتى", ["huruf-jarr"]),
        ("رب", ["huruf-jarr"]),
        ("واو القسم", ["huruf-jarr"]),
        ("تاء القسم", ["huruf-jarr"]),
        # حاشا/خلا/عدا are named in istithna.json, but only as sisters of
        # إِلَّا; their jarr reading is not taught anywhere, so: TODO.
        ("حاشا", []),
        ("مذ", []),
        ("منذ", []),
        ("خلى (خَلَا)", []),
        ("عدى (عَدَا)", []),
        ("لولا", []),
        ("كيمه (كَيْ)", []),
        ("لعل", []),
    ]),
    ("amil-tablolari-turkce.txt", "İsmini nasb, haberini raf edenler (8)", [
        ("اِن", ["inna-wa-akhawatuha"]),
        ("ان", ["inna-wa-akhawatuha"]),
        ("كأن", ["inna-wa-akhawatuha"]),
        ("لكن", ["inna-wa-akhawatuha"]),
        ("ليت", ["inna-wa-akhawatuha"]),
        ("لعل", ["inna-wa-akhawatuha"]),
        # The table's eighth-but-one item; identity unclear in the
        # transcription (أَلَا?) and no note teaches an الا of this class.
        ("الا", []),
        # لا نافية للجنس — la-nafiya-lil-jins says it works like إِنَّ.
        ("لا", ["la-nafiya-lil-jins"]),
    ]),
    ("amil-tablolari-turkce.txt", "İsmini raf, haberini nasb edenler (2)", [
        ("ما مشابه بليس", ["ma-la-mushabbaha"]),
        ("لا مشابه بليس", ["ma-la-mushabbaha"]),
    ]),
    ("amil-tablolari-turkce.txt", "Fiil-i muzariyi nasb edenler (4)", [
        # an-masdariyya lists all four: أَنْ، لَنْ، كَيْ، إِذَنْ.
        ("ان", ["an-masdariyya"]),
        ("لن", ["an-masdariyya"]),
        ("كى", ["an-masdariyya"]),
        ("اذن", ["an-masdariyya"]),
    ]),
    # -- research/sources/mamul-tablolari-turkce.txt ------------------------
    ("mamul-tablolari-turkce.txt", "Cevazim (15)", [
        ("لم", ["lam-jazim"]),
        ("لما", ["lam-jazim"]),  # named there as لَمْ's neighbour
        ("امر لامى (لام الأمر)", ["lam-amr"]),
        ("نهى لاسى (لا الناهية)", ["la-nahiya"]),
        ("ان", ["in-shartiyya"]),
        ("مهما", []),
        # in-shartiyya names the jazm nouns مَنْ ما مَتَى أَيْنَ أَيُّ حَيْثُمَا.
        ("ما", ["in-shartiyya"]),
        ("من", ["in-shartiyya"]),
        ("اين", ["in-shartiyya"]),
        ("متى", ["in-shartiyya"]),
        ("انى", []),
        ("اى", ["in-shartiyya"]),
        ("حيثما", ["in-shartiyya"]),
        ("اذما", []),
        ("اذاما", []),
    ]),
    ("mamul-tablolari-turkce.txt", "Amil-i kıyasi (9)", [
        # fail.json: "Its governor (عامل) is the verb itself."
        ("Mutlak Fiil", ["fail"]),
        ("İsmi Fail", []),
        ("İsmi Meful", []),
        ("Sıfatı Müşebbehe", ["sifa-mushabbaha"]),
        ("İsmi Tefdıl", ["ism-tafdil"]),
        ("Masdar", ["masdar"]),
        ("İsmi Muzaf", ["idafa-definiteness"]),
        # The vague-but-complete noun (measures, weights, numbers) is the
        # governor tamyiz.json teaches the tamyiz after.
        ("İsmi Mübhemüt Tam", ["tamyiz"]),
        ("Manayı Fiil", []),
    ]),
    ("mamul-tablolari-turkce.txt", "Amil-i ma'nevî (2)", [
        ("Mübteda – Haberi Raf eder", ["mubtada-khabar"]),
        ("Nevasıb ve Cevazımdan Hali olan Fiili Muzariyi raf eder",
         ["mudari-marfu"]),
    ]),
    ("mamul-tablolari-turkce.txt", "Ma'mulu mensub (13)", [
        ("Mefulu mutlak", ["maful-mutlaq"]),
        ("Mefulu bih", ["maful-bihi"]),
        ("Mefulu fih", ["maful-fih"]),
        ("Mefulu leh", ["maful-lah"]),
        ("Mefulu maah", ["maful-maah"]),
        ("Hal", ["hal"]),
        ("Temyiz", ["tamyiz"]),
        ("Müstesna", ["istithna", "istithna-mufarragh"]),
        ("كان Babının Haberi", ["kana-wa-akhawatuha"]),
        ("ان Babının ismi", ["inna-wa-akhawatuha"]),
        ("Cinsini nefi için olan لا nın ismi", ["la-nafiya-lil-jins"]),
        ("ليس Müşabih olan ما ve لا nın haberi", ["ma-la-mushabbaha"]),
        ("Nevasıbdan biri kendisine dahil olan fiili muzari",
         ["an-masdariyya"]),
    ]),
    # -- research/sources/irab-taksimat-tablolari-turkce.txt ----------------
    ("irab-taksimat-tablolari-turkce.txt", "Ma'mulu mecrur (2)", [
        ("Harfi Cerle Mecrur", ["huruf-jarr"]),
        ("İzafetle Mecrur", ["idafa-definiteness"]),
    ]),
    ("irab-taksimat-tablolari-turkce.txt", "Ma'mulu meczum (1)", [
        ("Cevazımdan biri kendisine dâhil olan Fiili muzari",
         ["lam-jazim", "la-nahiya", "lam-amr", "in-shartiyya"]),
    ]),
    ("irab-taksimat-tablolari-turkce.txt", "Ma'mulu bit-tebeiyye (5)", [
        ("Sıfat", ["naat-sifa", "jumla-sifa"]),
        ("Atıf", ["atf-nasaq"]),
        ("Te'kid", ["tawkid"]),
        ("Bedel", ["badal"]),
        ("Atfı beyan", ["atf-bayan"]),
    ]),
]


def registry_ids() -> set:
    """The set of note ids that actually exist on disk."""
    ids = set()
    for path in sorted(GRAMMAR_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        ids.add(data.get("id") or path.stem)
    return ids


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any mapped note id does not exist on disk")
    args = ap.parse_args()

    existing = registry_ids()
    print(f"Registry: {len(existing)} notes in {GRAMMAR_DIR.relative_to(ROOT)}\n")

    bad_ids = []
    grand_cov = grand_n = 0
    current_source = None
    for source, title, items in CANON:
        if source != current_source:
            current_source = source
            print(f"── research/sources/{source}")
        covered = sum(1 for _, notes in items if notes)
        grand_cov += covered
        grand_n += len(items)
        print(f"  {title}: {covered}/{len(items)} covered")
        for name, notes in items:
            if notes:
                missing = [n for n in notes if n not in existing]
                bad_ids.extend((title, name, n) for n in missing)
                mark = "✗ BAD ID" if missing else "✓"
                print(f"    {mark} {name}  ->  {', '.join(notes)}")
            else:
                print(f"    TODO {name}  (no registry note teaches this yet)")
        print()

    todo = grand_n - grand_cov
    pct = 100 * grand_cov / grand_n if grand_n else 100
    print(f"Overall: {grand_cov}/{grand_n} canonical items covered "
          f"({pct:.0f}%), {todo} TODO")

    if bad_ids:
        print(f"\n{len(bad_ids)} mapped id(s) do not exist on disk "
              "— fix the mapping in this file:")
        for title, name, note in bad_ids:
            print(f"  [{title}] {name} -> {note}")
        if args.strict:
            return 1
    else:
        print("All mapped note ids exist on disk. ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())
