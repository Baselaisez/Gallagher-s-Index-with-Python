# -*- coding: utf-8 -*-
"""Author chapter 60 of talkhis-al-miftah — the RUJUʿ, the TAWRIYA (mujarrada /
murashshaha), the ISTIKHDAM in its two kinds and the LAFF WA-NASHR (murattab /
ghayr murattab / ijmali) — sahifa 140-141, lines ~4060-4100.

  RESTORED (the source carries the step only in Turkish): s1, s3-s4, s7, s10, the
          heads of s5-s6, s8-s9, s11-s13, the gloss of s13; the frames of every example.
  As printed: the ayat (20:5, 51:47, 28:73, 2:111) and the verses of Zuhayr,
          Muʿawiya b. Malik, al-Buhturi, Ibn Hayyus.

Frames: ruju (the claim and the retraction), tawriya (the word, its near and far
sense, the companion of the near sense when murashshaha), istikhdam (the word,
the pronouns, the sense by the word and the sense by the pronoun), laff-nashr
(the folded list and the spread list, matched by referent; murattab when the
surface order agrees, ijmali when the fold is one summary word).
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from talkhis_common import *
import sarf_gen as _sg

R = "ruju"; W = "tawriya"; X = "istikhdam"; L = "laff-wa-nashr"
TITLE = {"ar": "الرُّجُوعُ، وَالتَّوْرِيَةُ، وَالِاسْتِخْدَامُ، وَاللَّفُّ وَالنَّشْرُ",
         "en": "The Rujuʿ; the Tawriya; the Istikhdam; the Laff wa-Nashr",
         "tr": "Rücû; Tevriye; İstihdâm; Leff ü Neşr"}
S = []
def nahwa(full="نَحْوَ", tag=R, punct=":"):
    return tok(full, "nahwa", "noun", [tag, "maful-fih"], ("الْوَاوُ عَاطِفَةٌ، وَ" if full.startswith("وَ") else "") + "نَحْوَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ إِلَى الْمِثَالِ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.",
               "«such as» — a zarf annexed to the example.", "«… gibi» — örneğe izâfe edilmiş zarf.",
               segments=([seg("وَ", "wa", "conj"), seg("نَحْوَ", "nahwa", "noun")] if full.startswith("وَ") else None), punct=punct)
def wa_conj(full, lex, pos, tags, ar, en, tr, punct=None, pron=None):
    sg = [seg("وَ", "wa", "conj"), seg(full[1:] if pron is None else full[1:-len(pron[0])], lex, pos)]
    if pron: sg.append(seg(pron[0], pron[1], "pron"))
    return tok(full, lex, pos, tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=sg)
def minha(tag):
    return tok("وَمِنْهَا","min","part",[tag, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and among them» — a fronted khabar.", "«ve onlardan» — öne alınmış haber.",
               segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")])
def wahiya(tag, full="وَهِيَ"):
    lex = "hiya" if full.endswith("هِيَ") else "huwa"
    return tok(full, lex, "pron", [tag, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالضَّمِيرُ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.",
               segments=[seg("وَ","wa","conj"), seg(full[1:], lex, "pron")])
def an_masd(tag):
    return tok("أَنْ","an","part",[tag, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the interpreted masdar is the khabar.", "«… -mesi» — müevvel masdar haber.")
def mithal(word, lex, tag, first=False, punct=":"):
    return [tok("وَمِثَالُ" if not first else "مِثَالُ","mithal","noun",[tag, "mubtada-khabar", "idafa-definiteness"] + ([] if first else ["atf-nasaq"]), ("الْوَاوُ عَاطِفَةٌ، وَ" if not first else "") + "مِثَالُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«the example of» — the mubtada.", "«örneği» — mübtedâ.",
                segments=(None if first else [seg("وَ","wa","conj"), seg("مِثَالُ","mithal","noun")])),
            tok(word, lex, "noun", [tag, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«…» — mudaf ilayh.", "«…» — muzâfun ileyh.", punct=punct)]

# ----------- s1 — the rujuʿ (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "Among them is the RUJUʿ: the RETURN to the preceding speech by RETRACTING it, for a point." + R_EN,
 "tr": "Onlardan biri RÜCÛDUR: bir nükte için önceki söze onu NAKZEDEREK DÖNMEK." + R_TR},
 "tokens": [
  minha(R),
  tok("الرُّجُوعُ","ruju","noun",[R, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ رَجَعَ.", "«the rujuʿ» — masdar of رَجَعَ.", "«rücû» — رَجَعَ'nin masdarı.", punct="،"),
  wahiya(R, "وَهُوَ"),
  tok("الْعَوْدُ","awd","noun",[R, "mubtada-khabar", "masdar"], "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ عَادَ.", "«the return» — the khabar.", "«dönmek» — haber."),
  tok("إِلَى","ila","part",[R, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْكَلَامِ","kalam","noun",[R, "huruf-jarr"], "مَجْرُورٌ.", "«the speech».", "«söze»."),
  tok("السَّابِقِ","sabiq","noun",[R, "naat-sifa", "ism-fail"], "نَعْتٌ مَجْرُورٌ — اسْمُ فَاعِلِ سَبَقَ.", "«preceding» — a na't.", "«önceki» — na't."),
  tok("بِالنَّقْضِ","naqd","noun",[R, "huruf-jarr", "masdar"], "جَارٌّ وَمَجْرُورٌ — النَّقْضُ: إِبْطَالُ مَا قِيلَ.", "«by retracting» — the naqd: undoing what was said.", "«nakzederek» — nakz: söyleneni bozmak.",
      segments=[seg("بِ","bi","part"), seg("النَّقْضِ","naqd","noun")]),
  tok("لِنُكْتَةٍ","nukta","noun",[R, "huruf-jarr", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَنُكْتَةٍ مَجْرُورٌ — كَإِظْهَارِ التَّحَيُّرِ.", "«for a point» — such as showing bewilderment.", "«bir nükte için» — hayreti göstermek gibi.",
      segments=[seg("لِ","li","part"), seg("نُكْتَةٍ","nukta","noun")], punct=".")]})

# ----------- s2 — Zuhayr
S.append({"id": "s2", "translation": {
 "en": "As Zuhayr says: «Stand by the dwellings that time has NOT EFFACED — YES IT HAS, and the winds and the steady rains have changed them»." + R_EN,
 "tr": "Zuheyr'in dediği gibi: «Zamanın SİLMEDİĞİ diyarda dur — EVET SİLDİ, rüzgârlar ve sürekli yağmurlar onları değiştirdi»." + R_TR},
 "badi": [{"kind": "ruju", "pair": [5, 7]}],
 "tokens": [
  kaq(R, "كَقَوْلِ", "pron-3ms"),
  tok("زُهَيْرٍ","zuhayr","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — زُهَيْرُ بْنُ أَبِي سُلْمَى، صَاحِبُ الْمُعَلَّقَةِ.", "«Zuhayr» — b. Abi Sulma, of the Muʿallaqa.", "«Züheyr» — b. Ebî Sülmâ, Muallaka sahibi.", punct=":"),
  tok("قِفْ","waqafa","verb",[R, "imperative-amr", "mithal-verbs"], "فِعْلُ أَمْرٍ مِنْ وَقَفَ، حُذِفَتْ فَاؤُهُ، وَالْفَاعِلُ مُسْتَتِرٌ — أَنْتَ.", "«stand» — the imperative of the assimilated وَقَفَ, its waw dropped.", "«dur» — misâl وَقَفَ'nin emri, vâvı düşmüş."),
  tok("بِالدِّيَارِ","dar","noun",[R, "huruf-jarr", "jam-taksir"], "جَارٌّ وَمَجْرُورٌ — جَمْعُ دَارٍ.", "«by the dwellings» — plural of دَار.", "«diyarda» — دَار'ın çoğulu.",
      segments=[seg("بِ","bi","part"), seg("الدِّيَارِ","dar","noun")]),
  tok("الَّتِي","allati","pron",[R, "ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ نَعْتٌ لِلدِّيَارِ.", "«that» — the relative as a na't.", "«… -diği» — mevsûl, na't."),
  tok("لَمْ","lam","part",[R, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ — الدَّعْوَى الْأُولَى.", "«not» — the first claim begins.", "«-me» — ilk iddia başlar."),
  tok("يَعْفُهَا","afa","verb",[R, "lam-jazim", "naqis-verbs", "maful-bihi", "fail"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ الْأَلِفِ، وَهَا مَفْعُولٌ بِهِ — عَفَا الشَّيْءَ: مَحَاهُ؛ الْكَلَامُ السَّابِقُ الَّذِي يُرْجَعُ عَنْهُ.", "«has effaced it» — jazm by dropping the alif; the preceding speech that will be retracted.", "«onu sildi» — elif hazfiyle meczûm; geri dönülecek önceki söz.",
      segments=[seg("يَعْفُ","afa","verb"), seg("هَا","pron-3fs","pron")]),
  tok("الْقِدَمُ","qidam","noun",[R, "fail", "masdar"], "فَاعِلٌ مَرْفُوعٌ — مَصْدَرُ قَدُمَ: مُرُورُ الزَّمَانِ.", "«time» — the doer: the passing of the ages.", "«zaman» — fâil: eskilik, zamanın geçmesi.", punct="*"),
  tok("بَلَى","bala-yes","part",[R, "jawab-al-talab"], "حَرْفُ جَوَابٍ يُبْطِلُ النَّفْيَ — الرُّجُوعُ: نَقْضُ لَمْ يَعْفُهَا.", "«yes it has» — the answer-particle that undoes a negation: the RUJUʿ, retracting «has not effaced».", "«evet sildi» — nefyi bozan cevap harfi: RÜCÛ, «silmedi»yi nakzeder."),
  wa_conj("وَغَيَّرَهَا","ghayyara","verb",[R, "atf-nasaq", "maful-bihi", "form-ii-verbs"], "غَيَّرَ فِعْلٌ مَاضٍ، وَهَا مَفْعُولٌ بِهِ.", "«and changed them».", "«ve onları değiştirdi».", pron=("هَا","pron-3fs")),
  tok("الْأَرْوَاحُ","rih","noun",[R, "fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ رِيحٍ.", "«the winds» — the doer; plural of رِيح.", "«rüzgârlar» — fâil; رِيح'in çoğulu."),
  wa_conj("وَالدِّيَمُ","dima","noun",[R, "atf-nasaq", "jam-taksir"], "الدِّيَمُ مَعْطُوفٌ مَرْفُوعٌ — جَمْعُ دِيمَةٍ: الْمَطَرُ الدَّائِمُ.", "«and the steady rains» — plural of دِيمَة.", "«ve sürekli yağmurlar» — دِيمَة'nin çoğulu.", punct=".")]})
S[-1]["badi"] = [{"kind": "ruju", "pair": [6, 8]}]

# ----------- s3 — the tawriya defined (RESTORED matn)
S.append({"id": "s3", "translation": {
 "en": "Among them is the TAWRIYA, also called the IHAM: that a word with TWO SENSES, a NEAR and a FAR, be used, and the FAR one meant." + R_EN,
 "tr": "Onlardan biri, ÎHÂM da denilen TEVRİYEDİR: biri YAKIN, biri UZAK İKİ MÂNÂSI olan bir lafzın söylenip UZAK mânâsının kastedilmesi." + R_TR},
 "tokens": [
  minha(W),
  tok("التَّوْرِيَةُ","tawriya","noun",[W, "mubtada-khabar", "masdar", "form-ii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ وَرَّى: سَتَرَ.", "«the tawriya» — masdar of وَرَّى, to conceal.", "«tevriye» — وَرَّى'nın masdarı: gizlemek.", punct="،"),
  wa_conj("وَتُسَمَّى","samma","verb",[W, "atf-nasaq", "naib-al-fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "تُسَمَّى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is called».", "«ve denir»."),
  tok("الْإِيهَامَ","iham","noun",[W, "mafulayn", "masdar", "form-iv-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«the iham».", "«îhâm».", punct="،"),
  wahiya(W), an_masd(W),
  tok("يُطْلَقَ","atlaqa","verb",[W, "an-masdariyya", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«be used» — the passive: be let loose.", "«söylensin» — meçhûl: salınsın."),
  tok("لَفْظٌ","lafz","noun",[W, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a word».", "«bir lafız»."),
  tok("لَهُ","lahu","part",[W, "huruf-jarr", "jumla-sifa", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ؛ وَالْجُمْلَةُ نَعْتٌ لِلَفْظٍ.", "«having» — a fronted khabar; the clause describes «word».", "«… olan» — öne alınmış haber; cümle «lafız»ın na'tı.",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("مَعْنَيَانِ","mana","noun",[W, "mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two senses».", "«iki mânâ».", punct="،"),
  tok("قَرِيبٌ","qarib","noun",[W, "badal", "sifa-mushabbaha"], "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ.", "«a near» — badal of detail.", "«yakın» — tafsîl bedeli."),
  wa_conj("وَبَعِيدٌ","baid","noun",[W, "atf-nasaq", "sifa-mushabbaha"], "بَعِيدٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and a far».", "«ve uzak».", punct="،"),
  wa_conj("وَيُرَادَ","arada","verb",[W, "atf-nasaq", "naib-al-fail", "form-iv-verbs", "hollow-verbs"], "يُرَادَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَعْطُوفٌ عَلَى يُطْلَقَ، مَبْنِيٌّ لِلْمَجْهُولِ.", "«and be meant» — joined onto «be used».", "«ve kastedilsin» — «söylensin»e matuf."),
  tok("الْبَعِيدُ","baid","noun",[W, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — الْمَعْنَى الْبَعِيدُ هُوَ الْمُرَادُ.", "«the far» — the deputy doer: the far sense is the meant one.", "«uzak olan» — nâib-i fâil: uzak mânâ kastedilendir.", punct=".")]})

# ----------- s4 — two kinds (RESTORED matn)
S.append({"id": "s4", "translation": {
 "en": "It is of two kinds: the BARE (mujarrada), which is joined with nothing that suits the near sense; and the FURNISHED (murashshaha), which is joined with something that suits it." + R_EN,
 "tr": "İki kısımdır: yakın mânâya uygun hiçbir şeyle birlikte gelmeyen MÜCERREDE; ve ona uygun bir şeyle birlikte gelen MÜREŞŞAHA." + R_TR},
 "tokens": [
  wahiya(W),
  tok("ضَرْبَانِ","darb","noun",[W, "mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two kinds».", "«iki kısım».", punct=":"),
  tok("مُجَرَّدَةٌ","mujarrada","noun",[W, "badal", "ism-maful", "form-ii-verbs"], "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ — اسْمُ مَفْعُولِ جَرَّدَ.", "«bare» — ism maf'ul of جَرَّدَ.", "«mücerrede» — جَرَّدَ'nin ism-i mef'ûlü.", punct="،"),
  wahiya(W),
  tok("الَّتِي","allati","pron",[W, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«the one which» — the khabar.", "«… olan» — haber."),
  tok("لَا","la-nafiya","part",[W], "حَرْفُ نَفْيٍ.", "«not».", "«-mez»."),
  tok("تُجَامِعُ","jamaa-share","verb",[W, "ism-mawsul", "fail", "maful-bihi", "form-iii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مِنَ الْمُفَاعَلَةِ، وَالْفَاعِلُ مُسْتَتِرٌ — هِيَ؛ صِلَةٌ.", "«is joined with» — Form III; the sila.", "«birlikte gelir» — III. bâb; sıla."),
  tok("شَيْئًا","shay","noun",[W, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«anything».", "«bir şey»."),
  tok("مِمَّا","ma-mawsula","pron",[W, "huruf-jarr", "ism-mawsul"], "مِنْ جَارَّةٌ وَمَا مَوْصُولَةٌ، أُدْغِمَتِ النُّونُ فِي الْمِيمِ.", "«of what» — min and the relative ma, the nun assimilated.", "«… olandan» — min ve mevsûle mâ, nûn mîme idgam edilmiş.",
      segments=[seg("مِمْ","min","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يُلَائِمُ","laama","verb",[W, "ism-mawsul", "fail", "maful-bihi", "form-iii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مِنَ الْمُفَاعَلَةِ، وَالْفَاعِلُ مُسْتَتِرٌ؛ صِلَةٌ.", "«suits».", "«uygun düşer»."),
  tok("الْقَرِيبَ","qarib","noun",[W, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمَعْنَى الْقَرِيبَ.", "«the near» — the near sense.", "«yakın olana» — yakın mânâya.", punct="؛"),
  wa_conj("وَمُرَشَّحَةٌ","murashshaha","noun",[W, "atf-nasaq", "ism-maful", "form-ii-verbs"], "مُرَشَّحَةٌ مَعْطُوفٌ عَلَى مُجَرَّدَةٌ — اسْمُ مَفْعُولِ رَشَّحَ: قَوَّى.", "«and furnished» — ism maf'ul of رَشَّحَ, to strengthen.", "«ve müreşşaha» — رَشَّحَ'nin ism-i mef'ûlü: güçlendirmek.", punct="،"),
  wahiya(W),
  tok("الَّتِي","allati","pron",[W, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«the one which».", "«… olan»."),
  tok("تُجَامِعُ","jamaa-share","verb",[W, "ism-mawsul", "fail", "maful-bihi", "form-iii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ؛ صِلَةٌ.", "«is joined with».", "«birlikte gelir»."),
  tok("شَيْئًا","shay","noun",[W, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«something».", "«bir şey»."),
  tok("مِمَّا","ma-mawsula","pron",[W, "huruf-jarr", "ism-mawsul"], "مِنْ وَمَا الْمَوْصُولَةُ.", "«of what».", "«… olandan».",
      segments=[seg("مِمْ","min","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يُلَائِمُهُ","laama","verb",[W, "ism-mawsul", "fail", "maful-bihi", "form-iii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — يَعُودُ عَلَى الْقَرِيبِ.", "«suits it» — «it» the near sense.", "«ona uygun düşer» — «o» yakın mânâ.",
      segments=[seg("يُلَائِمُ","laama","verb"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s5 — mujarrada: 20:5
S.append({"id": "s5", "translation": {
 "en": "The example of the bare: «The All-Merciful SETTLED upon the Throne» (20:5) — the near sense «sat firm», the far sense «held sway»; nothing that suits the near sense is mentioned." + R_EN,
 "tr": "Mücerredenin örneği: «Rahmân arşa İSTİVÂ ETTİ» (Tâhâ 20:5) — yakın mânâ «karar kıldı», uzak mânâ «istîlâ etti»; yakın mânâya uygun bir şey anılmamış." + R_TR},
 "badi": [{"kind": "tawriya", "word": 4, "sub": "mujarrada", "near": {"en": "settled, sat firm", "tr": "karar kıldı, yerleşti"}, "far": {"en": "held sway, took full possession", "tr": "istîlâ etti, hükmü altına aldı"}}],
 "tokens": mithal("الْمُجَرَّدَةِ", "mujarrada", W, first=True) + [
  tok("الرَّحْمَنُ","rahman","noun",[W, "mubtada-khabar", "sighat-mubalagha"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the All-Merciful» — the mubtada.", "«Rahmân» — mübtedâ."),
  tok("عَلَى","ala","part",[W, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«upon».", "«-e»."),
  tok("الْعَرْشِ","arsh","noun",[W, "huruf-jarr"], "مَجْرُورٌ.", "«the Throne».", "«arşa»."),
  tok("اسْتَوَى","istawa","verb",[W, "mubtada-khabar", "fail", "form-viii-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ مِنَ الِافْتِعَالِ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ؛ وَالْجُمْلَةُ خَبَرٌ — التَّوْرِيَةُ: الْقَرِيبُ الِاسْتِقْرَارُ، وَالْبَعِيدُ الِاسْتِيلَاءُ وَهُوَ الْمُرَادُ؛ مُجَرَّدَةٌ إِذْ لَمْ يُذْكَرْ مَا يُلَائِمُ الْقَرِيبَ.", "«settled» — the TAWRIYA: the near sense is settling, the far sense holding sway, and the far is meant; bare, since nothing suiting the near sense is mentioned.", "«istivâ etti» — TEVRİYE: yakın mânâ karar kılma, uzak mânâ istîlâ ve uzak kastedilmiş; mücerrede, çünkü yakına uygun bir şey anılmamış.", punct=".")]}
)
S[-1]["badi"] = [{"kind": "tawriya", "word": 5, "sub": "mujarrada", "near": {"en": "settled, sat firm", "tr": "karar kıldı, yerleşti"}, "far": {"en": "held sway, took full possession", "tr": "istîlâ etti, hükmü altına aldı"}}]

# ----------- s6 — murashshaha: 51:47
S.append({"id": "s6", "translation": {
 "en": "And the example of the furnished: «And the heaven — We BUILT it with HANDS» (51:47) — the near sense of أَيْد «hands», the far sense «strength»; «We built» suits the near sense." + R_EN,
 "tr": "Müreşşahanın örneği: «Göğü ELLERLE BİNA ETTİK» (Zâriyât 51:47) — أَيْد'in yakın mânâsı «eller», uzak mânâsı «kuvvet»; «bina ettik» yakın mânâya uygundur." + R_TR},
 "badi": [{"kind": "tawriya", "word": 5, "sub": "murashshaha", "companion": 4, "near": {"en": "hands", "tr": "eller"}, "far": {"en": "strength, power", "tr": "kuvvet, güç"}}],
 "tokens": mithal("الْمُرَشَّحَةِ", "murashshaha", W) + [
  wa_conj("وَالسَّمَاءَ","sama","noun",[W, "atf-nasaq", "maful-bihi", "ism-mamdud"], "السَّمَاءَ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ — عَلَى الِاشْتِغَالِ.", "«and the heaven» — the object of a dropped verb that the spoken one explains.", "«ve göğü» — söylenenin açıkladığı hazfedilmiş fiilin mef'ûlü."),
  tok("بَنَيْنَاهَا","bana","verb",[W, "fail", "maful-bihi", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ — يُلَائِمُ الْأَيْدِيَ: التَّرْشِيحُ.", "«We built it» — suits «hands»: the furnishing.", "«onu bina ettik» — «eller»e uygun: terşîh.",
      segments=[seg("بَنَيْ","bana","verb"), seg("نَا","pron-1p","pron"), seg("هَا","pron-3fs","pron")]),
  tok("بِأَيْدٍ","ayd-strength","noun",[W, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — التَّوْرِيَةُ: الْقَرِيبُ جَمْعُ يَدٍ، وَالْبَعِيدُ الْقُوَّةُ وَهُوَ الْمُرَادُ؛ مُرَشَّحَةٌ لِذِكْرِ بَنَيْنَا.", "«with hands» — the TAWRIYA: the near sense the plural of يَد, the far sense strength, and the far is meant; furnished by «We built».", "«ellerle» — TEVRİYE: yakın mânâ يَد'in çoğulu, uzak mânâ kuvvet ve uzak kastedilmiş; «bina ettik» ile müreşşaha.",
      segments=[seg("بِ","bi","part"), seg("أَيْدٍ","ayd-strength","noun")], punct=".")]}
)
S[-1]["badi"] = [{"kind": "tawriya", "word": 4, "sub": "murashshaha", "companion": 3, "near": {"en": "hands", "tr": "eller"}, "far": {"en": "strength, power", "tr": "kuvvet, güç"}}]

# ----------- s7 — the istikhdam defined (RESTORED matn)
S.append({"id": "s7", "translation": {
 "en": "Among them is the ISTIKHDAM: that by a word with two senses ONE be meant, then by its PRONOUN the OTHER; or that by one of its two pronouns one sense be meant, and by the other the other." + R_EN,
 "tr": "Onlardan biri İSTİHDÂMDIR: iki mânâlı bir lafızla BİRİ, sonra ZAMİRİYLE ÖBÜRÜ kastedilir; yahut iki zamirinden biriyle bir mânâ, öbürüyle öbür mânâ kastedilir." + R_TR},
 "tokens": [
  minha(X),
  tok("الِاسْتِخْدَامُ","istikhdam","noun",[X, "mubtada-khabar", "masdar", "form-x-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ اسْتَخْدَمَ.", "«the istikhdam» — masdar of اسْتَخْدَمَ, to put to service.", "«istihdâm» — اسْتَخْدَمَ'nin masdarı: hizmete koşmak.", punct="،"),
  wahiya(X, "وَهُوَ"), an_masd(X),
  tok("يُرَادَ","arada","verb",[X, "an-masdariyya", "naib-al-fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«be meant».", "«kastedilsin»."),
  tok("بِلَفْظٍ","lafz","noun",[X, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«by a word».", "«bir lafızla».",
      segments=[seg("بِ","bi","part"), seg("لَفْظٍ","lafz","noun")]),
  tok("لَهُ","lahu","part",[X, "huruf-jarr", "jumla-sifa", "mubtada-khabar"], "خَبَرٌ مُقَدَّمٌ؛ وَالْجُمْلَةُ نَعْتٌ.", "«having».", "«… olan».",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("مَعْنَيَانِ","mana","noun",[X, "mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مُؤَخَّرٌ.", "«two senses».", "«iki mânâ»."),
  tok("أَحَدُهُمَا","ahad","noun",[X, "naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ — أَحَدُ الْمَعْنَيَيْنِ.", "«one of the two» — the deputy doer.", "«ikisinden biri» — nâib-i fâil.",
      segments=[seg("أَحَدُ","ahad","noun"), seg("هُمَا","pron-3d","pron")], punct="،"),
  tok("ثُمَّ","thumma","conj",[X, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  tok("بِضَمِيرِهِ","damir","noun",[X, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ — ضَمِيرِ اللَّفْظِ.", "«by its pronoun» — the word's pronoun.", "«zamiriyle» — lafzın zamiri.",
      segments=[seg("بِ","bi","part"), seg("ضَمِيرِ","damir","noun"), seg("هِ","pron-3ms","pron")]),
  tok("الْآخَرُ","akhar","noun",[X, "naib-al-fail"], "نَائِبُ فَاعِلٍ لِفِعْلٍ مَحْذُوفٍ — يُرَادَ الْآخَرُ.", "«the other» — the deputy doer of an understood «be meant».", "«öbürü» — anlaşılan «kastedilsin»in nâib-i fâili.", punct="؛"),
  tok("أَوْ","aw","conj",[X, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("يُرَادَ","arada","verb",[X, "atf-nasaq", "naib-al-fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَعْطُوفٌ.", "«be meant».", "«kastedilsin»."),
  tok("بِأَحَدِ","ahad","noun",[X, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ.", "«by one of».", "«birinden».",
      segments=[seg("بِ","bi","part"), seg("أَحَدِ","ahad","noun")]),
  tok("ضَمِيرَيْهِ","damir","noun",[X, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، مُضَافٌ.", "«its two pronouns».", "«iki zamiri».",
      segments=[seg("ضَمِيرَيْ","damir","noun"), seg("هِ","pron-3ms","pron")]),
  tok("أَحَدُهُمَا","ahad","noun",[X, "naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — أَحَدُ الْمَعْنَيَيْنِ.", "«one of them» — one of the senses.", "«biri» — mânâlardan biri.",
      segments=[seg("أَحَدُ","ahad","noun"), seg("هُمَا","pron-3d","pron")]),
  tok("ثُمَّ","thumma","conj",[X, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  tok("بِالْآخَرِ","akhar","noun",[X, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — بِالضَّمِيرِ الْآخَرِ.", "«by the other» — the other pronoun.", "«öbürüyle» — öbür zamirle.",
      segments=[seg("بِ","bi","part"), seg("الْآخَرِ","akhar","noun")]),
  tok("الْآخَرُ","akhar","noun",[X, "naib-al-fail"], "نَائِبُ فَاعِلٍ — الْمَعْنَى الْآخَرُ.", "«the other» — the other sense.", "«öbürü» — öbür mânâ.", punct=".")]})

# ----------- s8 — Muʿawiya b. Malik: the first kind
S.append({"id": "s8", "translation": {
 "en": "The example of the first, Muʿawiya b. Malik's: «When the SKY comes down on a people's land, we graze IT — even if they are angry»: by «sky» the rain, by its pronoun the herbage." + R_EN,
 "tr": "Birincinin örneği, Muâviye b. Mâlik'in: «GÖK bir kavmin toprağına indiğinde ONU otlatırız — kızsalar da»: «gök» ile yağmur, zamiriyle ot." + R_TR},
 "badi": [{"kind": "istikhdam", "word": 6, "sub": "lafz-damir", "refs": [10], "murad": {"en": "the rain (by the word)", "tr": "yağmur (lafızla)"}, "other": {"en": "the herbage it brings up (by the pronoun)", "tr": "bitirdiği ot (zamirle)"}}],
 "tokens": [
  tok("مِثَالُ","mithal","noun",[X, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«the example of».", "«örneği»."),
  tok("الْأَوَّلِ","awwal","noun",[X, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the first».", "«birincinin»."),
  tok("قَوْلُ","qawl","noun",[X, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the saying of» — the khabar.", "«sözü» — haber."),
  tok("مُعَاوِيَةَ","muawiya-ibn-malik","noun",[X, "idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مُعَاوِيَةُ بْنُ مَالِكٍ، مُعَوِّدُ الْحُكَمَاءِ.", "«Muʿawiya» — b. Malik, «the trainer of the wise».", "«Muâviye» — b. Mâlik, Muavvidü'l-hukemâ."),
  tok("بْنِ","ibn","noun",[X, "naat-sifa", "idafa-definiteness"], "نَعْتٌ، مُضَافٌ.", "«son of».", "«oğlu»."),
  tok("مَالِكٍ","malik-name","noun",[X, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Malik».", "«Mâlik».", punct=":"),
  tok("إِذَا","idha","part",[X, "idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«… -diğinde»."),
  tok("نَزَلَ","nazala","verb",[X, "idha-shartiyya", "fail"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ.", "«comes down».", "«iner»."),
  tok("السَّمَاءُ","sama","noun",[X, "fail", "ism-mamdud"], "فَاعِلٌ مَرْفُوعٌ — أُرِيدَ بِهِ الْمَطَرُ: الْمَعْنَى الْأَوَّلُ بِاللَّفْظِ نَفْسِهِ.", "«the sky» — the rain is meant: the first sense, by the word itself.", "«gök» — yağmur kastedilmiş: birinci mânâ, lafzın kendisiyle."),
  tok("بِأَرْضِ","ard","noun",[X, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ.", "«on the land of».", "«toprağına».",
      segments=[seg("بِ","bi","part"), seg("أَرْضِ","ard","noun")]),
  tok("قَوْمٍ","qawm","noun",[X, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a people».", "«bir kavmin».", punct="*"),
  tok("رَعَيْنَاهُ","raa-pasture","verb",[X, "fail", "maful-bihi", "naqis-verbs", "jawab-al-talab"], "فِعْلٌ مَاضٍ، وَنَا فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — يَعُودُ عَلَى السَّمَاءِ وَأُرِيدَ بِهِ النَّبْتُ: الْمَعْنَى الْآخَرُ بِالضَّمِيرِ؛ وَالْجُمْلَةُ جَوَابُ إِذَا.", "«we graze it» — the pronoun goes back to «sky» and the herbage is meant: the other sense, by the pronoun; the answer of «when».", "«onu otlatırız» — zamir «gök»e döner ve ot kastedilmiş: öbür mânâ, zamirle; «-diğinde»nin cevabı.",
      segments=[seg("رَعَيْ","raa-pasture","verb"), seg("نَا","pron-1p","pron"), seg("هُ","pron-3ms","pron")]),
  wa_conj("وَإِنْ","in-shartiyya","part",[X, "atf-nasaq", "in-shartiyya"], "إِنْ وَصْلِيَّةٌ — وَلَوْ.", "«even if» — the concessive in.", "«… -se de» — vasliyye in."),
  tok("كَانُوا","kana","verb",[X, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ.", "«they are».", "«onlar … olsalar».",
      segments=[seg("كَانُ","kana","verb"), seg("وا","pron-3mp","pron")]),
  tok("غِضَابًا","ghadban","noun",[X, "kana-wa-akhawatuha", "jam-taksir"], "خَبَرُ كَانَ مَنْصُوبٌ — جَمْعُ غَضْبَانَ.", "«angry» — plural of غَضْبَان.", "«kızgın» — غَضْبَان'ın çoğulu.", punct=".")]})
S[-1]["badi"] = [{"kind": "istikhdam", "word": 8, "sub": "lafz-damir", "refs": [11], "murad": {"en": "the rain (by the word)", "tr": "yağmur (lafızla)"}, "other": {"en": "the herbage it brings up (by the pronoun)", "tr": "bitirdiği ot (zamirle)"}}]

# ----------- s9 — al-Buhturi: the second kind
S.append({"id": "s9", "translation": {
 "en": "And the example of the second, al-Buhturi's: «May He water the GHADA and those who dwell in IT — though they kindled IT between my ribs»: by the first pronoun the place of the ghada, by the second its fire." + R_EN,
 "tr": "İkincinin örneği, Buhturî'nin: «GADÂYI ve ONDA oturanları sulasın — ONU kaburgalarımın arasında tutuşturmuş olsalar da»: birinci zamirle gadânın yeri, ikinciyle ateşi." + R_TR},
 "badi": [{"kind": "istikhdam", "word": 6, "sub": "damirayn", "refs": [7, 10], "murad": {"en": "the place of the ghada trees (first pronoun)", "tr": "gadâ ağaçlarının yeri (birinci zamir)"}, "other": {"en": "the fire of the ghada wood (second pronoun)", "tr": "gadâ odununun ateşi (ikinci zamir)"}}],
 "tokens": [
  wa_conj("وَمِثَالُ","mithal","noun",[X, "atf-nasaq", "mubtada-khabar", "idafa-definiteness"], "مِثَالُ مُبْتَدَأٌ، مُضَافٌ.", "«and the example of».", "«ve örneği»."),
  tok("الثَّانِي","thani","noun",[X, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«the second».", "«ikincinin»."),
  tok("قَوْلُ","qawl","noun",[X, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ، مُضَافٌ.", "«the saying of».", "«sözü»."),
  tok("الْبُحْتُرِيِّ","buhturi","noun",[X, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Buhturi».", "«Buhturî».", punct=":"),
  tok("فَسَقَى","saqa-water","verb",[X, "fail", "maful-bihi", "naqis-verbs", "khabar-fi-mana-al-insha"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَسَقَى فِعْلٌ مَاضٍ فِي مَعْنَى الدُّعَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ، اللهُ.", "«may He water» — the past in the sense of a prayer; the doer «He» concealed.", "«sulasın» — duâ mânâsında mâzî; fâil gizli «O».",
      segments=[seg("فَ","fa","conj"), seg("سَقَى","saqa-water","verb")]),
  tok("الْغَضَا","ghada","noun",[X, "maful-bihi", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — شَجَرٌ يَدُومُ جَمْرُهُ؛ اللَّفْظُ ذُو الْمَعْنَيَيْنِ: مَكَانُهُ وَنَارُهُ.", "«the ghada» — the tree whose embers last; the two-sense word: its place and its fire.", "«gadâ» — közü uzun süren ağaç; iki mânâlı lafız: yeri ve ateşi."),
  wa_conj("وَالسَّاكِنِيهِ","sakin","noun",[X, "atf-nasaq", "ism-fail", "jam-mudhakkar-salim", "idafa-lafziyya"], "السَّاكِنِي مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الضَّمِيرُ الْأَوَّلُ: أُرِيدَ بِهِ مَكَانُ الْغَضَا.", "«and those who dwell in it» — the sound plural, its nun dropped for the idafa; the FIRST pronoun: the ghada's place is meant.", "«ve onda oturanları» — cem'-i müzekker, nûnu izâfet için düşmüş; BİRİNCİ zamir: gadânın yeri kastedilmiş.", pron=("هِ","pron-3ms")),
  wa_conj("وَإِنْ","in-shartiyya","part",[X, "atf-nasaq", "in-shartiyya"], "إِنْ وَصْلِيَّةٌ.", "«though».", "«… -sa da»."),
  tok("هُمُ","hum","pron",[X, "mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ، وَالْمِيمُ مَضْمُومَةٌ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«they» — the mubtada.", "«onlar» — mübtedâ.", punct="*"),
  tok("شَبُّوهُ","shabba","verb",[X, "mubtada-khabar", "fail", "maful-bihi", "doubled-verbs"], "فِعْلٌ مَاضٍ مُضَاعَفٌ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — الضَّمِيرُ الثَّانِي: أُرِيدَ بِهِ نَارُ الْغَضَا؛ وَالْجُمْلَةُ خَبَرٌ.", "«they kindled it» — the SECOND pronoun: the ghada's fire is meant.", "«onu tutuşturdular» — İKİNCİ zamir: gadânın ateşi kastedilmiş.",
      segments=[seg("شَبُّ","shabba","verb"), seg("و","pron-3mp","pron"), seg("هُ","pron-3ms","pron")]),
  tok("بَيْنَ","bayna","noun",[X, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«between».", "«arasında»."),
  tok("جَوَانِحِي","janiha","noun",[X, "idafa-definiteness", "jam-taksir", "ya-al-mutakallim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ جَانِحَةٍ: الضُّلُوعُ الْقُصْرَى.", "«my ribs» — plural of جَانِحَة: the short ribs.", "«kaburgalarımın» — جَانِحَة'nin çoğulu: kısa kaburgalar.",
      segments=[seg("جَوَانِحِ","janiha","noun"), seg("ي","pron-1s","pron")]),
  wa_conj("وَضُلُوعِي","dil","noun",[X, "atf-nasaq", "jam-taksir", "ya-al-mutakallim"], "ضُلُوعِي مَعْطُوفٌ مَجْرُورٌ — جَمْعُ ضِلْعٍ.", "«and my ribs» — plural of ضِلْع.", "«ve kaburgalarım» — ضِلْع'in çoğulu.", pron=("ي","pron-1s"), punct=".")]})
S[-1]["badi"] = [{"kind": "istikhdam", "word": 5, "sub": "damirayn", "refs": [6, 9], "murad": {"en": "the place of the ghada trees (first pronoun)", "tr": "gadâ ağaçlarının yeri (birinci zamir)"}, "other": {"en": "the fire of the ghada wood (second pronoun)", "tr": "gadâ odununun ateşi (ikinci zamir)"}}]

# ----------- s10 — laff wa-nashr defined (RESTORED matn)
S.append({"id": "s10", "translation": {
 "en": "Among them is the LAFF WA-NASHR: the mention of SEVERAL things, in detail or in sum, then the mention of what belongs to EACH — without specifying — trusting that the hearer will return each to its owner." + R_EN,
 "tr": "Onlardan biri LEFF Ü NEŞİRDİR: BİRDEN ÇOK şeyin tafsîlen yahut icmâlen anılması, sonra — tayin etmeksizin — HER BİRİNE ait olanın anılması; dinleyenin her birini sahibine döndüreceğine güvenerek." + R_TR},
 "tokens": [
  minha(L),
  tok("اللَّفُّ","laff","noun",[L, "mubtada-khabar", "masdar", "doubled-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ لَفَّ: طَوَى.", "«the folding» — masdar of لَفَّ.", "«leff» — لَفَّ'nin masdarı: dürmek."),
  wa_conj("وَالنَّشْرُ","nashr","noun",[L, "atf-nasaq", "masdar"], "النَّشْرُ مَعْطُوفٌ مَرْفُوعٌ — مَصْدَرُ نَشَرَ: بَسَطَ.", "«and the spreading» — masdar of نَشَرَ.", "«ve neşir» — نَشَرَ'nin masdarı: yaymak.", punct="،"),
  wahiya(L, "وَهُوَ"),
  tok("ذِكْرُ","dhikr","noun",[L, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the mention of».", "«anılması»."),
  tok("مُتَعَدِّدٍ","mutaaddid","noun",[L, "idafa-definiteness", "ism-fail", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلِ تَعَدَّدَ.", "«several things» — ism fa'il of تَعَدَّدَ.", "«birden çok şey» — تَعَدَّدَ'nin ism-i fâili."),
  tok("عَلَى","ala","part",[L, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«… üzere»."),
  tok("التَّفْصِيلِ","tafsil","noun",[L, "huruf-jarr", "masdar", "form-ii-verbs"], "مَجْرُورٌ — مَصْدَرُ فَصَّلَ.", "«detail».", "«tafsîl»."),
  tok("أَوِ","aw","conj",[L, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("الْإِجْمَالِ","ijmal","noun",[L, "atf-nasaq", "masdar", "form-iv-verbs"], "مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ أَجْمَلَ.", "«sum».", "«icmâl».", punct="،"),
  tok("ثُمَّ","thumma","conj",[L, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  tok("ذِكْرُ","dhikr","noun",[L, "atf-nasaq", "idafa-definiteness", "masdar"], "مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«the mention of».", "«anılması»."),
  tok("مَا","ma-mawsula","pron",[L, "ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ.", "«what».", "«… olanın»."),
  tok("لِكُلٍّ","kull","noun",[L, "huruf-jarr", "zarf-mustaqarr-wa-laghw"], "جَارٌّ وَمَجْرُورٌ صِلَةٌ — لِكُلِّ وَاحِدٍ.", "«belongs to each» — the sila.", "«her birine ait» — sıla.",
      segments=[seg("لِ","li","part"), seg("كُلٍّ","kull","noun")]),
  tok("مِنْ","min","part",[L, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«without».", "«-sızın»."),
  tok("غَيْرِ","ghayr","noun",[L, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«(without)».", "«(-sızın)»."),
  tok("تَعْيِينٍ","tayin","noun",[L, "idafa-definiteness", "masdar", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ عَيَّنَ.", "«specifying».", "«tayin».", punct="،"),
  tok("ثِقَةً","thiqa","noun",[L, "maful-lah", "masdar"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ.", "«trusting» — the object of cause.", "«güvenerek» — mef'ûlün leh."),
  tok("بِأَنَّ","anna","part",[L, "huruf-jarr", "inna-wa-akhawatuha"], "الْبَاءُ جَارَّةٌ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«that».", "«… -ine».",
      segments=[seg("بِ","bi","part"), seg("أَنَّ","anna","part")]),
  tok("السَّامِعَ","sami-hearer","noun",[L, "inna-wa-akhawatuha", "ism-fail"], "اسْمُ أَنَّ مَنْصُوبٌ — اسْمُ فَاعِلِ سَمِعَ.", "«the hearer» — the ism of anna.", "«dinleyen» — ennenin ismi."),
  tok("يَرُدُّهُ","radda","verb",[L, "inna-wa-akhawatuha", "fail", "maful-bihi", "doubled-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مُضَاعَفٌ، وَالْهَاءُ مَفْعُولٌ بِهِ؛ وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«will return it» — anna's khabar.", "«onu döndürür» — ennenin haberi.",
      segments=[seg("يَرُدُّ","radda","verb"), seg("هُ","pron-3ms","pron")]),
  tok("إِلَيْهِ","ila","part",[L, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — إِلَى صَاحِبِهِ.", "«to it» — to its owner.", "«ona» — sahibine.",
      segments=[seg("إِلَيْ","ila","part"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s11 — murattab: 28:73
S.append({"id": "s11", "translation": {
 "en": "The detailed is of two kinds: ORDERED, such as: «Of His mercy He made for you the NIGHT and the DAY, that you may REST in it and SEEK of His bounty» (28:73)." + R_EN,
 "tr": "Tafsîlî iki kısımdır: MÜRETTEB — «Rahmetinden size GECEYİ ve GÜNDÜZÜ yarattı ki onda DİNLENESİNİZ ve lütfundan ARAYASINIZ» (Kasas 28:73) gibi." + R_TR},
 "badi": [{"kind": "laff-nashr", "first": [8, 9], "second": [10, 11], "sub": "murattab"}, bd("tibaq", [8, 9], sub="ijab", cls="ism")],
 "tokens": [
  tok("فَالْأَوَّلُ","awwal","noun",[L, "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْأَوَّلُ مُبْتَدَأٌ — الْمَذْكُورُ عَلَى التَّفْصِيلِ.", "«the first» — the detailed kind.", "«birincisi» — tafsîlî olan.",
      segments=[seg("فَ","fa","conj"), seg("الْأَوَّلُ","awwal","noun")]),
  tok("ضَرْبَانِ","darb","noun",[L, "mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two kinds».", "«iki kısım».", punct=":"),
  tok("مُرَتَّبٌ","murattab","noun",[L, "badal", "ism-maful", "form-ii-verbs"], "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ — اسْمُ مَفْعُولِ رَتَّبَ: النَّشْرُ عَلَى تَرْتِيبِ اللَّفِّ.", "«ordered» — the spreading in the order of the folding.", "«mürettep» — neşir leffin sırası üzere.", punct="،"),
  nahwa(tag=L),
  wa_conj("وَمِنْ","min","part",[L, "atf-nasaq", "huruf-jarr"], "مِنْ حَرْفُ جَرٍّ — لِلسَّبَبِيَّةِ.", "«and of» — the min of cause.", "«ve … -den» — sebep mini."),
  tok("رَحْمَتِهِ","rahma","noun",[L, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«His mercy».", "«rahmetinden».",
      segments=[seg("رَحْمَتِ","rahma","noun"), seg("هِ","pron-3ms","pron")]),
  tok("جَعَلَ","jaala","verb",[L, "fail", "mafulayn"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ.", "«He made».", "«yarattı»."),
  tok("لَكُمُ","lahu","part",[L, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ، وَالْمِيمُ مَضْمُومَةٌ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«for you».", "«size».",
      segments=[seg("لَ","li","part"), seg("كُمُ","pron-2mp","pron")]),
  tok("اللَّيْلَ","layl","noun",[L, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْأَوَّلُ مِنَ اللَّفِّ.", "«the night» — the first of the fold.", "«geceyi» — leffin birincisi."),
  wa_conj("وَالنَّهَارَ","nahar","noun",[L, "atf-nasaq"], "النَّهَارَ مَعْطُوفٌ مَنْصُوبٌ — الثَّانِي مِنَ اللَّفِّ؛ طِبَاقٌ مَعَ اللَّيْلِ.", "«and the day» — the second of the fold; a tibaq with «night».", "«ve gündüzü» — leffin ikincisi; «gece» ile tıbâk."),
  tok("لِتَسْكُنُوا","sakana","verb",[L, "lam-taleel", "afal-khamsa", "fail"], "اللَّامُ لِلتَّعْلِيلِ، وَتَسْكُنُوا مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — الْأَوَّلُ مِنَ النَّشْرِ: لِلَّيْلِ.", "«that you may rest» — the first of the spread: for the night.", "«dinlenesiniz diye» — neşrin birincisi: gece için.",
      segments=[seg("لِ","li","part"), seg("تَسْكُنُ","sakana","verb"), seg("وا","pron-2mp","pron")]),
  tok("فِيهِ","fi","part",[L, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — فِي اللَّيْلِ.", "«in it» — in the night.", "«onda» — gecede.",
      segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  wa_conj("وَلِتَبْتَغُوا","ibtagha","verb",[L, "atf-nasaq", "lam-taleel", "afal-khamsa", "form-viii-verbs", "naqis-verbs", "fail"], "اللَّامُ لِلتَّعْلِيلِ، وَتَبْتَغُوا مَنْصُوبٌ بِحَذْفِ النُّونِ — الثَّانِي مِنَ النَّشْرِ: لِلنَّهَارِ؛ عَلَى التَّرْتِيبِ.", "«and seek» — the second of the spread: for the day; in order.", "«ve arayasınız» — neşrin ikincisi: gündüz için; sırasıyla.", pron=("وا","pron-2mp")),
  tok("مِنْ","min","part",[L, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("فَضْلِهِ","fadl","noun",[L, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«His bounty».", "«lütfundan».",
      segments=[seg("فَضْلِ","fadl","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})
S[-1]["tokens"][12]["segments"] = [seg("وَ","wa","conj"), seg("لِ","li","part"), seg("تَبْتَغُ","ibtagha","verb"), seg("وا","pron-2mp","pron")]
S[-1]["badi"] = [{"kind": "laff-nashr", "first": [8, 9], "second": [10, 12], "sub": "murattab"}, bd("tibaq", [8, 9], sub="ijab", cls="ism")]

# ----------- s12 — ghayr murattab: Ibn Hayyus
S.append({"id": "s12", "translation": {
 "en": "And UNORDERED, as Ibn Hayyus says: «How could I forget, when you are a DUNE, a BOUGH and a GAZELLE — in GLANCE, in FIGURE and in HAUNCH»." + R_EN,
 "tr": "Ve GAYR-İ MÜRETTEB — İbn Hayyûs'un dediği gibi: «Nasıl unutayım; sen KUM TEPESİ, DAL ve CEYLANSIN — BAKIŞTA, BOYDA ve KALÇADA»." + R_TR},
 "badi": [{"kind": "laff-nashr", "first": [6, 7, 8], "second": [11, 10, 9], "sub": "ghayr-murattab"}],
 "tokens": [
  wa_conj("وَغَيْرُ","ghayr","noun",[L, "atf-nasaq", "idafa-definiteness"], "غَيْرُ مَعْطُوفٌ عَلَى مُرَتَّبٌ، مُضَافٌ.", "«and un-» — joined onto «ordered».", "«ve gayr-i» — «mürettep»e matuf."),
  tok("مُرَتَّبٍ","murattab","noun",[L, "idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ordered».", "«mürettep».", punct="،"),
  kaq(L, "كَقَوْلِ", "pron-3ms"),
  tok("ابْنِ","ibn","noun",[L, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«Ibn».", "«İbn»."),
  tok("حَيُّوسٍ","ibn-hayyus","noun",[L, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مُحَمَّدُ بْنُ سُلْطَانَ بْنِ حَيُّوسٍ، شَاعِرُ الشَّامِ.", "«Hayyus» — Muhammad b. Sultan b. Hayyus, the poet of Syria (d. 473/1081).", "«Hayyûs» — Muhammed b. Sultân b. Hayyûs, Şam şairi (ö. 473/1081).", punct=":"),
  tok("كَيْفَ","kayfa","noun",[L, "al-istifham", "hal"], "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«how» — the question-word as a hal.", "«nasıl» — istifhâm ismi, hâl."),
  tok("أَسْلُو","sala-forget","verb",[L, "fail", "naqis-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ، وَالْفَاعِلُ مُسْتَتِرٌ — أَنَا.", "«could I forget» — raf' estimated on the waw.", "«unutayım» — zamme vâv üzerinde takdîrî."),
  wa_conj("وَأَنْتِ","anti","pron",[L, "hal", "mubtada-khabar"], "الْوَاوُ حَالِيَّةٌ، وَأَنْتِ مُبْتَدَأٌ.", "«when you» — the waw of the hal; the mubtada.", "«sen … iken» — hâl vâvı; mübtedâ."),
  tok("حِقْفٌ","hiqf","noun",[L, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — الْأَوَّلُ مِنَ اللَّفِّ: كَثِيبُ الرَّمْلِ.", "«a dune» — the first of the fold.", "«kum tepesi» — leffin birincisi."),
  wa_conj("وَغُصْنٌ","ghusn","noun",[L, "atf-nasaq"], "غُصْنٌ مَعْطُوفٌ — الثَّانِي.", "«a bough» — the second.", "«dal» — ikincisi.", punct="*"),
  wa_conj("وَغَزَالٌ","ghazal","noun",[L, "atf-nasaq"], "غَزَالٌ مَعْطُوفٌ — الثَّالِثُ.", "«a gazelle» — the third.", "«ceylan» — üçüncüsü."),
  tok("لَحْظًا","lahz","noun",[L, "tamyiz", "masdar"], "تَمْيِيزٌ مَنْصُوبٌ — لِلْغَزَالِ: الثَّالِثِ.", "«in glance» — a tamyiz; for the gazelle, the third.", "«bakışta» — temyiz; ceylan için, üçüncü."),
  wa_conj("وَقَدًّا","qadd","noun",[L, "atf-nasaq", "tamyiz"], "قَدًّا مَعْطُوفٌ — لِلْغُصْنِ: الثَّانِي.", "«in figure» — for the bough, the second.", "«boyda» — dal için, ikinci."),
  wa_conj("وَرِدْفًا","ridf","noun",[L, "atf-nasaq", "tamyiz"], "رِدْفًا مَعْطُوفٌ — لِلْحِقْفِ: الْأَوَّلِ؛ فَالنَّشْرُ عَلَى خِلَافِ تَرْتِيبِ اللَّفِّ.", "«in haunch» — for the dune, the first: the spread runs against the fold's order.", "«kalçada» — kum tepesi için, birinci: neşir leffin sırasına aykırı.", punct=".")]})
S[-1]["badi"] = [{"kind": "laff-nashr", "first": [8, 9, 10], "second": [13, 12, 11], "sub": "ghayr-murattab"}]

# ----------- s13 — ijmali: 2:111
S.append({"id": "s13", "translation": {
 "en": "And the summed, such as: «They said: none shall enter the Garden but one who is a JEW or a CHRISTIAN» (2:111) — the Jews said «none but the Jews», the Christians «none but the Christians»; the two were folded into one «they said», since no confusion follows." + R_EN,
 "tr": "İcmâlî olan — «Dediler: cennete YAHUDİ yahut HRİSTİYAN olandan başkası girmeyecek» (Bakara 2:111) gibi — Yahudiler «Yahudilerden başkası», Hristiyanlar «Hristiyanlardan başkası» dedi; karışıklık doğmayacağı için ikisi tek «dediler»de dürüldü." + R_TR},
 "badi": [{"kind": "laff-nashr", "first": [3], "second": [10, 12], "sub": "ijmali"}],
 "tokens": [
  wa_conj("وَالثَّانِي","thani","noun",[L, "atf-nasaq", "mubtada-khabar", "ism-maqsur-manqus"], "الثَّانِي مُبْتَدَأٌ — الْمَذْكُورُ عَلَى الْإِجْمَالِ.", "«and the second» — the summed kind.", "«ve ikincisi» — icmâlî olan.", punct="،"),
  nahwa(tag=L),
  wa_conj("وَقَالُوا","qala","verb",[L, "atf-nasaq", "fail", "hollow-verbs"], "قَالُوا فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ — اللَّفُّ عَلَى الْإِجْمَالِ: الْيَهُودُ وَالنَّصَارَى مَعًا.", "«and they said» — the fold in sum: the Jews and the Christians together.", "«ve dediler» — icmâlî leff: Yahudiler ve Hristiyanlar birlikte.", pron=("وا","pron-3mp")),
  tok("لَنْ","lan","part",[L, "adawat-al-tasawwur"], "حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ.", "«never».", "«asla … -meyecek»."),
  tok("يَدْخُلَ","dakhala","verb",[L, "fail", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ.", "«shall enter».", "«girecek»."),
  tok("الْجَنَّةَ","janna","noun",[L, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the Garden».", "«cennete»."),
  tok("إِلَّا","illa","part",[L, "istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«but».", "«… -den başkası»."),
  tok("مَنْ","man-mawsula","pron",[L, "ism-mawsul", "fail", "istithna-mufarragh"], "اسْمٌ مَوْصُولٌ فَاعِلُ يَدْخُلَ.", "«one who» — the doer of «enter».", "«… olan» — «girecek»in fâili."),
  tok("كَانَ","kana","verb",[L, "ism-mawsul", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ؛ صِلَةٌ.", "«is».", "«olan»."),
  tok("هُودًا","hud","noun",[L, "kana-wa-akhawatuha", "jam-taksir"], "خَبَرُ كَانَ مَنْصُوبٌ — جَمْعُ هَائِدٍ: الْيَهُودُ؛ الْأَوَّلُ مِنَ النَّشْرِ.", "«a Jew» — plural of هَائِد; the first of the spread.", "«Yahudi» — هَائِد'in çoğulu; neşrin birincisi."),
  tok("أَوْ","aw","conj",[L, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("نَصَارَى","nasara-christians","noun",[L, "atf-nasaq", "jam-taksir", "mamnu-min-sarf"], "مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — الثَّانِي مِنَ النَّشْرِ.", "«a Christian» — the second of the spread.", "«Hristiyan» — neşrin ikincisi.", punct="."),
  tok("أَيْ","ay","part",[L], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  tok("قَالَتِ","qala","verb",[L, "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«said».", "«dedi».",
      segments=[seg("قَالَ","qala","verb"), seg("تِ","ta-tanith","part")]),
  tok("الْيَهُودُ","yahud","noun",[L, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the Jews».", "«Yahudiler»."),
  tok("لَنْ","lan","part",[L, "adawat-al-tasawwur"], "حَرْفُ نَفْيٍ وَنَصْبٍ.", "«never».", "«asla»."),
  tok("يَدْخُلَهَا","dakhala","verb",[L, "fail", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ، وَهَا مَفْعُولٌ بِهِ.", "«shall enter it».", "«ona girecek».",
      segments=[seg("يَدْخُلَ","dakhala","verb"), seg("هَا","pron-3fs","pron")]),
  tok("إِلَّا","illa","part",[L, "istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ.", "«but».", "«… -den başkası»."),
  tok("الْيَهُودُ","yahud","noun",[L, "fail", "istithna-mufarragh"], "فَاعِلٌ مَرْفُوعٌ.", "«the Jews».", "«Yahudiler».", punct="،"),
  wa_conj("وَقَالَتِ","qala","verb",[L, "atf-nasaq", "fail", "hollow-verbs"], "قَالَتِ فِعْلٌ مَاضٍ وَالتَّاءُ لِلتَّأْنِيثِ.", "«and said».", "«ve dedi».", pron=("تِ","ta-tanith")),
  tok("النَّصَارَى","nasara-christians","noun",[L, "fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the Christians».", "«Hristiyanlar»."),
  tok("لَنْ","lan","part",[L, "adawat-al-tasawwur"], "حَرْفُ نَفْيٍ وَنَصْبٍ.", "«never».", "«asla»."),
  tok("يَدْخُلَهَا","dakhala","verb",[L, "fail", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ، وَهَا مَفْعُولٌ بِهِ.", "«shall enter it».", "«ona girecek».",
      segments=[seg("يَدْخُلَ","dakhala","verb"), seg("هَا","pron-3fs","pron")]),
  tok("إِلَّا","illa","part",[L, "istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ.", "«but».", "«… -den başkası»."),
  tok("النَّصَارَى","nasara-christians","noun",[L, "fail", "istithna-mufarragh", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the Christians».", "«Hristiyanlar».", punct=".")]})
S[-1]["tokens"][19]["segments"] = [seg("وَ","wa","conj"), seg("قَالَ","qala","verb"), seg("تِ","ta-tanith","part")]
S[-1]["badi"] = [{"kind": "laff-nashr", "first": [2], "second": [9, 11], "sub": "ijmali"}]

# ---------------------------------------------------------------- glossary
def FG(*ks): return {k: find_gloss(k) for k in ks}
GLOSS_ADD = FG("afa", "ahad", "akhar", "ala", "allati", "an", "anna", "arada", "ard", "arsh", "atlaqa", "aw", "awwal", "ay", "baid", "bana", "bayna", "bi", "buhturi",
               "dakhala", "damir", "dar", "darb", "dhikr", "dima", "fadl", "fi", "ghayr", "ghayyara", "ghazal", "ghusn", "hiya", "hum", "huwa", "ibn", "idha", "iham",
               "ila", "illa", "in-shartiyya", "istawa", "jaala", "janna", "ka", "kalam", "kana", "kayfa", "kull", "la-nafiya", "laama", "lafz", "lahu", "lam", "lan",
               "layl", "ma-mawsula", "man-mawsula", "mana", "min", "mithal", "mujarrada", "murashshaha", "mutaaddid", "nahar", "nahwa", "naqd", "nasara-christians",
               "nazala", "nukta", "qala", "qarib", "qawl", "qawm", "radda", "rahma", "rahman", "rih", "sama", "samma", "saqa-water", "shabba", "shay", "thani", "thumma",
               "waqafa", "zuhayr", "wa", "fa", "li", "ta-tanith", "pron-1p", "pron-1s", "pron-2mp", "pron-3d", "pron-3fs", "pron-3mp", "pron-3ms")
GLOSS_ADD.update({
 "ruju": G("ruju", "رُجُوع", "ر ج ع", "noun", "rujuʿ — returning to the preceding speech by retracting it, for a point (masdar of رَجَعَ)", "rücû — bir nükte için önceki söze onu nakzederek dönmek (رَجَعَ'nin masdarı)", 6),
 "awd": G("awd", "عَوْد", "ع و د", "noun", "a return (masdar of عَادَ)", "dönüş (عَادَ'nin masdarı)", 3),
 "sabiq": G("sabiq", "سَابِق", "س ب ق", "noun", "preceding, earlier (ism fa'il of سَبَقَ)", "önceki (سَبَقَ'nin ism-i fâili)", 3),
 "qidam": G("qidam", "قِدَم", "ق د م", "noun", "oldness, the passing of time (masdar of قَدُمَ)", "eskilik, zamanın geçmesi (قَدُمَ'nin masdarı)", 4),
 "bala-yes": G("bala-yes", "بَلَى", None, "part", "yes indeed — the answer that undoes a negation", "evet, bilâkis — nefyi bozan cevap harfi", 3),
 "tawriya": G("tawriya", "تَوْرِيَة", "و ر ي", "noun", "tawriya — a two-sense word used for its far sense (masdar of وَرَّى, to conceal)", "tevriye — uzak mânâsı kastedilen iki mânâlı lafız (وَرَّى'nın masdarı: gizlemek)", 6),
 "jamaa-share": G("jamaa-share", "جَامَعَ", "ج م ع", "verb", "to be joined with, to accompany (Form III)", "birlikte bulunmak, eşlik etmek (III. bâb)", 4, form="III"),
 "ayd-strength": G("ayd-strength", "أَيْد", "أ ي د", "noun", "strength, power — and the plural of يَد, hands", "kuvvet, güç — ve يَد'in çoğulu, eller", 5),
 "istikhdam": G("istikhdam", "اِسْتِخْدَام", "خ د م", "noun", "istikhdam — one sense by the word, the other by its pronoun (masdar of اسْتَخْدَمَ)", "istihdâm — bir mânâ lafızla, öbürü zamiriyle (اسْتَخْدَمَ'nin masdarı)", 6),
 "muawiya-ibn-malik": G("muawiya-ibn-malik", "مُعَاوِيَة", None, "propn", "Muʿawiya b. Malik — the pre-Islamic poet called «the trainer of the wise»", "Muâviye b. Mâlik — Muavvidü'l-hukemâ diye anılan Câhiliye şairi", 6),
 "malik-name": G("malik-name", "مَالِك", "م ل ك", "propn", "Malik (a proper name)", "Mâlik (özel ad)", 3),
 "raa-pasture": G("raa-pasture", "رَعَى", "ر ع ي", "verb", "to graze, to pasture; to tend (naqis: رَعَى يَرْعَى)", "otlatmak; gözetmek (nâkıs: رَعَى يَرْعَى)", 3, form="I"),
 "ghadban": G("ghadban", "غَضْبَان", "غ ض ب", "noun", "angry (the فَعْلَان sifa)", "kızgın (فَعْلَان sıfatı)", 3, plural="غِضَاب"),
 "ghada": G("ghada", "غَضًا (الْغَضَا)", "غ ض و", "noun", "the ghada — a desert tree whose embers last long; its place; its fire", "gadâ — közü uzun süren çöl ağacı; yeri; ateşi", 6),
 "sakin": G("sakin", "سَاكِن", "س ك ن", "noun", "a dweller (ism fa'il of سَكَنَ)", "sâkin, oturan (سَكَنَ'nin ism-i fâili)", 3, plural="سَاكِنُونَ"),
 "janiha": G("janiha", "جَانِحَة", "ج ن ح", "noun", "a short rib (near the breast)", "kısa kaburga (göğse yakın)", 5, plural="جَوَانِح"),
 "dil": G("dil", "ضِلْع", "ض ل ع", "noun", "a rib", "kaburga", 3, plural="ضُلُوع"),
 "laff": G("laff", "لَفّ", "ل ف ف", "noun", "folding — the several things named first (masdar of لَفَّ)", "leff, dürme — önce anılan birden çok şey (لَفَّ'nin masdarı)", 6),
 "nashr": G("nashr", "نَشْر", "ن ش ر", "noun", "spreading — what belongs to each, named after (masdar of نَشَرَ)", "neşir, yayma — sonra anılan, her birine ait olan (نَشَرَ'nin masdarı)", 6),
 "tafsil": G("tafsil", "تَفْصِيل", "ف ص ل", "noun", "detailing, one by one (masdar of فَصَّلَ)", "tafsîl, tek tek (فَصَّلَ'nin masdarı)", 4),
 "ijmal": G("ijmal", "إِجْمَال", "ج م ل", "noun", "summing up (masdar of أَجْمَلَ)", "icmâl, toplu söyleme (أَجْمَلَ'nin masdarı)", 4),
 "tayin": G("tayin", "تَعْيِين", "ع ي ن", "noun", "specifying, assigning (masdar of عَيَّنَ)", "tayin, belirleme (عَيَّنَ'nin masdarı)", 4),
 "thiqa": G("thiqa", "ثِقَة", "و ث ق", "noun", "trust, confidence (masdar of وَثِقَ)", "güven (وَثِقَ'nin masdarı)", 4),
 "sami-hearer": G("sami-hearer", "سَامِع", "س م ع", "noun", "the hearer (ism fa'il of سَمِعَ)", "dinleyen (سَمِعَ'nin ism-i fâili)", 3),
 "murattab": G("murattab", "مُرَتَّب", "ر ت ب", "noun", "ordered (ism maf'ul of رَتَّبَ)", "mürettep, sıralı (رَتَّبَ'nin ism-i mef'ûlü)", 4),
 "sakana": G("sakana", "سَكَنَ", "س ك ن", "verb", "to rest, to be still; to dwell (سَكَنَ يَسْكُنُ)", "dinlenmek, sükûn bulmak; oturmak (سَكَنَ يَسْكُنُ)", 2, form="I"),
 "ibtagha": G("ibtagha", "اِبْتَغَى", "ب غ ي", "verb", "to seek (Form VIII, naqis)", "aramak, istemek (VIII. bâb, nâkıs)", 4, form="VIII"),
 "ibn-hayyus": G("ibn-hayyus", "ابْنُ حَيُّوسٍ", None, "propn", "Ibn Hayyus — Muhammad b. Sultan, the poet of Syria (d. 473/1081)", "İbn Hayyûs — Muhammed b. Sultân, Şam şairi (ö. 473/1081)", 6),
 "sala-forget": G("sala-forget", "سَلَا", "س ل و", "verb", "to forget, to find consolation (naqis: سَلَا يَسْلُو)", "unutmak, teselli bulmak (nâkıs: سَلَا يَسْلُو)", 4, form="I"),
 "anti": G("anti", "أَنْتِ", None, "pron", "you (feminine singular)", "sen (müennes)", 1),
 "hiqf": G("hiqf", "حِقْف", "ح ق ف", "noun", "a curved sand-dune", "kıvrık kum tepesi", 5, plural="أَحْقَاف"),
 "lahz": G("lahz", "لَحْظ", "ل ح ظ", "noun", "a glance (masdar of لَحَظَ)", "bakış (لَحَظَ'nin masdarı)", 4),
 "qadd": G("qadd", "قَدّ", "ق د د", "noun", "figure, stature", "boy, endam", 4),
 "ridf": G("ridf", "رِدْف", "ر د ف", "noun", "the haunch; one who rides behind", "kalça; terkiye binen", 5),
 "hud": G("hud", "هُود", "ه و د", "noun", "Jews (plural of هَائِد)", "Yahudiler (هَائِد'in çoğulu)", 4),
 "yahud": G("yahud", "الْيَهُود", "ه و د", "noun", "the Jews", "Yahudiler", 2),
})

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "jamaa-share", _sg.derived(_sg.B3, _sg.W3, "ُ", "جَامَع", "جَامِع", "جَامِع", "مُجَامَعَة", "مُجَامِع", "مُجَامَع", "جُومِعَ", "يُجَامَعُ"))
put_morph(mo, "raa-pasture", _sg.naqis1("fataha", "نَاقِصٌ يَائِيٌّ", "y", "رَعَ", "رْع", "a", "اِرْع", "رَعْي", "رَاعٍ (الرَّاعِي)", "مَرْعِيّ", "رُعِيَ", "يُرْعَى",
                                         note="نَاقِصٌ مِنْ بَابِ فَتَحَ: رَعَى يَرْعَى — رَعَوْا، رَعَتْ."))
put_morph(mo, "sakana", _sg.idgham(_sg.sound1("nasara", "سَكَن", "سْكُن", "اُسْكُن", "سُكُون", "سَاكِن", "مَسْكُون", "سُكِنَ", "يُسْكَنُ")))   # a nun-final lam meets the feminine plural's nun
put_morph(mo, "ibtagha", _sg.derived_naqis(_sg.B8, _sg.W8, "َ", "اِبْتَغَ", "بْتَغ", "i", "اِبْتَغ", "ابْتِغَاء", "مُبْتَغٍ (الْمُبْتَغِي)", "مُبْتَغًى", "ابْتُغِيَ", "يُبْتَغَى",
                                            note="نَاقِصٌ مِنَ الِافْتِعَالِ: ابْتَغَى يَبْتَغِي — ابْتَغَوْا، ابْتَغَتْ."))
put_morph(mo, "sala-forget", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "سَلَ", "سْل", "u", "اُسْل", "سُلُوّ", "سَالٍ (السَّالِي)", "مَسْلُوّ", "سُلِيَ", "يُسْلَى",
                                        note="نَاقِصٌ وَاوِيٌّ مِنْ بَابِ نَصَرَ: سَلَا يَسْلُو — سَلَوْا، سَلَتْ."))
for k in ("afa", "ghayyara", "waqafa", "samma", "atlaqa", "arada", "laama", "istawa", "bana", "nazala", "kana", "saqa-water", "shabba", "radda", "jaala", "qala", "dakhala"):
    if k not in mo["verbs"] and has_morph(k): mo["verbs"][k] = find_morph(k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_R = {
 "id": "ruju",
 "title": {"ar": "الرُّجُوعُ — الْعَوْدُ إِلَى الْكَلَامِ السَّابِقِ بِالنَّقْضِ لِنُكْتَةٍ", "en": "The rujuʿ — returning to what was said, to retract it, for a point", "tr": "Rücû — bir nükte için söylenene dönüp onu nakzetmek"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الرجوع: العود إلى الكلام السابق بالنقض لنكتة"],
 "question": {
  "en": ["Does the speaker TAKE BACK what he just said? «Stand by the dwellings that time has not effaced — YES IT HAS, and the winds and the rains have changed them.» That is the RUJUʿ.",
         "What is the point? A nukta — here bewilderment: the lover denies the ruin, then admits it. The retraction is the feeling.",
         "What does the engine look for? A negated claim and, after it, بَلَى (or a like particle) that undoes the negation on the same matter."],
  "tr": ["Konuşan az önce söylediğini GERİ Mİ ALIYOR? «Zamanın silmediği diyarda dur — EVET SİLDİ, rüzgârlar ve yağmurlar onları değiştirdi.» RÜCÛ budur.",
         "Nükte nedir? Burada hayret: âşık harabeyi inkâr eder, sonra kabul eder. Geri alış duygunun kendisidir.",
         "Motor neye bakar? Nefyedilmiş bir iddia ve ardında, aynı konuda nefyi bozan بَلَى (yahut benzeri harf)."]},
 "plain": {
  "en": "The rujuʿ: the speaker returns to what he has just said and retracts it, for a point — Zuhayr denies that time effaced the dwellings, then says «yes it has». The engine finds the claim and the retracting particle after it.",
  "tr": "Rücû: konuşan az önce söylediğine döner ve bir nükte için onu nakzeder — Züheyr zamanın diyarı sildiğini inkâr eder, sonra «evet sildi» der. Motor iddiayı ve ardındaki nakzeden harfi bulur."},
 "explanation": {
  "en": "The RUJUʿ (return) is الْعَوْدُ إِلَى الْكَلَامِ السَّابِقِ بِالنَّقْضِ لِنُكْتَةٍ — the RETURN to the preceding speech by RETRACTING it, for a point. Zuhayr: قِفْ بِالدِّيَارِ الَّتِي لَمْ يَعْفُهَا الْقِدَمُ * بَلَى وَغَيَّرَهَا الْأَرْوَاحُ وَالدِّيَمُ — he first says the dwellings are ones time has NOT effaced, then returns with بَلَى, «yes it has», and the winds and steady rains have changed them. The point (nukta) is the display of bewilderment: the heart refuses the ruin, the eye admits it. The retraction is not a correction of a slip; it is the figure. WHAT THE ENGINE CLAIMS: the BadiEngine reads the rujuʿ when a NEGATED clause (لَمْ / لَا / مَا …) is followed by بَلَى, or by a clause that affirms the same lemma the negation denied, inside one sentence; it reports the claim's verb and the retracting word as the pair. A بَلَى answering someone else's question is not a rujuʿ and is refused when the negation is not the speaker's own. It grades itself against the authored `ruju` frame of ch60.",
  "tr": "RÜCÛ (dönüş) الْعَوْدُ إِلَى الْكَلَامِ السَّابِقِ بِالنَّقْضِ لِنُكْتَةٍ'dir — bir nükte için önceki söze onu NAKZEDEREK DÖNMEK. Züheyr: قِفْ بِالدِّيَارِ الَّتِي لَمْ يَعْفُهَا الْقِدَمُ * بَلَى وَغَيَّرَهَا الْأَرْوَاحُ وَالدِّيَمُ — önce diyarın zamanın SİLMEDİĞİ diyar olduğunu söyler, sonra بَلَى ile döner, «evet sildi», rüzgârlar ve sürekli yağmurlar onları değiştirdi. Nükte hayretin gösterilmesidir: gönül harabeyi reddeder, göz kabul eder. Geri alış bir sürçmenin düzeltilmesi değil, sanatın kendisidir. MOTORUN İDDİASI: BadiEngine rücûyu, NEFYEDİLMİŞ bir cümlecik (لَمْ / لَا / مَا …) ardından بَلَى yahut nefyin inkâr ettiği kökü isbat eden bir cümlecik tek cümlede geldiğinde okur; iddianın fiili ile nakzeden kelimeyi çift olarak bildirir. Başkasının sorusuna cevap veren بَلَى rücû değildir; nefiy konuşanın kendisinin değilse reddedilir. Kendini 60. bâbın müellif `ruju` çerçevesine karşı sınar."},
 "examples": [
  {"ar": "قِفْ بِالدِّيَارِ الَّتِي لَمْ يَعْفُهَا الْقِدَمُ * بَلَى وَغَيَّرَهَا الْأَرْوَاحُ وَالدِّيَمُ", "en": "Zuhayr: the denial and its retraction.", "tr": "Züheyr: inkâr ve geri alınışı.", "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "الْعَوْدُ إِلَى الْكَلَامِ السَّابِقِ بِالنَّقْضِ لِنُكْتَةٍ", "en": "the definition.", "tr": "tarif.", "sourceStory": "talkhis-al-miftah", "sentence": "s1"}],
 "commonMistakes": [
  {"wrong": "«بَلَى burada bir sürçmeyi düzeltir»",
   "right": "«Sanattır: nakz, hayreti göstermek içindir — nükte budur»",
   "why": {"en": "The definition asks for a point; without one the return is a mere slip.", "tr": "Tarif nükte ister; nükte olmadan dönüş salt bir sürçmedir."}}],
 "relatedNotes": ["tibaq", "khilaf-muqtada-al-zahir", "ilm-al-badi", "tawriya"]}

NOTE_W = {
 "id": "tawriya",
 "title": {"ar": "التَّوْرِيَةُ (الْإِيهَامُ) — لَفْظٌ لَهُ مَعْنَيَانِ قَرِيبٌ وَبَعِيدٌ وَيُرَادُ الْبَعِيدُ؛ مُجَرَّدَةٌ وَمُرَشَّحَةٌ", "en": "The tawriya (iham) — a near sense shown, a far sense meant; bare and furnished", "tr": "Tevriye (îhâm) — yakın mânâ gösterilir, uzak mânâ kastedilir; mücerrede ve müreşşaha"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — التورية: أن يطلق لفظ له معنيان قريب وبعيد ويراد البعيد؛ وهي ضربان مجردة ومرشحة"],
 "question": {
  "en": ["Has the word TWO senses, and is the FAR one meant while the near one shows? اسْتَوَى (20:5): the near sense «sat firm», the far «held sway» — and the far is meant. That is the TAWRIYA, the IHAM.",
         "Is anything beside it that SUITS THE NEAR sense? بِأَيْدٍ (51:47) — «hands» is the near sense, «strength» the far; بَنَيْنَا, «We built», suits hands. That makes it FURNISHED (murashshaha). اسْتَوَى has no such neighbour: BARE (mujarrada).",
         "How is this unlike the iham al-tanasub? There the near sense is meant and the far only suits the neighbours; here the far is meant."],
  "tr": ["Kelimenin İKİ mânâsı var ve yakın görünürken UZAK mı kastediliyor? اسْتَوَى (Tâhâ 20:5): yakın «karar kıldı», uzak «istîlâ etti» — ve uzak kastedilmiş. TEVRİYE, ÎHÂM budur.",
         "Yanında YAKIN MÂNÂYA UYGUN bir şey var mı? بِأَيْدٍ (Zâriyât 51:47) — «eller» yakın, «kuvvet» uzak; بَنَيْنَا «bina ettik» ellere uyar. Bu onu MÜREŞŞAHA yapar. اسْتَوَى'nın öyle komşusu yok: MÜCERREDE.",
         "Îhâm-ı tenâsübden farkı? Orada yakın mânâ kastedilir, uzak yalnız komşulara uyar; burada uzak kastedilir."]},
 "plain": {
  "en": "A word with a near and a far sense, used for the far one: «settled on the Throne» meaning «held sway»; «We built it with hands» meaning «with strength». Bare when nothing beside it suits the near sense, furnished when something does («We built» suits hands). The engine finds the furnishing neighbour itself.",
  "tr": "Yakın ve uzak mânâlı bir kelime, uzak için kullanılır: «arşa istivâ etti» yani «istîlâ etti»; «ellerle bina ettik» yani «kuvvetle». Yanında yakına uygun bir şey yoksa mücerrede, varsa müreşşaha («bina ettik» ellere uyar). Motor iki mânâyı çerçeveden alır, terşîh eden komşuyu kendi bulur."},
 "explanation": {
  "en": "The TAWRIYA (from وَرَّى, to conceal), also called the IHAM, is أَنْ يُطْلَقَ لَفْظٌ لَهُ مَعْنَيَانِ قَرِيبٌ وَبَعِيدٌ وَيُرَادَ الْبَعِيدُ — that a word with TWO SENSES, a NEAR and a FAR, be used, and the FAR meant. It is of TWO KINDS: the BARE (مُجَرَّدَة), joined with nothing that suits the near sense — الرَّحْمَنُ عَلَى الْعَرْشِ اسْتَوَى (20:5): the near sense of اسْتَوَى is «sat firm, settled», the far is «held sway, took full possession», and the far is meant; nothing in the aya suits the near sense. And the FURNISHED (مُرَشَّحَة), joined with something that suits the near sense — وَالسَّمَاءَ بَنَيْنَاهَا بِأَيْدٍ (51:47): the near sense of أَيْد is «hands» (the plural of يَد), the far is «strength», and the far is meant; بَنَيْنَا, «We built», suits hands, and so furnishes the near sense. The tawriya is the mirror of the iham al-tanasub: there the near sense is meant and the far only suits the neighbours; here the far is meant and the near only shows. WHAT THE ENGINE CLAIMS: the BadiEngine cannot know a word's far sense from the sentence; it takes the NEAR and FAR from the authored frame and does the rest itself — it searches the sentence for a word whose stored field matches the NEAR sense (hands → build, carry, write…) and reports the tawriya as furnished with that companion lit, or bare when none is found; it grades the bare/furnished verdict against the frame's sub and the companion against the frame's companion. It grades itself against the authored `tawriya` frames of ch60.",
  "tr": "TEVRİYE (وَرَّى'dan: gizlemek), ÎHÂM da denir, أَنْ يُطْلَقَ لَفْظٌ لَهُ مَعْنَيَانِ قَرِيبٌ وَبَعِيدٌ وَيُرَادَ الْبَعِيدُ'dür — biri YAKIN biri UZAK İKİ MÂNÂSI olan bir lafzın söylenip UZAĞIN kastedilmesi. İKİ KISIMDIR: yakın mânâya uygun hiçbir şeyle birlikte gelmeyen MÜCERREDE (مُجَرَّدَة) — الرَّحْمَنُ عَلَى الْعَرْشِ اسْتَوَى (Tâhâ 20:5): اسْتَوَى'nın yakın mânâsı «karar kıldı, yerleşti», uzak mânâsı «istîlâ etti, hükmü altına aldı» ve uzak kastedilmiş; âyette yakına uygun bir şey yok. Ve yakın mânâya uygun bir şeyle birlikte gelen MÜREŞŞAHA (مُرَشَّحَة) — وَالسَّمَاءَ بَنَيْنَاهَا بِأَيْدٍ (Zâriyât 51:47): أَيْد'in yakın mânâsı «eller» (يَد'in çoğulu), uzak mânâsı «kuvvet» ve uzak kastedilmiş; بَنَيْنَا «bina ettik» ellere uyar ve yakın mânâyı terşîh eder. Tevriye îhâm-ı tenâsübün aynasıdır: orada yakın mânâ kastedilir, uzak yalnız komşulara uyar; burada uzak kastedilir, yakın yalnız görünür. MOTORUN İDDİASI: BadiEngine bir kelimenin uzak mânâsını cümleden bilemez; YAKIN ve UZAĞI müellif çerçevesinden alır, gerisini kendi yapar — cümlede yerleşik sahası YAKIN mânâyla örtüşen bir kelime arar (eller → bina etmek, taşımak, yazmak…) ve tevriyeyi o refik aydınlatılmış müreşşaha, bulunamazsa mücerrede olarak bildirir; mücerrede/müreşşaha hükmünü çerçevenin alt kısmına, refiki çerçevenin refikine karşı sınar. Kendini 60. bâbın müellif `tawriya` çerçevelerine karşı sınar."},
 "examples": [
  {"ar": "الرَّحْمَنُ عَلَى الْعَرْشِ اسْتَوَى", "en": "bare (20:5).", "tr": "mücerrede (Tâhâ 20:5).", "sourceStory": "talkhis-al-miftah", "sentence": "s5"},
  {"ar": "وَالسَّمَاءَ بَنَيْنَاهَا بِأَيْدٍ", "en": "furnished (51:47).", "tr": "müreşşaha (Zâriyât 51:47).", "sourceStory": "talkhis-al-miftah", "sentence": "s6"},
  {"ar": "أَنْ يُطْلَقَ لَفْظٌ لَهُ مَعْنَيَانِ قَرِيبٌ وَبَعِيدٌ وَيُرَادَ الْبَعِيدُ", "en": "the definition.", "tr": "tarif.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"}],
 "commonMistakes": [
  {"wrong": "«بِأَيْدٍ'de eller kastedilmiştir, çünkü bina etmek elle olur»",
   "right": "«Kuvvet kastedilmiştir; «bina ettik» yalnız yakın mânâyı terşîh eder — müreşşaha tevriye»",
   "why": {"en": "The furnishing neighbour serves the concealment: it makes the near sense plausible so the far one hides better.", "tr": "Terşîh eden komşu gizlemeye hizmet eder: yakın mânâyı mâkul kılar ki uzak daha iyi saklansın."}},
  {"wrong": "«Tevriye ile îhâm-ı tenâsüb aynı şeydir»",
   "right": "«Tevriyede uzak mânâ kastedilir; îhâm-ı tenâsübde yakın kastedilir, uzak yalnız komşulara uyar»",
   "why": {"en": "Same kind of word, opposite choice of the meant sense.", "tr": "Aynı türden kelime, kastedilen mânâda zıt seçim."}}],
 "relatedNotes": ["iham-al-tanasub", "haqiqa-majaz", "istikhdam", "kinaya", "ilm-al-badi"]}

NOTE_X = {
 "id": "istikhdam",
 "title": {"ar": "الِاسْتِخْدَامُ — مَعْنًى بِاللَّفْظِ وَالْآخَرُ بِضَمِيرِهِ، أَوْ بِضَمِيرَيْهِ", "en": "The istikhdam — one sense by the word, the other by its pronoun, or one by each of two pronouns", "tr": "İstihdâm — bir mânâ lafızla öbürü zamiriyle, yahut iki zamirinin her biriyle biri"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — الاستخدام: أن يراد بلفظ له معنيان أحدهما ثم بضميره الآخر، أو بأحد ضميريه أحدهما ثم بالآخر الآخر"],
 "question": {
  "en": ["Does a two-sense word mean ONE thing where it stands and the OTHER where its PRONOUN stands? «When the SKY comes down on a people's land we graze IT»: the sky is the rain, «it» is the herbage. That is the ISTIKHDAM, first kind.",
         "Or do TWO PRONOUNS of one word carry its two senses? «May He water the GHADA and those who dwell in IT, though they kindled IT between my ribs»: the first «it» is the place, the second the fire. Second kind.",
         "How is it not a tawriya? The tawriya means one sense and hides the other; the istikhdam uses BOTH, one at the word and one at the pronoun."],
  "tr": ["İki mânâlı bir kelime durduğu yerde BİRİNİ, ZAMİRİNİN durduğu yerde ÖBÜRÜNÜ mü kastediyor? «GÖK bir kavmin toprağına indiğinde ONU otlatırız»: gök yağmurdur, «onu» ottur. İSTİHDÂM, birinci kısım.",
         "Yahut bir kelimenin İKİ ZAMİRİ iki mânâsını mı taşıyor? «GADÂYI ve ONDA oturanları sulasın, ONU kaburgalarımın arasında tutuşturmuş olsalar da»: birinci «o» yer, ikinci ateş. İkinci kısım.",
         "Tevriyeden farkı? Tevriye bir mânâyı kasteder, öbürünü saklar; istihdâm İKİSİNİ de kullanır, biri kelimede biri zamirde."]},
 "plain": {
  "en": "A two-sense word works twice: one sense at the word, the other at its pronoun — «the sky comes down… we graze it» (rain, then herbage); or one sense at each of two pronouns — «the ghada… those in it… they kindled it» (place, then fire). The engine finds the pronouns; the senses come from the frame.",
  "tr": "İki mânâlı bir kelime iki kere çalıştırılır: bir mânâ kelimede, öbürü zamirinde — «gök iner… onu otlatırız» (yağmur, sonra ot); yahut iki zamirinin her birinde biri — «gadâ… onda oturanlar… onu tutuşturdular» (yer, sonra ateş). Motor kelimeye dönen zamirleri bulur; iki mânâ çerçeveden gelir."},
 "explanation": {
  "en": "The ISTIKHDAM (putting to service) is of TWO KINDS. FIRST: أَنْ يُرَادَ بِلَفْظٍ لَهُ مَعْنَيَانِ أَحَدُهُمَا ثُمَّ بِضَمِيرِهِ الْآخَرُ — that by a two-sense word ONE sense be meant, then by its PRONOUN the OTHER. Muʿawiya b. Malik: إِذَا نَزَلَ السَّمَاءُ بِأَرْضِ قَوْمٍ * رَعَيْنَاهُ وَإِنْ كَانُوا غِضَابًا — by «the sky» the RAIN is meant (one of the word's two figurative senses), and by its pronoun in رَعَيْنَاهُ, «we graze it», the HERBAGE the rain brings up. SECOND: أَوْ بِأَحَدِ ضَمِيرَيْهِ أَحَدُهُمَا ثُمَّ بِالْآخَرِ الْآخَرُ — that by one of the word's two pronouns one sense be meant and by the other the other. Al-Buhturi: فَسَقَى الْغَضَا وَالسَّاكِنِيهِ وَإِنْ هُمُ * شَبُّوهُ بَيْنَ جَوَانِحِي وَضُلُوعِي — the ghada is a desert tree; by the first pronoun (السَّاكِنِيهِ, «those who dwell in it») its PLACE is meant, by the second (شَبُّوهُ, «they kindled it») its FIRE. Beside the tawriya, which means one sense and conceals the other, the istikhdam USES BOTH. WHAT THE ENGINE CLAIMS: the BadiEngine finds the PRONOUNS on its own — every attached pronoun after the word that agrees with it in gender and number and has no nearer antecedent — and lights them; the two senses it takes from the authored frame («murad» at the word or first pronoun, «other» at the pronoun or second pronoun), since no surface fact decides them. It grades the pronoun set against the frame's refs and the kind (word-and-pronoun / two pronouns) against the frame's sub. It grades itself against the authored `istikhdam` frames of ch60.",
  "tr": "İSTİHDÂM (hizmete koşma) İKİ KISIMDIR. BİRİNCİ: أَنْ يُرَادَ بِلَفْظٍ لَهُ مَعْنَيَانِ أَحَدُهُمَا ثُمَّ بِضَمِيرِهِ الْآخَرُ — iki mânâlı bir lafızla BİR mânânın, sonra ZAMİRİYLE ÖBÜRÜNÜN kastedilmesi. Muâviye b. Mâlik: إِذَا نَزَلَ السَّمَاءُ بِأَرْضِ قَوْمٍ * رَعَيْنَاهُ وَإِنْ كَانُوا غِضَابًا — «gök» ile YAĞMUR kastedilmiş (kelimenin iki mecazî mânâsından biri), رَعَيْنَاهُ «onu otlatırız»daki zamiriyle yağmurun bitirdiği OT. İKİNCİ: أَوْ بِأَحَدِ ضَمِيرَيْهِ أَحَدُهُمَا ثُمَّ بِالْآخَرِ الْآخَرُ — kelimenin iki zamirinden biriyle bir mânânın, öbürüyle öbürünün kastedilmesi. Buhturî: فَسَقَى الْغَضَا وَالسَّاكِنِيهِ وَإِنْ هُمُ * شَبُّوهُ بَيْنَ جَوَانِحِي وَضُلُوعِي — gadâ bir çöl ağacıdır; birinci zamirle (السَّاكِنِيهِ «onda oturanlar») YERİ, ikinciyle (شَبُّوهُ «onu tutuşturdular») ATEŞİ kastedilmiş. Bir mânâyı kastedip öbürünü gizleyen tevriyenin yanında istihdâm İKİSİNİ DE KULLANIR. MOTORUN İDDİASI: BadiEngine ZAMİRLERİ kendi bulur — kelimeden sonra gelen, onunla cins ve sayıda uyuşan ve daha yakın merci'i olmayan her bitişik zamir — ve aydınlatır; iki mânâyı müellif çerçevesinden alır («murad» kelimede yahut birinci zamirde, «other» zamirde yahut ikinci zamirde), çünkü hiçbir yüzey olgusu bunlara karar vermez. Zamir kümesini çerçevenin refs'ine, kısmı (lafız-ve-zamir / iki zamir) çerçevenin alt kısmına karşı sınar. Kendini 60. bâbın müellif `istikhdam` çerçevelerine karşı sınar."},
 "examples": [
  {"ar": "إِذَا نَزَلَ السَّمَاءُ بِأَرْضِ قَوْمٍ * رَعَيْنَاهُ وَإِنْ كَانُوا غِضَابًا", "en": "first kind: the word and its pronoun.", "tr": "birinci kısım: lafız ve zamiri.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "فَسَقَى الْغَضَا وَالسَّاكِنِيهِ وَإِنْ هُمُ * شَبُّوهُ بَيْنَ جَوَانِحِي وَضُلُوعِي", "en": "second kind: two pronouns.", "tr": "ikinci kısım: iki zamir.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"}],
 "commonMistakes": [
  {"wrong": "«رَعَيْنَاهُ'daki zamir yağmura döner: yağmuru otlatırız»",
   "right": "«Lafzen göğe döner, mânâca ota: istihdâm — zamir öbür mânâyı taşır»",
   "why": {"en": "The pronoun's antecedent is the word; its sense is the word's other sense. That split is the figure.", "tr": "Zamirin merci'i kelimedir; mânâsı kelimenin öbür mânâsıdır. Bu ayrılık sanatın kendisidir."}}],
 "relatedNotes": ["tawriya", "iham-al-tanasub", "majaz-mursal", "ilm-al-badi"]}

NOTE_L = {
 "id": "laff-wa-nashr",
 "title": {"ar": "اللَّفُّ وَالنَّشْرُ — مُرَتَّبٌ، وَغَيْرُ مُرَتَّبٍ، وَإِجْمَالِيٌّ", "en": "The laff wa-nashr — fold and spread: ordered, unordered, summed", "tr": "Leff ü neşr — dürme ve yayma: mürettep, gayr-i mürettep, icmâlî"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — اللف والنشر: ذكر متعدد على التفصيل أو الإجمال ثم ذكر ما لكل من غير تعيين ثقة بأن السامع يرده إليه"],
 "question": {
  "en": ["Are SEVERAL things named first, and then what belongs to EACH — without saying which is whose? «He made for you the NIGHT and the DAY, that you may REST in it and SEEK of His bounty» (28:73). That is the LAFF WA-NASHR: the fold, then the spread.",
         "Does the spread keep the fold's ORDER? Night → rest, day → seek: ORDERED. Ibn Hayyus: dune, bough, gazelle — in glance, figure, haunch: the spread runs BACKWARDS, UNORDERED.",
         "Is the fold one word? «THEY said: none shall enter but a Jew or a Christian» (2:111): the Jews and the Christians are folded into one «they said», then spread. SUMMED (ijmali) — trusting the hearer to sort them."],
  "tr": ["Önce BİRDEN ÇOK şey, sonra — hangisi kiminki denmeden — HER BİRİNE ait olan mı anılıyor? «Size GECEYİ ve GÜNDÜZÜ yarattı ki onda DİNLENESİNİZ ve lütfundan ARAYASINIZ» (Kasas 28:73). LEFF Ü NEŞR budur: dürme, sonra yayma.",
         "Yayma dürmenin SIRASINI koruyor mu? Gece → dinlenme, gündüz → arama: MÜRETTEP. İbn Hayyûs: kum tepesi, dal, ceylan — bakışta, boyda, kalçada: yayma TERSİNE gider, GAYR-İ MÜRETTEP.",
         "Dürme tek kelime mi? «DEDİLER: Yahudi yahut Hristiyandan başkası girmeyecek» (Bakara 2:111): Yahudiler ve Hristiyanlar tek «dediler»de dürülmüş, sonra yayılmış. İCMÂLÎ — dinleyenin ayırt edeceğine güvenerek."]},
 "plain": {
  "en": "Several things are named, then what belongs to each, without saying which is whose — the hearer sorts them. Night and day, then rest and seek: ordered. Dune, bough, gazelle, then glance, figure, haunch: unordered. Two sects folded into one «they said»: summed. The engine matches fold to spread and reports the order.",
  "tr": "Birden çok şey anılır, sonra hangisi kiminki denmeden her birine ait olan — dinleyen ayırt eder. Gece ve gündüz, sonra dinlenme ve arama: mürettep. Kum tepesi, dal, ceylan, sonra bakış, boy, kalça: gayr-i mürettep. İki fırka tek «dediler»de dürülmüş: icmâlî. Motor dürmeyi yaymaya sahayla eşler, sırayı bildirir."},
 "explanation": {
  "en": "The LAFF WA-NASHR (folding and spreading) is ذِكْرُ مُتَعَدِّدٍ عَلَى التَّفْصِيلِ أَوِ الْإِجْمَالِ ثُمَّ ذِكْرُ مَا لِكُلٍّ مِنْ غَيْرِ تَعْيِينٍ ثِقَةً بِأَنَّ السَّامِعَ يَرُدُّهُ إِلَيْهِ — the mention of SEVERAL things, in detail or in sum, then the mention of what belongs to EACH, without specifying, trusting that the hearer will return each to its owner. The DETAILED fold is of two kinds. ORDERED (مُرَتَّب), the spread in the fold's order: وَمِنْ رَحْمَتِهِ جَعَلَ لَكُمُ اللَّيْلَ وَالنَّهَارَ لِتَسْكُنُوا فِيهِ وَلِتَبْتَغُوا مِنْ فَضْلِهِ (28:73) — night and day, then rest (for the night) and seek (for the day). UNORDERED (غَيْرُ مُرَتَّب): Ibn Hayyus, كَيْفَ أَسْلُو وَأَنْتِ حِقْفٌ وَغُصْنٌ * وَغَزَالٌ لَحْظًا وَقَدًّا وَرِدْفًا — dune, bough, gazelle; then glance (the gazelle's), figure (the bough's), haunch (the dune's): the spread runs backwards. The SUMMED fold (إِجْمَالِيّ): وَقَالُوا لَنْ يَدْخُلَ الْجَنَّةَ إِلَّا مَنْ كَانَ هُودًا أَوْ نَصَارَى (2:111) — the Jews said «none but the Jews», the Christians «none but the Christians»; the two sects are folded into one «they said» and spread in «a Jew or a Christian», since each sect's charging the other with error is known and no confusion follows. WHAT THE ENGINE CLAIMS: the BadiEngine reads the laff wa-nashr when a sentence carries a LIST of two or more coordinated words (the fold) followed by a second list of the same count (the spread), and it matches each spread member to a fold member by the stored FIELD table (night → rest/dwell, day → seek/work; gazelle → glance, bough → figure, dune → haunch) or, failing that, by position; it reports the matching and whether the surface order is kept (ordered / unordered). The summed kind has a one-word fold, so the engine takes its members from the frame and only checks the spread list. It grades itself against the authored `laff-nashr` frames of ch60.",
  "tr": "LEFF Ü NEŞR (dürme ve yayma) ذِكْرُ مُتَعَدِّدٍ عَلَى التَّفْصِيلِ أَوِ الْإِجْمَالِ ثُمَّ ذِكْرُ مَا لِكُلٍّ مِنْ غَيْرِ تَعْيِينٍ ثِقَةً بِأَنَّ السَّامِعَ يَرُدُّهُ إِلَيْهِ'dir — BİRDEN ÇOK şeyin tafsîlen yahut icmâlen anılması, sonra tayin etmeksizin HER BİRİNE ait olanın anılması; dinleyenin her birini sahibine döndüreceğine güvenerek. TAFSÎLÎ dürme iki kısımdır. MÜRETTEP (مُرَتَّب), yayma dürmenin sırasında: وَمِنْ رَحْمَتِهِ جَعَلَ لَكُمُ اللَّيْلَ وَالنَّهَارَ لِتَسْكُنُوا فِيهِ وَلِتَبْتَغُوا مِنْ فَضْلِهِ (Kasas 28:73) — gece ve gündüz, sonra dinlenme (gece için) ve arama (gündüz için). GAYR-İ MÜRETTEP (غَيْرُ مُرَتَّب): İbn Hayyûs, كَيْفَ أَسْلُو وَأَنْتِ حِقْفٌ وَغُصْنٌ * وَغَزَالٌ لَحْظًا وَقَدًّا وَرِدْفًا — kum tepesi, dal, ceylan; sonra bakış (ceylanın), boy (dalın), kalça (kum tepesinin): yayma tersine gider. İCMÂLÎ dürme (إِجْمَالِيّ): وَقَالُوا لَنْ يَدْخُلَ الْجَنَّةَ إِلَّا مَنْ كَانَ هُودًا أَوْ نَصَارَى (Bakara 2:111) — Yahudiler «Yahudilerden başkası», Hristiyanlar «Hristiyanlardan başkası» dedi; iki fırka tek «dediler»de dürülüp «Yahudi yahut Hristiyan»da yayılmıştır, çünkü her fırkanın öbürünü dalâletle suçladığı bilinir ve karışıklık doğmaz. MOTORUN İDDİASI: BadiEngine leff ü neşri, bir cümle iki yahut daha çok atıflı kelimelik bir LİSTE (dürme) ve ardından aynı sayıda ikinci bir liste (yayma) taşıdığında okur; her yayma üyesini yerleşik SAHA tablosuyla (gece → dinlenme/sükûn, gündüz → arama/çalışma; ceylan → bakış, dal → boy, kum tepesi → kalça) yahut olmazsa konumla bir dürme üyesine eşler; eşlemeyi ve yüzey sırasının korunup korunmadığını (mürettep / gayr-i mürettep) bildirir. İcmâlî kısmın dürmesi tek kelimedir; motor üyelerini çerçeveden alır, yalnız yayma listesini denetler. Kendini 60. bâbın müellif `laff-nashr` çerçevelerine karşı sınar."},
 "examples": [
  {"ar": "جَعَلَ لَكُمُ اللَّيْلَ وَالنَّهَارَ لِتَسْكُنُوا فِيهِ وَلِتَبْتَغُوا مِنْ فَضْلِهِ", "en": "ordered (28:73).", "tr": "mürettep (Kasas 28:73).", "sourceStory": "talkhis-al-miftah", "sentence": "s11"},
  {"ar": "كَيْفَ أَسْلُو وَأَنْتِ حِقْفٌ وَغُصْنٌ * وَغَزَالٌ لَحْظًا وَقَدًّا وَرِدْفًا", "en": "unordered: Ibn Hayyus.", "tr": "gayr-i mürettep: İbn Hayyûs.", "sourceStory": "talkhis-al-miftah", "sentence": "s12"},
  {"ar": "وَقَالُوا لَنْ يَدْخُلَ الْجَنَّةَ إِلَّا مَنْ كَانَ هُودًا أَوْ نَصَارَى", "en": "summed (2:111).", "tr": "icmâlî (Bakara 2:111).", "sourceStory": "talkhis-al-miftah", "sentence": "s13"}],
 "commonMistakes": [
  {"wrong": "«لَحْظًا وَقَدًّا وَرِدْفًا sırasıyla kum tepesi, dal, ceylana aittir»",
   "right": "«Tersine: bakış ceylanın, boy dalın, kalça kum tepesinin — gayr-i mürettep leff ü neşr»",
   "why": {"en": "The hearer returns each to its owner by sense, not by position; the poet trusted that.", "tr": "Dinleyen her birini konumla değil mânâyla sahibine döndürür; şair buna güvendi."}},
  {"wrong": "«2:111'de leff ü neşr yoktur, çünkü iki fırka ayrı ayrı anılmamıştır»",
   "right": "«İcmâlî leff ü neşirdir: iki fırka tek «dediler»de dürülmüş, «Yahudi yahut Hristiyan»da yayılmıştır»",
   "why": {"en": "The definition allows the fold to be in sum; the spread still returns each to its sect.", "tr": "Tarif dürmenin icmâlen olmasına izin verir; yayma yine her birini fırkasına döndürür."}}],
 "relatedNotes": ["muqabala", "muraat-al-nazir", "atf-nasaq", "tibaq", "ilm-al-badi"]}

ADD_EN = (" Chapter 60 (lines ~4060-4100, sahifa 140-141) carries the rujuʿ, the tawriya (bare and furnished), the istikhdam in its "
          "two kinds and the laff wa-nashr (ordered, unordered, summed): the ayat (s5 20:5, s6 51:47, s11 28:73, s13 2:111) and the "
          "verses of Zuhayr (s2), Muʿawiya b. Malik (s8), al-Buhturi (s9) and Ibn Hayyus (s12) are Arabic as the source prints them. "
          "s1, s3-s4, s7, s10, the heads of s5-s6, s8-s9, s11-s13 and the gloss of s13, with the frames of every example, are "
          "RESTORATIONS, not quotations: the source carries those steps only in Ottoman-Turkish paraphrase, and the Arabic restores the "
          "matn's wording in the musannif's register; each is marked «restored» in its translation. The examples carry `badi` frames "
          "(ruju pair, tawriya with near/far and the furnishing companion, istikhdam with its pronouns and the two senses, laff-nashr "
          "with the fold and the spread matched by referent).")
ADD_TR = (" Altmışıncı bâb (satır ~4060-4100, sahife 140-141) rücûyu, tevriyeyi (mücerrede ve müreşşaha), iki kısmıyla istihdâmı ve "
          "leff ü neşri (mürettep, gayr-i mürettep, icmâlî) taşır: âyetler (s5 Tâhâ 20:5, s6 Zâriyât 51:47, s11 Kasas 28:73, s13 Bakara "
          "2:111) ile Züheyr (s2), Muâviye b. Mâlik (s8), Buhturî (s9) ve İbn Hayyûs (s12) beyitleri kaynağın bastığı Arapçadır. s1, "
          "s3-s4, s7, s10, s5-s6, s8-s9, s11-s13'ün başları ve s13'ün açıklaması, her örneğin çerçeveleriyle birlikte, ALINTI DEĞİL GERİ "
          "YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın ifadesini musannifin üslûbunda geri yazar; "
          "her biri tercümesinde «geri yazılmıştır» diye işaretlidir. Örnekler `badi` çerçeveleri (rücû çifti, yakın/uzak ve terşîh eden "
          "refikiyle tevriye, zamirleri ve iki mânâsıyla istihdâm, merci'e göre eşlenmiş dürme ve yaymasıyla leff ü neşr) taşır.")
write_out(60, S, TITLE, ADD_EN, ADD_TR, "4060-4100", GLOSS_ADD, notes=(NOTE_R, NOTE_W, NOTE_X, NOTE_L),
          related=(("iham-al-tanasub", ["tawriya", "istikhdam"]), ("ilm-al-badi", ["ruju", "tawriya", "istikhdam", "laff-wa-nashr"]), ("muqabala", ["laff-wa-nashr"]), ("kinaya", ["tawriya"])))
report(60, S, GLOSS_ADD, (NOTE_R, NOTE_W, NOTE_X, NOTE_L))
