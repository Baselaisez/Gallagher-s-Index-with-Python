# -*- coding: utf-8 -*-
"""Author chapter 55 of talkhis-al-miftah — the faṣl on what the word MAJAZ is
also applied to (sahifa 133-134, lines ~3874-3890): a word whose I'RAB changed
by the dropping or the adding of a word (وَجَاءَ رَبُّكَ، وَاسْأَلِ الْقَرْيَةَ — the
majaz by OMISSION; لَيْسَ كَمِثْلِهِ شَيْءٌ — the majaz by ADDITION); then the
KINAYA's definition, how it differs from the majaz, Sakkaki's account of the
difference and its refutation.

  RESTORED (the source carries the step only in Turkish): s1, s4, s6-s10.
  As printed: the three ayat (s2, s3, s5).
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from talkhis_common import *
import sarf_gen as _sg

Z = "majaz-ziyada-nuqsan"; F = "farq-al-kinaya-wal-majaz"; K = "kinaya"
TITLE = {"ar": "الْمَجَازُ بِالنُّقْصَانِ وَالزِّيَادَةِ، وَتَعْرِيفُ الْكِنَايَةِ وَالْفَرْقُ بَيْنَهَا وَبَيْنَ الْمَجَازِ",
         "en": "The Majaz by Omission and by Addition; the Kinaya Defined and Told from the Majaz",
         "tr": "Noksan ve Ziyâde ile Mecaz; Kinâyenin Tarifi ve Mecazdan Farkı"}
S = []
def wq(full="وَقَوْلِهِ", tag=Z):
    return tok(full, "qawl", "noun", [tag, "atf-nasaq", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَقَوْلِ مَعْطُوفٌ عَلَى قَوْلِ الْأُولَى مَجْرُورٌ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
               "«and His saying» — joined onto the first قَوْل; a mudaf.", "«ve sözü» — ilk قَوْل'e matuf; muzâf.",
               segments=[seg("وَ", "wa", "conj"), seg("قَوْلِ", "qawl", "noun"), seg("هِ", "pron-3ms", "pron")], punct=":")

# ----------- s1 — the fasl (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "A section. The word MAJAZ is sometimes applied to a word whose I'RAB has changed by the dropping of a word or the adding of a word." + R_EN,
 "tr": "Fasıl. MECAZ lafzı bazen, bir lafzın düşmesi yahut bir lafzın eklenmesiyle İ'RÂBININ hükmü değişen kelimeye de söylenir." + R_TR},
 "tokens": [
  tok("فَصْلٌ","fasl","noun",[Z, "mubtada-khabar"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — هَذَا فَصْلٌ.", "«a section» — the khabar of a dropped «this is».", "«fasıl» — hazfedilmiş «bu»nun haberi.", punct=":"),
  tok("قَدْ","qad","part",[Z, "qad-harf"], "حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ.", "«sometimes» — qad with a mudari'.", "«bazen» — muzâri ile kad."),
  tok("يُطْلَقُ","atlaqa","verb",[Z, "naib-al-fail", "form-iv-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is applied» — the passive mudari' of Form IV.", "«ıtlak olunur, söylenir» — IV. bâbın meçhûl muzârii."),
  tok("الْمَجَازُ","majaz","noun",[Z, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the majaz» — the deputy doer.", "«mecaz» — nâib-i fâil."),
  tok("عَلَى","ala","part",[Z, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("كَلِمَةٍ","kalima","noun",[Z, "huruf-jarr", "jumla-sifa"], "مَجْرُورٌ — وَالْجُمْلَةُ بَعْدَهُ صِفَةٌ لَهُ.", "«a word» — the clause after it describes it.", "«bir kelime» — sonraki cümle onun sıfatı."),
  tok("تَغَيَّرَ","taghayyara","verb",[Z, "jumla-sifa", "form-v-verbs"], "فِعْلٌ مَاضٍ مِنَ الْخَامِسِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ لِكَلِمَةٍ.", "«has changed» — Form V; the clause in the place of jarr, a sifa of «word».", "«değişmiş» — V. bâb; cümle cer mahallinde, «kelime»nin sıfatı."),
  tok("حُكْمُ","hukm","noun",[Z, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the rule of» — the doer; a mudaf.", "«hükmü» — fâil; muzâf."),
  tok("إِعْرَابِهَا","irab","noun",[Z, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its i'rab» — mudaf ilayh, with its pronoun.", "«i'râbının» — muzâfun ileyh, zamiriyle.",
      segments=[seg("إِعْرَابِ","irab","noun"), seg("هَا","pron-3fs","pron")]),
  tok("بِحَذْفِ","hadhf","noun",[Z, "huruf-jarr", "idafa-definiteness", "masdar"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ — الْبَاءُ لِلسَّبَبِيَّةِ؛ مَصْدَرُ حَذَفَ.", "«by the dropping of» — the ba of cause; masdar of حَذَفَ.", "«düşmesiyle» — sebep bâsı; حَذَفَ'nin masdarı.",
      segments=[seg("بِ","bi","part"), seg("حَذْفِ","hadhf","noun")]),
  tok("لَفْظٍ","lafz","noun",[Z, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a word» — mudaf ilayh.", "«bir lafzın» — muzâfun ileyh."),
  tok("أَوْ","aw","conj",[Z, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("زِيَادَةِ","ziyada","noun",[Z, "atf-nasaq", "idafa-definiteness", "masdar"], "مَعْطُوفٌ عَلَى حَذْفِ مَجْرُورٌ، مُضَافٌ — مَصْدَرُ زَادَ.", "«the adding of» — joined onto «dropping»; a mudaf.", "«eklenmesi» — «düşme»ye matuf; muzâf."),
  tok("لَفْظٍ","lafz","noun",[Z, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a word» — mudaf ilayh.", "«bir lafzın» — muzâfun ileyh.", punct=".")]})

# ----------- s2 — 89:22 (as printed)
S.append({"id": "s2", "translation": {
 "en": "As in His saying, exalted is He: «And your Lord CAME» (89:22) — that is, the command of your Lord.",
 "tr": "Allah Teâlâ'nın şu sözü gibi: «Ve Rabbin GELDİ» (Fecr 89:22) — yani Rabbinin emri."},
 "majaz": [mj(3, "nuqsan", None, {"en": "your Lord", "tr": "Rabbin"}, {"en": "the COMMAND of your Lord — the mudaf أَمْرُ is dropped and the mudaf ilayh takes its raf'", "tr": "Rabbinin EMRİ — muzâf أَمْرُ düşmüş, muzâfun ileyh onun ref'ini almış"}, qarina={"en": "the Lord does not come as bodies come", "tr": "Rab, cisimlerin geldiği gibi gelmez"})],
 "tokens": [
  kaq(Z), taala(Z),
  tok("وَجَاءَ","jaa","verb",[Z, "fail"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَجَاءَ فِعْلٌ مَاضٍ — أَجْوَفُ مَهْمُوزُ اللَّامِ.", "«and came» — a hollow verb with a hamza for its last radical.", "«ve geldi» — lâmı hemzeli ecvef fiil.",
      segments=[seg("وَ","wa","conj"), seg("جَاءَ","jaa","verb")]),
  tok("رَبُّكَ","rabb","noun",[Z, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — وَالتَّقْدِيرُ: أَمْرُ رَبِّكَ؛ حُذِفَ الْمُضَافُ وَأُقِيمَ الْمُضَافُ إِلَيْهِ مَقَامَهُ فَأُعْطِيَ إِعْرَابَهُ.", "«your Lord» — the doer in raf'; the taqdir is «the command of your Lord»: the mudaf dropped, the mudaf ilayh set in its place and given its i'rab.", "«Rabbin» — fâil merfû; takdiri «Rabbinin emri»: muzâf düşmüş, muzâfun ileyh yerine geçip i'râbını almış.",
      segments=[seg("رَبُّ","rabb","noun"), seg("كَ","pron-2ms","pron")], punct=".")]})

# ----------- s3 — 12:82 (as printed)
S.append({"id": "s3", "translation": {
 "en": "And His saying: «And ASK THE TOWN» (12:82) — that is, the people of the town.",
 "tr": "Ve şu sözü: «KÖYE SOR» (Yûsuf 12:82) — yani köyün halkına."},
 "majaz": [mj(3, "nuqsan", None, {"en": "the town", "tr": "köy"}, {"en": "the PEOPLE of the town — the mudaf أَهْلَ is dropped and the mudaf ilayh takes its nasb", "tr": "köyün HALKI — muzâf أَهْلَ düşmüş, muzâfun ileyh onun nasbını almış"}, qarina={"en": "a town is not asked", "tr": "köye sorulmaz"})],
 "tokens": [
  wq(), taala(Z),
  tok("وَاسْأَلِ","saala","verb",[Z, "imperative-amr", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَاسْأَلِ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ أَنْتَ.", "«and ask» — the amr, built on the sukun and given a kasra where two sakins meet; the doer «you» concealed of necessity.", "«ve sor» — sükûn üzere mebnî emir, iki sâkin buluşunca kesre almış; fâil vücûben gizli «sen».",
      segments=[seg("وَ","wa","conj"), seg("اسْأَلِ","saala","verb")]),
  tok("الْقَرْيَةَ","qarya","noun",[Z, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — وَالتَّقْدِيرُ: أَهْلَ الْقَرْيَةِ؛ حُذِفَ الْمُضَافُ وَقَامَ الْمُضَافُ إِلَيْهِ مَقَامَهُ فِي النَّصْبِ.", "«the town» — the object; the taqdir «the PEOPLE of the town»: the mudaf dropped, the mudaf ilayh standing in its nasb.", "«köyü» — mef'ûl; takdiri «köyün HALKI»: muzâf düşmüş, muzâfun ileyh onun nasbında.", punct=".")]})

# ----------- s4 — the nukta (RESTORED)
S.append({"id": "s4", "translation": {
 "en": "In the two ayat the MUDAF is dropped and the mudaf ilayh is given its i'rab; this is called a majaz BY OMISSION." + R_EN,
 "tr": "Bu iki âyette MUZÂF düşürülmüş ve muzâfun ileyhe onun i'râbı verilmiştir; buna NOKSAN İLE mecaz denir." + R_TR},
 "tokens": [
  tok("فَفِي","fi","part",[Z, "huruf-jarr"], "الْفَاءُ لِلتَّفْرِيعِ، وَفِي حَرْفُ جَرٍّ.", "«so in».", "«böylece … -de».",
      segments=[seg("فَ","fa","conj"), seg("فِي","fi","part")]),
  tok("الْآيَتَيْنِ","aya","noun",[Z, "huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«the two ayat» — jarr by the ya of the dual.", "«iki âyet» — tesniye yâsıyla mecrur."),
  tok("حُذِفَ","hadhafa","verb",[Z, "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is dropped» — the passive mazi.", "«düşürülmüştür» — meçhûl mâzî."),
  tok("الْمُضَافُ","mudaf","noun",[Z, "naib-al-fail", "ism-maful"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — اسْمُ مَفْعُولِ أَضَافَ.", "«the mudaf» — the deputy doer; ism maf'ul of أَضَافَ.", "«muzâf» — nâib-i fâil; أَضَافَ'nin ism-i mef'ûlü."),
  tok("وَأُعْطِيَ","aata","verb",[Z, "naib-al-fail", "mafulayn", "form-iv-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأُعْطِيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — يَتَعَدَّى إِلَى مَفْعُولَيْنِ، نَابَ الْأَوَّلُ عَنِ الْفَاعِلِ.", "«and is given» — passive; of two objects, the first deputises.", "«ve verilmiştir» — meçhûl; iki mef'ûlden ilki nâib olmuş.",
      segments=[seg("وَ","wa","conj"), seg("أُعْطِيَ","aata","verb")]),
  tok("الْمُضَافُ","mudaf","noun",[Z, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the mudaf» — the deputy doer.", "«muzâf» — nâib-i fâil."),
  tok("إِلَيْهِ","ila","part",[Z, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — تَمَامُ اسْمِ الْمُضَافِ إِلَيْهِ.", "«ilayh» — completing the name «mudaf ilayh».", "«ileyh» — «muzâfun ileyh» adının tamamı.",
      segments=[seg("إِلَيْ","ila","part"), seg("هِ","pron-3ms","pron")]),
  tok("إِعْرَابَهُ","irab","noun",[Z, "mafulayn", "idafa-definiteness"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — إِعْرَابَ الْمُضَافِ.", "«its i'rab» — the second object: the mudaf's i'rab.", "«onun i'râbı» — ikinci mef'ûl: muzâfın i'râbı.",
      segments=[seg("إِعْرَابَ","irab","noun"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("وَيُسَمَّى","samma","verb",[Z, "naib-al-fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُسَمَّى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — هُوَ، أَيْ هَذَا الْمَجَازُ.", "«and it is called» — passive; the deputy doer concealed «it».", "«ve denir» — meçhûl; nâib-i fâil gizli «o».",
      segments=[seg("وَ","wa","conj"), seg("يُسَمَّى","samma","verb")]),
  tok("مَجَازًا","majaz","noun",[Z, "mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a majaz» — the second object.", "«mecaz» — ikinci mef'ûl."),
  tok("بِالنُّقْصَانِ","nuqsan","noun",[Z, "huruf-jarr", "naat-sifa"], "جَارٌّ وَمَجْرُورٌ نَعْتٌ لِمَجَازًا.", "«by omission» — a na't of «majaz».", "«noksan ile» — «mecaz»ın na'ti.",
      segments=[seg("بِ","bi","part"), seg("النُّقْصَانِ","nuqsan","noun")], punct=".")]})

# ----------- s5 — 42:11 (as printed)
S.append({"id": "s5", "translation": {
 "en": "And His saying: «There is nothing LIKE HIS LIKE» (42:11) — that is, nothing like Him.",
 "tr": "Ve şu sözü: «O'NUN MİSLİ GİBİ hiçbir şey yoktur» (Şûrâ 42:11) — yani O'nun gibi hiçbir şey."},
 "majaz": [mj(3, "ziyada", None, {"en": "like His like", "tr": "O'nun misli gibi"}, {"en": "like HIM — the kaf is added, and مِثْل, the khabar of laysa, moves from nasb to jarr", "tr": "O'NUN gibi — kâf eklenmiş; leysenin haberi olan مِثْل nasbdan cerre geçmiş"}, qarina={"en": "God has no like whose like could be denied", "tr": "Allah'ın, misli nefyedilecek bir misli yoktur"})],
 "tokens": [
  wq(), taala(Z),
  tok("لَيْسَ","laysa","verb",[Z, "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ.", "«is not» — the frozen sister of kana.", "«değildir» — kânenin donmuş kardeşi."),
  tok("كَمِثْلِهِ","mithl","noun",[Z, "kana-wa-akhawatuha", "huruf-jarr", "idafa-definiteness"], "الْكَافُ زَائِدَةٌ، وَمِثْلِ مَجْرُورٌ بِهَا لَفْظًا فِي مَحَلِّ نَصْبِ خَبَرِ لَيْسَ الْمُقَدَّمِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«like His like» — the kaf is EXTRA: مِثْل is majrur in wording and in the place of nasb as the fronted khabar of laysa.", "«O'nun misli gibi» — kâf ZÂİD: مِثْل lafzen mecrur, mahallen leysenin öne alınmış haberi olarak mansub.",
      segments=[seg("كَ","ka","part"), seg("مِثْلِ","mithl","noun"), seg("هِ","pron-3ms","pron")]),
  tok("شَيْءٌ","shay","noun",[Z, "kana-wa-akhawatuha"], "اسْمُ لَيْسَ الْمُؤَخَّرُ مَرْفُوعٌ.", "«anything» — the delayed ism of laysa.", "«bir şey» — leysenin sona kalmış ismi.", punct=".")]})

# ----------- s6 — the nukta (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "The KAF was added, so the i'rab of «مِثْل» changed from nasb to jarr; this is called a majaz BY ADDITION." + R_EN,
 "tr": "KÂF eklenmiş, böylece «مِثْل»in i'râbı nasbdan cerre dönmüştür; buna ZİYÂDE İLE mecaz denir." + R_TR},
 "tokens": [
  tok("زِيدَتِ","zada","verb",[Z, "naib-al-fail", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — أَجْوَفُ: زِيدَ؛ وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«was added» — the hollow passive زِيدَ; the ta of the feminine takes a kasra where two sakins meet.", "«eklendi» — ecvef meçhûl زِيدَ; te'nis tâsı iki sâkin buluşunca kesre almış.",
      segments=[seg("زِيدَ","zada","verb"), seg("تِ","ta-tanith","part")]),
  tok("الْكَافُ","kaf","noun",[Z, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — اسْمُ الْحَرْفِ.", "«the kaf» — the deputy doer; the letter's name.", "«kâf» — nâib-i fâil; harfin adı."),
  tok("فَتَغَيَّرَ","taghayyara","verb",[Z, "fail", "form-v-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَتَغَيَّرَ فِعْلٌ مَاضٍ مِنَ الْخَامِسِ.", "«so … changed» — Form V.", "«böylece … değişti» — V. bâb.",
      segments=[seg("فَ","fa","conj"), seg("تَغَيَّرَ","taghayyara","verb")]),
  tok("إِعْرَابُ","irab","noun",[Z, "fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the i'rab of» — the doer; a mudaf.", "«i'râbı» — fâil; muzâf."),
  tok("مِثْلِ","mithl","noun",[Z, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْكَلِمَةُ الْمَحْكِيَّةُ.", "«مِثْل» — mudaf ilayh; the quoted word.", "«مِثْل» — muzâfun ileyh; anılan kelime."),
  tok("مِنَ","min","part",[Z, "huruf-jarr"], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from» — a fatha where two sakins meet.", "«-den» — iki sâkin buluşunca fetha."),
  tok("النَّصْبِ","nasb","noun",[Z, "huruf-jarr"], "مَجْرُورٌ.", "«nasb».", "«nasb»."),
  tok("إِلَى","ila","part",[Z, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  tok("الْجَرِّ","jarr","noun",[Z, "huruf-jarr"], "مَجْرُورٌ.", "«jarr».", "«cer».", punct="،"),
  tok("وَيُسَمَّى","samma","verb",[Z, "naib-al-fail", "mafulayn", "form-ii-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُسَمَّى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it is called» — passive; the deputy doer concealed.", "«ve denir» — meçhûl; nâib-i fâil gizli.",
      segments=[seg("وَ","wa","conj"), seg("يُسَمَّى","samma","verb")]),
  tok("مَجَازًا","majaz","noun",[Z, "mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a majaz» — the second object.", "«mecaz» — ikinci mef'ûl."),
  tok("بِالزِّيَادَةِ","ziyada","noun",[Z, "huruf-jarr", "naat-sifa"], "جَارٌّ وَمَجْرُورٌ نَعْتٌ لِمَجَازًا.", "«by addition» — a na't of «majaz».", "«ziyâde ile» — «mecaz»ın na'ti.",
      segments=[seg("بِ","bi","part"), seg("الزِّيَادَةِ","ziyada","noun")], punct=".")]})

# ----------- s7 — the kinaya's definition (RESTORED matn)
S.append({"id": "s7", "translation": {
 "en": "The KINAYA is a word by which the ENTAILMENT of its meaning is intended, while intending the meaning itself along with it remains permitted." + R_EN,
 "tr": "KİNÂYE, mânâsının LÂZIMI kastedilen, bununla beraber mânâsının kendisinin de kastedilmesi câiz kalan lafızdır." + R_TR},
 "tokens": [
  tok("الْكِنَايَةُ","kinaya","noun",[K, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the kinaya» — the mubtada.", "«kinâye» — mübtedâ."),
  tok("لَفْظٌ","lafz","noun",[K, "mubtada-khabar", "jumla-sifa"], "خَبَرٌ مَرْفُوعٌ — وَالْجُمْلَةُ بَعْدَهُ صِفَةٌ لَهُ.", "«a word» — the khabar; the clause after it describes it.", "«bir lafız» — haber; sonraki cümle sıfatı."),
  tok("أُرِيدَ","arada","verb",[K, "jumla-sifa", "naib-al-fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — أَجْوَفُ: أُرِيدَ؛ وَالْجُمْلَةُ صِفَةٌ لِلَفْظٍ.", "«is intended» — the hollow passive; the clause a sifa of «word».", "«kastedilir» — ecvef meçhûl; cümle «lafız»ın sıfatı.",),
  tok("بِهِ","bi","part",[K, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِأُرِيدَ.", "«by it» — attached to «is intended».", "«onunla» — «kastedilir»e müteallik.",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("لَازِمُ","lazim","noun",[K, "naib-al-fail", "idafa-definiteness", "ism-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ — اسْمُ فَاعِلِ لَزِمَ.", "«the entailment of» — the deputy doer; a mudaf; ism fa'il of لَزِمَ.", "«lâzımı» — nâib-i fâil; muzâf; لَزِمَ'nin ism-i fâili."),
  tok("مَعْنَاهُ","mana","noun",[K, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its meaning» — mudaf ilayh; the kasra estimated on the alif.", "«mânâsının» — muzâfun ileyh; kesre elif üzerinde takdîrî.",
      segments=[seg("مَعْنَا","mana","noun"), seg("هُ","pron-3ms","pron")]),
  tok("مَعَ","maa","noun",[K, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«together with» — a zarf; a mudaf.", "«beraber» — zarf; muzâf."),
  tok("جَوَازِ","jawaz","noun",[K, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — مَصْدَرُ جَازَ.", "«the permissibility of» — mudaf ilayh, itself a mudaf.", "«câiz olması» — muzâfun ileyh, kendisi de muzâf."),
  tok("إِرَادَتِهِ","irada","noun",[K, "idafa-definiteness", "masdar", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ أَرَادَ؛ الضَّمِيرُ لِلْمَعْنَى.", "«intending it» — masdar of أَرَادَ; the pronoun is the meaning's.", "«onun kastedilmesi» — أَرَادَ'nin masdarı; zamir mânânın.",
      segments=[seg("إِرَادَتِ","irada","noun"), seg("هِ","pron-3ms","pron")]),
  tok("مَعَهُ","maa","noun",[K, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَعَ اللَّازِمِ.", "«along with it» — with the entailment.", "«onunla beraber» — lâzımla.",
      segments=[seg("مَعَ","maa","noun"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s8 — the difference from the majaz (RESTORED matn)
S.append({"id": "s8", "translation": {
 "en": "So it is plain that it differs from the MAJAZ in that intending the meaning is permitted along with intending its entailment." + R_EN,
 "tr": "Böylece onun, lâzımının kastıyla beraber mânânın kastının câiz olması cihetinden MECAZA muhalif olduğu ortaya çıktı." + R_TR},
 "tokens": [
  tok("فَظَهَرَ","zahara","verb",[F, "fail"], "الْفَاءُ لِلتَّفْرِيعِ، وَظَهَرَ فِعْلٌ مَاضٍ، وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ فَاعِلُهُ.", "«so it is plain» — the interpreted masdar after it is its doer.", "«böylece ortaya çıktı» — sonraki müevvel masdar fâili.",
      segments=[seg("فَ","fa","conj"), seg("ظَهَرَ","zahara","verb")]),
  tok("أَنَّهَا","anna","part",[F, "inna-wa-akhawatuha"], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهَا اسْمُهُ — الْكِنَايَةُ.", "«that it» — anna with its ism: the kinaya.", "«onun» — enne ve ismi: kinâye.",
      segments=[seg("أَنَّ","anna","part"), seg("هَا","pron-3fs","pron")]),
  tok("تُخَالِفُ","khalafa","verb",[F, "inna-wa-akhawatuha", "form-iii-verbs", "maful-bihi", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مِنَ الثَّالِثِ، وَالْفَاعِلُ مُسْتَتِرٌ — هِيَ؛ وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«differs from» — Form III; the doer concealed «she»; the clause the khabar of anna.", "«muhalif olur» — III. bâb; fâil gizli «o»; cümle ennenin haberi."),
  tok("الْمَجَازَ","majaz","noun",[F, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the majaz» — the object.", "«mecaza» — mef'ûl."),
  tok("مِنْ","min","part",[F, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("جِهَةِ","jiha","noun",[F, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the side of» — a mudaf.", "«ciheti» — muzâf."),
  tok("جَوَازِ","jawaz","noun",[F, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the permissibility of» — mudaf ilayh, a mudaf.", "«câiz olması» — muzâfun ileyh, muzâf."),
  tok("إِرَادَةِ","irada","noun",[F, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«intending» — mudaf ilayh, a mudaf.", "«kastı» — muzâfun ileyh, muzâf."),
  tok("الْمَعْنَى","mana","noun",[F, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the meaning» — mudaf ilayh; the kasra estimated.", "«mânâ» — muzâfun ileyh; kesre takdîrî."),
  tok("مَعَ","maa","noun",[F, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«along with» — a zarf.", "«beraber» — zarf."),
  tok("إِرَادَةِ","irada","noun",[F, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«intending» — mudaf ilayh.", "«kastı» — muzâfun ileyh."),
  tok("لَازِمِهِ","lazim","noun",[F, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its entailment» — mudaf ilayh with its pronoun.", "«lâzımının» — muzâfun ileyh, zamiriyle.",
      segments=[seg("لَازِمِ","lazim","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s9 — Sakkaki's difference (RESTORED matn)
S.append({"id": "s9", "translation": {
 "en": "And SAKKAKI told the two apart by this: in the kinaya the passage is FROM THE ENTAILMENT, and in the majaz FROM THE ENTAILER." + R_EN,
 "tr": "SEKKÂKÎ ikisini şununla ayırdı: kinâyede intikal LÂZIMDAN, mecazda MELZÛMDANDIR." + R_TR},
 "tokens": [
  tok("وَفَرَّقَ","farraqa","verb",[F, "fail", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَفَرَّقَ فِعْلٌ مَاضٍ مِنَ الثَّانِي.", "«and told apart» — Form II.", "«ve ayırdı» — II. bâb.",
      segments=[seg("وَ","wa","conj"), seg("فَرَّقَ","farraqa","verb")]),
  tok("السَّكَّاكِيُّ","sakkaki","noun",[F, "fail", "ism-mansub"], "فَاعِلٌ مَرْفُوعٌ.", "«Sakkaki» — the doer.", "«Sekkâkî» — fâil."),
  tok("بَيْنَهُمَا","bayna","noun",[F, "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُمَا مُضَافٌ إِلَيْهِ — الْكِنَايَةُ وَالْمَجَازُ.", "«between the two» — a zarf with the dual pronoun: the kinaya and the majaz.", "«ikisi arasını» — zarf, tesniye zamiriyle: kinâye ve mecaz.",
      segments=[seg("بَيْنَ","bayna","noun"), seg("هُمَا","pron-3d","pron")]),
  tok("بِأَنَّ","anna","part",[F, "huruf-jarr", "inna-wa-akhawatuha"], "الْبَاءُ جَارَّةٌ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ.", "«by that» — the ba over anna; the interpreted masdar is majrur.", "«şununla» — bâ, enne üzerinde; müevvel masdar mecrur.",
      segments=[seg("بِ","bi","part"), seg("أَنَّ","anna","part")]),
  tok("الِانْتِقَالَ","intiqal","noun",[F, "inna-wa-akhawatuha", "masdar", "form-viii-verbs"], "اسْمُ أَنَّ مَنْصُوبٌ — مَصْدَرُ انْتَقَلَ.", "«the passage» — the ism of anna; masdar of انْتَقَلَ.", "«intikal» — ennenin ismi; انْتَقَلَ'nin masdarı."),
  tok("فِي","fi","part",[F, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْكِنَايَةِ","kinaya","noun",[F, "huruf-jarr"], "مَجْرُورٌ.", "«the kinaya».", "«kinâye»."),
  tok("مِنَ","min","part",[F, "huruf-jarr", "inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ.", "«from» — the jarr phrase is the khabar of anna.", "«-den» — câr-mecrûr ennenin haberi."),
  tok("اللَّازِمِ","lazim","noun",[F, "huruf-jarr", "inna-wa-akhawatuha"], "مَجْرُورٌ — فِي مَحَلِّ رَفْعِ خَبَرِ أَنَّ.", "«the entailment» — the khabar of anna, in the place of raf'.", "«lâzım» — ennenin haberi, ref mahallinde.", punct="،"),
  tok("وَفِي","fi","part",[F, "huruf-jarr", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and in».", "«ve … -de».",
      segments=[seg("وَ","wa","conj"), seg("فِي","fi","part")]),
  tok("الْمَجَازِ","majaz","noun",[F, "huruf-jarr"], "مَجْرُورٌ.", "«the majaz».", "«mecaz»."),
  tok("مِنَ","min","part",[F, "huruf-jarr"], "حَرْفُ جَرٍّ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَالِانْتِقَالُ فِي الْمَجَازِ مِنَ الْمَلْزُومِ.", "«from» — the khabar of a dropped mubtada: «the passage in the majaz is from…».", "«-den» — hazfedilmiş mübtedânın haberi."),
  tok("الْمَلْزُومِ","malzum","noun",[F, "huruf-jarr", "ism-maful"], "مَجْرُورٌ — اسْمُ مَفْعُولِ لَزِمَ.", "«the entailer» — ism maf'ul of لَزِمَ: what the entailment follows from.", "«melzûm» — لَزِمَ'nin ism-i mef'ûlü: lâzımın kendisinden çıktığı şey.", punct=".")]})

# ----------- s10 — the refutation (RESTORED matn)
S.append({"id": "s10", "translation": {
 "en": "And it was answered: as long as the entailment is not itself an entailer, no passage is made from it; so the passage is from the entailer in both." + R_EN,
 "tr": "Şöyle cevap verildi: lâzım, melzûm olmadıkça ondan intikal olmaz; öyleyse intikal ikisinde de melzûmdandır." + R_TR},
 "tokens": [
  tok("وَرُدَّ","radda","verb",[F, "naib-al-fail", "doubled-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَرُدَّ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — مُضَاعَفٌ؛ وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — هُوَ، أَيْ هَذَا الْفَرْقُ.", "«and it was answered» — the doubled passive; the deputy doer concealed: this difference.", "«ve cevap verildi» — muzâaf meçhûl; nâib-i fâil gizli: bu fark.",
      segments=[seg("وَ","wa","conj"), seg("رُدَّ","radda","verb")]),
  tok("بِأَنَّ","anna","part",[F, "huruf-jarr", "inna-wa-akhawatuha"], "الْبَاءُ جَارَّةٌ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ.", "«by that».", "«şununla».",
      segments=[seg("بِ","bi","part"), seg("أَنَّ","anna","part")]),
  tok("اللَّازِمَ","lazim","noun",[F, "inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the entailment» — the ism of anna.", "«lâzım» — ennenin ismi."),
  tok("مَا","ma-masdariyya","part",[F, "hal-ma-man", "maful-fih"], "مَا مَصْدَرِيَّةٌ ظَرْفِيَّةٌ — مُدَّةَ عَدَمِ كَوْنِهِ مَلْزُومًا.", "«as long as» — the masdar-making ma of time: «for the time it is not an entailer».", "«-dıkça» — zarf mânâlı masdariyye mâ: «melzûm olmadığı sürece»."),
  tok("لَمْ","lam","part",[F, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not» — the jazim of the past.", "«-medi» — mâzîye çeviren câzim."),
  tok("يَكُنْ","kana","verb",[F, "lam-jazim", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ، حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهُ مُسْتَتِرٌ — هُوَ.", "«it is» — kana in jazm; its middle letter dropped where two sakins meet; its ism concealed «it».", "«olmaz» — cezmde kâne; iki sâkin buluşunca orta harfi düşmüş; ismi gizli «o»."),
  tok("مَلْزُومًا","malzum","noun",[F, "kana-wa-akhawatuha", "ism-maful"], "خَبَرُ يَكُنْ مَنْصُوبٌ.", "«an entailer» — the khabar of kana.", "«melzûm» — kânenin haberi."),
  tok("لَمْ","lam","part",[F, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-mez»."),
  tok("يَنْتَقِلْ","intaqala","verb",[F, "lam-jazim", "inna-wa-akhawatuha", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، مِنَ الِافْتِعَالِ، وَالْفَاعِلُ مُسْتَتِرٌ — هُوَ، أَيِ الذِّهْنُ؛ وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«no passage is made» — jazm by lam; Form VIII; the doer concealed «it», the mind; the clause the khabar of anna.", "«intikal olmaz» — lem ile cezm; VIII. bâb; fâil gizli «o», zihin; cümle ennenin haberi."),
  tok("مِنْهُ","min","part",[F, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — مِنَ اللَّازِمِ.", "«from it» — from the entailment.", "«ondan» — lâzımdan.",
      segments=[seg("مِنْ","min","part"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("فَيَكُونُ","kana","verb",[F, "kana-wa-akhawatuha", "hollow-verbs", "mudari-marfu"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.", "«so … is» — kana in raf'.", "«öyleyse … olur» — merfû kâne.",
      segments=[seg("فَ","fa","conj"), seg("يَكُونُ","kana","verb")]),
  tok("الِانْتِقَالُ","intiqal","noun",[F, "kana-wa-akhawatuha", "masdar"], "اسْمُ يَكُونُ مَرْفُوعٌ.", "«the passage» — the ism of kana.", "«intikal» — kânenin ismi."),
  tok("مِنَ","min","part",[F, "huruf-jarr", "kana-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُونُ.", "«from» — the jarr phrase is the khabar of kana.", "«-den» — câr-mecrûr kânenin haberi."),
  tok("الْمَلْزُومِ","malzum","noun",[F, "huruf-jarr", "kana-wa-akhawatuha"], "مَجْرُورٌ — فِي مَحَلِّ نَصْبِ خَبَرِ يَكُونُ.", "«the entailer» — the khabar of kana, in the place of nasb.", "«melzûm» — kânenin haberi, nasb mahallinde.", punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "fasl": find_gloss("fasl"), "qad": find_gloss("qad"), "majaz": find_gloss("majaz"), "ala": find_gloss("ala"), "kalima": find_gloss("kalima"),
 "atlaqa": G("atlaqa", "أَطْلَقَ", "ط ل ق", "verb", "to apply (a word) to; to set free (Form IV)", "(bir lafzı) ıtlak etmek, söylemek; salıvermek (IV. bâb)", 4, form="IV"),
 "taghayyara": G("taghayyara", "تَغَيَّرَ", "غ ي ر", "verb", "to change, be altered (Form V)", "değişmek (V. bâb)", 3, form="V"),
 "hukm": find_gloss("hukm"), "irab": find_gloss("irab"), "lafz": find_gloss("lafz"), "aw": find_gloss("aw"), "ziyada": find_gloss("ziyada"),
 "hadhf": G("hadhf", "حَذْف", "ح ذ ف", "noun", "dropping, ellipsis (masdar of حَذَفَ)", "hazif, düşürme (حَذَفَ'nin masdarı)", 4),
 "qawl": find_gloss("qawl"), "taala": find_gloss("taala"), "jaa": find_gloss("jaa"), "rabb": find_gloss("rabb"), "saala": find_gloss("saala"), "qarya": find_gloss("qarya"),
 "fi": find_gloss("fi"), "aya": find_gloss("aya"), "hadhafa": find_gloss("hadhafa"),
 "mudaf": G("mudaf", "مُضَاف", "ض ي ف", "noun", "the mudaf — the annexed head of an idafa (ism maf'ul of أَضَافَ)", "muzâf — izâfetin baş kelimesi (أَضَافَ'nin ism-i mef'ûlü)", 3),
 "aata": find_gloss("aata"), "ila": find_gloss("ila"), "samma": find_gloss("samma"), "nuqsan": find_gloss("nuqsan"),
 "laysa": find_gloss("laysa"), "mithl": find_gloss("mithl"), "shay": find_gloss("shay"), "zada": find_gloss("zada"),
 "kaf": G("kaf", "الْكَاف", None, "noun", "the letter kaf — as a name", "kâf harfi — ad olarak", 3),
 "nasb": G("nasb", "نَصْب", "ن ص ب", "noun", "nasb — the accusative case", "nasb — nasb hâli", 3),
 "jarr": G("jarr", "جَرّ", "ج ر ر", "noun", "jarr — the genitive case", "cer — cer hâli", 3),
 "min": find_gloss("min"), "kinaya": find_gloss("kinaya"), "arada": find_gloss("arada"), "bi": find_gloss("bi"), "lazim": find_gloss("lazim"),
 "mana": find_gloss("mana"), "maa": find_gloss("maa"),
 "jawaz": G("jawaz", "جَوَاز", "ج و ز", "noun", "permissibility (masdar of جَازَ)", "câiz olma, cevaz (جَازَ'nin masdarı)", 4),
 "irada": G("irada", "إِرَادَة", "ر و د", "noun", "intending, will (masdar of أَرَادَ)", "kasıt, irâde (أَرَادَ'nin masdarı)", 3),
 "zahara": find_gloss("zahara"), "anna": find_gloss("anna"),
 "khalafa": G("khalafa", "خَالَفَ", "خ ل ف", "verb", "to contradict, go against; to differ from (Form III)", "muhalif olmak, aykırı düşmek (III. bâb)", 3, form="III"),
 "jiha": find_gloss("jiha"),
 "farraqa": G("farraqa", "فَرَّقَ", "ف ر ق", "verb", "to tell apart, distinguish (Form II)", "ayırmak, fark koymak (II. bâb)", 3, form="II"),
 "sakkaki": find_gloss("sakkaki"), "bayna": find_gloss("bayna"), "intiqal": find_gloss("intiqal"),
 "malzum": G("malzum", "مَلْزُوم", "ل ز م", "noun", "the entailer — what an entailment follows from (ism maf'ul of لَزِمَ)", "melzûm — lâzımın kendisinden çıktığı şey (لَزِمَ'nin ism-i mef'ûlü)", 5),
 "radda": find_gloss("radda"), "ma-masdariyya": find_gloss("ma-masdariyya"), "lam": find_gloss("lam"), "kana": find_gloss("kana"), "intaqala": find_gloss("intaqala"),
 "wa": find_gloss("wa"), "fa": find_gloss("fa"), "ka": find_gloss("ka"), "pron-3ms": find_gloss("pron-3ms"), "pron-3fs": find_gloss("pron-3fs"), "pron-2ms": find_gloss("pron-2ms"),
 "pron-3d": G("pron-3d", "هُمَا", None, "pron", "they two / them two (attached dual pronoun)", "o ikisi (bitişik tesniye zamiri)", 2),
 "ta-tanith": find_gloss("ta-tanith"),
}

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "atlaqa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَطْلَق", "طْلِق", "أَطْلِق", "إِطْلَاق", "مُطْلِق", "مُطْلَق", "أُطْلِقَ", "يُطْلَقُ",
                                    "فِي الْمَتْنِ مَبْنِيٌّ لِلْمَجْهُولِ: يُطْلَقُ الْمَجَازُ."))
put_morph(mo, "taghayyara", _sg.derived(_sg.B5, _sg.W5, "َ", "تَغَيَّر", "تَغَيَّر", "تَغَيَّر", "تَغَيُّر", "مُتَغَيِّر", None, None, None,
                                        "لَازِمٌ: تَغَيَّرَ الْحُكْمُ."))
put_morph(mo, "khalafa", _sg.derived(_sg.B3, _sg.W3, "ُ", "خَالَف", "خَالِف", "خَالِف", "مُخَالَفَة", "مُخَالِف", "مُخَالَف", "خُولِفَ", "يُخَالَفُ"))
put_morph(mo, "farraqa", _sg.derived(_sg.B2, _sg.W2, "ُ", "فَرَّق", "فَرِّق", "فَرِّق", "تَفْرِيق", "مُفَرِّق", "مُفَرَّق", "فُرِّقَ", "يُفَرَّقُ"))
for k in ("zahara", "hadhafa", "zada", "aata", "samma", "saala", "jaa", "radda", "intaqala", "arada", "kana"):
    if k not in mo["verbs"] and has_morph(k): mo["verbs"][k] = find_morph(k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_Z = {
 "id": "majaz-ziyada-nuqsan",
 "title": {"ar": "الْمَجَازُ بِالنُّقْصَانِ وَبِالزِّيَادَةِ — الْإِعْرَابُ الَّذِي انْتَقَلَ", "en": "The majaz by omission and by addition — the i'rab that moved", "tr": "Noksan ve ziyâde ile mecaz — yer değiştiren i'rab"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — فصل: قد يطلق المجاز على كلمة تغير حكم إعرابها"],
 "question": {
  "en": ["Did a word DROP OUT and hand its i'rab to its neighbour? وَاسْأَلِ الْقَرْيَةَ: the mudaf أَهْلَ is gone and the mudaf ilayh wears its nasb — the majaz BY OMISSION.",
         "Was a letter ADDED that changed the i'rab? لَيْسَ كَمِثْلِهِ شَيْءٌ: the kaf is extra, and مِثْل, the khabar of laysa that should be mansub, stands in jarr — the majaz BY ADDITION.",
         "Is any MEANING moved? No: this «majaz» is a name for the i'rab's move, not for a word used off its sense. That is why the Talkhis says the word majaz is merely APPLIED to it."],
  "tr": ["Bir kelime DÜŞÜP i'râbını komşusuna mı verdi? وَاسْأَلِ الْقَرْيَةَ: muzâf أَهْلَ gitmiş, muzâfun ileyh onun nasbını giymiş — NOKSAN İLE mecaz.",
         "İ'râbı değiştiren bir harf mi EKLENDİ? لَيْسَ كَمِثْلِهِ شَيْءٌ: kâf zâid; leysenin mansub olması gereken haberi مِثْل cerde — ZİYÂDE İLE mecaz.",
         "Bir MÂNÂ mı kaymış? Hayır: bu «mecaz», i'râbın kaymasının adıdır, mânâsından kaydırılmış kelimenin değil. Telhîs bu yüzden mecaz lafzının ona yalnız ITLAK olunduğunu söyler."]},
 "plain": {
  "en": "Two things are also CALLED majaz though no meaning moves: a word that took its dropped neighbour's i'rab (وَاسْأَلِ الْقَرْيَةَ — «the people of» is gone) and a word whose i'rab an added letter changed (لَيْسَ كَمِثْلِهِ — the kaf is extra). The engine restores the dropped mudaf as a ghost and marks the extra kaf.",
  "tr": "Mânâ kaymadığı hâlde iki şeye de mecaz DENİR: düşen komşusunun i'râbını alan kelime (وَاسْأَلِ الْقَرْيَةَ — «halkı» gitmiş) ve eklenen bir harfin i'râbını değiştirdiği kelime (لَيْسَ كَمِثْلِهِ — kâf zâid). Motor ikisini nahivden okur: düşen muzâfı hayâlet olarak, zâid kâfı olamayacak bir cer olarak."},
 "explanation": {
  "en": "The Talkhis closes the majaz with a caution: the word majaz is SOMETIMES APPLIED (قَدْ يُطْلَقُ) to a word whose rule of i'rab CHANGED by the dropping of a word or the adding of one. In وَجَاءَ رَبُّكَ (89:22) and وَاسْأَلِ الْقَرْيَةَ (12:82) the MUDAF is dropped — أَمْرُ, أَهْلَ — and the mudaf ilayh is GIVEN ITS I'RAB: رَبُّكَ takes the doer's raf' that belonged to «the command», الْقَرْيَةَ the object's nasb that belonged to «the people». This is the majaz BY OMISSION (بِالنُّقْصَانِ). In لَيْسَ كَمِثْلِهِ شَيْءٌ (42:11) a KAF is ADDED, and مِثْل — the khabar of laysa, which should be mansub — passes from nasb to jarr: the majaz BY ADDITION (بِالزِّيَادَةِ). Neither is a word used off its meaning; both are named majaz because the i'rab «passed over» (جَازَ) to a place that is not its own. WHAT THE ENGINE CLAIMS: the omission it reads as a GHOST — the TaqdirEngine restores the dropped mudaf where a verb of asking takes a place as its object, and the arc map draws the restored word dashed; the addition it reads off the nahw — a kaf whose majrur must fill laysa's khabar seat is marked extra, and the CaseEngine keeps the seat's nasb beside the wording's jarr (مَجْرُورٌ لَفْظًا فِي مَحَلِّ نَصْبٍ).",
  "tr": "Telhîs mecazı bir ihtarla kapatır: mecaz lafzı BAZEN, bir lafzın düşmesi yahut eklenmesiyle i'râb hükmü DEĞİŞEN kelimeye de ITLAK OLUNUR (قَدْ يُطْلَقُ). وَجَاءَ رَبُّكَ (Fecr 89:22) ve وَاسْأَلِ الْقَرْيَةَ (Yûsuf 12:82)'de MUZÂF düşmüş — أَمْرُ, أَهْلَ — ve muzâfun ileyhe ONUN İ'RÂBI VERİLMİŞTİR: رَبُّكَ «emr»in fâil ref'ini, الْقَرْيَةَ «halk»ın mef'ûl nasbını alır. Bu NOKSAN İLE (بِالنُّقْصَانِ) mecazdır. لَيْسَ كَمِثْلِهِ شَيْءٌ (Şûrâ 42:11)'de bir KÂF EKLENMİŞ ve leysenin mansub olması gereken haberi مِثْل nasbdan cerre geçmiştir: ZİYÂDE İLE (بِالزِّيَادَةِ) mecaz. İkisi de mânâsından kaydırılmış kelime değildir; i'râb kendi olmayan bir yere «geçtiği» (جَازَ) için mecaz adını alır. MOTORUN İDDİASI: noksanı HAYÂLET olarak okur — TakdirEngine, sorma fiili bir yeri mef'ûl aldığında düşen muzâfı geri koyar ve i'rab haritası geri konan kelimeyi kesikli çizer; ziyâdeyi nahivden okur — mecrûru leysenin haber makamını doldurmak zorunda olan kâf zâid işaretlenir ve CaseEngine, lafzın cerinin yanında makamın nasbını tutar (مَجْرُورٌ لَفْظًا فِي مَحَلِّ نَصْبٍ)."},
 "examples": [
  {"ar": "وَاسْأَلِ الْقَرْيَةَ", "en": "the mudaf أَهْلَ dropped; its nasb on الْقَرْيَةَ.", "tr": "muzâf أَهْلَ düşmüş; nasbı الْقَرْيَةَ üzerinde.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "وَجَاءَ رَبُّكَ", "en": "the mudaf أَمْرُ dropped; its raf' on رَبُّكَ.", "tr": "muzâf أَمْرُ düşmüş; ref'i رَبُّكَ üzerinde.", "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "لَيْسَ كَمِثْلِهِ شَيْءٌ", "en": "the kaf added; مِثْل in jarr where laysa's khabar should be mansub.", "tr": "kâf eklenmiş; leysenin haberi mansub olacakken مِثْل cerde.", "sourceStory": "talkhis-al-miftah", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«وَاسْأَلِ الْقَرْيَةَ'de الْقَرْيَة halk için mecâz-ı mürseldir (mahalliyye)»",
   "right": "«Muzâf hazfi vardır: أَهْلَ düşmüş, الْقَرْيَة onun nasbını almıştır — noksan ile mecaz»",
   "why": {"en": "The Talkhis files this ayah under the i'rab's move, not under a relation between two meanings. The word «town» keeps its sense; a word is missing before it.", "tr": "Telhîs bu âyeti iki mânâ arasındaki bir alâkaya değil i'râbın kaymasına bağlar. «Köy» mânâsını korur; önünde bir kelime eksiktir."}},
  {"wrong": "«لَيْسَ كَمِثْلِهِ شَيْءٌ: Allah'ın mislinin misli yoktur»",
   "right": "«Kâf zâiddir: Allah'ın misli yoktur — مِثْل, leysenin haberidir»",
   "why": {"en": "Read with the kaf as real, the ayah would affirm a like of God whose like is denied. The added letter changes only the i'rab, never the sense.", "tr": "Kâf gerçek sayılırsa âyet, misli nefyedilen bir Allah misli isbat ederdi. Zâid harf yalnız i'râbı değiştirir, mânâyı asla."}}],
 "relatedNotes": ["haqiqa-majaz", "majaz-mursal", "idafa-definiteness", "kana-wa-akhawatuha", "kinaya", "farq-al-kinaya-wal-majaz"]}
NOTE_F = {
 "id": "farq-al-kinaya-wal-majaz",
 "title": {"ar": "الْفَرْقُ بَيْنَ الْكِنَايَةِ وَالْمَجَازِ — جَوَازُ إِرَادَةِ الْمَعْنَى", "en": "The kinaya told from the majaz — the literal sense stays permitted", "tr": "Kinâyenin mecazdan farkı — hakikî mânâ câiz kalır"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — الكناية: لفظ أريد به لازم معناه مع جواز إرادته معه"],
 "question": {
  "en": ["May the LITERAL sense still be meant? طَوِيلُ النِّجَادِ — the sword-belt may really be long, AND the man tall. Both stand: a KINAYA. In رَأَيْتُ أَسَدًا the man cannot also be a lion: a MAJAZ, whose clue bars the literal sense.",
         "From WHICH side does the mind pass? Sakkaki: in the kinaya from the entailment (the long belt) to the entailer (the tall man), in the majaz from the entailer to the entailment.",
         "Does that hold? The Talkhis answers no: an entailment is only passed from once it is itself an entailer — so in both the passage is from the entailer."],
  "tr": ["HAKİKÎ mânâ hâlâ kastedilebilir mi? طَوِيلُ النِّجَادِ — kılıç kayışı gerçekten uzun VE adam uzun boylu olabilir. İkisi de durur: KİNÂYE. رَأَيْتُ أَسَدًا'da adam aynı zamanda arslan olamaz: karînesi hakikati engelleyen MECAZ.",
         "Zihin HANGİ taraftan geçer? Sekkâkî: kinâyede lâzımdan (uzun kayış) melzûma (uzun boylu adam), mecazda melzûmdan lâzıma.",
         "Bu tutar mı? Telhîs hayır der: bir lâzımdan ancak kendisi melzûm olunca geçilir — öyleyse ikisinde de intikal melzûmdandır."]},
 "plain": {
  "en": "A kinaya means a word's ENTAILMENT while the word's own meaning stays permitted; a majaz bars that meaning. The engine tests the surface: a clue that refuses the literal reading makes a majaz, a wording the literal reading survives makes a kinaya candidate.",
  "tr": "Kinâye, kelimenin kendi mânâsı câiz kalırken LÂZIMINI kasteder; mecaz o mânâyı engeller. Motor yüzeyi sınar: hakikî okumayı reddeden karîne mecaz yapar; hakikî okumanın hayatta kaldığı ifade kinâye adayı yapar."},
 "explanation": {
  "en": "The KINAYA is لَفْظٌ أُرِيدَ بِهِ لَازِمُ مَعْنَاهُ مَعَ جَوَازِ إِرَادَتِهِ مَعَهُ — a word by which the ENTAILMENT of its meaning is intended, while intending the meaning itself along with it remains PERMITTED. From this it is plain how it DIFFERS FROM THE MAJAZ: in the majaz a clue BARS the literal meaning (a man is not a lion), in the kinaya nothing bars it — طَوِيلُ النِّجَادِ may be said of a tall man whose belt really is long. SAKKAKI told the two apart otherwise: in the kinaya the mind PASSES FROM THE ENTAILMENT (the long belt) to the entailer (the tall body), in the majaz from the entailer to the entailment. The Talkhis REFUTES it: an entailment is not passed from unless it is itself an ENTAILER of the thing reached — the long belt entails the tall body only because tall bodies wear long belts — so that in both the passage is from the entailer; the true difference is the one stated first, the permitted literal sense. WHAT THE ENGINE CLAIMS: for every majaz frame it names the clue that bars the literal sense; for a kinaya candidate it reports that no such clue was found and that the literal reading survives — the sifa-shaped head really describes its annexed noun (كَثِيرُ الرَّمَادِ: the ash really is much). It does not decide the entailment; that is the reader's knowledge, carried on the authored rungs.",
  "tr": "KİNÂYE لَفْظٌ أُرِيدَ بِهِ لَازِمُ مَعْنَاهُ مَعَ جَوَازِ إِرَادَتِهِ مَعَهُ'dur — mânâsının LÂZIMI kastedilen, bununla beraber mânâsının kendisinin de kastedilmesi CÂİZ kalan lafız. Buradan MECAZDAN FARKI ortaya çıkar: mecazda bir karîne hakikî mânâyı ENGELLER (adam arslan değildir), kinâyede hiçbir şey engellemez — طَوِيلُ النِّجَادِ, kayışı gerçekten uzun olan uzun boylu bir adam için söylenebilir. SEKKÂKÎ ikisini başka türlü ayırdı: kinâyede zihin LÂZIMDAN (uzun kayış) melzûma (uzun boy), mecazda melzûmdan lâzıma GEÇER. Telhîs REDDEDER: bir lâzımdan, ulaşılan şeyin MELZÛMU olmadıkça geçilmez — uzun kayış uzun boyu ancak uzun boylular uzun kayış taktığı için gerektirir — öyleyse ikisinde de intikal melzûmdandır; gerçek fark önce söylenendir: hakikî mânânın câiz kalması. MOTORUN İDDİASI: her mecaz çerçevesi için hakikati engelleyen karîneyi adlandırır; kinâye adayı için böyle bir karîne bulunmadığını ve hakikî okumanın hayatta kaldığını bildirir — sıfat şekilli baş, izâfe edildiği ismi gerçekten vasfeder (كَثِيرُ الرَّمَادِ: kül gerçekten çoktur). Lâzımı motor karara bağlamaz; o, müellifin basamaklarında taşınan okuyucu bilgisidir."},
 "examples": [
  {"ar": "لَفْظٌ أُرِيدَ بِهِ لَازِمُ مَعْنَاهُ مَعَ جَوَازِ إِرَادَتِهِ مَعَهُ", "en": "the definition.", "tr": "tarif.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"},
  {"ar": "الِانْتِقَالُ فِي الْكِنَايَةِ مِنَ اللَّازِمِ وَفِي الْمَجَازِ مِنَ الْمَلْزُومِ", "en": "Sakkaki's difference.", "tr": "Sekkâkî'nin farkı.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"},
  {"ar": "اللَّازِمُ مَا لَمْ يَكُنْ مَلْزُومًا لَمْ يَنْتَقِلْ مِنْهُ", "en": "the refutation.", "tr": "reddi.", "sourceStory": "talkhis-al-miftah", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«Kinâye de mecazdır: طَوِيلُ النِّجَادِ'da kayış değil boy kastedilir»",
   "right": "«Kinâyedir: boy kastedilir, fakat kayışın uzunluğu da câiz kalır — mecazda hakikat engellenir, kinâyede engellenmez»",
   "why": {"en": "The one line between the two is the permitted literal sense. Where a clue forbids it, the word is a majaz; where nothing forbids it, a kinaya.", "tr": "İkisi arasındaki tek çizgi câiz kalan hakikî mânâdır. Bir karîne onu yasaklarsa mecaz, yasaklamazsa kinâyedir."}},
  {"wrong": "«Sekkâkî'nin farkı doğrudur: kinâyede intikal lâzımdandır»",
   "right": "«Telhîs reddeder: lâzım, melzûm olmadıkça ondan intikal olmaz; ikisinde de melzûmdandır»",
   "why": {"en": "A thing is passed from only because it entails what is reached. So every passage starts from an entailer, and Sakkaki's line does not divide.", "tr": "Bir şeyden ancak ulaşılanı gerektirdiği için geçilir. Öyleyse her intikal bir melzûmdan başlar; Sekkâkî'nin çizgisi ayırmaz."}}],
 "relatedNotes": ["kinaya", "haqiqa-majaz", "majaz-ziyada-nuqsan", "aqsam-al-kinaya", "istiara", "istiara-makniyya"]}
# the kinaya note moves in with the bayan door
_kn = GR / "kinaya.json"
_k = json.loads(_kn.read_text(encoding="utf-8"))
if _k.get("group") != "bayan":
    _k["group"] = "bayan"; _kn.write_text(json.dumps(_k, ensure_ascii=False, indent=1), encoding="utf-8")

ADD_EN = (" Chapter 55 (lines ~3874-3890, sahifa 133-134) carries the faṣl on the majaz by omission and by addition and the "
          "kinaya's definition with its difference from the majaz: the three ayat (s2 89:22, s3 12:82, s5 42:11) are Arabic as "
          "the source prints them. s1, s4 and s6-s10 are RESTORATIONS, not quotations: the source carries those steps only in "
          "Ottoman-Turkish paraphrase, and the Arabic restores the matn's wording in the musannif's register; each is marked "
          "«restored» in its translation. s2, s3 and s5 carry `nuqsan` / `ziyada` majaz frames.")
ADD_TR = (" Elli beşinci bâb (satır ~3874-3890, sahife 133-134) noksan ve ziyâde ile mecaz faslını ve kinâyenin tarifini mecazdan "
          "farkıyla taşır: üç âyet (s2 Fecr 89:22, s3 Yûsuf 12:82, s5 Şûrâ 42:11) kaynağın bastığı Arapçadır. s1, s4 ve s6-s10 "
          "ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın ifadesini "
          "musannifin üslûbunda geri yazar; her biri tercümesinde «geri yazılmıştır» diye işaretlidir. s2, s3 ve s5 `nuqsan` / "
          "`ziyada` mecaz çerçevesi taşır.")
write_out(55, S, TITLE, ADD_EN, ADD_TR, "3874-3890", GLOSS_ADD, notes=(NOTE_Z, NOTE_F),
          related=(("kinaya", ["farq-al-kinaya-wal-majaz", "majaz-ziyada-nuqsan"]), ("haqiqa-majaz", ["majaz-ziyada-nuqsan"]), ("majaz-mursal", ["majaz-ziyada-nuqsan"])))
report(55, S, GLOSS_ADD, (NOTE_Z, NOTE_F))
