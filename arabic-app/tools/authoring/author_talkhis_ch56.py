# -*- coding: utf-8 -*-
"""Author chapter 56 of talkhis-al-miftah — the KINAYA's three kinds (sahifa
134-136, lines ~3890-3940): the kinaya by which a THING is sought, not a quality
or an attribution (the hearts of ʿAmr b. Maʿdikarib's bayt; the human being as a
sum of marks); the kinaya by which a QUALITY is sought — near and plain (the long
sword-belt), near and hidden (the broad nape), far (the much ash, with its rungs);
the kinaya by which an ATTRIBUTION is sought (Ziyad al-Aʿjam's dome; glory between
the two garments); the described thing left unspoken (the hadith of the Muslim,
a taʿrid); Sakkaki's taʿrid, talwih, ramz, imaʾ and ishara; the taʿrid that is a
majaz.

  RESTORED (the source carries the step only in Turkish): s1, s2, s4-s12, s14-s16, s18-s21.
  As printed: the bayt of ʿAmr b. Maʿdikarib (s3), the bayt of Ziyad al-Aʿjam (s13), the
          hadith (s17); the Arabs' sayings inside the restored frames.

Every kinaya carries an authored `kinaya` frame: the SAID (a span of token
indexes), the KIND by what is sought (sifa / mawsuf / nisba), the MEANT (lazim),
the RUNGS the mind climbs (wasait — none for a qariba), Sakkaki's name where the
chapter gives one, and whether the wording carries the pronoun (the tasrih inside
طَوِيلُ النِّجَادِ).
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from talkhis_common import *
import sarf_gen as _sg

A = "aqsam-al-kinaya"; B = "kinaya-qariba-baida"; T = "tarid-talwih-ramz"; K = "kinaya"
TITLE = {"ar": "أَقْسَامُ الْكِنَايَةِ: الْمَطْلُوبُ بِهَا مَوْصُوفٌ أَوْ صِفَةٌ أَوْ نِسْبَةٌ، وَالتَّعْرِيضُ وَالتَّلْوِيحُ وَالرَّمْزُ وَالْإِيمَاءُ",
         "en": "The Kinds of the Kinaya: a Thing, a Quality or an Attribution Sought; the Taʿrid, the Talwih, the Ramz and the Imaʾ",
         "tr": "Kinâyenin Kısımları: Mevsûf, Sıfat yahut Nisbet İstenen; Ta'rîz, Telvîh, Remz ve Îmâ"}
S = []
def kin(full, punct=None, tag=A):
    return tok(full, "kinaya", "noun", [tag, "hal"], "حَالٌ مَنْصُوبٌ — أَيْ حَالَ كَوْنِهِ كِنَايَةً.", "«as a kinaya» — a hal: «being a kinaya».", "«kinâye olarak» — hâl.", punct=punct)
def an_(full, lex, tag, ar, en, tr, segs=None, punct=None):
    return tok(full, lex, "noun", [tag, "huruf-jarr"], ar, en, tr, segments=segs, punct=punct)

# ----------- s1 — the three kinds; the first (RESTORED matn)
S.append({"id": "s1", "translation": {
 "en": "It is of three kinds. The FIRST: that by which something OTHER than a quality or an attribution is sought." + R_EN,
 "tr": "Üç kısımdır. BİRİNCİSİ: kendisiyle sıfat ve nisbetin GAYRI istenendir." + R_TR},
 "tokens": [
  tok("وَهِيَ","hiya","pron",[A, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهِيَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — الْكِنَايَةُ.", "«and it» — the detached pronoun, the mubtada: the kinaya.", "«ve o» — munfasıl zamir, mübtedâ: kinâye.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")]),
  tok("ثَلَاثَةُ","thalatha","noun",[A, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — عَدَدٌ.", "«three» — the khabar; a number, a mudaf.", "«üç» — haber; sayı, muzâf."),
  tok("أَقْسَامٍ","qism","noun",[A, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — تَمْيِيزُ الْعَدَدِ، جَمْعُ قِسْمٍ.", "«kinds» — the number's mudaf ilayh; plural of قِسْم.", "«kısım» — sayının muzâfun ileyhi; قِسْم'in çoğulu.", punct="."),
  tok("الْأُولَى","ula-first","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مُؤَنَّثُ الْأَوَّلِ.", "«the first» — the mubtada; feminine of أَوَّل; the damma estimated.", "«birincisi» — mübtedâ; أَوَّل'in müennesi; zamme takdîrî.", punct=":"),
  tok("الْمَطْلُوبُ","matlub","noun",[A, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ طَلَبَ؛ وَنَائِبُ فَاعِلِهِ غَيْرُ.", "«that which is sought» — the khabar; ism maf'ul of طَلَبَ, whose deputy doer is «other».", "«istenen» — haber; طَلَبَ'nin ism-i mef'ûlü; nâib-i fâili «gayr»."),
  tok("بِهَا","bi","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالْمَطْلُوبِ.", "«by it» — attached to «sought».", "«kendisiyle» — «istenen»e müteallik.",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")]),
  tok("غَيْرُ","ghayr","noun",[A, "naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ لِلْمَطْلُوبِ مَرْفُوعٌ، مُضَافٌ.", "«other than» — the deputy doer of the participle; a mudaf.", "«gayrı» — ism-i mef'ûlün nâib-i fâili; muzâf."),
  tok("صِفَةٍ","sifa","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a quality» — mudaf ilayh.", "«sıfat» — muzâfun ileyh."),
  tok("وَلَا","la-nafiya","part",[A, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor» — the waw joins; la stresses the negation.", "«ve ne de» — vâv atfeder; lâ nefyi pekiştirir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("نِسْبَةٍ","nisba","noun",[A, "atf-nasaq"], "مَعْطُوفٌ عَلَى صِفَةٍ مَجْرُورٌ.", "«an attribution» — joined onto «quality».", "«nisbet» — «sıfat»a matuf.", punct=".")]})

# ----------- s2 — one meaning; the poet named (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "Of it there is what is ONE meaning, as in the saying of ʿAmr b. Maʿdikarib:" + R_EN,
 "tr": "Ondan bir kısmı TEK bir mânâdır; Amr b. Ma'dîkerib'in şu sözü gibi:" + R_TR},
 "tokens": [
  tok("فَمِنْهَا","min","part",[A, "huruf-jarr", "mubtada-khabar"], "الْفَاءُ لِلتَّفْصِيلِ، وَمِنْهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«of it» — the fronted khabar.", "«ondan» — öne alınmış haber.",
      segments=[seg("فَ","fa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")]),
  tok("مَا","ma-mawsula","pron",[A, "mubtada-khabar", "ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعِ مُبْتَدَإٍ مُؤَخَّرٍ.", "«what» — the relative, the delayed mubtada.", "«şu ki» — ism-i mevsûl, sona kalmış mübtedâ."),
  tok("هِيَ","hiya","pron",[A, "ism-mawsul", "mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — وَالْجُمْلَةُ صِلَةٌ.", "«it is» — the mubtada of the sila.", "«o» — sılanın mübtedâsı."),
  tok("مَعْنًى","mana","noun",[A, "mubtada-khabar", "ism-maqsur-manqus"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَقْصُورٌ مُنَوَّنٌ.", "«a meaning» — the khabar; the maqsur with its tanwin.", "«bir mânâ» — haber; tenvinli maksûr."),
  tok("وَاحِدٌ","wahid","noun",[A, "naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«one» — a na't.", "«tek» — na't.", punct="،"),
  tok("كَقَوْلِ","qawl","noun",[A, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ؛ قَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in the saying of» — the kaf of «for instance».", "«sözü gibi» — «meselâ» kâfı.",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")]),
  tok("عَمْرِو","amr-ibn-madikarib","propn",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَمْرُو بْنُ مَعْدِي كَرِبَ الزُّبَيْدِيُّ، الصَّحَابِيُّ الْفَارِسُ.", "«ʿAmr» — mudaf ilayh; ʿAmr b. Maʿdikarib al-Zubaydi, the Companion and horseman.", "«Amr» — muzâfun ileyh; Amr b. Ma'dîkerib ez-Zübeydî, sahâbî ve süvari."),
  tok("بْنِ","ibn","noun",[A, "naat-sifa", "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ، مُضَافٌ — حُذِفَتْ هَمْزَتُهُ بَيْنَ عَلَمَيْنِ.", "«son of» — a na't; its hamza dropped between two names.", "«oğlu» — na't; iki alem arasında hemzesi düşmüş."),
  tok("مَعْدِي","madikarib","propn",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْجُزْءُ الْأَوَّلُ مِنَ الْمُرَكَّبِ الْمَزْجِيِّ مَعْدِي كَرِبَ.", "«Maʿdi» — the first half of the compound name.", "«Ma'dî» — mezcî mürekkeb adın ilk yarısı."),
  tok("كَرِبَ","madikarib","propn",[A, "idafa-definiteness", "mamnu-min-sarf"], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ — الْمُرَكَّبُ الْمَزْجِيُّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«karib» — the second half, built on the fatha: the mixed compound is barred from tanwin.", "«kerib» — fetha üzere ikinci yarı: mezcî mürekkeb gayr-i munsarif.", punct=":")]})

# ----------- s3 — the bayt (as printed)
S.append({"id": "s3", "translation": {
 "en": "«…who strike with every white keen blade, • and who thrust at the GATHERING-PLACES OF RANCOURS» — the hearts.",
 "tr": "«…her beyaz keskin kılıçla vuranlar, • KİNLERİN TOPLANDIĞI YERLERE saplayanlar» — yani kalplere."},
 "kinaya": [kn([5, 6], "mawsuf", {"en": "the HEARTS — the one thing where rancours gather", "tr": "KALPLER — kinlerin toplandığı tek şey"}, wasait=[], head=5)],
 "tokens": [
  tok("الضَّارِبِينَ","darib","noun",[A, "naat-sifa", "ism-fail", "jam-mudhakkar-salim"], "نَعْتٌ لِلْكُمَاةِ فِي الْبَيْتِ قَبْلَهُ مَنْصُوبٌ بِالْيَاءِ — جَمْعُ مُذَكَّرٍ سَالِمٌ؛ اسْمُ فَاعِلِ ضَرَبَ.", "«who strike» — a na't of «the champions» in the bayt before; nasb by the ya of the sound plural.", "«vuranlar» — önceki beyitteki «yiğitler»in na'ti; cem-i müzekker-i sâlim yâsıyla mansub."),
  tok("بِكُلِّ","kull","noun",[A, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ.", "«with every» — a mudaf.", "«her … ile» — muzâf.",
      segments=[seg("بِ","bi","part"), seg("كُلِّ","kull","noun")]),
  tok("أَبْيَضَ","abyad","noun",[A, "idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ عَلَى أَفْعَلَ؛ صِفَةٌ قَامَتْ مَقَامَ مَوْصُوفِهَا: سَيْفٍ.", "«white» — mudaf ilayh in jarr by the fatha (the أَفْعَل of colour); a quality standing for its noun: a sword.", "«beyaz» — fetha ile mecrur muzâfun ileyh (renk أَفْعَل'i); mevsûfunun yerine geçmiş sıfat: kılıç."),
  tok("مِخْذَمٍ","mikhdham","noun",[A, "naat-sifa"], "نَعْتٌ مَجْرُورٌ — اسْمُ آلَةٍ عَلَى مِفْعَلٍ: الْقَاطِعُ.", "«keen» — a na't; the instrument-noun مِفْعَل: the cutter.", "«keskin» — na't; مِفْعَل âlet ismi: kesici.", punct="•"),
  tok("وَالطَّاعِنِينَ","tain","noun",[A, "atf-nasaq", "ism-fail", "jam-mudhakkar-salim"], "الْوَاوُ عَاطِفَةٌ، وَالطَّاعِنِينَ مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ — اسْمُ فَاعِلِ طَعَنَ.", "«and who thrust» — joined; ism fa'il of طَعَنَ.", "«ve saplayanlar» — matuf; طَعَنَ'nin ism-i fâili.",
      segments=[seg("وَ","wa","conj"), seg("الطَّاعِنِينَ","tain","noun")]),
  tok("مَجَامِعَ","majma","noun",[A, "maful-bihi", "idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مَفْعُولٌ بِهِ لِلطَّاعِنِينَ مَنْصُوبٌ، مُضَافٌ — جَمْعُ مَجْمَعٍ عَلَى مَفَاعِلَ.", "«the gathering-places of» — the object of «who thrust»; a mudaf; plural of مَجْمَع on مَفَاعِل.", "«toplanma yerlerine» — «saplayanlar»ın mef'ûlü; muzâf; مَجْمَع'in مَفَاعِل çoğulu."),
  tok("الْأَضْغَانِ","dighn","noun",[A, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ ضِغْنٍ؛ الْمُرَادُ: الْقُلُوبُ — كِنَايَةٌ عَنْ مَوْصُوفٍ.", "«rancours» — mudaf ilayh; plural of ضِغْن. The MEANT: the hearts — a kinaya for a THING.", "«kinler» — muzâfun ileyh; ضِغْن'in çoğulu. KASTEDİLEN: kalpler — MEVSÛFTAN kinâye.", punct=".")]})

# ----------- s4 — a sum of meanings (RESTORED matn)
S.append({"id": "s4", "translation": {
 "en": "And of it there is what is a SUM of meanings, as in our saying, as a kinaya for the human being: «a living thing, upright of stature, broad of nail»." + R_EN,
 "tr": "Ondan bir kısmı da mânâların TOPLAMIDIR; insandan kinâye olarak «boyu dik, tırnağı geniş bir canlı» dememiz gibi." + R_TR},
 "kinaya": [kn([9, 13], "mawsuf", {"en": "the HUMAN BEING — the one thing all three marks belong to", "tr": "İNSAN — üç alâmetin birden ait olduğu tek şey"}, wasait=[], head=9)],
 "tokens": [
  tok("وَمِنْهَا","min","part",[A, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَمِنْهَا خَبَرٌ مُقَدَّمٌ.", "«and of it» — the fronted khabar.", "«ve ondan» — öne alınmış haber.",
      segments=[seg("وَ","wa","conj"), seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")]),
  tok("مَا","ma-mawsula","pron",[A, "mubtada-khabar", "ism-mawsul"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«what» — the delayed mubtada.", "«şu ki» — sona kalmış mübtedâ."),
  tok("هِيَ","hiya","pron",[A, "ism-mawsul", "mubtada-khabar"], "مُبْتَدَأٌ — وَالْجُمْلَةُ صِلَةٌ.", "«it is» — the sila's mubtada.", "«o» — sılanın mübtedâsı."),
  tok("مَجْمُوعُ","majmu","noun",[A, "mubtada-khabar", "idafa-definiteness", "ism-maful"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — اسْمُ مَفْعُولِ جَمَعَ.", "«a sum of» — the khabar; a mudaf; ism maf'ul of جَمَعَ.", "«toplamı» — haber; muzâf; جَمَعَ'nin ism-i mef'ûlü."),
  tok("مَعَانٍ","mana","noun",[A, "idafa-definiteness", "jam-taksir", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — مَنْقُوصٌ مُنَوَّنٌ، جَمْعُ مَعْنًى.", "«meanings» — mudaf ilayh; the manqus plural with its ya dropped under the tanwin.", "«mânâlar» — muzâfun ileyh; tenvin altında yâsı düşmüş menkûs çoğul.", punct="،"),
  tok("كَقَوْلِنَا","qawl","noun",[A, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«as in our saying» — the kaf of «for instance»; «our» the mudaf ilayh.", "«dememiz gibi» — «meselâ» kâfı; «biz» muzâfun ileyh.",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("نَا","pron-1p","pron")]),
  kin("كِنَايَةً"),
  tok("عَنِ","an","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«for» — a kasra where two sakins meet.", "«-den» — iki sâkin buluşunca kesre."),
  tok("الْإِنْسَانِ","insan","noun",[A, "huruf-jarr"], "مَجْرُورٌ — الْمَكْنِيُّ عَنْهُ.", "«the human being» — the thing hinted at.", "«insan» — kendisinden kinâye edilen.", punct=":"),
  tok("حَيٌّ","hayy","noun",[A, "mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — هُوَ حَيٌّ؛ صِفَةٌ مُشَبَّهَةٌ.", "«a living thing» — the khabar of a dropped «he is»; a sifa mushabbaha.", "«bir canlı» — hazfedilmiş «o»nun haberi; sıfat-ı müşebbehe."),
  tok("مُسْتَوِي","mustawi","noun",[A, "naat-sifa", "ism-fail", "idafa-definiteness", "ism-maqsur-manqus"], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، مُضَافٌ — اسْمُ فَاعِلِ اسْتَوَى؛ الْإِضَافَةُ لَفْظِيَّةٌ.", "«upright of» — a na't; the manqus keeps its ya as a mudaf; ism fa'il of اسْتَوَى; the idafa is lafziyya.", "«dik» — na't; menkûs muzâf olunca yâsını tutar; اسْتَوَى'nın ism-i fâili; izâfet lafzî."),
  tok("الْقَامَةِ","qama-stature","noun",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَاعِلٌ فِي الْمَعْنَى.", "«stature» — mudaf ilayh; the doer in meaning.", "«boyu» — muzâfun ileyh; mânâca fâil."),
  tok("عَرِيضُ","arid-wide","noun",[A, "naat-sifa", "sifa-mushabbaha", "idafa-definiteness"], "نَعْتٌ ثَانٍ مَرْفُوعٌ، مُضَافٌ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِيلٍ مِنْ عَرُضَ.", "«broad of» — a second na't; the sifa mushabbaha فَعِيل of عَرُضَ, a mudaf.", "«geniş» — ikinci na't; عَرُضَ'nin فَعِيل sıfat-ı müşebbehesi, muzâf."),
  tok("الْأَظْفَارِ","zufr","noun",[A, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ ظُفْرٍ.", "«nail» — mudaf ilayh; plural of ظُفْر.", "«tırnağı» — muzâfun ileyh; ظُفْر'un çoğulu.", punct=".")]})

# ----------- s5 — the condition (RESTORED matn)
S.append({"id": "s5", "translation": {
 "en": "Its condition is that it be PROPER to the thing hinted at." + R_EN,
 "tr": "Şartı, mekniyyün anha HAS olmasıdır." + R_TR},
 "tokens": [
  tok("وَشَرْطُهَا","shart","noun",[A, "mubtada-khabar", "idafa-definiteness"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَشَرْطُ مُبْتَدَأٌ مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its condition» — the mubtada with its pronoun.", "«ve şartı» — mübtedâ, zamiriyle.",
      segments=[seg("وَ","wa","conj"), seg("شَرْطُ","shart","noun"), seg("هَا","pron-3fs","pron")]),
  tok("الِاخْتِصَاصُ","ikhtisas","noun",[A, "mubtada-khabar", "masdar", "form-viii-verbs"], "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ اخْتَصَّ.", "«being proper» — the khabar; masdar of اخْتَصَّ.", "«has olmak» — haber; اخْتَصَّ'nin masdarı."),
  tok("بِالْمَكْنِيِّ","makni","noun",[A, "huruf-jarr", "ism-maful"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالِاخْتِصَاصِ — اسْمُ مَفْعُولِ كَنَى.", "«to the thing hinted at» — attached to «being proper»; ism maf'ul of كَنَى.", "«mekniyye» — «has olmak»a müteallik; كَنَى'nın ism-i mef'ûlü.",
      segments=[seg("بِ","bi","part"), seg("الْمَكْنِيِّ","makni","noun")]),
  tok("عَنْهُ","an","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — تَمَامُ اسْمِ الْمَكْنِيِّ عَنْهُ.", "«at» — completing «the thing hinted at».", "«kendisinden» — «mekniyyün anh» adının tamamı.",
      segments=[seg("عَنْ","an","part"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s6 — the second (RESTORED matn)
S.append({"id": "s6", "translation": {
 "en": "The SECOND: that by which a QUALITY is sought." + R_EN,
 "tr": "İKİNCİSİ: kendisiyle SIFAT istenendir." + R_TR},
 "tokens": [
  tok("الثَّانِيَةُ","thani","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — مُؤَنَّثُ الثَّانِي.", "«the second» — the mubtada; feminine of ثَانِي.", "«ikincisi» — mübtedâ; ثَانِي'nin müennesi.", punct=":"),
  tok("الْمَطْلُوبُ","matlub","noun",[A, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ.", "«that which is sought» — the khabar.", "«istenen» — haber."),
  tok("بِهَا","bi","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«by it».", "«kendisiyle».",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")]),
  tok("صِفَةٌ","sifa","noun",[A, "naib-al-fail"], "نَائِبُ فَاعِلٍ لِلْمَطْلُوبِ مَرْفُوعٌ.", "«a quality» — the participle's deputy doer.", "«sıfat» — ism-i mef'ûlün nâib-i fâili.", punct=".")]})

# ----------- s7 — near and plain (RESTORED matn; the sayings as printed)
S.append({"id": "s7", "translation": {
 "en": "It is either NEAR, if the passage is without a go-between — and then either PLAIN, as in their saying, as a kinaya for tallness: «long is his sword-belt», and «long of sword-belt»;" + R_EN,
 "tr": "Ya YAKINDIR — intikal vasıtasız olursa — ve o zaman ya AÇIKTIR; boy uzunluğundan kinâye olarak «kılıç kayışı uzundur» ve «kılıç kayışı uzun» demeleri gibi;" + R_TR},
 "kinaya": [kn([16, 17], "sifa", {"en": "TALLNESS — a long belt hangs from a tall body", "tr": "UZUN BOY — uzun kayış uzun bedenden sarkar"}, sub="qariba-wadiha", wasait=[], tasrih=False, head=16),
            kn([18, 19], "sifa", {"en": "TALLNESS — and the pronoun folded into the idafa half-says it", "tr": "UZUN BOY — izâfete katlanmış zamir onu yarı söyler"}, sub="qariba-wadiha", wasait=[], tasrih=True, head=18)],
 "tokens": [
  tok("وَهِيَ","hiya","pron",[B, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهِيَ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")]),
  tok("إِمَّا","imma","part",[B, "atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("قَرِيبَةٌ","qarib","noun",[B, "mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ.", "«near» — the khabar.", "«yakın» — haber."),
  tok("إِنْ","in-shartiyya","part",[B, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer»."),
  tok("كَانَ","kana","verb",[B, "in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ.", "«is» — kana as the shart verb, in the place of jazm.", "«olur» — şart fiili kâne, cezm mahallinde."),
  tok("الِانْتِقَالُ","intiqal","noun",[B, "kana-wa-akhawatuha", "masdar"], "اسْمُ كَانَ مَرْفُوعٌ.", "«the passage» — the ism of kana.", "«intikal» — kânenin ismi."),
  tok("بِلَا","bila","part",[B, "huruf-jarr", "kana-wa-akhawatuha"], "الْبَاءُ جَارَّةٌ وَلَا اسْمٌ بِمَعْنَى غَيْرٍ مَجْرُورٌ مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«without» — the ba over la in the sense of «other than»; the phrase is kana's khabar.", "«-sız» — bâ ve «gayr» mânâsında lâ; ibare kânenin haberi.",
      segments=[seg("بِ","bi","part"), seg("لَا","la-nafiya","part")]),
  tok("وَاسِطَةٍ","wasita","noun",[B, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«a go-between» — mudaf ilayh; the jawab is dropped, shown by what precedes.", "«vasıta» — muzâfun ileyh; cevap hazfedilmiş, öncesi gösterir.", punct="،"),
  tok("وَهِيَ","hiya","pron",[B, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَهِيَ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")]),
  tok("إِمَّا","imma","part",[B, "atf-nasaq"], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("وَاضِحَةٌ","wadih","noun",[B, "mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلِ وَضَحَ.", "«plain» — the khabar; ism fa'il of وَضَحَ.", "«açık» — haber; وَضَحَ'nin ism-i fâili."),
  tok("كَقَوْلِهِمْ","qawl","noun",[B, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ — الْعَرَبُ.", "«as in their saying» — the Arabs'.", "«demeleri gibi» — Arapların.",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِمْ","pron-3mp","pron")]),
  kin("كِنَايَةً", tag=B),
  tok("عَنْ","an","part",[B, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-den»."),
  tok("طُولِ","tul","noun",[B, "huruf-jarr", "idafa-definiteness", "masdar"], "مَجْرُورٌ، مُضَافٌ — مَصْدَرُ طَالَ.", "«the length of» — a mudaf; masdar of طَالَ.", "«uzunluğu» — muzâf; طَالَ'nin masdarı."),
  tok("الْقَامَةِ","qama-stature","noun",[B, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمَكْنِيُّ عَنْهُ: الصِّفَةُ.", "«stature» — mudaf ilayh; the thing hinted at: a quality.", "«boy» — muzâfun ileyh; kendisinden kinâye edilen: sıfat.", punct=":"),
  tok("طَوِيلٌ","tawil-long","noun",[B, "mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِيلٍ مِنْ طَالَ؛ لَا ضَمِيرَ فِيهَا: كِنَايَةٌ صِرْفَةٌ.", "«long» — the fronted khabar; the sifa mushabbaha فَعِيل of طَالَ; NO pronoun in it: a pure kinaya.", "«uzun» — öne alınmış haber; طَالَ'nin فَعِيل sıfat-ı müşebbehesi; içinde zamir YOK: sırf kinâye."),
  tok("نِجَادُهُ","nijad","noun",[B, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — حَمَائِلُ السَّيْفِ.", "«his sword-belt» — the delayed mubtada; the sword's baldric.", "«kılıç kayışı» — sona kalmış mübtedâ; kılıcın hamâili.", punct="،"),
  tok("وَطَوِيلُ","tawil-long","noun",[B, "atf-nasaq", "sifa-mushabbaha", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَطَوِيلُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — هُوَ طَوِيلُ؛ مُضَافٌ إِضَافَةً لَفْظِيَّةً، وَفِيهِ ضَمِيرٌ مُسْتَتِرٌ هُوَ فَاعِلُهُ: فِيهِ نَوْعُ تَصْرِيحٍ.", "«and long of» — the khabar of a dropped «he is»; a lafzi idafa, and a concealed pronoun inside it is its doer: a shade of plain statement.", "«ve … uzun» — hazfedilmiş «o»nun haberi; lafzî izâfet ve içinde fâili olan gizli zamir: bir tür tasrih.",
      segments=[seg("وَ","wa","conj"), seg("طَوِيلُ","tawil-long","noun")]),
  tok("النِّجَادِ","nijad","noun",[B, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ الْفَاعِلُ فِي الْمَعْنَى.", "«sword-belt» — mudaf ilayh; the doer in meaning.", "«kılıç kayışı» — muzâfun ileyh; mânâca fâil.", punct="؛")]})

# ----------- s8 — the second is more specific (RESTORED matn)
S.append({"id": "s8", "translation": {
 "en": "and the second is MORE SPECIFIC, because it contains the pronoun." + R_EN,
 "tr": "ikincisi, zamiri içerdiği için DAHA HUSÛSÎDİR." + R_TR},
 "tokens": [
  tok("وَالثَّانِي","thani","noun",[B, "mubtada-khabar", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — مَنْقُوصٌ.", "«and the second» — the mubtada; a manqus, the damma estimated on its ya.", "«ve ikincisi» — mübtedâ; menkûs, zamme yâ üzerinde takdîrî.",
      segments=[seg("وَ","wa","conj"), seg("الثَّانِي","thani","noun")]),
  tok("أَخَصُّ","akhass","noun",[B, "mubtada-khabar", "ism-tafdil", "doubled-verbs"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ مِنَ الْمُضَاعَفِ خَصَّ: أُدْغِمَ الْمِثْلَانِ.", "«more specific» — the khabar; the ism tafdil of the doubled خَصَّ, its two likes merged.", "«daha husûsî» — haber; muzâaf خَصَّ'nin ism-i tafdîli, iki benzer idgam edilmiş."),
  tok("لِتَضَمُّنِهِ","tadammun","noun",[B, "huruf-jarr", "idafa-definiteness", "masdar", "form-v-verbs"], "اللَّامُ لِلتَّعْلِيلِ، وَتَضَمُّنِ مَجْرُورٌ مُضَافٌ إِلَى الْهَاءِ — مَصْدَرُ تَضَمَّنَ، وَالضَّمِيرُ فَاعِلُهُ فِي الْمَعْنَى.", "«because it contains» — the lam of cause; masdar of تَضَمَّنَ, its pronoun the doer in meaning.", "«içermesi sebebiyle» — ta'lîl lâmı; تَضَمَّنَ'nin masdarı, zamiri mânâca fâili.",
      segments=[seg("لِ","li","part"), seg("تَضَمُّنِ","tadammun","noun"), seg("هِ","pron-3ms","pron")]),
  tok("الضَّمِيرَ","damir","noun",[B, "maful-bihi"], "مَفْعُولٌ بِهِ لِلْمَصْدَرِ مَنْصُوبٌ.", "«the pronoun» — the masdar's object.", "«zamiri» — masdarın mef'ûlü.", punct=".")]})

# ----------- s9 — near and hidden (RESTORED matn; the saying as printed)
S.append({"id": "s9", "translation": {
 "en": "Or HIDDEN, as in their saying, as a kinaya for the dull-witted: «broad of nape»." + R_EN,
 "tr": "Yahut GİZLİDİR; ahmaktan kinâye olarak «ensesi geniş» demeleri gibi." + R_TR},
 "kinaya": [kn([6, 7], "sifa", {"en": "DULL-WITTEDNESS — a broad nape, a large head, and the slowness folk-belief ties to it: the tie is real but hidden", "tr": "AHMAKLIK — geniş ense, büyük baş ve halk inanışının ona bağladığı ağırlık: bağ gerçek ama gizli"}, sub="qariba-khafiyya", wasait=[], tasrih=True, head=6)],
 "tokens": [
  tok("وَإِمَّا","imma","part",[B, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِمَّا حَرْفُ تَفْصِيلٍ.", "«or».", "«yahut».",
      segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("خَفِيَّةٌ","khafi","noun",[B, "atf-nasaq", "sifa-mushabbaha"], "مَعْطُوفٌ عَلَى وَاضِحَةٍ مَرْفُوعٌ.", "«hidden» — joined onto «plain».", "«gizli» — «açık»a matuf."),
  tok("كَقَوْلِهِمْ","qawl","noun",[B, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in their saying».", "«demeleri gibi».",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِمْ","pron-3mp","pron")]),
  kin("كِنَايَةً", tag=B),
  tok("عَنِ","an","part",[B, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-den»."),
  tok("الْأَبْلَهِ","ablah","noun",[B, "huruf-jarr", "sifa-mushabbaha"], "مَجْرُورٌ — أَفْعَلُ الْوَصْفِ، مِنْ بَلِهَ.", "«the dull-witted» — the أَفْعَل of quality, from بَلِهَ.", "«ahmak» — vasıf أَفْعَل'i, بَلِهَ'den.", punct=":"),
  tok("عَرِيضُ","arid-wide","noun",[B, "mubtada-khabar", "sifa-mushabbaha", "idafa-definiteness"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ — صِفَةٌ مُشَبَّهَةٌ.", "«broad of» — the khabar of a dropped «he is»; a mudaf.", "«geniş» — hazfedilmiş «o»nun haberi; muzâf."),
  tok("الْقَفَا","qafa","noun",[B, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«nape» — mudaf ilayh; the maqsur, its kasra estimated.", "«ense» — muzâfun ileyh; maksûr, kesre takdîrî.", punct=".")]})

# ----------- s10 — far (RESTORED matn; the saying as printed)
S.append({"id": "s10", "translation": {
 "en": "Or it is FAR, if the passage is by a go-between, as in their saying, as a kinaya for the hospitable man: «much of ash»." + R_EN,
 "tr": "Yahut UZAKTIR — intikal vasıta ile olursa —; misafirperverden kinâye olarak «külü çok» demeleri gibi." + R_TR},
 "kinaya": [kn([11, 12], "sifa", {"en": "HOSPITALITY — reached only by climbing", "tr": "MİSAFİRPERVERLİK — ancak basamaklarla ulaşılır"}, sub="baida", head=11, tasrih=True,
                wasait=[{"en": "much burning of firewood", "tr": "çok odun yakma"}, {"en": "much cooking", "tr": "çok yemek pişirme"}, {"en": "many eaters", "tr": "çok yiyen"}, {"en": "many guests", "tr": "çok misafir"}])],
 "tokens": [
  tok("وَإِمَّا","imma","part",[B, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَإِمَّا حَرْفُ تَفْصِيلٍ.", "«or».", "«yahut».",
      segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("بَعِيدَةٌ","baid","noun",[B, "atf-nasaq", "sifa-mushabbaha"], "مَعْطُوفٌ عَلَى قَرِيبَةٍ مَرْفُوعٌ.", "«far» — joined onto «near».", "«uzak» — «yakın»a matuf."),
  tok("إِنْ","in-shartiyya","part",[B, "in-shartiyya"], "حَرْفُ شَرْطٍ.", "«if».", "«eğer»."),
  tok("كَانَ","kana","verb",[B, "in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.", "«is» — the shart verb.", "«olur» — şart fiili."),
  tok("الِانْتِقَالُ","intiqal","noun",[B, "kana-wa-akhawatuha", "masdar"], "اسْمُ كَانَ مَرْفُوعٌ.", "«the passage» — the ism of kana.", "«intikal» — kânenin ismi."),
  tok("بِوَاسِطَةٍ","wasita","noun",[B, "huruf-jarr", "kana-wa-akhawatuha"], "جَارٌّ وَمَجْرُورٌ خَبَرُ كَانَ — وَالْجَوَابُ مَحْذُوفٌ.", "«by a go-between» — kana's khabar; the jawab dropped.", "«vasıta ile» — kânenin haberi; cevap hazfedilmiş.",
      segments=[seg("بِ","bi","part"), seg("وَاسِطَةٍ","wasita","noun")], punct="،"),
  tok("كَقَوْلِهِمْ","qawl","noun",[B, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in their saying».", "«demeleri gibi».",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِمْ","pron-3mp","pron")]),
  kin("كِنَايَةً", tag=B),
  tok("عَنِ","an","part",[B, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-den»."),
  tok("الْمِضْيَافِ","midyaf","noun",[B, "huruf-jarr", "sighat-mubalagha"], "مَجْرُورٌ — صِيغَةُ مُبَالَغَةٍ عَلَى مِفْعَالٍ مِنْ ضَافَ: كَثِيرُ الضِّيَافَةِ.", "«the hospitable man» — the intensive مِفْعَال of ضَافَ: much given to hosting.", "«misafirperver» — ضَافَ'nin مِفْعَال mübalağası: çok ağırlayan.", punct=":"),
  tok("هُوَ","huwa","pron",[B, "mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«he» — the mubtada.", "«o» — mübtedâ."),
  tok("كَثِيرُ","kathir","noun",[B, "mubtada-khabar", "sifa-mushabbaha", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِيلٍ مِنْ كَثُرَ؛ الْإِضَافَةُ لَفْظِيَّةٌ.", "«much of» — the khabar; the sifa mushabbaha فَعِيل of كَثُرَ; a lafzi idafa.", "«çok» — haber; كَثُرَ'nin فَعِيل sıfat-ı müşebbehesi; lafzî izâfet."),
  tok("الرَّمَادِ","ramad","noun",[B, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَاعِلٌ فِي الْمَعْنَى: رَمَادُهُ كَثِيرٌ.", "«ash» — mudaf ilayh; the doer in meaning: his ash is much.", "«külü» — muzâfun ileyh; mânâca fâil: külü çoktur.", punct=".")]})

# ----------- s11 — the rungs (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "For the mind passes from the abundance of ash to the abundance of burnt firewood, then to the abundance of cooking, then to the abundance of eaters, then to the abundance of guests, then to the thing meant." + R_EN,
 "tr": "Çünkü zihin külün çokluğundan odun yakmanın çokluğuna, sonra yemek pişirmenin çokluğuna, sonra yiyenlerin çokluğuna, sonra misafirlerin çokluğuna, sonra maksada intikal eder." + R_TR},
 "tokens": [
  tok("فَإِنَّ","inna","part",[B, "inna-wa-akhawatuha"], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for indeed».", "«çünkü».",
      segments=[seg("فَ","fa","conj"), seg("إِنَّ","inna","part")]),
  tok("الذِّهْنَ","dhihn","noun",[B, "inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ.", "«the mind» — the ism of inna.", "«zihin» — innenin ismi."),
  tok("يَنْتَقِلُ","intaqala","verb",[B, "inna-wa-akhawatuha", "form-viii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ؛ وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«passes» — the doer concealed «it»; the clause inna's khabar.", "«intikal eder» — fâil gizli «o»; cümle innenin haberi."),
  tok("مِنْ","min","part",[B, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("كَثْرَةِ","kathra","noun",[B, "huruf-jarr", "idafa-definiteness", "masdar"], "مَجْرُورٌ، مُضَافٌ.", "«the abundance of» — a mudaf.", "«çokluğu» — muzâf."),
  tok("الرَّمَادِ","ramad","noun",[B, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْمَكْنِيُّ بِهِ: الدَّرَجَةُ الْأُولَى.", "«ash» — the said: the first step.", "«kül» — söylenen: ilk basamak."),
  tok("إِلَى","ila","part",[B, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("كَثْرَةِ","kathra","noun",[B, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the abundance of».", "«çokluğuna»."),
  tok("إِحْرَاقِ","ihraq","noun",[B, "idafa-definiteness", "masdar", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ، مُضَافٌ — مَصْدَرُ أَحْرَقَ.", "«burning» — masdar of أَحْرَقَ.", "«yakma» — أَحْرَقَ'nin masdarı."),
  tok("الْحَطَبِ","hatab","noun",[B, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْوَاسِطَةُ الْأُولَى.", "«firewood» — the first rung.", "«odun» — ilk vasıta.", punct="،"),
  tok("ثُمَّ","thumma","conj",[B, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.", "«then» — order with a pause.", "«sonra» — aralıklı tertip."),
  tok("إِلَى","ila","part",[B, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("كَثْرَةِ","kathra","noun",[B, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the abundance of».", "«çokluğuna»."),
  tok("الطَّبْخِ","tabkh","noun",[B, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ — الْوَاسِطَةُ الثَّانِيَةُ.", "«cooking» — the second rung.", "«pişirme» — ikinci vasıta.", punct="،"),
  tok("ثُمَّ","thumma","conj",[B, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  tok("إِلَى","ila","part",[B, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("كَثْرَةِ","kathra","noun",[B, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the abundance of».", "«çokluğuna»."),
  tok("الْآكِلِينَ","akil","noun",[B, "idafa-definiteness", "ism-fail", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — جَمْعُ مُذَكَّرٍ سَالِمٌ؛ الْوَاسِطَةُ الثَّالِثَةُ.", "«eaters» — jarr by the ya of the sound plural; the third rung.", "«yiyenler» — cem-i müzekker-i sâlim yâsıyla mecrur; üçüncü vasıta.", punct="،"),
  tok("ثُمَّ","thumma","conj",[B, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  tok("إِلَى","ila","part",[B, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("كَثْرَةِ","kathra","noun",[B, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the abundance of».", "«çokluğuna»."),
  tok("الضِّيفَانِ","dayf","noun",[B, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ ضَيْفٍ؛ الْوَاسِطَةُ الرَّابِعَةُ.", "«guests» — plural of ضَيْف; the fourth rung.", "«misafirler» — ضَيْف'in çoğulu; dördüncü vasıta.", punct="،"),
  tok("ثُمَّ","thumma","conj",[B, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  tok("إِلَى","ila","part",[B, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْمَقْصُودِ","maqsud","noun",[B, "huruf-jarr", "ism-maful"], "مَجْرُورٌ — الْمَكْنِيُّ عَنْهُ: أَنَّهُ مِضْيَافٌ.", "«the thing meant» — the top of the ladder: that he is hospitable.", "«maksad» — merdivenin tepesi: misafirperver olduğu.", punct=".")]})

# ----------- s12 — the third (RESTORED matn)
S.append({"id": "s12", "translation": {
 "en": "The THIRD: that by which an ATTRIBUTION is sought, as in the saying of Ziyad al-Aʿjam:" + R_EN,
 "tr": "ÜÇÜNCÜSÜ: kendisiyle NİSBET istenendir; Ziyâd el-A'cem'in şu sözü gibi:" + R_TR},
 "tokens": [
  tok("الثَّالِثَةُ","thalith","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the third» — the mubtada.", "«üçüncüsü» — mübtedâ.", punct=":"),
  tok("الْمَطْلُوبُ","matlub","noun",[A, "mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«that which is sought» — the khabar.", "«istenen» — haber."),
  tok("بِهَا","bi","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«by it».", "«kendisiyle».",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")]),
  tok("نِسْبَةٌ","nisba","noun",[A, "naib-al-fail"], "نَائِبُ فَاعِلٍ لِلْمَطْلُوبِ مَرْفُوعٌ.", "«an attribution» — the participle's deputy doer.", "«nisbet» — nâib-i fâil.", punct="،"),
  tok("كَقَوْلِ","qawl","noun",[A, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ، وَقَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in the saying of».", "«sözü gibi».",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")]),
  tok("زِيَادٍ","ziyad","propn",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — زِيَادٌ الْأَعْجَمُ، شَاعِرُ الدَّوْلَةِ الْأُمَوِيَّةِ.", "«Ziyad» — mudaf ilayh; Ziyad al-Aʿjam, the Umayyad-era poet.", "«Ziyâd» — muzâfun ileyh; Ziyâd el-A'cem, Emevî devri şairi."),
  tok("الْأَعْجَمِ","ajam","noun",[A, "naat-sifa"], "نَعْتٌ مَجْرُورٌ — لَقَبُهُ، لِلُكْنَةٍ فِي لِسَانِهِ.", "«al-Aʿjam» — a na't; his byname, for a foreign burr in his speech.", "«el-A'cem» — na't; lakabı, dilindeki pelteklikten.", punct=":")]})

# ----------- s13 — the bayt (as printed)
S.append({"id": "s13", "translation": {
 "en": "«Indeed liberality, manliness and bounty • are IN A DOME PITCHED OVER IBN AL-HASHRAJ».",
 "tr": "«Şüphesiz cömertlik, mertlik ve ihsan • İBNÜ'L-HAŞREC ÜZERİNE KURULMUŞ BİR KUBBEDEDİR»."},
 "kinaya": [kn([4, 9], "nisba", {"en": "these qualities BELONG TO IBN AL-HASHRAJ — placed in the dome pitched over him, not stated of him", "tr": "bu vasıflar İBNÜ'L-HAŞREC'İNDİR — onun üzerine kurulmuş kubbenin içine konmuş, ona söylenmemiş"}, wasait=[], head=4)],
 "tokens": [
  tok("إِنَّ","inna","part",[A, "inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«indeed».", "«şüphesiz»."),
  tok("السَّمَاحَةَ","samaha","noun",[A, "inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ — الصِّفَةُ الْأُولَى.", "«liberality» — the ism of inna; the first quality.", "«cömertlik» — innenin ismi; ilk vasıf."),
  tok("وَالْمُرُوءَةَ","muruwa","noun",[A, "atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ.", "«and manliness» — joined.", "«ve mertlik» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("الْمُرُوءَةَ","muruwa","noun")]),
  tok("وَالنَّدَى","nada-bounty","noun",[A, "atf-nasaq", "ism-maqsur-manqus"], "مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«and bounty» — joined; the maqsur, its fatha estimated.", "«ve ihsan» — matuf; maksûr, fetha takdîrî.",
      segments=[seg("وَ","wa","conj"), seg("النَّدَى","nada-bounty","noun")], punct="•"),
  tok("فِي","fi","part",[A, "huruf-jarr", "inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ: النِّسْبَةُ الْمَكْنِيُّ بِهَا.", "«in» — the jarr phrase is inna's khabar: the attribution said.", "«-de» — câr-mecrûr innenin haberi: söylenen nisbet."),
  tok("قُبَّةٍ","qubba","noun",[A, "huruf-jarr", "jumla-sifa"], "مَجْرُورٌ — وَالْجُمْلَةُ بَعْدَهُ صِفَةٌ لَهُ.", "«a dome» — the clause after it describes it.", "«bir kubbe» — sonraki cümle sıfatı."),
  tok("ضُرِبَتْ","daraba","verb",[A, "jumla-sifa", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — هِيَ؛ ضَرَبَ الْقُبَّةَ: نَصَبَهَا.", "«pitched» — the passive; its deputy doer concealed «it»; to pitch a dome is to set it up.", "«kurulmuş» — meçhûl; nâib-i fâil gizli «o»; kubbeyi vurmak: kurmak.",
      segments=[seg("ضُرِبَ","daraba","verb"), seg("تْ","ta-tanith","part")]),
  tok("عَلَى","ala","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«over».", "«üzerine»."),
  tok("ابْنِ","ibn","noun",[A, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the son of» — a mudaf.", "«oğlu» — muzâf."),
  tok("الْحَشْرَجِ","hashraj","propn",[A, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَبْدُ اللهِ بْنُ الْحَشْرَجِ، أَمِيرُ نَيْسَابُورَ، الْمَمْدُوحُ.", "«al-Hashraj» — mudaf ilayh; ʿAbdallah b. al-Hashraj, governor of Nishapur, the one praised.", "«el-Haşrec» — muzâfun ileyh; Abdullah b. el-Haşrec, Nîşâbur emîri, memdûh.", punct=".")]})

# ----------- s14 — the musannif's explanation (RESTORED)
S.append({"id": "s14", "translation": {
 "en": "For he meant to affirm that these qualities are PROPER to him; so he left the plain statement — «he is proper to them» — for the kinaya, by making them inside a dome pitched over him." + R_EN,
 "tr": "Çünkü bu vasıfların ona HAS olduğunu isbat etmek istedi; «o bunlara mahsustur» diye tasrihi bırakıp, onları üzerine kurulmuş bir kubbenin içinde kılmakla kinâyeye gitti." + R_TR},
 "tokens": [
  tok("فَإِنَّهُ","inna","part",[A, "inna-wa-akhawatuha"], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ، وَالْهَاءُ اسْمُهُ — الشَّاعِرُ.", "«for he» — inna with its ism: the poet.", "«çünkü o» — inne ve ismi: şair.",
      segments=[seg("فَ","fa","conj"), seg("إِنَّ","inna","part"), seg("هُ","pron-3ms","pron")]),
  tok("أَرَادَ","arada","verb",[A, "inna-wa-akhawatuha", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ؛ وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«meant» — the doer concealed «he»; the clause inna's khabar.", "«istedi» — fâil gizli «o»; cümle innenin haberi."),
  tok("أَنْ","an-masdariyya","part",[A, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«to».", "«-mek»."),
  tok("يُثْبِتَ","athbata","verb",[A, "an-masdariyya", "form-iv-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ أَرَادَ.", "«affirm» — nasb by أَنْ; the interpreted masdar is the object of «meant».", "«isbat etmek» — أَنْ ile mansub; müevvel masdar «istedi»nin mef'ûlü."),
  tok("اخْتِصَاصَهُ","ikhtisas","noun",[A, "maful-bihi", "idafa-definiteness", "masdar"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his being proper» — the object, with its pronoun.", "«ona has olmasını» — mef'ûl, zamiriyle.",
      segments=[seg("اخْتِصَاصَ","ikhtisas","noun"), seg("هُ","pron-3ms","pron")]),
  tok("بِهَذِهِ","hadhihi","pron",[A, "huruf-jarr", "asma-al-ishara"], "الْبَاءُ جَارَّةٌ، وَهَذِهِ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«to these» — the demonstrative in the place of jarr.", "«bu … -a» — işaret ismi cer mahallinde.",
      segments=[seg("بِ","bi","part"), seg("هَذِهِ","hadhihi","pron")]),
  tok("الصِّفَاتِ","sifa","noun",[A, "badal", "jam-muannath-salim"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«qualities» — badal of the demonstrative; the sound feminine plural.", "«vasıflar» — işaret isminin bedeli; cem-i müennes-i sâlim.", punct="؛"),
  tok("فَتَرَكَ","taraka","verb",[A, "maful-bihi"], "الْفَاءُ لِلتَّفْرِيعِ، وَتَرَكَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ.", "«so he left» — the doer concealed.", "«böylece bıraktı» — fâil gizli.",
      segments=[seg("فَ","fa","conj"), seg("تَرَكَ","taraka","verb")]),
  tok("التَّصْرِيحَ","tasrih","noun",[A, "maful-bihi", "masdar", "form-ii-verbs"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — مَصْدَرُ صَرَّحَ.", "«the plain statement» — the object; masdar of صَرَّحَ.", "«tasrihi» — mef'ûl; صَرَّحَ'nin masdarı."),
  tok("بِأَنْ","an-masdariyya","part",[A, "huruf-jarr", "an-masdariyya"], "الْبَاءُ جَارَّةٌ، وَأَنْ مَصْدَرِيَّةٌ.", "«by saying».", "«diyerek».",
      segments=[seg("بِ","bi","part"), seg("أَنْ","an-masdariyya","part")]),
  tok("يَقُولَ","qala","verb",[A, "an-masdariyya", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ.", "«say» — nasb by أَنْ.", "«demek» — أَنْ ile mansub.", punct=":"),
  tok("هُوَ","huwa","pron",[A, "mubtada-khabar"], "مُبْتَدَأٌ — مَقُولُ الْقَوْلِ.", "«he» — the mubtada of the quoted speech.", "«o» — mekulü'l-kavlin mübtedâsı."),
  tok("مَخْصُوصٌ","makhsus","noun",[A, "mubtada-khabar", "ism-maful", "doubled-verbs"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ خَصَّ.", "«proper» — the khabar; ism maf'ul of خَصَّ.", "«mahsus» — haber; خَصَّ'nin ism-i mef'ûlü."),
  tok("بِهَا","bi","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«to them».", "«bunlara».",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")], punct="،"),
  tok("إِلَى","ila","part",[A, "huruf-jarr"], "حَرْفُ جَرٍّ — تَرَكَ كَذَا إِلَى كَذَا: عَدَلَ عَنْهُ إِلَيْهِ.", "«for» — «he left X for Y».", "«-e» — «şunu bırakıp buna gitti»."),
  tok("الْكِنَايَةِ","kinaya","noun",[A, "huruf-jarr"], "مَجْرُورٌ.", "«the kinaya».", "«kinâye»."),
  tok("بِأَنْ","an-masdariyya","part",[A, "huruf-jarr", "an-masdariyya"], "الْبَاءُ جَارَّةٌ، وَأَنْ مَصْدَرِيَّةٌ.", "«by».", "«-mekle».",
      segments=[seg("بِ","bi","part"), seg("أَنْ","an-masdariyya","part")]),
  tok("جَعَلَهَا","jaala","verb",[A, "an-masdariyya", "mafulayn"], "فِعْلٌ مَاضٍ فِي مَحَلِّ نَصْبٍ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ، وَهَا مَفْعُولٌ أَوَّلُ.", "«making them» — the doer concealed; «them» the first object.", "«onları kılmak» — fâil gizli; «onları» birinci mef'ûl.",
      segments=[seg("جَعَلَ","jaala","verb"), seg("هَا","pron-3fs","pron")]),
  tok("فِي","fi","part",[A, "huruf-jarr", "mafulayn"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مَفْعُولٌ ثَانٍ.", "«inside» — the jarr phrase is the second object.", "«içinde» — câr-mecrûr ikinci mef'ûl."),
  tok("قُبَّةٍ","qubba","noun",[A, "huruf-jarr"], "مَجْرُورٌ.", "«a dome».", "«bir kubbe»."),
  tok("مَضْرُوبَةٍ","madrub","noun",[A, "naat-sifa", "ism-maful"], "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ.", "«pitched» — a na't.", "«kurulmuş» — na't."),
  tok("عَلَيْهِ","ala","part",[A, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«over him».", "«üzerine».",
      segments=[seg("عَلَيْ","ala","part"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s15 — the sayings (RESTORED frame; the sayings as printed)
S.append({"id": "s15", "translation": {
 "en": "And like it is their saying: «GLORY is between his two garments», and «GENEROSITY is between his two cloaks»." + R_EN,
 "tr": "Onun gibisi de «ŞEREF iki elbisesi arasındadır» ve «KEREM iki hırkası arasındadır» demeleridir." + R_TR},
 "kinaya": [kn([3, 4], "nisba", {"en": "glory is HIS — set between the garments that clothe him, not stated of him", "tr": "şeref ONUNDUR — ona söylenmemiş, onu saran elbiselerin arasına konmuş"}, wasait=[], head=3),
            kn([6, 7], "nisba", {"en": "generosity is HIS", "tr": "kerem ONUNDUR"}, wasait=[], head=6)],
 "tokens": [
  tok("وَمِثْلُهُ","mithl","noun",[A, "mubtada-khabar", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَمِثْلُ مُبْتَدَأٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and like it» — the mubtada.", "«ve onun gibisi» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("مِثْلُ","mithl","noun"), seg("هُ","pron-3ms","pron")]),
  tok("قَوْلُهُمْ","qawl","noun",[A, "mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«their saying» — the khabar.", "«demeleri» — haber.",
      segments=[seg("قَوْلُ","qawl","noun"), seg("هُمْ","pron-3mp","pron")], punct=":"),
  tok("الْمَجْدُ","majd","noun",[A, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — الصِّفَةُ الْمَنْسُوبَةُ.", "«glory» — the mubtada; the quality attributed.", "«şeref» — mübtedâ; nisbet edilen vasıf."),
  tok("بَيْنَ","bayna","noun",[A, "maful-fih", "idafa-definiteness", "mubtada-khabar"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ — خَبَرٌ: النِّسْبَةُ الْمَكْنِيُّ بِهَا.", "«between» — a zarf, the khabar: the attribution said.", "«arasında» — zarf, haber: söylenen nisbet."),
  tok("ثَوْبَيْهِ","thawb","noun",[A, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his two garments» — the dual in jarr by its ya, its nun dropped for the idafa.", "«iki elbisesi» — yâsıyla mecrur tesniye, izâfet için nûnu düşmüş.",
      segments=[seg("ثَوْبَيْ","thawb","noun"), seg("هِ","pron-3ms","pron")], punct="،"),
  tok("وَالْكَرَمُ","karam","noun",[A, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْكَرَمُ مُبْتَدَأٌ.", "«and generosity» — the mubtada.", "«ve kerem» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْكَرَمُ","karam","noun")]),
  tok("بَيْنَ","bayna","noun",[A, "maful-fih", "idafa-definiteness", "mubtada-khabar"], "ظَرْفٌ مَنْصُوبٌ مُضَافٌ — خَبَرٌ.", "«between» — the khabar.", "«arasında» — haber."),
  tok("بُرْدَيْهِ","burd","noun",[A, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنَّى بُرْدٍ.", "«his two cloaks» — the dual of بُرْد.", "«iki hırkası» — بُرْد'ün tesniyesi.",
      segments=[seg("بُرْدَيْ","burd","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s16 — the mawsuf left unspoken (RESTORED matn)
S.append({"id": "s16", "translation": {
 "en": "And in the second and the third kinds the described thing is SOMETIMES NOT MENTIONED — as in his saying ﷺ, as a taʿrid at one who harms the Muslims:" + R_EN,
 "tr": "İkinci ve üçüncü kısımda mevsûf BAZEN ZİKREDİLMEZ — Müslümanlara eziyet edene ta'rîz olarak Peygamber'in ﷺ şu sözü gibi:" + R_TR},
 "tokens": [
  tok("وَقَدْ","qad","part",[T, "qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ لِلتَّقْلِيلِ.", "«and sometimes».", "«ve bazen».",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("لَا","la-nafiya","part",[T], "حَرْفُ نَفْيٍ.", "«not».", "«-mez»."),
  tok("يُذْكَرُ","dhakara","verb",[T, "naib-al-fail", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is mentioned» — the passive.", "«zikredilir» — meçhûl."),
  tok("الْمَوْصُوفُ","mawsuf","noun",[T, "naib-al-fail", "ism-maful"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the described thing» — the deputy doer.", "«mevsûf» — nâib-i fâil."),
  tok("فِي","fi","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْقِسْمَيْنِ","qism","noun",[T, "huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«the two kinds» — the dual.", "«iki kısım» — tesniye."),
  tok("الْأَخِيرَيْنِ","akhir-last","noun",[T, "naat-sifa", "al-muthanna"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ.", "«the last» — a na't in the dual.", "«son» — tesniye na't.", punct="،"),
  kaq(T, "كَقَوْلِهِ", punct=None),
  saw(T, punct=None),
  tok("تَعْرِيضًا","tarid","noun",[T, "maful-lah", "masdar", "form-ii-verbs"], "مَفْعُولٌ لَهُ مَنْصُوبٌ — أَوْ حَالٌ؛ مَصْدَرُ عَرَّضَ: أَنْ يُقَالَ الشَّيْءُ وَيُرَادَ غَيْرُهُ إِشَارَةً.", "«as a taʿrid» — the object of purpose (or a hal); masdar of عَرَّضَ: to say a thing and glance at another.", "«ta'rîz olarak» — mef'ûlün leh (yahut hâl); عَرَّضَ'nin masdarı: bir şeyi söyleyip başkasına dokundurmak."),
  tok("لِمَنْ","man-mawsula","pron",[T, "huruf-jarr", "ism-mawsul"], "اللَّامُ جَارَّةٌ، وَمَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«at the one who» — the relative in the place of jarr.", "«… edene» — ism-i mevsûl cer mahallinde.",
      segments=[seg("لِ","li","part"), seg("مَنْ","man-mawsula","pron")]),
  tok("يُؤْذِي","adha-verb","verb",[T, "ism-mawsul", "form-iv-verbs", "naqis-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ؛ وَالْجُمْلَةُ صِلَةٌ.", "«harms» — raf' estimated on the ya; the doer concealed; the clause is the sila.", "«eziyet eder» — zamme yâ üzerinde takdîrî; fâil gizli; cümle sıla."),
  tok("الْمُسْلِمِينَ","muslim","noun",[T, "maful-bihi", "jam-mudhakkar-salim"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ.", "«the Muslims» — the object; nasb by the ya.", "«Müslümanlara» — mef'ûl; yâ ile mansub.", punct=":")]})

# ----------- s17 — the hadith (as printed)
S.append({"id": "s17", "translation": {
 "en": "«The MUSLIM is he from whose tongue and hand the Muslims are safe» — a kinaya denying the harmer the quality of Islam, with no one named.",
 "tr": "«MÜSLÜMAN, Müslümanların dilinden ve elinden selâmette olduğu kimsedir» — eziyet edenden İslâm vasfını nefyeden bir kinâye; kimse anılmadan."},
 "kinaya": [kn([0, 6], "nisba", {"en": "the HARMER is no true Muslim — the quality is denied him without his being named: the taʿrid", "tr": "EZİYET EDEN gerçek Müslüman değildir — vasıf, adı anılmadan ondan nefyedilir: ta'rîz"}, wasait=[], sakkaki="tarid", mawsuf=False, head=0)],
 "tokens": [
  tok("الْمُسْلِمُ","muslim","noun",[T, "mubtada-khabar", "ism-fail"], "مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ فَاعِلِ أَسْلَمَ.", "«the Muslim» — the mubtada.", "«Müslüman» — mübtedâ."),
  tok("مَنْ","man-mawsula","pron",[T, "mubtada-khabar", "ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعِ خَبَرٍ.", "«he who» — the relative, the khabar.", "«… kimsedir» — ism-i mevsûl, haber."),
  tok("سَلِمَ","salima","verb",[T, "ism-mawsul", "fail"], "فِعْلٌ مَاضٍ — وَالْجُمْلَةُ صِلَةٌ.", "«are safe» — the sila.", "«selâmette oldu» — sıla."),
  tok("الْمُسْلِمُونَ","muslim","noun",[T, "fail", "jam-mudhakkar-salim"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ.", "«the Muslims» — the doer; raf' by the waw.", "«Müslümanlar» — fâil; vâv ile merfû."),
  tok("مِنْ","min","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("لِسَانِهِ","lisan","noun",[T, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عَائِدُ الصِّلَةِ.", "«his tongue» — the sila's returning pronoun.", "«dili» — sılanın âidi.",
      segments=[seg("لِسَانِ","lisan","noun"), seg("هِ","pron-3ms","pron")]),
  tok("وَيَدِهِ","yad","noun",[T, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَيَدِ مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his hand» — joined.", "«ve eli» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("يَدِ","yad","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s18 — Sakkaki's names (RESTORED)
S.append({"id": "s18", "translation": {
 "en": "Sakkaki divided the kinaya into TAʿRID, TALWIH, RAMZ, IMAʾ and ISHARA." + R_EN,
 "tr": "Sekkâkî kinâyeyi TA'RÎZ, TELVÎH, REMZ, ÎMÂ ve İŞÂRET diye böldü." + R_TR},
 "tokens": [
  tok("وَقَسَّمَ","qassama","verb",[T, "fail", "form-ii-verbs", "maful-bihi"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَسَّمَ فِعْلٌ مَاضٍ مِنَ الثَّانِي.", "«and divided» — Form II.", "«ve böldü» — II. bâb.",
      segments=[seg("وَ","wa","conj"), seg("قَسَّمَ","qassama","verb")]),
  tok("السَّكَّاكِيُّ","sakkaki","noun",[T, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Sakkaki» — the doer.", "«Sekkâkî» — fâil."),
  tok("الْكِنَايَةَ","kinaya","noun",[T, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the kinaya» — the object.", "«kinâyeyi» — mef'ûl."),
  tok("إِلَى","ila","part",[T, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«into».", "«-e»."),
  tok("تَعْرِيضٍ","tarid","noun",[T, "huruf-jarr", "masdar"], "مَجْرُورٌ.", "«taʿrid» — the glancing hint.", "«ta'rîz» — dokundurma."),
  tok("وَتَلْوِيحٍ","talwih","noun",[T, "atf-nasaq", "masdar"], "مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ لَوَّحَ: أَشَارَ مِنْ بَعِيدٍ.", "«and talwih» — masdar of لَوَّحَ: to signal from afar.", "«ve telvîh» — لَوَّحَ'nin masdarı: uzaktan işaret etmek.",
      segments=[seg("وَ","wa","conj"), seg("تَلْوِيحٍ","talwih","noun")]),
  tok("وَرَمْزٍ","ramz","noun",[T, "atf-nasaq", "masdar"], "مَعْطُوفٌ مَجْرُورٌ — الْإِشَارَةُ الْخَفِيَّةُ بِالشَّفَةِ أَوِ الْحَاجِبِ.", "«and ramz» — the hidden sign, with lip or brow.", "«ve remz» — dudak yahut kaşla gizli işaret.",
      segments=[seg("وَ","wa","conj"), seg("رَمْزٍ","ramz","noun")]),
  tok("وَإِيمَاءٍ","ima","noun",[T, "atf-nasaq", "masdar", "form-iv-verbs"], "مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ أَوْمَأَ.", "«and imaʾ» — masdar of أَوْمَأَ.", "«ve îmâ» — أَوْمَأَ'nin masdarı.",
      segments=[seg("وَ","wa","conj"), seg("إِيمَاءٍ","ima","noun")]),
  tok("وَإِشَارَةٍ","ishara","noun",[T, "atf-nasaq", "masdar", "form-iv-verbs"], "مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ أَشَارَ.", "«and ishara» — masdar of أَشَارَ.", "«ve işâret» — أَشَارَ'nin masdarı.",
      segments=[seg("وَ","wa","conj"), seg("إِشَارَةٍ","ishara","noun")], punct=".")]})

# ----------- s19 — which name fits which (RESTORED matn)
S.append({"id": "s19", "translation": {
 "en": "The fitting name for the INCIDENTAL kinaya is taʿrid; for the others — if the go-betweens are many, talwih; if few, with hiddenness, ramz; and without hiddenness, imaʾ and ishara." + R_EN,
 "tr": "ARAZÎ olan kinâyeye uygun ad ta'rîzdir; diğerleri için — vasıtalar çoksa telvîh; azsa ve gizlilikle remz; gizliliksiz îmâ ve işârettir." + R_TR},
 "tokens": [
  tok("فَالْمُنَاسِبُ","munasib","noun",[T, "mubtada-khabar", "ism-fail", "form-iii-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْمُنَاسِبُ مُبْتَدَأٌ — اسْمُ فَاعِلِ نَاسَبَ.", "«the fitting name» — the mubtada; ism fa'il of نَاسَبَ.", "«uygun olan» — mübtedâ; نَاسَبَ'nin ism-i fâili.",
      segments=[seg("فَ","fa","conj"), seg("الْمُنَاسِبُ","munasib","noun")]),
  tok("لِلْعَرَضِيَّةِ","aradi","noun",[T, "huruf-jarr", "ism-mansub"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالْمُنَاسِبِ — الْكِنَايَةُ الْعَرَضِيَّةُ: الَّتِي تُسَاقُ لِغَرَضٍ عَارِضٍ فِي مُخَاطَبٍ.", "«for the incidental one» — the kinaya driven at a passing purpose in a hearer.", "«arazî olana» — bir muhataba yönelik geçici bir garazla söylenen kinâye.",
      segments=[seg("لِ","li","part"), seg("الْعَرَضِيَّةِ","aradi","noun")]),
  tok("التَّعْرِيضُ","tarid","noun",[T, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«taʿrid» — the khabar.", "«ta'rîz» — haber.", punct="،"),
  tok("وَلِغَيْرِهَا","ghayr","noun",[T, "huruf-jarr", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ جَارَّةٌ، وَغَيْرِ مَجْرُورٌ مُضَافٌ إِلَى الْهَاءِ — وَالْخَبَرُ الْمُبْتَدَأُ الْآتِي.", "«and for the others» — the following nouns are its khabar.", "«ve diğerleri için» — haber, gelecek isimler.",
      segments=[seg("وَ","wa","conj"), seg("لِ","li","part"), seg("غَيْرِ","ghayr","noun"), seg("هَا","pron-3fs","pron")]),
  tok("إِنْ","in-shartiyya","part",[T, "in-shartiyya"], "حَرْفُ شَرْطٍ.", "«if».", "«eğer»."),
  tok("كَثُرَتِ","kathura","verb",[T, "in-shartiyya", "fail"], "فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — مِنْ بَابِ حَسُنَ.", "«are many» — the shart verb; the feminine ta with its kasra; of the bab of حَسُنَ.", "«çok olursa» — şart fiili; te'nis tâsı kesreli; حَسُنَ bâbından.",
      segments=[seg("كَثُرَ","kathura","verb"), seg("تِ","ta-tanith","part")]),
  tok("الْوَسَائِطُ","wasita","noun",[T, "fail", "jam-taksir", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ وَاسِطَةٍ عَلَى فَعَائِلَ.", "«the go-betweens» — the doer; plural of وَاسِطَة.", "«vasıtalar» — fâil; وَاسِطَة'nin çoğulu."),
  tok("التَّلْوِيحُ","talwih","noun",[T, "mubtada-khabar", "in-shartiyya"], "مُبْتَدَأٌ مَرْفُوعٌ، خَبَرُهُ لِغَيْرِهَا الْمُتَقَدِّمُ — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ فِي الْمَعْنَى.", "«talwih» — the mubtada whose khabar is the fronted «for the others»; the sentence is the jawab in meaning.", "«telvîh» — haberi öne alınmış «diğerleri için» olan mübtedâ; cümle mânâca şartın cevabı.", punct="،"),
  tok("وَإِنْ","in-shartiyya","part",[T, "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».",
      segments=[seg("وَ","wa","conj"), seg("إِنْ","in-shartiyya","part")]),
  tok("قَلَّتْ","qalla","verb",[T, "in-shartiyya", "doubled-verbs"], "فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ — مُضَاعَفٌ؛ وَالْفَاعِلُ مُسْتَتِرٌ — هِيَ، الْوَسَائِطُ.", "«are few» — the doubled shart verb; the doer concealed «they», the go-betweens.", "«az olursa» — muzâaf şart fiili; fâil gizli «onlar», vasıtalar.",
      segments=[seg("قَلَّ","qalla","verb"), seg("تْ","ta-tanith","part")]),
  tok("مَعَ","maa","noun",[T, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with».", "«ile»."),
  tok("خَفَاءٍ","khafaa","noun",[T, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ خَفِيَ.", "«hiddenness» — masdar of خَفِيَ.", "«gizlilik» — خَفِيَ'nin masdarı."),
  tok("الرَّمْزُ","ramz","noun",[T, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ، خَبَرُهُ لِغَيْرِهَا.", "«ramz» — the mubtada.", "«remz» — mübtedâ.", punct="،"),
  tok("وَبِلَا","bila","part",[T, "huruf-jarr", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَبِلَا: الْبَاءُ جَارَّةٌ وَلَا بِمَعْنَى غَيْرٍ.", "«and without».", "«ve … -sız».",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("لَا","la-nafiya","part")]),
  tok("خَفَاءٍ","khafaa","noun",[T, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«hiddenness».", "«gizlilik»."),
  tok("الْإِيمَاءُ","ima","noun",[T, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«imaʾ» — the mubtada.", "«îmâ» — mübtedâ."),
  tok("وَالْإِشَارَةُ","ishara","noun",[T, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْإِشَارَةُ مَعْطُوفٌ مَرْفُوعٌ.", "«and ishara» — joined.", "«ve işâret» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("الْإِشَارَةُ","ishara","noun")], punct=".")]})

# ----------- s20 — the taʿrid that is a majaz (RESTORED matn)
S.append({"id": "s20", "translation": {
 "en": "The taʿrid may sometimes be a MAJAZ, as in your saying «You have hurt me, so you shall know», meaning a person beside the one addressed, and not him." + R_EN,
 "tr": "Ta'rîz bazen MECAZ olur; muhatabı değil onun yanındaki bir insanı kastederek «Bana eziyet ettin, yakında bileceksin» demen gibi." + R_TR},
 "tokens": [
  tok("وَقَدْ","qad","part",[T, "qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ لِلتَّقْلِيلِ.", "«and sometimes».", "«ve bazen».",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يَكُونُ","kana","verb",[T, "kana-wa-akhawatuha", "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«is» — kana.", "«olur» — kâne."),
  tok("التَّعْرِيضُ","tarid","noun",[T, "kana-wa-akhawatuha"], "اسْمُ يَكُونُ مَرْفُوعٌ.", "«the taʿrid» — the ism of kana.", "«ta'rîz» — kânenin ismi."),
  tok("مَجَازًا","majaz","noun",[T, "kana-wa-akhawatuha"], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«a majaz» — the khabar of kana.", "«mecaz» — kânenin haberi.", punct="،"),
  kaq(T, "كَقَوْلِكَ", "pron-2ms", punct=":"),
  tok("آذَيْتَنِي","adha-verb","verb",[T, "form-iv-verbs", "naqis-verbs", "maful-bihi", "fail"], "فِعْلٌ مَاضٍ مِنَ الرَّابِعِ نَاقِصٌ، وَالتَّاءُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«you have hurt me» — Form IV naqis; the ta its doer, the guarding nun, the ya its object.", "«bana eziyet ettin» — IV. bâb nâkıs; tâ fâil, vikâye nûnu, yâ mef'ûl.",
      segments=[seg("آذَيْ","adha-verb","verb"), seg("تَ","pron-2ms","pron"), seg("نِي","pron-1s","pron")]),
  tok("فَسَتَعْرِفُ","arafa","verb",[T, "mudari-marfu", "fail"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَالسِّينُ لِلِاسْتِقْبَالِ، وَتَعْرِفُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا — أَنْتَ.", "«so you shall know» — the sin of the future; the doer «you» concealed of necessity.", "«yakında bileceksin» — istikbal sîni; fâil vücûben gizli «sen».",
      segments=[seg("فَ","fa","conj"), seg("سَ","sa","part"), seg("تَعْرِفُ","arafa","verb")], punct="،"),
  tok("مُرِيدًا","murid","noun",[T, "hal", "ism-fail", "form-iv-verbs"], "حَالٌ مَنْصُوبٌ مِنْ فَاعِلِ الْقَوْلِ — اسْمُ فَاعِلِ أَرَادَ.", "«meaning» — a hal of the speaker; ism fa'il of أَرَادَ.", "«kastederek» — söyleyenin hâli; أَرَادَ'nin ism-i fâili."),
  tok("إِنْسَانًا","insan","noun",[T, "maful-bihi"], "مَفْعُولٌ بِهِ لِمُرِيدًا مَنْصُوبٌ.", "«a person» — the participle's object.", "«bir insanı» — ism-i fâilin mef'ûlü."),
  tok("مَعَ","maa","noun",[T, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«beside».", "«yanında»."),
  tok("الْمُخَاطَبِ","mukhatab","noun",[T, "idafa-definiteness", "ism-maful", "form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولِ خَاطَبَ.", "«the one addressed» — ism maf'ul of خَاطَبَ.", "«muhatab» — خَاطَبَ'nin ism-i mef'ûlü."),
  tok("دُونَهُ","duna","noun",[T, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَيْ لَا الْمُخَاطَبَ.", "«and not him» — «short of him»: the addressee not meant.", "«o değil» — «onun berisinde»: muhatab kastedilmemiş.",
      segments=[seg("دُونَ","duna","noun"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s21 — both meant: a kinaya (RESTORED matn)
S.append({"id": "s21", "translation": {
 "en": "And if you mean them both, it is a KINAYA; and in both cases a clue is indispensable." + R_EN,
 "tr": "İkisini birden kastedersen KİNÂYE olur; iki hâlde de karîne şarttır." + R_TR},
 "tokens": [
  tok("وَإِنْ","in-shartiyya","part",[T, "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if».", "«ve eğer».",
      segments=[seg("وَ","wa","conj"), seg("إِنْ","in-shartiyya","part")]),
  tok("أَرَدْتَهُمَا","arada","verb",[T, "in-shartiyya", "form-iv-verbs", "hollow-verbs", "maful-bihi"], "فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، حُذِفَتْ أَلِفُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ فَاعِلٌ، وَهُمَا مَفْعُولٌ بِهِ.", "«you mean them both» — the hollow shart verb, its alif dropped; the ta its doer; «them both» its object.", "«ikisini kastedersen» — ecvef şart fiili, elifi düşmüş; tâ fâil; «ikisini» mef'ûl.",
      segments=[seg("أَرَدْ","arada","verb"), seg("تَ","pron-2ms","pron"), seg("هُمَا","pron-3d","pron")]),
  tok("جَمِيعًا","jami","noun",[T, "hal"], "حَالٌ مَنْصُوبٌ — أَوْ تَوْكِيدٌ.", "«both together» — a hal, or a tawkid.", "«birlikte» — hâl, yahut te'kîd."),
  tok("كَانَ","kana","verb",[T, "in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ — هُوَ، الْقَوْلُ.", "«it is» — kana as the jawab; its ism concealed «it», the saying.", "«olur» — cevap olarak kâne; ismi gizli «o», söz."),
  tok("كِنَايَةً","kinaya","noun",[T, "kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a kinaya» — the khabar of kana.", "«kinâye» — kânenin haberi.", punct="؛"),
  tok("وَلَا","la-nafiya-lil-jins","part",[T, "la-nafiya-lil-jins"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«and no» — the genus-denying la.", "«ve hiç» — cinsi nefyeden lâ.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya-lil-jins","part")]),
  tok("بُدَّ","budd","noun",[T, "la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ — لَا بُدَّ: لَا مَفَرَّ.", "«escape» — the ism of la, built on the fatha: «there is no avoiding».", "«çare» — lânın ismi, fetha üzere mebnî: «kaçınılmaz»."),
  tok("فِيهِمَا","fi","part",[T, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — فِي الصُّورَتَيْنِ.", "«in both» — in the two cases.", "«ikisinde» — iki sûrette.",
      segments=[seg("فِي","fi","part"), seg("هِمَا","pron-3d","pron")]),
  tok("مِنْ","min","part",[T, "huruf-jarr", "la-nafiya-lil-jins"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ لَا.", "«of» — the jarr phrase is la's khabar.", "«-den» — câr-mecrûr lânın haberi."),
  tok("قَرِينَةٍ","qarina","noun",[T, "huruf-jarr"], "مَجْرُورٌ.", "«a clue».", "«bir karîne».", punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "hiya": find_gloss("hiya"), "thalatha": find_gloss("thalatha"), "qism": find_gloss("qism"),
 "ula-first": G("ula-first", "الْأُولَى", "أ و ل", "noun", "the first (feminine of أَوَّل)", "birincisi (أَوَّل'in müennesi)", 2),
 "matlub": G("matlub", "مَطْلُوب", "ط ل ب", "noun", "sought, what is sought (ism maf'ul of طَلَبَ)", "istenen, matlûb (طَلَبَ'nin ism-i mef'ûlü)", 3),
 "bi": find_gloss("bi"), "ghayr": find_gloss("ghayr"), "sifa": find_gloss("sifa"), "la-nafiya": find_gloss("la-nafiya"), "nisba": find_gloss("nisba"),
 "min": find_gloss("min"), "ma-mawsula": find_gloss("ma-mawsula"), "mana": find_gloss("mana"), "wahid": find_gloss("wahid"), "qawl": find_gloss("qawl"),
 "amr-ibn-madikarib": G("amr-ibn-madikarib", "عَمْرُو بْنُ مَعْدِي كَرِبَ", None, "propn", "ʿAmr b. Maʿdikarib al-Zubaydi (d. c. 21/642), Companion, horseman and poet", "Amr b. Ma'dîkerib ez-Zübeydî (ö. yak. 21/642), sahâbî, süvari ve şair", 6),
 "ibn": find_gloss("ibn"),
 "madikarib": G("madikarib", "مَعْدِي كَرِبَ", None, "propn", "Maʿdikarib — a mixed compound name, barred from tanwin", "Ma'dîkerib — mezcî mürekkeb ad, gayr-i munsarif", 6),
 "darib": G("darib", "ضَارِب", "ض ر ب", "noun", "one who strikes (ism fa'il of ضَرَبَ)", "vuran (ضَرَبَ'nin ism-i fâili)", 3),
 "kull": find_gloss("kull"), "abyad": find_gloss("abyad"),
 "mikhdham": G("mikhdham", "مِخْذَم", "خ ذ م", "noun", "a keen, cutting blade (instrument-noun of خَذَمَ, to cut)", "keskin, kesici kılıç (خَذَمَ'nin âlet ismi)", 6),
 "tain": G("tain", "طَاعِن", "ط ع ن", "noun", "one who thrusts (a spear) (ism fa'il of طَعَنَ)", "(mızrak) saplayan (طَعَنَ'nin ism-i fâili)", 4),
 "majma": G("majma", "مَجْمَع", "ج م ع", "noun", "gathering-place (noun of place of جَمَعَ)", "toplanma yeri (جَمَعَ'nin mekân ismi)", 4, plural="مَجَامِع"),
 "dighn": G("dighn", "ضِغْن", "ض غ ن", "noun", "rancour, hidden hatred", "kin, gizli düşmanlık", 5, plural="أَضْغَان"),
 "majmu": G("majmu", "مَجْمُوع", "ج م ع", "noun", "sum, total (ism maf'ul of جَمَعَ)", "toplam, mecmû (جَمَعَ'nin ism-i mef'ûlü)", 3),
 "kinaya": find_gloss("kinaya"), "an": find_gloss("an"), "insan": find_gloss("insan"), "hayy": find_gloss("hayy"),
 "mustawi": G("mustawi", "مُسْتَوٍ (الْمُسْتَوِي)", "س و ي", "noun", "upright, even, straight (ism fa'il of اسْتَوَى)", "dik, düz (اسْتَوَى'nın ism-i fâili)", 4),
 "qama-stature": G("qama-stature", "قَامَة", "ق و م", "noun", "stature, height of the body", "boy, kamet", 3),
 "arid-wide": G("arid-wide", "عَرِيض", "ع ر ض", "noun", "broad, wide (sifa mushabbaha of عَرُضَ)", "geniş (عَرُضَ'nin sıfat-ı müşebbehesi)", 3),
 "zufr": find_gloss("zufr"), "shart": find_gloss("shart"),
 "ikhtisas": G("ikhtisas", "اِخْتِصَاص", "خ ص ص", "noun", "being proper to, exclusiveness (masdar of اخْتَصَّ)", "has olma, ihtisas (اخْتَصَّ'nin masdarı)", 5),
 "makni": find_gloss("makni"), "thani": find_gloss("thani"), "imma": find_gloss("imma"), "qarib": find_gloss("qarib"), "in-shartiyya": find_gloss("in-shartiyya"),
 "kana": find_gloss("kana"), "intiqal": find_gloss("intiqal"), "bila": find_gloss("bila"), "wasita": find_gloss("wasita"),
 "wadih": G("wadih", "وَاضِح", "و ض ح", "noun", "plain, clear (ism fa'il of وَضَحَ)", "açık, vâzıh (وَضَحَ'nin ism-i fâili)", 3),
 "tul": find_gloss("tul"),
 "tawil-long": G("tawil-long", "طَوِيل", "ط و ل", "noun", "long, tall (sifa mushabbaha of طَالَ)", "uzun (طَالَ'nin sıfat-ı müşebbehesi)", 2),
 "nijad": G("nijad", "نِجَاد", "ن ج د", "noun", "sword-belt, baldric", "kılıç kayışı, hamâil", 6),
 "akhass": G("akhass", "أَخَصّ", "خ ص ص", "noun", "more specific (ism tafdil of the doubled خَصَّ)", "daha husûsî (muzâaf خَصَّ'nin ism-i tafdîli)", 5),
 "tadammun": G("tadammun", "تَضَمُّن", "ض م ن", "noun", "containing, implication (masdar of تَضَمَّنَ)", "içerme, tazammun (تَضَمَّنَ'nin masdarı)", 5),
 "li": find_gloss("li"),
 "damir": G("damir", "ضَمِير", "ض م ر", "noun", "pronoun", "zamir", 2, plural="ضَمَائِر"),
 "khafi": find_gloss("khafi"),
 "ablah": G("ablah", "أَبْلَه", "ب ل ه", "noun", "dull-witted, simple (the أَفْعَل of quality)", "ahmak, ebleh (vasıf أَفْعَل'i)", 5),
 "qafa": G("qafa", "قَفًا (الْقَفَا)", "ق ف و", "noun", "nape of the neck", "ense, kafa", 4),
 "baid": find_gloss("baid"),
 "midyaf": G("midyaf", "مِضْيَاف", "ض ي ف", "noun", "very hospitable (the intensive مِفْعَال of ضَافَ)", "misafirperver (ضَافَ'nin مِفْعَال mübalağası)", 6),
 "huwa": find_gloss("huwa"), "kathir": find_gloss("kathir"),
 "ramad": G("ramad", "رَمَاد", "ر م د", "noun", "ash", "kül", 3),
 "inna": find_gloss("inna"), "dhihn": find_gloss("dhihn"), "intaqala": find_gloss("intaqala"), "kathra": find_gloss("kathra"), "ila": find_gloss("ila"),
 "ihraq": G("ihraq", "إِحْرَاق", "ح ر ق", "noun", "burning (masdar of أَحْرَقَ)", "yakma (أَحْرَقَ'nin masdarı)", 4),
 "hatab": G("hatab", "حَطَب", "ح ط ب", "noun", "firewood", "odun", 3),
 "thumma": find_gloss("thumma"),
 "tabkh": G("tabkh", "طَبْخ", "ط ب خ", "noun", "cooking (masdar of طَبَخَ)", "pişirme (طَبَخَ'nin masdarı)", 3),
 "akil": G("akil", "آكِل", "أ ك ل", "noun", "eater (ism fa'il of أَكَلَ)", "yiyen (أَكَلَ'nin ism-i fâili)", 2),
 "dayf": G("dayf", "ضَيْف", "ض ي ف", "noun", "guest", "misafir", 2, plural="ضِيفَان"),
 "maqsud": find_gloss("maqsud"), "thalith": find_gloss("thalith"),
 "ziyad": G("ziyad", "زِيَادٌ الْأَعْجَمُ", None, "propn", "Ziyad al-Aʿjam (d. c. 100/718), Umayyad-era poet of Persian origin", "Ziyâd el-A'cem (ö. yak. 100/718), Fars asıllı Emevî devri şairi", 6),
 "ajam": G("ajam", "أَعْجَم", "ع ج م", "noun", "non-Arab, one whose Arabic is not clear", "acem, Arapçası düzgün olmayan", 5),
 "samaha": G("samaha", "سَمَاحَة", "س م ح", "noun", "liberality, open-handedness", "cömertlik, semâhat", 5),
 "muruwa": G("muruwa", "مُرُوءَة", "م ر أ", "noun", "manliness, honour", "mertlik, mürüvvet", 5),
 "nada-bounty": G("nada-bounty", "نَدًى (النَّدَى)", "ن د ي", "noun", "bounty, generosity; dew", "ihsan, cömertlik; çiy", 5),
 "fi": find_gloss("fi"),
 "qubba": G("qubba", "قُبَّة", "ق ب ب", "noun", "dome, domed tent", "kubbe, kubbeli çadır", 4, plural="قِبَاب"),
 "daraba": find_gloss("daraba"), "ala": find_gloss("ala"),
 "hashraj": G("hashraj", "الْحَشْرَج", None, "propn", "al-Hashraj — ʿAbdallah b. al-Hashraj, governor of Nishapur, Ziyad's patron", "el-Haşrec — Abdullah b. el-Haşrec, Nîşâbur vâlisi, Ziyâd'ın memdûhu", 6),
 "arada": find_gloss("arada"), "an-masdariyya": find_gloss("an-masdariyya"), "athbata": find_gloss("athbata"), "hadhihi": find_gloss("hadhihi"), "taraka": find_gloss("taraka"),
 "tasrih": G("tasrih", "تَصْرِيح", "ص ر ح", "noun", "plain statement (masdar of صَرَّحَ)", "tasrih, açıkça söyleme (صَرَّحَ'nin masdarı)", 4),
 "qala": find_gloss("qala"),
 "makhsus": G("makhsus", "مَخْصُوص", "خ ص ص", "noun", "proper to, singled out (ism maf'ul of خَصَّ)", "mahsus (خَصَّ'nin ism-i mef'ûlü)", 4),
 "jaala": find_gloss("jaala"), "madrub": find_gloss("madrub"), "mithl": find_gloss("mithl"),
 "majd": G("majd", "مَجْد", "م ج د", "noun", "glory, nobility", "şeref, mecd", 3),
 "bayna": find_gloss("bayna"), "thawb": find_gloss("thawb"),
 "karam": G("karam", "كَرَم", "ك ر م", "noun", "generosity", "kerem, cömertlik", 2),
 "burd": G("burd", "بُرْد", "ب ر د", "noun", "striped cloak", "hırka, bürde", 5, plural="بُرُود"),
 "qad": find_gloss("qad"), "dhakara": find_gloss("dhakara"), "mawsuf": find_gloss("mawsuf"),
 "akhir-last": G("akhir-last", "أَخِير", "أ خ ر", "noun", "last, latter", "son, sonuncu", 3),
 "salla-allahu": find_gloss("salla-allahu"),
 "tarid": G("tarid", "تَعْرِيض", "ع ر ض", "noun", "taʿrid — the glancing hint, said of one and aimed at another (masdar of عَرَّضَ)", "ta'rîz — birine söylenip başkasına dokundurma (عَرَّضَ'nin masdarı)", 6),
 "man-mawsula": find_gloss("man-mawsula"),
 "adha-verb": G("adha-verb", "آذَى", "أ ذ ي", "verb", "to hurt, harm (Form IV, naqis)", "eziyet etmek (IV. bâb, nâkıs)", 3, form="IV"),
 "muslim": find_gloss("muslim"), "salima": find_gloss("salima"), "lisan": find_gloss("lisan"), "yad": find_gloss("yad"),
 "qassama": G("qassama", "قَسَّمَ", "ق س م", "verb", "to divide (Form II)", "taksim etmek, bölmek (II. bâb)", 3, form="II"),
 "sakkaki": find_gloss("sakkaki"),
 "talwih": G("talwih", "تَلْوِيح", "ل و ح", "noun", "talwih — the far hint, with many rungs (masdar of لَوَّحَ)", "telvîh — çok vasıtalı uzak kinâye (لَوَّحَ'nin masdarı)", 6),
 "ramz": G("ramz", "رَمْز", "ر م ز", "noun", "ramz — the hidden hint with few rungs; a sign with lip or brow", "remz — az vasıtalı gizli kinâye; dudak yahut kaşla işaret", 5),
 "ima": G("ima", "إِيمَاء", "و م أ", "noun", "imaʾ — the plain hint with few rungs (masdar of أَوْمَأَ)", "îmâ — az vasıtalı açık kinâye (أَوْمَأَ'nin masdarı)", 5),
 "ishara": find_gloss("ishara"),
 "munasib": G("munasib", "مُنَاسِب", "ن س ب", "noun", "fitting, suitable (ism fa'il of نَاسَبَ)", "uygun, münasip (نَاسَبَ'nin ism-i fâili)", 3),
 "aradi": G("aradi", "عَرَضِيّ", "ع ر ض", "noun", "incidental — the kinaya aimed at a passing purpose (nisba to عَرَض)", "arazî — geçici bir garaza yönelik kinâye (عَرَض'a nisbet)", 6),
 "kathura": G("kathura", "كَثُرَ", "ك ث ر", "verb", "to be many, abundant (كَثُرَ يَكْثُرُ)", "çok olmak (كَثُرَ يَكْثُرُ)", 3, form="I"),
 "qalla": G("qalla", "قَلَّ", "ق ل ل", "verb", "to be few (doubled: قَلَّ يَقِلُّ)", "az olmak (muzâaf: قَلَّ يَقِلُّ)", 3, form="I"),
 "maa": find_gloss("maa"),
 "khafaa": G("khafaa", "خَفَاء", "خ ف ي", "noun", "hiddenness (masdar of خَفِيَ)", "gizlilik (خَفِيَ'nin masdarı)", 4),
 "majaz": find_gloss("majaz"), "arafa": find_gloss("arafa"), "sa": find_gloss("sa"), "murid": find_gloss("murid"),
 "mukhatab": G("mukhatab", "مُخَاطَب", "خ ط ب", "noun", "the one addressed (ism maf'ul of خَاطَبَ)", "muhatab (خَاطَبَ'nin ism-i mef'ûlü)", 3),
 "duna": find_gloss("duna"), "jami": find_gloss("jami"), "la-nafiya-lil-jins": find_gloss("la-nafiya-lil-jins"), "budd": find_gloss("budd"), "qarina": find_gloss("qarina"),
 "wa": find_gloss("wa"), "fa": find_gloss("fa"), "ka": find_gloss("ka"), "pron-3ms": find_gloss("pron-3ms"), "pron-3fs": find_gloss("pron-3fs"), "pron-3mp": find_gloss("pron-3mp"),
 "pron-2ms": find_gloss("pron-2ms"), "pron-1p": find_gloss("pron-1p"), "pron-1s": find_gloss("pron-1s"), "pron-3d": find_gloss("pron-3d"), "ta-tanith": find_gloss("ta-tanith"),
}

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "adha-verb", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "آذَ", "ؤْذ", "i", "آذ", "إِيذَاء", "مُؤْذٍ (الْمُؤْذِي)", "مُؤْذًى", "أُوذِيَ", "يُؤْذَى",
                                             "مَهْمُوزُ الْفَاءِ نَاقِصٌ عَلَى أَفْعَلَ: آذَى يُؤْذِي — آذَيْتَنِي."))
put_morph(mo, "qassama", _sg.derived(_sg.B2, _sg.W2, "ُ", "قَسَّم", "قَسِّم", "قَسِّم", "تَقْسِيم", "مُقَسِّم", "مُقَسَّم", "قُسِّمَ", "يُقَسَّمُ"))
put_morph(mo, "kathura", _sg.sound1("karuma", "كَثُر", "كْثُر", "اُكْثُر", "كَثْرَة", "كَثِير", None, None, None, "لَازِمٌ مِنْ بَابِ حَسُنَ؛ اسْمُ فَاعِلِهِ صِفَةٌ مُشَبَّهَةٌ: كَثِير."))
def doubled(bab, yv, m, mm, d, dd, amr, masdar, fail, maful=None, pmz=None, pmd=None, note=None):
    b = _sg.BABS[bab]
    return _sg.idgham(_sg.entry(b[0] + " — مُضَاعَفٌ", b[1], masdar, fail, _sg.mazi14(m, mm), _sg.mudari14(yv, d, dd), amr,
                                "يَ" + d + "َ", "يَ" + d + "َ", "تَ" + d + "َ", maful, pmz, pmd, note))
put_morph(mo, "qalla", doubled("daraba", "َ", "قَلّ", "قَلَل", "قِلّ", "قْلِل", ["قِلَّ", "قِلَّا", "قِلُّوا", "قِلِّي", "قِلَّا", "اِقْلِلْنَ"], "قِلَّة", "قَلِيل", None, None, None,
                              "مُضَاعَفٌ لَازِمٌ مِنْ بَابِ ضَرَبَ: قَلَّ يَقِلُّ؛ اسْمُ فَاعِلِهِ صِفَةٌ مُشَبَّهَةٌ: قَلِيل."))
for k in ("daraba", "salima", "arafa", "dhakara", "taraka", "jaala", "qala", "athbata", "arada", "kana", "intaqala"):
    if k not in mo["verbs"] and has_morph(k): mo["verbs"][k] = find_morph(k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_A = {
 "id": "aqsam-al-kinaya",
 "title": {"ar": "أَقْسَامُ الْكِنَايَةِ — الْمَطْلُوبُ بِهَا مَوْصُوفٌ أَوْ صِفَةٌ أَوْ نِسْبَةٌ", "en": "The kinds of the kinaya — a thing, a quality, or an attribution sought", "tr": "Kinâyenin kısımları — mevsûf, sıfat yahut nisbet istenen"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — الكناية ثلاثة أقسام"],
 "question": {
  "en": ["WHAT is sought by the hint? A THING (the hearts, named as «the gathering-places of rancours»; the human being, as «a living thing, upright, broad-nailed»)? Then the kinaya is for a MAWSUF, and it must be proper to that thing alone.",
         "A QUALITY of a thing named (tallness, said as «long of sword-belt»; dullness, as «broad of nape»)? Then the kinaya is for a SIFA.",
         "An ATTRIBUTION — that a quality belongs to someone (liberality «in a dome pitched over Ibn al-Hashraj»; «glory between his two garments»)? Then the kinaya is for a NISBA: the quality is set in his tent or his clothes, not stated of him."],
  "tr": ["Kinâyeyle NE isteniyor? Bir ŞEY mi (kalpler, «kinlerin toplandığı yerler» diye; insan, «boyu dik tırnağı geniş bir canlı» diye)? Öyleyse kinâye MEVSÛF içindir ve yalnız o şeye has olmalıdır.",
         "Adlandırılmış bir şeyin SIFATI mı (uzun boy, «kılıç kayışı uzun» diye; ahmaklık, «ensesi geniş» diye)? Öyleyse SIFAT kinâyesidir.",
         "Bir NİSBET mi — bir vasfın birine ait olduğu (cömertlik «İbnü'l-Haşrec üzerine kurulmuş kubbede»; «şeref iki elbisesi arasında»)? Öyleyse NİSBET kinâyesidir: vasıf ona söylenmez, çadırına yahut elbisesine konur."]},
 "plain": {
  "en": "Three kinds by what the hint reaches for: a THING (the hearts, a human), a QUALITY (tall, dull, hospitable), or an ATTRIBUTION (glory is his). The engine reads the shape: a quality-word annexed to a noun points at a sifa, a quality with a place for its khabar at a nisba, adjectives with no head noun at a mawsuf.",
  "tr": "Kinâyenin ulaşmak istediğine göre üç kısım: bir ŞEY (kalpler, insan), bir SIFAT (uzun, ahmak, misafirperver) yahut bir NİSBET (şeref onundur). Motor şekli okur: isme izâfe edilmiş vasıf kelimesi sıfata, haberi bir yer yahut elbise olan vasıf mübtedâsı nisbete, baş ismi olmayan sıfatlar mevsûfa işaret eder."},
 "explanation": {
  "en": "The kinaya is of THREE KINDS by what is SOUGHT (الْمَطْلُوبُ بِهَا). FIRST, that by which something OTHER THAN A QUALITY OR AN ATTRIBUTION is sought — a thing. Of it there is what is ONE meaning: ʿAmr b. Maʿdikarib's الضَّارِبِينَ بِكُلِّ أَبْيَضَ مِخْذَمٍ وَالطَّاعِنِينَ مَجَامِعَ الْأَضْغَانِ, where «the gathering-places of rancours» means the HEARTS; and what is a SUM of meanings: حَيٌّ مُسْتَوِي الْقَامَةِ عَرِيضُ الْأَظْفَارِ for the human being — with the CONDITION that the marks be PROPER to the thing hinted at. SECOND, that by which a QUALITY is sought — see the note on the near and the far kinaya. THIRD, that by which an ATTRIBUTION is sought: Ziyad al-Aʿjam's إِنَّ السَّمَاحَةَ وَالْمُرُوءَةَ وَالنَّدَى • فِي قُبَّةٍ ضُرِبَتْ عَلَى ابْنِ الْحَشْرَجِ — he meant to affirm that these qualities are PROPER to the man, and left the plain «he is proper to them» for the kinaya, by placing them inside a dome pitched over him; likewise الْمَجْدُ بَيْنَ ثَوْبَيْهِ and الْكَرَمُ بَيْنَ بُرْدَيْهِ. In the second and third kinds the DESCRIBED THING is sometimes NOT MENTIONED: الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ, a TAʿRID at one who harms the Muslims — the quality of Islam denied him with no one named. WHAT THE ENGINE CLAIMS: it reads the KIND off the nahw. A quality-shaped head (the SifaEngine's فَعِيل، فَاعِل، أَفْعَل، مِفْعَال) ANNEXED to a definite noun — a lafzi idafa — is a SIFA candidate (كَثِيرُ الرَّمَادِ، طَوِيلُ النِّجَادِ، عَرِيضُ الْقَفَا), as is an indefinite quality-word with a pronoun-bearing noun as its doer (طَوِيلٌ نِجَادُهُ). An ABSTRACT quality as MUBTADA whose khabar is a PLACE or a GARMENT annexed to a person (بَيْنَ ثَوْبَيْهِ، فِي قُبَّةٍ … عَلَى ابْنِ الْحَشْرَجِ) is a NISBA candidate. A run of quality-words with NO HEAD NOUN before them (حَيٌّ مُسْتَوِي الْقَامَةِ عَرِيضُ الْأَظْفَارِ), or a participle standing where a noun should (الضَّارِبِينَ بِكُلِّ أَبْيَضَ), is a MAWSUF candidate. It grades that reading against the authored frame's kind and span; the thing MEANT it never derives — that is knowledge, carried on the frame.",
  "tr": "Kinâye, kendisiyle İSTENENe (الْمَطْلُوبُ بِهَا) göre ÜÇ KISIMDIR. BİRİNCİSİ, kendisiyle SIFAT VE NİSBETİN GAYRI — bir şey — istenendir. Bunun bir kısmı TEK mânâdır: Amr b. Ma'dîkerib'in الضَّارِبِينَ بِكُلِّ أَبْيَضَ مِخْذَمٍ وَالطَّاعِنِينَ مَجَامِعَ الْأَضْغَانِ beyti; «kinlerin toplandığı yerler» KALPLERdir. Bir kısmı mânâların TOPLAMIdır: insan için حَيٌّ مُسْتَوِي الْقَامَةِ عَرِيضُ الْأَظْفَارِ — alâmetlerin kendisinden kinâye edilene HAS olması ŞARTIYLA. İKİNCİSİ, kendisiyle SIFAT istenendir — yakın ve uzak kinâye notuna bakınız. ÜÇÜNCÜSÜ, kendisiyle NİSBET istenendir: Ziyâd el-A'cem'in إِنَّ السَّمَاحَةَ وَالْمُرُوءَةَ وَالنَّدَى • فِي قُبَّةٍ ضُرِبَتْ عَلَى ابْنِ الْحَشْرَجِ beyti — bu vasıfların adama HAS olduğunu isbat etmek istemiş, açık «o bunlara mahsustur»u bırakıp onları üzerine kurulmuş bir kubbeye koymakla kinâyeye gitmiştir; الْمَجْدُ بَيْنَ ثَوْبَيْهِ ve الْكَرَمُ بَيْنَ بُرْدَيْهِ de böyledir. İkinci ve üçüncü kısımda MEVSÛF bazen ZİKREDİLMEZ: الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ, Müslümanlara eziyet edene bir TA'RÎZ — kimse anılmadan İslâm vasfı ondan nefyedilir. MOTORUN İDDİASI: KISMI nahivden okur. Ma'rife bir isme İZÂFE edilmiş vasıf şekilli baş (SifaEngine'in فَعِيل، فَاعِل، أَفْعَل، مِفْعَال'i) — lafzî izâfet — SIFAT adayıdır (كَثِيرُ الرَّمَادِ، طَوِيلُ النِّجَادِ، عَرِيضُ الْقَفَا); fâili zamir taşıyan bir isim olan nekre vasıf kelimesi de öyle (طَوِيلٌ نِجَادُهُ). Haberi bir kişiye izâfe edilmiş YER yahut ELBİSE olan SOYUT bir vasıf MÜBTEDÂSI (بَيْنَ ثَوْبَيْهِ، فِي قُبَّةٍ … عَلَى ابْنِ الْحَشْرَجِ) NİSBET adayıdır. Önünde BAŞ İSİM olmayan bir vasıf dizisi (حَيٌّ مُسْتَوِي الْقَامَةِ عَرِيضُ الْأَظْفَارِ) yahut isim yerinde duran bir ism-i fâil (الضَّارِبِينَ بِكُلِّ أَبْيَضَ) MEVSÛF adayıdır. Bu okumayı müellif çerçevesinin kısmı ve aralığıyla sınar; KASTEDİLENİ asla türetmez — o, çerçevede taşınan bilgidir."},
 "examples": [
  {"ar": "وَالطَّاعِنِينَ مَجَامِعَ الْأَضْغَانِ", "en": "a thing sought: the hearts.", "tr": "mevsûf istenen: kalpler.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "حَيٌّ مُسْتَوِي الْقَامَةِ عَرِيضُ الْأَظْفَارِ", "en": "a sum of marks proper to the human being.", "tr": "insana has alâmetlerin toplamı.", "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "فِي قُبَّةٍ ضُرِبَتْ عَلَى ابْنِ الْحَشْرَجِ", "en": "an attribution sought: the qualities are his.", "tr": "nisbet istenen: vasıflar onun.", "sourceStory": "talkhis-al-miftah", "sentence": "s13"},
  {"ar": "الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ", "en": "the described thing unspoken: a taʿrid.", "tr": "mevsûf anılmamış: ta'rîz.", "sourceStory": "talkhis-al-miftah", "sentence": "s17"}],
 "commonMistakes": [
  {"wrong": "«مَجَامِعَ الْأَضْغَانِ kalpler için mecâz-ı mürseldir (mahalliyye)»",
   "right": "«Mevsûftan kinâyedir: kalpler, kinlerin toplandığı yer olarak GERÇEKTEN kastedilebilir; hakikat engellenmemiştir»",
   "why": {"en": "Nothing in the bayt bars the literal reading — rancours do gather in hearts. Where the literal sense stays permitted, the word is a kinaya, not a majaz.", "tr": "Beyitte hakikî okumayı engelleyen bir şey yok — kinler gerçekten kalplerde toplanır. Hakikî mânâ câiz kaldıkça kelime mecaz değil kinâyedir."}},
  {"wrong": "«الْمَجْدُ بَيْنَ ثَوْبَيْهِ sıfat kinâyesidir: şeref bir vasıftır»",
   "right": "«Nisbet kinâyesidir: şeref adlandırılmıştır; kinâye, onun ONA AİT olmasındadır»",
   "why": {"en": "The quality is spoken outright; what is hinted is its ATTRIBUTION to the man, by placing it between his garments. The kind is fixed by what is left unsaid.", "tr": "Vasıf açıkça söylenmiştir; ima edilen, elbiseleri arasına konarak onun ADAMA NİSBETİdir. Kısım, söylenmeyenle belirlenir."}}],
 "relatedNotes": ["kinaya", "farq-al-kinaya-wal-majaz", "kinaya-qariba-baida", "tarid-talwih-ramz", "sifa-mushabbaha", "idafa-definiteness", "mubtada-khabar"]}
NOTE_B = {
 "id": "kinaya-qariba-baida",
 "title": {"ar": "الْكِنَايَةُ الْقَرِيبَةُ وَالْبَعِيدَةُ — الْوَسَائِطُ وَالضَّمِيرُ", "en": "The near and the far kinaya — the rungs, and the pronoun inside", "tr": "Yakın ve uzak kinâye — basamaklar ve içteki zamir"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — الثانية: المطلوب بها صفة"],
 "question": {
  "en": ["How many RUNGS does the mind climb from the said to the meant? None — the passage is direct — makes the kinaya NEAR (قَرِيبَة): a long sword-belt hangs from a tall body. Four — much ash → much burning → much cooking → many eaters → many guests → hospitable — make it FAR (بَعِيدَة).",
         "Is the near one PLAIN or HIDDEN? «Long of sword-belt» every hearer climbs at once (وَاضِحَة); «broad of nape» for a dull wit is a real but hidden tie (خَفِيَّة).",
         "Does the wording carry a PRONOUN? طَوِيلٌ نِجَادُهُ is the pure kinaya: two words, no pronoun in the quality. طَوِيلُ النِّجَادِ folds a concealed pronoun into its idafa — its doer — and so contains a shade of plain statement: it is MORE SPECIFIC."],
  "tr": ["Zihin söylenenden kastedilene KAÇ BASAMAK çıkar? Hiç — intikal doğrudan — kinâyeyi YAKIN (قَرِيبَة) yapar: uzun kılıç kayışı uzun bedenden sarkar. Dört — çok kül → çok yakma → çok pişirme → çok yiyen → çok misafir → misafirperver — UZAK (بَعِيدَة) yapar.",
         "Yakın olan AÇIK mı GİZLİ mi? «Kılıç kayışı uzun»u her dinleyen hemen çıkar (وَاضِحَة); ahmak için «ensesi geniş» gerçek fakat gizli bir bağdır (خَفِيَّة).",
         "İfade ZAMİR taşıyor mu? طَوِيلٌ نِجَادُهُ sırf kinâyedir: iki kelime, vasıfta zamir yok. طَوِيلُ النِّجَادِ izâfetine gizli bir zamir — fâilini — katlar ve bir tür tasrih taşır: DAHA HUSÛSÎDİR."]},
 "plain": {
  "en": "A quality-kinaya is NEAR when the meant follows the said at once, FAR when the mind climbs rungs (ash → firewood → cooking → guests → hospitable). The near is plain or hidden. The engine counts the authored rungs and reads the pronoun test off the idafa: the annexed form hides a doer, the two-word form does not.",
  "tr": "Sıfat kinâyesi, kastedilen söylenenden hemen çıkıyorsa YAKIN, zihin basamak çıkıyorsa UZAKtır (kül → odun → pişirme → yiyen → misafir → misafirperver). Yakın olan açık yahut gizlidir. Motor müellifin basamaklarını sayar ve zamir sınamasını izâfetten okur: izâfeli şekil içinde fâil gizler, iki kelimeli şekil gizlemez."},
 "explanation": {
  "en": "The kinaya by which a QUALITY is sought is either NEAR (قَرِيبَة), if the passage is WITHOUT A GO-BETWEEN, or FAR (بَعِيدَة), if it is by a go-between. The near one is either PLAIN (وَاضِحَة) — as the Arabs' kinaya for tallness, طَوِيلٌ نِجَادُهُ and طَوِيلُ النِّجَادِ, «long of sword-belt» — or HIDDEN (خَفِيَّة) — as their kinaya for the dull-witted, عَرِيضُ الْقَفَا, «broad of nape». Of the two sayings for tallness the SECOND is MORE SPECIFIC (أَخَصُّ), because it CONTAINS THE PRONOUN: the idafa طَوِيلُ النِّجَادِ carries a concealed doer inside the quality-word, and so half-says the man's tallness, while طَوِيلٌ نِجَادُهُ is a pure kinaya. The FAR one is كَثِيرُ الرَّمَادِ for the hospitable man: the mind passes from the ABUNDANCE OF ASH to the abundance of BURNT FIREWOOD, then to the abundance of COOKING, then to the abundance of EATERS, then to the abundance of GUESTS, then to the thing meant — four rungs. WHAT THE ENGINE CLAIMS: it draws the LADDER from the authored rungs (wasait) and names the kinaya near where the rungs are none and far where they are one or more; the plain/hidden division it shows as the chapter's, since a tie's plainness is the hearer's knowledge. The PRONOUN TEST it settles itself: a quality-word annexed to a definite noun (an idafa lafziyya) hides a doer inside — the concealed pronoun the sifa mushabbaha's construction table also counts — while an indefinite quality-word whose doer is the pronoun-bearing noun after it (نِجَادُهُ) holds no pronoun of its own. The SifaEngine settles that the head is a quality-word (فَعِيل of كَثُرَ، طَالَ، عَرُضَ), the DabtEngine that it is annexed.",
  "tr": "Kendisiyle SIFAT istenen kinâye, intikal VASITASIZ ise YAKIN (قَرِيبَة), vasıta ile ise UZAK (بَعِيدَة)tır. Yakın olan ya AÇIK (وَاضِحَة)tır — Arapların uzun boy kinâyesi طَوِيلٌ نِجَادُهُ ve طَوِيلُ النِّجَادِ, «kılıç kayışı uzun» gibi — ya GİZLİ (خَفِيَّة)dir — ahmak için عَرِيضُ الْقَفَا, «ensesi geniş» gibi. Uzun boy için iki sözden İKİNCİSİ DAHA HUSÛSÎDİR (أَخَصُّ), çünkü ZAMİRİ İÇERİR: طَوِيلُ النِّجَادِ izâfeti vasıf kelimesinin içinde gizli bir fâil taşır ve adamın uzunluğunu yarı söyler; طَوِيلٌ نِجَادُهُ ise sırf kinâyedir. UZAK olan, misafirperver için كَثِيرُ الرَّمَادِ'dır: zihin KÜLÜN ÇOKLUĞUndan YAKILAN ODUNun çokluğuna, sonra PİŞİRMEnin, sonra YİYENLERin, sonra MİSAFİRLERin çokluğuna, sonra kastedilene geçer — dört basamak. MOTORUN İDDİASI: MERDİVENİ müellifin basamaklarından (vesâit) çizer; basamak yoksa yakın, bir yahut daha çoksa uzak der; açık/gizli ayrımını bâbın taksimi olarak gösterir, çünkü bir bağın açıklığı dinleyenin bilgisidir. ZAMİR SINAMASINI kendisi çözer: ma'rife bir isme izâfe edilmiş vasıf kelimesi (lafzî izâfet) içinde bir fâil gizler — sıfat-ı müşebbehenin terkip tablosunun da saydığı gizli zamir — nekre vasıf kelimesinin fâili ise sonraki zamirli isimdir (نِجَادُهُ) ve kendi zamiri yoktur. Başın vasıf kelimesi olduğunu SifaEngine (كَثُرَ، طَالَ، عَرُضَ'nin فَعِيل'i), izâfe edildiğini DabtEngine çözer."},
 "examples": [
  {"ar": "طَوِيلٌ نِجَادُهُ", "en": "near and plain; no pronoun inside — the pure kinaya.", "tr": "yakın ve açık; içinde zamir yok — sırf kinâye.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"},
  {"ar": "طَوِيلُ النِّجَادِ", "en": "near and plain; the pronoun folded in — more specific.", "tr": "yakın ve açık; zamir katlanmış — daha husûsî.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"},
  {"ar": "عَرِيضُ الْقَفَا", "en": "near and hidden.", "tr": "yakın ve gizli.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"},
  {"ar": "كَثِيرُ الرَّمَادِ", "en": "far — four rungs to the hospitable man.", "tr": "uzak — misafirperverliğe dört basamak.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«كَثِيرُ الرَّمَادِ: külü çok olan adam, yani ocağı büyük — yakın kinâye»",
   "right": "«Uzak kinâyedir: kül → odun → pişirme → yiyen → misafir → misafirperver; dört vasıta»",
   "why": {"en": "Nearness is counted in rungs, not in how familiar the phrase feels. The Talkhis spells out four passages before the meant is reached.", "tr": "Yakınlık ibarenin ne kadar tanıdık geldiğiyle değil basamakla sayılır. Telhîs kastedilene varmadan dört geçiş sayar."}},
  {"wrong": "«طَوِيلُ النِّجَادِ ile طَوِيلٌ نِجَادُهُ aynı sözdür»",
   "right": "«İkincisi (izâfeli olan) zamiri içerdiği için daha husûsîdir: bir tür tasrih taşır»",
   "why": {"en": "The idafa hides a doer in the quality-word; the two-word sentence leaves the quality bare. That concealed pronoun is a grain of plain statement inside the hint.", "tr": "İzâfet, vasıf kelimesinde bir fâil gizler; iki kelimeli cümle vasfı çıplak bırakır. O gizli zamir, imanın içinde bir tasrih zerresidir."}}],
 "relatedNotes": ["kinaya", "aqsam-al-kinaya", "tarid-talwih-ramz", "sifa-mushabbaha", "idafa-definiteness", "fail"]}
NOTE_T = {
 "id": "tarid-talwih-ramz",
 "title": {"ar": "التَّعْرِيضُ وَالتَّلْوِيحُ وَالرَّمْزُ وَالْإِيمَاءُ — تَقْسِيمُ السَّكَّاكِيِّ", "en": "Taʿrid, talwih, ramz and imaʾ — Sakkaki's names for the kinaya", "tr": "Ta'rîz, telvîh, remz ve îmâ — Sekkâkî'nin kinâye adları"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — وقسمها السكاكي إلى تعريض وتلويح ورمز وإيماء وإشارة"],
 "question": {
  "en": ["Is the hint driven at a PASSING PURPOSE in a hearer (the harmer, told «the Muslim is he from whose tongue and hand the Muslims are safe»)? Then it is a TAʿRID — the glancing hint.",
         "Otherwise, are the RUNGS MANY? Then TALWIH, the signal from afar (كَثِيرُ الرَّمَادِ). FEW and hidden? RAMZ, the sign with lip or brow (عَرِيضُ الْقَفَا). Few and plain? IMAʾ and ISHARA (طَوِيلُ النِّجَادِ).",
         "Can a taʿrid be a MAJAZ? Yes — «You have hurt me, so you shall know», said to one man and meant of another beside him: the addressee is barred, so it is a majaz; meant of both, it is a kinaya. Either way a clue is indispensable."],
  "tr": ["İma bir dinleyendeki GEÇİCİ BİR GARAZA mı yöneltilmiş (eziyet edene «Müslüman, Müslümanların dilinden ve elinden selâmette olduğu kimsedir» denmesi)? Öyleyse TA'RÎZ — dokundurmadır.",
         "Değilse BASAMAKLAR ÇOK mu? TELVÎH, uzaktan işaret (كَثِيرُ الرَّمَادِ). AZ ve gizli mi? REMZ, dudak yahut kaşla işaret (عَرِيضُ الْقَفَا). Az ve açık mı? ÎMÂ ve İŞÂRET (طَوِيلُ النِّجَادِ).",
         "Ta'rîz MECAZ olabilir mi? Evet — «Bana eziyet ettin, yakında bileceksin», birine söylenip yanındaki başkası kastedilirse: muhatab dışlanır, mecazdır; ikisi de kastedilirse kinâye. İki hâlde de karîne şarttır."]},
 "plain": {
  "en": "Sakkaki's four names sort the kinaya by purpose and by rungs: the taʿrid glances at a hearer; of the rest, many rungs make a talwih, few and hidden a ramz, few and plain an imaʾ. The engine offers them as a shortlist from the rung count; the taʿrid, and whether it is a majaz, only the authored frame can say.",
  "tr": "Sekkâkî'nin dört adı kinâyeyi garaza ve basamağa göre sıralar: ta'rîz dinleyene dokundurur; kalanlardan çok basamak telvîh, az ve gizli remz, az ve açık îmâ. Motor onları basamak sayısından kısa liste olarak sunar; ta'rîzi ve mecaz olup olmadığını yalnız müellif çerçevesi söyler."},
 "explanation": {
  "en": "SAKKAKI divided the kinaya into TAʿRID, TALWIH, RAMZ, IMAʾ and ISHARA. The FITTING name for the INCIDENTAL kinaya (الْعَرَضِيَّة — one driven at a passing purpose in a hearer) is TAʿRID, the glancing hint: the Prophet's ﷺ الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ, said as a taʿrid at one who harms the Muslims, denies him the quality of Islam without naming him — an example, too, of the described thing left UNSPOKEN in the second and third kinds. For the others: if the GO-BETWEENS are MANY, TALWIH (لَوَّحَ — to signal from afar); if FEW, with hiddenness, RAMZ (the sign with lip or brow); and without hiddenness, IMAʾ and ISHARA. Then Sakkaki added that the taʿrid may sometimes be a MAJAZ: your آذَيْتَنِي فَسَتَعْرِفُ, «you have hurt me, so you shall know», said to one man while you mean another beside him and NOT him — the addressee is barred, so the word is off its meaning, a majaz; if you mean them BOTH, it is a kinaya, the literal sense kept; and in both cases a CLUE is indispensable. WHAT THE ENGINE CLAIMS: from the authored rung count it prints Sakkaki's name as a SHORTLIST — none or one plain rung: imaʾ/ishara; few with a hidden tie: ramz; many: talwih — and marks a frame taʿrid only where the author has named it, since a passing purpose lives in the situation, not in the words. The majaz/kinaya line of the last example it states as the rule it is: barred addressee → majaz, both meant → kinaya.",
  "tr": "SEKKÂKÎ kinâyeyi TA'RÎZ, TELVÎH, REMZ, ÎMÂ ve İŞÂRET diye böldü. ARAZÎ kinâyeye (الْعَرَضِيَّة — bir dinleyendeki geçici bir garaza yöneltilmiş olana) UYGUN ad TA'RÎZ, dokundurmadır: Peygamber'in ﷺ الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ sözü, Müslümanlara eziyet edene ta'rîz olarak, onu adlandırmadan İslâm vasfını ondan nefyeder — ikinci ve üçüncü kısımda MEVSÛFUN ANILMAMASINA da örnektir. Diğerleri için: VASITALAR ÇOKSA TELVÎH (لَوَّحَ — uzaktan işaret etmek); AZSA ve gizlilikle REMZ (dudak yahut kaşla işaret); gizliliksiz ÎMÂ ve İŞÂRET. Sonra Sekkâkî ta'rîzin bazen MECAZ olabileceğini ekledi: senin آذَيْتَنِي فَسَتَعْرِفُ, «bana eziyet ettin, yakında bileceksin» sözün, birine söylenip yanındaki başkası kastedilir, o kastedilmezse — muhatab dışlanır, kelime mânâsının dışındadır, mecazdır; İKİSİNİ birden kastedersen kinâyedir, hakikî mânâ tutulur; iki hâlde de KARÎNE şarttır. MOTORUN İDDİASI: müellifin basamak sayısından Sekkâkî'nin adını KISA LİSTE olarak basar — basamak yok yahut bir açık basamak: îmâ/işâret; az ve gizli bağ: remz; çok: telvîh — ve bir çerçeveyi yalnız müellif adlandırmışsa ta'rîz diye işaretler, çünkü geçici garaz kelimelerde değil durumda yaşar. Son örneğin mecaz/kinâye çizgisini olduğu kural olarak söyler: muhatab dışlanmış → mecaz, ikisi kastedilmiş → kinâye."},
 "examples": [
  {"ar": "الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ", "en": "a taʿrid at the harmer.", "tr": "eziyet edene ta'rîz.", "sourceStory": "talkhis-al-miftah", "sentence": "s17"},
  {"ar": "إِنْ كَثُرَتِ الْوَسَائِطُ التَّلْوِيحُ", "en": "many rungs: talwih.", "tr": "çok basamak: telvîh.", "sourceStory": "talkhis-al-miftah", "sentence": "s19"},
  {"ar": "آذَيْتَنِي فَسَتَعْرِفُ", "en": "a taʿrid that is a majaz when the addressee is not meant.", "tr": "muhatab kastedilmeyince mecaz olan ta'rîz.", "sourceStory": "talkhis-al-miftah", "sentence": "s20"}],
 "commonMistakes": [
  {"wrong": "«Ta'rîz, kinâyenin dışında ayrı bir sanattır»",
   "right": "«Sekkâkî'ye göre kinâyenin bir kısmıdır: arazî — bir dinleyene yönelik — kinâyeye uygun ad»",
   "why": {"en": "The Talkhis lists the taʿrid among Sakkaki's divisions of the kinaya, distinguished by its purpose, not by a different mechanism.", "tr": "Telhîs ta'rîzi Sekkâkî'nin kinâye taksimleri arasında sayar; farkı mekanizmasında değil garazındadır."}},
  {"wrong": "«آذَيْتَنِي فَسَتَعْرِفُ her zaman kinâyedir»",
   "right": "«Muhatab kastedilmiyorsa mecaz, ikisi kastediliyorsa kinâye — karîne belirler»",
   "why": {"en": "Whether the literal addressee is barred decides the kind, and that is a fact of the situation the clue must carry.", "tr": "Hakikî muhatabın dışlanıp dışlanmadığı kısmı belirler; bu, karînenin taşıması gereken bir durum gerçeğidir."}}],
 "relatedNotes": ["kinaya", "aqsam-al-kinaya", "kinaya-qariba-baida", "farq-al-kinaya-wal-majaz", "haqiqa-majaz"]}

ADD_EN = (" Chapter 56 (lines ~3890-3940, sahifa 134-136) carries the kinaya's three kinds, the described thing left unspoken, "
          "and Sakkaki's taʿrid, talwih, ramz and imaʾ: the bayt of ʿAmr b. Maʿdikarib (s3), the bayt of Ziyad al-Aʿjam (s13) "
          "and the hadith of the Muslim (s17) are Arabic as the source prints it, as are the Arabs' sayings inside the restored "
          "frames. s1, s2, s4-s12, s14-s16 and s18-s21 are RESTORATIONS, not quotations: the source carries those steps only in "
          "Ottoman-Turkish paraphrase, and the Arabic restores the matn's wording in the musannif's register; each is marked "
          "«restored» in its translation. Every kinaya carries an authored `kinaya` frame (the said, the kind, the meant, the "
          "rungs, Sakkaki's name, the pronoun test).")
ADD_TR = (" Elli altıncı bâb (satır ~3890-3940, sahife 134-136) kinâyenin üç kısmını, anılmayan mevsûfu ve Sekkâkî'nin ta'rîz, "
          "telvîh, remz ve îmâsını taşır: Amr b. Ma'dîkerib'in beyti (s3), Ziyâd el-A'cem'in beyti (s13) ve Müslüman hadisi (s17) "
          "kaynağın bastığı Arapçadır; geri yazılmış çerçevelerin içindeki Arap sözleri de öyle. s1, s2, s4-s12, s14-s16 ve "
          "s18-s21 ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın "
          "ifadesini musannifin üslûbunda geri yazar; her biri tercümesinde «geri yazılmıştır» diye işaretlidir. Her kinâye bir "
          "müellif `kinaya` çerçevesi taşır (söylenen, kısım, kastedilen, basamaklar, Sekkâkî'nin adı, zamir sınaması).")
write_out(56, S, TITLE, ADD_EN, ADD_TR, "3890-3940", GLOSS_ADD, notes=(NOTE_A, NOTE_B, NOTE_T),
          related=(("kinaya", ["aqsam-al-kinaya", "kinaya-qariba-baida", "tarid-talwih-ramz"]), ("sifa-mushabbaha", ["kinaya-qariba-baida"]), ("farq-al-kinaya-wal-majaz", ["aqsam-al-kinaya", "tarid-talwih-ramz"])))
report(56, S, GLOSS_ADD, (NOTE_A, NOTE_B, NOTE_T))
