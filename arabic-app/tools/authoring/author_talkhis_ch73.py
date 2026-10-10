# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 73: the KHATIMA opens — the poetic SARIQAT (the takings): when two poets agree (the general purpose is no
theft; the way of signifying is, unless everyone shares it), the two kinds of taking (plain and hidden), and the PLAIN kind: the naskh /
intihal (the words whole, blamed), the ighara / maskh (the order changed or part of the words taken) in its three grades — the second
better (praised), worse (blamed), or equal (the merit stays with the first). Source lines ~4617-4660 (sahifa 159-161).

  RESTORED (the source carries the rulings only in Turkish): s1-s8, s12-s14, s17, s20 — the received matn, marked sentence by sentence.
  The bayts are the source's own printed Arabic: Ma'n b. Aws (s10-s11, taken whole by Ibn al-Zubayr), Bashshar and Salm (s15-s16),
  Abu Tammam and al-Mutanabbi twice (s18-s19, s21-s22).

  python3 tools/authoring/author_talkhis_ch73.py
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

K = "sariqat-shiriyya"
A = "ilm-al-arud"
QF = "al-qafiya"
TITLE = {"ar": "الْخَاتِمَةُ — السَّرِقَاتُ الشِّعْرِيَّةُ: الظَّاهِرُ مِنْهَا", "en": "The khatima — the poetic takings: the plain kind", "tr": "Hâtime — şiir sirkatleri: zâhir olanı"}
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
def fi(tag, punct=None): return tok("فِي", "fi", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def pr3ms(): return seg("هُ", "pron-3ms", "pron")
def pr3msi(): return seg("هِ", "pron-3ms", "pron")
def qawl(name_full, name_lex, name_en, name_tr, tag, gr_extra=None, punct=":"):
    return [tok("كَقَوْلِ", "qawl", "noun", [tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ، مُضَافٌ.", "«as the saying of».", "«… sözü gibi».",
                segments=[seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun")]),
            tok(name_full, name_lex, "propn", [tag, "idafa-definiteness"] + (gr_extra or []), "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَمٌ.", name_en, name_tr, punct=punct)]

# ----------- s1 — the khatima (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "A CLOSING SECTION — on the poetic takings (sariqat) and what connects to them." + R_EN,
 "tr": "HÂTİME — şiir sirkatleri (çalıntıları) ve onlara bağlı olanlar hakkında." + R_TR},
 "tokens": [
  tok("خَاتِمَةٌ", "khatima", "noun", [K, "mubtada-khabar", "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ مَرْفُوعٌ: هَذِهِ خَاتِمَةٌ.", "«a closing section» — the khabar of an omitted «this is».", "«hâtime» — hazfedilmiş mübtedânın haberi: «bu bir hâtimedir»."),
  fi(K),
  tok("السَّرِقَاتِ", "sariqa", "noun", [K, "huruf-jarr", "jam-muannath-salim"], "مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the takings» — the sound feminine plural.", "«sirkatler» — cem-i müennes-i sâlim."),
  tok("الشِّعْرِيَّةِ", "shiri", "noun", [K, "naat-sifa", "ism-mansub"], "نَعْتٌ مَجْرُورٌ — اسْمٌ مَنْسُوبٌ إِلَى الشِّعْرِ.", "«poetic» — the nisba adjective.", "«şiirle ilgili» — nisbet sıfatı."),
  tok("وَمَا", "ma-mawsula", "pron", [K, "atf-nasaq", "ism-mawsul", "anwa-ma"], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَعْطُوفٌ عَلَى السَّرِقَاتِ فِي مَحَلِّ جَرٍّ.", "«and what» — the relative, joined to the takings.", "«ve … olan» — ism-i mevsûl, sirkatlere ma'tûf.",
      segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-mawsula", "pron")]),
  tok("يَتَّصِلُ", "ittasala", "verb", [K, "jumla-sifa", "form-viii-verbs", "mudari-marfu", "mithal-verbs"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«connects» — the sila of the relative; اِتَّصَلَ, Form VIII of وَصَلَ.", "«bağlanır» — mevsûlün sılası; اِتَّصَلَ, vasale'nin iftiâli."),
  tok("بِهَا", "bi", "prep", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to them».", "«onlara».", segments=[seg("بِ", "bi", "prep"), seg("هَا", "pron-3fs", "pron")]),
 ]})

# ----------- s2 — the agreement in the general purpose (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "The agreement of two poets, if it is in the PURPOSE in general — as describing the brave man as a lion and the generous one as the sea — is not counted a taking, for it is settled in minds and customs." + R_EN,
 "tr": "İki şairin ittifakı, GENEL bir maksatta olursa — cesuru arslan, cömerdi deniz diye vasıflamak gibi — sirkat sayılmaz; çünkü o, akıllarda ve âdetlerde yerleşmiştir." + R_TR},
 "tokens": [
  tok("اتِّفَاقُ", "ittifaq", "noun", [K, "mubtada-khabar", "idafa-definiteness", "masdar", "form-viii-verbs"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ اتَّفَقَ.", "«the agreement» — the mubtada.", "«ittifakı» — mübtedâ."),
  tok("الْقَائِلَيْنِ", "qail", "noun", [K, "idafa-definiteness", "al-muthanna", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«of the two sayers» — the dual.", "«iki söyleyenin» — tesniye."),
  tok("إِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer»."),
  tok("كَانَ", "kana", "verb", [K, "in-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it is» — the shart verb; its ism concealed.", "«olursa» — şart fiili; ismi gizli."),
  fi(K),
  tok("الْغَرَضِ", "gharad", "noun", [K, "huruf-jarr", "kana-wa-akhawatuha"], "مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«the purpose» — kana's khabar in the jarr phrase.", "«maksatta» — câr-mecrûr kânenin haberi."),
  tok("عَلَى", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«üzere»."),
  tok("الْعُمُومِ", "umum", "noun", [K, "huruf-jarr", "masdar"], "مَجْرُورٌ — عَلَى الْعُمُومِ: عَامًّا.", "«generality» — «in general».", "«umum» — «genel olarak»."),
  tok("كَوَصْفِ", "wasf", "noun", [K, "huruf-jarr", "idafa-definiteness", "masdar"], "الْكَافُ لِلتَّمْثِيلِ، وَوَصْفِ مَجْرُورٌ، مُضَافٌ.", "«as describing».", "«vasıflamak gibi».",
      segments=[seg("كَ", "ka", "part"), seg("وَصْفِ", "wasf", "noun")]),
  tok("الشُّجَاعِ", "shuja", "noun", [K, "idafa-definiteness", "sifa-mushabbaha"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the brave man».", "«cesuru»."),
  tok("بِالْأَسَدِ", "asad", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْأَسَدِ مَجْرُورٌ.", "«as a lion».", "«arslan diye».", segments=[seg("بِ", "bi", "prep"), seg("الْأَسَدِ", "asad", "noun")]),
  tok("وَالْجَوَادِ", "jawad", "noun", [K, "atf-nasaq", "sighat-mubalagha"], "الْوَاوُ عَاطِفَةٌ، وَالْجَوَادِ مَعْطُوفٌ عَلَى الشُّجَاعِ مَجْرُورٌ.", "«and the generous man» — joined to the brave.", "«ve cömerdi» — cesura ma'tûf.",
      segments=[seg("وَ", "wa", "conj"), seg("الْجَوَادِ", "jawad", "noun")]),
  tok("بِالْبَحْرِ", "bahr", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْبَحْرِ مَجْرُورٌ.", "«as the sea».", "«deniz diye».", segments=[seg("بِ", "bi", "prep"), seg("الْبَحْرِ", "bahr", "noun")]),
  tok("فَلَا", "la-nafiya", "part", [K, "in-shartiyya"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَلَا نَافِيَةٌ.", "«then … not» — the fa of the jawab.", "«o zaman … -mez» — cevap fâ'sı.",
      segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("يُعَدُّ", "adda-count", "verb", [K, "naib-al-fail", "doubled-verbs", "mudari-marfu"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ.", "«is (not) counted» — the passive; the jawab.", "«sayılmaz» — meçhul; cevap cümlesi."),
  tok("سَرِقَةً", "sariqa", "noun", [K, "mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — عَدَّهُ سَرِقَةً: عَدَّ يَنْصِبُ مَفْعُولَيْنِ.", "«a taking» — the second object of عَدَّ.", "«sirkat» — adde'nin ikinci mef'ûlü."),
  tok("لِتَقَرُّرِهِ", "taqarrur", "noun", [K, "lam-taleel", "idafa-definiteness", "masdar", "form-v-verbs"], "اللَّامُ لِلتَّعْلِيلِ، وَتَقَرُّرِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ تَقَرَّرَ.", "«because it is settled» — the lam of cause on the masdar.", "«yerleşmiş olduğu için» — ta'lîl lâmı masdar üzerinde.",
      segments=[seg("لِ", "li", "prep"), seg("تَقَرُّرِ", "taqarrur", "noun"), pr3msi()]),
  fi(K),
  tok("الْعُقُولِ", "aql", "noun", [K, "huruf-jarr", "jam-taksir"], "مَجْرُورٌ — جَمْعُ عَقْلٍ.", "«minds».", "«akıllarda»."),
  tok("وَالْعَادَاتِ", "ada", "noun", [K, "atf-nasaq", "jam-muannath-salim"], "الْوَاوُ عَاطِفَةٌ، وَالْعَادَاتِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ.", "«and customs».", "«ve âdetlerde».",
      segments=[seg("وَ", "wa", "conj"), seg("الْعَادَاتِ", "ada", "noun")]),
 ]})
S[-1]["badi"] = [{"kind": "tibaq", "sub": "ijab", "pair": [ix(S[-1], "الشُّجَاعِ"), ix(S[-1], "وَالْجَوَادِ")]}] if False else []

# ----------- s3 — the way of signifying (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "And if it is in the WAY OF SIGNIFYING it — then if people share in knowing it, it is like the first." + R_EN,
 "tr": "Ona DELÂLET YÖNÜNDE olursa — insanlar onu bilmekte ortaksa, birincisi gibidir." + R_TR},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».", segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("كَانَ", "kana", "verb", [K, "in-shartiyya", "kana-wa-akhawatuha"], "فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is».", "«olursa»."),
  fi(K),
  tok("وَجْهِ", "wajh", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — خَبَرُ كَانَ.", "«the way» — annexed.", "«yönünde» — muzâf."),
  tok("الدَّلَالَةِ", "dalala", "noun", [K, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of signifying».", "«delâletin»."),
  tok("عَلَيْهِ", "ala", "prep", [K, "huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — مُتَعَلِّقٌ بِالدَّلَالَةِ.", "«it» — what the way signifies.", "«ona» — delâletin mütealliki.", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("فَإِنِ", "in-shartiyya", "part", [K, "in-shartiyya"], "الْفَاءُ وَاقِعَةٌ فِي الْجَوَابِ، وَإِنْ حَرْفُ شَرْطٍ ثَانٍ — كُسِرَتِ النُّونُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«then if» — a second shart in the first's jawab; the nun's kasra for the two sakins.", "«o zaman eğer» — cevapta ikinci şart; iki sâkin için nûn kesreli.",
      segments=[seg("فَ", "fa", "conj"), seg("إِنِ", "in-shartiyya", "part")]),
  tok("اشْتَرَكَ", "ishtaraka", "verb", [K, "in-shartiyya", "form-viii-verbs"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ.", "«share» — the shart verb.", "«ortak olursa» — şart fiili."),
  tok("النَّاسُ", "nas", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«people» — the doer.", "«insanlar» — fâil."),
  fi(K),
  tok("مَعْرِفَتِهِ", "marifa", "noun", [K, "huruf-jarr", "idafa-definiteness", "masdar"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«knowing it».", "«onu bilmekte».", segments=[seg("مَعْرِفَتِ", "marifa", "noun"), pr3msi()]),
  tok("فَهُوَ", "huwa", "pron", [K, "in-shartiyya", "mubtada-khabar"], "الْفَاءُ وَاقِعَةٌ فِي الْجَوَابِ، وَهُوَ مُبْتَدَأٌ.", "«then it» — the jawab's mubtada.", "«o zaman o» — cevabın mübtedâsı.", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("كَالْأَوَّلِ", "awwal", "noun", [K, "huruf-jarr", "mubtada-khabar"], "الْكَافُ حَرْفُ جَرٍّ، وَالْأَوَّلِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«like the first» — the khabar.", "«birincisi gibi» — haber.", segments=[seg("كَ", "ka", "prep"), seg("الْأَوَّلِ", "awwal", "noun")]),
 ]})

# ----------- s4 — otherwise: precedence may be claimed (RESTORED)
S.append({"id": "s4", "translation": {
 "en": "Otherwise it is allowed that PRECEDENCE and SURPLUS be claimed in it." + R_EN,
 "tr": "Yoksa onda ÖNCELİK ve FAZLALIK iddia edilmesi câizdir." + R_TR},
 "tokens": [
  tok("وَإِلَّا", "illa", "part", [K, "in-shartiyya", "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَإِلَّا: إِنْ لَا — شَرْطٌ حُذِفَ فِعْلُهُ: وَإِنْ لَمْ يَشْتَرِكُوا.", "«otherwise» — إِنْ + لَا with the shart verb dropped.", "«yoksa» — إِنْ + لَا, şart fiili hazfedilmiş.",
      segments=[seg("وَ", "wa", "conj"), seg("إِلَّا", "illa", "part")]),
  tok("جَازَ", "jaza", "verb", [K, "in-shartiyya", "hollow-verbs"], "فِعْلٌ مَاضٍ — جَوَابُ الشَّرْطِ.", "«it is allowed» — the jawab.", "«câizdir» — cevap."),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — أَنْ يُدَّعَى: الِادِّعَاءُ، فَاعِلُ جَازَ.", "«that» — the masdar-an; the clause is the doer of «is allowed».", "«-ması» — masdariyye en; cümle câze'nin fâili."),
  tok("يُدَّعَى", "iddaa", "verb", [K, "an-masdariyya", "naib-al-fail", "form-viii-verbs", "naqis-verbs"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«be claimed» — the passive, its nasb estimated on the alif.", "«iddia edilmesi» — meçhul; nasbı elif üzerinde takdîrî."),
  tok("فِيهِ", "fi", "prep", [K, "huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«in it».", "«onda».", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("السَّبْقُ", "sabq", "noun", [K, "naib-al-fail", "masdar"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — مَصْدَرُ سَبَقَ.", "«precedence» — the passive's deputy.", "«öncelik» — nâib-i fâil."),
  tok("وَالزِّيَادَةُ", "ziyada", "noun", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالزِّيَادَةُ مَعْطُوفٌ مَرْفُوعٌ.", "«and surplus» — joined.", "«ve fazlalık» — ma'tûf.",
      segments=[seg("وَ", "wa", "conj"), seg("الزِّيَادَةُ", "ziyada", "noun")]),
 ]})

# ----------- s5 — the two kinds of the rare purpose (RESTORED)
S.append({"id": "s5", "translation": {
 "en": "And it is of two kinds: one RARE in itself, which only the elect know; and one COMMON, in which a working has been done that carries it out of the trite into the rare." + R_EN,
 "tr": "O da iki türlüdür: kendinde NÂDİR olup yalnız havâssın bildiği; ve AVÂMÎ olup içinde onu bayağılıktan garâbete çıkaran bir tasarruf yapılmış olan." + R_TR},
 "tokens": [
  tok("وَهُوَ", "huwa", "pron", [K, "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("ضَرْبَانِ", "darb", "noun", [K, "mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى.", "«two kinds» — the khabar, a dual.", "«iki türlüdür» — haber, tesniye.", punct=":"),
  tok("خَاصِّيٌّ", "khassi", "noun", [K, "badal", "ism-mansub"], "بَدَلُ تَفْصِيلٍ مِنْ ضَرْبَانِ مَرْفُوعٌ — مَنْسُوبٌ إِلَى الْخَاصَّةِ.", "«a rare one» — the badal of detail; the nisba of the elect.", "«nâdir olanı» — tafsil bedeli; havâssa nisbet."),
  fi(K),
  tok("نَفْسِهِ", "nafs", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in itself».", "«kendinde».", segments=[seg("نَفْسِ", "nafs", "noun"), pr3msi()]),
  tok("لَا", "la-nafiya", "part", [K, "jumla-sifa"], "حَرْفُ نَفْيٍ — وَالْجُمْلَةُ بَعْدَهُ نَعْتٌ لِخَاصِّيٍّ.", "«not» — the clause is the na't.", "«-mez» — cümle sıfattır."),
  tok("يَعْرِفُهُ", "arafa", "verb", [K, "jumla-sifa", "mudari-marfu", "istithna-mufarragh"], "مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«know it».", "«onu bilir».", segments=[seg("يَعْرِفُ", "arafa", "verb"), pr3ms()]),
  tok("إِلَّا", "illa", "part", [K, "istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«except» — the emptied exception.", "«-den başka» — müferrağ istisnâ."),
  tok("الْخَوَاصُّ", "khass", "noun", [K, "istithna-mufarragh", "fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — الِاسْتِثْنَاءُ مُفَرَّغٌ: جَمْعُ خَاصَّةٍ.", "«the elect» — the doer after the emptied illa.", "«havâss» — müferrağ illâdan sonra fâil.", punct="،"),
  tok("وَعَامِّيٌّ", "ammi", "noun", [K, "atf-nasaq", "ism-mansub"], "الْوَاوُ عَاطِفَةٌ، وَعَامِّيٌّ مَعْطُوفٌ عَلَى خَاصِّيٍّ مَرْفُوعٌ.", "«and a common one» — joined to the rare.", "«ve avâmî olanı» — nâdire ma'tûf.",
      segments=[seg("وَ", "wa", "conj"), seg("عَامِّيٌّ", "ammi", "noun")]),
  tok("تُصُرِّفَ", "tasarrafa", "verb", [K, "jumla-sifa", "naib-al-fail", "form-v-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ — وَالْجُمْلَةُ نَعْتٌ.", "«a working has been done» — the passive; the jarr phrase stands as its deputy.", "«tasarruf edilmiş» — meçhul; câr-mecrûr nâib-i fâildir."),
  tok("فِيهِ", "fi", "prep", [K, "huruf-jarr", "naib-al-fail"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«in it».", "«onda».", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("بِمَا", "ma-mawsula", "pron", [K, "huruf-jarr", "ism-mawsul", "anwa-ma"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«by what».", "«onu … -an şeyle».", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("أَخْرَجَهُ", "akhraja", "verb", [K, "ism-mawsul", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (الْعَائِدُ)، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةُ مَا.", "«carries it out» — the sila; the doer is the returning pronoun.", "«onu çıkaran» — sıla; fâil âid zamir.", segments=[seg("أَخْرَجَ", "akhraja", "verb"), pr3ms()]),
  tok("مِنَ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ — فُتِحَتِ النُّونُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  tok("الِابْتِذَالِ", "ibtidhal", "noun", [K, "huruf-jarr", "masdar", "form-viii-verbs"], "مَجْرُورٌ — مَصْدَرُ ابْتَذَلَ: صَيْرُورَةُ الْمَعْنَى مُبْتَذَلًا مَشْهُورًا.", "«the trite» — the masdar of Form VIII: being worn by common use.", "«bayağılık» — iftiâl masdarı: mananın ele düşmüşlüğü."),
  tok("إِلَى", "ila", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«into».", "«-e»."),
  tok("الْغَرَابَةِ", "gharaba", "noun", [K, "huruf-jarr", "masdar"], "مَجْرُورٌ.", "«the rare».", "«garâbete»."),
 ]})
S[-1]["badi"] = [{"kind": "tibaq", "sub": "ijab", "pair": [ix(S[-1], "خَاصِّيٌّ"), ix(S[-1], "وَعَامِّيٌّ")]},
                 {"kind": "tibaq", "sub": "ijab", "pair": [ix(S[-1], "الِابْتِذَالِ"), ix(S[-1], "الْغَرَابَةِ")]}]

# ----------- s6 — the two kinds of taking (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "And the TAKING is of two kinds: PLAIN and not plain." + R_EN,
 "tr": "AHZ (alma) iki türlüdür: ZÂHİR ve zâhir olmayan." + R_TR},
 "tokens": [
  tok("وَالْأَخْذُ", "akhdh", "noun", [K, "mubtada-khabar", "masdar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْأَخْذُ مُبْتَدَأٌ — مَصْدَرُ أَخَذَ.", "«and the taking» — the mubtada.", "«ve ahz» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("الْأَخْذُ", "akhdh", "noun")]),
  tok("ضَرْبَانِ", "darb", "noun", [K, "mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two kinds».", "«iki türlüdür».", punct=":"),
  tok("ظَاهِرٌ", "zahir", "noun", [K, "badal", "ism-fail"], "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ.", "«plain» — the badal of detail.", "«zâhir» — tafsil bedeli."),
  tok("وَغَيْرُ", "ghayr", "noun", [K, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَغَيْرُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and other than» — joined, annexed.", "«ve … olmayan» — ma'tûf, muzâf.", segments=[seg("وَ", "wa", "conj"), seg("غَيْرُ", "ghayr", "noun")]),
  tok("ظَاهِرٍ", "zahir", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«plain».", "«zâhir»."),
 ]})
S[-1]["badi"] = [{"kind": "tibaq", "sub": "salb", "pair": [ix(S[-1], "ظَاهِرٌ"), ix(S[-1], "ظَاهِرٍ")]}]

# ----------- s7 — the plain taking (RESTORED)
S.append({"id": "s7", "translation": {
 "en": "The PLAIN is that the meaning be taken whole — either with the wording whole, or part of it, or alone." + R_EN,
 "tr": "ZÂHİR olanı, mananın bütünüyle alınmasıdır — ya lafzın bütünüyle, ya bir kısmıyla, ya da tek başına." + R_TR},
 "tokens": [
  tok("فَالظَّاهِرُ", "zahir", "noun", [K, "mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالظَّاهِرُ مُبْتَدَأٌ.", "«the plain» — the mubtada.", "«zâhir olanı» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("الظَّاهِرُ", "zahir", "noun")]),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — أَنْ يُؤْخَذَ: خَبَرٌ.", "«that» — the clause is the khabar.", "«-sıdır» — cümle haber."),
  tok("يُؤْخَذَ", "akhadha", "verb", [K, "an-masdariyya", "naib-al-fail"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«be taken» — the passive in nasb.", "«alınması» — meçhul, mansûb."),
  tok("الْمَعْنَى", "mana", "noun", [K, "naib-al-fail", "ism-maqsur-manqus"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the meaning» — the deputy.", "«mananın» — nâib-i fâil."),
  tok("كُلُّهُ", "kull", "noun", [K, "tawkid", "idafa-definiteness"], "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«whole» — the tawkid.", "«bütünüyle» — te'kîd.", segments=[seg("كُلُّ", "kull", "noun"), pr3ms()]),
  tok("مَعَ", "maa", "noun", [K, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with».", "«ile»."),
  tok("اللَّفْظِ", "lafz", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the wording».", "«lafzın»."),
  tok("كُلِّهِ", "kull", "noun", [K, "tawkid", "idafa-definiteness"], "تَوْكِيدٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«whole».", "«bütünüyle».", segments=[seg("كُلِّ", "kull", "noun"), pr3msi()]),
  tok("أَوْ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya»."),
  tok("بَعْضِهِ", "bad", "noun", [K, "atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ عَلَى كُلِّهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«part of it».", "«bir kısmıyla».", segments=[seg("بَعْضِ", "bad", "noun"), pr3msi()]),
  tok("أَوْ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  tok("وَحْدَهُ", "wahda", "noun", [K, "hal", "idafa-definiteness"], "حَالٌ مَنْصُوبٌ: مُنْفَرِدًا، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«alone» — the hal.", "«tek başına» — hâl.", segments=[seg("وَحْدَ", "wahda", "noun"), pr3ms()]),
 ]})
S[-1]["badi"] = [{"kind": "taqsim", "sub": "tayin", "set": [ix(S[-1], "كُلِّهِ"), ix(S[-1], "بَعْضِهِ"), ix(S[-1], "وَحْدَهُ")]}] if False else []

# ----------- s8 — the naskh (RESTORED)
S.append({"id": "s8", "translation": {
 "en": "So if the wording is taken whole with no change to its order, it is BLAMED, for it is pure theft — and it is called NASKH (copying) and INTIHAL (plagiarism)." + R_EN,
 "tr": "Lafız, nazmı değiştirilmeden bütünüyle alınırsa MEZMÛMDUR; çünkü sırf hırsızlıktır — buna NESH (kopya) ve İNTİHÂL (başkasınınkini kendine mal etme) denir." + R_TR},
 "tokens": [
  tok("فَإِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "الْفَاءُ لِلتَّفْصِيلِ، وَإِنْ حَرْفُ شَرْطٍ.", "«so if».", "«eğer».", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("أُخِذَ", "akhadha", "verb", [K, "in-shartiyya", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ.", "«is taken» — the passive shart verb.", "«alınırsa» — meçhul şart fiili."),
  tok("اللَّفْظُ", "lafz", "noun", [K, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the wording» — the deputy.", "«lafız» — nâib-i fâil."),
  tok("كُلُّهُ", "kull", "noun", [K, "tawkid", "idafa-definiteness"], "تَوْكِيدٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«whole».", "«bütünüyle».", segments=[seg("كُلُّ", "kull", "noun"), pr3ms()]),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«with».", "«-den»."),
  tok("غَيْرِ", "ghayr", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«no» — «other than».", "«olmaksızın» — «başka»."),
  tok("تَغْيِيرٍ", "taghyir", "noun", [K, "idafa-definiteness", "masdar", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ غَيَّرَ.", "«change».", "«değiştirme»."),
  tok("لِنَظْمِهِ", "nazm", "noun", [K, "huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَنَظْمِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِتَغْيِيرٍ.", "«to its order».", "«nazmına».", segments=[seg("لِ", "li", "prep"), seg("نَظْمِ", "nazm", "noun"), pr3msi()]),
  tok("فَهُوَ", "huwa", "pron", [K, "in-shartiyya", "mubtada-khabar"], "الْفَاءُ وَاقِعَةٌ فِي الْجَوَابِ، وَهُوَ مُبْتَدَأٌ.", "«it is».", "«o … -dır».", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("مَذْمُومٌ", "madhmum", "noun", [K, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ ذَمَّ.", "«blamed» — the khabar.", "«mezmûm» — haber."),
  tok("لِأَنَّهُ", "anna", "part", [K, "inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا.", "«because it» — the lam of cause on أَنَّ with its ism.", "«çünkü o» — ta'lîl lâmı, enne ve ismi.",
      segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part"), pr3ms()]),
  tok("سَرِقَةٌ", "sariqa", "noun", [K, "inna-wa-akhawatuha"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«theft» — anna's khabar.", "«hırsızlık» — ennenin haberi."),
  tok("مَحْضَةٌ", "mahd", "noun", [K, "naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«pure».", "«sırf».", punct="،"),
  tok("وَيُسَمَّى", "samma", "verb", [K, "naib-al-fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُسَمَّى مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ.", "«and it is called».", "«ve buna … denir».", segments=[seg("وَ", "wa", "conj"), seg("يُسَمَّى", "samma", "verb")]),
  tok("نَسْخًا", "naskh-copy", "noun", [K, "mafulayn", "masdar"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — النَّسْخُ: النَّقْلُ حَرْفًا بِحَرْفٍ.", "«naskh — copying» — the second object of the naming.", "«nesh — kopya» — tesmiyenin ikinci mef'ûlü."),
  tok("وَانْتِحَالًا", "intihal", "noun", [K, "atf-nasaq", "masdar", "form-viii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَانْتِحَالًا مَعْطُوفٌ مَنْصُوبٌ — ادِّعَاءُ قَوْلِ الْغَيْرِ.", "«and intihal — claiming another's saying as one's own».", "«ve intihâl — başkasının sözünü kendine mal etmek».",
      segments=[seg("وَ", "wa", "conj"), seg("انْتِحَالًا", "intihal", "noun")]),
 ]})

# ----------- s9 — Ibn al-Zubayr and Ma'n b. Aws
S.append({"id": "s9", "translation": {
 "en": "As it is related that ʿAbdallah b. al-Zubayr did that with the two bayts of Maʿn b. Aws:",
 "tr": "Nitekim Abdullah b. Zübeyr'in bunu Ma'n b. Evs'in iki beytiyle yaptığı hikâye olunur:"},
 "tokens": [
  tok("كَمَا", "kama", "part", [K, "huruf-jarr", "anwa-ma"], "الْكَافُ حَرْفُ جَرٍّ وَمَا مَصْدَرِيَّةٌ.", "«as».", "«nitekim … gibi».", segments=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  tok("حُكِيَ", "haka", "verb", [K, "naib-al-fail", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — وَنَائِبُ الْفَاعِلِ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ.", "«it is related» — the passive; the أَنَّ-clause is its deputy.", "«hikâye olunur» — meçhul; enne cümlesi nâib-i fâil."),
  tok("أَنَّ", "anna", "part", [K, "inna-wa-akhawatuha", "inna-am-anna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — فُتِحَتْ لِأَنَّهَا مَعَ مَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ.", "«that» — fatha: the clause is a masdar.", "«-dığı» — fetha: cümle masdar hükmünde."),
  tok("عَبْدَ", "abd", "noun", [K, "inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ، مُضَافٌ.", "«ʿAbd» — anna's ism, annexed.", "«Abd» — ennenin ismi, muzâf."),
  tok("اللهِ", "allah", "propn", [K, "idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Allah».", "«Allah»."),
  tok("بْنَ", "ibn", "noun", [K, "naat-sifa", "idafa-definiteness"], "نَعْتٌ لِعَبْدِ اللهِ مَنْصُوبٌ، مُضَافٌ — حُذِفَتْ هَمْزَتُهُ بَيْنَ عَلَمَيْنِ.", "«son of» — the na't, its hamza dropped between two names.", "«oğlu» — sıfat; iki alem arasında hemzesi düşer."),
  tok("الزُّبَيْرِ", "zubayr", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَمٌ.", "«al-Zubayr».", "«Zübeyr»."),
  tok("فَعَلَ", "faala", "verb", [K, "inna-wa-akhawatuha"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«did» — anna's khabar.", "«yaptı» — ennenin haberi."),
  tok("ذَلِكَ", "dhalika", "pron", [K, "maful-bihi", "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«that» — the object.", "«bunu» — mef'ûl."),
  tok("بِبَيْتَيْ", "bayt", "noun", [K, "huruf-jarr", "al-muthanna", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَبَيْتَيْ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«with the two bayts of» — the dual, its nun dropped for the idafa.", "«iki beytiyle» — tesniye; izâfetle nûnu düşer.",
      segments=[seg("بِ", "bi", "prep"), seg("بَيْتَيْ", "bayt", "noun")]),
  tok("مَعْنِ", "man-aws", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَمٌ.", "«Maʿn».", "«Ma'n»."),
  tok("بْنِ", "ibn", "noun", [K, "naat-sifa", "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ، مُضَافٌ.", "«son of».", "«oğlu»."),
  tok("أَوْسٍ", "aws", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَمٌ.", "«Aws».", "«Evs».", punct=":"),
 ]})

# ----------- s10-s11 — Ma'n b. Aws (ṭawīl)
S.append({"id": "s10", "translation": {
 "en": "«If you do not deal justly with your brother, you will find him * on the edge of estrangement, if he has sense» (Maʿn b. Aws — a bayt of the ṭawīl).",
 "tr": "«Kardeşine insafla davranmazsan onu * hicranın kıyısında bulursun, aklı varsa» (Ma'n b. Evs — tavîl bahrinden bir beyit)."},
 "tokens": [
  tok("إِذَا", "idha", "noun", [K, A, "idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«if / when» — the conditional zarf.", "«-ince / -se» — şart manalı zarf."),
  tok("أَنْتَ", "anta", "pron", [K, "idha-shartiyya", "fail", "hadhf-wa-taqdir"], "ضَمِيرٌ مُنْفَصِلٌ فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ مَا بَعْدَهُ: إِذَا لَمْ تُنْصِفْ أَنْتَ.", "«you» — the doer of a dropped verb the next one explains.", "«sen» — sonrakinin açıkladığı hazfedilmiş fiilin fâili."),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-me-»."),
  tok("تُنْصِفْ", "ansafa", "verb", [K, "lam-jazim", "form-iv-verbs"], "مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — أَنْصَفَ: عَامَلَ بِالْإِنْصَافِ.", "«deal justly» — jussive after لَمْ; Form IV.", "«insaf etmezsen» — lem ile meczûm; if'âl."),
  tok("أَخَاكَ", "akh", "noun", [K, "maful-bihi", "five-nouns", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْأَلِفِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your brother» — the object, its nasb by the alif (the five nouns).", "«kardeşine» — mef'ûl; nasbı elifle (esmâ-i hamse).",
      segments=[seg("أَخَا", "akh", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("وَجَدْتَهُ", "wajada", "verb", [K, "idha-shartiyya", "mafulayn"], "الْوَاوُ زَائِدَةٌ أَوِ الْفَاءُ مُقَدَّرَةٌ، وَوَجَدْتَ فِعْلٌ مَاضٍ وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ — جَوَابُ إِذَا.", "«you will find him» — the jawab; the ha its first object.", "«onu … bulursun» — izânın cevabı; hâ ilk mef'ûl.",
      segments=[seg("وَجَدْتَ", "wajada", "verb"), pr3ms()], punct="*"),
  tok("عَلَى", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-de»."),
  tok("طَرَفِ", "taraf", "noun", [K, "huruf-jarr", "idafa-definiteness", "mafulayn"], "مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَوْضِعِ الْمَفْعُولِ الثَّانِي.", "«the edge» — the jarr phrase stands as the second object.", "«kıyısında» — câr-mecrûr ikinci mef'ûl yerinde."),
  tok("الْهِجْرَانِ", "hijran", "noun", [K, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ هَجَرَ.", "«of estrangement».", "«hicranın»."),
  tok("إِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ — جَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«if» — its jawab is what came before.", "«-se» — cevabı öncekidir."),
  tok("كَانَ", "kana", "verb", [K, "in-shartiyya", "kana-wa-akhawatuha"], "فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«he is».", "«ise»."),
  tok("يَعْقِلُ", "aqala", "verb", [K, QF, "kana-wa-akhawatuha", "mudari-marfu"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ كَانَ. الرَّوِيُّ اللَّامُ وَالْمَجْرَى الضَّمَّةُ.", "«has sense» — kana's khabar; the rhyme word: rawi lam, majra damma.", "«akleder» — kânenin haberi; kafiye kelimesi: revî lâm, mecrâ damme."),
 ]})
S.append({"id": "s11", "translation": {
 "en": "«and he will mount the sword's edge rather than that you wrong him, * when there is no way to step aside from the sword's blade».",
 "tr": "«ve senin ona zulmünden ise kılıcın keskinine biner — * kılıcın ağzından sapılacak yer yoksa»."},
 "tokens": [
  tok("وَيَرْكَبُ", "rakiba", "verb", [K, A, "atf-nasaq", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَرْكَبُ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and he mounts».", "«ve biner».", segments=[seg("وَ", "wa", "conj"), seg("يَرْكَبُ", "rakiba", "verb")]),
  tok("حَدَّ", "hadd", "noun", [K, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«the edge».", "«keskinine»."),
  tok("السَّيْفِ", "sayf", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of the sword».", "«kılıcın»."),
  tok("مِنْ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ — مِنْ أَنْ: بَدَلًا مِنْ أَنْ.", "«rather than».", "«-mektense»."),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that».", "«-mesi»."),
  tok("تَضِيمَهُ", "dama-wrong", "verb", [K, "an-masdariyya", "hollow-verbs"], "مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالْهَاءُ مَفْعُولٌ بِهِ — ضَامَ يَضِيمُ: ظَلَمَ.", "«you wrong him» — ضَامَ, hollow: to wrong.", "«ona zulmetmen» — dâme yedîmu, ecvef: zulmetmek.",
      segments=[seg("تَضِيمَ", "dama-wrong", "verb"), pr3ms()], punct="*"),
  tok("إِذَا", "idha", "noun", [K, "idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-ince»."),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not».", "«-me-»."),
  tok("يَكُنْ", "kana", "verb", [K, "lam-jazim", "kana-wa-akhawatuha", "hollow-verbs"], "مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ — حُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«there is (not)» — jussive; the waw fell before the sukun.", "«yoksa» — meczûm; iki sâkin için vâv düştü."),
  tok("عَنْ", "an", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("شَفْرَةِ", "shafra", "noun", [K, "huruf-jarr", "idafa-definiteness", "kana-wa-akhawatuha"], "مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُنْ مُقَدَّمٌ.", "«the blade» — kana's fronted khabar.", "«ağzından» — kânenin öne alınmış haberi."),
  tok("السَّيْفِ", "sayf", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of the sword».", "«kılıcın»."),
  tok("مَزْحَلُ", "mazhal", "noun", [K, QF, "kana-wa-akhawatuha"], "اسْمُ يَكُنْ مُؤَخَّرٌ مَرْفُوعٌ — اسْمُ مَكَانٍ مِنْ زَحَلَ: مَوْضِعُ التَّنَحِّي. الرَّوِيُّ اللَّامُ.", "«a place to step aside» — kana's delayed ism; ism makan.", "«sapılacak yer» — kânenin sona bırakılmış ismi; ism-i mekân."),
 ]})
S[-1]["badi"] = [{"kind": "sariqa", "sub": "zahir", "kind2": "naskh", "with": "s10", "grade": "madhmum"}] if False else []

# ----------- s12 — the synonym (RESTORED)
S.append({"id": "s12", "translation": {
 "en": "And likewise if his wording, whole or part, is replaced by what is synonymous with it." + R_EN,
 "tr": "Onun lafzının bütünü veya bir kısmı eş anlamlısıyla değiştirilirse de böyledir." + R_TR},
 "tokens": [
  tok("وَكَذَا", "kadha", "part", [K, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَكَذَا: كَذَلِكَ — خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: وَالْحُكْمُ كَذَا.", "«and likewise» — the khabar of an omitted «the ruling is».", "«böyledir de» — hazfedilmiş mübtedânın haberi.", segments=[seg("وَ", "wa", "conj"), seg("كَذَا", "kadha", "part")]),
  tok("إِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer»."),
  tok("بُدِّلَ", "baddala", "verb", [K, "in-shartiyya", "naib-al-fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ.", "«is replaced» — the passive shart verb.", "«değiştirilirse» — meçhul şart fiili."),
  tok("بِكَلَامِهِ", "kalam", "noun", [K, "huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَكَلَامِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — بَاءُ الْبَدَلِ: مَا يُتْرَكُ.", "«his wording» — the ba marks what is given up.", "«onun lafzı» — bedel bâ'sı: bırakılan.",
      segments=[seg("بِ", "bi", "prep"), seg("كَلَامِ", "kalam", "noun"), pr3msi()]),
  tok("كُلِّهِ", "kull", "noun", [K, "tawkid", "idafa-definiteness"], "تَوْكِيدٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«whole».", "«bütünü».", segments=[seg("كُلِّ", "kull", "noun"), pr3msi()]),
  tok("أَوْ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  tok("بَعْضِهِ", "bad", "noun", [K, "atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«part of it».", "«bir kısmı».", segments=[seg("بَعْضِ", "bad", "noun"), pr3msi()]),
  tok("مَا", "ma-mawsula", "pron", [K, "ism-mawsul", "naib-al-fail", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ: مَا يُرَادِفُهُ.", "«what» — the relative, the passive's deputy.", "«… olan şey» — mevsûl, nâib-i fâil."),
  tok("يُرَادِفُهُ", "radafa", "verb", [K, "ism-mawsul", "form-iii-verbs", "mudari-marfu"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةُ مَا: رَادَفَ: وَافَقَ فِي الْمَعْنَى.", "«is synonymous with it» — the sila; Form III.", "«onunla eş anlamlı olan» — sıla; mufâale.",
      segments=[seg("يُرَادِفُ", "radafa", "verb"), pr3ms()]),
 ]})

# ----------- s13 — the ighara (RESTORED)
S.append({"id": "s13", "translation": {
 "en": "And if it is with a change of its order, or part of the wording is taken, it is called IGHARA (a raid) and MASKH (a disfiguring)." + R_EN,
 "tr": "Nazmı değiştirilerek olursa, yahut lafzın bir kısmı alınırsa, buna İĞÂRE (yağma) ve MESH (bozarak dönüştürme) denir." + R_TR},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».", segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("كَانَ", "kana", "verb", [K, "in-shartiyya", "kana-wa-akhawatuha"], "فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (الْأَخْذُ).", "«it is».", "«olursa»."),
  tok("مَعَ", "maa", "noun", [K, "maful-fih", "idafa-definiteness", "kana-wa-akhawatuha"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — خَبَرُ كَانَ.", "«with» — kana's khabar.", "«ile» — kânenin haberi."),
  tok("تَغْيِيرِ", "taghyir", "noun", [K, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«a change».", "«değiştirme»."),
  tok("نَظْمِهِ", "nazm", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«of its order».", "«nazmının».", segments=[seg("نَظْمِ", "nazm", "noun"), pr3msi()]),
  tok("أَوْ", "aw", "conj", [K, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("أُخِذَ", "akhadha", "verb", [K, "atf-nasaq", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — مَعْطُوفٌ عَلَى كَانَ.", "«is taken» — joined to the shart verb.", "«alınırsa» — şart fiiline ma'tûf."),
  tok("بَعْضُ", "bad", "noun", [K, "naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ.", "«part» — the deputy.", "«bir kısmı» — nâib-i fâil."),
  tok("اللَّفْظِ", "lafz", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of the wording».", "«lafzın»."),
  tok("سُمِّيَ", "samma", "verb", [K, "in-shartiyya", "naib-al-fail", "mafulayn"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — جَوَابُ الشَّرْطِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«it is called» — the jawab.", "«… denir» — cevap."),
  tok("إِغَارَةً", "ighara", "noun", [K, "mafulayn", "masdar", "form-iv-verbs", "hollow-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — مَصْدَرُ أَغَارَ: شَنَّ الْغَارَةَ.", "«ighara — a raid» — the masdar of Form IV, hollow.", "«iğâre — yağma» — if'âl masdarı, ecvef."),
  tok("وَمَسْخًا", "maskh", "noun", [K, "atf-nasaq", "masdar"], "الْوَاوُ عَاطِفَةٌ، وَمَسْخًا مَعْطُوفٌ مَنْصُوبٌ — الْمَسْخُ: تَحْوِيلُ الصُّورَةِ إِلَى أَقْبَحَ.", "«and maskh — disfiguring» — turning a form into an uglier one.", "«ve mesh — bozarak dönüştürme» — sureti çirkinine çevirmek.",
      segments=[seg("وَ", "wa", "conj"), seg("مَسْخًا", "maskh", "noun")]),
 ]})

# ----------- s14 — the first grade: the second is better (RESTORED) + Bashshar
S.append({"id": "s14", "translation": {
 "en": "Then if the second is more eloquent, by its being marked with some merit, it is PRAISED — as the saying of Bashshar:" + R_EN,
 "tr": "İkincisi bir fazilete mahsus olmakla daha beliğ olursa MEMDÛHTUR — Beşşâr'ın şu sözü gibi:" + R_TR},
 "tokens": [
  tok("فَإِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "الْفَاءُ لِلتَّفْصِيلِ، وَإِنْ حَرْفُ شَرْطٍ.", "«then if».", "«eğer».", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("كَانَ", "kana", "verb", [K, "in-shartiyya", "kana-wa-akhawatuha"], "فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.", "«is».", "«olursa»."),
  tok("الثَّانِي", "thani", "noun", [K, "kana-wa-akhawatuha", "ism-maqsur-manqus"], "اسْمُ كَانَ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«the second» — kana's ism; a manqus.", "«ikincisi» — kânenin ismi; mankûs."),
  tok("أَبْلَغَ", "ablagh", "noun", [K, "kana-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"], "خَبَرُ كَانَ مَنْصُوبٌ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more eloquent» — kana's khabar; the elative, a diptote.", "«daha beliğ» — kânenin haberi; ism-i tafdîl, gayr-ı munsarif."),
  tok("لِاخْتِصَاصِهِ", "ikhtisas", "noun", [K, "lam-taleel", "idafa-definiteness", "masdar", "form-viii-verbs"], "اللَّامُ لِلتَّعْلِيلِ، وَاخْتِصَاصِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«by its being marked out».", "«mahsus olmasıyla».",
      segments=[seg("لِ", "li", "prep"), seg("اخْتِصَاصِ", "ikhtisas", "noun"), pr3msi()]),
  tok("بِفَضِيلَةٍ", "fadila", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَفَضِيلَةٍ مَجْرُورٌ.", "«with some merit».", "«bir faziletle».", segments=[seg("بِ", "bi", "prep"), seg("فَضِيلَةٍ", "fadila", "noun")]),
  tok("فَمَمْدُوحٌ", "mamduh", "noun", [K, "in-shartiyya", "hadhf-wa-taqdir", "ism-maful"], "الْفَاءُ وَاقِعَةٌ فِي الْجَوَابِ، وَمَمْدُوحٌ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: فَهُوَ مَمْدُوحٌ.", "«it is praised» — the jawab, its mubtada omitted.", "«memdûhtur» — cevap; mübtedâsı hazf.",
      segments=[seg("فَ", "fa", "conj"), seg("مَمْدُوحٌ", "mamduh", "noun")], punct="،"),
 ] + qawl("بَشَّارٍ", "bashshar", "«Bashshar» — Bashshar b. Burd.", "«Beşşâr» — Beşşâr b. Bürd.", K)})
S.append({"id": "s15", "translation": {
 "en": "«Whoever watches people warily does not win his need, * and the bold, ardent man wins the good things» (Bashshar — basīṭ).",
 "tr": "«İnsanları gözetleyen ihtiyacına eremez; * güzel şeyleri cesur, hırslı kişi kazanır» (Beşşâr — basît)."},
 "tokens": [
  tok("مَنْ", "man", "noun", [K, A, "in-shartiyya", "mubtada-khabar"], "اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«whoever» — the conditional noun, the mubtada.", "«kim … -se» — şart ismi, mübtedâ."),
  tok("رَاقَبَ", "raqaba", "verb", [K, "in-shartiyya", "form-iii-verbs"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«watches warily» — the shart verb; Form III.", "«gözetlerse» — şart fiili; mufâale."),
  tok("النَّاسَ", "nas", "noun", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«people».", "«insanları»."),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not».", "«-mez»."),
  tok("يَظْفَرْ", "zafira", "verb", [K, "lam-jazim", "in-shartiyya"], "مُضَارِعٌ مَجْزُومٌ بِلَمْ — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ: ظَفِرَ بِهِ: نَالَهُ.", "«win» — jussive; the jawab clause.", "«eremez» — meczûm; cevap cümlesi."),
  tok("بِحَاجَتِهِ", "haja", "noun", [K, "huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَحَاجَتِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his need».", "«ihtiyacına».", segments=[seg("بِ", "bi", "prep"), seg("حَاجَتِ", "haja", "noun"), pr3msi()], punct="*"),
  tok("وَفَازَ", "faza", "verb", [K, "atf-nasaq", "hollow-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَفَازَ فِعْلٌ مَاضٍ — فَازَ يَفُوزُ.", "«and wins» — hollow.", "«ve kazanır» — ecvef.", segments=[seg("وَ", "wa", "conj"), seg("فَازَ", "faza", "verb")]),
  tok("بِالطَّيِّبَاتِ", "tayyib", "noun", [K, "huruf-jarr", "jam-muannath-salim"], "الْبَاءُ حَرْفُ جَرٍّ، وَالطَّيِّبَاتِ مَجْرُورٌ بِالْكَسْرَةِ.", "«the good things».", "«güzel şeyleri».", segments=[seg("بِ", "bi", "prep"), seg("الطَّيِّبَاتِ", "tayyib", "noun")]),
  tok("الْفَاتِكُ", "fatik", "noun", [K, "fail", "ism-fail"], "فَاعِلٌ مَرْفُوعٌ — الْفَاتِكُ: الْجَرِيءُ.", "«the bold man» — the doer, delayed.", "«cesur kişi» — fâil, sona bırakılmış."),
  tok("اللَّهِجُ", "lahij", "noun", [K, QF, "naat-sifa", "sifa-mushabbaha"], "نَعْتٌ مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ: الْمُولَعُ الْحَرِيصُ. الرَّوِيُّ الْجِيمُ.", "«ardent» — the na't; rhyme: rawi jim.", "«hırslı» — sıfat; kafiye: revî cîm."),
 ]})
S.append({"id": "s16", "translation": {
 "en": "And the saying of Salm: «Whoever watches people warily dies of worry, * and the daring man wins pleasure» — taken from Bashshar's bayt, and more eloquent than it: an ighara that is praised.",
 "tr": "Ve Selm'in: «İnsanları gözetleyen tasadan ölür; * lezzete cüretkâr olan erer» sözü — Beşşâr'ın beytinden alınmış ve ondan daha beliğ: memdûh bir iğâre."},
 "tokens": [
  tok("وَقَوْلِ", "qawl", "noun", [K, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَقَوْلِ مَعْطُوفٌ عَلَى قَوْلِ بَشَّارٍ مَجْرُورٌ، مُضَافٌ.", "«and the saying of».", "«ve … sözü».", segments=[seg("وَ", "wa", "conj"), seg("قَوْلِ", "qawl", "noun")]),
  tok("سَلْمٍ", "salm", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — سَلْمٌ الْخَاسِرُ، تِلْمِيذُ بَشَّارٍ.", "«Salm» — Salm al-Khasir, Bashshar's pupil.", "«Selm» — Selm el-Hâsir, Beşşâr'ın talebesi.", punct=":"),
  tok("مَنْ", "man", "noun", [K, A, "in-shartiyya", "mubtada-khabar"], "اسْمُ شَرْطٍ مُبْتَدَأٌ.", "«whoever».", "«kim»."),
  tok("رَاقَبَ", "raqaba", "verb", [K, "in-shartiyya", "form-iii-verbs"], "فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.", "«watches warily».", "«gözetlerse»."),
  tok("النَّاسَ", "nas", "noun", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«people».", "«insanları»."),
  tok("مَاتَ", "mata", "verb", [K, "in-shartiyya", "hollow-verbs"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ — جَوَابُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«dies» — the jawab.", "«ölür» — cevap."),
  tok("هَمًّا", "hamm", "noun", [K, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ — أَوْ مَفْعُولٌ لِأَجْلِهِ: مِنَ الْهَمِّ.", "«of worry» — the tamyiz (or the object of cause).", "«tasadan» — temyîz (yahut mef'ûlün leh).", punct="*"),
  tok("وَفَازَ", "faza", "verb", [K, "atf-nasaq", "hollow-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَفَازَ فِعْلٌ مَاضٍ.", "«and wins».", "«ve erer».", segments=[seg("وَ", "wa", "conj"), seg("فَازَ", "faza", "verb")]),
  tok("بِاللَّذَّةِ", "ladhdha", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَاللَّذَّةِ مَجْرُورٌ.", "«pleasure».", "«lezzete».", segments=[seg("بِ", "bi", "prep"), seg("اللَّذَّةِ", "ladhdha", "noun")]),
  tok("الْجَسُورُ", "jasur", "noun", [K, QF, "fail", "sighat-mubalagha"], "فَاعِلٌ مَرْفُوعٌ — صِيغَةُ مُبَالَغَةٍ عَلَى فَعُولٍ: الْجَرِيءُ. الرَّوِيُّ الرَّاءُ.", "«the daring man» — the doer; فَعُول; rhyme: rawi ra.", "«cüretkâr» — fâil; fe'ûl vezni; kafiye: revî râ."),
 ]})
S[-1]["badi"] = [{"kind": "sariqa", "sub": "zahir", "kind2": "ighara", "with": "s15", "grade": "mamduh"}]

# ----------- s17 — the second grade: worse (RESTORED) + Abu Tammam
S.append({"id": "s17", "translation": {
 "en": "And if it is below it, it is BLAMED — as the saying of Abu Tammam:" + R_EN,
 "tr": "Ondan aşağı olursa MEZMÛMDUR — Ebû Temmâm'ın şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».", segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("كَانَ", "kana", "verb", [K, "in-shartiyya", "kana-wa-akhawatuha"], "فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (الثَّانِي).", "«it is».", "«olursa»."),
  tok("دُونَهُ", "duna", "noun", [K, "maful-fih", "idafa-definiteness", "kana-wa-akhawatuha"], "ظَرْفٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرُ كَانَ.", "«below it» — kana's khabar.", "«ondan aşağı» — kânenin haberi.", segments=[seg("دُونَ", "duna", "noun"), pr3ms()]),
  tok("فَمَذْمُومٌ", "madhmum", "noun", [K, "in-shartiyya", "hadhf-wa-taqdir", "ism-maful"], "الْفَاءُ وَاقِعَةٌ فِي الْجَوَابِ، وَمَذْمُومٌ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ.", "«it is blamed».", "«mezmûmdur».", segments=[seg("فَ", "fa", "conj"), seg("مَذْمُومٌ", "madhmum", "noun")], punct="،"),
 ] + qawl("أَبِي", "abu-tammam", "«Abu» — Abu Tammam.", "«Ebû» — Ebû Temmâm.", K, ["five-nouns"], punct=None) + [
  tok("تَمَّامٍ", "abu-tammam", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْكُنْيَةُ.", "«Tammam».", "«Temmâm».", punct=":")]})
S.append({"id": "s18", "translation": {
 "en": "«Far be it — time will not bring the like of him; * indeed time is niggardly with the like of him» (Abu Tammam — kāmil).",
 "tr": "«Heyhât — zaman onun benzerini getirmez; * gerçekten zaman onun benzerine cimridir» (Ebû Temmâm — kâmil)."},
 "tokens": [
  tok("هَيْهَاتَ", "hayhat", "noun", [K, A, "ism-fil"], "اسْمُ فِعْلٍ مَاضٍ بِمَعْنَى بَعُدَ، مَبْنِيٌّ عَلَى الْفَتْحِ، وَفَاعِلُهُ مُسْتَتِرٌ.", "«far be it» — an ism fi'l meaning «it is far».", "«heyhât» — «uzak oldu» manasında ism-i fiil."),
  tok("لَا", "la-nafiya", "part", [K, "hal-ma-man"], "حَرْفُ نَفْيٍ.", "«not».", "«-mez»."),
  tok("يَأْتِي", "ata", "verb", [K, "mudari-marfu", "naqis-verbs"], "مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«brings».", "«getirir»."),
  tok("الزَّمَانُ", "zaman", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«time».", "«zaman»."),
  tok("بِمِثْلِهِ", "mithl", "noun", [K, "huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَمِثْلِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«the like of him».", "«onun benzerini».", segments=[seg("بِ", "bi", "prep"), seg("مِثْلِ", "mithl", "noun"), pr3msi()], punct="*"),
  tok("إِنَّ", "inna", "part", [K, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«indeed».", "«gerçekten»."),
  tok("الزَّمَانَ", "zaman", "noun", [K, "inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ.", "«time» — inna's ism.", "«zaman» — innenin ismi."),
  tok("بِمِثْلِهِ", "mithl", "noun", [K, "huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَمِثْلِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِبَخِيلٍ.", "«with the like of him».", "«onun benzerine».", segments=[seg("بِ", "bi", "prep"), seg("مِثْلِ", "mithl", "noun"), pr3msi()]),
  tok("لَبَخِيلُ", "bakhil", "noun", [K, QF, "inna-wa-akhawatuha", "sifa-mushabbaha"], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَبَخِيلُ خَبَرُ إِنَّ مَرْفُوعٌ — نُوِّنَ فِي الْأَصْلِ وَأُطْلِقَ لِلْقَافِيَةِ. الرَّوِيُّ اللَّامُ، وَالرِّدْفُ الْيَاءُ.", "«is niggardly» — inna's khabar with the sliding lam; the rhyme drops its tanwin.", "«cimridir» — innenin haberi, kayan lâm ile; kafiye tenvini bırakır.",
      segments=[seg("لَ", "la-ibtida", "part"), seg("بَخِيلُ", "bakhil", "noun")]),
 ]})
S.append({"id": "s19", "translation": {
 "en": "And the saying of Abu l-Tayyib: «His generosity infected time, so time grew generous through him — * yet time may well be niggardly with him» — taken from Abu Tammam's bayt and below it: an ighara that is blamed.",
 "tr": "Ve Ebü't-Tayyib'in: «Onun cömertliği zamana bulaştı da zaman onunla cömert oldu; * gerçi zaman ona cimri olabilir» sözü — Ebû Temmâm'ın beytinden alınmış ve ondan aşağı: mezmûm bir iğâre."},
 "tokens": [
  tok("وَقَوْلِ", "qawl", "noun", [K, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَقَوْلِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the saying of».", "«ve … sözü».", segments=[seg("وَ", "wa", "conj"), seg("قَوْلِ", "qawl", "noun")]),
  tok("أَبِي", "abu-tayyib", "propn", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«Abu» — the five nouns.", "«Ebû» — esmâ-i hamse."),
  tok("الطَّيِّبِ", "abu-tayyib", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو الطَّيِّبِ الْمُتَنَبِّي.", "«l-Tayyib» — al-Mutanabbi.", "«et-Tayyib» — Mütenebbî.", punct=":"),
  tok("أَعْدَى", "ada-infect", "verb", [K, A, "form-iv-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ — أَعْدَى: نَقَلَ الْعَدْوَى.", "«infected» — Form IV of the naqis root.", "«bulaştırdı» — if'âl, nâkıs.", segments=[seg("أَعْدَى", "ada-infect", "verb")]),
  tok("الزَّمَانَ", "zaman", "noun", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ مُقَدَّمٌ عَلَى الْفَاعِلِ.", "«time» — the object, before its doer.", "«zamana» — mef'ûl, fâilden önce."),
  tok("سَخَاؤُهُ", "sakha", "noun", [K, "fail", "idafa-definiteness", "ism-mamdud"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَمْدُودٌ: سَخَاء.", "«his generosity» — the doer; a mamdud.", "«cömertliği» — fâil; memdûd.", segments=[seg("سَخَاؤُ", "sakha", "noun"), pr3ms()]),
  tok("فَسَخَا", "sakha-verb", "verb", [K, "atf-nasaq", "naqis-verbs"], "الْفَاءُ عَاطِفَةٌ لِلتَّعْقِيبِ، وَسَخَا فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (الزَّمَانُ) — سَخَا يَسْخُو: جَادَ.", "«so it grew generous» — the fa of sequence; naqis verb.", "«böylece cömert oldu» — ta'kîb fâ'sı; nâkıs fiil.", segments=[seg("فَ", "fa", "conj"), seg("سَخَا", "sakha-verb", "verb")]),
  tok("بِهِ", "bi", "prep", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«through him».", "«onunla».", segments=[seg("بِ", "bi", "prep"), pr3msi()], punct="*"),
  tok("وَلَقَدْ", "qad", "part", [K, "qad-harf", "insha-wa-tamanni"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَاللَّامُ لِلتَّوْكِيدِ، وَقَدْ حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ: رُبَّمَا.", "«yet it may well» — قَدْ with the mudari: «sometimes».", "«gerçi … -bilir» — muzâri ile kad: taklîl.",
      segments=[seg("وَ", "wa", "conj"), seg("لَ", "la-ibtida", "part"), seg("قَدْ", "qad", "part")]),
  tok("يَكُونُ", "kana", "verb", [K, "kana-wa-akhawatuha", "hollow-verbs", "mudari-marfu"], "مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«is».", "«olur»."),
  tok("بِهِ", "bi", "prep", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — مُتَعَلِّقٌ بِبَخِيلًا.", "«with him».", "«ona».", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("الزَّمَانُ", "zaman", "noun", [K, "kana-wa-akhawatuha"], "اسْمُ يَكُونُ مَرْفُوعٌ.", "«time» — kana's ism.", "«zaman» — kânenin ismi."),
  tok("بَخِيلَا", "bakhil", "noun", [K, QF, "kana-wa-akhawatuha", "sifa-mushabbaha"], "خَبَرُ يَكُونُ مَنْصُوبٌ — أُبْدِلَ التَّنْوِينُ أَلِفَ الْإِطْلَاقِ لِلْقَافِيَةِ. الرَّوِيُّ اللَّامُ، وَالْوَصْلُ الْأَلِفُ.", "«niggardly» — kana's khabar; the rhyme's alif of itlaq for the tanwin.", "«cimri» — kânenin haberi; tenvin yerine ıtlak elifi."),
 ]})
S[-1]["badi"] = [{"kind": "sariqa", "sub": "zahir", "kind2": "ighara", "with": "s18", "grade": "madhmum"},
                 {"kind": "tibaq", "sub": "ijab", "pair": [ix(S[-1], "فَسَخَا"), ix(S[-1], "بَخِيلَا")]}]

# ----------- s20 — the third grade: equal (RESTORED) + Abu Tammam
S.append({"id": "s20", "translation": {
 "en": "And if it is its equal, it is farther from blame — and the merit is the first's — as the saying of Abu Tammam:" + R_EN,
 "tr": "Onun dengi olursa zemden uzaktır — fazilet ise birincinindir — Ebû Temmâm'ın şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».", segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  tok("كَانَ", "kana", "verb", [K, "in-shartiyya", "kana-wa-akhawatuha"], "فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is».", "«olursa»."),
  tok("مِثْلَهُ", "mithl", "noun", [K, "kana-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ كَانَ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its equal» — kana's khabar.", "«onun dengi» — kânenin haberi.", segments=[seg("مِثْلَ", "mithl", "noun"), pr3ms()]),
  tok("فَأَبْعَدُ", "abad", "noun", [K, "in-shartiyya", "hadhf-wa-taqdir", "ism-tafdil"], "الْفَاءُ وَاقِعَةٌ فِي الْجَوَابِ، وَأَبْعَدُ خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: فَهُوَ أَبْعَدُ — اسْمُ تَفْضِيلٍ.", "«it is farther» — the jawab; the elative.", "«daha uzaktır» — cevap; ism-i tafdîl.", segments=[seg("فَ", "fa", "conj"), seg("أَبْعَدُ", "abad", "noun")]),
  tok("مِنَ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("الذَّمِّ", "dhamm", "noun", [K, "huruf-jarr", "masdar"], "مَجْرُورٌ.", "«blame».", "«zemden».", punct="،"),
  tok("وَالْفَضْلُ", "fadl", "noun", [K, "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْفَضْلُ مُبْتَدَأٌ.", "«and the merit» — the mubtada.", "«fazilet ise» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("الْفَضْلُ", "fadl", "noun")]),
  tok("لِلْأَوَّلِ", "awwal", "noun", [K, "huruf-jarr", "mubtada-khabar"], "اللَّامُ حَرْفُ جَرٍّ، وَالْأَوَّلِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is the first's» — the khabar.", "«birincinindir» — haber.", segments=[seg("لِ", "li", "prep"), seg("الْأَوَّلِ", "awwal", "noun")], punct="،"),
 ] + qawl("أَبِي", "abu-tammam", "«Abu» — Abu Tammam.", "«Ebû» — Ebû Temmâm.", K, ["five-nouns"], punct=None) + [
  tok("تَمَّامٍ", "abu-tammam", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Tammam».", "«Temmâm».", punct=":")]})
S.append({"id": "s21", "translation": {
 "en": "«Had the seeker of death lost his way, he would have found * no guide to souls but parting» (Abu Tammam — kāmil).",
 "tr": "«Ölümü arayan yolunu şaşırsaydı, * canlara ayrılıktan başka kılavuz bulamazdı» (Ebû Temmâm — kâmil)."},
 "tokens": [
  tok("لَوْ", "law", "part", [K, A, "in-shartiyya"], "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.", "«had» — the unreal law.", "«-saydı» — imtinâ' harfi."),
  tok("حَارَ", "hara", "verb", [K, "in-shartiyya", "hollow-verbs"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ: حَارَ يَحَارُ: ضَلَّ.", "«lost his way» — hollow.", "«şaşırsaydı» — ecvef."),
  tok("مُرْتَادُ", "murtad", "noun", [K, "fail", "idafa-definiteness", "ism-fail", "form-viii-verbs", "hollow-verbs"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ — اسْمُ فَاعِلٍ مِنِ ارْتَادَ: طَلَبَ.", "«the seeker» — the doer; ism fa'il of Form VIII.", "«arayan» — fâil; iftiâl ism-i fâili."),
  tok("الْمَنِيَّةِ", "maniyya", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of death».", "«ölümü»."),
  tok("لَمْ", "lam", "part", [K, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not».", "«-mez-»."),
  tok("يَجِدْ", "wajada", "verb", [K, "lam-jazim", "in-shartiyya", "mithal-verbs"], "مُضَارِعٌ مَجْزُومٌ بِلَمْ — جَوَابُ لَوْ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«would have found» — law's jawab.", "«bulamazdı» — lev'in cevabı.", punct="*"),
  tok("إِلَّا", "illa", "part", [K, "istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«but».", "«-den başka»."),
  tok("الْفِرَاقَ", "firaq", "noun", [K, "istithna-mufarragh", "maful-bihi", "masdar"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الِاسْتِثْنَاءُ مُفَرَّغٌ.", "«parting» — the object after the emptied illa.", "«ayrılığı» — müferrağ illâdan sonra mef'ûl."),
  tok("عَلَى", "ala", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("النُّفُوسِ", "nafs", "noun", [K, "huruf-jarr", "jam-taksir"], "مَجْرُورٌ — جَمْعُ نَفْسٍ.", "«souls».", "«canlara»."),
  tok("دَلِيلَا", "dalil", "noun", [K, QF, "hal"], "حَالٌ مَنْصُوبٌ — أُبْدِلَ التَّنْوِينُ أَلِفَ الْإِطْلَاقِ. الرَّوِيُّ اللَّامُ، وَالرِّدْفُ الْيَاءُ.", "«as a guide» — the hal; the alif of itlaq.", "«kılavuz olarak» — hâl; ıtlak elifi."),
 ]})
S.append({"id": "s22", "translation": {
 "en": "And the saying of Abu l-Tayyib: «Were it not for parting from loved ones, the deaths would find * no roads to our souls» — taken from Abu Tammam's bayt and its equal: an ighara far from blame, the merit staying with the first.",
 "tr": "Ve Ebü't-Tayyib'in: «Sevgililerden ayrılık olmasaydı ölümler * ruhlarımıza yol bulamazdı» sözü — Ebû Temmâm'ın beytinden alınmış ve onun dengi: zemden uzak bir iğâre, fazilet birincinin."},
 "tokens": [
  tok("وَقَوْلِ", "qawl", "noun", [K, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَقَوْلِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and the saying of».", "«ve … sözü».", segments=[seg("وَ", "wa", "conj"), seg("قَوْلِ", "qawl", "noun")]),
  tok("أَبِي", "abu-tayyib", "propn", [K, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«Abu».", "«Ebû»."),
  tok("الطَّيِّبِ", "abu-tayyib", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«l-Tayyib».", "«et-Tayyib».", punct=":"),
  tok("لَوْلَا", "lawla", "part", [K, A, "in-shartiyya", "hadhf-wa-taqdir"], "حَرْفُ امْتِنَاعٍ لِوُجُودٍ — وَخَبَرُ الْمُبْتَدَإِ بَعْدَهُ مَحْذُوفٌ وُجُوبًا: مَوْجُودَةٌ.", "«were it not for» — the mubtada after it has its khabar dropped by rule.", "«olmasaydı» — sonrasındaki mübtedânın haberi vücûben hazf."),
  tok("مُفَارَقَةُ", "mufaraqa", "noun", [K, "mubtada-khabar", "idafa-definiteness", "masdar", "form-iii-verbs"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ فَارَقَ.", "«parting» — the mubtada.", "«ayrılık» — mübtedâ."),
  tok("الْأَحْبَابِ", "habib", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ حَبِيبٍ.", "«from loved ones».", "«sevgililerden»."),
  tok("مَا", "ma-nafiya", "part", [K, "in-shartiyya", "anwa-ma"], "حَرْفُ نَفْيٍ — وَالْجُمْلَةُ جَوَابُ لَوْلَا.", "«not» — the jawab of lawla.", "«-mazdı» — levlânın cevabı."),
  tok("وَجَدَتْ", "wajada", "verb", [K, "in-shartiyya", "mithal-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«would find».", "«bulamazdı».", punct="*"),
  tok("لَهَا", "li", "prep", [K, "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — حَشْوٌ لَا حَاجَةَ إِلَيْهِ فِي الْمَعْنَى.", "«for themselves» — a filler word the meaning does not need.", "«kendilerine» — mananın muhtaç olmadığı haşiv.", segments=[seg("لَ", "li", "prep"), seg("هَا", "pron-3fs", "pron")]),
  tok("الْمَنَايَا", "maniyya", "noun", [K, "fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — جَمْعُ مَنِيَّةٍ.", "«the deaths» — the doer.", "«ölümler» — fâil."),
  tok("إِلَى", "ila", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("أَرْوَاحِنَا", "ruh", "noun", [K, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، وَنَا مُضَافٌ إِلَيْهِ — جَمْعُ رُوحٍ.", "«our souls».", "«ruhlarımıza».", segments=[seg("أَرْوَاحِ", "ruh", "noun"), seg("نَا", "pron-1p", "pron")]),
  tok("سُبُلَا", "sabil", "noun", [K, QF, "maful-bihi", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — جَمْعُ سَبِيلٍ، أُبْدِلَ التَّنْوِينُ أَلِفَ الْإِطْلَاقِ. الرَّوِيُّ اللَّامُ.", "«roads» — the object; the alif of itlaq.", "«yollar» — mef'ûl; ıtlak elifi."),
 ]})
S[-1]["badi"] = [{"kind": "sariqa", "sub": "zahir", "kind2": "ighara", "with": "s21", "grade": "mithl"}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "khatima": need("khatima", "خَاتِمَة", "خ ت م", "noun", "a closing section, an epilogue (ism fa'il of خَتَمَ, feminine)", "hâtime, kapanış bölümü (hateme'nin ism-i fâili, müennes)", 5),
 "shiri": need("shiri", "شِعْرِيّ", "ش ع ر", "noun", "poetic (the nisba of شِعْر)", "şiirle ilgili (şi'r'in nisbesi)", 4),
 "qail": need("qail", "قَائِل", "ق و ل", "noun", "a sayer, a speaker (ism fa'il of قَالَ)", "söyleyen (kâle'nin ism-i fâili)", 3),
 "umum": need("umum", "عُمُوم", "ع م م", "noun", "generality (masdar of عَمَّ) — عَلَى الْعُمُومِ: in general", "umum, genellik (amme masdarı) — ale'l-umûm: genel olarak", 5),
 "shuja": need("shuja", "شُجَاع", "ش ج ع", "noun", "brave (a sifa mushabbaha on فُعَال)", "cesur, şecaatli (fu'âl vezninde sıfat-ı müşebbehe)", 4),
 "jawad": need("jawad", "جَوَاد", "ج و د", "noun", "generous, open-handed (فَعَال)", "cömert (fe'âl vezninde)", 5),
 "adda-count": need("adda-count", "عَدَّ", "ع د د", "verb", "to count, to reckon as (doubled; عَدَّ يَعُدُّ — takes two objects)", "saymak, … saymak (muzâaf; adde yeuddu — iki mef'ûl alır)", 4),
 "taqarrur": need("taqarrur", "تَقَرُّر", "ق ر ر", "noun", "being settled, established (masdar of Form V تَقَرَّرَ)", "yerleşmiş olma (tefa'ul masdarı)", 6),
 "sabq": need("sabq", "سَبْق", "س ب ق", "noun", "precedence, getting there first (masdar of سَبَقَ)", "öncelik, önce gelme (sebeka masdarı)", 4),
 "khassi": need("khassi", "خَاصِّيّ", "خ ص ص", "noun", "belonging to the elect; rare (the nisba of خَاصَّة)", "havâssa mahsus; nâdir (hâssanın nisbesi)", 6),
 "ammi": need("ammi", "عَامِّيّ", "ع م م", "noun", "common, of the general run (the nisba of عَامَّة)", "avâmî, umuma âit (âmmenin nisbesi)", 6),
 "tasarrafa": need("tasarrafa", "تَصَرَّفَ", "ص ر ف", "verb", "to act freely on, to work upon (Form V; تَصَرَّفَ فِيهِ)", "tasarruf etmek, üzerinde işlemek (tefa'ul; tasarrafe fîhi)", 5),
 "ibtidhal": need("ibtidhal", "ابْتِذَال", "ب ذ ل", "noun", "triteness, being worn by common use (masdar of Form VIII ابْتَذَلَ)", "bayağılık, ele düşmüşlük (iftiâl masdarı)", 6),
 "madhmum": need("madhmum", "مَذْمُوم", "ذ م م", "noun", "blamed, blameworthy (ism maf'ul of ذَمَّ)", "mezmûm, kınanmış (zemme'nin ism-i mef'ûlü)", 4),
 "mahd": need("mahd", "مَحْض", "م ح ض", "noun", "pure, sheer, nothing but", "sırf, hâlis, katıksız", 5),
 "naskh-copy": need("naskh-copy", "نَسْخ", "ن س خ", "noun", "naskh — copying a text letter for letter (masdar of نَسَخَ); of poetry: taking the words whole", "nesh — bir metni harfi harfine kopya etmek (nesaha masdarı); şiirde: lafzı bütünüyle almak", 6),
 "abd": need("abd", "عَبْد", "ع ب د", "noun", "a servant, a slave (pl. عِبَاد) — in names: ʿAbd Allah", "kul, köle (ç. عِبَاد) — adlarda: Abdullah", 2, plural="عِبَاد"),
 "allah": need("allah", "اللهُ", None, "propn", "Allah — the name of God", "Allah — Cenâb-ı Hakk'ın adı", 1),
 "zubayr": need("zubayr", "الزُّبَيْر", None, "propn", "al-Zubayr — ʿAbdallah b. al-Zubayr, the Companion's son", "Zübeyr — sahâbî oğlu Abdullah b. Zübeyr", 6),
 "man-aws": need("man-aws", "مَعْن", None, "propn", "Maʿn — Maʿn b. Aws al-Muzani, the mukhadram poet", "Ma'n — muhadram şair Ma'n b. Evs el-Müzenî", 6),
 "aws": need("aws", "أَوْس", None, "propn", "Aws — Maʿn's father", "Evs — Ma'n'ın babası", 6),
 "ansafa": need("ansafa", "أَنْصَفَ", "ن ص ف", "verb", "to deal justly with (Form IV; أَنْصَفَ يُنْصِفُ)", "insaf etmek, âdil davranmak (if'âl; ensafe yunsifu)", 5),
 "hijran": need("hijran", "هِجْرَان", "ه ج ر", "noun", "estrangement, forsaking (a masdar of هَجَرَ)", "hicran, terk etme (hecere'nin masdarı)", 5),
 "aqala": need("aqala", "عَقَلَ", "ع ق ل", "verb", "to have sense, to understand (عَقَلَ يَعْقِلُ)", "akletmek, anlamak (akale ya'kilu)", 3),
 "dama-wrong": need("dama-wrong", "ضَامَ", "ض ي م", "verb", "to wrong, to oppress (hollow; ضَامَ يَضِيمُ)", "zulmetmek, haksızlık etmek (ecvef; dâme yedîmu)", 6),
 "shafra": need("shafra", "شَفْرَة", "ش ف ر", "noun", "the blade, the cutting edge (pl. شِفَار)", "kılıç ağzı, keskin kenar (ç. شِفَار)", 6, plural="شِفَار"),
 "mazhal": need("mazhal", "مَزْحَل", "ز ح ل", "noun", "a place to step aside to (ism makan of زَحَلَ)", "sapılacak, çekilecek yer (zehale'nin ism-i mekânı)", 6),
 "baddala": need("baddala", "بَدَّلَ", "ب د ل", "verb", "to replace, to change (Form II; بَدَّلَ يُبَدِّلُ)", "değiştirmek, yerine koymak (tef'îl; beddele yubeddilu)", 4),
 "radafa": need("radafa", "رَادَفَ", "ر د ف", "verb", "to be synonymous with (Form III; رَادَفَ يُرَادِفُ)", "eş anlamlı olmak (mufâale; râdefe yurâdifu)", 6),
 "ighara": need("ighara", "إِغَارَة", "غ و ر", "noun", "ighara — a raid (masdar of Form IV أَغَارَ); of poetry: taking the words with their order changed", "iğâre — baskın, yağma (if'âl masdarı); şiirde: lafzı nazmı değişmiş olarak almak", 6),
 "maskh": need("maskh", "مَسْخ", "م س خ", "noun", "maskh — disfiguring, turning a form into an uglier one (masdar of مَسَخَ)", "mesh — bir sureti çirkinine çevirme (mesaha masdarı)", 6),
 "fadila": need("fadila", "فَضِيلَة", "ف ض ل", "noun", "a merit, a virtue (pl. فَضَائِل)", "fazilet, meziyet (ç. فَضَائِل)", 4, plural="فَضَائِل"),
 "zafira": need("zafira", "ظَفِرَ", "ظ ف ر", "verb", "to win, to attain (ظَفِرَ بِهِ يَظْفَرُ)", "kazanmak, ermek (zafire bihi yazferu)", 5),
 "faza": need("faza", "فَازَ", "ف و ز", "verb", "to win, to succeed (hollow; فَازَ يَفُوزُ)", "kazanmak, ermek (ecvef; fâze yefûzu)", 3),
 "fatik": need("fatik", "فَاتِك", "ف ت ك", "noun", "bold, daring (ism fa'il of فَتَكَ)", "cesur, atılgan (feteke'nin ism-i fâili)", 6),
 "lahij": need("lahij", "لَهِج", "ل ه ج", "noun", "ardent, eager for (a sifa mushabbaha: لَهِجَ بِهِ)", "düşkün, hırslı (sıfat-ı müşebbehe: lehice bihi)", 6),
 "salm": need("salm", "سَلْم", None, "propn", "Salm — Salm al-Khasir, the ʿAbbasid poet, Bashshar's pupil", "Selm — Abbâsî şairi Selm el-Hâsir, Beşşâr'ın talebesi", 6),
 "jasur": need("jasur", "جَسُور", "ج س ر", "noun", "daring, bold (an intensive on فَعُول)", "cüretkâr, cesur (fe'ûl vezninde mübalağa)", 5),
 "hayhat": need("hayhat", "هَيْهَاتَ", None, "noun", "«far be it!» — an ism fi'l meaning «it is far»", "«heyhât!» — «uzak oldu» manasında ism-i fiil", 5),
 "abu-tammam": need("abu-tammam", "أَبُو تَمَّامٍ", None, "propn", "Abu Tammam — the ʿAbbasid poet (d. 231 AH)", "Ebû Temmâm — Abbâsî şairi (ö. 231)", 5),
 "abu-tayyib": need("abu-tayyib", "أَبُو الطَّيِّبِ", None, "propn", "Abu l-Tayyib — al-Mutanabbi (d. 354 AH)", "Ebü't-Tayyib — Mütenebbî (ö. 354)", 5),
 "la-ibtida": need("la-ibtida", "لَ", None, "part", "the lam of emphasis (lam al-ibtida', sliding onto inna's khabar)", "te'kîd lâmı (lâm-ı ibtidâ, innenin haberine kayar)", 4),
 "qad": need("qad", "قَدْ", None, "part", "qad — certainty with the mazi, «sometimes» with the mudari", "kad — mâzî ile tahkik, muzâri ile taklîl", 3),
 "ada-infect": need("ada-infect", "أَعْدَى", "ع د و", "verb", "to infect, to pass on (Form IV of the naqis root; أَعْدَى يُعْدِي)", "bulaştırmak, geçirmek (if'âl, nâkıs; a'dâ yu'dî)", 6),
 "sakha-verb": need("sakha-verb", "سَخَا", "س خ و", "verb", "to be generous (naqis; سَخَا يَسْخُو)", "cömert olmak (nâkıs; sehâ yeshû)", 5),
 "abad": need("abad", "أَبْعَد", "ب ع د", "noun", "farther (the elative of بَعِيد)", "daha uzak (baîd'in ism-i tafdîli)", 4),
 "murtad": need("murtad", "مُرْتَاد", "ر و د", "noun", "a seeker (ism fa'il of Form VIII ارْتَادَ, hollow)", "arayan, talip (iftiâl ism-i fâili, ecvef)", 6),
 "firaq": need("firaq", "فِرَاق", "ف ر ق", "noun", "parting, separation (a masdar of فَارَقَ)", "ayrılık, firâk (fâraka'nın masdarı)", 4),
 "man": need("man", "مَنْ", None, "pron", "who, whoever — the relative and conditional noun (the mim's fatha tells it from مِنْ)", "kim, her kim — ism-i mevsûl ve şart ismi (mîmin fethası مِنْ'den ayırır)", 2),
 "lawla": need("lawla", "لَوْلَا", None, "part", "were it not for — the particle of hindrance by existence", "olmasaydı — vücûd sebebiyle imtinâ' harfi", 4),
}
_MISSING = []
for k in ("sariqa", "fi", "wa", "in-shartiyya", "kana", "gharad", "ala", "wasf", "asad", "bahr", "la-nafiya", "fa", "aql", "ada", "wajh", "dalala", "ishtaraka", "nas", "marifa", "huwa", "awwal", "ka",
          "illa", "jaza", "an-masdariyya", "iddaa", "ziyada", "darb", "nafs", "arafa", "khass", "akhraja", "min", "ila", "gharaba", "akhdh", "ghayr", "zahir", "akhadha", "mana", "kull", "maa", "lafz", "aw",
          "bad", "wahda", "taghyir", "nazm", "li", "anna", "samma", "intihal", "kama", "ma-masdariyya", "haka", "ibn", "faala", "dhalika", "bayt", "idha", "anta", "lam", "akh", "wajada", "taraf",
          "kadha", "kalam", "ma-mawsula", "thani", "ablagh", "ikhtisas", "bi", "mamduh", "qawl", "bashshar", "raqaba", "haja", "tayyib", "mata", "hamm", "ladhdha", "duna", "ata", "zaman",
          "mithl", "inna", "bakhil", "sakha", "hara", "maniyya", "dalil", "dhamm", "fadl", "law", "habib", "mufaraqa", "ma-nafiya", "ruh", "sabil", "rakiba", "hadd", "sayf", "an", "ittifaq",
          "ittasala", "pron-3ms", "pron-3fs", "pron-2ms", "pron-1p"):
    if k not in TG:
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
put_morph(mo, "adda-count", gem("nasara", "عَدّ", "عَدَد", "عُدّ", "عْدُد", ["عُدَّ", "عُدَّا", "عُدُّوا", "عُدِّي", "عُدَّا", "اُعْدُدْنَ"], "عَدّ", "عَادّ", "مَعْدُود", "عُدَّ", "يُعَدُّ",
                                "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: عَدَّ يَعُدُّ — يُعَدُّ سَرِقَةً: مَجْهُولُهُ."))
put_morph(mo, "tasarrafa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَصَرَّف", "تَصَرَّف", "تَصَرَّف", "تَصَرُّف", "مُتَصَرِّف", "مُتَصَرَّف", "تُصُرِّفَ", "يُتَصَرَّفُ"))
put_morph(mo, "ansafa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَنْصَف", "نْصِف", "أَنْصِف", "إِنْصَاف", "مُنْصِف", "مُنْصَف", "أُنْصِفَ", "يُنْصَفُ"))
put_morph(mo, "aqala", _sg.sound1("daraba", "عَقَل", "عْقِل", "اِعْقِل", "عَقْل", "عَاقِل", "مَعْقُول", "عُقِلَ", "يُعْقَلُ"))
put_morph(mo, "dama-wrong", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "ضَام", "ضِم", "ضِيم", "ضِم", "ضِيم", "ضِم", "ضَيْم", "ضَائِم", "مَضِيم", "ضِيمَ", "يُضَامُ",
                                       "ضَامَ يَضِيمُ: ظَلَمَ — أَجْوَفٌ يَائِيٌّ مِنْ بَابِ ضَرَبَ."))
put_morph(mo, "baddala", _sg.derived(_sg.B2, _sg.W2, "ُ", "بَدَّل", "بَدِّل", "بَدِّل", "تَبْدِيل", "مُبَدِّل", "مُبَدَّل", "بُدِّلَ", "يُبَدَّلُ"))
put_morph(mo, "radafa", _sg.derived(_sg.B3, _sg.W3, "ُ", "رَادَف", "رَادِف", "رَادِف", "مُرَادَفَة", "مُرَادِف", "مُرَادَف", "رُودِفَ", "يُرَادَفُ"))
put_morph(mo, "raqaba", _sg.derived(_sg.B3, _sg.W3, "ُ", "رَاقَب", "رَاقِب", "رَاقِب", "مُرَاقَبَة", "مُرَاقِب", "مُرَاقَب", "رُوقِبَ", "يُرَاقَبُ"))
put_morph(mo, "zafira", _sg.sound1("samia", "ظَفِر", "ظْفَر", "اِظْفَر", "ظَفَر", "ظَافِر", "مَظْفُور", "ظُفِرَ", "يُظْفَرُ"))
put_morph(mo, "faza", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "فَاز", "فُز", "فُوز", "فُز", "فُوز", "فُز", "فَوْز", "فَائِز", None, None, None,
                                 "فَازَ يَفُوزُ — أَجْوَفٌ وَاوِيٌّ مِنْ بَابِ نَصَرَ."))
_e = _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَعْدَ", "عْد", "i", "أَعْد", "إِعْدَاء", "مُعْدٍ (الْمُعْدِي)", "مُعْدًى", "أُعْدِيَ", "يُعْدَى",
                       note="أَعْدَى يُعْدِي: نَقَلَ الْعَدْوَى — نَاقِصٌ يَائِيٌّ مِنْ بَابِ الْإِفْعَالِ.")
put_morph(mo, "ada-infect", _e)
put_morph(mo, "sakha-verb", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "سَخَ", "سْخ", "u", "اُسْخ", "سَخَاء", "سَاخٍ (السَّاخِي)", None, None, None,
                                      "سَخَا يَسْخُو: جَادَ — نَاقِصٌ وَاوِيٌّ مِنْ بَابِ نَصَرَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_S = {
 "id": "sariqat-shiriyya",
 "title": {"ar": "السَّرِقَاتُ الشِّعْرِيَّةُ — الْأَخْذُ الظَّاهِرُ: نَسْخٌ وَإِغَارَةٌ وَإِلْمَامٌ", "en": "The poetic takings — the plain kind: naskh, ighara, ilmam", "tr": "Şiir sirkatleri — zâhir olanı: nesh, iğâre, ilmâm"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الخاتمة: في السرقات الشعرية وما يتصل بها؛ الأخذ ضربان ظاهر وغير ظاهر"],
 "question": {
  "en": ["When do two poets NOT steal from each other? When they agree in a purpose everyone shares — the brave man is a lion, the generous a sea — for that is settled in minds and customs (s2). And when the WAY of signifying is one everyone knows, likewise (s3).",
         "What is the PLAIN taking? The meaning taken whole — with all the words (naskh / intihal: blamed, a pure theft — Ibn al-Zubayr reciting Maʿn's two bayts as his own), with the order changed or part of the words (ighara / maskh), or alone (ilmam / salkh).",
         "How is the ighara judged? By the SECOND poem against the first: better — praised (Salm over Bashshar); worse — blamed (al-Mutanabbi's time-bayt under Abu Tammam's); equal — no blame, but the merit is the first's (the parting-bayts).",
         "What does the engine read? Which bayt took from which is history and the frame says it (`with`); the engine counts the ROOTS the two bayts share and names the kind the count licenses — all of them naskh, a third or more ighara, fewer ilmam — and prints the shared words. The grade (better, worse, equal) is taste, and stays the author's."],
  "tr": ["İki şair ne zaman birbirinden ÇALMIŞ olmaz? Herkesin paylaştığı bir maksatta birleştiklerinde — cesur arslandır, cömert denizdir — çünkü bu akıllarda ve âdetlerde yerleşiktir (s2). Delâlet YÖNÜ herkesçe bilinen bir şeyse de böyledir (s3).",
         "ZÂHİR alma nedir? Mananın bütünüyle alınması — bütün lafızla (nesh / intihâl: mezmûm, sırf hırsızlık — İbnü'z-Zübeyr'in Ma'n'ın iki beytini kendi diye okuması), nazmı değişmiş yahut lafzın bir kısmıyla (iğâre / mesh), yahut tek başına (ilmâm / selh).",
         "İğâre nasıl değerlendirilir? İKİNCİ şiir birinciye göre: daha iyiyse memdûh (Selm Beşşâr'a karşı); daha kötüyse mezmûm (Mütenebbî'nin zaman beyti Ebû Temmâm'ınkinin altında); dengiyse zem yok, fakat fazilet birincinin (ayrılık beyitleri).",
         "Motor neyi okur? Hangi beytin hangisinden aldığı tarihtir ve çerçeve söyler (`with`); motor iki beytin paylaştığı KÖKLERİ sayar ve sayının izin verdiği cinsi adlandırır — hepsi nesh, üçte biri ve fazlası iğâre, daha azı ilmâm — ve ortak kelimeleri basar. Derece (iyi, kötü, denk) zevk işidir ve yazarın kalır."]},
 "plain": {
  "en": "Taking another poet's meaning: with all his words it is theft; with some it is a raid, judged by whether the taker did better; with none of them it is an allusion.",
  "tr": "Başka şairin manasını almak: bütün sözleriyle hırsızlıktır; bir kısmıyla yağmadır, alanın daha iyi yapıp yapmadığına göre yargılanır; hiçbiriyle ise ilmâmdır."},
 "explanation": {
  "en": "اتِّفَاقُ الْقَائِلَيْنِ إِنْ كَانَ فِي الْغَرَضِ عَلَى الْعُمُومِ فَلَا يُعَدُّ سَرِقَةً. The khatima of the Talkhis begins by fencing off what is NOT a taking: a purpose the whole language shares (the lion, the sea), and a way of signifying that everyone knows. Only past that fence may precedence be claimed — and there the purpose is either rare in itself (the elect alone know it) or common but worked into rarity. The taking itself is plain or hidden. The plain kind takes the meaning whole: with all the words and their order unchanged it is naskh and intihal, blamed without appeal, even when synonyms are swapped in; with the order changed or part of the words it is ighara and maskh, and here the second poem is judged against the first — praised when it adds a merit (Salm's مَاتَ هَمًّا over Bashshar's لَمْ يَظْفَرْ بِحَاجَتِهِ), blamed when it falls short (al-Mutanabbi's وَلَقَدْ يَكُونُ بِهِ الزَّمَانُ بَخِيلَا under Abu Tammam's إِنَّ الزَّمَانَ بِمِثْلِهِ لَبَخِيلُ), and neither when equal, the merit staying with the first. The next chapter takes the meaning alone (ilmam, salkh) and the hidden kind.",
  "tr": "اتِّفَاقُ الْقَائِلَيْنِ إِنْ كَانَ فِي الْغَرَضِ عَلَى الْعُمُومِ فَلَا يُعَدُّ سَرِقَةً. Telhîs'in hâtimesi önce sirkat OLMAYANI çitler: bütün dilin paylaştığı bir maksat (arslan, deniz) ve herkesin bildiği bir delâlet yönü. Öncelik ancak bu çitin ötesinde iddia edilebilir — orada maksat ya kendinde nâdirdir (yalnız havâss bilir) ya avâmî olup garâbete işlenmiştir. Almanın kendisi zâhir veya hafîdir. Zâhir olanı manayı bütünüyle alır: bütün lafız ve nazmı değişmeden alınırsa nesh ve intihâldir, eş anlamlılar konsa bile itirazsız mezmûmdur; nazmı değişmiş yahut lafzın bir kısmı alınmışsa iğâre ve meshtir ve burada ikinci şiir birinciye göre yargılanır — bir fazilet katarsa memdûh (Selm'in مَاتَ هَمًّا'sı Beşşâr'ın لَمْ يَظْفَرْ بِحَاجَتِهِ'sine karşı), geri kalırsa mezmûm (Mütenebbî'nin وَلَقَدْ يَكُونُ بِهِ الزَّمَانُ بَخِيلَا'sı Ebû Temmâm'ın إِنَّ الزَّمَانَ بِمِثْلِهِ لَبَخِيلُ'ünün altında), denkse ikisi de değil, fazilet birincinin. Sonraki bâb manayı tek başına almayı (ilmâm, selh) ve hafî olanı işler."},
 "examples": [
  {"ar": "إِذَا أَنْتَ لَمْ تُنْصِفْ أَخَاكَ وَجَدْتَهُ * عَلَى طَرَفِ الْهِجْرَانِ إِنْ كَانَ يَعْقِلُ", "en": "Maʿn b. Aws — taken whole by Ibn al-Zubayr: naskh.", "tr": "Ma'n b. Evs — İbnü'z-Zübeyr'in bütünüyle aldığı: nesh.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"},
  {"ar": "مَنْ رَاقَبَ النَّاسَ مَاتَ هَمًّا * وَفَازَ بِاللَّذَّةِ الْجَسُورُ", "en": "Salm from Bashshar — an ighara that is praised.", "tr": "Selm, Beşşâr'dan — memdûh bir iğâre.", "sourceStory": "talkhis-al-miftah", "sentence": "s16"},
  {"ar": "أَعْدَى الزَّمَانَ سَخَاؤُهُ فَسَخَا بِهِ * وَلَقَدْ يَكُونُ بِهِ الزَّمَانُ بَخِيلَا", "en": "al-Mutanabbi from Abu Tammam — an ighara that is blamed.", "tr": "Mütenebbî, Ebû Temmâm'dan — mezmûm bir iğâre.", "sourceStory": "talkhis-al-miftah", "sentence": "s19"},
  {"ar": "لَوْلَا مُفَارَقَةُ الْأَحْبَابِ مَا وَجَدَتْ * لَهَا الْمَنَايَا إِلَى أَرْوَاحِنَا سُبُلَا", "en": "al-Mutanabbi from Abu Tammam — equal: no blame, the merit the first's.", "tr": "Mütenebbî, Ebû Temmâm'dan — denk: zem yok, fazilet birincinin.", "sourceStory": "talkhis-al-miftah", "sentence": "s22"}],
 "commonMistakes": [
  {"wrong": "«İki şair de cömerdi denize benzetmiş: ikincisi çalmış»",
   "right": "«Cömerdi denize benzetmek akıllarda ve âdetlerde yerleşik bir maksattır; onda ittifak sirkat sayılmaz»",
   "why": {"en": "The first fence of the khatima: a shared purpose belongs to the language, not to a poet. Only a rare purpose, or a rare way of signifying, can be taken.", "tr": "Hâtimenin ilk çiti: ortak maksat şairin değil dilindir. Ancak nâdir bir maksat yahut nâdir bir delâlet yönü alınabilir."}},
  {"wrong": "«Kelimeleri eş anlamlılarıyla değiştirdim, artık nesh değil»",
   "right": "«وَكَذَا إِنْ بُدِّلَ بِكَلَامِهِ كُلِّهِ أَوْ بَعْضِهِ مَا يُرَادِفُهُ — eş anlamlı koymak nazmı bırakır; nesh olarak mezmûmdur»",
   "why": {"en": "The book closes the loophole in its own words: the synonym swap keeps the order and is still naskh.", "tr": "Kitap açığı kendi sözleriyle kapatır: eş anlamlı değişimi nazmı korur ve yine neshtir."}}],
 "relatedNotes": ["ilm-al-badi", "jinas", "radd-al-ajuz"]}

NOTE_A = {
 "id": "ilm-al-arud",
 "title": {"ar": "عِلْمُ الْعَرُوضِ — التَّقْطِيعُ وَالْبُحُورُ", "en": "ʿIlm al-ʿarud — the scansion and the metres", "tr": "İlm-i arûz — taktî' ve bahirler"},
 "level": 6, "group": "arud",
 "classicalSources": ["الخليل بن أحمد — كتاب العروض: البحور الخمسة عشر وتفاعيلها؛ الأخفش — المتدارك", "الخزرجية (الشيخ ضياء الدين الخزرجي) — منظومة في العروض والقافية"],
 "question": {
  "en": ["What is a bayt made of? Not letters but UNITS: a letter that moves (mutaḥarrik, /) and a letter that stands (sākin, ○). A tanwīn is a nūn, a shadda is two letters, the article's alif and its assimilated lām are not said mid-line, a long vowel is a letter that stands, a madd falls before a waṣl, and the close is lengthened (ishbāʿ) or read in pause.",
         "What is a tafʿīla? A named run of units — فَعُولُنْ //○/○, مَفَاعِيلُنْ //○/○/○, مُسْتَفْعِلُنْ /○/○//○, فَاعِلُنْ /○//○, فَاعِلَاتُنْ /○//○/○, مُتَفَاعِلُنْ ///○//○, مُفَاعَلَتُنْ //○///○, مَفْعُولَاتُ /○/○/○/ — and a baḥr is a fixed row of them per hemistich: the ṭawīl فَعُولُنْ مَفَاعِيلُنْ فَعُولُنْ مَفَاعِلُنْ, the basīṭ مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ, the kāmil مُتَفَاعِلُنْ ×3, the wāfir مُفَاعَلَتُنْ مُفَاعَلَتُنْ فَعُولُنْ, the khafīf فَاعِلَاتُنْ مُسْتَفْعِلُنْ فَاعِلَاتُنْ …",
         "What may change? The ziḥāf inside the line (a sākin dropped: مُتَفْعِلُنْ, فَعِلُنْ, مَفَاعِلُنْ; a mutaḥarrik stilled: مُتْفَاعِلُنْ, مُفَاعَلْتُنْ) and the ʿilla at the ʿarūḍ and the ḍarb (a foot cut: فَعِلُنْ for فَاعِلُنْ, مُفَاعَلْ for مُفَاعَلَتُنْ). The card names the form each foot took.",
         "What does the engine read? It builds the units off the marks by these rules and tries every baḥr: the one whose feet consume both hemistichs with the fewest ziḥāfāt is the metre; where none does, it says so and shows the units. It also audits the hemistich mark: where the metre closes the ṣadr inside a word the bayt is mudawwar, and where the mark stands elsewhere the mark is wrong."],
  "tr": ["Beyit neden yapılır? Harflerden değil BİRİMLERDEN: hareketli harf (müteharrik, /) ve sâkin harf (○). Tenvin nûndur, şedde iki harftir, harf-i tarifin elifi ve idgamlı lâmı mısra içinde okunmaz, uzun ünlü sâkin bir harftir, vasıldan önce med düşer, sonda ya işbâ yapılır ya vakıf.",
         "Tef'ile nedir? Adlandırılmış bir birim dizisi — فَعُولُنْ //○/○, مَفَاعِيلُنْ //○/○/○, مُسْتَفْعِلُنْ /○/○//○, فَاعِلُنْ /○//○, فَاعِلَاتُنْ /○//○/○, مُتَفَاعِلُنْ ///○//○, مُفَاعَلَتُنْ //○///○, مَفْعُولَاتُ /○/○/○/ — bahir ise her mısrada sabit bir tef'ile sırasıdır: tavîl فَعُولُنْ مَفَاعِيلُنْ فَعُولُنْ مَفَاعِلُنْ, basît مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ, kâmil مُتَفَاعِلُنْ ×3, vâfir مُفَاعَلَتُنْ مُفَاعَلَتُنْ فَعُولُنْ, hafîf فَاعِلَاتُنْ مُسْتَفْعِلُنْ فَاعِلَاتُنْ …",
         "Ne değişebilir? Mısra içinde zihâf (bir sâkin düşer: مُتَفْعِلُنْ, فَعِلُنْ, مَفَاعِلُنْ; bir müteharrik sâkinleşir: مُتْفَاعِلُنْ, مُفَاعَلْتُنْ) ve arûz ile darbda illet (tef'ile kesilir: فَاعِلُنْ yerine فَعِلُنْ, مُفَاعَلَتُنْ yerine مُفَاعَلْ). Kart her tef'ilenin aldığı şekli söyler.",
         "Motor neyi okur? Birimleri bu kurallarla harekelerden kurar ve her bahri dener: tef'ileleri iki mısrayı en az zihâfla dolduran bahir vezindir; hiçbiri doldurmazsa bunu söyler ve birimleri gösterir. Mısra işaretini de denetler: vezin sadrı bir kelimenin içinde kapatıyorsa beyit müdevverdir, işaret başka yerdeyse işaret yanlıştır."]},
 "plain": {
  "en": "A verse is a fixed row of sound-patterns; scan the letters into moving and still ones and the pattern names the metre.",
  "tr": "Şiir sabit bir ses örgüsü dizisidir; harfleri hareketli ve sâkin diye ayır, örgü vezni söyler."},
 "explanation": {
  "en": "الْعَرُوضُ مِيزَانُ الشِّعْرِ. Al-Khalil's science weighs a line by its units, not its letters: every consonant with a vowel is a mutaḥarrik, every consonant without one — and every long vowel — a sākin. The written page hides some of the units and shows others that are not said: a tanwīn is a nūn (كِتَابٌ = كِتَابُنْ), a shadda is a sākin and a mutaḥarrik (الشَّمْس = أَشْ شَمْس), the alif of waṣl is silent after the first word and a long vowel before it falls (مَا الْحَقُّ = مَلْحَقُّ), the pronoun's hāʾ may be lengthened (بِهِ = بِهِي), and the last vowel of a hemistich is lengthened or the word is read in pause. The units then fall into feet — sabab (a mutaḥarrik and a sākin: /○), watid (two moving and one still: //○) — and the feet into the eight tafāʿīl, and the tafāʿīl into the sixteen buḥūr. The changes the metre licenses are the ziḥāfāt (inside the line) and the ʿilal (at the two closes), each with its name: khabn drops the second sākin (مُتَفْعِلُنْ), ṭayy the fourth (مُسْتَعِلُنْ), qabḍ the fifth (مَفَاعِلُنْ, فَعُولُ), iḍmār stills the second letter (مُتْفَاعِلُنْ), ʿaṣb the fifth (مُفَاعَلْتُنْ); ḥadhf cuts the last sabab (فَعُولُنْ → فَعُو), qaṭʿ the watid's last (فَاعِلُنْ → فَاعِلْ = فَعْلُنْ). The scansion is exact because the marks are: a vowelled bayt has one reading, and the engine finds it or refuses.",
  "tr": "الْعَرُوضُ مِيزَانُ الشِّعْرِ. Halîl'in ilmi mısrayı harfleriyle değil birimleriyle tartar: harekeli her ünsüz müteharrik, harekesiz her ünsüz — ve her uzun ünlü — sâkindir. Yazılı sayfa bazı birimleri gizler, okunmayan bazılarını gösterir: tenvin nûndur (كِتَابٌ = كِتَابُنْ), şedde bir sâkin bir müteharriktir (الشَّمْس = أَشْ شَمْس), vasıl elifi ilk kelimeden sonra sessizdir ve öncesindeki uzun ünlü düşer (مَا الْحَقُّ = مَلْحَقُّ), zamir hâsı uzayabilir (بِهِ = بِهِي), mısra sonunda son hareke uzatılır yahut kelime vakıf okunur. Birimler sonra cüzlere düşer — sebeb (bir müteharrik bir sâkin: /○), veted (iki hareketli bir sâkin: //○) — cüzler sekiz tef'ileye, tef'ileler on altı bahre. Veznin izin verdiği değişimler zihâflar (mısra içinde) ve illetlerdir (iki sonda), her birinin adı vardır: habn ikinci sâkini düşürür (مُتَفْعِلُنْ), tayy dördüncüyü (مُسْتَعِلُنْ), kabz beşinciyi (مَفَاعِلُنْ, فَعُولُ), izmâr ikinci harfi sâkinleştirir (مُتْفَاعِلُنْ), asb beşinciyi (مُفَاعَلْتُنْ); hazf son sebebi keser (فَعُولُنْ → فَعُو), kat' vetedin sonunu (فَاعِلُنْ → فَاعِلْ = فَعْلُنْ). Taktî' kesindir çünkü harekeler kesindir: harekeli bir beytin tek okunuşu vardır, motor onu bulur ya da reddeder."},
 "examples": [
  {"ar": "إِذَا أَنْتَ لَمْ تُنْصِفْ أَخَاكَ وَجَدْتَهُ * عَلَى طَرَفِ الْهِجْرَانِ إِنْ كَانَ يَعْقِلُ", "en": "ṭawīl — فَعُولُنْ مَفَاعِيلُنْ فَعُولُ مَفَاعِلُنْ.", "tr": "tavîl — فَعُولُنْ مَفَاعِيلُنْ فَعُولُ مَفَاعِلُنْ.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"},
  {"ar": "مَنْ رَاقَبَ النَّاسَ لَمْ يَظْفَرْ بِحَاجَتِهِ * وَفَازَ بِالطَّيِّبَاتِ الْفَاتِكُ اللَّهِجُ", "en": "basīṭ — مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ.", "tr": "basît — مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ.", "sourceStory": "talkhis-al-miftah", "sentence": "s15"},
  {"ar": "هَيْهَاتَ لَا يَأْتِي الزَّمَانُ بِمِثْلِهِ * إِنَّ الزَّمَانَ بِمِثْلِهِ لَبَخِيلُ", "en": "kāmil — مُتْفَاعِلُنْ مُتْفَاعِلُنْ مُتَفَاعِلُنْ, the iḍmār stilling the second letter.", "tr": "kâmil — مُتْفَاعِلُنْ مُتْفَاعِلُنْ مُتَفَاعِلُنْ, izmâr ikinci harfi sâkinleştirir.", "sourceStory": "talkhis-al-miftah", "sentence": "s18"}],
 "commonMistakes": [
  {"wrong": "«كِتَابٌ üç harftir: /○/»",
   "right": "«كِتَابُنْ — tenvin bir nûndur: //○/○»",
   "why": {"en": "The scansion reads what is SAID: the tanwīn is a sākin nūn, the shadda two letters, the article's alif nothing mid-line.", "tr": "Taktî' SÖYLENENİ okur: tenvin sâkin bir nûn, şedde iki harf, harf-i tarifin elifi mısra içinde hiçtir."}},
  {"wrong": "«Her tef'ilede مُتْفَاعِلُنْ var: kâmil»",
   "right": "«Bir yerde bile مُتَفَاعِلُنْ yoksa rajazdır — مُسْتَفْعِلُنْ ile aynı birimler»",
   "why": {"en": "The kāmil with every foot stilled is indistinguishable from the rajaz; the books call it rajaz, and the engine prefers the baḥr that needs fewer changes.", "tr": "Her tef'ilesi sâkinleşmiş kâmil recezden ayırt edilemez; kitaplar ona recez der, motor daha az değişim isteyen bahri yeğler."}}],
 "relatedNotes": ["al-qafiya", "saj", "tashtir"]}

NOTE_Q = {
 "id": "al-qafiya",
 "title": {"ar": "الْقَافِيَةُ — حُرُوفُهَا وَحَرَكَاتُهَا وَأَسْمَاؤُهَا", "en": "The qafiya — its letters, its vowels and its names", "tr": "Kafiye — harfleri, harekeleri ve adları"},
 "level": 6, "group": "arud",
 "classicalSources": ["الخليل بن أحمد — القافية: الروي والوصل والخروج والردف والتأسيس والدخيل؛ المجرى والنفاذ والحذو والإشباع والرس والتوجيه", "الخزرجية — باب القافية"],
 "question": {
  "en": ["Which letter is the RAWĪ? The last letter the rhyme rests on — the lām of يَعْقِلُ / مَزْحَلُ, the jīm of اللَّهِجُ. A long vowel after it is the WAṢL (يَعْقِلُو), a pronoun's hāʾ after it the waṣl too and the vowel after that the KHURŪJ.",
         "What stands before the rawī? A long vowel right before it is the RIDF (the yāʾ of بَخِيلُ, the alif of غِضَابَا); an alif with ONE letter between it and the rawī is the TAʾSĪS and that letter the DAKHĪL (تُقَاتِلِ: alif, tāʾ, lām).",
         "What are the six vowels called? The rawī's own is the MAJRĀ (ḍamma in يَعْقِلُ — a muṭlaqa rhyme; a sākin rawī makes it muqayyada); the waṣl-hāʾ's the NAFĀDH; the one before the ridf the ḤADHW; the dakhīl's the ISHBĀʿ; the one before the taʾsīs the RASS; the one before a sākin rawī the TAWJĪH.",
         "And its name? Count the moving letters between the close's last two still ones: none — mutarādif; one — mutawātir (تَسْتَطِيعُو); two — mutadārik (مَنْزِلِي); three — mutarākib (سُبُلَا); four — mutakāwis. The engine reads all of it off the last word of the ʿajuz."],
  "tr": ["REVÎ hangi harftir? Kafiyenin dayandığı son harf — يَعْقِلُ / مَزْحَلُ'nun lâmı, اللَّهِجُ'nun cîmi. Ondan sonraki uzun ünlü VASL'dır (يَعْقِلُو), sonraki zamir hâsı da vasl, onun ardındaki ünlü HURÛC.",
         "Revîden önce ne durur? Hemen önündeki uzun ünlü RİDF'tir (بَخِيلُ'nün yâ'sı, غِضَابَا'nın elifi); revî ile arasında TEK harf bulunan elif TE'SÎS, o harf DAHÎL'dir (تُقَاتِلِ: elif, tâ, lâm).",
         "Altı hareke nasıl adlanır? Revînin kendi harekesi MECRÂ (يَعْقِلُ'da damme — mutlaka kafiye; sâkin revî onu mukayyede yapar); vasl hâsınınki NEFÂZ; ridften öncekisi HAZV; dahîlinki İŞBÂ; te'sîsten öncekisi RESS; sâkin revîden öncekisi TEVCÎH.",
         "Adı? Sonun son iki sâkini arasındaki hareketli harfleri say: hiç — mütrâdif; bir — mütevâtir (تَسْتَطِيعُو); iki — mütedârik (مَنْزِلِي); üç — müterâkib (سُبُلَا); dört — mütekâvis. Motor hepsini acüzün son kelimesinden okur."]},
 "plain": {
  "en": "The rhyme is the last word's tail read by rule: which letter carries it, which long vowels lean on it, and what its vowels are called.",
  "tr": "Kafiye, son kelimenin kurala göre okunan kuyruğudur: onu hangi harf taşır, hangi uzun ünlüler ona yaslanır, harekeleri ne diye anılır."},
 "explanation": {
  "en": "الْقَافِيَةُ مِنْ آخِرِ حَرْفٍ فِي الْبَيْتِ إِلَى أَوَّلِ سَاكِنٍ يَلِيهِ مِنْ قَبْلِهِ مَعَ الْمُتَحَرِّكِ الَّذِي قَبْلَ السَّاكِنِ. Al-Khalil defines the rhyme as a stretch of the close, not a letter, and then names every seat in it. The rawī is the letter the poem is called by (a lāmiyya, a jīmiyya): the last real consonant of the close — a long vowel or a pronoun after it is the waṣl, and a vowel lengthened after the hāʾ the khurūj. Before the rawī two things may stand: the ridf, a madd letter leaning directly on it (the yāʾ of بَخِيلُ, the alif of غِضَابَا — the wāw and the yāʾ may alternate through a poem, the alif never), and the taʾsīs, an alif one letter away from it, that one letter being the dakhīl (تُقَاتِلِ). Six vowels have names because each must be kept through the poem: the majrā on the rawī — a rhyme is muṭlaqa when the rawī moves and muqayyada when it stands; the nafādh on the waṣl's hāʾ; the ḥadhw before the ridf; the ishbāʿ on the dakhīl; the rass before the taʾsīs; the tawjīh before a sākin rawī. And the whole close is named by the moving letters between its last two sākins — mutarādif, mutawātir, mutadārik, mutarākib, mutakāwis. Luzūm mā lā yalzam (ch72) is precisely keeping, before the rawī, a letter these rules did not require.",
  "tr": "الْقَافِيَةُ مِنْ آخِرِ حَرْفٍ فِي الْبَيْتِ إِلَى أَوَّلِ سَاكِنٍ يَلِيهِ مِنْ قَبْلِهِ مَعَ الْمُتَحَرِّكِ الَّذِي قَبْلَ السَّاكِنِ. Halîl kafiyeyi bir harf değil sonun bir parçası olarak tanımlar, sonra içindeki her yeri adlandırır. Revî, şiirin kendisiyle anıldığı harftir (lâmiyye, cîmiyye): sonun son gerçek ünsüzü — ondan sonraki uzun ünlü yahut zamir vasldır, hâ'dan sonra uzatılan hareke hurûc. Revîden önce iki şey durabilir: ridf, ona doğrudan yaslanan med harfi (بَخِيلُ'nün yâ'sı, غِضَابَا'nın elifi — vâv ile yâ şiir boyunca değişebilir, elif asla), ve te'sîs, ondan bir harf uzakta elif, o bir harf de dahîl (تُقَاتِلِ). Altı harekenin adı vardır çünkü her biri şiir boyunca korunmalıdır: revîde mecrâ — revî hareketliyse kafiye mutlaka, sâkinse mukayyede; vasl hâsında nefâz; ridften önce hazv; dahîlde işbâ; te'sîsten önce ress; sâkin revîden önce tevcîh. Sonun bütünü de son iki sâkin arasındaki hareketlilerle adlanır — mütrâdif, mütevâtir, mütedârik, müterâkib, mütekâvis. Lüzûm-i mâ lâ yelzem (bâb 72) tam da bu kuralların istemediği bir harfi revîden önce korumaktır."},
 "examples": [
  {"ar": "عَلَى طَرَفِ الْهِجْرَانِ إِنْ كَانَ يَعْقِلُ", "en": "rawī lām, majrā ḍamma, waṣl wāw — a mutadārik rhyme.", "tr": "revî lâm, mecrâ damme, vasl vâv — mütedârik kafiye.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"},
  {"ar": "إِنَّ الزَّمَانَ بِمِثْلِهِ لَبَخِيلُ", "en": "rawī lām with the yāʾ as ridf and a kasra as ḥadhw.", "tr": "revî lâm, yâ ridf, kesre hazv.", "sourceStory": "talkhis-al-miftah", "sentence": "s18"},
  {"ar": "لَهَا الْمَنَايَا إِلَى أَرْوَاحِنَا سُبُلَا", "en": "rawī lām, the alif of iṭlāq as waṣl — a mutarākib rhyme.", "tr": "revî lâm, ıtlak elifi vasl — müterâkib kafiye.", "sourceStory": "talkhis-al-miftah", "sentence": "s22"}],
 "commonMistakes": [
  {"wrong": "«بَخِيلَا'nın revîsi eliftir: son harf o»",
   "right": "«Elif, revî lâmdan sonraki vasldır; kafiye lâmiyyedir»",
   "why": {"en": "A long vowel after the last consonant is never the rawī; it is the waṣl, and the poem is named by the consonant.", "tr": "Son ünsüzden sonraki uzun ünlü asla revî değildir; vasldır ve şiir ünsüzle anılır."}}],
 "relatedNotes": ["ilm-al-arud", "luzum-ma-la-yalzam", "saj"]}

ADD_EN = (" Chapter 73 (lines ~4617-4660, sahifa 159-161) opens the khatima: the poetic takings — the agreement in a general purpose is no taking (s2), "
          "the way of signifying is unless shared (s3-s5), the two kinds of taking (s6-s7), the naskh and intihal (s8; Maʿn b. Aws taken whole by "
          "Ibn al-Zubayr, s9-s11; the synonym swap, s12), the ighara and maskh in its three grades (s13; Bashshar and Salm s14-s16; Abu Tammam and "
          "al-Mutanabbi s17-s19 and s20-s22). The rulings are RESTORED from the received matn and marked; the bayts are the source's printed Arabic. "
          "The `badi` frame `sariqa` sits on the TAKER's bayt and names the source in `with`, the kind in `kind2` and the book's grade in `grade`. "
          "Two ʿarud notes (ilm-al-arud, al-qafiya, group arud) anchor on the bayts' first and rhyme words.")
ADD_TR = (" Yetmiş üçüncü bâb (satır ~4617-4660, sahife 159-161) hâtimeyi açar: şiir sirkatleri — genel maksatta ittifak sirkat değildir (s2), "
          "delâlet yönü ortak değilse öyledir (s3-s5), almanın iki türü (s6-s7), nesh ve intihâl (s8; İbnü'z-Zübeyr'in bütünüyle aldığı Ma'n b. Evs, "
          "s9-s11; eş anlamlı değişimi, s12), üç derecesiyle iğâre ve mesh (s13; Beşşâr ve Selm s14-s16; Ebû Temmâm ve Mütenebbî s17-s19 ve s20-s22). "
          "Hükümler alınan metinden GERİ YAZILMIŞ ve işaretlenmiştir; beyitler kaynağın basılı Arapçasıdır. `badi` çerçevesi `sariqa` ALANIN "
          "beytinde durur; kaynağı `with`te, cinsi `kind2`de, kitabın derecesini `grade`de adlandırır. İki arûz notu (ilm-al-arud, al-qafiya, "
          "grup arud) beyitlerin ilk ve kafiye kelimelerine bağlanır.")
write_out(73, S, TITLE, ADD_EN, ADD_TR, "4617-4660", GLOSS_ADD, notes=(NOTE_S, NOTE_A, NOTE_Q),
          related=(("ilm-al-badi", ["sariqat-shiriyya"]), ("saj", ["ilm-al-arud", "al-qafiya"]), ("luzum-ma-la-yalzam", ["al-qafiya"]), ("tashtir", ["ilm-al-arud"])))
report(73, S, GLOSS_ADD, (NOTE_S, NOTE_A, NOTE_Q))
