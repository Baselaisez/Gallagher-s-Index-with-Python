# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 20: THE VERB — its definition, its marks (قَدْ، السِّين، سَوْفَ، the jāzims, the quiescent tāʾ, the attached raised
pronouns), what قَدْ and the two future particles mean; THE MĀḌĪ defined and built (fatḥa — written or estimated —, sukūn with a vowelled
raised pronoun, ḍamma with the wāw); THE MUḌĀRIʿ defined by نَأَيْتَ, why it resembles the noun, the four letters and whom they stand for,
the prefix vowel (ḍamma in the four-lettered, fatḥa elsewhere), the only verb that declines and its three cases with their signs.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~283-296 of the transcription.

  VERBATIM: s1, s4, s6. RESTORED (received matn, marked): s2, s5, s9, s10. COMMENTARY (the notebook): s3, s7, s8, s11.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch20.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-fil-wal-madi-wal-mudari-fil-kafiya"
NJ = "nawasib-wa-jawazim-al-mudari"
TITLE = {"ar": "الْفِعْلُ: الْمَاضِي وَالْمُضَارِعُ", "en": "The verb: the māḍī and the muḍāriʿ", "tr": "Fiil: mâzî ve muzâri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
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
def form(full, lex, en, tr, ar="صِيغَةٌ مَحْكِيَّةٌ.", first=False, punct=None, tags=()):
    t = ["idafa-definiteness"] if first else []
    return (cited(full, lex, "verb", t + list(tags), ("فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — " if first else "مَعْطُوفٌ — ") + ar, en, tr, punct=punct) if first
            else cited_wa("وَ" + full, lex, "verb", list(tags), full + " مَعْطُوفٌ — " + ar, en, tr, full, punct=punct))

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The verb: what signifies a meaning in itself, joined to one of the three times.",
 "tr": "Fiil: üç zamandan birine yakın (bitişik) olan, kendi nefsinde bulunan bir mânâya delâlet eden kelimedir."},
 "tokens": [
  W("الْفِعْلُ", "fil", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the verb» — the mubtada.", "«fiil» — mübtedâ.", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the khabar.", "«... olan» — haber."),
  W("دَلَّ", "dalla", "verb", ["ism-mawsul", "fail", "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«signifies».", "«delâlet eden»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«a».", "«-e»."),
  W("مَعْنًى", "mana", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«meaning».", "«mânâ»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("نَفْسِهِ", "nafs", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِفَةٌ لِمَعْنًى.", "«itself» — unlike a particle.", "«kendi nefsinde» — harfin aksine.", segments=[seg("نَفْسِ", "nafs", "noun"), pr3msi()]),
  W("مُقْتَرِنٍ", "muqtarin", "noun", ["naat-sifa", "ism-fail", "form-viii-verbs"], "صِفَةٌ ثَانِيَةٌ لِمَعْنًى مَجْرُورَةٌ.", "«joined» — unlike a noun.", "«bitişik» — ismin aksine."),
  bi_("بِأَحَدِ", "ahad", "noun", ["idafa-definiteness"], "أَحَدِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«to one of».", "«birine».", "أَحَدِ"),
  W("الْأَزْمِنَةِ", "zaman", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ زَمَانٍ.", "«the times».", "«zamanlardan»."),
  W("الثَّلَاثَةِ", "thalatha", "noun", ["naat-sifa", "asma-al-adad-fil-kafiya"], "صِفَةٌ مَجْرُورَةٌ.", "«three».", "«üç».", punct="."),
 ]})

# ----------- s2 (RESTORED): the marks
S.append({"id": "s2", "translation": {
 "en": "And among its marks are the entry of قَدْ, the sīn, سَوْفَ and the jāzims, and the attachment of the quiescent tāʾ of the feminine, as فَعَلَتْ, and of the raised, apparent, attached pronouns, as فَعَلْتَ." + R_EN,
 "tr": "Hâssalarından: قَدْ, sîn, سَوْفَ ve cezm edicilerin dâhil olması; sâkin te'nîs tâsının, فَعَلَتْ gibi, ve merfû bâriz muttasıl zamirlerin, فَعَلْتَ gibi, bitişmesi." + R_TR},
 "tokens": [
  atf_wa("وَمِنْ", "min", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "مِنْ حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and among».", "«ve ... -den».", "مِنْ"),
  W("خَوَاصِّهِ", "khassa", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ خَاصَّةٍ.", "«its marks».", "«hâssalarından».", segments=[seg("خَوَاصِّ", "khassa", "noun"), pr3msi()]),
  W("دُخُولُ", "dukhul", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the entry of».", "«dâhil olması»."),
  cited("قَدْ", "qad", "part", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«qad».", "«kad»."),
  cited_wa("وَالسِّينِ", "sin-letter", "noun", [], "السِّينِ مَعْطُوفٌ مَجْرُورٌ.", "«the sīn».", "«sîn».", "السِّينِ"),
  cited_wa("وَسَوْفَ", "sawfa", "part", [], "سَوْفَ مَعْطُوفٌ.", "«sawfa».", "«sevfe».", "سَوْفَ"),
  atf_wa("وَالْجَوَازِمِ", "jazim", "noun", [NJ, "jam-taksir"], "الْجَوَازِمِ مَعْطُوفٌ مَجْرُورٌ.", "«and the jāzims».", "«ve cezm ediciler».", "الْجَوَازِمِ", punct="،"),
  atf_wa("وَلُحُوقُ", "luhuq", "noun", ["mubtada-khabar", "idafa-definiteness"], "لُحُوقُ مَعْطُوفٌ عَلَى دُخُولُ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the attachment of».", "«ve bitişmesi».", "لُحُوقُ"),
  W("تَاءِ", "ta-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the tāʾ of».", "«tâsının»."),
  W("التَّأْنِيثِ", "tanith", "noun", ["idafa-definiteness", "al-muannath-wa-alamatuh"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine».", "«te'nîs»."),
  W("السَّاكِنَةِ", "sakin", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«quiescent».", "«sâkin»."),
  nahwu(),
  cited("فَعَلَتْ", "faala", "verb", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ — فِعْلٌ مَاضٍ وَتَاءُ التَّأْنِيثِ السَّاكِنَةُ.", "«she did».", "«o (kadın) yaptı».", punct="،", segments=[seg("فَعَلَ", "faala", "verb"), seg("تْ", "ta-tanith", "part")]),
  atf_wa("وَالضَّمَائِرِ", "damir", "noun", ["idafa-definiteness", "jam-taksir"], "الضَّمَائِرِ مَعْطُوفٌ عَلَى تَاءِ مَجْرُورٌ.", "«and the pronouns».", "«ve zamirlerin».", "الضَّمَائِرِ"),
  W("الْمَرْفُوعَةِ", "marfu", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«raised».", "«merfû»."),
  W("الْبَارِزَةِ", "bariz", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«apparent».", "«bâriz»."),
  W("الْمُتَّصِلَةِ", "muttasil", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«attached».", "«muttasıl»."),
  nahwu(),
  cited("فَعَلْتَ", "faala", "verb", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ — فِعْلٌ مَاضٍ وَالتَّاءُ فَاعِلٌ.", "«you did».", "«yaptın».", punct=".", segments=[seg("فَعَلْ", "faala", "verb"), seg("تَ", "pron-2ms", "pron")]),
 ]})

# ----------- s3 (COMMENTARY): the particles' meanings
S.append({"id": "s3", "translation": {
 "en": "And قَدْ with the māḍī is for confirmation, as قَدْ صَدَقَ, and with the muḍāriʿ for rarity, as إِنَّ الْكَذُوبَ قَدْ يَصْدُقُ; and the sīn is for the near future, as سَيَأْتِي زَيْدٌ, and سَوْفَ for the far, as سَوْفَ يَأْتِي زَيْدٌ." + C_EN,
 "tr": "قَدْ mâzî ile tahkîk içindir, قَدْ صَدَقَ gibi; muzâri ile taklîl içindir, إِنَّ الْكَذُوبَ قَدْ يَصْدُقُ gibi; sîn yakın istikbâl içindir, سَيَأْتِي زَيْدٌ gibi; سَوْفَ uzak istikbâl içindir, سَوْفَ يَأْتِي زَيْدٌ gibi." + C_TR},
 "tokens": [
  cited_wa("وَقَدْ", "qad", "part", ["mubtada-khabar"], "قَدْ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and qad».", "«ve kad».", "قَدْ"),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  W("الْمَاضِي", "madi", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the māḍī».", "«mâzî»."),
  li_("لِلتَّحْقِيقِ", "tahqiq", "noun", ["mubtada-khabar"], "التَّحْقِيقِ مَجْرُورٌ — خَبَرٌ.", "«is for confirmation».", "«tahkîk içindir».", "التَّحْقِيقِ", segs=[seg("لِ", "li", "prep"), seg("لتَّحْقِيقِ", "tahqiq", "noun")]),
  nahwu(),
  cited("قَدْ", "qad", "part", ["idafa-definiteness"], "حَرْفُ تَحْقِيقٍ.", "«indeed».", "«muhakkak»."),
  cited("صَدَقَ", "sadaqa-be-true", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«he spoke truly».", "«doğru söyledi».", punct="،"),
  atf_wa("وَمَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "مَعَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and with».", "«ve ... ile».", "مَعَ"),
  W("الْمُضَارِعِ", "mudari", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the muḍāriʿ».", "«muzâri»."),
  li_("لِلتَّقْلِيلِ", "taqlil", "noun", ["mubtada-khabar"], "التَّقْلِيلِ مَجْرُورٌ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«for rarity».", "«taklîl içindir».", "التَّقْلِيلِ", segs=[seg("لِ", "li", "prep"), seg("لتَّقْلِيلِ", "taqlil", "noun")]),
  nahwu(),
  cited("إِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«indeed».", "«muhakkak»."),
  cited("الْكَذُوبَ", "kadhub", "noun", ["inna-wa-akhawatuha", "sighat-mubalagha"], "اسْمُ إِنَّ مَنْصُوبٌ — فَعُولٌ لِلْمُبَالَغَةِ.", "«the habitual liar».", "«çok yalancı»."),
  cited("قَدْ", "qad", "part", [], "حَرْفُ تَقْلِيلٍ.", "«sometimes».", "«bazen»."),
  cited("يَصْدُقُ", "sadaqa-be-true", "verb", ["inna-wa-akhawatuha", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«speaks truly».", "«doğru söyler».", punct="؛"),
  cited_wa("وَالسِّينُ", "sin-letter", "noun", ["mubtada-khabar"], "السِّينُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the sīn».", "«ve sîn».", "السِّينُ"),
  li_("لِلِاسْتِقْبَالِ", "istiqbal", "noun", ["mubtada-khabar"], "الِاسْتِقْبَالِ مَجْرُورٌ — خَبَرٌ.", "«is for the future».", "«istikbâl içindir».", "الِاسْتِقْبَالِ", segs=[seg("لِ", "li", "prep"), seg("لِاسْتِقْبَالِ", "istiqbal", "noun")]),
  W("الْقَرِيبِ", "qarib", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«near».", "«yakın»."),
  nahwu(),
  cited("سَيَأْتِي", "ata", "verb", ["fail", "ism-maqsur-manqus"], "السِّينُ لِلِاسْتِقْبَالِ، وَيَأْتِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«will come (soon)».", "«yakında gelir».", segments=[seg("سَ", "sin-letter", "part"), seg("يَأْتِي", "ata", "verb")]),
  cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd».", punct="،"),
  cited_wa("وَسَوْفَ", "sawfa", "part", ["mubtada-khabar"], "سَوْفَ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and sawfa».", "«ve sevfe».", "سَوْفَ"),
  li_("لِلْبَعِيدِ", "baid", "noun", ["mubtada-khabar"], "الْبَعِيدِ مَجْرُورٌ — خَبَرٌ.", "«for the far».", "«uzak için».", "الْبَعِيدِ", segs=[seg("لِ", "li", "prep"), seg("لْبَعِيدِ", "baid", "noun")]),
  nahwu(),
  cited("سَوْفَ", "sawfa", "part", [], "حَرْفُ اسْتِقْبَالٍ.", "«will (later)».", "«ileride»."),
  cited("يَأْتِي", "ata", "verb", ["fail", "ism-maqsur-manqus"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«come».", "«gelir»."),
  cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd».", punct="."),
 ]})

# ----------- s4 (VERBATIM): the māḍī
S.append({"id": "s4", "translation": {
 "en": "The māḍī: what signifies a time before your time.",
 "tr": "Mâzî: içinde bulunduğun zamandan önceki bir zamana delâlet edendir."},
 "tokens": [
  W("الْمَاضِي", "madi", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the māḍī».", "«mâzî».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("دَلَّ", "dalla", "verb", ["ism-mawsul", "fail", "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«signifies».", "«delâlet eden»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«a».", "«-e»."),
  W("زَمَانٍ", "zaman", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«time».", "«zaman»."),
  W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness", "naat-sifa"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — صِفَةٌ لِزَمَانٍ.", "«before».", "«önceki»."),
  W("زَمَانِكَ", "zaman", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — زَمَانُ التَّكَلُّمِ.", "«your time» — the moment of speaking.", "«senin zamanından» — konuşma ânı.", punct=".", segments=[seg("زَمَانِ", "zaman", "noun"), seg("كَ", "pron-2ms", "pron")]),
 ]})

# ----------- s5 (RESTORED): its bināʾ
S.append({"id": "s5", "translation": {
 "en": "And it is built on the fatḥa, written — as ضَرَبَ، ضَرَبَا، ضَرَبَتْ، ضَرَبَتَا — or estimated, as رَمَى; on the sukūn with a vowelled raised pronoun, as ضَرَبْتُ، ضَرَبْنَ، ضَرَبْنَا; and on the ḍamma with the wāw, as ضَرَبُوا." + R_EN,
 "tr": "Fetha üzere mebnîdir — lafzan, ضَرَبَ، ضَرَبَا، ضَرَبَتْ، ضَرَبَتَا gibi; takdîren, رَمَى gibi — harekeli merfû zamirle sükûn üzere, ضَرَبْتُ، ضَرَبْنَ، ضَرَبْنَا gibi; vâv ile zamme üzere, ضَرَبُوا gibi." + R_TR},
 "tokens": [
  atf_wa("وَهُوَ", "huwa", "pron", ["mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هُوَ"),
  W("مَبْنِيٌّ", "mabni", "noun", ["mubtada-khabar", "al-mabni-wal-mudmar"], "خَبَرٌ مَرْفُوعٌ.", "«is built».", "«mebnîdir»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  W("الْفَتْحِ", "fath", "noun", ["huruf-jarr", "al-mabni-wal-mudmar"], "مَجْرُورٌ.", "«the fatḥa».", "«fetha»."),
  W("لَفْظًا", "lafz", "noun", ["hal"], "حَالٌ مَنْصُوبٌ، أَوْ تَمْيِيزٌ.", "«written».", "«lafzan»."),
  nahwu(),
  form("ضَرَبَ", "daraba", "«he struck».", "«vurdu».", first=True),
  form("ضَرَبَا", "daraba", "«they two struck».", "«o ikisi vurdu»."),
  form("ضَرَبَتْ", "daraba", "«she struck».", "«o (kadın) vurdu»."),
  form("ضَرَبَتَا", "daraba", "«they two (f.) struck».", "«o iki kadın vurdu».", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("تَقْدِيرًا", "taqdir", "noun", ["hal", "atf-nasaq"], "مَعْطُوفٌ عَلَى لَفْظًا مَنْصُوبٌ.", "«estimated».", "«takdîren»."),
  nahwu(),
  cited("رَمَى", "rama", "verb", ["idafa-definiteness", "ism-maqsur-manqus"], "فِي مَحَلِّ جَرٍّ — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«he threw» — the fatḥa estimated on the alif.", "«attı» — fetha elif üzerinde mukadder.", punct="؛"),
  atf_wa("وَعَلَى", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ — مَعْطُوفٌ عَلَى عَلَى الْفَتْحِ.", "«and on».", "«ve ... üzere».", "عَلَى"),
  W("السُّكُونِ", "sukun", "noun", ["huruf-jarr", "al-mabni-wal-mudmar"], "مَجْرُورٌ.", "«the sukūn».", "«sükûn»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  W("الضَّمِيرِ", "damir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the pronoun».", "«zamir»."),
  W("الْمَرْفُوعِ", "marfu", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«raised».", "«merfû»."),
  W("الْمُتَحَرِّكِ", "mutaharrik", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«vowelled».", "«harekeli»."),
  nahwu(),
  form("ضَرَبْتُ", "daraba", "«I struck».", "«vurdum».", first=True),
  form("ضَرَبْنَ", "daraba", "«they (f.) struck».", "«o kadınlar vurdu»."),
  form("ضَرَبْنَا", "daraba", "«we struck».", "«vurduk».", punct="؛"),
  atf_wa("وَعَلَى", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ.", "«and on».", "«ve ... üzere».", "عَلَى"),
  W("الضَّمِّ", "damm", "noun", ["huruf-jarr", "al-mabni-wal-mudmar"], "مَجْرُورٌ.", "«the ḍamma».", "«zamme»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  W("الْوَاوِ", "waw-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَاوُ الْجَمَاعَةِ.", "«the wāw».", "«vâv»."),
  nahwu(),
  form("ضَرَبُوا", "daraba", "«they struck».", "«vurdular».", first=True, punct="."),
 ]})

# ----------- s6 (VERBATIM): the muḍāriʿ
S.append({"id": "s6", "translation": {
 "en": "The muḍāriʿ: what resembles the noun by one of the letters of نَأَيْتَ.",
 "tr": "Muzâri: نَأَيْتَ harflerinden biriyle isme benzeyendir."},
 "tokens": [
  W("الْمُضَارِعُ", "mudari", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the muḍāriʿ».", "«muzâri».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("أَشْبَهَ", "ashbaha", "verb", ["ism-mawsul", "fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«resembles».", "«benzeyen»."),
  W("الِاسْمَ", "ism", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the noun».", "«isme»."),
  bi_("بِأَحَدِ", "ahad", "noun", ["idafa-definiteness"], "أَحَدِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by one of».", "«biriyle».", "أَحَدِ"),
  W("حُرُوفِ", "harf", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the letters of».", "«harflerinden»."),
  cited("نَأَيْتَ", "nayta", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — كَلِمَةٌ تَجْمَعُ حُرُوفَ الْمُضَارَعَةِ: ن أ ي ت.", "«naʾayta» — the four prefix letters in one word.", "«ne'eyte» — dört muzâraat harfi tek kelimede.", punct="."),
 ]})

# ----------- s7 (COMMENTARY): why it resembles the noun
S.append({"id": "s7", "translation": {
 "en": "And it resembles the noun because it is shared between the present and the future, as the noun is shared among meanings; and it is made specific to the future by the sīn and سَوْفَ." + C_EN,
 "tr": "İsme benzer, çünkü isim mânâlar arasında müşterek olduğu gibi o da hâl ile istikbâl arasında müşterektir; sîn ve سَوْفَ ile istikbâle tahsîs edilir." + C_TR},
 "tokens": [
  atf_wa("وَإِنَّمَا", "innama", "part", ["qasr"], "إِنَّمَا أَدَاةُ حَصْرٍ.", "«and only».", "«ve ancak».", "إِنَّمَا"),
  W("أَشْبَهَ", "ashbaha", "verb", ["fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«it resembles».", "«benzer»."),
  W("الِاسْمَ", "ism", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the noun».", "«isme»."),
  W("لِأَنَّهُ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا.", "«because it».", "«çünkü o».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3ms()]),
  W("مُشْتَرَكٌ", "mushtarak", "noun", ["inna-wa-akhawatuha", "ism-maful"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is shared».", "«müşterektir»."),
  W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«between».", "«arasında»."),
  W("الْحَالِ", "hal-state", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the present».", "«hâl»."),
  atf_wa("وَالِاسْتِقْبَالِ", "istiqbal", "noun", [], "الِاسْتِقْبَالِ مَعْطُوفٌ مَجْرُورٌ.", "«and the future».", "«ve istikbâl».", "الِاسْتِقْبَالِ"),
  W("كَمَا", "kama", "part", ["huruf-jarr"], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ.", "«as».", "«... gibi».", segments=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  W("أَنَّ", "anna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«that».", "«-dığı»."),
  W("الِاسْمَ", "ism", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the noun».", "«isim»."),
  W("مُشْتَرَكٌ", "mushtarak", "noun", ["inna-wa-akhawatuha", "ism-maful"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is shared».", "«müşterektir»."),
  W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«among».", "«arasında»."),
  W("مَعَانٍ", "mana", "noun", ["idafa-definiteness", "ism-maqsur-manqus", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِفَتْحَةٍ مُقَدَّرَةٍ — صِيغَةُ مُنْتَهَى الْجُمُوعِ الْمَنْقُوصَةُ، تَنْوِينُهُ لِلْعِوَضِ.", "«meanings» — the tanwīn of compensation.", "«mânâlar» — ivaz tenvini.", punct="؛"),
  atf_wa("وَتَخْصِيصُهُ", "takhsis", "noun", ["mubtada-khabar", "idafa-definiteness"], "تَخْصِيصُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its specification».", "«ve tahsîsi».", "تَخْصِيصُ", extra_segs=[seg("تَخْصِيصُ", "takhsis", "noun"), pr3ms()]),
  li_("لِلِاسْتِقْبَالِ", "istiqbal", "noun", [], "الِاسْتِقْبَالِ مَجْرُورٌ.", "«to the future».", "«istikbâle».", "الِاسْتِقْبَالِ", segs=[seg("لِ", "li", "prep"), seg("لِاسْتِقْبَالِ", "istiqbal", "noun")]),
  bi_("بِالسِّينِ", "sin-letter", "noun", ["mubtada-khabar"], "السِّينِ مَجْرُورٌ — خَبَرٌ.", "«is by the sīn».", "«sîn ile».", "السِّينِ"),
  cited_wa("وَسَوْفَ", "sawfa", "part", [], "سَوْفَ مَعْطُوفٌ.", "«and sawfa».", "«ve sevfe».", "سَوْفَ", punct="."),
 ]})

# ----------- s8 (COMMENTARY): the four letters
S.append({"id": "s8", "translation": {
 "en": "So the hamza is for the speaker alone, as أَضْرِبُ; the nūn for him with others, as نَضْرِبُ; the tāʾ for the addressee without restriction and for the absent feminine and her dual, as تَضْرِبُ; and the yāʾ for what remains of the absent." + C_EN,
 "tr": "Hemze yalnız mütekellim içindir, أَضْرِبُ gibi; nûn başkalarıyla birlikte onun içindir, نَضْرِبُ gibi; tâ mutlak olarak muhâtab ve gâibe ile tesniyesi içindir, تَضْرِبُ gibi; yâ gâibden geri kalanlar içindir." + C_TR},
 "tokens": [
  W("فَالْهَمْزَةُ", "hamza-letter", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْهَمْزَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the hamza».", "«hemze».", segments=[seg("فَ", "fa", "conj"), seg("الْهَمْزَةُ", "hamza-letter", "noun")]),
  li_("لِلْمُتَكَلِّمِ", "mutakallim", "noun", ["mubtada-khabar"], "الْمُتَكَلِّمِ مَجْرُورٌ — خَبَرٌ.", "«is for the speaker».", "«mütekellim içindir».", "الْمُتَكَلِّمِ", segs=[seg("لِ", "li", "prep"), seg("لْمُتَكَلِّمِ", "mutakallim", "noun")]),
  W("وَحْدَهُ", "wahda", "noun", ["hal", "idafa-definiteness"], "حَالٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«alone».", "«yalnız».", segments=[seg("وَحْدَ", "wahda", "noun"), pr3ms()]),
  nahwu(),
  cited("أَضْرِبُ", "daraba", "verb", ["idafa-definiteness", "fail"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I strike».", "«vururum».", punct="؛"),
  atf_wa("وَالنُّونُ", "nun-letter", "noun", ["mubtada-khabar"], "النُّونُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the nūn».", "«ve nûn».", "النُّونُ"),
  li_("لَهُ", "li", "prep", ["mubtada-khabar"], "الْهَاءُ مَجْرُورٌ — خَبَرٌ.", "«for him».", "«onun için».", "هُ", segs=[seg("لَ", "li", "prep"), pr3ms()]),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  W("غَيْرِهِ", "ghayr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«others».", "«başkaları».", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  nahwu(),
  cited("نَضْرِبُ", "daraba", "verb", ["idafa-definiteness", "fail"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«we strike».", "«vururuz».", punct="؛"),
  atf_wa("وَالتَّاءُ", "ta-letter", "noun", ["mubtada-khabar"], "التَّاءُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the tāʾ».", "«ve tâ».", "التَّاءُ"),
  li_("لِلْمُخَاطَبِ", "mukhatab", "noun", ["mubtada-khabar"], "الْمُخَاطَبِ مَجْرُورٌ — خَبَرٌ.", "«is for the addressee».", "«muhâtab içindir».", "الْمُخَاطَبِ", segs=[seg("لِ", "li", "prep"), seg("لْمُخَاطَبِ", "mukhatab", "noun")]),
  W("مُطْلَقًا", "mutlaqan", "noun", ["hal"], "حَالٌ مَنْصُوبٌ — مُفْرَدًا وَمُثَنًّى وَمَجْمُوعًا، مُذَكَّرًا وَمُؤَنَّثًا.", "«without restriction».", "«mutlak olarak»."),
  atf_wa("وَلِلْغَائِبَةِ", "ghaib", "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْغَائِبَةِ مَجْرُورٌ.", "«and for the absent feminine».", "«ve gâibe için».", "لِ", extra_segs=[seg("لِ", "li", "prep"), seg("لْغَائِبَةِ", "ghaib", "noun")]),
  atf_wa("وَمُثَنَّاهَا", "muthanna", "noun", ["idafa-definiteness", "al-muthanna"], "مُثَنَّا مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهَا مُضَافٌ إِلَيْهِ.", "«and her dual».", "«ve tesniyesi».", "مُثَنَّا", extra_segs=[seg("مُثَنَّا", "muthanna", "noun"), pr3fs()]),
  nahwu(),
  cited("تَضْرِبُ", "daraba", "verb", ["idafa-definiteness", "fail"], "فِعْلٌ مُضَارِعٌ — لِلْمُخَاطَبِ وَلِلْغَائِبَةِ.", "«you strike / she strikes».", "«vurursun / o (kadın) vurur».", punct="؛"),
  atf_wa("وَالْيَاءُ", "ya-letter", "noun", ["mubtada-khabar"], "الْيَاءُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the yāʾ».", "«ve yâ».", "الْيَاءُ"),
  li_("لِمَا", "ma-mawsula", "pron", ["mubtada-khabar", "ism-mawsul", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — خَبَرٌ.", "«for what».", "«... için».", "مَا"),
  W("بَقِيَ", "baqiya", "verb", ["ism-mawsul", "fail"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«remains».", "«geri kalan»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("الْغَائِبِ", "ghaib", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the absent».", "«gâib».", punct="."),
 ]})

# ----------- s9 (RESTORED): the prefix vowel
S.append({"id": "s9", "translation": {
 "en": "And the letter of muḍāraʿa carries a ḍamma in the four-lettered — as يُفْعِلُ، يُفَعِّلُ، يُفَاعِلُ — and a fatḥa in what is other than it, as يَسْتَفْعِلُ." + R_EN,
 "tr": "Muzâraat harfi rubâîde mazmûmdur — يُفْعِلُ، يُفَعِّلُ، يُفَاعِلُ gibi — onun dışındakilerde meftûhtur, يَسْتَفْعِلُ gibi." + R_TR},
 "tokens": [
  atf_wa("وَحَرْفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness"], "حَرْفُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the letter of».", "«ve harfi».", "حَرْفُ"),
  W("الْمُضَارَعَةِ", "mudaraa", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«muḍāraʿa».", "«muzâraat»."),
  W("مَضْمُومٌ", "madmum", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«carries a ḍamma».", "«mazmûmdur»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الرُّبَاعِيِّ", "rubai", "noun", ["huruf-jarr"], "مَجْرُورٌ — مَا مَاضِيهِ عَلَى أَرْبَعَةِ أَحْرُفٍ، مُجَرَّدًا كَانَ أَوْ مَزِيدًا.", "«the four-lettered» — bare or augmented.", "«rubâî» — mücerred ya da mezîd."),
  nahwu(),
  cited("يُفْعِلُ", "yufilu-wazn", "noun", ["idafa-definiteness", "form-iv-verbs"], "فِي مَحَلِّ جَرٍّ — وَزْنُ مُضَارِعِ أَفْعَلَ.", "«yufʿilu».", "«yüf'ilü»."),
  cited_wa("وَيُفَعِّلُ", "yufailu-wazn", "noun", ["form-ii-verbs"], "يُفَعِّلُ مَعْطُوفٌ — وَزْنُ مُضَارِعِ فَعَّلَ.", "«yufaʿʿilu».", "«yüfa''ilü».", "يُفَعِّلُ"),
  cited_wa("وَيُفَاعِلُ", "yufaailu-wazn", "noun", ["form-iii-verbs"], "يُفَاعِلُ مَعْطُوفٌ — وَزْنُ مُضَارِعِ فَاعَلَ.", "«yufāʿilu».", "«yüfâ'ilü».", "يُفَاعِلُ", punct="،"),
  W("مَفْتُوحٌ", "maftuh", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَهُوَ.", "«and a fatḥa».", "«meftûhtur»."),
  W("فِيمَا", "fi", "prep", ["huruf-jarr", "ism-mawsul", "anwa-ma"], "فِي حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«in what».", "«... olanda».", segments=[seg("فِي", "fi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  W("سِوَاهُ", "siwa", "noun", ["ism-mawsul", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«is other than it».", "«onun dışında».", segments=[seg("سِوَا", "siwa", "noun"), pr3ms()]),
  nahwu(),
  cited("يَسْتَفْعِلُ", "yastafilu-wazn", "noun", ["idafa-definiteness", "form-x-verbs"], "فِي مَحَلِّ جَرٍّ — وَزْنُ مُضَارِعِ اسْتَفْعَلَ.", "«yastafʿilu».", "«yestef'ilü».", punct="."),
 ]})

# ----------- s10 (RESTORED): the only declining verb
S.append({"id": "s10", "translation": {
 "en": "And no verb other than it declines; and it declines when neither the nūn of the feminine plural nor the nūn of emphasis is attached to it — and its iʿrāb is rafʿ, naṣb and jazm." + R_EN,
 "tr": "Fiillerden onun dışındakiler mu'reb olmaz; cemi müennes nûnu ile te'kîd nûnu kendisine bitişmediğinde mu'reb olur — i'râbı ref', nasb ve cezmdir." + R_TR},
 "tokens": [
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve -maz».", "لَا"),
  W("يُعْرَبُ", "araba", "verb", ["naib-al-fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«declines».", "«mu'reb olur»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("الْأَفْعَالِ", "fil", "noun", ["huruf-jarr", "jam-taksir"], "مَجْرُورٌ — جَمْعُ فِعْلٍ.", "«the verbs».", "«fiillerden»."),
  W("غَيْرُهُ", "ghayr", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«any other than it».", "«onun dışındakiler».", punct="؛", segments=[seg("غَيْرُ", "ghayr", "noun"), pr3ms()]),
  atf_wa("وَيُعْرَبُ", "araba", "verb", ["naib-al-fail", "form-iv-verbs"], "يُعْرَبُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it declines».", "«ve mu'reb olur».", "يُعْرَبُ"),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-diğinde»."),
  W("لَمْ", "lam-jazima", "part", [NJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-me-»."),
  W("تَتَّصِلْ", "ittasala", "verb", [NJ, "fail", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ.", "«is attached».", "«bitişmediğinde»."),
  bi_("بِهِ", "bi", "prep", [], "الْهَاءُ مَجْرُورٌ.", "«to it».", "«kendisine».", "هِ", segs=[seg("بِ", "bi", "prep"), pr3msi()]),
  W("نُونُ", "nun-letter", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the nūn of».", "«nûnu»."),
  W("جَمْعِ", "jam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the plural of».", "«cemi»."),
  W("الْمُؤَنَّثِ", "muannath", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine».", "«müennes»."),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor».", "«ve ... ne de».", "لَا"),
  W("نُونُ", "nun-letter", "noun", ["atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the nūn of».", "«nûnu»."),
  W("التَّأْكِيدِ", "takid", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«emphasis».", "«te'kîd».", punct="؛"),
  atf_wa("وَإِعْرَابُهُ", "irab", "noun", ["mubtada-khabar", "idafa-definiteness"], "إِعْرَابُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its iʿrāb».", "«ve i'râbı».", "إِعْرَابُ", extra_segs=[seg("إِعْرَابُ", "irab", "noun"), pr3ms()]),
  W("رَفْعٌ", "raf", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is rafʿ».", "«ref'»."),
  atf_wa("وَنَصْبٌ", "nasb", "noun", [], "نَصْبٌ مَعْطُوفٌ.", "«and naṣb».", "«ve nasb».", "نَصْبٌ"),
  atf_wa("وَجَزْمٌ", "jazm", "noun", [NJ], "جَزْمٌ مَعْطُوفٌ.", "«and jazm».", "«ve cezm».", "جَزْمٌ", punct="."),
 ]})

# ----------- s11 (COMMENTARY): the signs
S.append({"id": "s11", "translation": {
 "en": "So the sound verb bare of an apparent pronoun takes rafʿ by the ḍamma, naṣb by the fatḥa and jazm by the sukūn — يَضْرِبُ، لَنْ يَضْرِبَ، لَمْ يَضْرِبْ; and the one to which an apparent pronoun other than the plural nūn is attached takes rafʿ by the nūn and naṣb and jazm by its dropping — يَضْرِبَانِ، لَنْ يَضْرِبَا، لَمْ يَضْرِبَا." + C_EN,
 "tr": "Bâriz zamirden mücerred sahîh fiilin ref'i zamme, nasbı fetha, cezmi sükûn iledir — يَضْرِبُ، لَنْ يَضْرِبَ، لَمْ يَضْرِبْ; cemi nûnu dışında bir bâriz zamir bitişenin ref'i nûn ile, nasbı ve cezmi onun hazfiyledir — يَضْرِبَانِ، لَنْ يَضْرِبَا، لَمْ يَضْرِبَا." + C_TR},
 "tokens": [
  W("فَالصَّحِيحُ", "sahih", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَالصَّحِيحُ مُبْتَدَأٌ مَرْفُوعٌ — الصَّحِيحُ الْآخِرِ.", "«so the sound verb».", "«sahîh fiil».", segments=[seg("فَ", "fa", "conj"), seg("الصَّحِيحُ", "sahih", "noun")]),
  W("الْمُجَرَّدُ", "mujarrad", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«bare».", "«mücerred»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("الضَّمِيرِ", "damir", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a pronoun».", "«zamir»."),
  W("الْبَارِزِ", "bariz", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«apparent».", "«bâriz»."),
  W("رَفْعُهُ", "raf", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its rafʿ».", "«ref'i».", segments=[seg("رَفْعُ", "raf", "noun"), pr3ms()]),
  bi_("بِالضَّمَّةِ", "damma", "noun", ["mubtada-khabar"], "الضَّمَّةِ مَجْرُورٌ — خَبَرٌ.", "«is by the ḍamma».", "«zamme iledir».", "الضَّمَّةِ"),
  atf_wa("وَنَصْبُهُ", "nasb", "noun", ["mubtada-khabar", "idafa-definiteness"], "نَصْبُ مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its naṣb».", "«ve nasbı».", "نَصْبُ", extra_segs=[seg("نَصْبُ", "nasb", "noun"), pr3ms()]),
  bi_("بِالْفَتْحَةِ", "fatha", "noun", ["mubtada-khabar"], "الْفَتْحَةِ مَجْرُورٌ — خَبَرٌ.", "«by the fatḥa».", "«fetha iledir».", "الْفَتْحَةِ"),
  atf_wa("وَجَزْمُهُ", "jazm", "noun", ["mubtada-khabar", "idafa-definiteness", NJ], "جَزْمُ مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its jazm».", "«ve cezmi».", "جَزْمُ", extra_segs=[seg("جَزْمُ", "jazm", "noun"), pr3ms()]),
  bi_("بِالسُّكُونِ", "sukun", "noun", ["mubtada-khabar"], "السُّكُونِ مَجْرُورٌ — خَبَرٌ.", "«by the sukūn».", "«sükûn iledir».", "السُّكُونِ"),
  nahwu(),
  cited("يَضْرِبُ", "daraba", "verb", ["idafa-definiteness", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«he strikes».", "«vurur».", punct="،"),
  cited_wa("وَلَنْ", "lan", "part", [NJ], "لَنْ حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ.", "«and lan».", "«ve len».", "لَنْ"),
  cited("يَضْرِبَ", "daraba", "verb", [NJ, "fail"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«he will never strike».", "«asla vurmayacak».", punct="،"),
  cited_wa("وَلَمْ", "lam-jazima", "part", [NJ], "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and lam».", "«ve lem».", "لَمْ"),
  cited("يَضْرِبْ", "daraba", "verb", [NJ, "fail"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ.", "«he did not strike».", "«vurmadı».", punct="؛"),
  atf_wa("وَمَا", "ma-mawsula", "pron", ["mubtada-khabar", "ism-mawsul", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and the one».", "«ve ... olan».", "مَا"),
  W("اتَّصَلَ", "ittasala", "verb", ["ism-mawsul", "fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«is attached».", "«bitişen»."),
  bi_("بِهِ", "bi", "prep", [], "الْهَاءُ مَجْرُورٌ — الْعَائِدُ.", "«to it».", "«kendisine».", "هِ", segs=[seg("بِ", "bi", "prep"), pr3msi()]),
  W("ضَمِيرٌ", "damir", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a pronoun».", "«bir zamir»."),
  W("بَارِزٌ", "bariz", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«apparent».", "«bâriz»."),
  W("غَيْرُ", "ghayr", "noun", ["naat-sifa", "idafa-definiteness"], "صِفَةٌ ثَانِيَةٌ مَرْفُوعَةٌ، وَهُوَ مُضَافٌ.", "«other than».", "«dışında»."),
  W("نُونِ", "nun-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the nūn of».", "«nûnu»."),
  W("الْجَمْعِ", "jam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعِ الْمُؤَنَّثِ.", "«the plural».", "«cemi»."),
  W("رَفْعُهُ", "raf", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its rafʿ».", "«ref'i».", segments=[seg("رَفْعُ", "raf", "noun"), pr3ms()]),
  bi_("بِالنُّونِ", "nun-letter", "noun", ["mubtada-khabar"], "النُّونِ مَجْرُورٌ — خَبَرٌ.", "«is by the nūn».", "«nûn iledir».", "النُّونِ"),
  atf_wa("وَنَصْبُهُ", "nasb", "noun", ["mubtada-khabar", "idafa-definiteness"], "نَصْبُ مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its naṣb».", "«ve nasbı».", "نَصْبُ", extra_segs=[seg("نَصْبُ", "nasb", "noun"), pr3ms()]),
  atf_wa("وَجَزْمُهُ", "jazm", "noun", ["idafa-definiteness", NJ], "جَزْمُ مَعْطُوفٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its jazm».", "«ve cezmi».", "جَزْمُ", extra_segs=[seg("جَزْمُ", "jazm", "noun"), pr3ms()]),
  bi_("بِحَذْفِهَا", "hadhf", "noun", ["mubtada-khabar", "idafa-definiteness", "hadhf-wa-taqdir"], "حَذْفِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — خَبَرٌ.", "«are by its dropping».", "«onun hazfiyledir».", "حَذْفِ", segs=[seg("بِ", "bi", "prep"), seg("حَذْفِ", "hadhf", "noun"), pr3fs()]),
  nahwu(),
  cited("يَضْرِبَانِ", "daraba", "verb", ["idafa-definiteness", "fail", "al-muthanna"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«they two strike».", "«o ikisi vurur».", punct="،"),
  cited_wa("وَلَنْ", "lan", "part", [NJ], "لَنْ حَرْفُ نَفْيٍ وَنَصْبٍ.", "«and lan».", "«ve len».", "لَنْ"),
  cited("يَضْرِبَا", "daraba", "verb", [NJ, "fail", "al-muthanna"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِحَذْفِ النُّونِ.", "«they two will never strike».", "«o ikisi asla vurmayacak».", punct="،"),
  cited_wa("وَلَمْ", "lam-jazima", "part", [NJ], "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ.", "«and lam».", "«ve lem».", "لَمْ"),
  cited("يَضْرِبَا", "daraba", "verb", [NJ, "fail", "al-muthanna"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ.", "«they two did not strike».", "«o ikisi vurmadı».", punct="."),
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
 "sin-letter": need("sin-letter", "سِين", None, "noun", "the letter sīn — prefixed to the muḍāriʿ for the near future", "sîn harfi — yakın istikbâl için muzârinin başına gelir", 3),
 "luhuq": need("luhuq", "لُحُوق", "ل ح ق", "noun", "attachment, following on (of a suffix)", "bitişme, ardından gelme (bir ekin)", 4),
 "taqlil": need("taqlil", "تَقْلِيل", "ق ل ل", "noun", "rarity, lessening — the sense of قَدْ before a muḍāriʿ", "taklîl, azaltma — muzâri önündeki قَدْ'in mânâsı", 4),
 "kadhub": need("kadhub", "كَذُوب", "ك ذ ب", "noun", "a habitual liar — فَعُول", "çok yalancı — فَعُول", 4),
 "nayta": need("nayta", "نَأَيْتَ", None, "noun", "the mnemonic for the four letters of the muḍāriʿ: ن أ ي ت", "muzârinin dört harfinin hatırlatıcısı: ن أ ي ت", 3),
 "rubai": need("rubai", "رُبَاعِيّ", "ر ب ع", "noun", "four-lettered (of a verb's māḍī) — bare دَحْرَجَ or augmented أَفْعَلَ، فَعَّلَ، فَاعَلَ", "rubâî (mâzîsi dört harfli) — mücerred دَحْرَجَ veya mezîd أَفْعَلَ، فَعَّلَ، فَاعَلَ", 4),
 "yufilu-wazn": need("yufilu-wazn", "يُفْعِلُ", None, "noun", "the pattern يُفْعِلُ — the muḍāriʿ of Form IV, its prefix on a ḍamma", "yüf'ilü vezni — IV. bâbın muzârisi, ön eki zammeli", 3),
 "yufailu-wazn": need("yufailu-wazn", "يُفَعِّلُ", None, "noun", "the pattern يُفَعِّلُ — the muḍāriʿ of Form II, its prefix on a ḍamma", "yüfa''ilü vezni — II. bâbın muzârisi, ön eki zammeli", 3),
 "yufaailu-wazn": need("yufaailu-wazn", "يُفَاعِلُ", None, "noun", "the pattern يُفَاعِلُ — the muḍāriʿ of Form III, its prefix on a ḍamma", "yüfâ'ilü vezni — III. bâbın muzârisi, ön eki zammeli", 3),
 "yastafilu-wazn": need("yastafilu-wazn", "يَسْتَفْعِلُ", None, "noun", "the pattern يَسْتَفْعِلُ — the muḍāriʿ of Form X, its prefix on a fatḥa", "yestef'ilü vezni — X. bâbın muzârisi, ön eki fethalı", 3),
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
print("kafiya ch20 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الْفِعْلُ وَالْمَاضِي وَالْمُضَارِعُ فِي الْكَافِيَةِ", "en": "The verb in the Kafiya: its definition and marks, قَدْ and the two futures, the māḍī and its three bināʾs, the muḍāriʿ of نَأَيْتَ with its prefix vowel and its iʿrāb", "tr": "Kâfiye'de fiil: tarifi ve hâssaları, قَدْ ile iki istikbâl, mâzî ve üç binâsı, نَأَيْتَ'nin muzârisi, ön ek harekesi ve i'râbı"},
 "level": 3, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — الفعل: ما دل على معنى في نفسه مقترن بأحد الأزمنة الثلاثة؛ ومن خواصه قد والسين وسوف والجوازم وتاء التأنيث الساكنة والضمائر المرفوعة البارزة المتصلة؛ الماضي: ما دل على زمان قبل زمانك، مبني على الفتح؛ المضارع: ما أشبه الاسم بأحد حروف نأيت؛ حرف المضارعة مضموم في الرباعي مفتوح فيما سواه؛ ويعرب إذا لم تتصل به نون جمع المؤنث ونون التأكيد", "ضياء صونغور اوغلى — دفتر الكافية: قد للتحقيق وللتقليل؛ السين وسوف؛ ضرب ضربا ضربت ضربتا؛ رمى؛ ضربوا؛ وجه شبه المضارع بالاسم؛ الهمزة والنون والتاء والياء؛ علامات الرفع والنصب والجزم"],
 "question": {
  "en": ["What makes a word a VERB? It means something in itself (so it is not a particle) and that meaning is tied to a time (so it is not a noun): past, present or future. The definition is the same three-way split the first chapter made, now from the verb's side.",
         "How do you recognise one? By what only a verb admits: قَدْ, the sīn, سَوْفَ and the jāzims in front; the quiescent tāʾ of the feminine (فَعَلَتْ) and the raised attached pronouns (فَعَلْتَ) behind.",
         "What do the particles mean? قَدْ before a māḍī confirms (قَدْ صَدَقَ, «he did speak truly»); before a muḍāriʿ it says «sometimes» (إِنَّ الْكَذُوبَ قَدْ يَصْدُقُ). The sīn is the near future, سَوْفَ the far.",
         "What is the MĀḌĪ and how is it built? A verb for a time before the moment of speaking, built on the fatḥa — written (ضَرَبَ، ضَرَبَا، ضَرَبَتْ، ضَرَبَتَا) or estimated on an alif (رَمَى) — on the sukūn when a vowelled subject pronoun follows (ضَرَبْتُ، ضَرَبْنَ، ضَرَبْنَا), and on the ḍamma before the wāw of the plural (ضَرَبُوا). The sukūn is its bināʾ, never a jazm.",
         "What is the MUḌĀRIʿ? The verb that «resembles the noun» by one of نَأَيْتَ — hamza for I, nūn for we, tāʾ for you and for she and they-two-f., yāʾ for the rest of the absent. It resembles the noun because, like a noun, it is shared between two meanings (present and future) until the sīn or سَوْفَ narrows it — and that resemblance is why it, alone among verbs, declines.",
         "Which vowel does the prefix take? A ḍamma whenever the māḍī has four letters — bare دَحْرَجَ or augmented أَفْعَلَ، فَعَّلَ، فَاعَلَ (يُفْعِلُ، يُفَعِّلُ، يُفَاعِلُ) — and a fatḥa everywhere else (يَضْرِبُ، يَسْتَفْعِلُ).",
         "How does it decline? Rafʿ, naṣb and jazm, as long as neither the feminine-plural nūn nor the emphatic nūn is attached. A sound verb with no apparent pronoun shows ḍamma, fatḥa, sukūn (يَضْرِبُ، لَنْ يَضْرِبَ، لَمْ يَضْرِبْ); one carrying a dual, plural or second-feminine pronoun keeps its nūn in rafʿ and drops it in naṣb and jazm (يَضْرِبَانِ، لَنْ يَضْرِبَا، لَمْ يَضْرِبَا) — the five verbs. The SarfTagger reads the person off exactly these letters, and the IrabSign reads the case off exactly these endings."],
  "tr": ["Bir kelimeyi FİİL yapan nedir? Kendi başına bir mânâsı vardır (harf değildir) ve o mânâ bir zamana bağlıdır (isim değildir): mâzî, hâl ya da istikbâl. Tarif, ilk bâbın yaptığı üçlü ayrımın fiil tarafından görülmüş hâlidir.",
         "Nasıl tanınır? Yalnız fiilin kabul ettikleriyle: önünde قَدْ, sîn, سَوْفَ ve cezm ediciler; ardında sâkin te'nîs tâsı (فَعَلَتْ) ve merfû bitişik zamirler (فَعَلْتَ).",
         "Edatlar ne anlatır? Mâzî önündeki قَدْ tahkîk eder (قَدْ صَدَقَ, «gerçekten doğru söyledi»); muzâri önünde «bazen» der (إِنَّ الْكَذُوبَ قَدْ يَصْدُقُ). Sîn yakın istikbâl, سَوْفَ uzak.",
         "MÂZÎ nedir, nasıl binâ edilir? Konuşma ânından önceki zaman için fiil; fetha üzere mebnî — lafzan (ضَرَبَ، ضَرَبَا، ضَرَبَتْ، ضَرَبَتَا) ya da elif üzerinde takdîren (رَمَى) — harekeli özne zamiri gelince sükûn üzere (ضَرَبْتُ، ضَرَبْنَ، ضَرَبْنَا), cemi vâvından önce zamme üzere (ضَرَبُوا). Sükûn onun binâsıdır, asla cezm değil.",
         "MUZÂRİ nedir? نَأَيْتَ'den biriyle «isme benzeyen» fiil — hemze ben, nûn biz, tâ sen ve o (kadın) ile o iki kadın, yâ gâibin geri kalanı. İsme benzer, çünkü isim gibi, sîn ya da سَوْفَ daraltana kadar iki mânâ (hâl ve istikbâl) arasında müşterektir — ve bu benzerlik, fiiller içinde yalnız onun mu'reb olmasının sebebidir.",
         "Ön ek hangi harekeyi alır? Mâzî dört harfli olduğunda zamme — mücerred دَحْرَجَ ya da mezîd أَفْعَلَ، فَعَّلَ، فَاعَلَ (يُفْعِلُ، يُفَعِّلُ، يُفَاعِلُ) — başka her yerde fetha (يَضْرِبُ، يَسْتَفْعِلُ).",
         "Nasıl çekilir? Cemi müennes nûnu ile te'kîd nûnu bitişmedikçe ref', nasb ve cezm. Bâriz zamirsiz sahîh fiil zamme, fetha, sükûn gösterir (يَضْرِبُ، لَنْ يَضْرِبَ، لَمْ يَضْرِبْ); tesniye, cemi ya da muhâtaba zamiri taşıyan ref'te nûnunu tutar, nasb ve cezmde düşürür (يَضْرِبَانِ، لَنْ يَضْرِبَا، لَمْ يَضْرِبَا) — ef'âl-i hamse. SarfTagger şahsı tam bu harflerden, IrabSign hâli tam bu sonlardan okur."]},
 "plain": {
  "en": "A verb is a word whose meaning carries a time; only verbs take قَدْ, the sīn, سَوْفَ, a jāzim, the feminine تْ or a subject ending. The past is fixed on a fatḥa (sukūn before a vowelled ending, ḍamma before وا); the present-future starts with one of نَأَيْتَ and alone changes its ending for case.",
  "tr": "Fiil, mânâsı bir zaman taşıyan kelimedir. Tanırsınız, çünkü yalnız fiiller قَدْ, sîn, سَوْفَ, cezm edici, dişil تْ ya da özne eki alır. Geçmiş zaman fethaya sabitlenir (harekeli ekten önce sükûn, وا'dan önce zamme); şimdiki-gelecek zaman نَأَيْتَ'den biriyle başlar ve hâle göre sonu değişen tek fiildir."},
 "explanation": {
  "en": "The chapter opens the Kafiya's second part — the verb — with the definition that mirrors the noun's: a meaning in itself (against the particle) joined to a time (against the noun). The marks follow, and they are the practical half of the definition: a learner who cannot yet parse a word can still ask whether قَدْ, the sīn, سَوْفَ or لَمْ could stand before it and whether تْ or تَ could stand after it. The notebook's gloss on the particles is kept because it is doctrine, not decoration: قَدْ confirms a past and limits a present. The māḍī is defined by position relative to the speaker's own moment and built on the fatḥa, and the chapter's most useful sentence is the three-way account of that bināʾ — fatḥa written or estimated, sukūn before a vowelled subject pronoun because two vowels would otherwise crowd the ending, ḍamma before the wāw because the wāw demands it. None of these is iʿrāb, and the engine's IrabSign has the rule that the opening vowel, not the ending, decides what an ending means. The muḍāriʿ is defined by its letters, and the notebook's question — why does it resemble the noun? — is answered the classical way: it is ambiguous between present and future as a noun is ambiguous among meanings, and it is narrowed by the sīn and سَوْفَ as a noun is narrowed by the article. That resemblance is the ground of its iʿrāb, and the chapter closes on the two shapes that iʿrāb takes: vowels on a sound verb, the nūn kept or dropped on the five verbs. The received يُدَحْرِجُ is the notebook's model of the bare four-lettered verb; it is printed there with a khāʾ, and the chapter cites the patterns rather than the word.",
  "tr": "Bâb Kâfiye'nin ikinci kısmını — fiili — ismin tarifini aynalayan tarifle açar: kendi başına bir mânâ (harfe karşı), bir zamana bağlı (isme karşı). Hâssalar izler ve tarifin pratik yarısıdır: henüz bir kelimeyi tahlil edemeyen öğrenci yine de önüne قَدْ, sîn, سَوْفَ ya da لَمْ, ardına تْ ya da تَ gelip gelemeyeceğini sorabilir. Defterin edat açıklaması süs değil doktrin olduğu için tutulmuştur: قَدْ mâzîyi tahkîk eder, muzâriyi azaltır. Mâzî konuşanın kendi ânına göre konumla tarif edilir ve fetha üzere binâ edilir; bâbın en yararlı cümlesi bu binânın üçlü hesabıdır — fetha lafzan ya da takdîren, harekeli özne zamirinden önce sükûn (yoksa sonda iki hareke sıkışırdı), vâvdan önce zamme (vâv öyle ister). Bunların hiçbiri i'râb değildir ve motorun IrabSign'ı bir sonun ne anlama geldiğine sonun değil açılış harekesinin karar verdiği kuralını taşır. Muzâri harfleriyle tarif edilir ve defterin sorusu — neden isme benzer? — klasik biçimde cevaplanır: isim mânâlar arasında müphem olduğu gibi o da hâl ile istikbâl arasında müphemdir ve isim lâm ile daraltıldığı gibi o da sîn ve سَوْفَ ile daraltılır. Bu benzerlik i'râbının temelidir ve bâb i'râbın aldığı iki biçimle kapanır: sahîh fiilde harekeler, ef'âl-i hamsede tutulan ya da düşen nûn. Alınan يُدَحْرِجُ defterin mücerred rubâî modelidir; orada hâ ile basılmıştır ve bâb kelimeyi değil vezinleri zikreder."},
 "examples": [
  {"ar": "الْفِعْلُ: مَا دَلَّ عَلَى مَعْنًى فِي نَفْسِهِ مُقْتَرِنٍ بِأَحَدِ الْأَزْمِنَةِ الثَّلَاثَةِ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "قَدْ صَدَقَ — إِنَّ الْكَذُوبَ قَدْ يَصْدُقُ", "en": "قَدْ confirming, then limiting.", "tr": "Tahkîk eden, sonra azaltan قَدْ.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "الْمَاضِي: مَا دَلَّ عَلَى زَمَانٍ قَبْلَ زَمَانِكَ", "en": "The māḍī.", "tr": "Mâzî.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "ضَرَبَ، رَمَى — ضَرَبْتُ — ضَرَبُوا", "en": "Fatḥa, sukūn, ḍamma: the three bināʾs.", "tr": "Fetha, sükûn, zamme: üç binâ.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "الْمُضَارِعُ: مَا أَشْبَهَ الِاسْمَ بِأَحَدِ حُرُوفِ نَأَيْتَ", "en": "The muḍāriʿ.", "tr": "Muzâri.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "يُفْعِلُ، يُفَعِّلُ، يُفَاعِلُ — يَسْتَفْعِلُ", "en": "The prefix vowel.", "tr": "Ön ek harekesi.", "sourceStory": "al-kafiya", "sentence": "s9"},
  {"ar": "يَضْرِبُ، لَنْ يَضْرِبَ، لَمْ يَضْرِبْ — يَضْرِبَانِ، لَنْ يَضْرِبَا، لَمْ يَضْرِبَا", "en": "The signs of the three cases.", "tr": "Üç hâlin alâmetleri.", "sourceStory": "al-kafiya", "sentence": "s11"}],
 "commonMistakes": [
  {"wrong": "«ضَرَبْتُ — cezm ile sükûn»",
   "right": "«ضَرَبْتُ — harekeli merfû zamirden önce sükûn üzere MEBNÎ; mâzî hiç mu'reb olmaz»",
   "why": {"en": "There is no jāzim; the sukūn is the māḍī's bināʾ before a vowelled subject pronoun.", "tr": "Cezm edici yoktur; sükûn, harekeli özne zamirinden önce mâzînin binâsıdır."}},
  {"wrong": "«يَضْرِبُ — ön ek zammeli: يُضْرِبُ»",
   "right": "«يَضْرِبُ — sülâsî mücerredde fetha; zamme yalnız dört harfli mâzîde: يُكْرِمُ، يُعَلِّمُ، يُقَاتِلُ»",
   "why": {"en": "The ḍamma marks the four-lettered māḍī; يُضْرِبُ would be the passive.", "tr": "Zamme dört harfli mâzîyi işaretler; يُضْرِبُ meçhûl olurdu."}},
  {"wrong": "«لَمْ يَضْرِبَانِ»",
   "right": "«لَمْ يَضْرِبَا — ef'âl-i hamsede cezm nûnun hazfiyledir»",
   "why": {"en": "A verb carrying the dual alif takes its naṣb and jazm by dropping the nūn.", "tr": "Tesniye elifi taşıyan fiil nasb ve cezmini nûnu düşürerek alır."}},
  {"wrong": "«قَدْ يَصْدُقُ — kesinlikle doğru söyler»",
   "right": "«قَدْ يَصْدُقُ — bazen doğru söyler; قَدْ muzâri önünde taklîl içindir»",
   "why": {"en": "قَدْ confirms only before a māḍī; before a muḍāriʿ it limits.", "tr": "قَدْ yalnız mâzî önünde tahkîk eder; muzâri önünde azaltır."}}],
 "relatedNotes": ["al-murab-wal-mabni-wal-irab", NJ, "al-mabni-wal-mudmar", "al-majzum-wal-shart-wal-jaza", "form-iv-verbs"]}

ADD_EN = (" Chapter 20 (notebook lines ~283-296): the verb, the māḍī and the muḍāriʿ defined in the notebook's own Arabic (s1, s4, s6); the marks, the māḍī's three bināʾs, the prefix vowel and the muḍāriʿ's iʿrāb restored from the received matn and marked (s2, s5, s9, s10); "
          "قَدْ and the two futures, why the muḍāriʿ resembles the noun, the four letters and the signs of the three cases as commentary (s3, s7, s8, s11). DIVERGENCE: the notebook prints the four-lettered model as يُدَخْرِجُ (with khāʾ) for the received يُدَحْرِجُ; the chapter cites the patterns instead of the word.")
ADD_TR = (" Yirminci bâb (defter satırları ~283-296): fiil, mâzî ve muzâri defterin kendi Arapçasıyla tarif edilir (s1, s4, s6); hâssalar, mâzînin üç binâsı, ön ek harekesi ve muzârinin i'râbı alınan metinden geri yazılmış ve işaretlenmiştir (s2, s5, s9, s10); "
          "قَدْ ile iki istikbâl, muzârinin isme benzeme sebebi, dört harf ve üç hâlin alâmetleri şerh olarak (s3, s7, s8, s11). FARK: defter rubâî modeli alınan يُدَحْرِجُ yerine يُدَخْرِجُ (hâ ile) basar; bâb kelime yerine vezinleri zikreder.")
write_out(20, S, TITLE, ADD_EN, ADD_TR, "283-296", GLOSS_ADD, notes=(NOTE,),
          related=(("al-murab-wal-mabni-wal-irab", [K]), (NJ, [K])))
report(20, S, GLOSS_ADD, (NOTE,))
