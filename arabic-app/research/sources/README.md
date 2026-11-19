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

## The 2026-10-01 uploads — seven PDFs, read cover to cover

| file | contents |
|---|---|
| `avamil-dersi-servet-hayma-2023.txt` | Servet Hayma's 44-page «Avâmil dersi» (İhtisas Okulu, 24 Jan 2023): Birgivī's 60 ʿāmil / 30 maʿmūl / 10 iʿrāb tree taught through the «İ'rab Mağazası» metaphor (Müşteri = the word kind, Beden = the sign, Endam = the maʿmūl seat, Etki eden = the ʿāmil), the nine declension classes with their tam/nakıs sign tables, taqdīrī iʿrāb's three obstacles (teazzür / istiskal / münasebet), the mabnī lists, the 14 sentence kinds with and without a maḥall, the «AJAN EN» mnemonic for the hidden أن |
| `serhul-mugni-ders-notlari-kisa-1.txt` | 96 pages of Şerhu'l-Muğnî lesson notes in modern Turkish: the ism in 15 kinds, the six nouns, ghayr munṣarif's nine causes, the munādā's seven rulings, the 17 lāzim-mabnī ẓarfs, taṣghīr and nisba, jamʿ qilla, the nawāsikh with muqāraba/rajāʾ/shurūʿ, the 20 jarr letters, the 24-row sarf table |
| `izzi-sarf-grafikleri.txt` | 48 infographic pages on al-ʿIzzī fī al-taṣrīf: the verb's divisions, the six bābs, the mazīd wazns, majhūl/amr formation as numbered steps, the iftiʿāl ibdāl, nūn al-tawkīd by person (اِذْهَبْنَانِّ, لَا تَخْشَوُنَّ), the three idghām rulings (wājib / jāʾiz لَمْ يَمْدُدْ ~ يَمُدَّ / mumtaniʿ مَدَدْتُ), the weak classes |
| `izhar-al-asrar-matn-lithograph.txt` | **the Arabic matn of Birgivī's Iẓhār al-Asrār**, transcribed page by page (printed ٨٤–١٦٠ of an Ottoman majmūʿa lithograph, 77 scanned pages at 160 dpi) from the large framed text; the ḥāshiya in the margins is left untranscribed. This is the first clean, continuous Arabic Iẓhār on the shelf: `izhar-full-corrected.txt` carries the matn only inside Ottoman commentary, and `izhar-tercume-full.txt`'s inline Arabic is RTL-garbled. Spellings as printed (ثلثة، الصلوة) |
| `nahiv-kafiye-ozeti-turkce.txt` | a 14-page Turkish Kâfiye summary keyed to the printed matn by (sahife, satır): the nine ghayr-munṣarif causes each with its condition, the four-and-four precedence rules, tanāzuʿ, the mafʿūl muṭlaq's seven qiyāsī ʿāmil-deletions, the mustathnā's four wājib-naṣb seats, the five pronoun sets, the الذي-khabar conditions, maʿrifa's six ranks, the ʿamal conditions of the derived nouns, the hidden-أن and hidden-إن seats, inna's kasra/fatḥa seats, tanwīn's five kinds |
| `qisas-al-nabiyyin-nadwi-leveling-notes.txt` | Nadwī's «قصص النبيين للأطفال» vols. 1–2 (Karachi scans, in copyright): NOT transcribed — the author's prefaces paraphrased (delight, clarity, ease, nothing false; pupils made to retell, recite and recall) and two short measured specimens of the opening pages as calibration points for Qissa's own level ramp. Nothing from it may ship as content |

What the Iẓhār matn settles: Birgivī's own words for the three bābs the
whole Ottoman nahw curriculum hangs on — the ʿāmil (sixty: the twenty jarr
letters, the eight inna-sisters, مَا and لَا, the four nawāṣib, the five jawāzim …
the nine qiyāsī and the two maʿnawī), the maʿmūl (thirty: nine marfūʿ, thirteen
manṣūb, two majrūr, one majzūm, five tawābiʿ), and the iʿrāb (ten signs in four
cross-cutting divisions: by essence, by seat, by kind, by quality lafẓī /
taqdīrī / maḥallī, with the seven taqdīrī seats and the two maḥallī seats
enumerated, then the mabnī with its wājib and jāʾiz lists). Every «sixty / thirty
/ ten» count the Avâmil lecture and the AVAMIL100 panel use is now backed by the
received text rather than by a Turkish table.

The Avâmil lecture is the wave-26 tutoring reference: its «İ'rab Mağazası»
(the shop where a word comes in as a customer, the ʿāmil fits it with a body,
the maʿmūl seat is its figure, the sign is the garment) is exactly the per-
sentence card the engines can fill from their own verdicts, which is why it
became the IrabShop tutor rather than a note. The İzzî graphics are the sarf
engine reference for the same wave: its nūn al-tawkīd and idghām rules are
stated as decision tables, which is the shape an engine wants.

**`tasrif-al-izzi-src.txt`** (wave 165) — the matn of al-Zanjānī's «تَصْرِيفُ الْعِزِّيِّ» (d. 655 AH), read from the
page images of the owner's two scans (pp. 49–102 of the print): the classical matn only — nothing of the modern
editor's introduction, headings or footnotes, and neither the copyist's colophon nor the poem after it. The
vowelling, the punctuation and the division into nineteen chapters are ours; «يَعْتَلُّ» is read active where the
print vowels the passive. It is the source of `content/samples/tasrif-al-izzi` (see `tools/authoring/izzi/`).

**`shudhur-al-dhahab-src.txt`** (wave 166) — the matn of Ibn Hishām al-Anṣārī's «شُذُورُ الذَّهَبِ فِي مَعْرِفَةِ كَلَامِ
الْعَرَبِ» (d. 761 AH), part one, read from the page images of the owner's scan of the author's own SHARḤ (pp. 31–93
of the print): only the passages the author opens with «قُلْتُ» — the matn — without that word; nothing of his
sharḥ («وَأَقُولُ …»), and nothing of the modern editor's preface, biographies, headings or footnotes. The vowelling,
the punctuation, the «…» around examples and āyāt, and the division into seven chapters are ours. Two readings the
matn's own argument needs are kept as printed: «تُحَاجُّونِي» with one nūn (p. 90) and «مَنْ يَتَّقِي» with its yāʾ
(p. 92). The scan ends inside «بَابُ الْبِنَاءِ» (p. 99), so that chapter is not in the file. It is the source of
`content/samples/shudhur-al-dhahab` (see `tools/authoring/shudhur/`).

**Part two** (2026-11-18, appended to the same file under its own header) — printed pp. 100–375 of the same edition,
from the owner's three further scans (image-only PDFs): bābs 8–50, from البناء through the marfūʿāt, the manṣūbāt, the
majrūrāt and the jawāzim to عمل الفعل. Matn only, as above, but here the harakāt are ONLY those the page prints (many
particles stand bare) — nothing was vowelled from memory; `[?…]` marks the three words not read with certainty, and every
āya carries a `# VERSE-CHECK` line naming where its reference came from (eight have none in the edition). Pages 94–99
are in the first scan and not yet transcribed. **`shudhur-al-dhahab-qawaid.jsonl`** is NOT matn: 210 rules a learner must
know, one per line, drawn from the author's sharḥ on those pages (`bab`, `page`, `rule_ar` — quoted only where read with
certainty, else a close paraphrase — `rule_en`, `rule_tr` in the madrasa register, the page's own examples with the
transcriber's full vowelling, and an `engine_hint`). It is the input of the engine triage and of new grammar notes; a
rule enters the app only through a note or an engine rule with its own smoke check.

**`siyar-abi-hanifa-src.txt`** (2026-11-19) — six passages of al-Dhahabī's entry on Imam Abū Ḥanīfa al-Nuʿmān ibn Thābit
(no. 163) in «سير أعلام النبلاء» by Shams al-Dīn Muḥammad ibn Aḥmad al-Dhahabī (d. 748 AH), in the edition al-Maktaba
al-Shāmila names «ط الرسالة» (Muʾassasat al-Risāla), book 10906, vol. 6, printed pp. 390, 391, 394, 395, 399, 401, 403.
Fetched 2026-11-19 from https://shamela.ws/book/10906/4640, /4641, /4644, /4645, /4649, /4651 and /4653 (the running
page of the site, not the printed page; the entry runs /4640–/4653). One block per Shamela page, each holding only the
contiguous span the package uses, copied exactly as the page gives it — the edition's own partial vowelling, its
spelling and punctuation, nothing normalised or corrected; the editor's footnotes are not copied. It is the source of
`content/samples/siyar-abi-hanifa` (see `tools/authoring/author_siyar_abi_hanifa.py`, whose manifest attribution lists
the two vowelling layers and everything left out between the spans).

**`muallaqat-zuhayr-src.txt`** (2026-11-19) — the Shamela pages behind `content/samples/muallaqat-zuhayr`, the Muʿallaqa
of Zuhayr ibn Abī Sulmā given WHOLE (all 62 verses of al-Zawzanī's recension), in three groups. (A) Ibn Qutayba (d. 276
AH), «الشعر والشعراء», the edition al-Maktaba al-Shāmila names «دار الحديث، القاهرة، 1423 هـ», book 23785, the entry
«زهير بن أبى سلمى», vol. 1 p. 144 (§§ 212–213 are the span used as chapter 1): https://shamela.ws/book/23785/137.
(B) al-Zawzanī (d. 486 AH), «شرح المعلقات السبع», the edition Shamela names «دار إحياء التراث العربي، ط 1، 1423 هـ /
2002 م», book 11253, «معلقة زهير», printed pp. 133–152 — the verse text, order and count of the package, with his
commentary on every verse: https://shamela.ws/book/11253/143 through /162. (C) Muḥammad ʿAlī Ṭāhā al-Durra, «فتح الكبير
المتعال إعراب المعلقات العشر الطوال», the edition Shamela names «مكتبة السوادي، جدة، ط 2، 1409 هـ / 1989 م», book 151017,
vol. 2 pp. 271–364 — the iʿrāb of the whole ode (his recension orders and counts the verses differently and has three
verses al-Zawzanī does not), used as a CHECK on every token's line and as the second witness for the verse text:
https://shamela.ws/book/151017/808 through /901. Fetched 2026-11-19; `/book/<id>/<n>` is the site's running page, the
block header gives the printed volume and page. One block per page, the whole page exactly as the site gives it — the
edition's own partial vowelling, its typos and the editors' footnotes untouched; nothing normalised. See
`tools/authoring/author_muallaqat_zuhayr.py`, whose manifest attribution lists the two vowelling layers, the verse
numbers of every chapter and every place where the edition's print was departed from, with its witness.

**`muallaqat-imri-al-qays-src.txt`** (2026-11-19) — the Shamela pages behind `content/samples/muallaqat-imri-al-qays`, the
Muʿallaqa of Imruʾ al-Qays given WHOLE (all 81 verses of al-Zawzanī's recension), in four groups. (A) Ibn Qutayba (d. 276
AH), «الشعر والشعراء», the edition al-Maktaba al-Shāmila names «دار الحديث، القاهرة، 1423 هـ», book 23785, the entry on
Imruʾ al-Qays, vol. 1 pp. 108–112 (p. 109 holds the span used as chapter 1, «فبلغه مقتل أبيه … حتّى يثأر بأبيه»; the
others bear on the khabar and on his similes): https://shamela.ws/book/23785/101, /102, /104, /105. (B) al-Zawzanī (d.
486 AH), «شرح المعلقات السبع», the edition Shamela names «دار إحياء التراث العربي، ط 1، 1423 هـ / 2002 م», book 11253,
«معلقة امرئ القيس», printed pp. 35–78 — the verse text, order and count of the package, with his commentary on every
verse: https://shamela.ws/book/11253/46 through /89. (C) Muḥammad ʿAlī Ṭāhā al-Durra, «فتح الكبير المتعال إعراب المعلقات
العشر الطوال», the edition Shamela names «مكتبة السوادي، جدة، ط 2، 1409 هـ / 1989 م», book 151017, vol. 1 pp. 23–162 —
the iʿrāb of the whole ode (his recension orders and counts the verses differently: 92 verses), used as a CHECK on every
token's line and as a witness for the verse text: https://shamela.ws/book/151017/22 through /161. (D) al-Khaṭīb
al-Tibrīzī (d. 502 AH), «شرح القصائد العشر», the edition Shamela names «إدارة الطباعة المنيرية، 1352 هـ», book 37488,
printed pp. 16–54 — a fully vowelled second witness, cited wherever a slip of the e-text is corrected or a bare vowel
is supplied: https://shamela.ws/book/37488/15 through /53. Fetched 2026-11-19; `/book/<id>/<n>` is the site's running
page, the block header gives the printed volume and page. One block per page, the whole page exactly as the site gives
it — the edition's own partial vowelling, its typos and the editors' footnotes untouched; nothing normalised. See
`tools/authoring/author_muallaqat_imri_al_qays.py`, whose manifest attribution lists the two vowelling layers, the verse
numbers of every chapter, every correction with its witness, and the basis of every figure of balāgha.

**`muhammad-ibn-zayd-wa-al-umawi-src.txt`** and **`muhammad-ibn-zayd-wa-al-umawi-witness.txt`** (2026-11-19) — the ḥikāya
of Muḥammad ibn Zayd al-ʿAlawī, the Dāʿī in Ṭabaristān, and the Umayyad (with the story inside it of Muḥammad ibn Hishām
ibn ʿAbd al-Malik, al-Manṣūr's jewel and Muḥammad ibn Zayd ibn ʿAlī), from «المستجاد من فعلات الأجواد» by al-Muḥassin ibn
ʿAlī al-Tanūkhī (d. 384 AH). EDITION as al-Maktaba al-Shāmila names it: book 768, whose card names NO edition — «الكتاب
مرقم آليا غير موافق للمطبوع», text «نقلا عن موقع الوراق»; the page numbers are Shamela's running pages, not the print's.
Fetched 2026-11-19 from https://shamela.ws/book/768/42 (from «[حكاية] حدث القاضي أبو القاسم علي بن المحسن…») and
https://shamela.ws/book/768/43 (to «…وجاؤوه بكتاب بسلامته»). The `-src` file holds only this ḥikāya, one block per Shamela
page, exactly as the page gives it: UNVOWELLED, its slips untouched («الخاج», «فقال إليه رجل», «أمن أيهم», «بهاذ»,
«للحسنين», «وهذا يعنيه», «وإنه مأخوذ», «محمد بم زيد», the broken «امضيا به معه بعد من المسجد قال له»). The `-witness`
file is the SECOND WITNESS those slips are mended against, and nothing more: the same story in al-Tanūkhī's «الفرج بعد
الشدة», which the text itself cites — ed. ʿAbbūd al-Shāljī, Dār Ṣādir, Beirut 1398/1978, vol. 2, pp. 334–337 (Shamela book
12828, card «ترقيم الكتاب موافق للمطبوع»), https://shamela.ws/book/12828/640–643, whole pages with the site's partial
vowelling untouched. The Qurʾānic phrase in the dialogue (al-Anʿām 124) was checked on Tafsīr al-Jalālayn,
https://shamela.ws/book/12876/1083 («{الله أعلم حيث يجعل رسالاته} بالجمع والإفراد»). It is the source of
`content/samples/muhammad-ibn-zayd-wa-al-umawi` (see `tools/authoring/author_muhammad_ibn_zayd_wa_al_umawi.py`, whose
manifest attribution lists every correction `was → now`, the readings kept against the witness, and the vowels left for
the scholar — the e-text being bare, every vowel in the package is editorial).

**`siyar-ibn-al-mubarak-src.txt`** (2026-11-19) — four passages (six chapter spans) of al-Dhahabī's entry on ʿAbd Allāh ibn
al-Mubārak (no. 112) in «سير أعلام النبلاء» by Shams al-Dīn Muḥammad ibn Aḥmad al-Dhahabī (d. 748 AH), in the edition
al-Maktaba al-Shāmila names «ط الرسالة» (Muʾassasat al-Risāla), book 10906, vol. 8, printed pp. 378, 379, 384, 385, 386, 387.
Fetched 2026-11-19 from https://shamela.ws/book/10906/5504, /5505, /5510, /5511, /5512 and /5513 (the running page of the
site, not the printed page; the entry runs /5504–/5549). One block per Shamela page and chapter, each holding only the
contiguous span the package uses, copied exactly as the page gives it — the edition's own partial vowelling, its spelling,
punctuation and footnote marks, nothing normalised or corrected; the editor's footnotes are not copied. It is the source of
`content/samples/siyar-ibn-al-mubarak` (see `tools/authoring/author_siyar_ibn_al_mubarak.py`, which checks every chapter
against this file letter by letter and whose manifest attribution lists the two vowelling layers, the one correction and
everything left out between the spans). **`siyar-ibn-al-mubarak-witness.txt`** (2026-11-19) holds the witness lines: the
Risāla edition's own 8/381 (https://shamela.ws/book/10906/5507) and Ibn Kathīr, «البداية والنهاية», the edition Shamela
names «ت التركي», book 4445, 13/610–611 (https://shamela.ws/book/4445/8278, /8279) — the witnesses for the one correction
«خُوَارِزْميَّةٌ» → «خُوَارِزْمِيَّةً» and for the kept reading «لَا مُلْكَ هَارُونَ»; and the same passages in «سير أعلام النبلاء»
«ط الحديث» (Dār al-Ḥadīth), book 22669, 7/365, 368, 369 (https://shamela.ws/book/22669/3930, /3933, /3934), which differ
from the Risāla text in one word («يطعمهم» for «وَيُطعِمُهُم»).

**`siyar-al-shaykh-al-mufid-src.txt`** (2026-11-19) — the WHOLE of al-Dhahabī's entry no. 213, «الشيخ المفيد محمد بن محمد بن
النعمان البغدادي», in «سير أعلام النبلاء» by Shams al-Dīn Muḥammad ibn Aḥmad al-Dhahabī (d. 748 AH), in the edition
al-Maktaba al-Shāmila names «ط الرسالة» (Muʾassasat al-Risāla), book 10906, vol. 17, printed pp. 344–345. Fetched 2026-11-19
from https://shamela.ws/book/10906/10755 (17/344, the heading and the body) and https://shamela.ws/book/10906/10756
(17/345, to «يُكْنَى أَبَا عَبْدِ اللهِ.», where entry no. 214 begins) — the running page of the site, not the printed page.
One block per Shamela page, copied exactly as the page gives it — the edition's own partial vowelling, its spelling and
punctuation, the entry number, the star of the heading and the footnote marks, nothing normalised or corrected; the
editor's footnotes themselves are not copied. It is the source of `content/samples/siyar-al-shaykh-al-mufid` (see
`tools/authoring/author_siyar_al_shaykh_al_mufid.py`, whose manifest attribution lists the two vowelling layers; the
package holds the entire entry, in three adjacent spans).

- `muallaqat-antara-src.txt` — (1) Ibn Qutayba, al-Shiʿr wa-l-shuʿarāʾ (Dār al-Ḥadīth, Cairo, 1423 AH), shamela.ws/book/23785/236–238 (1/243–245, § 419); (2) al-Zawzanī, Sharḥ al-Muʿallaqāt al-sabʿ (Dār Iḥyāʾ al-Turāth al-ʿArabī, 1423/2002), shamela.ws/book/11253/268–288 (pp. 245–265); (3) Muḥammad ʿAlī Ṭāhā al-Durra, Fatḥ al-Kabīr al-Mutaʿāl: Iʿrāb al-Muʿallaqāt al-ʿashr al-ṭiwāl (Maktabat al-Sawādī, Jeddah, 2nd ed., 1409/1989), shamela.ws/book/151017/670–803 (2/131–264). Fetched 2026-11-19. One block per Shamela page (158 blocks), verbatim. Used for the package `muallaqat-antara`.
