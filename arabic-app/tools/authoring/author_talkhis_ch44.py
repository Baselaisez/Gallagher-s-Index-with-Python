# -*- coding: utf-8 -*-
"""Author chapter 44 of talkhis-al-miftah — الِاعْتِرَاضُ.

Sahifa 99-100 (lines ~2890-2915): the eighth occasion of itnab —
I'TIRAD, the parenthetic jumla: bringing, inside a speech or between
two speeches joined in meaning, one jumla or more WITH NO PLACE IN
I'RAB, for a point other than repelling misreading (that point being
takmil's own job):

  • TANZIH: وَيَجْعَلُونَ لِلّٰهِ الْبَنَاتِ سُبْحَانَهُ وَلَهُمْ مَا
    يَشْتَهُونَ (16:57) — «glory be to Him» breaks in mid-aya.
  • DU'A: 'Awf b. Muhallim's إِنَّ الثَّمَانِينَ وَبُلِّغْتَهَا • قَدْ
    أَحْوَجَتْ سَمْعِي إِلَى تَرْجُمَانْ — «may you be brought to
    them!» interrupts inna and its khabar.
  • TANBIH: وَاعْلَمْ فَعِلْمُ الْمَرْءِ يَنْفَعُهُ • أَنْ سَوْفَ
    يَأْتِي كُلُّ مَا قُدِرَا — «and a man's knowledge avails him»
    steps between اعْلَمْ and its object clause.

ATTRIBUTION: s3 is al-Nahl 16:57 (part), received Qur'anic text quoted
exactly in standard imla as the source prints it; s4-s5 are 'Awf b.
Muhallim's bayt (تَرْجُمَانْ kept with the source's rhyme sukun) and
s6-s7 the tanbih bayt, as the source recites them, split at the
hemistich; s1-s2 are the musannif's definition as the source recites
it, split at بِجُمْلَةٍ per its own two clauses.

Grammar this chapter teaches:
  • note 148 `itirad` — the definition verbatim, the nuktas, and the
    closing khilafs on i'tirad's reach.
  • the khabar-jarr-phrase + مَا mawsula frame (وَلَهُمْ مَا
    يَشْتَهُونَ); the majhul-mazi YOU-cell (بُلِّغْتَ); the ma'tuf on
    a majrur refusing the verb reading (أَوْ أَكْثَرَ).
  • new paradigms: بَلَّغَ (II), أَحْوَجَ (IV); نَفَعَ copied from l4.
"""
import json, pathlib, sys, re
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PKG = ROOT / "content/samples/talkhis-al-miftah"
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
def g(lemma, root, pos, en, tr, level, plural=None, form=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    if form: e["form"] = form
    return e
def copy_gloss(pkg, key):
    d = json.loads((ROOT / f"content/samples/{pkg}/glossary.json").read_text(encoding="utf-8"))["entries"]
    return d[key]
S = []

TITLE44 = {"ar": "الِاعْتِرَاضُ",
           "en": "I'tirad — the Parenthetic Sentence",
           "tr": "İ'tirâz — Ara Cümle"}

# ----------- s1 — the definition, first clause
S.append({"id": "s1", "translation": {
 "en": "I'TIRAD is bringing — inside a speech, or between two speeches joined in meaning —",
 "tr": "İ'TİRÂZ — bir sözün içinde yahut mânâca birbirine bağlı iki söz arasında —"},
 "tokens": [
  tok("الِاعْتِرَاضُ","itirad","noun",["itirad"],
      "مُبْتَدَأٌ مَرْفُوعٌ.",
      "«the parenthesis» — the eighth occasion, as mubtada.",
      "«i'tirâz» — sekizinci sebep; mübtedâ."),
  tok("أَنْ","an-nasiba","part",["itirad","an-masdariyya"],
      "مَصْدَرِيَّةٌ نَاصِبَةٌ.",
      "«that» —",
      "«-mek» —"),
  tok("يُؤْتَى","ata","verb",["itirad","naib-al-fail"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ بِفَتْحَةٍ مُقَدَّرَةٍ — وَالْمَصْدَرُ خَبَرٌ.",
      "«there be brought» — the definitional frame's passive, a third time.",
      "«getirilmek» — tarif çerçevesinin meçhûlü, üçüncü kez."),
  tok("فِي","fi","part",["itirad"],
      "حَرْفُ جَرٍّ.",
      "«inside» —",
      "«içinde» —"),
  tok("أَثْنَاءِ","athna","noun",["itirad"],
      "مَجْرُورٌ بِفِي وَهُوَ مُضَافٌ — جَمْعُ ثِنْيٍ: تَضَاعِيفُ الشَّيْءِ.",
      "«the folds of» — plural of ثِنْي: a speech's inner folds.",
      "«kıvrımlarında» — ثِنْي'in cem'i: sözün iç kıvrımları."),
  tok("كَلَامٍ","kalam","noun",["itirad"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«a speech» —",
      "«bir sözün» —"),
  tok("أَوْ","aw","part",["itirad","atf-nasaq"],
      "حَرْفُ عَطْفٍ.",
      "«or» —",
      "«yahut» —"),
  tok("بَيْنَ","bayna","noun",["itirad","maful-fih"],
      "ظَرْفٌ مَنْصُوبٌ مَعْطُوفٌ عَلَى مَحَلِّ الْجَارِّ وَهُوَ مُضَافٌ.",
      "«between» — the zarf joined onto the jarr phrase's place.",
      "«arasında» — câr-mecrûrun mahalline atfedilmiş zarf."),
  tok("كَلَامَيْنِ","kalam","noun",["itirad","al-muthanna"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.",
      "«two speeches» — the dual's jarr worn as a ya.",
      "«iki sözün» — tesniyenin yâ ile cerri."),
  tok("مُتَّصِلَيْنِ","muttasil","noun",["itirad","ism-fail","form-viii-verbs"],
      "صِفَةٌ مَجْرُورَةٌ بِالْيَاءِ — اسْمُ فَاعِلٍ مِنِ اتَّصَلَ.",
      "«joined» — Form VIII's ism fa'il, dual like its noun.",
      "«bağlı» — VIII. bâbın ism-i fâili; ismi gibi tesniye."),
  tok("مَعْنًى","mana","noun",["itirad","tamyiz","ism-maqsur-manqus"],
      "تَمْيِيزٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.",
      "«in meaning» — the tamyiz: joined HOW? in sense, not on the page.",
      "«mânâca» — temyiz: NASIL bağlı? sayfada değil, mânâda.",
      punct="—")],
 "jumal": [
  J("فِي أَثْنَاءِ كَلَامٍ أَوْ بَيْنَ كَلَامَيْنِ مُتَّصِلَيْنِ مَعْنًى",
    "ظَرْفَا الِاعْتِرَاضِ — دَاخِلَ الْكَلَامِ أَوْ بَيْنَ كَلَامَيْنِ.",
    "The two seats a parenthesis may take.",
    "Ara cümlenin alabileceği iki oturak."),
  J("مُتَّصِلَيْنِ مَعْنًى",
    "الصِّفَةُ وَتَمْيِيزُهَا.",
    "Joined in MEANING: the page may separate what sense binds.",
    "MÂNÂCA bağlı: sayfa ayırsa da mânâ bağlar.")]})

# ----------- s2 — the definition, second clause
S.append({"id": "s2", "translation": {
 "en": "— one jumla or more, WITH NO PLACE IN I'RAB, for a point other than repelling misreading.",
 "tr": "— i'râbdan MAHALLİ OLMAYAN bir yahut birden çok cümleyi, ihâmı def'in dışında bir nükte için getirmektir."},
 "tokens": [
  tok("بِجُمْلَةٍ","jumla","noun",["itirad"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِيُؤْتَى.",
      "«one jumla» —",
      "«bir cümle» —",
      segments=[seg("بِ","bi","part"), seg("جُمْلَةٍ","jumla","noun")]),
  tok("أَوْ","aw","part",["itirad","atf-nasaq"],
      "حَرْفُ عَطْفٍ.",
      "«or» —",
      "«yahut» —"),
  tok("أَكْثَرَ","akthar","noun",["itirad","ism-tafdil","mamnu-min-sarf"],
      "مَعْطُوفٌ عَلَى جُمْلَةٍ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.",
      "«or more» — the diptote tafdil wears its jarr as a fatha; joined onto the majrur, it can hide no verb.",
      "«veya daha çok» — gayr-i munsarif tafdîl, cerrini fetha ile giyer; mecrura atfedilmiş, fiil saklayamaz."),
  tok("لَا","la-nafiya-lil-jins","part",["itirad","la-nafiya-lil-jins"],
      "لَا النَّافِيَةُ لِلْجِنْسِ.",
      "«no» — the genus-denying la: no place AT ALL.",
      "«hiçbir» — cinsini nefyeden lâ: aslâ mahal yok."),
  tok("مَحَلَّ","mahall","noun",["itirad","la-nafiya-lil-jins"],
      "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.",
      "«place» — la's ism, mabni on the fatha.",
      "«mahal» — lânın ismi; fetha üzere mebnî."),
  tok("لَهَا","li","part",["itirad"],
      "جَارٌّ وَمَجْرُورٌ — خَبَرُ لَا.",
      "«for it» — la's khabar.",
      "«onun» — lânın haberi.",
      segments=[seg("لَ","li","part"), seg("هَا","pron-3fs","pron")]),
  tok("مِنَ","min","part",["itirad"],
      "حَرْفُ جَرٍّ لِلْبَيَانِ.",
      "«in» —",
      "«-dan» —"),
  tok("الْإِعْرَابِ","irab","noun",["itirad"],
      "مَجْرُورٌ بِمِنْ — لَا مُبْتَدَأٌ وَلَا خَبَرٌ وَلَا مَفْعُولٌ: جُمْلَةٌ خَارِجَ الشَّجَرَةِ.",
      "«i'rab» — the parenthesis hangs on no branch of the sentence's tree.",
      "«i'râbdan» — ara cümle, cümle ağacının hiçbir dalına asılı değildir."),
  tok("لِنُكْتَةٍ","nukta","noun",["itirad"],
      "جَارٌّ وَمَجْرُورٌ.",
      "«for a point» —",
      "«bir nükte için» —",
      segments=[seg("لِ","li","part"), seg("نُكْتَةٍ","nukta","noun")]),
  tok("سِوَى","siwa","noun",["itirad","istithna"],
      "صِفَةٌ لِنُكْتَةٍ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ وَهُوَ مُضَافٌ.",
      "«other than» — the exception carving takmil's own job out of i'tirad's licence.",
      "«dışında» — tekmîlin öz işini i'tirâz ruhsatından oyan istisnâ."),
  tok("دَفْعِ","daf-repel","noun",["itirad"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "«the repelling of» —",
      "«def'inin» —"),
  tok("الْإِيهَامِ","iham","noun",["itirad"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ أَوْهَمَ.",
      "«misreading» — for THAT surplus is takmil, the previous chapter's.",
      "«ihâmın» — çünkü O fazla tekmîldir, önceki bâbındır.",
      punct=".")],
 "jumal": [
  J("بِجُمْلَةٍ أَوْ أَكْثَرَ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ",
    "الْمُعْتَرِضَةُ وَشَرْطُهَا — جُمْلَةٌ بِلَا مَحَلٍّ.",
    "The parenthesis's badge: a whole jumla hanging on no branch of the i'rab.",
    "Ara cümlenin nişanı: i'râbın hiçbir dalına asılı olmayan tam cümle."),
  J("لِنُكْتَةٍ سِوَى دَفْعِ الْإِيهَامِ",
    "الْقَيْدُ الْفَاصِلُ عَنِ التَّكْمِيلِ.",
    "The clause that keeps i'tirad and takmil two chapters.",
    "İ'tirâz ile tekmîli iki bâb tutan kayıt.")]})

# ----------- s3 — Nahl 16:57: the tanzih parenthesis
S.append({"id": "s3", "translation": {
 "en": "And they assign to Allah daughters — GLORY BE TO HIM — and to themselves what they desire (16:57). The parenthesis breaks in for TANZIH.",
 "tr": "Allah'a kızları isnat ederler — O MÜNEZZEHTİR — kendilerine de arzuladıklarını (16:57). Ara cümle TENZÎH için girer."},
 "tokens": [
  tok("وَيَجْعَلُونَ","jaala","verb",["itirad","afal-khamsa"],
      "الْوَاوُ عَاطِفَةٌ، وَيَجْعَلُونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ.",
      "«and they assign» —",
      "«ve kılarlar» —",
      segments=[seg("وَ","wa","part"), seg("يَجْعَلُونَ","jaala","verb")]),
  tok("لِلّٰهِ","allah","propn",["itirad"],
      "اللَّامُ جَارَّةٌ وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — الْمَفْعُولُ الثَّانِي مُقَدَّمٌ.",
      "«to Allah» — the second object fronted.",
      "«Allah'a» — öne alınmış ikinci mef'ûl.",
      segments=[seg("لِ","li","part"), seg("اللّٰهِ","allah","propn")]),
  tok("الْبَنَاتِ","bint","noun",["itirad","jam-muannath-salim"],
      "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ وَعَلَامَتُهُ الْكَسْرَةُ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.",
      "«daughters» — the sound feminine plural wears its NASB as a kasra.",
      "«kızları» — cem'-i müennes-i sâlim, NASBINI kesre ile giyer."),
  tok("سُبْحَانَهُ","subhana","noun",["itirad","maful-mutlaq"],
      "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ اعْتِرَاضٌ لِلتَّنْزِيهِ.",
      "«glory be to Him» — a maf'ul mutlaq whose verb is never spoken: the parenthesis, breaking in to declare Him far above the claim.",
      "«O münezzehtir» — fiili hiç söylenmeyen mef'ûl-i mutlak: iddiadan tenzîh için giren ara cümle.",
      segments=[seg("سُبْحَانَ","subhana","noun"), seg("هُ","pron-3ms","pron")]),
  tok("وَلَهُمْ","li","part",["itirad"],
      "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ جَارَّةٌ وَالضَّمِيرُ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.",
      "«and to themselves» — the resumed speech: the fronted khabar.",
      "«kendilerine de» — kaldığı yerden söz: öne alınmış haber.",
      segments=[seg("وَ","wa","part"), seg("لَ","li","part"), seg("هُمْ","pron-3mp","pron")]),
  tok("مَا","ma-mawsula","pron",["itirad","ism-mawsul"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.",
      "«what» — the delayed mubtada after its jarr-phrase khabar.",
      "«arzuladıkları şey» — câr-mecrûr haberden sonra ertelenmiş mübtedâ."),
  tok("يَشْتَهُونَ","ishtaha","verb",["itirad","form-viii-verbs","afal-khamsa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ — وَالْجُمْلَةُ صِلَةٌ، وَالْعَائِدُ مَحْذُوفٌ: يَشْتَهُونَهُ.",
      "«they desire» — the sila with its aid concealed (يَشْتَهُونَهُ).",
      "«arzularlar» — âidi gizli sıla (يَشْتَهُونَهُ).",
      punct=".")],
 "jumal": [
  J("سُبْحَانَهُ",
    "جُمْلَةُ الِاعْتِرَاضِ — لِلتَّنْزِيهِ، وَلَا مَحَلَّ لَهَا.",
    "The tanzih parenthesis: one word wide, no branch of the i'rab holds it.",
    "Tenzîh ara cümlesi: bir kelime genişliğinde; i'râbın hiçbir dalı onu tutmaz."),
  J("وَلَهُمْ مَا يَشْتَهُونَ",
    "الْخَبَرُ الْمُقَدَّمُ وَالْمَوْصُولُ الْمُبْتَدَأُ — عَوْدُ الْكَلَامِ بَعْدَ الِاعْتِرَاضِ.",
    "The speech resumes across the parenthesis as if unbroken — the proof the break had no place.",
    "Söz, ara cümlenin üstünden hiç kesilmemiş gibi sürer — kesintinin mahalsizliğinin delili.")]})

# ----------- s4 — 'Awf's bayt, first hemistich: the du'a parenthesis
S.append({"id": "s4", "translation": {
 "en": "Truly the eighty — AND MAY YOU BE BROUGHT TO THEM! —",
 "tr": "Gerçekten seksen yaş — SEN DE ONA ERDİRİLESİN! —"},
 "tokens": [
  tok("إِنَّ","inna","part",["itirad","inna-wa-akhawatuha"],
      "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.",
      "«truly» —",
      "«gerçekten» —"),
  tok("الثَّمَانِينَ","thamanun","noun",["itirad","jam-mudhakkar-salim"],
      "اسْمُ إِنَّ مَنْصُوبٌ بِالْيَاءِ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.",
      "«the eighty» — the decade-numeral rides the sound-plural rail: nasb as a ya.",
      "«seksen» — onluk sayı, sâlim cem' rayında: yâ ile nasb."),
  tok("وَبُلِّغْتَهَا","ballagha","verb",["itirad","naib-al-fail","form-ii-verbs"],
      "الْوَاوُ اعْتِرَاضِيَّةٌ، وَبُلِّغْتَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ نَائِبُ فَاعِلٍ، وَهَا مَفْعُولٌ ثَانٍ — دُعَاءٌ مُعْتَرِضٌ.",
      "«and may you be brought to them» — the passive «you» cell, breaking in as a PRAYER between inna and its khabar: live to eighty yourself!",
      "«sen de erdirilesin» — meçhûlün «sen» hânesi; inne ile haberi arasına DUÂ olarak girer: sen de seksene er!",
      punct="•", segments=[seg("وَ","wa","part"), seg("بُلِّغْتَ","ballagha","verb"), seg("هَا","pron-3fs","pron")])],
 "jumal": [
  J("إِنَّ الثَّمَانِينَ وَبُلِّغْتَهَا",
    "اسْمُ إِنَّ ثُمَّ الِاعْتِرَاضُ — وَالْخَبَرُ فِي الْعَجُزِ.",
    "Inna's ism, then the parenthesis; the khabar waits in the second hemistich.",
    "İnne'nin ismi, sonra ara cümle; haber ikinci mısrada bekler."),
  J("وَبُلِّغْتَهَا",
    "جُمْلَةُ الِاعْتِرَاضِ لِلدُّعَاءِ.",
    "The du'a parenthesis: the poet blesses his listener mid-complaint.",
    "Duâ ara cümlesi: şair, yakınmasının ortasında dinleyenine duâ eder.")]})

# ----------- s5 — the second hemistich
S.append({"id": "s5", "translation": {
 "en": "— has made my hearing need an interpreter. (the source glosses: here تَرْجُمَان means a repeater and explainer.)",
 "tr": "— kulağımı bir tercümana muhtaç etti. (kaynağın notu: تَرْجُمَان burada tekrarlayıp anlaşılır kılan demektir.)"},
 "tokens": [
  tok("قَدْ","qad","part",["itirad","qad-harf"],
      "حَرْفُ تَحْقِيقٍ.",
      "«indeed» —",
      "«gerçekten» —"),
  tok("أَحْوَجَتْ","ahwaja","verb",["itirad","form-iv-verbs"],
      "فِعْلٌ مَاضٍ وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ هِيَ — وَالْجُمْلَةُ خَبَرُ إِنَّ.",
      "«has made … need» — Form IV of حَاجَة: inna's khabar arrives at last.",
      "«muhtaç etti» — حَاجَة'nin IV. bâbı: inne'nin haberi nihayet gelir."),
  tok("سَمْعِي","sam","noun",["itirad","ya-al-mutakallim"],
      "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ.",
      "«my hearing» —",
      "«kulağımı» —",
      segments=[seg("سَمْعِ","sam","noun"), seg("ي","pron-1s","pron")]),
  tok("إِلَى","ila","part",["itirad"],
      "حَرْفُ جَرٍّ.",
      "«to» —",
      "«-a» —"),
  tok("تَرْجُمَانْ","tarjuman","noun",["itirad"],
      "مَجْرُورٌ — وَسُكِّنَ لِلْوَقْفِ وَالْقَافِيَةِ.",
      "«an interpreter» — its rhyme-sukun kept as the source prints it.",
      "«tercümana» — kafiye sükûnu, kaynağın bastığı gibi.",
      punct="•")],
 "jumal": [
  J("قَدْ أَحْوَجَتْ سَمْعِي إِلَى تَرْجُمَانْ",
    "خَبَرُ إِنَّ — وَصَلَ بَعْدَ الِاعْتِرَاضِ سَلِيمًا.",
    "The khabar lands whole: the parenthesis delayed it and damaged nothing.",
    "Haber sapasağlam iner: ara cümle geciktirdi, hiçbir şey bozmadı."),
  J("إِلَى تَرْجُمَانْ",
    "الْجَارُّ الْمَوْقُوفُ عَلَيْهِ لِلْقَافِيَةِ.",
    "Old age in one image: ears that need a repeater.",
    "İhtiyarlık tek tabloda: tekrarcıya muhtaç kulaklar.")]})

# ----------- s6 — the tanbih bayt, first hemistich
S.append({"id": "s6", "translation": {
 "en": "And KNOW — for a man's knowledge avails him —",
 "tr": "Ve BİL — çünkü kişinin bilgisi ona fayda verir —"},
 "tokens": [
  tok("وَاعْلَمْ","alima","verb",["itirad","imperative-amr"],
      "الْوَاوُ بِحَسَبِ مَا قَبْلَهَا، وَاعْلَمْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ أَنْتَ.",
      "«and know» — the amr whose object clause the parenthesis will delay.",
      "«ve bil» — mef'ûl cümlesini ara cümlenin geciktireceği emir.",
      segments=[seg("وَ","wa","part"), seg("اعْلَمْ","alima","verb")]),
  tok("فَعِلْمُ","ilm","noun",["itirad"],
      "الْفَاءُ اعْتِرَاضِيَّةٌ، وَعِلْمُ مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«for the knowledge of» — the parenthesis opens on its own fa.",
      "«çünkü bilgisi» — ara cümle kendi fâsıyla açılır.",
      segments=[seg("فَ","fa","part"), seg("عِلْمُ","ilm","noun")]),
  tok("الْمَرْءِ","mar","noun",["itirad"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«a man» —",
      "«kişinin» —"),
  tok("يَنْفَعُهُ","nafaa","verb",["itirad","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ، وَالْكُلُّ اعْتِرَاضٌ لِلتَّنْبِيهِ.",
      "«avails him» — the whole clause is the TANBIH parenthesis: it tells the hearer why to listen before saying what to hear.",
      "«ona fayda verir» — bütün cümle TENBÎH ara cümlesidir: neyi duyacağını söylemeden önce niçin dinleyeceğini söyler.",
      punct="•", segments=[seg("يَنْفَعُ","nafaa","verb"), seg("هُ","pron-3ms","pron")])],
 "jumal": [
  J("فَعِلْمُ الْمَرْءِ يَنْفَعُهُ",
    "جُمْلَةُ الِاعْتِرَاضِ لِلتَّنْبِيهِ — بَيْنَ اعْلَمْ وَمَفْعُولِهِ.",
    "The tanbih parenthesis, standing between «know» and the thing to be known.",
    "«Bil» ile bilinecek şeyin arasında duran tenbîh ara cümlesi."),
  J("وَاعْلَمْ",
    "الْأَمْرُ الَّذِي سَيَطُولُ انْتِظَارُ مَفْعُولِهِ.",
    "A command whose object must wait a whole clause.",
    "Mef'ûlü koca bir cümle bekleyecek emir.")]})

# ----------- s7 — the second hemistich: the delayed object clause
S.append({"id": "s7", "translation": {
 "en": "— that all that has been decreed shall surely come. (أَنْ here is the lightened أَنَّ, its ism a concealed shan-pronoun; the final alif is the rhyme's itlaq.)",
 "tr": "— takdir edilen her şeyin mutlaka geleceğini. (buradaki أَنْ, muhaffef أَنَّ'dir; ismi gizli şan zamiri; sondaki elif kafiye ıtlâkıdır.)"},
 "tokens": [
  tok("أَنْ","an-nasiba","part",["itirad","inna-am-anna"],
      "حَرْفٌ مُخَفَّفٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا مَحْذُوفٌ هُوَ الشَّأْنُ — وَالْمَصْدَرُ سَدَّ مَسَدَّ مَفْعُولَيِ اعْلَمْ.",
      "«that» — the lightened anna: its clause finally fills «know»'s object seats.",
      "«ki» — muhaffef enne: cümlesi nihayet «bil»in mef'ûl yerlerini doldurur."),
  tok("سَوْفَ","sawfa","part",["itirad"],
      "حَرْفُ اسْتِقْبَالٍ — وَهُوَ الْفَاصِلُ الَّذِي تَطْلُبُهُ الْمُخَفَّفَةُ.",
      "«shall» — and the very buffer the lightened anna demands before its verb.",
      "«ileride» — muhaffef ennenin fiilinden önce istediği fâsıla da budur."),
  tok("يَأْتِي","ata","verb",["itirad","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.",
      "«shall come» — the naqis mudari, its damma hidden.",
      "«gelecek» — nâkıs muzâri; dammesi gizli."),
  tok("كُلُّ","kull","noun",["itirad"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«all» —",
      "«hepsi» —"),
  tok("مَا","ma-mawsula","pron",["itirad","ism-mawsul"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "«that» —",
      "«şeyin» —"),
  tok("قُدِرَا","qadara","verb",["itirad","naib-al-fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ هُوَ — وَالْأَلِفُ لِلْإِطْلَاقِ.",
      "«has been decreed» — the passive mazi with the rhyme's prolonging alif.",
      "«takdir edildi» — meçhûl mâzî; elif, kafiye ıtlâkı.",
      punct="•")],
 "jumal": [
  J("أَنْ سَوْفَ يَأْتِي كُلُّ مَا قُدِرَا",
    "الْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيِ اعْلَمْ — بَعْدَ الِاعْتِرَاضِ.",
    "The delayed object clause arrives — the lightened anna, its sawfa buffer, and the decree.",
    "Geciken mef'ûl cümlesi gelir — muhaffef enne, sevfe fâsılası ve takdir."),
  J("قُدِرَا",
    "الْمَجْهُولُ وَأَلِفُ الْإِطْلَاقِ.",
    "Fate in the passive: no doer named, none needed.",
    "Kaderde meçhûl: fâil anılmaz, gerekmez de.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "itirad": g("اِعْتِرَاض", "ع ر ض", "noun", "parenthesis (balagha); objection", "i'tirâz: ara cümle; itiraz", 6),
 "athna": g("أَثْنَاء", "ث ن ي", "noun", "the folds, midst (of)", "esnâ, iç kıvrımlar", 4),
 "muttasil": g("مُتَّصِل", "و ص ل", "noun", "joined, connected (ism fa'il of اِتَّصَلَ)", "muttasıl, bağlı (اِتَّصَلَ'nin ism-i fâili)", 4),
 "irab": g("إِعْرَاب", "ع ر ب", "noun", "i'rab: the case system", "i'râb", 3),
 "iham": g("إِيهَام", "و ه م", "noun", "misleading suggestion (masdar of أَوْهَمَ)", "îhâm, vehme düşürme (أَوْهَمَ'nin masdarı)", 5),
 "subhana": g("سُبْحَان", "س ب ح", "noun", "glory (only as سُبْحَانَ + mudaf ilayh)", "sübhân (yalnız سُبْحَانَ + muzâfun ileyh)", 3),
 "thamanun": g("ثَمَانُونَ", "ث م ن", "noun", "eighty (declines like the sound masculine plural)", "seksen (cem'-i müzekker-i sâlim gibi i'râblanır)", 3),
 "ballagha": g("بَلَّغَ", "ب ل غ", "verb", "to make reach, bring to", "ulaştırmak, erdirmek", 3, form="II"),
 "ahwaja": g("أَحْوَجَ", "ح و ج", "verb", "to make (someone) need", "muhtaç etmek", 4, form="IV"),
 "sam": g("سَمْع", "س م ع", "noun", "hearing", "işitme, kulak", 3),
 "tarjuman": g("تَرْجُمَان", "ت ر ج م", "noun", "interpreter; (here) one who repeats and makes plain", "tercüman; (burada) tekrarlayıp anlaşılır kılan", 5),
 "qadara": g("قَدَرَ", "ق د ر", "verb", "to decree, apportion", "takdir etmek", 3, form="I"),
 "daf-repel": g("دَفْع", "د ف ع", "noun", "repelling (masdar)", "def etme (masdar)", 4),
 "bayna": copy_gloss("kitab-al-sulh", "bayna"),
 "siwa": copy_gloss("aqaid-ahl-al-sunna", "siwa"),
 "mahall": copy_gloss("wasiyyat-abi-hanifa-samti", "mahall"),
 "nafaa": copy_gloss("wasiyyat-abi-hanifa-l4", "nafaa"),
 "la-nafiya-lil-jins": copy_gloss("aqaid-ahl-al-sunna", "la-nafiya-lil-jins"),
 "bint": dict(copy_gloss("jumal-al-tadrib", "bint"), plural="بَنَات"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/44.json").write_text(
    json.dumps({"chapter": 44, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 44 for c in man["chapters"]):
    man["chapters"].append({"n": 44, "title": TITLE44})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.44.0"
ADD_EN = (" Chapter 44 carries i'tirad (lines ~2890-2915, sahifa 99-100): s3 is al-Nahl 16:57 "
          "(part), received Qur'anic text quoted exactly in standard imla as the source prints "
          "it; s4-s5 are 'Awf b. Muhallim's bayt (its rhyme sukun on تَرْجُمَانْ kept as "
          "printed) and s6-s7 the tanbih bayt, as the source recites them, split at the "
          "hemistich; s1-s2 are the musannif's definition per the package's definitional "
          "frame, split at its own two clauses.")
ADD_TR = (" Kırk dördüncü bâb i'tirâzı taşır (satır ~2890-2915, sahife 99-100): s3 Nahl 16:57 "
          "(kısmen) — kaynağın bastığı standart imlâ ile aynen alınmış mervî Kur'ân metni; "
          "s4-s5 Avf b. Muhallim'in beyti (تَرْجُمَانْ'daki kafiye sükûnu basıldığı gibi), "
          "s6-s7 tenbîh beyti — kaynağın okuduğu şekliyle, mısra başından bölünmüş; s1-s2, "
          "musannifin tarifi — paketin tarif çerçevesince, kendi iki cümlesinden ayrılmıştır.")
if "2890-2915" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "ballagha" not in mo["verbs"]:
    mo["verbs"]["ballagha"] = _sg.derived(
        _sg.B2, _sg.W2, "ُ", "بَلَّغ", "بَلِّغ", "بَلِّغ",
        "تَبْلِيغ", "مُبَلِّغ", "مُبَلَّغ", "بُلِّغَ", "يُبَلَّغُ")
if "ahwaja" not in mo["verbs"]:
    # Form IV of a hollow root conjugated SOUND (أَحْوَجَ يُحْوِجُ — the
    # defect-and-colour class refuses i'lal, like أَعْوَرَ).
    mo["verbs"]["ahwaja"] = _sg.derived(
        _sg.B4, _sg.W4, "ُ", "أَحْوَج", "حْوِج", "أَحْوِج",
        "إِحْوَاج", "مُحْوِج", "مُحْوَج", "أُحْوِجَ", "يُحْوَجُ",
        "أَجْوَفُ لَا يُعَلُّ فِي هٰذَا الْبَابِ: أَحْوَجَ يُحْوِجُ.")
if "qadara" not in mo["verbs"]:
    mo["verbs"]["qadara"] = _sg.sound1(
        "daraba", "قَدَر", "قْدِر", "اِقْدِر", "قَدْر", "قَادِر",
        "مَقْدُور", "قُدِرَ", "يُقْدَرُ")
if "nafaa" not in mo["verbs"]:
    src = json.loads((ROOT / "content/samples/wasiyyat-abi-hanifa-l4/morphology.json").read_text(encoding="utf-8"))
    mo["verbs"]["nafaa"] = src["verbs"]["nafaa"]
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 148
GR = ROOT / "content/grammar"
NOTE148 = {
 "id": "itirad",
 "title": {"ar": "الِاعْتِرَاضُ",
           "en": "I'tirad — the parenthetic sentence",
           "tr": "İ'tirâz — ara cümle"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — الإطناب: الاعتراض"],
 "question": {
  "en": ["Does a whole jumla (or more) break into the speech — or between two speeches joined in meaning — holding NO place in the i'rab? That is i'tirad.",
         "What point does the break earn? Tanzih (سُبْحَانَهُ in 16:57), du'a (وَبُلِّغْتَهَا), tanbih (فَعِلْمُ الْمَرْءِ يَنْفَعُهُ) — anything but repelling misreading, which is takmil's own job.",
         "Does the speech resume across the break as if unbroken? It must — that seamless resumption is the parenthesis's proof."],
  "tr": ["Sözün içine — yahut mânâca bağlı iki söz arasına — i'râbda YERİ OLMAYAN tam bir cümle (veya birden çok) mi giriyor? İ'tirâz budur.",
         "Kesinti hangi nükteyi kazanır? Tenzîh (16:57'de سُبْحَانَهُ), duâ (وَبُلِّغْتَهَا), tenbîh (فَعِلْمُ الْمَرْءِ يَنْفَعُهُ) — îhâmı def' hariç; o, tekmîlin öz işidir.",
         "Söz, kesintinin üstünden hiç kesilmemiş gibi sürüyor mu? Sürmelidir — o pürüzsüz devam, ara cümlenin delilidir."]},
 "plain": {
  "en": "The eighth occasion of itnab: a sentence with no seat in the i'rab breaks into the speech for a point — glory cried out mid-accusation (16:57), a blessing dropped mid-complaint, a why-listen slipped between «know» and the thing to know. Cut it and the grammar never notices; keep it and the speech gains a second voice.",
  "tr": "Itnâbın sekizinci sebebi: i'râbda oturağı olmayan bir cümle, bir nükte için sözün içine girer — iftira ortasında haykırılan tesbih (16:57), yakınma ortasına bırakılan duâ (Avf'ın beyti), «bil» ile bilinecek şeyin arasına sıkışan niçin-dinlemeli. Kes, gramer fark etmez; bırak, söz ikinci bir ses kazanır."},
 "explanation": {
  "en": "The definition: أَنْ يُؤْتَى فِي أَثْنَاءِ كَلَامٍ أَوْ بَيْنَ كَلَامَيْنِ مُتَّصِلَيْنِ مَعْنًى بِجُمْلَةٍ أَوْ أَكْثَرَ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ لِنُكْتَةٍ سِوَى دَفْعِ الْإِيهَامِ — inside one speech or between two joined in meaning, one jumla or more with NO PLACE IN I'RAB, for a point OTHER than repelling misreading (that exclusion keeps takmil a separate chapter). The nuktas the source counts: TANZIH — وَيَجْعَلُونَ لِلّٰهِ الْبَنَاتِ سُبْحَانَهُ وَلَهُمْ مَا يَشْتَهُونَ (16:57), where the glorification bursts in between the accusation and its completion; DU'A — 'Awf b. Muhallim's إِنَّ الثَّمَانِينَ وَبُلِّغْتَهَا قَدْ أَحْوَجَتْ سَمْعِي إِلَى تَرْجُمَانْ, the blessing «may you be brought to them!» standing between inna and its khabar; TANBIH — وَاعْلَمْ فَعِلْمُ الْمَرْءِ يَنْفَعُهُ أَنْ سَوْفَ يَأْتِي كُلُّ مَا قُدِرَا, where «a man's knowledge avails him» delays the object clause of اعْلَمْ (and that clause arrives as the LIGHTENED أَنْ with its concealed shan-pronoun and its سَوْفَ buffer). A parenthesis may even run MORE than one jumla between two speeches: فَأْتُوهُنَّ مِنْ حَيْثُ أَمَرَكُمُ اللهُ إِنَّ اللهَ يُحِبُّ التَّوَّابِينَ وَيُحِبُّ الْمُتَطَهِّرِينَ نِسَاؤُكُمْ حَرْثٌ لَكُمْ (2:222-223). The CLOSING KHILAFS: some allow the i'tirad's nukta to be even daf' al-iham (then it swallows part of takmil); some allow it at a speech's very END with nothing after (then it covers tadhyil's ground); and some allow a NON-jumla parenthesis (then tatmim and takmil shapes fall in). The musannif's tighter definition keeps the four chapters four.",
  "tr": "Tarif: أَنْ يُؤْتَى فِي أَثْنَاءِ كَلَامٍ أَوْ بَيْنَ كَلَامَيْنِ مُتَّصِلَيْنِ مَعْنًى بِجُمْلَةٍ أَوْ أَكْثَرَ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ لِنُكْتَةٍ سِوَى دَفْعِ الْإِيهَامِ — bir sözün içine yahut mânâca bağlı iki söz arasına, i'râbda YERİ OLMAYAN bir veya birden çok cümleyi, îhâmı def'in DIŞINDA bir nükte için getirmek (bu istisnâ, tekmîli ayrı bâb tutar). Kaynağın saydığı nükteler: TENZÎH — وَيَجْعَلُونَ لِلّٰهِ الْبَنَاتِ سُبْحَانَهُ وَلَهُمْ مَا يَشْتَهُونَ (16:57): tesbih, iftira ile tamamı arasında patlar; DUÂ — Avf b. Muhallim'in إِنَّ الثَّمَانِينَ وَبُلِّغْتَهَا قَدْ أَحْوَجَتْ سَمْعِي إِلَى تَرْجُمَانْ beyti: «sen de ona erdirilesin!» duâsı inne ile haberi arasında durur; TENBÎH — وَاعْلَمْ فَعِلْمُ الْمَرْءِ يَنْفَعُهُ أَنْ سَوْفَ يَأْتِي كُلُّ مَا قُدِرَا: «kişinin bilgisi ona fayda verir», اعْلَمْ'in mef'ûl cümlesini geciktirir (o cümle de MUHAFFEF أَنْ ile gelir: gizli şan zamiri, سَوْفَ fâsılası). Ara cümle iki söz arasında BİRDEN ÇOK da olabilir: فَأْتُوهُنَّ مِنْ حَيْثُ أَمَرَكُمُ اللهُ إِنَّ اللهَ يُحِبُّ التَّوَّابِينَ وَيُحِبُّ الْمُتَطَهِّرِينَ نِسَاؤُكُمْ حَرْثٌ لَكُمْ (2:222-223). KAPANIŞ HİLÂFLARI: kimi, i'tirâzın nüktesine îhâm def'ini de kattı (o zaman tekmîlin bir kısmını yutar); kimi, sözün TÂ SONUNDA, ardından bir şey gelmeden de câiz gördü (o zaman tezyîlin sahasına taşar); kimi de cümle OLMAYAN ara söze cevaz verdi (o zaman tetmîm ve tekmîl sûretleri içeri düşer). Musannifin dar tarifi, dört bâbı dört tutar."},
 "examples": [
  {"ar": "سُبْحَانَهُ",
   "en": "the tanzih parenthesis (16:57).",
   "tr": "tenzîh ara cümlesi (16:57).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "وَبُلِّغْتَهَا",
   "en": "the du'a parenthesis, between inna and its khabar.",
   "tr": "inne ile haberi arasında duâ ara cümlesi.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "فَعِلْمُ الْمَرْءِ يَنْفَعُهُ",
   "en": "the tanbih parenthesis, delaying «know»'s object clause.",
   "tr": "«bil»in mef'ûl cümlesini geciktiren tenbîh ara cümlesi.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«Ara cümle sözü böler, akışı bozar»",
   "right": "«İ'tirâz, i'râbda yeri olmadığı İÇİN akışı bozamaz — söz üstünden kesilmemiş gibi geçer»",
   "why": {"en": "The parenthesis's badge is precisely its placelessness: hanging on no branch of the i'rab, it can break nothing. Strike سُبْحَانَهُ from 16:57 and the accusation reads straight through — which is why keeping it costs no grammar and buys a cry of glory.",
           "tr": "Ara cümlenin nişanı tam da yersizliğidir: i'râbın hiçbir dalına asılı olmadığından hiçbir şey koparamaz. 16:57'den سُبْحَانَهُ'yu sil, iftira dümdüz okunur — bu yüzden onu tutmak gramere hiçbir şeye mal olmaz, bir tesbih çığlığı kazandırır."}}],
 "relatedNotes": ["asbab-al-itnab", "takmil-wa-tatmim", "tadhyil", "la-nafiya-lil-jins",
                  "maful-mutlaq", "inna-am-anna", "jumla-mutarida", "ism-mawsul"]}

(GR / "itirad.json").write_text(
    json.dumps(NOTE148, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch44:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + ballagha/ahwaja/qadara (+nafaa copied); note 148")
