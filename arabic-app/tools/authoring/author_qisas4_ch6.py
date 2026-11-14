# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 6: «قِصَّةُ دَاوُدَ وَسُلَيْمَانَ — آلَاءُ اللهِ» — the opening of the story of Dāwūd and
Sulaymān (print pp. 11–13): the Qurʾān tells of God's bounties too (intro, §1 with 27:15–16), and the favour on Dāwūd (§2 with
34:10–11 and 21:79–80).
python3 tools/authoring/author_qisas4_ch6.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ دَاوُدَ وَسُلَيْمَانَ: آلَاءُ اللهِ", "en": "Dāwūd and Sulaymān: the bounties of God", "tr": "Dâvûd ve Süleyman: Allah'ın nimetleri"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"
def majrur(full, lex, en, tr, punct=None, tags=(), ar="مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [HJ] + list(tags), ar, en, tr, punct=punct)
def mudaf_ilayh(full, lex, en, tr, punct=None, tags=(), ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [ID] + list(tags), ar, en, tr, punct=punct)
def naat(full, lex, en, tr, punct=None, tags=(), case="jarr"):
    C = {"jarr": "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ.", "raf": "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "nasb": "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ."}[case]
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
def wa_name_nasb(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "propn", [AT, MM] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and» + " + en + " — joined; a diptote name.", "«ve» + " + tr + " — ma'tûf; gayr-i munsarıf özel isim.", punct=punct, segments=wa_(full[2:], lex, "propn"))
def wa_name_raf(full, lex, en, tr, punct=None, tags=(), sign="بِالضَّمَّةِ"):
    return tok(full, lex, "propn", [AT, MM] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " مَعْطُوفٌ مَرْفُوعٌ " + sign + " — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and» + " + en + " — joined, in rafʿ; a diptote name.", "«ve» + " + tr + " — ma'tûf, merfû; gayr-i munsarıf özel isim.", punct=punct, segments=wa_(full[2:], lex, "propn"))
def masdar_jarr(full, lex, en, tr, punct=None, wa=False, tags=()):
    if wa: return atf(full, lex, en, tr, "jarr", punct=punct, tags=["masdar"] + list(tags))
    return majrur(full, lex, en, tr, punct=punct, tags=["masdar"] + list(tags))

# ---------------------------------------------------------------- the intro (print p. 11)
sen("s1", "And the Qurʾān did not confine itself to recounting the days of God and what the prophets and messengers met of denial, mockery, insult and pursuit from the nations they were sent among,",
        "Kur'ân, Allah'ın günlerini ve peygamberlerle resûllerin, içlerine gönderildikleri ümmetlerden gördükleri yalanlama, alay, hakaret ve kovalamayı anlatmakla yetinmedi;", [
  tok("وَلَمْ", "lam-jazima", "part", [LJ], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not» — lam: negation, jazm, and the māḍī sense.", "«ve … -medi» — lem: nefiy, cezim ve mâzîye çevirme.", segments=wa_("لَمْ", "lam-jazima", "part")),
  tok("يَقْتَصِرِ", "iqtasara", "verb", [LJ, "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«confine itself» — jazm by lam (sukūn), kasra for the two sukūns.", "«yetinmek» — lem ile meczum (sükûn); iki sâkin için kesre.", ),
  fail("الْقُرْآنُ", "quran", "«the Qurʾān»", "«Kur'ân»"),
  prep("عَلَى", "ala", "«to»", "«-e»"),
  majrur("ذِكْرِ", "dhikr", "«the recounting»", "«anmak»", tags=[ID, "masdar"], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  mudaf_ilayh("أَيَّامِ", "yawm", "«the days»", "«günleri»", tags=[JT], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»"),
  tok("وَمَا", "ma-mawsula", "pron", [AT, MW], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ عَلَى ذِكْرِ فِي مَحَلِّ جَرٍّ.", "«and what» — the relative, joined to «recounting», in the place of jarr.", "«ve … -diklerini» — ism-i mevsûl, zikr'e ma'tûf, mahallen mecrûr.", segments=wa_("مَا", "ma-mawsula", "pron")),
  tok("لَقِيَهُ", "laqiya", "verb", [MW, MB, "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِلَةٌ.", "«met» — the ṣila; its object the hāʾ.", "«karşılaştı» — sıla; mef'ûl hâ.", segments=[seg("لَقِيَ", "laqiya", "verb"), pr3ms()]),
  fail("الْأَنْبِيَاءُ", "nabi", "«the prophets»", "«peygamberler»", tags=[JT]),
  atf("وَالرُّسُلُ", "rasul", "«the messengers»", "«resûller»", "raf", tags=[JT]),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  masdar_jarr("تَكْذِيبٍ", "takdhib", "«denial»", "«yalanlama»"),
  masdar_jarr("وَسُخْرِيَةٍ", "sukhriya", "«mockery»", "«alay»", wa=True),
  masdar_jarr("وَإِهَانَةٍ", "ihana", "«insult»", "«hakaret»", wa=True),
  masdar_jarr("وَمُطَارَدَةٍ", "mutarada", "«pursuit»", "«kovalama»", wa=True),
  prep("مِنَ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْأُمَمِ", "umma", "«the nations»", "«ümmetler»", tags=[JT]),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ لِلْأُمَمِ.", "«which» — a naʿt of the nations.", "«… -dikleri» — ümmetlerin sıfatı."),
  tok("بُعِثُوا", "baatha", "verb", [MW, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْوَاوُ نَائِبُ فَاعِلٍ — صِلَةٌ.", "«they were sent» — a passive; the wāw is the deputy doer; the ṣila.", "«gönderildiler» — meçhul; vâv nâib-i fâil; sıla."),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«among them»", "«içlerine»", punct="،"),
])
sen("s2", "and what these nations met of punishment and torment, ruin and destruction, for their denial of the messengers, their mockery of them, their plotting against them and their resolve to kill them — as has passed before you in the stories of the prophets.",
        "ve bu ümmetlerin, resûlleri yalanlamaları, onlarla alay etmeleri, onlara tuzak kurmaları ve onları öldürmeye kalkışmaları yüzünden gördükleri ceza ve azabı, helâk ve yıkımı — peygamberlerin kıssalarında önünüzden geçtiği gibi.", [
  tok("وَمَا", "ma-mawsula", "pron", [AT, MW], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«and what» — the relative, joined, in the place of jarr.", "«ve … -diklerini» — ism-i mevsûl, ma'tûf, mahallen mecrûr.", segments=wa_("مَا", "ma-mawsula", "pron")),
  mazi_ta("لَقِيَتْ", "laqiya", "«met»", "«gördü»", tags=[MW, "naqis-verbs"]),
  tok("هٰذِهِ", "hadhihi", "pron", ["asma-al-ishara", FL], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«these» — a demonstrative, the doer.", "«bu» — ism-i işâret, fâil."),
  tok("الْأُمَمُ", "umma", "noun", [BD, JT], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ (أَوْ عَطْفُ بَيَانٍ).", "«nations» — the badal of the demonstrative, in rafʿ.", "«ümmetler» — ism-i işâretten bedel, merfû."),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  masdar_jarr("عُقُوبَةٍ", "uquba", "«punishment»", "«ceza»"),
  masdar_jarr("وَعَذَابٍ", "adhab", "«torment»", "«azap»", wa=True, punct="،"),
  masdar_jarr("وَهَلَاكٍ", "halak", "«ruin»", "«helâk»", wa=True),
  masdar_jarr("وَدَمَارٍ", "damar", "«destruction»", "«yıkım»", wa=True, punct="،"),
  noun_pron("لِتَكْذِيبِهَا", "takdhib", "لِتَكْذِيبِ", "هَا", "pron-3fs", "اللَّامُ لِلتَّعْلِيلِ حَرْفُ جَرٍّ، وَتَكْذِيبِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«for their denial» — the lām of cause.", "«yalanlamaları yüzünden» — ta'lîl lâmı.", tags=[HJ, TA, ID, "masdar"]),
  tok("لِلرُّسُلِ", "rasul", "noun", [HJ, JT], "اللَّامُ حَرْفُ جَرٍّ، وَالرُّسُلِ مَجْرُورٌ — مَفْعُولُ الْمَصْدَرِ.", "«of the messengers» — the maṣdar's object through the lām.", "«resûlleri» — masdarın mef'ûlü, lâm ile.", punct="،", segments=[seg("لِ", "li", "prep"), seg("الرُّسُلِ", "rasul", "noun")]),
  noun_pron("وَاسْتِهْزَائِهَا", "istihza", "وَاسْتِهْزَائِ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَاسْتِهْزَائِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their mockery»", "«ve alay etmeleri»", tags=[AT, ID, "masdar"]),
  prep_pron("بِهِمْ", "bi", "هِمْ", "pron-3mp", "«of them»", "«onlarla»", punct="،"),
  noun_pron("وَكَيْدِهَا", "kayd", "وَكَيْدِ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَكَيْدِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their plotting»", "«ve tuzakları»", tags=[AT, ID, "masdar"]),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«against them»", "«onlara»", punct="،"),
  noun_pron("وَهَمِّهَا", "hamm", "وَهَمِّ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَهَمِّ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their resolve»", "«ve kalkışmaları»", tags=[AT, ID, "masdar"]),
  noun_pron("بِقَتْلِهِمْ", "qatl", "بِقَتْلِ", "هِمْ", "pron-3mp", "الْبَاءُ حَرْفُ جَرٍّ، وَقَتْلِ مَجْرُورٌ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«to kill them»", "«onları öldürmeye»", punct="،", tags=[HJ, ID, "masdar"]),
  tok("كَمَا", "kama", "part", [HJ], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ.", "«as» — the kāf of likeness with the maṣdar-mā.", "«… gibi» — teşbih kâfı ve masdariyye mâ."),
  mazi("مَرَّ", "marra", "«has passed»", "«geçti»", tags=["doubled-verbs"], hidden=None),
  prep_pron("بِكُمْ", "bi", "كُمْ", "pron-2mp", "«before you»", "«önünüzden»"),
  fi(), majrur("قَصَصِ", "qasas", "«the stories»", "«kıssaları»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  tok("النَّبِيِّينَ", "nabi", "noun", [ID, JS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«of the prophets» — jarr by the yāʾ, a sound plural.", "«peygamberlerin» — cem'-i müzekker sâlim, yâ ile mecrûr.", punct="."),
])

# ---------------------------------------------------------------- §1 الْقُرْآنُ يَتَحَدَّثُ عَنْ آلَاءِ اللهِ
sen("s3", "Rather, the Qurʾān spoke much of the bounties of God, and told — at length at times, in brief at times — of many favours He bestowed on many of the prophets:",
        "Aksine Kur'ân, Allah'ın nimetlerinden çokça söz etti; kimi zaman uzun uzun, kimi zaman kısaca, peygamberlerden pek çoğuna lütfettiği nice nimeti anlattı:", [
  tok("بَلْ", "bal", "part", [AT], "حَرْفُ إِضْرَابٍ وَابْتِدَاءٍ.", "«rather» — bal, turning from the previous sentence.", "«aksine» — idrâb (dönüş) ve ibtidâ harfi."),
  mazi("تَحَدَّثَ", "tahaddatha", "«spoke»", "«söz etti»", tags=["form-v-verbs"], hidden=None),
  fail("الْقُرْآنُ", "quran", "«the Qurʾān»", "«Kur'ân»"),
  tok("كَثِيرًا", "kathir", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ (أَيْ: حَدِيثًا كَثِيرًا).", "«much» — standing for the absolute object (a long speaking).", "«çokça» — mef'ûl-i mutlaktan nâib (çok söz)."),
  prep("عَنْ", "an", "«of»", "«-den»"),
  majrur("آلَاءِ", "ala-bounties", "«the bounties»", "«nimetleri»", tags=[ID, JT], ar="مَجْرُورٌ بِعَنْ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»", punct="،"),
  mazi("وَحَكَى", "haka", "«and told»", "«ve anlattı»", tags=[AT, "naqis-verbs"], wa=True, hidden="هُوَ"),
  fi(), masdar_jarr("بَسْطٍ", "bast", "«length»", "«uzun uzun»"),
  tok("أَحْيَانًا", "ahyanan", "noun", [MF, JT], "ظَرْفُ زَمَانٍ مَنْصُوبٌ.", "«at times» — a ẓarf of time.", "«kimi zaman» — zaman zarfı."),
  tok("وَفِي", "fi", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and in»", "«ve … -de»", segments=wa_("فِي", "fi", "prep")),
  masdar_jarr("اخْتِصَارٍ", "ikhtisar", "«brevity»", "«kısaca»"),
  tok("أَحْيَانًا", "ahyanan", "noun", [MF, JT], "ظَرْفُ زَمَانٍ مَنْصُوبٌ.", "«at times» — a ẓarf of time.", "«kimi zaman» — zaman zarfı."),
  prep("عَنْ", "an", "«of»", "«-den»"),
  majrur("نِعَمٍ", "nima", "«favours»", "«nimetler»", tags=[JT]),
  naat("كَثِيرَةٍ", "kathir", "«many»", "«nice»", punct="،"),
  mazi("أَنْعَمَ", "anama", "«He bestowed»", "«lütfetti»", tags=["jumla-sifa", "form-iv-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِنِعَمٍ"),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«them»", "«onları»"),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  majrur("كَثِيرٍ", "kathir", "«many»", "«pek çoğuna»"),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْأَنْبِيَاءِ", "nabi", "«the prophets»", "«peygamberler»", tags=[JT], punct="،"),
])
sen("s4", "among them Dāwūd and Sulaymān, among them Ayyūb and Yūnus, and Zakariyyā and Yaḥyā.",
        "Onlardan Dâvûd ile Süleyman, onlardan Eyyûb ile Yûnus, Zekeriyyâ ile Yahyâ.", [
  prep_pron("مِنْهُمْ", "min", "هُمْ", "pron-3mp", "«among them» — a fronted khabar.", "«onlardan» — öne alınmış haber.", tags=[MK], extra_ar=" — خَبَرٌ مُقَدَّمٌ"),
  tok("دَاوُدُ", "dawud", "propn", [MK, MM], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Dāwūd» — the delayed mubtadaʾ; a diptote name.", "«Dâvûd» — sonraya bırakılmış mübtedâ; gayr-i munsarıf."),
  wa_name_raf("وَسُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»", punct="،"),
  prep_pron("وَمِنْهُمْ", "min", "هُمْ", "pron-3mp", "«and among them»", "«ve onlardan»", tags=[AT, MK], extra_ar=" — خَبَرٌ مُقَدَّمٌ"),
  tok("أَيُّوبُ", "ayyub", "propn", [MK, MM], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ayyūb» — the delayed mubtadaʾ; a diptote.", "«Eyyûb» — mübtedâ; gayr-i munsarıf."),
  wa_name_raf("وَيُونُسُ", "yunus", "«Yūnus»", "«Yûnus»", punct="،"),
  wa_name_raf("وَزَكَرِيَّا", "zakariyya", "«Zakariyyā»", "«Zekeriyyâ»", sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ"),
  wa_name_raf("وَيَحْيَى", "yahya", "«Yaḥyā»", "«Yahyâ»", sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ", punct="."),
])
sen("s5", "As for Dāwūd and Sulaymān, God established them both in the land, widened kingship for them, extended knowledge to them, and taught them much of what people did not know;",
        "Dâvûd ile Süleyman'a gelince: Allah onlara yeryüzünde iktidar verdi, mülkü onlar için genişletti, ilmi onlar için uzattı ve onlara insanların bilmediği pek çok şeyi öğretti;", [
  tok("فَأَمَّا", "amma", "part", ["amma-tafsiliyya"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for» — ammā, the particle of detailing with its answer-fāʾ.", "«… -e gelince» — emmâ, tafsîl edatı; cevabı fâ ile gelir.", segments=[seg("فَ", "fa", "conj"), seg("أَمَّا", "amma", "part")]),
  tok("دَاوُدُ", "dawud", "propn", [MK, MM], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Dāwūd» — the mubtadaʾ; a diptote.", "«Dâvûd» — mübtedâ; gayr-i munsarıf."),
  wa_name_raf("وَسُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»"),
  tok("فَقَدْ", "qad", "part", ["fa-khabar-mubtada", "qad-harf"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَقَدْ حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهَا خَبَرٌ.", "«then indeed» — the fāʾ of ammā's answer with qad; the clause after is the khabar.", "«işte» — emmâ'nın cevap fâ'sı ile kad; sonraki cümle haberdir.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  mazi("مَكَّنَ", "makkana", "«established»", "«iktidar verdi»", tags=["form-ii-verbs"], hidden=None),
  allah_fail(),
  li_pron("لَهُمَا", "هُمَا", "pron-3d", "«for them both»", "«onlara (ikisine)»"),
  fi(), majrur("الْأَرْضِ", "ard", "«the land»", "«yeryüzünde»", punct="،"),
  mazi("وَوَسَّعَ", "wassaa", "«and widened»", "«ve genişletti»", tags=[AT, "form-ii-verbs"], wa=True, hidden="هُوَ"),
  li_pron("لَهُمَا", "هُمَا", "pron-3d", "«for them»", "«onlar için»"),
  fi(), majrur("الْمُلْكِ", "mulk", "«kingship»", "«mülkü»", punct="،"),
  mazi("وَمَدَّ", "madda", "«and extended»", "«ve uzattı»", tags=[AT, "doubled-verbs"], wa=True, hidden="هُوَ"),
  li_pron("لَهُمَا", "هُمَا", "pron-3d", "«to them»", "«onlar için»"),
  fi(), majrur("الْعِلْمِ", "ilm", "«knowledge»", "«ilmi»", punct="،"),
  tok("وَعَلَّمَهُمَا", "allama", "verb", [AT, MX, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَعَلَّمَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمَا مَفْعُولٌ بِهِ أَوَّلُ.", "«and taught them» — a two-object verb; the dual pronoun is the first object.", "«ve onlara öğretti» — iki mef'ûllü fiil; humâ ilk mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("عَلَّمَ", "allama", "verb"), seg("هُمَا", "pron-3d", "pron")]),
  tok("كَثِيرًا", "kathir", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«much» — the second object.", "«pek çok şeyi» — ikinci mef'ûl."),
  tok("مِمَّا", "ma-mawsula", "pron", [HJ, MW], "مِنْ حَرْفُ جَرٍّ أُدْغِمَتْ فِي مَا الْمَوْصُولَةِ، وَمَا فِي مَحَلِّ جَرٍّ.", "«of what» — min fused into the relative mā.", "«… -diklerinden» — min, ism-i mevsûl mâ ile idgam edilmiş.", segments=[seg("مِ", "min", "prep"), seg("مَّا", "ma-mawsula", "pron")]),
  tok("جَهِلَهُ", "jahila", "verb", [MW, MB], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«did not know» — the ṣila; its object the hāʾ.", "«bilmedi» — sıla; mef'ûl hâ.", segments=[seg("جَهِلَ", "jahila", "verb"), pr3ms()]),
  nas_fail(punct="،"),
])
sen("s6", "He subjected to them the strong and the insolent, and what does not submit among the animals and the inanimate things; so He said:",
        "Güçlüleri ve azgınları, hayvanlardan ve cansızlardan boyun eğmeyenleri onların emrine verdi; şöyle buyurdu:", [
  mazi("سَخَّرَ", "sakhkhara", "«He subjected»", "«emrine verdi»", tags=["form-ii-verbs"], hidden="هُوَ"),
  li_pron("لَهُمَا", "هُمَا", "pron-3d", "«to them»", "«onlara»"),
  tok("الْأَقْوِيَاءَ", "qawi", "noun", [MB, JT, MM], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ تَكْسِيرٍ عَلَى أَفْعِلَاءَ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«the strong» — the object; a diptote broken plural.", "«güçlüleri» — mef'ûl; gayr-i munsarıf cem'-i teksîr."),
  atf("وَالْعُتَاةَ", "ati", "«the insolent»", "«azgınları»", "nasb", tags=[JT], punct="،"),
  tok("وَمَا", "ma-mawsula", "pron", [AT, MW], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ فِي مَحَلِّ نَصْبٍ.", "«and what» — the relative, joined to the object.", "«ve … -meyenleri» — ism-i mevsûl, mef'ûle ma'tûf.", segments=wa_("مَا", "ma-mawsula", "pron")),
  la_nafiya(),
  neg_mudari("يَنْقَادُ", "inqada", "«submits»", "«boyun eğer»", tags=[MW, "hollow-verbs", "form-vii-verbs"], hidden="هُوَ", extra=" — صِلَةٌ"),
  prep("مِنَ", "min", "«among»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  tok("الْحَيَوَانَاتِ", "hayawan", "noun", [HJ, JM], "مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the animals» — a sound feminine plural.", "«hayvanlar» — cem'-i müennes sâlim."),
  tok("وَالْجَمَادَاتِ", "jamad", "noun", [AT, JM], "الْوَاوُ عَاطِفَةٌ، وَالْجَمَادَاتِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ.", "«and the inanimate things»", "«ve cansızlar»", punct="،", segments=wa_("الْجَمَادَاتِ", "jamad", "noun")),
  qala(full="فَقَالَ", wa=False, hidden="هُوَ", tags=["fa-khabar-mubtada"]),
])
sen("s7", "«And We gave Dāwūd and Sulaymān knowledge, and they both said: Praise be to God, who favoured us over many of His believing servants» (27:15).",
        "«Andolsun Dâvûd'a ve Süleyman'a ilim verdik; ikisi de dediler ki: Bizi mümin kullarının birçoğundan üstün kılan Allah'a hamdolsun» (27:15).", [
  *quran([
  tok("وَلَقَدْ", "qad", "part", ["qad-harf", "tawkid"], "الْوَاوُ لِلْقَسَمِ (أَوْ لِلِاسْتِئْنَافِ)، وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and surely» — the lām of the oath's answer with qad.", "«andolsun» — kasem cevabının lâmı ve kad.", segments=[seg("وَ", "wa", "conj"), seg("لَ", "lam-qasam", "part"), seg("قَدْ", "qad", "part")]),
  tok("آتَيْنَا", "aataa", "verb", [MX, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ — يَنْصِبُ مَفْعُولَيْنِ.", "«We gave» — built on sukūn before nā; nā the doer; two objects follow.", "«verdik» — nâ'ya bitiştiği için sükûn üzere mebnî; nâ fâil; iki mef'ûl alır.", segments=[seg("آتَيْ", "aataa", "verb"), seg("نَا", "pron-1p", "pron")]),
  maful_name("دَاوُدَ", "dawud", "«Dāwūd»", "«Dâvûd'a»"),
  wa_name_nasb("وَسُلَيْمَانَ", "sulayman", "«Sulaymān»", "«Süleyman'a»"),
  tok("عِلْمًا", "ilm", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«knowledge» — the second object.", "«ilim» — ikinci mef'ûl."),
  tok("وَقَالَا", "qala", "verb", [AT, "al-muthanna", "hollow-verbs", MB], "الْوَاوُ عَاطِفَةٌ، وَقَالَ فِعْلٌ مَاضٍ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ.", "«and they both said» — the dual alif is the doer.", "«ve ikisi dediler» — tesniye elifi fâil.", segments=wa_("قَالَا", "qala", "verb")),
  tok("الْحَمْدُ", "hamd", "noun", [MK, "masdar"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«praise» — the mubtadaʾ.", "«hamd» — mübtedâ."),
  tok("لِلّٰهِ", "allah", "propn", [MK, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«to God» — the jarr phrase is the khabar.", "«Allah'a» — câr-mecrûr haber.", segments=[seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ لِلَفْظِ الْجَلَالَةِ.", "«who» — a naʿt of the Name.", "«… olan» — lafza-i celâlin sıfatı."),
  tok("فَضَّلَنَا", "faddala", "verb", [MW, MB, "form-ii-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَنَا مَفْعُولٌ بِهِ — صِلَةٌ.", "«favoured us» — the ṣila; nā the object.", "«bizi üstün kıldı» — sıla; nâ mef'ûl.", segments=[seg("فَضَّلَ", "faddala", "verb"), seg("نَا", "pron-1p", "pron")]),
  prep("عَلَى", "ala", "«over»", "«-den»"),
  majrur("كَثِيرٍ", "kathir", "«many»", "«birçoğu»"),
  prep("مِنْ", "min", "«of»", "«-den»"),
  noun_pron("عِبَادِهِ", "abd", "عِبَادِ", "هِ", "pron-3ms", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His servants»", "«kullarının»", tags=[HJ, ID, JT]),
  tok("الْمُؤْمِنِينَ", "mumin", "noun", [NA, JS, "ism-fail"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«believing» — the naʿt, jarr by the yāʾ.", "«mümin» — sıfat, yâ ile mecrûr.", punct="."),
  ]),
])
sen("s8", "«And Sulaymān inherited Dāwūd, and said: O people, we have been taught the speech of birds and given of everything — this is indeed the manifest favour» (27:16).",
        "«Süleyman Dâvûd'a mirasçı oldu ve dedi ki: Ey insanlar, bize kuşların dili öğretildi ve bize her şeyden verildi; şüphesiz bu apaçık lütuftur» (27:16).", [
  *quran([
  mazi("وَوَرِثَ", "waritha", "«and inherited»", "«ve mirasçı oldu»", tags=[AT, "mithal-verbs"], wa=True, hidden=None),
  fail_name("سُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»"),
  maful_name("دَاوُدَ", "dawud", "«Dāwūd»", "«Dâvûd'a»"),
  qala(full="وَقَالَ", wa=True, hidden="هُوَ", punct=None),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("أَيُّهَا", "ayyuha", "noun", ["vocative-munada", "huruf-tanbih"], "مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ، وَهَا لِلتَّنْبِيهِ.", "«O you» — the munādā ayy, built on ḍamma; hā of alerting.", "«ey» — münâdâ eyyü, damme üzere mebnî; hâ tenbih içindir."),
  tok("النَّاسُ", "nas", "noun", ["vocative-munada", NA], "نَعْتٌ لِأَيٍّ (أَوْ عَطْفُ بَيَانٍ) مَرْفُوعٌ بِالضَّمَّةِ.", "«people» — the naʿt of ayy, in rafʿ.", "«insanlar» — eyyü'nün sıfatı, merfû."),
  tok("عُلِّمْنَا", "allama", "verb", [NF, MX, "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَا نَائِبُ فَاعِلٍ (الْمَفْعُولُ الْأَوَّلُ).", "«we have been taught» — a passive; nā the deputy doer (the first object).", "«bize öğretildi» — meçhul; nâ nâib-i fâil (ilk mef'ûl).", segments=[seg("عُلِّمْ", "allama", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("مَنْطِقَ", "mantiq", "noun", [MB, MX, ID], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ، مُضَافٌ.", "«the speech» — the second object, annexed.", "«dilini» — ikinci mef'ûl, muzâf."),
  mudaf_ilayh("الطَّيْرِ", "tayr", "«of birds»", "«kuşların»"),
  tok("وَأُوتِينَا", "aataa", "verb", [AT, NF, "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأُوتِيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَا نَائِبُ فَاعِلٍ.", "«and we were given» — a passive; nā the deputy doer.", "«ve bize verildi» — meçhul; nâ nâib-i fâil.", segments=[seg("وَ", "wa", "conj"), seg("أُوتِي", "aataa", "verb"), seg("نَا", "pron-1p", "pron")]),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("كُلِّ", "kull", "«every»", "«her»", tags=[ID], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("شَيْءٍ", "shay", "«thing»", "«şey»"),
  inna(),
  tok("هٰذَا", "hadha", "pron", [IW, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«this» — the ism of inna.", "«bu» — inne'nin ismi."),
  tok("لَهُوَ", "huwa", "pron", [IW, "damir-fasl"], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَهُوَ ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ (أَوْ مُبْتَدَأٌ).", "«it is» — the sliding lām of ibtidāʾ and the pronoun of separation.", "«… -dır» — kaydırılmış ibtidâ lâmı ve fasıl zamiri.", segments=[seg("لَ", "lam-qasam", "part"), seg("هُوَ", "huwa", "pron")]),
  khabar_inna("الْفَضْلُ", "fadl", "«the favour»", "«lütuf»"),
  naat("الْمُبِينُ", "mubin", "«manifest»", "«apaçık»", case="raf", punct="."),
  ]),
])

# ---------------------------------------------------------------- §2 نِعْمَةُ اللهِ عَلَى دَاوُدَ
sen("s9", "As for Dāwūd, God subjected to him the mountains and the birds, echoing him in supplication and glorification; He taught him the craft of coats of mail and softened iron for him:",
        "Dâvûd'a gelince: Allah dağları ve kuşları, duada ve tesbihte ona eşlik eder hâlde onun emrine verdi; ona zırh yapma sanatını öğretti ve demiri onun için yumuşattı:", [
  tok("فَأَمَّا", "amma", "part", ["amma-tafsiliyya"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for» — ammā.", "«… -e gelince» — emmâ.", segments=[seg("فَ", "fa", "conj"), seg("أَمَّا", "amma", "part")]),
  tok("دَاوُدُ", "dawud", "propn", [MK, MM], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Dāwūd» — the mubtadaʾ; a diptote.", "«Dâvûd» — mübtedâ; gayr-i munsarıf."),
  tok("فَقَدْ", "qad", "part", ["fa-khabar-mubtada", "qad-harf"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«then indeed» — the answer-fāʾ with qad.", "«işte» — cevap fâ'sı ile kad.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  mazi("سَخَّرَ", "sakhkhara", "«subjected»", "«emrine verdi»", tags=["form-ii-verbs"], hidden=None),
  allah_fail(),
  li_pron("لَهُ", "هُ", "pron-3ms", "«to him»", "«ona»"),
  maful_("الْجِبَالَ", "jabal", "«the mountains»", "«dağları»", tags=[JT]),
  atf("وَالطَّيْرَ", "tayr", "«the birds»", "«kuşları»", "nasb"),
  mudari("تُجَاوِبُ", "jawaba", "«echoing»", "«eşlik ederek»", tags=[HL, "form-iii-verbs"], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ"),
  prep_pron("مَعَهُ", "maa", "هُ", "pron-3ms", "«with him»", "«onunla»", extra_ar=" — مَعَ ظَرْفٌ مُضَافٌ"),
  fi(), majrur("الدُّعَاءِ", "dua", "«supplication»", "«dua»", tags=["masdar"]),
  atf("وَالتَّسْبِيحِ", "tasbih", "«glorification»", "«tesbih»", "jarr", tags=["masdar"], punct="،"),
  tok("وَعَلَّمَهُ", "allama", "verb", [AT, MX, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَعَلَّمَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«and taught him» — the hāʾ is the first object.", "«ve ona öğretti» — hâ ilk mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("عَلَّمَ", "allama", "verb"), pr3ms()]),
  tok("صَنْعَةَ", "sana-craft", "noun", [MB, MX, ID], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ، مُضَافٌ.", "«the craft» — the second object, annexed.", "«sanatını» — ikinci mef'ûl, muzâf."),
  mudaf_ilayh("الدُّرُوعِ", "dir", "«of coats of mail»", "«zırhların»", tags=[JT], punct="،"),
  mazi("وَأَلَانَ", "alana", "«and softened»", "«ve yumuşattı»", tags=[AT, "hollow-verbs", "form-iv-verbs"], wa=True, hidden="هُوَ"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«for him»", "«onun için»"),
  maful_("الْحَدِيدَ", "hadid", "«iron»", "«demiri»", punct=":"),
])
sen("s10", "«And We gave Dāwūd a favour from Us: O mountains, echo with him — and the birds; and We softened iron for him» (34:10).",
        "«Andolsun Dâvûd'a katımızdan bir lütuf verdik: Ey dağlar, onunla birlikte tesbih edin — kuşlar da; ve demiri onun için yumuşattık» (34:10).", [
  *quran([
  tok("وَلَقَدْ", "qad", "part", ["qad-harf", "tawkid"], "الْوَاوُ لِلْقَسَمِ (أَوْ لِلِاسْتِئْنَافِ)، وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and surely» — the oath's lām with qad.", "«andolsun» — kasem lâmı ve kad.", segments=[seg("وَ", "wa", "conj"), seg("لَ", "lam-qasam", "part"), seg("قَدْ", "qad", "part")]),
  tok("آتَيْنَا", "aataa", "verb", [MX, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ.", "«We gave» — nā the doer.", "«verdik» — nâ fâil.", segments=[seg("آتَيْ", "aataa", "verb"), seg("نَا", "pron-1p", "pron")]),
  maful_name("دَاوُدَ", "dawud", "«Dāwūd»", "«Dâvûd'a»"),
  tok("مِنَّا", "min", "prep", [HJ], "مِنْ حَرْفُ جَرٍّ، وَنَا فِي مَحَلِّ جَرٍّ.", "«from Us»", "«katımızdan»", segments=[seg("مِنْ", "min", "prep"), seg("نَا", "pron-1p", "pron")]),
  tok("فَضْلًا", "fadl", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a favour» — the second object.", "«bir lütuf» — ikinci mef'ûl."),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("جِبَالُ", "jabal", "noun", ["vocative-munada", JT], "مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«mountains» — the munādā, built on ḍamma.", "«dağlar» — münâdâ, damme üzere mebnî."),
  tok("أَوِّبِي", "awwaba", "verb", [AM, "form-ii-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ فَاعِلٌ.", "«echo» — an imperative built on the dropped nūn; the yāʾ is the doer.", "«tesbih edin» — nûnun düşmesi üzere mebnî emir; muhâtaba yâ'sı fâil."),
  prep_pron("مَعَهُ", "maa", "هُ", "pron-3ms", "«with him»", "«onunla»", extra_ar=" — مَعَ ظَرْفٌ مُضَافٌ"),
  tok("وَالطَّيْرَ", "tayr", "noun", [AT], "الْوَاوُ عَاطِفَةٌ، وَالطَّيْرَ مَعْطُوفٌ عَلَى مَحَلِّ جِبَالُ مَنْصُوبٌ (وَقِيلَ: مَفْعُولٌ مَعَهُ).", "«and the birds» — joined to the place of the munādā, in naṣb.", "«ve kuşlar» — münâdânın mahalline ma'tûf, mansub.", segments=wa_("الطَّيْرَ", "tayr", "noun")),
  tok("وَأَلَنَّا", "alana", "verb", [AT, "hollow-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَلَنَّ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ.", "«and We softened» — the hollow IV before nā; nā the doer.", "«ve yumuşattık» — ecvef if'âl; nâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("أَلَنْ", "alana", "verb"), seg("نَا", "pron-1p", "pron")]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«for him»", "«onun için»"),
  maful_("الْحَدِيدَ", "hadid", "«iron»", "«demiri»", punct="."),
  ]),
])
sen("s11", "«— that: make full coats of mail and measure the links well; and do righteous work: I see what you do» (34:11).",
        "«— Şöyle ki: Geniş zırhlar yap ve örgüsünü ölçülü tut; ve salih amel işleyin: Ben yaptıklarınızı görmekteyim» (34:11).", [
  *quran([
  tok("أَنِ", "an-masdariyya", "part", ["an-masdariyya"], "أَنْ تَفْسِيرِيَّةٌ (وَقِيلَ: مَصْدَرِيَّةٌ)، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«that» — the explaining an; kasra for the two sukūns.", "«şöyle ki» — tefsîriyye en; iki sâkin için kesre."),
  tok("اعْمَلْ", "amila", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«make» — an imperative on sukūn; the doer concealed.", "«yap» — sükûn üzere mebnî emir; fâil gizli."),
  tok("سَابِغَاتٍ", "sabigha", "noun", [MB, JM, "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ (صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: دُرُوعًا).", "«full [coats]» — the object, naṣb by KASRA: a sound feminine plural.", "«geniş [zırhlar]» — mef'ûl; cem'-i müennes sâlim KESRE ile mansub."),
  tok("وَقَدِّرْ", "qaddara", "verb", [AT, AM, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَقَدِّرْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and measure» — an imperative; the doer concealed.", "«ve ölçülü tut» — emir; fâil gizli.", segments=wa_("قَدِّرْ", "qaddara", "verb")),
  fi(), majrur("السَّرْدِ", "sard", "«the links»", "«örgüsünde»", tags=["masdar"]),
  tok("وَاعْمَلُوا", "amila", "verb", [AT, AM], "الْوَاوُ عَاطِفَةٌ، وَاعْمَلُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«and do» — an imperative on the dropped nūn; the wāw is the doer.", "«ve yapın» — nûnun düşmesi üzere mebnî emir; vâv fâil.", segments=wa_("اعْمَلُوا", "amila", "verb")),
  tok("صَالِحًا", "salih", "noun", [MB, "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ (صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: عَمَلًا صَالِحًا).", "«righteous [work]» — the object; the noun it qualifies is left out.", "«salih [amel]» — mef'ûl; mevsûfu hazfedilmiş."),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.", "«indeed I» — inna with the yāʾ as its ism.", "«şüphesiz ben» — inne; yâ ismi.", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("بِمَا", "bi", "prep", [HJ, MW], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِبَصِيرٌ.", "«of what» — bi with the relative; attached to the khabar.", "«… -larınızı» — bâ ve ism-i mevsûl mâ; habere bağlı.", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  khamsa("تَعْمَلُونَ", "amila", "«you do»", "«yapıyorsunuz»", tags=[MW], extra_ar=" — صِلَةٌ"),
  khabar_inna("بَصِيرٌ", "basir", "«all-seeing»", "«görücü»", tags=["sighat-mubalagha"], punct="."),
  ]),
])
sen("s12", "And He says: «And We subjected the mountains, with Dāwūd, to glorify — and the birds; and We were the doers» (21:79).",
        "Ve buyurur: «Dağları Dâvûd'la birlikte tesbih eder hâlde emrine verdik, kuşları da; biz yapanlardık» (21:79).", [
  tok("وَيَقُولُ", "qala", "verb", ["mudari-marfu", "hollow-verbs", MB], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَقُولُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (اللهُ).", "«and He says» — a muḍāriʿ in rafʿ; the doer concealed (God).", "«ve buyurur» — merfû muzari; fâil gizli (Allah).", punct=":", segments=wa_("يَقُولُ", "qala", "verb")),
  *quran([
  tok("وَسَخَّرْنَا", "sakhkhara", "verb", [MB, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَسَخَّرْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ.", "«and We subjected» — nā the doer.", "«ve emrine verdik» — nâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("سَخَّرْ", "sakhkhara", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("مَعَ", "maa", "noun", [MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with» — a ẓarf, annexed.", "«ile» — zarf, muzâf."),
  tok("دَاوُدَ", "dawud", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Dāwūd» — the muḍāf ilayh, jarr by FATḤA (a diptote).", "«Dâvûd» — muzâfun ileyh; gayr-i munsarıf, fetha ile mecrûr."),
  maful_("الْجِبَالَ", "jabal", "«the mountains»", "«dağları»", tags=[JT]),
  tok("يُسَبِّحْنَ", "sabbaha", "verb", [HL, "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ فَاعِلٌ — وَالْجُمْلَةُ حَالٌ.", "«glorifying» — a muḍāriʿ built on sukūn before the women's nūn; the nūn is the doer; the clause is the ḥāl.", "«tesbih eder hâlde» — nisve nûnuna bitişen muzari, sükûn üzere mebnî; nûn fâil; cümle hâl."),
  atf("وَالطَّيْرَ", "tayr", "«the birds»", "«kuşları»", "nasb"),
  tok("وَكُنَّا", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَنَا اسْمُهُ.", "«and We were» — kāna with nā as its ism.", "«ve biz … idik» — kâne; nâ ismi.", segments=[seg("وَ", "wa", "conj"), seg("كُنْ", "kana", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("فَاعِلِينَ", "fail-doer", "noun", [KN, JS, "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«doers» — kāna's khabar, naṣb by the yāʾ.", "«yapanlar» — kâne'nin haberi, yâ ile mansub.", punct="."),
  ]),
])
sen("s13", "«And We taught him the making of armour for you, to protect you from your violence — so are you thankful?» (21:80).",
        "«Ve ona, sizi savaşınızın şiddetinden korusun diye sizin için zırh yapmayı öğrettik; şükrediyor musunuz?» (21:80).", [
  *quran([
  tok("وَعَلَّمْنَاهُ", "allama", "verb", [AT, MX, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَعَلَّمْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«and We taught him» — nā the doer; the hāʾ the first object.", "«ve ona öğrettik» — nâ fâil; hâ ilk mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("عَلَّمْ", "allama", "verb"), seg("نَا", "pron-1p", "pron"), pr3ms()]),
  tok("صَنْعَةَ", "sana-craft", "noun", [MB, MX, ID], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ، مُضَافٌ.", "«the making» — the second object, annexed.", "«yapmayı» — ikinci mef'ûl, muzâf."),
  mudaf_ilayh("لَبُوسٍ", "labus", "«of armour»", "«zırh»"),
  li_pron("لَكُمْ", "كُمْ", "pron-2mp", "«for you» — a sifa of the armour.", "«sizin için» — zırhın sıfatı.", tags=[NA], extra=" — نَعْتٌ لِلَبُوسٍ"),
  tok("لِتُحْصِنَكُمْ", "ahsana-fortify", "verb", [TA, MB, "form-iv-verbs"], "اللَّامُ لِلتَّعْلِيلِ، وَتُحْصِنَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَكُمْ مَفْعُولٌ بِهِ.", "«to protect you» — the lām of cause; naṣb by a hidden an; kum the object.", "«sizi korusun diye» — ta'lîl lâmı; gizli en ile mansub; küm mef'ûl.", segments=[seg("لِ", "li", "prep"), seg("تُحْصِنَ", "ahsana-fortify", "verb"), seg("كُمْ", "pron-2mp", "pron")]),
  prep("مِنْ", "min", "«from»", "«-den»"),
  noun_pron("بَأْسِكُمْ", "bas", "بَأْسِ", "كُمْ", "pron-2mp", "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«your violence»", "«savaşınızın şiddetinden»", tags=[HJ, ID]),
  tok("فَهَلْ", "hal-istifham", "part", ["al-istifham"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَهَلْ حَرْفُ اسْتِفْهَامٍ.", "«so are …?» — the question particle hal.", "«… mu?» — soru edatı hel.", segments=[seg("فَ", "fa", "conj"), seg("هَلْ", "hal-istifham", "part")]),
  tok("أَنْتُمْ", "antum", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«you» — the mubtadaʾ.", "«siz» — mübtedâ."),
  tok("شَاكِرُونَ", "shakir", "noun", [MK, JS, "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«thankful» — the khabar, rafʿ by the wāw.", "«şükredenler» — haber, vâv ile merfû.", punct="."),
  ]),
])

# ---------------------------------------------------------------- the glossary (a key is a GLOBAL claim — checked with lemma_clash.py)
CAND = {
 "dawud": G("dawud", "دَاوُد", None, "propn", "Dāwūd (David) — the prophet-king; a diptote name", "Dâvûd — peygamber-hükümdar; gayr-i munsarıf", 1),
 "sulayman": G("sulayman", "سُلَيْمَان", None, "propn", "Sulaymān (Solomon) — Dāwūd's son and heir; a diptote name", "Süleyman — Dâvûd'un oğlu ve vârisi; gayr-i munsarıf", 1),
 "ayyub": G("ayyub", "أَيُّوب", None, "propn", "Ayyūb (Job)", "Eyyûb", 1),
 "yunus": G("yunus", "يُونُس", None, "propn", "Yūnus (Jonah)", "Yûnus", 1),
 "zakariyya": G("zakariyya", "زَكَرِيَّا", None, "propn", "Zakariyyā (Zechariah)", "Zekeriyyâ", 1),
 "yahya": G("yahya", "يَحْيَى", None, "propn", "Yaḥyā (John)", "Yahyâ", 1),
 "iqtasara": G("iqtasara", "اِقْتَصَرَ", "ق ص ر", "verb", "to confine oneself to, to be limited to (Form VIII, with ʿalā)", "-le yetinmek, sınırlı kalmak (iftiâl, alâ ile)", 3),
 "dhikr": G("dhikr", "ذِكْر", "ذ ك ر", "noun", "mention, recounting; remembrance", "zikir, anma; hatırlama", 2),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "a day", "gün", 1, plural="أَيَّام"),
 "laqiya": G("laqiya", "لَقِيَ", "ل ق ي", "verb", "to meet, to encounter", "karşılaşmak, görmek", 2),
 "rasul": G("rasul", "رَسُول", "ر س ل", "noun", "a messenger", "resûl, elçi", 1, plural="رُسُل"),
 "takdhib": G("takdhib", "تَكْذِيب", "ك ذ ب", "noun", "denial, calling a liar (maṣdar of Form II)", "yalanlama (tef'îl masdarı)", 2),
 "sukhriya": G("sukhriya", "سُخْرِيَة", "س خ ر", "noun", "mockery, derision", "alay, eğlenme", 3),
 "ihana": G("ihana", "إِهَانَة", "ه و ن", "noun", "insult, humiliation (maṣdar of Form IV)", "hakaret, aşağılama (if'âl masdarı)", 3),
 "mutarada": G("mutarada", "مُطَارَدَة", "ط ر د", "noun", "pursuit, hounding (maṣdar of Form III)", "kovalama, takip (müfâale masdarı)", 3),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "a nation, a community", "ümmet, topluluk", 1, plural="أُمَم"),
 "baatha": G("baatha", "بَعَثَ", "ب ع ث", "verb", "to send, to raise up", "göndermek, diriltmek", 2),
 "uquba": G("uquba", "عُقُوبَة", "ع ق ب", "noun", "punishment, penalty", "ceza, ukûbet", 2),
 "adhab": G("adhab", "عَذَاب", "ع ذ ب", "noun", "torment, punishment", "azap", 1),
 "halak": G("halak", "هَلَاك", "ه ل ك", "noun", "ruin, perishing", "helâk, yok olma", 2),
 "damar": G("damar", "دَمَار", "د م ر", "noun", "destruction, devastation", "yıkım, dumûr", 3),
 "istihza": G("istihza", "اِسْتِهْزَاء", "ه ز أ", "noun", "mockery, ridicule (maṣdar of Form X)", "alay etme, istihzâ (istif'âl masdarı)", 3),
 "kayd": G("kayd", "كَيْد", "ك ي د", "noun", "plotting, a scheme", "tuzak, hile", 2),
 "hamm": G("hamm", "هَمّ", "ه م م", "noun", "resolve, intent; worry", "kalkışma, niyet; kaygı", 3),
 "qatl": G("qatl", "قَتْل", "ق ت ل", "noun", "killing", "öldürme", 1),
 "marra": G("marra", "مَرَّ", "م ر ر", "verb", "to pass (by)", "geçmek, uğramak", 1),
 "qasas": G("qasas", "قَصَص", "ق ص ص", "noun", "stories, the telling of stories", "kıssalar, kıssa anlatımı", 2),
 "bal": G("bal", "بَلْ", None, "part", "rather, nay — the particle of turning (iḍrāb)", "bilakis, aksine — idrâb edatı", 2),
 "tahaddatha": G("tahaddatha", "تَحَدَّثَ", "ح د ث", "verb", "to speak, to talk (Form V, with ʿan)", "söz etmek, konuşmak (tefa''ul, an ile)", 2),
 "ala-bounties": G("ala-bounties", "آلَاء", "أ ل و", "noun", "bounties, blessings (plural of إِلًى / أَلًى; Qurʾānic)", "nimetler, lütuflar (Kur'ânî çoğul)", 3),
 "haka": G("haka", "حَكَى", "ح ك ي", "verb", "to tell, to relate", "anlatmak, nakletmek", 2),
 "bast": G("bast", "بَسْط", "ب س ط", "noun", "spreading out; telling at length", "yayma; uzun uzun anlatma", 3),
 "ahyanan": G("ahyanan", "أَحْيَانًا", "ح ي ن", "noun", "at times, sometimes (an adverb)", "bazen, kimi zaman (zarf)", 2),
 "ikhtisar": G("ikhtisar", "اِخْتِصَار", "خ ص ر", "noun", "brevity, abridgement (maṣdar of Form VIII)", "kısaltma, özetleme (iftiâl masdarı)", 3),
 "nima": G("nima", "نِعْمَة", "ن ع م", "noun", "a favour, a blessing", "nimet", 1, plural="نِعَم"),
 "anama": G("anama", "أَنْعَمَ", "ن ع م", "verb", "to bestow a favour (Form IV, with bi … ʿalā)", "nimet vermek, lütfetmek (if'âl)", 2),
 "amma": G("amma", "أَمَّا", None, "part", "as for … — the particle of detailing; its answer takes the fāʾ", "… -e gelince — tafsîl edatı; cevabı fâ alır", 2),
 "makkana": G("makkana", "مَكَّنَ", "م ك ن", "verb", "to establish, to give power (Form II, with li … fī)", "iktidar vermek, yerleştirmek (tef'îl)", 3),
 "ard": G("ard", "أَرْض", "أ ر ض", "noun", "the earth, the land", "yer, toprak", 1),
 "wassaa": G("wassaa", "وَسَّعَ", "و س ع", "verb", "to widen, to make ample (Form II)", "genişletmek (tef'îl)", 3),
 "mulk": G("mulk", "مُلْك", "م ل ك", "noun", "kingship, dominion", "mülk, hükümdarlık", 2),
 "madda": G("madda", "مَدَّ", "م د د", "verb", "to extend, to stretch out", "uzatmak, yaymak", 2),
 "ilm": G("ilm", "عِلْم", "ع ل م", "noun", "knowledge", "ilim", 1),
 "allama": G("allama", "عَلَّمَ", "ع ل م", "verb", "to teach (Form II; two objects)", "öğretmek (tef'îl; iki mef'ûl)", 1),
 "jahila": G("jahila", "جَهِلَ", "ج ه ل", "verb", "not to know, to be ignorant of", "bilmemek, câhil olmak", 2),
 "sakhkhara": G("sakhkhara", "سَخَّرَ", "س خ ر", "verb", "to subject, to make serviceable (Form II, with li)", "emrine vermek, boyun eğdirmek (tef'îl)", 3),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong, mighty", "güçlü, kuvvetli", 1, plural="أَقْوِيَاء"),
 "ati": G("ati", "عَاتٍ", "ع ت و", "noun", "insolent, rebellious (an active participle)", "azgın, âsi (ism-i fâil)", 3, plural="عُتَاة"),
 "inqada": G("inqada", "اِنْقَادَ", "ق و د", "verb", "to submit, to be led (Form VII, hollow)", "boyun eğmek, güdülmek (infiâl, ecvef)", 3),
 "hayawan": G("hayawan", "حَيَوَان", "ح ي ي", "noun", "an animal", "hayvan", 1, plural="حَيَوَانَات"),
 "jamad": G("jamad", "جَمَاد", "ج م د", "noun", "an inanimate thing", "cansız varlık, cemâd", 3, plural="جَمَادَات"),
 "aataa": G("aataa", "آتَى", "أ ت ي", "verb", "to give (Form IV; two objects)", "vermek (if'âl; iki mef'ûl)", 2),
 "hamd": G("hamd", "حَمْد", "ح م د", "noun", "praise", "hamd, övgü", 1),
 "faddala": G("faddala", "فَضَّلَ", "ف ض ل", "verb", "to favour, to prefer (Form II, with ʿalā)", "üstün kılmak, tercih etmek (tef'îl)", 2),
 "abd": G("abd", "عَبْد", "ع ب د", "noun", "a servant, a slave", "kul, köle", 1, plural="عِبَاد"),
 "waritha": G("waritha", "وَرِثَ", "و ر ث", "verb", "to inherit (an assimilated verb: يَرِثُ)", "mirasçı olmak (misâl fiil: yerisü)", 2),
 "ayyuha": G("ayyuha", "أَيُّ", None, "noun", "O you — the vocative ayy with the hā of alerting", "ey — nidâ eyyü ile tenbih hâ'sı", 2),
 "mantiq": G("mantiq", "مَنْطِق", "ن ط ق", "noun", "speech, language (of birds)", "konuşma, dil (kuş dili)", 3),
 "tayr": G("tayr", "طَيْر", "ط ي ر", "noun", "birds (a collective)", "kuşlar (cins ismi)", 1),
 "fadl": G("fadl", "فَضْل", "ف ض ل", "noun", "favour, grace", "lütuf, fazilet", 1),
 "mubin": G("mubin", "مُبِين", "ب ي ن", "noun", "manifest, clear", "apaçık", 1),
 "jabal": G("jabal", "جَبَل", "ج ب ل", "noun", "a mountain", "dağ", 1, plural="جِبَال"),
 "jawaba": G("jawaba", "جَاوَبَ", "ج و ب", "verb", "to answer back, to echo (Form III)", "karşılık vermek, eşlik etmek (müfâale)", 3),
 "dua": G("dua", "دُعَاء", "د ع و", "noun", "supplication, prayer", "dua", 1),
 "tasbih": G("tasbih", "تَسْبِيح", "س ب ح", "noun", "glorification (maṣdar of Form II)", "tesbih (tef'îl masdarı)", 2),
 "sana-craft": G("sana-craft", "صَنْعَة", "ص ن ع", "noun", "a craft, the making of something", "sanat, yapım", 2),
 "dir": G("dir", "دِرْع", "د ر ع", "noun", "a coat of mail, armour", "zırh", 3, plural="دُرُوع"),
 "alana": G("alana", "أَلَانَ", "ل ي ن", "verb", "to soften (Form IV, hollow)", "yumuşatmak (if'âl, ecvef)", 3),
 "hadid": G("hadid", "حَدِيد", "ح د د", "noun", "iron", "demir", 1),
 "awwaba": G("awwaba", "أَوَّبَ", "أ و ب", "verb", "to echo back the praise, to glorify in turn (Form II; Qurʾānic)", "tesbihi tekrarlamak, eşlik etmek (tef'îl; Kur'ânî)", 3),
 "sabigha": G("sabigha", "سَابِغَة", "س ب غ", "noun", "full, ample (of a coat of mail); a full coat of mail", "geniş, tam (zırh); geniş zırh", 3, plural="سَابِغَات"),
 "qaddara": G("qaddara", "قَدَّرَ", "ق د ر", "verb", "to measure, to proportion (Form II)", "ölçmek, ölçülü yapmak (tef'îl)", 2),
 "sard": G("sard", "سَرْد", "س ر د", "noun", "the links of mail, the weave of armour", "zırh örgüsü, halkaların dizilişi", 3),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to do, to work", "yapmak, çalışmak", 1),
 "salih": G("salih", "صَالِح", "ص ل ح", "noun", "righteous, sound", "salih, iyi", 1),
 "basir": G("basir", "بَصِير", "ب ص ر", "noun", "all-seeing (an intensive)", "görücü, gören (mübalağa)", 2),
 "sabbaha": G("sabbaha", "سَبَّحَ", "س ب ح", "verb", "to glorify (Form II)", "tesbih etmek (tef'îl)", 1),
 "fail-doer": G("fail-doer", "فَاعِل", "ف ع ل", "noun", "a doer, one who does", "yapan, fâil", 2),
 "labus": G("labus", "لَبُوس", "ل ب س", "noun", "armour, a garment of war (Qurʾānic)", "zırh, savaş giysisi (Kur'ânî)", 3),
 "ahsana-fortify": G("ahsana-fortify", "أَحْصَنَ", "ح ص ن", "verb", "to fortify, to protect (Form IV)", "korumak, sağlamlaştırmak (if'âl)", 3),
 "bas": G("bas", "بَأْس", "ب أ س", "noun", "violence, might; war", "şiddet, savaş gücü", 2),
 "hal-istifham": G("hal-istifham", "هَلْ", None, "part", "the question particle hal", "soru edatı hel", 1),
 "antum": G("antum", "أَنْتُمْ", None, "pron", "you (masc. plural)", "siz", 1),
 "shakir": G("shakir", "شَاكِر", "ش ك ر", "noun", "thankful (an active participle)", "şükreden (ism-i fâil)", 1, plural="شَاكِرُونَ"),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "many, much", "çok", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (feminine)", "bu (müennes)", 1),
 "allati": G("allati", "الَّتِي", None, "pron", "which, who (feminine relative)", "ki o (müennes ism-i mevsûl)", 1),
 "lam-qasam": G("lam-qasam", "لَ (لَامُ الْقَسَمِ)", None, "part", "the lām of the oath's answer / of ibtidāʾ", "kasem cevabının lâmı / ibtidâ lâmı", 2),
 "pron-3d": G("pron-3d", "هُمَا", None, "pron", "they two / them two (attached and detached)", "o ikisi / onlara (ikisine)", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us / our (attached)", "biz / bizi / bizim (bitişik)", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "my / me (the attached yāʾ)", "benim / beni (bitişik yâ)", 1),
 "lam-jazima": G("lam-jazima", "لَمْ", None, "part", "lam — negation and jazm of the muḍāriʿ, turning its sense to the past", "lem — muzariyi cezm eden, anlamını mâzîye çeviren nefiy edatı", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this (masculine)", "bu (müzekker)", 1),
 "pron-2mp": G("pron-2mp", "كُمْ", None, "pron", "you / your (masc. plural, attached)", "siz / sizin (bitişik)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tahaddatha", _sg.derived(_sg.B5, _sg.W5, "َ", "تَحَدَّث", "تَحَدَّث", "تَحَدَّث", "تَحَدُّث", "مُتَحَدِّث", "مُتَحَدَّث", "تُحُدِّثَ", "يُتَحَدَّثُ", "تَحَدَّثَ يَتَحَدَّثُ: تَكَلَّمَ."))
put_morph(mo, "makkana", _sg.derived(_sg.B2, _sg.W2, "ُ", "مَكَّن", "مَكِّن", "مَكِّن", "تَمْكِين", "مُمَكِّن", "مُمَكَّن", "مُكِّنَ", "يُمَكَّنُ", "مَكَّنَ لَهُ فِي الْأَرْضِ: جَعَلَ لَهُ فِيهَا سُلْطَانًا."))
put_morph(mo, "wassaa", _sg.derived(_sg.B2, _sg.W2, "ُ", "وَسَّع", "وَسِّع", "وَسِّع", "تَوْسِيع", "مُوَسِّع", "مُوَسَّع", "وُسِّعَ", "يُوَسَّعُ", "وَسَّعَ لَهُ فِي الْمُلْكِ: بَسَطَهُ لَهُ."))
put_morph(mo, "sakhkhara", _sg.derived(_sg.B2, _sg.W2, "ُ", "سَخَّر", "سَخِّر", "سَخِّر", "تَسْخِير", "مُسَخِّر", "مُسَخَّر", "سُخِّرَ", "يُسَخَّرُ", "سَخَّرَ لَهُ الشَّيْءَ: ذَلَّلَهُ لَهُ وَجَعَلَهُ طَوْعَ أَمْرِهِ."))
put_morph(mo, "faddala", _sg.derived(_sg.B2, _sg.W2, "ُ", "فَضَّل", "فَضِّل", "فَضِّل", "تَفْضِيل", "مُفَضِّل", "مُفَضَّل", "فُضِّلَ", "يُفَضَّلُ", "فَضَّلَهُ عَلَى غَيْرِهِ: جَعَلَهُ أَفْضَلَ مِنْهُ."))
put_morph(mo, "jahila", _sg.sound1("samia", "جَهِل", "جْهَل", "اِجْهَل", "جَهْل", "جَاهِل", "مَجْهُول", "جُهِلَ", "يُجْهَلُ", "جَهِلَ الشَّيْءَ: لَمْ يَعْلَمْهُ."))
put_morph(mo, "jawaba", _sg.derived(_sg.B3, _sg.W3, "ُ", "جَاوَب", "جَاوِب", "جَاوِب", "مُجَاوَبَة", "مُجَاوِب", "مُجَاوَب", "جُووِبَ", "يُجَاوَبُ", "جَاوَبَهُ: رَدَّ عَلَيْهِ وَرَجَّعَ مَعَهُ الصَّوْتَ."))
put_morph(mo, "awwaba", _sg.derived(_sg.B2, _sg.W2, "ُ", "أَوَّب", "أَوِّب", "أَوِّب", "تَأْوِيب", "مُؤَوِّب", "مُؤَوَّب", "أُوِّبَ", "يُؤَوَّبُ", "أَوَّبَ مَعَهُ: رَجَّعَ التَّسْبِيحَ مَعَهُ."))
put_morph(mo, "ahsana-fortify", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَحْصَن", "حْصِن", "أَحْصِن", "إِحْصَان", "مُحْصِن", "مُحْصَن", "أُحْصِنَ", "يُحْصَنُ", "أَحْصَنَهُ: حَفِظَهُ وَمَنَعَهُ."))
put_morph(mo, "alana", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَلَان", "أَلَن", "لِين", "لِن", "أَلِين", "أَلِن", "إِلَانَة", "مُلِين", "مُلَان", "أُلِينَ", "يُلَانُ", "أَلَانَ الشَّيْءَ: جَعَلَهُ لَيِّنًا."))
put_morph(mo, "inqada", _sg.derived_hollow(_sg.B7, _sg.W7, "َ", "اِنْقَاد", "اِنْقَد", "نْقَاد", "نْقَد", "اِنْقَاد", "اِنْقَد", "اِنْقِيَاد", "مُنْقَاد", None, None, None, "اِنْقَادَ لَهُ: خَضَعَ وَأَطَاعَ."))
put_morph(mo, "waritha", _sg.entry("مِنْ بَابِ حَسِبَ يَحْسِبُ — مِثَالٌ وَاوِيٌّ (تَسْقُطُ وَاوُهُ فِي الْمُضَارِعِ)", "فَعِلَ يَفْعِلُ", "إِرْث / وِرَاثَة", "وَارِث", _sg.mazi14("وَرِث"), _sg.mudari14("َ", "رِث"), _sg.amr_attach("رِث"), "يَرِثَ", "يَرِثْ", "تَرِثْ", "مَوْرُوث", "وُرِثَ", "يُورَثُ", "وَرِثَهُ: صَارَ إِلَيْهِ مَالُهُ أَوْ مُلْكُهُ بَعْدَهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch6 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 6 (print pp. 11–13; the story of Dāwūd and Sulaymān opens): the Qurʾān tells of God's bounties too (s1–s4), the two kings' gifts with 27:15–16 (s5–s8), the favour on Dāwūd with 34:10–11 and 21:79–80 (s9–s13)."
ADD_TR = " Altıncı bölüm (baskı s. 11–13; Dâvûd ve Süleyman kıssası açılır): Kur'ân Allah'ın nimetlerini de anlatır (s1–s4), iki hükümdara verilenler ve 27:15–16 (s5–s8), Dâvûd'a lütuf ile 34:10–11 ve 21:79–80 (s9–s13)."
write_out(6, S, TITLE, ADD_EN, ADD_TR, "Dāwūd and Sulaymān §intro–2", GLOSS_ADD, notes=(), related=())
report(6, S, GLOSS_ADD, ())
