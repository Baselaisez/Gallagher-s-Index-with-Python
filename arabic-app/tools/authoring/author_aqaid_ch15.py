# -*- coding: utf-8 -*-
"""Author chapter 15 of aqaid-ahl-al-sunna — the rest of the karamat list.

Picks the matn up exactly where chapter 14 stopped, inside the enumeration:
the speech of the inanimate and of the beast, the warding off of what was
coming from affliction, the sufficing against enemies in what matters — and
other such things; and that is a mu'jiza for the Messenger.

Verbatim contiguous span, re-vowelled against the received text. It stops
before «لِأَنَّهُ يَظْهَرُ بِهَا أَنَّهُ وَلِيٌّ», the argument that follows.
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
def g(lemma, root, pos, en, tr, level, plural=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    return e
S = []

TITLE15 = {"ar": "تَمَامُ الْكَرَامَاتِ وَكَوْنُهَا مُعْجِزَةً",
           "en": "The Rest of the Karamat, and Their Being a Mu'jiza",
           "tr": "Kerâmetlerin Devamı ve Mu'cize Oluşu"}

S.append({"id": "s1", "translation": {
 "en": "and the speech of the inanimate thing and of the dumb beast,",
 "tr": "cansızın ve dilsiz hayvanın konuşması,"},
 "tokens": [
  tok("وَكَلَامِ","kalam","noun",["huruf-jarr","atf-nasaq","idafa-definiteness","masdar"],
      "مَعْطُوفٌ عَلَى «قَطْعِ» مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «كَلَّمَ».",
      "Joined to «crossing», in jarr and a mudaf — the masdar of كَلَّمَ.",
      "«قَطْعِ»e ma'tûf, mecrur ve muzâf — «كَلَّمَ»nin masdarı.",
      segments=[seg("وَ","wa","conj"), seg("كَلَامِ","kalam","noun")]),
  tok("الْجَمَادِ","jamad","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ فِي الْمَعْنَى فَاعِلُ الْمَصْدَرِ.",
      "The mudaf ilayh in jarr — in meaning, the DOER of the masdar: the stone is what speaks.",
      "Mecrûr muzâfun ileyh — mana bakımından masdarın FÂİLİDİR: konuşan cansızdır."),
  tok("وَالْعَجْمَاءِ","ajma","noun",["atf-nasaq","idafa-definiteness","sifa-mushabbaha"],
      "مَعْطُوفٌ عَلَى «الْجَمَادِ» مَجْرُورٌ — مُؤَنَّثُ «أَعْجَم» عَلَى فَعْلَاءَ، وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ لَوْلَا «الْ».",
      "Joined to «the inanimate», in jarr — the feminine of أَعْجَم on فَعْلَاء, which would be a diptote were the article not on it.",
      "«الْجَمَادِ»e ma'tûf, mecrur — fa'lâ' vezninde «أَعْجَم»in müennesi; «ال» olmasaydı gayr-i munsarif olurdu.",
      segments=[seg("وَ","wa","conj"), seg("الْعَجْمَاءِ","ajma","noun")], punct="،"),
 ],
 "jumal": [J("وَكَلَامِ الْجَمَادِ وَالْعَجْمَاءِ",
   "مَعْطُوفٌ عَلَى الْجَارِّ وَالْمَجْرُورِ — لَا مَحَلَّ لَهُ.",
   "Joined to the jarr phrase — no mahall arises.",
   "Câr-mecrûra ma'tûftur — mahal söz konusu değildir.")]})

S.append({"id": "s2", "translation": {
 "en": "and the turning away of what was coming, out of affliction,",
 "tr": "gelmekte olan belânın def'i,"},
 "tokens": [
  tok("وَانْدِفَاعِ","indifa","noun",["huruf-jarr","atf-nasaq","idafa-definiteness","form-vii-verbs","masdar"],
      "مَعْطُوفٌ عَلَى «قَطْعِ» مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «انْدَفَعَ» عَلَى انْفِعَالٍ، وَهُوَ مُطَاوِعُ «دَفَعَ».",
      "Joined to «crossing», in jarr and a mudaf — the masdar of انْدَفَعَ on انْفِعَال, the SUBMISSIVE of دَفَعَ: he pushed it, and it gave way.",
      "«قَطْعِ»e ma'tûf, mecrur ve muzâf — infiâl vezninde «انْدَفَعَ» masdarı; «دَفَعَ»nin mutâvaatıdır.",
      segments=[seg("وَ","wa","conj"), seg("انْدِفَاعِ","indifa","noun")]),
  tok("الْمُتَوَجِّهِ","mutawajjih","noun",["idafa-definiteness","ism-fail","form-v-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «تَوَجَّهَ»، أَيِ الْبَلَاءُ الْمُقْبِلُ.",
      "The mudaf ilayh in jarr — the ism fa'il of تَوَجَّهَ: the affliction that was heading toward him.",
      "Mecrûr muzâfun ileyh — «تَوَجَّهَ»nin ism-i fâili; yönelmekte olan belâ."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِبَيَانِ الْجِنْسِ.",
      "A jarr letter marking the kind.",
      "Cinsi beyan için cer harfi."),
  tok("الْبَلَاءِ","bala","noun",["huruf-jarr"],
      "مَجْرُورٌ بِالْكَسْرَةِ — مَمْدُودٌ.",
      "In jarr by the kasra — a mamdud noun.",
      "Kesra ile mecrur — memdûddur.", punct="،"),
 ],
 "jumal": [J("وَانْدِفَاعِ الْمُتَوَجِّهِ مِنَ الْبَلَاءِ",
   "مَعْطُوفٌ عَلَى الْجَارِّ وَالْمَجْرُورِ — لَا مَحَلَّ لَهُ.",
   "Joined to the jarr phrase — no mahall arises.",
   "Câr-mecrûra ma'tûftur — mahal söz konusu değildir.")]})

S.append({"id": "s3", "translation": {
 "en": "and the sufficing against what matters, from the enemies — and other things besides.",
 "tr": "düşmanlardan gelen mühim şeye kâfî gelinmesi ve bunlardan başka şeyler."},
 "tokens": [
  tok("وَكِفَايَةِ","kifaya","noun",["huruf-jarr","atf-nasaq","idafa-definiteness","masdar"],
      "مَعْطُوفٌ عَلَى «قَطْعِ» مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «كَفَى» النَّاقِصِ.",
      "Joined to «crossing», in jarr and a mudaf — the masdar of the naqis verb كَفَى.",
      "«قَطْعِ»e ma'tûf, mecrur ve muzâf — nâkıs «كَفَى»nin masdarı.",
      segments=[seg("وَ","wa","conj"), seg("كِفَايَةِ","kifaya","noun")]),
  tok("الْمُهِمِّ","muhimm","noun",["idafa-definiteness","ism-fail","form-iv-verbs","doubled-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «أَهَمَّ» الْمُضَاعَفِ، أَيْ مَا يُهِمُّ الْمَرْءَ وَيَشْغَلُهُ.",
      "The mudaf ilayh in jarr — the ism fa'il of the doubled أَهَمَّ: what weighs on a man and occupies him.",
      "Mecrûr muzâfun ileyh — muzâaf «أَهَمَّ»nin ism-i fâili; insanı meşgul eden şey."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلِابْتِدَاءِ.",
      "A jarr letter of origin.",
      "İbtidâ için cer harfi."),
  tok("الْأَعْدَاءِ","aduw","noun",["huruf-jarr"],
      "مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ «عَدُوٍّ» عَلَى أَفْعَالٍ.",
      "In jarr by the kasra — the plural of عَدُوّ on أَفْعَال.",
      "Kesra ile mecrur — «عَدُوّ»un ef'âl vezninde cem'i.", punct="،"),
  tok("وَغَيْرِ","ghayr","noun",["huruf-jarr","atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «قَطْعِ» مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "Joined to «crossing», in jarr and a mudaf.",
      "«قَطْعِ»e ma'tûf, mecrur ve muzâf.",
      segments=[seg("وَ","wa","conj"), seg("غَيْرِ","ghayr","noun")]),
  tok("ذَلِكَ","dhalika","pron",["ism-mawsul","idafa-definiteness"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "A demonstrative, fixed, in the position of jarr as the mudaf ilayh.",
      "İsm-i işâret — mebnî, muzâfun ileyh olarak mahallen mecrûr."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلْبَيَانِ.",
      "A jarr letter of explication.",
      "Beyan için cer harfi."),
  tok("الْأَشْيَاءِ","shay","noun",["huruf-jarr","mamnu-min-sarf"],
      "مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ «شَيْءٍ»، وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ لَوْلَا «الْ».",
      "In jarr by the kasra — the plural of شَيْء, a diptote were the article not on it.",
      "Kesra ile mecrur — «شَيْء»in cem'i; «ال» olmasaydı gayr-i munsarif olurdu.", punct="،"),
 ],
 "jumal": [J("وَكِفَايَةِ الْمُهِمِّ مِنَ الْأَعْدَاءِ وَغَيْرِ ذَلِكَ مِنَ الْأَشْيَاءِ",
   "مَعْطُوفٌ عَلَى الْجَارِّ وَالْمَجْرُورِ — لَا مَحَلَّ لَهُ.",
   "Joined to the jarr phrase — no mahall arises.",
   "Câr-mecrûra ma'tûftur — mahal söz konusu değildir.")]})

S.append({"id": "s4", "translation": {
 "en": "And that is a mu'jiza for the Messenger for one of whose community this karama appeared.",
 "tr": "Ve bu, ümmetinden birine bu kerâmet zâhir olan Resul için bir mu'cizedir."},
 "tokens": [
  tok("وَيَكُونُ","kana","verb",["kana-wa-akhawatuha","hollow-verbs","mudari-marfu"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«يَكُونُ» فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.",
      "Isti'naf waw; «is» is a defective mudari in raf'.",
      "İstinâf vâvı; «يَكُونُ» merfû nâkıs muzâridir.",
      segments=[seg("وَ","wa","conj"), seg("يَكُونُ","kana","verb")]),
  tok("ذَلِكَ","dhalika","pron",["kana-wa-akhawatuha"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ «يَكُونُ».",
      "A demonstrative, fixed, in the position of raf' as the ism of «is».",
      "İsm-i işâret — mebnî, «يَكُونُ»nun ismi olarak mahallen merfû."),
  tok("مُعْجِزَةً","mujiza","noun",["kana-wa-akhawatuha","ism-fail","form-iv-verbs"],
      "خَبَرُ «يَكُونُ» مَنْصُوبٌ — اسْمُ فَاعِلٍ مِنْ «أَعْجَزَ».",
      "The khabar of «is», in nasb — the ism fa'il of أَعْجَزَ.",
      "«يَكُونُ»nun mansub haberi — «أَعْجَزَ»nin ism-i fâili."),
  tok("لِلرَّسُولِ","rasul","noun",["huruf-jarr"],
      "اللَّامُ حَرْفُ جَرٍّ، وَ«الرَّسُولِ» مَجْرُورٌ بِهَا.",
      "The lam is a jarr letter; «the Messenger» is in jarr after it.",
      "Lâm cer harfi; «الرَّسُولِ» onunla mecrurdur.",
      segments=[seg("لِ","li","prep"), seg("الرَّسُولِ","rasul","noun")]),
  tok("الَّذِي","alladhi","pron",["ism-mawsul","naat-sifa"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«الرَّسُولِ».",
      "A relative noun, fixed, in the position of jarr as a na't of «the Messenger».",
      "İsm-i mevsûl — mebnî, «الرَّسُولِ»in na'tı olarak mahallen mecrûr."),
  tok("ظَهَرَتْ","zahara","verb",["jumla-sifa"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.",
      "A past verb, the ta marking the feminine; the clause is the sila — i'rabless.",
      "Mâzî fiil, tâ te'nîs içindir; cümle sıladır, mahalsizdir."),
  tok("هَذِهِ","hadhihi","pron",["fail"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "A demonstrative, fixed, in the position of raf' as the fa'il.",
      "İsm-i işâret — mebnî, fâil olarak mahallen merfû."),
  tok("الْكَرَامَةُ","karama","noun",["badal"],
      "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ — أَوْ عَطْفُ بَيَانٍ.",
      "A badal of the demonstrative, in raf' — or an atf bayan.",
      "İsm-i işâretten merfû bedel — yahut atf-ı beyân."),
  tok("لِوَاحِدٍ","wahid","noun",["huruf-jarr"],
      "اللَّامُ حَرْفُ جَرٍّ، وَ«وَاحِدٍ» مَجْرُورٌ بِهَا، مُتَعَلِّقٌ بِـ«ظَهَرَتْ».",
      "The lam is a jarr letter; «one» is in jarr after it, attaching to «appeared».",
      "Lâm cer harfi; «وَاحِدٍ» onunla mecrur, «ظَهَرَتْ»e taalluk eder.",
      segments=[seg("لِ","li","prep"), seg("وَاحِدٍ","wahid","noun")]),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلتَّبْعِيضِ.",
      "A jarr letter of partition.",
      "Teb'îz için cer harfi."),
  tok("أُمَّتِهِ","umma","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "In jarr by the kasra and a mudaf; the ha is its mudaf ilayh.",
      "Kesra ile mecrur ve muzâf; hâ muzâfun ileyhtir.",
      segments=[seg("أُمَّتِ","umma","noun"), seg("هِ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [J("وَيَكُونُ ذَلِكَ مُعْجِزَةً لِلرَّسُولِ",
   "جُمْلَةٌ فِعْلِيَّةٌ نَاسِخَةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf clause governed by kana — i'rabless.",
   "Kâne ile mensuh istinâfî cümle — mahalsizdir."),
  J("ظَهَرَتْ هَذِهِ الْكَرَامَةُ لِوَاحِدٍ مِنْ أُمَّتِهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause serving as the sila — i'rabless.",
   "Mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "kalam":      g("كَلَام", "ك ل م", "noun", "speech (masdar)", "kelâm; konuşma (masdar)", 2),
 "jamad":      g("جَمَاد", "ج م د", "noun", "an inanimate thing", "cansız; cemâd", 3),
 "ajma":       g("عَجْمَاء", "ع ج م", "noun", "a dumb beast (fem. of a'jam)", "dilsiz hayvan; acmâ", 4),
 "indifa":     g("انْدِفَاع", "د ف ع", "noun", "being warded off (masdar, Form VII)", "def' olunma; indifâ (masdar)", 4),
 "mutawajjih": g("مُتَوَجِّه", "و ج ه", "noun", "heading toward, oncoming", "yönelen; müteveccih", 4),
 "bala":       g("بَلَاء", "ب ل و", "noun", "affliction, trial", "belâ; imtihan", 2),
 "kifaya":     g("كِفَايَة", "ك ف ي", "noun", "sufficing (masdar)", "kifâyet; yetme (masdar)", 3),
 "muhimm":     g("مُهِمّ", "ه م م", "noun", "what matters, what weighs", "mühim; önemli olan", 3),
 "aduw":       g("عَدُوّ", "ع د و", "noun", "enemy", "düşman; adüvv", 2, "أَعْدَاء"),
 "ghayr":      g("غَيْر", "غ ي ر", "noun", "other than", "-den başkası; gayr", 1),
 "dhalika":    g("ذَلِكَ", None, "pron", "that (masc.)", "şu; o (eril)", 1),
 "hadhihi":    g("هَذِهِ", None, "pron", "this (fem.)", "bu (dişil)", 1),
 "shay":       g("شَيْء", "ش ي أ", "noun", "thing", "şey", 1, "أَشْيَاء"),
 "alladhi":    g("الَّذِي", None, "pron", "the one who, which (masc.)", "ki o; -en (eril mevsûl)", 2),
 "wahid":      g("وَاحِد", "و ح د", "noun", "one", "bir; vâhid", 1),
 "umma":       g("أُمَّة", "أ م م", "noun", "community, umma", "ümmet", 2),
}

def build_morph():
    return {}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/15.json").write_text(json.dumps({"chapter": 15, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 15 for c in man["chapters"]):
    man["chapters"].append({"n": 15, "title": TITLE15})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.13.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch15:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
