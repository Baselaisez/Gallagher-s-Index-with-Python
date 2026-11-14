# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part One — chapter 2: «إِبْرَاهِيمُ يَكْسِرُ الْأَصْنَامَ» — the close of section 3 and sections 4–5 of «من كسر الأصنام؟»
(print pp. 9–11): the feast day, the idols that will not answer, the axe, and «who did this to our gods?». The dialogue quotes
al-Anbiyāʾ 21:59–63 and al-Ṣāffāt 37:92 exactly as the print sets them (the quoted sentences are marked). Every printed line is one
sentence; the vowelling is the print's. python3 tools/authoring/author_qisas_ch2.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas_common import *
import qisas_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
K = "kana-wa-akhawatuha"
TITLE = {"ar": "إِبْرَاهِيمُ يَكْسِرُ الْأَصْنَامَ", "en": "Ibrāhīm breaks the idols", "tr": "İbrâhim putları kırıyor"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

# ---------------------------------------------------------------- token helpers
def W(wa): return ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "")
def Wen(wa): return ("«and» + " if wa else "")
def Wtr(wa): return ("«ve» + " if wa else "")
def qala(full="قَالَ", punct=":", wa=False, hidden=None):
    ar = W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}" if hidden else "") + " — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ."
    return tok(full, "qala", "verb", ["hollow-verbs", "maful-bihi"], ar, Wen(wa) + "«said» — a māḍī built on fatḥa; what is said is its object.", Wtr(wa) + "«dedi» — fetha üzere mebnî mâzî; söylenen söz mef'ûlüdür.", punct=punct, segments=(wa_("قَالَ", "qala", "verb") if wa else None))
def qalu(full="قَالُوا", punct=":", wa=False, tags=()):
    return tok(full, "qala", "verb", ["hollow-verbs", "maful-bihi"] + list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ.", Wen(wa) + "«they said» — a māḍī built on ḍamma before the group's wāw; the wāw is the doer.", Wtr(wa) + "«dediler» — cemi vâvı sebebiyle zamme üzere mebnî mâzî; vâv fâildir.", punct=punct, segments=(wa_("قَالُوا", "qala", "verb") if wa else None))
def mazi(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, wa=False, extra_ar=""):
    ar = W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}" if hidden else "") + extra_ar + "."
    segs = (wa_(full[2:], lex, "verb") if wa else None)
    return tok(full, lex, "verb", list(tags), ar, Wen(wa) + en + (" — a māḍī built on fatḥa; the doer is the concealed pronoun." if hidden else " — a māḍī built on fatḥa."), Wtr(wa) + tr + (" — fetha üzere mebnî mâzî; fâil gizli zamirdir." if hidden else " — fetha üzere mebnî mâzî."), punct=punct, segments=segs)
def mazi_pl(full, lex, en, tr, tags=(), punct=None, wa=False):
    segs = (wa_(full[2:], lex, "verb") if wa else None)
    return tok(full, lex, "verb", list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ.", Wen(wa) + en + " — a māḍī built on ḍamma before the group's wāw; the wāw is the doer.", Wtr(wa) + tr + " — cemi vâvı ile zamme üzere mebnî mâzî; vâv fâildir.", punct=punct, segments=segs)
def mazi_ta(full, lex, en, tr, tags=(), punct=None, wa=False, extra=""):
    segs = (wa_(full[2:], lex, "verb") if wa else None)
    return tok(full, lex, "verb", list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ" + extra + ".", Wen(wa) + en + " — a māḍī built on fatḥa; the tāʾ marks the feminine.", Wtr(wa) + tr + " — fetha üzere mebnî mâzî; tâ te'nis içindir.", punct=punct, segments=segs)
def fail(full, lex, en, tr, tags=(), punct=None, extra_ar=""):
    return tok(full, lex, "noun", ["fail"] + list(tags), "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ" + extra_ar + ".", en + " — the doer, rafʿ by ḍamma.", tr + " — fâil, damme ile merfû.", punct=punct)
def fail_name(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", ["fail", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the doer; a foreign name, a diptote.", tr + " — fâil; yabancı özel isim, gayr-i munsarıf.", punct=punct)
def maful(full, lex, en, tr, tags=(), punct=None, extra_ar=""):
    return tok(full, lex, "noun", ["maful-bihi"] + list(tags), "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ" + extra_ar + ".", en + " — the object, naṣb by fatḥa.", tr + " — mef'ûl-i bih, fetha ile mansub.", punct=punct)
def asnam_maful(punct=None): return maful("الْأَصْنَامَ", "sanam", "«the idols»", "«putları»", tags=["jam-taksir"], punct=punct, extra_ar=" — جَمْعُ صَنَمٍ")
def nas_fail(punct=None, wa=False): return fail("النَّاسُ", "nas", "«the people»", "«insanlar»", punct=punct)
def mudari(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, extra_ar=""):
    return tok(full, lex, "verb", ["mudari-marfu"] + list(tags), f"فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}{extra_ar}.", en + " — a muḍāriʿ in rafʿ; the doer is concealed.", tr + " — merfû muzari; fâil gizli zamirdir.", punct=punct)
def khamsa(full, lex, en, tr, tags=(), punct=None, extra_ar="", wa=False):
    segs = (wa_(full[2:], lex, "verb") if wa else None)
    return tok(full, lex, "verb", ["afal-khamsa", "mudari-marfu"] + list(tags), W(wa) + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ" + extra_ar + ".", Wen(wa) + en + " — one of the five verbs, rafʿ by the kept nūn; the wāw is the doer.", Wtr(wa) + tr + " — ef'âl-i hamseden, nûnun sübûtu ile merfû; vâv fâildir.", punct=punct, segments=segs)
def ala(full="أَلَا", punct=None, wa=False, tags=()):
    return tok(full, "hamza-istifham", "part", ["al-istifham", "khuruj-al-istifham", "la-nafiya"] + list(tags), "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَلَا نَافِيَةٌ — اسْتِفْهَامٌ خَرَجَ إِلَى التَّقْرِيعِ وَالْعَرْضِ.", "«won't you…?» — the question hamza over the negating lā; a question that rebukes or offers.", "«…mez misiniz?» — nefiy lâ'sı üzerindeki istifham hemzesi; azarlama ve arz için.", punct=punct, segments=[seg("أَ", "hamza-istifham", "part"), seg("لَا", "la-nafiya", "part")])
def la_nafiya(full="لَا", wa=False, punct=None):
    return tok(full, "la-nafiya", "part", ["la-nafiya"], W(wa) + "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", Wen(wa) + "«not» — the negating lā, no government.", Wtr(wa) + "«değil/-mez» — nefiy lâ'sı, amel etmez.", punct=punct, segments=(wa_("لَا", "la-nafiya", "part") if wa else None))
def neg_mudari(full, lex, en, tr, tags=(), hidden="هِيَ", punct=None, extra=""):
    return tok(full, lex, "verb", ["la-nafiya", "mudari-marfu"] + list(tags), f"فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: {hidden}{extra}.", en + " — rafʿ after the negating lā; the doer is concealed.", tr + " — nefiy lâ'sından sonra merfû; fâil gizli zamirdir.", punct=punct)
def anna(wa=False, full=None):
    full = full or ("وَأَنَّ" if wa else "أَنَّ")
    return tok(full, "anna", "part", ["inna-wa-akhawatuha"] + (["atf-nasaq"] if wa else []), W(wa) + "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ، وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولُ يَعْرِفُ.", Wen(wa) + "«that» — a particle like a verb: naṣb on its ism, rafʿ on its khabar; the clause is the object of «know».", Wtr(wa) + "«-dığını» — fiile benzeyen harf: ismini nasb, haberini ref eder; cümle «bilir»in mef'ûlüdür.", segments=(wa_("أَنَّ", "anna", "part") if wa else None))
def ism_anna(full, lex, en, tr, tags=(), punct=None, extra=""):
    return tok(full, lex, "noun", ["inna-wa-akhawatuha"] + list(tags), "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ" + extra + ".", en + " — the ism of anna, in naṣb.", tr + " — enne'nin ismi, mansub.", punct=punct)
def khabar_anna(full, lex, en, tr, tags=(), punct=None, extra=""):
    return tok(full, lex, "noun", ["inna-wa-akhawatuha"] + list(tags), "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ" + extra + ".", en + " — the khabar of anna, in rafʿ.", tr + " — enne'nin haberi, merfû.", punct=punct)
def kana(full="وَكَانَ", punct=None, wa=True):
    return tok(full, "kana", "verb", [K, "hollow-verbs"], W(wa) + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", Wen(wa) + "«was» — the defective verb kāna: it raises its ism and puts its khabar in naṣb.", Wtr(wa) + "«idi» — nâkıs fiil kâne: ismini ref, haberini nasb eder.", punct=punct, segments=(wa_("كَانَ", "kana", "verb") if wa else None))
def kanu(full="وَكَانُوا", wa=True):
    return tok(full, "kana", "verb", [K, "hollow-verbs"], W(wa) + "كَانُوا فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهَا فِي مَحَلِّ رَفْعٍ.", Wen(wa) + "«they were» — kāna with the group's wāw as its ism.", Wtr(wa) + "«idiler» — kâne; cemi vâvı onun ismidir.", segments=(wa_("كَانُوا", "kana", "verb") if wa else None))
def ism_kana(full, lex, en, tr, tags=(), punct=None):
    return tok(full, lex, "noun", [K] + list(tags), "اسْمُ كَانَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.", en + " — the ism of kāna, raised by ḍamma.", tr + " — kâne'nin ismi, damme ile merfû.", punct=punct)
def khabar_kana_khamsa(full, lex, en, tr):
    return tok(full, lex, "verb", [K, "afal-khamsa", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", en + " — one of the five verbs, rafʿ by the nūn; the clause is kāna's khabar.", tr + " — ef'âl-i hamseden; cümle kâne'nin haberidir.")
def ishara(full, lex, case, en, tr, punct=None, tags=()):
    C = {"nasb": ("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "object"), "jarr": ("فِي مَحَلِّ جَرٍّ", "in the place of jarr"), "raf": ("فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "the mubtadaʾ")}[case]
    return tok(full, lex, "pron", ["asma-al-ishara"] + list(tags), f"اسْمُ إِشَارَةٍ مَبْنِيٌّ {C[0]}.", en + f" — a demonstrative, built; {C[1]}.", tr + " — ism-i işâret, mebnî; mahallen " + {"nasb": "mansub (mef'ûl)", "jarr": "mecrûr", "raf": "merfû (mübtedâ)"}[case] + ".", punct=punct)
def pron_anta(full="أَنْتَ", punct=None, tags=()):
    return tok(full, "anta", "pron", ["mubtada-khabar"] + list(tags), "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«you» — a detached pronoun built on fatḥa, the mubtadaʾ.", "«sen» — fetha üzere mebnî munfasıl zamir, mübtedâ.", punct=punct)
def pron_ana(full="أَنَا", punct=None):
    return tok(full, "pron-1s-munfasil", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«I» — a detached pronoun built on sukūn, the mubtadaʾ.", "«ben» — sükûn üzere mebnî munfasıl zamir, mübtedâ.", punct=punct)
def li_asnam(punct=None, tags=()):
    return tok("لِلْأَصْنَامِ", "sanam", "noun", ["huruf-jarr", "jam-taksir"] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَالْأَصْنَامِ مَجْرُورٌ بِالْكَسْرَةِ.", "«to the idols» — the lām of jarr; in jarr by kasra.", "«putlara» — cer lâmı; kesre ile mecrûr.", punct=punct, segments=[seg("لِ", "li", "prep"), seg("الْأَصْنَامِ", "sanam", "noun")])
def sen(sid, en, tr, toks): S.append({"id": sid, "translation": {"en": en, "tr": tr}, "tokens": toks})
def quran(toks, first_tag=True):
    toks[0]["quoteBefore"] = "«"; toks[-1]["quoteAfter"] = "»"
    if first_tag: toks[0].setdefault("grammar", []).insert(0, "al-iqtibas-wal-tadmin")
    return toks

# ================================================================ §3 close (p. 9)
sen("s1", "Ibrāhīm said: I will break the idols when the people have gone, and then the people will understand.",
    "İbrâhim dedi: İnsanlar gidince putları kırarım; o zaman insanlar anlar.", [
  qala(punct=None), fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=":"),
  pron_ana(),
  tok("أَكْسِرُ", "kasara", "verb", ["mubtada-khabar", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.", "«I break» — a muḍāriʿ in rafʿ; the doer «I» is concealed by necessity; the clause is the khabar.", "«kırarım» — merfû muzari; fâil zorunlu gizli «ben»; cümle haberdir."),
  asnam_maful(),
  tok("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ — وَجَوَابُهُ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«when» — a time-adverb with a conditional sense, built; its answer is what precedes.", "«-ınca» — şart mânâsı taşıyan zaman zarfı, mebnî; cevabı öncekidir."),
  mazi("ذَهَبَ", "dhahaba", "«went»", "«gitti»", tags=["idha-shartiyya"], hidden=None, extra_ar="، فِعْلُ الشَّرْطِ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا إِلَيْهِ"),
  nas_fail(punct="،"),
  tok("وَحِينَئِذٍ", "hinaidhin", "noun", ["atf-nasaq", "maful-fih", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَحِينَ ظَرْفُ زَمَانٍ مَنْصُوبٌ مُضَافٌ إِلَى إِذْ، وَالتَّنْوِينُ عِوَضٌ عَنْ جُمْلَةٍ مَحْذُوفَةٍ — أَيْ: حِينَ إِذْ ذَهَبُوا.", "«and then» — «at the time» annexed to «idh»; the tanwīn stands in for a dropped clause.", "«ve o zaman» — «hîn» zarfı «iz»e muzâf; tenvin hazfedilen cümlenin ivazıdır.", segments=[seg("وَ", "wa", "conj"), seg("حِينَئِذٍ", "hinaidhin", "noun")]),
  mudari("يَفْهَمُ", "fahima", "«understand»", "«anlar»", hidden=None, extra_ar=""),
  nas_fail(punct=".")])
S[-1]["tokens"][8] = tok("يَفْهَمُ", "fahima", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«understand(s)» — a muḍāriʿ in rafʿ.", "«anlar» — merfû muzari.")

# ================================================================ §4 إبراهيم يكسر الأصنام
sen("s2", "And a feast day came, and the people rejoiced.", "Ve bir bayram günü geldi; insanlar sevindi.", [
  mazi("وَجَاءَ", "jaa", "«came»", "«geldi»", tags=["hollow-verbs"], hidden=None, wa=True),
  tok("يَوْمُ", "yawm", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«a day» — the doer, in rafʿ; annexed.", "«günü» — fâil, merfû; muzâf."),
  tok("عِيدٍ", "id", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«of feast» — the annexed noun, in jarr.", "«bayram» — muzâfun ileyh, mecrûr."),
  tok("فَفَرِحَ", "fariha", "verb", ["atf-nasaq"], "الْفَاءُ عَاطِفَةٌ لِلتَّعْقِيبِ، وَفَرِحَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«so rejoiced» — the fāʾ of sequence; a māḍī.", "«hemen sevindi» — ta'kib fâsı; mâzî.", segments=[seg("فَ", "fa", "conj"), seg("فَرِحَ", "fariha", "verb")]),
  nas_fail(punct=".")])
sen("s3", "And the people went out for the feast, and the children went out.", "Ve insanlar bayrama çıktı, çocuklar çıktı.", [
  mazi("وَخَرَجَ", "kharaja", "«went out»", "«çıktı»", hidden=None, wa=True), nas_fail(),
  tok("لِلْعِيدِ", "id", "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْعِيدِ مَجْرُورٌ بِالْكَسْرَةِ.", "«for the feast» — the lām of jarr; in jarr.", "«bayram için» — cer lâmı; mecrûr.", segments=[seg("لِ", "li", "prep"), seg("الْعِيدِ", "id", "noun")]),
  mazi("وَخَرَجَ", "kharaja", "«went out»", "«çıktı»", hidden=None, wa=True),
  fail("الْأَطْفَالُ", "atfal", "«the children»", "«çocuklar»", tags=["jam-taksir"], punct=".", extra_ar=" — جَمْعُ طِفْلٍ")])
sen("s4", "And Ibrāhīm's father went out and said to Ibrāhīm: Won't you come out with us?", "Ve İbrâhim'in babası çıktı ve İbrâhim'e dedi: Bizimle çıkmaz mısın?", [
  mazi("وَخَرَجَ", "kharaja", "«went out»", "«çıktı»", hidden=None, wa=True),
  tok("وَالِدُ", "walid-father", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the father» — the doer; annexed.", "«babası» — fâil; muzâf."),
  tok("إِبْرَاهِيمَ", "ibrahim", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«of Ibrāhīm» — the annexed noun, jarr shown by fatḥa: a diptote.", "«İbrâhim'in» — muzâfun ileyh; gayr-i munsarıf olduğu için fetha ile mecrûr."),
  qala("وَقَالَ", punct=None, wa=True, hidden="هُوَ"),
  tok("لِإِبْرَاهِيمَ", "ibrahim", "propn", ["huruf-jarr", "mamnu-min-sarf"], "اللَّامُ حَرْفُ جَرٍّ، وَإِبْرَاهِيمَ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«to Ibrāhīm» — the lām of jarr; jarr by fatḥa, a diptote.", "«İbrâhim'e» — cer lâmı; kesre yerine fetha ile mecrûr, gayr-i munsarıf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("إِبْرَاهِيمَ", "ibrahim", "propn")]),
  ala(),
  tok("تَخْرُجُ", "kharaja", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.", "«you come out» — a muḍāriʿ in rafʿ; «you» is concealed by necessity.", "«çıkarsın» — merfû muzari; fâil zorunlu gizli «sen»."),
  tok("مَعَنَا", "maa", "noun", ["maful-fih", "idafa-definiteness"], "مَعَ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«with us» — the adverb «with» in naṣb, annexed to the pronoun «us».", "«bizimle» — mansub mekân zarfı; «biz» zamiri muzâfun ileyh.", punct="؟", segments=[seg("مَعَ", "maa", "noun"), seg("نَا", "pron-1p", "pron")])])
sen("s5", "Ibrāhīm said: I am sick!", "İbrâhim dedi: Ben hastayım!", [
  qala(punct=None), fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=":"),
  pron_ana(),
  tok("سَقِيمٌ", "saqim", "noun", ["mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِيلٍ.", "«sick» — the khabar, in rafʿ; a resembling adjective on faʿīl.", "«hasta» — haber, merfû; faîl vezninde sıfat-ı müşebbehe.", punct="!")])
sen("s6", "And the people went, and Ibrāhīm stayed in the house.", "Ve insanlar gitti; İbrâhim evde kaldı.", [
  mazi("وَذَهَبَ", "dhahaba", "«went»", "«gitti»", hidden=None, wa=True), nas_fail(),
  mazi("وَبَقِيَ", "baqiya", "«stayed»", "«kaldı»", tags=["naqis-verbs"], hidden=None, wa=True),
  fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْبَيْتِ", "bayt", "noun", ["huruf-jarr"], "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the house» — in jarr by «in».", "«evde» — fî ile mecrûr.", punct=".")])
sen("s7", "And Ibrāhīm came to the idols and said to the idols:", "Ve İbrâhim putların yanına geldi ve putlara dedi:", [
  mazi("وَجَاءَ", "jaa", "«came»", "«geldi»", tags=["hollow-verbs"], hidden=None, wa=True),
  fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  tok("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْأَصْنَامِ", "sanam", "noun", ["huruf-jarr", "jam-taksir"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ.", "«the idols» — in jarr by «to».", "«putlara» — ilâ ile mecrûr.", punct="،"),
  qala("وَقَالَ", punct=None, wa=True, hidden="هُوَ"), li_asnam(punct=":")])
sen("s8", "Won't you speak? Won't you hear?", "Konuşmaz mısınız? İşitmez misiniz?", [
  ala(), khamsa("تَتَكَلَّمُونَ", "takallama", "«you speak»", "«konuşursunuz»", tags=["form-v-verbs"], punct="؟"),
  ala(), khamsa("تَسْمَعُونَ", "samia", "«you hear»", "«işitirsiniz»", punct="؟")])
sen("s9", "Here is food and drink! Won't you eat? Won't you drink?", "İşte yemek ve içecek! Yemez misiniz? İçmez misiniz?", [
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»"),
  tok("طَعَامٌ", "taam", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«food» — the khabar, in rafʿ.", "«yemek» — haber, merfû."),
  tok("وَشَرَابٌ", "sharab", "noun", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَشَرَابٌ مَعْطُوفٌ عَلَى طَعَامٍ مَرْفُوعٌ مِثْلُهُ.", "«and drink» — joined to «food», in the same rafʿ.", "«ve içecek» — taâm'a ma'tûf, merfû.", punct="!", segments=[seg("وَ", "wa", "conj"), seg("شَرَابٌ", "sharab", "noun")]),
  ala(), khamsa("تَأْكُلُونَ", "akala", "«you eat»", "«yersiniz»", punct="؟"),
  ala(), khamsa("تَشْرَبُونَ", "shariba", "«you drink»", "«içersiniz»", punct="؟")])
sen("s10", "And the idols were silent, because they are stones that do not speak.", "Ve putlar sustu; çünkü onlar konuşmayan taşlardır.", [
  mazi_ta("وَسَكَتَتِ", "sakata", "«were silent»", "«sustu»", wa=True, extra=" — وَكُسِرَتِ التَّاءُ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("الْأَصْنَامُ", "sanam", "«the idols»", "«putlar»", tags=["jam-taksir"]),
  tok("لِأَنَّهَا", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«because they» — the lām of cause on anna; the pronoun «they» is its ism.", "«çünkü onlar» — ta'lil lâmı + enne; «onlar» zamiri ismidir.", segments=[seg("لِأَنَّ", "lianna", "part"), seg("هَا", "pron-3fs", "pron")]),
  khabar_anna("حِجَارَةٌ", "hijara", "«stones»", "«taşlardır»", tags=["jam-taksir"], extra=" — جَمْعُ حَجَرٍ"),
  la_nafiya(),
  neg_mudari("لَا تَنْطِقُ", "nataqa", "«do not speak»", "«konuşmaz»", tags=["jumla-sifa"], punct=".", extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِحِجَارَةٍ")])
S[-1]["tokens"][-1]["surface"] = {"full": "تَنْطِقُ", "smart": "تَنْطِقُ", "bare": bare("تَنْطِقُ")}
sen("s11", "Ibrāhīm said: «What is the matter with you that you do not speak?» (al-Ṣāffāt 37:92)", "İbrâhim dedi: «Size ne oluyor da konuşmuyorsunuz?» (Sâffât 37:92)", [
  qala(punct=None), fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=":")] + quran([
  tok("مَا", "ma-istifham", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«what» — the interrogative noun, built; the mubtadaʾ.", "«ne» — mebnî istifham ismi; mübtedâ."),
  tok("لَكُمْ", "li", "prep", ["huruf-jarr", "mubtada-khabar"], "اللَّامُ حَرْفُ جَرٍّ، وَكُمْ ضَمِيرٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ.", "«with you» — the lām of jarr on the pronoun; the phrase is the khabar.", "«size» — cer lâmı + zamir; câr-mecrûr haberdir.", segments=[seg("لَ", "li", "prep"), seg("كُمْ", "pron-2mp", "pron")]),
  la_nafiya(),
  khamsa("تَنْطِقُونَ", "nataqa", "«you speak»", "«konuşursunuz»", tags=["la-nafiya", "hal"], punct=".", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ ضَمِيرِ لَكُمْ")]))
sen("s12", "And the idols were silent and did not speak.", "Ve putlar sustu, konuşmadı.", [
  mazi_ta("وَسَكَتَتِ", "sakata", "«were silent»", "«sustu»", wa=True, extra=" — وَكُسِرَتِ التَّاءُ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("الْأَصْنَامُ", "sanam", "«the idols»", "«putlar»", tags=["jam-taksir"]),
  tok("وَمَا", "ma-nafiya", "part", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«and not» — the negating mā, no government.", "«ve -medi» — nefiy mâ'sı, amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  mazi_ta("نَطَقَتْ", "nataqa", "«spoke»", "«konuştu»", punct=".", extra="، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ")])
sen("s13", "Then Ibrāhīm got angry and took the axe.", "O zaman İbrâhim kızdı ve baltayı aldı.", [
  tok("حِينَئِذٍ", "hinaidhin", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ مُضَافٌ إِلَى إِذْ، وَالتَّنْوِينُ عِوَضٌ عَنْ جُمْلَةٍ مَحْذُوفَةٍ.", "«then» — a time-adverb annexed to «idh»; the tanwīn stands in for a dropped clause.", "«o zaman» — «iz»e muzâf zaman zarfı; tenvin ivazdır."),
  mazi("غَضِبَ", "ghadiba", "«got angry»", "«kızdı»", hidden=None),
  fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  mazi("وَأَخَذَ", "akhadha", "«took»", "«aldı»", hidden="هُوَ", wa=True),
  maful("الْفَأْسَ", "fas", "«the axe»", "«baltayı»", punct=".")])
sen("s14", "And Ibrāhīm struck the idols with the axe and broke the idols.", "Ve İbrâhim putlara baltayla vurdu ve putları kırdı.", [
  mazi("وَضَرَبَ", "daraba", "«struck»", "«vurdu»", hidden=None, wa=True),
  fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  asnam_maful(),
  tok("بِالْفَأْسِ", "fas", "noun", ["huruf-jarr"], "الْبَاءُ لِلِاسْتِعَانَةِ حَرْفُ جَرٍّ، وَالْفَأْسِ مَجْرُورٌ بِالْكَسْرَةِ.", "«with the axe» — the bāʾ of means; in jarr.", "«baltayla» — istiâne bâsı; mecrûr.", segments=[seg("بِ", "bi", "prep"), seg("الْفَأْسِ", "fas", "noun")]),
  mazi("وَكَسَرَ", "kasara", "«broke»", "«kırdı»", hidden="هُوَ", wa=True),
  asnam_maful(punct=".")])
sen("s15", "And Ibrāhīm left the biggest idol and hung the axe on its neck.", "Ve İbrâhim en büyük putu bıraktı ve baltayı onun boynuna astı.", [
  mazi("وَتَرَكَ", "taraka", "«left»", "«bıraktı»", hidden=None, wa=True),
  fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»"),
  maful("الصَّنَمَ", "sanam", "«the idol»", "«putu»"),
  tok("الْأَكْبَرَ", "akbar", "noun", ["naat-sifa", "ism-tafdil"], "صِفَةٌ لِلصَّنَمِ مَنْصُوبَةٌ بِالْفَتْحَةِ — اسْمُ تَفْضِيلٍ عَلَى أَفْعَلَ.", "«the biggest» — the adjective of «the idol», in naṣb; an elative on afʿal.", "«en büyük» — sanem'in sıfatı, mansub; ef'al vezninde ism-i tafdîl."),
  tok("وَعَلَّقَ", "allaqa", "verb", ["atf-nasaq", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَعَلَّقَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and hung» — a Form II māḍī; the doer «he» is concealed.", "«ve astı» — tef'îl bâbından mâzî; fâil gizli «o».", segments=[seg("وَ", "wa", "conj"), seg("عَلَّقَ", "allaqa", "verb")]),
  maful("الْفَأْسَ", "fas", "«the axe»", "«baltayı»"),
  tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  tok("عُنُقِهِ", "unuq", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِفِي، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«its neck» — in jarr; the pronoun «its» is the annexed noun.", "«boynuna» — fî ile mecrûr; zamir muzâfun ileyh.", punct=".", segments=[seg("عُنُقِ", "unuq", "noun"), seg("هِ", "pron-3ms", "pron")])])

# ================================================================ §5 من فعل هذا؟
sen("s16", "And the people returned and entered the house of the idols.", "Ve insanlar döndü ve putların evine girdiler.", [
  mazi("وَرَجَعَ", "rajaa", "«returned»", "«döndü»", hidden=None, wa=True), nas_fail(),
  mazi_pl("وَدَخَلُوا", "dakhala", "«entered»", "«girdiler»", tags=["atf-nasaq"], wa=True),
  tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«into».", "«-e»."),
  tok("بَيْتِ", "bayt", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِفِي، وَهُوَ مُضَافٌ.", "«the house» — in jarr; annexed.", "«evine» — fî ile mecrûr; muzâf."),
  tok("الْأَصْنَامِ", "sanam", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«of the idols» — the annexed noun, in jarr.", "«putların» — muzâfun ileyh, mecrûr.", punct=".")])
sen("s17", "And the people wanted to prostrate to the idols, because it was a feast day.", "Ve insanlar putlara secde etmek istediler; çünkü bayram günüydü.", [
  mazi("وَأَرَادَ", "arada", "«wanted»", "«istedi»", tags=["hollow-verbs", "form-iv-verbs"], hidden=None, wa=True), nas_fail(),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ أَرَادَ.", "«to» — the maṣdar-making particle; the clause is the object of «wanted».", "«-mek» — nasb eden masdariyye harfi; cümle «istedi»nin mef'ûlüdür."),
  tok("يَسْجُدُوا", "sajada", "verb", ["an-masdariyya", "afal-khamsa"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«they prostrate» — in naṣb by an, its sign the dropped nūn; the wāw is the doer.", "«secde etmeleri» — en ile mansub, nûnun düşmesiyle; vâv fâildir."),
  li_asnam(),
  tok("لِأَنَّهُ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«because it» — the lām of cause on anna; the pronoun is its ism.", "«çünkü o» — ta'lil lâmı + enne; zamir ismidir.", segments=[seg("لِأَنَّ", "lianna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("يَوْمُ", "yawm", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«a day» — the khabar of anna, in rafʿ; annexed.", "«günü» — enne'nin haberi, merfû; muzâf."),
  tok("عِيدٍ", "id", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«of feast» — the annexed noun, in jarr.", "«bayram» — muzâfun ileyh, mecrûr.", punct=".")])
sen("s18", "But the people were astonished and amazed.", "Fakat insanlar şaşırdı ve hayrete düştü.", [
  tok("وَلٰكِنْ", "lakin", "part", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the lightened lākin: a particle of correction, no government.", "«fakat» — tahfif edilmiş lâkin: istidrak harfi, amel etmez.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنْ", "lakin", "part")]),
  tok("تَعَجَّبَ", "taajjaba", "verb", ["form-v-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — مِنْ بَابِ التَّفَعُّلِ.", "«were astonished» — a Form V māḍī.", "«şaşırdı» — tefa''ul bâbından mâzî."),
  nas_fail(),
  mazi_pl("وَدَهِشُوا", "dahisha", "«were amazed»", "«hayrete düştüler»", tags=["atf-nasaq"], punct=".", wa=True)])
sen("s19", "And the people were sorry and angry.", "Ve insanlar üzüldü ve kızdı.", [
  tok("وَتَأَسَّفَ", "taassafa", "verb", ["form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَأَسَّفَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — مِنْ بَابِ التَّفَعُّلِ.", "«were sorry» — a Form V māḍī.", "«üzüldü» — tefa''ul bâbından mâzî.", segments=[seg("وَ", "wa", "conj"), seg("تَأَسَّفَ", "taassafa", "verb")]),
  nas_fail(),
  mazi_pl("وَغَضِبُوا", "ghadiba", "«got angry»", "«kızdılar»", tags=["atf-nasaq"], punct=".", wa=True)])
sen("s20", "They said: «Who did this to our gods?» (al-Anbiyāʾ 21:59)", "Dediler: «Bunu ilâhlarımıza kim yaptı?» (Enbiyâ 21:59)", [
  qalu()] + quran([
  tok("مَنْ", "man", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«who» — the interrogative noun, built; the mubtadaʾ.", "«kim» — mebnî istifham ismi; mübtedâ."),
  mazi("فَعَلَ", "faala", "«did»", "«yaptı»", hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ"),
  ishara("هٰذَا", "hadha", "nasb", "«this»", "«bunu»"),
  tok("بِآلِهَتِنَا", "ilah", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "الْبَاءُ حَرْفُ جَرٍّ، وَآلِهَةِ مَجْرُورٌ بِالْكَسْرَةِ مُضَافٌ، وَنَا ضَمِيرٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — آلِهَة جَمْعُ إِلَهٍ.", "«to our gods» — the bāʾ of jarr; «gods» (plural of ilāh) annexed to «our».", "«ilâhlarımıza» — cer bâsı; «ilâhlar» (ilâh'ın çoğulu) «biz»e muzâf.", punct="؟", segments=[seg("بِ", "bi", "prep"), seg("آلِهَةِ", "ilah", "noun"), seg("نَا", "pron-1p", "pron")])]))
sen("s21", "«They said: We heard a young man speaking of them, called Ibrāhīm.» (al-Anbiyāʾ 21:60)", "«Dediler: Onları anan bir genç işittik; ona İbrâhim denir.» (Enbiyâ 21:60)", quran([
  qalu(tags=["al-iqtibas-wal-tadmin"]),
  tok("سَمِعْنَا", "samia", "verb", ["maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«we heard» — a māḍī built on sukūn before «we»; the pronoun is the doer.", "«işittik» — «biz» zamiri sebebiyle sükûn üzere mebnî mâzî; zamir fâildir.", segments=[seg("سَمِعْ", "samia", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("فَتًى", "fatan", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمٌ مَقْصُورٌ.", "«a young man» — the object; naṣb by an estimated fatḥa on the alif: a maqṣūr noun.", "«bir genç» — mef'ûl; elif üzerinde takdîrî fetha ile mansub: maksûr isim."),
  tok("يَذْكُرُهُمْ", "dhakara", "verb", ["jumla-sifa", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ صِفَةٌ لِفَتًى.", "«speaking of them» — a muḍāriʿ with its concealed doer and the object pronoun; the clause describes «a young man».", "«onları anan» — muzari; fâil gizli, «onlar» mef'ûl; cümle fetâ'nın sıfatıdır.", segments=[seg("يَذْكُرُ", "dhakara", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("يُقَالُ", "qala", "verb", ["naib-al-fail", "jumla-sifa", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ — وَالْجُمْلَةُ صِفَةٌ ثَانِيَةٌ لِفَتًى.", "«it is said» — a passive muḍāriʿ; the jarr phrase after it stands as its deputy doer; a second description of the young man.", "«denir» — meçhul muzari; sonraki câr-mecrûr nâib-i fâildir; fetâ'nın ikinci sıfatı."),
  tok("لَهُ", "li", "prep", ["huruf-jarr", "naib-al-fail"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«to him» — the jarr phrase in the place of rafʿ as deputy doer.", "«ona» — câr-mecrûr, mahallen merfû nâib-i fâil.", segments=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")]),
  tok("إِبْرَاهِيمُ", "ibrahim", "propn", ["mamnu-min-sarf", "naib-al-fail"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ مَرْفُوعٌ بِالضَّمَّةِ — أَيْ: هُوَ إِبْرَاهِيمُ؛ وَالْجُمْلَةُ مَقُولُ الْقَوْلِ. عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ibrāhīm» — the khabar of an unspoken mubtadaʾ («he is Ibrāhīm»), the thing said; a diptote name.", "«İbrâhim» — hazfedilmiş mübtedânın haberi («o İbrâhim'dir»), söylenen söz; gayr-i munsarıf özel isim.", punct=".")], first_tag=False))
sen("s22", "«They said: Was it you who did this to our gods, O Ibrāhīm?» (al-Anbiyāʾ 21:62)", "«Dediler: Bunu ilâhlarımıza sen mi yaptın ey İbrâhim?» (Enbiyâ 21:62)", quran([
  qalu(tags=["al-iqtibas-wal-tadmin"]),
  tok("أَأَنْتَ", "anta", "pron", ["al-istifham", "mubtada-khabar"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَأَنْتَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَتَقْدِيمُ الضَّمِيرِ عَلَى الْفِعْلِ لِأَنَّ السُّؤَالَ عَنِ الْفَاعِلِ.", "«was it you» — the question hamza on the detached pronoun, the mubtadaʾ; fronted because the doer is what is asked.", "«sen mi» — istifham hemzesi + munfasıl zamir, mübtedâ; soru fâil hakkında olduğu için öne alınmıştır.", segments=[seg("أَ", "hamza-istifham", "part"), seg("أَنْتَ", "anta", "pron")]),
  tok("فَعَلْتَ", "faala", "verb", ["mubtada-khabar"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرٌ.", "«you did» — a māḍī built on sukūn before the doer's tāʾ; the tāʾ is the doer; the clause is the khabar.", "«yaptın» — fâil tâsı sebebiyle sükûn üzere mebnî mâzî; tâ fâildir; cümle haberdir.", segments=[seg("فَعَلْ", "faala", "verb"), seg("تَ", "pron-2ms", "pron")]),
  ishara("هٰذَا", "hadha", "nasb", "«this»", "«bunu»"),
  tok("بِآلِهَتِنَا", "ilah", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "الْبَاءُ حَرْفُ جَرٍّ، وَآلِهَةِ مَجْرُورٌ مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«to our gods» — the bāʾ of jarr; annexed to «our».", "«ilâhlarımıza» — cer bâsı; «biz»e muzâf.", segments=[seg("بِ", "bi", "prep"), seg("آلِهَةِ", "ilah", "noun"), seg("نَا", "pron-1p", "pron")]),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi."),
  tok("إِبْرَاهِيمُ", "ibrahim", "propn", ["vocative-munada", "mamnu-min-sarf"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Ibrāhīm» — a single proper-name vocative, built on ḍamma in the place of naṣb.", "«İbrâhim» — müfred alem münâdâ, zamme üzere mebnî, mahallen mansub.", punct="؟")], first_tag=False))
sen("s23", "«He said: Rather, this big one of them did it — so ask them, if they can speak.» (al-Anbiyāʾ 21:63)", "«Dedi: Hayır, onu şu büyükleri yaptı; konuşabiliyorlarsa onlara sorun.» (Enbiyâ 21:63)", quran([
  qala(punct=None, hidden="هُوَ"),
  tok("بَلْ", "bal", "part", ["al-iqtibas-wal-tadmin"], "حَرْفُ إِضْرَابٍ.", "«rather» — a particle of correction.", "«hayır, bilakis» — idrâb harfi."),
  tok("فَعَلَهُ", "faala", "verb", ["maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«did it» — a māḍī; the pronoun «it» is its object, placed before the doer.", "«onu yaptı» — mâzî; «onu» zamiri öne alınmış mef'ûldür.", segments=[seg("فَعَلَ", "faala", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("كَبِيرُهُمْ", "kabir", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَهُمْ ضَمِيرٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«their big one» — the doer, delayed, in rafʿ; annexed to «them».", "«büyükleri» — sonraya bırakılmış fâil, merfû; «onlar»a muzâf.", segments=[seg("كَبِيرُ", "kabir", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "naat-sifa"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِكَبِيرِهِمْ (أَوْ بَدَلٌ).", "«this» — a built demonstrative in the place of rafʿ, describing «their big one» (or its badal).", "«şu» — mebnî ism-i işâret, mahallen merfû; kebîruhum'un sıfatı (veya bedeli)."),
  tok("فَاسْأَلُوهُمْ", "saala", "verb", ["imperative-amr", "fa-khabar-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَاسْأَلُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَهُمْ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«so ask them» — the fāʾ of consequence; an imperative built on the dropped nūn; the wāw is the doer, «them» the object.", "«o halde onlara sorun» — tefrî' fâsı; nûnun hazfi üzere mebnî emir; vâv fâil, «onlar» mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("اسْأَلُوا", "saala", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("إِنْ", "in-shart", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ — وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«if» — the conditional particle; its answer is unspoken, shown by what precedes.", "«eğer» — cezm eden şart harfi; cevabı hazfedilmiştir."),
  tok("كَانُوا", "kana", "verb", ["in-shartiyya", K, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْوَاوُ اسْمُهَا.", "«they were» — the defective verb as the condition's verb, in the place of jazm; the wāw is its ism.", "«idiler» — şart fiili olarak mahallen meczûm nâkıs fiil; vâv ismidir."),
  tok("يَنْطِقُونَ", "nataqa", "verb", [K, "afal-khamsa", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«speak» — one of the five verbs; the clause is kāna's khabar.", "«konuşurlar» — ef'âl-i hamseden; cümle kâne'nin haberidir.", punct=".")], first_tag=False))
sen("s24", "And the people knew that the idols were stones.", "Ve insanlar putların taş olduğunu bilirlerdi.", [
  kana(), ism_kana("النَّاسُ", "nas", "«the people»", "«insanlar»"),
  khabar_kana_khamsa("يَعْرِفُونَ", "arafa", "«know»", "«bilirler»"),
  anna(), ism_anna("الْأَصْنَامَ", "sanam", "«the idols»", "«putların»", tags=["jam-taksir"]),
  khabar_anna("حِجَارَةٌ", "hijara", "«stones»", "«taş»", tags=["jam-taksir"], punct=".")])
sen("s25", "And they knew that stones neither hear nor speak.", "Ve taşların işitmediğini ve konuşmadığını bilirlerdi.", [
  kanu(), khabar_kana_khamsa("يَعْرِفُونَ", "arafa", "«know»", "«bilirler»"),
  anna(), ism_anna("الْحِجَارَةَ", "hijara", "«the stones»", "«taşların»", tags=["jam-taksir"]),
  la_nafiya(), neg_mudari("تَسْمَعُ", "samia", "«hear»", "«işitir»", extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ"),
  la_nafiya("وَلَا", wa=True), neg_mudari("تَنْطِقُ", "nataqa", "«speak»", "«konuşur»", tags=["atf-nasaq"], punct=".", extra=" — مَعْطُوفٌ عَلَى تَسْمَعُ")])
sen("s26", "And they knew that the biggest idol was also a stone.", "Ve en büyük putun da taş olduğunu bilirlerdi.", [
  kanu(), khabar_kana_khamsa("يَعْرِفُونَ", "arafa", "«know»", "«bilirler»"),
  anna(), ism_anna("الصَّنَمَ", "sanam", "«the idol»", "«putun»"),
  tok("الْأَكْبَرَ", "akbar", "noun", ["naat-sifa", "ism-tafdil"], "صِفَةٌ لِلصَّنَمِ مَنْصُوبَةٌ بِالْفَتْحَةِ — اسْمُ تَفْضِيلٍ.", "«the biggest» — the adjective, in naṣb; an elative.", "«en büyük» — sıfat, mansub; ism-i tafdîl."),
  tok("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ — أَيْ: آضَ أَيْضًا — مَنْصُوبٌ بِالْفَتْحَةِ.", "«also» — an absolute object of an unspoken verb, in naṣb.", "«de, dahi» — hazfedilmiş fiilin mef'ûl-i mutlakı, mansub."),
  khabar_anna("حَجَرٌ", "hajar", "«a stone»", "«taştır»", punct=".")])
sen("s27", "And that the biggest idol cannot walk or move.", "Ve en büyük putun yürüyemediğini ve kımıldayamadığını.", [
  anna(wa=True), ism_anna("الصَّنَمَ", "sanam", "«the idol»", "«putun»"),
  tok("الْأَكْبَرَ", "akbar", "noun", ["naat-sifa", "ism-tafdil"], "صِفَةٌ لِلصَّنَمِ مَنْصُوبَةٌ بِالْفَتْحَةِ.", "«the biggest» — the adjective, in naṣb.", "«en büyük» — sıfat, mansub."),
  la_nafiya(), neg_mudari("يَقْدِرُ", "qadara-able", "«is able»", "«güç yetirir»", hidden="هُوَ", extra=" — وَالْجُمْلَةُ خَبَرُ أَنَّ"),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ يَقْدِرُ.", "«to» — the maṣdar-making particle; the clause is the object of «is able».", "«-meye» — masdariyye harfi; cümle «güç yetirir»in mef'ûlüdür."),
  tok("يَمْشِيَ", "masha", "verb", ["an-masdariyya", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«walk» — in naṣb by an, the fatḥa written on the yāʾ; the doer is concealed.", "«yürümeye» — en ile mansub; fetha yâ üzerinde zâhirdir; fâil gizli."),
  tok("وَيَتَحَرَّكَ", "taharraka", "verb", ["atf-nasaq", "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَتَحَرَّكَ مَعْطُوفٌ عَلَى يَمْشِيَ مَنْصُوبٌ بِالْفَتْحَةِ — مِنْ بَابِ التَّفَعُّلِ.", "«or move» — joined to «walk», in naṣb; a Form V verb.", "«ve kımıldamaya» — yemşiye'ye ma'tûf, mansub; tefa''ul bâbından.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("يَتَحَرَّكَ", "taharraka", "verb")])])
sen("s28", "And that the biggest idol cannot break the idols.", "Ve en büyük putun putları kıramadığını.", [
  anna(wa=True), ism_anna("الصَّنَمَ", "sanam", "«the idol»", "«putun»"),
  tok("الْأَكْبَرَ", "akbar", "noun", ["naat-sifa", "ism-tafdil"], "صِفَةٌ لِلصَّنَمِ مَنْصُوبَةٌ بِالْفَتْحَةِ.", "«the biggest» — the adjective, in naṣb.", "«en büyük» — sıfat, mansub."),
  la_nafiya(), neg_mudari("يَقْدِرُ", "qadara-able", "«is able»", "«güç yetirir»", hidden="هُوَ", extra=" — وَالْجُمْلَةُ خَبَرُ أَنَّ"),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«to» — the maṣdar-making particle.", "«-meye» — masdariyye harfi."),
  tok("يَكْسِرَ", "kasara", "verb", ["an-masdariyya"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«break» — in naṣb by an; the doer is concealed.", "«kırmaya» — en ile mansub; fâil gizli."),
  asnam_maful(punct=".")])
sen("s29", "So they said to Ibrāhīm: You know that the idols do not speak.", "Bunun üzerine İbrâhim'e dediler: Sen putların konuşmadığını bilirsin.", [
  tok("فَقَالُوا", "qala", "verb", ["atf-nasaq", "hollow-verbs", "maful-bihi"], "الْفَاءُ عَاطِفَةٌ، وَقَالُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«so they said» — the fāʾ of sequence; a māḍī on ḍamma, the wāw its doer.", "«bunun üzerine dediler» — ta'kib fâsı; zamme üzere mebnî mâzî, vâv fâil.", segments=[seg("فَ", "fa", "conj"), seg("قَالُوا", "qala", "verb")]),
  tok("لِإِبْرَاهِيمَ", "ibrahim", "propn", ["huruf-jarr", "mamnu-min-sarf"], "اللَّامُ حَرْفُ جَرٍّ، وَإِبْرَاهِيمَ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«to Ibrāhīm» — jarr by fatḥa, a diptote.", "«İbrâhim'e» — fetha ile mecrûr, gayr-i munsarıf.", punct=":", segments=[seg("لِ", "li", "prep"), seg("إِبْرَاهِيمَ", "ibrahim", "propn")]),
  pron_anta(),
  tok("تَعْلَمُ", "alima", "verb", ["mubtada-khabar", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ — وَالْجُمْلَةُ خَبَرٌ.", "«you know» — a muḍāriʿ in rafʿ; «you» concealed by necessity; the clause is the khabar.", "«bilirsin» — merfû muzari; fâil zorunlu gizli «sen»; cümle haberdir."),
  anna(), ism_anna("الْأَصْنَامَ", "sanam", "«the idols»", "«putların»", tags=["jam-taksir"]),
  la_nafiya(), neg_mudari("تَنْطِقُ", "nataqa", "«speak»", "«konuşur»", punct=".", extra=" — وَالْجُمْلَةُ خَبَرُ أَنَّ")])
sen("s30", "Ibrāhīm said: Then how do you worship the idols, when they neither harm nor benefit?", "İbrâhim dedi: Öyleyse putlara nasıl tapıyorsunuz; onlar ne zarar verir ne fayda?", [
  qala(punct=None), fail_name("إِبْرَاهِيمُ", "ibrahim", "«Ibrāhīm»", "«İbrâhim»", punct=":"),
  tok("فَكَيْفَ", "kayfa", "noun", ["al-istifham", "hal"], "الْفَاءُ لِلتَّفْرِيعِ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«then how» — the fāʾ of consequence; the interrogative «how», built, in the place of naṣb as a ḥāl.", "«öyleyse nasıl» — tefrî' fâsı; mebnî istifham ismi, mahallen mansub hâl.", segments=[seg("فَ", "fa", "conj"), seg("كَيْفَ", "kayfa", "noun")]),
  khamsa("تَعْبُدُونَ", "abada", "«you worship»", "«taparsınız»"),
  asnam_maful(),
  tok("وَإِنَّهَا", "inna", "part", ["inna-wa-akhawatuha", "anwa-al-waw", "hal"], "الْوَاوُ حَالِيَّةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«while they» — the wāw of state; inna with the pronoun «they» as its ism; the clause is a ḥāl.", "«oysa onlar» — hâl vâvı; inne + «onlar» zamiri ismi; cümle hâldir.", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part"), seg("هَا", "pron-3fs", "pron")]),
  la_nafiya(), neg_mudari("تَضُرُّ", "darra", "«harm»", "«zarar verir»", tags=["doubled-verbs"], extra=" — وَالْجُمْلَةُ خَبَرُ إِنَّ"),
  la_nafiya("وَلَا", wa=True), neg_mudari("تَنْفَعُ", "nafaa", "«benefit»", "«fayda verir»", tags=["atf-nasaq"], punct="؟", extra=" — مَعْطُوفٌ عَلَى تَضُرُّ")])
sen("s31", "And how do you ask the idols, when they neither speak nor hear?", "Ve putlardan nasıl dilekte bulunuyorsunuz; onlar ne konuşur ne işitir?", [
  tok("وَكَيْفَ", "kayfa", "noun", ["al-istifham", "hal", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«and how» — the interrogative «how», built, in the place of naṣb as a ḥāl.", "«ve nasıl» — mebnî istifham ismi, mahallen mansub hâl.", segments=[seg("وَ", "wa", "conj"), seg("كَيْفَ", "kayfa", "noun")]),
  khamsa("تَسْأَلُونَ", "saala", "«you ask»", "«dilersiniz»"),
  asnam_maful(),
  tok("وَإِنَّهَا", "inna", "part", ["inna-wa-akhawatuha", "anwa-al-waw", "hal"], "الْوَاوُ حَالِيَّةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا اسْمُهَا — وَالْجُمْلَةُ حَالٌ.", "«while they» — the wāw of state; inna with its pronoun ism; the clause is a ḥāl.", "«oysa onlar» — hâl vâvı; inne + zamir ismi; cümle hâldir.", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part"), seg("هَا", "pron-3fs", "pron")]),
  la_nafiya(), neg_mudari("تَنْطِقُ", "nataqa", "«speak»", "«konuşur»", extra=" — وَالْجُمْلَةُ خَبَرُ إِنَّ"),
  la_nafiya("وَلَا", wa=True), neg_mudari("تَسْمَعُ", "samia", "«hear»", "«işitir»", tags=["atf-nasaq"], punct="؟", extra=" — مَعْطُوفٌ عَلَى تَنْطِقُ")])
sen("s32", "Don't you understand anything? Do you not reason?", "Hiçbir şey anlamıyor musunuz? Akıl etmiyor musunuz?", [
  ala(), khamsa("تَفْهَمُونَ", "fahima", "«you understand»", "«anlarsınız»"),
  maful("شَيْئًا", "shay", "«anything»", "«bir şey»", punct="،"),
  tok("أَفَلَا", "hamza-istifham", "part", ["al-istifham", "khuruj-al-istifham", "la-nafiya", "atf-nasaq"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَالْفَاءُ عَاطِفَةٌ، وَلَا نَافِيَةٌ — وَقُدِّمَتِ الْهَمْزَةُ عَلَى الْفَاءِ لِأَنَّ لَهَا الصَّدَارَةَ.", "«do you then not» — the hamza of denial, the fāʾ of joining and the negating lā; the hamza stands first because it owns the sentence-head.", "«o halde … -mez misiniz» — inkârî istifham hemzesi, atıf fâsı ve nefiy lâ'sı; hemze sadâret hakkı için fâ'dan önce gelir.", segments=[seg("أَ", "hamza-istifham", "part"), seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  khamsa("تَعْقِلُونَ", "aqala", "«you reason»", "«akıl edersiniz»", punct="؟")])
sen("s33", "And the people fell silent and were ashamed!", "Ve insanlar sustu ve utandı!", [
  mazi("وَسَكَتَ", "sakata", "«fell silent»", "«sustu»", hidden=None, wa=True), nas_fail(),
  mazi_pl("وَخَجِلُوا", "khajila", "«were ashamed»", "«utandılar»", tags=["atf-nasaq"], punct="!", wa=True)])

# ---------------------------------------------------------------- glossary: reuse what any package owns; mint only the new words
NEW = {
 "kasara": G("kasara", "كَسَرَ", "ك س ر", "verb", "to break", "kırmak", 1, form="I"),
 "hinaidhin": G("hinaidhin", "حِينَئِذٍ", "ح ي ن", "noun", "then, at that time (ḥīna + idh; the tanwīn replaces a dropped clause)", "o zaman, o vakit (hîn + iz; tenvin hazfedilen cümlenin ivazı)", 2),
 "saqim": G("saqim", "سَقِيم", "س ق م", "noun", "sick, ailing (adjective on faʿīl)", "hasta (faîl vezninde sıfat)", 2),
 "sakata": G("sakata", "سَكَتَ", "س ك ت", "verb", "to be silent, fall silent", "susmak", 1, form="I"),
 "fas": G("fas", "فَأْس", "ف أ س", "noun", "axe", "balta", 1, plural="فُؤُوس"),
 "akbar": G("akbar", "أَكْبَر", "ك ب ر", "noun", "bigger, biggest (elative of kabīr; a diptote)", "daha/en büyük (kebîr'in ism-i tafdîli; gayr-i munsarıf)", 1),
 "taajjaba": G("taajjaba", "تَعَجَّبَ", "ع ج ب", "verb", "to be astonished, to wonder", "şaşmak, hayret etmek", 2, form="V"),
 "dahisha": G("dahisha", "دَهِشَ", "د ه ش", "verb", "to be amazed, dumbfounded", "hayrete düşmek, afallamak", 2, form="I"),
 "taassafa": G("taassafa", "تَأَسَّفَ", "أ س ف", "verb", "to be sorry, to regret", "üzülmek, hayıflanmak", 2, form="V"),
 "hajar": G("hajar", "حَجَر", "ح ج ر", "noun", "a stone", "taş", 1, plural="حِجَارَة"),
 "taharraka": G("taharraka", "تَحَرَّكَ", "ح ر ك", "verb", "to move (intransitive), to stir", "kımıldamak, hareket etmek", 2, form="V"),
 "khajila": G("khajila", "خَجِلَ", "خ ج ل", "verb", "to be ashamed, abashed", "utanmak, mahcup olmak", 2, form="I"),
 "qadara-able": G("qadara-able", "قَدَرَ", "ق د ر", "verb", "to be able (qadara ʿalā / qadara an); the same verb as «to decree»", "güç yetirmek, yapabilmek (aynı fiilin «takdir etmek» anlamı da vardır)", 1, form="I"),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (the negating mā before a verb)", "-medi, değil (fiilden önce nefiy mâ'sı)", 1),
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
put_morph(mo, "kasara", _sg.sound1("daraba", "كَسَر", "كْسِر", "اِكْسِر", "كَسْر", "كَاسِر", "مَكْسُور", "كُسِرَ", "يُكْسَرُ"))
put_morph(mo, "sakata", _sg.idgham(_sg.sound1("nasara", "سَكَت", "سْكُت", "اُسْكُت", "سُكُوت", "سَاكِت", note="لَازِمٌ، فَلَا مَفْعُولَ لَهُ وَلَا مَجْهُولَ.")))
put_morph(mo, "dahisha", _sg.sound1("samia", "دَهِش", "دْهَش", "اِدْهَش", "دَهَش", "دَاهِش", note="لَازِمٌ."))
put_morph(mo, "khajila", _sg.sound1("samia", "خَجِل", "خْجَل", "اِخْجَل", "خَجَل", "خَاجِل", note="لَازِمٌ."))
put_morph(mo, "taajjaba", _sg.derived("مِنْ بَابِ التَّفَعُّلِ", "تَفَعَّلَ يَتَفَعَّلُ", "َ", "تَعَجَّب", "تَعَجَّب", "تَعَجَّب", "تَعَجُّب", "مُتَعَجِّب", note="لَازِمٌ — مُطَاوِعُ «عَجَّبَ»."))
put_morph(mo, "taassafa", _sg.derived("مِنْ بَابِ التَّفَعُّلِ", "تَفَعَّلَ يَتَفَعَّلُ", "َ", "تَأَسَّف", "تَأَسَّف", "تَأَسَّف", "تَأَسُّف", "مُتَأَسِّف", note="لَازِمٌ — مَهْمُوزُ الْفَاءِ."))
put_morph(mo, "taharraka", _sg.derived("مِنْ بَابِ التَّفَعُّلِ", "تَفَعَّلَ يَتَفَعَّلُ", "َ", "تَحَرَّك", "تَحَرَّك", "تَحَرَّك", "تَحَرُّك", "مُتَحَرِّك", note="لَازِمٌ — مُطَاوِعُ «حَرَّكَ»."))
if "qadara-able" not in mo["verbs"]: mo["verbs"]["qadara-able"] = find_morph("qadara")
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        try: mo["verbs"][_k] = find_morph(_k)
        except KeyError: pass
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

ADD_EN = (" Chapter 2 (print pp. 9–11: the close of section 3 and sections 4–5): the feast day and the breaking of the idols (s1–s15), "
          "and «who did this to our gods?» (s16–s33). s11 quotes al-Ṣāffāt 37:92 and s20–s23 quote al-Anbiyāʾ 21:59–63 as the print sets them "
          "(s21 reads يَذْكُرُهُمْ as the Karachi print has it); the quoted sentences are marked. One printed line is one sentence; the printed vowelling is kept.")
ADD_TR = (" İkinci bölüm (basılı s. 9–11: 3. kısmın sonu ile 4–5. kısımlar): bayram günü ve putların kırılması (s1–s15) ve «bunu ilâhlarımıza kim yaptı?» (s16–s33). "
          "s11 Sâffât 37:92'yi, s20–s23 Enbiyâ 21:59–63'ü baskıdaki şekliyle aktarır (s21 Karaçi baskısındaki gibi يَذْكُرُهُمْ okur); alıntı cümleler işaretlidir. "
          "Basılı her satır bir cümledir; basılı hareke korunmuştur.")
write_out(2, S, TITLE, ADD_EN, ADD_TR, "pp. 9–11", GLOSS_ADD)
report(2, S, GLOSS_ADD, ())
