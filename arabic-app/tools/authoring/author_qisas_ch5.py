# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 5: «إِلَى مَكَّةَ» — sections 11–13 of «من كسر الأصنام؟» (print pp. 18–21): the call to
the father (Maryam 19:42, 19:44 and 19:47 quoted as the print sets them and marked), the journey to Mecca with Hājar, and the well
of Zamzam. Every printed line is one sentence (the long closing line of §13 is cut at its own pauses); the vowelling is the print's.
python3 tools/authoring/author_qisas_ch5.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "إِلَى مَكَّةَ", "en": "To Mecca", "tr": "Mekke'ye"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

# ---------------------------------------------------------------- local helpers
def ibrahim_fail(punct=None): return fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=punct)
def ibrahim_jarr_mudaf(punct=None):
    return tok("إِبْرَاهِيمَ", "ibrahim", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ibrāhīm» — the annexed noun; a diptote, so its jarr is a fatḥa.", "«İbrâhim'in» — muzâfun ileyh; gayr-ı munsarif, cerri fetha ile.", punct=punct)
def name_fail(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", ["fail", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the doer; a diptote name.", tr + " — fâil; gayr-ı munsarif alem.", punct=punct)
def name_maful(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "propn", ["maful-bihi", "mamnu-min-sarf"] + list(tags), "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the object; a diptote name.", tr + " — mef'ûl; gayr-ı munsarif alem.", punct=punct)
def name_badal(full, lex, en, tr, case, punct=None):
    C = {"raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "rafʿ", "merfû"), "nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "naṣb", "mansub")}[case]
    return tok(full, lex, "propn", ["badal", "mamnu-min-sarf"], f"بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) {C[0]} — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + f" — the badal of the noun before it, in {C[1]}; a diptote name.", tr + f" — öncesindeki ismin bedeli, {C[2]}; gayr-ı munsarif alem.", punct=punct)
def makka_jarr(punct=None, prep="إِلَى"):
    return tok("مَكَّةَ", "makka", "propn", ["huruf-jarr", "mamnu-min-sarf"], f"مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Mecca» — in jarr by the fatḥa: a feminine proper name, a diptote.", "«Mekke» — fetha ile mecrur: müennes alem, gayr-ı munsarif.", punct=punct)
def zamzam_mudaf_ilayh(punct=None):
    return tok("زَمْزَمَ", "zamzam", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Zamzam» — the annexed noun; a diptote, so its jarr is a fatḥa.", "«Zemzem» — muzâfun ileyh; gayr-ı munsarif, cerri fetha ile.", punct=punct)
def kanat_makka(punct=None):
    return [tok("وَكَانَتْ", "kana", "verb", [K, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and … was» — kāna with the feminine tāʾ.", "«ve … idi» — te'nis tâ'sıyla kâne.", segments=[seg("وَ", "wa", "conj"), seg("كَانَتْ", "kana", "verb")]),
            tok("مَكَّةُ", "makka", "propn", [K, "mamnu-min-sarf"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Mecca» — kāna's ism, in rafʿ (no tanwīn: a diptote).", "«Mekke» — kâne'nin ismi, merfû (tenvinsiz: gayr-ı munsarif).")]
def laysa_fiha():
    return [tok("لَيْسَ", "laysa", "verb", [K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«there is not» — the frozen laysa; its clause is kāna's khabar.", "«yoktur» — câmid leyse; cümlesi kâne'nin haberi."),
            tok("فِيهَا", "fi", "prep", ["huruf-jarr", K], "فِي حَرْفُ جَرٍّ، وَهَا ضَمِيرٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ لَيْسَ مُقَدَّمٌ.", "«in it» — the jarr phrase is laysa's khabar, fronted.", "«onda» — câr-mecrur leyse'nin öne alınmış haberi.", segments=[seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")])]
def laysa_ism(full, lex, en, tr, punct=None):
    return tok(full, lex, "noun", [K], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", en + " — laysa's ism, delayed, in rafʿ.", tr + " — leyse'nin te'hir edilmiş ismi, merfû.", punct=punct)
def wa_la_atf(full, lex, en, tr, punct=None):
    return [la_nafiya("وَلَا", wa=True),
            tok(full, lex, "noun", ["atf-nasaq", K], "مَعْطُوفٌ عَلَى اسْمِ لَيْسَ مَرْفُوعٌ بِالضَّمَّةِ.", en + " — joined to laysa's ism, in rafʿ.", tr + " — leyse'nin ismine atıf, merfû.", punct=punct)]
def ya_abati(punct=None):
    return [tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi."),
            tok("أَبَتِ", "ab", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالتَّاءُ عِوَضٌ عَنْ يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَهِيَ مُضَافٌ إِلَيْهِ.", "«O my father» — a munādā annexed to the speaker's yāʾ, whose tāʾ stands in for the dropped yāʾ; naṣb estimated.", "«ey babacığım» — mütekellim yâsına muzâf münâdâ; tâ hazfedilmiş yânın bedeli; nasb takdîrî.", punct=punct)]
def lima(full="لِمَ", wa=False):
    return tok(full, "ma-istifham", "pron", ["al-istifham", "huruf-jarr"], W(wa) + "اللَّامُ حَرْفُ جَرٍّ، وَمَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، حُذِفَتْ أَلِفُهَا لِدُخُولِ الْجَارِّ.", Wen(wa) + "«why?» — the jarr lām on the interrogative mā, whose alif drops after a preposition.", Wtr(wa) + "«niçin?» — istifhâm mâ'sı üzerinde cer lâmı; harf-i cerden sonra elifi düşer.",
               segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("لِ", "li", "prep"), seg("مَ", "ma-istifham", "pron")])
def ma_mawsula(punct=None):
    return tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what» — the relative noun, built; the object of «worship».", "«-i (şey ki)» — ism-i mevsûl, mebnî; «tapmak»ın mef'ûlü.", punct=punct)
def sila_la(verb, lex, en, tr, wa=False, punct=None, tags=(), muq=False):
    return [la_nafiya("وَلَا" if wa else "لَا", wa=wa),
            tok(verb, lex, "verb", ["la-nafiya", "mudari-marfu"] + list(tags), ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ" if muq else "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ") + " بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — " + ("مَعْطُوفٌ عَلَى صِلَةِ الْمَوْصُولِ" if wa else "وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا") + ".",
                en + " — rafʿ after the negating lā; the doer «it» is concealed" + (" — joined to the ṣila" if wa else " — the clause is the relative's ṣila") + ".", tr + " — nefiy lâ'sından sonra merfû; fâil gizli «o»" + (" — sılaya atıf" if wa else " — cümle sıladır") + ".", punct=punct)]
def mudari_ana(full, lex, en, tr, tags=(), punct=None, wa=False, extra="", khabar=True):
    return tok(full, lex, "verb", ["mudari-marfu"] + list(tags), W(wa) + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنَا" + extra + (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ" if khabar else "") + ".",
               Wen(wa) + en + " — a muḍāriʿ in rafʿ; the doer «I» is concealed by necessity" + ("; the clause is the khabar" if khabar else "") + ".", Wtr(wa) + tr + " — merfû muzâri; fâil vücûben gizli «ben»" + ("; cümle haberdir" if khabar else "") + ".", punct=punct)
def ana_mubtada(full="أَنَا", punct=None):
    return tok(full, "pron-1s-munfasil", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«I» — the detached pronoun, the mubtadaʾ.", "«ben» — munfasıl zamir, mübtedâ.", punct=punct)
def an_nasb(full, lex, en, tr, tags=(), punct=None, wa=False, obj="", muq=False, extra=""):
    """أَنْ يَدْعُوَ، وَيَعْبُدَ — the an-verb and its joined fellows, the doer concealed."""
    return tok(full, lex, "verb", ["an-masdariyya"] + (["atf-nasaq"] if wa else []) + list(tags), W(wa) + ("فِعْلٌ مُضَارِعٌ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ" if wa else ("فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ" + (" الظَّاهِرَةُ عَلَى الْوَاوِ" if muq else ""))) + "، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ" + extra + ".",
               Wen(wa) + en + (" — joined to the an-verb, in naṣb" if wa else " — in naṣb after an") + "; the doer «he» is concealed.", Wtr(wa) + tr + (" — en'li fiile atıf, mansub" if wa else " — en ile mansub") + "; fâil gizli «o».", punct=punct,
               segments=([seg("وَ", "wa", "conj"), seg(full[1:], lex, "verb")] if wa else None))
def malik_fail(punct=None): return fail("الْمَلِكُ", "malik-king", "«the king»", "«kral»", punct=punct)
def walid_fail(punct=None):
    return tok("وَالِدُ", "walid-father", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the father» — the doer, a muḍāf.", "«babası» — fâil, muzâf.", punct=punct)
def hajar(case, punct=None, role=None):
    R = {"raf": ("فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", "the doer, in rafʿ", "fâil, merfû", ["fail"]), "nasb": ("مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "the object, in naṣb", "mef'ûl, mansub", ["maful-bihi"]), "kanaIsm": ("اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ", "kāna's ism, in rafʿ", "kâne'nin ismi, merfû", [K])}[role or case]
    return tok("هَاجَرُ" if case == "raf" else "هَاجَرَ", "hajar-name", "propn", R[3] + ["mamnu-min-sarf"], R[0] + " — عَلَمٌ أَعْجَمِيٌّ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Hājar» — " + R[1] + "; a foreign feminine name, a diptote.", "«Hâcer» — " + R[2] + "; yabancı müennes alem, gayr-ı munsarif.", punct=punct)
def huna(punct=None, wa=False):
    return tok("وَهُنَا" if wa else "هُنَا", "huna", "noun", ["maful-fih"], W(wa) + "اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ.", Wen(wa) + "«here» — the demonstrative of place, built; an adverb of place.", Wtr(wa) + "«burada» — mekân ism-i işâreti, mebnî; mekân zarfı.", punct=punct, segments=([seg("وَ", "wa", "conj"), seg("هُنَا", "huna", "noun")] if wa else None))

# ================================================================ §11 دعوة الوالد (pp. 18–19)
sen("s1", "And Ibrāhīm wanted to call his father too, so he said to him:", "Ve İbrâhim babasını da davet etmek istedi; ona dedi:", [
  mazi("وَأَرَادَ", "arada", "«wanted»", "«istedi»", hidden=None, wa=True, tags=["form-iv-verbs", "hollow-verbs"]), ibrahim_fail(),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِأَرَادَ.", "«to» — the subjunctive maṣdar particle; the clause is the object of «wanted».", "«-meyi» — nasb eden masdariyye harfi; te'vilî masdar «istedi»nin mef'ûlü."),
  an_nasb("يَدْعُوَ", "daa", "«call»", "«davet etsin»", tags=["naqis-verbs"], muq=True),
  tok("وَالِدَهُ", "walid-father", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — the object; annexed to the pronoun.", "«babasını» — mef'ûl; zamire muzâf.", segments=[seg("وَالِدَ", "walid-father", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ (آضَ) مَنْصُوبٌ بِالْفَتْحَةِ.", "«too» — an absolute object of a dropped verb.", "«de» — hazfedilmiş fiilin mef'ûl-i mutlakı.", punct="،"),
  qala("فَقَالَ", punct=None, wa=True, hidden="هُوَ"),
  tok("لَهُ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ جَرٍّ.", "«to him».", "«ona».", punct=":", segments=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")])])
# (the fāʾ of فَقَالَ is read from the surface by qala() itself — the index-5 patch that once sat here landed on أَيْضًا)

sen("s2", "«O my father, why do you worship what neither hears nor sees?» (Maryam 19:42)", "«Ey babacığım, ne işitmeyen ne gören şeye niçin tapıyorsun?» (Meryem 19:42)", quran(ya_abati() + [
  lima(), tok("تَعْبُدُ", "abada", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«do you worship» — the doer «you» is concealed by necessity.", "«tapıyorsun» — fâil vücûben gizli «sen»."),
  ma_mawsula()] + sila_la("يَسْمَعُ", "samia", "«hears»", "«işitir»") + sila_la("يُبْصِرُ", "absara", "«sees»", "«görür»", wa=True, tags=["form-iv-verbs"], punct=".")))
sen("s3", "And why do you worship what neither benefits nor harms?", "Ve ne fayda veren ne zarar veren şeye niçin tapıyorsun?", [
  lima("وَلِمَ", wa=True), tok("تَعْبُدُ", "abada", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«do you worship».", "«tapıyorsun»."),
  ma_mawsula()] + sila_la("يَنْفَعُ", "nafaa", "«benefits»", "«fayda verir»") + sila_la("يَضُرُّ", "darra", "«harms»", "«zarar verir»", wa=True, tags=["doubled-verbs"], punct="."))
sen("s4", "«O my father, do not worship Satan!» (19:44)", "«Ey babacığım, şeytana tapma!» (19:44)", quran(ya_abati() + [
  tok("لَا", "la-nafiya", "part", ["la-nahiya"], "لَا النَّاهِيَةُ، حَرْفُ جَزْمٍ.", "«do not» — the prohibiting lā: it governs jazm.", "«-me» — nehiy lâ'sı: cezm eder."),
  tok("تَعْبُدِ", "abada", "verb", ["la-nahiya", "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَكُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«worship» — jazm by sukūn after the prohibiting lā; the sukūn turns to kasra before the article's silent alif.", "«tapma» — nehiy lâ'sıyla meczum; iki sâkin karşılaştığı için kesre aldı."),
  maful("الشَّيْطَانَ", "shaytan", "«Satan»", "«şeytana»", punct="!")]))
sen("s5", "O my father, worship the Most Merciful!", "Ey babacığım, Rahmân'a tap!", ya_abati() + [
  tok("اعْبُدِ", "abada", "verb", ["imperative-amr"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَكُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«worship!» — an imperative built on sukūn (kasra before the article's silent alif).", "«tap!» — sükûn üzere mebnî emir (harf-i tariften önce kesre)."),
  tok("الرَّحْمٰنَ", "rahman", "propn", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the Most Merciful» — the object.", "«Rahmân'a» — mef'ûl.", punct="!")])
sen("s6", "And Ibrāhīm's father grew angry and said: I will beat you — so leave me, and do not say a word.", "Ve İbrâhim'in babası öfkelendi ve dedi: Seni döverim; beni bırak ve bir şey söyleme.", [
  mazi("وَغَضِبَ", "ghadiba", "«grew angry»", "«öfkelendi»", hidden=None, wa=True), walid_fail(), ibrahim_jarr_mudaf(punct="،"),
  qala("وَقَالَ", wa=True, hidden="هُوَ"),
  ana_mubtada(),
  tok("أَضْرِبُكَ", "daraba", "verb", ["mudari-marfu", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْكَافُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ.", "«I will beat you» — the doer «I» concealed; the kāf is its object; the clause is the khabar.", "«seni döverim» — fâil gizli «ben»; kâf mef'ûl; cümle haber.", punct="،", segments=[seg("أَضْرِبُ", "daraba", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("فَاتْرُكْنِي", "taraka", "verb", ["imperative-amr", "ya-al-mutakallim", "maful-bihi"], "الْفَاءُ لِلتَّفْرِيعِ، وَاتْرُكْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«so leave me» — an imperative; the nūn of protection before the speaker's yāʾ, its object.", "«öyleyse beni bırak» — emir; mütekellim yâsından önce vikâye nûnu; yâ mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("اتْرُكْ", "taraka", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("وَلَا", "la-nafiya", "part", ["la-nahiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا النَّاهِيَةُ حَرْفُ جَزْمٍ.", "«and do not» — the prohibiting lā.", "«ve -me» — nehiy lâ'sı.", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("تَقُلْ", "qala", "verb", ["la-nahiya", "hollow-verbs", "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«say» — jazm by sukūn; the hollow verb drops its wāw before the sukūn (تَقُولُ → تَقُلْ).", "«söyleme» — sükûnla meczum; ecvef fiil sükûndan önce vâvını düşürür."),
  maful("شَيْئًا", "shay", "«anything»", "«bir şey»", punct=".")])
sen("s7", "And Ibrāhīm was forbearing, so he said to his father: «Peace be upon you.» (19:47)", "Ve İbrâhim halîm idi; babasına dedi: «Selâm sana.» (19:47)", [
  kana(), tok("إِبْرَاهِيمُ", "ibrahim", "propn", [K, "mamnu-min-sarf"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«Ibrāhīm» — kāna's ism.", "«İbrâhim» — kâne'nin ismi."),
  tok("حَلِيمًا", "halim", "noun", [K, "sifa-mushabbaha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — صِفَةٌ مُشَبَّهَةٌ.", "«forbearing» — kāna's khabar, in naṣb.", "«halîm» — kâne'nin haberi, mansub.", punct="،"),
  qala("فَقَالَ", punct=None, wa=True, hidden="هُوَ"),
  tok("لِوَالِدِهِ", "walid-father", "noun", ["huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَوَالِدِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his father» — the jarr lām; annexed to the pronoun.", "«babasına» — cer lâmı; zamire muzâf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("وَالِدِ", "walid-father", "noun"), seg("هِ", "pron-3ms", "pron")])] + quran([
  tok("سَلَامٌ", "salam", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ (نَكِرَةٌ سُوِّغَ الِابْتِدَاءُ بِهَا لِأَنَّهَا دُعَاءٌ).", "«peace» — the mubtadaʾ (an indefinite allowed to open because it is a prayer).", "«selâm» — mübtedâ (dua olduğu için nekre ile başlandı)."),
  tok("عَلَيْكَ", "ala", "prep", ["huruf-jarr", "mubtada-khabar"], "عَلَى حَرْفُ جَرٍّ، وَالْكَافُ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«upon you» — the jarr phrase is the khabar.", "«sana» — câr-mecrur haber.", punct=".", segments=[seg("عَلَيْ", "ala", "prep"), seg("كَ", "pron-2ms", "pron")])]))
for _t in S[-1]["tokens"]:
    if _t["surface"]["full"] == "فَقَالَ": _t["segments"] = [seg("فَ", "fa", "conj"), seg("قَالَ", "qala", "verb")]; _t["irab"]["ar"] = _t["irab"]["ar"].replace("الْوَاوُ عَاطِفَةٌ", "الْفَاءُ عَاطِفَةٌ")
sen("s8", "And he said to him: I am going away from here, and I will call upon my Lord.", "Ve ona dedi: Ben buradan gidiyorum ve Rabbime dua edeceğim.", [
  qala("وَقَالَ", punct=None, wa=True, hidden="هُوَ"),
  tok("لَهُ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«to him».", "«ona».", punct=":", segments=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")]),
  ana_mubtada(), mudari_ana("أَذْهَبُ", "dhahaba", "«am going»", "«gidiyorum»"),
  tok("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-dan»."),
  tok("هُنَا", "huna", "noun", ["huruf-jarr", "asma-al-ishara"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِمِنْ.", "«here» — the demonstrative of place, built; in the place of jarr after «from».", "«bura» — mekân ism-i işâreti, mebnî; min ile mahallen mecrur."),
  tok("وَأَدْعُو", "daa", "verb", ["atf-nasaq", "mudari-marfu", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَدْعُو فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«and I will call» — joined; rafʿ by an estimated ḍamma on the wāw.", "«ve dua edeceğim» — atıf; vâv üzerinde takdîrî damme ile merfû.", segments=[seg("وَ", "wa", "conj"), seg("أَدْعُو", "daa", "verb")]),
  tok("رَبِّي", "rabb", "noun", ["maful-bihi", "ya-al-mutakallim", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَهُوَ مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord» — the object, naṣb estimated before the speaker's yāʾ.", "«Rabbime» — mef'ûl, mütekellim yâsından önce takdîrî fetha.", punct=".", segments=[seg("رَبِّ", "rabb", "noun"), seg("ي", "pron-1s", "pron")])])
sen("s9", "And Ibrāhīm was very sorry, and he wanted to go to another land, worship his Lord, and call people to Allah.", "Ve İbrâhim çok üzüldü; başka bir beldeye gitmek, Rabbine ibadet etmek ve insanları Allah'a çağırmak istedi.", [
  mazi("وَتَأَسَّفَ", "taassafa", "«was sorry»", "«üzüldü»", hidden=None, wa=True, tags=["form-v-verbs"]), ibrahim_fail(),
  tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ.", "«very» — standing in for the absolute object.", "«çok» — mef'ûl-i mutlak nâibi.", punct="،"),
  mazi("وَأَرَادَ", "arada", "«and wanted»", "«ve istedi»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "form-iv-verbs", "hollow-verbs"]),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«to» — the subjunctive particle.", "«-mek» — masdariyye harfi."),
  an_nasb("يَذْهَبَ", "dhahaba", "«go»", "«gitsin»"),
  tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("بَلَدٍ", "balad", "noun", ["huruf-jarr"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«a land» — in jarr.", "«bir beldeye» — mecrur."),
  tok("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«another» — the naʿt, in jarr by a fatḥa (a diptote).", "«başka» — sıfat, fetha ile mecrur (gayr-ı munsarif).", punct="،"),
  an_nasb("وَيَعْبُدَ", "abada", "«worship»", "«ibadet etsin»", wa=True),
  tok("رَبَّهُ", "rabb", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his Lord» — the object; annexed.", "«Rabbine» — mef'ûl; muzâf.", punct="،", segments=[seg("رَبَّ", "rabb", "noun"), seg("هُ", "pron-3ms", "pron")]),
  an_nasb("وَيَدْعُوَ", "daa", "«call»", "«çağırsın»", wa=True, tags=["naqis-verbs"]),
  maful("النَّاسَ", "nas", "«the people»", "«insanları»"),
  tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("اللهِ", "allah", "propn", ["huruf-jarr"], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«Allah» — in jarr.", "«Allah'a» — mecrur.", punct=".")])

# ================================================================ §12 إلى مكة (pp. 19–20)
sen("s10", "Ibrāhīm's people grew angry, the king grew angry, and Ibrāhīm's father grew angry.", "İbrâhim'in kavmi öfkelendi, kral öfkelendi, İbrâhim'in babası öfkelendi.", [
  mazi("وَغَضِبَ", "ghadiba", "«grew angry»", "«öfkelendi»", hidden=None, wa=True),
  tok("قَوْمُ", "qawm", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the people of» — the doer, a muḍāf.", "«kavmi» — fâil, muzâf."), ibrahim_jarr_mudaf(),
  mazi("وَغَضِبَ", "ghadiba", "«and grew angry»", "«ve öfkelendi»", hidden=None, wa=True, tags=["atf-nasaq"]), malik_fail(),
  mazi("وَغَضِبَ", "ghadiba", "«and grew angry»", "«ve öfkelendi»", hidden=None, wa=True, tags=["atf-nasaq"]), walid_fail(), ibrahim_jarr_mudaf(punct=".")])
sen("s11", "And Ibrāhīm wanted to travel to another land, worship Allah there, and call people to Allah.", "Ve İbrâhim başka bir beldeye yolculuk etmek, orada Allah'a ibadet etmek ve insanları Allah'a çağırmak istedi.", [
  mazi("وَأَرَادَ", "arada", "«wanted»", "«istedi»", hidden=None, wa=True, tags=["form-iv-verbs", "hollow-verbs"]), ibrahim_fail(),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«to».", "«-mek»."),
  an_nasb("يُسَافِرَ", "safara", "«travel»", "«yolculuk etsin»", tags=["form-iii-verbs"]),
  tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("بَلَدٍ", "balad", "noun", ["huruf-jarr"], "مَجْرُورٌ بِإِلَى.", "«a land».", "«bir beldeye»."),
  tok("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«another» — the naʿt; a diptote.", "«başka» — sıfat; gayr-ı munsarif."),
  an_nasb("وَيَعْبُدَ", "abada", "«worship»", "«ibadet etsin»", wa=True),
  tok("فِيهِ", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«in it» — there.", "«orada».", segments=[seg("فِي", "fi", "prep"), seg("هِ", "pron-3ms", "pron")]),
  tok("اللهَ", "allah", "propn", ["maful-bihi"], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the object.", "«Allah'a» — mef'ûl."),
  an_nasb("وَيَدْعُوَ", "daa", "«call»", "«çağırsın»", wa=True, tags=["naqis-verbs"]),
  maful("النَّاسَ", "nas", "«the people»", "«insanları»"),
  tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("اللهِ", "allah", "propn", ["huruf-jarr"], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِإِلَى.", "«Allah» — in jarr.", "«Allah'a» — mecrur.", punct=".")])
sen("s12", "And Ibrāhīm left his land and bade his father farewell.", "Ve İbrâhim beldesinden çıktı ve babasıyla vedalaştı.", [
  mazi("وَخَرَجَ", "kharaja", "«left»", "«çıktı»", hidden=None, wa=True), ibrahim_fail(),
  tok("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-dan»."),
  tok("بَلَدِهِ", "balad", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِمِنْ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his land» — in jarr; annexed.", "«beldesinden» — mecrur; muzâf.", segments=[seg("بَلَدِ", "balad", "noun"), seg("هِ", "pron-3ms", "pron")]),
  mazi("وَوَدَّعَ", "waddaa", "«and bade farewell»", "«ve vedalaştı»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "form-ii-verbs"]),
  tok("وَالِدَهُ", "walid-father", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — the object.", "«babasını» — mef'ûl.", punct=".", segments=[seg("وَالِدَ", "walid-father", "noun"), seg("هُ", "pron-3ms", "pron")])])
sen("s13", "And Ibrāhīm set out for Mecca, and with him was his wife Hājar.", "Ve İbrâhim Mekke'ye yöneldi; yanında eşi Hâcer vardı.", [
  mazi("وَقَصَدَ", "qasada", "«set out for»", "«yöneldi»", hidden=None, wa=True), ibrahim_fail(),
  name_maful("مَكَّةَ", "makka", "«Mecca»", "«Mekke'ye»"),
  tok("وَمَعَهُ", "maa", "noun", ["maful-fih", "mubtada-khabar"], "الْوَاوُ حَالِيَّةٌ، وَمَعَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ خَبَرٌ مُقَدَّمٌ.", "«and with him» — the wāw of ḥāl; the ẓarf «with» annexed to the pronoun stands as the fronted khabar.", "«ve yanında» — hâl vâvı; zamire muzâf zarf, öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("زَوْجُهُ", "zawj", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his wife» — the delayed mubtadaʾ; annexed.", "«eşi» — te'hir edilmiş mübtedâ; muzâf.", segments=[seg("زَوْجُ", "zawj", "noun"), seg("هُ", "pron-3ms", "pron")]),
  name_badal("هَاجَرُ", "hajar-name", "«Hājar»", "«Hâcer»", "raf", punct=".")])
sen("s14", "And Mecca had neither grass nor trees.", "Ve Mekke'de ne ot ne ağaç vardı.", kanat_makka() + laysa_fiha() + [laysa_ism("عُشْبٌ", "ushb", "«grass»", "«ot»")] + wa_la_atf("شَجَرٌ", "shajar", "«trees»", "«ağaç»", punct="."))
sen("s15", "And Mecca had neither a well nor a river.", "Ve Mekke'de ne kuyu ne ırmak vardı.", kanat_makka() + laysa_fiha() + [laysa_ism("بِئْرٌ", "bir", "«a well»", "«kuyu»")] + wa_la_atf("نَهْرٌ", "nahr", "«a river»", "«ırmak»", punct="."))
sen("s16", "And Mecca had neither animal nor human.", "Ve Mekke'de ne hayvan ne insan vardı.", kanat_makka() + laysa_fiha() + [laysa_ism("حَيَوَانٌ", "hayawan", "«an animal»", "«hayvan»")] + wa_la_atf("بَشَرٌ", "bashar", "«a human»", "«insan»", punct="."))
sen("s17", "And Ibrāhīm reached Mecca and settled there.", "Ve İbrâhim Mekke'ye ulaştı ve oraya yerleşti.", [
  mazi("وَوَصَلَ", "wasala", "«reached»", "«ulaştı»", hidden=None, wa=True, tags=["mithal-verbs"]), ibrahim_fail(),
  tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."), makka_jarr(),
  mazi("وَنَزَلَ", "nazala", "«and settled»", "«ve yerleşti»", hidden="هُوَ", wa=True, tags=["atf-nasaq"]),
  tok("فِيهَا", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ.", "«there» — in it.", "«oraya».", punct=".", segments=[seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")])])
sen("s18", "And Ibrāhīm left his wife Hājar and his son Ismāʿīl.", "Ve İbrâhim eşi Hâcer'i ve oğlu İsmâil'i bıraktı.", [
  mazi("وَتَرَكَ", "taraka", "«left»", "«bıraktı»", hidden=None, wa=True), ibrahim_fail(),
  tok("زَوْجَهُ", "zawj", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his wife» — the object; annexed.", "«eşini» — mef'ûl; muzâf.", segments=[seg("زَوْجَ", "zawj", "noun"), seg("هُ", "pron-3ms", "pron")]),
  name_badal("هَاجَرَ", "hajar-name", "«Hājar»", "«Hâcer'i»", "nasb"),
  tok("وَوَلَدَهُ", "walad", "noun", ["atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَوَلَدَ مَعْطُوفٌ عَلَى زَوْجَهُ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his son» — joined to «his wife», in naṣb; annexed.", "«ve oğlunu» — «eşini»ye atıf, mansub; muzâf.", segments=[seg("وَ", "wa", "conj"), seg("وَلَدَ", "walad", "noun"), seg("هُ", "pron-3ms", "pron")]),
  name_badal("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil'i»", "nasb", punct=".")])
sen("s19", "And when Ibrāhīm wanted to go, his wife Hājar said: Where to, my master?", "Ve İbrâhim gitmek isteyince eşi Hâcer dedi: Nereye, efendim?", [
  tok("وَلَمَّا", "lamma", "part", ["maful-fih"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَمَّا حِينِيَّةٌ ظَرْفُ زَمَانٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", "«and when» — the temporal lammā, a mabnī adverb.", "«ve …-ince» — zaman zarfı lemmâ, mebnî.", segments=[seg("وَ", "wa", "conj"), seg("لَمَّا", "lamma", "part")]),
  mazi("أَرَادَ", "arada", "«wanted»", "«istedi»", hidden=None, tags=["form-iv-verbs", "hollow-verbs"]), ibrahim_fail(),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«to».", "«-mek»."),
  an_nasb("يَذْهَبَ", "dhahaba", "«go»", "«gitsin»"),
  tok("قَالَتْ", "qala", "verb", ["hollow-verbs", "maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«she said» — the feminine tāʾ; what is said is the object.", "«dedi» — te'nis tâ'sı; söylenen söz mef'ûl."),
  tok("زَوْجُهُ", "zawj", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his wife» — the doer; annexed.", "«eşi» — fâil; muzâf.", segments=[seg("زَوْجُ", "zawj", "noun"), seg("هُ", "pron-3ms", "pron")]),
  name_badal("هَاجَرُ", "hajar-name", "«Hājar»", "«Hâcer»", "raf", punct=":"),
  tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("أَيْنَ", "ayna", "pron", ["al-istifham", "huruf-jarr"], "اسْمُ اسْتِفْهَامٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ بِإِلَى.", "«where?» — the interrogative of place, built; in the place of jarr.", "«nere(ye)?» — mekân istifhâm ismi, mebnî; mahallen mecrur."),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O».", "«ey»."),
  tok("سَيِّدِي", "sayyid", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my master» — a munādā annexed to the speaker's yāʾ; naṣb estimated.", "«efendim» — mütekellim yâsına muzâf münâdâ; nasb takdîrî.", punct="؟", segments=[seg("سَيِّدِ", "sayyid", "noun"), seg("ي", "pron-1s", "pron")])])
sen("s20", "Are you leaving me here?", "Beni burada mı bırakıyorsun?", [
  tok("أَتَتْرُكُنِي", "taraka", "verb", ["al-istifham", "mudari-marfu", "ya-al-mutakallim", "maful-bihi"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَتَتْرُكُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«are you leaving me?» — the question hamza; the doer «you» concealed; the nūn of protection before the speaker's yāʾ, its object.", "«beni bırakıyor musun?» — istifhâm hemzesi; fâil gizli «sen»; vikâye nûnu, yâ mef'ûl.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تَتْرُكُ", "taraka", "verb"), seg("نِي", "pron-1s", "pron")]),
  huna(punct="؟")])
sen("s21", "Are you leaving me while there is no water here and no food!", "Burada ne su ne yiyecek varken beni bırakıyor musun!", [
  tok("أَتَتْرُكُنِي", "taraka", "verb", ["al-istifham", "mudari-marfu", "ya-al-mutakallim", "maful-bihi"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَتَتْرُكُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«are you leaving me?» — the question hamza on the verb; the speaker's yāʾ is its object.", "«beni bırakıyor musun?» — fiil üzerinde istifhâm hemzesi; mütekellim yâsı mef'ûl.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تَتْرُكُ", "taraka", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("وَلَيْسَ", "laysa", "verb", [K, "hollow-verbs", "hal"], "الْوَاوُ حَالِيَّةٌ، وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«while there is not» — the wāw of ḥāl; the laysa clause is the ḥāl.", "«…yokken» — hâl vâvı; leyse cümlesi hâldir.", segments=[seg("وَ", "wa", "conj"), seg("لَيْسَ", "laysa", "verb")]),
  tok("هُنَا", "huna", "noun", ["maful-fih", K], "اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ ظَرْفٌ — خَبَرُ لَيْسَ مُقَدَّمٌ.", "«here» — the adverb of place, laysa's fronted khabar.", "«burada» — mekân zarfı, leyse'nin öne alınmış haberi."),
  laysa_ism("مَاءٌ", "ma-water", "«water»", "«su»")] + wa_la_atf("طَعَامٌ", "taam", "«food»", "«yiyecek»", punct="!"))
sen("s22", "Has Allah commanded you this?", "Bunu sana Allah mı emretti?", [
  tok("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«…?» — the question particle.", "«mı?» — istifhâm harfi."),
  tok("أَمَرَكَ", "amara-v", "verb", ["maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«commanded you» — a māḍī; the kāf is its object.", "«sana emretti» — mâzî; kâf mef'ûl.", segments=[seg("أَمَرَ", "amara-v", "verb"), seg("كَ", "pron-2ms", "pron")]),
  allah_fail(),
  tok("بِهٰذَا", "hadha", "pron", ["huruf-jarr", "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«this» — the bāʾ on the demonstrative.", "«bunu(nla)» — ism-i işâret üzerinde bâ.", punct="؟", segments=[seg("بِ", "bi", "prep"), seg("هٰذَا", "hadha", "pron")])])
sen("s23", "Ibrāhīm said: Yes!", "İbrâhim dedi: Evet!", [
  qala(punct=None), ibrahim_fail(punct=":"),
  tok("نَعَمْ", "naam", "part", [], "حَرْفُ جَوَابٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "«yes» — the answer particle, built on sukūn.", "«evet» — cevap harfi, sükûn üzere mebnî.", punct="!")])
sen("s24", "Hājar said: Then He will not let us perish!", "Hâcer dedi: Öyleyse bizi zayi etmez!", [
  mazi_ta("قَالَتْ", "qala", "«said»", "«dedi»", tags=["hollow-verbs", "maful-bihi"]), hajar("raf", punct=":"),
  tok("إِذًا", "idhan", "part", [], "حَرْفُ جَوَابٍ وَجَزَاءٍ، مُهْمَلٌ هُنَا لِأَنَّ الْفِعْلَ بَعْدَهُ مَنْفِيٌّ بِلَا.", "«then» — the particle of answer and consequence; it governs nothing here, because a negating lā stands between it and the verb.", "«öyleyse» — cevap ve cezâ harfi; burada amel etmez, zira fiil lâ ile menfî."),
  la_nafiya(),
  tok("يُضِيعُنَا", "adaa-lose", "verb", ["la-nafiya", "mudari-marfu", "form-iv-verbs", "hollow-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَنَا ضَمِيرٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«let us perish» — rafʿ after the negating lā; the doer «He» concealed; «us» is the object.", "«bizi zayi eder» — nefiy lâ'sından sonra merfû; fâil gizli «O»; «biz» mef'ûl.", punct="!", segments=[seg("يُضِيعُ", "adaa-lose", "verb"), seg("نَا", "pron-1p", "pron")])])

# ================================================================ §13 بئر زمزم (pp. 20–21)
sen("s25", "Once Ismāʿīl grew thirsty, and his mother wanted to give him water to drink.", "Bir keresinde İsmâil susadı ve annesi ona su içirmek istedi.", [
  mazi("وَعَطِشَ", "atisha", "«grew thirsty»", "«susadı»", hidden=None, wa=True), name_fail("إِسْمَاعِيلُ", "ismail", "«Ismāʿīl»", "«İsmâil»"),
  tok("مَرَّةً", "marra-once", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلْعَدَدِ مَنْصُوبٌ بِالْفَتْحَةِ (وَقِيلَ: ظَرْفُ زَمَانٍ).", "«once» — an absolute object of number (or an adverb of time).", "«bir kez» — sayı bildiren mef'ûl-i mutlak (yahut zaman zarfı).", punct="،"),
  mazi_ta("وَأَرَادَتْ", "arada", "«and wanted»", "«ve istedi»", tags=["atf-nasaq", "form-iv-verbs", "hollow-verbs"], wa=True),
  tok("أُمُّهُ", "umm", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his mother» — the doer; annexed.", "«annesi» — fâil; muzâf.", segments=[seg("أُمُّ", "umm", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«to».", "«-mek»."),
  tok("تَسْقِيَهُ", "saqa-water", "verb", ["an-masdariyya", "naqis-verbs", "mafulayn", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«give him to drink» — naṣb after an, the fatḥa written on the yāʾ; «him» is the first object.", "«ona içirsin» — en ile mansub, fetha yâ üzerinde yazılı; «o» birinci mef'ûl.", segments=[seg("تَسْقِيَ", "saqa-water", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("مَاءً", "ma-water", "noun", ["mafulayn", "maful-bihi"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«water» — the second object.", "«su» — ikinci mef'ûl.", punct=".")])
sen("s26", "But where is the water?", "Fakat su nerede?", [
  tok("وَلٰكِنْ", "lakin", "part", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the light lākin, governing nothing.", "«fakat» — muhaffef lâkin, amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنْ", "lakin", "part")]),
  tok("أَيْنَ", "ayna", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "«where?» — the interrogative, built; the fronted khabar.", "«nerede?» — istifhâm ismi, mebnî; öne alınmış haber."),
  tok("الْمَاءُ", "ma-water", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the water» — the delayed mubtadaʾ.", "«su» — te'hir edilmiş mübtedâ.", punct="؟")])
sen("s27", "And Mecca has no well, and Mecca has no river!", "Mekke'de kuyu yok, Mekke'de ırmak yok!", [
  tok("وَمَكَّةُ", "makka", "propn", ["mubtada-khabar", "mamnu-min-sarf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَمَكَّةُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and Mecca» — the mubtadaʾ; a diptote.", "«ve Mekke» — mübtedâ; gayr-ı munsarif.", segments=[seg("وَ", "wa", "conj"), seg("مَكَّةُ", "makka", "propn")]),
  tok("لَيْسَ", "laysa", "verb", [K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.", "«there is not» — laysa; its clause is the khabar.", "«yoktur» — leyse; cümlesi haber."),
  tok("فِيهَا", "fi", "prep", ["huruf-jarr", K], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — خَبَرُ لَيْسَ مُقَدَّمٌ.", "«in it» — laysa's fronted khabar.", "«onda» — leyse'nin öne alınmış haberi.", segments=[seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")]),
  laysa_ism("بِئْرٌ", "bir", "«a well»", "«kuyu»", punct="،"),
  tok("وَمَكَّةُ", "makka", "propn", ["mubtada-khabar", "mamnu-min-sarf", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَكَّةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and Mecca» — the mubtadaʾ of a joined clause.", "«ve Mekke» — atfedilen cümlenin mübtedâsı.", segments=[seg("وَ", "wa", "conj"), seg("مَكَّةُ", "makka", "propn")]),
  tok("لَيْسَ", "laysa", "verb", [K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ — وَالْجُمْلَةُ خَبَرٌ.", "«there is not».", "«yoktur»."),
  tok("فِيهَا", "fi", "prep", ["huruf-jarr", K], "فِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — خَبَرُ لَيْسَ مُقَدَّمٌ.", "«in it».", "«onda».", segments=[seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")]),
  laysa_ism("نَهْرٌ", "nahr", "«a river»", "«ırmak»", punct="!")])
sen("s28", "And Hājar kept seeking water, running from al-Ṣafā to al-Marwa and from al-Marwa to al-Ṣafā.", "Ve Hâcer su arıyor, Safâ'dan Merve'ye ve Merve'den Safâ'ya koşuyordu.", [
  tok("وَكَانَتْ", "kana", "verb", [K, "hollow-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and … was» — kāna with the feminine tāʾ.", "«ve … idi» — te'nis tâ'sıyla kâne.", segments=[seg("وَ", "wa", "conj"), seg("كَانَتْ", "kana", "verb")]),
  hajar("raf", role="kanaIsm"),
  tok("تَطْلُبُ", "talaba", "verb", ["mudari-marfu", K], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«kept seeking» — the clause is kāna's khabar.", "«arıyordu» — cümle kâne'nin haberi."),
  maful("الْمَاءَ", "ma-water", "«the water»", "«suyu»"),
  tok("وَتَجْرِي", "jara", "verb", ["atf-nasaq", "mudari-marfu", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَجْرِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and running» — joined; rafʿ by an estimated ḍamma on the yāʾ.", "«ve koşuyordu» — atıf; yâ üzerinde takdîrî damme.", segments=[seg("وَ", "wa", "conj"), seg("تَجْرِي", "jara", "verb")]),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، وَفُتِحَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-dan»."),
  tok("الصَّفَا", "safa-q", "propn", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ كَسْرَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ — اسْمٌ مَقْصُورٌ.", "«al-Ṣafā» — in jarr, the kasra estimated on the alif (a maqṣūr noun).", "«Safâ» — mecrur, kesre elif üzerinde takdîrî (maksûr isim)."),
  tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْمَرْوَةِ", "marwa", "propn", ["huruf-jarr"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«al-Marwa» — in jarr.", "«Merve» — mecrur."),
  tok("وَمِنَ", "min", "prep", ["huruf-jarr", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمِنَ حَرْفُ جَرٍّ.", "«and from».", "«ve -den».", segments=[seg("وَ", "wa", "conj"), seg("مِنَ", "min", "prep")]),
  tok("الْمَرْوَةِ", "marwa", "propn", ["huruf-jarr"], "مَجْرُورٌ بِمِنْ.", "«al-Marwa».", "«Merve»."),
  tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الصَّفَا", "safa-q", "propn", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِإِلَى بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«al-Ṣafā» — in jarr, estimated.", "«Safâ» — takdîrî mecrur.", punct=".")])
sen("s29", "And Allah helped Hājar and helped Ismāʿīl, and created water for them both.", "Ve Allah Hâcer'e yardım etti ve İsmâil'e yardım etti; ikisi için su yarattı.", [
  mazi("وَنَصَرَ", "nasara", "«helped»", "«yardım etti»", hidden=None, wa=True), allah_fail(), hajar("nasb"),
  mazi("وَنَصَرَ", "nasara", "«and helped»", "«ve yardım etti»", hidden="هُوَ", wa=True, tags=["atf-nasaq"]), name_maful("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil'e»"),
  mazi("فَخَلَقَ", "khalaqa", "«so He created»", "«ve yarattı»", hidden="هُوَ", wa=True, tags=["atf-nasaq"]),
  tok("لَهُمَا", "li", "prep", ["huruf-jarr", "al-muthanna"], "اللَّامُ حَرْفُ جَرٍّ، وَهُمَا ضَمِيرُ الْمُثَنَّى فِي مَحَلِّ جَرٍّ.", "«for them both» — the dual pronoun after the lām.", "«ikisine» — lâmdan sonra tesniye zamiri.", segments=[seg("لَ", "li", "prep"), seg("هُمَا", "pron-3d", "pron")]),
  maful("مَاءً", "ma-water", "«water»", "«su»", punct=".")])
for _t in S[-1]["tokens"]:
    if _t["surface"]["full"] == "فَخَلَقَ": _t["segments"] = [seg("فَ", "fa", "conj"), seg("خَلَقَ", "khalaqa", "verb")]; _t["irab"]["ar"] = _t["irab"]["ar"].replace("الْوَاوُ عَاطِفَةٌ", "الْفَاءُ عَاطِفَةٌ")
sen("s30", "And the water came out of the ground; Ismāʿīl drank and Hājar drank, and the water remained, and it became the well of Zamzam.", "Ve su yerden çıktı; İsmâil içti, Hâcer içti, su kaldı ve Zemzem kuyusu oldu.", [
  mazi("وَخَرَجَ", "kharaja", "«came out»", "«çıktı»", hidden=None, wa=True), fail("الْمَاءُ", "ma-water", "«the water»", "«su»"),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("الْأَرْضِ", "ard", "noun", ["huruf-jarr"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the ground» — in jarr.", "«yerden» — mecrur."),
  mazi("وَشَرِبَ", "shariba", "«and drank»", "«ve içti»", hidden=None, wa=True, tags=["atf-nasaq"]), name_fail("إِسْمَاعِيلُ", "ismail", "«Ismāʿīl»", "«İsmâil»"),
  mazi_ta("وَشَرِبَتْ", "shariba", "«and drank»", "«ve içti»", tags=["atf-nasaq"], wa=True), hajar("raf"),
  mazi("وَبَقِيَ", "baqiya", "«and remained»", "«ve kaldı»", hidden=None, wa=True, tags=["atf-nasaq", "naqis-verbs"]), fail("الْمَاءُ", "ma-water", "«the water»", "«su»"),
  tok("فَكَانَ", "kana", "verb", [K, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — أَيِ الْمَاءُ.", "«and it became» — kāna with its ism concealed («it» — the water).", "«ve oldu» — kâne, ismi gizli («o» — su).", segments=[seg("فَ", "fa", "conj"), seg("كَانَ", "kana", "verb")]),
  tok("بِئْرَ", "bir", "noun", [K, "idafa-definiteness"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the well of» — kāna's khabar, a muḍāf.", "«kuyusu» — kâne'nin haberi, muzâf."),
  zamzam_mudaf_ilayh(punct=".")])
sen("s31", "And Allah blessed Zamzam.", "Ve Allah Zemzem'i mübarek kıldı.", [
  tok("فَبَارَكَ", "baraka-bless", "verb", ["form-iii-verbs"], "الْفَاءُ عَاطِفَةٌ، وَبَارَكَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«and blessed» — a Form III māḍī.", "«ve mübarek kıldı» — III. bâb mâzî.", segments=[seg("فَ", "fa", "conj"), seg("بَارَكَ", "baraka-bless", "verb")]),
  allah_fail(),
  tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("زَمْزَمَ", "zamzam", "propn", ["huruf-jarr", "mamnu-min-sarf"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Zamzam» — in jarr by a fatḥa; a diptote name.", "«Zemzem» — fetha ile mecrur; gayr-ı munsarif alem.", punct=".")])
sen("s32", "And this is the well from which people drink during the Hajj, and they bring Zamzam water to their lands.", "Ve bu, insanların hacda içtiği ve Zemzem suyunu memleketlerine götürdükleri kuyudur.", [
  tok("وَهٰذِهِ", "hadhihi", "pron", ["mubtada-khabar", "asma-al-ishara"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهٰذِهِ اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and this» — the demonstrative, the mubtadaʾ.", "«ve bu» — ism-i işâret, mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("هٰذِهِ", "hadhihi", "pron")]),
  tok("هِيَ", "pron-3fs-munfasil", "pron", ["damir-fasl"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "«it (is)» — the pronoun of separation, no place in iʿrāb.", "«o(dur)» — fasıl zamiri, i'rabdan mahalli yok."),
  tok("الْبِئْرُ", "bir", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the well» — the khabar.", "«kuyu» — haber."),
  tok("الَّتِي", "allati", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِلْبِئْرِ.", "«which» — the feminine relative, built; the naʿt of «the well».", "«ki o» — müennes ism-i mevsûl, mebnî; «kuyu»nun sıfatı."),
  tok("يَشْرَبُ", "shariba", "verb", ["mudari-marfu", "ism-mawsul"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«drink» — the ṣila's verb.", "«içer» — sıla fiili."),
  tok("مِنْهَا", "min", "prep", ["huruf-jarr", "ism-mawsul"], "مِنْ حَرْفُ جَرٍّ، وَهَا ضَمِيرٌ فِي مَحَلِّ جَرٍّ — وَهُوَ الْعَائِدُ عَلَى الْمَوْصُولِ.", "«from it» — the pronoun is the ʿāʾid returning to the relative.", "«ondan» — zamir mevsûle dönen âiddir.", segments=[seg("مِنْ", "min", "prep"), seg("هَا", "pron-3fs", "pron")]),
  nas_fail(),
  tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْحَجِّ", "hajj", "noun", ["huruf-jarr"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the Hajj» — in jarr.", "«hacda» — mecrur."),
  khamsa("وَيَأْتُونَ", "ata", "«and they bring»", "«ve getirirler»", wa=True, tags=["atf-nasaq", "naqis-verbs"], extra_ar=" — مَعْطُوفٌ عَلَى يَشْرَبُ"),
  tok("بِمَاءِ", "ma-water", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ لِلتَّعْدِيَةِ، وَمَاءِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«the water of» — the bāʾ of transitivity («bring»); a muḍāf.", "«suyunu» — ta'diye bâ'sı; muzâf.", segments=[seg("بِ", "bi", "prep"), seg("مَاءِ", "ma-water", "noun")]),
  zamzam_mudaf_ilayh(),
  tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("بَلَدِهِمْ", "balad", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِإِلَى، وَهُوَ مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their land» — in jarr; annexed to «their».", "«memleketlerine» — mecrur; muzâf.", punct=".", segments=[seg("بَلَدِ", "balad", "noun"), seg("هِمْ", "pron-3mp", "pron")])])
sen("s33", "Have you drunk Zamzam water?", "Zemzem suyu içtin mi?", [
  tok("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ.", "«…?» — the question particle.", "«mi?» — istifhâm harfi."),
  tok("شَرِبْتَ", "shariba", "verb", [], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«have you drunk» — a māḍī built on sukūn before the doer's tāʾ; the tāʾ «you» is the doer.", "«içtin» — fâil tâsından önce sükûn üzere mebnî mâzî; tâ fâil.", segments=[seg("شَرِبْ", "shariba", "verb"), seg("تَ", "pron-2ms", "pron")]),
  tok("مَاءَ", "ma-water", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the water of» — the object, a muḍāf.", "«suyunu» — mef'ûl, muzâf."),
  zamzam_mudaf_ilayh(punct="؟")])

# ---------------------------------------------------------------- glossary
NEW = {
 "absara": G("absara", "أَبْصَرَ", "ب ص ر", "verb", "to see, to perceive by sight", "görmek", 2, form="IV"),
 "halim": G("halim", "حَلِيم", "ح ل م", "noun", "forbearing, mild (ṣifa mushabbaha)", "halîm, yumuşak huylu", 2),
 "balad": G("balad", "بَلَد", "ب ل د", "noun", "land, country, town", "belde, memleket", 1, plural="بِلَاد"),
 "safara": G("safara", "سَافَرَ", "س ف ر", "verb", "to travel", "yolculuk etmek", 1, form="III"),
 "zawj": G("zawj", "زَوْج", "ز و ج", "noun", "spouse (here: wife)", "eş (burada: hanım)", 1, plural="أَزْوَاج"),
 "hajar-name": G("hajar-name", "هَاجَر", None, "propn", "Hājar (Hagar), Ibrāhīm's wife, Ismāʿīl's mother", "Hâcer, İbrâhim'in eşi, İsmâil'in annesi", 1),
 "ushb": G("ushb", "عُشْب", "ع ش ب", "noun", "grass, herbage", "ot, çimen", 1),
 "bir": G("bir", "بِئْر", "ب أ ر", "noun", "a well", "kuyu", 1, plural="آبَار"),
 "ismail": G("ismail", "إِسْمَاعِيل", None, "propn", "Ismāʿīl (Ishmael), the prophet, son of Ibrāhīm", "İsmâil (a.s.), İbrâhim'in oğlu", 1),
 "naam": G("naam", "نَعَمْ", None, "part", "yes (the answer particle)", "evet (cevap harfi)", 1),
 "idhan": G("idhan", "إِذًا", None, "part", "then, in that case (the particle of answer and consequence)", "öyleyse, o halde (cevap ve cezâ harfi)", 2),
 "adaa-lose": G("adaa-lose", "أَضَاعَ", "ض ي ع", "verb", "to lose, to let perish, to neglect", "zayi etmek, kaybetmek", 2, form="IV"),
 "atisha": G("atisha", "عَطِشَ", "ع ط ش", "verb", "to be thirsty", "susamak", 1, form="I"),
 "safa-q": G("safa-q", "الصَّفَا", "ص ف و", "propn", "al-Ṣafā, the hill by the Kaʿba (one end of the saʿy)", "Safâ, Kâbe yanındaki tepe (sa'yin bir ucu)", 2),
 "marwa": G("marwa", "الْمَرْوَة", "م ر و", "propn", "al-Marwa, the hill facing al-Ṣafā (the other end of the saʿy)", "Merve, Safâ'nın karşısındaki tepe (sa'yin öbür ucu)", 2),
 "zamzam": G("zamzam", "زَمْزَم", None, "propn", "Zamzam, the well in Mecca", "Zemzem, Mekke'deki kuyu", 1),
 "baraka-bless": G("baraka-bless", "بَارَكَ", "ب ر ك", "verb", "to bless (بَارَكَ فِي: to put blessing in)", "mübarek kılmak, bereket vermek", 2, form="III"),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "atisha", _sg.sound1("samia", "عَطِش", "عْطَش", "اِعْطَش", "عَطَش", "عَاطِش", note="لَازِمٌ — وَالصِّفَةُ الْمَشْهُورَةُ مِنْهُ: عَطْشَان."))
put_morph(mo, "safara", _sg.derived("مِنْ بَابِ الْمُفَاعَلَةِ", "فَاعَلَ يُفَاعِلُ", "ُ", "سَافَر", "سَافِر", "سَافِر", "مُسَافَرَة", "مُسَافِر", note="لَازِمٌ."))
put_morph(mo, "baraka-bless", _sg.derived("مِنْ بَابِ الْمُفَاعَلَةِ", "فَاعَلَ يُفَاعِلُ", "ُ", "بَارَك", "بَارِك", "بَارِك", "مُبَارَكَة", "مُبَارِك", "مُبَارَك", "بُورِكَ", "يُبَارَكُ"))
put_morph(mo, "absara", _sg.derived("مِنْ بَابِ الْإِفْعَالِ", "أَفْعَلَ يُفْعِلُ", "ُ", "أَبْصَر", "بْصِر", "أَبْصِر", "إِبْصَار", "مُبْصِر", "مُبْصَر", "أُبْصِرَ", "يُبْصَرُ"))
put_morph(mo, "adaa-lose", _sg.derived_hollow("مِنْ بَابِ الْإِفْعَالِ — أَجْوَفُ يَائِيٌّ", "أَفْعَلَ يُفْعِلُ", "ُ", "أَضَاع", "أَضَع", "ضِيع", "ضِع", "أَضِيع", "أَضِع", "إِضَاعَة", "مُضِيع", "مُضَاع", "أُضِيعَ", "يُضَاعُ", note="أَجْوَفُ: قُلِبَتِ الْيَاءُ أَلِفًا فِي الْمَاضِي (أَضْيَعَ → أَضَاعَ) وَثَبَتَتْ فِي الْمُضَارِعِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 5 (print pp. 18–21, sections 11–13): the call to the father (s1–s9), the journey to Mecca (s10–s24) and the well of Zamzam (s25–s33). "
          "s2, s4 and s7 quote Maryam 19:42, 19:44 and 19:47 as the print sets them (marked). One printed line is one sentence, except that the print's long closing line of §13 is cut at its own pauses into s30–s32 and the two questions of p. 20 stand as s19–s21; the printed vowelling is kept.")
ADD_TR = (" Beşinci bölüm (basılı s. 18–21, 11–13. kısımlar): babaya davet (s1–s9), Mekke yolculuğu (s10–s24) ve Zemzem kuyusu (s25–s33). "
          "s2, s4 ve s7 Meryem 19:42, 19:44 ve 19:47'yi baskıdaki şekliyle aktarır (işaretli). Basılı her satır bir cümledir; yalnız 13. kısmın uzun kapanış satırı kendi duraklarından s30–s32 olarak bölünmüş, s. 20'deki iki soru s19–s21 olarak ayrılmıştır; basılı hareke korunmuştur.")
write_out(5, S, TITLE, ADD_EN, ADD_TR, "pp. 18–21", GLOSS_ADD)
report(5, S, GLOSS_ADD, ())
