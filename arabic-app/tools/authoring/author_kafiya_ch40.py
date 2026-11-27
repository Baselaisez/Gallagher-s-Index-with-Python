# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 40: THE LETTERS OF URGING هَلَّا أَلَّا لَوْلَا لَوْمَا (head of the sentence; a verb stated or implied; on a māḍī
reproach + urging, on a muḍāriʿ a command by urging); the letter of expectation قَدْ (on a māḍī: certainty with expectation, and
bringing the past near the present — the awaited amir, the muʾadhdhin's قَدْ قَامَتِ الصَّلَاةُ; on a muḍāriʿ: certainty with
fewness); the two question letters (head of the sentence; on both kinds of sentence; the hamza more general than هَلْ in four ways).
Source: the Ottoman notebook (Ziya Sungur-oglu), line ~346 of the transcription.

  COMMENTARY (the notebook): s1-s9 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch40.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-tahdid-wa-qad-wal-istifham-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "حُرُوفُ التَّحْضِيضِ وَقَدْ وَحَرْفَا الِاسْتِفْهَامِ", "en": "The letters of urging, qad, and the two letters of question", "tr": "Tahdîd harfleri, kad ve iki istifham harfi"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def prTa(): return seg("تَ", "pron-2ms", "pron")
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def pr2mp(): return seg("كُمْ", "pron-2mp", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
def pr3mp(): return seg("هُمْ", "pron-3mp", "pron")
def pr3d(): return seg("هُمَا", "pron-3d", "pron")
def W(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return tok(full, lex, pos, [K] + tags, ar, en, tr, punct=punct, segments=segments)
def nahwu(punct=":"):
    return W("نَحْوُ", "nahw", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness"],
             "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ، وَمَا بَعْدَهُ مُضَافٌ إِلَيْهِ.", "«for instance» — the khabar of a dropped mubtada, annexed to what it cites.",
             "«meselâ» — hazfedilmiş bir mübtedânın haberi; zikrettiğine muzâf.", punct=punct)
def atf_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    segs = [seg("وَ", "wa", "conj")] + (extra_segs if extra_segs else [seg(inner, lex, pos)])
    return W(full, lex, pos, ["atf-nasaq"] + tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=segs)
def cited(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return W(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ — " + ar, en, tr, punct=punct, segments=segments)
def cited_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    return atf_wa(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — " + ar, en, tr, inner, punct=punct, extra_segs=extra_segs)
def li_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "اللَّامُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("لِ", "li", "prep"), seg(inner, lex, pos)]))
def bi_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْبَاءُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("بِ", "bi", "prep"), seg(inner, lex, pos)]))
def ka_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("كَ", "ka", "part"), seg(inner, lex, pos)]))
def jw(full): return full[0] + full[2:] if full[0] == "ا" and full[1] in "ُِ" else full

AT = "atf-nasaq"
IS = "al-istifham"
QD = "qad-harf"
def HL(full, lex, en, tr, inner=None, punct=None, pos="part", tags=()):
    if inner: return cited_wa(full, lex, pos, [AT, K] + list(tags), inner + " مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", en, tr, inner, punct=punct)
    return cited(full, lex, pos, ["mubtada-khabar", K] + list(tags), "لَفْظٌ مَحْكِيٌّ — خَبَرٌ.", en, tr, punct=punct)
def DAKHALAT(wa=True, tags=()):
    if wa: return atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... zaman».", "إِذَا")
    return W("فَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْصِيلِ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«so when».", "«... zaman».", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")])
def DKH(): return W("دَخَلَتْ", "dakhala", "verb", ["idha-shartiyya", "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ — فِعْلُ الشَّرْطِ.", "«it enters».", "«girerse».", segments=[seg("دَخَلَ", "dakhala", "verb"), seg("تْ", "ta-tanith", "part")])
def ALA(): return W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«... üzerine»."),
def MADI(punct=None): return W("الْمَاضِي", "madi", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«a past verb».", "«mâzî».", punct=punct)
def MUDARI(punct=None): return W("الْمُضَارِعِ", "mudari", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a muḍāriʿ».", "«muzâri».", punct=punct)
def AFADAT(full="أَفَادَتْ", en="«it conveys».", tr="«ifade eder».", tags=()):
    return W(full, "afada", "verb", ["fail", "form-iv-verbs", "hollow-verbs", "al-fa-fi-jawab-al-shart"] + list(tags), "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — جَوَابُ إِذَا.", en, tr, segments=[seg("أَفَادَ", "afada", "verb"), seg("تْ" if full.endswith("تْ") else "تِ", "ta-tanith", "part")])
def ZAYDAN(punct=None, ar="مَفْعُولٌ بِهِ مَنْصُوبٌ."): return cited("زَيْدًا", "zayd", "propn", ["maful-bihi"], ar, "«Zayd».", "«Zeyd'e».", punct=punct)
def ZAYD(punct=None, tags=("fail",), ar="فَاعِلٌ مَرْفُوعٌ.", tr="«Zeyd»."): return cited("زَيْدٌ", "zayd", "propn", list(tags), ar, "«Zayd».", tr, punct=punct)
def QAIM(punct=None): return cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«standing».", "«ayakta».", punct=punct)
def HAL(punct=None, ar="حَرْفُ اسْتِفْهَامٍ."): return cited("هَلْ", "hal-istifham", "part", [IS, K], ar, "«is».", "«mi».", punct=punct)
def HAMZA_N(full, tags, ar, en, tr, punct=None): return W(full, "hamza-letter", "noun", tags, ar, en, tr, punct=punct)

S.append({"id": "s1", "translation": {
 "en": "The letters of urging are هَلَّا, أَلَّا, لَوْلَا and لَوْمَا; they come at the head of the sentence, and a verb must follow them, stated or implied." + C_EN,
 "tr": "Tahdîd harfleri هَلَّا, أَلَّا, لَوْلَا ve لَوْمَا'dır; sözün başında gelirler ve onlara lafzen ya da takdiren bir fiil lâzımdır." + C_TR},
 "tokens": [
  W("حُرُوفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the letters of».", "«harfleri»."),
  W("التَّحْضِيضِ", "tahdid", "noun", ["idafa-definiteness", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«urging».", "«tahdîd».", punct=":"),
  HL("هَلَّا", "halla", "«hallā».", "«hellâ»."),
  HL("وَأَلَّا", "alla-tahdid", "«allā».", "«ellâ».", "أَلَّا"),
  HL("وَلَوْلَا", "lawla", "«lawlā».", "«levlâ».", "لَوْلَا"),
  HL("وَلَوْمَا", "lawma", "«and lawmā».", "«ve levmâ».", "لَوْمَا", punct="؛"),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and they».", "«ve onlar».", "هِيَ"),
  W("تَقَعُ", "waqaa", "verb", ["mubtada-khabar", "fail", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الْجُمْلَةُ خَبَرٌ.", "«come».", "«gelirler»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-de»."),
  W("صَدْرِ", "sadr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the head of».", "«başında»."),
  W("الْكَلَامِ", "kalam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sentence».", "«sözün».", punct="،"),
  atf_wa("وَيَلْزَمُهَا", "lazima", "verb", ["fail", "maful-bihi", "taqdim-al-musnad"], "يَلْزَمُ فِعْلٌ مُضَارِعٌ، وَهَا مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«and must follow them».", "«ve onlara ... lâzımdır».", "يَلْزَمُهَا", extra_segs=[seg("يَلْزَمُ", "lazima", "verb"), pr3fs()]),
  W("فِعْلٌ", "fil", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a verb».", "«bir fiil»."),
  W("لَفْظًا", "lafz", "adv", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«stated».", "«lafzen»."),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("تَقْدِيرًا", "taqdir", "adv", [AT, "tamyiz"], "مَعْطُوفٌ مَنْصُوبٌ.", "«implied».", "«takdiren».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "When they enter on a past verb they convey a reproach to the hearer for leaving the act undone in the past and an urging of him to do it in the future — as هَلَّا نَصَرْتَ زَيْدًا, «why did you not help Zayd? — help him from now on»; and when they enter on a muḍāriʿ they convey a command by way of urging — as هَلَّا تَنْصُرُ زَيْدًا, «Zayd deserves help; help him»." + C_EN,
 "tr": "Mâzînin başında geldiklerinde geçmişte o fiili terk ettiğinden ötürü muhatabı kınama ve gelecekte o fiili yapmaya teşvik mânâsı ifade eder — هَلَّا نَصَرْتَ زَيْدًا gibi: «Zeyd'e yardım etmedin mi? Bari bundan sonra et»; muzârinin başında geldiklerinde teşvik yoluyla emir ifade eder — هَلَّا تَنْصُرُ زَيْدًا gibi: «Zeyd yardıma lâyıktır, ona yardım et»." + C_TR},
 "tokens": [
  DAKHALAT(wa=False), DKH(), *ALA(), MADI(),
  AFADAT(),
  W("تَوْبِيخَ", "tawbikh", "noun", ["maful-bihi", "idafa-definiteness", "form-ii-verbs"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«a reproach to».", "«kınama»."),
  W("الْمُخَاطَبِ", "mukhatab", "noun", ["idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the hearer».", "«muhatabı»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-den ötürü»."),
  W("تَرْكِ", "tark", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«leaving».", "«terk ettiğinden»."),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the act».", "«o fiili»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-te»."),
  MADI(),
  atf_wa("وَتَشْوِيقَهُ", "tashwiq", "noun", [AT, "idafa-definiteness", "form-ii-verbs"], "تَشْوِيقَ مَعْطُوفٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and an urging of him».", "«ve onu teşvik».", "تَشْوِيقَهُ", extra_segs=[seg("تَشْوِيقَ", "tashwiq", "noun"), pr3ms()]),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("فِعْلِهِ", "fil", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«doing it».", "«onu yapmaya».", segments=[seg("فِعْلِ", "fil", "noun"), pr3msi()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-te»."),
  W("الْمُسْتَقْبَلِ", "mustaqbal", "noun", ["huruf-jarr", "ism-maful", "form-x-verbs"], "مَجْرُورٌ.", "«the future».", "«gelecekte».", punct="،"),
  nahwu(),
  cited("هَلَّا", "halla", "part", [K, "insha-wa-tamanni"], "حَرْفُ تَحْضِيضٍ — مَعَ الْمَاضِي لِلتَّوْبِيخِ.", "«why did you not».", "«... -medin mi»."),
  cited("نَصَرْتَ", "nasara", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«help».", "«yardım et-».", segments=[seg("نَصَرْ", "nasara", "verb"), prTa()]),
  ZAYDAN(punct="؛"),
  DAKHALAT(), DKH(), *ALA(), MUDARI(),
  AFADAT("أَفَادَتِ"),
  W("الْأَمْرَ", "amr", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a command».", "«emir»."),
  bi_("بِطَرِيقِ", "tariq", "noun", ["idafa-definiteness"], "طَرِيقِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by way of».", "«... yoluyla».", "طَرِيقِ"),
  W("التَّشْوِيقِ", "tashwiq", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«urging».", "«teşvik».", punct="،"),
  nahwu(),
  cited("هَلَّا", "halla", "part", [K, "insha-wa-tamanni"], "حَرْفُ تَحْضِيضٍ — مَعَ الْمُضَارِعِ لِلْأَمْرِ.", "«will you not».", "«... -mez misin»."),
  cited("تَنْصُرُ", "nasara", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«help».", "«yardım et-»."),
  ZAYDAN(punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And the letter of expectation is قَدْ: when it enters on a past verb it conveys certainty together with expectation — as قَدْ رَكِبَ زَيْدٌ." + C_EN,
 "tr": "Tevakku harfi قَدْ'dir: mâzînin başında geldiğinde tevakku ile beraber tahkik mânâsı ifade eder — قَدْ رَكِبَ زَيْدٌ gibi." + C_TR},
 "tokens": [
  atf_wa("وَحَرْفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness"], "حَرْفُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the letter of».", "«ve ... harfi».", "حَرْفُ"),
  W("التَّوَقُّعِ", "tawaqqu", "noun", ["idafa-definiteness", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«expectation».", "«tevakku»."),
  cited("قَدْ", "qad", "part", ["mubtada-khabar", QD, K], "لَفْظٌ مَحْكِيٌّ — خَبَرٌ.", "«is qad».", "«kad'dir».", punct=":"),
  DAKHALAT(wa=False), DKH(), *ALA(), MADI(),
  AFADAT("أَفَادَتِ"),
  W("التَّحْقِيقَ", "tahqiq", "noun", ["maful-bihi", "form-ii-verbs"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«certainty».", "«tahkik»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«together with».", "«... ile beraber»."),
  W("التَّوَقُّعِ", "tawaqqu", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«expectation».", "«tevakku».", punct="،"),
  nahwu(),
  cited("قَدْ", "qad", "part", [QD, K], "حَرْفُ تَحْقِيقٍ وَتَوَقُّعٍ.", "«indeed».", "«(beklenen) gerçekten»."),
  cited("رَكِبَ", "rakiba", "verb", ["fail"], "فِعْلٌ مَاضٍ.", "«has mounted».", "«bindi»."),
  ZAYD(punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And it may convey, together with that, bringing the past near to the present — as your saying to one awaiting the amir's mounting: قَدْ رَكِبَ, «what you awaited has just now happened», and the muʾadhdhin's saying قَدْ قَامَتِ الصَّلَاةُ." + C_EN,
 "tr": "Bazen bununla beraber mâzîyi hâle yaklaştırma mânâsı da ifade eder — emîrin binmesini bekleyen kişiye قَدْ رَكِبَ demen gibi: «beklediğin iş şimdi oldu»; müezzinin قَدْ قَامَتِ الصَّلَاةُ sözü de böyledir." + C_TR},
 "tokens": [
  atf_wa("وَقَدْ", "qad", "part", [QD], "قَدْ لِلتَّقْلِيلِ مَعَ الْمُضَارِعِ.", "«and it may».", "«ve bazen».", "قَدْ"),
  W("تُفِيدُ", "afada", "verb", ["fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«convey».", "«ifade eder»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«together with».", "«... ile beraber»."),
  W("ذَلِكَ", "dhalika", "pron", ["idafa-definiteness", "asma-al-ishara-wal-mawsulat"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that».", "«bununla»."),
  W("تَقْرِيبَ", "taqrib", "noun", ["maful-bihi", "idafa-definiteness", "form-ii-verbs"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«bringing near».", "«yaklaştırma»."),
  W("الْمَاضِي", "madi", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the past».", "«mâzîyi»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الْحَالِ", "hal-noun", "noun", ["huruf-jarr"], "مَجْرُورٌ — زَمَنُ الْحَالِ.", "«the present».", "«hâle».", punct="،"),
  ka_("كَقَوْلِكَ", "qawl", "noun", ["idafa-definiteness"], "قَوْلِ مَجْرُورٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«as your saying».", "«demen gibi».", "قَوْلِ", segs=[seg("كَ", "ka", "prep"), seg("قَوْلِ", "qawl", "noun"), pr2ms()]),
  li_("لِمَنْ", "man", "pron", ["ism-mawsul", "asma-al-ishara-wal-mawsulat"], "مَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«to one who».", "«... kişiye».", "مَنْ"),
  W("يَنْتَظِرُ", "intazara", "verb", ["ism-mawsul", "fail", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ.", "«awaits».", "«bekleyen»."),
  W("رُكُوبَ", "rukub", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the mounting of».", "«binmesini»."),
  W("الْأَمِيرِ", "amir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the amir».", "«emîrin».", punct=":"),
  cited("قَدْ", "qad", "part", [QD, K], "حَرْفُ تَحْقِيقٍ — يُقَرِّبُ الْمَاضِيَ مِنَ الْحَالِ.", "«just now».", "«işte şimdi»."),
  cited("رَكِبَ", "rakiba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«he has mounted».", "«bindi».", punct="،"),
  atf_wa("وَكَقَوْلِ", "qawl", "noun", [AT, "idafa-definiteness"], "الْكَافُ حَرْفُ جَرٍّ، وَقَوْلِ مَجْرُورٌ مَعْطُوفٌ، وَهُوَ مُضَافٌ.", "«and as the saying of».", "«ve ... sözü gibi».", "قَوْلِ", extra_segs=[seg("كَ", "ka", "prep"), seg("قَوْلِ", "qawl", "noun")]),
  W("الْمُؤَذِّنِ", "muadhdhin", "noun", ["idafa-definiteness", "ism-fail", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the muʾadhdhin».", "«müezzinin».", punct=":"),
  cited("قَدْ", "qad", "part", [QD, K], "حَرْفُ تَحْقِيقٍ وَتَقْرِيبٍ.", "«now».", "«işte»."),
  cited("قَامَتِ", "qama", "verb", ["fail", "hollow-verbs", "al-fail-al-muzhar-wa-tanith-amilih"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«has begun».", "«başladı».", segments=[seg("قَامَ", "qama", "verb"), seg("تِ", "ta-tanith", "part")]),
  cited("الصَّلَاةُ", "salat", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the prayer».", "«namaz».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And when it enters on a muḍāriʿ it conveys certainty together with fewness — as إِنَّ الْكَذُوبَ قَدْ يَصْدُقُ, «even the habitual liar sometimes tells the truth»." + C_EN,
 "tr": "Muzârinin başında geldiğinde tahkik ile beraber taklil mânâsı ifade eder — إِنَّ الْكَذُوبَ قَدْ يَصْدُقُ gibi: «çok yalancı kişi de bazen doğru söyler»." + C_TR},
 "tokens": [
  DAKHALAT(), DKH(), *ALA(), MUDARI(),
  AFADAT("أَفَادَتِ"),
  W("التَّحْقِيقَ", "tahqiq", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«certainty».", "«tahkik»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«together with».", "«... ile beraber»."),
  W("التَّقْلِيلِ", "taqlil", "noun", ["idafa-definiteness", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«fewness».", "«taklil».", punct="،"),
  nahwu(),
  cited("إِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«indeed».", "«muhakkak»."),
  cited("الْكَذُوبَ", "kadhub", "noun", ["inna-wa-akhawatuha", "sighat-mubalagha"], "اسْمُ إِنَّ مَنْصُوبٌ — صِيغَةُ مُبَالَغَةٍ.", "«the habitual liar».", "«çok yalancı»."),
  cited("قَدْ", "qad", "part", [QD, K], "حَرْفُ تَحْقِيقٍ وَتَقْلِيلٍ مَعَ الْمُضَارِعِ.", "«sometimes».", "«bazen»."),
  cited("يَصْدُقُ", "sadaqa-verb", "verb", ["inna-wa-akhawatuha", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الْجُمْلَةُ خَبَرُ إِنَّ.", "«tells the truth».", "«doğru söyler».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And the two letters of question are the hamza and هَلْ; they come at the head of the sentence and enter on the verbal and the nominal sentence alike — as أَزَيْدٌ قَائِمٌ and هَلْ زَيْدٌ قَائِمٌ, and أَقَامَ زَيْدٌ and هَلْ قَامَ زَيْدٌ." + C_EN,
 "tr": "İki istifham harfi hemze ve هَلْ'dir; sözün başında gelirler ve fiil cümlesine de isim cümlesine de dahil olurlar — أَزَيْدٌ قَائِمٌ ve هَلْ زَيْدٌ قَائِمٌ, أَقَامَ زَيْدٌ ve هَلْ قَامَ زَيْدٌ gibi." + C_TR},
 "tokens": [
  atf_wa("وَحَرْفَا", "harf", "noun", ["mubtada-khabar", "idafa-definiteness", "al-muthanna"], "حَرْفَا مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«and the two letters of».", "«ve iki ... harfi».", "حَرْفَا"),
  W("الِاسْتِفْهَامِ", "istifham", "noun", ["idafa-definiteness", IS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«question».", "«istifham».", punct=":"),
  HAMZA_N("الْهَمْزَةُ", ["mubtada-khabar", IS, K], "خَبَرٌ مَرْفُوعٌ.", "«the hamza».", "«hemze»."),
  cited_wa("وَهَلْ", "hal-istifham", "part", [AT, IS, K], "هَلْ مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«and hal».", "«ve hel».", "هَلْ", punct="؛"),
  atf_wa("وَهُمَا", "pron-dual", "pron", ["mubtada-khabar"], "هُمَا مُبْتَدَأٌ.", "«and they».", "«ve onlar».", "هُمَا"),
  W("يَقَعَانِ", "waqaa", "verb", ["mubtada-khabar", "fail", "al-muthanna", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ — الْجُمْلَةُ خَبَرٌ.", "«come».", "«gelirler»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-de»."),
  W("صَدْرِ", "sadr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the head of».", "«başında»."),
  W("الْكَلَامِ", "kalam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sentence».", "«sözün».", punct="،"),
  atf_wa("وَيَدْخُلَانِ", "dakhala", "verb", ["fail", "al-muthanna"], "يَدْخُلَانِ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«and enter».", "«ve dahil olurlar».", "يَدْخُلَانِ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("الْجُمْلَةِ", "jumla", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the sentence».", "«cümlesine»."),
  W("الْفِعْلِيَّةِ", "filiyya", "noun", ["naat-sifa", "ism-mansub"], "صِفَةٌ مَجْرُورَةٌ.", "«verbal».", "«fiil»."),
  atf_wa("وَالِاسْمِيَّةِ", "ismiyya", "noun", [AT, "ism-mansub"], "الِاسْمِيَّةِ مَعْطُوفٌ مَجْرُورٌ.", "«and the nominal».", "«ve isim».", "الِاسْمِيَّةِ", punct="،"),
  nahwu(),
  cited("أَزَيْدٌ", "zayd", "propn", ["mubtada-khabar", IS], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَزَيْدٌ مُبْتَدَأٌ — جُمْلَةٌ اسْمِيَّةٌ.", "«is Zayd».", "«Zeyd ... mi».", segments=[seg("أَ", "hamza-istifham", "part"), seg("زَيْدٌ", "zayd", "propn")]),
  QAIM(punct="،"),
  HAL(),
  ZAYD(tags=("mubtada-khabar",), ar="مُبْتَدَأٌ مَرْفُوعٌ."),
  QAIM(punct="،"),
  cited("أَقَامَ", "qama", "verb", ["fail", "hollow-verbs", IS], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَقَامَ فِعْلٌ مَاضٍ — جُمْلَةٌ فِعْلِيَّةٌ.", "«did stand».", "«kalktı mı».", segments=[seg("أَ", "hamza-istifham", "part"), seg("قَامَ", "qama", "verb")]),
  ZAYD(punct="،"),
  HAL(),
  cited("قَامَ", "qama", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«did stand».", "«kalktı mı»."),
  ZAYD(punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And the use of the hamza is more general than that of هَلْ: the hamza enters on the noun though a verb is present — as أَزَيْدًا ضَرَبْتَ — while هَلْ زَيْدًا ضَرَبْتَ is not said." + C_EN,
 "tr": "Hemzenin kullanımı هَلْ'inkinden daha umumîdir: fiil bulunduğu hâlde hemze ismin üzerine dahil olur — أَزَيْدًا ضَرَبْتَ gibi; fakat هَلْ زَيْدًا ضَرَبْتَ denmez." + C_TR},
 "tokens": [
  atf_wa("وَاسْتِعْمَالُ", "istimal", "noun", ["mubtada-khabar", "idafa-definiteness", "form-x-verbs"], "اسْتِعْمَالُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the use of».", "«ve ... kullanımı».", "اسْتِعْمَالُ"),
  HAMZA_N("الْهَمْزَةِ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the hamza».", "«hemzenin»."),
  W("أَعَمُّ", "aamm", "noun", ["mubtada-khabar", "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«is more general».", "«daha umumîdir»."),
  W("مِنْ", "min", "prep", ["huruf-jarr", "ism-tafdil"], "حَرْفُ جَرٍّ.", "«than».", "«-den»."),
  cited("هَلْ", "hal-istifham", "part", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«hal».", "«hel».", punct=":"),
  W("فَتَدْخُلُ", "dakhala", "verb", ["fail", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَتَدْخُلُ فِعْلٌ مُضَارِعٌ.", "«so enters».", "«dahil olur».", segments=[seg("فَ", "fa", "conj"), seg("تَدْخُلُ", "dakhala", "verb")]),
  HAMZA_N("الْهَمْزَةُ", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the hamza».", "«hemze»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("الِاسْمِ", "ism", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the noun».", "«ismin»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness", "hal"], "ظَرْفٌ مَنْصُوبٌ — فِي مَوْضِعِ الْحَالِ، وَهُوَ مُضَافٌ.", "«though».", "«... hâlde»."),
  W("وُجُودِ", "wujud", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«there is».", "«bulunduğu»."),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb».", "«fiil».", punct="،"),
  nahwu(),
  cited("أَزَيْدًا", "zayd", "propn", ["maful-bihi", "taqdim-al-musnad", IS], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَزَيْدًا مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«was it Zayd».", "«Zeyd'i mi».", segments=[seg("أَ", "hamza-istifham", "part"), seg("زَيْدًا", "zayd", "propn")]),
  cited("ضَرَبْتَ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«you struck».", "«dövdün».", punct="،", segments=[seg("ضَرَبْ", "daraba", "verb"), prTa()]),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«fakat ... -mez».", "لَا"),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is said».", "«denmez».", punct=":"),
  HAL(ar="حَرْفُ اسْتِفْهَامٍ — لَا يَدْخُلُ عَلَى الِاسْمِ مَعَ وُجُودِ الْفِعْلِ."),
  cited("زَيْدًا", "zayd", "propn", ["maful-bihi", "taqdim-al-musnad"], "مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«Zayd».", "«Zeyd'i»."),
  cited("ضَرَبْتَ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«you struck».", "«dövdün».", punct=".", segments=[seg("ضَرَبْ", "daraba", "verb"), prTa()]),
 ]})

S.append({"id": "s8", "translation": {
 "en": "And the hamza is used to affirm what it enters on by way of denial, while هَلْ is not — as أَتَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ, «do you strike Zayd, when he is your brother?»." + C_EN,
 "tr": "Hemze, dahil olduğu şeyi inkâr yoluyla isbat için kullanılır, هَلْ kullanılmaz — أَتَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ gibi: «kardeşin olduğu hâlde Zeyd'i döver misin?»." + C_TR},
 "tokens": [
  atf_wa("وَتُسْتَعْمَلُ", "istamala", "verb", ["naib-al-fail", "form-x-verbs"], "تُسْتَعْمَلُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is used».", "«ve kullanılır».", "تُسْتَعْمَلُ"),
  HAMZA_N("الْهَمْزَةُ", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the hamza».", "«hemze»."),
  li_("لِإِثْبَاتِ", "ithbat", "noun", ["idafa-definiteness", "lam-taleel"], "إِثْبَاتِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«to affirm».", "«isbat için».", "إِثْبَاتِ"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "idafa-definiteness", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what».", "«... şeyi»."),
  W("دَخَلَتْ", "dakhala", "verb", ["ism-mawsul", "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — صِلَةٌ.", "«it enters».", "«dahil olduğu».", segments=[seg("دَخَلَ", "dakhala", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — عَائِدٌ.", "«on».", "«-e»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«by».", "«... yoluyla»."),
  W("وَجْهِ", "wajh", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«way of».", "«yolu»."),
  W("الْإِنْكَارِ", "inkar", "noun", ["idafa-definiteness", "form-iv-verbs", "khuruj-al-istifham"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«denial».", "«inkâr».", punct="،"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«while not».", "«... -maz».", "لَا"),
  W("تُسْتَعْمَلُ", "istamala", "verb", ["naib-al-fail", "form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is used».", "«kullanılmaz»."),
  cited("هَلْ", "hal-istifham", "part", ["naib-al-fail"], "نَائِبُ فَاعِلٍ — الْحَرْفُ مَحْكِيٌّ.", "«hal».", "«hel».", punct="،"),
  nahwu(),
  cited("أَتَضْرِبُ", "daraba", "verb", ["fail", IS, "khuruj-al-istifham"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَتَضْرِبُ فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«do you strike».", "«döver misin».", segments=[seg("أَ", "hamza-istifham", "part"), seg("تَضْرِبُ", "daraba", "verb")]),
  ZAYDAN(),
  atf_wa("وَهُوَ", "huwa", "pron", ["mubtada-khabar", "anwa-al-waw", "al-hal-jumla-wa-rabituha"], "الْوَاوُ حَالِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«when he».", "«... olduğu hâlde».", "هُوَ"),
  cited("أَخُوكَ", "akh", "noun", ["mubtada-khabar", "five-nouns", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«is your brother».", "«kardeşin».", punct=".", segments=[seg("أَخُو", "akh", "noun"), pr2ms()]),
 ]})

S.append({"id": "s9", "translation": {
 "en": "And the hamza is used opposite the joined أَمْ — as أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو — and هَلْ opposite the detached أَمْ — as هَلْ زَيْدٌ عِنْدَكَ أَمْ عَمْرٌو; and the hamza enters on ثُمَّ, the fāʾ and the wāw — أَثُمَّ إِذَا مَا وَقَعَ, أَفَمَنْ كَانَ, أَوَمَنْ كَانَ — while هَلْ does not." + C_EN,
 "tr": "Hemze muttasıl أَمْ mukabilinde kullanılır — أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو gibi; هَلْ ise munkatı أَمْ mukabilinde — هَلْ زَيْدٌ عِنْدَكَ أَمْ عَمْرٌو gibi; hemze ثُمَّ, fâ ve vâv üzerine dahil olur — أَثُمَّ إِذَا مَا وَقَعَ, أَفَمَنْ كَانَ, أَوَمَنْ كَانَ — هَلْ dahil olmaz." + C_TR},
 "tokens": [
  atf_wa("وَتُسْتَعْمَلُ", "istamala", "verb", ["naib-al-fail", "form-x-verbs"], "تُسْتَعْمَلُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is used».", "«ve kullanılır».", "تُسْتَعْمَلُ"),
  HAMZA_N("الْهَمْزَةُ", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the hamza».", "«hemze»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«opposite».", "«... mukabilinde»."),
  W("مُقَابَلَةِ", "muqabala", "noun", ["huruf-jarr", "idafa-definiteness", "form-iii-verbs"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«(the facing of)».", "«mukabil»."),
  cited("أَمِ", "am", "part", ["idafa-definiteness", AT], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«am».", "«em»."),
  W("الْمُتَّصِلَةِ", "muttasil", "noun", ["naat-sifa", "ism-fail", "form-viii-verbs"], "صِفَةٌ مَجْرُورَةٌ.", "«joined».", "«muttasıl».", punct="،"),
  nahwu(),
  cited("أَزَيْدٌ", "zayd", "propn", ["mubtada-khabar", IS], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَزَيْدٌ مُبْتَدَأٌ.", "«is Zayd».", "«Zeyd mi».", segments=[seg("أَ", "hamza-istifham", "part"), seg("زَيْدٌ", "zayd", "propn")]),
  cited("عِنْدَكَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ مَنْصُوبٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — خَبَرٌ.", "«with you».", "«yanında».", segments=[seg("عِنْدَ", "inda", "noun"), pr2ms()]),
  cited("أَمْ", "am", "part", [AT], "أَمِ الْمُتَّصِلَةُ.", "«or».", "«yoksa»."),
  cited("عَمْرٌو", "amr-name", "propn", [AT], "مَعْطُوفٌ مَرْفُوعٌ.", "«ʿAmr».", "«Amr».", punct="،"),
  cited_wa("وَهَلْ", "hal-istifham", "part", ["mubtada-khabar", IS, K], "هَلْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ — خَبَرُهُ مَحْذُوفٌ: تُسْتَعْمَلُ.", "«and hal».", "«hel ise».", "هَلْ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«opposite».", "«... mukabilinde»."),
  W("مُقَابَلَةِ", "muqabala", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«(the facing of)».", "«mukabil»."),
  cited("أَمِ", "am", "part", ["idafa-definiteness", AT], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«am».", "«em»."),
  W("الْمُنْقَطِعَةِ", "munqati", "noun", ["naat-sifa", "ism-fail", "form-vii-verbs"], "صِفَةٌ مَجْرُورَةٌ.", "«detached».", "«munkatı».", punct="،"),
  nahwu(),
  HAL(),
  ZAYD(tags=("mubtada-khabar",), ar="مُبْتَدَأٌ مَرْفُوعٌ."),
  cited("عِنْدَكَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ مَنْصُوبٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — خَبَرٌ.", "«with you».", "«yanında».", segments=[seg("عِنْدَ", "inda", "noun"), pr2ms()]),
  cited("أَمْ", "am", "part", [AT], "أَمِ الْمُنْقَطِعَةُ — بِمَعْنَى بَلْ وَالْهَمْزَةِ.", "«or rather».", "«yoksa»."),
  cited("عَمْرٌو", "amr-name", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ لِخَبَرٍ مَحْذُوفٍ: بَلْ أَعَمْرٌو عِنْدَكَ.", "«ʿAmr».", "«Amr mı».", punct="؛"),
  atf_wa("وَتَدْخُلُ", "dakhala", "verb", ["fail"], "تَدْخُلُ فِعْلٌ مُضَارِعٌ.", "«and enters».", "«ve dahil olur».", "تَدْخُلُ"),
  HAMZA_N("الْهَمْزَةُ", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the hamza».", "«hemze»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  cited("ثُمَّ", "thumma", "conj", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«thumma».", "«sümme»."),
  atf_wa("وَالْفَاءِ", "fa-letter", "noun", [AT], "الْفَاءِ مَعْطُوفٌ مَجْرُورٌ.", "«the fāʾ».", "«fâ».", "الْفَاءِ"),
  atf_wa("وَالْوَاوِ", "waw-letter", "noun", [AT], "الْوَاوِ مَعْطُوفٌ مَجْرُورٌ.", "«and the wāw».", "«ve vâv».", "الْوَاوِ", punct="،"),
  nahwu(),
  cited("أَثُمَّ", "thumma", "conj", [IS, AT, K], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَثُمَّ حَرْفُ عَطْفٍ.", "«is it then».", "«sonra mı».", segments=[seg("أَ", "hamza-istifham", "part"), seg("ثُمَّ", "thumma", "conj")]),
  cited("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«... zaman»."),
  cited("مَا", "ma-zaida", "part", ["majaz-ziyada-nuqsan", "anwa-ma"], "زَائِدَةٌ بَعْدَ إِذَا.", "«(-)».", "«(-)»."),
  cited("وَقَعَ", "waqaa", "verb", ["idha-shartiyya", "fail", "mithal-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — فِعْلُ الشَّرْطِ.", "«it has befallen».", "«vuku bulduğu».", punct="،"),
  cited("أَفَمَنْ", "man", "pron", [IS, AT, "mubtada-khabar", K], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَالْفَاءُ عَاطِفَةٌ، وَمَنْ اسْمٌ مَوْصُولٌ مُبْتَدَأٌ.", "«so is he who».", "«o hâlde ... olan mı».", segments=[seg("أَ", "hamza-istifham", "part"), seg("فَ", "fa", "conj"), seg("مَنْ", "man", "pron")]),
  cited("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "ism-mawsul", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ — صِلَةٌ.", "«was».", "«... olan».", punct="،"),
  cited("أَوَمَنْ", "man", "pron", [IS, AT, "mubtada-khabar", K], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَالْوَاوُ عَاطِفَةٌ، وَمَنْ اسْمٌ مَوْصُولٌ مُبْتَدَأٌ.", "«and is he who».", "«ve ... olan mı».", segments=[seg("أَ", "hamza-istifham", "part"), seg("وَ", "waw-atf", "conj"), seg("مَنْ", "man", "pron")]),
  cited("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "ism-mawsul", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ — صِلَةٌ.", "«was».", "«... olan».", punct="،"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«while not».", "«... -maz».", "لَا"),
  W("تَدْخُلُ", "dakhala", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ.", "«does enter».", "«dahil olmaz»."),
  cited("هَلْ", "hal-istifham", "part", ["fail"], "فَاعِلٌ — الْحَرْفُ مَحْكِيٌّ.", "«hal».", "«hel».", punct="."),
 ]})

def _nfc(o):
    if isinstance(o, str): return N(o)
    if isinstance(o, list): return [_nfc(x) for x in o]
    if isinstance(o, dict): return {k: _nfc(v) for k, v in o.items()}
    return o
S = _nfc(S)
for _s in S:
    for _t in _s["tokens"]: _t["surface"]["bare"] = bare(_t["surface"]["full"])

def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "tahdid": need("tahdid", "تَحْضِيض", "ح ض ض", "noun", "urging, incitement — the sense of هَلَّا، أَلَّا، لَوْلَا، لَوْمَا before a verb (masdar, Form II)", "tahdîd, teşvik — هَلَّا، أَلَّا، لَوْلَا، لَوْمَا'nın bir fiil önündeki mânâsı (tefʿîl masdarı)", 4),
 "alla-tahdid": need("alla-tahdid", "أَلَّا (التَّحْضِيض)", "أ ل ا", "part", "allā of urging — «why not …?» before a verb", "tahdîd ellâ'sı — bir fiil önünde «neden … -mezsin?»", 4),
 "lawma": need("lawma", "لَوْمَا", "ل و م ا", "part", "lawmā — a letter of urging, like لَوْلَا before a verb", "levmâ — fiil önünde لَوْلَا gibi bir tahdîd harfi", 4),
 "tawaqqu": need("tawaqqu", "تَوَقُّع", "و ق ع", "noun", "expectation — the sense قَدْ adds to a past verb (masdar, Form V)", "tevakku, bekleme — قَدْ'in mâzîye kattığı mânâ (tefeʿʿul masdarı)", 4),
 "tashwiq": need("tashwiq", "تَشْوِيق", "ش و ق", "noun", "urging, rousing a desire (masdar, Form II)", "teşvik, istek uyandırma (tefʿîl masdarı)", 3),
 "rukub": need("rukub", "رُكُوب", "ر ك ب", "noun", "mounting, riding (masdar of رَكِبَ)", "binme, binicilik (rekibe'nin masdarı)", 2),
 "lafz": need("lafz", "لَفْظ", "ل ف ظ", "noun", "wording, utterance", "lafız, söz", 2, plural="أَلْفَاظ"),
 "taqdir": need("taqdir", "تَقْدِير", "ق د ر", "noun", "estimation, assumption", "takdir, varsayım", 3),
}
_used = []
for _s in S:
    for _t in _s["tokens"]:
        _used.append(_t["lex"])
        for _g in (_t.get("segments") or []): _used.append(_g["lex"])
_MISSING = []
for k in sorted(set(_used)):
    if k in TG or k in CAND: continue
    try: CAND[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
GLOSS_ADD = {k: v for k, v in CAND.items() if v}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch38 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "حُرُوفُ التَّحْضِيضِ وَقَدْ وَحَرْفَا الِاسْتِفْهَامِ فِي الْكَافِيَةِ", "en": "The letters of urging, qad and the two question letters in the Kafiya: what each adds to a past and to a present verb, and the four places where the hamza goes and hal cannot", "tr": "Kâfiye'de tahdîd harfleri, kad ve iki istifham harfi: her birinin mâzîye ve muzâriye kattığı, hemzenin gidip hel'in gidemediği dört yer"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — حروف التحضيض هلا وألا ولولا ولوما؛ حرف التوقع قد؛ حرفا الاستفهام الهمزة وهل", "ضياء صونغور اوغلى — دفتر الكافية: التحضيض مع الماضي للتوبيخ ومع المضارع للأمر؛ قد مع الماضي للتحقيق والتوقع وتقريب الماضي من الحال ومع المضارع للتقليل؛ الهمزة أعم من هل في أربعة مواضع"],
 "question": {
  "en": ["What do the four letters of urging do? They demand a verb, stated or implied, and the verb's tense sets the sense: on a PAST verb هَلَّا نَصَرْتَ زَيْدًا reproaches you for not having helped and urges you to; on a PRESENT verb هَلَّا تَنْصُرُ زَيْدًا is a command dressed as urging. The tense after the letter decides, and the iʿrāb lines label the sentence accordingly.",
         "Is لَوْلَا here the same لَوْلَا as in لَوْلَا زَيْدٌ لَهَلَكَ عَمْرٌو? No. Before a NOUN it is the lawlā of imtināʿ (a mubtadaʾ with a dropped khabar follows); before a VERB it is a letter of urging. The word after it decides, and the hadhf engine's khabar-lawlā rule is restricted to the noun case for exactly this reason.",
         "What does قَدْ add to a past verb? Certainty with EXPECTATION — قَدْ رَكِبَ زَيْدٌ answers someone who was waiting for it — and so it also pulls the past up to the present: the muʾadhdhin's قَدْ قَامَتِ الصَّلَاةُ means «now». On a present verb it adds certainty with FEWNESS: إِنَّ الْكَذُوبَ قَدْ يَصْدُقُ, «sometimes».",
         "Where may both question letters go? At the head of a nominal or a verbal sentence alike: أَزَيْدٌ قَائِمٌ / هَلْ زَيْدٌ قَائِمٌ, أَقَامَ زَيْدٌ / هَلْ قَامَ زَيْدٌ.",
         "Where does the hamza go and هَلْ cannot? Four places: (1) on a fronted noun when a verb is present — أَزَيْدًا ضَرَبْتَ, never هَلْ زَيْدًا ضَرَبْتَ; (2) the denying question that affirms — أَتَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ; (3) facing the joined أَمْ — أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو, while هَلْ faces only the detached أَمْ; (4) before ثُمَّ, the fāʾ and the wāw — أَثُمَّ، أَفَمَنْ، أَوَمَنْ. The analyzer's particle table carries هَلْ; the iʿrāb lines here carry the four restrictions.",
         "Why does أَفَمَنْ put the hamza BEFORE the fāʾ? Because the question letter has the head of the sentence by right (ṣadr al-kalām) and the coordinator yields to it — the same precedence the Tartīb chapter lists among the obligatory orders."],
  "tr": ["Dört tahdîd harfi ne yapar? Lafzen ya da takdiren bir fiil ister ve fiilin zamanı mânâyı belirler: MÂZÎ üzerinde هَلَّا نَصَرْتَ زَيْدًا yardım etmediğin için seni kınar ve etmeye teşvik eder; MUZÂRİ üzerinde هَلَّا تَنْصُرُ زَيْدًا teşvik kılığında bir emirdir. Harften sonraki zaman karar verir; i'râb satırları cümleyi ona göre etiketler.",
         "Buradaki لَوْلَا, لَوْلَا زَيْدٌ لَهَلَكَ عَمْرٌو'daki لَوْلَا ile aynı mı? Hayır. İSİM önünde imtinâ levlâ'sıdır (haberi hazfedilmiş bir mübteda izler); FİİL önünde bir tahdîd harfidir. Sonraki kelime karar verir ve hazif motorunun haber-i levlâ kuralı tam bu sebeple isim hâliyle sınırlıdır.",
         "قَدْ mâzîye ne katar? BEKLENTİ ile tahkik — قَدْ رَكِبَ زَيْدٌ onu bekleyene cevaptır — ve bu yüzden mâzîyi hâle de çeker: müezzinin قَدْ قَامَتِ الصَّلَاةُ'si «şimdi» demektir. Muzâriye AZLIK ile tahkik katar: إِنَّ الْكَذُوبَ قَدْ يَصْدُقُ, «bazen».",
         "İki istifham harfi nereye gidebilir? İsim ya da fiil cümlesinin başına, ikisine de: أَزَيْدٌ قَائِمٌ / هَلْ زَيْدٌ قَائِمٌ, أَقَامَ زَيْدٌ / هَلْ قَامَ زَيْدٌ.",
         "Hemze nereye gider de هَلْ gidemez? Dört yer: (1) fiil varken öne alınmış isim üzerine — أَزَيْدًا ضَرَبْتَ, asla هَلْ زَيْدًا ضَرَبْتَ; (2) isbat eden inkârî soru — أَتَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ; (3) muttasıl أَمْ'in karşısında — أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو, هَلْ ise yalnız munkatı أَمْ'in karşısında; (4) ثُمَّ, fâ ve vâv'dan önce — أَثُمَّ، أَفَمَنْ، أَوَمَنْ. Analizörün harf tablosu هَلْ'i taşır; buradaki i'râb satırları dört kısıtı taşır.",
         "أَفَمَنْ hemzeyi niçin fâ'nın ÖNÜNE koyar? Çünkü istifham harfinin sözün başı (sadru'l-kelâm) hakkıdır ve atıf harfi ona yol verir — Tertîb bâbının vâcip sıralar arasında saydığı aynı öncelik."]},
 "plain": {
  "en": "Three small families. «Why don't you …?» words scold about the past and push toward the future. Qad before a past verb says «it really happened, as expected»; before a present verb, «sometimes». Both question words open a sentence, but only the hamza can sit on a fronted noun, deny, or face a real either-or.",
  "tr": "Üç küçük aile. «Neden … -mezsin?» kelimeleri geçmiş için azarlar, gelecek için iter. Mâzî önünde kad «beklendiği gibi gerçekten oldu», muzâri önünde «bazen» der. İki soru kelimesi de cümle açar; ama yalnız hemze öne alınmış ismin üstüne oturur, inkâr eder ve gerçek bir ya-ya da'nın karşısına geçer."},
 "explanation": {
  "en": "Three particle families that the Kafiya lists in a line each and the notebook unfolds by the TENSE of the verb they precede. For the letters of urging and for قَدْ the pattern is the same: the letter's sense is fixed by whether a māḍī or a muḍāriʿ follows, which is a surface fact the analyzer can read. The notebook's worked example for قَدْ — the man waiting for the amir to mount, and the muʾadhdhin — gives the taqrīb sense a scene, and the chapter keeps it. The question letters are set side by side in the four places the notebook names, each with its pair of sentences, one admitted and one refused; the refusals are the lesson, and the iʿrāb lines state them. The hamza's precedence over the coordinators (أَفَمَنْ) ties this chapter to the Tartīb engine's list of obligatory orders.",
  "tr": "Kâfiye'nin birer satırla saydığı, defterin ise önlerine geldikleri fiilin ZAMANIYLA açtığı üç harf ailesi. Tahdîd harfleri ve قَدْ için kalıp aynıdır: harfin mânâsını ardından mâzî mi muzâri mi geldiği belirler; bu, analizörün okuyabileceği bir yüzey olgusudur. Defterin قَدْ için yürüttüğü örnek — emîrin binmesini bekleyen adam ve müezzin — takrîb mânâsına bir sahne verir ve bâb onu korur. İstifham harfleri defterin adlandırdığı dört yerde, biri kabul biri ret edilen cümle çiftleriyle yan yana konur; retler derstir ve i'râb satırları onları söyler. Hemzenin atıf harflerine önceliği (أَفَمَنْ) bu bâbı Tertîb motorunun vâcip sıralar listesine bağlar."},
 "examples": [
  {"ar": "هَلَّا نَصَرْتَ زَيْدًا — هَلَّا تَنْصُرُ زَيْدًا", "en": "Urging: reproach on a past verb, command on a present one.", "tr": "Tahdîd: mâzîde kınama, muzâride emir.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "قَدْ رَكِبَ زَيْدٌ — قَدْ قَامَتِ الصَّلَاةُ", "en": "Qad: certainty, expectation, nearness to the present.", "tr": "Kad: tahkik, tevakku, hâle yakınlık.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "إِنَّ الْكَذُوبَ قَدْ يَصْدُقُ", "en": "Qad on a present verb: sometimes.", "tr": "Muzâri önünde kad: bazen.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "أَزَيْدًا ضَرَبْتَ — لَا: هَلْ زَيْدًا ضَرَبْتَ", "en": "The hamza on a fronted noun; hal refused.", "tr": "Öne alınmış isimde hemze; hel reddedilir.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "أَتَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ", "en": "The denying question that affirms.", "tr": "İsbat eden inkârî soru.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "أَثُمَّ إِذَا مَا وَقَعَ — أَفَمَنْ كَانَ — أَوَمَنْ كَانَ", "en": "The hamza before thumma, the fāʾ and the wāw.", "tr": "Sümme, fâ ve vâv'dan önce hemze.", "sourceStory": "al-kafiya", "sentence": "s9"}],
 "commonMistakes": [
  {"wrong": "«هَلْ زَيْدًا ضَرَبْتَ؟»",
   "right": "«أَزَيْدًا ضَرَبْتَ؟ — fiil varken öne alınmış ismin üstüne yalnız hemze gelir»",
   "why": {"en": "Hal cannot sit on a fronted noun when a verb is present.", "tr": "Fiil varken hel öne alınmış ismin üstüne oturamaz."}},
  {"wrong": "«هَلْ زَيْدٌ عِنْدَكَ أَمْ عَمْرٌو — muttasıl em»",
   "right": "«hel'den sonraki em munkatıdır; muttasıl em'in önüne hemze gelir»",
   "why": {"en": "The joined am needs the hamza, not hal.", "tr": "Muttasıl em hemze ister, hel değil."}},
  {"wrong": "«فَأَمَنْ كَانَ»",
   "right": "«أَفَمَنْ كَانَ — hemze sadru'l-kelâmdır, fâ ona yol verir»",
   "why": {"en": "The question letter takes the head of the sentence; the coordinator follows it.", "tr": "İstifham harfi sözün başını alır; atıf harfi onu izler."}},
  {"wrong": "«قَدْ يَصْدُقُ = kesinlikle doğru söyler»",
   "right": "«bazen doğru söyler — muzâri önünde kad taklil içindir»",
   "why": {"en": "On a present verb qad adds fewness, not emphasis.", "tr": "Muzâri önünde kad te'kid değil azlık katar."}}],
 "relatedNotes": ["al-istifham", "khuruj-al-istifham", "qad-harf", "aw-imma-am-la-bal-lakin-fil-kafiya", "insha-wa-tamanni"]}

ADD_EN = (" Chapter 40 (notebook line ~346): the letters of urging (sense by the tense that follows), qad (certainty and expectation on a past verb, with the amir and the muʾadhdhin; fewness on a present one) and the two question letters with the four places the hamza alone may take — the notebook's exposition, kept as commentary (s1-s9).")
ADD_TR = (" Kırkıncı bâb (defter satırı ~346): tahdîd harfleri (mânâ ardından gelen zamanla), kad (mâzîde tahkik ve tevakku, emîr ve müezzin örnekleriyle; muzâride taklil) ve yalnız hemzenin alabildiği dört yerle iki istifham harfi — defterin açıklaması, şerh olarak (s1-s9).")
write_out(40, S, TITLE, ADD_EN, ADD_TR, "346", GLOSS_ADD, notes=(NOTE,),
          related=(("al-istifham", [K]), ("qad-harf", [K])))
report(40, S, GLOSS_ADD, (NOTE,))
