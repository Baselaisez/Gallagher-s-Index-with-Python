#!/usr/bin/env python3
"""(wave 183) A verb whose doer is WRITTEN keeps no hidden one beside it.

The engine composes a verb's line before it knows what the next word turned out to be, so a line could say
«وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ» while the very next word's line says «فَاعِلٌ مَرْفُوعٌ» (قَالَ عَطَاءُ),
or «وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ» before «نَائِبُ فَاعِلٍ» (تُبْدَلُ الْمِيمُ، لَا يُوجَدُ فِي آخِرِ الِاسْمِ وَاوٌ).
Two doers for one verb is no grammar: الْفَاعِلُ لَا يَتَعَدَّدُ. The written one stands; the hidden clause is dropped
from the verb's line in all three languages.

The scan from the verb walks only over what can stand between a verb and its doer — particles, a jarr phrase with
its annexation, a ẓarf, a fronted object — and stops at anything else, at a pause, and at a word joined by a
conjunction (which opens its own seat). Used by pkg_from_engine.py on every package it builds, and runnable over
landed packages:

    python3 tools/authoring/doer_dedupe.py content/samples/<pkg> [...]      # rewrites chapters in place
    python3 tools/authoring/doer_dedupe.py --dry content/samples/*          # reports only
"""
import io, json, os, re, sys, glob

HID_AR = re.compile(r"، وَ(?:الْفَاعِلُ|نَائِبُ الْفَاعِلِ) ضَمِيرٌ مُسْتَتِرٌ(?: وُجُوبًا| جَوَازًا)?(?: تَقْدِيرُهُ [^،.]+)?")
HID_EN = re.compile(r"; its (?:deputy )?doer is a hidden pronoun(?: «[^»]+»)?")
HID_TR = re.compile(r"; (?:nâib-i )?fâili gizli zamir(?:dir)?(?: «[^»]+»)?")
DOER = re.compile(r"^(?:فَاعِلٌ|نَائِبُ فَاعِلٍ)(?![ًٌٍَُِّْ]*[ء-ي])|فِي مَحَلِّ رَفْعٍ (?:فَاعِلٌ|نَائِبُ فَاعِلٍ)")
BETWEEN = re.compile(r"^(?:«[^»]+» )?(?:حَرْفُ|مَجْرُورٌ|مُضَافٌ إِلَيْهِ|ظَرْفُ|مَفْعُولٌ بِهِ|اللَّامُ حَرْفُ جَرٍّ|الْبَاءُ حَرْفُ جَرٍّ|الْكَافُ حَرْفُ جَرٍّ|اسْمٌ مَجْرُورٌ)")
PAUSE = re.compile(r"[.:،؛؟!]")


def _ar(t):
    return ((t.get("irab") or {}).get("ar") or "")


def doer_dedupe(toks, window=6):
    """drops the hidden-doer clause from every verb line whose written doer follows; returns the token indexes changed"""
    hit = []
    for i, t in enumerate(toks):
        if t.get("pos") != "verb": continue
        ir = t.get("irab") or {}
        if not HID_AR.search(ir.get("ar") or ""): continue
        if PAUSE.search(t.get("punctAfter") or ""): continue
        found = False
        for j in range(i + 1, min(i + 1 + window, len(toks))):
            lj = _ar(toks[j])
            if toks[j].get("pos") != "verb" and DOER.search(lj) and not lj.startswith(("الْوَاوُ", "الْفَاءُ")): found = True; break
            if toks[j].get("pos") == "verb": break
            if not (toks[j].get("pos") == "part" or BETWEEN.search(lj)): break
            if PAUSE.search(toks[j].get("punctAfter") or ""): break
        if not found: continue
        ir["ar"] = HID_AR.sub("", ir["ar"], count=1)
        if isinstance(ir.get("en"), str): ir["en"] = HID_EN.sub("", ir["en"], count=1)
        if isinstance(ir.get("tr"), str): ir["tr"] = HID_TR.sub("", ir["tr"], count=1)
        hit.append(i)
    return hit


def main(argv):
    dry = "--dry" in argv
    total = 0
    for pkg in [a for a in argv if not a.startswith("--")]:
        n = 0
        for f in sorted(glob.glob(os.path.join(pkg, "chapters", "*.json"))):
            raw = io.open(f, encoding="utf-8").read()
            c = json.loads(raw)
            changed = False
            for si, s in enumerate(c.get("sentences", [])):
                hit = doer_dedupe(s.get("tokens", []))
                for i in hit:
                    n += 1; changed = True
                    if dry: print(f"{os.path.basename(pkg)} {os.path.basename(f)[:-5]}:s{si + 1}:{i} {s['tokens'][i]['surface']['full']} → {' '.join(x['surface']['full'] for x in s['tokens'][i + 1:i + 4])}")
            if changed and not dry:
                indent = 2 if raw.startswith("{\n  ") else (1 if raw.startswith("{\n ") else None)
                out = json.dumps(c, ensure_ascii=False, indent=indent) if indent else json.dumps(c, ensure_ascii=False, separators=(",", ":") if '": ' not in raw[:400] else None)
                io.open(f, "w", encoding="utf-8").write(out + ("\n" if raw.endswith("\n") else ""))
        if n: print(f"{os.path.basename(pkg)}: {n} verb line(s) relieved of a second doer")
        total += n
    print(f"total {total}")


if __name__ == "__main__":
    main(sys.argv[1:])
