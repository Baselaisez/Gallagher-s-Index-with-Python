# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 7: «شُكْرُ دَاوُدَ وَمُلْكُ سُلَيْمَانَ» — §3 (Dāwūd's thanks for the favour, with 38:26)
and §4 (God's favour on Sulaymān: the wind and the jinn, with 21:81–82 and 34:12–13); print pp. 13–14.
python3 tools/authoring/author_qisas4_ch7.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "شُكْرُ دَاوُدَ وَمُلْكُ سُلَيْمَانَ", "en": "Dāwūd's thanks and Sulaymān's dominion", "tr": "Dâvûd'un şükrü ve Süleyman'ın mülkü"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; LN = "la-nahiya"
def majrur(full, lex, en, tr, punct=None, tags=(), ar="مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [HJ] + list(tags), ar, en, tr, punct=punct)
def mudaf_ilayh(full, lex, en, tr, punct=None, tags=(), ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [ID] + list(tags), ar, en, tr, punct=punct)
def naat(full, lex, en, tr, punct=None, tags=(), case="jarr", wa=False):
    C = {"jarr": "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ.", "raf": "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "nasb": "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ."}[case]
    if wa: return tok(full, lex, "noun", [AT, NA] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " " + C[:-1] + " — مَعْطُوفٌ عَلَى النَّعْتِ قَبْلَهُ.", "«and» + " + en + " — a second naʿt, joined.", "«ve» + " + tr + " — ikinci sıfat, ma'tûf.", punct=punct, segments=wa_(full[2:], lex, "noun"))
    return tok(full, lex, "noun", [NA] + list(tags), C, en + " — the naʿt.", tr + " — sıfat.", punct=punct)
def prep_pron(full, lex, pron_form, pron_lex, en, tr, punct=None, tags=(), extra_ar=""):
    pre = full[:len(full) - len(pron_form)]
    return tok(full, lex, "prep", [HJ] + list(tags), "حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ" + extra_ar + ".", en, tr, punct=punct, segments=[seg(pre, lex, "prep"), seg(pron_form, pron_lex, "pron")])
def maful_(full, lex, en, tr, punct=None, tags=(), ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [MB] + list(tags), ar, en, tr, punct=punct)
def noun_pron(full, lex, stem, pron_form, pron_lex, ar, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", list(tags), ar, en, tr, punct=punct, segments=[seg(stem, lex, "noun"), seg(pron_form, pron_lex, "pron")])
def atf(full, lex, en, tr, case="jarr", punct=None, tags=(), pos="noun", sign=None):
    C = {"jarr": "مَعْطُوفٌ مَجْرُورٌ " + (sign or "بِالْكَسْرَةِ"), "raf": "مَعْطُوفٌ مَرْفُوعٌ " + (sign or "بِالضَّمَّةِ"), "nasb": "مَعْطُوفٌ مَنْصُوبٌ " + (sign or "بِالْفَتْحَةِ")}[case]
    return tok(full, lex, pos, [AT] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " " + C + ".", "«and» + " + en + " — joined by the wāw.", "«ve» + " + tr + " — vâv ile atıf.", punct=punct, segments=wa_(full[2:], lex, pos))
def prep(full, lex, en, tr, punct=None, ar="حَرْفُ جَرٍّ."): return tok(full, lex, "prep", [HJ], ar, en, tr, punct=punct)
def li_pron(full, pron_form, pron_lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, "li", "prep", [HJ] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ" + extra + ".", en, tr, punct=punct, segments=[seg(full[:2], "li", "prep"), seg(pron_form, pron_lex, "pron")])
def khabar_kana(full, lex, en, tr, punct=None, tags=(), ar="خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [KN] + list(tags), ar, en + " — kāna's khabar.", tr + " — kâne'nin haberi.", punct=punct)
def amr_hidden(full, lex, en, tr, punct=None, tags=(), wa=False, fa=False, extra=""):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ("الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَ" if fa else "")
    segs = (wa_(full[2:], lex, "verb") if wa else ([seg("فَ", "fa", "conj"), seg(full[2:], lex, "verb")] if fa else None))
    return tok(full, lex, "verb", [AM] + ([AT] if (wa or fa) else []) + list(tags), pre + "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ" + extra + ".", en + " — an imperative on sukūn; the doer concealed.", tr + " — sükûn üzere mebnî emir; fâil gizli.", punct=punct, segments=segs)

# ---------------------------------------------------------------- §3 شُكْرُهُ عَلَى هٰذِهِ النِّعْمَةِ (print p. 13)
sen("s1", "And Dāwūd was — with this wide dominion and this skilled, strong hand — a humble, ever-returning servant,",
        "Dâvûd, bu geniş mülk ve bu becerikli, güçlü el ile birlikte, huşû içinde, Allah'a çokça dönen bir kuldu;", [
  kana(),
  tok("دَاوُدُ", "dawud", "propn", [KN, MM], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Dāwūd» — kāna's ism; a diptote.", "«Dâvûd» — kâne'nin ismi; gayr-i munsarıf."),
  tok("مَعَ", "maa", "noun", [MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with» — a ẓarf, annexed.", "«ile» — zarf, muzâf."),
  tok("هٰذَا", "hadha", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«this» — the muḍāf ilayh.", "«bu» — muzâfun ileyh."),
  tok("الْمُلْكِ", "mulk", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«dominion» — the badal of the demonstrative.", "«mülk» — ism-i işâretten bedel."),
  naat("الْوَاسِعِ", "wasi-wide", "«wide»", "«geniş»", tags=["ism-fail"]),
  atf("وَالْيَدِ", "yad", "«the hand»", "«el»", "jarr"),
  naat("الْحَاذِقَةِ", "hadhiq", "«skilled»", "«becerikli»", tags=["ism-fail"]),
  naat("الْقَوِيَّةِ", "qawi", "«strong»", "«güçlü»"),
  khabar_kana("عَبْدًا", "abd", "«a servant»", "«bir kul»"),
  naat("خَاشِعًا", "khashi", "«humble»", "«huşû içinde»", case="nasb", tags=["ism-fail"]),
  naat("أَوَّابًا", "awwab", "«ever-returning [to God]»", "«çokça (Allah'a) dönen»", case="nasb", tags=["sighat-mubalagha"], punct="،"),
])
sen("s2", "constant in remembrance, long in supplication and glorification, a just ruler,",
        "zikri dâimî, duası ve tesbihi uzun, âdil bir hükümdar;", [
  tok("دَائِمَ", "daim", "noun", [NA, ID, "idafa-lafziyya", "ism-fail"], "نَعْتٌ مَنْصُوبٌ، مُضَافٌ (إِضَافَةٌ لَفْظِيَّةٌ).", "«constant in» — a naʿt annexed to its complement (a verbal iḍāfa).", "«… dâimî» — sıfat, lafzî izâfetle muzâf."),
  mudaf_ilayh("الذِّكْرِ", "dhikr", "«remembrance»", "«zikri»", tags=["masdar"], punct="،"),
  tok("طَوِيلَ", "tawil-long", "noun", [NA, ID, "idafa-lafziyya", "sifa-mushabbaha"], "نَعْتٌ مَنْصُوبٌ، مُضَافٌ (إِضَافَةٌ لَفْظِيَّةٌ).", "«long in» — a naʿt annexed (a verbal iḍāfa).", "«… uzun» — sıfat, lafzî izâfetle muzâf."),
  mudaf_ilayh("الدُّعَاءِ", "dua", "«supplication»", "«duası»", tags=["masdar"]),
  atf("وَالتَّسْبِيحِ", "tasbih", "«glorification»", "«tesbihi»", "jarr", tags=["masdar"], punct="،"),
  tok("حَاكِمًا", "hakim-ruler", "noun", [NA, "ism-fail"], "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ (أَوْ خَبَرٌ ثَانٍ لِكَانَ).", "«a ruler» — a naʿt (or a second khabar of kāna).", "«bir hükümdar» — sıfat (ya da kâne'nin ikinci haberi)."),
  naat("مُقْسِطًا", "muqsit", "«just»", "«âdil»", case="nasb", tags=["ism-fail", "form-iv-verbs"], punct="،"),
])
sen("s3", "judging between people with truth and never favouring anyone; God the Exalted says:",
        "insanlar arasında hak ile hükmeder, kimseyi kayırmazdı; Allah Teâlâ buyurur ki:", [
  mudari("يَحْكُمُ", "hakama", "«judging»", "«hükmeder»", tags=[HL], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ (أَوْ نَعْتٌ)"),
  tok("بَيْنَ", "bayna", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«between» — a ẓarf of place, annexed.", "«arasında» — mekân zarfı, muzâf."),
  mudaf_ilayh("النَّاسِ", "nas", "«people»", "«insanlar»"),
  tok("بِالْحَقِّ", "haqq", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَقِّ مَجْرُورٌ.", "«with truth»", "«hak ile»", segments=[seg("بِ", "bi", "prep"), seg("الْحَقِّ", "haqq", "noun")]),
  la_nafiya(wa=True),
  neg_mudari("يُحَابِي", "haba", "«favours [anyone]»", "«kayırır»", tags=[AT, "naqis-verbs", "form-iii-verbs"], hidden="هُوَ", extra=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ"),
  mudari("يَقُولُ", "qala", "«says»", "«buyurur»", tags=["hollow-verbs", MB], hidden=None, punct=None),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«the Exalted» — a parenthetical māḍī of praise.", "«Teâlâ» — mu'teriza duâ cümlesi.", punct=":"),
])
sen("s4", "«O Dāwūd, We have made you a vicegerent in the land, so judge between people with truth, and do not follow desire, lest it lead you astray from the path of God» (38:26).",
        "«Ey Dâvûd! Biz seni yeryüzünde halife kıldık; insanlar arasında hak ile hükmet, hevâya uyma; yoksa seni Allah'ın yolundan saptırır» (38:26).", [
  *quran([
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("دَاوُدُ", "dawud", "propn", ["vocative-munada", MM], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Dāwūd» — the munādā, built on ḍamma.", "«Dâvûd» — münâdâ, damme üzere mebnî."),
  tok("إِنَّا", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا اسْمُهَا فِي مَحَلِّ نَصْبٍ.", "«indeed We» — inna with nā as its ism.", "«şüphesiz biz» — inne; nâ ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("ا", "pron-1p", "pron")]),
  tok("جَعَلْنَاكَ", "jaala", "verb", [IW, MX], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ أَوَّلُ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«We have made you» — nā the doer, the kāf the first object; the clause is inna's khabar.", "«seni kıldık» — nâ fâil, kâf ilk mef'ûl; cümle inne'nin haberi.", segments=[seg("جَعَلْ", "jaala", "verb"), seg("نَا", "pron-1p", "pron"), seg("كَ", "pron-2ms", "pron")]),
  tok("خَلِيفَةً", "khalifa", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a vicegerent» — the second object.", "«halife» — ikinci mef'ûl."),
  fi(), majrur("الْأَرْضِ", "ard", "«the land»", "«yeryüzünde»"),
  amr_hidden("فَاحْكُمْ", "hakama", "«so judge»", "«hükmet»", fa=True),
  tok("بَيْنَ", "bayna", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«between»", "«arasında»"),
  mudaf_ilayh("النَّاسِ", "nas", "«people»", "«insanlar»"),
  tok("بِالْحَقِّ", "haqq", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحَقِّ مَجْرُورٌ.", "«with truth»", "«hak ile»", segments=[seg("بِ", "bi", "prep"), seg("الْحَقِّ", "haqq", "noun")]),
  tok("وَلَا", "la-nahiya", "part", [AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَاهِيَةٌ جَازِمَةٌ.", "«and do not» — the prohibiting lā, which gives jazm.", "«ve … -me» — nehiy lâ'sı, cezmeder.", segments=wa_("لَا", "la-nahiya", "part")),
  tok("تَتَّبِعِ", "ittabaa", "verb", [LN, MB, "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«follow» — jazm by lā (sukūn), kasra for the two sukūns.", "«uyma» — lâ ile meczum (sükûn); iki sâkin için kesre."),
  tok("الْهَوَى", "hawa-desire", "noun", [MB, "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«desire» — the object, naṣb by an estimated fatḥa (a maqṣūr).", "«hevâ» — mef'ûl; elif üzerinde takdîrî fetha (maksûr)."),
  tok("فَيُضِلَّكَ", "adalla", "verb", ["fa-khabar-mubtada", MB, "doubled-verbs", "form-iv-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَيُضِلَّ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ فَاءِ السَّبَبِيَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«lest it lead you astray» — the fāʾ of cause; naṣb by a hidden an; the kāf the object.", "«yoksa seni saptırır» — sebep fâ'sı; gizli en ile mansub; kâf mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("يُضِلَّ", "adalla", "verb"), seg("كَ", "pron-2ms", "pron")]),
  prep("عَنْ", "an", "«from»", "«-den»"),
  majrur("سَبِيلِ", "sabil", "«the path»", "«yolu»", tags=[ID], ar="مَجْرُورٌ بِعَنْ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»", punct="."),
  ]),
])
sen("s5", "«Indeed those who stray from the path of God — for them is a severe torment, for having forgotten the Day of Reckoning» (38:26).",
        "«Allah'ın yolundan sapanlara, hesap gününü unutmaları yüzünden şiddetli bir azap vardır» (38:26).", [
  *quran([
  inna(),
  tok("الَّذِينَ", "alladhina", "pron", [IW, MW], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«those who» — the relative, inna's ism.", "«… -anlar» — ism-i mevsûl, inne'nin ismi."),
  khamsa("يَضِلُّونَ", "dalla-stray", "«stray»", "«saparlar»", tags=[MW, "doubled-verbs"], extra_ar=" — صِلَةٌ"),
  prep("عَنْ", "an", "«from»", "«-den»"),
  majrur("سَبِيلِ", "sabil", "«the path»", "«yolu»", tags=[ID], ar="مَجْرُورٌ بِعَنْ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»"),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«for them» — a fronted khabar.", "«onlara» — öne alınmış haber.", tags=[MK], extra=" — خَبَرٌ مُقَدَّمٌ"),
  tok("عَذَابٌ", "adhab", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«a torment» — the delayed mubtadaʾ; the clause is inna's khabar.", "«bir azap» — sonraya bırakılmış mübtedâ; cümle inne'nin haberi."),
  naat("شَدِيدٌ", "shadid", "«severe»", "«şiddetli»", case="raf", tags=["sifa-mushabbaha"]),
  tok("بِمَا", "bi", "prep", [HJ, "anwa-ma"], "الْبَاءُ لِلسَّبَبِيَّةِ، وَمَا مَصْدَرِيَّةٌ.", "«for» — the bāʾ of cause with the maṣdar-mā.", "«… yüzünden» — sebep bâ'sı ve masdariyye mâ.", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  mazi_pl("نَسُوا", "nasiya", "«they forgot»", "«unuttular»", tags=["naqis-verbs", MB]),
  tok("يَوْمَ", "yawm", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«the Day» — the object, annexed.", "«gününü» — mef'ûl, muzâf."),
  mudaf_ilayh("الْحِسَابِ", "hisab", "«of Reckoning»", "«hesap»", tags=["masdar"], punct="."),
  ]),
])

# ---------------------------------------------------------------- §4 نِعْمَةُ اللهِ عَلَى سُلَيْمَانَ (print pp. 13–14)
sen("s6", "As for Sulaymān, God subjected to him the winds, running at his command and carrying him from place to place, so that he reached it in the shortest time and the quickest span;",
        "Süleyman'a gelince: Allah rüzgârları onun emrine verdi; onun buyruğuyla eser, onu bir yerden bir yere taşırdı, o da oraya en kısa vakitte ve en hızlı zamanda ulaşırdı;", [
  tok("فَأَمَّا", "amma", "part", ["amma-tafsiliyya"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for» — ammā.", "«… -e gelince» — emmâ.", segments=[seg("فَ", "fa", "conj"), seg("أَمَّا", "amma", "part")]),
  tok("سُلَيْمَانُ", "sulayman", "propn", [MK, MM], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sulaymān» — the mubtadaʾ; a diptote.", "«Süleyman» — mübtedâ; gayr-i munsarıf."),
  tok("فَقَدْ", "qad", "part", ["fa-khabar-mubtada", "qad-harf"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«then indeed» — the answer-fāʾ with qad.", "«işte» — cevap fâ'sı ile kad.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  mazi("سَخَّرَ", "sakhkhara", "«subjected»", "«emrine verdi»", tags=["form-ii-verbs"], hidden=None),
  allah_fail(),
  li_pron("لَهُ", "هُ", "pron-3ms", "«to him»", "«ona»"),
  maful_("الرِّيَاحَ", "rih", "«the winds»", "«rüzgârları»", tags=[JT]),
  mudari("تَجْرِي", "jara", "«running»", "«eser»", tags=[HL, "naqis-verbs"], hidden="هِيَ", extra_ar=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْجُمْلَةُ حَالٌ"),
  noun_pron("بِأَمْرِهِ", "amr-noun", "بِأَمْرِ", "هِ", "pron-3ms", "الْبَاءُ حَرْفُ جَرٍّ، وَأَمْرِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«at his command»", "«onun buyruğuyla»", tags=[HJ, ID]),
  tok("وَتَحْمِلُهُ", "hamala", "verb", [AT, "mudari-marfu", MB], "الْوَاوُ عَاطِفَةٌ، وَتَحْمِلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and carrying him» — the hāʾ is the object.", "«ve onu taşır» — hâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("تَحْمِلُ", "hamala", "verb"), pr3ms()]),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("مَكَانٍ", "makan", "«a place»", "«bir yer»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("مَكَانٍ", "makan", "«a place»", "«bir yere»", punct="،"),
  tok("فَيَصِلُ", "wasala", "verb", [AT, "mudari-marfu", "mithal-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّعْقِيبِ)، وَيَصِلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«so he reaches» — the fāʾ of sequence; the doer concealed.", "«o da ulaşır» — ta'kîb fâ'sı; fâil gizli.", segments=[seg("فَ", "fa", "conj"), seg("يَصِلُ", "wasala", "verb")]),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«it»", "«oraya»"),
  fi(), majrur("أَقْرَبِ", "aqrab", "«the shortest»", "«en kısa»", tags=[ID, "ism-tafdil", MM], ar="مَجْرُورٌ بِفِي، مُضَافٌ — اسْمُ تَفْضِيلٍ."),
  mudaf_ilayh("وَقْتٍ", "waqt", "«time»", "«vakit»"),
  tok("وَأَسْرَعِ", "asra", "noun", [AT, ID, "ism-tafdil", MM], "الْوَاوُ عَاطِفَةٌ، وَأَسْرَعِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ — اسْمُ تَفْضِيلٍ.", "«and the quickest»", "«ve en hızlı»", segments=wa_("أَسْرَعِ", "asra", "noun")),
  mudaf_ilayh("زَمَانٍ", "zaman", "«span»", "«zaman»", punct="،"),
])
sen("s7", "and He subjected to him the strong and the skilled among the jinn, and the rebels among the devils, who carried out his orders and completed his giant building and construction projects.",
        "cinlerden güçlü ve becerikli olanları, şeytanlardan âsileri de onun emrine verdi; bunlar onun buyruklarını yerine getirir, dev imar ve yapı projelerini tamamlardı.", [
  mazi("وَسَخَّرَ", "sakhkhara", "«and He subjected»", "«ve emrine verdi»", tags=[AT, "form-ii-verbs"], wa=True, hidden="هُوَ"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«to him»", "«ona»"),
  tok("الْأَقْوِيَاءَ", "qawi", "noun", [MB, JT, MM], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ تَكْسِيرٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«the strong» — the object; a diptote plural.", "«güçlüleri» — mef'ûl; gayr-i munsarıf."),
  tok("وَالْحَاذِقِينَ", "hadhiq", "noun", [AT, JS, "ism-fail"], "الْوَاوُ عَاطِفَةٌ، وَالْحَاذِقِينَ مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«and the skilled» — joined; naṣb by the yāʾ.", "«ve becerikliler» — ma'tûf; yâ ile mansub.", segments=wa_("الْحَاذِقِينَ", "hadhiq", "noun")),
  prep("مِنَ", "min", "«among»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْجِنِّ", "jinn", "«the jinn»", "«cinler»", punct="،"),
  tok("وَالْمَارِدِينَ", "marid-rebel", "noun", [AT, JS, "ism-fail"], "الْوَاوُ عَاطِفَةٌ، وَالْمَارِدِينَ مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ.", "«and the rebels» — joined; naṣb by the yāʾ.", "«ve âsileri» — ma'tûf; yâ ile mansub.", segments=wa_("الْمَارِدِينَ", "marid-rebel", "noun")),
  prep("مِنَ", "min", "«among»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الشَّيَاطِينِ", "shaytan", "«the devils»", "«şeytanlar»", tags=[JT], punct="،"),
  khamsa("يُنَفِّذُونَ", "naffadha", "«carrying out»", "«yerine getirirler»", tags=[HL, MB, "form-ii-verbs"], extra_ar=" — وَالْجُمْلَةُ حَالٌ"),
  noun_pron("أَوَامِرَهُ", "amr-noun", "أَوَامِرَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his orders»", "«buyruklarını»", tags=[MB, ID, JT], punct="،"),
  khamsa("وَيُكْمِلُونَ", "akmala", "«and completing»", "«ve tamamlarlar»", tags=[AT, MB, "form-iv-verbs"], wa=True),
  noun_pron("مَشَارِيعَهُ", "mashru", "مَشَارِيعَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his projects»", "«projelerini»", tags=[MB, ID, JT]),
  naat("الْعُمْرَانِيَّةَ", "umrani", "«building»", "«imar»", case="nasb", tags=["ism-mansub"]),
  naat("وَالْبِنَائِيَّةَ", "binai", "«construction»", "«yapı»", case="nasb", tags=["ism-mansub"], wa=True),
  naat("الْعِمْلَاقَةَ", "imlaq", "«giant»", "«dev»", case="nasb", punct="."),
])
sen("s8", "«And to Sulaymān [We subjected] the wind, blowing strongly, running at his command to the land We had blessed; and We were knowing of everything» (21:81).",
        "«Süleyman'a da şiddetle esen rüzgârı [boyun eğdirdik]; onun emriyle, bereket verdiğimiz yere doğru akardı; biz her şeyi bilenlerdik» (21:81).", [
  *quran([
  tok("وَلِسُلَيْمَانَ", "sulayman", "propn", [AT, HJ, MM], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَسُلَيْمَانَ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — مُتَعَلِّقٌ بِفِعْلٍ مَحْذُوفٍ (سَخَّرْنَا).", "«and to Sulaymān» — jarr by FATḤA (a diptote); the verb «We subjected» is understood.", "«ve Süleyman'a» — gayr-i munsarıf, fetha ile mecrûr; fiil (sahharnâ) mukadder.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("سُلَيْمَانَ", "sulayman", "propn")]),
  tok("الرِّيحَ", "rih", "noun", [MB, "hadhf-wa-taqdir"], "مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: سَخَّرْنَا.", "«the wind» — the object of the understood «We subjected».", "«rüzgârı» — mukadder fiilin mef'ûlü."),
  tok("عَاصِفَةً", "asifa", "noun", [HL, "ism-fail"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«blowing strongly» — the ḥāl.", "«şiddetle eser hâlde» — hâl."),
  mudari("تَجْرِي", "jara", "«running»", "«akar»", tags=[HL, "naqis-verbs"], hidden="هِيَ", extra_ar=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْجُمْلَةُ حَالٌ ثَانِيَةٌ"),
  noun_pron("بِأَمْرِهِ", "amr-noun", "بِأَمْرِ", "هِ", "pron-3ms", "الْبَاءُ حَرْفُ جَرٍّ، وَأَمْرِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«at his command»", "«onun emriyle»", tags=[HJ, ID]),
  prep("إِلَى", "ila", "«to»", "«-e doğru»"),
  majrur("الْأَرْضِ", "ard", "«the land»", "«yere»"),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ لِلْأَرْضِ.", "«which» — a naʿt of the land.", "«… -diğimiz» — yerin sıfatı."),
  tok("بَارَكْنَا", "baraka-bless", "verb", [MW, "form-iii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ — صِلَةٌ.", "«We blessed» — the ṣila; nā the doer.", "«bereket verdik» — sıla; nâ fâil.", segments=[seg("بَارَكْ", "baraka-bless", "verb"), seg("نَا", "pron-1p", "pron")]),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in it»", "«ona»"),
  tok("وَكُنَّا", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَنَا اسْمُهُ.", "«and We were» — kāna with nā as its ism.", "«ve biz … idik» — kâne; nâ ismi.", segments=[seg("وَ", "wa", "conj"), seg("كُنْ", "kana", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("بِكُلِّ", "kull", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَكُلِّ مَجْرُورٌ، مُضَافٌ — مُتَعَلِّقٌ بِعَالِمِينَ.", "«of every» — attached to the khabar.", "«her» — habere bağlı.", segments=[seg("بِ", "bi", "prep"), seg("كُلِّ", "kull", "noun")]),
  mudaf_ilayh("شَيْءٍ", "shay", "«thing»", "«şeyi»"),
  tok("عَالِمِينَ", "alim-knowing", "noun", [KN, JS, "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«knowing» — kāna's khabar, naṣb by the yāʾ.", "«bilenler» — kâne'nin haberi, yâ ile mansub.", punct="."),
  ]),
])
sen("s9", "«And among the devils were some who dived for him and did work besides that; and We were their keepers» (21:82).",
        "«Şeytanlardan da onun için dalgıçlık edenler ve bundan başka işler yapanlar vardı; biz onları gözetirdik» (21:82).", [
  *quran([
  tok("وَمِنَ", "min", "prep", [AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَمِنَ حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«and among» — the jarr phrase is a fronted khabar.", "«ve … -den» — câr-mecrûr öne alınmış haber.", segments=wa_("مِنَ", "min", "prep")),
  majrur("الشَّيَاطِينِ", "shaytan", "«the devils»", "«şeytanlar»", tags=[JT]),
  tok("مَنْ", "man-mawsula", "pron", [MK, MW], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.", "«some who» — the relative, the delayed mubtadaʾ.", "«… -enler» — ism-i mevsûl, sonraya bırakılmış mübtedâ."),
  khamsa("يَغُوصُونَ", "ghasa", "«dived»", "«dalarlar»", tags=[MW, "hollow-verbs"], extra_ar=" — صِلَةٌ"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«for him»", "«onun için»"),
  khamsa("وَيَعْمَلُونَ", "amila", "«and did»", "«ve yaparlar»", tags=[AT, MB], wa=True),
  tok("عَمَلًا", "amal-work", "noun", [MB, "masdar"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«work» — the object.", "«iş» — mef'ûl."),
  tok("دُونَ", "duna", "noun", [NA, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — فِي مَحَلِّ نَصْبٍ نَعْتٌ لِعَمَلًا.", "«besides» — a ẓarf, annexed; a naʿt of the work.", "«… -den başka» — zarf, muzâf; amelin sıfatı."),
  tok("ذٰلِكَ", "dhalika", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that» — the muḍāf ilayh.", "«bu» — muzâfun ileyh."),
  tok("وَكُنَّا", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَنَا اسْمُهُ.", "«and We were» — kāna with nā as its ism.", "«ve biz … idik» — kâne; nâ ismi.", segments=[seg("وَ", "wa", "conj"), seg("كُنْ", "kana", "verb"), seg("نَا", "pron-1p", "pron")]),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«of them»", "«onları»"),
  tok("حَافِظِينَ", "hafiz", "noun", [KN, JS, "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«keepers» — kāna's khabar, naṣb by the yāʾ.", "«gözetenler» — kâne'nin haberi, yâ ile mansub.", punct="."),
  ]),
])
sen("s10", "«And to Sulaymān the wind — its morning course a month and its evening course a month; and We made the spring of molten brass flow for him» (34:12).",
        "«Süleyman'a da rüzgârı [boyun eğdirdik]: sabah gidişi bir ay, akşam dönüşü bir ay; erimiş bakır kaynağını onun için akıttık» (34:12).", [
  *quran([
  tok("وَلِسُلَيْمَانَ", "sulayman", "propn", [AT, HJ, MM], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَسُلَيْمَانَ مَجْرُورٌ بِالْفَتْحَةِ — مُتَعَلِّقٌ بِفِعْلٍ مَحْذُوفٍ (سَخَّرْنَا).", "«and to Sulaymān» — jarr by fatḥa; the verb is understood.", "«ve Süleyman'a» — fetha ile mecrûr; fiil mukadder.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("سُلَيْمَانَ", "sulayman", "propn")]),
  tok("الرِّيحَ", "rih", "noun", [MB, "hadhf-wa-taqdir"], "مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: سَخَّرْنَا.", "«the wind» — the object of the understood verb.", "«rüzgârı» — mukadder fiilin mef'ûlü."),
  noun_pron("غُدُوُّهَا", "ghuduww", "غُدُوُّ", "هَا", "pron-3fs", "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ حَالٌ.", "«its morning course» — the mubtadaʾ; the clause is a ḥāl.", "«sabah gidişi» — mübtedâ; cümle hâl.", tags=[MK, ID, HL, "masdar"]),
  tok("شَهْرٌ", "shahr", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a month» — the khabar.", "«bir ay» — haber."),
  noun_pron("وَرَوَاحُهَا", "rawah", "وَرَوَاحُ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَرَوَاحُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its evening course» — a second mubtadaʾ.", "«ve akşam dönüşü» — ikinci mübtedâ.", tags=[AT, MK, ID, "masdar"]),
  tok("شَهْرٌ", "shahr", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a month» — the khabar.", "«bir ay» — haber."),
  tok("وَأَسَلْنَا", "asala", "verb", [AT, MB, "hollow-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَسَلْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ.", "«and We made flow» — the hollow IV before nā; nā the doer.", "«ve akıttık» — ecvef if'âl; nâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("أَسَلْ", "asala", "verb"), seg("نَا", "pron-1p", "pron")]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«for him»", "«onun için»"),
  tok("عَيْنَ", "ayn", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«the spring» — the object, annexed.", "«kaynağını» — mef'ûl, muzâf."),
  mudaf_ilayh("الْقِطْرِ", "qitr", "«of molten brass»", "«erimiş bakırın»", punct="."),
  ]),
])
sen("s11", "«And among the jinn were some who worked before him by the leave of his Lord; and whoever of them swerved from Our command, We made him taste of the torment of the Blaze» (34:12).",
        "«Cinlerden de Rabbinin izniyle onun önünde çalışanlar vardı; onlardan kim emrimizden saparsa ona alevli azaptan tattırırız» (34:12).", [
  *quran([
  tok("وَمِنَ", "min", "prep", [AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَمِنَ حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and among» — a fronted khabar.", "«ve … -den» — öne alınmış haber.", segments=wa_("مِنَ", "min", "prep")),
  majrur("الْجِنِّ", "jinn", "«the jinn»", "«cinler»"),
  tok("مَنْ", "man-mawsula", "pron", [MK, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.", "«some who» — the relative, the delayed mubtadaʾ.", "«… -enler» — ism-i mevsûl, mübtedâ."),
  mudari("يَعْمَلُ", "amila", "«worked»", "«çalışır»", tags=[MW], hidden="هُوَ", extra_ar=" — صِلَةٌ"),
  tok("بَيْنَ", "bayna", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«before» (lit. between)", "«önünde»"),
  noun_pron("يَدَيْهِ", "yad", "يَدَيْ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his two hands» — a dual in jarr by the yāʾ; its nūn dropped for the iḍāfa.", "«iki elinin» — tesniye, yâ ile mecrûr; nûnu izâfet için düşmüş.", tags=[ID, "al-muthanna"]),
  tok("بِإِذْنِ", "idhn", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَإِذْنِ مَجْرُورٌ، مُضَافٌ.", "«by the leave»", "«izniyle»", segments=[seg("بِ", "bi", "prep"), seg("إِذْنِ", "idhn", "noun")]),
  noun_pron("رَبِّهِ", "rabb", "رَبِّ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«of his Lord»", "«Rabbinin»", tags=[ID]),
  tok("وَمَنْ", "man-shartiyya", "pron", [AT, SH, MK], "الْوَاوُ عَاطِفَةٌ، وَمَنْ اسْمُ شَرْطٍ جَازِمٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and whoever» — the conditional man, giving jazm; a mubtadaʾ.", "«ve kim» — şart ismi, cezmeder; mübtedâ.", segments=wa_("مَنْ", "man-shartiyya", "pron")),
  tok("يَزِغْ", "zagha", "verb", [SH, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِعْلُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، حُذِفَ حَرْفُ الْعِلَّةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«swerves» — the shart verb in jazm; the hollow's long vowel drops before the sukūn.", "«sapar» — şart fiili, meczum; ecvefin uzun ünlüsü iki sâkin yüzünden düşmüş."),
  prep_pron("مِنْهُمْ", "min", "هُمْ", "pron-3mp", "«of them»", "«onlardan»"),
  prep("عَنْ", "an", "«from»", "«-den»"),
  noun_pron("أَمْرِنَا", "amr-noun", "أَمْرِ", "نَا", "pron-1p", "مَجْرُورٌ بِعَنْ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«Our command»", "«emrimizden»", tags=[HJ, ID]),
  tok("نُذِقْهُ", "adhaqa", "verb", [SH, MX, "hollow-verbs", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ جَوَابُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«We make him taste» — the answer verb in jazm; the hāʾ the object.", "«ona tattırırız» — cevap fiili, meczum; hâ mef'ûl.", segments=[seg("نُذِقْ", "adhaqa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("عَذَابِ", "adhab", "«the torment»", "«azabından»", tags=[ID], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("السَّعِيرِ", "sair", "«of the Blaze»", "«alevli ateşin»", punct="."),
  ]),
])
sen("s12", "«They made for him whatever he wished: sanctuaries, statues, basins like reservoirs, and cauldrons firmly set» (34:13).",
        "«Onun için dilediğini yaparlardı: mâbetler, heykeller, havuz gibi çanaklar ve yerinden kalkmaz kazanlar» (34:13).", [
  *quran([
  khamsa("يَعْمَلُونَ", "amila", "«they made»", "«yaparlar»", tags=[MB]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«for him»", "«onun için»"),
  tok("مَا", "ma-mawsula", "pron", [MB, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«whatever» — the relative, the object.", "«… -ni» — ism-i mevsûl, mef'ûl."),
  mudari("يَشَاءُ", "shaa", "«he wished»", "«diler»", tags=[MW, "hollow-verbs"], hidden="هُوَ", extra_ar=" — صِلَةٌ"),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  tok("مَحَارِيبَ", "mihrab", "noun", [HJ, JT, MM], "مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ (صِيغَةُ مُنْتَهَى الْجُمُوعِ).", "«sanctuaries» — jarr by FATḤA: a diptote plural of the utmost form.", "«mâbetler» — gayr-i munsarıf (müntehe'l-cumû'); fetha ile mecrûr."),
  tok("وَتَمَاثِيلَ", "timthal", "noun", [AT, JT, MM], "الْوَاوُ عَاطِفَةٌ، وَتَمَاثِيلَ مَعْطُوفٌ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and statues» — joined; a diptote, jarr by fatḥa.", "«ve heykeller» — ma'tûf; gayr-i munsarıf, fetha ile.", segments=wa_("تَمَاثِيلَ", "timthal", "noun")),
  atf("وَجِفَانٍ", "jafna", "«basins»", "«çanaklar»", "jarr", tags=[JT]),
  tok("كَالْجَوَابِ", "jawabi-basins", "noun", [HJ, NA, "tashbih"], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَالْجَوَابِ مَجْرُورٌ — نَعْتٌ لِجِفَانٍ.", "«like reservoirs» — the kāf of likeness; a naʿt of the basins.", "«havuz gibi» — teşbih kâfı; çanakların sıfatı.", segments=[seg("كَ", "ka", "prep"), seg("الْجَوَابِ", "jawabi-basins", "noun")]),
  atf("وَقُدُورٍ", "qidr", "«cauldrons»", "«kazanlar»", "jarr", tags=[JT]),
  tok("رَاسِيَاتٍ", "rasiya", "noun", [NA, JM, "ism-fail"], "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«firmly set» — the naʿt; a sound feminine plural.", "«yerinden kalkmaz» — sıfat; cem'-i müennes sâlim.", punct="."),
  ]),
])
sen("s13", "«Work, O family of Dāwūd, in thankfulness — and few of My servants are the thankful» (34:13).",
        "«Ey Dâvûd ailesi, şükür olarak çalışın — kullarımdan şükreden azdır» (34:13).", [
  *quran([
  tok("اعْمَلُوا", "amila", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«work» — an imperative on the dropped nūn; the wāw is the doer.", "«çalışın» — nûnun düşmesi üzere mebnî emir; vâv fâil."),
  tok("آلَ", "aal", "noun", ["vocative-munada", ID], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ، حُذِفَ حَرْفُ النِّدَاءِ.", "«O family [of]» — a munādā annexed, in naṣb; the vocative particle dropped.", "«ey ailesi» — muzâf münâdâ, mansub; nidâ harfi hazfedilmiş."),
  tok("دَاوُدَ", "dawud", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«of Dāwūd» — jarr by fatḥa (a diptote).", "«Dâvûd'un» — gayr-i munsarıf, fetha ile mecrûr."),
  tok("شُكْرًا", "shukr", "noun", ["maful-lah", "masdar"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ (أَوْ مَفْعُولٌ مُطْلَقٌ: اشْكُرُوا شُكْرًا).", "«in thankfulness» — the object of purpose (or an absolute object).", "«şükür olarak» — mef'ûlün leh (ya da mef'ûl-i mutlak)."),
  tok("وَقَلِيلٌ", "qalil", "noun", [AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ (أَوِ الْحَالِ)، وَقَلِيلٌ خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ.", "«and few» — a fronted khabar.", "«ve az» — öne alınmış haber.", segments=wa_("قَلِيلٌ", "qalil", "noun")),
  prep("مِنْ", "min", "«of»", "«-den»"),
  noun_pron("عِبَادِيَ", "abd", "عِبَادِ", "يَ", "pron-1s", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ (فُتِحَتْ).", "«My servants»", "«kullarımdan»", tags=[HJ, ID, JT, "ya-al-mutakallim"]),
  tok("الشَّكُورُ", "shakur", "noun", [MK, "sighat-mubalagha"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the thankful» — the delayed mubtadaʾ; an intensive.", "«çok şükreden» — sonraya bırakılmış mübtedâ; mübalağa sîgası.", punct="."),
  ]),
])

# ---------------------------------------------------------------- the glossary (checked with lemma_clash.py: wasi-wide, hadhiq, hakim-ruler, hawa-desire, dalla-stray, marid-rebel, jawabi-basins are the new keys where the plain key means another word)
CAND = {
 "wasi-wide": G("wasi-wide", "وَاسِع", "و س ع", "noun", "wide, ample (an active participle)", "geniş (ism-i fâil)", 1),
 "yad": G("yad", "يَد", "ي د ي", "noun", "a hand", "el", 1, plural="أَيْدٍ"),
 "hadhiq": G("hadhiq", "حَاذِق", "ح ذ ق", "noun", "skilled, adept (an active participle)", "becerikli, mahir (ism-i fâil)", 3, plural="حُذَّاق"),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong, mighty", "güçlü, kuvvetli", 1, plural="أَقْوِيَاء"),
 "abd": G("abd", "عَبْد", "ع ب د", "noun", "a servant, a slave", "kul, köle", 1, plural="عِبَاد"),
 "khashi": G("khashi", "خَاشِع", "خ ش ع", "noun", "humble, in awe (an active participle)", "huşû içinde, boyun eğmiş (ism-i fâil)", 2),
 "awwab": G("awwab", "أَوَّاب", "أ و ب", "noun", "ever-returning to God, penitent (an intensive; Qurʾānic)", "Allah'a çokça dönen, evvâb (mübalağa; Kur'ânî)", 3),
 "daim": G("daim", "دَائِم", "د و م", "noun", "constant, lasting (an active participle)", "dâimî, sürekli (ism-i fâil)", 2),
 "dhikr": G("dhikr", "ذِكْر", "ذ ك ر", "noun", "remembrance, mention", "zikir, anma", 2),
 "tawil-long": G("tawil-long", "طَوِيل", "ط و ل", "noun", "long", "uzun", 1),
 "dua": G("dua", "دُعَاء", "د ع و", "noun", "supplication, prayer", "dua", 1),
 "tasbih": G("tasbih", "تَسْبِيح", "س ب ح", "noun", "glorification", "tesbih", 2),
 "hakim-ruler": G("hakim-ruler", "حَاكِم", "ح ك م", "noun", "a ruler, a judge (an active participle)", "hükümdar, hâkim (ism-i fâil)", 2, plural="حُكَّام"),
 "muqsit": G("muqsit", "مُقْسِط", "ق س ط", "noun", "just, equitable (the active participle of Form IV)", "âdil, adaletli (if'âl ism-i fâili)", 3),
 "hakama": G("hakama", "حَكَمَ", "ح ك م", "verb", "to judge, to rule", "hükmetmek", 1),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between — a ẓarf of place", "arasında — mekân zarfı", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "haqq": G("haqq", "حَقّ", "ح ق ق", "noun", "truth, right", "hak, gerçek", 1),
 "haba": G("haba", "حَابَى", "ح ب و", "verb", "to favour, to be partial to (Form III, defective)", "kayırmak, taraf tutmak (müfâale, nâkıs)", 3),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "He is exalted (Form VI, said of God)", "yücedir (tefâul; Allah için)", 1),
 "jaala": G("jaala", "جَعَلَ", "ج ع ل", "verb", "to make (two objects), to set", "kılmak (iki mef'ûl), yapmak", 1),
 "khalifa": G("khalifa", "خَلِيفَة", "خ ل ف", "noun", "a vicegerent, a successor", "halife", 2, plural="خُلَفَاء"),
 "ard": G("ard", "أَرْض", "أ ر ض", "noun", "the earth, the land", "yer, toprak", 1),
 "la-nahiya": G("la-nahiya", "لَا (النَّاهِيَة)", None, "part", "the prohibiting lā — it gives the muḍāriʿ jazm", "nehiy lâ'sı — muzariyi cezmeder", 1),
 "ittabaa": G("ittabaa", "اِتَّبَعَ", "ت ب ع", "verb", "to follow (Form VIII)", "uymak, izlemek (iftiâl)", 2),
 "hawa-desire": G("hawa-desire", "هَوًى", "ه و ي", "noun", "desire, caprice (a maqṣūr noun)", "hevâ, nefsin arzusu (maksûr isim)", 2),
 "adalla": G("adalla", "أَضَلَّ", "ض ل ل", "verb", "to lead astray (Form IV, doubled)", "saptırmak (if'âl, muzâaf)", 2),
 "sabil": G("sabil", "سَبِيل", "س ب ل", "noun", "a path, a way", "yol, sebil", 1),
 "dalla-stray": G("dalla-stray", "ضَلَّ", "ض ل ل", "verb", "to stray, to go astray (doubled)", "sapmak (muzâaf)", 2),
 "shadid": G("shadid", "شَدِيد", "ش د د", "noun", "severe, strong", "şiddetli, güçlü", 1),
 "ma-masdariyya": G("ma-masdariyya", "مَا (الْمَصْدَرِيَّة)", None, "part", "the maṣdar-mā — turns the clause after it into a verbal noun", "masdariyye mâ — sonrasını masdara çevirir", 2),
 "nasiya": G("nasiya", "نَسِيَ", "ن س ي", "verb", "to forget", "unutmak", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "a day", "gün", 1, plural="أَيَّام"),
 "hisab": G("hisab", "حِسَاب", "ح س ب", "noun", "reckoning, account", "hesap", 2),
 "rih": G("rih", "رِيح", "ر و ح", "noun", "wind", "rüzgâr", 1, plural="رِيَاح"),
 "jara": G("jara", "جَرَى", "ج ر ي", "verb", "to run, to flow", "akmak, koşmak", 1),
 "amr-noun": G("amr-noun", "أَمْر", "أ م ر", "noun", "a command, an order; a matter", "emir, buyruk; iş", 1, plural="أَوَامِر"),
 "hamala": G("hamala", "حَمَلَ", "ح م ل", "verb", "to carry", "taşımak", 1),
 "makan": G("makan", "مَكَان", "ك و ن", "noun", "a place", "yer, mekân", 1),
 "wasala": G("wasala", "وَصَلَ", "و ص ل", "verb", "to arrive, to reach (an assimilated verb: يَصِلُ)", "ulaşmak, varmak (misâl fiil: yasilu)", 1),
 "aqrab": G("aqrab", "أَقْرَب", "ق ر ب", "noun", "nearer, nearest; shortest (an elative)", "en yakın; en kısa (ism-i tafdîl)", 2),
 "waqt": G("waqt", "وَقْت", "و ق ت", "noun", "time, a moment", "vakit", 1),
 "asra": G("asra", "أَسْرَع", "س ر ع", "noun", "quicker, quickest (an elative)", "en hızlı (ism-i tafdîl)", 2),
 "zaman": G("zaman", "زَمَان", "ز م ن", "noun", "time, a span of time", "zaman", 1),
 "jinn": G("jinn", "جِنّ", "ج ن ن", "noun", "the jinn (a collective)", "cinler (cins ismi)", 1),
 "marid-rebel": G("marid-rebel", "مَارِد", "م ر د", "noun", "a rebel, an insolent one (an active participle)", "âsi, azgın (ism-i fâil)", 3),
 "shaytan": G("shaytan", "شَيْطَان", "ش ط ن", "noun", "a devil", "şeytan", 1, plural="شَيَاطِين"),
 "naffadha": G("naffadha", "نَفَّذَ", "ن ف ذ", "verb", "to carry out, to execute (Form II)", "yerine getirmek, uygulamak (tef'îl)", 3),
 "akmala": G("akmala", "أَكْمَلَ", "ك م ل", "verb", "to complete (Form IV)", "tamamlamak (if'âl)", 2),
 "mashru": G("mashru", "مَشْرُوع", "ش ر ع", "noun", "a project (a passive participle)", "proje, girişim (ism-i mef'ûl)", 3, plural="مَشَارِيع"),
 "umrani": G("umrani", "عُمْرَانِيّ", "ع م ر", "noun", "of building and development (a nisba)", "imara ait, imar- (nisbet)", 3),
 "binai": G("binai", "بِنَائِيّ", "ب ن ي", "noun", "of construction (a nisba)", "yapıya ait, inşaat- (nisbet)", 3),
 "imlaq": G("imlaq", "عِمْلَاق", "ع م ل ق", "noun", "giant, gigantic", "dev, devasa", 3),
 "asifa": G("asifa", "عَاصِفَة", "ع ص ف", "noun", "blowing violently (of wind); a storm", "şiddetle esen; fırtına", 3),
 "baraka-bless": G("baraka-bless", "بَارَكَ", "ب ر ك", "verb", "to bless (Form III, with fī)", "bereket vermek (müfâale, fî ile)", 2),
 "alim-knowing": G("alim-knowing", "عَالِم", "ع ل م", "noun", "knowing; a scholar (an active participle)", "bilen; âlim (ism-i fâil)", 1, plural="عُلَمَاء"),
 "man-mawsula": G("man-mawsula", "مَنْ (الْمَوْصُولَة)", None, "pron", "who, whoever — the relative man", "… -en kimse — ism-i mevsûl men", 1),
 "ghasa": G("ghasa", "غَاصَ", "غ و ص", "verb", "to dive (hollow)", "dalmak (ecvef)", 3),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to do, to work", "yapmak, çalışmak", 1),
 "amal-work": G("amal-work", "عَمَل", "ع م ل", "noun", "work, a deed", "iş, amel", 1),
 "duna": G("duna", "دُونَ", "د و ن", "noun", "besides, short of — a ẓarf", "… -den başka, aşağısında — zarf", 2),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o, şu", 1),
 "hafiz": G("hafiz", "حَافِظ", "ح ف ظ", "noun", "a keeper, a guardian (an active participle)", "koruyan, gözeten (ism-i fâil)", 2),
 "ghuduww": G("ghuduww", "غُدُوّ", "غ د و", "noun", "the morning course, going out in the morning (a maṣdar)", "sabah gidişi (masdar)", 3),
 "shahr": G("shahr", "شَهْر", "ش ه ر", "noun", "a month", "ay", 1, plural="شُهُور"),
 "rawah": G("rawah", "رَوَاح", "ر و ح", "noun", "the evening course, returning in the evening (a maṣdar)", "akşam dönüşü (masdar)", 3),
 "asala": G("asala", "أَسَالَ", "س ي ل", "verb", "to make flow (Form IV, hollow)", "akıtmak (if'âl, ecvef)", 3),
 "ayn": G("ayn", "عَيْن", "ع ي ن", "noun", "a spring; an eye", "kaynak, pınar; göz", 1, plural="عُيُون"),
 "qitr": G("qitr", "قِطْر", "ق ط ر", "noun", "molten brass, copper", "erimiş bakır", 3),
 "idhn": G("idhn", "إِذْن", "أ ذ ن", "noun", "leave, permission", "izin", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "man-shartiyya": G("man-shartiyya", "مَنْ (الشَّرْطِيَّة)", None, "pron", "whoever — the conditional man, giving jazm to two verbs", "kim … -se — şart ismi men, iki fiili cezmeder", 2),
 "zagha": G("zagha", "زَاغَ", "ز ي غ", "verb", "to swerve, to deviate (hollow)", "sapmak, kaymak (ecvef)", 3),
 "adhaqa": G("adhaqa", "أَذَاقَ", "ذ و ق", "verb", "to make taste (Form IV, hollow; two objects)", "tattırmak (if'âl, ecvef; iki mef'ûl)", 3),
 "adhab": G("adhab", "عَذَاب", "ع ذ ب", "noun", "torment, punishment", "azap", 1),
 "sair": G("sair", "سَعِير", "س ع ر", "noun", "the Blaze — a name of Hell", "alevli ateş, Saîr — cehennemin bir adı", 3),
 "shaa": G("shaa", "شَاءَ", "ش ي أ", "verb", "to will, to wish (hollow)", "dilemek (ecvef)", 1),
 "mihrab": G("mihrab", "مِحْرَاب", "ح ر ب", "noun", "a sanctuary, a prayer niche; a palace", "mâbet, mihrap; saray", 3, plural="مَحَارِيب"),
 "timthal": G("timthal", "تِمْثَال", "م ث ل", "noun", "a statue, an image", "heykel, timsal", 3, plural="تَمَاثِيل"),
 "jafna": G("jafna", "جَفْنَة", "ج ف ن", "noun", "a large bowl, a basin", "büyük çanak, tekne", 3, plural="جِفَان"),
 "jawabi-basins": G("jawabi-basins", "جَوَابٍ (جَمْعُ جَابِيَةٍ)", "ج ب ي", "noun", "reservoirs, cisterns — the plural of jābiya (Qurʾānic جَوَابٍ, 34:13)", "havuzlar, sarnıçlar — câbiye'nin çoğulu (Kur'ânî cevâb, 34:13)", 3),
 "qidr": G("qidr", "قِدْر", "ق د ر", "noun", "a cauldron, a cooking pot", "kazan, tencere", 2, plural="قُدُور"),
 "rasiya": G("rasiya", "رَاسِيَة", "ر س و", "noun", "firmly set, immovable (an active participle)", "yerinden kalkmaz, sabit (ism-i fâil)", 3, plural="رَاسِيَات"),
 "aal": G("aal", "آل", "أ و ل", "noun", "family, house (of a prophet or a king)", "âl, aile, hanedan", 2),
 "shukr": G("shukr", "شُكْر", "ش ك ر", "noun", "thankfulness, gratitude", "şükür", 1),
 "qalil": G("qalil", "قَلِيل", "ق ل ل", "noun", "few, little", "az", 1),
 "shakur": G("shakur", "شَكُور", "ش ك ر", "noun", "very thankful (an intensive)", "çok şükreden (mübalağa)", 2),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "every, all", "her, bütün", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "a thing", "şey", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (masc. singular, attached)", "sen / senin (bitişik)", 1),
 "ka": G("ka", "كَ", None, "prep", "the kāf of likeness — «like»", "teşbih kâfı — «gibi»", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this (masculine)", "bu (müzekker)", 1),
 "mulk": G("mulk", "مُلْك", "م ل ك", "noun", "kingship, dominion", "mülk, hükümdarlık", 2),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "hakama", _sg.sound1("nasara", "حَكَم", "حْكُم", "اُحْكُم", "حُكْم", "حَاكِم", "مَحْكُوم", "حُكِمَ", "يُحْكَمُ", "حَكَمَ بَيْنَهُمْ: قَضَى."))
put_morph(mo, "jaala", _sg.sound1("fataha", "جَعَل", "جْعَل", "اِجْعَل", "جَعْل", "جَاعِل", "مَجْعُول", "جُعِلَ", "يُجْعَلُ", "جَعَلَهُ كَذَا: صَيَّرَهُ."))
put_morph(mo, "ittabaa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِتَّبَع", "تَّبِع", "اِتَّبِع", "اِتِّبَاع", "مُتَّبِع", "مُتَّبَع", "اُتُّبِعَ", "يُتَّبَعُ", "اِتَّبَعَهُ: سَارَ خَلْفَهُ وَاقْتَدَى بِهِ."))
put_morph(mo, "hamala", _sg.sound1("daraba", "حَمَل", "حْمِل", "اِحْمِل", "حَمْل", "حَامِل", "مَحْمُول", "حُمِلَ", "يُحْمَلُ", "حَمَلَ الشَّيْءَ: رَفَعَهُ وَنَقَلَهُ."))
put_morph(mo, "naffadha", _sg.derived(_sg.B2, _sg.W2, "ُ", "نَفَّذ", "نَفِّذ", "نَفِّذ", "تَنْفِيذ", "مُنَفِّذ", "مُنَفَّذ", "نُفِّذَ", "يُنَفَّذُ", "نَفَّذَ الْأَمْرَ: أَمْضَاهُ وَعَمِلَ بِهِ."))
put_morph(mo, "akmala", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَكْمَل", "كْمِل", "أَكْمِل", "إِكْمَال", "مُكْمِل", "مُكْمَل", "أُكْمِلَ", "يُكْمَلُ", "أَكْمَلَ الشَّيْءَ: أَتَمَّهُ."))
put_morph(mo, "wasala", _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مِثَالٌ وَاوِيٌّ (تَسْقُطُ وَاوُهُ فِي الْمُضَارِعِ)", "فَعَلَ يَفْعِلُ", "وُصُول", "وَاصِل", _sg.mazi14("وَصَل"), _sg.mudari14("َ", "صِل"), _sg.amr_attach("صِل"), "يَصِلَ", "يَصِلْ", "تَصِلْ", "مَوْصُول", "وُصِلَ", "يُوصَلُ", "وَصَلَ إِلَى الْمَكَانِ: بَلَغَهُ."))
put_morph(mo, "ghasa", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "غَاص", "غُص", "غُوص", "غُص", "غُوص", "غُص", "غَوْص", "غَائِص", None, None, None, "غَاصَ فِي الْمَاءِ: نَزَلَ تَحْتَهُ."))
put_morph(mo, "zagha", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "زَاغ", "زِغ", "زِيغ", "زِغ", "زِيغ", "زِغ", "زَيْغ", "زَائِغ", None, None, None, "زَاغَ عَنِ الطَّرِيقِ: مَالَ عَنْهُ."))
put_morph(mo, "asala", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَسَال", "أَسَل", "سِيل", "سِل", "أَسِيل", "أَسِل", "إِسَالَة", "مُسِيل", "مُسَال", "أُسِيلَ", "يُسَالُ", "أَسَالَ الْمَاءَ: أَجْرَاهُ."))
put_morph(mo, "adhaqa", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَذَاق", "أَذَق", "ذِيق", "ذِق", "أَذِيق", "أَذِق", "إِذَاقَة", "مُذِيق", "مُذَاق", "أُذِيقَ", "يُذَاقُ", "أَذَاقَهُ الْعَذَابَ: جَعَلَهُ يَذُوقُهُ."))
put_morph(mo, "adalla", _sg.entry(_sg.B4 + " — مُضَاعَفٌ", _sg.W4, "إِضْلَال", "مُضِلّ", _sg.mazi14("أَضَلّ", "أَضْلَل"), _sg.mudari14("ُ", "ضِلّ", "ضْلِل"), ["أَضِلَّ", "أَضِلَّا", "أَضِلُّوا", "أَضِلِّي", "أَضِلَّا", "أَضْلِلْنَ"], "يُضِلَّ", "يُضِلَّ", "تُضِلَّ", "مُضَلّ", "أُضِلَّ", "يُضَلُّ", "أَضَلَّهُ: جَعَلَهُ يَضِلُّ — مُضَاعَفٌ: يُفَكُّ إِدْغَامُهُ عِنْدَ السُّكُونِ (أَضْلَلْتُ)، وَالْجَزْمُ بِالْفَتْحِ — لَمْ يُضِلَّ."))
put_morph(mo, "dalla-stray", _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مُضَاعَفٌ", "فَعَلَ يَفْعِلُ", "ضَلَال", "ضَالّ", _sg.mazi14("ضَلّ", "ضَلَل"), _sg.mudari14("َ", "ضِلّ", "ضْلِل"), ["ضِلَّ", "ضِلَّا", "ضِلُّوا", "ضِلِّي", "ضِلَّا", "اِضْلِلْنَ"], "يَضِلَّ", "يَضِلَّ", "تَضِلَّ", None, None, None, "ضَلَّ عَنِ الطَّرِيقِ: حَادَ عَنْهُ — مُضَاعَفٌ: ضَلَلْتُ، يَضْلِلْنَ؛ الْجَزْمُ بِالْفَتْحِ — لَمْ يَضِلَّ، وَيَجُوزُ لَمْ يَضْلِلْ."))
put_morph(mo, "haba", _sg.derived_naqis("مِنْ بَابِ الْمُفَاعَلَةِ", "فَاعَلَ يُفَاعِلُ", "ُ", "حَابَ", "حَاب", "i", "حَاب", "مُحَابَاة", "مُحَابٍ", "مُحَابًى", "حُوبِيَ", "يُحَابَى", "حَابَاهُ: مَالَ إِلَيْهِ وَانْحَازَ لَهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch7 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 7 (print pp. 13–14, §3–4): Dāwūd's thanks for the favour with 38:26 (s1–s5); God's favour on Sulaymān — the wind and the jinn with 21:81–82 and 34:12–13 (s6–s13)."
ADD_TR = " Yedinci bölüm (baskı s. 13–14, 3–4. kısımlar): Dâvûd'un nimete şükrü ve 38:26 (s1–s5); Süleyman'a lütuf — rüzgâr ve cinler, 21:81–82 ve 34:12–13 ile (s6–s13)."
write_out(7, S, TITLE, ADD_EN, ADD_TR, "Dāwūd and Sulaymān §3–4", GLOSS_ADD, notes=(), related=())
report(7, S, GLOSS_ADD, ())
