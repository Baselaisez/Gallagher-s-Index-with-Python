# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 6: «رُؤْيَا إِبْرَاهِيمَ» — section 14 of «من كسر الأصنام؟» (print pp. 21–23): Ibrāhīm's
return to Mecca, the dream, the aya of al-Ṣāffāt 37:102 as the print sets it (two lines, both marked), Minā, the ram, the Feast of
Sacrifice. Every printed line is one sentence; the vowelling is the print's.
python3 tools/authoring/author_qisas_ch6.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
from talkhis_common import bare
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "رُؤْيَا إِبْرَاهِيمَ", "en": "Ibrāhīm's dream", "tr": "İbrâhim'in rüyası"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

# ---------------------------------------------------------------- local helpers
def ibrahim_fail(punct=None): return fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=punct)
def ibrahim_ism_kana(punct=None):
    return tok("إِبْرَاهِيمُ", "ibrahim", "propn", [K, "mamnu-min-sarf"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ibrāhīm» — kāna's ism, in rafʿ.", "«İbrâhim» — kâne'nin ismi, merfû.", punct=punct)
def ismail_ism_kana(punct=None):
    return tok("إِسْمَاعِيلُ", "ismail", "propn", [K, "mamnu-min-sarf"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ismāʿīl» — kāna's ism, in rafʿ.", "«İsmâil» — kâne'nin ismi, merfû.", punct=punct)
def name_fail(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", ["fail", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the doer; a diptote name.", tr + " — fâil; gayr-i munsarıf özel isim.", punct=punct)
def name_maful(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "propn", ["maful-bihi", "mamnu-min-sarf"] + list(tags), "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the object; a diptote name.", tr + " — mef'ûl-i bih; gayr-i munsarıf özel isim.", punct=punct)
def name_jarr(full, lex, en, tr, prep, punct=None, tags=()):
    return tok(full, lex, "propn", ["huruf-jarr", "mamnu-min-sarf"] + list(tags), f"مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — in jarr by a fatḥa; a diptote name.", tr + " — fetha ile mecrur; gayr-i munsarıf özel isim.", punct=punct)
def name_mudaf_ilayh(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the muḍāf ilayh, jarr by a fatḥa; a diptote.", tr + " — muzâfun ileyh, fetha ile mecrur; gayr-i munsarıf.", punct=punct)
def name_badal(full, lex, en, tr, case, punct=None):
    C = {"raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "rafʿ", "merfû"), "nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "naṣb", "mansub"), "jarr": ("مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ", "jarr (by a fatḥa)", "mecrur (fetha ile)")}[case]
    return tok(full, lex, "propn", ["badal", "mamnu-min-sarf"], f"بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) {C[0]} — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + f" — the badal of the word before, in {C[1]}; a diptote.", tr + f" — öncekinin bedeli, {C[2]}; gayr-i munsarıf.", punct=punct)
def makka_jarr(punct=None, prep="إِلَى"):
    return tok("مَكَّةَ", "makka", "propn", ["huruf-jarr", "mamnu-min-sarf"], f"مَجْرُورٌ بِـ{prep} وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Mecca» — in jarr by a fatḥa; a feminine name, a diptote.", "«Mekke» — fetha ile mecrur; müennes özel isim, gayr-i munsarıf.", punct=punct)
def fi(punct=None): return tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def ala(): return tok("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on, upon».", "«üzerine».")
def ila(): return tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e».")
def manam_jarr(punct=None):
    return tok("الْمَنَامِ", "manam", "noun", ["huruf-jarr"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the dream (sleep)» — in jarr.", "«rüyada (uykuda)» — mecrur.", punct=punct)
def an():
    return tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ.", "«to» — the subjunctive maṣdar particle; the clause it makes is the object.", "«-mek» — masdariyye nasb harfi; te'vîl edilen masdar mef'ûldür.")
def an_verb(full, lex, en, tr, tags=(), punct=None, muq=False):
    return tok(full, lex, "verb", ["an-masdariyya"] + list(tags), "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ " + ("الْفَتْحَةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ" if muq else "الْفَتْحَةُ") + "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", en + " — in naṣb after an; the doer «he» is concealed.", tr + " — en ile mansub; fâil gizli «o».", punct=punct)
def ma_mawsula(punct=None):
    return tok("مَا", "ma-mawsula", "pron", ["maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what» — the relative, built; in the place of naṣb as the object.", "«-diği şeyi» — ism-i mevsûl, mebnî; mahallen mansub mef'ûl.", punct=punct)
def fa_mazi(full, lex, en, tr, hidden="هُوَ", tags=(), punct=None):
    """فَأَرَادَ، فَوَضَعَ، فَأَرْسَلَ، فَأَمَرَ — the fāʾ of sequence on a māḍī."""
    return tok(full, lex, "verb", list(tags), "الْفَاءُ عَاطِفَةٌ، وَ" + full[1:].replace("ْ", "ْ") + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}" if hidden else "") + ".",
               "«and (then)» + " + en + (" — a māḍī; the doer is concealed." if hidden else " — a māḍī built on fatḥa."), "«ve (sonra)» + " + tr + (" — mâzî; fâil gizli zamirdir." if hidden else " — fetha üzere mebnî mâzî."), punct=punct,
               segments=[seg("فَ", "fa", "conj"), seg(full[1:], lex, "verb")])
def ya_abati():
    return [tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi."),
            tok("أَبَتِ", "ab", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالتَّاءُ عِوَضٌ عَنْ يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَالْكَسْرَةُ دَلِيلُ الْيَاءِ.", "«O my father» — a vocative annexed to the speaker's yāʾ; the tāʾ stands in for the dropped yāʾ, the kasra is its trace.", "«ey babacığım» — mütekellim yâsına muzâf münâdâ; tâ hazfedilen yânın ivazı, kesre yânın izidir.")]

# ================================================================ §14 رؤيا إبراهيم (pp. 21–23)
sen("s1", "And Ibrāhīm returned to Mecca after a while.", "Ve İbrâhim bir müddet sonra Mekke'ye döndü.", [
  mazi("وَعَادَ", "ada-return", "«returned»", "«döndü»", hidden=None, wa=True, tags=["hollow-verbs"]), ibrahim_fail(), ila(), makka_jarr(),
  tok("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«after» — an adverb of time in naṣb; a muḍāf.", "«sonra» — mansub zaman zarfı; muzâf."),
  tok("مُدَّةٍ", "mudda", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«a while» — the muḍāf ilayh, in jarr.", "«bir müddet» — muzâfun ileyh, mecrur.", punct=".")])
sen("s2", "And he met Ismāʿīl and met Hājar, and Ibrāhīm rejoiced in his son Ismāʿīl.", "Ve İsmâil'le karşılaştı, Hâcer'le karşılaştı; İbrâhim oğlu İsmâil'e sevindi.", [
  mazi("وَلَقِيَ", "laqiya", "«met»", "«karşılaştı»", hidden="هُوَ", wa=True, tags=["naqis-verbs"]), name_maful("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil'le»"),
  mazi("وَلَقِيَ", "laqiya", "«and met»", "«ve karşılaştı»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "naqis-verbs"]), name_maful("هَاجَرَ", "hajar-name", "«Hājar»", "«Hâcer'le»", punct="،"),
  mazi("وَفَرِحَ", "fariha", "«and rejoiced»", "«ve sevindi»", hidden=None, wa=True, tags=["atf-nasaq"]), ibrahim_fail(),
  tok("بِوَلَدِهِ", "walad", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَوَلَدِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in his son» — the bāʾ of jarr; annexed to «his».", "«oğluna» — cer bâsı; «onun»a muzâf.", segments=[seg("بِ", "bi", "prep"), seg("وَلَدِ", "walad", "noun"), seg("هِ", "pron-3ms", "pron")]),
  name_badal("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil»", "jarr", punct=".")])
sen("s3", "And Ismāʿīl was a small boy who ran and played and went out with his father.", "Ve İsmâil küçük bir çocuktu; koşar, oynar ve babasıyla dışarı çıkardı.", [
  kana(), ismail_ism_kana(),
  tok("وَلَدًا", "walad", "noun", [K], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a boy» — kāna's khabar, in naṣb.", "«bir çocuk» — kâne'nin haberi, mansub."),
  tok("صَغِيرًا", "saghir", "noun", ["naat-sifa"], "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«small» — the naʿt, in naṣb.", "«küçük» — sıfat, mansub.", punct="،"),
  tok("يَجْرِي", "jara", "verb", ["mudari-marfu", "naqis-verbs", "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَانٍ لِوَلَدًا.", "«(who) runs» — a muḍāriʿ, the ḍamma estimated on the yāʾ; the clause is a second naʿt of «a boy».", "«koşan» — muzâri, damme yâ üzerinde takdîrî; cümle «çocuk»un ikinci sıfatıdır."),
  tok("وَيَلْعَبُ", "laiba", "verb", ["atf-nasaq", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَلْعَبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and plays» — joined to «runs».", "«ve oynar» — «koşar»a atıf.", segments=[seg("وَ", "wa", "conj"), seg("يَلْعَبُ", "laiba", "verb")]),
  tok("وَيَخْرُجُ", "kharaja", "verb", ["atf-nasaq", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَخْرُجُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and goes out» — joined.", "«ve çıkar» — atıf.", segments=[seg("وَ", "wa", "conj"), seg("يَخْرُجُ", "kharaja", "verb")]),
  tok("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«with» — an adverb in naṣb; a muḍāf.", "«ile» — mansub zarf; muzâf."),
  tok("وَالِدِهِ", "walid-father", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father» — the muḍāf ilayh; itself annexed to «his».", "«babası» — muzâfun ileyh; kendisi de «onun»a muzâf.", punct=".", segments=[seg("وَالِدِ", "walid-father", "noun"), seg("هِ", "pron-3ms", "pron")])])
sen("s4", "And Ibrāhīm loved Ismāʿīl very much.", "Ve İbrâhim İsmâil'i çok severdi.", [
  kana(), ibrahim_ism_kana(),
  tok("يُحِبُّ", "ahabba", "verb", [K, "mudari-marfu", "form-iv-verbs", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«loved» — a muḍāriʿ; the clause is kāna's khabar.", "«severdi» — muzâri; cümle kâne'nin haberidir."),
  name_maful("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil'i»"),
  tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«very much» — standing in for the absolute object.", "«çok» — mef'ûl-i mutlak nâibi.", punct=".")])
sen("s5", "And one night Ibrāhīm saw in a dream that he was slaughtering Ismāʿīl.", "Ve bir gece İbrâhim rüyada İsmâil'i kurban ettiğini gördü.", [
  tok("وَذَاتَ", "dhat", "noun", ["maful-fih", "idafa-definiteness"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَذَاتَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«one (night)» — an adverb of time in naṣb; annexed.", "«bir (gece)» — mansub zaman zarfı; muzâf.", segments=[seg("وَ", "wa", "conj"), seg("ذَاتَ", "dhat", "noun")]),
  tok("لَيْلَةٍ", "layla", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«night» — the muḍāf ilayh.", "«gece» — muzâfun ileyh."),
  tok("رَأَى", "raa", "verb", ["naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«saw» — a māḍī built on a fatḥa estimated on the alif.", "«gördü» — elif üzerinde takdîrî fetha üzere mebnî mâzî."), ibrahim_fail(), fi(), manam_jarr(),
  tok("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha", "maful-bihi"], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِرَأَى.", "«that he» — anna with its ism «he» attached; the clause is the object of «saw».", "«-diğini» — enne ve ismi «o»; te'vîl edilen masdar «gördü»nün mef'ûlüdür.", segments=[seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("يَذْبَحُ", "dhabaha", "verb", ["mudari-marfu", "inna-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.", "«slaughters» — a muḍāriʿ; the clause is anna's khabar.", "«kurban ediyor» — muzâri; cümle enne'nin haberidir."),
  name_maful("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil'i»", punct=".")])
sen("s6", "And Ibrāhīm was a truthful prophet, and his dream was a true dream.", "Ve İbrâhim sâdık bir peygamberdi; rüyası da sâdık bir rüyaydı.", [
  kana(), ibrahim_ism_kana(),
  tok("نَبِيًّا", "nabi", "noun", [K], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a prophet» — kāna's khabar.", "«bir peygamber» — kâne'nin haberi."),
  tok("صَادِقًا", "sadiq", "noun", ["naat-sifa"], "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«truthful» — the naʿt.", "«sâdık» — sıfat.", punct="،"),
  tok("وَكَانَ", "kana", "verb", [K, "hollow-verbs", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«and … was» — kāna again, joined.", "«ve … idi» — atıfla kâne.", segments=[seg("وَ", "wa", "conj"), seg("كَانَ", "kana", "verb")]),
  tok("مَنَامُهُ", "manam", "noun", [K, "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his dream» — kāna's ism; annexed.", "«rüyası» — kâne'nin ismi; muzâf.", segments=[seg("مَنَامُ", "manam", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("مَنَامًا", "manam", "noun", [K], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a dream» — kāna's khabar.", "«bir rüya» — kâne'nin haberi."),
  tok("صَادِقًا", "sadiq", "noun", ["naat-sifa"], "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«true» — the naʿt.", "«sâdık» — sıfat.", punct=".")])
sen("s7", "And Ibrāhīm was the intimate friend of Allah, so he wanted to do what Allah had commanded him in the dream.", "Ve İbrâhim Allah'ın halîli idi; Allah'ın rüyada ona emrettiğini yapmak istedi.", [
  kana(), ibrahim_ism_kana(),
  tok("خَلِيلَ", "khalil", "noun", [K, "idafa-definiteness"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the intimate friend of» — kāna's khabar, a muḍāf.", "«halîli» — kâne'nin haberi, muzâf."),
  tok("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«Allah» — the muḍāf ilayh.", "«Allah'ın» — muzâfun ileyh.", punct="،"),
  fa_mazi("فَأَرَادَ", "arada", "«wanted»", "«istedi»", tags=["form-iv-verbs", "hollow-verbs"]), an(), an_verb("يَفْعَلَ", "faala", "«do»", "«yapsın»"),
  ma_mawsula(),
  tok("أَمَرَهُ", "amara-v", "verb", ["maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«commanded him» — the clause is the relative's ṣila; «him» is its object.", "«ona emretti» — cümle mevsûlün sılasıdır; «ona» mef'ûl.", segments=[seg("أَمَرَ", "amara-v", "verb"), seg("هُ", "pron-3ms", "pron")]),
  allah_fail(), fi(), manam_jarr(punct=".")])
sen("s8", "And Ibrāhīm said to Ismāʿīl:", "Ve İbrâhim İsmâil'e dedi:", [
  qala("وَقَالَ", punct=None, wa=True), ibrahim_fail(),
  tok("لِإِسْمَاعِيلَ", "ismail", "propn", ["huruf-jarr", "mamnu-min-sarf"], "اللَّامُ حَرْفُ جَرٍّ، وَإِسْمَاعِيلَ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«to Ismāʿīl» — the lām of jarr; the name takes a fatḥa, a diptote.", "«İsmâil'e» — cer lâmı; isim fetha alır, gayr-i munsarıf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("إِسْمَاعِيلَ", "ismail", "propn")])])
sen("s9", "«My son, I see in a dream that I am slaughtering you — so look, what do you think?» (al-Ṣāffāt 37:102)", "«Oğlum, rüyada seni kurban ettiğimi görüyorum; bak, ne dersin?» (Sâffât 37:102)", quran([
  tok("إِنِّي", "inna", "part", ["inna-wa-akhawatuha", "ya-al-mutakallim"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed I» — inna with the speaker's yāʾ as its ism (the wiqāya nūn contracted).", "«şüphesiz ben» — inne ve ismi olan mütekellim yâsı (vikaye nûnu idgamlı).", segments=[seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أَرَى", "raa", "verb", ["mudari-marfu", "inna-wa-akhawatuha", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنَا — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«I see» — the ḍamma estimated on the alif; the clause is inna's khabar.", "«görüyorum» — damme elif üzerinde takdîrî; cümle inne'nin haberidir."),
  fi(), manam_jarr(),
  tok("أَنِّي", "anna", "part", ["inna-wa-akhawatuha", "ya-al-mutakallim", "maful-bihi"], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِأَرَى.", "«that I» — anna with the speaker's yāʾ; the clause is the object of «I see».", "«-diğimi» — enne ve ismi mütekellim yâsı; masdar «görüyorum»un mef'ûlü.", segments=[seg("أَنَّ", "anna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أَذْبَحُكَ", "dhabaha", "verb", ["mudari-marfu", "inna-wa-akhawatuha", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنَا، وَالْكَافُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.", "«I slaughter you» — the doer «I» concealed, «you» the object; the clause is anna's khabar.", "«seni kurban ediyorum» — fâil gizli «ben», «seni» mef'ûl; cümle enne'nin haberi.", segments=[seg("أَذْبَحُ", "dhabaha", "verb"), seg("كَ", "pron-2ms", "pron")]),
  tok("فَانْظُرْ", "nazara", "verb", ["imperative-amr"], "الْفَاءُ لِلتَّفْرِيعِ، وَانْظُرْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«so look» — an imperative built on sukūn; «you» concealed.", "«öyleyse bak» — sükûn üzere mebnî emir; «sen» gizli.", segments=[seg("فَ", "fa", "conj"), seg("انْظُرْ", "nazara", "verb")]),
  tok("مَاذَا", "madha", "pron", ["al-istifham", "maful-bihi"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ لِتَرَى.", "«what» — the interrogative, fronted as the object of «you see».", "«ne» — soru ismi, «görürsün»ün öne alınmış mef'ûlü."),
  tok("تَرَى", "raa", "verb", ["mudari-marfu", "al-istifham", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ — وَالْجُمْلَةُ الِاسْتِفْهَامِيَّةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِانْظُرْ.", "«you think (see)» — the ḍamma estimated on the alif; «you» concealed; the question-clause is the object of «look».", "«dersin (görürsün)» — damme elif üzerinde takdîrî; «sen» gizli; soru cümlesi «bak»ın mef'ûlüdür.")]))
sen("s10", "«He said: O my father, do what you are commanded; you will find me, if Allah wills, among the patient.» (37:102)", "«Dedi: Ey babacığım, sana emredileni yap; inşallah beni sabredenlerden bulacaksın.» (37:102)", quran([
  qala("قَالَ", punct=None, hidden="هُوَ")] + ya_abati() + [
  tok("افْعَلْ", "faala", "verb", ["imperative-amr"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«do» — an imperative built on sukūn.", "«yap» — sükûn üzere mebnî emir."),
  ma_mawsula(),
  tok("تُؤْمَرُ", "amara-v", "verb", ["naib-al-fail", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ وُجُوبًا: أَنْتَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«you are commanded» — a passive muḍāriʿ; «you» is the deputy doer; the clause is the ṣila.", "«sana emrediliyor» — meçhul muzâri; «sen» nâib-i fâil; cümle sıladır."),
  tok("سَتَجِدُنِي", "wajada", "verb", ["mudari-marfu", "ya-al-mutakallim", "maful-bihi", "mithal-verbs"], "السِّينُ لِلِاسْتِقْبَالِ، وَتَجِدُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ.", "«you will find me» — the future sīn; «you» concealed; the wiqāya nūn and «me», the first object.", "«beni bulacaksın» — istikbâl sîni; «sen» gizli; vikaye nûnu ve ilk mef'ûl «beni».", segments=[seg("سَ", "sa", "part"), seg("تَجِدُ", "wajada", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("إِنْ", "in-shart", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if» — the conditional particle, a jāzim.", "«eğer» — cezm eden şart harfi."),
  tok("شَاءَ", "shaa", "verb", ["in-shartiyya", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«wills» — the shart verb (a māḍī in the place of jazm); the jawāb is omitted, shown by what precedes.", "«dilerse» — şart fiili (mâzî, mahallen meczûm); cevap hazfedilmiş, öncesi gösterir."),
  allah_fail(),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«among» — the jarr letter, voweled for the meeting of two sukūns.", "«-den» — cer harfi, iki sâkin karşılaştığı için harekelenmiş."),
  tok("الصَّابِرِينَ", "sabir", "noun", ["huruf-jarr", "jam-mudhakkar-salim"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ لِتَجِدُ.", "«the patient» — in jarr by the yāʾ, a sound masculine plural; the phrase is the second object of «find».", "«sabredenler» — yâ ile mecrur, cem-i müzekker sâlim; câr-mecrûr «bul»un ikinci mef'ûlüdür.", punct=".")]))
sen("s11", "And Ibrāhīm took Ismāʿīl with him and took a knife.", "Ve İbrâhim İsmâil'i yanına aldı ve bir bıçak aldı.", [
  mazi("وَأَخَذَ", "akhadha", "«took»", "«aldı»", hidden=None, wa=True), ibrahim_fail(), name_maful("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil'i»"),
  tok("مَعَهُ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«with him» — an adverb in naṣb, annexed to «him».", "«yanına» — mansub zarf, «onun»a muzâf.", segments=[seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")]),
  mazi("وَأَخَذَ", "akhadha", "«and took»", "«ve aldı»", hidden="هُوَ", wa=True, tags=["atf-nasaq"]),
  maful("سِكِّينًا", "sikkin", "«a knife»", "«bir bıçak»", punct=".")])
sen("s12", "And when Ibrāhīm reached Minā, he wanted to slaughter Ismāʿīl.", "Ve İbrâhim Minâ'ya varınca İsmâil'i kurban etmek istedi.", [
  tok("وَلَمَّا", "lamma", "part", ["maful-fih"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَمَّا حِينِيَّةٌ ظَرْفُ زَمَانٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", "«and when» — the temporal lammā, built, in the place of naṣb.", "«ve … -ınca» — zaman zarfı lemmâ, mebnî, mahallen mansub.", segments=[seg("وَ", "wa", "conj"), seg("لَمَّا", "lamma", "part")]),
  mazi("بَلَغَ", "balagha", "«reached»", "«vardı»", hidden=None), ibrahim_fail(),
  tok("مِنًى", "mina", "propn", ["maful-bihi", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — اسْمٌ مَقْصُورٌ مُنَوَّنٌ.", "«Minā» — the object, the fatḥa estimated on the alif; a maqṣūr name with tanwīn.", "«Minâ» — mef'ûl, fetha elif üzerinde takdîrî; tenvinli maksûr isim.", punct="،"),
  mazi("أَرَادَ", "arada", "«he wanted»", "«istedi»", hidden="هُوَ", tags=["form-iv-verbs", "hollow-verbs"]), an(), an_verb("يَذْبَحَ", "dhabaha", "«slaughter»", "«kurban etsin»"),
  name_maful("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil'i»", punct=".")])
sen("s13", "And Ismāʿīl lay down on the ground, and Ibrāhīm wanted to slaughter, so he put the knife on Ismāʿīl's throat.", "Ve İsmâil yere uzandı; İbrâhim kurban etmek istedi ve bıçağı İsmâil'in boğazına koydu.", [
  mazi("وَاضْطَجَعَ", "idtajaa", "«lay down»", "«uzandı»", hidden=None, wa=True, tags=["form-viii-verbs"]), name_fail("إِسْمَاعِيلُ", "ismail", "«Ismāʿīl»", "«İsmâil»"), ala(),
  tok("الْأَرْضِ", "ard", "noun", ["huruf-jarr"], "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the ground» — in jarr.", "«yere» — mecrur.", punct="،"),
  mazi("وَأَرَادَ", "arada", "«and wanted»", "«ve istedi»", hidden=None, wa=True, tags=["form-iv-verbs", "hollow-verbs"]), ibrahim_fail(), an(), an_verb("يَذْبَحَ", "dhabaha", "«slaughter»", "«kurban etsin»"),
  fa_mazi("فَوَضَعَ", "wadaa", "«put»", "«koydu»", tags=["mithal-verbs"]),
  maful("السِّكِّينَ", "sikkin", "«the knife»", "«bıçağı»"), ala(),
  tok("حُلْقُومِ", "hulqum", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«the throat of» — in jarr; a muḍāf.", "«boğazına» — mecrur; muzâf."),
  name_mudaf_ilayh("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil'in»", punct=".")])
sen("s14", "But Allah loves to see whether His intimate friend does what He commands him.", "Fakat Allah, halîlinin kendisine emrettiğini yapıp yapmadığını görmeyi sever.", [
  tok("وَلٰكِنَّ", "lakinna", "part", ["inna-wa-akhawatuha"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", "«but» — the corrective sister of inna: naṣb on its ism, rafʿ on its khabar.", "«fakat» — istidrâk için inne'nin kardeşi: ismini nasb, haberini ref eder.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part")]),
  tok("اللهَ", "allah", "propn", ["inna-wa-akhawatuha"], "لَفْظُ الْجَلَالَةِ اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the ism of lākinna, in naṣb.", "«Allah» — lâkinne'nin ismi, mansub."),
  tok("يُحِبُّ", "ahabba", "verb", ["inna-wa-akhawatuha", "mudari-marfu", "form-iv-verbs", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ.", "«loves» — a muḍāriʿ; the clause is lākinna's khabar.", "«sever» — muzâri; cümle lâkinne'nin haberidir."),
  an(), an_verb("يَرَى", "raa", "«see»", "«görsün»", tags=["naqis-verbs"], muq=True),
  tok("هَلْ", "hal-istifham", "part", ["al-istifham", "maful-bihi"], "حَرْفُ اسْتِفْهَامٍ — وَالْجُمْلَةُ الِاسْتِفْهَامِيَّةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِيَرَى.", "«whether» — the question particle; the whole question is the object of «see».", "«mı» — istifhâm harfi; soru cümlesi «görsün»ün mef'ûlüdür."),
  tok("يَفْعَلُ", "faala", "verb", ["mudari-marfu", "al-istifham"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«does» — a muḍāriʿ in rafʿ.", "«yapar» — merfû muzâri."),
  tok("خَلِيلُهُ", "khalil", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His intimate friend» — the doer; annexed to «His».", "«halîli» — fâil; «O'nun»a muzâf.", segments=[seg("خَلِيلُ", "khalil", "noun"), seg("هُ", "pron-3ms", "pron")]),
  ma_mawsula(),
  tok("يَأْمُرُهُ", "amara-v", "verb", ["mudari-marfu", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (اللهُ)، وَالْهَاءُ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«He commands him» — the doer «He» concealed; «him» the object; the clause is the ṣila.", "«ona emreder» — fâil gizli «O»; «ona» mef'ûl; cümle sıladır.", punct=".", segments=[seg("يَأْمُرُ", "amara-v", "verb"), seg("هُ", "pron-3ms", "pron")])])
sen("s15", "And whether he loves Allah more, or loves his son more.", "Ve Allah'ı mı daha çok sever, yoksa oğlunu mu daha çok sever.", [
  tok("وَهَلْ", "hal-istifham", "part", ["al-istifham", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَهَلْ حَرْفُ اسْتِفْهَامٍ.", "«and whether» — joined; the question particle.", "«ve … mı» — atıf; istifhâm harfi.", segments=[seg("وَ", "wa", "conj"), seg("هَلْ", "hal-istifham", "part")]),
  tok("يُحِبُّ", "ahabba", "verb", ["mudari-marfu", "al-istifham", "form-iv-verbs", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (الْخَلِيلُ).", "«he loves» — the doer «he» (the friend) concealed.", "«sever» — fâil gizli «o» (halîl)."),
  tok("اللهَ", "allah", "propn", ["maful-bihi"], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the object.", "«Allah'ı» — mef'ûl."),
  tok("أَكْثَرَ", "akthar", "noun", ["maful-mutlaq", "ism-tafdil", "mamnu-min-sarf"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ (أَيْ: حُبًّا أَكْثَرَ) — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more» — standing in for the absolute object (a greater love); an elative, a diptote.", "«daha çok» — mef'ûl-i mutlak nâibi (daha çok bir sevgi); ism-i tafdîl, gayr-i munsarıf."),
  tok("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or» — the joining particle.", "«yoksa» — atıf harfi."),
  tok("يُحِبُّ", "ahabba", "verb", ["atf-nasaq", "mudari-marfu", "form-iv-verbs", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«loves» — joined by «or».", "«sever» — «yoksa» ile atıf."),
  tok("ابْنَهُ", "ibn", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his son» — the object; annexed.", "«oğlunu» — mef'ûl; muzâf.", segments=[seg("ابْنَ", "ibn", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("أَكْثَرَ", "akthar", "noun", ["maful-mutlaq", "ism-tafdil", "mamnu-min-sarf"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more» — for the absolute object; an elative, a diptote.", "«daha çok» — mef'ûl-i mutlak nâibi; ism-i tafdîl.", punct=".")])
sen("s16", "And Ibrāhīm passed the test.", "Ve İbrâhim imtihanı kazandı.", [
  mazi("وَنَجَحَ", "najaha", "«succeeded»", "«kazandı»", hidden=None, wa=True), ibrahim_fail(), fi(),
  tok("الِامْتِحَانِ", "imtihan", "noun", ["huruf-jarr", "form-viii-verbs"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — مَصْدَرُ اِمْتَحَنَ.", "«the test» — in jarr; the maṣdar of Form VIII.", "«imtihanda» — mecrur; VIII. bâbın masdarı.", punct=".")])
sen("s17", "So Allah sent Jibrīl with a ram from Paradise and said: Slaughter this, and do not slaughter Ismāʿīl.", "Bunun üzerine Allah Cebrâil'i cennetten bir koçla gönderdi ve dedi: Bunu kes, İsmâil'i kesme.", [
  fa_mazi("فَأَرْسَلَ", "arsala", "«sent»", "«gönderdi»", hidden=None, tags=["form-iv-verbs"]), allah_fail(),
  name_maful("جِبْرِيلَ", "jibril", "«Jibrīl»", "«Cebrâil'i»"),
  tok("بِكَبْشٍ", "kabsh", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَكَبْشٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«with a ram» — the bāʾ of jarr.", "«bir koçla» — cer bâsı.", segments=[seg("بِ", "bi", "prep"), seg("كَبْشٍ", "kabsh", "noun")]),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  tok("الْجَنَّةِ", "janna", "noun", ["huruf-jarr"], "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«Paradise» — in jarr.", "«cennetten» — mecrur."),
  qala("وَقَالَ", punct=":", wa=True, hidden="هُوَ"),
  tok("اذْبَحْ", "dhabaha", "verb", ["imperative-amr"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«slaughter» — an imperative built on sukūn.", "«kes» — sükûn üzere mebnî emir."),
  ishara("هٰذَا", "hadha", "nasb", "«this»", "«bunu»"),
  tok("وَلَا", "la-nafiya", "part", ["la-nahiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا النَّاهِيَةُ حَرْفُ جَزْمٍ.", "«and do not» — the prohibiting lā: it governs jazm.", "«ve -me» — nehiy lâ'sı: cezm eder.", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("تَذْبَحْ", "dhabaha", "verb", ["la-nahiya", "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«slaughter» — jazm by sukūn after the prohibiting lā.", "«kesme» — nehiy lâ'sıyla sükûn ile meczûm."),
  name_maful("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil'i»", punct=".")])
sen("s18", "And Allah loved Ibrāhīm's deed, so He commanded the Muslims to sacrifice on the Feast of Sacrifice.", "Ve Allah İbrâhim'in amelini sevdi; Müslümanlara Kurban Bayramı'nda kurban kesmeyi emretti.", [
  mazi("وَأَحَبَّ", "ahabba", "«loved»", "«sevdi»", hidden=None, wa=True, tags=["form-iv-verbs", "doubled-verbs"]), allah_fail(),
  tok("عَمَلَ", "amal-work", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the deed of» — the object; a muḍāf.", "«amelini» — mef'ûl; muzâf."),
  name_mudaf_ilayh("إِبْرَاهِيمَ", "ibrahim", "«Ibrāhīm»", "«İbrâhim'in»", punct="،"),
  fa_mazi("فَأَمَرَ", "amara-v", "«commanded»", "«emretti»"),
  tok("الْمُسْلِمِينَ", "muslim", "noun", ["maful-bihi", "jam-mudhakkar-salim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the Muslims» — the object, naṣb by the yāʾ; a sound masculine plural.", "«Müslümanlara» — mef'ûl, yâ ile mansub; cem-i müzekker sâlim."),
  tok("بِالذَّبْحِ", "dhabh", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالذَّبْحِ مَجْرُورٌ بِالْكَسْرَةِ — مَصْدَرُ ذَبَحَ.", "«to sacrifice» — the bāʾ of jarr on the maṣdar.", "«kurban kesmeyi» — masdar üzerinde cer bâsı.", segments=[seg("بِ", "bi", "prep"), seg("الذَّبْحِ", "dhabh", "noun")]),
  fi(),
  tok("عِيدِ", "id", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ.", "«the feast of» — in jarr; a muḍāf.", "«bayramında» — mecrur; muzâf."),
  tok("الْأَضْحَى", "adha-eid", "propn", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — اسْمٌ مَقْصُورٌ.", "«al-Aḍḥā (the Sacrifice)» — the muḍāf ilayh, the kasra estimated on the alif; a maqṣūr noun.", "«Kurban (el-Adhâ)» — muzâfun ileyh, kesre elif üzerinde takdîrî; maksûr isim.", punct=".")])
sen("s19", "May Allah bless Ibrāhīm, the intimate friend, and grant him peace.", "Allah, halîl İbrâhim'e salât ve selâm eylesin.", [
  tok("صَلَّى", "salla", "verb", ["naqis-verbs", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ — وَهُوَ دُعَاءٌ.", "«may … bless» — a māḍī (a prayer), the fatḥa estimated on the alif.", "«salât eylesin» — mâzî (dua), fetha elif üzerinde takdîrî."), allah_fail(), ala(),
  name_jarr("إِبْرَاهِيمَ", "ibrahim", "«Ibrāhīm»", "«İbrâhim'e»", "عَلَى"),
  tok("الْخَلِيلِ", "khalil", "noun", ["naat-sifa"], "نَعْتٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the intimate friend» — the naʿt, in jarr.", "«halîl» — sıfat, mecrur."),
  mazi("وَسَلَّمَ", "sallama", "«and grant peace»", "«ve selâm eylesin»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "form-ii-verbs"], punct=".")])
sen("s20", "And may Allah bless his son Ismāʿīl and grant him peace.", "Ve Allah, oğlu İsmâil'e salât ve selâm eylesin.", [
  mazi("وَصَلَّى", "salla", "«and may … bless»", "«ve salât eylesin»", hidden=None, wa=True, tags=["naqis-verbs", "form-ii-verbs"]), allah_fail(), ala(),
  tok("ابْنِهِ", "ibn", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his son» — in jarr; annexed.", "«oğlu» — mecrur; muzâf.", segments=[seg("ابْنِ", "ibn", "noun"), seg("هِ", "pron-3ms", "pron")]),
  name_badal("إِسْمَاعِيلَ", "ismail", "«Ismāʿīl»", "«İsmâil'e»", "jarr"),
  mazi("وَسَلَّمَ", "sallama", "«and grant peace»", "«ve selâm eylesin»", hidden="هُوَ", wa=True, tags=["atf-nasaq", "form-ii-verbs"], punct=".")])
for _s in S:
    for _t in _s["tokens"]:
        if _t["surface"]["full"] == "وَصَلَّى": _t["irab"]["ar"] = _t["irab"]["ar"].replace("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ")
        if _t["surface"]["full"] == "وَلَقِيَ" and "atf" not in " ".join(_t["grammar"]): pass

# ---------------------------------------------------------------- glossary
NEW = {
 "laqiya": G("laqiya", "لَقِيَ", "ل ق ي", "verb", "to meet (someone)", "karşılaşmak, bulmak", 1, form="I"),
 "laiba": G("laiba", "لَعِبَ", "ل ع ب", "verb", "to play", "oynamak", 1, form="I"),
 "manam": G("manam", "مَنَام", "ن و م", "noun", "sleep; a dream seen in sleep", "uyku; uykuda görülen rüya", 1),
 "dhabaha": G("dhabaha", "ذَبَحَ", "ذ ب ح", "verb", "to slaughter, to sacrifice", "boğazlamak, kurban etmek", 1, form="I"),
 "sabir": G("sabir", "صَابِر", "ص ب ر", "noun", "patient, steadfast (ism fāʿil of صَبَرَ)", "sabırlı, sabreden (ism-i fâil)", 1, plural="صَابِرُونَ"),
 "sikkin": G("sikkin", "سِكِّين", "س ك ن", "noun", "a knife", "bıçak", 1, plural="سَكَاكِين"),
 "mina": G("mina", "مِنًى", None, "propn", "Minā, the valley by Mecca where the pilgrims sacrifice", "Minâ, Mekke yanındaki vadi; hacıların kurban kestiği yer", 2),
 "idtajaa": G("idtajaa", "اِضْطَجَعَ", "ض ج ع", "verb", "to lie down (on one's side)", "yan üstü uzanmak, yatmak", 2, form="VIII"),
 "hulqum": G("hulqum", "حُلْقُوم", "ح ل ق", "noun", "the throat, the windpipe", "boğaz, gırtlak", 2),
 "imtihan": G("imtihan", "اِمْتِحَان", "م ح ن", "noun", "a test, a trial (maṣdar of اِمْتَحَنَ)", "imtihan, sınav (imtehane'nin masdarı)", 1),
 "jibril": G("jibril", "جِبْرِيل", None, "propn", "Jibrīl (Gabriel), the angel of revelation", "Cebrâil (a.s.), vahiy meleği", 1),
 "kabsh": G("kabsh", "كَبْش", "ك ب ش", "noun", "a ram", "koç", 1, plural="كِبَاش"),
 "dhabh": G("dhabh", "ذَبْح", "ذ ب ح", "noun", "slaughtering, sacrifice (maṣdar of ذَبَحَ)", "kurban kesme, boğazlama (zebeha'nın masdarı)", 1),
 "adha-eid": G("adha-eid", "الْأَضْحَى", "ض ح و", "propn", "al-Aḍḥā — the Feast of Sacrifice (عِيدُ الْأَضْحَى)", "Kurban Bayramı (ıydü'l-adhâ)", 1),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
assert bare(GLOSS_ADD.get("sadiq", TG.get("sadiq", {})).get("lemma", "صَادِق")) == "صادق", "sadiq must be صَادِق here"
# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "laqiya", _sg.entry(_sg.BABS["samia"][0] + " — نَاقِصٌ", _sg.BABS["samia"][1], "لِقَاء", "لَاقٍ",
                                  _sg.mazi_naqis_kasra("لَقِ", "لَقُوا"), _sg.mudari_naqis("َ", "لْق", "a"), _sg.amr_naqis("اِلْق", "a"),
                                  "يَلْقَى", "يَلْقَ", "تَلْقَ", "مَلْقِيّ", "لُقِيَ", "يُلْقَى", note="نَاقِصٌ مِنْ بَابِ سَمِعَ: لَقِيَ يَلْقَى — مُتَعَدٍّ."))
put_morph(mo, "laiba", _sg.sound1("samia", "لَعِب", "لْعَب", "اِلْعَب", "لَعِب", "لَاعِب", note="لَازِمٌ."))
put_morph(mo, "dhabaha", _sg.sound1("fataha", "ذَبَح", "ذْبَح", "اِذْبَح", "ذَبْح", "ذَابِح", "مَذْبُوح", "ذُبِحَ", "يُذْبَحُ"))
put_morph(mo, "idtajaa", _sg.derived("مِنْ بَابِ الِافْتِعَالِ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِضْطَجَع", "ضْطَجِع", "اِضْطَجِع", "اِضْطِجَاع", "مُضْطَجِع",
                                     note="لَازِمٌ — تَاءُ الِافْتِعَالِ قُلِبَتْ طَاءً بَعْدَ الضَّادِ: اِضْتَجَعَ → اِضْطَجَعَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
ADD_EN = (" Chapter 6 (print pp. 21–23, section 14 «رُؤْيَا إِبْرَاهِيمَ»): the return to Mecca and the boy Ismāʿīl (s1–s4), the dream and the aya (s5–s10), Minā, the ram and the Feast of Sacrifice (s11–s20). "
          "s9 and s10 quote al-Ṣāffāt 37:102 as the print sets it, in its two lines (marked); the print's own vowelling is kept (إِنِّي أَرَى، أَنِّي أَذْبَحُكَ). One printed line is one sentence; the page break inside s3 is ignored.")
ADD_TR = (" Altıncı bölüm (basılı s. 21–23, 14. kısım «رُؤْيَا إِبْرَاهِيمَ»): Mekke'ye dönüş ve çocuk İsmâil (s1–s4), rüya ve âyet (s5–s10), Minâ, koç ve Kurban Bayramı (s11–s20). "
          "s9 ve s10 Sâffât 37:102'yi baskıdaki şekliyle iki satır hâlinde aktarır (işaretli); baskının harekesi korunmuştur. Basılı her satır bir cümledir; s3 içindeki sayfa geçişi dikkate alınmamıştır.")
write_out(6, S, TITLE, ADD_EN, ADD_TR, "pp. 21–23", GLOSS_ADD)
report(6, S, GLOSS_ADD, ())
