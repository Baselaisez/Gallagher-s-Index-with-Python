#!/usr/bin/env python3
"""passive_trilingual.py — one line, three languages, one statement.

Where the Arabic line of a passive verb names a DEPUTY doer, the English and the Turkish must name it too:
  «… وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ …»            ↔ «; its deputy doer is a hidden pronoun …» / «; nâib-i fâili gizli zamir …»
  «… وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَحْكِيَّةُ بَعْدَهُ» ↔ «; its deputy doer is the clause quoted after it» / «; nâib-i fâili ondan sonra hikâye edilen cümledir»
The engine builder wrote «its doer is a hidden pronoun» under both (wave 185 found 82 + 15 such lines on the shelf).

  from passive_trilingual import passive_trilingual; passive_trilingual(toks)
  python3 tools/authoring/passive_trilingual.py [--dry] content/samples/<pkg> …      (keeps indent=1 JSON)
"""
import io, json, re, sys, glob, os

HID = "نَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ"
QUO = "نَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَحْكِيَّةُ بَعْدَهُ"
EN_HID = re.compile(r"; its doer is a hidden pronoun((?: «[^»]+»)?)")
TR_HID = re.compile(r"; fâili gizli zamir((?:dir)?(?: «[^»]+»)?)")


def passive_trilingual(toks):
    """rewrites the en/tr of the tokens' lines in place; returns the number of lines changed"""
    n = 0
    for t in toks:
        ir = t.get("irab") or {}
        ar, en, tr = ir.get("ar", ""), ir.get("en", ""), ir.get("tr", "")
        if QUO in ar:
            en2 = EN_HID.sub("; its deputy doer is the clause quoted after it", en)
            tr2 = TR_HID.sub("; nâib-i fâili ondan sonra hikâye edilen cümledir", tr)
        elif HID in ar:
            en2 = EN_HID.sub(lambda m: "; its deputy doer is a hidden pronoun" + m.group(1), en)
            tr2 = TR_HID.sub(lambda m: "; nâib-i fâili gizli zamir" + m.group(1), tr)
        else:
            continue
        if en2 != en or tr2 != tr:
            ir["en"], ir["tr"] = en2, tr2
            n += 1
    return n


def main(argv):
    dry = "--dry" in argv
    total = 0
    for pkg in [a for a in argv if not a.startswith("--")]:
        k = 0
        for f in sorted(glob.glob(os.path.join(pkg, "chapters", "*.json"))):
            raw = io.open(f, encoding="utf-8").read()
            d = json.loads(raw)
            if json.dumps(d, ensure_ascii=False, indent=1) != raw.rstrip("\n"):
                print("  skipped (not an indent=1 file):", f)
                continue
            c = sum(passive_trilingual(s.get("tokens") or []) for s in d.get("sentences") or [])
            if c and not dry:
                io.open(f, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + ("\n" if raw.endswith("\n") else ""))
            k += c
        print(f"{os.path.basename(os.path.normpath(pkg))}: {k} line(s)")
        total += k
    print("total", total, "(dry)" if dry else "")


if __name__ == "__main__":
    main(sys.argv[1:])
