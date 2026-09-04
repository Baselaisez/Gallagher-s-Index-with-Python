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

### Balagha: the layer now exists

The Talkhis and the ʿAlaqat documents are rhetoric, not grammar — majaz and its
relations, tashbih, kinaya, the divisions maʿani / bayan / badiʿ. The registry
now carries a fourth group, `balagha`, with five notes drawn from them:
`haqiqa-majaz`, `tashbih`, `istiara`, `kinaya`, `qasr`.

The ʿAlaqat treatise supplies the definitions verbatim, which is why the notes
can quote them rather than paraphrase: majaz is «لفظ مستعمل في غير ما وضع له …
بعلاقة بينهما مع قرينة مانعة عن إرادة الموضوع له», kinaya is «لفظ مستعمل في لازم
ما وضع له بلا قرينة مانعة» — and that last clause, *without* a blocking clue, is
the whole difference between the two.

Every note anchors to text already in the corpus. That was the argument for the
layer: the stories had been doing rhetoric all along — «be to him as you are to
fire», «laughter kills the heart», «beasts are what get called from behind» —
and the app had nothing to say about it. Only maʿani and bayan are covered;
badiʿ is still untouched.

## Fifth batch — the 35 babs, and a fiqh text with no Arabic in it

| File | Source | Status |
|---|---|---|
| `sarf-35-bab-tablosu.txt` | إلمي صرفك بابلرى — the complete 35-bab taxonomy: wazn, mawzun, ʿalāmat, binā and a sample sentence for each | → `thulathi-mujarrad-babs`, and the meanings in `augmented-babs` |
| `misal-kaideleri-mesnedli.txt` | the mithal rules again, this time **with page citations** (Marah al-Arwah 83-84, ʿIzzi 148-150, Maqsud 183/205, Mulakhkhas 66) | → citations added to `mithal-verbs`; **corrected an error** (see below) |
| `buyu-tarifler-turkish.txt` | بيوع بحثى تعريفلر — Turkish definitions for the chapter on sales, then nikah | → the `kitab-al-buyu` story (see below) |
| `irab-taksimat-turkish.txt` | i'rab taxonomy in Turkish: mamul majrur/majzum, i'rab by haraka/harf/hazf, lafzi/taqdiri/mahalli, and the table of case-marks by noun class | headers extracted; **the table cells did not survive** — the Word table structure defeats the stream reader. Re-supplying as `.docx` or PDF would recover it |

### A correction the citations forced

`mithal-verbs` said the asl of عِدَة was وِعْدًا. The mesnedli copy gives وِعْدَة —
which is the only reading consistent with the rule, since the rule is about the
وزن فِعْلَة. Fixed, with the page reference. Two copies of the same ruleset
disagreed and the one carrying citations was right; that is an argument for
preferring sources that cite.

### The Buyu' document has no Arabic in it

It is a Turkish definition list — «Beyi: karşılıklı rıza ile bir malı başka bir
mal ile değiştirmektir» — covering bay', the three khiyars, murabaha, tawliya,
wadi'a, musawama, riba, salam, sarf, rahn, hajr, iqrar, ijara, shuf'a, the four
sharikas, mudaraba, wakala, kafala, hawala, sulh, hiba, waqf, ghasb, wadi'a,
'ariya, laqit, luqata, mafqud, ibaq, ma'dhun, ihya' al-mawat, muzara'a, and then
a nikah section.

To make a story out of it the Arabic had to be supplied. Each ta'rif in
`kitab-al-buyu` is the **received wording** of the standard Hanafi definition the
Turkish is translating — chiefly al-Quduri's Mukhtasar and al-Marghinani's
Hidaya, with the Mecelle (art. 105) behind the definition of bay'. Where the two
diverge the received wording wins: the source's havale definition names the
creditor's dhimma, which is a slip, so نَقْلُ الدَّيْنِ مِنْ ذِمَّةٍ إِلَى ذِمَّةٍ
was not used at all rather than reproduce it. The manifest states all of this,
and adds that these are teaching definitions for reading practice, not a fatwa.

The nikah section of the document is left for a later story.

## Turkish i'rab tables and the edat (question) test — added 2026-07-28

Five `.doc` uploads, decoded utf-16-le from the WordDocument stream:

| file | contents |
|---|---|
| `edatlar-irab-soru-testi.txt` | **the question test** — which Turkish interrogative each i'rab role answers |
| `amil-tablolari-turkce.txt` | the 'amil tables: 20 huruf jarr, inna's 8 sisters, ma/la mushabbaha bi-laysa, the 4 nawasib |
| `mamul-tablolari-turkce.txt` | the 15 jawazim, 'amil qiyasi (9), 'amil ma'nawi (2), the mansubat (13) |
| `irab-taksimat-tablolari-turkce.txt` | majrur, majzum, i'rab bi hasab al-dhat (haraka / harf / hazf), the five tawabi' |
| `kafiya-turkce-sual-cevap.txt` | al-Kafiya in Turkish question-and-answer form |

`edatlar` is the one that changed the app. It records the Ottoman madrasah's own
answer to *how do I know which i'rab this is?* — you ask which question the word
answers. Fa'il answers «Ne? Kim?»; maf'ul fih answers «Nerede? Ne zaman?»; hal
answers «Ne olduğu halde?». It is now the `question` field on eleven nahw notes.

The device works in Turkish because Turkish case endings line up with Arabic's.
The English in those notes is therefore a **functional equivalent, not a
translation** — English has no cases to line up, so «Neyi?» and «Neye?» both
come out as some form of "what", and the note says so rather than pretending the
mapping is exact.

One line of the maf'ul fih entry is damaged in the original by binary noise
(`... kadar, Ne zamana kadar`). Only the interrogatives that read cleanly were
transcribed; the fragment was left out rather than guessed at.

## The 2026-07-29 uploads

| file | contents |
|---|---|
| `kafiya-internet-digest.txt` | a compact modern-Turkish Kafiya digest: murab/mebni, gayr-ı munsarıf, precedence and hazf rules, tenâzu, mef'ul types, ef'âl-i kulûb/nâkısa/mukârebe, and the full particle taxonomy |
| `emali-qasida-ottoman.txt` | Bed' al-Amali (Siraj al-Din al-Ushi) verse by verse, with an Ottoman-Turkish word-by-word parse, translation and Q&A after each verse |

The digest closed the canon audit. The amil table's mystery `الا` in the إنّ
row is أَلَا التنبيه — it habitually stands directly before إِنَّ (أَلَا إِنَّ
زَيْدًا قَائِمٌ), which explains its seat in that row, and it governs nothing
itself (`huruf-tanbih` says so). «Manayı Fiil» among the governors is the
digest's third amil of hal — «mana fiildir, هذا زيد قائما gibi» — now
`mana-al-fil`. With those two, `check_canon.py --strict` reports 81/81.

The Emali file is future story material, not yet content: the Arabic verses
are the received qasida text (good), but the commentary is Ottoman Turkish in
Arabic script and must be converted to modern Turkish — and the verse i'rab
authored from scratch — before any of it faces a reader.
