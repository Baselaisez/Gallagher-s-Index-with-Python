#!/usr/bin/env python3
"""hand209.py — (wave 209) two drafted lines of «الْأُصُولُ الْمُنِيفَةُ» the wave's reader rules brought to light.

  28:s5  … وَيُضِلُّ اللهُ الظَّالِمِينَ …
      «الظَّالِمِينَ» is written with its yāʾ behind a singular doer in rafʿ: it is the verb's object, in naṣb by the yāʾ.
      The drafted line called it a naʿt «مَرْفُوعٌ بِالْوَاوِ» — a wāw the word does not wear.

  34:s1  خُرُوجُ الدَّجَّالِ … وَمَا وَرَدَ بِالْأَخْبَارِ الصَّحِيحَةِ حَقٌّ كَائِنٌ
      «حَقٌّ» is the khabar of the mubtadaʾ the sentence opens with («خُرُوجُ …» and what is joined to it); the doer of
      «وَرَدَ» is the relative's returning pronoun, as the verb's own stored line says. The drafted line called «حَقٌّ»
      a doer.

The written vowels are left exactly as shipped. Writes into the package's fixes.json (so a regeneration keeps the
fix) and, with --apply, into the shipped chapters.
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
SAMPLES = HERE.parent.parent / "content" / "samples"
PKG, FOLDER = "al-usul-al-munifa", "usul"

LINES = [
    ("28:s5:21", "الظَّالِمِينَ",
     {"irab": {"ar": "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
               "en": "The object (maf'ul bihi), in nasb; the sign is the ya — a sound masculine plural.",
               "tr": "Mef'ûlün bih, mansûb; alâmeti yâ ile — cem'-i müzekker sâlim."},
      "tags": ["maful-bihi", "jam-mudhakkar-salim"]}),
    ("34:s1:27", "حَقٌّ",
     {"irab": {"ar": "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.",
               "en": "The khabar (predicate), in raf'; the sign is the damma.",
               "tr": "Haber, merfû; alâmeti damme ile."},
      "tags": ["mubtada-khabar"]}),
]


def main():
    apply = "--apply" in sys.argv
    fp = HERE / FOLDER / "fixes.json"
    f = json.load(open(fp, encoding="utf-8"))
    for where, word, v in LINES:
        f[where] = {**(f.get(where) or {}), "irab": dict(v["irab"]), "tags": list(v["tags"])}
    text = json.dumps(f, ensure_ascii=False, indent=1)
    open(fp, "w", encoding="utf-8").write(text)
    print(PKG, len(f), "fixes in fixes.json")
    if not apply:
        return
    for where, word, v in LINES:
        ch, sid, i = where.split(":")
        p = SAMPLES / PKG / "chapters" / f"{ch}.json"
        d = json.load(open(p, encoding="utf-8"))
        t = next(s for s in d["sentences"] if s["id"] == sid)["tokens"][int(i)]
        assert t["surface"]["full"] == word, t["surface"]["full"]
        print(f"{where} {word}\n   - {t['irab']['ar']}\n   + {v['irab']['ar']}")
        t["irab"] = dict(v["irab"]); t["grammar"] = list(v["tags"])
        out = json.dumps(d, ensure_ascii=False, indent=1)
        open(p, "w", encoding="utf-8").write(out)


if __name__ == "__main__":
    main()
