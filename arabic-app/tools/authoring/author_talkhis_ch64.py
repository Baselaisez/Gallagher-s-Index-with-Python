# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 64: the ACCEPTED MUBALAGHA (tabligh, ighraq, ghuluww; the ghuluww made acceptable by a word
that brings it near the possible, by a fine takhyil, by both, or by jest) and the MADHHAB KALAMI (an argument in the
theologians' manner). Source lines ~4200-4245 (sahifa 145-146).

  RESTORED (the source carries the step only in Turkish): s1, s2 (the definition and the three degrees), s4, s6, s8 (the
  three degrees' conditions), s10, s12, s14, s16 (the accepted kinds' headings), s18 (the kalami's definition) and the three
  bayts of al-Nabigha (s20-s22): the source paraphrases them only in Turkish; the Arabic is the received text of the bayts the
  Talkhis cites. The other examples (s3, s5, s7, s9, s11, s13, s15, s17, s19) are the source's printed Arabic.

  python3 tools/authoring/author_talkhis_ch64.py
"""
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from talkhis_common import *
import talkhis_common as _tc
import sarf_gen as _sg
if os.environ.get("DRY_PKG"):
    _tc.PKG = pathlib.Path(os.environ["DRY_PKG"]); _tc.GR = pathlib.Path(os.environ["DRY_GR"])
PKG = _tc.PKG

M = "mubalagha-maqbula"; K = "madhhab-kalami"
TITLE = {"ar": "الْمُبَالَغَةُ الْمَقْبُولَةُ، وَالْمَذْهَبُ الْكَلَامِيُّ", "en": "The accepted Mubalagha; the Madhhab Kalami", "tr": "Makbul Mübalağa; Mezheb-i Kelâmî"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
def minha(tag):
    return tok("وَمِنْهَا","min","part",[tag, "atf-nasaq", "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and among them is» — the fronted khabar.", "«ve onlardan biri» — öne alınmış haber.",
               segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")])
def wahiya(tag): 
    return tok("وَهِيَ","hiya","pron",[tag, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهِيَ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.", segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")])
def wahuwa(tag):
    return tok("وَهُوَ","huwa","pron",[tag, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it is» — the mubtada.", "«ve o» — mübtedâ.", segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")])
def an_masd(tag):
    return tok("أَنْ","an-masdariyya","part",[tag, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the masdar-making an; the clause is the khabar.", "«-mak» — masdar yapan en; cümle haberdir.")
def kaqawl(tag, punct=None):
    return tok("كَقَوْلِ","qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in the saying of» — the kaf of «for instance».", "«sözü gibi» — «meselâ» kâfı.",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")], punct=punct)
def kaqh(tag):
    return tok("كَقَوْلِهِ","qawl","noun",[tag, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«as in His saying».", "«O'nun sözü gibi».",
               segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")])
def wa_conj(full, lex, pos, tags, ar, en, tr, punct=None, pron=None):
    sg = [seg("وَ", "wa", "conj"), seg(full[1:] if pron is None else full[1:-len(pron[0])], lex, pos)]
    if pron: sg.append(seg(pron[0], pron[1], "pron"))
    return tok(full, lex, pos, tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=sg)
def fa_in(tag, cond_ar, cond_en, cond_tr, name_ar, name_en, name_tr, lex):
    # the RESTORED condition sentence: فَإِنْ كَانَ الْمُدَّعَى مُمْكِنًا … فَهُوَ تَبْلِيغٌ
    return None
def ix(sen, word, nth=1):
    n = 0
    for i, t in enumerate(sen["tokens"]):
        if t["surface"]["full"] == word:
            n += 1
            if n == nth: return i
    raise KeyError(word)

# ----------- s1 — the definition (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "Among them is the accepted MUBALAGHA: to claim, for a quality, that it reaches in strength or in weakness a degree that is IMPOSSIBLE or FAR-FETCHED." + R_EN,
 "tr": "Onlardan biri makbul MÜBALAĞADIR: bir vasıf için, şiddet yahut zaafta İMKÂNSIZ yahut UZAK görülen bir dereceye ulaştığını iddia etmek." + R_TR},
 "tokens": [
  minha(M),
  tok("الْمُبَالَغَةُ","mubalagha","noun",[M, "mubtada-khabar", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ بَالَغَ.", "«the mubalagha» — the delayed mubtada.", "«mübalağa» — sona bırakılmış mübtedâ."),
  tok("الْمَقْبُولَةُ","maqbul","noun",[M, "naat-sifa", "ism-maful"], "نَعْتٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ قَبِلَ.", "«accepted» — a na't.", "«makbul» — na't.", punct="،"),
  wahiya(M),
  an_masd(M),
  tok("يُدَّعَى","iddaa","verb",[M, "an-masdariyya", "naib-al-fail", "form-viii-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — اِدَّعَى: أَصْلُهُ اِدْتَعَى، قُلِبَتِ التَّاءُ دَالًا وَأُدْغِمَتْ.", "«it is claimed» — a passive; iddaʿa's ta turned into a dal and merged.", "«iddia edilir» — meçhul; iddeâ'nın tâsı dâla dönüp idgam edilmiş."),
  tok("لِوَصْفٍ","wasf","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for a quality».", "«bir vasıf için».", segments=[seg("لِ","li","part"), seg("وَصْفٍ","wasf","noun")]),
  tok("بُلُوغُهُ","bulugh","noun",[M, "naib-al-fail", "idafa-definiteness", "masdar"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ بَلَغَ.", "«its reaching» — the naib al-fail.", "«ulaşması» — nâib-i fâil.", segments=[seg("بُلُوغُ","bulugh","noun"), seg("هُ","pron-3ms","pron")]),
  tok("فِي","fi","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الشِّدَّةِ","shidda","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«strength».", "«şiddet»."),
  tok("أَوِ","aw","part",[M, "atf-nasaq"], "حَرْفُ عَطْفٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or» — its kasra before the wasl.", "«yahut» — vasıl kesresi."),
  tok("الضَّعْفِ","daf","noun",[M, "atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«weakness».", "«zaaf»."),
  tok("حَدًّا","hadd","noun",[M, "maful-bihi"], "مَفْعُولٌ بِهِ لِلْمَصْدَرِ مَنْصُوبٌ.", "«a degree» — the masdar's object.", "«bir dereceye» — masdarın mef'ûlü."),
  tok("مُسْتَحِيلًا","mustahil","noun",[M, "naat-sifa", "ism-fail", "form-x-verbs"], "نَعْتٌ مَنْصُوبٌ — اسْمُ فَاعِلِ اسْتَحَالَ.", "«impossible» — a na't.", "«imkânsız» — na't."),
  tok("أَوْ","aw","part",[M, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("مُسْتَبْعَدًا","mustabad","noun",[M, "atf-nasaq", "ism-maful", "form-x-verbs"], "مَعْطُوفٌ مَنْصُوبٌ — اسْمُ مَفْعُولِ اسْتَبْعَدَ.", "«far-fetched» — joined; the ism maf'ul of istabʿada.", "«uzak görülen» — ma'tûf; istebade'nin ism-i mef'ûlü.", punct=".")]})

# ----------- s2 — the three degrees (RESTORED matn)
S.append({"id": "s2", "translation": {
 "en": "It is of three kinds: TABLIGH, IGHRAQ and GHULUWW." + R_EN, "tr": "Üç kısımdır: TEBLİĞ, İĞRÂK ve GULÜV." + R_TR},
 "tokens": [
  wahiya(M),
  tok("ثَلَاثَةُ","thalatha","noun",[M, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ — الْعَدَدُ عَلَى خِلَافِ الْمَعْدُودِ فِي التَّأْنِيثِ.", "«three» — the khabar, annexed; the number's ta against its masculine counted.", "«üç» — haber, muzâf; sayı, ma'dûdun cinsine ters."),
  tok("أَقْسَامٍ","aqsam","noun",[M, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«kinds».", "«kısım».", punct=":"),
  tok("تَبْلِيغٌ","tabligh","noun",[M, "badal", "masdar"], "بَدَلٌ مِنْ ثَلَاثَةُ مَرْفُوعٌ — مَصْدَرُ بَلَّغَ: الدَّرَجَةُ الْأُولَى.", "«tabligh» — a badal; the first degree.", "«tebliğ» — bedel; ilk derece."),
  wa_conj("وَإِغْرَاقٌ","ighraq","noun",[M, "atf-nasaq", "masdar"], "إِغْرَاقٌ مَعْطُوفٌ مَرْفُوعٌ — مَصْدَرُ أَغْرَقَ: الدَّرَجَةُ الثَّانِيَةُ.", "«and ighraq» — the second degree.", "«ve iğrâk» — ikinci derece."),
  wa_conj("وَغُلُوٌّ","ghuluww","noun",[M, "atf-nasaq", "masdar"], "غُلُوٌّ مَعْطُوفٌ مَرْفُوعٌ — مَصْدَرُ غَلَا: الدَّرَجَةُ الثَّالِثَةُ.", "«and ghuluww» — the third degree.", "«ve gulüv» — üçüncü derece.", punct=".")]})

# ----------- s3 — Imru' al-Qays: tabligh (possible in reason and in custom)
S.append({"id": "s3", "translation": {
 "en": "The TABLIGH — when the claim is possible both in reason and in custom — as Imru' al-Qays says: «It ran down, in one course, a bull and a doe, • caught in a row, and did not break into sweat to be washed»." + R_EN,
 "tr": "TEBLİĞ — iddia hem aklen hem âdeten mümkünse — İmruülkays'ın dediği gibi: «Bir yaban boğasıyla bir yaban ineğini tek koşuda • ardarda avladı da yıkanacak kadar terlemedi»." + R_TR},
 "tokens": [
  tok("فَالتَّبْلِيغُ","tabligh","noun",[M, "mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَالتَّبْلِيغُ مُبْتَدَأٌ مَرْفُوعٌ، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«the tabligh» — the mubtada; its khabar the phrase after.", "«tebliğ» — mübtedâ; haberi sonraki câr-mecrûr.",
      segments=[seg("فَ","fa","conj"), seg("التَّبْلِيغُ","tabligh","noun")]),
  kaqawl(M),
  tok("امْرِئِ","imru","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ — تَتْبَعُ هَمْزَتُهُ حَرَكَةَ آخِرِهِ.", "«Imru'» — its hamza follows the case vowel.", "«İmru» — hemzesi son harekeye uyar."),
  tok("الْقَيْسِ","qays","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Qays».", "«'l-Kays».", punct=":"),
  tok("فَعَادَى","ada-hunt","verb",[M, "form-iii-verbs", "naqis-verbs"], "الْفَاءُ عَاطِفَةٌ، وَعَادَى فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: الْفَرَسُ — عَادَى بَيْنَ الصَّيْدَيْنِ: وَالَى بَيْنَهُمَا فِي طَلَقٍ وَاحِدٍ.", "«it ran down» — the doer concealed: the horse; ʿada bayna: to take two prey in one course.", "«avladı» — fâil gizli: at; âdâ beyne: iki avı tek koşuda almak.",
      segments=[seg("فَ","fa","conj"), seg("عَادَى","ada-hunt","verb")]),
  tok("عِدَاءً","ida","noun",[M, "maful-mutlaq", "masdar"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — مَصْدَرُ عَادَى عَلَى فِعَالٍ.", "«in one course» — the maf'ul mutlaq; the masdar on fiʿal.", "«tek koşuda» — mef'ûl-i mutlak; fiâl vezninde masdar."),
  tok("بَيْنَ","bayna","noun",[M, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ.", "«between».", "«arasında»."),
  tok("ثَوْرٍ","thawr","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — ثَوْرُ الْوَحْشِ.", "«a bull» — the wild bull.", "«bir boğa» — yaban boğası."),
  wa_conj("وَنَعْجَةٍ","naja","noun",[M, "atf-nasaq"], "نَعْجَةٍ مَعْطُوفٌ مَجْرُورٌ — نَعْجَةُ الْوَحْشِ: الْبَقَرَةُ.", "«and a doe» — the wild cow.", "«ve bir inek» — yaban ineği.", punct="*"),
  tok("دِرَاكًا","dirak","noun",[M, "hal", "masdar"], "حَالٌ مَنْصُوبٌ — مَصْدَرٌ بِمَعْنَى مُتَدَارِكَيْنِ: مُتَتَابِعَيْنِ.", "«caught in a row» — a hal; a masdar for «one after the other».", "«ardarda» — hâl; «birbiri ardınca» mânâsında masdar."),
  tok("فَلَمْ","lam","part",[M, "lam-jazim"], "الْفَاءُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and did not».", "«ve …-medi».", segments=[seg("فَ","fa","conj"), seg("لَمْ","lam","part")]),
  tok("يَنْضَحْ","nadaha","verb",[M, "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ: الْفَرَسُ — نَضَحَ: عَرِقَ.", "«break into sweat» — jussive by lam; nadaha: to sweat.", "«terlemedi» — lem ile meczûm; nadaha: terlemek."),
  tok("بِمَاءٍ","ma-water","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — أَيْ بِعَرَقٍ.", "«with water» — with sweat.", "«su ile» — terle.", segments=[seg("بِ","bi","part"), seg("مَاءٍ","ma-water","noun")]),
  tok("فَيُغْسَلِ","ghasala","verb",[M, "atf-nasaq", "naib-al-fail", "lam-jazim"], "الْفَاءُ عَاطِفَةٌ، وَيُغْسَلِ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَعْطُوفٌ عَلَى الْمَجْزُومِ، حُرِّكَ بِالْكَسْرِ لِلْقَافِيَةِ.", "«to be washed» — a passive joined to the jussive; the rhyme gives it a kasra.", "«yıkansın» — meczûma ma'tûf meçhul; kâfiye kesre verir.",
      segments=[seg("فَ","fa","conj"), seg("يُغْسَلِ","ghasala","verb")], punct=".")]})
S[-1]["badi"] = [{"kind": "mubalagha", "sub": "tabligh", "receipt": "none", "word": ix(S[-1], "يَنْضَحْ")}]

# ----------- s4 — ighraq's condition (RESTORED matn)
S.append({"id": "s4", "translation": {
 "en": "The IGHRAQ — when the claim is possible in reason but not in custom." + R_EN, "tr": "İĞRÂK — iddia aklen mümkün, âdeten değilse." + R_TR},
 "tokens": [
  wa_conj("وَالْإِغْرَاقُ","ighraq","noun",[M, "atf-nasaq", "mubtada-khabar"], "الْإِغْرَاقُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the ighraq» — the mubtada.", "«ve iğrâk» — mübtedâ."),
  tok("مَا","ma-mawsula","pron",[M, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«what» — the khabar.", "«…-dır» — haber."),
  tok("أَمْكَنَ","amkana","verb",[M, "ism-mawsul", "form-iv-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ، وَالْفَاعِلُ مُسْتَتِرٌ: الْمُدَّعَى.", "«is possible» — the sila.", "«mümkündür» — sıla."),
  tok("عَقْلًا","aql","noun",[M, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in reason» — a tamyiz.", "«aklen» — temyiz."),
  tok("لَا","la-nafiya","part",[M, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلنَّفْيِ.", "«not».", "«…değil»."),
  tok("عَادَةً","ada","noun",[M, "atf-nasaq", "tamyiz"], "مَعْطُوفٌ مَنْصُوبٌ.", "«in custom».", "«âdeten».", punct=".")]})

# ----------- s5 — ʿAmr b. al-Ayham: ighraq
S.append({"id": "s5", "translation": {
 "en": "As ʿAmr b. al-Ayham al-Taghlibi says: «We honour our neighbour while he is among us • and we make our honouring FOLLOW HIM wherever he turns» — possible in reason, not in custom." + R_EN,
 "tr": "Amr b. Eyhem et-Tağlibî'nin dediği gibi: «Aramızda olduğu sürece komşumuza ikram ederiz • ve ikramımızı nereye giderse ARDINCA GÖNDERİRİZ» — aklen mümkün, âdeten değil." + R_TR},
 "tokens": [
  kaqawl(M),
  tok("عَمْرِو","amr-alam","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — وَاوُ عَمْرٍو فَارِقَةٌ لَا تُنْطَقُ.", "«ʿAmr» — its silent waw tells it from ʿUmar.", "«Amr» — okunmayan vâvı Ömer'den ayırır."),
  tok("بْنِ","ibn","noun",[M, "naat-sifa", "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ مُضَافٌ.", "«son of».", "«oğlu»."),
  tok("الْأَيْهَمِ","ayham","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Ayham».", "«Eyhem»."),
  tok("التَّغْلِبِيِّ","taghlibi","noun",[M, "naat-sifa", "ism-mansub"], "نَعْتٌ مَجْرُورٌ — نِسْبَةٌ إِلَى تَغْلِبَ.", "«al-Taghlibi» — the nisba to Taghlib.", "«et-Tağlibî» — Tağlib'e nisbet.", punct=":"),
  wa_conj("وَنُكْرِمُ","akrama","verb",[M, "mudari-marfu", "form-iv-verbs"], "نُكْرِمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«we honour».", "«ikram ederiz»."),
  tok("جَارَنَا","jar","noun",[M, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our neighbour» — the object.", "«komşumuza» — mef'ûl.", segments=[seg("جَارَ","jar","noun"), seg("نَا","pron-1p","pron")]),
  tok("مَا","ma-mawsula","part",[M, "anwa-ma", "maful-fih"], "مَا مَصْدَرِيَّةٌ ظَرْفِيَّةٌ.", "«as long as».", "«…-dıkça»."),
  tok("دَامَ","dama","verb",[M, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«he remains» — dama; its ism concealed.", "«olduğu sürece» — dâme; ismi gizli."),
  tok("فِينَا","fi","part",[M, "huruf-jarr", "kana-wa-akhawatuha"], "جَارٌّ وَمَجْرُورٌ خَبَرُ دَامَ.", "«among us» — dama's khabar.", "«aramızda» — dâme'nin haberi.", segments=[seg("فِي","fi","part"), seg("نَا","pron-1p","pron")], punct="*"),
  wa_conj("وَنُتْبِعُهُ","atbaa","verb",[M, "mudari-marfu", "form-iv-verbs", "mafulayn"], "نُتْبِعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ يَنْصِبُ مَفْعُولَيْنِ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ.", "«and we make follow him» — a two-object verb; the pronoun its first object.", "«ve ardınca göndeririz» — iki mef'ûl alan fiil; zamir ilk mef'ûl.", pron=("هُ","pron-3ms")),
  tok("الْكَرَامَةَ","karama","noun",[M, "maful-bihi"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«the honouring» — the second object.", "«ikramı» — ikinci mef'ûl."),
  tok("حَيْثُ","haythu","noun",[M, "maful-fih"], "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«wherever» — a zarf built on the damma.", "«nereye» — damme üzere mebnî zarf."),
  tok("مَالَا","mala","verb",[M, "hollow-verbs", "idafa-definiteness"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — مَالَ: اِنْتَقَلَ؛ وَالْأَلِفُ لِلْإِطْلَاقِ.", "«he turns» — mala: to move away; the alif is the rhyme's.", "«giderse» — mâle: yönelmek; elif ıtlâk elifi.", punct=".")]})
S[-1]["badi"] = [{"kind": "mubalagha", "sub": "ighraq", "receipt": "none", "word": ix(S[-1], "وَنُتْبِعُهُ")}]

# ----------- s6 — ghuluww's condition (RESTORED matn)
S.append({"id": "s6", "translation": {
 "en": "The GHULUWW — when the claim is possible neither in reason nor in custom. The first two kinds are accepted." + R_EN,
 "tr": "GULÜV — iddia ne aklen ne âdeten mümkünse. İlk iki kısım makbuldür." + R_TR},
 "tokens": [
  wa_conj("وَالْغُلُوُّ","ghuluww","noun",[M, "atf-nasaq", "mubtada-khabar"], "الْغُلُوُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the ghuluww» — the mubtada.", "«ve gulüv» — mübtedâ."),
  tok("مَا","ma-mawsula","pron",[M, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«what» — the khabar.", "«…-dır» — haber."),
  tok("لَا","la-nafiya","part",[M, "anwa-ma"], "نَافِيَةٌ.", "«not».", "«…-mez»."),
  tok("يُمْكِنُ","amkana","verb",[M, "ism-mawsul", "mudari-marfu", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«is possible» — the sila.", "«mümkün olmaz» — sıla."),
  tok("عَقْلًا","aql","noun",[M, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in reason».", "«aklen»."),
  wa_conj("وَلَا","la-nafiya","part",[M, "atf-nasaq"], "لَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor».", "«ne de»."),
  tok("عَادَةً","ada","noun",[M, "atf-nasaq", "tamyiz"], "مَعْطُوفٌ مَنْصُوبٌ.", "«in custom».", "«âdeten».", punct="."),
  wa_conj("وَالْأَوَّلَانِ","awwal","noun",[M, "mubtada-khabar", "al-muthanna"], "الْأَوَّلَانِ مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى.", "«and the first two» — the mubtada, a dual.", "«ve ilk ikisi» — mübtedâ, tesniye."),
  tok("مَقْبُولَانِ","maqbul","noun",[M, "mubtada-khabar", "al-muthanna", "ism-maful"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«accepted» — the khabar.", "«makbuldür» — haber.", punct=".")]})

# ----------- s7 — Abu Nuwas: ghuluww (the unborn drops fear you)
S.append({"id": "s7", "translation": {
 "en": "As Abu Nuwas says: «You so terrified the people of polytheism • that EVEN THE DROPS not yet created fear you» — possible neither in reason nor in custom: the ghuluww." + R_EN,
 "tr": "Ebû Nüvâs'ın dediği gibi: «Şirk ehlini öyle korkuttun ki • HENÜZ YARATILMAMIŞ NUTFELER BİLE senden korkar» — ne aklen ne âdeten mümkün: gulüv." + R_TR},
 "tokens": [
  kaqawl(M),
  tok("أَبِي","ab","noun",[M, "idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "«Abu» — of the five nouns, its jarr the ya.", "«Ebû» — esmâ-i hamseden, cerri yâ ile."),
  tok("نُوَاسٍ","nuwas","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو نُوَاسٍ الْحَسَنُ بْنُ هَانِئٍ.", "«Nuwas» — al-Hasan b. Hani'.", "«Nüvâs» — Hasan b. Hâni'.", punct=":"),
  tok("أَخَفْتَ","akhafa","verb",[M, "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — أَخَافَ: أَجْوَفُ عَلَى أَفْعَلَ، أَخَفْتُ بِحَذْفِ الْأَلِفِ لِلسَّاكِنِ.", "«you terrified» — a hollow Form IV; the alif dropped before the ta.", "«korkuttun» — ecvef IV. bâb; elif tâdan önce düşmüş."),
  tok("أَهْلَ","ahl","noun",[M, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ مُضَافٌ.", "«the people».", "«ehlini»."),
  tok("الشِّرْكِ","shirk","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of polytheism».", "«şirkin»."),
  tok("حَتَّى","hatta","part",[M, "huruf-jarr"], "حَرْفُ ابْتِدَاءٍ — تَدْخُلُ عَلَى الْجُمْلَةِ: غَايَةُ الْمُبَالَغَةِ.", "«so that even» — hatta opening a clause: the reach of the hyperbole.", "«hattâ» — cümle açan hattâ: mübalağanın ucu."),
  tok("إِنَّهُ","inna","part",[M, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ اسْمُهَا.", "«indeed» — inna with the pronoun of the matter as its ism.", "«muhakkak» — şân zamiri ismi olan inne.", segments=[seg("إِنَّ","inna","part"), seg("هُ","pron-3ms","pron")], punct="*"),
  tok("لَتَخَافُكَ","khafa","verb",[M, "mudari-marfu", "hollow-verbs", "maful-bihi"], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَتَخَافُ مُضَارِعٌ مَرْفُوعٌ، وَالْكَافُ مَفْعُولٌ بِهِ — الْجُمْلَةُ خَبَرُ إِنَّ.", "«fear you» — the slid lam of ibtida', then the marfuʿ verb with its object; the clause is inna's khabar.", "«senden korkar» — kaydırılmış ibtidâ lâmı, merfû fiil ve mef'ûlü; cümle inne'nin haberi.",
      segments=[seg("لَ","lam-ibtida","part"), seg("تَخَافُ","khafa","verb"), seg("كَ","pron-2ms","pron")]),
  tok("النُّطَفُ","nutfa","noun",[M, "fail", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ نُطْفَةٍ.", "«the drops» — the doer; the plural of nutfa.", "«nutfeler» — fâil; nutfe'nin çoğulu."),
  tok("الَّتِي","allati","pron",[M, "ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ نَعْتٌ.", "«which» — a relative as na't.", "«…-mış olan» — na't olan ism-i mevsûl."),
  tok("لَمْ","lam","part",[M, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«…-mamış»."),
  tok("تُخْلَقِ","khalaqa","verb",[M, "lam-jazim", "naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ، حُرِّكَ بِالْكَسْرِ لِلْقَافِيَةِ — صِلَةٌ.", "«have been created» — a passive jussive; the rhyme gives it a kasra.", "«yaratılmamış» — meçhul meczûm; kâfiye kesre verir.", punct=".")]})
S[-1]["badi"] = [{"kind": "mubalagha", "sub": "ghuluww", "receipt": "hatta", "word": ix(S[-1], "حَتَّى")}]

# ----------- s8 — accepted ghuluww, first kind (RESTORED matn)
S.append({"id": "s8", "translation": {
 "en": "Some ghuluww is accepted: what a word enters that brings it NEAR to the possible." + R_EN,
 "tr": "Gulüvün makbul olanı da vardır: kendisine, onu mümküne YAKLAŞTIRAN bir kelime girmiş olan." + R_TR},
 "tokens": [
  wa_conj("وَمِنَ","min","part",[M, "huruf-jarr", "mubtada-khabar"], "مِنَ جَارٌّ، حُرِّكَتْ نُونُهُ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — خَبَرٌ مُقَدَّمٌ.", "«and of» — the fronted khabar; min's nun takes a fatha before the wasl.", "«ve …-den» — öne alınmış haber; nûn vasıldan önce fetha alır."),
  tok("الْغُلُوِّ","ghuluww","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«the ghuluww».", "«gulüvden»."),
  tok("مَقْبُولٌ","maqbul","noun",[M, "mubtada-khabar", "ism-maful"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«an accepted kind» — the delayed mubtada.", "«makbul olanı» — sona bırakılmış mübtedâ.", punct=":"),
  tok("مَا","ma-mawsula","pron",[M, "ism-mawsul", "badal"], "اسْمٌ مَوْصُولٌ بَدَلٌ.", "«what» — a badal.", "«…-an» — bedel."),
  tok("دَخَلَهُ","dakhala","verb",[M, "ism-mawsul", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«enters it» — the sila; the pronoun its object.", "«girmiş» — sıla; zamir mef'ûl.", segments=[seg("دَخَلَ","dakhala","verb"), seg("هُ","pron-3ms","pron")]),
  tok("مَا","ma-mawsula","pron",[M, "ism-mawsul", "fail"], "اسْمٌ مَوْصُولٌ فَاعِلٌ.", "«that which» — the doer.", "«…-an şey» — fâil."),
  tok("يُقَرِّبُهُ","qarraba","verb",[M, "ism-mawsul", "mudari-marfu", "form-ii-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«brings it near» — the sila.", "«yaklaştıran» — sıla.", segments=[seg("يُقَرِّبُ","qarraba","verb"), seg("هُ","pron-3ms","pron")]),
  tok("إِلَى","ila","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الصِّحَّةِ","sihha","noun",[M, "huruf-jarr"], "مَجْرُورٌ — أَيِ الْإِمْكَانِ.", "«soundness» — to the possible.", "«sıhhate» — mümküne.", punct=".")]})

# ----------- s9 — 24:35 يَكَادُ زَيْتُهَا يُضِيءُ
S.append({"id": "s9", "translation": {
 "en": "As He says, exalted is He: «Its oil WELL-NIGH glows, though no fire has touched it» — «its oil glows» would be ghuluww; يَكَادُ brings it near, and it is accepted." + R_EN,
 "tr": "Nitekim Allah Teâlâ buyurur: «Ona ateş dokunmasa bile yağı NEREDEYSE aydınlatır» — «yağı aydınlatır» gulüv olurdu; يَكَادُ onu yaklaştırır, makbul olur." + R_TR},
 "tokens": [
  kaqh(M), taala(M),
  tok("يَكَادُ","kada","verb",[M, "kana-wa-akhawatuha", "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَفْعَالِ الْمُقَارَبَةِ، يَرْفَعُ الِاسْمَ وَخَبَرُهُ جُمْلَةٌ فِعْلِيَّةٌ — الْكَلِمَةُ الَّتِي تُقَرِّبُ الْغُلُوَّ.", "«well-nigh» — kada, a verb of nearness: it raises its ism and its khabar is a verb clause; the word that brings the ghuluww near.", "«neredeyse» — mukarebe fiili kâde: ismini ref eder, haberi fiil cümlesidir; gulüvü yaklaştıran kelime."),
  tok("زَيْتُهَا","zayt","noun",[M, "kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ يَكَادُ مَرْفُوعٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its oil» — the ism of kada.", "«yağı» — kâde'nin ismi.", segments=[seg("زَيْتُ","zayt","noun"), seg("هَا","pron-3fs","pron")]),
  tok("يُضِيءُ","adaa","verb",[M, "kana-wa-akhawatuha", "mudari-marfu", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ يَكَادُ.", "«glows» — the clause is kada's khabar.", "«aydınlatır» — cümle kâde'nin haberi."),
  wa_conj("وَلَوْ","law","part",[M, "in-shartiyya"], "لَوْ هُنَا وَصْلِيَّةٌ: بِمَعْنَى وَإِنْ.", "«though» — the concessive law.", "«…-sa bile» — vasliye lev."),
  tok("لَمْ","lam","part",[M, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ.", "«not».", "«…-masa»."),
  tok("تَمْسَسْهُ","massa","verb",[M, "lam-jazim", "doubled-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، فُكَّ إِدْغَامُهُ لِلسُّكُونِ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«has touched it» — jussive; the doubled letters unmerged before the sukun.", "«dokunmasa» — meczûm; şedde sükûndan önce açılmış.", segments=[seg("تَمْسَسْ","massa","verb"), seg("هُ","pron-3ms","pron")]),
  tok("نَارٌ","nar","noun",[M, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a fire» — the doer.", "«bir ateş» — fâil.", punct=".")]})
S[-1]["badi"] = [{"kind": "mubalagha", "sub": "ghuluww", "receipt": "kada", "word": ix(S[-1], "يَكَادُ")}]

# ----------- s10 — accepted ghuluww, second kind (RESTORED matn)
S.append({"id": "s10", "translation": {"en": "And of it: what carries a FINE FANCY." + R_EN, "tr": "Ve ondan: GÜZEL BİR HAYAL taşıyan." + R_TR},
 "tokens": [
  wa_conj("وَمِنْهُ","min","part",[M, "huruf-jarr", "mubtada-khabar"], "مِنْهُ جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«and of it» — the fronted khabar.", "«ve ondan» — öne alınmış haber.", pron=("هُ","pron-3ms")),
  tok("مَا","ma-mawsula","pron",[M, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what».", "«…-an»."),
  tok("تَضَمَّنَ","tadammana","verb",[M, "ism-mawsul", "form-v-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«carries» — the sila.", "«içeren» — sıla."),
  tok("نَوْعًا","naw","noun",[M, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a kind».", "«bir tür»."),
  tok("حَسَنًا","hasan","noun",[M, "naat-sifa", "sifa-mushabbaha"], "نَعْتٌ مَنْصُوبٌ.", "«fine».", "«güzel»."),
  tok("مِنَ","min","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ.", "«of».", "«-den»."),
  tok("التَّخْيِيلِ","takhyil","noun",[M, "huruf-jarr", "masdar"], "مَجْرُورٌ — مَصْدَرُ خَيَّلَ.", "«fancy» — the masdar of khayyala.", "«hayalin» — hayyele'nin masdarı.", punct=".")]})

# ----------- s11 — al-Mutanabbi: the hooves knotted a dust one could walk on
S.append({"id": "s11", "translation": {
 "en": "As al-Mutanabbi says: «Their hooves knotted a dust above them; • had they sought to pace upon it, they COULD have» — a fine fancy: the ghuluww is accepted." + R_EN,
 "tr": "Mütenebbî'nin dediği gibi: «Tırnakları üstlerine bir toz düğümledi; • üstünde yürümek isteselerdi, MÜMKÜN OLURDU» — güzel bir hayal: gulüv makbuldür." + R_TR},
 "tokens": [
  kaqawl(M),
  tok("الْمُتَنَبِّي","mutanabbi","noun",[M, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«al-Mutanabbi».", "«Mütenebbî».", punct=":"),
  tok("عَقَدَتْ","aqada","verb",[M], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«knotted».", "«düğümledi»."),
  tok("سَنَابِكُهَا","sunbuk","noun",[M, "fail", "idafa-definiteness", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ سُنْبُكٍ: طَرَفُ الْحَافِرِ.", "«their hoof-tips» — the doer; the plural of sunbuk.", "«tırnak uçları» — fâil; sünbük'ün çoğulu.", segments=[seg("سَنَابِكُ","sunbuk","noun"), seg("هَا","pron-3fs","pron")]),
  tok("عَلَيْهَا","ala","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«above them».", "«üstlerine».", segments=[seg("عَلَيْ","ala","part"), seg("هَا","pron-3fs","pron")]),
  tok("عِثْيَرًا","ithyar","noun",[M, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْعِثْيَرُ: الْغُبَارُ.", "«a dust» — the object.", "«bir toz» — mef'ûl.", punct="*"),
  tok("لَوْ","law","part",[M, "in-shartiyya"], "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ — التَّخْيِيلُ يُبْنَى عَلَيْهِ.", "«had» — the law of the unreal; the fancy is built on it.", "«…-seydi» — imtinâ lev'i; hayal onun üstüne kurulur."),
  tok("تَبْتَغِي","ibtagha","verb",[M, "in-shartiyya", "mudari-marfu", "form-viii-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«they sought» — the shart's verb.", "«isteselerdi» — şart fiili."),
  tok("عَنَقًا","anaq","noun",[M, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْعَنَقُ: ضَرْبٌ مِنَ السَّيْرِ.", "«a pacing» — a gait.", "«bir yürüyüş» — bir yürüyüş tarzı."),
  tok("عَلَيْهِ","ala","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«upon it».", "«üstünde».", segments=[seg("عَلَيْ","ala","part"), seg("هِ","pron-3ms","pron")]),
  tok("لَأَمْكَنَا","amkana","verb",[M, "in-shartiyya", "form-iv-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَأَمْكَنَ فِعْلٌ مَاضٍ، وَالْأَلِفُ لِلْإِطْلَاقِ.", "«it could have» — the lam of law's answer; the alif the rhyme's.", "«mümkün olurdu» — lev'in cevap lâmı; elif ıtlâk elifi.",
      segments=[seg("لَ","lam-qasam","part"), seg("أَمْكَنَا","amkana","verb")], punct=".")]})
S[-1]["badi"] = [{"kind": "mubalagha", "sub": "ghuluww", "receipt": "law", "word": ix(S[-1], "لَوْ")}]

# ----------- s12 — both together (RESTORED matn)
S.append({"id": "s12", "translation": {"en": "At times the two — the nearing word and the fine fancy — come TOGETHER." + R_EN, "tr": "Bazen ikisi — yaklaştıran kelime ile güzel hayal — BİR ARADA gelir." + R_TR},
 "tokens": [
  wa_conj("وَقَدْ","qad","part",[M, "qad-harf"], "قَدْ لِلتَّقْلِيلِ.", "«and at times».", "«ve bazen»."),
  tok("يَجْتَمِعَانِ","ijtamaa","verb",[M, "mudari-marfu", "form-viii-verbs", "afal-khamsa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ — مِنَ الْأَفْعَالِ الْخَمْسَةِ.", "«the two come together» — one of the five verbs, marfuʿ by its nun.", "«ikisi bir araya gelir» — ef'âl-i hamseden, nûnla merfû.", punct=".")]})

# ----------- s13 — al-Arrajani: it seems to me the stars are nailed …
S.append({"id": "s13", "translation": {
 "en": "As al-Arrajani says: «IT SEEMS TO ME the stars are nailed into the dark • and my eyelids bound to them by my lashes» — a fancy, and the word يُخَيَّلُ that brings it near, together." + R_EN,
 "tr": "Errecânî'nin dediği gibi: «BANA ÖYLE GELİR Kİ yıldızlar karanlığa çivilenmiş • ve göz kapaklarım kirpiklerimle onlara bağlanmış» — hayal ile onu yaklaştıran يُخَيَّلُ, bir arada." + R_TR},
 "tokens": [
  kaqawl(M),
  tok("الْأَرَّجَانِيِّ","arrajani","noun",[M, "idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نِسْبَةٌ إِلَى أَرَّجَانَ.", "«al-Arrajani» — the nisba to Arrajan.", "«Errecânî» — Errecân'a nisbet.", punct=":"),
  tok("يُخَيَّلُ","khayyala","verb",[M, "mudari-marfu", "naib-al-fail", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ — الْكَلِمَةُ الَّتِي تُقَرِّبُ.", "«it seems» — a passive; the an-clause is its naib; the nearing word.", "«öyle gelir» — meçhul; en cümlesi nâibi; yaklaştıran kelime."),
  tok("لِي","li","part",[M, "huruf-jarr", "ya-al-mutakallim"], "جَارٌّ وَمَجْرُورٌ.", "«to me».", "«bana».", segments=[seg("لِ","li","part"), seg("ي","pron-1s","pron")]),
  tok("أَنْ","an-masdariyya","part",[M, "an-masdariyya"], "أَنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ — أَوْ مَصْدَرِيَّةٌ دَخَلَتْ عَلَى الْمَاضِي.", "«that» — the lightened anna, its ism the pronoun of the matter.", "«ki» — hafifletilmiş enne, ismi şân zamiri."),
  tok("سُمِّرَ","sammara","verb",[M, "naib-al-fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«are nailed» — a passive.", "«çivilenmiş» — meçhul."),
  tok("الشُّهْبُ","shihab","noun",[M, "naib-al-fail", "jam-taksir"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — جَمْعُ شِهَابٍ: النُّجُومُ.", "«the stars» — the naib; the plural of shihab.", "«yıldızlar» — nâib-i fâil; şihâb'ın çoğulu."),
  tok("فِي","fi","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«into».", "«-e»."),
  tok("الدُّجَى","duja","noun",[M, "huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ: الظُّلْمَةُ.", "«the dark» — a maqsur.", "«karanlığa» — maksûr.", punct="*"),
  wa_conj("وَشُدَّتْ","shadda","verb",[M, "naib-al-fail", "doubled-verbs"], "شُدَّتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and are bound» — a passive.", "«ve bağlanmış» — meçhul."),
  tok("بِأَهْدَابِي","hudb","noun",[M, "huruf-jarr", "idafa-definiteness", "ya-al-mutakallim", "jam-taksir"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ — جَمْعُ هُدْبٍ.", "«by my lashes» — the plural of hudb.", "«kirpiklerimle» — hüdb'ün çoğulu.",
      segments=[seg("بِ","bi","part"), seg("أَهْدَابِ","hudb","noun"), seg("ي","pron-1s","pron")]),
  tok("إِلَيْهِنَّ","ila","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الضَّمِيرُ لِلشُّهْبِ.", "«to them» — the stars.", "«onlara» — yıldızlara.", segments=[seg("إِلَيْ","ila","part"), seg("هِنَّ","pron-3fp","pron")]),
  tok("أَجْفَانِي","jafn","noun",[M, "naib-al-fail", "idafa-definiteness", "ya-al-mutakallim", "jam-taksir"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ — جَمْعُ جَفْنٍ.", "«my eyelids» — the naib al-fail before the speaker's ya.", "«göz kapaklarım» — mütekellim yâsından önce nâib-i fâil.",
      segments=[seg("أَجْفَانِ","jafn","noun"), seg("ي","pron-1s","pron")], punct=".")]})
S[-1]["badi"] = [{"kind": "mubalagha", "sub": "ghuluww", "receipt": "khayyal", "word": ix(S[-1], "يُخَيَّلُ")}]

# ----------- s14 — the jest (RESTORED matn)
S.append({"id": "s14", "translation": {"en": "And of it: what comes out in the manner of JEST." + R_EN, "tr": "Ve ondan: ŞAKA yollu söylenen." + R_TR},
 "tokens": [
  wa_conj("وَمِنْهُ","min","part",[M, "huruf-jarr", "mubtada-khabar"], "مِنْهُ خَبَرٌ مُقَدَّمٌ.", "«and of it».", "«ve ondan».", pron=("هُ","pron-3ms")),
  tok("مَا","ma-mawsula","pron",[M, "ism-mawsul", "mubtada-khabar"], "مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what».", "«…-en»."),
  tok("أُخْرِجَ","akhraja","verb",[M, "ism-mawsul", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ.", "«is brought out» — the sila.", "«çıkarılan» — sıla."),
  tok("مَخْرَجَ","makhraj","noun",[M, "maful-mutlaq", "idafa-definiteness"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ مُضَافٌ — مَصْدَرٌ مِيمِيٌّ.", "«in the manner» — a mimi masdar as maf'ul mutlaq.", "«tarzında» — mef'ûl-i mutlak olan mîmî masdar."),
  tok("الْهَزْلِ","hazl","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of jest».", "«şakanın».", punct=".")]})

# ----------- s15 — the jest bayt: drunk yesterday if I resolve to drink tomorrow
S.append({"id": "s15", "translation": {
 "en": "As the poet says: «I get drunk YESTERDAY if I resolve to drink TOMORROW — • that, indeed, is a wonder» — said in jest, the mubalagha is accepted." + R_EN,
 "tr": "Şairin dediği gibi: «YARIN içmeye niyet etsem DÜN sarhoş olurum — • bu, gerçekten şaşılacak şeydir» — şaka yollu söylenmiş, mübalağa makbuldür." + R_TR},
 "tokens": [
  tok("كَقَوْلِ","qawl","noun",[M, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in the saying of».", "«sözü gibi».", segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")]),
  tok("الشَّاعِرِ","shair","noun",[M, "idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the poet».", "«şairin».", punct=":"),
  tok("أَسْكَرُ","sakira","verb",[M, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — جَوَابُ الشَّرْطِ مُقَدَّمٌ فِي الْمَعْنَى.", "«I get drunk» — the answer, put first in sense.", "«sarhoş olurum» — mânâca öne alınmış cevap."),
  tok("بِالْأَمْسِ","ams","noun",[M, "huruf-jarr", "maful-fih"], "جَارٌّ وَمَجْرُورٌ — أَمْسِ مَبْنِيٌّ عَلَى الْكَسْرِ: الزَّمَنُ الْمَاضِي.", "«yesterday» — ams, built on the kasra: the past.", "«dün» — kesre üzere mebnî ems: geçmiş.", segments=[seg("بِ","bi","part"), seg("الْأَمْسِ","ams","noun")]),
  tok("إِنْ","in-shartiyya","part",[M, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«…-sem»."),
  tok("عَزَمْتُ","azama","verb",[M, "in-shartiyya"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ.", "«I resolve» — the shart's verb.", "«niyet etsem» — şart fiili."),
  tok("عَلَى","ala","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e».", punct="*"),
  tok("الشُّرْبِ","shurb","noun",[M, "huruf-jarr", "masdar"], "مَجْرُورٌ — مَصْدَرُ شَرِبَ.", "«drinking».", "«içmeye»."),
  tok("غَدًا","ghad","noun",[M, "maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ — الزَّمَنُ الْآتِي: طِبَاقٌ مَعَ الْأَمْسِ.", "«tomorrow» — the future: a tibaq with yesterday.", "«yarın» — gelecek: dün ile tıbâk."),
  tok("إِنَّ","inna","part",[M, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«indeed».", "«gerçekten»."),
  tok("ذَا","dha","pron",[M, "asma-al-ishara", "inna-wa-akhawatuha"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«that» — the ism of inna.", "«bu» — inne'nin ismi."),
  tok("مِنَ","min","part",[M, "huruf-jarr", "inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ.", "«of» — the phrase is inna's khabar.", "«-den» — câr-mecrûr inne'nin haberi."),
  tok("الْعَجَبِ","ajab","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«wonder».", "«şaşılacak şey».", punct=".")]})
S[-1]["badi"] = [{"kind": "mubalagha", "sub": "ghuluww", "receipt": "hazl", "word": ix(S[-1], "بِالْأَمْسِ")},
                 {"kind": "tibaq", "sub": "ijab", "pair": [ix(S[-1], "بِالْأَمْسِ"), ix(S[-1], "غَدًا")], "class": "ism"}]

# ----------- s16 — the madhhab kalami (RESTORED matn)
S.append({"id": "s16", "translation": {
 "en": "Among them is the MADHHAB KALAMI: to bring a proof for the claim, in the manner of the people of kalam." + R_EN,
 "tr": "Onlardan biri MEZHEB-İ KELÂMÎDİR: iddia için, kelâm ehlinin yolu üzere delil getirmek." + R_TR},
 "tokens": [
  minha(K),
  tok("الْمَذْهَبُ","madhhab","noun",[K, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the madhhab» — the delayed mubtada.", "«mezheb» — sona bırakılmış mübtedâ."),
  tok("الْكَلَامِيُّ","kalami","noun",[K, "naat-sifa", "ism-mansub"], "نَعْتٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى عِلْمِ الْكَلَامِ.", "«kalami» — a na't; the nisba to kalam.", "«kelâmî» — na't; kelâm ilmine nisbet.", punct="،"),
  wahuwa(K),
  tok("إِيرَادُ","irad","noun",[K, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ مُضَافٌ — مَصْدَرُ أَوْرَدَ.", "«the bringing» — the khabar.", "«getirmek» — haber."),
  tok("حُجَّةٍ","hujja","noun",[K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of a proof».", "«bir delil»."),
  tok("لِلْمَطْلُوبِ","matlub","noun",[K, "huruf-jarr", "ism-maful"], "جَارٌّ وَمَجْرُورٌ — اسْمُ مَفْعُولِ طَلَبَ: الدَّعْوَى.", "«for the claim» — the thing sought.", "«iddia için» — istenen şey.", segments=[seg("لِ","li","part"), seg("الْمَطْلُوبِ","matlub","noun")]),
  tok("عَلَى","ala","part",[K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«üzere»."),
  tok("طَرِيقَةِ","tariqa","noun",[K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ مُضَافٌ.", "«the manner».", "«yolu»."),
  tok("أَهْلِ","ahl","noun",[K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ مُضَافٌ.", "«of the people».", "«ehlinin»."),
  tok("الْكَلَامِ","kalam","noun",[K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عِلْمُ الْكَلَامِ: الْمَنْطِقُ فِي الْعَقَائِدِ.", "«of kalam» — the science of reasoned belief.", "«kelâmın» — akāidde mantık.", punct=".")]})

# ----------- s17 — 21:22 لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللَّهُ لَفَسَدَتَا
S.append({"id": "s17", "translation": {
 "en": "As He says, exalted is He: «HAD there been in them gods other than Allah, they would BOTH have gone to ruin» — the two have not gone to ruin, so there are no gods but He: the proof in the theologians' shape." + R_EN,
 "tr": "Nitekim Allah Teâlâ buyurur: «İkisinde Allah'tan başka ilâhlar OLSAYDI, ikisi de BOZULURDU» — ikisi bozulmadı, öyleyse O'ndan başka ilâh yoktur: kelâmcıların şeklinde delil." + R_TR},
 "tokens": [
  kaqh(K), taala(K),
  tok("لَوْ","law","part",[K, "in-shartiyya"], "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ — الْمُقَدِّمَةُ الشَّرْطِيَّةُ.", "«had» — the law of the unreal: the conditional premise.", "«…-saydı» — imtinâ lev'i: şartlı öncül."),
  tok("كَانَ","kana","verb",[K, "kana-wa-akhawatuha", "in-shartiyya", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِعْلُ الشَّرْطِ.", "«there been» — kana, the shart's verb.", "«olsaydı» — kâne, şart fiili."),
  tok("فِيهِمَا","fi","part",[K, "huruf-jarr", "kana-wa-akhawatuha"], "جَارٌّ وَمَجْرُورٌ خَبَرُ كَانَ مُقَدَّمٌ — الضَّمِيرُ لِلسَّمَاءِ وَالْأَرْضِ.", "«in them» — kana's fronted khabar: the heaven and the earth.", "«ikisinde» — kâne'nin öne alınmış haberi: gök ve yer.", segments=[seg("فِي","fi","part"), seg("هِمَا","pron-3d","pron")]),
  tok("آلِهَةٌ","ilah","noun",[K, "kana-wa-akhawatuha", "jam-taksir"], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ — جَمْعُ إِلَهٍ.", "«gods» — kana's delayed ism.", "«ilâhlar» — kâne'nin sona bırakılmış ismi."),
  tok("إِلَّا","illa","part",[K, "istithna", "naat-sifa"], "إِلَّا هُنَا بِمَعْنَى غَيْرِ: صِفَةٌ لِآلِهَةٌ.", "«other than» — illa in the sense of ghayr: a na't of «gods».", "«…-den başka» — gayr mânâsında illâ: «ilâhlar»ın sıfatı."),
  tok("اللَّهُ","allah","noun",[K, "naat-sifa"], "لَفْظُ الْجَلَالَةِ مَرْفُوعٌ تَبَعًا لِآلِهَةٌ — عَلَى أَنَّ إِلَّا صِفَةٌ.", "«Allah» — marfuʿ, following «gods», illa being a na't.", "«Allah» — «ilâhlar»a tâbi merfû; illâ sıfat olduğundan."),
  tok("لَفَسَدَتَا","fasada","verb",[K, "in-shartiyya", "al-muthanna"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَفَسَدَتَا فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْأَلِفُ فَاعِلٌ — النَّتِيجَةُ الْمُمْتَنِعَةُ.", "«they would both have gone to ruin» — the answer with its lam; the alif the dual doer: the consequence that is denied.", "«ikisi de bozulurdu» — lâmlı cevap; elif tesniye fâil: reddedilen sonuç.",
      segments=[seg("لَ","lam-qasam","part"), seg("فَسَدَتَا","fasada","verb")], punct=".")]})
S[-1]["badi"] = [{"kind": "kalami", "sub": "law", "word": ix(S[-1], "لَوْ"), "companion": ix(S[-1], "لَفَسَدَتَا")}]

# ----------- s18 — al-Nabigha, bayt 1 (RESTORED text of the cited bayt)
S.append({"id": "s18", "translation": {
 "en": "And al-Nabigha's verses (the oath): «I have SWORN, and left no doubt for your soul; • and beyond Allah a man has no recourse»." + R_EN,
 "tr": "Ve Nâbiğa'nın beyitleri (yemin): «YEMİN ETTİM, nefsine hiçbir şüphe bırakmadım; • Allah'ın ötesinde insan için sığınak yoktur»." + R_TR},
 "tokens": [
  wa_conj("وَقَوْلِ","qawl","noun",[K, "atf-nasaq", "huruf-jarr", "idafa-definiteness"], "قَوْلِ مَعْطُوفٌ عَلَى قَوْلِهِ مَجْرُورٌ مُضَافٌ.", "«and the saying of».", "«ve … sözü»."),
  tok("النَّابِغَةِ","nabigha","noun",[K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — النَّابِغَةُ الذُّبْيَانِيُّ.", "«al-Nabigha» — al-Dhubyani.", "«Nâbiğa» — ez-Zübyânî.", punct=":"),
  tok("حَلَفْتُ","halafa","verb",[K], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — الْقَسَمُ: أَصْلُ الْحُجَّةِ.", "«I have sworn» — the oath: the root of the argument.", "«yemin ettim» — yemin: delilin kökü."),
  tok("فَلَمْ","lam","part",[K, "lam-jazim"], "الْفَاءُ عَاطِفَةٌ، وَلَمْ جَازِمَةٌ.", "«and did not».", "«ve …-medim».", segments=[seg("فَ","fa","conj"), seg("لَمْ","lam","part")]),
  tok("أَتْرُكْ","taraka","verb",[K, "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«leave».", "«bırakmadım»."),
  tok("لِنَفْسِكَ","nafs","noun",[K, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«for your soul».", "«nefsine».", segments=[seg("لِ","li","part"), seg("نَفْسِ","nafs","noun"), seg("كَ","pron-2ms","pron")]),
  tok("رِيبَةً","riba-doubt","noun",[K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الرِّيبَةُ: الشَّكُّ.", "«a doubt» — the object.", "«bir şüphe» — mef'ûl.", punct="*"),
  wa_conj("وَلَيْسَ","laysa","verb",[K, "kana-wa-akhawatuha"], "لَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ.", "«and there is not» — laysa.", "«ve yoktur» — leyse."),
  tok("وَرَاءَ","wara","noun",[K, "maful-fih", "idafa-definiteness", "kana-wa-akhawatuha"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ خَبَرُ لَيْسَ مُقَدَّمٌ.", "«beyond» — a zarf, laysa's fronted khabar.", "«ötesinde» — zarf, leyse'nin öne alınmış haberi."),
  tok("اللَّهِ","allah","noun",[K, "idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Allah».", "«Allah'ın»."),
  tok("لِلْمَرْءِ","mar","noun",[K, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for a man».", "«insan için».", segments=[seg("لِ","li","part"), seg("الْمَرْءِ","mar","noun")]),
  tok("مَذْهَبُ","madhhab","noun",[K, "kana-wa-akhawatuha"], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ، سُكِّنَ لِلْقَافِيَةِ — الْمَذْهَبُ: الْمَلْجَأُ.", "«a recourse» — laysa's delayed ism; the rhyme quiets its tanwin.", "«bir sığınak» — leyse'nin sona bırakılmış ismi; kâfiye tenvinini susturur.", punct=".")]})
S[-1]["badi"] = [{"kind": "kalami", "sub": "qasam", "word": ix(S[-1], "حَلَفْتُ"), "companion": ix(S[-1], "وَلَيْسَ")}]

# ----------- s19 — al-Nabigha, bayt 2 (the conditional argument)
S.append({"id": "s19", "translation": {
 "en": "«IF a treachery of mine has been carried to you, • then the tale-bearer who carried it is the MORE deceitful and the MORE lying»." + R_EN,
 "tr": "«EĞER benden sana bir hıyanet ulaştırılmışsa, • onu ulaştıran koğucu DAHA hain ve DAHA yalancıdır»." + R_TR},
 "tokens": [
  tok("لَئِنْ","lain","part",[K, "in-shartiyya", "lam-jazim"], "اللَّامُ مُوَطِّئَةٌ لِلْقَسَمِ، وَإِنْ شَرْطِيَّةٌ — الْمُقَدِّمَةُ.", "«if indeed» — the oath-paving lam and the conditional: the premise.", "«eğer» — yemine zemin döşeyen lâm ve şart: öncül."),
  tok("كُنْتَ","kana","verb",[K, "kana-wa-akhawatuha", "in-shartiyya", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِعْلُ الشَّرْطِ، وَالتَّاءُ اسْمُهُ.", "«you have» — kana, the shart's verb; the ta its ism.", "«…-mışsan» — kâne, şart fiili; tâ ismi."),
  tok("قَدْ","qad","part",[K, "qad-harf"], "حَرْفُ تَحْقِيقٍ.", "«indeed».", "«gerçekten»."),
  tok("بُلِّغْتَ","ballagha","verb",[K, "naib-al-fail", "form-ii-verbs", "kana-wa-akhawatuha", "mafulayn"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ نَائِبُ فَاعِلٍ — الْجُمْلَةُ خَبَرُ كَانَ؛ بَلَّغَ يَنْصِبُ مَفْعُولَيْنِ، فَالثَّانِي بَاقٍ.", "«been carried (a tale)» — a passive; the ta its naib; the clause is kana's khabar; the second object of ballagha remains.", "«ulaştırılmışsan» — meçhul; tâ nâib; cümle kâne'nin haberi; bellağa'nın ikinci mef'ûlü kalır."),
  tok("عَنِّي","an","part",[K, "huruf-jarr", "ya-al-mutakallim"], "جَارٌّ وَمَجْرُورٌ — أُدْغِمَتْ نُونُ عَنْ فِي نُونِ الْوِقَايَةِ.", "«of me» — the nun of ʿan merged with the nun of protection.", "«benden» — an'ın nûnu vikāye nûnuna idgam edilmiş.", segments=[seg("عَنْ","an","part"), seg("نِي","pron-1s","pron")]),
  tok("خِيَانَةً","khiyana","noun",[K, "maful-bihi"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a treachery» — the second object.", "«bir hıyanet» — ikinci mef'ûl.", punct="*"),
  tok("لَمُبْلِغُكَ","mubligh","noun",[K, "mubtada-khabar", "idafa-definiteness", "ism-fail", "tawkid"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَمُبْلِغُ مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — اسْمُ فَاعِلِ أَبْلَغَ.", "«the one who carried it to you» — the oath's answer opens with its lam; the mubtada, an ism fa'il annexed.", "«sana ulaştıran» — yeminin cevabı lâmıyla açılır; mübtedâ, muzâf ism-i fâil.",
      segments=[seg("لَ","lam-qasam","part"), seg("مُبْلِغُ","mubligh","noun"), seg("كَ","pron-2ms","pron")]),
  tok("الْوَاشِي","washi","noun",[K, "naat-sifa", "ism-maqsur-manqus", "ism-fail"], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ: النَّمَّامُ.", "«the tale-bearer» — a na't; a manqus.", "«koğucu» — na't; manqûs."),
  tok("أَغَشُّ","aghashsh","noun",[K, "mubtada-khabar", "ism-tafdil", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ — أَفْعَلُ تَفْضِيلٍ مِنَ الْمُضَاعَفِ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more deceitful» — the khabar; an elative of a doubled root, a diptote.", "«daha hain» — haber; muzâaf kökten ism-i tafdîl, gayr-i munsarif."),
  wa_conj("وَأَكْذَبُ","akdhab","noun",[K, "atf-nasaq", "ism-tafdil", "mamnu-min-sarf"], "أَكْذَبُ مَعْطُوفٌ مَرْفُوعٌ — أَفْعَلُ تَفْضِيلٍ.", "«and more lying» — an elative, joined.", "«ve daha yalancı» — ma'tûf ism-i tafdîl.", punct=".")]})
S[-1]["badi"] = [{"kind": "kalami", "sub": "lain", "word": ix(S[-1], "لَئِنْ"), "companion": ix(S[-1], "لَمُبْلِغُكَ")}]

# ----------- s20 — al-Nabigha, bayt 3 (the analogy)
S.append({"id": "s20", "translation": {
 "en": "«…LIKE YOUR OWN DOING with a people you took into your favour, • whom you did not then find at fault in their praising you» — my case is proved by yours: the analogy closes the argument." + R_EN,
 "tr": "«…himayene aldığın bir kavme SENİN YAPTIĞIN GİBİ, • ki onları seni övmelerinde suçlu görmedin» — benim hâlim seninkiyle ispatlanır: kıyas delili kapatır." + R_TR},
 "tokens": [
  tok("كَفِعْلِكَ","fil","noun",[K, "huruf-jarr", "idafa-definiteness", "mubtada-khabar", "tashbih"], "الْكَافُ لِلتَّشْبِيهِ، وَفِعْلِ مَجْرُورٌ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: فِعْلِي كَفِعْلِكَ؛ الْقِيَاسُ.", "«like your doing» — the khabar of an unspoken «my doing is»: the analogy.", "«senin yaptığın gibi» — hazfedilmiş «benim yaptığım»ın haberi: kıyas.",
      segments=[seg("كَ","ka","part"), seg("فِعْلِ","fil","noun"), seg("كَ","pron-2ms","pron")]),
  tok("فِي","fi","part",[K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«with».", "«…-e»."),
  tok("قَوْمٍ","qawm","noun",[K, "huruf-jarr"], "مَجْرُورٌ — نَكِرَةٌ تَلِيهَا جُمْلَةُ الصِّفَةِ.", "«a people» — an indefinite with its clause of description after it.", "«bir kavim» — ardından sıfat cümlesi gelen nekre."),
  tok("أَرَاكَ","raa","verb",[K, "mudari-marfu", "jumla-sifa", "mafulayn"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْكَافُ مَفْعُولٌ أَوَّلُ — الْجُمْلَةُ نَعْتٌ لِقَوْمٍ.", "«I see you» — the doer «I», the pronoun the first object; the clause describes the people.", "«seni görüyorum» — fâil «ben», zamir ilk mef'ûl; cümle kavmin sıfatı.",
      segments=[seg("أَرَا","raa","verb"), seg("كَ","pron-2ms","pron")]),
  tok("اصْطَنَعْتَهُمْ","istanaa","verb",[K, "mafulayn", "form-viii-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْجُمْلَةُ مَفْعُولٌ ثَانٍ لِأَرَى؛ اِصْطَنَعَ: تَاءُ الِافْتِعَالِ قُلِبَتْ طَاءً بَعْدَ الصَّادِ.", "«you took into your favour» — the clause is the second object of «I see»; the ta of iftiʿal turned into a ta' after the sad.", "«himayene aldın» — cümle «görüyorum»un ikinci mef'ûlü; iftiâl tâsı sâddan sonra tı'ya dönmüş.",
      segments=[seg("اصْطَنَعْتَ","istanaa","verb"), seg("هُمْ","pron-3mp","pron")], punct="*"),
  tok("فَلَمْ","lam","part",[K, "lam-jazim"], "الْفَاءُ عَاطِفَةٌ، وَلَمْ جَازِمَةٌ.", "«then did not».", "«ve …-medin».", segments=[seg("فَ","fa","conj"), seg("لَمْ","lam","part")]),
  tok("تَرَهُمْ","raa","verb",[K, "lam-jazim", "mafulayn"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ الْأَلِفِ، وَالْفَاعِلُ أَنْتَ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ.", "«find them» — jussive by dropping the alif; the pronoun the first object.", "«onları görmedin» — elifin düşmesiyle meczûm; zamir ilk mef'ûl.",
      segments=[seg("تَرَ","raa","verb"), seg("هُمْ","pron-3mp","pron")]),
  tok("فِي","fi","part",[K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«…-de»."),
  tok("مَدْحِهِمْ","madh","noun",[K, "huruf-jarr", "idafa-definiteness", "masdar"], "مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«their praising».", "«övmelerinde».", segments=[seg("مَدْحِ","madh","noun"), seg("هِمْ","pron-3mp","pron")]),
  tok("لَكَ","li","part",[K, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«you».", "«seni».", segments=[seg("لَ","li","part"), seg("كَ","pron-2ms","pron")]),
  tok("أَذْنَبُوا","adhnaba","verb",[K, "mafulayn", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ — الْجُمْلَةُ مَفْعُولٌ ثَانٍ لِتَرَ.", "«at fault» — the clause is the second object of «find».", "«suç işlemiş» — cümle «görmedin»in ikinci mef'ûlü.", punct=".")]})
S[-1]["badi"] = [{"kind": "kalami", "sub": "qiyas", "word": ix(S[-1], "كَفِعْلِكَ"), "companion": ix(S[-1], "أَرَاكَ")}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "mubalagha": need("mubalagha", "مُبَالَغَة", "ب ل غ", "noun", "hyperbole, overstatement (masdar of بَالَغَ)", "mübalağa, aşırılık (بَالَغَ'nin masdarı)", 4),
 "maqbul": need("maqbul", "مَقْبُول", "ق ب ل", "noun", "accepted (ism maf'ul of قَبِلَ)", "makbul, kabul edilmiş (قَبِلَ'nin ism-i mef'ûlü)", 3),
 "iddaa": need("iddaa", "اِدَّعَى", "د ع و", "verb", "to claim (Form VIII, naqis; اِدَّعَى يَدَّعِي)", "iddia etmek (VIII. bâb, nâkıs; اِدَّعَى يَدَّعِي)", 4, form="VIII"),
 "wasf": need("wasf", "وَصْف", "و ص ف", "noun", "a quality, a describing (masdar of وَصَفَ)", "vasıf, nitelik (وَصَفَ'nin masdarı)", 3),
 "bulugh": need("bulugh", "بُلُوغ", "ب ل غ", "noun", "reaching, attaining (masdar of بَلَغَ)", "ulaşma, erme (بَلَغَ'nin masdarı)", 3),
 "shidda": need("shidda", "شِدَّة", "ش د د", "noun", "strength, intensity", "şiddet, kuvvet", 3),
 "daf": need("daf", "ضَعْف", "ض ع ف", "noun", "weakness", "zaaf, zayıflık", 3),
 "hadd": need("hadd", "حَدّ", "ح د د", "noun", "a limit, a degree; a definition", "sınır, derece; tarif", 3),
 "mustahil": need("mustahil", "مُسْتَحِيل", "ح و ل", "noun", "impossible (ism fa'il of اسْتَحَالَ)", "imkânsız, muhal (اسْتَحَالَ'nin ism-i fâili)", 4),
 "mustabad": need("mustabad", "مُسْتَبْعَد", "ب ع د", "noun", "far-fetched, deemed remote (ism maf'ul of اسْتَبْعَدَ)", "uzak görülen (اسْتَبْعَدَ'nin ism-i mef'ûlü)", 5),
 "thalatha": need("thalatha", "ثَلَاثَة", "ث ل ث", "noun", "three", "üç", 1),
 "tabligh": need("tabligh", "تَبْلِيغ", "ب ل غ", "noun", "tabligh — the hyperbole possible in reason and custom (masdar of بَلَّغَ)", "tebliğ — aklen ve âdeten mümkün mübalağa (بَلَّغَ'nin masdarı)", 5),
 "ighraq": need("ighraq", "إِغْرَاق", "غ ر ق", "noun", "ighraq — the hyperbole possible in reason, not in custom (masdar of أَغْرَقَ)", "iğrâk — aklen mümkün, âdeten değil (أَغْرَقَ'nin masdarı)", 5),
 "ghuluww": need("ghuluww", "غُلُوّ", "غ ل و", "noun", "ghuluww — the hyperbole possible neither in reason nor in custom (masdar of غَلَا)", "gulüv — ne aklen ne âdeten mümkün mübalağa (غَلَا'nın masdarı)", 5),
 "imru": need("imru", "امْرُؤ", "م ر ء", "noun", "a man (in the name Imru' al-Qays)", "adam, kişi (İmruülkays adında)", 5),
 "qays": need("qays", "الْقَيْس", None, "propn", "al-Qays (in the name Imru' al-Qays, the pre-Islamic poet)", "el-Kays (Câhiliye şairi İmruülkays adında)", 5),
 "ada-hunt": need("ada-hunt", "عَادَى", "ع د و", "verb", "عَادَى بَيْنَ: to run down two prey in one course (Form III, naqis)", "عَادَى بَيْنَ: iki avı tek koşuda almak (III. bâb, nâkıs)", 6, form="III"),
 "ida": need("ida", "عِدَاء", "ع د و", "noun", "one course after two prey (masdar of عَادَى)", "iki av ardınca tek koşu (عَادَى'nın masdarı)", 6),
 "thawr": need("thawr", "ثَوْر", "ث و ر", "noun", "a bull; the wild bull (oryx)", "boğa; yaban boğası", 3),
 "naja": need("naja", "نَعْجَة", "ن ع ج", "noun", "a ewe; the wild cow (oryx doe)", "koyun; yaban ineği", 4),
 "dirak": need("dirak", "دِرَاك", "د ر ك", "noun", "in succession, one after the other (a masdar used as hal)", "ardarda, birbiri ardınca (hâl olarak masdar)", 6),
 "nadaha": need("nadaha", "نَضَحَ", "ن ض ح", "verb", "to sprinkle; (of a horse) to sweat (نَضَحَ يَنْضَحُ)", "sıçratmak; (at) terlemek (نَضَحَ يَنْضَحُ)", 5, form="I"),
 "ghasala": need("ghasala", "غَسَلَ", "غ س ل", "verb", "to wash (غَسَلَ يَغْسِلُ)", "yıkamak (غَسَلَ يَغْسِلُ)", 2, form="I"),
 "aql": need("aql", "عَقْل", "ع ق ل", "noun", "reason, intellect", "akıl", 2),
 "ayham": need("ayham", "الْأَيْهَم", None, "propn", "al-Ayham (in the name ʿAmr b. al-Ayham al-Taghlibi)", "el-Eyhem (Amr b. Eyhem et-Tağlibî adında)", 6),
 "taghlibi": need("taghlibi", "التَّغْلِبِيّ", None, "propn", "al-Taghlibi — of the tribe Taghlib", "et-Tağlibî — Tağlib kabilesinden", 6),
 "jar": need("jar", "جَار", "ج و ر", "noun", "a neighbour", "komşu", 2, plural="جِيرَان"),
 "dama": need("dama", "دَامَ", "د و م", "verb", "to endure, to last (دَامَ يَدُومُ; مَا دَامَ: as long as — a sister of كَانَ)", "sürmek, devam etmek (دَامَ يَدُومُ; مَا دَامَ: …-dıkça — كَانَ'nin kardeşi)", 3, form="I"),
 "atbaa": need("atbaa", "أَتْبَعَ", "ت ب ع", "verb", "to make (something) follow (someone) — two objects (Form IV)", "ardınca göndermek, tâbi kılmak — iki mef'ûl (IV. bâb)", 4, form="IV"),
 "haythu": need("haythu", "حَيْثُ", None, "noun", "where, wherever (a zarf built on the damma)", "nerede, nereye (damme üzere mebnî zarf)", 3),
 "mala": need("mala", "مَالَ", "م ي ل", "verb", "to incline, to turn away (مَالَ يَمِيلُ — hollow)", "meyletmek, yönelmek (مَالَ يَمِيلُ — ecvef)", 3, form="I"),
 "nuwas": need("nuwas", "نُوَاس", None, "propn", "Nuwas (in the name Abu Nuwas — al-Hasan b. Hani', the ʿAbbasid poet, d. c. 198/814)", "Nüvâs (Ebû Nüvâs adında — Hasan b. Hâni', Abbâsî şairi, ö. yak. 198/814)", 6),
 "akhafa": need("akhafa", "أَخَافَ", "خ و ف", "verb", "to frighten, to terrify (Form IV, hollow)", "korkutmak (IV. bâb, ecvef)", 4, form="IV"),
 "shirk": need("shirk", "شِرْك", "ش ر ك", "noun", "polytheism, associating partners with Allah", "şirk", 3),
 "nutfa": need("nutfa", "نُطْفَة", "ن ط ف", "noun", "a drop (of seed)", "nutfe, damla", 4, plural="نُطَف"),
 "dakhala": need("dakhala", "دَخَلَ", "د خ ل", "verb", "to enter (دَخَلَ يَدْخُلُ)", "girmek (دَخَلَ يَدْخُلُ)", 1, form="I"),
 "qarraba": need("qarraba", "قَرَّبَ", "ق ر ب", "verb", "to bring near (Form II)", "yaklaştırmak (II. bâb)", 3, form="II"),
 "sihha": need("sihha", "صِحَّة", "ص ح ح", "noun", "soundness, validity", "sıhhat, doğruluk", 3),
 "kada": need("kada", "كَادَ", "ك و د", "verb", "to be on the point of, well-nigh (كَادَ يَكَادُ — a verb of nearness, a sister of كَانَ)", "neredeyse …-mak, az kalsın (كَادَ يَكَادُ — mukarebe fiili, كَانَ'nin kardeşi)", 4, form="I"),
 "zayt": need("zayt", "زَيْت", "ز ي ت", "noun", "oil", "yağ, zeytinyağı", 2),
 "adaa": need("adaa", "أَضَاءَ", "ض و ء", "verb", "to shine, to give light (Form IV, hollow)", "ışımak, aydınlatmak (IV. bâb, ecvef)", 4, form="IV"),
 "massa": need("massa", "مَسَّ", "م س س", "verb", "to touch (doubled: مَسَّ يَمَسُّ)", "dokunmak (muzâaf: مَسَّ يَمَسُّ)", 3, form="I"),
 "tadammana": need("tadammana", "تَضَمَّنَ", "ض م ن", "verb", "to contain, to carry within (Form V)", "içermek, tazammun etmek (V. bâb)", 4, form="V"),
 "hasan": need("hasan", "حَسَن", "ح س ن", "noun", "fine, good, beautiful", "güzel, iyi", 2),
 "takhyil": need("takhyil", "تَخْيِيل", "خ ي ل", "noun", "fancy, imagining (masdar of خَيَّلَ)", "hayal ettirme, tahyîl (خَيَّلَ'nin masdarı)", 5),
 "aqada": need("aqada", "عَقَدَ", "ع ق د", "verb", "to knot, to tie (عَقَدَ يَعْقِدُ)", "düğümlemek, bağlamak (عَقَدَ يَعْقِدُ)", 3, form="I"),
 "sunbuk": need("sunbuk", "سُنْبُك", None, "noun", "the tip of a hoof", "tırnak ucu", 6, plural="سَنَابِك"),
 "ithyar": need("ithyar", "عِثْيَر", "ع ث ر", "noun", "dust raised by hooves", "tırnakların kaldırdığı toz", 6),
 "anaq": need("anaq", "عَنَق", "ع ن ق", "noun", "a pacing gait (of a horse)", "rahvan yürüyüş", 6),
 "ijtamaa": need("ijtamaa", "اِجْتَمَعَ", "ج م ع", "verb", "to come together, to gather (Form VIII)", "bir araya gelmek, toplanmak (VIII. bâb)", 3, form="VIII"),
 "arrajani": need("arrajani", "الْأَرَّجَانِيّ", None, "propn", "al-Arrajani — Ahmad b. Muhammad, the judge-poet of Arrajan (d. 544/1149)", "el-Errecânî — Ahmed b. Muhammed, Errecân kadısı ve şairi (ö. 544/1149)", 6),
 "khayyala": need("khayyala", "خَيَّلَ", "خ ي ل", "verb", "خُيِّلَ إِلَيْهِ: it seemed to him (Form II, passive)", "خُيِّلَ إِلَيْهِ: ona öyle geldi (II. bâb, meçhul)", 5, form="II"),
 "sammara": need("sammara", "سَمَّرَ", "س م ر", "verb", "to nail (Form II)", "çivilemek (II. bâb)", 5, form="II"),
 "shihab": need("shihab", "شِهَاب", "ش ه ب", "noun", "a star, a shooting star", "yıldız, şihâb", 4, plural="شُهْب"),
 "shadda": need("shadda", "شَدَّ", "ش د د", "verb", "to tighten, to bind (doubled: شَدَّ يَشُدُّ)", "sıkmak, bağlamak (muzâaf: شَدَّ يَشُدُّ)", 4, form="I"),
 "hudb": need("hudb", "هُدْب", "ه د ب", "noun", "an eyelash", "kirpik", 5, plural="أَهْدَاب"),
 "jafn": need("jafn", "جَفْن", "ج ف ن", "noun", "an eyelid", "göz kapağı", 5, plural="أَجْفَان"),
 "akhraja": need("akhraja", "أَخْرَجَ", "خ ر ج", "verb", "to bring out (Form IV)", "çıkarmak (IV. bâb)", 2, form="IV"),
 "makhraj": need("makhraj", "مَخْرَج", "خ ر ج", "noun", "a way out; a manner of bringing out (mimi masdar)", "çıkış; çıkarma tarzı (mîmî masdar)", 4),
 "hazl": need("hazl", "هَزْل", "ه ز ل", "noun", "jest, joking", "şaka, hezl", 4),
 "shair": need("shair", "شَاعِر", "ش ع ر", "noun", "a poet", "şair", 2),
 "sakira": need("sakira", "سَكِرَ", "س ك ر", "verb", "to get drunk (سَكِرَ يَسْكَرُ)", "sarhoş olmak (سَكِرَ يَسْكَرُ)", 4, form="I"),
 "shurb": need("shurb", "شُرْب", "ش ر ب", "noun", "drinking (masdar of شَرِبَ)", "içme (شَرِبَ'nin masdarı)", 2),
 "ajab": need("ajab", "عَجَب", "ع ج ب", "noun", "a wonder, astonishment", "şaşılacak şey, hayret", 3),
 "kalami": need("kalami", "كَلَامِيّ", "ك ل م", "noun", "of kalam — in the theologians' manner (a nisba)", "kelâmî — kelâmcıların yolu üzere (nisbet)", 5),
 "irad": need("irad", "إِيرَاد", "و ر د", "noun", "bringing forward, adducing (masdar of أَوْرَدَ)", "getirme, îrâd (أَوْرَدَ'nin masdarı)", 4),
 "tariqa": need("tariqa", "طَرِيقَة", "ط ر ق", "noun", "a way, a manner", "yol, tarz", 2),
 "kalam": need("kalam", "كَلَام", "ك ل م", "noun", "speech; the science of kalam", "söz; kelâm ilmi", 2),
 "ilah": need("ilah", "إِلَه", "أ ل ه", "noun", "a god, a deity", "ilâh", 2, plural="آلِهَة"),
 "fasada": need("fasada", "فَسَدَ", "ف س د", "verb", "to go to ruin, to be spoiled (فَسَدَ يَفْسُدُ)", "bozulmak, fesada uğramak (فَسَدَ يَفْسُدُ)", 3, form="I"),
 "nabigha": need("nabigha", "النَّابِغَة", None, "propn", "al-Nabigha al-Dhubyani — Ziyad b. Muʿawiya, the pre-Islamic poet (d. c. 604)", "Nâbiğa ez-Zübyânî — Ziyâd b. Muâviye, Câhiliye şairi (ö. yak. 604)", 6),
 "halafa": need("halafa", "حَلَفَ", "ح ل ف", "verb", "to swear an oath (حَلَفَ يَحْلِفُ)", "yemin etmek (حَلَفَ يَحْلِفُ)", 3, form="I"),
 "riba-doubt": need("riba-doubt", "رِيبَة", "ر ي ب", "noun", "a doubt, a suspicion", "şüphe, kuşku", 4),
 "wara": need("wara", "وَرَاءَ", "و ر ي", "noun", "behind, beyond (a zarf)", "arkasında, ötesinde (zarf)", 3),
 "khiyana": need("khiyana", "خِيَانَة", "خ و ن", "noun", "treachery, betrayal", "hıyanet", 3),
 "mubligh": need("mubligh", "مُبْلِغ", "ب ل غ", "noun", "one who carries (a word) to another (ism fa'il of أَبْلَغَ)", "ulaştıran, haber taşıyan (أَبْلَغَ'nin ism-i fâili)", 4),
 "aghashsh": need("aghashsh", "أَغَشّ", "غ ش ش", "noun", "more deceitful (elative of غَاشّ)", "daha hain, daha aldatıcı (غَاشّ'ın ism-i tafdîli)", 5),
 "akdhab": need("akdhab", "أَكْذَب", "ك ذ ب", "noun", "more lying (elative of كَاذِب)", "daha yalancı (كَاذِب'in ism-i tafdîli)", 4),
 "istanaa": need("istanaa", "اِصْطَنَعَ", "ص ن ع", "verb", "to take into one's favour, to make one's own (Form VIII)", "himayesine almak, kendine bağlamak (VIII. bâb)", 5, form="VIII"),
 "adhnaba": need("adhnaba", "أَذْنَبَ", "ذ ن ب", "verb", "to commit a fault, to sin (Form IV)", "suç işlemek, günah işlemek (IV. bâb)", 3, form="IV"),
 "madh": need("madh", "مَدْح", "م د ح", "noun", "praise (masdar of مَدَحَ)", "medih, övgü (مَدَحَ'nin masdarı)", 3),
 "mutanabbi": need("mutanabbi", "الْمُتَنَبِّي", None, "propn", "al-Mutanabbi — Abu l-Tayyib Ahmad b. al-Husayn, the poet of Sayf al-Dawla (d. 354/965)", "el-Mütenebbî — Ebü't-Tayyib Ahmed b. Hüseyin, Seyfüddevle'nin şairi (ö. 354/965)", 6),
}
for k in ("qawl", "min", "huwa", "hiya", "an-masdariyya", "fi", "li", "bi", "ila", "ka", "wa", "fa", "pron-3fs", "pron-3ms", "pron-3mp", "pron-1s", "pron-1p", "pron-2ms", "pron-3d", "pron-3fp",
          "aw", "aqsam", "ma-mawsula", "amkana", "ada", "amr-alam", "ibn", "akrama", "karama", "ab", "ahl", "hatta", "inna", "khafa", "allati", "lam", "khalaqa", "ma-water",
          "awwal", "law", "ibtagha", "ala", "qad", "duja", "azama", "ams", "ghad", "dha", "madhhab", "hujja", "matlub", "kana", "illa", "allah", "taraka", "nafs", "laysa",
          "mar", "lain", "ballagha", "an", "washi", "fil", "qawm", "raa", "taala", "naw", "tawkid", "lam-ibtida"):
    if k not in TG: CAND[k] = find_gloss(k)
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
def gem(bab_key, L, F, Lm, Fm, amr, masdar, fail, maful, pmz, pmd, note):
    b, w = _sg.BABS[bab_key]
    return _sg.entry(b + " — مُضَاعَفٌ", w, masdar, fail, _sg.mazi14(L, F), _sg.mudari14("َ", Lm, Fm), amr,
                     "يَ" + Lm + "َ", "يَ" + Lm + "َ", "تَ" + Lm + "َ", maful, pmz, pmd, note)
put_morph(mo, "iddaa", _sg.derived_naqis(_sg.B8, _sg.W8, "َ", "اِدَّعَ", "دَّع", "i", "اِدَّع", "اِدِّعَاء", "مُدَّعٍ (الْمُدَّعِي)", "مُدَّعًى", "اُدُّعِيَ", "يُدَّعَى",
                                         "اِفْتَعَلَ مِنْ دَعَا: اِدْتَعَى — قُلِبَتْ تَاءُ الِافْتِعَالِ دَالًا بَعْدَ الدَّالِ وَأُدْغِمَتْ: اِدَّعَى يَدَّعِي."))
put_morph(mo, "ada-hunt", _sg.derived_naqis(_sg.B3, _sg.W3, "ُ", "عَادَ", "عَاد", "i", "عَاد", "مُعَادَاة", "مُعَادٍ (الْمُعَادِي)", "مُعَادًى", "عُودِيَ", "يُعَادَى",
                                            "فَاعَلَ مِنْ عَدَا: عَادَى بَيْنَ الصَّيْدَيْنِ — وَالَى بَيْنَهُمَا؛ مَصْدَرُهُ فِي الْبَيْتِ عِدَاءٌ عَلَى فِعَالٍ."))
put_morph(mo, "nadaha", _sg.sound1("fataha", "نَضَح", "نْضَح", "اِنْضَح", "نَضْح", "نَاضِح", maful="مَنْضُوح", pmz="نُضِحَ", pmd="يُنْضَحُ"))
put_morph(mo, "ghasala", _sg.sound1("daraba", "غَسَل", "غْسِل", "اِغْسِل", "غَسْل", "غَاسِل", maful="مَغْسُول", pmz="غُسِلَ", pmd="يُغْسَلُ"))
put_morph(mo, "atbaa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَتْبَع", "تْبِع", "أَتْبِع", "إِتْبَاع", "مُتْبِع", "مُتْبَع", "أُتْبِعَ", "يُتْبَعُ"))
put_morph(mo, "mala", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "مَال", "مِل", "مِيل", "مِل", "مِيل", "مِل", "مَيْل", "مَائِل",
                                  note="أَجْوَفُ يَائِيٌّ: مَالَ يَمِيلُ — مِلْتُ بِحَذْفِ الْأَلِفِ لِلسَّاكِنِ."))
put_morph(mo, "akhafa", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَخَاف", "أَخَف", "خِيف", "خِف", "أَخِيف", "أَخِف", "إِخَافَة", "مُخِيف", "مُخَاف", "أُخِيفَ", "يُخَافُ",
                                           "أَجْوَفُ عَلَى أَفْعَلَ: أَخَافَ يُخِيفُ — أَخَفْتُ: حُذِفَتِ الْأَلِفُ لِلسَّاكِنِ."))
put_morph(mo, "dakhala", _sg.sound1("nasara", "دَخَل", "دْخُل", "اُدْخُل", "دُخُول", "دَاخِل", maful="مَدْخُول", pmz="دُخِلَ", pmd="يُدْخَلُ"))
put_morph(mo, "qarraba", _sg.derived(_sg.B2, _sg.W2, "ُ", "قَرَّب", "قَرِّب", "قَرِّب", "تَقْرِيب", "مُقَرِّب", "مُقَرَّب", "قُرِّبَ", "يُقَرَّبُ"))
put_morph(mo, "kada", _sg.hollow1("fataha", "أَجْوَفُ وَاوِيٌّ", "كَاد", "كِد", "كَاد", "كَد", "كَد", "كَد", "كَوْد", "كَائِد",
                                  note="أَجْوَفُ وَاوِيٌّ مِنْ بَابِ فَتَحَ عَلَى الْمَشْهُورِ (وَقِيلَ مِنْ بَابِ سَمِعَ): كَادَ يَكَادُ — كِدْتُ؛ مِنْ أَفْعَالِ الْمُقَارَبَةِ يَرْفَعُ الِاسْمَ وَخَبَرُهُ مُضَارِعٌ."))
put_morph(mo, "adaa", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَضَاء", "أَضَأ", "ضِيء", "ضِئ", "أَضِئ", "أَضِئ", "إِضَاءَة", "مُضِيء", "مُضَاء", "أُضِيءَ", "يُضَاءُ",
                                         "أَجْوَفُ مَهْمُوزُ اللَّامِ عَلَى أَفْعَلَ: أَضَاءَ يُضِيءُ — أَضَأْتُ."))
put_morph(mo, "massa", gem("fataha", "مَسّ", "مَسِس", "مَسّ", "مْسَس", ["مَسَّ", "مَسَّا", "مَسُّوا", "مَسِّي", "مَسَّا", "اِمْسَسْنَ"], "مَسّ", "مَاسّ", "مَمْسُوس", "مُسَّ", "يُمَسُّ",
                        "مُضَاعَفٌ مِنْ بَابِ سَمِعَ: مَسَّ يَمَسُّ — مَسِسْتُ، لَمْ تَمْسَسْهُ: يُفَكُّ الْإِدْغَامُ عِنْدَ السَّاكِنِ."))
mo["verbs"]["massa"]["majzum"] = "يَمْسَسْ"; mo["verbs"]["massa"]["majzum2"] = "تَمْسَسْ"   # the book writes the jussive with its idgham undone (لَمْ تَمْسَسْهُ)
put_morph(mo, "tadammana", _sg.idgham(_sg.derived(_sg.B5, _sg.W5, "َ", "تَضَمَّن", "تَضَمَّن", "تَضَمَّن", "تَضَمُّن", "مُتَضَمِّن", "مُتَضَمَّن", "تُضُمِّنَ", "يُتَضَمَّنُ")))
put_morph(mo, "aqada", _sg.sound1("daraba", "عَقَد", "عْقِد", "اِعْقِد", "عَقْد", "عَاقِد", maful="مَعْقُود", pmz="عُقِدَ", pmd="يُعْقَدُ"))
put_morph(mo, "ijtamaa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِجْتَمَع", "جْتَمِع", "اِجْتَمِع", "اِجْتِمَاع", "مُجْتَمِع", "مُجْتَمَع", "اُجْتُمِعَ", "يُجْتَمَعُ"))
put_morph(mo, "khayyala", _sg.derived(_sg.B2, _sg.W2, "ُ", "خَيَّل", "خَيِّل", "خَيِّل", "تَخْيِيل", "مُخَيِّل", "مُخَيَّل", "خُيِّلَ", "يُخَيَّلُ",
                                      "خُيِّلَ إِلَيْهِ: مَبْنِيٌّ لِلْمَجْهُولِ فِي الْمَتْنِ."))
put_morph(mo, "sammara", _sg.derived(_sg.B2, _sg.W2, "ُ", "سَمَّر", "سَمِّر", "سَمِّر", "تَسْمِير", "مُسَمِّر", "مُسَمَّر", "سُمِّرَ", "يُسَمَّرُ"))
put_morph(mo, "shadda", gem("nasara", "شَدّ", "شَدَد", "شُدّ", "شْدُد", ["شُدَّ", "شُدَّا", "شُدُّوا", "شُدِّي", "شُدَّا", "اُشْدُدْنَ"], "شَدّ", "شَادّ", "مَشْدُود", "شُدَّ", "يُشَدُّ",
                         "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: شَدَّ يَشُدُّ — شُدَّتْ: مَبْنِيٌّ لِلْمَجْهُولِ."))
put_morph(mo, "akhraja", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَخْرَج", "خْرِج", "أَخْرِج", "إِخْرَاج", "مُخْرِج", "مُخْرَج", "أُخْرِجَ", "يُخْرَجُ"))
put_morph(mo, "sakira", _sg.sound1("samia", "سَكِر", "سْكَر", "اِسْكَر", "سُكْر", "سَكْرَان", note="لَازِمٌ مِنْ بَابِ سَمِعَ: سَكِرَ يَسْكَرُ؛ وَصْفُهُ سَكْرَانُ عَلَى فَعْلَانَ."))
put_morph(mo, "fasada", _sg.sound1("nasara", "فَسَد", "فْسُد", "اُفْسُد", "فَسَاد", "فَاسِد", note="لَازِمٌ: فَسَدَ يَفْسُدُ — لَفَسَدَتَا."))
put_morph(mo, "halafa", _sg.sound1("daraba", "حَلَف", "حْلِف", "اِحْلِف", "حَلِف", "حَالِف", maful="مَحْلُوف", pmz="حُلِفَ", pmd="يُحْلَفُ"))
put_morph(mo, "istanaa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِصْطَنَع", "صْطَنِع", "اِصْطَنِع", "اِصْطِنَاع", "مُصْطَنِع", "مُصْطَنَع", "اُصْطُنِعَ", "يُصْطَنَعُ",
                                     "اِفْتَعَلَ مِنْ صَنَعَ: قُلِبَتْ تَاءُ الِافْتِعَالِ طَاءً بَعْدَ الصَّادِ: اِصْطَنَعَ."))
put_morph(mo, "adhnaba", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَذْنَب", "ذْنِب", "أَذْنِب", "إِذْنَاب", "مُذْنِب", None, None, None, "لَازِمٌ: أَذْنَبَ يُذْنِبُ."))
# a verb copied in from another package brings its paradigm with it (the release gate wants every glossary verb conjugated)
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_M = {
 "id": "mubalagha-maqbula",
 "title": {"ar": "الْمُبَالَغَةُ الْمَقْبُولَةُ — تَبْلِيغٌ وَإِغْرَاقٌ وَغُلُوٌّ، وَمَا يُقْبَلُ مِنَ الْغُلُوِّ", "en": "The accepted mubalagha — tabligh, ighraq, ghuluww, and the ghuluww that is accepted", "tr": "Makbul mübalağa — tebliğ, iğrâk, gulüv ve makbul olan gulüv"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — المبالغة المقبولة: أن يدعى لوصف بلوغه في الشدة أو الضعف حدا مستحيلا أو مستبعدا؛ وهي ثلاثة أقسام: تبليغ وإغراق وغلو؛ ومن الغلو مقبول: ما دخله ما يقربه إلى الصحة، وما تضمن نوعا حسنا من التخييل، وما أخرج مخرج الهزل"],
 "question": {
  "en": ["Is a quality claimed to reach a degree that is IMPOSSIBLE or FAR-FETCHED? Then it is a MUBALAGHA — and its degree is measured by two yardsticks, reason and custom.",
         "Possible in both? TABLIGH — Imru' al-Qays's horse takes a bull and a doe in one course and does not sweat. Possible in reason, not in custom? IGHRAQ — the honouring that follows the neighbour wherever he goes. Possible in neither? GHULUWW — the uncreated drops fear you.",
         "Is a ghuluww still ACCEPTED? When a word brings it near to the possible (يَكَادُ زَيْتُهَا يُضِيءُ), when it carries a fine fancy (a dust one could pace upon — لَوْ … لَأَمْكَنَا), when both come together (يُخَيَّلُ لِي أَنْ سُمِّرَ الشُّهْبُ), or when it is said in jest (drunk yesterday for tomorrow's wine).",
         "What does the engine read? The degree is the author's judgement (reason, custom) — a DOC shortlist; the RECEIPT of acceptance is read off the surface: the verb of nearness كَادَ, the unreal لَوْ with its لَ-answer, the حَتَّى that opens the consequence, the يُخَيَّلُ, the tibaq of yesterday and tomorrow that marks the jest."],
  "tr": ["Bir vasfın İMKÂNSIZ yahut UZAK bir dereceye ulaştığı mı iddia ediliyor? O hâlde MÜBALAĞADIR — derecesi iki ölçüyle ölçülür: akıl ve âdet.",
         "İkisinde de mümkün mü? TEBLİĞ — İmruülkays'ın atı bir boğayla bir ineği tek koşuda alır da terlemez. Aklen mümkün, âdeten değil mi? İĞRÂK — komşunun gittiği yere giden ikram. Hiçbirinde mümkün değil mi? GULÜV — yaratılmamış nutfeler senden korkar.",
         "Gulüv yine de MAKBUL mü? Onu mümküne yaklaştıran bir kelime girince (يَكَادُ زَيْتُهَا يُضِيءُ), güzel bir hayal taşıyınca (üstünde yürünebilecek toz — لَوْ … لَأَمْكَنَا), ikisi bir araya gelince (يُخَيَّلُ لِي أَنْ سُمِّرَ الشُّهْبُ), yahut şaka yollu söylenince (yarının şarabı için dün sarhoş).",
         "Motor neyi okur? Derece müellifin hükmüdür (akıl, âdet) — bir DOC listesi; kabulün ALINDISI yüzeyden okunur: mukarebe fiili كَادَ, لَ-cevaplı gayr-i vâki لَوْ, sonucu açan حَتَّى, يُخَيَّلُ, şakayı işaretleyen dün-yarın tıbâkı."]},
 "plain": {
  "en": "The mubalagha claims a quality reaches an impossible or far-fetched degree: tabligh (possible in reason and custom), ighraq (in reason only), ghuluww (in neither). The first two are accepted; the ghuluww too when a nearing word, a fine fancy, both, or jest carries it. The engine reads those receipts.",
  "tr": "Mübalağa, bir vasfın imkânsız yahut uzak bir dereceye ulaştığını iddia eder: tebliğ (aklen ve âdeten mümkün), iğrâk (yalnız aklen), gulüv (hiçbirinde). İlk ikisi makbuldür; gulüv de yaklaştıran kelime, güzel hayal, ikisi yahut şaka taşıyınca. Motor o alındıları okur."},
 "explanation": {
  "en": "The accepted MUBALAGHA is أَنْ يُدَّعَى لِوَصْفٍ بُلُوغُهُ فِي الشِّدَّةِ أَوِ الضَّعْفِ حَدًّا مُسْتَحِيلًا أَوْ مُسْتَبْعَدًا. It is of three degrees. TABLIGH: the claim is possible in reason and in custom — Imru' al-Qays: فَعَادَى عِدَاءً بَيْنَ ثَوْرٍ وَنَعْجَةٍ دِرَاكًا فَلَمْ يَنْضَحْ بِمَاءٍ فَيُغْسَلِ, a horse that takes two prey in one course and does not sweat. IGHRAQ: possible in reason, not in custom — ʿAmr b. al-Ayham: وَنُكْرِمُ جَارَنَا مَا دَامَ فِينَا وَنُتْبِعُهُ الْكَرَامَةَ حَيْثُ مَالَا, an honouring that follows the neighbour wherever he turns. GHULUWW: possible in neither — Abu Nuwas: أَخَفْتَ أَهْلَ الشِّرْكِ حَتَّى إِنَّهُ لَتَخَافُكَ النُّطَفُ الَّتِي لَمْ تُخْلَقِ. The first two are accepted; of the ghuluww, three kinds are accepted: what a nearing word enters — يَكَادُ زَيْتُهَا يُضِيءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌ (24:35), where «its oil glows» would be ghuluww and يَكَادُ brings it near the possible; what carries a fine fancy — al-Mutanabbi's عَقَدَتْ سَنَابِكُهَا عَلَيْهَا عِثْيَرًا لَوْ تَبْتَغِي عَنَقًا عَلَيْهِ لَأَمْكَنَا; the two together — al-Arrajani's يُخَيَّلُ لِي أَنْ سُمِّرَ الشُّهْبُ فِي الدُّجَى وَشُدَّتْ بِأَهْدَابِي إِلَيْهِنَّ أَجْفَانِي; and what is said in jest — أَسْكَرُ بِالْأَمْسِ إِنْ عَزَمْتُ عَلَى الشُّرْبِ غَدًا إِنَّ ذَا مِنَ الْعَجَبِ. WHAT THE ENGINE CLAIMS: the degree (tabligh / ighraq / ghuluww) is a judgement about the world — possible by reason, possible by custom — and the engine does not pretend to it: it shows the three as a DOC shortlist beside the author's choice. The RECEIPT of acceptance it does read: كَادَ and its forms (a verb of nearness taking a marfuʿ ism and a verb-clause khabar — the seats DabtEngine hands it), the unreal لَوْ with its لَ-answer (ShartEngine's frame), the حَتَّى that opens a consequence clause with إِنَّ, the passive يُخَيَّلُ, and the jest's tibaq of أَمْس and غَد off the contraries table.",
  "tr": "Makbul MÜBALAĞA أَنْ يُدَّعَى لِوَصْفٍ بُلُوغُهُ فِي الشِّدَّةِ أَوِ الضَّعْفِ حَدًّا مُسْتَحِيلًا أَوْ مُسْتَبْعَدًا'dır. Üç derecedir. TEBLİĞ: iddia aklen ve âdeten mümkün — İmruülkays: فَعَادَى عِدَاءً بَيْنَ ثَوْرٍ وَنَعْجَةٍ دِرَاكًا فَلَمْ يَنْضَحْ بِمَاءٍ فَيُغْسَلِ, iki avı tek koşuda alıp terlemeyen at. İĞRÂK: aklen mümkün, âdeten değil — Amr b. Eyhem: وَنُكْرِمُ جَارَنَا مَا دَامَ فِينَا وَنُتْبِعُهُ الْكَرَامَةَ حَيْثُ مَالَا, komşunun gittiği yere giden ikram. GULÜV: hiçbirinde mümkün değil — Ebû Nüvâs: أَخَفْتَ أَهْلَ الشِّرْكِ حَتَّى إِنَّهُ لَتَخَافُكَ النُّطَفُ الَّتِي لَمْ تُخْلَقِ. İlk ikisi makbuldür; gulüvün üç türü makbuldür: yaklaştıran kelime girmiş olan — يَكَادُ زَيْتُهَا يُضِيءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌ (Nûr 35), «yağı aydınlatır» gulüv olurdu, يَكَادُ onu mümküne yaklaştırır; güzel bir hayal taşıyan — Mütenebbî'nin عَقَدَتْ سَنَابِكُهَا عَلَيْهَا عِثْيَرًا لَوْ تَبْتَغِي عَنَقًا عَلَيْهِ لَأَمْكَنَا'sı; ikisi bir arada — Errecânî'nin يُخَيَّلُ لِي أَنْ سُمِّرَ الشُّهْبُ فِي الدُّجَى وَشُدَّتْ بِأَهْدَابِي إِلَيْهِنَّ أَجْفَانِي'si; ve şaka yollu söylenen — أَسْكَرُ بِالْأَمْسِ إِنْ عَزَمْتُ عَلَى الشُّرْبِ غَدًا إِنَّ ذَا مِنَ الْعَجَبِ. MOTORUN İDDİASI: derece (tebliğ / iğrâk / gulüv) dünya hakkında bir hükümdür — aklen mümkün, âdeten mümkün — motor buna kalkışmaz: üçünü müellifin seçiminin yanında bir DOC listesi olarak gösterir. Kabulün ALINDISINI okur: كَادَ ve şekilleri (merfû isim ve fiil cümlesi haber alan mukarebe fiili — DabtEngine'in verdiği koltuklar), لَ-cevaplı gayr-i vâki لَوْ (ShartEngine'in çerçevesi), إِنَّ'li sonuç cümlesi açan حَتَّى, meçhul يُخَيَّلُ, ve zıtlar tablosundan şakanın أَمْس-غَد tıbâkı."},
 "examples": [
  {"ar": "فَعَادَى عِدَاءً بَيْنَ ثَوْرٍ وَنَعْجَةٍ * دِرَاكًا فَلَمْ يَنْضَحْ بِمَاءٍ فَيُغْسَلِ", "en": "Imru' al-Qays — tabligh.", "tr": "İmruülkays — tebliğ.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "وَنُكْرِمُ جَارَنَا مَا دَامَ فِينَا * وَنُتْبِعُهُ الْكَرَامَةَ حَيْثُ مَالَا", "en": "ʿAmr b. al-Ayham — ighraq.", "tr": "Amr b. Eyhem — iğrâk.", "sourceStory": "talkhis-al-miftah", "sentence": "s5"},
  {"ar": "أَخَفْتَ أَهْلَ الشِّرْكِ حَتَّى إِنَّهُ * لَتَخَافُكَ النُّطَفُ الَّتِي لَمْ تُخْلَقِ", "en": "Abu Nuwas — ghuluww.", "tr": "Ebû Nüvâs — gulüv.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"},
  {"ar": "يَكَادُ زَيْتُهَا يُضِيءُ وَلَوْ لَمْ تَمْسَسْهُ نَارٌ", "en": "24:35 — the nearing word.", "tr": "Nûr 35 — yaklaştıran kelime.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"},
  {"ar": "عَقَدَتْ سَنَابِكُهَا عَلَيْهَا عِثْيَرًا * لَوْ تَبْتَغِي عَنَقًا عَلَيْهِ لَأَمْكَنَا", "en": "al-Mutanabbi — the fine fancy.", "tr": "Mütenebbî — güzel hayal.", "sourceStory": "talkhis-al-miftah", "sentence": "s11"},
  {"ar": "يُخَيَّلُ لِي أَنْ سُمِّرَ الشُّهْبُ فِي الدُّجَى * وَشُدَّتْ بِأَهْدَابِي إِلَيْهِنَّ أَجْفَانِي", "en": "al-Arrajani — both together.", "tr": "Errecânî — ikisi bir arada.", "sourceStory": "talkhis-al-miftah", "sentence": "s13"},
  {"ar": "أَسْكَرُ بِالْأَمْسِ إِنْ عَزَمْتُ عَلَى الشُّرْبِ غَدًا * إِنَّ ذَا مِنَ الْعَجَبِ", "en": "the jest.", "tr": "şaka.", "sourceStory": "talkhis-al-miftah", "sentence": "s15"}],
 "commonMistakes": [
  {"wrong": "«يَكَادُ زَيْتُهَا يُضِيءُ mübalağa değildir, çünkü yağ aydınlatmaz»",
   "right": "«Gulüvdür — yağ ateşsiz aydınlatmaz — fakat يَكَادُ onu mümküne yaklaştırdığı için MAKBULDÜR»",
   "why": {"en": "The nearing word does not remove the hyperbole; it makes it acceptable.", "tr": "Yaklaştıran kelime mübalağayı kaldırmaz; onu makbul kılar."}}],
 "relatedNotes": ["tibaq", "tajrid", "kana-wa-akhawatuha", "istiara", "ilm-al-badi"]}

NOTE_K = {
 "id": "madhhab-kalami",
 "title": {"ar": "الْمَذْهَبُ الْكَلَامِيُّ — إِيرَادُ حُجَّةٍ لِلْمَطْلُوبِ عَلَى طَرِيقَةِ أَهْلِ الْكَلَامِ", "en": "The madhhab kalami — a proof for the claim, in the theologians' manner", "tr": "Mezheb-i kelâmî — iddia için kelâmcıların yolu üzere delil"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — المذهب الكلامي: إيراد حجة للمطلوب على طريقة أهل الكلام"],
 "question": {
  "en": ["Does the speech PROVE its claim the way a theologian would — a premise, a consequence, and the conclusion drawn from denying the consequence? لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللَّهُ لَفَسَدَتَا: HAD there been other gods, both would be ruined; they are not; so there are none. That is the MADHHAB KALAMI.",
         "Al-Nabigha argues in three steps: an OATH that leaves no doubt (حَلَفْتُ فَلَمْ أَتْرُكْ لِنَفْسِكَ رِيبَةً), a CONDITIONAL that turns the charge on the accuser (لَئِنْ كُنْتَ قَدْ بُلِّغْتَ عَنِّي خِيَانَةً لَمُبْلِغُكَ الْوَاشِي أَغَشُّ وَأَكْذَبُ), and an ANALOGY that closes it (كَفِعْلِكَ فِي قَوْمٍ أَرَاكَ اصْطَنَعْتَهُمْ).",
         "What does the engine read? The argument's SHAPES: the unreal لَوْ with كَانَ, an إِلَّا inside its premise and a لَ-answer (the reductio); an oath verb with لَيْسَ or a negation after it; the لَئِنْ … لَ- frame; and the كَ + masdar + pronoun that opens an analogy."],
  "tr": ["Söz, iddiasını bir kelâmcı gibi mi İSPAT EDİYOR — öncül, sonuç ve sonucun reddinden çıkan netice? لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللَّهُ لَفَسَدَتَا: başka ilâhlar OLSAYDI ikisi de bozulurdu; bozulmadı; öyleyse yoktur. MEZHEB-İ KELÂMÎ budur.",
         "Nâbiğa üç adımda delil getirir: şüphe bırakmayan YEMİN (حَلَفْتُ فَلَمْ أَتْرُكْ لِنَفْسِكَ رِيبَةً), suçu suçlayana çeviren ŞART (لَئِنْ كُنْتَ قَدْ بُلِّغْتَ عَنِّي خِيَانَةً لَمُبْلِغُكَ الْوَاشِي أَغَشُّ وَأَكْذَبُ) ve kapatan KIYAS (كَفِعْلِكَ فِي قَوْمٍ أَرَاكَ اصْطَنَعْتَهُمْ).",
         "Motor neyi okur? Delilin ŞEKİLLERİNİ: كَانَ'li gayr-i vâki لَوْ, öncülünde bir إِلَّا ve لَ-cevabı (hulf); ardında لَيْسَ yahut nefiy olan yemin fiili; لَئِنْ … لَ- çerçevesi; kıyas açan كَ + masdar + zamir."]},
 "plain": {
  "en": "The madhhab kalami brings a proof for the claim in the theologians' manner — the unreal condition whose consequence is denied (21:22), al-Nabigha's oath, conditional and analogy. The engine reads the shapes of the argument: لَوْ كَانَ … إِلَّا … لَ-, the oath with its negation, لَئِنْ … لَ-, and كَ + masdar.",
  "tr": "Mezheb-i kelâmî iddia için kelâmcıların yolu üzere delil getirir — sonucu reddedilen gayr-i vâki şart (Enbiyâ 22), Nâbiğa'nın yemini, şartı ve kıyası. Motor delilin şekillerini okur: لَوْ كَانَ … إِلَّا … لَ-, nefiyli yemin, لَئِنْ … لَ- ve كَ + masdar."},
 "explanation": {
  "en": "The MADHHAB KALAMI is إِيرَادُ حُجَّةٍ لِلْمَطْلُوبِ عَلَى طَرِيقَةِ أَهْلِ الْكَلَامِ — to bring a proof for what is claimed in the manner of the theologians. The Qur'an: لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللَّهُ لَفَسَدَتَا (21:22) — the ruin of heaven and earth would follow from a plurality of gods; the ruin is not seen; so the plurality is not: the consequence denied proves the premise false. Al-Nabigha's apology to al-Nuʿman argues the same way: he swears and leaves no doubt (حَلَفْتُ فَلَمْ أَتْرُكْ لِنَفْسِكَ رِيبَةً وَلَيْسَ وَرَاءَ اللَّهِ لِلْمَرْءِ مَذْهَبُ); if a treachery was reported, the reporter is the more deceitful (لَئِنْ كُنْتَ قَدْ بُلِّغْتَ عَنِّي خِيَانَةً لَمُبْلِغُكَ الْوَاشِي أَغَشُّ وَأَكْذَبُ); and his praising other kings is as the king's own favour to a people he did not then fault (كَفِعْلِكَ فِي قَوْمٍ أَرَاكَ اصْطَنَعْتَهُمْ فَلَمْ تَرَهُمْ فِي مَدْحِهِمْ لَكَ أَذْنَبُوا) — the analogy closes the case. WHAT THE ENGINE CLAIMS: it does not weigh the argument; it reads its SHAPE off the seats — ShartEngine's لَوْ frame with كَانَ, an إِلَّا inside the premise and the لَ-answer (the reductio); a verb of swearing followed by a negation (لَيْسَ, لَمْ); the لَئِنْ frame with the oath's لَ-answer opening the apodosis; and a clause opened by كَ + a masdar with a pronoun (كَفِعْلِكَ), the analogy — and names the sub from the shape it found.",
  "tr": "MEZHEB-İ KELÂMÎ إِيرَادُ حُجَّةٍ لِلْمَطْلُوبِ عَلَى طَرِيقَةِ أَهْلِ الْكَلَامِ'dır — iddia edilen için kelâmcıların yolu üzere delil getirmek. Kur'an: لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللَّهُ لَفَسَدَتَا (Enbiyâ 22) — göğün ve yerin bozulması ilâhların çokluğundan çıkardı; bozulma görülmüyor; öyleyse çokluk yoktur: reddedilen sonuç öncülü yanlışlar. Nâbiğa'nın Nu'mân'a özrü de böyle delil getirir: yemin eder, şüphe bırakmaz (حَلَفْتُ فَلَمْ أَتْرُكْ لِنَفْسِكَ رِيبَةً وَلَيْسَ وَرَاءَ اللَّهِ لِلْمَرْءِ مَذْهَبُ); bir hıyanet ulaştırıldıysa ulaştıran daha haindir (لَئِنْ كُنْتَ قَدْ بُلِّغْتَ عَنِّي خِيَانَةً لَمُبْلِغُكَ الْوَاشِي أَغَشُّ وَأَكْذَبُ); başka hükümdarları övmesi, kralın suçlu görmediği bir kavme kendi ihsanı gibidir (كَفِعْلِكَ فِي قَوْمٍ أَرَاكَ اصْطَنَعْتَهُمْ فَلَمْ تَرَهُمْ فِي مَدْحِهِمْ لَكَ أَذْنَبُوا) — kıyas dâvâyı kapatır. MOTORUN İDDİASI: delili tartmaz; ŞEKLİNİ koltuklardan okur — ShartEngine'in كَانَ'li لَوْ çerçevesi, öncülde إِلَّا ve لَ-cevabı (hulf); ardında nefiy (لَيْسَ, لَمْ) gelen yemin fiili; apodozu yeminin لَ-cevabıyla açan لَئِنْ çerçevesi; ve zamirli masdar ile كَ'nin açtığı cümle (كَفِعْلِكَ), kıyas — ve alt türü bulduğu şekilden adlandırır."},
 "examples": [
  {"ar": "لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللَّهُ لَفَسَدَتَا", "en": "21:22 — the reductio.", "tr": "Enbiyâ 22 — hulf.", "sourceStory": "talkhis-al-miftah", "sentence": "s17"},
  {"ar": "حَلَفْتُ فَلَمْ أَتْرُكْ لِنَفْسِكَ رِيبَةً * وَلَيْسَ وَرَاءَ اللَّهِ لِلْمَرْءِ مَذْهَبُ", "en": "al-Nabigha — the oath.", "tr": "Nâbiğa — yemin.", "sourceStory": "talkhis-al-miftah", "sentence": "s18"},
  {"ar": "لَئِنْ كُنْتَ قَدْ بُلِّغْتَ عَنِّي خِيَانَةً * لَمُبْلِغُكَ الْوَاشِي أَغَشُّ وَأَكْذَبُ", "en": "al-Nabigha — the conditional.", "tr": "Nâbiğa — şart.", "sourceStory": "talkhis-al-miftah", "sentence": "s19"},
  {"ar": "كَفِعْلِكَ فِي قَوْمٍ أَرَاكَ اصْطَنَعْتَهُمْ * فَلَمْ تَرَهُمْ فِي مَدْحِهِمْ لَكَ أَذْنَبُوا", "en": "al-Nabigha — the analogy.", "tr": "Nâbiğa — kıyas.", "sourceStory": "talkhis-al-miftah", "sentence": "s20"}],
 "commonMistakes": [
  {"wrong": "«Her لَوْ cümlesi mezheb-i kelâmîdir»",
   "right": "«Mezheb-i kelâmî, لَوْ'in bir DELİL kurmasıdır: sonucun reddi öncülü yanlışlar; sıradan bir temenni لَوْ'i delil değildir»",
   "why": {"en": "The definition asks for a proof brought for a claim, not for the particle.", "tr": "Tarif, iddia için getirilen delili ister, harfi değil."}}],
 "relatedNotes": ["mubalagha-maqbula", "in-shartiyya", "kana-wa-akhawatuha", "istithna", "tashbih", "ilm-al-badi"]}

ADD_EN = (" Chapter 64 (lines ~4200-4245, sahifa 145-146) carries the accepted mubalagha (Imru' al-Qays s3, ʿAmr b. al-Ayham s5, Abu Nuwas s7, 24:35 s9, "
          "al-Mutanabbi s11, al-Arrajani s13, the jest s15) and the madhhab kalami (21:22 s17; al-Nabigha s18-s20). The examples s3-s15 and s17 are the "
          "source's printed Arabic. s1, s2, s4, s6, s8, s10, s12, s14, s16 (the definitions, the degrees' conditions and the headings) are RESTORED, NOT "
          "QUOTED: the source carries those steps only in its Ottoman-Turkish gloss, and the Arabic restores the matn's wording in the author's own "
          "idiom. Al-Nabigha's three bayts (s18-s20) are likewise RESTORED: the source names the poet and paraphrases the bayts in Turkish only; the "
          "Arabic is the received text of the bayts the Talkhis cites under the madhhab kalami. Each restored sentence is marked «restored» in its "
          "translation. The examples carry `badi` frames (mubalagha with its degree as `sub` and the acceptance's `receipt`; kalami with the "
          "argument's shape as `sub`).")
ADD_TR = (" Altmış dördüncü bâb (satır ~4200-4245, sahife 145-146) makbul mübalağayı (İmruülkays s3, Amr b. Eyhem s5, Ebû Nüvâs s7, Nûr 35 s9, Mütenebbî "
          "s11, Errecânî s13, şaka s15) ve mezheb-i kelâmîyi (Enbiyâ 22 s17; Nâbiğa s18-s20) taşır. s3-s15 ve s17 örnekleri kaynağın bastığı "
          "Arapçadır. s1, s2, s4, s6, s8, s10, s12, s14, s16 (tarifler, derecelerin şartları ve başlıklar) ALINTI DEĞİL GERİ YAZIMDIR: kaynak o "
          "adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın ifadesini musannifin üslûbunda geri yazar. Nâbiğa'nın üç beyti (s18-s20) "
          "de GERİ YAZIMDIR: kaynak şairi anar ve beyitleri yalnız Türkçe özetler; Arapça, Telhîs'in mezheb-i kelâmî altında andığı beyitlerin mütedâvil "
          "metnidir. Her geri yazılmış cümle tercümesinde «geri yazılmıştır» diye işaretlidir. Örnekler `badi` çerçeveleri taşır (mübalağa: derecesi "
          "`sub`, kabulün alındısı `receipt`; kelâmî: delilin şekli `sub`).")
write_out(64, S, TITLE, ADD_EN, ADD_TR, "4200-4245", GLOSS_ADD, notes=(NOTE_M, NOTE_K),
          related=(("tibaq", ["mubalagha-maqbula"]), ("ilm-al-badi", ["mubalagha-maqbula", "madhhab-kalami"]), ("in-shartiyya", ["madhhab-kalami"]), ("kana-wa-akhawatuha", ["mubalagha-maqbula"])))
report(64, S, GLOSS_ADD, (NOTE_M, NOTE_K))
