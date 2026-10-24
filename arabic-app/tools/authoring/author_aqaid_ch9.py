# -*- coding: utf-8 -*-
"""Author chapter 9 of aqaid-ahl-al-sunna — the grave sin, shafa'a and iman.

Continues the matn after the sam'iyyat: a major sin does not put the
believer outside faith, shirk alone is unforgiven, intercession is
established, and iman is defined — التَّصْدِيقُ وَالْإِقْرَار. Verbatim
contiguous spans re-vowelled against the received text; each sentence
stops at a matn period and no clause is skipped from the middle.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/aqaid-ahl-al-sunna"
sys.path.insert(0, str(ROOT / "tools/authoring"))
import sarf_gen as _sg
DIA = re.compile("[ً-ٰ]")
def bare(s): return DIA.sub("", s)
def tok(full, lex, pos, grammar, ar, en, tr, punct=None, segments=None):
    t = {"surface": {"full": full, "smart": full, "bare": bare(full)}, "lex": lex, "pos": pos}
    if grammar: t["grammar"] = grammar
    t["irab"] = {"ar": ar, "en": en, "tr": tr}
    if segments: t["segments"] = segments
    if punct: t["punctAfter"] = punct
    return t
def seg(form, lex, pos): return {"form": form, "lex": lex, "pos": pos}
J = lambda text, ar, en, tr: {"text": text, "ar": ar, "en": en, "tr": tr}
S = []

S.append({"id": "s1", "translation": {
 "en": "And the grave sin does not take the believing servant out of faith, nor does it enter him into unbelief.",
 "tr": "Büyük günah, mü'min kulu imandan çıkarmaz; onu küfre de sokmaz."},
 "tokens": [
  tok("وَالْكَبِيرَةُ","kabira","noun",["mubtada-khabar","sifa-mushabbaha"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الْكَبِيرَةُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "Isti'naf waw; الْكَبِيرَة is the mubtada in raf'.",
      "İstinâf vâvı; «الْكَبِيرَةُ» merfû mübtedadır.",
      segments=[seg("وَ","wa","conj"), seg("الْكَبِيرَةُ","kabira","noun")]),
  tok("لَا","la-nafiya","part",[],
      "«لَا» نَافِيَةٌ غَيْرُ عَامِلَةٍ.",
      "The negating la — it governs nothing.",
      "Amel etmeyen nefiy lâsıdır."),
  tok("تُخْرِجُ","akhraja","verb",["mudari-marfu","form-iv-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مِنْ «أَخْرَجَ»، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A mudari in raf' from أَخْرَجَ (Form IV); the clause stands as the khabar, in raf' position.",
      "«أَخْرَجَ» (if'âl) fiilinin merfû muzârisi; cümle haber olarak mahallen merfûdur."),
  tok("الْعَبْدَ","abd","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "The direct object, in nasb.",
      "Mensub mef'ûlün bihtir."),
  tok("الْمُؤْمِنَ","mumin","noun",["naat-sifa","ism-fail"],
      "نَعْتٌ مَنْصُوبٌ تَابِعٌ لِـ«الْعَبْدَ».",
      "A na't in nasb, following الْعَبْد.",
      "«الْعَبْدَ»ye tâbi mensub na'ttır."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلِابْتِدَاءِ.",
      "The jarr letter of starting-point.",
      "İbtidâ bildiren cer harfidir."),
  tok("الْإِيمَانِ","iman","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«مِنْ».",
      "In jarr after مِنْ.",
      "«مِنْ» ile mecrurdur.", punct="،"),
  tok("وَلَا","la-nafiya","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ.",
      "Joining waw; the لا negates.",
      "Atıf vâvı; «لَا» nefiy içindir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("تُدْخِلُهُ","adkhala","verb",["mudari-marfu","form-iv-verbs","maful-bihi"],
      "مَعْطُوفٌ عَلَى «تُخْرِجُ» — مُضَارِعٌ مِنْ «أَدْخَلَ»، وَالْهَاءُ مَفْعُولٌ بِهِ.",
      "Joined to تُخْرِجُ — a mudari of أَدْخَلَ; the ha is its object.",
      "«تُخْرِجُ»e ma'tûf — «أَدْخَلَ» fiilinin muzârisi; hâ zamiri mef'ûlün bihtir.",
      segments=[seg("تُدْخِلُ","adkhala","verb"), seg("هُ","pron-3ms","pron")]),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfidir."),
  tok("الْكُفْرِ","kufr","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي».",
      "In jarr after فِي.",
      "«فِي» ile mecrurdur.", punct="."),
 ],
 "jumal": [
  J("وَالْكَبِيرَةُ لَا تُخْرِجُ الْعَبْدَ الْمُؤْمِنَ مِنَ الْإِيمَانِ",
    "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا.",
    "A resumed nominal clause — i'rabless.",
    "Müste'nefe isim cümlesi — mahalsizdir."),
  J("لَا تُخْرِجُ الْعَبْدَ الْمُؤْمِنَ",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
    "A verbal clause standing as the mubtada's khabar, in raf' position.",
    "Mübtedanın haberi olarak mahallen merfû fiil cümlesi.")]})

S.append({"id": "s2", "translation": {
 "en": "And intercession is established for the messengers and the best of people, in the matter of those guilty of grave sins.",
 "tr": "Şefaat, büyük günah sahipleri hakkında rasûller ve seçkinler için sabittir."},
 "tokens": [
  tok("وَالشَّفَاعَةُ","shafaa","noun",["mubtada-khabar","masdar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الشَّفَاعَةُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "Isti'naf waw; الشَّفَاعَة is the mubtada in raf'.",
      "İstinâf vâvı; «الشَّفَاعَةُ» merfû mübtedadır.",
      segments=[seg("وَ","wa","conj"), seg("الشَّفَاعَةُ","shafaa","noun")]),
  tok("ثَابِتَةٌ","thabit","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مُؤَنَّثٌ.",
      "The khabar in raf' — a feminine ism fa'il.",
      "Merfû haber — müennes ism-i fâildir."),
  tok("لِلرُّسُلِ","li","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«ثَابِتَةٌ».",
      "Preposition-phrase attached to ثَابِتَة.",
      "«ثَابِتَةٌ»a mütealliḳ câr-mecrûr.",
      segments=[seg("لِ","li","prep"), seg("الرُّسُلِ","rusul","noun")]),
  tok("وَالْأَخْيَارِ","akhyar","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ — جَمْعُ «خَيِّر».",
      "Joined in jarr — the plural of خَيِّر.",
      "Ma'tûf, mecrur — «خَيِّر» kelimesinin cem'idir.",
      segments=[seg("وَ","wa","conj"), seg("الْأَخْيَارِ","akhyar","noun")]),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfidir."),
  tok("حَقِّ","haqq","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ وَهُوَ مُضَافٌ — «فِي حَقِّ» بِمَعْنَى «فِي شَأْنِ».",
      "In jarr and a mudaf — فِي حَقِّ means «in the matter of».",
      "Mecrur ve muzâf — «فِي حَقِّ», «hakkında» manasındadır."),
  tok("أَهْلِ","ahl","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "Mudaf ilayh in jarr, itself a mudaf.",
      "Mecrûr muzâfun ileyh ve muzâftır."),
  tok("الْكَبَائِرِ","kabair","noun",["idafa-definiteness","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — «الْكَبَائِر» صِيغَةُ مُنْتَهَى الْجُمُوعِ، جُرَّتْ بِالْكَسْرَةِ لِدُخُولِ «أَلْ».",
      "Mudaf ilayh in jarr — الْكَبَائِر is a diptote, taking the kasra because ال has entered it.",
      "Mecrûr muzâfun ileyh — «الْكَبَائِر» gayr-i munsariftir; «el» girdiği için kesra ile mecrurdur.", punct="."),
 ],
 "jumal": [J("وَالشَّفَاعَةُ ثَابِتَةٌ لِلرُّسُلِ وَالْأَخْيَارِ",
   "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا.",
   "A resumed nominal clause — i'rabless.",
   "Müste'nefe isim cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And those guilty of grave sins among the believers do not abide forever in the fire.",
 "tr": "Mü'minlerden büyük günah sahipleri ateşte ebedî kalmazlar."},
 "tokens": [
  tok("وَأَهْلُ","ahl","noun",["mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَ«أَهْلُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "Joining waw; أَهْل is the mubtada in raf', itself a mudaf.",
      "Atıf vâvı; «أَهْلُ» merfû mübteda ve muzâftır.",
      segments=[seg("وَ","wa","conj"), seg("أَهْلُ","ahl","noun")]),
  tok("الْكَبَائِرِ","kabair","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "Mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyhtir."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلتَّبْعِيضِ.",
      "The jarr letter of partition — «some of».",
      "Teb'îz bildiren cer harfidir — «-den bir kısmı»."),
  tok("الْمُؤْمِنِينَ","mumin","noun",["huruf-jarr","jam-mudhakkar-salim"],
      "مَجْرُورٌ بِالْيَاءِ — جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "In jarr by the ya — a sound masculine plural.",
      "Yâ ile mecrur — cem'-i müzekker-i sâlimdir."),
  tok("لَا","la-nafiya","part",[],
      "«لَا» نَافِيَةٌ.",
      "The negating la.",
      "Nefiy lâsıdır."),
  tok("يَخْلُدُونَ","khalada","verb",["mudari-marfu","afal-khamsa"],
      "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْجُمْلَةُ خَبَرٌ.",
      "A mudari of the five verbs, in raf' by its retained nun; the waw is the fa'il and the clause is the khabar.",
      "Ef'âl-i hamseden muzâri; nûnun sübûtuyla merfûdur, vâv fâildir, cümle haberdir.",
      segments=[seg("يَخْلُدُ","khalada","verb"), seg("ونَ","pron-3mp","pron")]),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfidir."),
  tok("النَّارِ","nar","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي».",
      "In jarr after فِي.",
      "«فِي» ile mecrurdur.", punct="."),
 ],
 "jumal": [
  J("وَأَهْلُ الْكَبَائِرِ مِنَ الْمُؤْمِنِينَ لَا يَخْلُدُونَ فِي النَّارِ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
    "A joined nominal clause — i'rabless.",
    "Ma'tûf isim cümlesi — mahalsizdir."),
  J("لَا يَخْلُدُونَ فِي النَّارِ",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
    "A verbal clause standing as the khabar, in raf' position.",
    "Haber olarak mahallen merfû fiil cümlesi.")]})

S.append({"id": "s4", "translation": {
 "en": "And faith is affirming what he brought from Allah the Exalted, and professing it.",
 "tr": "İman, onun Allah Teâlâ katından getirdiğini tasdik etmek ve ona ikrarda bulunmaktır."},
 "tokens": [
  tok("وَالْإِيمَانُ","iman","noun",["mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الْإِيمَانُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "Isti'naf waw; الْإِيمَان is the mubtada in raf'.",
      "İstinâf vâvı; «الْإِيمَانُ» merfû mübtedadır.",
      segments=[seg("وَ","wa","conj"), seg("الْإِيمَانُ","iman","noun")]),
  tok("هُوَ","pron-3ms-munfasil","pron",["damir-fasl"],
      "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.",
      "A damir fasl between mubtada and khabar — no place in i'rab.",
      "Mübteda ile haber arasında zamîr-i fasl — i'râbdan mahalli yoktur."),
  tok("التَّصْدِيقُ","tasdiq","noun",["mubtada-khabar","form-ii-verbs","masdar"],
      "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ «صَدَّقَ».",
      "The khabar in raf' — the masdar of صَدَّقَ (Form II).",
      "Merfû haber — «صَدَّقَ» (tef'îl) masdarıdır."),
  tok("بِمَا","bi","prep",["huruf-jarr","ism-mawsul","anwa-ma"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«مَا» مَوْصُولَةٌ مَجْرُورَةٌ بِهَا، مُتَعَلِّقٌ بِـ«التَّصْدِيقُ».",
      "The ba is a jarr letter and «ma» the relative in jarr after it, attached to التَّصْدِيق.",
      "Bâ cer harfi, «mâ» mevsûledir ve onunla mecrurdur; «التَّصْدِيقُ»a mütealliḳtır.",
      segments=[seg("بِ","bi","prep"), seg("مَا","ma-mawsula","pron")]),
  tok("جَاءَ","jaa","verb",["thulathi-mujarrad-babs","hollow-verbs"],
      "فِعْلٌ مَاضٍ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.",
      "A past verb with a hidden fa'il; the clause is the sila of the relative.",
      "Mâzî fiil, fâili gizli zamir; cümle mevsûlün sılasıdır."),
  tok("بِهِ","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«جَاءَ» — وَالْبَاءُ لِلتَّعْدِيَةِ.",
      "Preposition-phrase attached to جَاءَ — the ba makes the verb transitive: «brought».",
      "«جَاءَ»ye mütealliḳ câr-mecrûr — bâ ta'diye içindir: «getirdi».",
      segments=[seg("بِ","bi","prep"), seg("هِ","pron-3ms","pron")]),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلِابْتِدَاءِ.",
      "The jarr letter of starting-point.",
      "İbtidâ bildiren cer harfidir."),
  tok("عِنْدِ","inda","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "In jarr and a mudaf.",
      "Mecrur ve muzâftır."),
  tok("اللهِ","allah","noun",["idafa-definiteness"],
      "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The majestic name — mudaf ilayh in jarr.",
      "Lafza-i celâl — mecrûr muzâfun ileyhtir."),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "Past verb; a parenthetic clause of exaltation.",
      "Mâzî fiil; ta'zîm için mu'terizadır."),
  tok("وَالْإِقْرَارُ","iqrar","noun",["atf-nasaq","form-iv-verbs","masdar"],
      "مَعْطُوفٌ عَلَى «التَّصْدِيقُ» مَرْفُوعٌ — مَصْدَرُ «أَقَرَّ».",
      "Joined to التَّصْدِيق in raf' — the masdar of أَقَرَّ (Form IV).",
      "«التَّصْدِيقُ»a ma'tûf, merfû — «أَقَرَّ» (if'âl) masdarıdır.",
      segments=[seg("وَ","wa","conj"), seg("الْإِقْرَارُ","iqrar","noun")]),
  tok("بِهِ","bi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«الْإِقْرَارُ».",
      "Preposition-phrase attached to الْإِقْرَار.",
      "«الْإِقْرَارُ»a mütealliḳ câr-mecrûr.",
      segments=[seg("بِ","bi","prep"), seg("هِ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [
  J("وَالْإِيمَانُ هُوَ التَّصْدِيقُ… وَالْإِقْرَارُ بِهِ",
    "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا.",
    "A resumed nominal clause — i'rabless.",
    "Müste'nefe isim cümlesi — mahalsizdir."),
  J("جَاءَ بِهِ مِنْ عِنْدِ اللهِ",
    "جُمْلَةٌ فِعْلِيَّةٌ صِلَةٌ لِـ«مَا» — لَا مَحَلَّ لَهَا.",
    "A verbal clause, the sila of «ma» — i'rabless.",
    "«Mâ»nın sıla cümlesi — mahalsizdir.")]})

TITLE9 = {"ar": "الْكَبِيرَةُ وَالشَّفَاعَةُ وَالْإِيمَانُ",
          "en": "The Grave Sin, Intercession and Faith",
          "tr": "Kebîre, Şefaat ve İman"}

def g(lemma, root, pos, en, tr, lvl):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": lvl}
    if root: e["root"] = root
    return e
GLOSS_ADD = {
 "kabira": g("كَبِيرَة","ك ب ر","noun","a grave sin","büyük günah; kebîre",3),
 "kabair": g("كَبَائِر","ك ب ر","noun","grave sins (plural)","büyük günahlar (cem')",4),
 "akhraja": g("أَخْرَجَ","خ ر ج","verb","to take out, expel","çıkarmak",2),
 "adkhala": g("أَدْخَلَ","د خ ل","verb","to make enter, admit","sokmak; dâhil etmek",2),
 "shafaa": g("شَفَاعَة","ش ف ع","noun","intercession (masdar)","şefaat (masdar)",3),
 "rusul": g("رُسُل","ر س ل","noun","messengers (plural of rasul)","rasûller (rasûlün cem'i)",2),
 "akhyar": g("أَخْيَار","خ ي ر","noun","the best of people (plural of khayyir)","ahyâr; hayırlılar",4),
 "khalada": g("خَلَدَ","خ ل د","verb","to abide forever","ebedî kalmak",3),
 "tasdiq": g("تَصْدِيق","ص د ق","noun","affirming as true (masdar)","tasdik (masdar)",3),
 "iqrar": g("إِقْرَار","ق ر ر","noun","professing, acknowledging (masdar)","ikrar (masdar)",3),
 "jaa": g("جَاءَ","ج ي أ","verb","to come; (with ba) to bring","gelmek; (bâ ile) getirmek",1),
}

def build_morph():
    samti = json.loads((ROOT / "content/samples/wasiyyat-abi-hanifa-samti/morphology.json").read_text(encoding="utf-8"))["verbs"]
    yunus = json.loads((ROOT / "content/samples/yunus-wa-al-hut/morphology.json").read_text(encoding="utf-8"))["verbs"]
    out = {"akhraja": samti["akhraja"], "jaa": yunus["jaa"]}
    out["adkhala"] = _sg.derived(_sg.B4, _sg.W4, "ُ", "أَدْخَل", "دْخِل", "أَدْخِل",
                                 "إِدْخَال", "مُدْخِل", "مُدْخَل", "أُدْخِلَ", "يُدْخَلُ")
    out["khalada"] = _sg.sound1("nasara", "خَلَد", "خْلُد", "اُخْلُد", "خُلُود", "خَالِد")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/9.json").write_text(json.dumps({"chapter": 9, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 9 for c in man["chapters"]):
    man["chapters"].append({"n": 9, "title": TITLE9})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.7.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8")); mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch9:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
