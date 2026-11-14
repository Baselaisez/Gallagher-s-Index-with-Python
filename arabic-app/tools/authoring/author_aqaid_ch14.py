# -*- coding: utf-8 -*-
"""Author chapter 14 of aqaid-ahl-al-sunna — the karamat of the awliya.

Picks the matn up where chapter 13 stopped: the karamat of the friends of
Allah are true, and the karama appears for the wali by way of the breaking
of custom — crossing a far distance in a short time, food and drink and
clothing appearing at need, walking on water and in the air.

Verbatim contiguous span, re-vowelled against the received text. The chapter
STOPS EARLY inside the matn's long enumeration: what follows (the speech of
the inanimate, the warding off of affliction, and the argument that the
karama is a mu'jiza for the Messenger) continues in the next chapter. A span
may stop early; it may never skip from the middle.
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

TITLE14 = {"ar": "كَرَامَاتُ الْأَوْلِيَاءِ",
           "en": "The Karamat of the Friends of Allah",
           "tr": "Evliyânın Kerâmetleri"}

S.append({"id": "s1", "translation": {
 "en": "And the karamat of the friends of Allah are true.",
 "tr": "Evliyânın kerâmetleri haktır."},
 "tokens": [
  tok("وَكَرَامَاتُ","karama","noun",["mubtada-khabar","idafa-definiteness","jam-muannath-salim"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«كَرَامَاتُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.",
      "Isti'naf waw; «the karamat» is the mubtada in raf' and a mudaf — a sound feminine plural.",
      "İstinâf vâvı; «كَرَامَاتُ» merfû mübtedâ ve muzâf — cem'-i müennes-i sâlim.",
      segments=[seg("وَ","wa","conj"), seg("كَرَامَاتُ","karama","noun")]),
  tok("الْأَوْلِيَاءِ","wali","noun",["idafa-definiteness","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ «وَلِيٍّ» عَلَى أَفْعِلَاءَ، وَظَهَرَتِ الْكَسْرَةُ لِدُخُولِ «الْ».",
      "The mudaf ilayh in jarr by the kasra — the plural of وَلِيّ on أَفْعِلَاء, and the kasra SHOWS because the article restores it.",
      "Kesra ile mecrûr muzâfun ileyh — «وَلِيّ»in ef'ilâ' vezninde cem'i; «ال» girdiği için kesra zâhirdir."),
  tok("حَقٌّ","haqq","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "The khabar in raf' by the damma.",
      "Damme ile merfû haber.", punct="،"),
 ],
 "jumal": [J("وَكَرَامَاتُ الْأَوْلِيَاءِ حَقٌّ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "So the karama appears for the friend of Allah by way of the breaking of custom.",
 "tr": "Kerâmet, velî için âdetin bozulması yoluyla zâhir olur."},
 "tokens": [
  tok("فَتَظْهَرُ","zahara","verb",["mudari-marfu"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَ«تَظْهَرُ» فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "The fa BRANCHES off what was just said; «appears» is a mudari in raf' by the damma.",
      "Fâ tefrî' içindir; «تَظْهَرُ» damme ile merfû muzâridir.",
      segments=[seg("فَ","fa","conj"), seg("تَظْهَرُ","zahara","verb")]),
  tok("الْكَرَامَةُ","karama","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "The fa'il, in raf' by the damma.",
      "Damme ile merfû fâil."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«تَظْهَرُ».",
      "A jarr letter; the phrase attaches to «appears».",
      "Cer harfi; câr-mecrûr «تَظْهَرُ»ye taalluk eder."),
  tok("طَرِيقِ","tariq","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ.",
      "In jarr by the kasra, and a mudaf.",
      "Kesra ile mecrur ve muzâf."),
  tok("نَقْضِ","naqd","noun",["idafa-definiteness","masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «نَقَضَ».",
      "The mudaf ilayh in jarr, itself a mudaf — the masdar of نَقَضَ.",
      "Mecrûr muzâfun ileyh, kendisi de muzâf — «نَقَضَ»nin masdarı."),
  tok("الْعَادَةِ","ada","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ فِي الْمَعْنَى مَفْعُولُ «نَقْضِ».",
      "The mudaf ilayh in jarr — and in meaning it is the object of «breaking».",
      "Mecrûr muzâfun ileyh — mana bakımından «نَقْضِ»in mef'ûlüdür."),
  tok("لِلْوَلِيِّ","wali","noun",["huruf-jarr"],
      "اللَّامُ حَرْفُ جَرٍّ لِلِاخْتِصَاصِ، وَ«الْوَلِيِّ» مَجْرُورٌ بِهَا.",
      "The lam is a jarr letter of belonging; «the friend of Allah» is in jarr after it.",
      "Lâm ihtisâs için cer harfidir; «الْوَلِيِّ» onunla mecrurdur.",
      segments=[seg("لِ","li","prep"), seg("الْوَلِيِّ","wali","noun")], punct="،"),
 ],
 "jumal": [J("فَتَظْهَرُ الْكَرَامَةُ عَلَى طَرِيقِ نَقْضِ الْعَادَةِ لِلْوَلِيِّ",
   "جُمْلَةٌ فِعْلِيَّةٌ مُفَرَّعَةٌ عَلَى مَا قَبْلَهَا — لَا مَحَلَّ لَهَا.",
   "A verbal clause branching off what came before — i'rabless.",
   "Öncesine tefrî' edilen fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "Such as crossing the far distance in the short span,",
 "tr": "Uzak mesafeyi kısa zamanda kat etmek gibi,"},
 "tokens": [
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِبَيَانِ الْجِنْسِ — أَيْ مِنْ قَبِيلِ كَذَا.",
      "A jarr letter marking the KIND — «of the sort of».",
      "Cinsi beyan için cer harfi — «şu kabîlden» demektir."),
  tok("قَطْعِ","qat","noun",["huruf-jarr","idafa-definiteness","masdar"],
      "مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ — مَصْدَرُ «قَطَعَ».",
      "In jarr by the kasra and a mudaf — the masdar of قَطَعَ.",
      "Kesra ile mecrur ve muzâf — «قَطَعَ»nin masdarı."),
  tok("الْمَسَافَةِ","masafa","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ فِي الْمَعْنَى مَفْعُولُ الْمَصْدَرِ.",
      "The mudaf ilayh in jarr — in meaning, the object of the masdar.",
      "Mecrûr muzâfun ileyh — mana bakımından masdarın mef'ûlüdür."),
  tok("الْبَعِيدَةِ","baid","noun",["naat-sifa","sifa-mushabbaha"],
      "نَعْتٌ لِـ«الْمَسَافَةِ» مَجْرُورٌ — عَلَى وَزْنِ فَعِيلٍ.",
      "A na't of «the distance», in jarr — on the wazn فَعِيل.",
      "«الْمَسَافَةِ»nin na'tı, mecrur — fa'îl vezninde."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلظَّرْفِيَّةِ.",
      "A jarr letter of containment — the «in» of time here.",
      "Zarfiyet için cer harfi."),
  tok("الْمُدَّةِ","mudda","noun",["huruf-jarr","doubled-verbs"],
      "مَجْرُورٌ بِالْكَسْرَةِ — مِنَ الْمُضَاعَفِ «مَدَّ».",
      "In jarr by the kasra — from the doubled root مَدَّ.",
      "Kesra ile mecrur — muzâaf «مَدَّ»den."),
  tok("الْقَلِيلَةِ","qalil","noun",["naat-sifa","sifa-mushabbaha"],
      "نَعْتٌ لِـ«الْمُدَّةِ» مَجْرُورٌ — وَالْمُقَابَلَةُ بَيْنَ «الْبَعِيدَةِ» وَ«الْقَلِيلَةِ» هِيَ مَوْضِعُ نَقْضِ الْعَادَةِ.",
      "A na't of «the span», in jarr — and it is the OPPOSITION between «far» and «short» that is where custom breaks.",
      "«الْمُدَّةِ»nin na'tı, mecrur — âdetin bozulduğu yer, «الْبَعِيدَةِ» ile «الْقَلِيلَةِ» arasındaki mukabeledir.", punct="،"),
 ],
 "jumal": [J("مِنْ قَطْعِ الْمَسَافَةِ الْبَعِيدَةِ فِي الْمُدَّةِ الْقَلِيلَةِ",
   "جَارٌّ وَمَجْرُورٌ بَيَانِيٌّ — لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ إِذْ لَيْسَ بِجُمْلَةٍ.",
   "An explicative jarr phrase — not a clause at all, so no question of mahall arises.",
   "Beyân bildiren câr-mecrûr — cümle olmadığı için mahal söz konusu değildir.")]})

S.append({"id": "s4", "translation": {
 "en": "and the appearing of food and drink and clothing at the moment of need,",
 "tr": "ihtiyaç anında yiyeceğin, içeceğin ve giyeceğin zuhûru,"},
 "tokens": [
  tok("وَظُهُورِ","zuhur","noun",["huruf-jarr","atf-nasaq","idafa-definiteness","masdar"],
      "مَعْطُوفٌ عَلَى «قَطْعِ» مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «ظَهَرَ».",
      "Joined to «crossing», in jarr and a mudaf — the masdar of ظَهَرَ.",
      "«قَطْعِ»e ma'tûf, mecrur ve muzâf — «ظَهَرَ»nin masdarı.",
      segments=[seg("وَ","wa","conj"), seg("ظُهُورِ","zuhur","noun")]),
  tok("الطَّعَامِ","taam","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ فِي الْمَعْنَى فَاعِلُ الْمَصْدَرِ.",
      "The mudaf ilayh in jarr — in meaning, the DOER of the masdar: the food is what appears.",
      "Mecrûr muzâfun ileyh — mana bakımından masdarın FÂİLİDİR: zuhûr eden yemektir."),
  tok("وَالشَّرَابِ","sharab","noun",["atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «الطَّعَامِ» مَجْرُورٌ.",
      "Joined to «the food», in jarr.",
      "«الطَّعَامِ»e ma'tûf, mecrurdur.",
      segments=[seg("وَ","wa","conj"), seg("الشَّرَابِ","sharab","noun")]),
  tok("وَاللِّبَاسِ","libas","noun",["atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «الطَّعَامِ» مَجْرُورٌ.",
      "Joined to «the food», in jarr.",
      "«الطَّعَامِ»e ma'tûf, mecrurdur.",
      segments=[seg("وَ","wa","conj"), seg("اللِّبَاسِ","libas","noun")]),
  tok("عِنْدَ","inda","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِـ«ظُهُورِ».",
      "A time-adverb in nasb and a mudaf, attaching to «the appearing».",
      "Mansub zaman zarfı ve muzâf; «ظُهُورِ»e taalluk eder."),
  tok("الْحَاجَةِ","haja","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyh.", punct="،"),
 ],
 "jumal": [J("وَظُهُورِ الطَّعَامِ وَالشَّرَابِ وَاللِّبَاسِ عِنْدَ الْحَاجَةِ",
   "مَعْطُوفٌ عَلَى الْجَارِّ وَالْمَجْرُورِ قَبْلَهُ — لَا مَحَلَّ لَهُ.",
   "Joined to the jarr phrase before it — no mahall arises.",
   "Öncesindeki câr-mecrûra ma'tûftur — mahal söz konusu değildir.")]})

S.append({"id": "s5", "translation": {
 "en": "and walking upon the water and in the air.",
 "tr": "su üstünde ve havada yürümek."},
 "tokens": [
  tok("وَالْمَشْيِ","mashy","noun",["huruf-jarr","atf-nasaq","masdar","naqis-verbs"],
      "مَعْطُوفٌ عَلَى «قَطْعِ» مَجْرُورٌ — مَصْدَرُ «مَشَى» النَّاقِصِ.",
      "Joined to «crossing», in jarr — the masdar of the naqis verb مَشَى.",
      "«قَطْعِ»e ma'tûf, mecrur — nâkıs «مَشَى»nin masdarı.",
      segments=[seg("وَ","wa","conj"), seg("الْمَشْيِ","mashy","noun")]),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلِاسْتِعْلَاءِ، مُتَعَلِّقٌ بِـ«الْمَشْيِ».",
      "A jarr letter of being ON something, attaching to «walking».",
      "İsti'lâ için cer harfi; «الْمَشْيِ»ye taalluk eder."),
  tok("الْمَاءِ","ma","noun",["huruf-jarr"],
      "مَجْرُورٌ بِالْكَسْرَةِ.",
      "In jarr by the kasra.",
      "Kesra ile mecrurdur."),
  tok("وَفِي","fi","prep",["huruf-jarr","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«فِي» حَرْفُ جَرٍّ — وَتَبَدَّلَ الْحَرْفُ لِأَنَّ الْهَوَاءَ يُحَاطُ بِهِ لَا يُعْلَى عَلَيْهِ.",
      "Joining waw, then «fi» — the LETTER changes because one is surrounded by air, not perched on it.",
      "Atıf vâvı, sonra «فِي» — harf değişti; zira havaya çıkılmaz, hava kuşatır.",
      segments=[seg("وَ","wa","conj"), seg("فِي","fi","prep")]),
  tok("الْهَوَاءِ","hawa","noun",["huruf-jarr"],
      "مَجْرُورٌ بِالْكَسْرَةِ.",
      "In jarr by the kasra.",
      "Kesra ile mecrurdur.", punct="."),
 ],
 "jumal": [J("وَالْمَشْيِ عَلَى الْمَاءِ وَفِي الْهَوَاءِ",
   "مَعْطُوفٌ عَلَى الْجَارِّ وَالْمَجْرُورِ — لَا مَحَلَّ لَهُ.",
   "Joined to the jarr phrase — no mahall arises.",
   "Câr-mecrûra ma'tûftur — mahal söz konusu değildir.")]})

GLOSS_ADD = {
 "karama": g("كَرَامَة", "ك ر م", "noun", "a karama — an honour breaking custom", "kerâmet", 3, "كَرَامَات"),
 "wali":   g("وَلِيّ", "و ل ي", "noun", "a friend of Allah", "velî", 3, "أَوْلِيَاء"),
 "zahara": g("ظَهَرَ", "ظ ه ر", "verb", "to appear, become manifest", "zâhir olmak", 2),
 "tariq":  g("طَرِيق", "ط ر ق", "noun", "way, road", "yol; tarîk", 2),
 "naqd":   g("نَقْض", "ن ق ض", "noun", "breaking, undoing (masdar)", "nakz; bozma (masdar)", 4),
 "qat":    g("قَطْع", "ق ط ع", "noun", "cutting, crossing (masdar)", "kat'; kesme (masdar)", 3),
 "masafa": g("مَسَافَة", "س و ف", "noun", "distance", "mesafe", 2),
 "baid":   g("بَعِيد", "ب ع د", "noun", "far, distant", "uzak; baîd", 2),
 "mudda":  g("مُدَّة", "م د د", "noun", "a span of time", "müddet", 2),
 "qalil":  g("قَلِيل", "ق ل ل", "noun", "few, little, short", "az; kalîl", 2),
 "zuhur":  g("ظُهُور", "ظ ه ر", "noun", "appearing (masdar)", "zuhûr (masdar)", 3),
 "taam":   g("طَعَام", "ط ع م", "noun", "food", "yiyecek; taâm", 1),
 "sharab": g("شَرَاب", "ش ر ب", "noun", "drink", "içecek; şarâb", 1),
 "libas":  g("لِبَاس", "ل ب س", "noun", "clothing", "giyecek; libâs", 2),
 "inda":   g("عِنْدَ", None, "noun", "at, with (adverb of place and time)", "yanında; -dığı zaman (zarf)", 1),
 "haja":   g("حَاجَة", "ح و ج", "noun", "need", "ihtiyaç; hâcet", 2),
 "mashy":  g("مَشْي", "م ش ي", "noun", "walking (masdar)", "yürüme (masdar)", 3),
 "ma":     g("مَاء", "م و ه", "noun", "water", "su", 1),
 "hawa":   g("هَوَاء", "ه و ي", "noun", "air", "hava", 2),
}

def build_morph():
    return { "zahara": _sg.sound1("fataha", "ظَهَر", "ظْهَر", "اِظْهَر", "ظُهُور", "ظَاهِر") }

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/14.json").write_text(json.dumps({"chapter": 14, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 14 for c in man["chapters"]):
    man["chapters"].append({"n": 14, "title": TITLE14})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.12.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8")); mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch14:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
