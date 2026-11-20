# Atölye audit — findings

**Build audited:** the released v331 `prototype/reader.html`, as copied to
`/tmp/claude-0/-home-user-Gallagher-s-Index-with-Python/612c64cf-e6b9-547d-9c53-f32b7b6377b6/scratchpad/atolye-audit/reader.html`
before the engine agent's current edits. Nothing in the repo was touched.

**Method.** Every one of the 37 tools was driven in headless Chromium on the copy: the lab was opened, the input set,
the lab's own render function called, and the rendered text read. Every finding below was produced twice in this
session (the first run, then the confirmation scripts `work/rv.js` and `work/rv2.js`), and the book line was opened for
each citation. The earlier agent's working notes were treated as unverified: each candidate was re-run, and those that
did not reproduce are listed at the end.

**Line numbers.** `L…` is the line in the audited v331 copy. The repo file has moved since (the engine agent is
editing it). When this was written the offsets were: below L13933 unchanged · L13933–L19150 **+1** ·
L19150–L19900 **+318** · above L19900 **+321**. Where the repo line differs it is given in square brackets. Function
names are the stable anchor.

**Severity.** WRONG = a form or a line that is false. MISLEADING = states a certainty the letters do not give.
MISSING = silent (or a bare refusal) where the tool's own description promises an answer. A refusal with a true reason
and a labelled shortlist that contains the right answer are not findings.

## Counts

| Group | WRONG | MISLEADING | MISSING | Total |
|---|---|---|---|---|
| A · Taṣrīf and iʿlāl (13 ṣarf tools) | 48 | 7 | 5 | 60 |
| B · Iʿrāb (14 naḥw tools) | 46 | 2 | 6 | 54 |
| C · The rest (balāgha 5, fahm 5) | 7 | 2 | 3 | 12 |
| **All** | **101** | **11** | **14** | **126** |

Two tools came out clean on everything tried: **Numbers** (عَدَد) and **Hamza** (هَمْزَة). Etiquette and Q&A hold book
text and take no grammar input (see «Not auditable»).

---

# A · Taṣrīf and iʿlāl

Ranked by how often a learner would meet the fault.

### A01 · I'lāl lab · WRONG — the muḍāriʿ and the amr are always built on يَفْعِلُ / اُفْعُلْ, whatever the root's bāb
- **Input:** root `قول`, shape `يَفْعِلُ`; root `خوف`, shapes `يَفْعِلُ` and `اُفْعُلْ`; also `نوم`, `صون`, `وجل`, `وضع`, `عور`.
- **Shown:** «ITS ORIGIN يَقْوِلُ → WHAT IS SAID يَقِيلُ»; خوف «يَخْوِفُ → يَخِيفُ», «اُخْوُفْ → خُفْ»; نوم «يَنِيمُ / نُمْ»;
  صون «يَصِينُ»; وجل «يَجِلُ / جِلْ»; وضع «يَوْضِعُ → يَضِعُ», «ضِعْ»; عور «يَعِيرُ / عُرْ».
- **Correct:** يَقُولُ · يَخَافُ / خَفْ · يَنَامُ / نَمْ · يَصُونُ · يَوْجَلُ / اِيجَلْ · يَضَعُ / ضَعْ · يَعْوَرُ / اِعْوَرْ. The lab's intro
  promises «the ORIGIN the books start from»; for قول the books start from يَقْوُلُ, for خوف from يَخْوَفُ.
- **Book:** ʿIzzī `tasrif-al-izzi-src.txt` L168 (يَضَعُ … «فِي الْأَصْلِ يَفْعِلُ بِالْكَسْرِ، فَفُتِحَتِ الْعَيْنُ لِحَرْفِ الْحَلْقِ»),
  L199–L202 (خَفْ خَافَا…). The Sarf lab itself derives all of these rightly.
- **Engine:** `IlalEngine.SHAPES` L8617 (`mudari`, `amr` hard-wired), `IlalEngine.build` L8665; `renderIlalOut` L15194 [15195].

### A02 · Tawkīd nūn lab · WRONG — the hollow imperative keeps its short form before the nūn
- **Input:** `قُلْ`, `بِعْ`, `خَفْ`, `يَنَامُ`, `يُجِيبُ`, `اِسْتَقِمْ` (the first row of each table).
- **Shown:** قُلْ → «قُلَنَّ / قُلَنْ»; بِعْ → «بِعَنَّ»; خَفْ → «خَفَنَّ»; نَمْ → «نَمَنَّ»; أَجِبْ → «أَجِبَنَّ»; اِسْتَقِمْ → «اِسْتَقِمَنَّ».
- **Correct:** قُولَنَّ / قُولَنْ · بِيعَنَّ · خَافَنَّ · نَامَنَّ · أَجِيبَنَّ · اِسْتَقِيمَنَّ (the lām is vowelled again, so the ʿayn returns).
- **Book:** ʿIzzī L201 «وَبِالتَّأْكِيدِ: بِيعَنَّ بِيعَانِّ بِيعُنَّ، بِيعِنَّ بِيعَانِّ بِعْنَانِّ», L202 «وَخَافَنَّ خَافَانِّ خَافُنَّ…»,
  L203 «صُونَنْ وَبِيعَنْ وَخَافَنْ».
- **Engine:** `TawkidNunEngine.table` L26588 [26909] (class L26501 [26822]).

### A03 · Sarf lab · WRONG — the nāqiṣ of bāb فَتَحَ is refused with a false sentence
- **Input:** root `سعي` (also `نهي`, `رعي`, `بهو`). The lab itself snaps to Form I, bāb 3 and marks the verb attested.
- **Shown:** «This class does not recite that bab.»
- **Correct:** سَعَى يَسْعَى اِسْعَ (the paradigm of يَخْشَى with a fatḥa māḍī).
- **Book:** ʿIzzī L312 «وَنَأَى يَنْأَى كَرَعَى يَرْعَى».
- **Engine:** `sarfDerive` L7596, `return no("naqis-bab")` L7661; message `conjNoForm` L3062, `renderConjOut` L14739 [14740].

### A04 · Root Finder · WRONG — a corpus noun crashes the lab and the previous answer stays on screen
- **Input:** type `كَتَبَ`, then `مِيزَان` (also `قَاضٍ`, `دُعَاء`, `قَائِل`, `مُسْتَقِيم`, `مُصْطَفَى`, `فَتًى`, `هُدًى`, `لِلْمُعَلِّمِينَ`).
- **Shown:** the box keeps «الْجَذْر · Root: ك ت ب» for مِيزَان. `TypeError: Cannot read properties of undefined (reading 'tense')`.
  With such a word left in the field, reopening the tab throws inside `renderLabBody`.
- **Correct:** و ز ن (`RootFinder.find` does return `{root:"و ز ن", via:"corpus", lemma:"مِيزَان"}` — but with no `cell`).
- **Book:** — (crash).
- **Engine:** `renderJadhrOut` L14823 [14824], the call `formCellLabel(r.cell)` L14835 [14836]; `formCellLabel` L6810.

### A05 · I'lāl lab · WRONG — the nāqiṣ muḍāriʿ is left unfinished
- **Input:** `دعو`, `رمي`, `خشي`, `سعي`, `نهي`, `وقي`, `سرو`, shape `يَفْعِلُ`.
- **Shown:** دعو «يَدْعِوُ → يَدْعِيُ» (one step); رمي «يَرْمِيُ → يَرْمِيُ» (no rule fired); وقي «يَقِيُ»; سرو «يَسْرِيُ».
- **Correct:** the ḍamma on the weak lām is dropped: يَرْمِي, يَقِي (and يَدْعُو from its own يَفْعُلُ).
- **Book:** ʿIzzī, the nāqiṣ chapter (L226–L255); the Sarf lab's own chain says «اسْتُثْقِلَتِ الضَّمَّةُ عَلَى حَرْفِ الْعِلَّةِ فَحُذِفَتْ».
- **Engine:** `IlalEngine.build` L8665 (rule table of class L8371).

### A06 · Sarf lab · WRONG — the mithāl yāʾī is refused in Form I
- **Input:** root `يسر` (auto-picked I/2), `يبس` (I/4), `يمن`, `يتم`, `ينع`.
- **Shown:** «This class does not recite that bab.»
- **Correct:** يَسَرَ يَيْسِرُ اِيسِرْ; يَبِسَ يَيْبَسُ; يَمُنَ يَيْمُنُ.
- **Book:** ʿIzzī L173 «وَأَمَّا الْيَاءُ فَتَثْبُتُ عَلَى كُلِّ حَالٍ، نَحْوُ: يَمُنَ يَيْمُنُ … وَيَسَرَ يَيْسِرُ»; Maqṣūd `maqsud-sarf.txt`
  L839–L849 (the whole paradigm of يَسَرَ).
- **Engine:** `sarfDerive` L7674 `return no("mithal-ya")`.

### A07 · Tasgir · Nisba lab · WRONG — nisba of the ة-nouns that have lost their lām
- **Input:** `سَنَة`, `لُغَة`, `شَفَة`.
- **Shown:** «سنِيّ», «لغِيّ», «شفِيّ».
- **Correct:** سَنَوِيّ · لُغَوِيّ · شَفَهِيّ (or شَفَوِيّ).
- **Book:** not treated in `research/sources` (the standard rule of the nasab chapter: the dropped lām returns). The
  sources themselves write «لُغَوِيَّه» (`alaka-ilm-bayan.txt` L339).
- **Engine:** `IsmEngine.nisba` L10419.

### A08 · Tasgir · Nisba lab · WRONG — the diminutive does not send a word back to its origin
- **Input:** `مِيزَان`, `دِينَار`, `مَاء`, `اِبْن`, `اِسْم`, `أُخْت`, `بِنْت`.
- **Shown:** «مُيَيْزِين», «دُيَيْنِير», «مُوَيْء», «اُبَيْن», «اُسَيْم», «أُخَيْت», «بُنَيْت».
- **Correct:** مُوَيْزِين · دُنَيْنِير · مُوَيْه · بُنَيّ · سُمَيّ · أُخَيَّة · بُنَيَّة.
- **Book:** not in `research/sources` beyond the Maqṣūd emsile rows; the standard rule «التصغير يردّ الأشياء إلى أصولها».
- **Engine:** `IsmEngine.tasgir` L10390.

### A09 · Tasgir · Nisba lab · WRONG — three-letter feminines by usage
- **Input:** `دَار`, `نَار`, `يَد`; and `حَرْب`.
- **Shown:** «دُوَيْر», «نُوَيْر», «يُدَيّ»; «حُرَيْبَة».
- **Correct:** دُوَيْرَة · نُوَيْرَة · يُدَيَّة; and حُرَيْب (the listed exception). The lab prints the rule itself for شَمْس / عَيْن
  («الْمُؤَنَّثُ السَّمَاعِيُّ تَظْهَرُ تَاؤُهُ فِي التَّصْغِيرِ») and does not apply it here.
- **Book:** not in `research/sources`; the lab's own printed rule.
- **Engine:** `IsmEngine.tasgir` L10390.

### A10 · Mizan lab · WRONG — the literal «Wazn: null»
- **Input:** `مُسْتَقِيم`, `مِيزَان`, `قَاضٍ`, `قَائِل`, `عُلَمَاء`, `سَمَاء`, `دُعَاء`, `مُصْطَفَى`.
- **Shown:** «الْوَزْن · Wazn: null», then a LEARNED guess: مُسْتَقِيم → مُسْتَفْعَل 52 % «ism mafʿūl» over مُسْتَفْعِل 19 %;
  عُلَمَاء → فَعْلَان 51 % / أَفْعِلَاء 19 %; دُعَاء → أَفْعِلَاء 22 %.
- **Correct:** مُسْتَفْعِل · مِفْعَال · فَاعٍ · فَاعِل · فُعَلَاء · فَعَال · فُعَال · مُفْتَعَل. For عُلَمَاء the right scale is not in the shortlist.
- **Book:** Maqṣūd emsile rows.
- **Engine:** `renderMizanOut` L15440 [15441] prints `r.wazn` unguarded; `WaznEngine.of` L10149.

### A11 · Root Finder · WRONG — the weak ism mafʿūl is called مَفْعَل
- **Input:** `مَبِيع`, `مَقُول`, `مَرْمِيّ`, `مَدْعُوّ`.
- **Shown:** «مَفْعَل — اسْمُ مَكَانٍ أَوْ زَمَانٍ أَوْ مَصْدَرٌ مِيمِيٌّ» (the root is right).
- **Correct:** مَفْعُول — اسم المفعول (مَبْيُوع → مَبِيع, مَقْوُول → مَقُول, مَرْمُوي → مَرْمِيّ).
- **Book:** Maqṣūd emsile rows «مَقُولٌ», «مَرْمِيٌّ»; ʿIzzī on the ism al-mafʿūl of the ajwaf and the nāqiṣ.
- **Engine:** `RootFinder.find` L9907 (the peeling rules' scale label); shown by `renderJadhrOut` L14823 [14824].

### A12 · Mizan lab · WRONG — the same words, with a malformed «computed» scale
- **Input:** `مَبِيع`, `مَقُول`, `مَرْمِيّ`.
- **Shown:** «Derived from the bab · مَفْعَل — اسْمُ مَكَانٍ…», COMPUTED «مَفِعل» / «مَفُعل» / «مَفْعِلّ»; for مَرْمِيّ LEARNED «مُفَعِّل 40 %».
- **Correct:** مَفْعُول by the aṣl (the lab says it gives «the wazn by the ASL, as the madrasah answers it»).
- **Book:** as A11.
- **Engine:** `WaznEngine.of` L10149, `WaznEngine.mizan` L10204.

### A13 · Sarf lab · WRONG — the maṣdar of اِسْتَفْعَلَ from a wāw-initial root
- **Input:** roots `وقف`, `وعب`, `وجب`, `ورد`, `وطن`, Form X.
- **Shown:** «اِسْتِوْقَاف», «اِسْتِوْعَاب», «اِسْتِوْجَاب», «اِسْتِوْرَاد», «اِسْتِوْطَان».
- **Correct:** اِسْتِيقَاف · اِسْتِيعَاب · اِسْتِيجَاب · اِسْتِيرَاد · اِسْتِيطَان (a quiescent wāw after a kasra turns to yāʾ — the lab does
  it in Form IV: إِيعَاد).
- **Book:** Maqṣūd L832–L834 «اَوْعَدَ يُوعِدُ اِيعاَداً»; ʿIzzī L173 on the same change.
- **Engine:** `sarfDerive`, Form X maṣdar builder L7902.

### A14 · Sarf lab · WRONG — the participles of اِفْتَعَلَ from a tāʾ-initial root
- **Input:** roots `تبع`, `تجر`, Form VIII.
- **Shown:** verb «اِتَّبَعَ يَتَّبِعُ» right, but اسم الفاعل «مُتْتَبِع», اسم المفعول «مُتْتَبَع»; «مُتْتَجِر», «مُتْتَجَر».
- **Correct:** مُتَّبِع / مُتَّبَع · مُتَّجِر / مُتَّجَر.
- **Book:** ʿIzzī L175 «اتَّعَدَ يَتَّعِدُ اتِّعَادًا فَهُوَ مُتَّعِدٌ، وَذَاكَ مُتَّعَدٌ».
- **Engine:** `sarfDerive`, Form VIII branch L7838–L7875 (the participle pair built at L7875 is not passed through `sjIdgham` L7127).

### A15 · I'lāl lab · WRONG — the nāqiṣ on مَفْعَلٌ is left untouched
- **Input:** `رمي`, `دعو`, `وقي`, `خشي`, shape `مَفْعَلٌ`.
- **Shown:** «مَرْمَيٌ → مَرْمَيٌ», «مَدْعَوٌ → مَدْعَوٌ», «مَوْقَيٌ» — with the note that no iʿlāl fires.
- **Correct:** مَرْمًى · مَدْعًى · مَوْقًى (a vowelled weak lām after a fatḥa turns to alif — the lab's own first rule).
- **Book:** ʿIzzī L337 «وَمِنَ الْمُعْتَلِّ اللَّامِ مَفْتُوحٌ أَبَدًا، كَالْمَأْوَى وَالْمَرْمَى».
- **Engine:** `IlalEngine.build` L8665.

### A16 · I'lāl lab · WRONG — the nāqiṣ on مِفْعَالٌ
- **Input:** `رمي`, `دعو`, `وقي`, shape `مِفْعَالٌ`.
- **Shown:** «مِرْمَايٌ», «مِدْعَاوٌ», «مِيقَايٌ», unchanged.
- **Correct:** مِرْمَاءٌ · مِدْعَاءٌ · مِيقَاءٌ (a weak lām after an added alif becomes hamza, as in دُعَاء, كِسَاء, إِعْطَاء).
- **Book:** Maqṣūd, the Form IV row of غَزَا («إِغْزَاءً») for the same change; not stated for the instrument noun itself.
- **Engine:** `IlalEngine.build` L8665.

### A17 · I'lāl lab · WRONG — the nāqiṣ on أَفْعَلُ is said to be «blocked»
- **Input:** `دعو`, `رمي`, `خشي`, `سعي`, shape `أَفْعَلُ`.
- **Shown:** «أَدْعَوُ → أَدْعَوُ», «أَرْمَيُ», «أَخْشَيُ», with «أَفْعَلُ التَّفْضِيلِ وَفِعْلُ التَّعَجُّبِ لَا يُعَلَّانِ».
- **Correct:** أَدْعَى · أَرْمَى · أَخْشَى. The rule quoted protects the ʿAYN (أَقْوَلُ, أَبْيَعُ); the lām does turn (أَعْلَى, أَدْنَى). The Ism lab
  itself prints «أَرْمَى — لَامُهُ الْمُعْتَلَّةُ تُقْلَبُ أَلِفًا».
- **Book:** Maqṣūd, the tafḍīl block of غَزَا / رَمَى.
- **Engine:** `IlalEngine.SAHIH_SHAPES` L8639, applied to every class.

### A18 · I'lāl lab · WRONG — the hollow root on مِفْعَالٌ is weakened
- **Input:** `كيل`, `قول`, `عور`, `صون`, `بيع`, shape `مِفْعَالٌ`.
- **Shown:** «مِكْيَالٌ → مِكَالٌ», «مِقَالٌ», «مِعَارٌ», «مِصَانٌ», «مِبَاعٌ» (three steps each).
- **Correct:** مِكْيَال · مِقْوَال · مِعْوَار — the instrument noun of a hollow root is not weakened.
- **Book:** Maqṣūd, the emsile row of قَالَ: «مِقْوَلٌ» (the lab's own Maqṣūd page shows it); CLAUDE.md L7954.
- **Engine:** `IlalEngine.build` L8665.

### A19 · I'lāl lab · WRONG — the lafīf maqrūn loses its ʿayn
- **Input:** `طوي`, shapes `فَاعِلٌ`, `مَفْعُولٌ`, `يَفْعِلُ`, `اُفْعُلْ`.
- **Shown:** «طَائٍ», «مَطِيٌّ», «يَطِيُّ», «طِ».
- **Correct:** طَاوٍ · مَطْوِيٌّ · يَطْوِي · اِطْوِ (the ʿayn of a lafīf maqrūn is treated as sound).
- **Book:** Maqṣūd, the paradigm of رَوَى (رَاوٍ، مَرْوِيٌّ، يَرْوِي، اِرْوِ) — the lab's own Maqṣūd page.
- **Engine:** `IlalEngine.build` L8665 (no lafīf guard).

### A20 · I'lāl lab · WRONG — the doubled root is shown unmerged as «what is said»
- **Input:** `مدد`, `فرر`, `مسس`, all shapes.
- **Shown:** «مَادِدٌ → مَادِدٌ», «يَمْدِدُ», «اُمْدُدْ», «مَمْدَدٌ».
- **Correct:** مَادٌّ · يَمُدُّ · مُدَّ · مَمَدٌّ.
- **Book:** ʿIzzī L140 «وَالْإِدْغَامُ وَاجِبٌ فِي نَحْوِ: مَدَّ يَمُدُّ».
- **Engine:** `IlalEngine.build` L8665 (idghām is not among its rules, and no note says so).

### A21 · I'lāl lab · WRONG — the amr of يسر, with an invented rule
- **Input:** `يسر`, shape `اُفْعُلْ`.
- **Shown:** «اُيْسُرْ → اِيْسُرْ — ثَقُلَتِ الضَّمَّةُ قَبْلَ الْيَاءِ فَقُلِبَتْ كَسْرَةً لِمُنَاسَبَتِهَا».
- **Correct:** اِيسِرْ (the verb is يَيْسِرُ). And by rule a quiescent yāʾ after a ḍamma turns to WĀW, not the reverse.
- **Book:** Maqṣūd L841 «اِيسِرْ»; ʿIzzī L173 «أَصْلُهُ مُيْسِرٌ، فَقُلِبَتِ الْيَاءُ … وَاوًا لِسُكُونِهَا وَانْضِمَامِ مَا قَبْلَهَا».
- **Engine:** `IlalEngine` rule table (class L8371).

### A22 · Sarf ledger · WRONG — تَرْمِينَ is given a hidden ḍamma
- **Input:** `تَرْمِينَ`.
- **Shown:** step 5 «الضَّمَّةُ مُقَدَّرَةٌ عَلَى حَرْفِ الْعِلَّةِ لِلثِّقَلِ أَوِ التَّعَذُّرِ»; the cell is read as the feminine singular only.
- **Correct:** the 2nd fem. sing. is raised by its nūn (one of the five verbs) and its lām is dropped (تَرْمِيِينَ → تَرْمِينَ); the
  fem. plural is built on the sukūn. No hidden ḍamma in either.
- **Book:** ʿIzzī L244 «تَرْمِي تَرْمِيَانِ تَرْمُونَ، تَرْمِينَ تَرْمِيَانِ تَرْمِينَ» (one spelling, two cells); Iẓhār L168 on the five verbs.
- **Engine:** `SarfLedger` L19907 [20228]; `renderSarfLedgerOut` L16730 [16731].

### A23 · Sarf ledger · WRONG — أَقِمْ is given a hamzat al-waṣl
- **Input:** `أَقِمْ`.
- **Shown:** step 5 «حُذِفَ حَرْفُ الْمُضَارَعَةِ، وَجِيءَ بِهَمْزَةِ الْوَصْلِ لِسُكُونِ مَا بَعْدَهُ».
- **Correct:** the hamza is the qaṭʿ hamza of أَفْعَلَ come back (the ledger's own step 3), and the qāf after it is vowelled.
- **Book:** ʿIzzī L98 «وَفَتَحُوا هَمْزَةَ أَكْرِمْ بِنَاءً عَلَى الْأَصْلِ الْمَرْفُوضِ، فَإِنَّ أَصْلَ تُكْرِمُ تُؤَكْرِمُ».
- **Engine:** `SarfLedger` L19907 [20228].

### A24 · Pronoun lab · WRONG — the five nouns with the speaker's yāʾ
- **Input:** attach `أَنَا` to `أَبُو`, `أَخُو`, `أَبَا`, `أَبِي` (kind: noun).
- **Shown:** «أَبِيَّ», «أَخِيَّ», «أَبَايَ», «أَبِيَّ».
- **Correct:** أَبِي / أَخِي in all three cases — with the speaker's yāʾ the five nouns leave the letters and take hidden vowels.
- **Book:** Iẓhār `izhar-al-asrar-matn-lithograph.txt` L162 «فهو الأسماء الستة المضافة إلى غير ياء المتكلم», L177 «ما أضيف إلى ياء
  المتكلم … فالكل تقديري نحو غلامي»; Kāfiya su'al-cevap `kafiya-ibn-hajib-sual-cevap.txt` L136.
- **Engine:** `DamirEngine.attach` L39926 [40247].

### A25 · Tasgir · Nisba lab · WRONG — malformed strings
- **Input:** `دُنْيَا`, `عَصًا`, `سَمَاء`, `كِسَاء`, `قَاضٍ`.
- **Shown:** «دُنَيِّا», «عُصَيْاَة», «سُمَيِّء», «كُسَيِّء», «قُوَيْض».
- **Correct:** دُنَيَّا · عُصَيَّة · سُمَيَّة · كُسَيّ · قُوَيْضٍ (the lab's own note under بَاب writes «قَاضٍ → قُوَيْضٍ»).
- **Book:** — (not possible spellings).
- **Engine:** `IsmEngine.tasgir` L10390.

### A26 · Tasgir · Nisba lab · WRONG — words ending in yāʾ or hamza
- **Input:** `قَاضِي`, `كُرْسِيّ`, `شَيْء`.
- **Shown:** قَاضِي → nisba «قاضيِيّ»; كُرْسِيّ → nisba «كرسيِيّ», diminutive «كُرَيْسِي»; شَيْء → nisba «شيءِيّ».
- **Correct:** قَاضِيّ (or قَاضَوِيّ) · كُرْسِيّ, كُرَيْسِيّ · شَيْئِيّ.
- **Book:** not in `research/sources`.
- **Engine:** `IsmEngine.nisba` L10419, `IsmEngine.tasgir` L10390.

### A27 · Tasgir · Nisba lab · WRONG — the dual and plural rows
- **Input:** `صَحْرَاء`, `حَمْرَاء`, `بِنْت`, `أَب`, `دَلْو`, `ظَبْي`, `كُبْرَى`, `كِتَاب`, `رَجُل`.
- **Shown:** sound feminine plural «صَحْرَاءَاتٌ», «حَمْرَاءَاتٌ», «بِنْتَاتٌ», «أَبَاتٌ», «رَجُلَاتٌ»; broken «صَحَارِيء», «حَمَارِيء»,
  «أَبْنَات», «أَدْلُو», «أَظْبُي», «كَبَارِى», «أَكْتِبَة»; dual of أَب «أَبَانِ».
- **Correct:** صَحْرَاوَاتٌ (the lab writes صَحْرَاوَانِ in the dual) · حَمْرَاوَات, حُمْر · بَنَات · أَبَوَانِ, آبَاء · أَدْلٍ · أَظْبٍ · كُبَر · كُتُب ·
  رِجَال (no sound feminine plural).
- **Book:** not in `research/sources` (Iẓhār treats only the signs).
- **Engine:** `IsmEngine.jamSalim` L10506 and the dual / broken-plural block of `renderIsmOut` L15358 [15359].

### A28 · Tasgir · Nisba lab · WRONG — مَسْجَد stated flat
- **Input:** root `سجد` (also `طلع`).
- **Shown:** «اسْمُ الزَّمَانِ وَالْمَكَانِ: مَسْجَد — مَفْعَل لِأَنَّ عَيْنَ مُضَارِعِهِ غَيْرُ مَكْسُورَةٍ»; طلع → «مَطْلَع».
- **Correct:** مَسْجِد, مَطْلِع — on the books' list of irregulars.
- **Book:** ʿIzzī L332 «وَشَذَّ الْمَسْجِدُ وَالْمَشْرِقُ وَالْمَغْرِبُ وَالْمَطْلِعُ وَالْمَجْزِرُ…»; Marāḥ `marah-al-arwah-src.txt` L478.
- **Engine:** `IsmEngine.zamanMakan` L10551.

### A29 · Tasgir · Nisba lab · WRONG — a superlative from a colour and a defect
- **Input:** roots `حمر`, `عور`.
- **Shown:** «أَفْعَل التَّفْضِيل · Superlative: أَحْمَرُ — أَفْعَلُ وَمُؤَنَّثُهُ فُعْلَى»; «أَعْوَرُ».
- **Correct:** no afʿal al-tafḍīl is built from a colour or a defect; أَحْمَرُ is the ṣifa and its feminine is حَمْرَاء.
- **Book:** Marāḥ L419 «مِمَّا لَيْسَ بِلَوْنٍ وَلَا عَيْبٍ», L421 «وَلَا يَجِيءُ مِنْ لَوْنٍ وَلَا عَيْبٍ، لِأَنَّ فِيهِمَا يَجِيءُ أَفْعَلُ لِلصِّفَةِ».
- **Engine:** `IsmEngine.tafdil` L10539.

### A30 · Derivation lab · WRONG — the same word read as an elative
- **Input:** `أَحْمَر`.
- **Shown:** «أَفْعَلُ · اسْمُ التَّفْضِيلِ · elative».
- **Correct:** الصفة المشبهة.
- **Book:** Marāḥ L419–L421.
- **Engine:** `IshtiqaqEngine` L8708; `renderIshtOut` L8276.

### A31 · Derivation lab · WRONG — a quality read as a maṣdar
- **Input:** `عَطْشَان`.
- **Shown:** «recited form · الْمَصْدَرُ · verbal noun … so it means being thirsty».
- **Correct:** صفة مشبهة on فَعْلَان (the lab answers غَضْبَان rightly); the maṣdar is عَطَش.
- **Book:** Marāḥ L408–L410: the ṣifa mushabbaha comes on «فَعْلَانُ» … «نَحْوُ … وَعَطْشَانُ وَأَحْوَلُ».
- **Engine:** `IshtiqaqEngine` L8708 (the «recited form» path).

### A32 · Derivation lab · WRONG — time nouns on مِفْعَال read as instruments
- **Input:** `مِيعَاد`, `مِيلَاد`.
- **Shown:** «مِفْعَالٌ · اسْمُ الْآلَةِ · noun of instrument», no alternative offered.
- **Correct:** nouns of time (the appointed time, the time of birth). مِيزَان / مِفْتَاح / مِنْشَار are answered rightly.
- **Book:** not listed word by word in `research/sources`.
- **Engine:** `IshtiqaqEngine` L8708.

### A33 · Tasgir · Nisba lab · WRONG — further diminutives and nisbas
- **Input:** `سُلْطَان`, `قُرَيْش`, `مُصْطَفَى`, `طَيّ`.
- **Shown:** «سُلَيْطَان»; «قُرَيِّش»; مُصْطَفَى → «مُصَيْطِف», nisba «مصطفَوِيّ»; طَيّ → «طَيَوِيّ».
- **Correct:** سُلَيْطِين (neither a name nor a ṣifa — the rule the lab prints keeps ـان only «فِي الْأَعْلَامِ وَالصِّفَاتِ») · قُرَيْش is
  already a diminutive · مُصَيْفٍ, مُصْطَفِيّ · طَوَوِيّ by the rule the lab prints («الْأُولَى تُرَدُّ إِلَى أَصْلِهَا»), heard طَائِيّ.
- **Book:** not in `research/sources`; the lab's own printed rules.
- **Engine:** `IsmEngine.tasgir` L10390, `IsmEngine.nisba` L10419.

### A34 · Tasgir · Nisba lab · WRONG — nonsense on weak-ending nouns
- **Input:** `قَاضٍ`, `عَصًا`.
- **Shown:** قَاضٍ → superlative «أَقْاَضُ», time/place «مَقْاَض / مَقْاِض»; عَصًا → «أَعْصَاُ», «مَعْصَا / مَعْصِا».
- **Correct:** a refusal, or the rows built on the corpus root (ق ض ي / ع ص و).
- **Book:** —.
- **Engine:** `renderIsmOut` L15358 [15359] (the root is taken from the bare letters when they number three).

### A35 · Sarf lab · WRONG — bāb كَرُمَ refused for the nāqiṣ and the mithāl
- **Input:** `سرو` (the lab's own auto-pick is bāb 5), `وجه` and `وسم` with bāb 5.
- **Shown:** «This class does not recite that bab.»
- **Correct:** سَرُوَ يَسْرُو; وَجُهَ يَوْجُهُ اُوجُهْ.
- **Book:** ʿIzzī L226 (the full māḍī of سَرُوَ), L167 «كَوَجُهَ يَوْجُهُ، وَالْأَمْرُ: اُوجُهْ».
- **Engine:** `sarfDerive` L7661 `no("naqis-bab")`, L7675 `no("mithal-bab")`.

### A36 · Sarf lab · WRONG — the iʿlāl chain of the mithāl in bāb فَتَحَ contradicts itself
- **Input:** roots `وضع`, `وهب`, `وقع`, `ودع` (Form I, bāb 3).
- **Shown:** «أَصْلُهُ يَوْضَعُ ← يَضَعُ — وَقَعَتِ الْوَاوُ بَيْنَ الْيَاءِ الْمَفْتُوحَةِ وَالْكَسْرَةِ فَحُذِفَتْ» (no kasra in the origin shown).
- **Correct:** أَصْلُهُ يَوْضِعُ; the wāw drops; then the ʿayn takes a fatḥa for the throat letter.
- **Book:** ʿIzzī L168; Marāḥ L721 «لِأَنَّ أَصْلَهُ يَوْضِعُ فَحُذِفَتِ الْوَاوُ».
- **Engine:** `ilalSteps` L8202, the mithāl step L8237–L8241.

### A37 · Sarf lab · WRONG — «the wāw was turned to tāʾ» said of a yāʾ
- **Input:** root `يسر`, Form VIII.
- **Shown:** «اِتَّسَرَ» with the note «قُلِبَتِ الْوَاوُ تَاءً وَأُدْغِمَتْ».
- **Correct:** قُلِبَتِ الْيَاءُ تَاءً.
- **Book:** ʿIzzī L107 «قُلِبَتِ الْوَاوُ وَالْيَاءُ وَالثَّاءُ تَاءً … اتَّقَى وَاتَّسَرَ», L175.
- **Engine:** `sarfDerive` Form VIII, note L7871.

### A38 · Sarf lab · WRONG — the model verb of اِفْعَوْعَلَ is misspelt
- **Input:** any root, Form XII (e.g. `عشب`, `خشن`).
- **Shown:** note «اِفْعَوْعَلَ: … اِغْشَوْشَبَتِ الْأَرْضُ: كَثُرَ عُشْبُهَا».
- **Correct:** اِعْشَوْشَبَتِ الْأَرْضُ.
- **Book:** ʿIzzī L33 «وَافْعَوْعَلَ، نَحْوُ: اعْشَوْشَبَ يَعْشَوْشِبُ اعْشِيشَابًا».
- **Engine:** `mazidDerive` L7343, note L7365.

### A39 · 35 doors · WRONG — door 16 is built on a root that is not a word
- **Input:** door 16.
- **Shown:** root «غ ش ب», model «اِغْشَوْشَبَ يَغْشَوْشِبُ اِغْشِيشَابًا» — while the same card's example reads «اِعْشَوْشَبَتِ الْأَرْضُ».
- **Correct:** ع ش ب — اِعْشَوْشَبَ يَعْشَوْشِبُ اِعْشِيشَابًا.
- **Book:** ʿIzzī L33. The app's source table `sarf-35-bab-tablosu.txt` L26 carries both spellings on one row («عشب الأرض -
  اعشوشب الأرض» beside «اغشَوشَب»), so the slip was copied from the table.
- **Engine:** `Bab35Engine.DOORS` entry `root: "غشب"` L7438.

### A40 · Sarf lab · WRONG — the hamza seat of a four-letter verb
- **Input:** root `طمأن`.
- **Shown:** «يُطَمْأِنُ», «مُطَمْأِن», «طَمْأِنْ».
- **Correct:** يُطَمْئِنُ · مُطَمْئِن · طَمْئِنْ.
- **Book:** ʿIzzī L140 «وَاطْمَأَنَّ يَطْمَئِنُّ».
- **Engine:** `rubai17Derive` L7376 (no hamza seating — hamzated triliterals are refused for this very reason).

### A41 · Tawkīd nūn lab · WRONG — hamza seats in the stored paradigm of قَرَأَ
- **Input:** `يَقْرَأُ` (also بَدَأَ, مَلَأَ).
- **Shown:** rows «اِقْرَأَا → اِقْرَأَانِّ», «اِقْرَأُوا → اِقْرَأُنَّ», «اِقْرَأِي → اِقْرَأِنَّ», «يَقْرَأَانِ», «تَقْرَأِينَ → تَقْرَأِنَّ».
- **Correct:** اِقْرَآ / اِقْرَآنِّ · اِقْرَئِي / اِقْرَئِنَّ · يَقْرَآنِ · تَقْرَئِينَ / تَقْرَئِنَّ. (The same stored tables hold «أَأْخُذُ», «أَأْكُلُ»,
  «أَأْمُرُ» for آخُذُ, آكُلُ, آمُرُ.)
- **Book:** Maqṣūd L1071 «اَقْرَئَانِ اَقْرَئُونَ»; L785–L786 «آخِذٌ … آخَذُ».
- **Engine:** the stored paradigm (`RootFinder.corpusIndex()` entry of قَرَأَ: `m.mudari`, `m.amr`), carried through
  `TawkidNunEngine.table` L26588 [26909].

### A42 · Maqṣūd lab · WRONG — malformed engine forms inside amber «orthography only» cells
- **Input:** models `مَدَّ`, `فَرَّ`, `عَضَّ` (block اسْمُ التَّفْضِيلِ, cells 2–3); `غَزَا` (Form IV, أَفْعِلْ بِهِ); `سَأَلَ`, `رَأَى` (الْمُبَالَغَةُ).
- **Shown:** the engine's form beside the book's: «أَمَدَُّانِ», «أَمَدُُّونَ» (two vowels on one letter); «إِغْزَاءِهِ»; «سَآّلٌ», «رَآّؤٌ».
- **Correct:** أَمَدَّانِ, أَمَدُّونَ · إِغْزَائِهِ · سَأَّالٌ · رَأَّاءٌ (the book's own cells). Amber is glossed in the legend as «differs only
  in the text's orthography» — here it is the engine's form that is broken.
- **Book:** `maqsud-sarf.txt`, the rows the cells quote.
- **Engine:** `MaqsudEngine.emsileI` L36042 [36363] (the mubālagha line L36054 [36375]), `MaqsudEngine.blocksI` L36062 [36383].
  The 22 red cells are all slips of the book's scan with the engine right — those are honest.

### A43 · Root Finder · WRONG — the root of مُدَّكِر
- **Input:** `مُدَّكِر`.
- **Shown:** «Root: د ك ر».
- **Correct:** ذ ك ر. The intro promises «reversing even the iftial ibdal».
- **Book:** ʿIzzī L105 «فِي افْتَعَلَ مِنَ الدَّرْءِ وَالذِّكْرِ وَالزَّجْرِ: ادَّرَأَ وَاذَّكَرَ وَازْدَجَرَ».
- **Engine:** `RootFinder.find` L9907.

### A44 · Root Finder · WRONG — scale labels that contradict the typed vowels; a wrong root
- **Input:** `كُتُب`, `رَحْمَة`, `مُقَاتَلَة`, `أَقْلَام`, `عِدَة`.
- **Shown:** «فَعَلَ / فَعَّلَ»; «فَعَلَ / فَعَّلَ»; «مُفَاعِل / مَفَاعِل»; «إِفْعَال — مَصْدَر»; عِدَة → «Root: ع د ة», «فَعَلَ / فَعَّلَ».
- **Correct:** فُعُل (plural) · فَعْلَة · مُفَاعَلَة (maṣdar of III) · أَفْعَال (plural) · root و ع د, scale عِلَة.
- **Book:** Maqṣūd emsile row of وَعَدَ («عِدَةً»).
- **Engine:** `RootFinder.find` L9907 (peeling-rule labels). The Mizan lab repeats عِدَة → «Root: ع د ة», COMPUTED «فِعَل»
  (`WaznEngine.of` L10149).

### A45 · Mizan lab · WRONG — اِتَّقَى is called unruled
- **Input:** `اِتَّقَى`, `يَتَّقِي`.
- **Shown:** «The corpus stores this form as recited (sema'i) — its wazn is not derived by rule», then LEARNED «تَفَعُّل 29 % /
  اِفْتِعَال 16 %» (for يَتَّقِي: «فَعَّال 40 %»).
- **Correct:** اِفْتَعَلَ / يَفْتَعِلُ, by rule. The Root Finder says «بَابُ الِافْتِعَالِ» for the same word.
- **Book:** ʿIzzī L107 «نَحْوُ: اتَّقَى».
- **Engine:** `WaznEngine.of` L10149; `renderMizanOut` L15440 [15441] (the `mizanStored` branch, string L2956).

### A46 · Sarf lab · WRONG — iftaʿala in the sense of tafāʿala is weakened
- **Input:** roots `جور`, `زوج`, `عور`, Form VIII.
- **Shown:** «اِجْتَارَ», «اِزْدَاجَ», «اِعْتَارَ».
- **Correct:** اِجْتَوَرَ · اِزْدَوَجَ · اِعْتَوَرَ.
- **Book:** Marāḥ L774 «وَنَحْوُ عَوِرَ وَاجْتَوَرَ لِأَنَّ حَرَكَةَ الْعَيْنِ وَالتَّاءِ فِي حُكْمِ السُّكُونِ».
- **Engine:** `sarfDerive` Form VIII ajwaf branch L7838–L7851.

### A47 · Sarf lab · WRONG — the reason given for the idghām of the māḍī
- **Input:** root `مدد` (any doubled root), Form I.
- **Shown:** «أَصْلُهُ مَدَدَ ← مَدَّ — نُقِلَتْ حَرَكَةُ الْأَوَّلِ ثُمَّ أُدْغِمَ الْمِثْلَانِ».
- **Correct:** in the māḍī the first twin's vowel is dropped (the mīm before it is already vowelled); the carrying-back
  belongs to the muḍāriʿ (يَمْدُدُ → يَمُدُّ).
- **Book:** ʿIzzī L140–L145.
- **Engine:** `ilalSteps` L8202, the `gem` step L8242–L8246.

### A48 · Root Finder · WRONG — two words typed together
- **Input:** `لَمْ يَرْمِ`, `لَمْ يَكُنْ`.
- **Shown:** «Root: ي ر م — مُفْعِل / مُفَعِّل»; «Root: ي ك ن».
- **Correct:** ر م ي, ك و ن (each is right when typed alone).
- **Book:** —.
- **Engine:** `renderJadhrOut` L14823 [14824] hands the whole string to `RootFinder.find` L9907.

### A49 · Sarf lab · MISLEADING — participles for the intransitive bāb
- **Input:** root `حسن`, Form I, bāb 5.
- **Shown:** chips «اسم الفاعل: حَاسِن», «اسم المفعول: مَحْسُون».
- **Correct:** bāb 5 is intransitive only — the 35-doors card says so itself — and its quality is حَسَن; there is no مَحْسُون.
- **Book:** ʿIzzī L44 «حَسُنَ زَيْدٌ … لَازِمًا».
- **Engine:** `sarfDerive` sound branch L7604.

### A50 · Sarf lab · MISLEADING — Form VII of a nūn-initial root is spelt two ways
- **Input:** root `نصر`, Form VII.
- **Shown:** verb «اِنَّصَرَ يَنَّصِرُ», but participle «مُنْنَصِر», maṣdar «اِنْنِصَار».
- **Correct:** one spelling throughout (the naql table writes the drill form unmerged: اِنْنَصَرَ).
- **Book:** `bablara-nakil-tablosu.txt` L6 «اِنْنَصَرَ».
- **Engine:** `sarfDerive` Form VII L7810–L7836.

### A51 · Root Finder · MISLEADING — one cell named where two fit
- **Input:** `قُلْنَ`, `تَقَاتَلُوا`, `أَكْبَر`.
- **Shown:** «الْأَمْرُ — command — you (pl, f)»; «الْأَمْرُ — command — you (pl)»; أَكْبَر → «الْمُضَارِعُ — I» of كَبِرَ.
- **Correct:** قُلْنَ is also the māḍī «they (f) said»; تَقَاتَلُوا also the māḍī «they fought»; أَكْبَر is far likelier the tafḍīl.
- **Book:** ʿIzzī L196–L199 (قُلْنَ in both tables).
- **Engine:** `RootFinder.fromCorpus` L9437 (the first matching cell wins).

### A52 · Mizan lab · MISLEADING — the same single cell for تَقَاتَلُوا
- **Input:** `تَقَاتَلُوا`.
- **Shown:** «الْأَمْرُ — command — you (pl)» only.
- **Correct:** the māḍī of the 3rd masc. plural as well.
- **Book:** —.
- **Engine:** `WaznEngine.of` L10149.

### A53 · Mizan lab · MISLEADING — a noun-pattern guess under an identified verb
- **Input:** `يَقُولُ`, `قُلْتُ`, `اِسْتَقَامَ`, `يَرْمُونَ`.
- **Shown:** under the right wazn, a LEARNED panel: يَقُولُ → «فُعُول 28 % — a broken plural»; قُلْتُ → «فُعْل 52 % — a heard masdar»;
  اِسْتَقَامَ → «اِفْتِعَال 46 %»; يَرْمُونَ → «تَفْعِيل 19 %».
- **Correct:** no noun pattern applies to a verb the corpus has already identified.
- **Book:** —.
- **Engine:** `renderMizanOut` L15440 [15441] (the learned panel is drawn for every input).

### A54 · Sarf ledger · MISLEADING — قُلْنَ
- **Input:** `قُلْنَ`.
- **Shown:** «الصِّيغَةُ: الْأَمْرُ — فِعْلُ أَمْرٍ» only, with the reason «الْتَقَى سَاكِنَانِ بِالْجَزْمِ فَحُذِفَتِ الْعَيْنُ».
- **Correct:** also the māḍī; and the lām is quiescent for the women's nūn, not for a jazm.
- **Book:** ʿIzzī L196–L199.
- **Engine:** `SarfLedger` L19907 [20228].

### A55 · Derivation lab · MISLEADING — فَعِيل in the sense of mafʿūl
- **Input:** `قَتِيل`, `جَرِيح`; `رَسُول`.
- **Shown:** «الصِّفَةُ الْمُشَبَّهَةُ · lasting quality»; رَسُول → «صِيغَةُ الْمُبَالَغَةِ».
- **Correct:** فَعِيل بمعنى مفعول (the Mizan panel says «fa'il in the SENSE of maf'ul (قَتِيل = مَقْتُول)»); رَسُول is فَعُول in the sense
  of مُرْسَل.
- **Book:** Marāḥ L431 «إِذَا كَانَ بِمَعْنَى مَفْعُولٍ، نَحْوُ قَتِيلٍ وَجَرِيحٍ».
- **Engine:** `IshtiqaqEngine` L8708.

### A56 · Sarf lab · MISSING — no ism mafʿūl for the derived nāqiṣ
- **Input:** `سمي` II, `ندي` III, `عطي` IV, `لقي` V, `شري` VIII, `غني` X.
- **Shown:** اسم الفاعل «مُسَمٍّ», «مُعْطٍ»… and no اسم المفعول chip.
- **Correct:** مُسَمًّى · مُنَادًى · مُعْطًى · مُتَلَقًّى · مُشْتَرًى · مُسْتَغْنًى.
- **Book:** Maqṣūd, the Form rows of غَزَا / رَمَى.
- **Engine:** `sarfDerive` nāqiṣ branches L7717, L7736, L7789, L7854, L7886 (no `maful`).

### A57 · Tawkīd nūn lab · MISSING — the doubled verb before ā / ū / ī
- **Input:** `مُدَّ`, `يَفِرُّ`, `يُحِبُّ`, `يَسْتَعِدُّ`.
- **Shown:** rows مُدَّا / مُدُّوا / مُدِّي / يَمُدَّانِ / يَمُدُّونَ / تَمُدِّينَ → heavy «—», light «refused», no reason.
- **Correct:** مُدَّانِّ · مُدُّنَّ · مُدِّنَّ · يَمُدَّانِّ · يَمُدُّنَّ · تَمُدِّنَّ; light مُدُّنْ, مُدِّنْ.
- **Book:** ʿIzzī L114 and L143 «مُدَّا مُدُّوا مُدِّي».
- **Engine:** `TawkidNunEngine.table` L26588 [26909].

### A58 · Root Finder and Mizan lab · MISSING — two-letter forms and a second clitic
- **Input:** `قُلْ`, `عِدْ`, `قِ`, `سَلْ`, `خُذْ`, `مَدَّ`, `كُنَّ`, `بِعْ`, `يَدٌ`; and `وَبِالْكِتَابِ`.
- **Shown:** «Type at least three Arabic letters.»; وَبِالْكِتَابِ → «No root found» (بِالْكِتَابِ alone is answered).
- **Correct:** the intro says «Type any form — conjugated, augmented, or wearing its clitics». The commonest imperatives
  and every doubled māḍī are shut out by a length test on the written letters.
- **Book:** —.
- **Engine:** `renderJadhrOut` L14827 [14828]; `renderMizanOut` L15444 [15445]; `RootFinder.find` L9907 for the clitic.

### A59 · Sarf ledger · MISSING — the passive of the hollow verb
- **Input:** `قِيلَ`, `يُقَالُ`.
- **Shown:** only «الْمَبْنِيُّ لِلْمَجْهُولِ: ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ آخِرِهِ» (which describes قُوِلَ), then «This cell is stored, not rebuilt».
- **Correct:** قُوِلَ → قِيلَ (the kasra carried back, the wāw turned to yāʾ); يُقْوَلُ → يُقَالُ. The intro promises «every sarf rule
  that turned the root into this spelling … the passive vowelling».
- **Book:** the standard iʿlāl of the hollow passive (not located verbatim in `research/sources`).
- **Engine:** `SarfLedger` L19907 [20228].

### A60 · Sarf ledger · MISSING — verbs whose only change is a dropped or merged letter
- **Input:** `يَرْمُونَ`, `يَخْشَوْنَ`, `يَمُدُّونَ`, `عِدْ`.
- **Shown:** root, bāb, cell and the prefix/suffix line — no rule step — then «✓ Rebuilt from the root by the rule engine».
- **Correct:** the lām dropped before the plural wāw (يَرْمِيُونَ → يَرْمُونَ; يَخْشَيُونَ → يَخْشَوْنَ), the idghām of يَمُدُّونَ, the wāw
  dropped in عِدْ (the ledger does tell it for يَعِدُ).
- **Book:** ʿIzzī L228 (the vowel before the plural wāw), L140, L167–L168.
- **Engine:** `SarfLedger` L19907 [20228].

---

# B · Iʿrāb

Ranked by how often a learner would meet the fault. Iẓhār = `izhar-al-asrar-matn-lithograph.txt`; Kāfiya =
`kafiya-ibn-hajib-sual-cevap.txt`; Qawāʿid = `qawaid-al-irab-ibn-hisham-matn.txt`.

### B01 · Analyzer (Jumla) · WRONG — the jarr of a diptote and of the five nouns is called «the plain kasra»
- **Input:** `مَرَرْتُ بِأَحْمَدَ`; `مَرَرْتُ بِأَبِيكَ`.
- **Shown:** بِأَحْمَدَ «اسْمٌ، مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ الظَّاهِرَةُ» (its own gloss beside it: «hence a diptote»); بِأَبِيكَ the same.
- **Correct:** مجرور وعلامة جره الفتحة نيابة عن الكسرة لأنه ممنوع من الصرف; بِأَبِيكَ: علامة جره الياء لأنه من الأسماء الستة.
- **Book:** Iẓhār L162 «بالضمة رفعا والفتحة نصبا وجرا فهو غير المنصرف», and «بالواو رفعا والألف نصبا والياء جرا فهو الأسماء الستة».
- **Engine:** `Murib.line` L19393 [19711], sign branch L19457–L19460 [19775–19778] (the `fatha-niyaba` branch exists but is not
  reached for a word fused to its jarr letter).

### B02 · Analyzer (Jumla) · WRONG — every sister is named after the mother
- **Input:** `لَيْسَ زَيْدٌ قَائِمًا`; `أَصْبَحَ الْبَرْدُ شَدِيدًا`; `مَا زَالَ زَيْدٌ قَائِمًا`; `لَعَلَّ زَيْدًا قَادِمٌ`; `لَيْتَ الشَّبَابَ يَعُودُ`; `كَأَنَّ زَيْدًا أَسَدٌ`.
- **Shown:** زَيْدٌ «اسْمُ كَانَ», قَائِمًا «خَبَرُ كَانَ» under لَيْسَ / أَصْبَحَ / مَا زَالَ; «اسْمُ إِنَّ / خَبَرُ إِنَّ» under لَعَلَّ / لَيْتَ / كَأَنَّ.
  أَصْبَحَ itself is described as «فِعْلٌ، مَنْصُوبٌ»; لَيْتَ only as «حَرْفٌ».
- **Correct:** اسم ليس / خبر ليس, اسم أصبح, اسم لعلّ … ; أَصْبَحَ فعل ماضٍ ناقص مبني على الفتح. (عَسَى and كَادَ are named rightly.)
- **Book:** Iẓhār L33 (the list: «وأصبح وأمسى … وما دام وليس»), L22 for إنّ's sisters.
- **Engine:** `Murib.RULE_OFFICE` L19151–L19155 [19469–19473] (`kanaIsm`, `kanaKhabar`, `innaIsm`, `innaKhabar` are fixed strings).

### B03 · Unsaid (Hadhf) · WRONG — the plain nominal sentence is said to have lost its mubtadaʾ
- **Input:** `زَيْدٌ قَائِمٌ` (also `زَيْدٌ عَالِمٌ`, `بَكْرٌ قَائِمٌ`, `زَيْدٌ مُنْطَلِقٌ`).
- **Shown:** «الْمُبْتَدَأُ مَحْذُوفٌ — هُوَ / هُمْ → زَيْدٌ — مُبْتَدَأٌ مَحْذُوفٌ جَوَازًا — وَصْفٌ لِمَعْلُومٍ».
- **Correct:** nothing is unsaid: زَيْدٌ مبتدأ، قَائِمٌ خبر. (`زَيْدٌ قَائِمٌ فِي الدَّارِ` and `الْعِلْمُ نُورٌ` are rightly left alone.)
- **Book:** Iẓhār, the mubtadaʾ chapter; the Ajurrūmiyya's own example.
- **Engine:** `HadhfEngine` L35140 [35461], rule `mubtadaWasf` L35161 [35482]; `renderHadhfOut` L39029 [39350].

### B04 · Analyzer (Jumla) · WRONG — the mafʿūl li-ajlih is never found
- **Input:** `قَامَ زَيْدٌ إِجْلَالًا لِعَمْرٍو`; `ضَرَبْتُهُ تَأْدِيبًا`.
- **Shown:** إِجْلَالًا «مَفْعُولٌ بِهِ» (the verb قَامَ is intransitive); تَأْدِيبًا «حَالٌ».
- **Correct:** مفعول لأجله in both.
- **Book:** Iẓhār L113 «والرابع المفعول له وهو اسم ما فعل لأجله مضمون عامله»; the Ajurrūmiyya's two examples are these very
  sentences.
- **Engine:** `Murib._decide` (office `mafulLah` exists at L19158 [19476] but is not assigned); `SentenceAnalyzer` L12227.

### B05 · Signs lab · WRONG — verbs are classed as nouns; the lab's own example is one of them
- **Input:** `يَرْمِي` (it stands in the input's placeholder: «كِتَابٌ، مُسْلِمِينَ، أَبُوكَ، الْقَاضِي، يَرْمِي»), `يَكْتُبُونَ`, `تَكْتُبِينَ`,
  `يَضْرِبَانِ`, `يَدْعُو`, `يَسْعَى`, `يَكْتُبُ`, `كَتَبَ`.
- **Shown:** يَرْمِي → «الْمُضَافُ إِلَى يَاءِ الْمُتَكَلِّمِ» (three hidden vowels «لِاشْتِغَالِ الْمَحَلِّ»); يَكْتُبُونَ / تَكْتُبِينَ → «جَمْعُ الْمُذَكَّرِ
  السَّالِمُ» (الواو / الياء); يَضْرِبَانِ → «الْمُثَنَّى»; يَدْعُو → «sound masculine plural, its nūn dropped»; يَسْعَى → «الِاسْمُ الْمَقْصُورُ»;
  يَكْتُبُ → «الْمُفْرَدُ الْمُنْصَرِفُ» with a JARR row; كَتَبَ → the same.
- **Correct:** يَرْمِي: المضارع المعتل الآخر — الضمة مقدرة، الفتحة ظاهرة، الجزم بحذف الآخر; يَكْتُبُونَ / تَكْتُبِينَ / يَضْرِبَانِ: الأفعال الخمسة —
  ثبوت النون / حذفها; كَتَبَ: مبني.
- **Book:** Iẓhār L168 («نحو يضربان ولن يضربا ولم يضربا»), L177–L180 (the weak-ended muḍāriʿ: «يغزو … يخشى»).
- **Engine:** `signWordHtml` L38719 [39040] calls `SignEngine.table(w)` with no part of speech; `SignEngine.classify` L35788 [36109].

### B06 · Dabt lab · WRONG — «ما احسن السماء»
- **Input:** `ما احسن السماء` (bare); and `ما احسنَ السماءَ` (with its endings).
- **Shown:** «ما · احْسُنِ · السماءَ». With the endings typed it still writes «احْسُنِ» and counts the learner's احسنَ as one fault.
- **Correct:** مَا أَحْسَنَ السَّمَاءَ (the verb of wonder).
- **Book:** the taʿajjub chapter (مَا أَفْعَلَهُ); not located verbatim in `research/sources`. The Faces lab reads the same مَا as «مَا التَّعَجُّبِيَّة».
- **Engine:** `DabtEngine` L20488 [20809]; `renderDabtOut` L16582 [16583].

### B07 · Endings (ʿAlāma) lab · WRONG — the jarr sign of every diptote is named «the kasra, written»
- **Input:** `أَحْمَد` (also `فَاطِمَة`, `مَسَاجِد`, `عُمَر`, `إِبْرَاهِيم`, `عُثْمَان`, `حَمْرَاء`, `أَفْضَل`, `مَكَّة`…).
- **Shown:** «جَرًّا: أَحْمَدَ — الْكَسْرَةُ — the kasra — written», while the step text under it says «in jarr it takes a FATHA in
  place of the kasra».
- **Correct:** the form is right; the sign is الفتحة نيابة عن الكسرة.
- **Book:** Iẓhār L162 «والفتحة نصبا وجرا فهو غير المنصرف».
- **Engine:** `AlamaEngine.table` (class L36734 [37055]) — `row.sign` for the mamnūʿ jarr row; `renderAlamaOut` L15155 [15156].

### B08 · Analyzer (Jumla) · WRONG — a hidden doer beside a written one
- **Input:** `جَاءَ الَّذِي قَامَ أَبُوهُ`; `زَيْدٌ قَامَ أَبُوهُ`.
- **Shown:** جَاءَ «وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ جَوَازًا تَقْدِيرُهُ هُوَ», الَّذِي given no office; in the second, قَامَ «الْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ
  جَوَازًا تَقْدِيرُهُ هُوَ» while أَبُوهُ is «وَالظَّاهِرُ أَنَّهُ فَاعِلٌ».
- **Correct:** الَّذِي اسم موصول في محل رفع فاعل جَاءَ; in the second the doer of قَامَ is أَبُوهُ and the clause is the khabar.
- **Book:** Iẓhār L80 (the hidden pronoun stands only where no written doer is); Qawāʿid ch. 4 («لا يذكر الفعل دون فاعله»).
- **Engine:** `Murib` hidden-doer line L19238–L19243 [19556–19561].

### B09 · Analyzer (Jumla) · WRONG — the لَا of prohibition is called a negation
- **Input:** `لَا تَضْرِبْ زَيْدًا`.
- **Shown:** لَا «حَرْفُ نَفْيٍ»; تَضْرِبْ «مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ السُّكُونُ».
- **Correct:** لا الناهية — حرف نهي وجزم (it is what jazms the verb).
- **Book:** Iẓhār L26 «وهي لم ولما … ولام الأمر ولاء النهي للطلب».
- **Engine:** `Murib.term` particle branch L19184 [19502] (`pk === "nafy"`).

### B10 · Order (Tartīb) lab · WRONG — the doer and the object are exchanged, and a forbidden order is passed
- **Input:** `ضَرَبَ زَيْدًا غُلَامُهُ`; `ضَرَبَ غُلَامُهُ زَيْدًا`.
- **Shown:** «doer: زَيْدًا · object: غُلَامُهُ — either order is allowed here»; for the second «doer: غُلَامُهُ · object: زَيْدًا —
  either order is allowed here».
- **Correct:** in the first the doer is غُلَامُهُ and the object MUST come first; the second is not allowed at all.
- **Book:** Kāfiya L427 «ضَرَبَ زَيْدًا غُلاَمُهُ … فاعله، مفعوله راجع ضمير بيتيشديگى زمان», L413 «ضَرَبَ غُلاَمُهُ زَيْداً … لفظا ورتبةً اضمار
  قبل الذكر اولديغندن جائز دگلدر». (`ضَرَبَ الْقَوْمَ أَخُوهُمْ` is read rightly.)
- **Engine:** `TartibEngine.readRows` L36293 [36614]; `renderTartibSentence` L38884 [39205].

### B11 · Order (Tartīb) lab · WRONG — the doer after the object is called «concealed»
- **Input:** `ضَرَبَ عَمْرًا زَيْدٌ`; `خَافَ رَبَّهُ عُمَرُ`.
- **Shown:** «doer: concealed · object: عَمْرًا»; «doer: concealed · object: رَبَّهُ».
- **Correct:** doer زَيْدٌ / عُمَرُ (the object is fronted).
- **Book:** Kāfiya L411 («ضَرَبَ غُلاَمَهُ زَيْدٌ»).
- **Engine:** `TartibEngine.readRows` L36293 [36614].

### B12 · Analyzer (Jumla) · WRONG — the mafʿūl maʿah and the tamyīz after a measure
- **Input:** `سِرْتُ وَالنِّيلَ`; `عِنْدِي رِطْلٌ زَيْتًا`.
- **Shown:** وَالنِّيلَ «وَالظَّاهِرُ أَنَّهُ مَفْعُولٌ بِهِ»; زَيْتًا «حَالٌ».
- **Correct:** مفعول معه (سَارَ is intransitive); تمييز.
- **Book:** Iẓhār L113 «والخامس المفعول معه»; L46 «وبالتنوين إما لفظا نحو رطل زيتا».
- **Engine:** `Murib._decide` (office tables L19151–L19158 [19469–19476]).

### B13 · Analyzer (Jumla) · WRONG — the verb of wonder
- **Input:** `مَا أَحْسَنَ زَيْدًا`.
- **Shown:** مَا «اسْمٌ، مَبْنِيٌّ لَا يَتَغَيَّرُ آخِرُهُ» (no office); أَحْسَنَ «وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ جَوَازًا تَقْدِيرُهُ هُوَ»; no word of taʿajjub.
- **Correct:** مَا التعجبية مبتدأ; أَحْسَنَ فعل ماضٍ للتعجب، فاعله ضمير مستتر وجوبًا يعود على «ما»; the clause is the khabar.
- **Book:** the taʿajjub chapter (its doer is concealed of necessity); not located verbatim in `research/sources`. Iẓhār L80
  defines the two kinds of concealment.
- **Engine:** `Murib` hidden-doer line L19241 [19559].

### B14 · Analyzer (Jumla) · WRONG — the badal and the vocative that resembles a muḍāf
- **Input:** `جَاءَ زَيْدٌ أَخُوكَ`; `يَا طَالِعًا جَبَلًا`.
- **Shown:** أَخُوكَ «مُبْتَدَأٌ»; طَالِعًا «اسْمٌ، مَبْنِيٌّ لَا يَتَغَيَّرُ آخِرُهُ، مُنَادًى», جَبَلًا «مَنْصُوبٌ» with no office.
- **Correct:** أَخُوكَ بدل; طَالِعًا منادى منصوب (شبيه بالمضاف), جَبَلًا مفعول به لاسم الفاعل.
- **Book:** Iẓhār L152 «بدل الكل … نحو جاءني زيد أخوك»; L192–L195 on the vocative.
- **Engine:** `Murib._decide`; the mabnī label L19443 [19761].

### B15 · Analyzer (Jumla) · WRONG — the sentence kind in the header
- **Input:** `إِنْ تَقُمْ أَقُمْ`; `كَمْ كِتَابًا قَرَأْتَ`; `وَاللهِ لَأَقُومَنَّ`.
- **Shown:** «جُمْلَةٌ اسْمِيَّةٌ» for all three; كَمْ and كِتَابًا get no office; وَاللهِ only «اسْمٌ عَلَمٌ».
- **Correct:** verbal sentences (a condition; كَمْ a fronted object with كِتَابًا its tamyīz; an oath with its answer).
- **Book:** Qawāʿid ch. 1, the kinds of sentence (not quoted).
- **Engine:** `renderJumlaOut` L14934 [14935] (header rule, strings at L14865 [14866]).

### B16 · Qawāʿid checker · WRONG — a tick on a broken rule
- **Input:** `عِنْدِي عِشْرُونَ كِتَابٍ`; `خَمْسَةَ عَشَرَ رَجُلًا`; `مَرَرْتُ بِأَحْمَدِ`.
- **Shown:** «✓ كِتَابٍ — الْمُضَافُ إِلَيْهِ مَجْرُورٌ», «2 rules fired — all kept»; «✓ عَشَرَ #2 — الْمُضَافُ إِلَيْهِ…»; «✓ بِأَحْمَدِ — مَا بَعْدَ حَرْفِ
  الْجَرِّ مَجْرُورٌ».
- **Correct:** the tamyīz of 20–90 is manṣūb (كِتَابًا) and عِشْرُونَ with its nūn is no muḍāf; خَمْسَةَ عَشَرَ is a built compound, not an
  iḍāfa; بِأَحْمَدَ.
- **Book:** Iẓhār L46 «وبنون شبه الجمع وهو عشرون إلى تسعين نحو عشرون درهما»; L162 for the diptote.
- **Engine:** `QawaidEngine` L19578 [19899]; `renderQawaidOut` L16670 [16671].

### B17 · Iḍāfa lab · WRONG — manqūṣ and maqṣūr
- **Input:** `قَاضِي` + `الْمَدِينَة`; `قَاضٍ` + `الْمَدِينَة`; `فَتًى` + `الْقَوْم`; `عَصًا` + `مُوسَى`; `دَار` + `الْقَاضِي`.
- **Shown:** «قَاضِيُ الْمَدِينَةِ»; «قَاضُ الْمَدِينَةِ»; «فَتًى الْقَوْمِ»; «عَصًا مُوسَى»; «دَارُ الْقَاضِيِ».
- **Correct:** قَاضِي الْمَدِينَةِ (hidden ḍamma) · فَتَى الْقَوْمِ · عَصَا مُوسَى (the tanwīn must fall) · دَارُ الْقَاضِي.
- **Book:** Iẓhār L177–L180 (the estimated iʿrāb of the manqūṣ and the maqṣūr).
- **Engine:** `IdafaEngine.build` L37285 [37606].

### B18 · Iḍāfa lab · WRONG — the tail that is a diptote or a sound plural
- **Input:** `اِبْن` + `عُمَر`; `كِتَاب` + `فَاطِمَة`; `كِتَاب` + `مُعَلِّمُونَ`.
- **Shown:** «اِبْنُ عُمَرٍ»; «كِتَابُ فَاطِمَةٍ»; «كِتَابُ مُعَلِّمُونٍ».
- **Correct:** اِبْنُ عُمَرَ · كِتَابُ فَاطِمَةَ · كِتَابُ مُعَلِّمِينَ. (`كِتَاب` + `أَحْمَد` → «كِتَابُ أَحْمَدَ» is right.)
- **Book:** Iẓhār L162.
- **Engine:** `IdafaEngine.build` L37285 [37606], tail step L37378 [37699].

### B19 · Iḍāfa lab · WRONG — a refusal with a false reason
- **Input:** `الْحَسَن` + `الْوَجْه`; `الضَّارِب` + `الرَّجُل`; `الضَّارِبَانِ` + `زَيْد`.
- **Shown:** ✕ «لَا يَجْتَمِعُ الْأَلِفُ وَاللَّامُ وَالْإِضَافَةُ — فَلَا يَصِحُّ أَنْ يَكُونَ الْمُضَافُ مُعَرَّفًا بِـ«أَلْ»» — «never by both».
- **Correct:** these are the permitted cases of the lafẓī iḍāfa: الْحَسَنُ الْوَجْهِ، الضَّارِبُ الرَّجُلِ، الضَّارِبَا زَيْدٍ.
- **Book:** Kāfiya L1329 «اَلضَّارِبَا زَيْدٍ، اَلضَّارِبُو زَيْدٍ», L1331 «اَلْحَسَنُ الْوَجْهِ», L1344 «الضَّارِبُ الرَّجُلِ … جائز».
- **Engine:** `IdafaEngine` refusal L37295 [37616].

### B20 · Iḍāfa lab · WRONG — a proper name is called indefinite
- **Input:** `كِتَاب` + `زَيْد` (any proper-name tail).
- **Shown:** the step «الْمُضَافُ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ نَكِرَةٌ فَيُنَوَّنُ».
- **Correct:** زَيْد is a maʿrifa (ʿalam) and takes tanwīn because it is munṣarif, not because it is indefinite.
- **Book:** Iẓhār L168 «والمراد بالمنصرف ما دخله الجر والتنوين نحو زيد».
- **Engine:** `IdafaEngine` tail step L37378 [37699].

### B21 · Vocative (Nidāʾ) lab · WRONG — names and built words are called «muḍāf»
- **Input:** `يَا مُوسَى`, `يَا فَتَى`, `يَا هٰذَا`, `يَا فَاطِمَ`, `يَا حَارِ`.
- **Shown:** «مُنَادًى مُضَافٌ — مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ»; يَا حَارِ → «فَتْحَةٌ مُقَدَّرَةٌ قَبْلَ يَاءِ الْمُتَكَلِّمِ».
- **Correct:** مُوسَى / فَتَى / هٰذَا: منادى مفرد مبني على ضم مقدر في محل نصب; فَاطِمَ / حَارِ: مرخَّم.
- **Book:** Iẓhār L192–L195 (the single definite vocative among the built words).
- **Engine:** `NidaEngine` L31071 [31392]; `renderNidaOut` L15308 [15309].

### B22 · Vocative (Nidāʾ) lab · WRONG — the hamza of calling is not a particle
- **Input:** `أَزَيْدُ`.
- **Shown:** «Start with a particle of calling: يَا، أَيَا، هَيَا، أَيْ، وَا.»
- **Correct:** the hamza is the particle for the near one.
- **Book:** Iẓhār L195 «وحروف النداء يا وأيا وهيا وآ وآي وأي والهمزة، ووا مختص بالندبة».
- **Engine:** `NidaEngine` particle list L31071 [31392]; message L3192.

### B23 · Endings (ʿAlāma) lab · WRONG — the five nouns typed with their wāw
- **Input:** `أَبُو`, `أَخُو`, `حَمُو`, `فُو`, `أُولُو`, `مُعَلِّمُو`.
- **Shown:** «أَبُوٌ / أَبُوًا / أَبُوٍ»; with the muḍāf switch on «أَبُوُ / أَبُوَ / أَبُوِ»; «أُولُوٌ»; «مُعَلِّمُوٌ».
- **Correct:** أَبُو / أَبَا / أَبِي; أُولُو / أُولِي; مُعَلِّمُو / مُعَلِّمِي. (`أَب` and `ذُو` with the muḍāf switch come out right.)
- **Book:** Iẓhār L162.
- **Engine:** `AlamaEngine.table` (class L36734 [37055]).

### B24 · Endings (ʿAlāma) lab · WRONG — the noun annexed to the speaker's yāʾ is read as a manqūṣ
- **Input:** `كِتَابِي`, `غُلَامِي`.
- **Shown:** رفعًا «كِتَابٍ», نصبًا «كِتَابِيَ», جرًّا «كِتَابٍ».
- **Correct:** كِتَابِي in all three, each sign estimated.
- **Book:** Iẓhār L177 «ما أضيف إلى ياء المتكلم … فالكل تقديري نحو غلامي».
- **Engine:** `AlamaEngine.table`.

### B25 · Endings (ʿAlāma) lab · WRONG — two diptotes given tanwīn
- **Input:** `أَشْيَاء`, `أُخَر`.
- **Shown:** «أَشْيَاءٌ / أَشْيَاءً / أَشْيَاءٍ»; «أُخَرٌ / أُخَرًا / أُخَرٍ».
- **Correct:** أَشْيَاءُ / أَشْيَاءَ / أَشْيَاءَ; أُخَرُ / أُخَرَ / أُخَرَ.
- **Book:** Iẓhār L168 onward (the causes that bar tanwīn: the alif of the feminine; ʿadl with description).
- **Engine:** `AlamaEngine.table` (the mamnūʿ test).

### B26 · Endings (ʿAlāma) lab · WRONG — a doubled mark and a false tanwīn on the maqṣūr
- **Input:** `مُوسَى`, `ذِكْرَى`, `مُصْطَفَى`, `كِلَا`, `كِلْتَا`.
- **Shown:** «مُوسًَى», «ذِكْرًَى», «مُصْطَفًَى», «كِلًَا», «كِلْتًَا» (a fatḥa and a tanwīn on one letter).
- **Correct:** مُوسَى and ذِكْرَى take no tanwīn; مُصْطَفًى; كِلَا / كِلْتَا never have it (always annexed).
- **Book:** Iẓhār L92 (the shortened alif of the feminine: «حبلى ودعوى»).
- **Engine:** `AlamaEngine.table` (maqṣūr branch).

### B27 · Endings (ʿAlāma) lab · WRONG — built words are declined
- **Input:** `هٰذَا`, `الَّذِي`, `مَنْ`.
- **Shown:** «هٰذًَا»; naṣb «الَّذِيَ»; «مَنٌْ / مَنًْا / مَنٍْ».
- **Correct:** a refusal: these are mabnī (the Signs lab says so for هٰذَا).
- **Book:** Iẓhār L192 (the list of the built).
- **Engine:** `AlamaEngine.table`; `renderAlamaOut` L15155 [15156].

### B28 · Endings (ʿAlāma) lab · WRONG — قَاضٍ typed as it is written
- **Input:** `قَاضٍ`, `جَوَارٍ`, `لَيَالٍ`.
- **Shown:** «قَاضٌ / قَاضًا / قَاضٍ»; «جَوَارٌ / جَوَارًا»; «لَيَالٌ» — with the root «ق ض ي» printed beside it.
- **Correct:** قَاضٍ / قَاضِيًا / قَاضٍ; جَوَارٍ / جَوَارِيَ / جَوَارٍ. The intro does warn «Hand a manqus over with its ya», but the
  page shows false forms instead of asking, though it knows the root.
- **Book:** Iẓhār L177–L180.
- **Engine:** `AlamaEngine.table`.

### B29 · İʿrāb Shop · WRONG — the fused jarr letter hides the word's class
- **Input:** `مَرَرْتُ بِأَحْمَدَ`; `مَرَرْتُ بِأَبِيكَ`.
- **Shown:** بِأَحْمَدَ — CUSTOMER «الْمُفْرَدُ», FIGURE «الْكَسْرَةُ»; بِأَبِيكَ — CUSTOMER «الْمُفْرَدُ», FIGURE «الْكَسْرَةُ الْمُقَدَّرَةُ … الِاسْتِثْقَالُ».
- **Correct:** غير المنصرف — الفتحة; الأسماء الخمسة — الياء. (`فِي مَسَاجِدَ` and `جَاءَ أَبُوكَ` are fitted rightly.)
- **Book:** Iẓhār L162.
- **Engine:** `IrabShopEngine.table` (class L36969 [37290]).

### B30 · Dabt lab · WRONG — two endings written wrong
- **Input:** `مررت باحمد`; `الحمد لله رب العالمين`.
- **Shown:** «باحمدْ»; «العالمينِ» (and رب left bare).
- **Correct:** بِأَحْمَدَ; الْعَالَمِينَ (the nūn of the sound plural is maftūḥa — `رايت المسلمين` → «المسلمِينَ» is written right).
- **Book:** Iẓhār L162.
- **Engine:** `DabtEngine` L20488 [20809].

### B31 · Kernel · WRONG — single verbs read as nouns
- **Input:** `قُلْ`, `مَدَّ`, `يَرْمِي`, `اِتَّقَى`, `يَكْتُبُونَ`, `قَاضٍ`.
- **Shown:** قُلْ → meaning «قَلَّ — to be few», «الْجَزْمُ بِالسُّكُونِ»; مَدَّ → «إِعْرَابٌ لَفْظِيٌّ بِالْحَرَكَةِ — الْفَتْحَة ظَاهِرَةٌ»; يَرْمِي → «إِعْرَابٌ
  لَفْظِيٌّ — الْكَسْرَة ظَاهِرَةٌ فِي آخِرِهِ»; اِتَّقَى → «اِسْمٌ مَقْصُورٌ»; يَكْتُبُونَ → «جَمْعُ مُذَكَّرٍ سَالِمٌ — الْوَاوُ عَلَامَةُ رَفْعِهِ»; قَاضٍ → «الْكَسْرَة
  ظَاهِرَةٌ».
- **Correct:** قُلْ is the amr of قَالَ, built on the sukūn; مَدَّ a built māḍī; يَرْمِي raised by a hidden ḍamma; اِتَّقَى a verb;
  يَكْتُبُونَ one of the five verbs; قَاضٍ a manqūṣ.
- **Book:** Iẓhār L168, L177–L180.
- **Engine:** `GrammarKernel.ask` L38033 [38354] (the single-word branch); `renderKernelOut` L15101 [15102].

### B32 · Kernel · WRONG — a crash on the sentence of wonder
- **Input:** `مَا أَحْسَنَ زَيْدًا`.
- **Shown:** `TypeError: isVerb is not a function`; the panel keeps what it showed before, and reopening the tab with
  the sentence in the field throws inside `renderLabBody`.
- **Correct:** مَا التعجبية.
- **Book:** — (crash).
- **Engine:** `GrammarKernel.askPhrase` L38186 [38507] → `MaEngine.read` L10661–L10665 (`isVerb` handed a non-function).

### B33 · Kernel · WRONG — a noun is sent to one of the thirty-five doors
- **Input:** `مِيزَان`.
- **Shown:** «بَابُهُ مِنَ الْخَمْسَةِ وَالثَّلَاثِينَ — by rule — 19 — فَعْلَلَ يُفَعْلِلُ فَعْلَلَةً وَفِعْلَالًا · masdar».
- **Correct:** an ism āla on مِفْعَال from و ز ن (its own gloss line above says «ism ala: مِوْزَان → مِيزَان»).
- **Book:** ʿIzzī, the instrument noun.
- **Engine:** `GrammarKernel.ask` L38033 [38354] (the door lookup by surface shape).

### B34 · Faces (Wujūh) lab · WRONG — a written-on wāw is «none of the twenty»
- **Input:** `جَاءَ زَيْدٌ وَعَمْرٌو`; `جَاءَ زَيْدٌ وَالشَّمْسُ طَالِعَةٌ`; `وَاللهِ لَأَفْعَلَنَّ`; `سِرْتُ وَالنِّيلَ`; also `أَيُّهُمْ يَقُمْ أَقُمْ مَعَهُ`.
- **Shown:** «None of the twenty words in this sentence.»
- **Correct:** the wāw is one of the twenty (the intro: «the wāw eight»): عاطفة / حالية / قسم / معية. Arabic never writes it apart,
  so the lab cannot read it at all.
- **Book:** Qawāʿid ch. 3, the wāw (L405 «… وهي الواو الزائدة», the last of its faces).
- **Engine:** `WujuhEngine` L34287 [34608] (token match on the bare word); message `wujuhNone` L2968.

### B35 · Faces (Wujūh) lab · WRONG — the conditional مَا
- **Input:** `مَا تَفْعَلْ أَفْعَلْ`.
- **Shown:** «نَافِيَة — negating — it opens its clause and a verb follows».
- **Correct:** شرطية (two majzūm verbs).
- **Book:** Qawāʿid ch. 3, مَا; Iẓhār L26 (ما among the words that jazm two verbs).
- **Engine:** `MaEngine.read` L10661 (class L10592).

### B36 · Faces (Wujūh) lab · WRONG — a reason that is not in the sentence
- **Input:** `مَنْ قَامَ`; `مَا عِنْدَكَ`.
- **Shown:** مَنْ → «شَرْطِيَّة … (فَ or a second majzūm) — the condition «whoever»»; مَا → «نَافِيَة» flat.
- **Correct:** مَنْ قَامَ has neither a فَ nor a majzūm: استفهام or موصولة; مَا عِنْدَكَ is as likely استفهام or موصولة.
- **Book:** Qawāʿid ch. 3, مَنْ and مَا.
- **Engine:** `WujuhEngine` L34287 [34608]; `MaEngine.read` L10661.

### B37 · Order (Tartīb) lab · WRONG — the pear eats Mūsā
- **Input:** `أَكَلَ الْكُمَّثْرَى مُوسَى`.
- **Shown:** «doer: الْكُمَّثْرَى · object: مُوسَى — لَبْسُ الْإِعْرَابِ وَالْقَرِينَةِ».
- **Correct:** the meaning is the qarīna, so there is no ambiguity: doer مُوسَى, the order is free.
- **Book:** Kāfiya L419 «اَكَلَ الْكُمَّثْرَى يَحْيىَ مثالنده فاعلنك يَحْيىَ اولديغنه دلالت ايدن معنوى قرينه».
- **Engine:** `TartibEngine.readRows` L36293 [36614].

### B38 · Order (Tartīb) lab · WRONG — «equal in generality» said of a name and an indefinite
- **Input:** `زَيْدٌ قَائِمٌ`; `قَائِمٌ زَيْدٌ`; `إِنَّمَا زَيْدٌ قَائِمٌ`; `لَزَيْدٌ قَائِمٌ`; `زَيْدًا ضَرَبْتُ`.
- **Shown:** «مُتَسَاوِيَانِ فِي الْعُمُومِ وَالْخُصُوصِ» for the first, third and fourth; قَائِمٌ زَيْدٌ → «mubtadaʾ: قَائِمٌ · khabar: زَيْدٌ»;
  زَيْدًا ضَرَبْتُ → «mubtadaʾ: زَيْدًا · khabar: ضَرَبْتُ».
- **Correct:** in زَيْدٌ قَائِمٌ the order is free (قَائِمٌ زَيْدٌ is a fronted khabar); the reasons in the third and fourth are the
  ḥaṣr and the lām's ṣadāra; زَيْدًا is a fronted object.
- **Book:** Kāfiya, the mubtadaʾ chapter (the rule is for two definites or two equals, with the stock example
  أَفْضَلُ مِنْكَ أَفْضَلُ مِنِّي; not found verbatim in the app's Kāfiya digests).
- **Engine:** `TartibEngine.readRows` L36293 [36614].

### B39 · Pause (Waqf) lab · WRONG — Iẓhār's line is applied to words it excludes
- **Input:** `ضَرَبَ`, `بِهِ`, `هُوَ`, `يَعْلَمُونَ`, `مُسْلِمُونَ`.
- **Shown:** «أَحْوَالُهُ الثَّلَاثُ تَقْدِيرِيَّةٌ (الْمَوْقُوفُ عَلَيْهِ بِلَا تَنْوِينِ التَّمَكُّنِ أَوْ بِتَاءِ التَّأْنِيثِ)».
- **Correct:** the first three are built; the last two are declined by letters, and their sign stays spoken in pause.
- **Book:** Iẓhār L183 «والسابع الموقوف عليه بالإسكان مما كان إعرابه بالحركة».
- **Engine:** `WaqfEngine` L31008 [31329], string L31021 [31342]; `renderWaqfOut` L15297 [15298].

### B40 · Pause (Waqf) lab · WRONG — the maqṣūr
- **Input:** `فَتًى`, `هُدًى`, `عَصًا`.
- **Shown:** «تَنْوِينُ النَّصْبِ يُبْدَلُ أَلِفًا» and «رَفْعُهُ وَجَرُّهُ تَقْدِيرِيٌّ دُونَ نَصْبِهِ».
- **Correct:** the tanwīn of a maqṣūr is not a naṣb tanwīn, and all three of its cases are estimated, in connected speech
  and in pause.
- **Book:** Iẓhār L177 (the maqṣūr among the wholly estimated).
- **Engine:** `WaqfEngine` L31008 [31329].

### B41 · Unsaid (Hadhf) · WRONG — أَهْلًا is called a mafʿūl muṭlaq
- **Input:** `أَهْلًا وَسَهْلًا`.
- **Shown:** «أَتَيْتَ → أَهْلًا — مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ».
- **Correct:** مفعول به لفعل محذوف (the lab supplies the right verb — أَتَيْتَ — and the wrong office: أَهْل is no maṣdar of أَتَى).
- **Book:** Kāfiya L756 «اَهْلاً وَسَهْلاً: اصلنده؛ اَتَيْتَ اَهْلاً», in the mafʿūl bihi chapter.
- **Engine:** `HadhfEngine` L35140 [35461].

### B42 · Inna lab · WRONG — the reason given after the wāw of ḥāl
- **Input:** `جِئْتُ وَإِنَّ زَيْدًا قَائِمٌ`.
- **Shown:** «إِنَّ — مَكْسُورَةٌ ✓ — فِي الْخَبَرِ عَنِ اسْمِ عَيْنٍ».
- **Correct:** the verdict is right, the seat is «بعد واو الحال».
- **Book:** Iẓhār L22 «… بعد واو الحال نحو قوله تعالى وإن فريقا من المؤمنين لكارهون».
- **Engine:** `InnaEngine` L36358 [36679], seat label L36363 [36684].

### B43 · Signs lab · WRONG — قَاضٍ and ذُو مَالٍ
- **Input:** `قَاضٍ`; `ذُو مَالٍ`.
- **Shown:** both «الْمُفْرَدُ الْمُنْصَرِفُ وَجَمْعُ التَّكْسِيرِ» with spoken ḍamma / fatḥa / kasra.
- **Correct:** المنقوص (the lab has the row for الْقَاضِي); الأسماء الخمسة (it has the row for أَبُوكَ).
- **Book:** Iẓhār L162, L177.
- **Engine:** `SignEngine.classify` L35788 [36109].

### B44 · Qawāʿid checker · WRONG — arcs in the iʿrāb map
- **Input:** `ضَرَبْتُ زَيْدٌ`; `رَأَيْتُ الْمُسْلِمُونَ`; `كَانَ زَيْدٌ قَائِمًا`.
- **Shown:** an arc «فَاعِلُهُ» to زَيْدٌ / الْمُسْلِمُونَ though the verb's تُ is its doer; under كَانَ the arcs «فَاعِلُهُ» and «مَفْعُولُهُ»
  beside «اسْمُهَا».
- **Correct:** no second doer; كَانَ has an ism and a khabar, no fāʿil and no mafʿūl.
- **Book:** Iẓhār L33.
- **Engine:** the map drawn in `renderQawaidOut` L16670 [16671] / `renderJumlaOut` L14934 [14935] from `SentenceAnalyzer.analyze`.

### B45 · Iḍāfa lab · WRONG — a pronoun typed as the tail
- **Input:** `أَخُو` + `هُوَ`; `غُلَام` + `ي`; `غُلَام` + `أَنَا`; `اِثْنَانِ` + `هُمْ`; `أَب` + `ي`.
- **Shown:** «أَخُوُ هُوٍ»; «غُلَامُ يِ»; «غُلَامُ أَنَا»; «اِثْنَا هُمِْ»; «أَبُو يِ».
- **Correct:** أَخُوهُ · غُلَامِي · أَبِي — or a refusal pointing to the Pronoun lab.
- **Book:** —.
- **Engine:** `IdafaEngine.build` L37285 [37606].

### B46 · Analyzer (Jumla) · WRONG — «nothing here governs anything»
- **Input:** `ضَرَبَ زَيْدٌ عَمْرًا`.
- **Shown:** under a map that draws «فَاعِلُهُ» and «مَفْعُولُهُ»: «No rule fires on this — nothing here governs anything.» The gloss
  line reads عَمْرًا as «life — the form kept for oaths».
- **Correct:** the verb governs both nouns; عَمْرًا is the name ʿAmr in the naṣb.
- **Book:** Iẓhār L149 «ضرب زيد عمرا».
- **Engine:** string L3229 (shown by the ledger when `QawaidEngine` L19578 [19899] has no rule for the sentence).

### B47 · Analyzer (Jumla) · MISLEADING — «built, its ending never changes» for the vocative and for لَا's noun
- **Input:** `يَا زَيْدُ`; `يَا رَجُلُ`; `لَا رَجُلَ فِي الدَّارِ`; `لَا إِلٰهَ إِلَّا اللهُ`.
- **Shown:** «اسْمٌ، مَبْنِيٌّ لَا يَتَغَيَّرُ آخِرُهُ، مُنَادًى» / «… اسْمُ لَا النَّافِيَةِ لِلْجِنْسِ».
- **Correct:** مبني على الضم في محل نصب; مبني على الفتح في محل نصب — the word is declinable everywhere else.
- **Book:** Iẓhār L195 (both listed among the non-inherent buildings).
- **Engine:** `Murib.line`, the mabnī label L19443 [19761].

### B48 · Kernel · MISLEADING — «the corpus's own iʿrāb» of another sentence
- **Input:** `ضَرَبَ زَيْدٌ عَمْرًا`; `فِي الدَّارِ`.
- **Shown:** «إِعْرَابُ الْمُدَوَّنَةِ · The corpus's own i'rab» followed by the parsing of a longer sentence that merely quotes the
  phrase («وَيَعْمَلُ — الْوَاوُ عَاطِفَةٌ … عَمَلَ فِعْلِهِ … مَاضِيًا كَانَ أَوْ غَيْرَهُ …»; for the second «وَيَجُوزُ …»).
- **Correct:** the lines of the typed words only, or a note that the phrase was found inside another sentence.
- **Book:** —.
- **Engine:** `GrammarKernel.askPhrase` L38186 [38507].

### B49 · Analyzer (Jumla) · MISSING — no case and no sign for the dual and the manqūṣ
- **Input:** `جَاءَ الزَّيْدَانِ`; `الزَّيْدَانِ يَقُومَانِ`; `رَأَيْتُ الْقَاضِيَ`.
- **Shown:** «اسْمٌ، وَالظَّاهِرُ أَنَّهُ فَاعِلٌ»; «اسْمٌ، مُبْتَدَأٌ»; «اسْمٌ، وَالظَّاهِرُ أَنَّهُ مَفْعُولٌ بِهِ».
- **Correct:** مرفوع وعلامة رفعه الألف لأنه مثنى; منصوب وعلامة نصبه الفتحة الظاهرة. (الزَّيْدُونَ / الزَّيْدَيْنِ do get «بِالْحُرُوفِ».)
- **Book:** Iẓhār L162.
- **Engine:** `Murib.line` L19393 [19711].

### B50 · Analyzer (Jumla) · MISSING — the tawkīd and other offices left unsaid
- **Input:** `جَاءَ الْقَوْمُ كُلُّهُمْ`; `جَاءَ زَيْدٌ نَفْسُهُ`; `قَرَأْتُ الْكِتَابَ كُلَّهُ`; `هٰذَا كِتَابٌ`; `صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ`.
- **Shown:** كُلُّهُمْ / نَفْسُهُ / كُلَّهُ — the case and «وَالضَّمِيرُ مُضَافٌ إِلَيْهِ», no office; هٰذَا no office; عَلَيْهِ «حَرْفٌ لَا مَحَلَّ لَهُ».
- **Correct:** توكيد; هٰذَا مبتدأ; عَلَى حرف جر والهاء في محل جر.
- **Book:** Iẓhār L149 «والثالث التأكيد»; Qawāʿid ch. 4 («لا يذكر المبتدأ دون خبره»).
- **Engine:** `Murib._decide` / `Murib.line` L19393 [19711].

### B51 · Qawāʿid checker · MISSING — «all kept» on broken sentences
- **Input:** `كَانَ زَيْدٌ قَائِمٌ`; `يَا عَبْدُ اللهِ`; `غُلَامُ زَيْدٌ`; `رَأَيْتُ الْمُسْلِمُونَ`; `ضَرَبْتُ زَيْدٌ`; `مَرَرْتُ بِأَبُوكَ`; `جَاءَ أَبَاكَ`.
- **Shown:** the first two: «1 / 2 rules fired — all kept.»; the rest: no ledger at all.
- **Correct:** a cross on the khabar of كَانَ, on the annexed vocative, on the muḍāf ilayh, on the object in the rafʿ, on the
  five nouns' letter. The intro promises «every nahw rule the sentence must keep … a cross where it broke it»; only
  the six seeded kinds (jarr, iḍāfa with ال on both, jazm, naṣb, inna's noun) are checked.
- **Book:** Iẓhār L33, L162, L195.
- **Engine:** `QawaidEngine.RULES` (class L19578 [19899]).

### B52 · Order (Tartīb) lab · MISSING — the Kāfiya's own examples are not read
- **Input:** `أَيْنَ زَيْدٌ`; `مَنْ أَبُوكَ`; `كَمْ مَالُكَ`; `مَا زَيْدٌ إِلَّا قَائِمٌ`; `أَفْضَلُ مِنْكَ أَفْضَلُ مِنِّي`; `مَنْ ضَرَبْتَ`.
- **Shown:** «no doer-object or mubtadaʾ-khabar pair found».
- **Correct:** the obligatory orders these sentences are quoted for (the khabar with ṣadāra, the ḥaṣr, the two equals).
- **Book:** Kāfiya L569 «اَيْنَ زَيْدٌ».
- **Engine:** `TartibEngine.readRows` L36293 [36614].

### B53 · Inna lab · MISSING — the word must already carry the answer
- **Input:** `علمت ان زيدا قائم`; `قلت انك قائم`; `أن زيدا قائم`; `عَلِمْتُ اَنَّ زَيْدًا قَائِمٌ` (the Ottoman spelling of the app's own sources).
- **Shown:** «No إِنَّ / أَنَّ in this sentence.»
- **Correct:** the seat decides: مفتوحة after عَلِمْتُ, مكسورة after the saying. The lab that rules on kasr and fatḥ reads only a
  hamza already written with its vowel.
- **Book:** Iẓhār L22.
- **Engine:** `InnaEngine` L36358 [36679] (token test).

### B54 · Unsaid (Hadhf) · MISSING — the ikhtiṣāṣ with أَيَّتُهَا
- **Input:** `اللَّهُمَّ اغْفِرْ لَنَا أَيَّتُهَا الْعِصَابَةُ`.
- **Shown:** nothing unsaid.
- **Correct:** أَخُصُّ, as the lab answers for `أَنَا أَفْعَلُ كَذَا أَيُّهَا الرَّجُلُ` and `نَحْنُ الْعَرَبَ…`.
- **Book:** the lab's own intro («the «I single out» of أَيُّهَا الرَّجُلُ»).
- **Engine:** `HadhfEngine` L35140 [35461].

---

# C · The rest (balāgha and the reading tools)

### C01 · Model lab · WRONG — full certainty on false roles for the grammar books' everyman
- **Input:** `قَامَ زَيْدٌ`; `ضَرَبَ زَيْدٌ عَمْرًا`; `فَتَحَ زَيْدٌ الْبَابَ`; `رَأَيْتُ زَيْدًا`; `مَرَرْتُ بِزَيْدٍ`; `كَانَ زَيْدٌ قَائِمًا`; `كِتَابُ زَيْدٍ جَدِيدٌ`;
  `إِنَّ زَيْدًا قَائِمٌ`.
- **Shown:** زَيْدٌ «الْخَبَر · khabar %100» (after قَامَ, فَتَحَ and كَانَ), «khabar %99» (after ضَرَبَ); زَيْدًا «khabar %98» after رَأَيْتُ;
  بِزَيْدٍ «khabar %100»; كِتَابُ «الْفَاعِل · fa'il %98»; under إِنَّ, زَيْدًا «الْحَال · hal / zarf / tamyiz %58» (with «governor's class:
  inna» among its own evidence chips); قَائِمًا after كَانَ «hal %78».
- **Correct:** فاعل · فاعل · فاعل · مفعول به · مجرور · اسم كان · مبتدأ · اسم إنّ — each settled by the Analyzer's rules. Other nouns in
  the same seats are read rightly (`جَاءَ الْمُعَلِّمُ` → fa'il %97; `قَرَأَ الطَّالِبُ الْكِتَابَ` → fa'il %77, maf'ul %100), so the fault
  follows the word زَيْد with its tanwīn — the one word every teacher types. The intro says the model «only votes where
  the rules cannot».
- **Book:** Iẓhār L149 «ضرب زيد عمرا» and the first example of every chapter.
- **Engine:** `renderModelOut` L15639 [15640]; `IrabModel` L11331.

### C02 · Understand (Fahm) · WRONG — the first person is read as the second
- **Input:** `رَأَيْتُ أَسَدًا فِي الْحَمَّامِ`; `جَاءَ الرَّجُلُ الَّذِي أَكْرَمْتُهُ` (the ḍamma is typed).
- **Shown:** «You saw a lion…» / TR «… gördün»; «… one who you honoured him» / TR «… ikram ettin».
- **Correct:** I saw; whom I honoured.
- **Book:** ʿIzzī, the māḍī table (تُ for the speaker).
- **Engine:** `FahmEngine` L16302 [16303]; `renderFahmOut` L16551 [16552].

### C03 · Understand (Fahm) · WRONG — two stock sentences
- **Input:** `ما احسن السماء`; `ضرب زيد عمرا`.
- **Shown:** «He did not be good the heaven.» · NOMINAL SENTENCE · «احْسُنِ an amr is built on the sukun»; «Zayd struck a life.» /
  TR «Zeyd ömür vurdu». (Also فِي الْحَمَّامِ → «in the one who catches a fever much».)
- **Correct:** «How fair the sky is!» (the same root fault as B06); «Zayd struck ʿAmr».
- **Book:** Iẓhār L149 «ضرب زيد عمرا».
- **Engine:** `FahmEngine` L16302 [16303] over `DabtEngine` L20488 [20809].

### C04 · Tashbīh lab · WRONG — the middle rank is called the lowest
- **Input:** `زَيْدٌ أَسَدٌ فِي الشَّجَاعَةِ`; `هُوَ بَحْرٌ فِي الْجُودِ`.
- **Shown:** «أَدْنَى الْمَرَاتِبِ — بِلَا أَدَاةٍ».
- **Correct:** مُتَوَسِّطُ الْمَرَاتِبِ — one of the two (the particle or the point of likeness) is dropped. The lab's own label defines
  the lowest as «adat and wajh both spoken».
- **Book:** Talkhīṣ `talkhis-al-miftah-balagha.txt` L3435–L3436 «متوسط مرتبه سى … ادات تشبيه و وجه شبه دن برى حذف اولونان تشبيه در.
  مثلا؛ زَيْدٌ كَالاَسَدِ ويا زَيْدٌ اَسَدٌ فِى الشَّجَاعَةِ».
- **Engine:** `TashbihEngine` L26853 [27174], rank labels L26894 [27215]; `renderTashbihOut` L28190 [28511].

### C05 · Kināya lab · WRONG — the book's far kināya is called near
- **Input:** `زَيْدٌ كَثِيرُ الرَّمَادِ`.
- **Shown:** «قَرِيبَةٌ · near» (no rung on the ladder).
- **Correct:** بَعِيدَة — the mind passes through the burning, the cooking, the guests.
- **Book:** Talkhīṣ L3907–L3909 «اگر انتقال واسطه ايله اولورسه بو كنايه بعيده در. مثلا … كَثيِرُ الرَّمَادْ»; L3902 gives طَوِيلُ النِّجَادِ as the
  near one.
- **Engine:** `KinayaEngine` L28676 [28997] (label L28685 [29006]); `renderKinayaOut` L28149 [28470].

### C06 · Badīʿ lab · WRONG — the textbook jinās tāmm is called a ṭibāq of negation
- **Input:** `وَيَوْمَ تَقُومُ السَّاعَةُ يُقْسِمُ الْمُجْرِمُونَ مَا لَبِثُوا غَيْرَ سَاعَةٍ`.
- **Shown:** «السَّاعَةُ ⇄ سَاعَةٍ — طِبَاقٌ — طِبَاقُ السَّلْبِ — اسْمَانِ — settled by the surface alone» (a jinās line stands beside it).
- **Correct:** الجناس التام only. Ṭibāq al-salb is one verb affirmed and negated — as the lab rightly answers for
  `لَا يَعْلَمُونَ يَعْلَمُونَ` and `فَلَا تَخْشَوُا النَّاسَ وَاخْشَوْنِ`.
- **Book:** Talkhīṣ, the badīʿ chapter (the verse is its example of the complete jinās).
- **Engine:** `BadiEngine` L29042 [29363], ṭibāq al-salb L29100 [29421]; `renderBadiOut` L28100 [28421].

### C07 · ʿArūḍ lab · WRONG — a foot shown with a letter removed
- **Input:** `بَانَتْ سُعَادُ فَقَلْبِي الْيَوْمَ مَتْبُولُ ✽ مُتَيَّمٌ إِثْرَهَا لَمْ يُفْدَ مَكْبُولُ`.
- **Shown:** baḥr «الْبَسِيط» (right), first foot «بَنَتْ سُعَا — مُتَفْعِلُنْ — //○//○».
- **Correct:** «بَانَتْ سُعَا — مُسْتَفْعِلُنْ — /○/○//○» (the alif of بَانَتْ is a still letter).
- **Book:** —.
- **Engine:** `ArudEngine` L30403 [30724]; `renderArudOut` L28091 [28412].

### C08 · Majāz lab · MISLEADING — «the literal reading stands»
- **Input:** `بَنَى الْأَمِيرُ الْمَدِينَةَ`; `نَهَارُهُ صَائِمٌ`; `عِيشَةٌ رَاضِيَةٌ`; `يَجْعَلُونَ أَصَابِعَهُمْ فِي آذَانِهِمْ`.
- **Shown:** «no majaz the surface can point at — the literal reading stands».
- **Correct:** the first three are the stock examples of the majāz ʿaqlī, the fourth of the whole for the part. «The engine
  finds none» would be true; «the literal reading stands» is not.
- **Book:** Talkhīṣ, the majāz ʿaqlī.
- **Engine:** `MajazEngine` L27531 [27852]; message L3269.

### C09 · Learning lab · MISLEADING — a guess against the app's own table
- **Input:** roots `حسن`, `كرم`, `سمع`.
- **Shown:** حسن → «ضَرَبَ يَضْرِبُ 32 % · سَمِعَ يَسْمَعُ 27 %»; كرم → «ضَرَبَ 40 % · نَصَرَ 28 %»; سمع → «فَتَحَ 50 % · سَمِعَ 23 %».
- **Correct:** حَسُنَ and كَرُمَ are the model verbs of bāb 5 (the Sarf lab auto-picks حسن I/5); the right bāb is not even second.
  The panel is labelled a guess («57 % held-out»), but it guesses where the tables already know.
- **Book:** ʿIzzī L17 «حَسُنَ يَحْسُنُ».
- **Engine:** `BabModel.badge` L30704 [31025]; `renderLearnOut` L28116 [28437].

### C10 · Kināya lab · MISSING — the same shape, unread
- **Input:** `زَيْدٌ جَبَانُ الْكَلْبِ`; `زَيْدٌ مَهْزُولُ الْفَصِيلِ`; `هِيَ نَؤُومُ الضُّحَى`; `فُلَانٌ طَاهِرُ الذَّيْلِ`; `هُوَ نَقِيُّ الثَّوْبِ`.
- **Shown:** «no kinaya the shape can point at — the wording is taken as it stands».
- **Correct:** each is «a quality annexed to a thing», the shape the intro names (and كَثِيرُ / طَوِيلُ / عَرِيضُ are read).
- **Book:** Talkhīṣ, the kināya chapter.
- **Engine:** `KinayaEngine` L28676 [28997].

### C11 · Badīʿ lab · MISSING — the complete jinās between identical words
- **Input:** `صَلَّيْتُ الْمَغْرِبَ فِي الْمَغْرِبِ`; `يَحْيَى لِيَحْيَا`.
- **Shown:** «no jinas the letters can show».
- **Correct:** الجناس التام.
- **Book:** Talkhīṣ, the jinās.
- **Engine:** `BadiEngine` L29042 [29363].

### C12 · ʿArūḍ lab · MISSING — sound lines get «no baḥr»
- **Input:** `أَنَا الْبَحْرُ فِي أَحْشَائِهِ الدُّرُّ كَامِنٌ ✽ فَهَلْ سَاءَلُوا الْغَوَّاصَ عَنْ صَدَفَاتِي`; the Alfiyya's opening
  `كَلَامُنَا لَفْظٌ مُفِيدٌ كَاسْتَقِمْ ✽ وَاسْمٌ وَفِعْلٌ ثُمَّ حَرْفٌ الْكَلِمْ`.
- **Shown:** «no baḥr the engine knows consumes this line — the units are shown as read».
- **Correct:** الطويل (أَنَا scans as أَنَ in connected speech); الرجز (حَرْفٌ الْ = حَرْفُنِ لْ — the tanwīn is not given its kasra
  before the waṣl, so the units show two still letters together, «o o»).
- **Book:** —.
- **Engine:** `ArudEngine` L30403 [30724] (the cutting rules listed under the output).

---

# Tools audited

A58 touches two tools and is listed under both; the table therefore sums to one more than the count of entries.

| # | Tool (id) | Group | Inputs tried | Findings |
|---|---|---|---|---|
| 1 | Sarf (`sarf`) | sarf | ≈290 root × form cells: sound, mithāl, ajwaf, nāqiṣ, doubled, 4-letter; Forms I (six bābs)–XIII; 17 roots typed in the field | 14 (11 W · 2 Ml · 1 Ms): A03, A06, A13, A14, A35, A36, A37, A38, A40, A46, A47, A49, A50, A56 |
| 2 | 35 doors (`bab35`) | sarf | all 35 doors (model, card, re-derivation) | 1 (1 W · 0 Ml · 0 Ms): A39 |
| 3 | Numbers Lab (`adad`) | sarf | 50 figures (1–9999) × 6 nouns, masc. and fem. | 0 — clean |
| 4 | Root Finder (`jadhr`) | sarf | 75 words: verbs in every cell, participles, maṣdars, plurals, clitics | 7 (5 W · 1 Ml · 1 Ms): A04, A11, A43, A44, A48, A51, A58 |
| 5 | Mizan (`mizan`) | sarf | 38 words | 6 (3 W · 2 Ml · 1 Ms): A10, A12, A45, A52, A53, A58 |
| 6 | Tasgir · Nisba (`ism`) | sarf | 75 nouns (diminutive, nisba), 27 roots (superlative, time/place, instrument), 21 nouns (dual and plurals) | 10 (10 W · 0 Ml · 0 Ms): A07, A08, A09, A25, A26, A27, A28, A29, A33, A34 |
| 7 | Maqṣūd (`maqsud`) | sarf | 18 model roots, 1,922 cells; the 141 non-green cells read | 1 (1 W · 0 Ml · 0 Ms): A42 |
| 8 | Pronouns (`damir`) | sarf | 37 hosts × 14 pronouns; 17 words read back | 1 (1 W · 0 Ml · 0 Ms): A24 |
| 9 | Hamza (`hamza`) | sarf | 70 words | 0 — clean |
| 10 | Derivation (`isht`) | sarf | 57 derived nouns | 4 (3 W · 1 Ml · 0 Ms): A30, A31, A32, A55 |
| 11 | I'lal (`ilal`) | sarf | 26 roots × 7 shapes | 9 (9 W · 0 Ml · 0 Ms): A01, A05, A15, A16, A17, A18, A19, A20, A21 |
| 12 | Sarf ledger (`sledger`) | sarf | 16 verbs | 5 (2 W · 1 Ml · 2 Ms): A22, A23, A54, A59, A60 |
| 13 | Tawkīd nūn (`tawkid`) | sarf | 36 verbs and emphatic forms | 3 (2 W · 0 Ml · 1 Ms): A02, A41, A57 |
| 14 | Analyzer (`jumla`) | nahw | 90 sentences (the standard examples of each chapter) | 13 (10 W · 1 Ml · 2 Ms): B01, B02, B04, B08, B09, B12, B13, B14, B15, B46, B47, B49, B50 |
| 15 | Endings (`alama`) | nahw | 60 nouns × 3 cases, 9 more with the switches | 7 (7 W · 0 Ml · 0 Ms): B07, B23, B24, B25, B26, B27, B28 |
| 16 | İ'rab Shop (`irabshop`) | nahw | 16 sentences | 1 (1 W · 0 Ml · 0 Ms): B29 |
| 17 | Inna (`inna`) | nahw | 36 sentences | 2 (1 W · 0 Ml · 1 Ms): B42, B53 |
| 18 | Faces (`wujuh`) | nahw | 43 sentences | 3 (3 W · 0 Ml · 0 Ms): B34, B35, B36 |
| 19 | Unsaid (`hadhf`) | nahw | 40 sentences | 3 (2 W · 0 Ml · 1 Ms): B03, B41, B54 |
| 20 | Signs (`sign`) | nahw | 25 words | 2 (2 W · 0 Ml · 0 Ms): B05, B43 |
| 21 | Order (`tartib`) | nahw | 28 sentences | 5 (4 W · 0 Ml · 1 Ms): B10, B11, B37, B38, B52 |
| 22 | Idafa (`idafa`) | nahw | 40 head + tail pairs, three cases | 5 (5 W · 0 Ml · 0 Ms): B17, B18, B19, B20, B45 |
| 23 | Vocative (`nida`) | nahw | 30 calls | 2 (2 W · 0 Ml · 0 Ms): B21, B22 |
| 24 | Pause (`waqf`) | nahw | 33 words | 2 (2 W · 0 Ml · 0 Ms): B39, B40 |
| 25 | Kernel (`kernel`) | nahw | 15 words and sentences | 4 (3 W · 1 Ml · 0 Ms): B31, B32, B33, B48 |
| 26 | Qawaid (`qawaid`) | nahw | 22 sentences (10 sound, 12 with one fault) | 3 (2 W · 0 Ml · 1 Ms): B16, B44, B51 |
| 27 | Dabt (`dabt`) | nahw | 20 bare sentences | 2 (2 W · 0 Ml · 0 Ms): B06, B30 |
| 28 | Tashbih (`tashbih`) | balagha | 15 likenings | 1 (1 W · 0 Ml · 0 Ms): C04 |
| 29 | Majaz (`majaz`) | balagha | 16 sentences | 1 (0 W · 1 Ml · 0 Ms): C08 |
| 30 | Kinaya (`kinaya`) | balagha | 12 phrases | 2 (1 W · 0 Ml · 1 Ms): C05, C10 |
| 31 | Badiʿ (`badi`) | balagha | 15 lines | 2 (1 W · 0 Ml · 1 Ms): C06, C11 |
| 32 | ʿArūḍ (`arud`) | balagha | 13 bayts | 2 (1 W · 0 Ml · 1 Ms): C07, C12 |
| 33 | Model (`model`) | fahm | 17 sentences | 1 (1 W · 0 Ml · 0 Ms): C01 |
| 34 | Etiquette (`adab`) | fahm | no input; 9 rule cards read | 0 |
| 35 | Understand (`fahm`) | fahm | 12 sentences | 2 (2 W · 0 Ml · 0 Ms): C02, C03 |
| 36 | Q&A (`sual`) | fahm | 13 banks (550 items); 6 read | 0 |
| 37 | Learning (`learn`) | fahm | 18 roots | 1 (0 W · 1 Ml · 0 Ms): C09 |

# Not auditable (or only in part)

- **Etiquette (adab).** No input of its own: nine rule cards from Qawāʿid al-Iʿrāb ch. 4 and a lint of the corpus.
  The nine statements were read against the chapter and stand; the lint counts were not re-derived.
- **Q&A (sual).** A browser over 13 banks (550 questions) of the books' own wording. Six items were read; the bank
  is book text, not engine output, and was not audited question by question.
- **Maqṣūd lab.** Audited as a comparison only: of 1,922 cells, the 141 that are not green were read one by one
  (22 red, 119 amber). The green cells show the book's text and the engine agreeing; a slip shared by both would not
  show.
- **Learning lab.** Only the bāb guess takes input (18 roots tried). The other two statistical panels run on the
  corpus and print their own held-out scores; those scores were not re-measured.
- **Sarf lab — hamzated and doubly-weak roots.** Refused outright («Hamzated and doubly-weak roots are beyond letter
  substitution…»). That is a refusal with a reason, so it is not a finding — but the owner should know that no mahmūz
  (أَخَذَ، سَأَلَ، قَرَأَ، رَأَى، أَتَى، جَاءَ) and no lafīf (وَقَى، طَوَى، وَلِيَ، حَيِيَ) can be conjugated in the lab at all, in any Form.
  The passive and the Form I maṣdar are likewise not generated, by design.
- **Stored paradigms.** Tools that read the corpus tables (Tawkīd, Root Finder, Mizan, Sarf ledger) were tried only
  on a few dozen verbs; A41 shows the tables themselves carry spelling faults for hamza-final verbs. A full sweep of
  the stored tables was outside this audit.

# Candidates from the earlier notes that were dropped

- **«نَصْبِرَ → اِنْفَعَلَ» (Root Finder)** — did not reproduce: نَصْبِرَ is answered «الْمُضَارِعُ — we» of صَبَرَ.
- **«إِذْ إِنَّ → خبرا عن اسم معنى» (Inna)** — did not reproduce: the lab says «يَجُوزُ الْوَجْهَانِ — لَا قَرِينَةَ».
- **«حَيْثُ إِنَّ marked ✗» (Inna)** — not a finding: Iẓhār L22 itself has «ومضافا إليها نحو اجلس حيث أن زيدا جالس».
- **«اِذَّكَرَ for اِدَّكَرَ» (Sarf)** — not a finding: ʿIzzī L105 as carried in the app reads «ادَّرَأَ وَاذَّكَرَ وَازْدَجَرَ».
- **Mechanical Form VII forms (اِنْنَصَرَ، اِنْرَمَى)** — not a finding in themselves: the naql tables recite them
  (`bablara-nakil-tablosu.txt` L6, Maqṣūd L831 «اِنْوَعَدَ»). Only the inconsistent spelling is kept (A50).
- **«أَضْحَكَ وَأَبْكَى no ṭibāq» (Badīʿ)** — not a finding: the labelled shortlist offers «طِبَاقٌ».
- **«قَدْ قَامَ زَيْدٌ → لِلتَّوَقُّعِ» (Faces)** — left out: a defensible face (Qawāʿid L371), shown with the full list.
- **Hamza lab** — 70 words, every verdict consistent with the matn's five rules; nothing to report.
- **Numbers lab** — 50 figures from 1 to 9999 with six nouns of both genders; nothing to report.
