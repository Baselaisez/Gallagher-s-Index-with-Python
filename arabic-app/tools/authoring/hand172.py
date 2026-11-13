#!/usr/bin/env python3
"""hand172.py — (wave 172) «خَبَرُ إِنَّ»: twenty-five lines in the three engine-drafted books said only «خَبَرٌ» of the
predicate that follows إِنَّ / أَنَّ wearing its noun as a pronoun (فَإِنَّهُ مُنَافِقٌ، لِأَنَّهُمْ ضُعَفَاءُ، أَنَّهُمَا مُهْتَدِيَتَانِ).
The line now names the particle whose khabar it is, and the token is anchored to the note on إِنَّ and her sisters.
Where a pronoun of separation stands between them (إِنَّهُ هُوَ التَّوَّابُ) the stored reading — the pronoun in the place of
rafʿ with its own khabar — is left as it is. Found by the label gauge (the engine's rule R13 named the office; the stored line did not).

The written vowels are left exactly as shipped; only the lines that name them change. Writes the lines into each
package's fixes.json (so a regeneration keeps them) and, with --apply, into the shipped chapters.
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
SAMPLES = HERE.parent.parent / "content" / "samples"
FOLDER = {"al-maqamat-birgivi": "maqamat", "al-usul-al-munifa": "usul", "tasrif-al-izzi": "izzi"}
FIX = json.loads(r'''{
 "al-maqamat-birgivi": {
  "2:s7:8": {
   "word": "مُنَافِقٌ",
   "after": "فَإِنَّهُ",
   "irab": {
    "ar": "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of إِنَّ, in raf'; the sign is the damma.",
    "tr": "İnne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "4:s1:4": {
   "word": "فَرْضٌ",
   "after": "لِأَنَّهُ",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma.",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "5:s3:8": {
   "word": "فَرْضٌ",
   "after": "لِأَنَّهُ",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma.",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  }
 },
 "al-usul-al-munifa": {
  "2:s15:21": {
   "word": "جَاهِلٌ",
   "after": "فَإِنَّهُ",
   "irab": {
    "ar": "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of إِنَّ, in raf'; the sign is the damma.",
    "tr": "İnne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "2:s22:8": {
   "word": "بِدْعَةٌ",
   "after": "فَإِنَّهَا",
   "irab": {
    "ar": "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of إِنَّ, in raf'; the sign is the damma.",
    "tr": "İnne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "3:s16:20": {
   "word": "مُقِرٌّ",
   "after": "أَنَّهُ",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma.",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "5:s8:16": {
   "word": "مُحْدَثَةٌ",
   "after": "إِنَّهَا",
   "irab": {
    "ar": "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of إِنَّ, in raf'; the sign is the damma.",
    "tr": "İnne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "7:s2:6": {
   "word": "أَفْعَالُ",
   "after": "لِأَنَّهَا",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma; annexed (mudaf).",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile; muzâf."
   },
   "tags": [
    "mubtada-khabar",
    "idafa-definiteness",
    "inna-wa-akhawatuha"
   ]
  },
  "8:s8:20": {
   "word": "مُؤْمِنَةٌ",
   "after": "فَإِنَّهَا",
   "irab": {
    "ar": "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of إِنَّ, in raf'; the sign is the damma.",
    "tr": "İnne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "13:s4:8": {
   "word": "ضُعَفَاءُ",
   "after": "لِأَنَّهُمْ",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma.",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "13:s4:18": {
   "word": "حُصُولٌ",
   "after": "لِأَنَّهُ",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma.",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "14:s17:42": {
   "word": "شِيعَةُ",
   "after": "فَإِنَّهُمْ",
   "irab": {
    "ar": "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.",
    "en": "The khabar (predicate) of إِنَّ, in raf'; the sign is the damma; annexed (mudaf).",
    "tr": "İnne'nin haberi, merfû; alâmeti damme ile; muzâf."
   },
   "tags": [
    "mubtada-khabar",
    "idafa-definiteness",
    "inna-wa-akhawatuha"
   ]
  },
  "14:s35:13": {
   "word": "مَجْبُورُونَ",
   "after": "لِأَنَّهُمْ",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the waw — a sound masculine plural.",
    "tr": "Enne'nin haberi, merfû; alâmeti vâv ile — cem'-i müzekker sâlim."
   },
   "tags": [
    "mubtada-khabar",
    "jam-mudhakkar-salim",
    "inna-wa-akhawatuha"
   ]
  },
  "20:s7:6": {
   "word": "مُؤْمِنٌ",
   "after": "فَإِنِّي",
   "irab": {
    "ar": "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of إِنَّ, in raf'; the sign is the damma.",
    "tr": "İnne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "20:s12:19": {
   "word": "مُؤْمِنٌ",
   "after": "أَنِّي",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma.",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "22:s12:10": {
   "word": "الْقَادَةُ",
   "after": "لِأَنَّهُمُ",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma.",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "24:s7:61": {
   "word": "مُؤْمِنٌ",
   "after": "أَنَّهُ",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma.",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "24:s13:12": {
   "word": "مُؤْمِنُونَ",
   "after": "أَنَّهُمْ",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the waw — a sound masculine plural.",
    "tr": "Enne'nin haberi, merfû; alâmeti vâv ile — cem'-i müzekker sâlim."
   },
   "tags": [
    "mubtada-khabar",
    "jam-mudhakkar-salim",
    "inna-wa-akhawatuha"
   ]
  },
  "24:s13:24": {
   "word": "كُفَّارٌ",
   "after": "أَنَّهُمْ",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma.",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "24:s15:47": {
   "word": "مُهْتَدِيَتَانِ",
   "after": "أَنَّهُمَا",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the alif — it is a dual.",
    "tr": "Enne'nin haberi, merfû; alâmeti elif ile — tesniyedir."
   },
   "tags": [
    "mubtada-khabar",
    "al-muthanna",
    "inna-wa-akhawatuha"
   ]
  },
  "24:s15:53": {
   "word": "ضَالَّتَانِ",
   "after": "أَنَّهُمَا",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the alif — it is a dual.",
    "tr": "Enne'nin haberi, merfû; alâmeti elif ile — tesniyedir."
   },
   "tags": [
    "mubtada-khabar",
    "al-muthanna",
    "inna-wa-akhawatuha"
   ]
  },
  "33:s2:25": {
   "word": "قَرِيبٌ",
   "after": "لِأَنَّهُ",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma.",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  }
 },
 "tasrif-al-izzi": {
  "5:s5:7": {
   "word": "زَائِدَةٌ",
   "after": "فَإِنَّهَا",
   "irab": {
    "ar": "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of إِنَّ, in raf'; the sign is the damma.",
    "tr": "İnne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "7:s5:6": {
   "word": "ضَمِيرٌ",
   "after": "فَإِنَّهُ",
   "irab": {
    "ar": "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of إِنَّ, in raf'; the sign is the damma.",
    "tr": "İnne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  },
  "17:s1:19": {
   "word": "حَرْفٌ",
   "after": "لِأَنَّهَا",
   "irab": {
    "ar": "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.",
    "en": "The khabar (predicate) of أَنَّ, in raf'; the sign is the damma.",
    "tr": "Enne'nin haberi, merfû; alâmeti damme ile."
   },
   "tags": [
    "mubtada-khabar",
    "inna-wa-akhawatuha"
   ]
  }
 }
}''')


def main():
    for pkg, fixes in FIX.items():
        fp = HERE / FOLDER[pkg] / "fixes.json"; f = json.load(open(fp, encoding="utf-8"))
        for k, v in fixes.items(): f[k] = {**(f.get(k) or {}), "irab": dict(v["irab"]), "tags": list(v["tags"])}
        json.dump(f, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print(pkg, len(f), "fixes in fixes.json")
        if "--apply" not in sys.argv: continue
        by = {}
        for k, v in fixes.items(): ch, sid, i = k.split(":"); by.setdefault(ch, []).append((sid, int(i), v))
        for ch, rows in by.items():
            p = SAMPLES / pkg / "chapters" / f"{ch}.json"; d = json.load(open(p, encoding="utf-8"))
            for sid, i, v in rows:
                t = next(s for s in d["sentences"] if s["id"] == sid)["tokens"][i]
                assert t["surface"]["full"] == v["word"], (pkg, ch, sid, i, t["surface"]["full"], v["word"])
                print(f"{ch}:{sid}:{i} {v['word']}\n   - {t['irab']['ar']}\n   + {v['irab']['ar']}")
                t["irab"] = dict(v["irab"]); t["grammar"] = list(v["tags"])
            json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
