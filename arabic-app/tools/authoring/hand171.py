#!/usr/bin/env python3
"""hand171.py — (wave 171) the nominal clauses the label gauge brought to light in the two engine-drafted books.

The drafted lines named a predicate «مُبْتَدَأٌ», or called the subject of a NEW clause «مَعْطُوفٌ» while naming its own
predicate «خَبَرٌ» in the next line. Each clause now reads mubtadaʾ + khabar:

  «الْمَقَامَاتُ»        1:s8   وَالطَّرِيقَةُ أَغْصَانُهَا
                         2:s12  وَقِيلَ: الْإِيمَانُ شَاةٌ، وَالْعَقْلُ رَاعٍ، وَالْإِبْلِيسُ ذِئْبٌ   (the quoted saying is three clauses; رَاعٍ is manqūṣ)
                         2:s13  وَقِيلَ: الْإِيمَانُ لَبَنٌ، وَالْعَقْلُ حَافِظٌ، وَالْإِبْلِيسُ كَلْبٌ
                         10:s2  … عَلَيْهِ السَّلَامُ: الْحَيَاءُ مِنَ الْإِيمَانِ          (the saying opens with its own mubtadaʾ)
  «الْأُصُولُ الْمُنِيفَةُ»  11:s2  وَهِيَ عُقُوبَةُ الْمَخْذُولِ
                         21:s1  وَالْعَمَلُ غَيْرُ الْإِيمَانِ وَالْإِيمَانُ غَيْرُ الْعَمَلِ
                         22:s12 وَهُمْ أُمَنَاءُ الرَّحْمٰنِ

The written vowels are left exactly as shipped; only the lines that name them change. Writes the lines into each
package's fixes.json (so a regeneration keeps them) and, with --apply, into the shipped chapters.
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
SAMPLES = HERE.parent.parent / "content" / "samples"
MK = ["mubtada-khabar"]; MKI = ["mubtada-khabar", "idafa-definiteness"]
MUB = {"irab": {"ar": "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "en": "The mubtada (subject of the nominal sentence), in raf'; the sign is the damma.", "tr": "Mübtedâ, merfû; alâmeti damme ile."}, "tags": MK}
WMUB = {"irab": {"ar": "الْوَاوُ عَاطِفَةٌ، وَمُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "en": "The waw conjoins; the mubtada (subject of the nominal sentence), in raf'; the sign is the damma.", "tr": "«ve» + mübtedâ, merfû; alâmeti damme ile."}, "tags": MK}
KH = {"irab": {"ar": "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "en": "The khabar (predicate), in raf'; the sign is the damma.", "tr": "Haber, merfû; alâmeti damme ile."}, "tags": MK}
KHM = {"irab": {"ar": "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "en": "The khabar (predicate), in raf'; the sign is the damma; annexed (mudaf).", "tr": "Haber, merfû; alâmeti damme ile; muzâf."}, "tags": MKI}
KHQ = {"irab": {"ar": "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ.", "en": "The khabar (predicate), in raf'; the sign is a damma estimated on the dropped yāʾ — a manqūṣ noun.", "tr": "Haber, merfû; alâmeti hazfedilmiş yâ üzerinde takdir edilen damme — menkûs isim."}, "tags": ["mubtada-khabar", "ism-maqsur-manqus"]}
PHIYA = {"irab": {"ar": "الْوَاوُ عَاطِفَةٌ، وَضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "en": "The waw conjoins; «she / it» — a detached pronoun; in the place of raf' as the mubtada.", "tr": "«ve» + «o (dişil)» — munfasıl zamir, mahallen merfû, mübtedâ."}, "tags": ["al-mabni-wal-mudmar", "mubtada-khabar"]}
PHUM = {"irab": {"ar": "الْوَاوُ عَاطِفَةٌ، وَضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "en": "The waw conjoins; «they» — a detached pronoun; in the place of raf' as the mubtada.", "tr": "«ve» + «onlar» — munfasıl zamir, mahallen merfû, mübtedâ."}, "tags": ["al-mabni-wal-mudmar", "mubtada-khabar"]}
FIX = {
 "al-maqamat-birgivi": ("maqamat", {
   "1:s8:9": (WMUB, "وَالطَّرِيقَةُ"),
   "2:s12:1": (MUB, "الْإِيمَانُ"), "2:s12:2": (KH, "شَاةٌ"), "2:s12:3": (WMUB, "وَالْعَقْلُ"), "2:s12:4": (KHQ, "رَاعٍ"), "2:s12:5": (WMUB, "وَالْإِبْلِيسُ"), "2:s12:6": (KH, "ذِئْبٌ"),
   "2:s13:1": (MUB, "الْإِيمَانُ"), "2:s13:2": (KH, "لَبَنٌ"), "2:s13:5": (WMUB, "وَالْإِبْلِيسُ"), "2:s13:6": (KH, "كَلْبٌ"),
   "10:s2:7": (MUB, "الْحَيَاءُ")}),
 "al-usul-al-munifa": ("usul", {
   "11:s2:13": (PHIYA, "وَهِيَ"), "11:s2:14": (KHM, "عُقُوبَةُ"),
   "21:s1:4": (KHM, "غَيْرُ"), "21:s1:6": (WMUB, "وَالْإِيمَانُ"), "21:s1:7": (KHM, "غَيْرُ"),
   "22:s12:11": (PHUM, "وَهُمْ"), "22:s12:12": (KHM, "أُمَنَاءُ")}),
}


def main():
    for pkg, (folder, fixes) in FIX.items():
        fp = HERE / folder / "fixes.json"; f = json.load(open(fp, encoding="utf-8"))
        for k, (v, _) in fixes.items(): f[k] = {**(f.get(k) or {}), "irab": dict(v["irab"]), "tags": list(v["tags"])}
        json.dump(f, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(pkg, len(f), "fixes in fixes.json")
        if "--apply" not in sys.argv: continue
        by = {}
        for k, v in fixes.items(): ch, sid, i = k.split(":"); by.setdefault(ch, []).append((sid, int(i), v))
        for ch, rows in by.items():
            p = SAMPLES / pkg / "chapters" / f"{ch}.json"; d = json.load(open(p, encoding="utf-8"))
            for sid, i, (v, word) in rows:
                t = next(s for s in d["sentences"] if s["id"] == sid)["tokens"][i]
                assert t["surface"]["full"] == word, (pkg, ch, sid, i, t["surface"]["full"], word)
                print(f"{ch}:{sid}:{i} {word}\n   - {t['irab']['ar']}\n   + {v['irab']['ar']}")
                t["irab"] = dict(v["irab"]); t["grammar"] = list(v["tags"])
            json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
