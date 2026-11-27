# Ibn ʿAqīl on the Alfiyya — coverage (v352-A, 2026-11-27)

Source `research/sources/sharh-ibn-aqil-src.txt` (Shamela 9904, 1,329 pages; the editor Muḥyī al-Dīn ʿAbd al-Ḥamīd's «منحة الجليل» in the notes of vols 1–2, his appendix «تكملة في تصريف الأفعال» kept out). Built by `tools/ledger/aqil_toc.py` → `aqil_ledger.py` → `aqil_alfiyya.py` → `tools/ilal/aqil_cut.py` / `aqil_ilal.py` → `aqil_report.py`.

## The book structured

76 bābs; **1006 verses of the Alfiyya** against the received 1,002 (gap +4 — the e-text gives 1006 verse lines against the Alfiyya's received 1,002 (+4). Where a line of the e-text holds the end of one verse and the start of the next (pp. 708–709, 841, 1106, 1130, 1255) the count follows the lines; the Shamela text's verse lines were not checked against a printed Alfiyya.); 675 commentary units; 361 shawāhid lines (292 numbers of the edition); 1122 examples «نحو …».

## The ledger by bāb

Statuses: **joined** = the same rule in Shudhūr / Qawāʿid / Iẓhār / Kāfiya (inherits its status); **applied** = the book's own example read right by the engines in the page (+ offered: beside another reading; + vowelled: read right once vowelled — v355); **⚠** = the engine misreads the book's example; **open** = no construction the iʿrāb line names, a single word cited, or a ṣarf bāb; **n-a** = not automatable (usage / rarity, a school's view, a dialect, a matter of meaning).

| bāb | verses | entries | joined | applied (offered, vowelled) | ⚠ | open | n-a |
|---|---:|---:|---:|---:|---:|---:|---:|
| مقدمة الناظم | 7 | 0 | 0 | 0 (0, 0) | 0 | 0 | 0 |
| الكلام وما يتألف منه | 7 | 7 | 1 | 0 (0, 0) | 0 | 4 | 2 |
| المعرب والمبني | 37 | 50 | 2 | 32 (1, 5) | 0 | 1 | 15 |
| النكرة والمعرفة | 21 | 17 | 0 | 12 (0, 0) | 0 | 0 | 5 |
| العلم | 10 | 10 | 0 | 4 (0, 1) | 0 | 0 | 6 |
| اسم الإشارة | 6 | 1 | 0 | 0 (0, 0) | 0 | 0 | 1 |
| الموصول | 19 | 23 | 0 | 14 (1, 1) | 0 | 0 | 9 |
| المعرف بأداة التعريف | 7 | 4 | 0 | 0 (0, 0) | 0 | 1 | 3 |
| الابتداء | 30 | 43 | 8 | 21 (2, 7) | 0 | 3 | 11 |
| كان وأخواتها | 15 | 19 | 0 | 10 (1, 4) | 0 | 0 | 9 |
| فصل في ما ولا ولات وإن المشبهات بليس | 6 | 13 | 0 | 6 (1, 4) | 0 | 0 | 7 |
| أفعال المقاربة | 11 | 8 | 0 | 3 (2, 0) | 0 | 1 | 4 |
| إن وأخواتها | 24 | 33 | 2 | 16 (1, 2) | 0 | 0 | 15 |
| لا التي لنفي الجنس | 9 | 23 | 14 | 7 (0, 2) | 0 | 0 | 2 |
| ظن وأخواتها | 16 | 11 | 0 | 6 (0, 0) | 0 | 2 | 3 |
| أعلم وأرى | 5 | 5 | 0 | 3 (0, 1) | 0 | 0 | 2 |
| الفاعل | 17 | 27 | 4 | 15 (0, 0) | 0 | 1 | 7 |
| النائب عن الفاعل | 13 | 18 | 0 | 6 (0, 5) | 0 | 1 | 11 |
| اشتغال العامل عن المعمول | 12 | 16 | 1 | 13 (0, 6) | 0 | 0 | 2 |
| تعدي الفعل ولزومه | 11 | 14 | 2 | 8 (0, 6) | 0 | 0 | 4 |
| التنازع في العمل | 8 | 10 | 0 | 5 (0, 0) | 0 | 0 | 5 |
| المفعول المطلق | 12 | 10 | 1 | 3 (0, 2) | 0 | 1 | 5 |
| المفعول له | 5 | 5 | 0 | 1 (0, 1) | 0 | 0 | 4 |
| المفعول فيه وهو المسمى ظرفا | 8 | 11 | 0 | 6 (1, 4) | 0 | 0 | 5 |
| المفعول معه | 5 | 4 | 1 | 3 (0, 2) | 0 | 0 | 0 |
| الاستثناء | 16 | 19 | 7 | 1 (0, 1) | 0 | 4 | 7 |
| الحال | 24 | 16 | 0 | 9 (1, 5) | 0 | 0 | 7 |
| التمييز | 8 | 9 | 0 | 5 (1, 5) | 0 | 0 | 4 |
| حروف الجر | 21 | 12 | 2 | 2 (0, 0) | 0 | 1 | 7 |
| الإضافة | 35 | 22 | 1 | 7 (0, 0) | 0 | 1 | 13 |
| المضاف الى ياء المتكلم | 4 | 4 | 0 | 3 (0, 0) | 0 | 1 | 0 |
| إعمال المصدر | 4 | 5 | 0 | 3 (0, 0) | 0 | 0 | 2 |
| إعمال اسم الفاعل | 12 | 7 | 1 | 3 (0, 3) | 0 | 0 | 3 |
| أبنية المصادر | 17 | 4 | 0 | 0 (0, 0) | 0 | 4 | 0 |
| أبنية أسماء الفاعلين والمفعولين والصفات المشبهات بها | 10 | 2 | 0 | 0 (0, 0) | 0 | 2 | 0 |
| الصفة المشبهة باسم الفاعل | 7 | 13 | 0 | 2 (1, 2) | 0 | 2 | 9 |
| التعجب | 10 | 9 | 1 | 3 (0, 3) | 0 | 1 | 4 |
| نعم وبئس وما جرى مجراهما | 11 | 8 | 0 | 5 (4, 4) | 0 | 0 | 3 |
| أفعل التفضيل | 10 | 9 | 0 | 4 (0, 4) | 0 | 0 | 5 |
| التوابع النعت | 14 | 12 | 0 | 8 (1, 5) | 0 | 0 | 4 |
| التوكيد | 14 | 9 | 0 | 6 (0, 2) | 0 | 0 | 3 |
| العطف | 6 | 3 | 0 | 1 (0, 0) | 2 | 0 | 0 |
| عطف النسق | 25 | 10 | 2 | 6 (0, 0) | 1 | 0 | 1 |
| البدل | 8 | 2 | 0 | 1 (0, 0) | 1 | 0 | 0 |
| النداء | 18 | 13 | 0 | 8 (0, 1) | 0 | 0 | 5 |
| المنادى المضاف الى ياء المتكلم | 3 | 4 | 0 | 4 (0, 0) | 0 | 0 | 0 |
| أسماء لازمت النداء | 3 | 2 | 0 | 2 (0, 0) | 0 | 0 | 0 |
| الاستغاثة | 3 | 3 | 0 | 3 (0, 1) | 0 | 0 | 0 |
| الندبة | 7 | 2 | 0 | 2 (0, 2) | 0 | 0 | 0 |
| الترخيم | 12 | 10 | 0 | 4 (0, 0) | 0 | 0 | 6 |
| الاختصاص | 2 | 0 | 0 | 0 (0, 0) | 0 | 0 | 0 |
| التحذير والإغراء | 5 | 1 | 0 | 0 (0, 0) | 0 | 0 | 1 |
| أسماء الأفعال والأصوات | 8 | 5 | 0 | 2 (0, 1) | 0 | 0 | 3 |
| نونا التوكيد | 14 | 10 | 0 | 10 (0, 7) | 0 | 0 | 0 |
| ما لا ينصرف | 27 | 12 | 1 | 3 (0, 3) | 0 | 0 | 8 |
| إعراب الفعل | 19 | 20 | 0 | 16 (1, 2) | 0 | 0 | 4 |
| عوامل الجزم | 14 | 12 | 0 | 10 (1, 10) | 0 | 0 | 2 |
| فصل لو | 3 | 3 | 0 | 2 (0, 0) | 0 | 0 | 1 |
| أما ولولا ولوما | 5 | 3 | 0 | 2 (0, 0) | 0 | 0 | 1 |
| الإخبار بالذي والألف واللام | 9 | 5 | 0 | 3 (0, 0) | 0 | 1 | 1 |
| العدد | 20 | 8 | 0 | 3 (0, 0) | 0 | 2 | 3 |
| كم وكأي وكذا | 4 | 3 | 0 | 2 (0, 1) | 0 | 0 | 1 |
| الحكاية | 8 | 8 | 0 | 3 (0, 3) | 0 | 1 | 4 |
| التأنيث | 13 | 2 | 0 | 0 (0, 0) | 0 | 2 | 0 |
| المقصور والممدود | 7 | 3 | 0 | 0 (0, 0) | 0 | 3 | 0 |
| كيفية تثنية المقصور والممدود وجمعهما تصحيحا | 13 | 11 | 0 | 0 (0, 0) | 0 | 11 | 0 |
| جمع التكسير | 42 | 13 | 0 | 0 (0, 0) | 0 | 13 | 0 |
| التصغير | 22 | 10 | 0 | 0 (0, 0) | 0 | 10 | 0 |
| النسب | 26 | 20 | 0 | 0 (0, 0) | 0 | 20 | 0 |
| الوقف | 19 | 12 | 0 | 0 (0, 0) | 0 | 12 | 0 |
| الإمالة | 15 | 4 | 0 | 0 (0, 0) | 0 | 4 | 0 |
| التصريف | 23 | 8 | 0 | 0 (0, 0) | 0 | 8 | 0 |
| فصل في زيادة همزة الوصل | 5 | 3 | 0 | 0 (0, 0) | 0 | 3 | 0 |
| الإبدال | 48 | 32 | 0 | 0 (0, 0) | 0 | 32 | 0 |
| الإدغام | 12 | 7 | 0 | 0 (0, 0) | 0 | 7 | 0 |
| تكملة في تصريف الأفعال | 0 | 0 | 0 | 0 (0, 0) | 0 | 0 | 0 |
| **all** | 1006 | 806 | 51 | 342 (20, 118) | 4 | 160 | 249 |

Joined to: izhar 25, shudhur 18, qawaid 5, kafiya 3. Joins need the same topic and the same example (or ≥ 3 shared content words): Ibn ʿAqīl restates the matns in his own words and examples, so most of his rule sentences stand as his own rows here.

## The Alfiyya on the notes

126 verses joined to 108 grammar notes (`content/rules/alfiyya.json`; the «Elfiye» card: the bayt, its bāb and number, Ibn ʿAqīl's ruling verbatim, our rendering on 23 of them, the rest Arabic-only). «Beyti bul» (Level 4): the ruling → its verse among three of the same bāb.

## Reasons appended to `ilal.json`

35 reasons (Ibn ʿAqīl 30, the editor 5) on 17 topics: alam, asma-afal, fail, ishtighal, istithna, maful-bih, maful-fih, maful-mutlaq, mudmar, muqaraba, naib-fail, nida, sifa-mushabbaha, tajjub, tanazu, tasghir, zawaid. Why the fāʿil is rafʿ and the mafʿūl naṣb: neither Ibn ʿAqīl nor his editor states it (searched: فرقا / للفرق / لأن near الفاعل / المفعول) — still open.

## Engine work order — every ⚠

Each row: the entry, the book's example as printed (unvowelled — the probe reads it as given), what the book rules (the bāb's construction, or the role the sentence names on a word), the engine's line. Per bāb the narrowest gate to try first.

### العطف (2)

Gate: the bāb's construction (`aqil_map.py`: معطوف|عطف)

- A897.1 (p. 3:222, Shamela 897) — «يا غلام يعمرا» — wants «عطف بيان» on يعمرا — engine: فعل مضارع، والفاعل ضمير مستتر جوازا تقديره «هو». — vowelled «يَا غُلَامُ يَعْمَرًا»: اسم، منصوب وعلامه نصبه الفتحه الظاهره. — triage b: يعمرا after a built vocative: «فيتعين أن يكون يعمرا عطف بيان»
- A897.2 (p. 3:222, Shamela 897) — «أنا الضارب الرجل زيد» — wants «عطف بيان» on زيد — engine: اسم، مبتدا، وخبره «الضارب» مقدم. — vowelled «أَنَا الضَّارِبُ الرَّجُلِ زَيْدٍ»: اسم، مجرور وعلامه جره الكسره الظاهره، وخبره «الضارب» مقدم. — triage b: «فيتعين كون زيد عطف بيان»

### عطف النسق (1)

Gate: the noun after a coordinating letter whose case follows a non-adjacent noun

- A903.1 (p. 3:228, Shamela 903) — «الذي يطير فيغضب زيد الذباب» — wants «معطوف» on فيغضب — engine: فعل مضارع، ونائب فاعله «الذباب». — vowelled «الَّذِي يَطِيرُ فَيَغْضَبُ زَيْدٌ الذُّبَابُ»: فعل مضارع، مرفوع وعلامه رفعه الضمه الظاهره، وفاعله «زيد». — triage b: the cut carried «ولو قلت ويغضب»; the fāʾ joins a clause with no return pronoun

### البدل (1)

Gate: a noun right after a definite noun of the same case without a coordinating letter

- A927.1 (p. 3:253, Shamela 927) — «من ذا أسعيد» — wants «بدل» on أسعيد — engine: اسم، مبتدا. — vowelled «مَنْ ذَا أَسَعِيدٌ»: اسم، مرفوع وعلامه رفعه الضمه الظاهره. — triage b: the badal of an interrogative takes the hamza; ذا read as ذو

## The v355 triage of the ⚠ rows

a = the print's artefact (read right once vowelled), b = a real gap (fixed or still ⚠), c = the probe's expectation or the cut was wrong (replaced), d = not decidable from the letters / not an example (now not-automatable or open). Counts: a 48, b 59, c 41, d 41 — now: a→applied-vowelled 48, b→applied 5, b→applied-vowelled 50, b→⚠ 4, c→applied 21, c→applied-vowelled 20, d→not-automatable 37, d→open 4

- A34.1 (المعرب والمبني) d — 
- A124.1 (العلم) d — 
- A127.1 (العلم) c — ʿalam jins takes a ḥāl
- A134.1 (اسم الإشارة) d — 
- A149.1 (الموصول) d — 
- A284.1 (كان وأخواتها) d — 
- A285.1 (كان وأخواتها) c — the editor's note on agreement (not a kāna ruling): the verb after a broken plural takes the feminine — the hidden doer «هي»
- A299.1 (كان وأخواتها) c — «إن يكه» is the forbidden form; the ruling's own allowed example is «لم يك زيد قائما» (same sentence)
- A347.1 (إن وأخواتها) c — the probe cut the ism: «ليت فيها غير البذي» — غيرَ the delayed ism
- A360.1 (إن وأخواتها) c — the probe cut the inna clause: «من يأتني فإنه مكرم»
- A371.1 (إن وأخواتها) c — the ruling is the faṣl pronoun between mubtadaʾ and khabar (the bāb's ism-inna regex is the wrong expectation)
- A382.1 (إن وأخواتها) c — أنْ lightened: the clause its khabar
- A445.1 (ظن وأخواتها) c — after قال the clause is in naṣb (مقول القول = the book's «في موضع نصب على المفعولية»)
- A454.1 (أعلم وأرى) d — 
- A499.1 (النائب عن الفاعل) c — the probe cut into the commentary; the ruling: «خير نائل» before the verb is a mubtadaʾ, the nāʾib hidden
- A504.1 (النائب عن الفاعل) d — 
- A505.1 (النائب عن الفاعل) d — 
- A506.1 (النائب عن الفاعل) c — the passive of iftaʿala / infaʿala hollow
- A507.1 (النائب عن الفاعل) d — 
- A513.1 (النائب عن الفاعل) d — 
- A513.2 (النائب عن الفاعل) d — 
- A517.1 (اشتغال العامل عن المعمول) c — «كنت تقول زيدا ضربت» — the object fronted, not ishtighal (no pronoun): مفعول به
- A523.1 (اشتغال العامل عن المعمول) c — the ruling is rafʿ obligatory (no ishtighal after إذا of surprise): زيد a mubtadaʾ
- A523.2 (اشتغال العامل عن المعمول) c — rafʿ obligatory before a condition word: زيد a mubtadaʾ
- A525.4 (اشتغال العامل عن المعمول) c — rafʿ chosen after أمّا: عمرو a mubtadaʾ
- A526.1 (اشتغال العامل عن المعمول) c — both faces allowed; the rafʿ face: عمرو a mubtadaʾ
- A527.1 (اشتغال العامل عن المعمول) c — rafʿ chosen: زيد a mubtadaʾ
- A529.1 (اشتغال العامل عن المعمول) c — rafʿ obligatory: an ism fiʿl explains no ʿāmil — زيد a mubtadaʾ
- A530.1 (اشتغال العامل عن المعمول) c — rafʿ obligatory: the participle with al- explains no ʿāmil — زيد a mubtadaʾ
- A532.2 (تعدي الفعل ولزومه) c — the intransitive reaches its object by a ḥarf: the jārr–majrūr hangs on the verb (no مفعول به in the line)
- A533.1 (تعدي الفعل ولزومه) c — the intransitive: its doer only — the probe cut into the commentary
- A537.1 (تعدي الفعل ولزومه) c — the intransitive reaches its object by a ḥarf
- A543.1 (تعدي الفعل ولزومه) c — the probe cut «في» from the commentary: «أعطيت زيدا درهما»
- A564.2 (المفعول المطلق) d — a report of usage — rarity («ويقل حذف عامل المصدر …»): the engine reads, it does not decide what is rare
- A573.2 (المفعول له) c — the book's ruling is «ولا يمتنع الجر بالحرف»: «لزهد» is the reason in a jarr phrase, not the manṣūb mafʿūl lahu — the probe asks for the jarr
- A575.1 (المفعول له) d — the editor's note naming a verse by its number («بيت الشاهد … رقم ١٦٤»): no example in the letters
- A577.1 (المفعول له) d — a matter of meaning: «ضربت ابني تأديبه» — the maṣdar annexed to the pronoun is the mafʿūl lahu, or (as the letters equally allow) a badal al-ishtimāl of «ابني»
- A578.2 (المفعول فيه وهو المسمى ظرفا) c — the book: البيت / الدار / الشأم are «ليس… منصوبة على الظرفية وإنما هي منصوبة على التشبيه بالمفعول به» (p. 2:191–192) — the probe asks for the mafʿūl reading and no ẓarf
- A590.1 (المفعول معه) c — the example shows the jarr passing over أل («تخطي العامل لها»), not the mafʿūl maʿah: the probe asks for the jarr
- A593.1 (المفعول معه) c — the book: «فرفع زيد عطفا على المضمر المتصل أولى من نصبه مفعولا معه» — the probe asks for the joined reading
- A619.1 (الاستثناء) d — a list of particles («لم وإن ولن ولما وما»), no sentence for the iʿrāb probe
- A636.1 (الحال) c — «فلا تقول: جاء زيد الراكب» — الراكب cannot be a ḥāl here; the reading left is the naʿt: the probe asks for naʿt and no ḥāl
- A656.1 (الحال) c — the cut took the forbidden order; the sentence's own ruling example is «فتقول زيد أحسن من عمرو ضاحكا»
- A657.2 (الحال) d — a report of usage — rarity («وقد ندر تقديمها»): the engine reads, it does not decide what is rare
- A659.1 (الحال) d — a forbidden form — the book's own «فلا تقول / يمتنع»: the example is ungrammatical by the ruling it illustrates, so there is no reading for the engine to assert
- A662.2 (الحال) d — a forbidden form — the book's own «فلا تقول / يمتنع»: the example is ungrammatical by the ruling it illustrates, so there is no reading for the engine to assert
- A725.1 (الإضافة) d — a forbidden form — the book's own «فلا تقول / يمتنع»: the example is ungrammatical by the ruling it illustrates, so there is no reading for the engine to assert
- A726.1 (الإضافة) d — a forbidden form — the book's own «فلا تقول / يمتنع»: the example is ungrammatical by the ruling it illustrates, so there is no reading for the engine to assert
- A729.1 (الإضافة) c — the cut «تسفهت الرياح» is Ibn ʿAqīl's paraphrase with the muḍāf dropped («لصحة الاستغناء عن المر بالرياح»): الرياح is the doer — the probe asks for it
- A794.1 (إعمال اسم الفاعل) c — the cut is a list of forms; the sentence's own example of their working is «هذان الضاربان زيدا وهؤلاء القاتلون بكرا»
- A796.1 (إعمال اسم الفاعل) c — the cut stopped before «وضارب زيدا»: the example is both faces, the naṣb one names the participle's object
- A818.1 (الصفة المشبهة باسم الفاعل) d — a fragment: the ṣifa listed without its mawṣūf and the maʿmūl's case left open by the listing (rafʿ / naṣb / jarr, «ست وثلاثون صورة») — no sentence the letters decide
- A819.1 (الصفة المشبهة باسم الفاعل) d — a forbidden form — the book's own «فلا تقول / يمتنع»: the example is ungrammatical by the ruling it illustrates, so there is no reading for the engine to assert
- A821.1 (الصفة المشبهة باسم الفاعل) c — the cut took the forbidden «زيد الوجه حسن»; the sentence's ruling example is «نحو زيد حسن وجهه» — وجهه the ṣifa's doer
- A822.1 (الصفة المشبهة باسم الفاعل) d — a single word cited («حسن»): the ruling is on its form, no sentence for the iʿrāb probe
- A822.2 (الصفة المشبهة باسم الفاعل) d — a fragment: the ṣifa listed without its mawṣūf and the maʿmūl's case left open by the listing (rafʿ / naṣb / jarr, «ست وثلاثون صورة») — no sentence the letters decide
- A823.1 (الصفة المشبهة باسم الفاعل) d — a fragment: the ṣifa listed without its mawṣūf and the maʿmūl's case left open by the listing (rafʿ / naṣb / jarr, «ست وثلاثون صورة») — no sentence the letters decide
- A823.2 (الصفة المشبهة باسم الفاعل) d — the cut is the commentary's gloss on the verse («الحسن ودون أل»), a single word cited — no sentence
- A823.3 (الصفة المشبهة باسم الفاعل) d — a forbidden form — the book's own «فلا تقول / يمتنع»: the example is ungrammatical by the ruling it illustrates, so there is no reading for the engine to assert
- A823.4 (الصفة المشبهة باسم الفاعل) d — a forbidden form — the book's own «فلا تقول / يمتنع»: the example is ungrammatical by the ruling it illustrates, so there is no reading for the engine to assert
- A824.1 (الصفة المشبهة باسم الفاعل) d — a forbidden form — the book's own «فلا تقول / يمتنع»: the example is ungrammatical by the ruling it illustrates, so there is no reading for the engine to assert
- A824.2 (الصفة المشبهة باسم الفاعل) d — a forbidden form — the book's own «فلا تقول / يمتنع»: the example is ungrammatical by the ruling it illustrates, so there is no reading for the engine to assert
- A831.1 (التعجب) d — a list of verbs cited for their form («دحرج وانطلق واستخرج»), no sentence of wonder
- A831.3 (التعجب) d — a forbidden form — the book's own «فلا تقول / يمتنع»: the example is ungrammatical by the ruling it illustrates, so there is no reading for the engine to assert
- A831.4 (التعجب) c — the example is the passive the verb of wonder may not be built from: the probe asks for its nāʾib
- A848.1 (نعم وبئس وما جرى مجراهما) c — the book: «الرفع بحب نحو حب زيد» — زيد is حَبَّ's doer: the probe asks for فاعل
- A865.1 (التوابع النعت) c — the book names «خبر المبتدأ نحو زيد قائم» (an example of what the definition must exclude): the probe asks for خبر
- A873.1 (التوابع النعت) d — a forbidden form — the book's own «فلا تقول / يمتنع»: the example is ungrammatical by the ruling it illustrates, so there is no reading for the engine to assert
- A896.1 (العطف) c — the book: «كل ما جاز أن يكون عطف بيان، جاز أن يكون بدلا» — بدل on زيدا is the book's own reading
- A961.2 (الترخيم) d — the clipped vocative («يا عثمَ، يا منصُ، يا مسكِ»): that a letter was dropped is not in the letters — «يا مسكِ» is spelt as «يا قومِ» (annexed to the dropped yāʾ)
- A970.1 (التحذير والإغراء) d — «ماز رأسك والسيف»: «مازِ» is the vocative «مازنُ» clipped — not in the letters (the taḥdhīr nouns after it are read)
- A976.1 (أسماء الأفعال والأصوات) d — a sound-word cited («هلا» for the horse): in the letters it is the particle «هلّا» — a homograph the letters do not decide
- A984.2 (نونا التوكيد) c — «هل تغزون» is the form WITHOUT the nūn; the ruling's own form is «هل تغزن» (same sentence)
- A993.1 (ما لا ينصرف) c — the cut is a list of words; the sentence's own example of the diptote is «ومررت بسكران»
- A1008.1 (ما لا ينصرف) d — a hypothetical woman's name («قاض علم امرأة»): that the word is a name is not in the letters
- A1050.1 (عوامل الجزم) c — the oath's answer (not a jazm ruling): the verb with lām and nūn
- A1084.2 (العدد) d — the ruling is on the ordinal's form («ثالث اثنين»); its iʿrāb is plain iḍāfa — no construction the iʿrāb line names
- A1088.1 (العدد) d — the ruling is on the ordinal's form («حادي وتسعون»), a fragment of numerals — no construction the iʿrāb line names
- A1094.1 (الحكاية) d — 
- A1095.3 (الحكاية) d — 
- A1097.1 (الحكاية) c — after a joining wāw no ḥikāya: زيد in rafʿ (mubtadaʾ or khabar)
- A1097.2 (الحكاية) c — only the ʿalam is told as heard: «من غلام زيد» in rafʿ

