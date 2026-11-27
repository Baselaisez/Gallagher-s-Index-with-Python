# Engine gaps — the work order from the other resources' ledger (v342-A, 2026-11-27)

Every `open` entry of the aux ledgers (`content/rules/coverage_*.json`, rendered in `research/book-coverage-2026-11-27.aux.md`) that
needs an ENGINE rule, ranked by corpus weight. v342-A did not edit engine code (the two book agents held the engines); each item
below is written to be executed without re-reading the source: the source line, the rule in one sentence, the engine and function,
a probe (input → expected output, the expected wording from the source or from the authored line), and the weight.

**How the weight was measured.** For each gap, every story token whose AUTHORED iʿrāb line states the role (the role named at the
head of the line) was collected from `content/samples/**`; its sentence was run through `SentenceAnalyzer.analyze` + `Murib.line` on
the built page (prototype/reader.html of 2026-11-26) and the engine's line was matched against the role. «authored» = tokens whose
authored line names it; «engine agrees» = of those, the engine names it too; the difference is what the rule would repair.
(Scripts: scratchpad aux342/gapitems*.json + w.js + runw.js; the probes below are also in the ledgers and re-run by the smoke check
«v342 — the other resources' ledger …», where they currently FAIL and are recorded as the ledger's open/noted entries.)

Probe form: `{ s, w, re }` = run `SentenceAnalyzer.analyze(s)`, take the row of word `w`, `Murib.line(rows, i).ar` (harakāt
stripped) must match `re`. Runner: `tools/ledger/aux_probe.js`.

| # | gap | engine · function | authored | engine agrees | to repair |
|---:|---|---|---:|---:|---:|
| 1 | the nāʾib al-fāʿil is read as a mubtadaʾ / left unnamed | `SentenceAnalyzer` role pass → `Murib.line` | 622 | 477 | **145** |
| 2 | أَمْ the ʿāṭifa is named only «حرف لا محل له» | `Murib.term` (reader.html ≈ l. 22611, `r.pk === "atf"`) + the analyzer's particle table | 42 | 0 | **42** |
| 3 | the mafʿūl lahu (a maṣdar of motive in naṣb) left as a bare manṣūb | `Murib.line` / `MansubEngine` | 90 | 53 | **37** |
| 4 | لَا the ʿāṭifa is named «حرف نفي» | `Murib.term` (the «لا» branches before `r.pk === "nafy"`) | 32 | 0 | **32** |
| 5 | the khabar of lā al-jins (a jarr phrase / ẓarf) is not named | `Murib.line` (the jarr row after the genus-lā's ism) / `TaalluqEngine` seat | 17 | 0 | **17** |
| 6 | حَتَّى the ʿāṭifa is named «حرف جر» while its follower is «معطوف» | `Murib.term` (the حتى branch, ≈ l. 22600) | 4 | 0 | **4** |
| 7 | مَا / أَيْنَ (and the other jāzim nouns of the table) as the condition's noun | `Murib.term` / `ShartIsmEngine` | 2 | 0 | **2** |
| 8 | IlalEngine.derive on a TYPED origin: the nāqiṣ plural, the nāqiṣ feminine dual, the mithāl of bāb fataḥa | `IlalEngine.derive` (the gates / `RULES`) | 0 misread (the reader's forms come from `sarfDerive`, which is right); the Iʿlāl lab's free input | — | 6 book derivations |
| 9 | three Ottoman spellings of the Birgivī sheet: a hamzat al-qaṭʿ written as a bare alif with its vowel | `SentenceAnalyzer` input normalisation | 0 | — | 3 book examples |
| 10 | six ʿalāqas of the majāz mursal the bayān notes name are not in `MajazEngine.ALAQA_NAMES` | `MajazEngine.ALAQA_NAMES` / `alaqaDoc` | ≈ 1 | — | 6 names |

## 1. The nāʾib al-fāʿil (145 tokens)

- **Source.** `awamil-birgivi-tables.txt:27` (TABLE 6, the nine marfūʿāt: «نائب فاعل»), `mamul-tablolari-turkce.txt` (the same list).
- **Rule.** The noun that stands in the doer's place after a passive verb — or after a passive participle that governs (اسم المفعول) — is
  «نائب فاعل مرفوع», never a mubtadaʾ; after قِيلَ / يُقَالُ + a jarr pronoun (لَهُ) the single word said is that nāʾib (v339-M keeps the
  clause case as the maqūl nāʾib).
- **Probes** (the authored line is the expected output):
  - `{ s: "وَيُقَالُ لَهُ أَصَمُّ لِشِدَّتِهِ", w: "أصم", re: "نائب فاعل" }` — marah-al-arwah:43:s1:3; engine now: «اسم، مرفوع …، مبتدأ، وهو مضاف».
  - `{ s: "الثَّانِيَةُ الْمَطْلُوبُ بِهَا صِفَةٌ", w: "صفة", re: "نائب فاعل" }` — talkhis-al-miftah:56:s6:4 (the nāʾib of the ism mafʿūl
    «الْمَطْلُوبُ»); engine now: «… مبتدأ …».
  - `{ s: "ثُمَّ قُتِلَ طُومَانَ بَايُ", w: "باي", re: "نائب فاعل" }` — marj-dabiq:5:s2:4 (the second half of a compound name).
- **Weight.** 622 authored, 477 agree, 145 to repair. Re-measure with the same harness after the fix; the ledger entry
  `birgivi-awamil-inventory#inv083` turns «applied» when its probe passes.

## 2. أَمْ the ʿāṭifa (42 tokens)

- **Source.** `awamil-birgivi-tables.txt:44` (TABLE 11, the ten ʿatf letters: «لَكِنْ | بَلْ | لاَ | اَمْ | اِمَّا | اَوْ | حَتَّى | ثُمَّ | فَاء | وَاوْ»).
- **Rule.** أَمْ (and أَمِ before a sākin) after a question — the muttaṣila after the hamza of equalisation / taʿyīn, the munqaṭiʿa
  otherwise — is «حَرْفُ عَطْفٍ» (the muttaṣila «مُعَادِلَةٌ لِلْهَمْزَةِ»); give it `pk: "atf"` in the particle table.
- **Probes.** `{ s: "أَتَمْشِي هٰذِهِ فِي الرَّمْلِ أَمْ تَصْعَدُ الْجَبَلَ", w: "ام", re: "حرف عطف" }` (qisas-al-nabiyyin-2:11:s11:5);
  `{ s: "ءَأَرْبَابٌ مُتَفَرِّقُونَ خَيْرٌ أَمِ اللهُ الْوَاحِدُ الْقَهَّارُ", w: "ام", re: "حرف عطف" }` (qisas-al-nabiyyin-1:13:s28:4). Engine now: «حرف لا محل له».
- **Weight.** 42 authored, 0 agree.

## 3. The mafʿūl lahu (37 tokens)

- **Source.** `mensubat.txt` (the manṣūbāt notebook; its own examples «ضَرَبْتُ زَيْدًا تَأْدِيبًا» and «ضَرَبْتُ زَيْدًا تَأْدِيبًا لَهُ»), TABLE 7 of the
  Birgivī tables («مفعول له»).
- **Rule.** An indefinite maṣdar of the heart's motive, in naṣb after a complete clause, sharing its verb's time and doer, is
  «مَفْعُولٌ لِأَجْلِهِ» — the book's own example passes; the misses are a maṣdar after a verb of saying or a clause ending in a jarr phrase.
- **Probes.** `{ s: "ضَرَبْتُ زَيْدًا تَأْدِيبًا", w: "تاديبا", re: "مفعول لاجله" }` (passes — keep it as the control);
  `{ s: "وَمِنْهُمْ مَنْ يَقُولُ تِ تَشْبِيهًا بِخُذْ", w: "تشبيها", re: "مفعول لاجله" }` (tasrif-al-izzi:17:s18:5; engine now: a bare «اسم، منصوب»);
  `{ s: <muallaqat-al-harith 1:6>, w: "استحسانا", re: "مفعول لاجله" }` (muallaqat-al-harith:1:s6:6).
- **Weight.** 90 authored (role at the head of the line), 53 agree.

## 4. لَا the ʿāṭifa (32 tokens)

- **Source.** TABLE 11 (above): «لاَ».
- **Rule.** لَا after a positive statement or a command, followed by a single word (not a verb, not a clause) that takes the case of a
  word before it, is «حَرْفُ عَطْفٍ» that denies of the second what was affirmed of the first («تَنْفِي عَنِ الْمَعْطُوفِ مَا ثَبَتَ لِلْمَعْطُوفِ
  عَلَيْهِ» — the authored line) — not the genus-lā (no indefinite built on fatḥa) and not the lā of prohibition (no jussive).
- **Probes.** `{ s: "وَالْإِغْرَاقُ مَا أَمْكَنَ عَقْلًا لَا عَادَةً", w: "لا", re: "حرف عطف" }` (talkhis-al-miftah:64:s4:5);
  `{ s: "وَهُوَ شَيْءٌ لَا كَالْأَشْيَاءِ وَمَعْنَى الشَّيْءِ الثَّابِتُ", w: "لا", re: "حرف عطف" }` (al-usul-al-munifa:4:s2:3). Engine now: «حرف نفي».
- **Weight.** 32 authored, 0 agree. Control: the genus-lā of «لَا رَيْبَ فِيهِ» must stay «النافية للجنس».

## 5. The khabar of lā al-jins (17 tokens)

- **Source.** `awamil-birgivi-tables.txt:28` (TABLE 6: «جنسينى نفى ايجون اولان "لا"نك خبرى»).
- **Rule.** After the genus-lā and its ism, the jarr phrase or ẓarf that completes the sentence is «جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ «لَا»»
  (the seat the v-wave TaalluqEngine already names for the mubtadaʾ's khabar; extend it to the genus-lā's khabar).
- **Probe.** `{ s: "لَا رَيْبَ فِيهِ", w: "فيه", re: "خبر «?لا" }` (talkhis-al-miftah:19:s2:3; authored: «جَارٌّ وَمَجْرُورٌ — خَبَرُ «لَا» غَيْرُ مُقَدَّمٍ»). Engine now:
  «حرف لا محل له من الإعراب».
- **Weight.** 17 authored lines name «خبر «لا»».

## 6. حَتَّى the ʿāṭifa (4 tokens)

- **Source.** TABLE 11 (above): «حَتَّى»; the Kāfiya's own example «مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءُ» (al-kafiya 37:s5).
- **Rule.** حَتَّى followed by a noun whose case is the case of a noun before it (not jarr), the noun a part of it (its strongest or
  weakest), is «حَرْفُ عَطْفٍ»; today `Murib.term` says «حرف جر» while the same sentence calls الْأَنْبِيَاءُ «معطوف» — the two lines contradict.
- **Probe.** `{ s: "مَاتَ النَّاسُ حَتَّى الْأَنْبِيَاءُ", w: "حتي", re: "حرف عطف" }`.
- **Weight.** 4 authored.

## 7. The jāzim nouns as the condition's noun (2 tokens; the table's fifteen)

- **Source.** `awamil-birgivi-tables.txt:17–18` (TABLE 3: «مَنْ | مَا | مَهْمَا | اِنْ … اِذَامَا | اِذْمَا | حَيْثُمَا | اَىُّ | اَنَّى | مَتَى | اَيْنَ»).
- **Rule.** مَا / أَيْنَ opening a clause whose verb is jussive (or a māḍī answered by a fāʾ clause) is «اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى …» with its seat.
- **Probes.** `{ s: "مَا أَصَابُوا مِنْ تَغْلَبِيٍّ فَمَطْلُولٌ عَلَيْهِ إِذَا أُصِيبَ الْعَفَاءُ", w: "ما", re: "شرط" }` (muallaqat-al-harith:7:s6:1);
  `{ s: "وَجَعَلَنِي مُبَارَكًا أَيْنَ مَا كُنْتُ", w: "اين", re: "شرط" }` (qisas-al-nabiyyin-4:34:s3:3). Engine now: «اسم، مبني لا يتغير آخره».
- **Weight.** 2 authored here (a short, high-value fix: the Birgivī table's own family).

## 8. IlalEngine.derive on a typed origin (the Iʿlāl lab's free input)

`sarfDerive` gives every form below correctly (غَزَوْا، رَمَوْا، غَزَتَا، رَمَتَا، يَهَبُ) and `IlalEngine.build(root, shape, bab)` gives يَهَبُ;
only `IlalEngine.derive(asl)` — the derivation the lab shows for an origin the learner types — stops short:

| source line | origin → expected (the sheet) | engine now | the missing step |
|---|---|---|---|
| `ilal-kaideleri-turkce.txt:21` | غَزَوُوا → غَزَوْا | غَزَوُوا (no rule fires) | qalb of the wāw to alif after a fatḥa, then «elif-i maklube» dropped for the two sākins (the plural wāw) |
| `ilal-kaideleri-turkce.txt:22` | رَمَيُوا → رَمَوْا | رَمَيُوا | the same with yāʾ |
| `ilal-kaideleri-turkce.txt:23` | غَزَوَتَا → غَزَتَا | غَزَاتَا | the feminine tāʾ is sākin in origin, so the alif dropped for two sākins stays dropped before the dual's alif |
| `ilal-kaideleri-turkce.txt:24` | رَمَيَتَا → رَمَتَا | رَمَاتَا | the same |
| `misal-kaideleri-mesnedli.txt:153–155` (Marāḥ p. 83, ʿIzzī p. 149) | يَوْهِبُ → يَهَبُ | يَهِبُ | `fath-halq` is bound to the lab's verb shapes (`E._lab === "verb"`): a typed يَوْعِلُ-origin of a bāb-3 root whose ʿayn or lām is a throat letter must take it too |

Probes: `{ ilal: "غَزَوُوا", out: "غَزَوْا" }`, `{ ilal: "رَمَيُوا", out: "رَمَوْا" }`, `{ ilal: "غَزَوَتَا", out: "غَزَتَا" }`, `{ ilal: "رَمَيَتَا", out: "رَمَتَا" }`,
`{ ilal: "يَوْهِبُ", out: "يَهَبُ" }`. Shelf shapes these rules describe: 56 nāqiṣ plural māḍīs (رَمَوْا، بَنَوْا، خَلَوْا …), 5 nāqiṣ feminine
duals (رَمَتَا، غَزَتَا …), ≈ 40 bāb-3 mithāl muḍāriʿs (يَدَعُ، يَضَعُ، يَقَعُ …) — read correctly today, derived wrongly only from a typed origin.

## 9. The Ottoman sheet's spelling of hamzat al-qaṭʿ

- **Source.** `awamil-birgivi-ottoman.txt:32, 35` and `awamil-birgivi-tables.txt:13` — «اَعْبُدُ اللهَ تَعاَلَى», «اِحْفَظِ اللهَ تَعاَلَى حَقَّهُ»,
  «اُحِبُّ اَنْ اُطِيعَ اللهَ تَعاَلَى»: the Ottoman print writes the hamza of a first-person verb or of أَنْ as a bare alif with its vowel.
- **Rule.** In `SentenceAnalyzer`'s input pass, a word-initial bare alif carrying fatḥa / ḍamma (never kasra: that is the waṣl of an
  imperative or a VIII–X maṣdar) is read as أَ / أُ for lookup — the surface shown stays as printed.
- **Probes.** `{ s: "اَعْبُدُ اللهَ تَعاَلَى", w: "الله", re: "مفعول به" }` (engine now: «… مضاف إليه» — اَعْبُدُ read as a noun);
  `{ s: "اُحِبُّ اَنْ اُطِيعَ اللهَ تَعاَلَى", w: "اطيع", re: "منصوب" }`; `{ s: "اِحْفَظِ اللهَ تَعاَلَى حَقَّهُ", w: "حقه", re: "بدل" }` (the last also needs
  the badal of an object pronoun-annexed noun).
- **Weight.** 0 story tokens (the shelf is in standard spelling); 3 of the Birgivī sheet's 27 examples. These three now stand verbatim, with
  their line anchors, in the notes `al-maful-bihi-wa-qismah`, `al-badal-wa-aqsamuh-wa-atf-al-bayan` and `an-masdariyya`.

## 10. The ʿalāqas the bayān notes name and MajazEngine does not

- **Source.** `alaka-ilm-bayan.txt` (≡ `alaqat-al-majaz-balagha.txt`, its raw Word dump): the ʿalāqas of the majāz mursal include
  «مصدريه، مظهريه، كون سابق، كون لاحق» and the iṭlāq / taqyīd pair.
- **Rule.** Add to `MajazEngine.ALAQA_NAMES` (and `alaqaDoc`) the keys `masdariyya`, `mazhariyya`, `kawnSabiq` («بِاعْتِبَارِ مَا كَانَ»),
  `kawnLahiq` («بِاعْتِبَارِ مَا يَكُونُ»), `itlaq`, `taqyid`, each with the notes' definition; the authored balāgha lines already use
  «بِاعْتِبَارِ مَا يَكُونُ» once.
- **Probe.** `{ js: "['masdariyya','mazhariyya','kawnSabiq','kawnLahiq','itlaq','taqyid'].every(k=>Object.values(MajazEngine.ALAQA_NAMES).includes(k))" }`.

## Not engine work (recorded so nobody looks for it here)

- The term sheets' 66 unglossed fiqh terms (`buyu-tarifler-turkish.txt` 64, `sulh-fiqh-turkce.txt` 1, `vakif-mali-turkce.txt` 1): they need
  AUTHORING (a story or a glossary entry with the Arabic term), not a rule; listed in the aux coverage file.
- Six slips of the sheets themselves (the engine is right): `bablara-nakil-12-wazn.txt` l. 15 اِتّجّلَ, l. 16 اِنَعَمَّ, l. 17 تَفّتَّحَ, l. 19
  اِسَتْذْهَبَ; `ilal-kaideleri-turkce.txt` l. 45 غَِبوَ; `sifa-mushabbaha-vezinleri.txt` l. 3 وحْهُهُ — «for the hoca», with the engine's form.
