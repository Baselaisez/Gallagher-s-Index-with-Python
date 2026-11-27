"""Author content/samples/mathal-al-maru-yajizu — «الْمَرْءُ يَعْجِزُ لَا الْمَحَالَةُ», the proverbs' shelf (v348-A), Level 5.

RECEIVED TEXT: Aktham ibn Ṣayfī's proverb in Abū ʿUbayd, and al-Bakrī's commentary: Abū al-Aswad's three verses that put the proverb
into verse and the story of the door between him and his cousin, «فصل المقال» (Shamela 1025, p. 311 = printed 1:299). The exact
passage: research/sources/mathal-al-maru-yajizu-src.txt. From «وقال أبو الأسود في نظم هذا المثل» to «وقال هذا الشعر», whole and in
order — the three verses (each one sentence, the hemistich marked «•»), then the tale; the two verses after it are not taken.
No correction. The verses' rhyme words are written as the print writes them, with the pausal hāʾ (الْجَهَالَهْ، الْمَحَالَهْ،
الْمَقَالَهْ). Every vowel is ours; «فَاحْتَلْتَ» is the print's reading (the editor's note gives «أخطأت» / «حاولت» / «واحتلت» elsewhere).
Run: python3 tools/authoring/author_mathal_al_maru_yajizu.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from amthal_common import *

SLUG = "mathal-al-maru-yajizu"
AA = ("أَبِي الْأَسْوَدِ", "Abū al-Aswad", "Ebü'l-Esved")
WAQF = ("، وَعَلَامَةُ الْإِعْرَابِ مُقَدَّرَةٌ مَنَعَ مِنْ ظُهُورِهَا سُكُونُ الْوَقْفِ — وَالتَّاءُ الْمَرْبُوطَةُ تُنْطَقُ هَاءً فِي الْوَقْفِ وَعَلَى ذٰلِكَ كُتِبَتْ", " — the case sign is estimated, hidden by the pause at the rhyme; the tāʾ marbūṭa is said (and here written) as hāʾ in pause", " — i'râb alâmeti, kafiyedeki vakf sükûnu yüzünden takdîrîdir; tâ-i merbûta vakıfta hâ okunur ve öyle yazılmıştır")
def AL_MAR(role="mub"):
    return MUBTADA("الْمَرْءُ", "mar") if role == "mub" else None
def YAJIZU(note=("", "", "")):
    return MUDARI("يَعْجِزُ", "ajaza", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ" + note[0], note_en=" — the clause is the predicate of «a man», in the seat of raf'" + note[1], note_tr=" — cümle mübtedânın haberi, mahallen merfû" + note[2])
def LA_ATF():
    return tok("لَا", "la-nafiya", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ يَنْفِي عَنِ الْمَعْطُوفِ مَا ثَبَتَ لِلْمَعْطُوفِ عَلَيْهِ.", "The conjunction لَا «not»: it denies of what follows what was affirmed of what went before.", "Atıf harfi lâ «değil»: öncekine sabit olanı sonrakinden nefyeder.")
def BI_ABI_ASWAD(note=("", "", "")):
    return [tok("بِأَبِي", "ab", "noun", ["huruf-jarr", "five-nouns", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَأَبِي مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ" + note[0] + ".", "The ba is a jarr letter; «Abū» is in jarr by the ya (one of the five nouns), annexed" + note[1] + ".", "Bâ cer harfi; «Ebî» esmâ-i hamseden olduğu için yâ ile mecrûr, muzâf" + note[2] + ".", segments=[seg("بِ", "bi", "prep"), seg("أَبِي", "ab", "noun")]),
            NM("الْأَسْوَدِ", "aswad")]

TITLES = [{"ar": "الْمَرْءُ يَعْجِزُ لَا الْمَحَالَةُ", "en": "It Is the Man Who Fails, Not the Way Out", "tr": "Âciz Kalan Kişidir, Çare Değil"}]
S1 = []
S1.append({"id": "s1", "translation": {"en": "It is a man who falls short — not the means.", "tr": "Âciz kalan kişidir, çare değil."},
 "tokens": [NOTE(AL_MAR(), " — وَهُوَ مِنْ أَمْثَالِ أَكْثَمَ بْنِ صَيْفِيٍّ" + HEAD_CL[0], " — one of the proverbs of Aktham ibn Ṣayfī" + HEAD_CL[1], " — Eksem b. Sayfî'nin atasözlerinden" + HEAD_CL[2]), YAJIZU(), LA_ATF(),
  ATF("الْمَحَالَةُ", "mahala-escape", note_ar=" — وَالْمَحَالَةُ: الْحِيلَةُ", note_en=" — مَحَالَة: a stratagem, a way out", note_tr=" — mehâle: hîle, çare", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "Abū al-Aswad said, putting this proverb into verse:", "tr": "Ebü'l-Esved bu atasözünü nazma dökerek şöyle dedi:"},
 "tokens": [QALA("وَقَالَ"), tok("أَبُو", "ab", "noun", ["fail", "five-nouns", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "The doer (fa'il), in raf' by the waw — one of the five nouns; annexed.", "Fâil, esmâ-i hamseden olduğu için vâv ile merfû; muzâf."),
  NM("الْأَسْوَدِ", "aswad", (" — وَأَبُو الْأَسْوَدِ الدُّؤَلِيُّ وَاضِعُ النَّحْوِ فِيمَا يُرْوَى", " — Abū al-Aswad al-Duʾalī, said to have laid down grammar", " — nahvi ilk vaz' ettiği rivâyet edilen Ebü'l-Esved ed-Düelî")),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَالَ»", "; the phrase hangs on «said»", "; câr-mecrûr «dedi»ye müteallik"),
  MAJR("نَظْمِ", "nazm", extra=["masdar"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  ISHARA("هٰذَا", "hadha", "جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "muzâfun ileyh — mecrûr"), BADAL("الْمَثَلِ", "mathal", "jarr", punct=":")]})
S1.append({"id": "s3", "translation": {"en": "«Did you defy the bidding of men of sense • and obey the bidding of the ignorant?", "tr": "«Akıl sahiplerinin sözüne isyan edip • cahillerin sözüne mi uydun?"},
 "tokens": [tok("أَعَصَيْتَ", "asa", "verb", ["al-istifham", "naqis-verbs", "al-bariz-al-muttasil", "fail"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ التَّوْبِيخِيِّ، وَعَصَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.",
      "The hamza asks in rebuke; «defied» is a past verb built on sukun because the ta of the doer is attached; that ta «you» is the doer — the clause is what is said.", "Hemze tevbîh istifhamı; asâ, fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî; tâ fâil — cümle mekūlü'l-kavl.", segments=[seg("أَ", "hamza-istifham", "part"), seg("عَصَيْ", "asa", "verb"), seg("تَ", "pron-2ms", "pron")]),
  MAFUL("أَمْرَ", "amr", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("ذَوِي", "dhu", extra=["jam-mudhakkar-salim"], sign="بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", note_ar="، مُضَافٌ", note_en=" — by the ya (attached to the sound masculine plural), its nun dropped for the annexation; annexed", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile, izâfet için nûnu düşmüş; muzâf"),
  MUDAF_ILAYH("النُّهَى", "nuha-minds", extra=["ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_ar=" — جَمْعُ نُهْيَةٍ: الْعَقْلُ", note_en=" — the kasra is estimated on the alif; plural of نُهْيَة «reason, sense»", note_tr=" — kesre elif üzerinde takdîrî; nühye'nin (akıl) çoğulu", punct="•"),
  tok("وَأَطَعْتَ", "ataa", "verb", ["form-iv-verbs", "hollow-verbs", "al-bariz-al-muttasil", "fail"], WA_AR + "أَطَاعَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "The waw conjoins; «obeyed» is a past verb built on sukun before the ta of the doer, its middle letter dropped where two sukuns meet; the ta «you» is its doer.", "«ve» + etâa, fâil tâ'sı karşısında sükûn üzere mebnî mâzî; iki sâkin yüzünden aynü'l-fiil düşmüş; tâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("أَطَعْ", "ataa", "verb"), seg("تَ", "pron-2ms", "pron")]),
  MAFUL("أَمْرَ", "amr", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("ذَوِي", "dhu", extra=["jam-mudhakkar-salim"], sign="بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", note_ar="، مُضَافٌ", note_en=" — by the ya; annexed", note_tr=" — yâ ile; muzâf"),
  tok("الْجَهَالَهْ", "jahala", "noun", ["idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ" + WAQF[0] + ".", "The second term of the idafa, in jarr" + WAQF[1] + ".", "Muzâfun ileyh, mecrûr" + WAQF[2] + ".", punct="؟")]})
S1.append({"id": "s4", "translation": {"en": "You schemed, when you broke with me — • it is a man who falls short, not the means;", "tr": "Benden koptuğunda hîleye başvurdun; • âciz kalan kişidir, çare değil;"},
 "tokens": [tok("فَاحْتَلْتَ", "ihtala", "verb", ["form-viii-verbs", "hollow-verbs", "al-bariz-al-muttasil", "fail"], "الْفَاءُ عَاطِفَةٌ، وَاحْتَالَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَحُذِفَتْ أَلِفُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "The fa conjoins; «you schemed» is a past verb built on sukun before the ta of the doer, its alif dropped where two sukuns meet; the ta «you» is its doer.", "«bunun üzerine» + ihtâle, fâil tâ'sı karşısında sükûn üzere mebnî mâzî; elifi iki sâkin yüzünden düşmüş; tâ fâil.", segments=[seg("فَ", "fa", "conj"), seg("احْتَلْ", "ihtala", "verb"), seg("تَ", "pron-2ms", "pron")]),
  ZARF("حِينَ", "hin", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«احْتَلْتَ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", note_en="; it hangs on «you schemed» and is annexed to the clause after it", note_tr="; «hîleye başvurdun»a müteallik, sonraki cümleye muzâf"),
  tok("صَرَمْتَنِي", "sarama-cut", "verb", ["al-bariz-al-muttasil", "fail", "maful-bihi", "ya-al-mutakallim"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «حِينَ» إِلَيْهَا.",
      "Past verb built on sukun before the ta of the doer; the ta «you» is its doer, the nun guards the verb and the ya «me» is its object — the clause is in the seat of jarr, annexed to «when».", "Fâil tâ'sı karşısında sükûn üzere mebnî mâzî; tâ fâil, nûn vikâye, yâ mef'ûlün bih — cümle «hîne»ye muzâfun ileyh, mahallen mecrûr.", punct="•", segments=[seg("صَرَمْ", "sarama-cut", "verb"), seg("تَ", "pron-2ms", "pron"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tok("وَالْمَرْءُ", "mar", "noun", ["mubtada-khabar"], "الْوَاوُ اعْتِرَاضِيَّةٌ أَوِ اسْتِئْنَافِيَّةٌ، وَالْمَرْءُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَهِيَ جُمْلَةُ الْمَثَلِ نَظَمَهَا الشَّاعِرُ.", "The waw opens a new clause (a parenthesis); «a man» is the mubtada, in raf' — the proverb itself, set in the verse.", "Vâv i'tirâziyye veya isti'nâfiyye; «kişi» mübtedâ, merfû — şairin nazma döktüğü atasözü cümlesi.", segments=[seg("وَ", "wa", "conj"), seg("الْمَرْءُ", "mar", "noun")]),
  YAJIZU(), LA_ATF(),
  tok("الْمَحَالَهْ", "mahala-escape", "noun", ["atf-nasaq"], "مَعْطُوفٌ عَلَى «الْمَرْءُ» مَرْفُوعٌ" + WAQF[0] + ".", "Conjoined to «a man», in raf'" + WAQF[1] + ".", "«Kişi»ye ma'tûf, merfû" + WAQF[2] + ".", punct="؛")]})
S1.append({"id": "s5", "translation": {"en": "the slave is beaten with the stick, • and for the free man a word suffices.»", "tr": "köle sopayla dövülür, • hür adama ise bir söz yeter.»"},
 "tokens": [tok("وَالْعَبْدُ", "abd", "noun", ["mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْعَبْدُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The waw conjoins; «the slave» is the mubtada, in raf'.", "«ve» + «köle» mübtedâ, merfû.", segments=[seg("وَ", "wa", "conj"), seg("الْعَبْدُ", "abd", "noun")]),
  tok("يُقْرَعُ", "qaraa-knock", "verb", ["naib-al-fail", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.", "Present verb in the passive, in raf'; its deputy doer the hidden «he» — the clause is the predicate, in the seat of raf'.", "Meçhul muzâri, merfû; nâib-i fâil gizli «o» — cümle mübtedânın haberi, mahallen merfû."),
  BI_NOUN("بِالْعَصَا", "asa-staff", "الْعَصَا", sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", extra=["ism-maqsur-manqus"], note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُقْرَعُ»", note_en=" — the kasra is estimated on the alif; the phrase hangs on «is beaten»", note_tr=" — kesre elif üzerinde takdîrî; câr-mecrûr «dövülür»e müteallik", punct="•"),
  tok("وَالْحُرُّ", "hurr", "noun", ["mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْحُرُّ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The waw conjoins; «the free man» is the mubtada, in raf'.", "«ve» + «hür» mübtedâ, merfû.", segments=[seg("وَ", "wa", "conj"), seg("الْحُرُّ", "hurr", "noun")]),
  tok("تَكْفِيهِ", "kafa", "verb", ["mudari-marfu", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «الْحُرُّ».",
      "Present verb in raf' by a damma estimated on the ya; «him» is its object, and its doer follows — the clause is the predicate of «the free man».", "Yâ üzerinde takdîrî damme ile merfû muzâri; zamir mef'ûlün bih, fâili sonra gelir — cümle «hür»ün haberi.", segments=[seg("تَكْفِي", "kafa", "verb"), seg("هِ", "pron-3ms", "pron")]),
  tok("الْمَقَالَهْ", "maqala", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ" + WAQF[0] + ".", "The doer (fa'il), in raf'" + WAQF[1] + ".", "Fâil, merfû" + WAQF[2] + ".", punct=".")]})
S1.append({"id": "s6", "translation": {"en": "The story of this poem was that a cousin of Abū al-Aswad, a close cousin on the father's side, was of bad character, and there was a door between them through which they came and went.", "tr": "Bu şiirin hikâyesi şuydu: Ebü'l-Esved'in yakın amcazadelerinden biri kötü huylu biriydi; aralarında gelip gittikleri bir kapı vardı."},
 "tokens": [ISTI(KANA("وَكَانَ")),
  PREP("مِنْ", "min", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ الْمُقَدَّمِ", "; the phrase hangs on the omitted, fronted predicate of كَانَ", "; câr-mecrûr kâne'nin öne alınmış mahzûf haberine müteallik", gloss_tr="«-den»"),
  MAJR("خَبَرِ", "khabar", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  ISHARA("هٰذَا", "hadha", "جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "muzâfun ileyh — mecrûr"), BADAL("الشِّعْرِ", "shir", "jarr"),
  tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهُ وَمِنْ مَعْمُولَيْهِ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ الْمُؤَخَّرُ.", "أَنَّ «that» — with its noun and predicate it makes a masdar, the noun of كَانَ placed last, in the seat of raf'.", "Enne — ismi ve haberiyle kurduğu müevvel masdar kâne'nin muahhar ismi, mahallen merfû."),
  tok("ابْنَ", "ibn", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The noun of أَنَّ, in nasb; annexed.", "Enne'nin ismi, mansûb; muzâf."),
  MUDAF_ILAYH("عَمٍّ", "amm-uncle"),
  tok("لِأَبِي", "li", "prep", ["huruf-jarr", "five-nouns", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَأَبِي مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«ابْنَ عَمٍّ».", "The lam is a jarr letter; «Abū» is in jarr by the ya (one of the five nouns), annexed — the phrase hangs on an omitted adjective of «a cousin».", "Lâm cer harfi; «Ebî» esmâ-i hamseden olduğu için yâ ile mecrûr, muzâf — câr-mecrûr «amcazade»nin mahzûf na'tına müteallik.", segments=[seg("لِ", "li", "prep"), seg("أَبِي", "ab", "noun")]),
  NM("الْأَسْوَدِ", "aswad"),
  HAL("دِنْيَةً", "dinya-kin", note_ar=" — أَيْ: لَاصِقَ النَّسَبِ، ابْنَ عَمٍّ لَحًّا", note_en=" — i.e. close in kinship, a full cousin on the father's side", note_tr=" — yani nesebi yakın, öz amcazade"),
  NOTE(KANA("كَانَ"), " — وَاسْمُهَا ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; its noun is the hidden «he»; the clause is the predicate of أَنَّ", "; ismi gizli «o»; cümle enne'nin haberi"),
  KHK("سَيِّءَ", "sayyi", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الْخُلُقِ", "khuluq", punct="،"),
  ISTI(KANA("وَكَانَ")),
  ZARF("بَيْنَهُمَا", "bayna", note_ar=" — مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ كَانَ الْمُقَدَّمِ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", note_en="; it hangs on the omitted, fronted predicate of كَانَ, annexed to «the two of them»", note_tr="; kâne'nin öne alınmış mahzûf haberine müteallik; «ikisi» zamirine muzâf", segments=[seg("بَيْنَ", "bayna", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  ISMK("بَابٌ", "bab", muakhkhar=True),
  tok("يَتَطَرَّقُونَ", "tatarraqa", "verb", ["afal-khamsa", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — يَعُودُ عَلَى أَهْلِ الدَّارَيْنِ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«بَابٌ».", "Present verb in raf' by the kept nun — one of the five verbs; the waw «they» (the two households) is its doer — the clause qualifies «a door».", "Ef'âl-i hamseden, nûnun sübûtuyla merfû muzâri; vâv fâil (iki hâne halkı) — cümle «kapı»nın na'tı, mahallen merfû.", segments=[seg("يَتَطَرَّقُ", "tatarraqa", "verb"), seg("ونَ", "pron-3mp", "pron")]),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَتَطَرَّقُونَ»", note_en=" — the phrase hangs on «came and went»", note_tr=" — câr-mecrûr «gelip giderlerdi»ye müteallik", punct=".")]})
S1.append({"id": "s7", "translation": {"en": "That door was one of the things that were of use to Abū al-Aswad; and his cousin wanted to block it.", "tr": "O kapı, Ebü'l-Esved'in işine yarayan şeylerdendi; amcazadesi ise onu kapatmak istedi."},
 "tokens": [ISTI(KANA("وَكَانَ")),
  tok("مِمَّا", "min", "prep", ["huruf-jarr", "ism-mawsul"], "مِنْ حَرْفُ جَرٍّ تَبْعِيضِيٌّ أُدْغِمَتْ نُونُهُ فِي مِيمِ «مَا»، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ الْمُقَدَّمِ.", "مِنْ «of», partitive, its nun merged into the mim of مَا «what», a relative in the seat of jarr — the phrase hangs on the omitted, fronted predicate of كَانَ.", "Min (teb'îz), nûnu «mâ»nın mîmine idgam edilmiş; mâ ism-i mevsûl, mahallen mecrûr — câr-mecrûr kâne'nin öne alınmış mahzûf haberine müteallik.", segments=[seg("مِمَّ", "min", "prep"), seg("ا", "ma-mawsula", "pron")]),
  MUDARI("يَرْفُقُ", "rafaqa", note_ar=" — وَالْجُمْلَةُ صِلَةُ «مَا»", note_en=" — the clause is the ṣila of «what»", note_tr=" — cümle «mâ»nın sılası"),
  *BI_ABI_ASWAD((" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَرْفُقُ»", " — the phrase hangs on «be of use»", " — câr-mecrûr «işine yarar»a müteallik")),
  ISHARA("ذٰلِكَ", "dhalika", "رَفْعٍ اسْمُ كَانَ الْمُؤَخَّرُ", "raf' as the noun of كَانَ placed last", "kâne'nin muahhar ismi — merfû"), BADAL("الْبَابُ", "bab", "raf", punct="،"),
  tok("وَأَنَّ", "anna", "part", ["inna-wa-akhawatuha", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى «أَنَّ ابْنَ عَمٍّ» قَبْلَهُ.", "The waw conjoins; أَنَّ «that» — the masdar it makes is conjoined to «that a cousin» before it.", "«ve» + enne — kurduğu müevvel masdar öncedeki «enne ibne ammin»e ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("أَنَّ", "anna", "part")]),
  tok("ابْنَ", "ibn", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The noun of أَنَّ, in nasb; annexed.", "Enne'nin ismi, mansûb; muzâf."),
  ENC_NOUN("عَمِّهِ", "amm-uncle", "هِ", "mudaf"),
  MADI("أَرَادَ", "arada", ["form-iv-verbs", "hollow-verbs"], hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", note_en=" — the clause is the predicate of أَنَّ", note_tr=" — cümle enne'nin haberi"),
  ENC_NOUN("سَدَّهُ", "sadd", "هُ", "maful", extra=["masdar"], note_ar=" — وَالْهَاءُ لِلْبَابِ", note_en=" — «it» is the door", note_tr=" — zamir kapıya döner", punct=".")]})
S1.append({"id": "s8", "translation": {"en": "One of their cousins said to him: «Do not make it hard for your cousin — leave the door.»", "tr": "Amcazadelerinden biri ona: «Amcanın oğluna zorluk çıkarma; kapıyı bırak» dedi."},
 "tokens": [ISTI(MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD))), LAHU("لَهُ", "pron-3ms", " («ona»)"),
  FAIL("بَعْضُ", "bad", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("بَنِي", "banu", extra=["jam-mudhakkar-salim"], sign="بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ", note_ar="، مُضَافٌ", note_en=" — by the ya, its nun dropped for the annexation; annexed", note_tr=" — yâ ile, izâfet için nûnu düşmüş; muzâf"),
  ENC_NOUN("عَمِّهِمْ", "amm-uncle", "هِمْ", "mudaf", punct=":"),
  LA_NAHIYA(),
  tok("تَشُقَّنَّ", "shaqqa", "verb", ["nun-tawkid", "la-nahiya", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الثَّقِيلَةِ فِي مَحَلِّ جَزْمٍ بِلَا النَّاهِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ، وَالنُّونُ حَرْفُ تَوْكِيدٍ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.",
      "Present verb built on fatha because the heavy nun of emphasis is attached, in the seat of jazm by the forbidding لَا; its doer «you» hidden; the nun is the particle of emphasis — the clause is what is said.", "Ağır te'kîd nûnu bitiştiği için fetha üzere mebnî muzâri, nehiy lâsı ile mahallen meczûm; fâil vücûben gizli «sen»; nûn te'kîd harfi — cümle mekūlü'l-kavl.", segments=[seg("تَشُقَّ", "shaqqa", "verb"), seg("نَّ", "nun-tawkid", "part")]),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَشُقَّنَّ»", "; the phrase hangs on «make it hard»", "; câr-mecrûr «zorluk çıkarma»ya müteallik"),
  MAJR("ابْنِ", "ibn", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), ENC_NOUN("عَمِّكَ", "amm-uncle", "كَ", "mudaf", punct="؛"),
  AMR("دَعِ", "wadaa-let", built="السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", built_en="sukun (with kasra where two sukuns meet)", built_tr="sükûn (iki sâkin yüzünden kesreli)"),
  MAFUL("الْبَابَ", "bab", punct=".")]})
S1.append({"id": "s9", "translation": {"en": "But he would have nothing but to block it; then he regretted it and wanted to open it, because the door was of use to them both alike;", "tr": "Ama o kapatmaktan başka bir şeye razı olmadı; sonra pişman oldu ve onu açmak istedi, çünkü kapı ikisinin de işine yarıyordu;"},
 "tokens": [ISTI(MADI_ALIF("فَأَبَى", "aba", ["mahmuz-verbs"], hidden=True, note_ar=" — وَفِيهِ مَعْنَى النَّفْيِ، فَجَازَ الِاسْتِثْنَاءُ الْمُفَرَّغُ بَعْدَهُ", note_en=" — it carries a negative sense, so an emptied exception may follow", note_tr=" — nefiy mânâsı taşır; bu yüzden ondan sonra müferrağ istisna caizdir")),
  ILLA(), ENC_NOUN("سَدَّهُ", "sadd", "هُ", "maful", extra=["masdar"], punct="،"),
  THUMMA(), MADI("نَدِمَ", "nadima", hidden=True),
  MADI("وَأَرَادَ", "arada", ["form-iv-verbs", "hollow-verbs"], hidden=True),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِـ«أَرَادَ»", "; the masdar it makes is the object of «wanted»", "; müevvel masdar «istedi»nin mef'ûlü"),
  MANSUB_AN("يَفْتَحَهُ", "fataha", enc="هُ", punct="،"),
  tok("لِأَنَّ", "anna", "part", ["lam-taleel", "huruf-jarr", "inna-wa-akhawatuha"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ مُتَعَلِّقٌ بِـ«أَرَادَ».", "The lam of cause, a jarr letter, and أَنَّ «that» — the masdar they make is in jarr, hanging on «wanted».", "Ta'lîl lâmı ve enne — kurulan müevvel masdar lâm ile mecrûr, «istedi»ye müteallik.", segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part")]),
  tok("الْبَابَ", "bab", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of أَنَّ, in nasb.", "Enne'nin ismi, mansûb."),
  NOTE(KANA("كَانَ"), " — وَاسْمُهَا مُسْتَتِرٌ: هُوَ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; its noun is the hidden «it»; the clause is the predicate of أَنَّ", "; ismi gizli «o»; cümle enne'nin haberi"),
  MUDARI_KH("يَرْفُقُ", "rafaqa"),
  JARR_PRON("بِهِمَا", "bi", "بِ", "هِمَا", " («ikisine»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَرْفُقُ»", note_en=" — the phrase hangs on «be of use»", note_tr=" — câr-mecrûr «işine yarar»a müteallik"),
  HAL("جَمِيعًا", "jami", note_ar=" — مِنَ الضَّمِيرِ فِي «بِهِمَا»", note_en=" — of «them» in «to them both»", note_tr=" — «bihimâ»daki zamirden", punct="،")]})
S1.append({"id": "s10", "translation": {"en": "but Abū al-Aswad would have nothing but to keep it blocked, and he spoke this poem.", "tr": "ama bu sefer Ebü'l-Esved kapalı kalmasından başkasına razı olmadı ve bu şiiri söyledi."},
 "tokens": [ISTI(MADI_ALIF("فَأَبَى", "aba", ["mahmuz-verbs"], note_ar="، وَالْفَاعِلُ بَعْدَهُ", note_en="; its doer follows", note_tr="; fâili sonra gelir")),
  tok("أَبُو", "ab", "noun", ["fail", "five-nouns", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "The doer (fa'il), in raf' by the waw — one of the five nouns; annexed.", "Fâil, esmâ-i hamseden olduğu için vâv ile merfû; muzâf."),
  NM("الْأَسْوَدِ", "aswad"), ILLA(), ENC_NOUN("سَدَّهُ", "sadd", "هُ", "maful", extra=["masdar"], punct="،"),
  QALA("وَقَالَ", hidden=True), ISHARA("هٰذَا", "hadha", "نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the direct object", "mef'ûlün bih — mansûb"), BADAL("الشِّعْرَ", "shir", "nasb", punct=".")]})

NEW_GLOSS = {
 "mahala-escape": NN("مَحَالَة", "ح و ل", "a stratagem, a way out, a means (as حِيلَة) — الْمَرْءُ يَعْجِزُ لَا الْمَحَالَةُ «it is the man who fails, not the means»", "hîle, çare, yol (حِيلَة gibi) — الْمَرْءُ يَعْجِزُ لَا الْمَحَالَةُ «âciz kalan kişidir, çare değil»", level=5),
 "nuha-minds": NN("نُهًى", "ن ه ي", "reason, good sense (pl. of نُهْيَة) — ذَوُو النُّهَى «men of sense»", "akıl, sağduyu (nühye'nin çoğulu) — ذَوُو النُّهَى «akıl sahipleri»", level=5),
 "ihtala": NV("اِحْتَالَ", "ح و ل", "VIII", "to use a stratagem, to contrive (Form VIII, hollow)", "hîle yapmak, çare aramak (iftiâl bâbı, ecvef)", level=5),
 "sarama-cut": NV("صَرَمَ", "ص ر م", "I", "to cut off; to break with (a friend) — صَرَمَ يَصْرِمُ", "kesmek; (bir dosttan) kopmak — sarame yasrimu", level=5),
 "dinya-kin": NN("دِنْيَة", "د ن و", "close in kinship — ابْنُ عَمٍّ دِنْيَةً «a full cousin on the father's side»", "nesebi yakın — ابْنُ عَمٍّ دِنْيَةً «öz amcazade»", level=5),
 "tatarraqa": NV("تَطَرَّقَ", "ط ر ق", "V", "to make one's way (through), to come and go (by a way) (Form V)", "(bir yoldan) geçmek, gelip gitmek (tefa''ul bâbı)", level=5),
}
GLOSS_HERE = {
 "aswad": ("black; here in the kunya Abū al-Aswad of Ẓālim ibn ʿAmr al-Duʾalī (d. 69 AH), the poet and first grammarian", "siyah; burada şair ve ilk nahivci Zâlim b. Amr ed-Düelî'nin (ö. 69) künyesi Ebü'l-Esved'de"),
 "rafaqa": ("to be gentle (with بِ); رَفَقَ بِهِ الشَّيْءُ: (of a thing) to be of use, to suit a man", "yumuşak davranmak (بِ ile); رَفَقَ بِهِ الشَّيْءُ: bir şey birinin işine yaramak"),
 "shaqqa": ("to tear, to split; شَقَّ عَلَيْهِ: to make things hard for a man (doubled)", "yarmak; شَقَّ عَلَيْهِ: birine zorluk çıkarmak (muzaaf)"),
}
V = {"ihtala": SG.derived_hollow(SG.B8 + " — أَجْوَفُ وَاوِيٌّ", SG.W8, "َ", "اِحْتَال", "اِحْتَل", "حْتَال", "حْتَل", "اِحْتَال", "اِحْتَل", "اِحْتِيَال", "مُحْتَال", None, None, None, "أَجْوَفُ مِنَ الِافْتِعَالِ: احْتَالَ يَحْتَالُ؛ لَازِمٌ."),
     "sarama-cut": SG.sound1("daraba", "صَرَم", "صْرِم", "اِصْرِم", "صَرْم", "صَارِم", "مَصْرُوم", "صُرِمَ", "يُصْرَمُ"),
     "tatarraqa": SG.derived(SG.B5, SG.W5, "َ", "تَطَرَّق", "تَطَرَّق", "تَطَرَّق", "تَطَرُّق", "مُتَطَرِّق", None, None, None, "لَازِمٌ: تَطَرَّقَ إِلَيْهِ.")}
FOR_HOCA = [
 ("«فَاحْتَلْتَ» (the print; the editor notes «أخطأت» in al-Khizāna, «حاولت» in al-Lisān, «واحتلت» in ط) and the second person throughout the three verses", "«فَاحْتَلْتَ» (baskı; muhakkik Hizâne'de «أخطأت», Lisân'da «حاولت», ط'de «واحتلت» kaydeder) ve üç beyitteki ikinci şahıs"),
 ("the rhyme words with the pausal hāʾ «الْجَهَالَهْ / الْمَحَالَهْ / الْمَقَالَهْ» and their case lines", "vakıf hâ'sıyla kafiye kelimeleri «الْجَهَالَهْ / الْمَحَالَهْ / الْمَقَالَهْ» ve i'râb satırları"),
 ("«دِنْيَةً» with kasra (دُنْيَا is also given) read as a ḥāl", "«دِنْيَةً» kesreli (دُنْيَا da denir), hâl okundu"),
 ("«وَالْمَرْءُ يَعْجِزُ» inside the verse: the waw read as parenthetic/resuming", "beyit içindeki «وَالْمَرْءُ يَعْجِزُ»: vâv i'tirâziyye/isti'nâfiyye okundu"),
]
MANIFEST = manifest(SLUG, level=5, title=TITLES[0],
    subtitle={"ar": "أَبُو الْأَسْوَدِ وَبَابُ ابْنِ عَمِّهِ — مِنْ «فَصْلِ الْمَقَالِ» لِلْبَكْرِيِّ، نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "Abū al-Aswad and his cousin's door — from al-Bakrī's Faṣl al-maqāl, the received text, word for word",
              "tr": "Ebü'l-Esved ve amcazadesinin kapısı — Bekrî'nin Faslü'l-makāl'inden, lafzıyla"},
    pages="p. 311 (printed 1:299), bāb 9", pages_ar="ص ٣١١ (الْمَطْبُوعُ ١: ٢٩٩)، الْبَابُ التَّاسِعُ",
    span_en="the proverb as the heading; al-Bakrī's «وقال أبو الأسود في نظم هذا المثل» with the three verses, then «وكان من خبر هذا الشعر … وقال هذا الشعر», whole and in order (the two verses after it are not taken)",
    span_tr="başlıkta atasözü; Bekrî'nin «وقال أبو الأسود في نظم هذا المثل» sözü ve üç beyit, ardından «وكان من خبر هذا الشعر … وقال هذا الشعر», tamamen ve sırasıyla (sonraki iki beyit alınmadı)",
    span_ar="الْمَثَلُ عُنْوَانًا، ثُمَّ أَبْيَاتُ أَبِي الْأَسْوَدِ الثَّلَاثَةُ، ثُمَّ خَبَرُ هٰذَا الشِّعْرِ إِلَى «وَقَالَ هٰذَا الشِّعْرَ»",
    extra_en="Each verse is one sentence, its first hemistich closed by «•». ", extra_tr="Her beyit tek cümledir; ilk mısraı «•» ile kapanır. ",
    hoca=FOR_HOCA)
finish(SLUG, TITLES, [S1], NEW_GLOSS, MANIFEST, GLOSS_HERE, V_NEW=V)
