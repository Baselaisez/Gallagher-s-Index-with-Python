# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 76 (the last): the three places the speaker must mind — the OPENING (husn al-ibtida; the ill omen to shun; baraʿat
al-istihlal), the TRANSITION (husn al-takhallus; the iqtidab of the ancients; the near iqtidab: أَمَّا بَعْدُ, the Qurʾanic هَذَا, the writers' هَذَا بَابٌ),
the CLOSE (husn al-intiha; the finest tells that the speech has ended) — and the book's last sentence on the suras. Source lines ~4820-4885
(sahifa 166-169). The Talkhis is COMPLETE with this chapter.

  RESTORED (the source carries the rulings only in Turkish): s1, s2, s5, s7, s9, s12, s15, s18, s20, s23, s26 — the received matn, marked.
  python3 tools/authoring/author_talkhis_ch76.py
"""
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
from talkhis_common import *
import talkhis_common as _tc
import sarf_gen as _sg
if os.environ.get("DRY_PKG"):
    _tc.PKG = pathlib.Path(os.environ["DRY_PKG"]); _tc.GR = pathlib.Path(os.environ["DRY_GR"])
PKG = _tc.PKG

K = "husn-al-ibtida-wal-takhallus-wal-intiha"
A = "ilm-al-arud"
QF = "al-qafiya"
TITLE = {"ar": "حُسْنُ الِابْتِدَاءِ وَالتَّخَلُّصِ وَالِانْتِهَاءِ", "en": "The fine opening, the fine transition and the fine close", "tr": "Hüsn-i ibtidâ, hüsn-i tahallus ve hüsn-i intihâ"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the source gives this ruling only in Turkish; this is the received matn of the Talkhis.)"
R_TR = " (Geri yazım: kaynak bu hükmü yalnız Türkçe verir; bu, Telhîs'in alınan metnidir.)"

def ix(sen, word, nth=1):
    n = 0
    for i, t in enumerate(sen["tokens"]):
        if t["surface"]["full"] == word:
            n += 1
            if n == nth: return i
    raise KeyError(word)
def span(sen, first, last):
    a, b = ix(sen, first), ix(sen, last); return list(range(a, b + 1))
def fi(tag, punct=None): return tok("فِي", "fi", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def pr3ms(): return seg("هُ", "pron-3ms", "pron")
def pr3msi(): return seg("هِ", "pron-3ms", "pron")
def pr3fs(): return seg("هَا", "pron-3fs", "pron")
def pr1p(): return seg("نَا", "pron-1p", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
def ka_qawl(name_toks, tag=None, wa=False):
    full = "وَكَقَوْلِ" if wa else "كَقَوْلِ"
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + [seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun")]
    return [tok(full, "qawl", "noun", [tag or K, "huruf-jarr", "idafa-definiteness"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ، مُضَافٌ.", "«as the saying of».", "«… sözü gibi».", segments=segs)] + name_toks
def name1(full, lex, en, tr): return [tok(full, lex, "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَمٌ.", en, tr, punct=":")]
def abu(second_full, second_lex, en2, tr2, note_ar, tags=()):
    return [tok("أَبِي", "ab", "noun", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«Abu».", "«Ebû»."),
            tok(second_full, second_lex, "propn", [K, "idafa-definiteness"] + list(tags), "مُضَافٌ إِلَيْهِ مَجْرُورٌ — " + note_ar, en2, tr2, punct=":")]
def abu_tammam(): return abu("تَمَّامٍ", "abu-tammam", "«Tammam».", "«Temmâm».", "أَبُو تَمَّامٍ.")
def FR(kind, ids, sub=None, source=None):
    d = {"kind": kind, "set": ids}
    if sub: d["sub"] = sub
    if source: d["source"] = source
    return d

# ----------- s1 — the three places (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "A section. The speaker must take care, in three places, that his speech be sweetest in wording, finest in manner and soundest in meaning: the opening, the transition and the close." + R_EN,
 "tr": "Fasıl. Mütekellim, sözünün lafızca en tatlı, üslûpça en güzel ve manaca en doğru olması için üç yerde dikkat etmelidir: başlangıç, geçiş ve son." + R_TR},
 "tokens": [
  tok("فَصْلٌ", "fasl", "noun", [K, "mubtada-khabar", "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هَذَا فَصْلٌ.", "«a section» — the khabar of a dropped mubtada.", "«fasıl» — mahzûf mübtedânın haberi.", punct="."),
  tok("يَنْبَغِي", "inbagha", "verb", [K, "form-vii-verbs", "naqis-verbs"], "مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — انْبَغَى: لَزِمَ.", "«it behoves».", "«gerekir»."),
  tok("لِلْمُتَكَلِّمِ", "mutakallim", "noun", [K, "huruf-jarr", "ism-fail", "form-v-verbs"], "اللَّامُ حَرْفُ جَرٍّ، وَالْمُتَكَلِّمِ مَجْرُورٌ — اسْمُ فَاعِلِ تَكَلَّمَ.", "«the speaker».", "«mütekellime».", segments=[seg("لِ", "li", "prep"), seg("الْمُتَكَلِّمِ", "mutakallim", "noun")]),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "fail"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ فَاعِلُ يَنْبَغِي.", "«that» — the masdar is the doer of «behoves».", "«-ması» — masdar yenbagî'nin fâili."),
  tok("يَتَأَنَّقَ", "taannaqa", "verb", [K, "an-masdariyya", "form-v-verbs"], "مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ — تَأَنَّقَ: بَالَغَ فِي الْإِحْسَانِ.", "«take care» — Form V: labour for the fine.", "«özenmesi» — tefa''ul: güzelliğe çalışmak."),
  fi(K),
  tok("ثَلَاثَةِ", "thalatha", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«three».", "«üç»."),
  tok("مَوَاضِعَ", "mawdi", "noun", [K, "idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«places» — a diptote plural.", "«yerde» — gayr-i munsarif cemi."),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("كَلَامِهِ", "kalam", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his speech».", "«sözünün».", segments=[seg("كَلَامِ", "kalam", "noun"), pr3msi()]),
  tok("لِيَكُونَ", "kana", "verb", [K, "lam-taleel", "kana-wa-akhawatuha"], "اللَّامُ لِلتَّعْلِيلِ، وَيَكُونَ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَاسْمُهُ مُسْتَتِرٌ: الْكَلَامُ.", "«so that it be».", "«olsun diye».", segments=[seg("لِ", "lam-taleel", "part"), seg("يَكُونَ", "kana", "verb")]),
  tok("أَعْذَبَ", "adhab", "noun", [K, "kana-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"], "خَبَرُ يَكُونَ مَنْصُوبٌ — اسْمُ تَفْضِيلٍ.", "«sweetest».", "«en tatlı»."),
  tok("لَفْظًا", "lafz", "noun", [K, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in wording».", "«lafızca»."),
  tok("وَأَحْسَنَ", "ahsan", "noun", [K, "atf-nasaq", "ism-tafdil"], "الْوَاوُ عَاطِفَةٌ، وَأَحْسَنَ مَعْطُوفٌ مَنْصُوبٌ.", "«and finest».", "«ve en güzel».", segments=[seg("وَ", "wa", "conj"), seg("أَحْسَنَ", "ahsan", "noun")]),
  tok("سَبْكًا", "sabk", "noun", [K, "tamyiz", "masdar"], "تَمْيِيزٌ مَنْصُوبٌ — السَّبْكُ: صَوْغُ الْكَلَامِ.", "«in manner» — the casting of speech.", "«üslûpça» — sözün dökümü."),
  tok("وَأَصَحَّ", "asahh", "noun", [K, "atf-nasaq", "ism-tafdil"], "الْوَاوُ عَاطِفَةٌ، وَأَصَحَّ مَعْطُوفٌ مَنْصُوبٌ.", "«and soundest».", "«ve en doğru».", segments=[seg("وَ", "wa", "conj"), seg("أَصَحَّ", "asahh", "noun")]),
  tok("مَعْنًى", "mana", "noun", [K, "tamyiz", "ism-maqsur-manqus"], "تَمْيِيزٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«in meaning».", "«manaca».", punct=":"),
  tok("الِابْتِدَاءُ", "ibtida-open", "noun", [K, "mubtada-khabar", "badal", "masdar", "form-viii-verbs"], "بَدَلٌ مِنْ ثَلَاثَةِ مَوَاضِعَ عَلَى الْمَحَلِّ، أَوْ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هِيَ الِابْتِدَاءُ.", "«the opening» — the badal of «three places».", "«başlangıç» — üç yerin bedeli."),
  tok("وَالتَّخَلُّصُ", "takhallus", "noun", [K, "atf-nasaq", "masdar", "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَالتَّخَلُّصُ مَعْطُوفٌ — مَصْدَرُ تَخَلَّصَ: الِانْتِقَالُ مِنْ مَعْنًى إِلَى آخَرَ.", "«and the transition» — passing from one theme to the next.", "«ve geçiş» — bir manadan diğerine geçme.", segments=[seg("وَ", "wa", "conj"), seg("التَّخَلُّصُ", "takhallus", "noun")]),
  tok("وَالِانْتِهَاءُ", "intiha", "noun", [K, "atf-nasaq", "masdar", "form-viii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَالِانْتِهَاءُ مَعْطُوفٌ — مَصْدَرُ انْتَهَى.", "«and the close».", "«ve son».", segments=[seg("وَ", "wa", "conj"), seg("الِانْتِهَاءُ", "intiha", "noun")], punct="."),
 ]})

# ----------- s2-s4 — the opening (RESTORED) + Imruʾ al-Qays + Ashjaʿ
S.append({"id": "s2", "translation": {"en": "As for the opening — as the saying of Imruʾ al-Qays:" + R_EN, "tr": "Başlangıca gelince — İmruülkays'ın şu sözü gibi:" + R_TR},
 "tokens": [
  tok("أَمَّا", "amma", "part", [K, "amma-tafsiliyya"], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for».", "«-e gelince»."),
  tok("الِابْتِدَاءُ", "ibtida-open", "noun", [K, "amma-tafsiliyya", "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the opening».", "«başlangıç»."),
  tok("فَكَقَوْلِ", "qawl", "noun", [K, "amma-tafsiliyya", "huruf-jarr", "idafa-definiteness", "mubtada-khabar"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَالْكَافُ حَرْفُ جَرٍّ، وَقَوْلِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«then as the saying of» — the khabar.", "«… sözü gibidir» — haber.", segments=[seg("فَ", "fa", "conj"), seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun")]),
  tok("امْرِئِ", "imru", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — امْرُؤٌ تَتْبَعُ هَمْزَتُهُ حَرَكَةَ الْإِعْرَابِ.", "«Imruʾ» — its hamza follows the case vowel.", "«İmru» — hemzesi i'rab harekesine uyar."),
  tok("الْقَيْسِ", "qays", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — امْرُؤُ الْقَيْسِ، صَاحِبُ الْمُعَلَّقَةِ.", "«al-Qays» — the poet of the Muʿallaqa.", "«el-Kays» — Muallaka şairi.", punct=":"),
 ]})
S.append({"id": "s3", "translation": {
 "en": "«Halt, you two, let us weep at the memory of a beloved and an abode» (ṭawīl) — a fine opening.",
 "tr": "«Durun ikiniz, bir sevgilinin ve bir yurdun anısına ağlayalım» (tavîl) — güzel bir başlangıç."},
 "tokens": [
  tok("قِفَا", "waqafa", "verb", [K, A, "imperative-amr", "mithal-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْأَلِفُ فَاعِلٌ — مِثَالٌ حُذِفَتْ وَاوُهُ: وَقَفَ يَقِفُ.", "«halt, you two» — the mithal verb drops its waw.", "«durun ikiniz» — misâl fiil vâvını düşürür."),
  tok("نَبْكِ", "baka", "verb", [K, "jawab-al-talab", "naqis-verbs"], "مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الطَّلَبِ بِحَذْفِ الْيَاءِ — بَكَى يَبْكِي.", "«let us weep» — jussive as the answer of the request.", "«ağlayalım» — talebin cevabında meczûm."),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ — لِلتَّعْلِيلِ.", "«at».", "«-den»."),
  tok("ذِكْرَى", "dhikra", "noun", [K, "huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«the memory of».", "«anısından»."),
  tok("حَبِيبٍ", "habib", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a beloved».", "«bir sevgilinin»."),
  tok("وَمَنْزِلِ", "manzil", "noun", [K, QF, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَنْزِلِ مَعْطُوفٌ مَجْرُورٌ — أُطْلِقَ لِلْقَافِيَةِ. الرَّوِيُّ اللَّامُ.", "«and an abode» — rawi lam.", "«ve bir yurdun» — revî lâm.", segments=[seg("وَ", "wa", "conj"), seg("مَنْزِلِ", "manzil", "noun")]),
 ]})
S[-1]["badi"] = [FR("husn-ibtida", list(range(0, 6)), "husn")]
S.append({"id": "s4", "translation": {
 "en": "And the saying of Ashjaʿ: «A palace upon which are greeting and peace — * the days have cast upon it their beauty» (kāmil) — a fine opening.",
 "tr": "Ve Eşca'ın: «Üzerinde tahiyye ve selâm olan bir köşk — * günler güzelliklerini üzerine atmış» (kâmil) sözü — güzel bir başlangıç."},
 "tokens": [tok("وَقَوْلِ", "qawl", "noun", [K, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَقَوْلِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the saying of».", "«ve … sözü».", segments=[seg("وَ", "wa", "conj"), seg("قَوْلِ", "qawl", "noun")])] + name1("أَشْجَعَ", "ashja", "«Ashjaʿ».", "«Eşca'».") + [
  tok("قَصْرٌ", "qasr", "noun", [K, A, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — نَكِرَةٌ مَوْصُوفَةٌ.", "«a palace» — a described nakira.", "«bir köşk» — mevsûf nekre."),
  tok("عَلَيْهِ", "ala", "prep", [K, "huruf-jarr", "mubtada-khabar"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ فِي الصِّفَةِ.", "«upon which».", "«üzerinde».", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("تَحِيَّةٌ", "tahiyya", "noun", [K, "mubtada-khabar", "naat-sifa", "jumla-sifa"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — وَالْجُمْلَةُ صِفَةُ قَصْرٍ.", "«greeting».", "«tahiyye»."),
  tok("وَسَلَامُ", "salam", "noun", [K, QF, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَسَلَامُ مَعْطُوفٌ مَرْفُوعٌ.", "«and peace».", "«ve selâm».", segments=[seg("وَ", "wa", "conj"), seg("سَلَامُ", "salam", "noun")], punct="*"),
  tok("خَلَعَتْ", "khalaa", "verb", [K, "fail", "mubtada-khabar"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — خَبَرُ قَصْرٌ.", "«have cast» — the khabar of «a palace».", "«atmış» — kasrın haberi."),
  tok("عَلَيْهِ", "ala", "prep", [K, "huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«upon it».", "«üzerine».", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("جَمَالَهَا", "jamal", "noun", [K, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their beauty».", "«güzelliklerini».", segments=[seg("جَمَالَ", "jamal", "noun"), pr3fs()]),
  tok("الْأَيَّامُ", "yawm", "noun", [K, QF, "fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ يَوْمٍ. الرَّوِيُّ الْمِيمُ.", "«the days» — rawi mim.", "«günler» — revî mîm."),
 ]})
S[-1]["badi"] = [FR("husn-ibtida", span(S[-1], "قَصْرٌ", "الْأَيَّامُ"), "husn")]

# ----------- s5-s6 — the ill omen to shun (RESTORED) + Ibn Muqatil
S.append({"id": "s5", "translation": {
 "en": "And what is taken for an ill omen must be shunned in the opening — as the saying of Ibn Muqatil:" + R_EN,
 "tr": "Başlangıçta uğursuz sayılan şeyden kaçınmak gerekir — İbn Mukâtil'in şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَيَجِبُ", "wajaba", "verb", [K, "mithal-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجِبُ مُضَارِعٌ مَرْفُوعٌ — وَجَبَ يَجِبُ.", "«and it is required».", "«ve gerekir».", segments=[seg("وَ", "wa", "conj"), seg("يَجِبُ", "wajaba", "verb")]),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "fail"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ فَاعِلٌ.", "«that».", "«-mak»."),
  tok("يُجْتَنَبَ", "ijtanaba", "verb", [K, "an-masdariyya", "naib-al-fail", "form-viii-verbs"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ.", "«be shunned».", "«kaçınılması»."),
  fi(K),
  tok("الِابْتِدَاءِ", "ibtida-open", "noun", [K, "huruf-jarr"], "مَجْرُورٌ.", "«the opening».", "«başlangıçta»."),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "naib-al-fail"], "اسْمٌ مَوْصُولٌ نَائِبُ فَاعِلٍ.", "«what».", "«şey»."),
  tok("يُتَطَيَّرُ", "tatayyara", "verb", [K, "ism-mawsul", "naib-al-fail", "form-v-verbs"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ؛ تَطَيَّرَ بِهِ: تَشَاءَمَ.", "«is taken for an ill omen» — Form V.", "«uğursuz sayılır» — tefa''ul."),
  tok("بِهِ", "bi", "prep", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — نَائِبُ الْفَاعِلِ.", "«by it».", "«ondan».", segments=[seg("بِ", "bi", "prep"), pr3msi()], punct="،"),
 ] + ka_qawl([tok("ابْنِ", "ibn", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«Ibn».", "«İbn»."),
              tok("مُقَاتِلٍ", "muqatil", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Muqatil» — Ibn Muqatil, the poet cited for the ill-omened opening.", "«Mukâtil» — uğursuz başlangıç için anılan şair.", punct=":")])})
S.append({"id": "s6", "translation": {
 "en": "«The appointed day of your loved ones for parting is tomorrow» (sarīʿ) — an opening to be shunned: he opened a poem with parting.",
 "tr": "«Sevdiklerinin ayrılık için sözleştiği gün yarındır» (serî') — kaçınılacak bir başlangıç: şiire ayrılıkla başladı."},
 "tokens": [
  tok("مَوْعِدُ", "mawid", "noun", [K, A, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرٌ مِيمِيٌّ مِنْ وَعَدَ.", "«the appointed day of».", "«sözleşilen günü»."),
  tok("أَحْبَابِكَ", "habib", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — جَمْعُ حَبِيبٍ.", "«your loved ones».", "«sevdiklerinin».", segments=[seg("أَحْبَابِ", "habib", "noun"), pr2ms()]),
  tok("بِالْفُرْقَةِ", "furqa", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْفُرْقَةِ مَجْرُورٌ — الْفُرْقَةُ: الِافْتِرَاقُ.", "«for parting».", "«ayrılık için».", segments=[seg("بِ", "bi", "prep"), seg("الْفُرْقَةِ", "furqa", "noun")]),
  tok("غَدُ", "ghad", "noun", [K, QF, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — أُطْلِقَ لِلْقَافِيَةِ. الرَّوِيُّ الدَّالُ.", "«is tomorrow» — rawi dal.", "«yarındır» — revî dâl."),
 ]})
S[-1]["badi"] = [FR("husn-ibtida", list(range(0, 4)), "tatayyur")]

# ----------- s7-s9 — baraʿat al-istihlal (RESTORED) + Abu Muhammad + Abu l-Faraj
S.append({"id": "s7", "translation": {
 "en": "And the finest opening is the one fitted to the purpose — and it is called BARAʿAT AL-ISTIHLAL: as the saying of Abu Muhammad in a congratulation:" + R_EN,
 "tr": "Başlangıcın en güzeli maksada uygun olanıdır — buna BERÂAT-İ İSTİHLÂL denir: Ebû Muhammed'in bir tebrikteki şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَأَحْسَنُهُ", "ahsan", "noun", [K, "mubtada-khabar", "ism-tafdil", "idafa-definiteness"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَحْسَنُ مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and the finest of it».", "«ve en güzeli».", segments=[seg("وَ", "wa", "conj"), seg("أَحْسَنُ", "ahsan", "noun"), pr3ms()]),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«what».", "«… olandır»."),
  tok("نَاسَبَ", "nasaba", "verb", [K, "ism-mawsul", "form-iii-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ؛ نَاسَبَ: لَاءَمَ.", "«fits».", "«uyan»."),
  tok("الْمَقْصُودَ", "maqsud", "noun", [K, "maful-bihi", "ism-maful"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the purpose».", "«maksada»."),
  tok("وَيُسَمَّى", "samma", "verb", [K, "naib-al-fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُسَمَّى مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it is called».", "«ve … denir».", segments=[seg("وَ", "wa", "conj"), seg("يُسَمَّى", "samma", "verb")]),
  tok("بَرَاعَةَ", "baraa", "noun", [K, "mafulayn", "idafa-definiteness", "masdar"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، مُضَافٌ — الْبَرَاعَةُ: التَّفَوُّقُ.", "«the excellence of».", "«berâat»."),
  tok("الِاسْتِهْلَالِ", "istihlal", "noun", [K, "idafa-definiteness", "masdar", "form-x-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الِاسْتِهْلَالُ: أَوَّلُ الْمَطَرِ، وَأَوَّلُ الصَّوْتِ.", "«the opening» — the first rain, the first cry.", "«istihlâl» — ilk yağmur, ilk ses.", punct=":"),
 ] + ka_qawl(abu("مُحَمَّدٍ", "muhammad", "«Muhammad».", "«Muhammed».", "أَبُو مُحَمَّدٍ الْخَازِنُ.")[:1] + [tok("مُحَمَّدٍ", "muhammad", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو مُحَمَّدٍ الْخَازِنُ.", "«Muhammad» — Abu Muhammad al-Khazin.", "«Muhammed» — Ebû Muhammed el-Hâzin.")]) + [
  fi(K),
  tok("تَهْنِئَةٍ", "tahnia", "noun", [K, "huruf-jarr", "masdar", "form-ii-verbs"], "مَجْرُورٌ — مَصْدَرُ هَنَّأَ.", "«a congratulation».", "«bir tebrikte».", punct=":"),
 ]})
S.append({"id": "s8", "translation": {
 "en": "«Good tidings! For fortune has fulfilled what it promised» (basīṭ) — the opening announces the congratulation.",
 "tr": "«Müjde! İkbal vaadini yerine getirdi» (basît) — başlangıç tebriği ilan eder."},
 "tokens": [
  tok("بُشْرَى", "bushra", "noun", [K, A, "mubtada-khabar", "hadhf-wa-taqdir", "ism-maqsur-manqus"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، خَبَرُهُ مَحْذُوفٌ: هَذِهِ بُشْرَى / لَكَ بُشْرَى.", "«good tidings!» — a mubtada with its khabar dropped.", "«müjde!» — haberi mahzûf mübtedâ."),
  tok("فَقَدْ", "qad", "part", [K, "qad-harf"], "الْفَاءُ لِلتَّعْلِيلِ، وَقَدْ لِلتَّحْقِيقِ.", "«for indeed».", "«çünkü».", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("أَنْجَزَ", "anjaza", "verb", [K, "form-iv-verbs"], "فِعْلٌ مَاضٍ — أَنْجَزَ الْوَعْدَ: وَفَّى بِهِ.", "«has fulfilled».", "«yerine getirdi»."),
  tok("الْإِقْبَالُ", "iqbal", "noun", [K, "fail", "masdar", "form-iv-verbs"], "فَاعِلٌ مَرْفُوعٌ — مَصْدَرُ أَقْبَلَ: الْحَظُّ.", "«fortune».", "«ikbal»."),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَفْعُولٌ بِهِ.", "«what».", "«… şeyi»."),
  tok("وَعَدَا", "waada", "verb", [K, QF, "ism-mawsul", "mithal-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْأَلِفُ لِلْإِطْلَاقِ — صِلَةٌ. الرَّوِيُّ الدَّالُ.", "«it promised» — the alif of release; rawi dal.", "«vaad etti» — ıtlâk elifi; revî dâl."),
 ]})
S[-1]["badi"] = [FR("baraat-istihlal", list(range(0, 6)))]
S.append({"id": "s9", "translation": {
 "en": "And the saying of Abu l-Faraj in an elegy: «It is the world that says, with a full mouth: * beware, beware of my violence and my slaughter!» (wāfir) — the opening announces the lament.",
 "tr": "Ve Ebü'l-Ferec'in bir mersiyedeki: «Dünyadır bu, ağız dolusu söyler: * sakın, sakın benim şiddetimden ve öldürmemden!» (vâfir) sözü — başlangıç ağıtı ilan eder."},
 "tokens": [tok("وَقَوْلِ", "qawl", "noun", [K, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَقَوْلِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the saying of».", "«ve … sözü».", segments=[seg("وَ", "wa", "conj"), seg("قَوْلِ", "qawl", "noun")])] + abu("الْفَرَجِ", "faraj", "«l-Faraj» — Abu l-Faraj al-Wawa? the poet the Talkhis cites; the received text names Abu l-Faraj.", "«l-Ferec» — Telhîs'in andığı şair Ebü'l-Ferec.", "أَبُو الْفَرَجِ.")[:1] + [tok("الْفَرَجِ", "faraj", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو الْفَرَجِ.", "«l-Faraj».", "«l-Ferec»."), fi(K),
  tok("مَرْثِيَةٍ", "marthiya", "noun", [K, "huruf-jarr"], "مَجْرُورٌ — الْمَرْثِيَةُ: قَصِيدَةُ الرِّثَاءِ.", "«an elegy».", "«bir mersiyede».", punct=":"),
  tok("هِيَ", "hiya", "pron", [K, A, "mubtada-khabar"], "مُبْتَدَأٌ.", "«it».", "«o»."),
  tok("الدُّنْيَا", "dunya", "noun", [K, "mubtada-khabar", "ism-maqsur-manqus"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«is the world».", "«dünyadır»."),
  tok("تَقُولُ", "qala", "verb", [K, "hal", "hollow-verbs"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ حَالٌ.", "«saying».", "«söyler»."),
  tok("بِمِلْءِ", "mil", "noun", [K, "huruf-jarr", "idafa-definiteness", "masdar"], "الْبَاءُ حَرْفُ جَرٍّ، وَمِلْءِ مَجْرُورٌ، مُضَافٌ.", "«with the fullness of».", "«dolusuyla».", segments=[seg("بِ", "bi", "prep"), seg("مِلْءِ", "mil", "noun")]),
  tok("فِيهَا", "fam", "noun", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — فُو مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهَا مُضَافٌ إِلَيْهِ.", "«her mouth» — fū, a five-noun, in jarr.", "«ağzının» — esmâ-i hamseden fû, cer hâli.", segments=[seg("فِي", "fam", "noun"), pr3fs()], punct="*"),
  tok("حَذَارِ", "hadhari", "noun", [K, "ism-fil"], "اسْمُ فِعْلِ أَمْرٍ بِمَعْنَى احْذَرْ، مَبْنِيٌّ عَلَى الْكَسْرِ — عَلَى فَعَالِ.", "«beware!» — the ism fiʿl on فَعَالِ.", "«sakın!» — fe'âli vezninde ism-i fiil."),
  tok("حَذَارِ", "hadhari", "noun", [K, "ism-fil", "tawkid"], "تَوْكِيدٌ لَفْظِيٌّ.", "«beware!» — repeated.", "«sakın!» — tekrar."),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("بَطْشِي", "batsh", "noun", [K, "huruf-jarr", "idafa-definiteness", "masdar", "ya-al-mutakallim"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my violence».", "«şiddetimden».", segments=[seg("بَطْشِ", "batsh", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("وَفَتْكِي", "fatk", "noun", [K, QF, "atf-nasaq", "idafa-definiteness", "masdar", "ya-al-mutakallim"], "الْوَاوُ عَاطِفَةٌ، وَفَتْكِ مَعْطُوفٌ مَجْرُورٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ. الرَّوِيُّ الْكَافُ، وَالْيَاءُ وَصْلٌ.", "«and my slaughter» — rawi kaf, the ya its wasl.", "«ve öldürmemden» — revî kâf, yâ vasl.", segments=[seg("وَ", "wa", "conj"), seg("فَتْكِ", "fatk", "noun"), seg("ي", "pron-1s", "pron")]),
 ]})
S[-1]["badi"] = [FR("baraat-istihlal", span(S[-1], "هِيَ", "وَفَتْكِي"))]

# ----------- s10-s13 — the takhallus (RESTORED) + Abu Tammam's two bayts
S.append({"id": "s10", "translation": {
 "en": "And as for the TRANSITION: it is the passing from what the speech was opened with — description, boast, complaint or the like — to the purpose, while keeping the fitness between them. As the saying of Abu Tammam:" + R_EN,
 "tr": "GEÇİŞE gelince: sözün açıldığı şeyden — tasvir, övünme, şikâyet ve benzerinden — aralarındaki uygunluğu gözeterek maksada geçmektir. Ebû Temmâm'ın şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, "amma-tafsiliyya"], "الْوَاوُ عَاطِفَةٌ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for».", "«ve … gelince».", segments=[seg("وَ", "wa", "conj"), seg("أَمَّا", "amma", "part")]),
  tok("التَّخَلُّصُ", "takhallus", "noun", [K, "amma-tafsiliyya", "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the transition».", "«geçiş»."),
  tok("فَهُوَ", "huwa", "pron", [K, "amma-tafsiliyya", "mubtada-khabar"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَهُوَ مُبْتَدَأٌ ثَانٍ.", "«then it is».", "«o».", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("الِانْتِقَالُ", "intiqal", "noun", [K, "mubtada-khabar", "masdar", "form-viii-verbs"], "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ انْتَقَلَ.", "«the passing».", "«geçmektir»."),
  tok("مِمَّا", "min", "prep", [K, "huruf-jarr", "ism-mawsul"], "مِنْ حَرْفُ جَرٍّ أُدْغِمَتْ نُونُهُ فِي مَا الْمَوْصُولَةِ.", "«from what».", "«… şeyden».", segments=[seg("مِ", "min", "prep"), seg("مَّا", "ma-mawsula", "noun")]),
  tok("افْتُتِحَ", "iftataha", "verb", [K, "ism-mawsul", "naib-al-fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«was opened».", "«açıldığı»."),
  tok("بِهِ", "bi", "prep", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ.", "«with it».", "«onunla».", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("الْكَلَامُ", "kalam", "noun", [K, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the speech».", "«söz»."),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ — لِلْبَيَانِ.", "«of».", "«-den»."),
  tok("وَصْفٍ", "wasf", "noun", [K, "huruf-jarr", "masdar"], "مَجْرُورٌ.", "«description».", "«tasvir»."),
  tok("أَوْ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("فَخْرٍ", "fakhr", "noun", [K, "atf-nasaq", "masdar"], "مَعْطُوفٌ مَجْرُورٌ.", "«boast».", "«övünme»."),
  tok("أَوْ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("شَكْوَى", "shakwa", "noun", [K, "atf-nasaq", "masdar", "ism-maqsur-manqus"], "مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«complaint».", "«şikâyet»."),
  tok("أَوْ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("غَيْرِهَا", "ghayr", "noun", [K, "atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«the like».", "«benzeri».", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3fs()]),
  tok("إِلَى", "ila", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْمَقْصُودِ", "maqsud", "noun", [K, "huruf-jarr", "ism-maful"], "مَجْرُورٌ.", "«the purpose».", "«maksada»."),
  tok("مَعَ", "maa", "noun", [K, "maful-fih"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with».", "«… ile»."),
  tok("رِعَايَةِ", "riaya", "noun", [K, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«keeping».", "«gözetme»."),
  tok("الْمُلَاءَمَةِ", "mulaama", "noun", [K, "idafa-definiteness", "masdar", "form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ لَاءَمَ.", "«the fitness».", "«uygunluğu»."),
  tok("بَيْنَهُمَا", "bayna", "noun", [K, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«between them».", "«aralarındaki».", segments=[seg("بَيْنَ", "bayna", "noun"), seg("هُمَا", "pron-3d", "pron")], punct="."),
 ] + ka_qawl(abu_tammam())})
S.append({"id": "s11", "translation": {
 "en": "«My people say at Qumis — and the night journey * and the strides of the long-necked Mahri camels have taken from us:» (basīṭ)",
 "tr": "«Kavmim Kûmis'te der — gece yolculuğu * ve uzun boyunlu Mehrî develerin adımları bizden aldığı hâlde:» (basît)"},
 "tokens": [
  tok("يَقُولُ", "qala", "verb", [K, A, "hollow-verbs"], "مُضَارِعٌ مَرْفُوعٌ.", "«say».", "«der»."),
  fi(K),
  tok("قُومَسٍ", "qumis", "propn", [K, "huruf-jarr"], "مَجْرُورٌ — قُومَسُ: كُورَةٌ بَيْنَ خُرَاسَانَ وَالرَّيِّ؛ صُرِفَ لِلضَّرُورَةِ.", "«Qumis» — a district on the Khurasan road.", "«Kûmis» — Horasan yolunda bir bölge."),
  tok("قَوْمِي", "qawm", "noun", [K, "fail", "idafa-definiteness", "ya-al-mutakallim"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my people».", "«kavmim».", segments=[seg("قَوْمِ", "qawm", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("وَقَدْ", "qad", "part", [K, "qad-harf", "hal"], "الْوَاوُ لِلْحَالِ، وَقَدْ لِلتَّحْقِيقِ.", "«while indeed».", "«… iken».", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("أَخَذَتْ", "akhadha", "verb", [K, "hal", "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — وَالْجُمْلَةُ حَالٌ.", "«have taken».", "«aldı».", punct="*"),
  tok("مِنَّا", "min", "prep", [K, "huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَنَا مَجْرُورٌ.", "«from us».", "«bizden».", segments=[seg("مِنْ", "min", "prep"), pr1p()]),
  tok("السُّرَى", "sura", "noun", [K, "fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — السُّرَى: سَيْرُ اللَّيْلِ.", "«the night journey».", "«gece yolculuğu»."),
  tok("وَخُطَا", "khutwa", "noun", [K, "atf-nasaq", "idafa-definiteness", "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَخُطَا مَعْطُوفٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ — جَمْعُ خُطْوَةٍ.", "«and the strides of».", "«ve adımları».", segments=[seg("وَ", "wa", "conj"), seg("خُطَا", "khutwa", "noun")]),
  tok("الْمَهْرِيَّةِ", "mahriyya", "noun", [K, "idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْإِبِلُ الْمَنْسُوبَةُ إِلَى مَهْرَةَ.", "«the Mahri camels».", "«Mehrî develerin»."),
  tok("الْقُودِ", "qud", "noun", [K, QF, "naat-sifa", "jam-taksir"], "نَعْتٌ مَجْرُورٌ — جَمْعُ أَقْوَدَ: الطَّوِيلُ الْعُنُقِ. الرَّوِيُّ الدَّالُ.", "«long-necked» — rawi dal.", "«uzun boyunlu» — revî dâl."),
 ]})
S.append({"id": "s12", "translation": {
 "en": "«Is it the rising-place of the sun you mean to bring us to? * I said: No — but the rising-place of generosity» — the transition from the journey to the praise: fine.",
 "tr": "«Bizi güneşin doğduğu yere mi götürmek istiyorsun? * Dedim: Hayır — cömertliğin doğduğu yere» — yolculuktan övgüye geçiş: güzel."},
 "tokens": [
  tok("أَمَطْلَعَ", "matla", "noun", [K, A, "al-istifham", "maful-bihi", "idafa-definiteness"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَمَطْلَعَ مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ، مُضَافٌ — اسْمُ مَكَانٍ.", "«is it the rising-place of» — the fronted object.", "«doğduğu yere mi» — öne alınmış mef'ûl.", segments=[seg("أَ", "hamza-istifham", "part"), seg("مَطْلَعَ", "matla", "noun")]),
  tok("الشَّمْسِ", "shams", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sun».", "«güneşin»."),
  tok("تَبْغِي", "bagha", "verb", [K, "naqis-verbs", "mafulayn"], "مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — بَغَى: طَلَبَ.", "«you mean».", "«istiyorsun»."),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ.", "«to».", "«-mek»."),
  tok("تَؤُمَّ", "amma-verb", "verb", [K, "an-masdariyya", "doubled-verbs"], "مُضَارِعٌ مَنْصُوبٌ — أَمَّ الْمَكَانَ: قَصَدَهُ.", "«bring to» — to make for a place.", "«yönelmek»."),
  tok("بِنَا", "bi", "prep", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَنَا مَجْرُورٌ.", "«us».", "«bizi».", segments=[seg("بِ", "bi", "prep"), pr1p()], punct="*"),
  tok("فَقُلْتُ", "qala", "verb", [K, "fail", "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَقُلْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I said».", "«dedim».", segments=[seg("فَ", "fa", "conj"), seg("قُلْ", "qala", "verb"), seg("تُ", "pron-1s", "pron")], punct=":"),
  tok("كَلَّا", "kalla", "part", [K, "insha-wa-tamanni"], "حَرْفُ رَدْعٍ وَزَجْرٍ.", "«no!».", "«hayır!»."),
  tok("وَلَكِنْ", "lakin", "part", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَكِنْ حَرْفُ اسْتِدْرَاكٍ.", "«but».", "«fakat».", segments=[seg("وَ", "wa", "conj"), seg("لَكِنْ", "lakin", "part")]),
  tok("مَطْلَعَ", "matla", "noun", [K, "maful-bihi", "idafa-definiteness", "hadhf-wa-taqdir"], "مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ: تَؤُمُّ مَطْلَعَ، مُضَافٌ.", "«the rising-place of» — the object of a dropped verb.", "«doğduğu yere» — mahzûf fiilin mef'ûlü."),
  tok("الْجُودِ", "jud", "noun", [K, QF, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ. الرَّوِيُّ الدَّالُ.", "«generosity» — rawi dal.", "«cömertliğin» — revî dâl."),
 ]})
S[-1]["badi"] = [FR("takhallus", span(S[-1], "فَقُلْتُ", "الْجُودِ"), "takhallus")]

# ----------- s13-s16 — the iqtidab (RESTORED) + Abu Tammam's two bayts
S.append({"id": "s13", "translation": {
 "en": "And sometimes the passing is to what has no fitness with the opening, and that is called IQTIDAB — and it is the way of the Arabs of the Jahiliyya and those after them who straddled both ages — as the saying of Abu Tammam:" + R_EN,
 "tr": "Bazen açılışla uygunluğu olmayana geçilir; buna İKTİDÂB denir — câhiliye Arapları ile onlardan sonra iki devri de gören muhadramların yoludur — Ebû Temmâm'ın şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَقَدْ", "qad", "part", [K, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ لِلتَّقْلِيلِ مَعَ الْمُضَارِعِ.", "«and sometimes» — qad of rarity.", "«ve bazen» — muzâri ile taklîl kad'ı.", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("يُنْتَقَلُ", "intaqala", "verb", [K, "naib-al-fail", "form-viii-verbs"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ.", "«one passes».", "«geçilir»."),
  tok("إِلَى", "ila", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "huruf-jarr"], "اسْمٌ مَوْصُولٌ مَجْرُورٌ.", "«what».", "«… şeye»."),
  tok("لَا", "la-nafiya", "part", [K, "la-nafiya-lil-jins"], "نَافِيَةٌ.", "«no».", "«olmayan»."),
  tok("مُلَاءَمَةَ", "mulaama", "noun", [K, "la-nafiya-lil-jins"], "اسْمُ لَا النَّافِيَةِ لِلْجِنْسِ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«fitness» — la's ism.", "«uygunluk» — lâ'nın ismi."),
  tok("لَهُ", "li", "prep", [K, "huruf-jarr", "la-nafiya-lil-jins"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرُ لَا.", "«for it» — la's khabar.", "«onun için» — lâ'nın haberi.", segments=[seg("لِ", "li", "prep"), pr3ms()]),
  tok("مَعَ", "maa", "noun", [K, "maful-fih"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with».", "«… ile»."),
  tok("الِابْتِدَاءِ", "ibtida-open", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the opening».", "«açılış».", punct="،"),
  tok("وَيُسَمَّى", "samma", "verb", [K, "naib-al-fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُسَمَّى مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it is called».", "«ve … denir».", segments=[seg("وَ", "wa", "conj"), seg("يُسَمَّى", "samma", "verb")]),
  tok("اقْتِضَابًا", "iqtidab", "noun", [K, "mafulayn", "masdar", "form-viii-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — الِاقْتِضَابُ: الْقَطْعُ وَالِارْتِجَالُ.", "«iqtidab» — a cutting-off.", "«iktidâb» — kesme, irticâl.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ.", "«and it is».", "«o».", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("مَذْهَبُ", "madhhab", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the way of».", "«yoludur»."),
  tok("الْعَرَبِ", "arab", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the Arabs».", "«Arapların»."),
  tok("الْجَاهِلِيَّةِ", "jahiliyya", "noun", [K, "naat-sifa", "ism-mansub"], "نَعْتٌ مَجْرُورٌ.", "«of the Jahiliyya».", "«câhiliye»."),
  tok("وَمَنْ", "man", "noun", [K, "atf-nasaq", "ism-mawsul"], "الْوَاوُ عَاطِفَةٌ، وَمَنْ اسْمٌ مَوْصُولٌ مَعْطُوفٌ.", "«and those who».", "«ve … kimselerin».", segments=[seg("وَ", "wa", "conj"), seg("مَنْ", "man", "noun")]),
  tok("يَلِيهِمْ", "waliya", "verb", [K, "ism-mawsul", "mithal-verbs", "naqis-verbs"], "مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُمْ مَفْعُولٌ — صِلَةٌ؛ وَلِيَ يَلِي.", "«come after them».", "«onlardan sonra gelen».", segments=[seg("يَلِي", "waliya", "verb"), seg("هِمْ", "pron-3mp", "pron")]),
  tok("مِنَ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("الْمُخَضْرَمِينَ", "mukhadram", "noun", [K, "huruf-jarr", "jam-mudhakkar-salim"], "مَجْرُورٌ بِالْيَاءِ — الْمُخَضْرَمُ: مَنْ أَدْرَكَ الْجَاهِلِيَّةَ وَالْإِسْلَامَ.", "«the mukhadrams» — those who saw both ages.", "«muhadramlar» — iki devri de görenler.", punct="،"),
 ] + ka_qawl(abu_tammam())})
S.append({"id": "s14", "translation": {
 "en": "«Had God seen that in grey hair there was good, * the righteous would neighbour Him in eternity grey-haired» (khafīf) —",
 "tr": "«Allah ak saçta bir hayır görseydi, * iyiler ebedîlik yurdunda O'na ak saçlı komşu olurlardı» (hafîf) —"},
 "tokens": [
  tok("لَوْ", "law", "part", [K, A, "in-shartiyya"], "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.", "«had».", "«-seydi»."),
  tok("رَأَى", "raa", "verb", [K, "naqis-verbs", "mafulayn"], "فِعْلٌ مَاضٍ — عِلْمِيَّةٌ تَنْصِبُ مَفْعُولَيْنِ.", "«seen» — the verb of knowing.", "«görseydi» — bilme fiili."),
  tok("اللهُ", "allah", "propn", [K, "fail"], "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.", "«God».", "«Allah»."),
  tok("أَنَّ", "anna", "part", [K, "inna-am-anna", "mafulayn"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ سَادٌّ مَسَدَّ الْمَفْعُولَيْنِ.", "«that».", "«-ını»."),
  fi(K),
  tok("الشَّيْبِ", "shayb", "noun", [K, "huruf-jarr", "inna-am-anna", "masdar"], "مَجْرُورٌ — خَبَرُ أَنَّ مُقَدَّمٌ.", "«grey hair» — anna's fronted khabar.", "«ak saçta» — ennenin öne alınmış haberi."),
  tok("خَيْرًا", "khayr", "noun", [K, "inna-am-anna"], "اسْمُ أَنَّ مُؤَخَّرٌ مَنْصُوبٌ.", "«good».", "«bir hayır».", punct="*"),
  tok("جَاوَرَتْهُ", "jawara", "verb", [K, "in-shartiyya", "form-iii-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْهَاءُ مَفْعُولٌ — جَوَابُ لَوْ.", "«would neighbour Him» — the jawab of law.", "«O'na komşu olurlardı» — lev'in cevabı.", segments=[seg("جَاوَرَتْ", "jawara", "verb"), pr3ms()]),
  tok("الْأَبْرَارُ", "barr", "noun", [K, "fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ بَرٍّ.", "«the righteous».", "«iyiler»."),
  fi(K),
  tok("الْخُلْدِ", "khuld", "noun", [K, "huruf-jarr", "masdar"], "مَجْرُورٌ — الْخُلْدُ: دَارُ الْبَقَاءِ.", "«eternity».", "«ebedîlik yurdunda»."),
  tok("شِيبًا", "ashyab", "noun", [K, QF, "hal", "jam-taksir"], "حَالٌ مَنْصُوبٌ — جَمْعُ أَشْيَبَ. الرَّوِيُّ الْبَاءُ.", "«grey-haired» — the hal; rawi ba.", "«ak saçlı olarak» — hâl; revî bâ."),
 ]})
S.append({"id": "s15", "translation": {
 "en": "«Every day the turns of the nights show * a rare trait from Abu Saʿid» — from the complaint of grey hair straight to the praise of Abu Saʿid, with no fitness between: iqtidab.",
 "tr": "«Gecelerin dönüşleri her gün * Ebû Saîd'den görülmemiş bir huy gösterir» — ak saç şikâyetinden doğrudan Ebû Saîd'in övgüsüne, arada uygunluk yok: iktidâb."},
 "tokens": [
  tok("كُلَّ", "kull", "noun", [K, A, "maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«every».", "«her»."),
  tok("يَوْمٍ", "yawm", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«day».", "«gün»."),
  tok("تُبْدِي", "abda", "verb", [K, "form-iv-verbs", "naqis-verbs", "mafulayn"], "مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«show».", "«gösterir»."),
  tok("صُرُوفُ", "sarf-turn", "noun", [K, "fail", "idafa-definiteness", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — جَمْعُ صَرْفٍ: حَوَادِثُ الدَّهْرِ.", "«the turns of».", "«dönüşleri»."),
  tok("اللَّيَالِي", "layla", "noun", [K, "idafa-definiteness", "jam-taksir", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — جَمْعُ لَيْلَةٍ، مَنْقُوصٌ.", "«the nights».", "«gecelerin».", punct="*"),
  tok("خُلُقًا", "khuluq", "noun", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a trait».", "«bir huy»."),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("أَبِي", "ab", "noun", [K, "huruf-jarr", "idafa-definiteness", "five-nouns"], "مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«Abu».", "«Ebû»."),
  tok("سَعِيدٍ", "said-name", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو سَعِيدٍ الثَّغْرِيُّ، مَمْدُوحُ أَبِي تَمَّامٍ.", "«Saʿid» — Abu Saʿid al-Thaghri, Abu Tammam's patron.", "«Saîd» — Ebû Temmâm'ın memduhu Ebû Saîd es-Sağrî."),
  tok("غَرِيبَا", "gharib", "noun", [K, QF, "naat-sifa"], "نَعْتٌ مَنْصُوبٌ — أُبْدِلَ التَّنْوِينُ أَلِفَ الْإِطْلَاقِ. الرَّوِيُّ الْبَاءُ.", "«rare» — rawi ba.", "«görülmemiş» — revî bâ."),
 ]})
S[-1]["badi"] = [FR("takhallus", list(range(0, 10)), "iqtidab")]

# ----------- s16-s18 — the near iqtidab: أَمَّا بَعْدُ, the Qurʾanic هَذَا, the writers' هَذَا بَابٌ (RESTORED + the received sayings)
S.append({"id": "s16", "translation": {
 "en": "And of the iqtidab is what is near to the transition — as your saying, after praising God: «Now then» — and this was called FASL AL-KHITAB (the decisive address);" + R_EN,
 "tr": "İktidâbtan geçişe yakın olanı vardır — Allah'a hamdden sonra «Emmâ ba'du» demen gibi — buna FASLÜ'L-HİTÂB da denmiştir;" + R_TR},
 "tokens": [
  tok("وَمِنَ", "min", "prep", [K, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْ حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and of».", "«ve … -dan».", segments=[seg("وَ", "wa", "conj"), seg("مِنَ", "min", "prep")]),
  tok("الِاقْتِضَابِ", "iqtidab", "noun", [K, "huruf-jarr"], "مَجْرُورٌ.", "«the iqtidab».", "«iktidâb»."),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what».", "«… olanı»."),
  tok("يَقْرُبُ", "qaruba", "verb", [K, "ism-mawsul"], "مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ؛ قَرُبَ يَقْرُبُ.", "«is near».", "«yakın olan»."),
  tok("مِنَ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("التَّخَلُّصِ", "takhallus", "noun", [K, "huruf-jarr"], "مَجْرُورٌ.", "«the transition».", "«geçişe»."),
  tok("كَقَوْلِكَ", "qawl", "noun", [K, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«as your saying».", "«demen gibi».", segments=[seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun"), pr2ms()]),
  tok("بَعْدَ", "bada", "noun", [K, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«after».", "«-den sonra»."),
  tok("حَمْدِ", "hamd", "noun", [K, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«praising».", "«hamd»."),
  tok("اللهِ", "allah", "propn", [K, "idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God».", "«Allah'a».", punct=":"),
  tok("أَمَّا", "amma", "part", [K, "amma-tafsiliyya"], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ — أَمَّا بَعْدُ: مَهْمَا يَكُنْ مِنْ شَيْءٍ بَعْدُ.", "«now» — «whatever comes after».", "«emmâ» — «bundan sonra ne olursa»."),
  tok("بَعْدُ", "bada", "noun", [K, "amma-tafsiliyya", "maful-fih"], "ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ لِقَطْعِهِ عَنِ الْإِضَافَةِ لَفْظًا.", "«then» — built on damma, its annexed dropped.", "«ba'du» — muzâfun ileyhi düşmüş, damme üzere mebnî.", punct="،"),
  tok("وَقَدْ", "qad", "part", [K, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ لِلتَّحْقِيقِ.", "«and indeed».", "«ve».", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("سُمِّيَ", "samma", "verb", [K, "naib-al-fail", "mafulayn"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«it was called».", "«… denmiştir»."),
  tok("فَصْلَ", "fasl", "noun", [K, "mafulayn", "idafa-definiteness"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، مُضَافٌ.", "«the decisive».", "«fasl»."),
  tok("الْخِطَابِ", "khitab", "noun", [K, "idafa-definiteness", "masdar", "form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«address».", "«hitâb».", punct="؛"),
 ]})
S[-1]["badi"] = [FR("takhallus", span(S[-1], "أَمَّا", "بَعْدُ"), "fasl-khitab")]
S.append({"id": "s17", "translation": {
 "en": "and as the saying of the Exalted: «This! And truly for the transgressors is an evil resort» — and: «This is a remembrance; and truly for the God-fearing is a fair resort» (Sad 55 and 49);",
 "tr": "ve Allah Teâlâ'nın: «Bu böyle! Azgınlar için de kötü bir dönüş yeri vardır» — ve: «Bu bir zikirdir; müttakîler için de güzel bir dönüş yeri vardır» (Sâd 55 ve 49) sözü gibi;"},
 "tokens": [
  tok("وَكَقَوْلِهِ", "qawl", "noun", [K, "huruf-jarr", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَالْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and as His saying».", "«ve O'nun sözü gibi».", segments=[seg("وَ", "wa", "conj"), seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  tok("تَعَالَى", "taala", "verb", [K, "form-vi-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ لِلتَّنْزِيهِ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«the Exalted».", "«Teâlâ».", punct=":"),
  tok("هَذَا", "hadha", "pron", [K, "asma-al-ishara", "mubtada-khabar", "hadhf-wa-taqdir"], "اسْمُ إِشَارَةٍ مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ: هَذَا كَمَا ذُكِرَ — بِهِ يُقْتَضَبُ الْكَلَامُ.", "«this!» — a mubtada whose khabar is dropped: the cut.", "«bu böyle!» — haberi mahzûf mübtedâ: kesiş.", punct="،"),
  tok("وَإِنَّ", "inna", "part", [K, "inna-wa-akhawatuha"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«and truly».", "«ve şüphesiz».", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part")]),
  tok("لِلطَّاغِينَ", "taghi", "noun", [K, "huruf-jarr", "inna-wa-akhawatuha", "jam-mudhakkar-salim", "ism-fail"], "اللَّامُ حَرْفُ جَرٍّ، وَالطَّاغِينَ مَجْرُورٌ بِالْيَاءِ — خَبَرُ إِنَّ مُقَدَّمٌ؛ جَمْعُ طَاغٍ.", "«for the transgressors» — inna's fronted khabar.", "«azgınlar için» — innenin öne alınmış haberi.", segments=[seg("لِ", "li", "prep"), seg("الطَّاغِينَ", "taghi", "noun")]),
  tok("لَشَرَّ", "sharr", "noun", [K, "inna-wa-akhawatuha", "idafa-definiteness", "tawkid"], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَشَرَّ اسْمُ إِنَّ مُؤَخَّرٌ مَنْصُوبٌ، مُضَافٌ.", "«an evil» — the slid lam; inna's delayed ism.", "«kötü» — kaymış lâm; innenin sona bırakılmış ismi.", segments=[seg("لَ", "la-ibtida", "part"), seg("شَرَّ", "sharr", "noun")]),
  tok("مَآبٍ", "maab", "noun", [K, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرٌ مِيمِيٌّ مِنْ آبَ: رَجَعَ.", "«resort» — the place of return.", "«dönüş yeri»."),
  tok("وَقَوْلِهِ", "qawl", "noun", [K, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَقَوْلِ مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and His saying».", "«ve O'nun sözü».", segments=[seg("وَ", "wa", "conj"), seg("قَوْلِ", "qawl", "noun"), pr3msi()], punct=":"),
  tok("هَذَا", "hadha", "pron", [K, "asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مُبْتَدَأٌ.", "«this».", "«bu»."),
  tok("ذِكْرٌ", "dhikr", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is a remembrance».", "«bir zikirdir».", punct="،"),
  tok("وَإِنَّ", "inna", "part", [K, "inna-wa-akhawatuha"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«and truly».", "«ve şüphesiz».", segments=[seg("وَ", "wa", "conj"), seg("إِنَّ", "inna", "part")]),
  tok("لِلْمُتَّقِينَ", "muttaqi", "noun", [K, "huruf-jarr", "inna-wa-akhawatuha", "jam-mudhakkar-salim", "ism-fail", "form-viii-verbs"], "اللَّامُ حَرْفُ جَرٍّ، وَالْمُتَّقِينَ مَجْرُورٌ بِالْيَاءِ — خَبَرُ إِنَّ مُقَدَّمٌ.", "«for the God-fearing».", "«müttakîler için».", segments=[seg("لِ", "li", "prep"), seg("الْمُتَّقِينَ", "muttaqi", "noun")]),
  tok("لَحُسْنَ", "husn", "noun", [K, "inna-wa-akhawatuha", "idafa-definiteness", "tawkid"], "اللَّامُ الْمُزَحْلَقَةُ، وَحُسْنَ اسْمُ إِنَّ مُؤَخَّرٌ مَنْصُوبٌ، مُضَافٌ.", "«a fair» — inna's delayed ism.", "«güzel» — innenin sona bırakılmış ismi.", segments=[seg("لَ", "la-ibtida", "part"), seg("حُسْنَ", "husn", "noun")]),
  tok("مَآبٍ", "maab", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«resort».", "«dönüş yeri».", punct="؛"),
 ]})
S[-1]["badi"] = [FR("takhallus", [ix(S[-1], "هَذَا")], "iqtidab", source="ص ٥٥"), FR("takhallus", [ix(S[-1], "هَذَا", 2)], "iqtidab", source="ص ٤٩")]
S.append({"id": "s18", "translation": {"en": "and of it is the saying of the writers: «This is a chapter»." + R_EN, "tr": "yazarların «Bu bir bâbdır» demesi de bundandır." + R_TR},
 "tokens": [
  tok("وَمِنْهُ", "min", "prep", [K, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهُ خَبَرٌ مُقَدَّمٌ.", "«and of it».", "«ve ondandır».", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("قَوْلُ", "qawl", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the saying of».", "«… demesi»."),
  tok("الْكُتَّابِ", "katib", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ كَاتِبٍ.", "«the writers».", "«yazarların».", punct=":"),
  tok("هَذَا", "hadha", "pron", [K, "asma-al-ishara", "mubtada-khabar"], "اسْمُ إِشَارَةٍ مُبْتَدَأٌ.", "«this».", "«bu»."),
  tok("بَابٌ", "bab", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is a chapter».", "«bir bâbdır».", punct="."),
 ]})
S[-1]["badi"] = [FR("takhallus", [ix(S[-1], "هَذَا")], "iqtidab")]

# ----------- s19-s22 — the close (RESTORED) + Abu Tammam's two bayts + Abu Ishaq
S.append({"id": "s19", "translation": {"en": "And as for the CLOSE — as the saying of Abu Tammam:" + R_EN, "tr": "SONA gelince — Ebû Temmâm'ın şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, "amma-tafsiliyya"], "الْوَاوُ عَاطِفَةٌ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for».", "«ve … gelince».", segments=[seg("وَ", "wa", "conj"), seg("أَمَّا", "amma", "part")]),
  tok("الِانْتِهَاءُ", "intiha", "noun", [K, "amma-tafsiliyya", "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the close».", "«son»."),
  tok("فَكَقَوْلِ", "qawl", "noun", [K, "amma-tafsiliyya", "huruf-jarr", "idafa-definiteness", "mubtada-khabar"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَالْكَافُ حَرْفُ جَرٍّ، وَقَوْلِ مَجْرُورٌ، مُضَافٌ — خَبَرٌ.", "«then as the saying of».", "«… sözü gibidir».", segments=[seg("فَ", "fa", "conj"), seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun")]),
 ] + abu_tammam()})
S.append({"id": "s20", "translation": {
 "en": "«And I am worthy, since I have reached you, of the wishes, * and you are worthy of what I hoped from you» (ṭawīl) —",
 "tr": "«Sana ulaştığıma göre ben arzulara lâyığım, * sen de senden umduğuma lâyıksın» (tavîl) —"},
 "tokens": [
  tok("وَإِنِّي", "inna", "part", [K, A, "inna-wa-akhawatuha", "ya-al-mutakallim"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ اسْمُهَا.", "«and I».", "«ve ben».", segments=[seg("وَ", "wa", "conj"), seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("جَدِيرٌ", "jadir", "noun", [K, "inna-wa-akhawatuha", "sifa-mushabbaha"], "خَبَرُ إِنَّ مَرْفُوعٌ — جَدِيرٌ بِهِ: حَقِيقٌ.", "«worthy» — inna's khabar.", "«lâyık» — innenin haberi."),
  tok("إِذْ", "idh", "part", [K, "maful-fih"], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ — لِلتَّعْلِيلِ.", "«since».", "«-diğime göre»."),
  tok("بَلَغْتُكَ", "balagha", "verb", [K, "fail", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ.", "«I have reached you».", "«sana ulaştım».", segments=[seg("بَلَغْ", "balagha", "verb"), seg("تُ", "pron-1s", "pron"), pr2ms()]),
  tok("بِالْمُنَى", "munya", "noun", [K, "huruf-jarr", "jam-taksir", "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْمُنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — جَمْعُ مُنْيَةٍ.", "«of the wishes».", "«arzulara».", segments=[seg("بِ", "bi", "prep"), seg("الْمُنَى", "munya", "noun")], punct="*"),
  tok("وَأَنْتَ", "anta", "pron", [K, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَأَنْتَ مُبْتَدَأٌ.", "«and you».", "«ve sen».", segments=[seg("وَ", "wa", "conj"), seg("أَنْتَ", "anta", "pron")]),
  tok("بِمَا", "bi", "prep", [K, "huruf-jarr", "ism-mawsul"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ مَجْرُورٌ.", "«of what».", "«… şeye».", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "noun")]),
  tok("أَمَّلْتُ", "ammala", "verb", [K, "ism-mawsul", "form-ii-verbs", "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — صِلَةٌ؛ أَمَّلَ: رَجَا.", "«I hoped».", "«umduğum».", segments=[seg("أَمَّلْ", "ammala", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("مِنْكَ", "min", "prep", [K, "huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْكَافُ مَجْرُورٌ.", "«from you».", "«senden».", segments=[seg("مِنْ", "min", "prep"), pr2ms()]),
  tok("جَدِيرُ", "jadir", "noun", [K, QF, "mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ مَرْفُوعٌ — أُطْلِقَ لِلْقَافِيَةِ. الرَّوِيُّ الرَّاءُ.", "«worthy» — rawi ra.", "«lâyıksın» — revî râ."),
 ]})
S.append({"id": "s21", "translation": {
 "en": "«So if you grant me your kindness — you are its people; * and if not, I am excusing and thankful» — the close: fine, and it tells that the speech has ended.",
 "tr": "«Bana kendiliğinden güzel ihsanda bulunursan sen bunun ehlisin; * bulunmazsan ben mazur görür ve teşekkür ederim» — son: güzel, ve sözün bittiğini haber verir."},
 "tokens": [
  tok("فَإِنْ", "in-shartiyya", "part", [K, A, "in-shartiyya"], "الْفَاءُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«so if».", "«eğer».", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("تُولِنِي", "awla-grant", "verb", [K, "in-shartiyya", "form-iv-verbs", "naqis-verbs", "mafulayn", "ya-al-mutakallim"], "مُضَارِعٌ مَجْزُومٌ بِحَذْفِ الْيَاءِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ أَوَّلُ — أَوْلَاهُ مَعْرُوفًا.", "«you grant me» — jussive by the dropped ya.", "«bana verirsen» — yâ düşmüş meczûm.", segments=[seg("تُولِ", "awla", "verb"), seg("نِي", "pron-1s", "pron")]),
  tok("مِنْكَ", "min", "prep", [K, "huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْكَافُ مَجْرُورٌ.", "«from you».", "«kendinden».", segments=[seg("مِنْ", "min", "prep"), pr2ms()]),
  tok("الْجَمِيلَ", "jamil", "noun", [K, "mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«kindness».", "«güzel ihsanı»."),
  tok("فَأَهْلُهُ", "ahl", "noun", [K, "in-shartiyya", "mubtada-khabar", "idafa-definiteness", "hadhf-wa-taqdir"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَأَهْلُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: فَأَنْتَ أَهْلُهُ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«you are its people» — the mubtada dropped.", "«sen bunun ehlisin» — mübtedâ mahzûf.", segments=[seg("فَ", "fa", "conj"), seg("أَهْلُ", "ahl", "noun"), pr3ms()], punct="*"),
  tok("وَإِلَّا", "illa", "part", [K, "in-shartiyya", "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ شَرْطِيَّةٌ أُدْغِمَتْ فِي لَا — أَيْ وَإِنْ لَمْ تُولِنِي.", "«and if not».", "«yoksa».", segments=[seg("وَ", "wa", "conj"), seg("إِلَّا", "illa", "part")]),
  tok("فَإِنِّي", "inna", "part", [K, "in-shartiyya", "inna-wa-akhawatuha", "ya-al-mutakallim"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ اسْمُهَا.", "«then I».", "«ben».", segments=[seg("فَ", "fa", "conj"), seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("عَاذِرٌ", "adhir", "noun", [K, "inna-wa-akhawatuha", "ism-fail"], "خَبَرُ إِنَّ مَرْفُوعٌ — اسْمُ فَاعِلِ عَذَرَ.", "«excusing».", "«mazur gören»."),
  tok("وَشَكُورُ", "shakur", "noun", [K, QF, "atf-nasaq", "sighat-mubalagha"], "الْوَاوُ عَاطِفَةٌ، وَشَكُورُ مَعْطُوفٌ مَرْفُوعٌ — صِيغَةُ مُبَالَغَةٍ؛ أُطْلِقَ لِلْقَافِيَةِ. الرَّوِيُّ الرَّاءُ.", "«and thankful» — rawi ra.", "«ve çok şükreden» — revî râ.", segments=[seg("وَ", "wa", "conj"), seg("شَكُورُ", "shakur", "noun")]),
 ]})
S[-1]["badi"] = [FR("husn-intiha", list(range(0, 9)))]
S.append({"id": "s22", "translation": {
 "en": "And the finest of it is what tells that the speech has ended — as the saying of Abu Ishaq: «May you last while time lasts, O refuge of its people — * and this is a prayer that embraces all creation» (ṭawīl)." + R_EN,
 "tr": "En güzeli, sözün bittiğini haber verendir — Ebû İshâk'ın: «Ehlinin sığınağı, zaman durdukça bâkî ol — * bu, bütün mahlûkatı kapsayan bir duadır» (tavîl) sözü gibi." + R_TR},
 "tokens": [
  tok("وَأَحْسَنُهُ", "ahsan", "noun", [K, "mubtada-khabar", "ism-tafdil", "idafa-definiteness"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَحْسَنُ مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and the finest of it».", "«ve en güzeli».", segments=[seg("وَ", "wa", "conj"), seg("أَحْسَنُ", "ahsan", "noun"), pr3ms()]),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«what».", "«… olandır»."),
  tok("آذَنَ", "adhana", "verb", [K, "ism-mawsul", "form-iv-verbs"], "فِعْلٌ مَاضٍ — آذَنَ بِالشَّيْءِ: أَعْلَمَ بِهِ.", "«tells».", "«haber veren»."),
  tok("بِانْتِهَاءِ", "intiha", "noun", [K, "huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَانْتِهَاءِ مَجْرُورٌ، مُضَافٌ.", "«of the ending of».", "«bittiğini».", segments=[seg("بِ", "bi", "prep"), seg("انْتِهَاءِ", "intiha", "noun")]),
  tok("الْكَلَامِ", "kalam", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the speech».", "«sözün».", punct="،"),
 ] + ka_qawl(abu("إِسْحَاقَ", "ishaq", "«Ishaq» — Abu Ishaq al-Sabi, the secretary (d. 384 AH).", "«İshâk» — kâtip Ebû İshâk es-Sâbî (ö. 384).", "أَبُو إِسْحَاقَ الصَّابِئُ.", tags=["mamnu-min-sarf"])) + [
  tok("بَقِيتَ", "baqiya", "verb", [K, A, "insha-wa-tamanni", "naqis-verbs"], "فِعْلٌ مَاضٍ فِي مَعْنَى الدُّعَاءِ، وَالتَّاءُ فَاعِلٌ — بَقِيَ يَبْقَى.", "«may you last» — a mazi as a prayer.", "«bâkî ol» — dua manasında mâzî.", segments=[seg("بَقِي", "baqiya", "verb"), seg("تَ", "pron-2ms", "pron")]),
  tok("بَقَاءَ", "baqa", "noun", [K, "maful-mutlaq", "idafa-definiteness", "masdar"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ، مُضَافٌ.", "«the lasting of».", "«… kaldığı gibi»."),
  tok("الدَّهْرِ", "dahr", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«time».", "«zamanın»."),
  tok("يَا", "ya-nida", "part", [K, "vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O».", "«ey»."),
  tok("كَهْفَ", "kahf", "noun", [K, "vocative-munada", "idafa-definiteness"], "مُنَادًى مَنْصُوبٌ، مُضَافٌ — الْكَهْفُ: الْمَلْجَأُ.", "«refuge of» — the munada, annexed.", "«sığınağı» — muzâf münâdâ."),
  tok("أَهْلِهِ", "ahl", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its people».", "«ehlinin».", segments=[seg("أَهْلِ", "ahl", "noun"), pr3msi()], punct="*"),
  tok("وَهَذَا", "hadha", "pron", [K, "asma-al-ishara", "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهَذَا مُبْتَدَأٌ.", "«and this».", "«ve bu».", segments=[seg("وَ", "wa", "conj"), seg("هَذَا", "hadha", "pron")]),
  tok("دُعَاءٌ", "dua", "noun", [K, "mubtada-khabar", "masdar"], "خَبَرٌ مَرْفُوعٌ.", "«is a prayer».", "«bir duadır»."),
  tok("لِلْبَرِيَّةِ", "bariyya", "noun", [K, "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْبَرِيَّةِ مَجْرُورٌ — الْبَرِيَّةُ: الْخَلْقُ.", "«for creation».", "«mahlûkat için».", segments=[seg("لِ", "li", "prep"), seg("الْبَرِيَّةِ", "bariyya", "noun")]),
  tok("شَامِلُ", "shamil", "noun", [K, QF, "naat-sifa", "ism-fail"], "نَعْتٌ مَرْفُوعٌ — أُطْلِقَ لِلْقَافِيَةِ. الرَّوِيُّ اللَّامُ.", "«embracing» — rawi lam.", "«kapsayan» — revî lâm."),
 ]})
S[-1]["badi"] = [FR("husn-intiha", span(S[-1], "بَقِيتَ", "شَامِلُ"))]

# ----------- s23 — the book's last sentence (RESTORED)
S.append({"id": "s23", "translation": {
 "en": "And the openings and closings of the suras have come upon the finest and most complete faces of eloquence — as becomes plain to one who reflects on them with what has passed in mind. And the Talkhis is done." + R_EN,
 "tr": "Sûrelerin başları ve sonları belâgat vecihlerinin en güzeli ve en mükemmeli üzere gelmiştir — geçen kaideleri hatırda tutarak düşünene açıkça görünür. Telhîs burada biter." + R_TR},
 "tokens": [
  tok("وَقَدْ", "qad", "part", [K, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ لِلتَّحْقِيقِ.", "«and indeed».", "«ve gerçekten».", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("جَاءَتْ", "jaa", "verb", [K, "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«have come».", "«gelmiştir»."),
  tok("فَوَاتِحُ", "fatiha", "noun", [K, "fail", "idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — جَمْعُ فَاتِحَةٍ.", "«the openings of».", "«başları»."),
  tok("السُّوَرِ", "sura", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ سُورَةٍ.", "«the suras».", "«sûrelerin»."),
  tok("وَخَوَاتِمُهَا", "khatima", "noun", [K, "atf-nasaq", "idafa-definiteness", "jam-taksir"], "الْوَاوُ عَاطِفَةٌ، وَخَوَاتِمُ مَعْطُوفٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعُ خَاتِمَةٍ.", "«and their closings».", "«ve sonları».", segments=[seg("وَ", "wa", "conj"), seg("خَوَاتِمُ", "khatima", "noun"), pr3fs()]),
  tok("عَلَى", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«upon».", "«üzere»."),
  tok("أَحْسَنِ", "ahsan", "noun", [K, "huruf-jarr", "ism-tafdil", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the finest of».", "«en güzeli»."),
  tok("الْوُجُوهِ", "wajh", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the faces».", "«vecihlerin»."),
  tok("وَأَكْمَلِهَا", "akmal", "noun", [K, "atf-nasaq", "ism-tafdil", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَأَكْمَلِ مَعْطُوفٌ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and the most complete of them».", "«ve en mükemmeli».", segments=[seg("وَ", "wa", "conj"), seg("أَكْمَلِ", "akmal", "noun"), pr3fs()], punct="،"),
  tok("كَمَا", "kama", "part", [K, "huruf-jarr", "anwa-ma"], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ.", "«as».", "«… gibi».", segments=[seg("كَ", "ka", "part"), seg("مَا", "ma-masdariyya", "part")]),
  tok("يَظْهَرُ", "zahara", "verb", [K, "anwa-ma"], "مُضَارِعٌ مَرْفُوعٌ.", "«becomes plain».", "«açıkça görünür»."),
  tok("لِلْمُتَأَمِّلِ", "mutaammil", "noun", [K, "huruf-jarr", "ism-fail", "form-v-verbs"], "اللَّامُ حَرْفُ جَرٍّ، وَالْمُتَأَمِّلِ مَجْرُورٌ — اسْمُ فَاعِلِ تَأَمَّلَ.", "«to one who reflects».", "«düşünene».", segments=[seg("لِ", "li", "prep"), seg("الْمُتَأَمِّلِ", "mutaammil", "noun")]),
  tok("فِيهَا", "fi", "prep", [K, "huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ.", "«on them».", "«onlar üzerine».", segments=[seg("فِي", "fi", "prep"), pr3fs()]),
  tok("مَعَ", "maa", "noun", [K, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with».", "«… ile»."),
  tok("تَذَكُّرِ", "tadhakkur", "noun", [K, "idafa-definiteness", "masdar", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — مَصْدَرُ تَذَكَّرَ.", "«remembering».", "«hatırlama»."),
  tok("مَا", "ma-mawsula", "noun", [K, "ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ.", "«what».", "«… şeyi»."),
  tok("مَرَّ", "marra", "verb", [K, "ism-mawsul", "doubled-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ.", "«has passed».", "«geçen».", punct="."),
  tok("وَقَدْ", "qad", "part", [K, "qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ لِلتَّحْقِيقِ.", "«and indeed».", "«ve».", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("تَمَّ", "tamma", "verb", [K, "fail", "doubled-verbs"], "فِعْلٌ مَاضٍ — مُضَاعَفٌ.", "«is done».", "«tamamlandı»."),
  tok("التَّلْخِيصُ", "talkhis", "noun", [K, "fail", "masdar", "form-ii-verbs"], "فَاعِلٌ مَرْفُوعٌ — مَصْدَرُ لَخَّصَ: تَلْخِيصُ الْمِفْتَاحِ.", "«the Talkhis».", "«Telhîs».", punct="."),
 ]})

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "ibtida-open": need("ibtida-open", "ابْتِدَاء", "ب د أ", "noun", "the opening, the beginning (masdar of Form VIII ابْتَدَأَ) — حُسْنُ الِابْتِدَاءِ: the fine opening", "ibtidâ, başlangıç (iftiâl masdarı) — hüsn-i ibtidâ: güzel başlangıç", 4),
 "takhallus": need("takhallus", "تَخَلُّص", "خ ل ص", "noun", "the transition, the way out (masdar of Form V تَخَلَّصَ) — حُسْنُ التَّخَلُّصِ: the fine passage from the opening to the aim", "tahallus, geçiş (tefa''ul masdarı) — hüsn-i tahallus: girişten maksada güzel geçiş", 5),
 "iqtidab": need("iqtidab", "اقْتِضَاب", "ق ض ب", "noun", "iqtidab — a cutting-off (masdar of Form VIII اقْتَضَبَ): passing to the aim with no transition, the way of the ancients", "iktidâb — kesip atma (iftiâl masdarı): geçiş yapmadan maksada atlama, kadîmlerin yolu", 5),
 "istihlal": need("istihlal", "اسْتِهْلَال", "ه ل ل", "noun", "istihlal — the first cry (masdar of Form X اسْتَهَلَّ) — بَرَاعَةُ الِاسْتِهْلَالِ: the opening that hints at the whole", "istihlâl — ilk çığlık (istif'âl masdarı) — berâat-i istihlâl: bütüne işaret eden giriş", 5),
 "baraa": need("baraa", "بَرَاعَة", "ب ر ع", "noun", "excellence, mastery (masdar of بَرُعَ)", "üstünlük, ustalık (berua masdarı)", 4),
 "fatiha": need("fatiha", "فَاتِحَة", "ف ت ح", "noun", "an opening (ism fa'il, fem.; pl. فَوَاتِح — فَوَاتِحُ السُّوَرِ: the openings of the suras)", "açılış, başlangıç (ism-i fâil, müennes; ç. فَوَاتِح — fevâtihu's-suver)", 3, plural="فَوَاتِح"),
 "akmal": need("akmal", "أَكْمَل", "ك م ل", "noun", "more complete (the elative of كَامِل)", "daha mükemmel (kâmil'in ism-i tafdîli)", 3),
 "asahh": need("asahh", "أَصَحّ", "ص ح ح", "noun", "sounder, more correct (the elative of صَحِيح)", "daha sahih, daha doğru (sahîh'in ism-i tafdîli)", 3),
 "mutaammil": need("mutaammil", "مُتَأَمِّل", "أ م ل", "noun", "one who reflects (ism fa'il of Form V تَأَمَّلَ)", "düşünen, teemmül eden (tefa''ul ism-i fâili)", 4),
 "tadhakkur": need("tadhakkur", "تَذَكُّر", "ذ ك ر", "noun", "remembering (masdar of Form V تَذَكَّرَ)", "hatırlama (tefa''ul masdarı)", 3),
 "talkhis": need("talkhis", "تَلْخِيص", "ل خ ص", "noun", "a summary, an abridgement (masdar of Form II لَخَّصَ) — the name of this book", "telhis, özet (tef'îl masdarı) — bu kitabın adı", 3),
 "khitab": need("khitab", "خِطَاب", "خ ط ب", "noun", "address, speech (masdar of Form III خَاطَبَ) — فَصْلُ الْخِطَابِ: the decisive word, أَمَّا بَعْدُ", "hitap (mufâale masdarı) — faslu'l-hitâb: kesin söz, emmâ ba'du", 3),
 "jadir": need("jadir", "جَدِير", "ج د ر", "noun", "worthy of, fit for (فَعِيل; جَدِيرٌ بِـ)", "lâyık, uygun (fa'îl; cedîrun bi-)", 4),
 "tahiyya": need("tahiyya", "تَحِيَّة", "ح ي ي", "noun", "a greeting (masdar of Form II حَيَّا; pl. تَحِيَّات)", "selâm, tahiyye (tef'îl masdarı; ç. تَحِيَّات)", 3, plural="تَحِيَّات"),
 "tahnia": need("tahnia", "تَهْنِئَة", "ه ن أ", "noun", "a congratulation (masdar of Form II هَنَّأَ)", "tebrik, tehniye (tef'îl masdarı)", 4),
 "marthiya": need("marthiya", "مَرْثِيَة", "ر ث ي", "noun", "an elegy (pl. مَرَاثٍ)", "mersiye, ağıt (ç. مَرَاثٍ)", 4, plural="مَرَاثٍ"),
 "mulaama": need("mulaama", "مُلَاءَمَة", "ل أ م", "noun", "fitness, suitability (masdar of Form III لَاءَمَ)", "uygunluk, mülâemet (mufâale masdarı)", 4),
 "sabk": need("sabk", "سَبْك", "س ب ك", "noun", "casting, the mould of the phrasing (masdar of سَبَكَ)", "dökme, ifadenin kalıbı (sebeke masdarı)", 5),
 "mukhadram": need("mukhadram", "مُخَضْرَم", "خ ض ر م", "noun", "a mukhadram — a poet who lived in both the Jahiliyya and Islam (pl. مُخَضْرَمُونَ)", "muhadram — hem Câhiliye'yi hem İslâm'ı gören şair (ç. مُخَضْرَمُونَ)", 5),
 "jahiliyya": need("jahiliyya", "الْجَاهِلِيَّة", "ج ه ل", "noun", "the Jahiliyya — the age before Islam", "Câhiliye — İslâm öncesi çağ", 3),
 "fakhr": need("fakhr", "فَخْر", "ف خ ر", "noun", "boasting, pride (masdar of فَخَرَ)", "övünme, fahr (fahara masdarı)", 3),
 "furqa": need("furqa", "فُرْقَة", "ف ر ق", "noun", "parting, separation", "ayrılık, firkat", 3),
 "mawid": need("mawid", "مَوْعِد", "و ع د", "noun", "an appointed time, a promise (pl. مَوَاعِيد)", "vaad edilen vakit, randevu (ç. مَوَاعِيد)", 3, plural="مَوَاعِيد"),
 "muqatil": need("muqatil", "مُقَاتِل", None, "propn", "Muqatil — in Ibn Muqatil, the poet whose ill-omened opening the book blames", "Mukâtil — İbn Mukâtil adında; uğursuz girişini kitabın kınadığı şair", 6),
 "faraj": need("faraj", "الْفَرَج", None, "propn", "al-Faraj — in the kunya Abu l-Faraj", "Ferec — Ebü'l-Ferec künyesinde", 5),
 "said-name": need("said-name", "سَعِيد", None, "propn", "Saʿid — a man's name; here in an address «O Saʿid»", "Saîd — erkek adı; burada «ey Saîd» hitabında", 3),
 "qumis": need("qumis", "قُومَس", None, "propn", "Qumis — a region of northern Persia (Abu Tammam's bayt)", "Kūmis — kuzey İran'da bir bölge (Ebû Temmâm'ın beyti)", 6),
 "mahriyya": need("mahriyya", "الْمَهْرِيَّة", None, "noun", "the Mahri camels — the noble breed of Mahra (a nisba)", "Mehrî develeri — Mehre'nin asil cinsi (nisbe)", 6),
 "qud": need("qud", "قُود", "ق و د", "noun", "long-necked, sleek (pl. of أَقْوَد / قَوْدَاء — of camels)", "uzun boyunlu, ince (akvad / kavdâ'nın çoğulu — develer için)", 6),
 "khutwa": need("khutwa", "خُطْوَة", "خ ط و", "noun", "a stride, a step (pl. خُطًا / خُطُوَات)", "adım (ç. خُطًا / خُطُوَات)", 3, plural="خُطًا"),
 "matla": need("matla", "مَطْلَع", "ط ل ع", "noun", "a rising-place; the opening bayt of a poem (pl. مَطَالِع)", "doğuş yeri; kasidenin ilk beyti (ç. مَطَالِع)", 4, plural="مَطَالِع"),
 "jud": need("jud", "جُود", "ج و د", "noun", "generosity, open-handedness (masdar of جَادَ)", "cömertlik, cûd (câde masdarı)", 3),
 "munya": need("munya", "مُنْيَة", "م ن ي", "noun", "a wish, a desire (pl. مُنًى)", "dilek, arzu (ç. مُنًى)", 4, plural="مُنًى"),
 "ashyab": need("ashyab", "أَشْيَب", "ش ي ب", "noun", "grey-haired (أَفْعَل; pl. شِيب)", "ak saçlı, ihtiyar (ef'al; ç. شِيب)", 5, plural="شِيب"),
 "layla": need("layla", "لَيْلَة", "ل ي ل", "noun", "a night (pl. لَيَالٍ / لَيْلَات)", "gece (ç. لَيَالٍ)", 2, plural="لَيَالٍ"),
 "sarf-turn": need("sarf-turn", "صَرْف", "ص ر ف", "noun", "a turn of fortune — صُرُوفُ الدَّهْرِ: the turns of time (pl. صُرُوف)", "talihin dönüşü — surûfu'd-dehr: zamanın cilveleri (ç. صُرُوف)", 5, plural="صُرُوف"),
 "iqbal": need("iqbal", "إِقْبَال", "ق ب ل", "noun", "good fortune, a coming-forward (masdar of Form IV أَقْبَلَ)", "ikbal, talih (if'âl masdarı)", 4),
 "hadhari": need("hadhari", "حَذَارِ", "ح ذ ر", "noun", "«beware!» — an ism fiʿl of command on the pattern فَعَالِ, built on kasra", "«sakın!» — fe'âli vezninde emir ism-i fiili, kesre üzere mebnî", 6),
 "batsh": need("batsh", "بَطْش", "ب ط ش", "noun", "violence, a grip of force (masdar of بَطَشَ)", "şiddet, sert tutuş (bataşe masdarı)", 4),
 "fatk": need("fatk", "فَتْك", "ف ت ك", "noun", "slaughter, assassination (masdar of فَتَكَ)", "öldürme, suikast (feteke masdarı)", 5),
 "fam": need("fam", "فَم", "ف و ه", "noun", "a mouth — annexed it becomes فُو / فِي / فَا (a five-noun)", "ağız — muzâf olunca فُو / فِي / فَا olur (beş isimden)", 3),
 "mil": need("mil", "مِلْء", "م ل أ", "noun", "fullness, a fill — بِمِلْءِ فِيهَا: with a full mouth", "doluluk — bi-mil'i fîhâ: ağız dolusu", 4),
 "adhir": need("adhir", "عَاذِر", "ع ذ ر", "noun", "one who excuses (ism fa'il of عَذَرَ)", "mazur gören (azere'nin ism-i fâili)", 4),
 "taghi": need("taghi", "طَاغٍ", "ط غ ي", "noun", "a transgressor (ism fa'il of طَغَى; pl. طَاغُونَ)", "azgın, tâğî (tağâ'nın ism-i fâili; ç. طَاغُونَ)", 4, plural="طَاغُونَ"),
 "maab": need("maab", "مَآب", "أ و ب", "noun", "a resort, a place of return (ism makan of آبَ)", "dönüş yeri, meâb (âbe'nin ism-i mekânı)", 5),
 "kahf": need("kahf", "كَهْف", "ك ه ف", "noun", "a cave, a refuge (pl. كُهُوف)", "mağara, sığınak (ç. كُهُوف)", 3, plural="كُهُوف"),
 "baqa": need("baqa", "بَقَاء", "ب ق ي", "noun", "lasting, endurance (masdar of بَقِيَ)", "bekâ, kalıcılık (bakiye masdarı)", 3),
 "shamil": need("shamil", "شَامِل", "ش م ل", "noun", "embracing, all-inclusive (ism fa'il of شَمِلَ)", "kapsayan, şümullü (şemile'nin ism-i fâili)", 4),
 "shakur": need("shakur", "شَكُور", "ش ك ر", "noun", "very thankful (فَعُول — a sighat mubalagha)", "çok şükreden (fa'ûl — mübâlağa sîgası)", 4),
 "manzil": need("manzil", "مَنْزِل", "ن ز ل", "noun", "an abode, a lodging (ism makan; pl. مَنَازِل)", "konak, menzil (ism-i mekân; ç. مَنَازِل)", 3, plural="مَنَازِل"),
 "lam-taleel": need("lam-taleel", "لِ (التَّعْلِيل)", None, "part", "the lam of cause — «so that», followed by a mansub mudari", "ta'lîl lâmı — «-mesi için», ardından mansûb muzâri", 3),
 "taannaqa": need("taannaqa", "تَأَنَّقَ", "أ ن ق", "verb", "to take pains, to be exquisite in (Form V; تَأَنَّقَ فِي)", "özenmek, incelik göstermek (tefa''ul; teennaka fî)", 5),
 "ijtanaba": need("ijtanaba", "اجْتَنَبَ", "ج ن ب", "verb", "to shun, to avoid (Form VIII; اجْتَنَبَ يَجْتَنِبُ)", "kaçınmak, sakınmak (iftiâl; ictenebe yectenibu)", 4),
 "khalaa": need("khalaa", "خَلَعَ", "خ ل ع", "verb", "to cast off, to take off (خَلَعَ يَخْلَعُ)", "çıkarmak, atmak (halea yahlau)", 3),
 "anjaza": need("anjaza", "أَنْجَزَ", "ن ج ز", "verb", "to fulfil a promise (Form IV; أَنْجَزَ يُنْجِزُ)", "vaadi yerine getirmek (if'âl; encece yuncizu)", 4),
 "waada": need("waada", "وَعَدَ", "و ع د", "verb", "to promise (an assimilated verb; وَعَدَ يَعِدُ)", "vaad etmek (misâl; vaade yaidu)", 3),
 "amma-verb": need("amma-verb", "أَمَّ", "أ م م", "verb", "to head for, to make for (doubled; أَمَّ يَؤُمُّ)", "yönelmek, kastetmek (muzâaf; emme yeummu)", 4),
 "jawara": need("jawara", "جَاوَرَ", "ج و ر", "verb", "to neighbour, to dwell beside (Form III; جَاوَرَ يُجَاوِرُ)", "komşu olmak, yanında bulunmak (mufâale; câvere yucâviru)", 4),
 "qaruba": need("qaruba", "قَرُبَ", "ق ر ب", "verb", "to be near (قَرُبَ يَقْرُبُ)", "yakın olmak (karube yakrubu)", 3),
 "iftataha": need("iftataha", "افْتَتَحَ", "ف ت ح", "verb", "to open, to begin with (Form VIII; افْتَتَحَ يَفْتَتِحُ)", "açmak, başlamak (iftiâl; iftetaha yeftetihu)", 4),
 "ammala": need("ammala", "أَمَّلَ", "أ م ل", "verb", "to hope for (Form II; أَمَّلَ يُؤَمِّلُ)", "ummak (tef'îl; emmele yuemmilu)", 4),
 "adhana": need("adhana", "آذَنَ", "أ ذ ن", "verb", "to announce, to give notice of (Form IV; آذَنَ يُؤْذِنُ بِـ)", "bildirmek, haber vermek (if'âl; âzene yu'zinu bi-)", 5),
 "tamma": need("tamma", "تَمَّ", "ت م م", "verb", "to be complete, to be done (doubled; تَمَّ يَتِمُّ)", "tamamlanmak (muzâaf; temme yetimmu)", 3),
 "awla-grant": need("awla-grant", "أَوْلَى", "و ل ي", "verb", "to grant someone a favour (Form IV, naqis; أَوْلَى يُولِي — two objects: أَوْلَاهُ الْجَمِيلَ)", "birine iyilik etmek, lütfetmek (if'âl, nâkıs; evlâ yûlî — iki mef'ûl)", 5),
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

# ---------------------------------------------------------------- paradigms
def gem(bab_key, L, F, Lm, Fm, amr, masdar, fail, maful, pmz, pmd, note):
    b, w = _sg.BABS[bab_key]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(L, F), _sg.mudari14("َ", Lm, Fm), amr,
                     "يَ" + Lm + "َ", "يَ" + Lm + "َ", "تَ" + Lm + "َ", maful, pmz, pmd, note)
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "taannaqa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَأَنَّق", "تَأَنَّق", "تَأَنَّق", "تَأَنُّق", "مُتَأَنِّق", None, None, None, "تَأَنَّقَ فِي كَلَامِهِ: تَكَلَّفَ فِيهِ الْحُسْنَ."))
put_morph(mo, "ijtanaba", _sg.derived("الْبَابُ الثَّامِنُ: اِفْتَعَلَ يَفْتَعِلُ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِجْتَنَب", "جْتَنِب", "اِجْتَنِب", "اِجْتِنَاب", "مُجْتَنِب", "مُجْتَنَب", "اُجْتُنِبَ", "يُجْتَنَبُ", "اجْتَنَبَ الشَّيْءَ: تَرَكَهُ جَانِبًا — مَجْهُولُهُ اُجْتُنِبَ يُجْتَنَبُ."))
put_morph(mo, "khalaa", _sg.sound1("fataha", "خَلَع", "خْلَع", "اِخْلَع", "خَلْع", "خَالِع", "مَخْلُوع", "خُلِعَ", "يُخْلَعُ", "خَلَعَ الثَّوْبَ: نَزَعَهُ — مِنْ بَابِ فَتَحَ لِأَجْلِ حَرْفِ الْحَلْقِ."))
put_morph(mo, "anjaza", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَنْجَز", "نْجِز", "أَنْجِز", "إِنْجَاز", "مُنْجِز", "مُنْجَز", "أُنْجِزَ", "يُنْجَزُ", "أَنْجَزَ الْوَعْدَ: وَفَّى بِهِ."))
put_morph(mo, "waada", _sg.sound1("daraba", "وَعَد", "عِد", "عِد", "وَعْد", "وَاعِد", "مَوْعُود", "وُعِدَ", "يُوعَدُ", "مِثَالٌ وَاوِيٌّ: تُحْذَفُ وَاوُهُ فِي الْمُضَارِعِ وَالْأَمْرِ — يَعِدُ، عِدْ.", cls="مِثَالٌ وَاوِيٌّ"))
put_morph(mo, "amma-verb", gem("nasara", "أَمّ", "أَمَم", "ؤُمّ", "أْمُم", ["أُمَّ", "أُمَّا", "أُمُّوا", "أُمِّي", "أُمَّا", "اؤْمُمْنَ"], "أَمّ", "آمّ", "مَأْمُوم", "أُمَّ", "يُؤَمُّ", "أَمَّ الشَّيْءَ: قَصَدَهُ — مُضَاعَفٌ مِنْ بَابِ نَصَرَ."))
put_morph(mo, "jawara", _sg.derived(_sg.B3, _sg.W3, "ُ", "جَاوَر", "جَاوِر", "جَاوِر", "مُجَاوَرَة", "مُجَاوِر", "مُجَاوَر", "جُووِرَ", "يُجَاوَرُ", "جَاوَرَهُ: كَانَ جَارَهُ."))
put_morph(mo, "qaruba", _sg.sound1("karuma", "قَرُب", "قْرُب", "اُقْرُب", "قُرْب", "قَرِيب", None, None, None, "قَرُبَ يَقْرُبُ: دَنَا — مِنْ بَابِ حَسُنَ، وَصِفَتُهُ قَرِيبٌ."))
put_morph(mo, "iftataha", _sg.derived("الْبَابُ الثَّامِنُ: اِفْتَعَلَ يَفْتَعِلُ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِفْتَتَح", "فْتَتِح", "اِفْتَتِح", "اِفْتِتَاح", "مُفْتَتِح", "مُفْتَتَح", "اُفْتُتِحَ", "يُفْتَتَحُ", "افْتَتَحَ الْكَلَامَ بِكَذَا: بَدَأَهُ بِهِ — مَجْهُولُهُ اُفْتُتِحَ."))
put_morph(mo, "ammala", _sg.derived(_sg.B2, _sg.W2, "ُ", "أَمَّل", "ؤَمِّل", "أَمِّل", "تَأْمِيل", "مُؤَمِّل", "مُؤَمَّل", "أُمِّلَ", "يُؤَمَّلُ", "أَمَّلَ الشَّيْءَ: رَجَاهُ."))
put_morph(mo, "adhana", _sg.derived(_sg.B4, _sg.W4, "ُ", "آذَن", "ؤْذِن", "آذِن", "إِيذَان", "مُؤْذِن", "مُؤْذَن", "أُوذِنَ", "يُؤْذَنُ", "آذَنَ بِالشَّيْءِ: أَعْلَمَ بِهِ — أَصْلُهُ أَأْذَنَ، فَقُلِبَتِ الْهَمْزَةُ الثَّانِيَةُ أَلِفًا."))
put_morph(mo, "awla-grant", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَوْلَ", "ول", "i", "أَوْل", "إِيلَاء", "مُولٍ (الْمُولِي)", "مُولًى", "أُولِيَ", "يُولَى", "أَوْلَاهُ الْجَمِيلَ: أَعْطَاهُ إِيَّاهُ — نَاقِصٌ يَائِيٌّ مِنَ الْإِفْعَالِ، يَتَعَدَّى إِلَى مَفْعُولَيْنِ؛ مَجْزُومُهُ تُولِ."))
put_morph(mo, "tamma", gem("daraba", "تَمّ", "تَمَم", "تِمّ", "تْمِم", ["تِمَّ", "تِمَّا", "تِمُّوا", "تِمِّي", "تِمَّا", "اِتْمِمْنَ"], "تَمَام", "تَامّ", None, None, None, "تَمَّ يَتِمُّ: كَمُلَ — مُضَاعَفٌ مِنْ بَابِ ضَرَبَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch76 gloss+morph ok", len(GLOSS_ADD))

# ---------------------------------------------------------------- note
NOTE = {
 "id": "husn-al-ibtida-wal-takhallus-wal-intiha",
 "title": {"ar": "حُسْنُ الِابْتِدَاءِ وَالتَّخَلُّصِ وَالِانْتِهَاءِ", "en": "The fine opening, the fine transition and the fine close", "tr": "Hüsn-i ibtidâ, hüsn-i tahallus ve hüsn-i intihâ"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الخاتمة: فصل — ينبغي للمتكلم أن يتأنق في ثلاثة مواضع من كلامه: الابتداء والتخلص والانتهاء"],
 "question": {
  "en": ["Where must the speaker take special care? In THREE places, says the Talkhis: the OPENING, the TRANSITION and the CLOSE — so the speech is sweeter in wording, finer in mould and sounder in meaning. The opening is the first thing that strikes the ear: if it is fine the hearer leans in (Imruʾ al-Qays's «halt, let us weep»; Ashjaʿ's «a palace on which are greeting and peace»). What must be shunned there is the ILL OMEN (Ibn Muqatil to a sultan: «the tryst of your loved ones is tomorrow's parting»). The finest opening is the one that FITS THE AIM — baraʿat al-istihlal: Abu Muhammad's «good tidings! fortune has fulfilled what it promised» in a congratulation, Abu l-Faraj's «beware, beware of my violence» in an elegy.",
         "What is the TAKHALLUS? Passing from what the speech opened with — a description, a boast, a complaint — to the aim, with FITNESS between the two: Abu Tammam, from the road to the praise, «is it the rising-place of the sun you seek for us? — No, but the rising-place of generosity». Passing with NO fitness is IQTIDAB, the way of the Jahiliyya Arabs and the mukhadrams after them (Abu Tammam again: from grey hair straight to Abu Saʿid). Near the takhallus stand أَمَّا بَعْدُ after the hamd (called fasl al-khitab), the Qurʾan's هَذَا that turns from the blessed to the transgressors (Sad 55, 49), and the writers' هَذَا بَابٌ.",
         "What is the fine CLOSE? The end is the last thing the hearer keeps: Abu Tammam's «I am worthy, having reached you with my wishes — and you are worthy of what I hoped from you; if you grant me your grace, you are its people; if not, I excuse and I thank». The FINEST close is the one that ANNOUNCES the speech has ended: «may you last as time lasts, O refuge of its people — and this is a prayer that embraces all creation». The book seals itself the same way: the openings and closings of the suras came on the finest and most complete of faces — «and the Talkhis is done».",
         "What does the engine read? The authored husn-ibtida / baraat-istihlal / takhallus / husn-intiha frames name a span and the reader lights it, showing the ill omen's word, the fitness the takhallus keeps (or the iqtidab's cut), and the close's announcing word. The ʿaruḍ engine scans every bayt cited here (ṭawīl, kāmil, basīṭ, khafīf) and the QafiyaEngine names the rhyme letter; the ḍabṭ engine writes the vocative كَهْفَ, the ism fiʿl حَذَارِ, the elative مَطْلَعَ under the hamza of question, and the five-noun فِيهَا after مِلْءِ."],
  "tr": ["Konuşan nerede özen göstermeli? Telhîs'e göre ÜÇ yerde: BAŞLANGIÇ, GEÇİŞ ve BİTİŞ — söz lafızca daha tatlı, kalıpça daha güzel, manaca daha sahih olsun diye. Başlangıç kulağa ilk çarpandır: güzelse dinleyen yönelir (İmruülkays'ın «durun, ağlayalım»ı; Eşca'ın «üzerinde selâm ve tahiyye olan bir saray»ı). Orada kaçınılacak olan UĞURSUZLUKTUR (İbn Mukâtil'in bir sultana: «sevdiklerinin randevusu yarın ayrılıkla»). En güzel başlangıç MAKSADA UYAN'dır — berâat-i istihlâl: Ebû Muhammed'in tebrikte «müjde! ikbal vaadini yerine getirdi», Ebü'l-Ferec'in mersiyede «sakın, sakın şiddetimden».",
         "TAHALLUS nedir? Sözün başladığı vasıf, fahr yahut şikâyetten maksada, ikisi arasında UYGUNLUK gözeterek geçmek: Ebû Temmâm yoldan medhe, «bizi güneşin doğduğu yere mi götürmek istiyorsun? — Hayır, cömertliğin doğduğu yere». Uygunluk gözetmeden geçiş İKTİDÂB'dır; Câhiliye Araplarının ve ardından muhadramların yoludur (yine Ebû Temmâm: ak saçtan doğrudan Ebû Saîd'e). Tahallusa yakın olan: hamdden sonra أَمَّا بَعْدُ (faslu'l-hitâb denmiştir), Kur'ân'ın müttakîlerden tâğîlere dönen هَذَا'sı (Sâd 55, 49) ve kâtiplerin هَذَا بَابٌ'ı.",
         "Güzel BİTİŞ nedir? Son, dinleyende kalan son şeydir: Ebû Temmâm'ın «dileklerimle sana ulaştığım için lâyığım — sen de senden umduğuma lâyıksın; bana lütfunu verirsen ehlisin; vermezsen mazur görür ve şükrederim»i. EN GÜZEL bitiş sözün BİTTİĞİNİ DUYURANDIR: «zaman durdukça kal, ey ehlinin sığınağı — bu, bütün yaratılmışı kapsayan bir duadır». Kitap kendini de öyle mühürler: sûrelerin başları ve sonları vecihlerin en güzeli ve en mükemmeli üzere gelmiştir — «ve Telhîs tamamlandı».",
         "Motor neyi okur? Yazarın husn-ibtida / baraat-istihlal / takhallus / husn-intiha çerçeveleri bir pasaj adlandırır, okuyucu onu yakar: uğursuzluk kelimesini, tahallusun gözettiği uygunluğu (yahut iktidâbın kesişini) ve bitişin duyuran kelimesini gösterir. Arûz motoru burada anılan her beyti tef'île döker (tavîl, kâmil, basît, hafîf), QafiyaEngine revî harfini adlandırır; zapt motoru münâdâ كَهْفَ'yi, ism-i fiil حَذَارِ'yi, soru hemzesi altındaki مَطْلَعَ'yi ve مِلْءِ'den sonraki beş isimden فِيهَا'yı yazar."]},
 "plain": {
  "en": "Open well (no ill omen, and best if the opening hints at the aim), pass well from opening to aim (or cut straight to it like the ancients), and close well — best with a line that says the speech is over.",
  "tr": "Güzel başla (uğursuzluk olmasın, en iyisi başlangıç maksada işaret etsin), başlangıçtan maksada güzel geç (yahut kadîmler gibi doğrudan kes), güzel bitir — en iyisi sözün bittiğini söyleyen bir satırla."},
 "explanation": {
  "en": "يَنْبَغِي لِلْمُتَكَلِّمِ أَنْ يَتَأَنَّقَ فِي ثَلَاثَةِ مَوَاضِعَ مِنْ كَلَامِهِ: الِابْتِدَاءُ وَالتَّخَلُّصُ وَالِانْتِهَاءُ. The last chapter of the Talkhis leaves the figures and turns to the SHAPE of a whole speech: its first words, its hinge and its last words. The rulings are RESTORED from the received matn and marked. The two ayas print as the source prints them; the bayts of Imruʾ al-Qays, Ashjaʿ, Ibn Muqatil, Abu Muhammad, Abu l-Faraj, Abu Tammam and Abu Ishaq are the received readings. With this chapter the Talkhis is complete: seventy-six chapters, from the definition of eloquence to the openings and closings of the suras.",
  "tr": "يَنْبَغِي لِلْمُتَكَلِّمِ أَنْ يَتَأَنَّقَ فِي ثَلَاثَةِ مَوَاضِعَ مِنْ كَلَامِهِ: الِابْتِدَاءُ وَالتَّخَلُّصُ وَالِانْتِهَاءُ. Telhîs'in son bâbı sanatları bırakıp bütün bir sözün ŞEKLİNE döner: ilk kelimeleri, menteşesi ve son kelimeleri. Hükümler alınan metinden GERİ YAZILMIŞ ve işaretlenmiştir. İki âyet kaynağın basılı şekliyledir; İmruülkays, Eşca', İbn Mukâtil, Ebû Muhammed, Ebü'l-Ferec, Ebû Temmâm ve Ebû İshâk'ın beyitleri alınan okuyuşlardır. Bu bâbla Telhîs tamamlanır: belâgatin tarifinden sûrelerin baş ve sonlarına yetmiş altı bâb."},
 "examples": [
  {"ar": "قِفَا نَبْكِ مِنْ ذِكْرَى حَبِيبٍ وَمَنْزِلِ", "en": "Imruʾ al-Qays — the fine opening.", "tr": "İmruülkays — güzel başlangıç.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "مَوْعِدُ أَحْبَابِكَ بِالْفُرْقَةِ غَدُ", "en": "Ibn Muqatil — the ill omen to be shunned.", "tr": "İbn Mukâtil — kaçınılacak uğursuzluk.", "sourceStory": "talkhis-al-miftah", "sentence": "s6"},
  {"ar": "بُشْرَى فَقَدْ أَنْجَزَ الْإِقْبَالُ مَا وَعَدَا", "en": "Abu Muhammad — baraʿat al-istihlal in a congratulation.", "tr": "Ebû Muhammed — tebrikte berâat-i istihlâl.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "أَمَطْلَعَ الشَّمْسِ تَبْغِي أَنْ تَؤُمَّ بِنَا * فَقُلْتُ: كَلَّا وَلَكِنْ مَطْلَعَ الْجُودِ", "en": "Abu Tammam — the takhallus from the road to the praise.", "tr": "Ebû Temmâm — yoldan medhe tahallus.", "sourceStory": "talkhis-al-miftah", "sentence": "s12"},
  {"ar": "بَقِيتَ بَقَاءَ الدَّهْرِ يَا كَهْفَ أَهْلِهِ * وَهَذَا دُعَاءٌ لِلْبَرِيَّةِ شَامِلُ", "en": "Abu Ishaq — the close that announces the end.", "tr": "Ebû İshâk — bitişi duyuran son.", "sourceStory": "talkhis-al-miftah", "sentence": "s22"}],
 "commonMistakes": [
  {"wrong": "«İktidâb bir kusurdur, tahallus gibi güzel değildir»",
   "right": "«وَهُوَ مَذْهَبُ الْعَرَبِ الْجَاهِلِيَّةِ وَمَنْ يَلِيهِمْ مِنَ الْمُخَضْرَمِينَ — kadîmlerin yoludur, kınanmış değildir»",
   "why": {"en": "The book records the iqtidab as the practice of the ancients, not as a fault; the takhallus is the later poets' refinement, and some iqtidab «comes near» it.", "tr": "Kitap iktidâbı kadîmlerin uygulaması olarak kaydeder, kusur olarak değil; tahallus sonraki şairlerin inceliğidir, bazı iktidâb ona «yaklaşır»."}},
  {"wrong": "«Her güzel başlangıç berâat-i istihlâldir»",
   "right": "«وَأَحْسَنُهُ مَا نَاسَبَ الْمَقْصُودَ وَيُسَمَّى بَرَاعَةَ الِاسْتِهْلَالِ — yalnız maksada uyan başlangıç»",
   "why": {"en": "Baraʿat al-istihlal is the narrower thing: the opening that already hints at what the speech is for (a congratulation opening with «good tidings»).", "tr": "Berâat-i istihlâl daha dar bir şeydir: sözün neye dair olduğuna şimdiden işaret eden başlangıç (tebrikin «müjde» ile açılması)."}}],
 "relatedNotes": ["al-iqtibas-wal-tadmin", "sariqat-shiriyya", "ilm-al-arud", "al-qafiya"]}

ADD_EN = (" Chapter 76 (lines ~4820-4885, sahifa 166-169) — the LAST chapter: the three places of care (s1), the fine opening (s2-s4; Imruʾ al-Qays, Ashjaʿ), "
          "the ill omen (s5-s6; Ibn Muqatil), baraʿat al-istihlal (s7-s9; Abu Muhammad, Abu l-Faraj), the takhallus (s10-s12; Abu Tammam), the iqtidab and what "
          "comes near it (s13-s18; Abu Tammam; أَمَّا بَعْدُ, the Qurʾanic هَذَا of Sad 55 and 49, the writers' هَذَا بَابٌ), the close (s19-s22; Abu Tammam, Abu Ishaq) "
          "and the book's last sentence on the suras with its colophon وَقَدْ تَمَّ التَّلْخِيصُ (s23). The rulings are RESTORED from the received matn and marked. "
          "The `badi` frames husn-ibtida (sub husn / tatayyur), baraat-istihlal, takhallus (sub takhallus / iqtidab / fasl-khitab) and husn-intiha carry the span. "
          "With this chapter the Talkhis al-Miftah is COMPLETE: 76 chapters.")
ADD_TR = (" Yetmiş altıncı bâb (satır ~4820-4885, sahife 166-169) — SON bâb: özen gösterilecek üç yer (s1), güzel başlangıç (s2-s4; İmruülkays, Eşca'), "
          "uğursuzluk (s5-s6; İbn Mukâtil), berâat-i istihlâl (s7-s9; Ebû Muhammed, Ebü'l-Ferec), tahallus (s10-s12; Ebû Temmâm), iktidâb ve ona yaklaşan "
          "(s13-s18; Ebû Temmâm; أَمَّا بَعْدُ, Sâd 55 ve 49'un هَذَا'sı, kâtiplerin هَذَا بَابٌ'ı), bitiş (s19-s22; Ebû Temmâm, Ebû İshâk) ve kitabın sûrelere dair "
          "son cümlesi ile وَقَدْ تَمَّ التَّلْخِيصُ ketebesi (s23). Hükümler alınan metinden GERİ YAZILMIŞ ve işaretlenmiştir. `badi` çerçeveleri husn-ibtida "
          "(alt: husn / tatayyur), baraat-istihlal, takhallus (alt: takhallus / iqtidab / fasl-khitab) ve husn-intiha pasajı taşır. Bu bâbla Telhîsü'l-Miftâh "
          "TAMAMLANMIŞTIR: 76 bâb.")
write_out(76, S, TITLE, ADD_EN, ADD_TR, "4820-4885", GLOSS_ADD, notes=(NOTE,),
          related=(("al-iqtibas-wal-tadmin", ["husn-al-ibtida-wal-takhallus-wal-intiha"]), ("sariqat-shiriyya", ["husn-al-ibtida-wal-takhallus-wal-intiha"]),
                   ("ilm-al-badi", ["husn-al-ibtida-wal-takhallus-wal-intiha"])))
report(76, S, GLOSS_ADD, (NOTE,))
