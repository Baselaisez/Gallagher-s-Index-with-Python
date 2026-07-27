# Madrasah source extracts

Text extracted from study materials supplied by the project owner (Turkish
madrasah curriculum, Ottoman-Turkish medium). These are **reference material for
authoring**, not app content: nothing here is shipped to the reader. The grammar
registry cites these works in each note's `classicalSources`.

| File | Source | Extracted from |
|---|---|---|
| `awamil-birgivi-ottoman.txt` | العوامل — Birgivi's *Awamil*, Ottoman-Turkish commentary | `AVAMİL (ni SON HALİ).docx` |
| `awamil-birgivi-tables.txt` | The same work's classification tables (the sixty governors and their governed forms) | tables of the above |
| `izhar-amil-mamul-irab.txt` | إظهار الأسرار — Birgivi's *Izhar*, âmil / ma'mûl / i'râb intensive | `izhar_amil_mamul_i_rab_kamp.doc` |
| `izhar-sual-cevap.txt` | *Izhar* question-and-answer study text | `izhar_sual_ve_cevaplar_tam.doc` |

A fifth upload (`2SARF.rar`, a sarf curriculum: Emsile, Bina, Maksud, and
weak-verb conjugation templates) could not be opened — the archive uses a
compression method the available extractors do not support, and every member
unpacked to zero bytes. Its file listing is preserved below in case the material
is re-supplied in another format.

<details><summary>2SARF.rar listing</summary>

```
1-EMSİLE/EMSİLE TAKSİMAT.jpg
1-EMSİLE/SÜLASİ MUHTELİFE ÇEKİMİ.xls
1-EMSİLE/ZİYADE BABLARDAN MUHTELİFE ÇEKİMİ.xls
1-EMSİLE/ziyade babların muhtelife çekimi harekeli.doc
1-EMSİLE/kelimeler 1.xls
2-BİNA/SUALLER.docx
2-BİNA/İLMİ SARFIN BABLARI arap.doc
3-MAKSUT/MAKSUT ÇALIŞMA KAĞIDI ÜNİ/...
4-KELİME ÇEKİM ŞABLONU/misal-i vavi.xls, misal-i yayi.xls,
    ecvef-i vavi.xls, ecvef-i yayi.xls, nakıs-ı vavi.xls, nakıs-ı yayi.xls,
    Z-DÜRER KELİMELERİ.xls
```
</details>

## What these sources changed in the app

**The Emsile-i Muhtelife** (`ZİYADE BABLARDAN MUHTELİFE ÇEKİMİ.xls`, which did
open). The app already had the *muttarida* — the fourteen-person conjugation
table. It did not have the muhtelife: the fourteen **forms** built from a single
verb, which is the first table of the madrasah curriculum. That table, with the
Turkish form names taken from this source, is now the fourth tab of the
Conjugation panel.

**The Awamil taxonomy.** `awamil-birgivi-tables.txt` is a complete map of the
domain — the governors (20 prepositions, the 8 sisters of inna, the 4 nawasib,
the 15 jawazim, the 9 analogical and 2 abstract governors) and, more usefully,
the governed forms: 9 marfu', 13 mansub, 2 majrur, 1 majzum, 5 by
apposition. Grammar notes carry an `awamil` field placing each in this scheme,
so the registry is organized by the tradition's own categories rather than
ad-hoc ones, and gaps in coverage are visible.

## A note on method

These are teaching texts with their own emphases; the aim is to follow the
classical framework, not to reproduce any single book. A rule enters the
registry when it is attested across the tradition (Emsile/Bina for sarf, Awamil,
Izhar, al-Kafiya and Qatr al-Nada for nahw), with story examples hanging off the
rule rather than defining it.

## Second batch

| File | Source | Status |
|---|---|---|
| `mensubat.txt` | المنصوبات — the thirteen governed-in-nasb categories, 237 questions in Ottoman Turkish | extracted |
| `ZİYADE BABLARDAN MUHTELİFE ÇEKİMİ.xls` | Emsile-i Muhtelife for the augmented babs | extracted (see above) |
| `SARF ... Kopya (7).xls` | blank conjugation worksheet: muttarida x (ma'lum / majhul), nun al-tawkid, muhtelife | extracted |
| `ZDÜRER KELİMELERİ.xls` | vocabulary from al-Durar | extracted |
| `SULH.doc`, `VAKIF_MALI.doc` | fiqh passages (sulh, waqf property) | **no recoverable text** |

The two fiqh documents could not be read: their WordDocument streams are
essentially empty — no text runs under any of the plausible encodings, and no
embedded images either. Re-supplying them as `.docx`, `.txt` or PDF would let
them become Level 5-6 stories, which is what they are suited to.

The Mensûbât file filled the gap the Awamil taxonomy had exposed: six of the
thirteen mansubat had no note. Each new note now quotes that source's
definition, and chapter 2 of the Abu Yusuf wasiyya was authored to give three
of them real examples rather than invented ones.

The SARF worksheet also shows two dimensions the app does not yet model:
**ma'lum / majhul** (active and passive) and the **nun al-tawkid** forms. The
passive already occurs in the corpus — تُسْأَلُ in Abu Yusuf 2:s8 is analyzed
as mabni li'l-majhul — so the data supports it before the tables do.

## Fourth batch — sarf rules and balagha

| File | Source | What it gave the app |
|---|---|---|
| `ilal-misal-ecvef-naqis.txt` | كواعد الإعلال — the i'lal rules for the three weak classes, Ottoman Turkish | the `mithal-verbs` and `naqis-verbs` notes, and a rewritten `hollow-verbs` |
| `bablara-nakil-tablosu.txt` | «bablara nakil» — 11 roots × 12 augmented babs | the `augmented-babs` note |
| `masdar-sifa-mubalagha-vezinleri.txt` | 32 masdar patterns, 17 sifa mushabbaha patterns, 8+1 mubalagha patterns | the `sighat-mubalagha` note |
| `alaqat-al-majaz-balagha.txt` | علاقات المجاز — the relations licensing figurative usage | not yet used — see below |
| `talkhis-al-miftah-balagha.txt` | تلخيص المفتاح (al-Qazwini), Ottoman-Turkish commentary, 247k Arabic letters | not yet used — see below |

### The i'lal document is a verification, not just a source

Every weak-verb paradigm in the corpus was hand-written before this document
arrived, on the principle that a derived form is a guessed form. The rules it
states confirm each of them independently:

| Rule in the source | Form already in the corpus |
|---|---|
| after dropping the alif, the preceding fatha becomes damma for a lost و, kasra for a lost ي | قُلْنَ, قُمْنَ, كُنَّ — and بِعْنَ, كِلْنَ |
| moving the vowel back, then dropping the weak letter when two sukuns meet | لَمْ يَقُلْ, لَمْ يَبِعْ |
| in the passive madi the damma goes and the kasra moves back | قِيلَ, بِيعَ, خِيفَ |
| the و/ي after the alif of the ism fa'il becomes hamza | قَائِل, قَائِم |
| i'lal in إفعال، انفعال، افتعال، استفعال only — not in فعّل، فاعل، تفعّل، تفاعل | تَصَوَّرَ / يَتَصَوَّرُ conjugated as sound, وَقَّرَ keeping its و |
| a final و past the third letter becomes ي | اِدَّعَى and its ism fa'il مُدَّعٍ |
| a kasra on a final weak letter is dropped as heavy | تَخْلِينَ, تَدَّعِينَ |

Nothing had to be corrected. That is the strongest argument yet for storing
these forms rather than deriving them at build time.

### Balagha: a layer the app does not have yet

The Talkhis and the ʿAlaqat documents are rhetoric, not grammar — majaz and its
relations, tashbih, kinaya, the three divisions maʿani / bayan / badiʿ. The
registry currently has three groups (sarf, nahw, awamil) and no place to put
them. Adding a fourth group is the natural next step once the nahw coverage
stops growing; the material is transcribed and waiting.
