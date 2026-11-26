"""Author content/samples/mathal-wafaqa-shannun-tabaqah — «وَافَقَ شَنٌّ طَبَقَةَ», the proverbs' shelf (v348-A), Level 5, two chapters.

RECEIVED TEXT: Abū ʿUbayd's proverb «وافق شناً طبقه» (his own reading: the waterskin and its lid) and the fourth account al-Bakrī gives,
al-Sharqī ibn al-Quṭāmī's tale of Shann the shrewd and the girl Ṭabaqa, «فصل المقال» (Shamela 1025, pp. 274–276 = printed 1:262–264).
The exact passage: research/sources/mathal-wafaqa-shannun-tabaqah-src.txt. The tale is whole and in order, from «وذكر الشرقي بن القطامي
فيه قولاً رابعاً» to «وافقه فاعتنقه»; it is cut into two chapters at «فدخلا القرية» (the cut and the chapter titles are ours). The three
other accounts before it are not taken. The editor's bracketed supplement «[وسارا حتى قربا من قرية]» (his note: «زيادة من س») stands
as the edition prints it. At about 250 words this tale runs past the shelf's usual 60–200; it is taken whole rather than cut.
CORRECTION (one): «وأنا ركب» → «وَأَنَا رَاكِبٌ», against al-Maydānī's Majmaʿ al-amthāl (research/sources/mathal-wafaqa-shannun-tabaqah-witness.txt,
§ 4340: «أنا راكب وأنت راكب»). Every vowel is ours.
Run: python3 tools/authoring/author_mathal_wafaqa_shannun_tabaqah.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from amthal_common import *

SLUG = "mathal-wafaqa-shannun-tabaqah"
SH = ("شَنٍّ", "Shann", "Şenn")
RJ = ("الرَّجُلِ", "the man", "adam")
def SHANN(role, punct=None):
    m = (" — عَلَمٌ مُنْصَرِفٌ", " — a fully declined name", " — munsarif alem")
    if role == "fail": return FAIL("شَنٌّ", "shann-name", "propn", note_ar=m[0], note_en=m[1], note_tr=m[2], punct=punct)
    if role == "ism_anna": return tok("شَنًّا", "shann-name", "propn", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ" + m[0] + ".", "The noun of أَنَّ, in nasb" + m[1] + ".", "Enne'nin ismi, mansûb" + m[2] + ".", punct=punct)
def QAL_SH(full="فَقَالَ"):
    return ISTI(MADI(full, "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD)))
def LI_RAFIQIHI(punct=":"):
    return tok("لِرَفِيقِهِ", "li", "prep", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "اللَّامُ حَرْفُ جَرٍّ، وَرَفِيقِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَالَ».",
        "The lam is a jarr letter; «companion» is in jarr, annexed to «his» — the phrase hangs on «said».", "Lâm cer harfi; «yol arkadaşı» mecrûr, «onun» zamirine muzâf — câr-mecrûr «dedi»ye müteallik.", punct=punct,
        segments=[seg("لِ", "li", "prep"), seg("رَفِيقِ", "rafiq-companion", "noun"), seg("هِ", "pron-3ms", "pron")])
def ATAHMILUNI(full="أَتَحْمِلُنِي", note=MAQUL):
    return tok(full, "hamala", "verb", ["al-istifham", "mudari-marfu", "al-bariz-al-muttasil", "maful-bihi", "ya-al-mutakallim"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَتَحْمِلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + note[0] + ".",
        "The hamza asks; «carry» is a present verb in raf', its doer «you» hidden; the nun guards the verb and the ya «me» is its object" + note[1] + ".", "Hemze istifham; tahmilu merfû muzâri, fâil vücûben gizli «sen»; nûn vikâye, yâ mef'ûlün bih" + note[2] + ".",
        segments=[seg("أَ", "hamza-istifham", "part"), seg("تَحْمِلُ", "hamala", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])
def AM():
    return tok("أَمْ", "am", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ مُعَادِلٌ لِلْهَمْزَةِ (أَمِ الْمُتَّصِلَةُ)، يُطْلَبُ بِهِ التَّعْيِينُ.", "The joined أَمْ «or», which balances the hamza and asks which of the two.", "Hemzeye denk muttasıl em «yoksa»: ikisinden hangisi olduğunu sorar.")
def AHMILUKA(punct="؟"):
    return MUDARI("أَحْمِلُكَ", "hamala", who="أَنَا", enc="كَ", wujub=True, note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ بِـ«أَمْ»", note_en=" — the clause is joined by «or»", note_tr=" — cümle «em» ile ma'tûf", punct=punct)
def AUKILA(full="أَأُكِلَ"):
    return tok(full, "akala", "verb", ["al-istifham", "naib-al-fail", "mahmuz-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَأُكِلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَنَائِبُ الْفَاعِلِ بَعْدَهُ — ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ آخِرِهِ.",
        "The hamza asks; «has been eaten» is a past verb in the passive, built on fatha — its first letter takes damma and the one before the last a kasra; its deputy doer follows.", "Hemze istifham; ükile meçhul mâzî, fetha üzere mebnî — evveli mazmûm, âhirinden önceki meksûr; nâib-i fâili sonra gelir.",
        segments=[seg("أَ", "hamza-istifham", "part"), seg("أُكِلَ", "akala", "verb")])
def HADHA_ZAR(punct=None):
    return [ISHARA("هٰذَا", "hadha", "رَفْعٍ نَائِبُ فَاعِلٍ", "raf' as the deputy doer", "nâib-i fâil — merfû"), BADAL("الزَّرْعُ", "zar", "raf", punct=punct)]
def AHAYYAN(full="أَحَيًّا"):
    return tok(full, "hayy", "noun", ["al-istifham", "hal"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَحَيًّا حَالٌ مُقَدَّمٌ مَنْصُوبٌ بِالْفَتْحَةِ — صَاحِبُهُ «مَنْ» أَوِ الضَّمِيرُ بَعْدَ «تَرَى».", "The hamza asks; «alive» is a hal placed first, in nasb — its owner is «who» (or the pronoun after «see»).", "Hemze istifham; «diri» öne alınmış hâl, mansûb — sahibi «men» (ya da «terâ»dan sonraki zamir).",
        segments=[seg("أَ", "hamza-istifham", "part"), seg("حَيًّا", "hayy", "noun")])
def TARA(full="تَرَى", enc=None, note=("", "", "")):
    t = MUDARI(full, "raa", who="أَنْتَ", naqis="ا", enc=enc, wujub=True, note_ar=note[0], note_en=note[1], note_tr=note[2])
    return t
def MAYYITAN(punct="؟"):
    return tok("مَيِّتًا", "mayyit", "noun", ["atf-nasaq", "hal"], "مَعْطُوفٌ عَلَى «حَيًّا» مَنْصُوبٌ بِالْفَتْحَةِ.", "Conjoined to «alive», in nasb.", "«Diri»ye ma'tûf, mansûb.", punct=punct)
def AMMA(): return tok("أَمَّا", "amma", "part", ["amma-tafsiliyya"], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ.", "أَمَّا «as for», the particle of condition and detailing, built on sukun, with no seat.", "Emmâ «gelince», şart ve tafsil harfi, sükûn üzere mebnî, mahalli yoktur.")
def WA_AMMA(): return tok("وَأَمَّا", "amma", "part", ["amma-tafsiliyya"], "الْوَاوُ عَاطِفَةٌ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "The waw conjoins; أَمَّا «as for», the particle of condition and detailing.", "«ve» + emmâ, şart ve tafsil harfi.", segments=[seg("وَ", "wa", "conj"), seg("أَمَّا", "amma", "part")])
def QAWLUHU(punct=":"): return ENC_NOUN("قَوْلُهُ", "qawl", "هُ", "mubtada", extra=["masdar"], note_ar=" — وَالْقَوْلُ الْمَحْكِيُّ بَعْدَهُ بَدَلٌ مِنْهُ", note_en=" — the words quoted after it are a badal of it", note_tr=" — sonra nakledilen söz ondan bedeldir", punct=punct)
def FA_INNAMA(): return tok("فَإِنَّمَا", "innama", "part", ["innama-kaffa", "amma-tafsiliyya"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَإِنَّمَا كَافَّةٌ وَمَكْفُوفَةٌ لِلْحَصْرِ — وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.", "The fa answers أَمَّا; إِنَّمَا «only», held back by its مَا, restricts — the clause after it is the predicate of «his saying», in the seat of raf'.", "Fâ emmâ'nın cevabındadır; innemâ kâffe ve mekfûfe, hasr içindir — sonraki cümle mübtedânın haberi, mahallen merfû.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّمَا", "innama", "part")])

TITLES = [{"ar": "شَنٌّ وَرَفِيقُهُ", "en": "Shann and His Companion", "tr": "Şenn ve Yol Arkadaşı"},
          {"ar": "طَبَقَةُ", "en": "Ṭabaqa", "tr": "Tabaka"}]
S1 = []
S1.append({"id": "s1", "translation": {"en": "The waterskin met its lid.", "tr": "Kırba kapağını buldu (tencere yuvarlandı kapağını buldu)."},
 "tokens": [MADI("وَافَقَ", "wafaqa", ["form-iii-verbs"], note_ar=" — وَالْفَاعِلُ «طَبَقُهُ» بَعْدَ الْمَفْعُولِ" + HEAD_CL[0], note_en="; its doer «its lid» comes after the object" + HEAD_CL[1], note_tr="; fâil «kapağı», mef'ûlden sonra gelir" + HEAD_CL[2]),
  MAFUL("شَنًّا", "shann-tf", note_ar=" — مَفْعُولٌ بِهِ مُقَدَّمٌ؛ وَالشَّنُّ: الْقِرْبَةُ الْخَلَقُ، عَلَى قَوْلِ أَبِي عُبَيْدٍ", note_en=" — placed first; a شَنّ is a worn waterskin, in Abū ʿUbayd's reading", note_tr=" — öne alınmış; şenn: eski kırba (Ebû Ubeyd'in yorumunda)"),
  ENC_NOUN("طَبَقُهُ", "tabaq-amr", "هُ", "fail", note_ar=" — وَالطَّبَقُ: الْغِطَاءُ، وَالْهَاءُ لِلشَّنِّ", note_en=" — a طَبَق is a cover, a lid; «its» is the waterskin's", note_tr=" — tabak: kapak; zamir kırbaya döner", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "Al-Sharqī ibn al-Quṭāmī gave a fourth account of it: he claimed that Shann was one of the shrewd and clever men of the Arabs,", "tr": "eş-Şarkî b. el-Kutâmî bu konuda dördüncü bir görüş zikretti: Şenn'in Arapların dâhî ve akıllılarından biri olduğunu ileri sürdü;"},
 "tokens": [ISTI(MADI("وَذَكَرَ", "dhakara", **W(FAIL_BAAD))), FAIL("الشَّرْقِيُّ", "sharqi-name", "propn"), BN("raf", ("الشَّرْقِيُّ", "al-Sharqī", "eş-Şarkî")),
  NM("الْقُطَامِيِّ", "qutami"),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («onda»)", note_ar=" — وَالْهَاءُ لِلْمَثَلِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«ذَكَرَ»", note_en=" — «it» is the proverb; the phrase hangs on «gave»", note_tr=" — zamir atasözüne döner; câr-mecrûr «zikretti»ye müteallik"),
  MAFUL("قَوْلًا", "qawl"), NAAT("رَابِعًا", "rabi", "nasb", punct=":"),
  MADI("زَعَمَ", "zaama", hidden=True, note_ar=" — يَعُودُ عَلَى الشَّرْقِيِّ؛ وَالْجُمْلَةُ تَفْسِيرٌ لِلْقَوْلِ", note_en=" (al-Sharqī) — the clause spells out the account", note_tr=" (eş-Şarkî) — cümle görüşü açıklar"),
  tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ «زَعَمَ».", "أَنَّ «that» — the masdar it makes stands for the two objects of «claimed».", "Enne — kurduğu müevvel masdar «iddia etti»nin iki mef'ûlü yerini tutar."),
  SHANN("ism_anna"),
  NOTE(KANA("كَانَ"), " — وَاسْمُهَا مُسْتَتِرٌ: هُوَ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; its noun is the hidden «he»; the clause is the predicate of أَنَّ", "; ismi gizli «o»; cümle enne'nin haberi"),
  PREP("مِنْ", "min", " — تَبْعِيضِيَّةٌ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ", " — partitive; the phrase hangs on the omitted predicate of كَانَ", "; teb'îz; câr-mecrûr kâne'nin mahzûf haberine müteallik", gloss_tr="«-den»"),
  MAJR("دُهَاةِ", "dahiya", extra=["jam-taksir"], note_ar=MUDAF[0] + " — جَمْعُ دَاهِيَةٍ: الْبَصِيرُ بِالْأُمُورِ", note_en=MUDAF[1] + " — the plural of دَاهِيَة, a man of shrewd judgement", note_tr=MUDAF[2] + " — dâhiye'nin çoğulu: işlere vâkıf, zeki"),
  MUDAF_ILAYH("الْعَرَبِ", "arab"),
  tok("وَعُقَلَائِهَا", "aqil", "noun", ["atf-nasaq", "jam-taksir", "idafa-definiteness", "al-bariz-al-muttasil"], "الْوَاوُ عَاطِفَةٌ، وَعُقَلَاءِ مَعْطُوفٌ عَلَى «دُهَاةِ» مَجْرُورٌ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ عَاقِلٍ.", "The waw conjoins; «the clever» (plural of عَاقِل) is conjoined to «the shrewd», in jarr by the kasra because it is annexed (to «its», the Arabs').", "«ve» + ukalâ (âkil'in çoğulu), «dühât»a ma'tûf; muzâf olduğu için kesre ile mecrûr; «hâ» muzâfun ileyh.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("عُقَلَائِ", "aqil", "noun"), seg("هَا", "pron-3fs", "pron")])]})
S1.append({"id": "s3", "translation": {"en": "and he set out roaming the land, hoping to win a woman like himself in sense and shrewdness and marry her.", "tr": "aklı ve zekâsı kendisi gibi olan bir kadın bulup onunla evlenmek umuduyla yeryüzünde dolaşmaya başladı."},
 "tokens": [tok("فَجَعَلَ", "jaala", "verb", ["afal-al-muqaraba", "kana-wa-akhawatuha"], "الْفَاءُ عَاطِفَةٌ، وَجَعَلَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَفْعَالِ الشُّرُوعِ، وَاسْمُهُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (شَنٌّ).", "The fa conjoins; جَعَلَ here is a defective verb of beginning («set out to»), its noun the hidden «he» (Shann).", "«bunun üzerine» + ceale burada şurû' fiili (nâkıs): «…maya başladı»; ismi gizli «o» (Şenn).", segments=[seg("فَ", "fa", "conj"), seg("جَعَلَ", "jaala", "verb")]),
  MUDARI("يَضْرِبُ", "daraba", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «جَعَلَ»؛ وَضَرَبَ فِي الْأَرْضِ: سَافَرَ", note_en=" — the clause is the predicate of «set out»; ضَرَبَ فِي الْأَرْضِ: to travel the land", note_tr=" — cümle «ceale»nin haberi; darabe fi'l-ard: yeryüzünde dolaşmak"),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَضْرِبُ»", "; the phrase hangs on «roaming»", "; câr-mecrûr «dolaşır»a müteallik"), MAJR("الْأَرْضِ", "ard"),
  tok("رَجَاءَ", "raja-hope", "noun", ["maful-lah", "masdar", "idafa-definiteness"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "An object of purpose (mafʿūl li-ajlih), in nasb; annexed.", "Mef'ûlün leh, mansûb; muzâf."),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; the masdar it makes is the second term of the idafa, in the seat of jarr", "; müevvel masdar muzâfun ileyh, mahallen mecrûr"),
  MANSUB_AN("يَظْفَرَ", "zafira"),
  BI_NOUN("بِامْرَأَةٍ", "imraa", "امْرَأَةٍ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَظْفَرَ»", note_en=" — the phrase hangs on «win»", note_tr=" — câr-mecrûr «bulmak»a müteallik"),
  tok("مِثْلِهِ", "mithl", "noun", ["naat-sifa", "idafa-definiteness", "al-bariz-al-muttasil"], "نَعْتٌ لِـ«امْرَأَةٍ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَ«مِثْل» لَا يَتَعَرَّفُ بِالْإِضَافَةِ فَوُصِفَتْ بِهِ النَّكِرَةُ.", "An adjective of «a woman», in jarr, annexed to «him» — مِثْل does not become definite by annexation, so it can describe an indefinite noun.", "«Kadın»ın na'tı, mecrûr; «o» zamirine muzâf — misl izâfetle marife olmaz, bu yüzden nekreyi niteler.", segments=[seg("مِثْلِ", "mithl", "noun"), seg("هِ", "pron-3ms", "pron")]),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مِثْلِهِ»", "; the phrase hangs on «like him»", "; câr-mecrûr «onun gibi»ye müteallik"),
  MAJR("الْعَقْلِ", "aql"), ATF("وَالدَّهَاءِ", "daha", case="jarr"),
  tok("فَيَتَزَوَّجَهَا", "tazawwaja", "verb", ["nawasib-wa-jawazim-al-mudari", "form-v-verbs", "al-bariz-al-muttasil", "maful-bihi"], "الْفَاءُ عَاطِفَةٌ، وَيَتَزَوَّجَ فِعْلٌ مُضَارِعٌ مَعْطُوفٌ عَلَى «يَظْفَرَ» مَنْصُوبٌ بِالْفَتْحَةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "The fa conjoins; «marry» is conjoined to «win» and in nasb by the fatha; its doer the hidden «he», and «her» its object.", "«bunun üzerine» + yetezevvece, «bulmak»a ma'tûf, fetha ile mansûb; fâil gizli «o», «hâ» mef'ûlün bih.", punct=".", segments=[seg("فَ", "fa", "conj"), seg("يَتَزَوَّجَ", "tazawwaja", "verb"), seg("هَا", "pron-3fs", "pron")])]})
S1.append({"id": "s4", "translation": {"en": "While he was on his way, a man fell in with him whose purpose was the same as his: to go to a certain place.", "tr": "O yolda giderken, bir adam ona yoldaş oldu; ikisinin de niyeti bir yere varmaktı."},
 "tokens": [tok("فَبَيْنَمَا", "baynama", "noun", ["maful-fih"], "الْفَاءُ عَاطِفَةٌ، وَبَيْنَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«وَافَقَهُ»، وَمَا زَائِدَةٌ كَافَّةٌ.", "The fa conjoins; بَيْنَ «while» is an adverb of time in nasb, hanging on «fell in with him»; مَا is extra and holds it back from annexation to a single noun.", "«bunun üzerine» + beyne zaman zarfı, mansûb, «yoldaş oldu»ya müteallik; mâ zâide ve kâffe.", segments=[seg("فَ", "fa", "conj"), seg("بَيْنَمَا", "baynama", "noun")]),
  tok("هُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun built on fatha, in the seat of raf' as the mubtada.", "Munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû."),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ", "; the phrase hangs on an omitted predicate", "; câr-mecrûr mahzûf habere müteallik"),
  ENC_NOUN("مَسِيرِهِ", "masir", "هِ", "majr"),
  ENC_MADI("وَافَقَهُ", "wafaqa", "هُ", ["form-iii-verbs"], note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَوَافَقَهُ فِي الطَّرِيقِ: صَادَفَهُ وَرَافَقَهُ", note_en="; its doer follows — وَافَقَهُ here: to fall in with a man on the road", note_tr="; fâili sonra gelir — burada: yolda rastlayıp ona yoldaş olmak"),
  FAIL("رَجُلٌ", "rajul"),
  MADI("اتَّفَقَتْ", "ittafaqa", ["form-viii-verbs"], fem=True, note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«رَجُلٌ»", note_en="; its doer follows — the clause qualifies «a man»", note_tr="; fâili sonra gelir — cümle «adam»ın na'tı"),
  ENC_NOUN("نِيَّتُهُمَا", "niyya", "هُمَا", "fail"),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«اتَّفَقَتْ»", "; the phrase hangs on «was the same»", "; câr-mecrûr «birleşti»ye müteallik"),
  MAJR("إِتْيَانِ", "ityan", extra=["masdar"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("مَوْضِعٍ", "mawdi"),
  tok("مَا", "ma-nafiya", "part", ["anwa-ma"], "حَرْفٌ زَائِدٌ لِلْإِبْهَامِ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ: «مَوْضِعٍ مَا» أَيْ: مَوْضِعٍ أَيِّ مَوْضِعٍ.", "An extra مَا of vagueness, built on sukun, with no seat: «a certain place».", "Belirsizlik için zâid mâ, sükûn üzere mebnî, mahalli yoktur: «bir yer».", punct="،")]})
S1.append({"id": "s5", "translation": {"en": "Shann turned to the man on their way and said to him: «Will you carry me, or shall I carry you?»", "tr": "Yolda Şenn adama döndü ve ona: «Sen mi beni taşırsın, ben mi seni taşıyayım?» dedi."},
 "tokens": [ISTI(MADI("فَأَقْبَلَ", "aqbala", ["form-iv-verbs"], **W(FAIL_BAAD))), SHANN("fail"),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَقْبَلَ»", "; the phrase hangs on «turned»", "; câr-mecrûr «döndü»ye müteallik"), MAJR("الرَّجُلِ", "rajul"),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَقْبَلَ»", "; the phrase hangs on «turned»", "; câr-mecrûr «döndü»ye müteallik"), ENC_NOUN("طَرِيقِهِ", "tariq", "هِ", "majr"),
  QALA("فَقَالَ", hidden=True), LAHU("لَهُ", "pron-3ms", " («ona»)", punct=":"),
  ATAHMILUNI(), AM(), AHMILUKA()]})
S1.append({"id": "s6", "translation": {"en": "The man thought him a fool for what he said, and said to him: «You are riding and I am riding — so how should I carry you, or you carry me?»", "tr": "Adam bu sözü yüzünden onu cahil saydı ve ona dedi ki: «Sen bineklisin, ben de bineklisin; nasıl ben seni taşırım ya da sen beni taşırsın?»"},
 "tokens": [ISTI(ENC_MADI("فَاسْتَجْهَلَهُ", "istajhala", "هُ", ["form-x-verbs"], note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَاسْتَجْهَلَهُ: عَدَّهُ جَاهِلًا", note_en="; its doer follows — اسْتَجْهَلَهُ: to think a man a fool", note_tr="; fâili sonra gelir — istechelehû: onu cahil saymak")),
  FAIL("الرَّجُلُ", "rajul"),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«اسْتَجْهَلَهُ»", "; the phrase hangs on «thought him a fool»", "; câr-mecrûr fiile müteallik"), ENC_NOUN("قَوْلِهِ", "qawl", "هِ", "majr", extra=["masdar"], punct="،"),
  QALA("وَقَالَ", hidden=True), LAHU("لَهُ", "pron-3ms", " («ona»)", punct=":"),
  tok("أَنْتَ", "anta", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.", "A detached pronoun built on fatha, in the seat of raf' as the mubtada — the sentence is what is said.", "Munfasıl zamir, fetha üzere mebnî, mübtedâ — cümle mekūlü'l-kavl."),
  KHABAR("رَاكِبٌ", "rakib", extra=["ism-fail"]),
  tok("وَأَنَا", "ana", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "الْوَاوُ عَاطِفَةٌ، وَأَنَا ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The waw conjoins; «I» is a detached pronoun built on sukun, in the seat of raf' as the mubtada.", "«ve» + «ben» munfasıl zamir, sükûn üzere mebnî, mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("أَنَا", "ana", "pron")]),
  KHABAR("رَاكِبٌ", "rakib", extra=["ism-fail"], punct="،"),
  KAYFA_HAL("فَكَيْفَ"),
  MUDARI("أَحْمِلُكَ", "hamala", who="أَنَا", enc="كَ", wujub=True),
  tok("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "أَوْ «or», a conjunction built on sukun.", "Ev «veya», atıf harfi, sükûn üzere mebnî."),
  MUDARI("تَحْمِلُنِي", "hamala", who="أَنْتَ", wujub=True, note_ar="، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", note_en="; the nun guards the verb and the ya «me» is its object", note_tr="; nûn vikâye, yâ mef'ûlün bih", punct="؟", segments=[seg("تَحْمِلُ", "hamala", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])]})
S1.append({"id": "s7", "translation": {"en": "Shann fell silent towards him, and the two went on until they came near a village — and there was a crop ready for harvest.", "tr": "Şenn sustu; ikisi yürüdüler, nihayet bir köye yaklaştılar; bir de baktılar ki ekin hasat vaktine gelmiş."},
 "tokens": [ISTI(MADI("فَسَكَتَ", "sakata", **W(FAIL_BAAD))), SHANN("fail"),
  JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ona karşı»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سَكَتَ»", note_en=" — the phrase hangs on «fell silent»", note_tr=" — câr-mecrûr «sustu»ya müteallik", punct="،"),
  tok("وَسَارَا", "sara-travel", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "fail", "al-muthanna"], WA_AR + "سَارَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "The waw conjoins; «went on» is a past verb built on fatha, and the alif of the two is its doer.", "«ve» + sâra fetha üzere mebnî mâzî; tesniye elifi fâil.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("سَارَ", "sara-travel", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("حَتَّى", "hatta", "part", ["ila-hatta-fi-wal-ba-fil-kafiya"], "حَرْفُ ابْتِدَاءٍ وَغَايَةٍ لَا مَحَلَّ لَهُ.", "حَتَّى here opens a clause and marks the end point («until»), with no seat.", "Hattâ burada ibtidâ ve gâye harfi, mahalli yoktur."),
  tok("قَرُبَا", "qaruba", "verb", ["al-bariz-al-muttasil", "fail", "al-muthanna"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "Past verb built on fatha; the alif of the two is its doer.", "Fetha üzere mebnî mâzî; tesniye elifi fâil.", segments=[seg("قَرُبَ", "qaruba", "verb"), seg("ا", "pron-3d", "pron")]),
  PREP("مِنْ", "min", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَرُبَا»", "; the phrase hangs on «came near»", "; câr-mecrûr «yaklaştılar»a müteallik", gloss_tr="«-den»"),
  MAJR("قَرْيَةٍ", "qarya", punct="،"),
  tok("فَإِذَا", "idha", "part", [], "الْفَاءُ عَاطِفَةٌ، وَإِذَا حَرْفُ مُفَاجَأَةٍ لَا مَحَلَّ لَهُ.", "The fa conjoins; إِذَا is the particle of surprise («and there was»), with no seat.", "«bunun üzerine» + müfâcee izâ'sı («bir de ne görsünler»), mahalli yoktur.", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")]),
  MUBTADA("زَرْعٌ", "zar", note_ar=" — وَسَاغَ الِابْتِدَاءُ بِهِ نَكِرَةً بَعْدَ «إِذَا» الْفُجَائِيَّةِ", note_en=" — an indefinite noun may open the sentence after the إِذَا of surprise", note_tr=" — müfâcee izâ'sından sonra nekre ile ibtidâ caizdir"),
  tok("قَدِ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "قَدْ affirms the past verb; kasra where two sukuns meet.", "Kad tahkîk harfi; iki sâkin yüzünden kesreli."),
  MADI("اسْتَحْصَدَ", "istahsada", ["form-x-verbs"], hidden=True, note_ar=" — أَيْ: حَانَ حَصَادُهُ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ", note_en=" — i.e. it was ready for harvest; the clause is the predicate of «a crop»", note_tr=" — yani hasat vakti geldi; cümle «ekin»in haberi", punct="،")]})
S1.append({"id": "s8", "translation": {"en": "Shann said to his companion: «Has this crop been eaten or not?»", "tr": "Şenn yol arkadaşına: «Bu ekin yenmiş mi, yenmemiş mi?» dedi."},
 "tokens": [QAL_SH(), SHANN("fail"), LI_RAFIQIHI(), AUKILA(), *HADHA_ZAR(),
  tok("أَمْ", "am", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ مُعَادِلٌ لِلْهَمْزَةِ.", "The joined أَمْ «or», balancing the hamza.", "Hemzeye denk em «yoksa»."),
  tok("لَا", "la-nafiya", "part", ["la-nafiya", "hadhf-wa-taqdir"], "حَرْفُ نَفْيٍ، وَالْجُمْلَةُ بَعْدَهُ مَحْذُوفَةٌ: أَمْ لَمْ يُؤْكَلْ.", "The negating لَا, its clause left out: «or (has it) not (been eaten)?»", "Nefy harfi lâ; cümlesi mahzûf: «yoksa yenmedi mi?»", punct="؟")]})
S1.append({"id": "s9", "translation": {"en": "He said to him: «You have brought us an absurdity once again!»", "tr": "Adam ona: «Yine bize saçma bir şey getirdin!» dedi."},
 "tokens": [ISTI(QALA("فَقَالَ", hidden=True)), LAHU("لَهُ", "pron-3ms", " («ona»)", punct=":"), QAD(),
  tok("جِئْتَنَا", "jaa", "verb", ["hollow-verbs", "mahmuz-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.", "Past verb built on sukun before the ta of the doer; the ta «you» is its doer and نَا «us» its object — the clause is what is said.", "Fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî; tâ fâil, «nâ» mef'ûlün bih — cümle mekūlü'l-kavl.", segments=[seg("جِئْ", "jaa", "verb"), seg("تَ", "pron-2ms", "pron"), seg("نَا", "pron-1p", "pron")]),
  tok("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: آضَ، مَنْصُوبٌ بِالْفَتْحَةِ.", "An absolute object of an omitted verb (آضَ), in nasb: «again, likewise».", "Mahzûf (آضَ) fiilin mef'ûl-i mutlakı, mansûb: «yine»."),
  BI_NOUN("بِمُحَالٍ", "muhal", "مُحَالٍ", note_ar=" — وَالْمُحَالُ: مَا لَا يَسْتَقِيمُ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جِئْتَنَا»", note_en=" — مُحَال: what makes no sense; the phrase hangs on «brought us»", note_tr=" — muhâl: tutarsız söz; câr-mecrûr «getirdin»e müteallik", punct="!")]})
S1.append({"id": "s10", "translation": {"en": "He fell silent towards him and did not answer him; [and the two went on until they came near a village].", "tr": "Şenn sustu, ona cevap vermedi; [ikisi yürüdüler, nihayet bir köye yaklaştılar]."},
 "tokens": [ISTI(MADI("فَسَكَتَ", "sakata", hidden=True)),
  JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ona karşı»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سَكَتَ»", note_en=" — the phrase hangs on «fell silent»", note_tr=" — câr-mecrûr «sustu»ya müteallik"),
  tok("وَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], WA_AR + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The waw conjoins; لَمْ negates and puts the verb in jazm.", "«ve» + lem: nefy, cezm ve kalb harfi.", segments=[seg("وَ", "wa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  tok("يُجِبْهُ", "ajaba", "verb", ["nawasib-wa-jawazim-al-mudari", "form-iv-verbs", "hollow-verbs", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "Present verb in jazm by لَمْ, its sign the sukun (its middle letter drops where two sukuns meet); its doer the hidden «he», and «him» its object.", "Lem ile meczûm muzâri, alâmeti sükûn (aynü'l-fiil iki sâkin yüzünden düşer); fâil gizli «o», zamir mef'ûlün bih.", punct="،", segments=[seg("يُجِبْ", "ajaba", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("وَسَارَا", "sara-travel", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "fail", "al-muthanna"], WA_AR + "سَارَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَهٰذِهِ الْجُمْلَةُ إِلَى «قَرْيَةٍ» زِيَادَةُ الْمُحَقِّقِ مِنَ النُّسْخَةِ «س».", "The waw conjoins; «went on» is a past verb built on fatha, and the alif of the two is its doer — this clause, to «a village», is the editor's supplement from manuscript س.", "«ve» + sâra fetha üzere mebnî mâzî; tesniye elifi fâil — «köy»e kadarki bu cümle, muhakkikin س nüshasından ilâvesidir.", segments=[seg("وَ", "wa", "conj"), seg("سَارَ", "sara-travel", "verb"), seg("ا", "pron-3d", "pron")]),
  tok("حَتَّى", "hatta", "part", ["ila-hatta-fi-wal-ba-fil-kafiya"], "حَرْفُ ابْتِدَاءٍ وَغَايَةٍ لَا مَحَلَّ لَهُ.", "حَتَّى opens a clause and marks the end point, with no seat.", "Hattâ ibtidâ ve gâye harfi, mahalli yoktur."),
  tok("قَرُبَا", "qaruba", "verb", ["al-bariz-al-muttasil", "fail", "al-muthanna"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "Past verb built on fatha; the alif of the two is its doer.", "Fetha üzere mebnî mâzî; tesniye elifi fâil.", segments=[seg("قَرُبَ", "qaruba", "verb"), seg("ا", "pron-3d", "pron")]),
  PREP("مِنْ", "min", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَرُبَا»", "; the phrase hangs on «came near»", "; câr-mecrûr «yaklaştılar»a müteallik", gloss_tr="«-den»"),
  MAJR("قَرْيَةٍ", "qarya", punct=".")]})

S2 = []
S2.append({"id": "s1", "translation": {"en": "They went into the village, and a funeral bier met them.", "tr": "Köye girdiler; karşılarına bir cenaze çıktı."},
 "tokens": [tok("فَدَخَلَا", "dakhala", "verb", ["al-bariz-al-muttasil", "fail", "al-muthanna"], "الْفَاءُ عَاطِفَةٌ، وَدَخَلَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "The fa conjoins; «went into» is a past verb built on fatha, and the alif of the two is its doer.", "«bunun üzerine» + dehale fetha üzere mebnî mâzî; tesniye elifi fâil.", segments=[seg("فَ", "fa", "conj"), seg("دَخَلَ", "dakhala", "verb"), seg("ا", "pron-3d", "pron")]),
  MAFUL("الْقَرْيَةَ", "qarya", note_ar=" — عَلَى التَّوَسُّعِ بِحَذْفِ «فِي»", note_en=" — by extension, without «in»", note_tr=" — «fî» hazfedilerek tevessüen", punct="،"),
  tok("فَتَلَقَّتْهُمَا", "talaqqa", "verb", ["form-v-verbs", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi"], "الْفَاءُ عَاطِفَةٌ، وَتَلَقَّى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ.",
      "The fa conjoins; «met» is a past verb built on a fatha estimated on the alif, dropped before the ta of the feminine; «them both» is its object, and its doer follows.", "«bunun üzerine» + telakkâ, düşen elif üzerinde takdîrî fetha ile mebnî mâzî; tâ te'nîs; «hümâ» mef'ûlün bih; fâili sonra gelir.", segments=[seg("فَ", "fa", "conj"), seg("تَلَقَّتْ", "talaqqa", "verb"), seg("هُمَا", "pron-3d", "pron")]),
  FAIL("جَنَازَةٌ", "janaza", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "Shann said to his companion: «Do you see the one on this bier as living, or dead?»", "tr": "Şenn yol arkadaşına: «Bu tabutun üzerindekini diri mi görüyorsun, ölü mü?» dedi."},
 "tokens": [QAL_SH(), SHANN("fail"), LI_RAFIQIHI(), AHAYYAN(),
  TARA(note=(" — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ", " — the clause is what is said", " — cümle mekūlü'l-kavl")),
  tok("مَنْ", "man", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "The relative «the one who», built on sukun, in the seat of nasb as the direct object.", "İsm-i mevsûl «men», sükûn üzere mebnî, mef'ûlün bih olarak mahallen mansûb."),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِلَةِ «مَنْ»", "; the phrase hangs on the omitted ṣila of «who»", "; câr-mecrûr «men»in mahzûf sılasına müteallik"),
  ISHARA("هٰذَا", "hadha", "جَرٍّ", "jarr", "mecrûr"), BADAL("النَّعْشِ", "nash-ant", "jarr"),
  tok("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "أَوْ «or», a conjunction built on sukun.", "Ev «veya», atıf harfi."),
  MAYYITAN()]})
S2.append({"id": "s3", "translation": {"en": "The man held back from answering him, thinking him a fool, and turned off to a house of his in the place.", "tr": "Adam onu cahil sayarak cevap vermekten kaçındı ve oradaki evine yöneldi."},
 "tokens": [ISTI(MADI("فَأَمْسَكَ", "amsaka", ["form-iv-verbs"], hidden=True, **W(HID(*RJ)))),
  PREP("عَنْ", "an", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَمْسَكَ»", "; the phrase hangs on «held back»", "; câr-mecrûr «kaçındı»ya müteallik", gloss_tr="«-den»"),
  ENC_NOUN("جَوَابِهِ", "jawab", "هِ", "majr"),
  tok("اسْتِجْهَالًا", "istijhal", "noun", ["maful-lah", "masdar"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "An object of purpose (mafʿūl li-ajlih), in nasb: «thinking him a fool».", "Mef'ûlün leh, mansûb: «cahil saydığından»."),
  NOTE(LAHU("لَهُ", "pron-3ms", " («onu»)", punct="،"), "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«اسْتِجْهَالًا»", "; the phrase hangs on the masdar", "; câr-mecrûr masdara müteallik"),
  MADI("وَعَدَلَ", "adala", hidden=True, note_ar=" — وَعَدَلَ إِلَيْهِ: مَالَ", note_en=" — عَدَلَ إِلَى: to turn off towards", note_tr=" — adele ilâ: bir yere sapmak"),
  NOTE(ILA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«عَدَلَ»", "; the phrase hangs on «turned off»", "; câr-mecrûr «yöneldi»ye müteallik"), MAJR("مَنْزِلٍ", "manzil"),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («orada»)", note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْهَاءُ لِلْمَوْضِعِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«مَنْزِلٍ»", note_en=" — the ba means «in», «it» the place; the phrase hangs on an omitted adjective of «a house»", note_tr=" — bâ «fî» anlamında, zamir o yere döner; câr-mecrûr «ev»in mahzûf na'tına müteallik", punct=".")]})
S2.append({"id": "s4", "translation": {"en": "The man had a daughter named Ṭabaqa; she asked her father about his guest,", "tr": "Adamın Tabaka adında bir kızı vardı; kız babasına misafirini sordu;"},
 "tokens": [ISTI(KANA("وَكَانَ")),
  tok("لِلرَّجُلِ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالرَّجُلِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ الْمُقَدَّمِ.", "The lam is a jarr letter; «the man» is in jarr — the phrase hangs on the omitted, fronted predicate of كَانَ.", "Lâm cer harfi; «adam» mecrûr — câr-mecrûr kâne'nin öne alınmış mahzûf haberine müteallik.", segments=[seg("لِ", "li", "prep"), seg("الرَّجُلِ", "rajul", "noun")]),
  ISMK("بِنْتٌ", "bint", muakhkhar=True),
  tok("تُسَمَّى", "samma", "verb", ["naib-al-fail", "form-ii-verbs", "naqis-verbs", "mudari-marfu", "mafulayn"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«بِنْتٌ».", "Present verb in the passive, in raf' by a damma estimated on the alif; its deputy doer the hidden «she» — the clause qualifies «a daughter».", "Meçhul muzâri, elif üzerinde takdîrî damme ile merfû; nâib-i fâil gizli «o» — cümle «kız»ın na'tı."),
  MAFUL("طَبَقَةَ", "tabaqa-name", "propn", ["mamnu-min-sarf", "mafulayn"], note_ar=" — وَهُوَ الْمَفْعُولُ الثَّانِي، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ", note_en=" — the second object; a feminine name, barred from tanwin", note_tr=" — ikinci mef'ûl; müennes alem, gayr-i munsarif", punct="،"),
  ISTI(MADI("فَسَأَلَتْ", "saala", ["mahmuz-verbs"], fem=True, hidden=True)),
  tok("أَبَاهَا", "ab", "noun", ["maful-bihi", "five-nouns", "idafa-definiteness", "al-bariz-al-muttasil"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The direct object, in nasb by the alif — one of the five nouns; annexed to «her».", "Mef'ûlün bih, esmâ-i hamseden olduğu için elif ile mansûb; «hâ» zamirine muzâf.", segments=[seg("أَبَا", "ab", "noun"), seg("هَا", "pron-3fs", "pron")]),
  PREP("عَنْ", "an", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سَأَلَتْ»", "; the phrase hangs on «asked»", "; câr-mecrûr «sordu»ya müteallik", gloss_tr="«hakkında»"),
  ENC_NOUN("ضَيْفِهِ", "dayf", "هِ", "majr", punct="،")]})
S2.append({"id": "s5", "translation": {"en": "and he said: «He is the most ignorant man I ever met», and told her his story.", "tr": "o da: «Gördüğüm insanların en cahilidir» dedi ve ona onun hikâyesini anlattı."},
 "tokens": [ISTI(QALA("فَقَالَ", hidden=True, punct=":")),
  tok("هُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.", "A detached pronoun built on fatha, the mubtada — the sentence is what is said.", "Munfasıl zamir, fetha üzere mebnî, mübtedâ — cümle mekūlü'l-kavl."),
  KHABAR("أَجْهَلُ", "ajhal", extra=["ism-tafdil"], note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ", note_en=", annexed — an elative («most ignorant»)", note_tr=", muzâf — ism-i tafdîl («en cahil»)"),
  tok("مَنْ", "man", "pron", ["ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The relative «whom», built on sukun, in the seat of jarr as the second term of the idafa.", "İsm-i mevsûl «men», sükûn üzere mebnî, muzâfun ileyh olarak mahallen mecrûr."),
  MADI_T("لَقِيتُ", "laqiya", who="ana", note_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ، وَالْعَائِدُ مَحْذُوفٌ: لَقِيتُهُ", note_en="; the clause is the ṣila, its returning pronoun left out", note_tr="; cümle sıla, âid zamir mahzûf"),
  PREP("مِنَ", "min", " — بَيَانِيَّةٌ، وَحُرِّكَتْ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ الْعَائِدِ الْمَحْذُوفِ", " — it explains the kind; fatha where two sukuns meet; the phrase hangs on an omitted hal of the left-out pronoun", "; beyân; iki sâkin yüzünden fethalı; câr-mecrûr mahzûf âidden hâle müteallik", gloss_tr="«-den»"),
  MAJR("النَّاسِ", "nas", punct="،"),
  MADI("وَقَصَّ", "qassa", ["doubled-verbs"], hidden=True),
  JARR_PRON("عَلَيْهَا", "ala", "عَلَيْ", "هَا", " («ona»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَصَّ»", note_en=" — the phrase hangs on «told»", note_tr=" — câr-mecrûr «anlattı»ya müteallik"),
  ENC_NOUN("خَبَرَهُ", "khabar", "هُ", "maful", punct=".")]})
S2.append({"id": "s6", "translation": {"en": "She said: «Father, this man is nothing but a learned and quick-witted man, and everything he said has a meaning.", "tr": "Kız dedi ki: «Babacığım, bu adam ancak bilgili ve zeki biridir; söylediği her şeyin bir anlamı vardır."},
 "tokens": [QALAT("فَقَالَتْ", punct=":"), YA(),
  tok("أَبَةِ", "ab", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالتَّاءُ عِوَضٌ عَنْ يَاءِ الْمُتَكَلِّمِ، مَبْنِيَّةٌ عَلَى الْكَسْرِ.", "A vocative annexed to the speaker's ya, which is dropped, in nasb by an estimated fatha; the ta stands in for the ya, built on kasra: «my father».", "Düşen mütekellim yâ'sına muzâf münâdâ, takdîrî fetha ile mansûb; tâ yâ'nın yerine gelmiştir, kesre üzere mebnî: «babacığım».", punct="،"),
  tok("مَا", "ma-nafiya", "part", ["anwa-ma", "istithna-mufarragh"], "حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ، بَطَلَ عَمَلُهُ بِانْتِقَاضِ النَّفْيِ بِـ«إِلَّا» — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.", "The negating مَا, built on sukun; it governs nothing, the negation being broken by «except» — the sentence is what is said.", "Nefy mâ'sı, sükûn üzere mebnî; nefy «illâ» ile bozulduğu için amel etmez — cümle mekūlü'l-kavl."),
  ISHARA("هٰذَا", "hadha", "رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "mübtedâ — merfû"),
  ILLA(),
  KHABAR("عَالِمٌ", "alim-scholar", extra=["ism-fail"]),
  NAAT("فَطِنٌ", "fatin-sharp", "raf", extra=["sifa-mushabbaha"], punct="،"),
  tok("وَلِكُلِّ", "li", "prep", ["huruf-jarr", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَكُلِّ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.", "The waw conjoins; the lam is a jarr letter and «every» is in jarr, annexed — the phrase hangs on an omitted, fronted predicate.", "«ve» + lâm cer harfi, «her» mecrûr, muzâf — câr-mecrûr öne alınmış mahzûf habere müteallik.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("كُلِّ", "kull", "noun")]),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The relative «what», built on sukun, in the seat of jarr as the second term of the idafa.", "İsm-i mevsûl «mâ», sükûn üzere mebnî, muzâfun ileyh olarak mahallen mecrûr."),
  ENC_MADI("قَالَهُ", "qala", "هُ", ["hollow-verbs"], hidden=True, note_ar=" — وَالْهَاءُ هِيَ الْعَائِدُ؛ وَالْجُمْلَةُ صِلَةُ «مَا»", note_en=" — «it» is the returning pronoun; the clause is the ṣila of «what»", note_tr=" — zamir âid; cümle «mâ»nın sılası"),
  tok("مَعْنًى", "mana", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِلتَّعَذُّرِ — اسْمٌ مَقْصُورٌ نَكِرَةٌ.", "The mubtada placed last, in raf' by a damma estimated on the alif (dropped before the tanwin) — an indefinite maqṣūr noun.", "Muahhar mübtedâ, (tenvin karşısında düşen) elif üzerinde takdîrî damme ile merfû — nekre maksûr isim.", punct=".")]})
S2.append({"id": "s7", "translation": {"en": "As for his words «Will you carry me, or shall I carry you?», he meant: will you talk to me or shall I talk to you, so that we put the weariness of travel off us.", "tr": "«Sen mi beni taşırsın, ben mi seni?» sözüyle şunu kastetti: Sen mi bana konuşursun, ben mi sana, ta ki yolculuğun yorgunluğunu üzerimizden atalım."},
 "tokens": [AMMA(), QAWLUHU(), ATAHMILUNI(note=(" — وَالْجُمْلَةُ مَحْكِيَّةٌ بَدَلٌ مِنْ «قَوْلُهُ»", " — the quoted clause is a badal of «his words»", " — nakledilen cümle «sözü»nden bedel")), AM(), MUDARI("أَحْمِلُكَ", "hamala", who="أَنَا", enc="كَ", wujub=True),
  tok("فَإِنَّهُ", "inna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "amma-tafsiliyya"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «قَوْلُهُ».", "The fa answers أَمَّا; إِنَّ with «he» as its noun — the clause is the predicate of «his words», in the seat of raf'.", "Fâ emmâ'nın cevabındadır; inne, «o» zamiri ismi — cümle «sözü»nün haberi, mahallen merfû.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  MADI("أَرَادَ", "arada", ["form-iv-verbs", "hollow-verbs"], hidden=True, punct=":", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", note_en=" — the clause is the predicate of إِنَّ", note_tr=" — cümle inne'nin haberi"),
  tok("أَتُحَدِّثُنِي", "haddatha", "verb", ["al-istifham", "mudari-marfu", "form-ii-verbs", "al-bariz-al-muttasil", "maful-bihi"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَتُحَدِّثُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«أَرَادَ».", "The hamza asks; «talk to» is a present verb in raf', its doer «you» hidden; the nun guards, the ya «me» is its object — the clause is the object of «meant».", "Hemze istifham; tuhaddisu merfû muzâri, fâil gizli «sen»; nûn vikâye, yâ mef'ûl — cümle «kastetti»nin mef'ûlü.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تُحَدِّثُ", "haddatha", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  AM(), MUDARI("أُحَدِّثُكَ", "haddatha", ["form-ii-verbs"], who="أَنَا", enc="كَ", wujub=True),
  tok("حَتَّى", "hatta", "part", ["ila-hatta-fi-wal-ba-fil-kafiya", "nawasib-wa-jawazim-al-mudari"], "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْمُضَارِعُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا.", "حَتَّى «so that», a particle of end and jarr; the present verb after it is in nasb by an أَنْ that must stay hidden.", "Hattâ gâye ve cer harfi; ondan sonraki muzâri vücûben gizli «en» ile mansûb."),
  MANSUB_AN("نُمِيطَ", "amata-remove", ["form-iv-verbs", "hollow-verbs"], who="نَحْنُ", by="أَنْ مُضْمَرَةٍ بَعْدَ حَتَّى", wujub=True, note_ar=" — وَأَمَاطَهُ: نَحَّاهُ وَأَزَالَهُ؛ وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى", note_en=" — أَمَاطَ: to remove, put away; the masdar so made is in jarr by حَتَّى", note_tr=" — emâta: gidermek, uzaklaştırmak; müevvel masdar hattâ ile mecrûr"),
  JARR_PRON("عَنَّا", "an", "عَنْ", "نَا", " («üzerimizden»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نُمِيطَ»", note_en=" — the phrase hangs on «put off»", note_tr=" — câr-mecrûr «atalım»a müteallik"),
  MAFUL("كَلَالَ", "lb-kalal", extra=["masdar"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("السَّفَرِ", "safar", punct=".")]})
S2.append({"id": "s8", "translation": {"en": "And as for his words «Has this crop been eaten?», what he means is: have its owners sold it and eaten its price, or not?", "tr": "«Bu ekin yenmiş mi?» sözüyle de şunu kastediyor: Sahipleri onu satıp parasını yediler mi, yemediler mi?"},
 "tokens": [WA_AMMA(), QAWLUHU(), AUKILA(), *HADHA_ZAR(), FA_INNAMA(),
  MUDARI("يُرِيدُ", "arada", ["form-iv-verbs", "hollow-verbs"], punct=":"),
  tok("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«يُرِيدُ».", "The question particle هَلْ — the clause is the object of «means».", "Hel istifham harfi — cümle «kastediyor»un mef'ûlü."),
  ENC_MADI("بَاعَهُ", "baa", "هُ", ["hollow-verbs"], note_ar="، وَالْفَاعِلُ بَعْدَهُ", note_en="; its doer follows", note_tr="; fâili sonra gelir"),
  ENC_NOUN("أَصْحَابُهُ", "sahib", "هُ", "fail", extra=["jam-taksir"]),
  tok("فَأَكَلُوا", "akala", "verb", ["al-bariz-al-muttasil", "fail"], "الْفَاءُ عَاطِفَةٌ، وَأَكَلَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "The fa conjoins; «ate» is a past verb built on damma before the waw of the group; that waw is its doer.", "«bunun üzerine» + ekele, cemâat vâvı yüzünden damme üzere mebnî mâzî; vâv fâil.", segments=[seg("فَ", "fa", "conj"), seg("أَكَلُ", "akala", "verb"), seg("وا", "pron-3mp", "pron")]),
  ENC_NOUN("ثَمَنَهُ", "thaman", "هُ", "maful"),
  tok("أَمْ", "am", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "أَمْ «or», a conjunction.", "Em «yoksa», atıf harfi."),
  tok("لَا", "la-nafiya", "part", ["la-nafiya", "hadhf-wa-taqdir"], "حَرْفُ نَفْيٍ، وَالْجُمْلَةُ بَعْدَهُ مَحْذُوفَةٌ.", "The negating لَا, its clause left out: «or not».", "Nefy harfi lâ; cümlesi mahzûf: «yoksa değil mi».", punct=".")]})
S2.append({"id": "s9", "translation": {"en": "And as for his words about the bier, «Do you see him living, or dead?», what he meant is: has he offspring through whom his memory will live on, or not?»", "tr": "Cenaze hakkındaki «Onu diri mi görüyorsun, ölü mü?» sözüyle de şunu kastetti: Adının yaşamasını sağlayacak bir zürriyeti var mı, yok mu?»"},
 "tokens": [WA_AMMA(), QAWLUHU(punct=None),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَوْلُهُ»", "; the phrase hangs on «his words»", "; câr-mecrûr «sözü»ne müteallik"), MAJR("الْجَنَازَةِ", "janaza", punct=":"),
  AHAYYAN(), TARA("تَرَاهُ", enc="هُ"), AM(), MAYYITAN(punct=None),
  FA_INNAMA(), MADI("أَرَادَ", "arada", ["form-iv-verbs", "hollow-verbs"], hidden=True, punct=":"),
  tok("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ — وَالْجُمْلَةُ مَفْعُولٌ بِهِ لِـ«أَرَادَ».", "The question particle هَلْ — the clause is the object of «meant».", "Hel istifham harfi — cümle «kastetti»nin mef'ûlü."),
  NOTE(LAHU("لَهُ", "pron-3ms", " («onun»)"), "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ", "; the phrase hangs on an omitted, fronted predicate", "; câr-mecrûr öne alınmış mahzûf habere müteallik"),
  MUBTADA("عَقِبٌ", "aqib-offspring", note_ar=" — مُؤَخَّرٌ؛ وَالْعَقِبُ: الْوَلَدُ وَوَلَدُ الْوَلَدِ", note_en=" — placed last; عَقِب: offspring, descendants", note_tr=" — muahhar; akib: zürriyet"),
  tok("يَحْيَا", "hayiya", "verb", ["mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«عَقِبٌ».", "Present verb in raf' by a damma estimated on the alif; its doer follows — the clause qualifies «offspring».", "Elif üzerinde takdîrî damme ile merfû muzâri; fâili sonra gelir — cümle «zürriyet»in na'tı."),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onunla»)", note_ar=" — وَالْهَاءُ هِيَ الرَّابِطُ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَحْيَا»", note_en=" — «it» is the binding pronoun; the phrase hangs on «live»", note_tr=" — zamir râbıt; câr-mecrûr «yaşar»a müteallik"),
  ENC_NOUN("ذِكْرُهُ", "dhikr", "هُ", "fail", extra=["masdar"]),
  tok("أَمْ", "am", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "أَمْ «or», a conjunction.", "Em «yoksa», atıf harfi."),
  tok("لَا", "la-nafiya", "part", ["la-nafiya", "hadhf-wa-taqdir"], "حَرْفُ نَفْيٍ، وَالْجُمْلَةُ بَعْدَهُ مَحْذُوفَةٌ.", "The negating لَا, its clause left out: «or not».", "Nefy harfi lâ; cümlesi mahzûf.", punct=".")]})
S2.append({"id": "s10", "translation": {"en": "The man went out to Shann and explained to him what he had hinted at to him;", "tr": "Adam Şenn'in yanına çıktı ve ona, kendisine ima ettiği şeyleri açıkladı;"},
 "tokens": [ISTI(MADI("فَخَرَجَ", "kharaja", **W(FAIL_BAAD))), FAIL("الرَّجُلُ", "rajul"),
  NOTE(ILA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«خَرَجَ»", "; the phrase hangs on «went out»", "; câr-mecrûr «çıktı»ya müteallik"), MAJR("شَنٍّ", "shann-name", "propn", note_ar=MUNSARIF[0], note_en=MUNSARIF[1], note_tr=MUNSARIF[2]),
  MADI("وَفَسَّرَ", "fassara", ["form-ii-verbs"], hidden=True), LAHU("لَهُ", "pron-3ms", " («ona»)"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "The relative «what», built on sukun, in the seat of nasb as the direct object.", "İsm-i mevsûl «mâ», sükûn üzere mebnî, mef'ûlün bih olarak mahallen mansûb."),
  NOTE(KANA("كَانَ"), " — وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (شَنٌّ)؛ وَالْجُمْلَةُ صِلَةُ «مَا»", "; its noun is the hidden «he» (Shann); the clause is the ṣila of «what»", "; ismi gizli «o» (Şenn); cümle «mâ»nın sılası"),
  MADI("رَمَزَ", "ramaza", hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", note_en=" — the clause is the predicate of كَانَ", note_tr=" — cümle kâne'nin haberi"),
  LAHU("لَهُ", "pron-3ms", " («ona»)"),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onu»)", note_ar=" — وَالْهَاءُ هِيَ الْعَائِدُ عَلَى «مَا»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«رَمَزَ»", note_en=" — «it» returns to «what»; the phrase hangs on «hinted»", note_tr=" — zamir «mâ»ya dönen âid; câr-mecrûr «ima etti»ye müteallik", punct="،")]})
S2.append({"id": "s11", "translation": {"en": "and Shann said: «You are not the owner of this sharpness — so tell me who its owner is.»", "tr": "Şenn de dedi ki: «Bu zekânın sahibi sen değilsin; bana sahibinin kim olduğunu haber ver.»"},
 "tokens": [QAL_SH(), SHANN("fail", punct=":"),
  tok("مَا", "ma-nafiya", "part", ["ma-la-laysa-wa-la-al-jins", "anwa-ma"], "مَا الْحِجَازِيَّةُ نَافِيَةٌ تَعْمَلُ عَمَلَ لَيْسَ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.", "The Ḥijāzī مَا, which negates and governs like لَيْسَ — the sentence is what is said.", "Hicâzî mâ: nefyeder ve leyse gibi amel eder — cümle mekūlü'l-kavl."),
  tok("أَنْتَ", "anta", "pron", ["ma-la-laysa-wa-la-al-jins", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ اسْمُ «مَا».", "A detached pronoun built on fatha, in the seat of raf' as the noun of مَا.", "Munfasıl zamir, fetha üzere mebnî, «mâ»nın ismi olarak mahallen merfû."),
  tok("بِصَاحِبِ", "bi", "prep", ["huruf-jarr", "ma-la-laysa-wa-la-al-jins", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَصَاحِبِ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا خَبَرُ «مَا»، مُضَافٌ.", "The ba is an extra jarr letter; «owner» is in jarr in form and in nasb in its seat, as the predicate of مَا; annexed.", "Bâ zâid cer harfi; «sahip» lafzen mecrûr, mahallen mansûb — «mâ»nın haberi; muzâf.", segments=[seg("بِ", "bi", "prep"), seg("صَاحِبِ", "sahib", "noun")]),
  ISHARA("هٰذِهِ", "hadhihi", "جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "muzâfun ileyh — mecrûr", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre"),
  BADAL("الْفِطْنَةِ", "fitna-wit", "jarr", punct="،"),
  AMR("فَأَنْبِئْنِي", "anbaa", ["form-iv-verbs", "mahmuz-verbs"], enc="نِي", wiqaya=True, note_ar=" — وَالْفَاءُ فَصِيحَةٌ", note_en=" — the fa «so» discloses the unstated condition", note_tr=" — fâ fasîha"),
  tok("مَنْ", "man", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ — وَالْجُمْلَةُ سَدَّتْ مَسَدَّ مَفْعُولَيْ «أَنْبِئْنِي» الثَّانِي وَالثَّالِثِ.", "The question word «who», built on sukun, in the seat of raf' as a fronted predicate — the clause stands for the second and third objects of «tell me».", "İstifham ismi «men», sükûn üzere mebnî, öne alınmış haber olarak mahallen merfû — cümle «haber ver»in ikinci ve üçüncü mef'ûlleri yerini tutar."),
  ENC_NOUN("صَاحِبُهَا", "sahib", "هَا", "mubtada", note_ar=" — مُؤَخَّرٌ", note_en=" — placed last", note_tr=" — muahhar", punct=".")]})
S2.append({"id": "s12", "translation": {"en": "He said: «A daughter of mine.»", "tr": "Adam: «Bir kızım» dedi."},
 "tokens": [MADI("قَالَ", "qala", ["hollow-verbs", "maful-bihi"], hidden=True, punct=":", note_ar=HID(*RJ)[0], note_en=HID(*RJ)[1], note_tr=HID(*RJ)[2]),
  tok("بِنْتٌ", "bint", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ: هِيَ بِنْتٌ، مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.", "The predicate of an omitted mubtada («she is a daughter»), in raf' — the sentence is what is said.", "Mahzûf mübtedânın haberi («o bir kızdır»), merfû — cümle mekūlü'l-kavl."),
  tok("لِي", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "ya-al-mutakallim"], "اللَّامُ حَرْفُ جَرٍّ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«بِنْتٌ».", "The lam is a jarr letter, and the ya «me» fills the seat of jarr — the phrase hangs on an omitted adjective of «a daughter».", "Lâm cer harfi; yâ mahallen mecrûr — câr-mecrûr «kız»ın mahzûf na'tına müteallik.", punct=".", segments=[seg("لِ", "li", "prep"), seg("ي", "pron-1s", "pron")])]})
S2.append({"id": "s13", "translation": {"en": "So he asked for her hand, and he gave her to him in marriage;", "tr": "Bunun üzerine Şenn onu istedi; babası da onu Şenn'e nikâhladı;"},
 "tokens": [ISTI(ENC_MADI("فَخَطَبَهَا", "khataba-sermon", "هَا", hidden=True, note_ar=" — يَعُودُ عَلَى شَنٍّ؛ وَخَطَبَ الْمَرْأَةَ: طَلَبَهَا لِلزَّوَاجِ", note_en=" (Shann) — خَطَبَ الْمَرْأَةَ: to ask for a woman's hand", note_tr=" (Şenn) — hatabe'l-mer'e: kadını nikâh için istemek", punct="،")),
  ENC_MADI("فَأَنْكَحَهَا", "ankaha", "هَا", ["form-iv-verbs"], hidden=True, note_ar=" — يَعُودُ عَلَى الرَّجُلِ؛ وَأَنْكَحَهُ إِيَّاهَا: زَوَّجَهُ", note_en=" (the man) — أَنْكَحَ: to give in marriage", note_tr=" (adam) — enkaha: nikâhlamak, evlendirmek"),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ona»)", note_ar=" — كَذَا فِي الْمَطْبُوعِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَنْكَحَهَا»", note_en=" — so the print; the phrase hangs on «gave her in marriage»", note_tr=" — baskıda böyle; câr-mecrûr «nikâhladı»ya müteallik", punct="،")]})
S2.append({"id": "s14", "translation": {"en": "and she was called Ṭabaqa; and the people said: «Shann has met Ṭabaqa — he matched her and so embraced her.»", "tr": "kızın adı Tabaka idi; insanlar da: «Şenn Tabaka'yı buldu; ona uydu ve onu kucakladı» dediler."},
 "tokens": [ISTI(tok("وَكَانَتْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ.", "The waw conjoins; كَانَ, the defective past verb, the ta marking the feminine; its noun the hidden «she».", "«ve» + kâne nâkıs mâzî, tâ te'nîs; ismi gizli «o».", segments=[seg("وَ", "wa", "conj"), seg("كَانَتْ", "kana", "verb")])),
  tok("تُسَمَّى", "samma", "verb", ["naib-al-fail", "form-ii-verbs", "naqis-verbs", "mudari-marfu", "mafulayn"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "Present verb in the passive, in raf' by a damma estimated on the alif; its deputy doer the hidden «she» — the clause is the predicate of كَانَ.", "Meçhul muzâri, elif üzerinde takdîrî damme ile merfû; nâib-i fâil gizli «o» — cümle kâne'nin haberi."),
  MAFUL("طَبَقَةَ", "tabaqa-name", "propn", ["mamnu-min-sarf", "mafulayn"], note_ar=" — وَهُوَ الْمَفْعُولُ الثَّانِي، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ", note_en=" — the second object; a feminine name, barred from tanwin", note_tr=" — ikinci mef'ûl; müennes alem, gayr-i munsarif", punct="،"),
  ISTI(MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD))), FAIL("النَّاسُ", "nas", punct=":"),
  NOTE(MADI("وَافَقَ", "wafaqa", ["form-iii-verbs"], **W(FAIL_BAAD)), MAQUL[0], MAQUL[1], MAQUL[2]), SHANN("fail"),
  MAFUL("طَبَقَةَ", "tabaqa-name", "propn", ["mamnu-min-sarf"], note_ar=" — عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ", note_en=" — a feminine name, barred from tanwin", note_tr=" — müennes alem, gayr-i munsarif", punct="،"),
  ENC_MADI("وَافَقَهُ", "wafaqa", "هُ", ["form-iii-verbs"], hidden=True, note_ar=" — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ مِنْ تَمَامِ الْمَثَلِ", note_en=" — the clause goes on with the rest of the proverb", note_tr=" — cümle atasözünün devamı olarak müste'nefedir"),
  ENC_MADI("فَاعْتَنَقَهُ", "itanaqa", "هُ", ["form-viii-verbs"], hidden=True, punct=".")]})

NEW_GLOSS = {
 "shann-name": NP("شَنّ", "Shann — a man's name, fully declined; in al-Sharqī's tale a shrewd Arab who sought a wife as clever as himself", "Şenn — erkek ismi, munsarif; eş-Şarkî'nin hikâyesinde kendisi kadar akıllı bir eş arayan zeki bir Arap", level=5),
 "tabaqa-name": NP("طَبَقَة", "Ṭabaqa — a woman's name, a diptote; the clever girl of the tale who read Shann's riddles", "Tabaka — kadın ismi, gayr-i munsarif; hikâyede Şenn'in bilmecelerini çözen zeki kız", level=5),
 "sharqi-name": NP("الشَّرْقِيّ", "al-Sharqī — al-Sharqī ibn al-Quṭāmī, the Kufan reporter of Arab lore and genealogy (2nd c. AH)", "eş-Şarkî — Kûfeli ahbâr ve neseb râvîsi eş-Şarkî b. el-Kutâmî (h. II. asır)", level=5),
 "qutami": NP("الْقُطَامِيّ", "al-Quṭāmī — the father of al-Sharqī ibn al-Quṭāmī", "el-Kutâmî — eş-Şarkî b. el-Kutâmî'nin babası", level=5),
 "dahiya": NN("دَاهِيَة", "د ه ي", "a man of shrewd, far-seeing judgement; pl. دُهَاة", "dâhî, uzak görüşlü zeki adam; çoğ. دُهَاة", level=5),
 "ityan": NN("إِتْيَان", "أ ت ي", "coming to, going to (masdar of أَتَى)", "gelme, varma (etâ'nın masdarı)", level=5),
 "istajhala": NV("اِسْتَجْهَلَ", "ج ه ل", "X", "to think (a man) a fool (Form X)", "(birini) cahil saymak (istif'âl bâbı)", level=5),
 "istijhal": NN("اِسْتِجْهَال", "ج ه ل", "thinking someone a fool (masdar of اسْتَجْهَلَ)", "birini cahil sayma (istechele'nin masdarı)", level=5),
 "rafiq-companion": NN("رَفِيق", "ر ف ق", "a companion on the road, a fellow traveller", "yol arkadaşı, refik", level=5),
 "istahsada": NV("اِسْتَحْصَدَ", "ح ص د", "X", "(of a crop) to be ready for reaping (Form X)", "(ekin) hasat vaktine gelmek (istif'âl bâbı)", level=5),
 "talaqqa": NV("تَلَقَّى", "ل ق ي", "V", "to meet, to come to meet; to receive (Form V, defective)", "karşılamak, karşısına çıkmak; almak (tefa''ul bâbı, nâkıs)", level=5),
 "ajhal": NN("أَجْهَل", "ج ه ل", "more / most ignorant (elative of جَاهِل)", "daha / en cahil (ism-i tafdîl)", level=5),
 "amata-remove": NV("أَمَاطَ", "م ي ط", "IV", "to remove, to put away (عَنْ: from) (Form IV, hollow)", "(عَنْ: -den) gidermek, uzaklaştırmak (if'âl bâbı, ecvef)", level=5),
 "aqib-offspring": NN("عَقِب", "ع ق ب", "offspring, descendants who carry on a man's name", "zürriyet, kişinin adını yaşatan nesil", level=5),
 "fitna-wit": NN("فِطْنَة", "ف ط ن", "quick wit, sharpness of mind", "zekâ, uyanıklık", level=5),
 "ramaza": NV("رَمَزَ", "ر م ز", "I", "to hint, to speak in riddles (لَهُ بِـ: to a man, with a thing) — رَمَزَ يَرْمُزُ", "ima etmek, rumuzla konuşmak — ramaza yarmuzu", level=5),
 "ankaha": NV("أَنْكَحَ", "ن ك ح", "IV", "to give (a woman) in marriage (Form IV)", "(kadını) nikâhla vermek, evlendirmek (if'âl bâbı)", level=5),
}
GLOSS_HERE = {
 "shann-tf": ("a worn-out waterskin (pl. شِنَان) — in Abū ʿUbayd's reading of وَافَقَ شَنًّا طَبَقُهُ «the waterskin met its lid»", "eskimiş kırba (çoğ. شِنَان) — Ebû Ubeyd'in وَافَقَ شَنًّا طَبَقُهُ yorumunda «kırba kapağını buldu»"),
 "tabaq-amr": ("a dish, a tray; a cover, a lid (pl. أَطْبَاق)", "tabak, tepsi; kapak (çoğ. أَطْبَاق)"),
 "nash-ant": ("a raised frame; a bier (on which the dead are carried)", "yükseltilmiş iskelet; tabut, na'ş"),
 "adala": ("to be just; عَدَلَ إِلَى: to turn aside towards", "adaletli olmak; عَدَلَ إِلَى: bir yere yönelmek"),
 "khataba-sermon": ("to address, to preach; خَطَبَ الْمَرْأَةَ: to ask for a woman's hand", "hitap etmek, hutbe okumak; خَطَبَ الْمَرْأَةَ: kadını nikâh için istemek"),
}
V = {"istajhala": SG.derived(SG.B10, SG.W10, "َ", "اِسْتَجْهَل", "سْتَجْهِل", "اِسْتَجْهِل", "اِسْتِجْهَال", "مُسْتَجْهِل", "مُسْتَجْهَل", "اُسْتُجْهِلَ", "يُسْتَجْهَلُ"),
     "istahsada": SG.derived(SG.B10, SG.W10, "َ", "اِسْتَحْصَد", "سْتَحْصِد", "اِسْتَحْصِد", "اِسْتِحْصَاد", "مُسْتَحْصِد", None, None, None, "لَازِمٌ: اسْتَحْصَدَ الزَّرْعُ — حَانَ حَصَادُهُ."),
     "talaqqa": SG.derived_naqis(SG.B5 + " — نَاقِصٌ", SG.W5, "َ", "تَلَقَّ", "تَلَقّ", "a", "تَلَقّ", "تَلَقٍّ (التَّلَقِّي)", "مُتَلَقٍّ", "مُتَلَقًّى", "تُلُقِّيَ", "يُتَلَقَّى", "نَاقِصٌ يَائِيٌّ مِنَ التَّفَعُّلِ: تَلَقَّى يَتَلَقَّى."),
     "amata-remove": SG.derived_hollow(SG.B4 + " — أَجْوَفُ يَائِيٌّ", SG.W4, "ُ", "أَمَاط", "أَمَط", "مِيط", "مِط", "أَمِيط", "أَمِط", "إِمَاطَة", "مُمِيط", "مُمَاط", "أُمِيطَ", "يُمَاطُ"),
     "ramaza": SG.sound1("nasara", "رَمَز", "رْمُز", "اُرْمُز", "رَمْز", "رَامِز", "مَرْمُوز", "رُمِزَ", "يُرْمَزُ"),
     "ankaha": SG.derived(SG.B4, SG.W4, "ُ", "أَنْكَح", "نْكِح", "أَنْكِح", "إِنْكَاح", "مُنْكِح", "مُنْكَح", "أُنْكِحَ", "يُنْكَحُ")}
FOR_HOCA = [
 ("the heading «وَافَقَ شَنًّا طَبَقُهُ» as the print's tanwīn shows (Abū ʿUbayd: the waterskin and its lid); the tale's close reads «وَافَقَ شَنٌّ طَبَقَةَ»", "başlık «وَافَقَ شَنًّا طَبَقُهُ», baskıdaki tenvinin gösterdiği gibi (Ebû Ubeyd: kırba ve kapağı); hikâyenin sonu «وَافَقَ شَنٌّ طَبَقَةَ»"),
 ("«أَحَيًّا تَرَى مَنْ عَلَى هٰذَا النَّعْشِ أَوْ مَيِّتًا»: «حَيًّا» read as a fronted ḥāl (or a second object of تَرَى)", "«أَحَيًّا تَرَى …»: «حَيًّا» öne alınmış hâl okundu (ya da terâ'nın ikinci mef'ûlü)"),
 ("«وَعَدَلَ إِلَى مَنْزِلٍ بِهِ»: whose house, and what «بِهِ» refers to", "«وَعَدَلَ إِلَى مَنْزِلٍ بِهِ»: kimin evi ve «بِهِ»nin mercii"),
 ("«فَأَنْكَحَهَا مِنْهُ» kept as printed (the usual is «أَنْكَحَهُ إِيَّاهَا»)", "«فَأَنْكَحَهَا مِنْهُ» baskıdaki gibi bırakıldı (bilinen kullanım «أَنْكَحَهُ إِيَّاهَا»)"),
 ("«يَا أَبَةِ» with the ta standing for the speaker's ya, as the print spells it", "«يَا أَبَةِ»: baskının yazımıyla, mütekellim yâ'sı yerine tâ"),
 ("the bracketed «[وَسَارَا حَتَّى قَرُبَا مِنْ قَرْيَةٍ]» (the editor's supplement from manuscript س) repeats an earlier clause — kept as printed", "köşeli «[وَسَارَا حَتَّى قَرُبَا مِنْ قَرْيَةٍ]» (muhakkikin س nüshasından ilâvesi) önceki bir cümleyi tekrarlar — baskıdaki gibi bırakıldı"),
]
MANIFEST = manifest(SLUG, level=5, title={"ar": "وَافَقَ شَنٌّ طَبَقَةَ", "en": "Shann Met Ṭabaqa", "tr": "Şenn Tabaka'yı Buldu"},
    subtitle={"ar": "شَنٌّ وَأَلْغَازُهُ، وَطَبَقَةُ الَّتِي فَسَّرَتْهَا — مِنْ «فَصْلِ الْمَقَالِ» لِلْبَكْرِيِّ، نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "Shann's riddles and Ṭabaqa who read them — from al-Bakrī's Faṣl al-maqāl, the received text, word for word",
              "tr": "Şenn'in bilmeceleri ve onları çözen Tabaka — Bekrî'nin Faslü'l-makāl'inden, lafzıyla"},
    pages="pp. 274–276 (printed 1:262–264), bāb 7", pages_ar="ص ٢٧٤–٢٧٦ (الْمَطْبُوعُ ١: ٢٦٢–٢٦٤)، الْبَابُ السَّابِعُ",
    span_en="Abū ʿUbayd's proverb as the heading; al-Sharqī ibn al-Quṭāmī's account in al-Bakrī's commentary, whole and in order, from «وذكر الشرقي بن القطامي فيه قولاً رابعاً» to «وافقه فاعتنقه», cut into two chapters at «فدخلا القرية» (the other three accounts are not taken); at about 250 words it runs past the shelf's usual length and is taken whole rather than cut",
    span_tr="Başlıkta Ebû Ubeyd'in atasözü; Bekrî'nin şerhindeki eş-Şarkî b. el-Kutâmî rivâyeti tamamen ve sırasıyla, «وذكر الشرقي بن القطامي فيه قولاً رابعاً»den «وافقه فاعتنقه»ye; «فدخلا القرية»da iki bölüme ayrıldı (diğer üç görüş alınmadı); yaklaşık 250 kelimeyle rafın olağan uzunluğunu aşar, kesilmeden alındı",
    span_ar="الْمَثَلُ عُنْوَانًا، ثُمَّ قَوْلُ الشَّرْقِيِّ بْنِ الْقُطَامِيِّ كُلُّهُ عَلَى تَرْتِيبِهِ إِلَى «وَافَقَهُ فَاعْتَنَقَهُ»، مَقْسُومًا فَصْلَيْنِ عِنْدَ «فَدَخَلَا الْقَرْيَةَ»",
    corrections=[("وأنا ركب", "وَأَنَا رَاكِبٌ")],
    witness_ar="«مَجْمَعُ الْأَمْثَالِ» لِلْمَيْدَانِيِّ (الشَّامِلَةُ ١٢٩٢٩، ٢: ٣٥٩، رَقْمُ ٤٣٤٠)", witness_en="al-Maydānī's Majmaʿ al-amthāl (Shamela 12929, 2:359, § 4340: «أنا راكب وأنت راكب»)", witness_tr="Meydânî, Mecmau'l-emsâl (Şâmile 12929, 2:359, § 4340: «أنا راكب وأنت راكب»)",
    kept=[("زِيَادَةُ الْمُحَقِّقِ «[وَسَارَا حَتَّى قَرُبَا مِنْ قَرْيَةٍ]»", "the editor's bracketed supplement «[وسارا حتى قربا من قرية]» (from manuscript س)", "muhakkikin köşeli ilâvesi «[وسارا حتى قربا من قرية]» (س nüshasından)"),
          ("«فَأَنْكَحَهَا مِنْهُ»", "«فأنكحها منه»", "«فأنكحها منه»")],
    hoca=FOR_HOCA)
finish(SLUG, TITLES, [S1, S2], NEW_GLOSS, MANIFEST, GLOSS_HERE, V_NEW=V)
