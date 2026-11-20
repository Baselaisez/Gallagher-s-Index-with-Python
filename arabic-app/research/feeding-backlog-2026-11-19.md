# The feeding backlog — what the source books still hold that the app does not teach

Written 2026-11-19 against `/home/user/qissa-main/arabic-app` (read-only), reader snapshot of the same day
(`feeding/reader-snap.html`, 63 MB). It replaces the backlog of `research/COVERAGE.md` §2 (stale: its items 1, 2, 3,
5, 7, 8, 10 are closed; see «What COVERAGE §2 still says» at the end).

How every claim here was checked:
- **Engines:** live probes of the snapshot in headless Chromium (`feeding/probe/`, `PP()` = `SentenceAnalyzer.analyze`
  + `CaseEngine.claim` + `Murib.line` per token; `sarfDerive`, `MaqsudEngine.formI`, `IlalEngine.derive/build`,
  `IshtiqaqEngine.family/read` called directly). Every «engine says» below is the output of such a call.
- **Corpus counts:** `feeding/corpus.tsv` — all 80,019 tokens of `content/samples/*/chapters/*.json` (story, chapter,
  sentence, surface, lex, pos, the token's `grammar` note ids, the authored iʿrāb line). Counts marked «authored lines»
  are lines whose authored iʿrāb names the construction (an upper bound on what an engine rule would touch).
- **Notes:** `feeding/notes_index.txt` — all 328 notes in `content/grammar/` with group, example count, anchored
  examples (`sourceStory` set) and `classicalSources`.
- **Atölye audit:** findings already in `research/atolye-audit-2026-11-19.md` are POINTED TO by id (A18, A28, A35, A46,
  A59, B08, B15), never restated.
- Function and class names, not line numbers, for the reader (it is changing under other agents). Line numbers are
  given for the SOURCE files only.

---

## 0. The shelf in one table

| Book (source file) | As text in the app | Notes that cite / anchor it | Engines fed by it | Games / catechism | Verdict |
|---|---|---|---|---|---|
| Taṣrīf al-ʿIzzī (`tasrif-al-izzi-src.txt`, 352 l.) | story `tasrif-al-izzi`, whole matn, 3,591 tokens | cited by 1 note (`mithal-verbs`, by page); **0 notes anchor to the story**; 969 of its 1,105 verb tokens carry no note id | `sarfDerive`, `mazidDerive`, `rubai17Derive`, `Bab35Engine`, `IzziSteps`, `TawkidNunEngine`, `IdghamRuleEngine`, `IshtiqaqEngine`, `LazimEngine` | gSarf, gBab35, gTawkid, gIdgham, gIsht; **no catechism** | ~70 % |
| Marāḥ al-Arwāḥ (`marah-al-arwah-src.txt` 821 l. to p. 144; `marah-al-arwah-matn.txt` raw to p. 182) | story `marah-al-arwah`, ch. 1–76, 7,358 tokens; **pp. 145–182 not in the story** | cited by 13 notes (bare title); **0 anchored**; 1,147 of 1,491 verb tokens carry no note id | `DamirEngine`, `HamzaEngine`, `IlalEngine` (its chain), `sarfDerive` (the permitted iftiʿāl forms, v302), `MaqsudEngine` | gDamir, gKursi, gIsht; **no catechism** | ~55 % |
| al-Maqṣūd (`maqsud-sarf.txt` 1,096 l., `maksut-sarf-ottoman.txt` 1,460 l.) | only `min-muqaddimat-al-maqsud`, 53 tokens | cited by 13 sarf notes (bare title) | `MaqsudEngine` (18 model roots, 1,922 cells) | gMaqsud; lab `maqsud`; **no catechism** | paradigms ~90 %, prose ~20 % |
| Shudhūr al-Dhahab (`shudhur-al-dhahab-src.txt` 305 l. + 210 rules) | story `shudhur-al-dhahab` = part one only (ch. 1–7, 25 sentences / 337 tokens); **part two (bābs 8–50, src l. 65–305) is not a text in the app** | **0 of 328 notes cite it; 0 anchored** | 51 rules DONE in v325–v331, 48 COVERED before, 13 in v332; 68 OPEN, 30 not automatable | none | rules ~55 %, text ~10 % |
| Qawāʿid al-Iʿrāb (`qawaid-al-irab-ibn-hisham-matn.txt` 456 l.; `qawaid-al-irab-turkish.txt` 91 l.) | **no story** | `anwa-al-jumal` cites it (2 examples, neither from the book) | `WujuhEngine` (bāb 3), `TaalluqEngine` (bāb 2), `AdabEngine` (bāb 4); **bāb 1 has no engine** | gWujuh, gAdab | ~50 % |
| Iẓhār al-Asrār (lithograph matn + 4 Turkish/Ottoman files) | story `izhar-al-asrar`, 66 ch., 7,977 tokens | 67 notes | `AmilEngine`, `SignEngine`, `IrabShopEngine`, `TaqdirEngine`, the AVAMIL100 panel | izhar-amil/mamul/irab banks (154); **`izhar-sual-cevap-tafsilatli.txt` (≈187 Q) unbanked and absent from COVERAGE** | ~85 % |
| al-Kāfiya (sual-cevap notebook, digest, özet, Turkish Q&A, Molla Jāmī) | story `al-kafiya`, 8,157 tokens | 47 notes | `TartibEngine`, `MamnuEngine`, `HadhfEngine` seats | kafiya-turkce (58), jami (80) | ~90 % |
| Talkhīṣ al-Miftāḥ (`talkhis-al-miftah-balagha.txt`) | story `talkhis-al-miftah`, 76 ch., 7,525 tokens | 130 notes (balāgha 52, badīʿ 45, bayān 21 …) | the balāgha engines (Tashbih, Istiara, Kinaya, Badi, Jinas …) | badi bank (44), alaka (70), 15 balāgha games | ~95 % |

---

## 1. Book by book, section by section

Legend: **N** = grammar note (id; «own» = the note uses the book's own examples; «anc» = anchored to story tokens) ·
**E** = engine and what it decides · **G** = game / catechism · **A** = Atölye tool · ✓ consumed · ◐ partly · ✗ not.

### 1.1 Taṣrīf al-ʿIzzī (`tasrif-al-izzi-src.txt`)

| Ch. (lines) | Doctrine | N | E | G | A | |
|---|---|---|---|---|---|---|
| 1 (2–10) divisions of the verb | sālim / ghayr sālim | `thulathi-mujarrad-babs` (not own, not anc) | `nakilClass` (type) | — | sarf | ◐ |
| 2 (11–17) six bābs, ḥalq letters, أَبَى شاذّ | `thulathi-mujarrad-babs` | `Bab35Engine`, `sarfDerive` | gBab35 | bab35 | ✓ |
| 3 (18–41) rubāʿī and mazīd | `augmented-babs`, `rubai-babs`, `form-*-verbs` (not own) | `mazidDerive`, `rubai17Derive` | gBab35 | bab35 | ✓ |
| 4 (42–46) lāzim / mutaʿaddī, taʿdiya | `al-lazim-wal-mutaaddi` | `LazimEngine` (T4, v326) | — | — | ✓ |
| 5–8 (47–98) māḍī, majhūl, muḍāriʿ, jazm/naṣb, amr | `imperative-amr`, `al-majhul-fil-kafiya` | `IzziSteps` (majhūl, amr), `sarfDerive` | gSarf | sarf, sledger | ✓ |
| 9 (99–107) two tāʾs; iftiʿāl ibdāl | `form-viii-verbs` | `sarfDerive` ibdāl ✓; **the muḍāriʿ with one tāʾ dropped is read as a māḍī** (F8) | — | — | ◐ |
| 10 (108–121) the two nūns | `nun-tawkid`, `nun-al-tawkid-fil-kafiya` | `TawkidNunEngine` | gTawkid | tawkid | ✓ |
| 11 (122–131) participles; مَمْرُورٌ بِهِ; فَعِيل; equal forms (مُخْتَار) | `ism-fail`, `ism-maful` | `IshtiqaqEngine` (مُخْتَار gets both readings ✓) | gIsht | isht | ✓ |
| 12 (132–154) muḍāʿaf, idghām | `doubled-verbs` (not own) | `IdghamRuleEngine` ✓ for wājib/mumtaniʿ; **the jāʾiz vowels of jazm/amr are not modelled, and the analyzer reads لَمْ يَمُدُّ as marfūʿ** (F4) | gIdgham | — | ◐ |
| 13 (155–177) mithāl | `mithal-verbs` (own, cites p. 148–150) | `sarfDerive` ✓; bāb 5 وَجُهَ refused → **A35** | — | sarf | ◐ |
| 14 (178–214) ajwaf | `hollow-verbs` | `sarfDerive`, `IlalEngine`; مَبِيع's two derivations and Tamīmī مَبْيُوع not shown (L4) | gSarf | ilal | ◐ |
| 15 (215–264) nāqiṣ | `naqis-verbs` | `sarfDerive` ✓ | gSarf | ilal | ✓ |
| 16 (265–286) lafīf | **no note** | `nakilClass` returns null for every lafīf root, so `sarfDerive` refuses; `MaqsudEngine.formI` conjugates only by model key and gets **وَجِيَ wrong** (F2) | — | — | ✗ |
| 17 (287–327) mahmūz | **no note** | `nakilClass` null for every hamzated root; `MaqsudEngine.formI` writes **اُأْمُلْ، اِأْزِرْ، اُأْدُبْ، اِأْوِ** where the book has اُومُلْ، اِيزِرْ، اُودُبْ، اِيوِ (F2); `HamzaEngine` writes the seat ✓ | gKursi (seat only) | hamza | ✗ |
| 18 (328–341) ism zamān / makān | **no note** | `IshtiqaqEngine` mafʿil/mafʿal ✓ (مَوْعِد، مَرْمًى); shādhdh مَسْجِد built as مَسْجَدٌ (**A28**, and the same in `IlalEngine.SHAPES.zaman` and `IshtiqaqEngine.family`); **مَفْعَلَة of abundance absent** (F5) | — | isht, ilal | ◐ |
| 19 (342–352) āla, marra, nawʿ | **no note** | `IshtiqaqEngine` mifʿal/mifʿāl/mifʿala ✓; the shādhdh مُدْهُن… set not read; `MaqsudEngine` marra/nawʿ cells | — | — | ◐ |

### 1.2 Marāḥ al-Arwāḥ (`marah-al-arwah-src.txt`; raw `marah-al-arwah-matn.txt`)

| Ch. (src lines) | N | E | G / A | |
|---|---|---|---|---|
| 1–8 (1–88) the seven things, maṣdar, ishtiqāq, the 35 bābs | `masdar`, `augmented-babs`, `rubai-babs` (title only) | `Bab35Engine`, `IshtiqaqEngine` | gBab35 / bab35 | ✓ |
| 9–17 (89–238) māḍī, the marks, the sixty pronouns | `al-mabni-wal-mudmar` | `DamirEngine` (v285, the Marāḥ's own count) | gDamir / damir | ✓ |
| 18–30 (239–373) muḍāriʿ, amr, the nūns | `nawasib-wa-jawazim-al-mudari`, `imperative-amr`, `nun-tawkid` | `sarfDerive`, `TawkidNunEngine` | gSarf, gTawkid | ✓ |
| 31–32 (374–392) majhūl | `al-majhul-fil-kafiya` | `IzziSteps` | — | ✓ |
| 33–40 (393–465) participles, ṣifa, tafḍīl, faʿīl/faʿūl, mubālagha | `ism-fail`, `sifa-mushabbaha`, `ism-tafdil`, `sighat-mubalagha` (none own, none anc) | `IshtiqaqEngine`, `SifaEngine`, `MubalaghaEngine` | gIsht | ◐ (notes) |
| 41–42 (466–492) zamān/makān, āla | **no note** | as ʿIzzī 18–19; the «أَحَدَ عَشَرَ اسْمًا» of mafʿil (l. 478) not modelled (F5) | — | ◐ |
| 43–46 (493–541) muḍāʿaf, the three meetings of two letters | `doubled-verbs` | `IdghamRuleEngine`; l. 530–531 (مُدَّ / مُدِّ allowed, «فِرُّ» forbidden) not modelled (F4) | gIdgham | ◐ |
| 47–51 (542–592) iftiʿāl assimilations | `form-viii-verbs` | `sarfDerive` (v302 permitted forms) ✓ | — | ✓ |
| 52–62 (593–686) mahmūz, two hamzas, يَرَى, writing the hamza | **no note** for the mahmūz verb | `HamzaEngine` (writing, v307) ✓; conjugation only by model key (F2) | gKursi / hamza | ◐ |
| 63–66 (687–730) mithāl | `mithal-verbs` | `sarfDerive`, `RootFinder` (v308) ✓ | — | ✓ |
| 67–76 (731–821) ajwaf: the sixteen-way table, the conditions of qalb, what is not weakened | `hollow-verbs` (does not carry ch. 70–76) | **`IlalEngine` contradicts ch. 70–76 on 12 of the book's own words** (L1); sarfDerive iʿlāls اسْتَحْوَذَ / أَغْيَلَ (L2); اِجْتَوَرَ → **A46** | — / ilal | ✗ |
| pp. 145–182 (matn l. 417–528): ajwaf conjugation to the end, ishmām, nāqiṣ, the ibdāl letters «اسْتَنْجَدَهُ يَوْمَ صَالَ زَطٌّ», lafīf | none | none for ibdāl as a doctrine | — | ✗ (F7) |

### 1.3 al-Maqṣūd (`maqsud-sarf.txt`, `maksut-sarf-ottoman.txt`)

| Section (lines) | N | E | G / A | |
|---|---|---|---|---|
| Emsile, the ten paradigm blocks, nakil, mazīd rows (≈ 300–460, 840–1096) | form notes | `MaqsudEngine.MODELS` (18 roots) | gMaqsud / maqsud | ✓ |
| Hamza of waṣl/qaṭʿ, vowels of the first letter (194–262) | `imperative-amr` | `sarfDerive` | — | ✓ |
| Meanings of the augmented bābs (≈ 465–560: taʿdiya, mushāraka, ṣayrūra, ṭalab, muṭāwaʿa …) | `augmented-babs` (one meaning per bāb, from sarf-35) | `Bab35Engine.DOORS[].bina` = one meaning | gBab35 | ◐ (F3) |
| The س / ج pairs (l. 71, 102, 297, 346, 1073, 1085 …; Ottoman twin has 13) | — | — | **no bank** | ✗ (F6) |
| `maksut-sarf-ottoman.txt` | — | — | — | not listed in COVERAGE at all |

### 1.4 Shudhūr al-Dhahab (`shudhur-al-dhahab-src.txt`, `shudhur-al-dhahab-qawaid.jsonl`)

Rule status (`feeding/shudhur_rules_status.json`, from the triage's per-rule table + the waves): COVERED 48 · DONE
(T1–T6, I-1/2/3/6/7/10/11/12/15/16/17/19/20/21) 51 · in v332 (I-4/5/8/9/18) 13 · OPEN 68 · not automatable 30.

| Bābs (src lines) | N (none cites Shudhūr; none anchored) | E | Open |
|---|---|---|---|
| 1–7 (2–55) word, speech, iʿrāb, the seven bābs, taqdīrī | `al-kalima-wal-kalam`, `al-murab-wal-mabni-wal-irab`, `mamnu-min-sarf`, `five-nouns`, `jam-*`, `afal-khamsa`, `ism-maqsur-manqus` | `SignEngine`, `IrabSign`, `TaqdirEngine` | — (story part one) |
| 8–14 (65–95) bināʾ on sukūn/fatḥ/kasr/ḍamm, lā's ism, the vocative | `al-mabni-*` (4 notes), `la-nafiya-lil-jins`, `vocative-munada` | `ZarfBinaEngine` (I-12), `NidaEngine`, `AdadEngine` (I-17) | R8, R9, R11, R13, R14, R17, R18, R23, R25/26 (I-23) |
| 15–21 (96–128) nakira, maʿrifa kinds | `al-marifa-*`, `asma-al-ishara*`, `ism-mawsul`, `anwa-al-lam-al-tarif` | `IdafaEngine` (I-15) | R32, R33, R37, R39, R42 (I-14), R43, R47 |
| 22–31 (129–185) marfūʿāt | `fail`, `naib-al-fail`, `mubtada-khabar`, `kana-*`, `afal-al-muqaraba*`, `ma-la-mushabbaha`, `inna-*` | `Murib.doer` (I-2), `MuqarabaEngine` (I-16) | R57, R59, R63, R65/66/68 (I-25), R72, R73, R76, R77/80/81 (I-24), R78/79 (I-13), R83 (I-27), R88 |
| 32–41 (186–242) manṣūbāt | `maful-*`, `hal`, `tamyiz`, `istithna*`, `at-tahdhir`, `ighra-wa-ikhtisas` | `DabtEngine`, `MansubEngine`, I-4/8/9/18 in v332, `IstithnaEngine` (I-21) | R94, R95 (I-23), R96, R97, R106, R107, R110 (I-26), R126 |
| 42–45 (243–266) khabar of kāna/kāda, ism inna/lā, the manṣūb muḍāriʿ | `an-masdariyya`, `nawasib-*`, `innama-kaffa` | `AnEngine` (I-1, I-6) | R136, R137/138 (I-24), R140, R141, R142, R145, R146, R150, R151, R153, R161 |
| 46–48 (267–281) majrūrāt, jarr by jiwār | `huruf-jarr*`, `mahall-al-majrur`; **no note on jarr al-jiwār** | `TaalluqEngine` | R172, R175, R176, R177, R180 |
| 49 (282–295) jawāzim | `al-majzum-wal-shart-wal-jaza`, `in-shartiyya` | `ShartEngine` (I-7) | R191, R192, R194 (I-22), R197, R199 |
| 50 (296–305) ʿamal al-fiʿl | `al-mutaaddi-wa-afal-al-qulub*`, `mafulayn` | `DabtEngine` valency | R205, R208, R209, R210 |

### 1.5 Qawāʿid al-Iʿrāb (`qawaid-al-irab-ibn-hisham-matn.txt`)

| Bāb (lines) | N | E | G / A | |
|---|---|---|---|---|
| 1, the sentence and its rulings (25–170): the two kinds, the seven clauses WITH a maḥall (khabar, ḥāl, mafʿūl/maqūl, muḍāf ilayh, jawāb of a jāzim with fāʾ/إذا, naʿt, follower of such a clause) and the seven WITHOUT (ibtidāʾiyya, ṣila, muʿtariḍa, tafsīriyya, jawāb al-qasam, jawāb of a non-jāzim, follower) | `anwa-al-jumal` (2 examples, **neither the book's**, 1 anc), `mawadi-irab-al-jumla`, `jumla-mutarida`, `jumla-sifa`, `al-hal-jumla-wa-rabituha` | **none decides a clause's maḥall**: `Murib.line` names only the ṣila («… صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا») and «وَالْجُمْلَةُ جَوَابُ الشَّرْطِ» (no maḥall) (R1) | — / jumla (header: **B15**) | ✗ |
| 2, the jārr-majrūr and ẓarf (not in this edition) | `zarf-mustaqarr-wa-laghw`, `mahall-al-majrur` | `TaalluqEngine` (v328) | — | ✓ |
| 3, the words the muʿrib needs (173–456: إذ، لمّا، نعم، إي، حتى، كلا، لا، إن، أن، لو، قد، الواو، ما) | `anwa-ma`, `anwa-al-waw`, `qad-harf`, `in-shartiyya`, `idha-shartiyya` | `WujuhEngine.WORDS` holds all of them; its 40 SEEDS predate the matn (arrived 2026-11-17) and are the common school stock — of the non-Qurʾānic ones only «مَا إِنْ زَيْدٌ قَائِمٌ» and the بَيْنَمَا frame match the matn's wording | gWujuh / wujuh | ◐ (R4) |
| 4 (not in this edition) | — | `AdabEngine` | gAdab / adab | ✓ |

### 1.6 Iẓhār, Kāfiya, Talkhīṣ — short form

- **Iẓhār.** Matn whole as a story; ʿāmil/maʿmūl/iʿrāb in notes, engines and three banks. Not consumed:
  `izhar-sual-cevap-tafsilatli.txt` (≈187 numbered Turkish Q&A; Arabic mojibake — re-dress from the story's chapters)
  — it is not even a row of COVERAGE; `izhar-full-corrected.txt`'s teacher margins (verification of
  `izhar-tercume-full.txt`'s RTL-garbled Arabic, COVERAGE row 11/13).
- **Kāfiya.** Matn whole; two banks; order rules in `TartibEngine`. Not consumed: the digest's poetic-licence diptote
  exceptions (`kafiya-internet-digest.txt`, COVERAGE row 30).
- **Talkhīṣ.** Consumed to the khātima (76 chapters, 130 notes, the badīʿ bank). Nothing to feed.
  `alaqat-al-majaz-balagha.txt` is unrecoverable binary.

---

## 2. The backlog

Rank order: **taṣrīf → iʿlāl → iʿrāb → the rest**; inside each tier, by corpus tokens touched. Each entry: source,
destination(s), size, tokens.

### Tier 1 — TAṢRĪF

#### F1 · The ṣarf books' own verbs carry no ṣarf note — STORY ANALYSIS + GRAMMAR NOTE · M · 2,116 tokens
- **Source:** the whole of ʿIzzī ch. 5–17 (l. 47–327) and Marāḥ ch. 9–76 — every recited paradigm cell.
- **Finding:** in `tasrif-al-izzi` 969 of 1,105 verb tokens have an empty `grammar` list, and the whole story links a
  ṣarf note 6 times; in `marah-al-arwah` 1,147 of 1,491 verb tokens are unlinked, 21 ṣarf links. The tokens point
  only at nahw notes (`huruf-jarr` 646 / 1,943, `idafa-definiteness` 579 / 1,716). No ṣarf note has an example
  anchored to either story (`notes_index.txt`: `hollow-verbs` anchors wasiyya/yunus; `doubled-verbs` 1 anchor, aqaid).
- **Destination:**
  - STORY ANALYSIS: in the `cellLines` builder (`tools/authoring/cell_lines.py`), a recited cell gets the note of its
    class — `hollow-verbs` (صَانَ…صُنَّا, l. 184–206), `naqis-verbs` (غَزَا…, l. 223–264), `doubled-verbs` (l. 140–154),
    `mithal-verbs` (l. 162–177), `nun-tawkid` (l. 117–120, 196–203), `imperative-amr` (l. 93–96), `al-majhul-fil-kafiya`
    (l. 55–58, 186–187). Gate on `cellLines`, as the builder's other rules.
  - GRAMMAR NOTE: each of those notes gets the book's own model row as an example with `sourceStory`
    `tasrif-al-izzi` / `marah-al-arwah` and the page in `classicalSources` (the ʿIzzī pages are in the src headers).
- **Check:** after rebuild, `tasrif-al-izzi` verb tokens with a ṣarf note ≥ 900; every ṣarf note ≥ 1 ʿIzzī anchor.

#### F2 · Hamzated and doubly-weak verbs are conjugated only by model key — ENGINE RULE (EXACT) · L · 2,015 verb tokens
- **Source:** ʿIzzī ch. 16–17, l. 266–327. «وَالْأَمْرُ: اُومُلْ، بِقَلْبِ الْهَمْزَةِ وَاوًا، لِأَنَّ الْهَمْزَتَيْنِ إِذَا الْتَقَتَا فِي كَلِمَةٍ وَاحِدَةٍ
  وَثَانِيَتُهُمَا سَاكِنَةٌ وَجَبَ قَلْبُهَا بِجِنْسِ حَرَكَةِ مَا قَبْلَهَا» (l. 290); «تَعُودُ الثَّانِيَةُ هَمْزَةً عِنْدَ الْوَصْلِ … نَحْوُ: وَأْمُلْ»
  (l. 291); «وَحُذِفَتِ الْهَمْزَةُ فِي خُذْ وَكُلْ وَمُرْ عَلَى غَيْرِ الْقِيَاسِ» (l. 293); اِيزِرْ (296), اُودُبْ (298), سَلْ (301), اِيتِ / تِ
  (306–307), اِيوِ (311), يَرَى / رَ / رَهْ (313–316); «وَجِيَ يَوْجَى كَرَضِيَ يَرْضَى، وَالْأَمْرُ: اِيجَ» (283–284). Marāḥ ch. 52–62
  (l. 593–686) states the same rules with reasons.
- **What the engines do today:** `nakilClass` returns null for any root with a hamza or with two weak radicals, so
  `sarfDerive` (Sarf lab, gSarf) refuses them («Hamzated and doubly-weak roots are beyond letter substitution»).
  `MaqsudEngine.formI` handles the 18 model keys (كُلْ، اِيتِ come out right for اَكَلَ، اَتَى), but on any OTHER root:
  `{root:"أ م ل",cls:"mahmuz-f",bab:1}` → amr **«اُأْمُلْ»**; أ ز ر bāb 2 → **«اِأْزِرْ»**; أ د ب bāb 5 → **«اُأْدُبْ»**;
  أ و ي → **«اِأْوِ»**; ه ن أ → muḍāriʿ **«يَهْنِأُ»** (book يَهْنِئُ, l. 295); و ج ي bāb 4 → **«يَجَى / جَهْ»** (the book keeps
  the wāw in bāb 4: يَوْجَى / اِيجَ).
- **Destination:**
  - ENGINE RULE `sarfDerive` (or a `nakilClass` that admits `mahmuz-f/a/l` and `lafif-*` and routes to the
    generalised `MaqsudEngine.formI`): the two-hamza rule as a rule, not a key; the three irregular amrs and سَلْ / تِ
    as a recited list (like `SOUND_HOLLOW`); لَفِيف مَفْرُوق keeps the wāw in bāb 4 exactly as the mithāl does.
    EXACT. Tests (from the book): أَمَلَ يَأْمُلُ → اُومُلْ and, after a wāw, وَأْمُلْ · أَتَى يَأْتِي → اِيتِ (variant تِ) ·
    وَجِيَ يَوْجَى → اِيجَ. Control: سَأَلَ يَسْأَلُ → اِسْأَلْ (hamza not first: no qalb), variant سَلْ only by the list.
  - GRAMMAR NOTE (new): `mahmuz-verbs` and `lafif-verbs`, each with ʿIzzī ch. 16 / 17 rows anchored to the story.
  - ATÖLYE sarf (accept the roots); GAME gSarf pool (233 lafīf + 1,782 hamzated verb tokens in the corpus become
    derivable).

#### F3 · The meanings of the augmented bābs — ENGINE RULE (SHORTLIST) + NOTE + GAME · M · ≈3,470 tokens
- **Source:** `maqsud-sarf.txt` ≈ l. 465–560 — the Maqṣūd's list of meanings per bāb (Ottoman: «تعديه»,
  «مشاركت ايكى كيشى آراسنده» l. 475–482 for فاعل/تفاعل, «صيرورت» l. 516, «طلب … اِسْتَغْفَرَ» l. 527–528); ʿIzzī l. 46
  (taʿdiya by tadʿīf and hamza).
- **Today:** `Bab35Engine.DOORS[].bina` carries ONE meaning per door; `augmented-babs` lists one per form.
- **Destination:** ENGINE `Bab35Engine` — a ranked list of the bāb's meanings with the signal (the Form I verb is
  lāzim → taʿdiya first for IV/II; two agents → mushāraka for III/VI; a plural agent → VI; X with a noun object →
  ṭalab). SHORTLIST. Tests: أَخْرَجَ (taʿdiya), قَاتَلَ (mushāraka), اِسْتَغْفَرَ (ṭalab). Control: أَكْرَمَ — no Form I
  lāzim in the lexicon to signal from: rule offers the list unranked. NOTE `augmented-babs` (the Maqṣūd's examples).
  GAME gBab35: a «which meaning?» round. Tokens: ṣarf-note links of Forms II–X in the corpus (IV 1,348 · II 692 ·
  VIII 531 · V 349 · III 219 · X 170 · VI 99 · VII 63).

#### F4 · The doubled verb in jazm and amr — ENGINE RULE (EXACT) · M · 858 doubled-verb tokens (26 in jazm/amr)
- **Source:** ʿIzzī l. 146–152: «وَجَائِزٌ إِذَا دَخَلَ الْجَازِمُ … لَمْ يَفِرَّ وَلَمْ يَعَضَّ بِكَسْرِ اللَّامِ وَفَتْحِهَا … وَإِنْ كَانَ الْعَيْنُ مِنَ
  الْمُضَارِعِ مَضْمُومًا فَيَجُوزُ الْحَرَكَاتُ الثَّلَاثُ … لَمْ يَمُدَّ بِحَرَكَاتِ الدَّالِ … فِرَّ وَعَضَّ بِكَسْرِ اللَّامِ وَفَتْحِهَا … مُدَّ بِحَرَكَاتِ
  الدَّالِ وَامْدُدْ». Marāḥ l. 530–531: «… نَحْوُ اُمْدُدْ وَمُدَّ بِفَتْحِ الدَّالِ لِلْخِفَّةِ، وَمُدِّ بِالْكَسْرِ … وَمِنْ ثَمَّ لَا يَجُوزُ فِرُّ».
- **Engines today:** `sarfDerive` gem gives one jussive (يَمُدَّ / يَفِرَّ) with the note «الْجَزْمُ بِالْفَتْحِ، وَيَجُوزُ الْفَكُّ» — no
  kasra for يَفِرّ, no three vowels for يَمُدّ. The analyzer **contradicts** the book: `PP("لَمْ يَمُدُّ")` → يَمُدُّ «مَرْفُوعٌ
  وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ». And the fakk-jussive with the kasra of the two sākins is not recognised:
  `PP("مَنْ يُضْلِلِ اللهُ فَلَا هَادِيَ لَهُ")` → يُضْلِلِ has no cell, so `ShartEngine`'s I-7 line does not fire on مَنْ («اسْمٌ،
  مَبْنِيٌّ لَا يَتَغَيَّرُ آخِرُهُ») although it fires on مَنْ يَعْمَلْ سُوءًا يُجْزَ بِهِ.
- **Destination:** ENGINE `sarfDerive` gem (list the permitted jussive/amr variants by bāb), `IdghamRuleEngine` (the
  jāʾiz ruling names its vowels), `SentenceAnalyzer` (after لَمْ / لَا nāhiya / lām al-amr a doubled muḍāriʿ with any
  final vowel, and the fakk form with a kasra before a sākin, is majzūm: «مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ السُّكُونُ الْمُقَدَّرُ،
  وَحُرِّكَ بِالْفَتْحِ لِلْخِفَّةِ / بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ / بِالضَّمِّ لِلْإِتْبَاعِ»). EXACT. Tests: لَمْ يَمُدُّ · لَمْ يَفِرِّ زَيْدٌ ·
  مَنْ يُضْلِلِ اللهُ فَلَا هَادِيَ لَهُ (fakk + kasra; مَنْ must get I-7's line). Control: «فِرُّ» as an amr must be refused
  (Marāḥ l. 531); يَمُدُّ with no jāzim stays marfūʿ. GAME gIdgham (add the jāʾiz vowel round). NOTE `doubled-verbs`
  (its examples are invented; add ʿIzzī l. 147–152 anchored).

#### F5 · Nouns of place/time, instrument, once and manner — GRAMMAR NOTE + ENGINE RULE · M · ≈60 tokens of the shādhdh set + every mafʿal/mifʿal token
- **Source:** ʿIzzī ch. 18–19, l. 330–352 (incl. «وَشَذَّ الْمَسْجِدُ وَالْمَشْرِقُ وَالْمَغْرِبُ وَالْمَطْلِعُ وَالْمَجْزِرُ وَالْمَرْفِقُ وَالْمَفْرِقُ
  وَالْمَسْكِنُ وَالْمَنْسِكُ وَالْمَسْقِطُ وَالْمَنْبِتُ» l. 332; «وَإِذَا كَثُرَ الشَّيْءُ بِالْمَكَانِ قِيلَ فِيهِ: مَفْعَلَةٌ … مَسْبَعَةٌ وَمَأْسَدَةٌ» l. 341;
  «وَشَذَّ مُدْهُنٌ وَمُسْعُطٌ …» l. 347; marra فَعْلَة / nawʿ فِعْلَة l. 349–352); Marāḥ ch. 41–42, l. 466–492 («وَأُعْطِيَ لِلْمَفْعِلِ
  أَحَدَ عَشَرَ اسْمًا» l. 478; Sībawayh: مُسْعُط is a name, not an instrument, l. 489–492).
- **Today:** there is **no note** for ism al-zamān/makān, ism al-āla, or marra/nawʿ (grep of `content/grammar/`).
  `IshtiqaqEngine.family("س ب ع")` returns nothing (no مَفْعَلَة pattern in `ISHTIQAQ_LAW`). The مَسْجَد error is
  **A28** — but the same wrong form comes out of `IshtiqaqEngine.family("س ج د")` (mafal=مَسْجَدٌ) and
  `IlalEngine.build("س ج د","zaman")` (مَسْجَدٌ), so A28's fix must reach both.
- **Destination:** GRAMMAR NOTE (new) `ism-al-zaman-wal-makan-wal-ala` with the ʿIzzī rows anchored; ENGINE
  `ISHTIQAQ_LAW` pattern `mafala-kathra` (EXACT on the root's noun, SHORTLIST in reading) and the eleven-word shādhdh
  list as a lexical override used by `family`, `SHAPES.zaman` and the Nisba lab. Tests: سَبُع → مَسْبَعَةٌ · سَجَدَ → مَسْجِدٌ
  (and «الْفَتْحُ حُكِيَ»: مَسْجَدٌ as the permitted variant, l. 333) · ذَهَبَ → مَذْهَبٌ. Control: جَلَسَ → مَجْلِسٌ (regular
  mafʿil, no override). Corpus: الْمَغْرِب 13, الْمَسْجِد ≈20, الْمَشْرِق 7, مَسَاكِن 3, مَطْلِع 3 …

#### F6 · No ṣarf catechism exists — CATECHISM · M · gCatechism pool +40
- **Source:** Marāḥ's «فَإِنْ قِيلَ … قُلْنَا» pairs (14 in the src: l. 21, 150, 265, 291, 295 … l. 817–821) and the
  reasoned refusals of ch. 72 and 76 (l. 769–821: each «وَلَا يُعَلُّ نَحْوُ X لِـ / حَتَّى …» is a question «لِمَ لَا يُعَلُّ X؟» with
  the book's answer — ≈20 items); the Maqṣūd's own س / ج pairs (`maqsud-sarf.txt` l. 71, 102, 297, 346, 1073, 1085;
  13 more in `maksut-sarf-ottoman.txt`).
- **Today:** 13 banks, 550 items — all nahw / balāgha. `CatechismEngine` and gCatechism are ready.
- **Destination:** CATECHISM `marah.json` (Arabic Q and A are the matn's own; anchor each to its chapter of
  `marah-al-arwah`), `maqsud.json` (Turkish from the Ottoman, Arabic re-dressed). Area `sarf`.

#### F7 · Marāḥ pp. 145–182 are not in the story — STORY + GRAMMAR NOTE · L
- **Source:** `marah-al-arwah-matn.txt` l. 417–528 ([ص 145]–[ص 182], raw, uncollated): the rest of the ajwaf
  (قُلْنَ / خِفْنَ / بِعْنَ, هَارٍ and شَاكٍ by deletion and by qalb, مَقُول and مَبِيع per Sībawayh and al-Akhfash, the passive
  قِيلَ with its three lughāt and ishmām); the nāqiṣ (156–162); the ibdāl chapter, «حُرُوفُ الْإِبْدَالِ: اسْتَنْجَدَهُ يَوْمَ صَالَ
  زَطٌّ» (163–176); the lafīf (177–182).
- **Destination:** STORY `marah-al-arwah` parts 28+ (collate against the page images first, as for pp. 9–144);
  GRAMMAR NOTE (new) `ibdal` with the book's letter-by-letter list; then F1 and F6 for those chapters.

#### F8 · The muḍāriʿ that dropped one of its two tāʾs — ENGINE RULE (SHORTLIST) · S · few
- **Source:** ʿIzzī l. 100–101: «وَيَجُوزُ حَذْفُ إِحْدَاهُمَا كَمَا فِي التَّنْزِيلِ: فَأَنْتَ لَهُ تَصَدَّى وَفَأَنْذَرْتُكُمْ نَارًا تَلَظَّى وَتَنَزَّلُ الْمَلَائِكَةُ».
- **Engine today:** `PP("فَأَنْتَ لَهُ تَصَدَّى")` → تَصَدَّى «فِعْلٌ مَاضٍ … تَقْدِيرُهُ هُوَ» (after أَنْتَ!); تَلَظَّى likewise a māḍī with
  «هُوَ» after نَارًا (feminine). تَنَزَّلُ is read right (its ḍamma decides).
- **Destination:** ENGINE `SentenceAnalyzer`: a تَفَعَّلَ / تَفَاعَلَ / تَفَعْلَلَ shape whose subject is 2nd person or a
  feminine noun cannot be a 3ms māḍī → offer «فِعْلٌ مُضَارِعٌ حُذِفَتْ إِحْدَى تَاءَيْهِ، أَصْلُهُ تَتَصَدَّى» first. SHORTLIST.
  Tests: the three āyāt. Control: الرَّجُلُ تَصَدَّى لَهُ (masc. subject: māḍī stays).

#### F9 · وَأْمُرْ — the hamza that comes back after wāw / fāʾ — ENGINE RULE (EXACT) · S · 11 tokens
- **Source:** ʿIzzī l. 291 «نَحْوُ: وَأْمُلْ», l. 294 «وَقَدْ يَجِيءُ مُرْ عَلَى الْأَصْلِ عِنْدَ الْوَصْلِ، كَقَوْلِهِ تَعَالَى: وَأْمُرْ أَهْلَكَ بِالصَّلَاةِ».
- **Engine today:** `PP("وَأْمُرْ أَهْلَكَ بِالصَّلَاةِ")` → وَأْمُرْ «اسْمٌ، مُبْتَدَأٌ», أَهْلَكَ «مُضَافٌ إِلَيْهِ».
- **Destination:** `SentenceAnalyzer`: وَ/فَ + أْ + a hamzated-first root's amr stem = the amr (the wāw/fāʾ is the
  conjunction). EXACT. Tests: وَأْمُرْ أَهْلَكَ بِالصَّلَاةِ · فَأْتِ بِهَا · وَأْتُوا الْبُيُوتَ مِنْ أَبْوَابِهَا. Control: وَأَمَرَ (māḍī). Corpus:
  وَأْتُونِي ×2, فَأْتِ ×2, وَأْمُرْ ×2, فَأْتُوهُنَّ, فَأْتِنَا … (11).

### Tier 2 — IʿLĀL

#### L1 · `IlalEngine` has no conditions on qalb — ENGINE RULE (EXACT) · M · ≈30 direct tokens, and every derived noun read through it
- **Source:** Marāḥ ch. 70, l. 757–763 (Ibn Jinnī's conditions: on a verb or a noun on the verb's measure, a vowel
  that is not accidental, no meaning of disturbance, no two iʿlāls in one word, no ḍamma forced on the weak letter in the
  muḍāriʿ, not kept to show the aṣl); ch. 71 l. 764–768 (by following: دِيَارٌ، قِيَامٌ، سِيَاطٌ); ch. 72 l. 769–783; ch. 74
  l. 792–800 (دَاعِيَةٌ); ch. 76 l. 807–821.
- **Engine today** (`IlalEngine.derive(asl)`, the rule runner under the Ilal lab and `IshtiqaqEngine`):

  | aṣl | engine | book |
  |---|---|---|
  | حَوَكَةٌ، خَوَنَةٌ | حَاكَةٌ، خَانَةٌ | unchanged — the tāʾ takes them off the verb's measure (l. 770) |
  | صَوَرَى | صَارَى | unchanged (l. 770) |
  | حَيَوَانٌ | **حَائَانٌ** | unchanged — the vowels show the disturbance of its meaning (l. 775) |
  | قَوَدٌ | قَادٌ | unchanged «حَتَّى يَدُلَّ عَلَى الْأَصْلِ» (l. 783) |
  | حَيِيَ، طَوَيَ | **حَائَ، طَائَ** | unchanged — two iʿlāls would meet (l. 777–780) |
  | أَدْوُرٌ، أَعْيُنٌ | دُورٌ، عِينٌ (hamza dropped as waṣl) | unchanged — not to be confused with verbs (l. 808) |
  | جَدْوَلٌ | جَدَالٌ | unchanged — the ilḥāq (l. 809) |
  | دَاعِوَةٌ | unchanged | دَاعِيَةٌ (l. 794) |
  | قِوَامٌ، دِوَارٌ، سِوَاطٌ | unchanged | قِيَامٌ، دِيَارٌ، سِيَاطٌ by following (l. 765) |
  | مُيْسِرٌ | مِيْسِرٌ | مُوسِرٌ (l. 785; `sarfDerive` IV is right, the raw runner is not) |

  Already in the audit, not repeated: the mifʿāl (مِقْوَال، مِخْيَاط) → **A18**; اِجْتَوَرَ / اِزْدَوَجَ → **A46**.
  `IshtiqaqEngine.read` returns no reading at all for حَيَوَانٌ، تِبْيَانٌ، قَوَدٌ.
- **Destination:** ENGINE `IlalEngine`: a `blocked()`-style gate before `qalb-alif` (noun not on a verb measure + tāʾ;
  faʿalān; faʿala / faʿal kept for the aṣl; two iʿlāls; afʿul plural; mulḥaq faʿwal), plus the `qalb-waw-kasra` rule
  for fiʿāl after a weakened singular/verb and for fāʿila of a nāqiṣ. EXACT. Tests (all the book's): حَيَوَانٌ stays ·
  طَوَى stays with its wāw · قِوَامٌ → قِيَامٌ. Control: قَوَلَ → قَالَ, دَوَرٌ → دَارٌ, غُيَبَةٌ stays (l. 791). NOTE
  `hollow-verbs` (add ch. 70–76 with the book's words). CATECHISM via F6.

#### L2 · مَا أَقْوَلَهُ، أَغْيَلَتْ، اسْتَحْوَذَ — ENGINE RULE (EXACT, recited set) · S · 1 token + every lab query
- **Source:** Marāḥ l. 821: «وَلَا يُعَلُّ مِثْلُ «مَا أَقْوَلَهُ» وَ «أَغْيَلَتِ الْمَرْأَةُ» وَ «اسْتَحْوَذَ» حَتَّى يَدْلُلْنَ عَلَى الْأَصْلِ».
- **Engine today:** `sarfDerive({rs:ح و ذ}, "X")` → **اِسْتَحَاذَ يَسْتَحِيذُ**; `sarfDerive(غ ي ل, "IV")` → **أَغَالَ**. The tafḍīl
  is already blocked (`IlalEngine.build(…,"tafdil")` → blocked ✓).
- **Destination:** `sarfDerive` — extend the `SOUND_HOLLOW` / `SOUND_HOLLOW_IV` recited sets with X ح و ذ, IV غ ي ل
  (and the ta'ajjub). Tests: اسْتَحْوَذَ عَلَيْهِمُ الشَّيْطَانُ (Sarf lab and analyzer), أَغْيَلَتِ الْمَرْأَةُ, مَا أَقْوَلَهُ. Control:
  اِسْتَقَامَ (regular, must still weaken).

#### L3 · The hollow passive's three lughāt and مَبِيع's two derivations — GRAMMAR NOTE + ENGINE (SHORTLIST) · S
- **Source:** ʿIzzī l. 186–187, 211–213 («وَالْمَحْذُوفُ وَاوُ الْمَفْعُولِ عِنْدَ سِيبَوَيْهِ، وَعَيْنُ الْفِعْلِ عِنْدَ أَبِي الْحَسَنِ
  الْأَخْفَشِ. وَبَنُو تَمِيمٍ يُثْبِتُونَ الْيَاءَ فَيَقُولُونَ: مَبْيُوعٌ»); Marāḥ matn [ص 152–154] (قِيلَ، ishmām, قُولَ).
- **Destination:** NOTE `hollow-verbs` (both chains, the Tamīmī form, the three readings of قِيلَ); `IlalEngine` names the
  deleted letter per school in the step list (two chains, both shown). The missing passive cells themselves are
  **A59** — point there.

#### L4 · The Ilal lab has seven shapes only — ATÖLYE · M
- **Source:** Marāḥ ch. 68, l. 736–742 (the sixteen-way table: four states of the weak letter × four of the letter
  before it, minus one — fifteen cases, each with its example قَوْلٌ، بَيَعَ، خَوِفَ، طَوُلَ …) and ch. 73–75 (each case's
  ruling).
- **Today:** `IlalEngine.SHAPES` = fāʿil, mafʿūl, āla, zamān, tafḍīl, muḍāriʿ, amr — no māḍī, no majhūl, no maṣdar.
- **Destination:** ATÖLYE ilal: add māḍī, majhūl, maṣdar fiʿāl / ifʿāl / istifʿāl, and a view of the fifteen cases
  that highlights the case the typed root falls in. GAME: a «which of the fifteen?» round in gIsht.

### Tier 3 — IʿRĀB

#### R1 · The maḥall of a clause — ENGINE RULE (EXACT + SHORTLIST) · L · 2,427 authored lines
- **Source:** Qawāʿid al-Iʿrāb bāb 1, `qawaid-al-irab-ibn-hisham-matn.txt` l. 44–170: «فِي الْجُمَلِ الَّتِي لَهَا مَحَلٌّ مِنَ
  الْإِعْرَابِ، وَهِيَ سَبْعٌ: إِحْدَاهَا الْوَاقِعَةُ خَبَرًا وَمَوْضِعُهَا رَفْعٌ …» (l. 47–49); the maqūl (l. 53); muḍāf ilayh after
  إِذْ، إِذَا، حَيْثُ، لَمَّا (l. 59); jawāb of a jāzim with fāʾ or إذا (l. 61–65); the seven without a maḥall (l. 96–170).
  `qawaid-al-irab-turkish.txt` bāb 1.
- **Engine today:** `Murib.line` names the ṣila («وَجُمْلَةُ … صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا») and «وَالْجُمْلَةُ جَوَابُ الشَّرْطِ»
  (no maḥall) — nothing else. Probes: `زَيْدٌ قَامَ أَبُوهُ` — no «وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ» (and a hidden doer beside
  أَبُوهُ = **B08**); `مَرَرْتُ بِرَجُلٍ يَقُومُ أَبُوهُ` — no «فِي مَحَلِّ جَرٍّ نَعْتٌ»; `مَنْ يُضْلِلِ اللهُ فَلَا هَادِيَ لَهُ` — no «فِي مَحَلِّ
  جَزْمٍ», and هَادِيَ «اسْمٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ» (it is lā's ism, built on the fatḥa).
- **Corpus:** authored lines that name a clause's maḥall: khabar 547 · naʿt/ṣifa 252 · ḥāl 190 · muḍāf ilayh 184 ·
  ṣila 146 · jawāb without maḥall 63 · jawāb in jazm 50 · muʿtariḍa 29 · maqūl 20 · jawāb al-qasam 9 (2,427 in all).
- **Destination:** ENGINE (a clause-line step in `Murib`, fed by the clause spans the analyzer already builds):
  EXACT for khabar (a verb clause straight after a mubtadaʾ with a resumptive pronoun), ṣifa (after an indefinite),
  muḍāf ilayh (after إِذْ/إِذَا/حَيْثُ/لَمَّا), maqūl (after قَالَ), jawāb with fāʾ/إِذَا after a jāzim; SHORTLIST ḥāl / naʿt /
  istiʾnāf with the signal. Tests (the matn's own): زَيْدٌ قَامَ أَبُوهُ · قَالَ إِنِّي عَبْدُ اللهِ · مَنْ يُضْلِلِ اللهُ فَلَا هَادِيَ لَهُ.
  Control: جَاءَ الَّذِي قَامَ أَبُوهُ (ṣila — today right, must stay). GRAMMAR NOTE `anwa-al-jumal` (2 invented
  examples → the matn's fourteen, anchored); ATÖLYE jumla (the header row, cf. **B15**); GAME gTahlil (a «what seat
  is this clause in?» question per tahlil sentence).

#### R2 · Shudhūr's rules never reach the notes — GRAMMAR NOTE · M · 0 → 210 examples
- **Source:** `shudhur-al-dhahab-qawaid.jsonl` (210 rules with the page's own examples, each with its `bab` and page).
- **Today:** 0 of 328 notes have Shudhūr in `classicalSources`; 0 note examples are anchored to `shudhur-al-dhahab`.
- **Destination:** extend the notes of §1.4's middle column with the rule's example and a «شذور الذهب (ابن هشام) —
  <bāb>، ص N» line. Priority by bāb size: the manṣūb muḍāriʿ (21 rules → `nawasib-wa-jawazim-al-mudari`,
  `an-masdariyya`), the jawāzim (14 → `al-majzum-wal-shart-wal-jaza`), the mustathnā (13 → `istithna`,
  `al-mustathna-*`), ʿamal al-fiʿl (11 → `al-mutaaddi-wa-afal-al-qulub`, `mafulayn`), nāʾib al-fāʿil (13 →
  `naib-al-fail`), ism inna (8 → `inna-wa-akhawatuha`, `masail-inna-wal-mukhaffafa-fil-kafiya`). New note: **jarr
  al-jiwār** (bāb 48, src l. 278–281 — no note covers it). Anchors come with R3.

#### R3 · Shudhūr part two as a text — STORY · L
- **Source:** `shudhur-al-dhahab-src.txt` l. 65–305 (printed pp. 100–375, bābs 8–50); the gap pp. 94–99 still to
  transcribe from the first scan.
- **Today:** the story is part one: 7 chapters, 25 sentences, 337 tokens (v265).
- **Destination:** STORY `shudhur-al-dhahab` parts 8–50 through `tools/authoring/shudhur/` (VERSE-CHECK lines first —
  eight āyāt have no reference in the edition). It also gives R2's notes their anchors and every OPEN triage rule its
  own test sentence inside the corpus.

#### R4 · Qawāʿid al-Iʿrāb as a text, and `WujuhEngine` re-seeded from it — STORY + ENGINE seeds · M
- **Source:** the matn file, bāb 1 (l. 25–170) and bāb 3 (l. 173–456; إذ l. 180, لمّا l. 195, إي l. 211, حتى, كلا l. 235,
  لا l. 243, إن l. 272, أن l. 286, then «ما» on twelve faces l. 413+).
- **Today:** no story; `WujuhEngine.SEEDS` (40) are the common school stock (إِنْ تَجْتَهِدْ تَنْجَحْ، لَوْ جِئْتَنِي
  لَأَكْرَمْتُكَ …) — the matn arrived on 2026-11-17, after the engine; of the non-Qurʾānic seeds only «مَا إِنْ زَيْدٌ
  قَائِمٌ» matches its wording (the āyāt were not compared: the file writes them in the muṣḥaf's script).
- **Destination:** STORY (the matn as the next Ibn Hishām text; every āya flagged in the file's header must be checked
  against the page first); ENGINE `WujuhEngine.SEEDS` ← the matn's own examples, one per face (EXACT gate: each seed
  must read to its face); GAME gWujuh pool.

#### R5 · The remaining Shudhūr triage — see §3.

#### R6 · The Iẓhār «tafsilatlı» question sheet — CATECHISM · M · ≈150 items
- **Source:** `izhar-sual-cevap-tafsilatli.txt` (1,406 l., 187 numbered entries; Turkish; its Arabic is mojibake).
  Not a row of COVERAGE.
- **Destination:** CATECHISM `izhar-tafsilatli.json`, Turkish Q/A, Arabic re-dressed from the `izhar-al-asrar`
  chapter each answer quotes (the method of v217–v219); drop items that duplicate `izhar-amil/mamul/irab`.

#### R7 · The diptote's poetic licence — ENGINE (SHORTLIST) · S
- **Source:** `kafiya-internet-digest.txt` (COVERAGE row 30: «poetic-license diptote exceptions remain»).
- **Destination:** `MamnuEngine`: a tanwīn on a diptote in a verse line (the muʿallaqāt stories) offered as
  «صُرِفَ لِلضَّرُورَةِ» instead of a contradiction.

### Tier 4 — THE REST

- **X1 · Bedʾ al-Amālī's 72 س/ج pairs** (`emali-qasida-ottoman.txt`, 62 «ج؛» answers) — CATECHISM `amali.json`
  anchored to `bad-al-amali` (586 tokens). M.
- **X2 · Şerhu'l-Muġnî notes** (`serhul-mugni-ders-notlari-kisa-1.txt`, COVERAGE row 36 PARTIAL): the munādā's seven
  rulings → `NidaEngine` / gNida seeds; jamʿ al-qilla → `JamEngine`. S each.
- **X3 · `izhar-full-corrected.txt` vs `izhar-tercume-full.txt`** — the cross-check COVERAGE §«Deferred» names. S.
- **X4 · `maksut-sarf-ottoman.txt`** — add a COVERAGE row; it is the Ottoman twin of `maqsud-sarf.txt` and feeds F3/F6.

---

## 3. The remaining Shudhūr triage, re-ranked

All are iʿrāb (no taṣrīf item remains). Ranked by corpus tokens. «auth.» = authored lines naming the construction
(upper bound); «tri.» = the triage's own count. Hooks and tests are the triage's (`shudhur/engine-triage.md`); each was
failing on 2026-11-19 unless marked.

| # | Item | Rules | Class | Tokens | Destination |
|---:|---|---|---|---|---|
| 1 | **R94** ishtighāl: زَيْدًا ضَرَبْتُهُ | R94 | EXACT | ≤126 auth. («يفسره») | `HadhfEngine` (v201 has ishtighāl's four rulings; the sentence-initial manṣūb + verb on its pronoun still gets no office) |
| 2 | **I-14** مَاذَا / لِمَاذَا | R42 | SHORTLIST | 53 tokens | `SentenceAnalyzer` particles + `MaEngine` |
| 3 | **I-13** Ḥijāzī مَا + bāʾ on its khabar | R78, R79 | EXACT | 49 auth. (tri. 30 missed) | `MaEngine` seat |
| 4 | **R141 / R142** إِنْ mukhaffafa / nāfiya + lām or لَمَّا | R141, R142 | EXACT | 40 auth. «مخففة من الثقيلة» | `SentenceAnalyzer` / `WujuhEngine` face `mukhaffafa` |
| 5 | **I-26** the participle governs its object | R110, R92 | EXACT | 36 auth. | `TaalluqEngine.VERBAL_WAZN` + `DabtEngine` |
| 6 | **R15** ـوَيْهِ names (سِيبَوَيْهِ) | R15 | EXACT | 30 tokens | analyzer pronoun peel |
| 7 | **R96** ikhtiṣāṣ: نَحْنُ الْعَرَبَ | R96 | EXACT | ≤31 auth. | `HadhfEngine` |
| 8 | **R209** taʿlīq | R209 | EXACT | 20 auth. | `DabtEngine.QULUB_VERBS` |
| 9 | **R208** ilghāʾ | R208 | EXACT | 17 auth. | `DabtEngine.QULUB_VERBS` |
| 10 | **I-22** وَإِلَّا / إِلَّا + majzūm | R194, R189 | EXACT | 16 tokens | `ShartEngine` |
| 11 | **R151** إِذَنْ by the verb's mood | R151 | EXACT | 15 auth. | `Murib.term` |
| 12 | **R57** إِذَا السَّمَاءُ انْشَقَّتْ | R57 | EXACT | 8 tri. / 17 auth. | `HadhfEngine` |
| 13 | **I-25** waṣf as mubtadaʾ | R65, R66, R68 | EXACT / SL | 8 auth. | `Murib.khabarOf` |
| 14 | **I-24** لَاتَ، لَا، إِنْ like laysa | R77, R80, R81, R137, R138 | EXACT / SL | ≤5 | analyzer + `Murib.term` |
| 15 | **R146** the light لَكِنِ | R146 | EXACT | 4 tri. | analyzer |
| 16 | **R172** tāʾ al-qasam | R172 | EXACT | 4 tokens | analyzer `JALALA_PRE` |
| 17 | **I-23** munādā with tanwīn; ʿalam + ابن + ʿalam | R25, R95, R26 | EXACT | 2 | `NidaEngine` |
| 18 | **I-27** إِنَّ after حَيْثُ / opening a ṣifa | R83 | EXACT | 0 | `InnaEngine.verdict` |
| — | the rest of the tail, each ≤ 3 corpus hits: R8, R9, R11, R13, R14, R17, R18, R23, R32/R33/R175 (رُبَّ), R37, R39, R43, R47, R59, R63, R72, R73, R76, R88, R97, R106, R107, R126, R136, R140, R145, R150, R153, R161, R176, R177, R180, R191, R192, R197, R199, R205, R210 | | | | the triage's long-tail table, unchanged |

Incidental bugs of the triage to re-verify before any of these: the five verbs' rafʿ «بِحَذْفِ النُّونِ» (26 lines) and
`Murib.line` throwing on بَاقِيَا / فَأَجْمِعُوا.

---

## 4. Per book — how much the app now carries

**Taṣrīf al-ʿIzzī — about 70 %.** The whole matn is a story and the engines it named are built: the six and the
mazīd bābs, the majhūl and amr by its own steps, the two nūns, the idghām rulings, the iftiʿāl assimilations, the
participles. What it still holds: its chapters 16–17 (lafīf, mahmūz) are not derivable for any root but the Maqṣūd's
models, and where they are derived the hamza-first amr is wrong (F2); the doubled verb's permitted jussive vowels
(F4); the noun of place's shādhdh list, the mafʿala of abundance and any note on place/instrument/once nouns (F5);
and the story's 1,105 verbs are taught by no ṣarf note (F1).

**Marāḥ al-Arwāḥ — about 55 %.** Seventy-six chapters (to p. 144) are a story, and it gave the app the sixty
pronouns, the writing of the hamza and the permitted iftiʿāl forms. But the chapters it ends on — the conditions
and exceptions of iʿlāl, 70–76 — are exactly what `IlalEngine` contradicts on twelve of the book's own words (L1, L2);
pp. 145–182 (the rest of the ajwaf, the nāqiṣ, the ibdāl, the lafīf) exist only as raw matn (F7); and its debate form
(«فَإِنْ قِيلَ … قُلْنَا») is the ṣarf catechism the app does not have (F6).

**al-Maqṣūd — paradigms about 90 %, prose about 20 %.** `MaqsudEngine` recites and re-derives its eighteen models
(1,922 cells). Its prose — the meanings of the augmented bābs (F3), its question pairs (F6) — is unused, and the
Arabic of the text is not in the app (53 tokens). The Ottoman twin is not even listed in COVERAGE.

**Shudhūr al-Dhahab — rules about 55 %, text about 10 %.** Of 210 rules, 99 are applied (48 before the triage, 51
by v325–v331), 13 are in v332, 30 are not automatable, 68 are open (§3). As a text the app carries part one only
(337 tokens); part two (bābs 8–50) is transcribed but unread, and no note quotes or anchors the book (R2, R3).

**Qawāʿid al-Iʿrāb — about 50 %.** Bābs 2–4 are engines (`TaalluqEngine`, `WujuhEngine`, `AdabEngine`) built
from the Turkish notes. Bāb 1 — which clause has a maḥall and which does not — has a note with two invented examples
and no engine, though 2,427 authored lines in the corpus state it (R1). The Arabic matn arrived after the engines and
is neither a story nor the source of their seeds (R4).

**Iẓhār al-Asrār — about 85 %.** Matn complete, three banks, the sixty / thirty / ten as engines and a panel. Left:
the 187-item modern-Turkish question sheet (R6) and the cross-check of the two translations (X3).

**al-Kāfiya — about 90 %.** Matn complete as a story, two banks, the order and the diptote engines. Left: the
digest's poetic-licence diptotes (R7).

**Talkhīṣ al-Miftāḥ — about 95 %.** Complete to the khātima; 130 notes, the balāgha engines and games. Nothing to
feed.

---

## 5. The ten to do first

1. **F2 — hamzated and lafīf verbs for any root** (ʿIzzī l. 266–327). Engine rule in `sarfDerive` / `MaqsudEngine.formI`:
   the two-hamza qalb (اُومُلْ، اِيزِرْ، اُودُبْ، اِيوِ), the recited خُذْ / كُلْ / مُرْ / سَلْ / تِ, the lafīf mafrūq that keeps its
   wāw in bāb 4 (وَجِيَ يَوْجَى اِيجَ). Tests: أَمَلَ → اُومُلْ · أَتَى → اِيتِ · وَجِيَ → يَوْجَى / اِيجَ; control سَأَلَ → اِسْأَلْ.
   2,015 verb tokens become derivable. L.
2. **F1 — tag the ʿIzzī's and the Marāḥ's recited cells with their ṣarf notes**, and anchor every ṣarf note to them
   (`cell_lines.py`, gated on `cellLines`). 2,116 verb tokens; today 27 links. M.
3. **F4 — the doubled verb in jazm and amr** (ʿIzzī l. 146–152, Marāḥ l. 530–531). `لَمْ يَمُدُّ` is read as marfūʿ and
   `مَنْ يُضْلِلِ اللهُ` loses its sharṭ line. Tests: لَمْ يَمُدُّ · لَمْ يَفِرِّ زَيْدٌ · مَنْ يُضْلِلِ اللهُ فَلَا هَادِيَ لَهُ; control: amr «فِرُّ»
   refused. M.
4. **F3 — the meanings of the augmented bābs** (`maqsud-sarf.txt` ≈ l. 465–560) as a ranked list in `Bab35Engine`,
   the note and a gBab35 round. Tests أَخْرَجَ / قَاتَلَ / اِسْتَغْفَرَ; control أَكْرَمَ unranked. M.
5. **L1 — the conditions of iʿlāl** (Marāḥ ch. 70–76, l. 757–821) as a gate in `IlalEngine`. Tests حَيَوَانٌ stays ·
   طَوَى stays · قِوَامٌ → قِيَامٌ; control قَوَلَ → قَالَ. M.
6. **L2 — اسْتَحْوَذَ / أَغْيَلَتْ / مَا أَقْوَلَهُ** (Marāḥ l. 821) into the recited sound set of `sarfDerive`. Control
   اِسْتَقَامَ. S.
7. **R1 — the maḥall of a clause** (Qawāʿid bāb 1, l. 44–170) as a `Murib` clause line. 2,427 authored lines. Tests
   زَيْدٌ قَامَ أَبُوهُ · قَالَ إِنِّي عَبْدُ اللهِ · مَنْ يُضْلِلِ اللهُ فَلَا هَادِيَ لَهُ; control جَاءَ الَّذِي قَامَ أَبُوهُ. L.
8. **F5 — the note on nouns of place, time, instrument, once and manner**, with مَفْعَلَة and the eleven shādhdh
   mafʿil (ʿIzzī l. 330–352, Marāḥ l. 466–492); make A28's fix reach `IshtiqaqEngine.family` and `SHAPES.zaman`. M.
9. **F6 — the first ṣarf catechism**: Marāḥ's «فَإِنْ قِيلَ … قُلْنَا» and ch. 72/76 refusals (≈34) + the Maqṣūd's
   س / ج pairs (≈19). M.
10. **R2 — Shudhūr into the notes**: the 210 rules' own examples and page lines into the nahw notes, starting with the
    manṣūb muḍāriʿ (21 rules), the jawāzim (14), the mustathnā (13); plus a new note on jarr al-jiwār. M.

---

## 6. What COVERAGE §2 still says, and what is true now

| COVERAGE §2 item | Now |
|---|---|
| 1 rubāʿī in the engines | closed (v200, `rubai17Derive`, `Bab35Engine`) |
| 2 iʿlāl exception path | partly closed (SOUND_HOLLOW, v179); the general conditions are L1, the Marāḥ list L2 |
| 3 participles' iʿlāl chain | closed (`IshtiqaqEngine` + `IlalEngine` steps) |
| 4 ʿalāqāt al-majāz | closed (alaka bank, gAlaqa, majaz lab) |
| 5 مَا's twelve faces | closed as an engine (`MaEngine`, v283); I-13 and I-14 remain (§3) |
| 6 iʿrāb meta-framework note | closed (`al-irab-wa-taqsimuhu-bil-dhat-wal-mahall`, `taqsim-al-irab-*`) |
| 7 vocative completion | closed (v201 `HadhfEngine` seats, gNida) |
| 8 taʿalluq | closed (v328) |
| 9 ʿilm al-maʿānī | closed (the Talkhīṣ notes) |
| 10 catechism | closed for nahw / balāgha; **open for ṣarf** (F6) and for the tafsilatlı sheet (R6) |
