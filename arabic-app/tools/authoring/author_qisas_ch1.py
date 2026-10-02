# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 1: «بَائِعُ الْأَصْنَامِ» — sections 1–3 of «من كسر الأصنام؟» (print pp. 6–8): Āzar the idol
seller, his son Ibrāhīm, and Ibrāhīm's advice to his father. Every printed line is one sentence; the vowelling is the print's.
Source transcript: the project owner's scan (see qisas_common). python3 tools/authoring/author_qisas_ch1.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
K = "kana-wa-akhawatuha"
TITLE = {"ar": "بَائِعُ الْأَصْنَامِ", "en": "The idol seller", "tr": "Put satıcısı"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

# ---------------------------------------------------------------- token helpers (the reader's few frames, each written once)
def kana(full="وَكَانَ", punct=None, wa=True):
    return tok(full, "kana", "verb", [K, "hollow-verbs"],
               ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
               ("«and» + " if wa else "") + "«was» — the defective verb kāna: it raises its ism and puts its khabar in naṣb.",
               ("«ve» + " if wa else "") + "«idi» — nâkıs fiil kâne: ismini ref, haberini nasb eder.", punct=punct,
               segments=(wa_("كَانَ", "kana", "verb") if wa else None))
def fi(punct=None): return tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def jiddan(punct="."): return tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ لِفِعْلٍ مَحْذُوفٍ — أَيْ: يَجِدُّ جِدًّا، وَهُوَ تَوْكِيدٌ لِلصِّفَةِ.", "«very» — an absolute object of an unspoken verb, stressing the adjective.", "«çok» — hazfedilmiş fiilin mef'ûl-i mutlakı, sıfatı pekiştirir.", punct=punct)
def ism_kana(full, lex, en, tr, tags=(), punct=None, segments=None):
    return tok(full, lex, "noun", [K] + list(tags), "اسْمُ كَانَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.", en + " — the ism of kāna, raised by ḍamma.", tr + " — kâne'nin ismi, damme ile merfû.", punct=punct, segments=segments)
def name_ism_kana(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", [K, "mamnu-min-sarf"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the ism of kāna; a foreign name, a diptote.", tr + " — kâne'nin ismi; yabancı özel isim, gayr-i munsarıf.", punct=punct)
def fail_name(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", ["fail", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the doer; a foreign name, a diptote.", tr + " — fâil; yabancı özel isim, gayr-i munsarıf.", punct=punct)
def khabar_mudari(full, lex, tags, en, tr, punct=None, hidden="هُوَ"):
    return tok(full, lex, "verb", [K, "mudari-marfu"] + list(tags), f"فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden} — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", en + " — a muḍāriʿ in rafʿ with a concealed doer; the clause is kāna's khabar.", tr + " — merfû muzâri, fâili gizli; cümle kâne'nin haberidir.", punct=punct)
def mudari(full, lex, tags, ar_extra, en, tr, punct=None, hidden="هُوَ"):
    return tok(full, lex, "verb", ["mudari-marfu"] + list(tags), f"فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}{ar_extra}", en, tr, punct=punct)
def ishara(full, lex, case, en, tr, punct=None, tags=(), segments=None):
    C = {"nasb": ("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "object"), "jarr": ("فِي مَحَلِّ جَرٍّ", "in the place of jarr"), "raf": ("فِي مَحَلِّ رَفْعٍ", "in the place of rafʿ")}[case]
    return tok(full, lex, "pron", ["asma-al-ishara"] + list(tags), f"اسْمُ إِشَارَةٍ مَبْنِيٌّ {C[0]}.", en + f" — a demonstrative, built; {C[1]}.", tr + " — ism-i işâret, mebnî; mahallen " + {"nasb": "mansub (mef'ûl)", "jarr": "mecrûr", "raf": "merfû"}[case] + ".", punct=punct, segments=segments)
def badal_of_ishara(full, lex, case, en, tr, punct=None, tags=()):
    sign = {"nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "naṣb by fatḥa", "fetha ile mansub"), "jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", "jarr by kasra", "kesre ile mecrûr"), "raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "rafʿ by ḍamma", "damme ile merfû")}[case]
    return tok(full, lex, "noun", ["badal", "asma-al-ishara"] + list(tags), f"بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ (أَوْ عَطْفُ بَيَانٍ) {sign[0]}.", en + f" — the substitute of the demonstrative, {sign[1]}.", tr + f" — ism-i işâretin bedeli, {sign[2]}.", punct=punct)
def asnam(case, punct=None, tags=(), rule="maful"):
    """الْأَصْنَام in its three seats"""
    if rule == "maful": return tok("الْأَصْنَامَ", "sanam", "noun", ["maful-bihi", "jam-taksir"] + list(tags), "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ صَنَمٍ عَلَى أَفْعَالٍ.", "«the idols» — the object; a broken plural of ṣanam.", "«putları» — mef'ûl-i bih; sanem'in cemi mükesseri.", punct=punct)
    return badal_of_ishara({"nasb": "الْأَصْنَامَ", "jarr": "الْأَصْنَامِ", "raf": "الْأَصْنَامُ"}[case], "sanam", case, "«the idols»", "«putlar»", punct=punct, tags=["jam-taksir"] + list(tags))
def li_hadhihi(punct=None):
    return tok("لِهٰذِهِ", "hadhihi", "pron", ["huruf-jarr", "asma-al-ishara"], "اللَّامُ حَرْفُ جَرٍّ، وَهٰذِهِ اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«to these» — the lām of jarr on a built demonstrative.", "«bu …-a» — cer lâmı, mebnî ism-i işâret mahallen mecrûr.", punct=punct, segments=[seg("لِ", "li", "prep"), seg("هٰذِهِ", "hadhihi", "pron")])
def la_nafiya(full="لَا", wa=False):
    return tok(full, "la-nafiya", "part", ["la-nafiya"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", ("«and» + " if wa else "") + "«not» — the negating lā, no government.", ("«ve» + " if wa else "") + "«değil/-mez» — nefiy lâ'sı, amel etmez.", segments=(wa_("لَا", "la-nafiya", "part") if wa else None))
def neg_mudari(full, lex, tags, en, tr, punct=None, hidden="هِيَ"):
    return tok(full, lex, "verb", ["la-nafiya", "mudari-marfu"] + list(tags), f"فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: {hidden} — الْأَصْنَامُ جَمْعُ تَكْسِيرٍ لِغَيْرِ الْعَاقِلِ يُعَامَلُ مُعَامَلَةَ الْمُفْرَدَةِ الْمُؤَنَّثَةِ.", en + " — rafʿ after the negating lā; the idols, a non-human plural, take the feminine singular verb.", tr + " — nefiy lâ'sından sonra merfû; akılsız çoğul, müfred müennes fiil alır.", punct=punct)
def anna():
    return tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha"], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ يَعْرِفُ.", "«that» — a particle like a verb; the clause it heads is what he knows.", "«-dığını» — fiile benzeyen harf; başındaki cümle «bilmek»in mef'ûlüdür.")
def asnam_ism_anna(punct=None):
    return tok("الْأَصْنَامَ", "sanam", "noun", ["inna-wa-akhawatuha", "jam-taksir"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the idols» — the ism of anna, in naṣb.", "«putların» — enne'nin ismi, mansub.", punct=punct)
def abi(full="أَبِي", wa=False, punct=None):
    return tok(full, "ab", "noun", ["vocative-munada", "ya-al-mutakallim", "five-nouns"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ الْيَاءِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَأُفْرِدَ لِلْإِضَافَةِ إِلَى الْيَاءِ.", ("«and» + " if wa else "") + "«my father» — a vocative annexed to the speaker's yāʾ; the naṣb is implied before the yāʾ.", ("«ve» + " if wa else "") + "«babacığım» — mütekellim yâsına muzâf münâdâ; nasb yâ'dan önce takdîrîdir.", punct=punct, segments=(wa_("أَبِي", "ab", "noun") if wa else [seg("أَبِ", "ab", "noun"), pr("ي", "pron-1s")]))
def limadha():
    return tok("لِمَاذَا", "limadha", "pron", ["al-istifham", "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَمَاذَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — أَيْ: لِأَيِّ شَيْءٍ.", "«why» — the lām of jarr on the interrogative mādhā.", "«niçin» — cer lâmı + soru ismi mâzâ.", segments=[seg("لِ", "li", "prep"), seg("مَاذَا", "madha", "pron")])
def ya_nida():
    return tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi.")

def sen(sid, en, tr, toks): S.append({"id": sid, "translation": {"en": en, "tr": tr}, "tokens": toks})

# ================================================================ §1 بائع الأصنام
sen("s1", "Many, many days ago.", "Günler, çok günler önce.", [
  tok("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُتَعَلِّقٌ بِمَحْذُوفٍ — أَيْ: كَانَ هٰذَا قَبْلَ أَيَّامٍ — وَهُوَ مُضَافٌ.", "«before» — an adverb of time, annexed; its verb is unspoken.", "«önce» — zaman zarfı, muzâf; fiili hazfedilmiştir."),
  tok("أَيَّامٍ", "yawm", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ يَوْمٍ.", "«days» — the annexed noun, in jarr; plural of yawm.", "«günler» — muzâfun ileyh, mecrûr; yevm'in çoğulu."),
  tok("كَثِيرَةٍ", "kathir", "noun", ["naat-sifa"], "صِفَةٌ لِأَيَّامٍ مَجْرُورَةٌ بِالْكَسْرَةِ.", "«many» — the adjective of «days», in jarr.", "«çok» — eyyâm'ın sıfatı, mecrûr.", punct="،"),
  tok("كَثِيرَةٍ", "kathir", "noun", ["tawkid", "naat-sifa"], "تَوْكِيدٌ لَفْظِيٌّ لِكَثِيرَةٍ الْأُولَى بِتَكْرِيرِهَا، مَجْرُورٌ مِثْلُهَا.", "«many» — repeated: a verbal emphasis of the first, in the same case.", "«çok» — tekrar: lafzî te'kid, aynı i'râbda."),
  jiddan()])
sen("s2", "There was in a village a very famous man.", "Bir köyde çok meşhur bir adam vardı.", [
  kana("كَانَ", wa=False), fi(),
  tok("قَرْيَةٍ", "qarya", "noun", ["huruf-jarr", K], "مَجْرُورٌ بِفِي، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ كَانَ مُقَدَّمٌ.", "«a village» — in jarr; the phrase is kāna's khabar, fronted.", "«bir köyde» — mecrûr; câr-mecrûr kâne'nin öne alınmış haberi."),
  tok("رَجُلٌ", "rajul", "noun", [K], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a man» — kāna's ism, delayed; rafʿ by ḍamma.", "«bir adam» — kâne'nin sonraya bırakılmış ismi, merfû."),
  tok("مَشْهُورٌ", "mashhur", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ لِرَجُلٍ مَرْفُوعَةٌ بِالضَّمَّةِ — اسْمُ مَفْعُولٍ.", "«famous» — the adjective of «a man», in rafʿ; a passive participle.", "«meşhur» — racül'ün sıfatı, merfû; ism-i mef'ûl."),
  jiddan()])
sen("s3", "And this man's name was Āzar.", "Ve bu adamın adı Âzer idi.", [
  kana(),
  tok("اسْمُ", "ism-name", "noun", [K, "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the name» — kāna's ism, raised; annexed.", "«adı» — kâne'nin ismi, merfû; muzâf."),
  tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«this» — a built demonstrative in the place of jarr, the annexed noun.", "«bu» — mebnî ism-i işâret, mahallen mecrûr muzâfun ileyh."),
  badal_of_ishara("الرَّجُلِ", "rajul", "jarr", "«man»", "«adamın»"),
  tok("آزَرَ", "azar", "propn", [K, "mamnu-min-sarf"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ فَلَا يُنَوَّنُ.", "«Āzar» — kāna's khabar in naṣb; a foreign name, a diptote with no tanwīn.", "«Âzer» — kâne'nin haberi, mansub; yabancı özel isim, tenvinsiz.", punct=".")])
sen("s4", "And Āzar used to sell idols.", "Ve Âzer putlar satardı.", [
  kana(), name_ism_kana("آزَرُ", "azar", "«Āzar»", "«Âzer»"),
  khabar_mudari("يَبِيعُ", "baa", ["hollow-verbs"], "«sells»", "«satar»"),
  asnam("nasb", punct=".")])
sen("s5", "And in this village there was a very big house.", "Ve bu köyde çok büyük bir ev vardı.", [
  kana(), fi(), ishara("هٰذِهِ", "hadhihi", "jarr", "«this»", "«bu»", tags=["huruf-jarr", K]),
  tok("الْقَرْيَةِ", "qarya", "noun", ["badal", "asma-al-ishara", K], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ.", "«village» — the substitute of the demonstrative, in jarr; the phrase is kāna's fronted khabar.", "«köy» — ism-i işâretin bedeli, mecrûr; câr-mecrûr kâne'nin öne alınmış haberi."),
  tok("بَيْتٌ", "bayt", "noun", [K], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a house» — kāna's ism, delayed; rafʿ.", "«bir ev» — kâne'nin sonraya bırakılmış ismi, merfû."),
  tok("كَبِيرٌ", "kabir", "noun", ["naat-sifa", "sifa-mushabbaha"], "صِفَةٌ لِبَيْتٍ مَرْفُوعَةٌ بِالضَّمَّةِ.", "«big» — the adjective of «a house», in rafʿ.", "«büyük» — beyt'in sıfatı, merfû."),
  jiddan()])
sen("s6", "And in this house there were idols — very many idols.", "Ve bu evde putlar vardı; çok, pek çok put.", [
  kana(), fi(), ishara("هٰذَا", "hadha", "jarr", "«this»", "«bu»", tags=["huruf-jarr", K]),
  tok("الْبَيْتِ", "bayt", "noun", ["badal", "asma-al-ishara", K], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ.", "«house» — the substitute of the demonstrative; the phrase is kāna's fronted khabar.", "«ev» — ism-i işâretin bedeli; câr-mecrûr kâne'nin öne alınmış haberi."),
  tok("أَصْنَامٌ", "sanam", "noun", [K, "jam-taksir"], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ صَنَمٍ.", "«idols» — kāna's ism, delayed; a broken plural.", "«putlar» — kâne'nin sonraya bırakılmış ismi; cemi mükesser.", punct="،"),
  tok("أَصْنَامٌ", "sanam", "noun", ["tawkid", "jam-taksir"], "تَوْكِيدٌ لَفْظِيٌّ بِالتَّكْرِيرِ مَرْفُوعٌ مِثْلُ الْأَوَّلِ.", "«idols» — repeated: verbal emphasis, in the same case.", "«putlar» — tekrar: lafzî te'kid, aynı i'râbda."),
  tok("كَثِيرَةٌ", "kathir", "noun", ["naat-sifa"], "صِفَةٌ لِأَصْنَامٍ مَرْفُوعَةٌ بِالضَّمَّةِ — أُفْرِدَتْ وَأُنِّثَتْ لِأَنَّ الْمَوْصُوفَ جَمْعٌ لِغَيْرِ الْعَاقِلِ.", "«many» — the adjective, in rafʿ; feminine singular because the noun is a non-human plural.", "«çok» — sıfat, merfû; mevsûf akılsız çoğul olduğu için müfred müennes."),
  jiddan()])
sen("s7", "And the people used to prostrate to these idols.", "Ve insanlar bu putlara secde ederlerdi.", [
  kana(), ism_kana("النَّاسُ", "nas", "«the people»", "«insanlar»"),
  tok("يَسْجُدُونَ", "sajada", "verb", [K, "mudari-marfu", "afal-khamsa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«prostrate» — one of the five forms, rafʿ by the kept nūn; the wāw is the doer; the clause is kāna's khabar.", "«secde ederler» — ef'âl-i hamseden, nûnun sübûtuyla merfû; vâv fâil; cümle kâne'nin haberi."),
  li_hadhihi(), asnam("jarr", punct=".", rule="badal")])
sen("s8", "And Āzar used to prostrate to these idols.", "Ve Âzer bu putlara secde ederdi.", [
  kana(), name_ism_kana("آزَرُ", "azar", "«Āzar»", "«Âzer»"),
  khabar_mudari("يَسْجُدُ", "sajada", [], "«prostrates»", "«secde eder»"),
  li_hadhihi(), asnam("jarr", punct=".", rule="badal")])
sen("s9", "And Āzar used to worship these idols.", "Ve Âzer bu putlara tapardı.", [
  kana(), name_ism_kana("آزَرُ", "azar", "«Āzar»", "«Âzer»"),
  khabar_mudari("يَعْبُدُ", "abada", [], "«worships»", "«tapar»"),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«these»", "«bu»"), asnam("nasb", punct=".", rule="badal")])

# ================================================================ §2 ولد آزر
sen("s10", "And Āzar had a sensible son — very sensible.", "Ve Âzer'in akıllı bir oğlu vardı; çok akıllı.", [
  kana(), name_ism_kana("آزَرُ", "azar", "«Āzar»", "«Âzer»"),
  tok("لَهُ", "li", "prep", ["huruf-jarr", "mubtada-khabar", K], "اللَّامُ حَرْفُ جَرٍّ وَالْهَاءُ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«to him» — a fronted khabar; the nominal clause is kāna's khabar.", "«onun» — öne alınmış haber; isim cümlesi kâne'nin haberi.", segments=[seg("لَ", "li", "prep"), pr("هُ", "pron-3ms")]),
  tok("وَلَدٌ", "walad", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a son» — the delayed mubtadaʾ, in rafʿ.", "«bir oğul» — sonraya bırakılmış mübtedâ, merfû."),
  tok("رَشِيدٌ", "rashid", "noun", ["naat-sifa", "sifa-mushabbaha"], "صِفَةٌ لِوَلَدٍ مَرْفُوعَةٌ بِالضَّمَّةِ.", "«sensible» — the adjective, in rafʿ.", "«akıllı» — sıfat, merfû.", punct="،"),
  tok("رَشِيدٌ", "rashid", "noun", ["tawkid", "naat-sifa"], "تَوْكِيدٌ لَفْظِيٌّ بِالتَّكْرِيرِ، مَرْفُوعٌ.", "«sensible» — repeated: verbal emphasis.", "«akıllı» — tekrar: lafzî te'kid."),
  jiddan()])
sen("s11", "And this boy's name was Ibrāhīm.", "Ve bu çocuğun adı İbrâhim idi.", [
  kana(),
  tok("اسْمُ", "ism-name", "noun", [K, "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the name» — kāna's ism, raised; annexed.", "«adı» — kâne'nin ismi, merfû; muzâf."),
  tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«this» — a built demonstrative in the place of jarr, the annexed noun.", "«bu» — mebnî ism-i işâret, mahallen mecrûr muzâfun ileyh."),
  badal_of_ishara("الْوَلَدِ", "walad", "jarr", "«boy»", "«çocuğun»"),
  tok("إِبْرَاهِيمَ", "ibrahim", "propn", [K, "mamnu-min-sarf"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ibrāhīm» — kāna's khabar in naṣb; a foreign name, a diptote.", "«İbrâhim» — kâne'nin haberi, mansub; yabancı özel isim, gayr-i munsarıf.", punct=".")])
sen("s12", "And Ibrāhīm used to see the people prostrating to the idols.", "Ve İbrâhim insanları putlara secde ederken görürdü.", [
  kana(), name_ism_kana("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  khabar_mudari("يَرَى", "raa", ["naqis-verbs"], "«sees»", "«görür»"),
  tok("النَّاسَ", "nas", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the people» — the object, in naṣb.", "«insanları» — mef'ûl-i bih, mansub."),
  tok("يَسْجُدُونَ", "sajada", "verb", ["hal", "afal-khamsa", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ النَّاسِ.", "«prostrating» — the clause is a ḥāl of «the people».", "«secde ederken» — cümle, en-nâs'ın hâli."),
  tok("لِلْأَصْنَامِ", "sanam", "noun", ["huruf-jarr", "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَالْأَصْنَامِ مَجْرُورٌ بِالْكَسْرَةِ.", "«to the idols» — the lām of jarr; in jarr by kasra.", "«putlara» — cer lâmı; kesre ile mecrûr.", punct=".", segments=[seg("لِ", "li", "prep"), seg("الْأَصْنَامِ", "sanam", "noun")])])
sen("s13", "And he sees the people worshipping the idols.", "Ve insanları putlara taparken görür.", [
  tok("وَيَرَى", "raa", "verb", ["atf-nasaq", "mudari-marfu", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَرَى مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and he sees» — rafʿ implied on the alif; the doer is concealed.", "«ve görür» — elif üzerinde takdîrî damme; fâil gizli.", segments=wa_("يَرَى", "raa", "verb")),
  tok("النَّاسَ", "nas", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the people» — the object.", "«insanları» — mef'ûl-i bih."),
  tok("يَعْبُدُونَ", "abada", "verb", ["hal", "afal-khamsa", "mudari-marfu"], "مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ حَالٌ.", "«worshipping» — the clause is a ḥāl.", "«taparken» — cümle hâldir."),
  asnam("nasb", punct=".")])
sen("s14", "And Ibrāhīm knew that the idols were stones.", "Ve İbrâhim putların taş olduğunu bilirdi.", [
  kana(), name_ism_kana("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  khabar_mudari("يَعْرِفُ", "arafa", [], "«knows»", "«bilir»"),
  anna(), asnam_ism_anna(),
  tok("حِجَارَةٌ", "hijara", "noun", ["inna-wa-akhawatuha", "jam-taksir"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ حَجَرٍ.", "«stones» — the khabar of anna, in rafʿ.", "«taştır» — enne'nin haberi, merfû.", punct=".")])
sen("s15", "And he knew that the idols neither speak nor hear.", "Ve putların konuşmadığını ve işitmediğini bilirdi.", [
  kana(), khabar_mudari("يَعْرِفُ", "arafa", [], "«knows»", "«bilir»"),
  anna(), asnam_ism_anna(), la_nafiya(),
  neg_mudari("تَتَكَلَّمُ", "takallama", ["form-v-verbs", "inna-wa-akhawatuha"], "«speak» — the clause is anna's khabar.", "«konuşmaz» — cümle enne'nin haberi."),
  la_nafiya("وَلَا", wa=True),
  neg_mudari("تَسْمَعُ", "samia", ["atf-nasaq"], "«hear» — joined to the first verb, rafʿ.", "«işitmez» — ilk fiile ma'tûf, merfû.", punct=".")])
sen("s16", "And he knew that the idols neither harm nor benefit.", "Ve putların zarar da fayda da vermediğini bilirdi.", [
  kana(), khabar_mudari("يَعْرِفُ", "arafa", [], "«knows»", "«bilir»"),
  anna(), asnam_ism_anna(), la_nafiya(),
  neg_mudari("تَضُرُّ", "darra", ["doubled-verbs", "inna-wa-akhawatuha"], "«harm» — a doubled verb; the clause is anna's khabar.", "«zarar verir» — muzâaf fiil; cümle enne'nin haberi."),
  la_nafiya("وَلَا", wa=True),
  neg_mudari("تَنْفَعُ", "nafaa", ["atf-nasaq"], "«benefit» — joined, rafʿ.", "«fayda verir» — ma'tûf, merfû.", punct=".")])
sen("s17", "And he saw that the flies sit on the idols and they do not drive them off.", "Ve sineklerin putların üstüne konduğunu, onların da kovmadığını görürdü.", [
  kana(), khabar_mudari("يَرَى", "raa", ["naqis-verbs"], "«sees»", "«görür»"),
  tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha"], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ يَرَى.", "«that» — the clause is what he sees.", "«-dığını» — cümle, «görür»ün mef'ûlüdür."),
  tok("الذُّبَابَ", "dhubab", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ جِنْسٍ.", "«the flies» — anna's ism, in naṣb; a collective.", "«sinekler» — enne'nin ismi, mansub; cins ismi."),
  mudari("يَجْلِسُ", "jalasa", ["inna-wa-akhawatuha"], " — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.", "«sits» — the clause is anna's khabar.", "«konar» — cümle enne'nin haberi."),
  tok("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üstüne»."),
  tok("الْأَصْنَامِ", "sanam", "noun", ["huruf-jarr", "jam-taksir"], "مَجْرُورٌ بِعَلَى، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the idols» — in jarr by ʿalā.", "«putların» — alâ ile mecrûr."),
  tok("فَلَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not» — the fāʾ of sequence and the negating lā.", "«ve … -mez» — ta'kib fâsı ve nefiy lâ'sı.", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  neg_mudari("تَدْفَعُ", "dafaa", [], "«drive off» — the idols, feminine singular agreement.", "«kovmaz» — putlar, müfred müennes uyum.", punct=".")])
sen("s18", "And he saw the mouse eating the idols' food and they do not stop it.", "Ve farenin putların yemeğini yediğini, onların da engel olmadığını görürdü.", [
  kana(), khabar_mudari("يَرَى", "raa", ["naqis-verbs"], "«sees»", "«görür»"),
  tok("الْفَأْرَ", "far-mouse", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the mouse» — the object.", "«fareyi» — mef'ûl-i bih."),
  mudari("يَأْكُلُ", "akala", ["hal"], " — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الْفَأْرِ.", "«eating» — the clause is a ḥāl of «the mouse».", "«yerken» — cümle fârin hâli."),
  tok("طَعَامَ", "taam", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«the food of» — the object, annexed.", "«yemeğini» — mef'ûl-i bih, muzâf."),
  tok("الْأَصْنَامِ", "sanam", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the idols» — the annexed noun, in jarr.", "«putların» — muzâfun ileyh, mecrûr."),
  tok("فَلَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not».", "«ve … -mez».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  neg_mudari("تَمْنَعُ", "manaa", [], "«stop» — the idols, feminine singular agreement.", "«engel olmaz» — putlar, müfred müennes uyum.", punct=".")])
sen("s19", "And Ibrāhīm used to say to himself: why do the people prostrate to the idols?", "Ve İbrâhim kendi kendine derdi: insanlar putlara niçin secde ediyor?", [
  kana(), name_ism_kana("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  khabar_mudari("يَقُولُ", "qala", ["hollow-verbs"], "«says»", "«der»"),
  fi(),
  tok("نَفْسِهِ", "nafs", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِفِي، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«himself» — in jarr; the pronoun is annexed.", "«kendi» — mecrûr; zamir muzâfun ileyh.", punct=":", segments=[seg("نَفْسِ", "nafs", "noun"), pr("هِ", "pron-3ms")]),
  limadha(),
  mudari("يَسْجُدُ", "sajada", ["al-istifham"], "", "«prostrate» — rafʿ; the doer follows.", "«secde eder» — merfû; fâil sonra gelir.", hidden="(الْفَاعِلُ بَعْدَهُ)"),
  tok("النَّاسُ", "nas", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the people» — the doer.", "«insanlar» — fâil."),
  tok("لِلْأَصْنَامِ", "sanam", "noun", ["huruf-jarr", "jam-taksir"], "اللَّامُ حَرْفُ جَرٍّ، وَالْأَصْنَامِ مَجْرُورٌ.", "«to the idols».", "«putlara».", punct="؟", segments=[seg("لِ", "li", "prep"), seg("الْأَصْنَامِ", "sanam", "noun")])])
sen("s20", "And Ibrāhīm used to ask himself: why do the people ask the idols?", "Ve İbrâhim kendine sorardı: insanlar putlardan niçin dilekte bulunuyor?", [
  kana(), name_ism_kana("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  khabar_mudari("يَسْأَلُ", "saala", [], "«asks»", "«sorar»"),
  tok("نَفْسَهُ", "nafs", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«himself» — the object; the pronoun annexed.", "«kendine» — mef'ûl-i bih; zamir muzâfun ileyh.", punct=":", segments=[seg("نَفْسَ", "nafs", "noun"), pr("هُ", "pron-3ms")]),
  limadha(),
  mudari("يَسْأَلُ", "saala", ["al-istifham"], "", "«ask» — rafʿ; the doer follows.", "«sorar» — merfû; fâil sonra gelir.", hidden="(الْفَاعِلُ بَعْدَهُ)"),
  tok("النَّاسُ", "nas", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the people» — the doer.", "«insanlar» — fâil."),
  asnam("nasb", punct="؟")])

# ================================================================ §3 نصيحة إبراهيم
sen("s21", "And Ibrāhīm used to say to his father:", "Ve İbrâhim babasına derdi:", [
  kana(), name_ism_kana("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  khabar_mudari("يَقُولُ", "qala", ["hollow-verbs"], "«says»", "«der»"),
  tok("لِوَالِدِهِ", "walid-father", "noun", ["huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَوَالِدِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to his father» — the lām of jarr; annexed to the pronoun.", "«babasına» — cer lâmı; zamire muzâf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("وَالِدِ", "walid-father", "noun"), pr("هِ", "pron-3ms")])])
sen("s22", "O my father, why do you worship these idols?", "Ey babacığım, bu putlara niçin tapıyorsun?", [
  ya_nida(), abi(punct="،"), limadha(),
  mudari("تَعْبُدُ", "abada", ["al-istifham"], "", "«you worship» — the doer is a concealed «you».", "«taparsın» — fâil gizli «sen».", hidden="أَنْتَ"),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«these»", "«bu»"), asnam("nasb", punct="؟", rule="badal")])
sen("s23", "And O my father, why do you prostrate to these idols?", "Ve ey babacığım, bu putlara niçin secde ediyorsun?", [
  tok("وَيَا", "ya-nida", "part", ["vocative-munada", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَيَا حَرْفُ نِدَاءٍ.", "«and O».", "«ve ey».", segments=wa_("يَا", "ya-nida", "part")),
  abi(), limadha(),
  mudari("تَسْجُدُ", "sajada", ["al-istifham"], "", "«you prostrate» — concealed «you».", "«secde edersin» — gizli «sen».", hidden="أَنْتَ"),
  li_hadhihi(), asnam("jarr", punct="؟", rule="badal")])
sen("s24", "And O my father, why do you ask these idols?", "Ve ey babacığım, bu putlardan niçin dilekte bulunuyorsun?", [
  tok("وَيَا", "ya-nida", "part", ["vocative-munada", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَيَا حَرْفُ نِدَاءٍ.", "«and O».", "«ve ey».", segments=wa_("يَا", "ya-nida", "part")),
  abi(), limadha(),
  mudari("تَسْأَلُ", "saala", ["al-istifham"], "", "«you ask» — concealed «you».", "«sorarsın» — gizli «sen».", hidden="أَنْتَ"),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«these»", "«bu»"), asnam("nasb", punct="؟", rule="badal")])
sen("s25", "These idols neither speak nor hear!", "Bu putlar ne konuşur ne işitir!", [
  tok("إِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«indeed» — the particle of emphasis.", "«şüphesiz» — te'kid ve nasb harfi."),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«these»", "«bu»", tags=["inna-wa-akhawatuha"]),
  tok("الْأَصْنَامَ", "sanam", "noun", ["badal", "inna-wa-akhawatuha", "jam-taksir"], "بَدَلٌ مِنِ اسْمِ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«idols» — the substitute of inna's ism, in naṣb.", "«putlar» — inne'nin isminin bedeli, mansub."),
  la_nafiya(),
  neg_mudari("تَتَكَلَّمُ", "takallama", ["form-v-verbs", "inna-wa-akhawatuha"], "«speak» — the clause is inna's khabar.", "«konuşmaz» — cümle inne'nin haberi."),
  la_nafiya("وَلَا", wa=True),
  neg_mudari("تَسْمَعُ", "samia", ["atf-nasaq"], "«hear» — joined.", "«işitmez» — ma'tûf.", punct="!")])
sen("s26", "And these idols neither harm nor benefit!", "Ve bu putlar ne zarar verir ne fayda!", [
  tok("وَإِنَّ", "inna", "part", ["inna-wa-akhawatuha", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«and indeed».", "«ve şüphesiz».", segments=wa_("إِنَّ", "inna", "part")),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«these»", "«bu»", tags=["inna-wa-akhawatuha"]),
  tok("الْأَصْنَامَ", "sanam", "noun", ["badal", "inna-wa-akhawatuha", "jam-taksir"], "بَدَلٌ مِنِ اسْمِ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«idols» — the substitute of inna's ism.", "«putlar» — inne'nin isminin bedeli."),
  la_nafiya(),
  neg_mudari("تَضُرُّ", "darra", ["doubled-verbs", "inna-wa-akhawatuha"], "«harm» — the clause is inna's khabar.", "«zarar verir» — cümle inne'nin haberi."),
  la_nafiya("وَلَا", wa=True),
  neg_mudari("تَنْفَعُ", "nafaa", ["atf-nasaq"], "«benefit» — joined.", "«fayda verir» — ma'tûf.", punct="!")])
sen("s27", "And for what do you set food and drink before them?", "Ve niçin onların önüne yemek ve içecek koyuyorsun?", [
  tok("وَلِأَيِّ", "ayy", "pron", ["huruf-jarr", "al-istifham", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَأَيِّ اسْمُ اسْتِفْهَامٍ مَجْرُورٌ بِالْكَسْرَةِ — وَهُوَ الْمُعْرَبُ مِنْ أَسْمَاءِ الِاسْتِفْهَامِ — مُضَافٌ.", "«and for which» — the lām of jarr on ayy, the one interrogative that declines; annexed.", "«ve hangi … için» — cer lâmı; eyy, i'râb alan tek soru ismi; muzâf.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("أَيِّ", "ayy", "pron")]),
  tok("شَيْءٍ", "shay", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«thing» — the annexed noun, in jarr.", "«şey» — muzâfun ileyh, mecrûr."),
  mudari("تَضَعُ", "wadaa", ["mithal-verbs", "al-istifham"], "", "«you set» — a mithāl verb whose wāw falls in the muḍāriʿ; concealed «you».", "«koyarsın» — misâl fiil, muzâride vâvı düşer; gizli «sen».", hidden="أَنْتَ"),
  tok("لَهَا", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ.", "«for them» — the lām of jarr with the pronoun.", "«onlara» — cer lâmı ve zamir.", segments=[seg("لَ", "li", "prep"), pr("هَا", "pron-3fs")]),
  tok("الطَّعَامَ", "taam", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the food» — the object.", "«yemeği» — mef'ûl-i bih."),
  tok("وَالشَّرَابَ", "sharab", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالشَّرَابَ مَعْطُوفٌ مَنْصُوبٌ.", "«and the drink» — joined to the object.", "«ve içeceği» — mef'ûle ma'tûf.", punct="؟", segments=wa_("الشَّرَابَ", "sharab", "noun"))])
sen("s28", "And these idols, O my father, neither eat nor drink!", "Ve bu putlar, ey babacığım, ne yer ne içer!", [
  tok("وَإِنَّ", "inna", "part", ["inna-wa-akhawatuha", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«and indeed».", "«ve şüphesiz».", segments=wa_("إِنَّ", "inna", "part")),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«these»", "«bu»", tags=["inna-wa-akhawatuha"]),
  tok("الْأَصْنَامَ", "sanam", "noun", ["badal", "inna-wa-akhawatuha", "jam-taksir"], "بَدَلٌ مِنِ اسْمِ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«idols» — the substitute of inna's ism.", "«putlar» — inne'nin isminin bedeli."),
  tok("يَا", "ya-nida", "part", ["vocative-munada", "jumla-mutarida"], "حَرْفُ نِدَاءٍ — وَجُمْلَةُ النِّدَاءِ مُعْتَرِضَةٌ بَيْنَ اسْمِ إِنَّ وَخَبَرِهَا.", "«O» — the vocative, a parenthesis between inna's ism and its khabar.", "«ey» — nidâ, inne'nin ismi ile haberi arasında i'tirâz cümlesi."),
  abi(),
  la_nafiya(),
  neg_mudari("تَأْكُلُ", "akala", ["inna-wa-akhawatuha"], "«eat» — the clause is inna's khabar.", "«yemez» — cümle inne'nin haberi."),
  la_nafiya("وَلَا", wa=True),
  neg_mudari("تَشْرَبُ", "shariba", ["atf-nasaq"], "«drink» — joined.", "«içmez» — ma'tûf.", punct="!")])
sen("s29", "And Āzar used to get angry and not understand.", "Ve Âzer kızar ve anlamazdı.", [
  kana(), name_ism_kana("آزَرُ", "azar", "«Āzar»", "«Âzer»"),
  khabar_mudari("يَغْضَبُ", "ghadiba", [], "«gets angry»", "«kızar»"),
  la_nafiya("وَلَا", wa=True),
  mudari("يَفْهَمُ", "fahima", ["atf-nasaq", "la-nafiya"], " — مَعْطُوفٌ عَلَى يَغْضَبُ.", "«understand» — joined to the first verb.", "«anlamaz» — ilk fiile ma'tûf.", punct=".")])
sen("s30", "And Ibrāhīm used to advise his people, and the people would get angry and not understand.", "Ve İbrâhim kavmine öğüt verirdi; insanlar kızar ve anlamazdı.", [
  kana(), name_ism_kana("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  khabar_mudari("يَنْصَحُ", "nasaha", [], "«advises»", "«öğüt verir»"),
  tok("لِقَوْمِهِ", "qawm", "noun", ["huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَقَوْمِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — نَصَحَ لَهُ وَنَصَحَهُ سَوَاءٌ.", "«to his people» — the lām of jarr; naṣaḥa takes the lām or a direct object alike.", "«kavmine» — cer lâmı; nasaha hem lâm'la hem doğrudan mef'ûl alır.", punct="،", segments=[seg("لِ", "li", "prep"), seg("قَوْمِ", "qawm", "noun"), pr("هِ", "pron-3ms")]),
  kana(), ism_kana("النَّاسُ", "nas", "«the people»", "«insanlar»"),
  tok("يَغْضَبُونَ", "ghadiba", "verb", [K, "mudari-marfu", "afal-khamsa"], "مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ كَانَ.", "«get angry» — rafʿ by the kept nūn; the clause is kāna's khabar.", "«kızarlar» — nûnun sübûtuyla merfû; cümle kâne'nin haberi."),
  la_nafiya("وَلَا", wa=True),
  tok("يَفْهَمُونَ", "fahima", "verb", ["atf-nasaq", "la-nafiya", "afal-khamsa", "mudari-marfu"], "مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — مَعْطُوفٌ عَلَى يَغْضَبُونَ.", "«understand» — joined to the first verb.", "«anlamazlar» — ilk fiile ma'tûf.", punct=".")])

# ---------------------------------------------------------------- the glossary: this package's own entries, and the keys the corpus already owns
NEW = {
 "jiddan": G("jiddan", "جِدًّا", "ج د د", "noun", "very, very much (an absolute object used as an adverb)", "çok, pek (zarf olarak mef'ûl-i mutlak)", 1),
 "azar": G("azar", "آزَر", None, "propn", "Āzar, Ibrāhīm's father (the idol seller)", "Âzer, İbrâhim'in babası (put satıcısı)", 0),
 "baa": G("baa", "بَاعَ", "ب ي ع", "verb", "to sell", "satmak", 1, form="I"),
 "sanam": G("sanam", "صَنَم", "ص ن م", "noun", "idol", "put", 1, plural="أَصْنَام"),
 "rashid": G("rashid", "رَشِيد", "ر ش د", "noun", "sensible, rightly guided", "akıllı, doğru yolda", 1),
 "ibrahim": G("ibrahim", "إِبْرَاهِيم", None, "propn", "Ibrāhīm (Abraham), the prophet", "İbrâhim, peygamber", 0),
 "dhubab": G("dhubab", "ذُبَاب", "ذ ب ب", "noun", "flies (collective)", "sinek(ler)", 1),
 "far-mouse": G("far-mouse", "فَأْر", "ف أ ر", "noun", "mouse", "fare", 1),
 "limadha": G("limadha", "لِمَاذَا", None, "pron", "why? (for what?)", "niçin?", 1),
 "walid-father": G("walid-father", "وَالِد", "و ل د", "noun", "father (the one who begot)", "baba", 1),
 "nasaha": G("nasaha", "نَصَحَ", "ن ص ح", "verb", "to advise sincerely, to counsel", "öğüt vermek, nasihat etmek", 1, form="I"),
}
_used = sorted({t["lex"] for s_ in S for t in s_["tokens"]} | {sg["lex"] for s_ in S for t in s_["tokens"] for sg in t.get("segments", [])})
GLOSS_ADD = {}; _MISSING = []
for k in _used:
    if k in TG: continue
    if k in NEW: GLOSS_ADD[k] = NEW[k]; continue
    try: GLOSS_ADD[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))

# ---------------------------------------------------------------- paradigms: the corpus's own where it has them, the generator's for the two new verbs
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "baa", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "بَاع", "بِع", "بِيع", "بِع", "بِيع", "بِع", "بَيْع", "بَائِع", "مَبِيع", "بِيعَ", "يُبَاعُ",
                                  "أَجْوَفُ يَائِيٌّ: قُلِبَتِ الْيَاءُ أَلِفًا فِي الْمَاضِي (بَيَعَ → بَاعَ)، وَحُذِفَتْ عِنْدَ السُّكُونِ (بِعْتُ)، وَفِي الْمَجْهُولِ: بِيعَ يُبَاعُ."))
put_morph(mo, "nasaha", _sg.sound1("fataha", "نَصَح", "نْصَح", "اِنْصَح", "نُصْح", "نَاصِح", "مَنْصُوح", "نُصِحَ", "يُنْصَحُ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

ADD_EN = (" Chapter 1 (print pp. 6–8, sections 1–3): Āzar the idol seller (s1–s9), his son Ibrāhīm who sees what the idols cannot do (s10–s20), "
          "and Ibrāhīm's advice to his father (s21–s30). One printed line is one sentence; the printed vowelling is kept.")
ADD_TR = (" Birinci bölüm (basılı s. 6–8, 1–3. kısımlar): put satıcısı Âzer (s1–s9), putların yapamadığını gören oğlu İbrâhim (s10–s20) "
          "ve İbrâhim'in babasına öğüdü (s21–s30). Basılı her satır bir cümledir; basılı hareke korunmuştur.")
write_out(1, S, TITLE, ADD_EN, ADD_TR, "pp. 6–8", GLOSS_ADD)
report(1, S, GLOSS_ADD, ())
