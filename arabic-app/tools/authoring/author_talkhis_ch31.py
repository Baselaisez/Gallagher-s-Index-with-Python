# -*- coding: utf-8 -*-
"""Author chapter 31 of talkhis-al-miftah — بَابُ الْفَصْلِ وَالْوَصْلِ (first slice).

Sahifa 78-79 (lines ~2245-2300): the definitions, the jumla-atf rule, the
jihat jamia, and the aya of the fasl.

  • الْوَصْلُ عَطْفُ بَعْضِ الْجُمَلِ عَلَى بَعْضٍ، وَالْفَصْلُ تَرْكُهُ.
  • Where the first jumla HAS a mahall and sharing is intended, the second
    is joined exactly as a mufrad would be — زَيْدٌ يَكْتُبُ وَيَشْعُرُ (the
    khabar jumla mahallan marfu', the joined jumla its equal) — and the waw
    demands the JIHAT JAMIA: related musnads on one musnad ilayh, or
    OPPOSED musnads on one musnad ilayh (زَيْدٌ يُعْطِي وَيَمْنَعُ).
  • With no mahall, a non-waw atf letter joins by its own meaning:
    دَخَلَ زَيْدٌ فَخَرَجَ عَمْرٌو (ta'qib), … ثُمَّ خَرَجَ عَمْرٌو (muhla).
  • The FASL: al-Baqara 2:14-15 — اللَّهُ يَسْتَهْزِئُ بِهِمْ is NOT joined
    onto the munafiqun's إِنَّا مَعَكُمْ, because it is not their speech.

ATTRIBUTION: 2:14 (from وَإِذَا خَلَوْا) and 2:15 (opening clause) are
received Qur'anic text quoted exactly in standard imla, as the source
itself prints them; the definitions are the Talkhis matn's own wording
(the source writes them as «وصل؛ عَطْفُ…» — restored to full nominal
sentences with the article, a recorded restoration); the four worked
examples are the source's own, verbatim.

Grammar this chapter teaches:
  • note 135 `al-fasl-wa-al-wasl` — the definitions, the jihat jamia
    (aql/wahm/khayal; the Abu Tammam fault), fa=ta'qib / thumma=muhla,
    and the aya's fasl.
  • engine work: WaslEngine — waslWaw / matufKhabar / faTaqib /
    thummaMuhla frames, rendered beside the shart and insha frames.
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
def copy_verb(pkg, key):
    d = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))["verbs"]
    return d[key]
S = []

TITLE31 = {"ar": "بَابُ الْفَصْلِ وَالْوَصْلِ",
           "en": "Fasl and Wasl: Joining Jumlas",
           "tr": "Fasl ve Vasl: Cümleleri Bağlamak"}

# ------------------------------------------------- s1 — the wasl's definition
S.append({"id": "s1", "translation": {
 "en": "WASL is the joining of some jumlas onto others.",
 "tr": "VASL, cümlelerin bir kısmının bir kısmı üzerine atfıdır."},
 "tokens": [
  tok("الْوَصْلُ","wasl","noun",["al-fasl-wa-al-wasl"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«the wasl» — the mubtada, marfu' by the plain damma.",
      "«vasl» — mübtedâ; açık dammeyle merfû."),
  tok("عَطْفُ","atf","noun",["al-fasl-wa-al-wasl"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ وَهُوَ مُضَافٌ.",
      "«the joining» — the khabar, marfu'; and a mudaf, so it wears no tanwin.",
      "«atfı» — haber; merfû ve muzâftır, bu yüzden tenvin taşımaz."),
  tok("بَعْضِ","bad","noun",["al-fasl-wa-al-wasl"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ.",
      "«some of» — mudaf ilayh in jarr, and itself a mudaf: the chain runs on.",
      "«bir kısmının» — muzâfun ileyh, mecrûr; kendisi de muzâf: zincir sürer."),
  tok("الْجُمَلِ","jumla","noun",["al-fasl-wa-al-wasl"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ الظَّاهِرَةِ.",
      "«the jumlas» — the chain's last mudaf ilayh, majrur by the plain kasra.",
      "«cümlelerin» — zincirin son muzâfun ileyhi; açık kesrayla mecrûr."),
  tok("عَلَى","ala","part",["al-fasl-wa-al-wasl"],
      "حَرْفُ جَرٍّ.",
      "«onto» — a jarr letter.",
      "«üzerine» — cer harfi."),
  tok("بَعْضٍ","bad","noun",["al-fasl-wa-al-wasl"],
      "اسْمٌ مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُتَعَلِّقٌ بِعَطْفُ.",
      "«others» — majrur by ala, the kasra its sign; the phrase hangs on «the joining».",
      "«bir kısmı» — عَلَى ile mecrûr; alâmeti kesra; öbek «atf»a taalluk eder.",
      punct=".")],
 "jumal": [
  J("الْوَصْلُ عَطْفُ بَعْضِ الْجُمَلِ عَلَى بَعْضٍ",
    "جُمْلَةٌ اسْمِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The bab's opening definition: a nominal sentence, no mahall.",
    "Bâbın açılış tarifi: isim cümlesi, mahalsiz."),
  J("الْوَصْلُ عَطْفُ",
    "حَدُّ الْوَصْلِ — وَمَوْضُوعُهُ الْجُمَلُ لَا الْمُفْرَدَاتُ.",
    "THE HADD OF WASL: its subject is JUMLAS, not single words — the whole bab asks when two sentences may share one atf letter.",
    "VASLIN HADDİ: konusu MÜFREDLER değil CÜMLELERDİR — bütün bâb, iki cümlenin bir atıf harfini ne zaman paylaşabileceğini sorar.")]})

# ------------------------------------------------- s2 — the fasl's definition
S.append({"id": "s2", "translation": {
 "en": "And FASL is the leaving of that joining.",
 "tr": "FASL ise o atfın terkidir."},
 "tokens": [
  tok("وَالْفَصْلُ","fasl","noun",["al-fasl-wa-al-wasl"],
      "الْوَاوُ عَاطِفَةٌ، وَالْفَصْلُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«and the fasl» — the waw joins definition onto definition (one bab is their jihat jamia); al-fasl is the mubtada, marfu'.",
      "«fasl ise» — vâv, tarifi tarife atfeder (cihet-i câmiaları tek bâb oluşlarıdır); el-fasl mübtedâdır, merfû.",
      segments=[seg("وَ","wa","part"), seg("الْفَصْلُ","fasl","noun")]),
  tok("تَرْكُ","tark","noun",["al-fasl-wa-al-wasl"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ وَهُوَ مُضَافٌ.",
      "«the leaving» — the khabar, marfu', and a mudaf.",
      "«terki» — haber; merfû ve muzâf."),
  tok("عَطْفِ","atf","noun",["al-fasl-wa-al-wasl"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "«of the joining» — mudaf ilayh in jarr, itself a mudaf.",
      "«atfının» — muzâfun ileyh, mecrûr; kendisi de muzâf."),
  tok("بَعْضِ","bad","noun",["al-fasl-wa-al-wasl"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "«some of» — mudaf ilayh, and again a mudaf.",
      "«bir kısmının» — muzâfun ileyh; yine muzâf."),
  tok("الْجُمَلِ","jumla","noun",["al-fasl-wa-al-wasl"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ الظَّاهِرَةِ.",
      "«the jumlas» — majrur by the plain kasra.",
      "«cümlelerin» — açık kesrayla mecrûr."),
  tok("عَلَى","ala","part",["al-fasl-wa-al-wasl"],
      "حَرْفُ جَرٍّ.",
      "«onto» — a jarr letter.",
      "«üzerine» — cer harfi."),
  tok("بَعْضٍ","bad","noun",["al-fasl-wa-al-wasl"],
      "اسْمٌ مَجْرُورٌ بِعَلَى، مُتَعَلِّقٌ بِعَطْفِ.",
      "«others» — majrur by ala, hanging on «the joining».",
      "«bir kısmı» — عَلَى ile mecrûr; «atf»a taalluk eder.",
      punct=".")],
 "jumal": [
  J("وَالْفَصْلُ تَرْكُ عَطْفِ بَعْضِ الْجُمَلِ عَلَى بَعْضٍ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ عَلَى جُمْلَةِ التَّعْرِيفِ الْأُولَى لَا مَحَلَّ لَهَا.",
    "The mirror definition, joined onto the first — two definitions of one bab share the waw lawfully.",
    "Ayna tarif, birincinin üzerine atfedilmiş — tek bâbın iki tarifi vâvı meşru paylaşır."),
  J("وَالْفَصْلُ تَرْكُ",
    "حَدُّ الْفَصْلِ — تَرْكٌ مَقْصُودٌ، لَا إِهْمَالٌ.",
    "THE HADD OF FASL: a DELIBERATE leaving, never neglect — the bab's four dawa'i name when silence beats the letter.",
    "FASLIN HADDİ: KASITLI bir terk, ihmal değil — bâbın dört dâîsi, sükûtun harfi ne zaman yendiğini adlandırır.")]})

# ------------------------- s3 — the wasl example: related musnads, one subject
S.append({"id": "s3", "translation": {
 "en": "Zayd writes and feels. (the WASL: two khabar jumlas on one subject, joined — the jihat jamia is the kinship of the two predicates.)",
 "tr": "Zeyd yazar ve hisseder. (VASL: tek özne üzerinde iki haber cümlesi, atfedilmiş — cihet-i câmia, iki yüklemin yakınlığıdır.)"},
 "tokens": [
  tok("زَيْدٌ","zayd","propn",["al-fasl-wa-al-wasl"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Zayd» — the mubtada, marfu' by the plain damma: the ONE musnad ilayh both jumlas will lean on.",
      "«Zeyd» — mübtedâ; açık dammeyle merfû: iki cümlenin de dayanacağı TEK müsnedün ileyh."),
  tok("يَكْتُبُ","kataba","verb",["al-fasl-wa-al-wasl"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ، وَالْجُمْلَةُ خَبَرٌ فِي مَحَلِّ رَفْعٍ.",
      "«he writes» — a marfu' mudari, its doer concealed; the JUMLA is the khabar, mahallan marfu'.",
      "«yazar» — merfû muzâri; fâili gizli; CÜMLE haberdir, mahallen merfû."),
  tok("وَيَشْعُرُ","shaara","verb",["al-fasl-wa-al-wasl"],
      "الْوَاوُ عَاطِفَةٌ، وَيَشْعُرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ الْخَبَرِ فِي مَحَلِّ رَفْعٍ.",
      "«and feels» — the waw joins JUMLA onto JUMLA: this clause is ma'tuf on the khabar clause and takes its mahall — raf' — exactly as a mufrad would.",
      "«ve hisseder» — vâv, CÜMLEYİ CÜMLEYE atfeder: bu cümle haber cümlesine ma'tûftur ve onun mahallini — ref'i — tıpkı bir müfred gibi alır.",
      punct=".", segments=[seg("وَ","wa","part"), seg("يَشْعُرُ","shaara","verb")])],
 "jumal": [
  J("يَكْتُبُ",
    "جُمْلَةُ الْخَبَرِ — فِي مَحَلِّ رَفْعٍ.",
    "The khabar clause, mahallan marfu'.",
    "Haber cümlesi — mahallen merfû."),
  J("وَيَشْعُرُ",
    "مَعْطُوفَةٌ عَلَى الْخَبَرِ فِي مَحَلِّ رَفْعٍ — وَالْجِهَةُ الْجَامِعَةُ تَنَاسُبُ الْمُسْنَدَيْنِ مَعَ اتِّحَادِ الْمُسْنَدِ إِلَيْهِ.",
    "Joined onto the khabar, sharing its raf' mahall — and the waw is LAWFUL because a jihat jamia stands: kindred predicates (writing, perceiving) on one and the same subject.",
    "Habere atfedilmiş, ref' mahallini paylaşır — vâv MEŞRUDUR, çünkü cihet-i câmia vardır: bir ve aynı özne üzerinde akraba yüklemler (yazmak, hissetmek).")]})

# --------------------------- s4 — the wasl example: OPPOSED musnads, one subject
S.append({"id": "s4", "translation": {
 "en": "Zayd gives and withholds. (the same waw — but here the jihat jamia is OPPOSITION between the two predicates, on one subject.)",
 "tr": "Zeyd verir ve esirger. (aynı vâv — fakat burada cihet-i câmia, tek özne üzerinde iki yüklemin ZITLIĞIDIR.)"},
 "tokens": [
  tok("زَيْدٌ","zayd","propn",["al-fasl-wa-al-wasl"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Zayd» — the mubtada, marfu'.",
      "«Zeyd» — mübtedâ; merfû."),
  tok("يُعْطِي","aata","verb",["al-fasl-wa-al-wasl"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْجُمْلَةُ خَبَرٌ فِي مَحَلِّ رَفْعٍ.",
      "«he gives» — a mudari whose damma is ESTIMATED on the heavy ya; the clause is the khabar, mahallan marfu'.",
      "«verir» — dammesi ağır yâ üzerinde TAKDÎRÎ muzâri; cümle haberdir, mahallen merfû."),
  tok("وَيَمْنَعُ","manaa","verb",["al-fasl-wa-al-wasl"],
      "الْوَاوُ عَاطِفَةٌ، وَيَمْنَعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ الْخَبَرِ فِي مَحَلِّ رَفْعٍ.",
      "«and withholds» — joined onto the khabar clause, its equal in raf'. Giving against withholding: the OPPOSITION itself is a uniting direction — didd stands next to didd in the mind.",
      "«ve esirger» — haber cümlesine atfedilmiş, ref'te dengi. Vermeye karşı esirgemek: ZITLIĞIN kendisi bir birleştirici yöndür — zıt, zihinde zıddının yanında durur.",
      punct=".", segments=[seg("وَ","wa","part"), seg("يَمْنَعُ","manaa","verb")])],
 "jumal": [
  J("يُعْطِي",
    "جُمْلَةُ الْخَبَرِ — فِي مَحَلِّ رَفْعٍ.",
    "The khabar clause, mahallan marfu'.",
    "Haber cümlesi — mahallen merfû."),
  J("وَيَمْنَعُ",
    "مَعْطُوفَةٌ فِي مَحَلِّ رَفْعٍ — وَالْجِهَةُ الْجَامِعَةُ التَّضَادُّ مَعَ اتِّحَادِ الْمُسْنَدِ إِلَيْهِ.",
    "Joined, sharing the raf' — the jihat jamia here is TADADD: opposition between the musnads with one musnad ilayh. The mind holds a thing and its opposite side by side, so the waw may bind them.",
    "Atfedilmiş, ref'i paylaşır — cihet-i câmia burada TEZATTIR: tek müsnedün ileyh üzerinde müsnedlerin zıtlığı. Zihin, bir şeyle zıddını yan yana tutar; vâv da onları bağlayabilir.")]})

# ------------------------------------------ s5 — the fa: ta'qib, no mahall
S.append({"id": "s5", "translation": {
 "en": "Zayd entered, and Amr left at once. (no mahall on the first jumla — the FA joins by its own meaning: immediate sequence.)",
 "tr": "Zeyd girdi, Amr hemen çıktı. (ilk cümlenin mahalli yok — FÂ kendi mânâsıyla bağlar: hemen ardından.)"},
 "tokens": [
  tok("دَخَلَ","dakhala","verb",["al-fasl-wa-al-wasl"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "«entered» — a mazi, mabni on the fatha.",
      "«girdi» — fetha üzere mebnî mâzî."),
  tok("زَيْدٌ","zayd","propn",["al-fasl-wa-al-wasl"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Zayd» — the fa'il, marfu'.",
      "«Zeyd» — fâil; merfû."),
  tok("فَخَرَجَ","kharaja","verb",["al-fasl-wa-al-wasl"],
      "الْفَاءُ عَاطِفَةٌ لِلتَّعْقِيبِ، وَخَرَجَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "«and at once left» — the FA of TA'QIB: the second deed follows the first with no interval, and that immediacy is the letter's own meaning.",
      "«ve hemen çıktı» — TAKİP FÂSI: ikinci fiil birincinin hemen ardından gelir; o hemenlik, harfin kendi mânâsıdır.",
      segments=[seg("فَ","fa","part"), seg("خَرَجَ","kharaja","verb")]),
  tok("عَمْرٌو","amr-alam","propn",["al-fasl-wa-al-wasl"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْوَاوُ صَامِتَةٌ لِلْفَرْقِ بَيْنَهُ وَبَيْنَ عُمَرَ.",
      "«Amr» — the fa'il, marfu'; its waw is SILENT, written only to tell عَمْرو from عُمَر.",
      "«Amr» — fâil; merfû. Vâvı SESSİZDİR; yalnız عَمْرو'yu عُمَر'den ayırmak için yazılır.",
      punct=".")],
 "jumal": [
  J("دَخَلَ زَيْدٌ",
    "جُمْلَةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The opening jumla — no mahall.",
    "Başlangıç cümlesi — mahalsiz."),
  J("فَخَرَجَ عَمْرٌو",
    "مَعْطُوفَةٌ بِالْفَاءِ عَلَى الِابْتِدَائِيَّةِ لَا مَحَلَّ لَهَا — وَالْفَاءُ لِلتَّعْقِيبِ.",
    "Joined by the FA onto a clause with no mahall — so it shares only the LETTER's meaning: sequence at once, which is what the speaker chose the fa to say.",
    "Mahalsiz cümleye FÂ ile atfedilmiş — paylaştığı yalnız HARFİN mânâsıdır: hemen ardından; konuşan fâ'yı tam bunu söylemek için seçti.")]})

# ------------------------------------------ s6 — thumma: muhla, no mahall
S.append({"id": "s6", "translation": {
 "en": "Zayd entered; then, after a while, Amr left. (same two deeds — THUMMA writes the pause between them.)",
 "tr": "Zeyd girdi; sonra, bir süre geçince, Amr çıktı. (aynı iki fiil — ثُمَّ aradaki mühleti yazar.)"},
 "tokens": [
  tok("دَخَلَ","dakhala","verb",["al-fasl-wa-al-wasl"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "«entered» — a mazi, mabni on the fatha.",
      "«girdi» — fetha üzere mebnî mâzî."),
  tok("زَيْدٌ","zayd","propn",["al-fasl-wa-al-wasl"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Zayd» — the fa'il, marfu'.",
      "«Zeyd» — fâil; merfû."),
  tok("ثُمَّ","thumma","part",["al-fasl-wa-al-wasl"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.",
      "«then» — the atf letter of ordered sequence WITH an interval: the muhla is thumma's own meaning.",
      "«sonra» — sıralı VE aralıklı atıf harfi: mühlet, ثُمَّ'nin kendi mânâsıdır."),
  tok("خَرَجَ","kharaja","verb",["al-fasl-wa-al-wasl"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "«left» — a mazi, mabni on the fatha.",
      "«çıktı» — fetha üzere mebnî mâzî."),
  tok("عَمْرٌو","amr-alam","propn",["al-fasl-wa-al-wasl"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْوَاوُ صَامِتَةٌ.",
      "«Amr» — the fa'il, marfu'; the silent waw again.",
      "«Amr» — fâil; merfû; sessiz vâv yine.",
      punct=".")],
 "jumal": [
  J("دَخَلَ زَيْدٌ",
    "جُمْلَةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The opening jumla — no mahall.",
    "Başlangıç cümlesi — mahalsiz."),
  J("ثُمَّ خَرَجَ عَمْرٌو",
    "مَعْطُوفَةٌ بِثُمَّ لَا مَحَلَّ لَهَا — وَثُمَّ لِلْمُهْلَةِ.",
    "Joined by THUMMA: one letter apart from s5, and the whole difference is the pause — choose the letter, and the interval is said without a word for it.",
    "ثُمَّ ile atfedilmiş: s5'ten tek harf farkla — bütün fark, aradaki mühlettir; harfi seç, aralık tek kelime harcanmadan söylenmiş olur.")]})

# --------------------------- s7 — al-Baqara 2:14 (from the source's citation)
S.append({"id": "s7", "translation": {
 "en": "And when they are alone with their satans they say: we are with you; we were only mocking. (al-Baqara 2:14)",
 "tr": "Şeytanlarıyla baş başa kaldıklarında ise derler ki: biz sizinleyiz; biz yalnızca alay ediyorduk. (Bakara 2:14)"},
 "tokens": [
  tok("وَإِذَا","idha","part",["al-fasl-wa-al-wasl"],
      "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ تَضَمَّنَ مَعْنَى الشَّرْطِ.",
      "«and when» — the waw joins the aya's clauses; idha is the zarf carrying a shart's meaning, its jawab the qawl to come.",
      "«ve …dıklarında» — vâv âyet cümlelerini bağlar; إِذَا, şart mânâsı yüklü zarftır; cevabı gelecek olan sözdür.",
      segments=[seg("وَ","wa","part"), seg("إِذَا","idha","part")]),
  tok("خَلَوْا","khala","verb",["al-fasl-wa-al-wasl"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ الْمُقَدَّرِ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ.",
      "«they are alone» — a naqis mazi, mabni on a damm ESTIMATED on the alif the two sakins deleted; the group's waw is the fa'il.",
      "«baş başa kalırlar» — nâkıs mâzî; iki sâkinin düşürdüğü elif üzerinde TAKDÎRÎ damme ile mebnî; cemaat vâvı fâildir."),
  tok("إِلَى","ila","part",["al-fasl-wa-al-wasl"],
      "حَرْفُ جَرٍّ.",
      "«with (toward)» — a jarr letter: خَلَا إِلَى is the idiom of withdrawing to be alone with.",
      "«…e (doğru)» — cer harfi: خَلَا إِلَى, biriyle baş başa kalmaya çekilme deyimidir."),
  tok("شَيَاطِينِهِمْ","shaytan","noun",["al-fasl-wa-al-wasl"],
      "اسْمٌ مَجْرُورٌ بِالْكَسْرَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ، مُتَعَلِّقٌ بِخَلَوْا.",
      "«their satans» — majrur; the pronoun is the mudaf ilayh; the phrase hangs on the verb.",
      "«şeytanlarına» — mecrûr; zamir muzâfun ileyhtir; öbek fiile taalluk eder.",
      segments=[seg("شَيَاطِينِ","shaytan","noun"), seg("هِمْ","pron-3mp","pron")]),
  tok("قَالُوا","qala","verb",["al-fasl-wa-al-wasl"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ جَوَابُ إِذَا.",
      "«they say» — mabni on the damm for the group's waw; the clause is IDHA's jawab.",
      "«derler» — cemaat vâvına bitiştiği için damme üzere mebnî; cümle, إِذَا'nın cevabıdır."),
  tok("إِنَّا","inna","part",["al-fasl-wa-al-wasl"],
      "إِنَّ حَرْفٌ نَاسِخٌ، وَنَا ضَمِيرٌ مُتَّصِلٌ اسْمُهَا فِي مَحَلِّ نَصْبٍ.",
      "«indeed we» — inna with its ism fused on: the na, in the position of nasb.",
      "«şüphesiz biz» — إِنَّ ile bitişik ismi: نَا, mahallen mansub.",
      segments=[seg("إِنَّ","inna","part"), seg("نَا","pron-1p","pron")]),
  tok("مَعَكُمْ","maa","noun",["al-fasl-wa-al-wasl"],
      "ظَرْفٌ مَنْصُوبٌ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ إِنَّ، وَالْكَافُ مُضَافٌ إِلَيْهِ.",
      "«with you» — the zarf, hanging on an omitted amil that is inna's KHABAR; the pronoun is its mudaf ilayh.",
      "«sizinle» — zarf; mahzûf bir âmile taalluk eder ki o, إِنَّ'nin HABERİDİR; zamir muzâfun ileyhtir.",
      segments=[seg("مَعَ","maa","noun"), seg("كُمْ","pron-2mp","pron")]),
  tok("إِنَّمَا","innama","part",["al-fasl-wa-al-wasl","qasr"],
      "كَافَّةٌ وَمَكْفُوفَةٌ — أَدَاةُ قَصْرٍ.",
      "«only» — inna with the restraining ma: a qasr tool; the government is stopped and the restriction remains.",
      "«ancak» — kâffe مَا ile إِنَّ: bir kasr edatı; amel durdurulmuş, kasr kalmıştır."),
  tok("نَحْنُ","nahnu","pron",["al-fasl-wa-al-wasl"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "«we» — the detached pronoun, mabni, in the position of raf': the mubtada.",
      "«biz» — munfasıl zamir; mebnî, mahallen merfû: mübtedâ."),
  tok("مُسْتَهْزِئُونَ","istahzaa","noun",["al-fasl-wa-al-wasl"],
      "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "«mockers» — the khabar, marfu' by the WAW: a sound masculine plural declines by letters.",
      "«alay edenleriz» — haber; VÂV ile merfû: cem'-i müzekker sâlim harflerle i'rablanır.",
      punct=".")],
 "jumal": [
  J("وَإِذَا خَلَوْا إِلَى شَيَاطِينِهِمْ قَالُوا",
    "جُمْلَةُ الشَّرْطِ وَجَوَابِهِ — مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا فِي الْآيَاتِ.",
    "The idha frame with its jawab, joined onto the ayat before it.",
    "Cevabıyla birlikte إِذَا çatısı — önceki âyetlere atfedilmiş."),
  J("إِنَّا مَعَكُمْ إِنَّمَا نَحْنُ مُسْتَهْزِئُونَ",
    "مَقُولُ الْقَوْلِ — فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    "THE QUOTED SPEECH: everything inside the munafiqun's mouths, in the position of nasb as the object of «they say» — mark where it ENDS, for the next sentence stands outside it.",
    "MEKÛLÜ'L-KAVL: münafıkların ağzındaki her şey; «derler»in mef'ûlü olarak mahallen mansub — NEREDE BİTTİĞİNİ işaretle; sonraki cümle onun dışındadır.")]})

# --------------------------- s8 — al-Baqara 2:15 (opening) — THE FASL
S.append({"id": "s8", "translation": {
 "en": "Allah mocks them. (al-Baqara 2:15 — NOT joined onto their speech: the fasl, because these are not the munafiqun's words.)",
 "tr": "Allah onlarla alay eder. (Bakara 2:15 — sözlerinin üzerine atfedilmemiştir: FASL; çünkü bu, münafıkların sözü değildir.)"},
 "tokens": [
  tok("اللَّهُ","allah","propn",["al-fasl-wa-al-wasl"],
      "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Allah» — the Name, the mubtada, marfu' — and NO atf letter stands before it: the absence is the bab's whole lesson.",
      "«Allah» — lafza-i celâl, mübtedâ, merfû — ve önünde HİÇBİR atıf harfi yok: bu yokluk, bâbın bütün dersidir."),
  tok("يَسْتَهْزِئُ","istahzaa","verb",["al-fasl-wa-al-wasl"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ، وَالْجُمْلَةُ خَبَرٌ فِي مَحَلِّ رَفْعٍ.",
      "«mocks» — a marfu' mudari, its doer concealed; the clause is the khabar, mahallan marfu'.",
      "«alay eder» — merfû muzâri; fâili gizli; cümle haberdir, mahallen merfû."),
  tok("بِهِمْ","bi","part",["al-fasl-wa-al-wasl"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِيَسْتَهْزِئُ.",
      "«at them» — the jarr phrase, hanging on the verb.",
      "«onlarla» — câr-mecrûr; fiile taalluk eder.",
      punct=".", segments=[seg("بِ","bi","part"), seg("هِمْ","pron-3mp","pron")])],
 "jumal": [
  J("اللَّهُ يَسْتَهْزِئُ بِهِمْ",
    "جُمْلَةٌ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا — فُصِلَتْ وَلَمْ تُعْطَفْ.",
    "AN ISTI'NAF, no mahall — the FASL itself: had a waw joined it onto إِنَّا مَعَكُمْ, it would read as the munafiqun's own words. The silence protects the meaning.",
    "İSTİ'NÂF, mahalsiz — FASLIN kendisi: bir vâv onu إِنَّا مَعَكُمْ'a bağlasaydı, münafıkların kendi sözü gibi okunurdu. Sükût, mânâyı korur."),
  J("يَسْتَهْزِئُ بِهِمْ",
    "جُمْلَةُ الْخَبَرِ — فِي مَحَلِّ رَفْعٍ.",
    "The khabar clause, mahallan marfu'.",
    "Haber cümlesi — mahallen merfû.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "wasl": g("وَصْل", "و ص ل", "noun", "joining, connection (of jumlas by atf)", "vasl, bağlama (cümlelerin atfı)", 6),
 "fasl": g("فَصْل", "ف ص ل", "noun", "separation; leaving the joining", "fasl, ayırma; atfı terk", 6),
 "atf": g("عَطْف", "ع ط ف", "noun", "joining, coordination (atf)", "atıf, bağlama", 5),
 "tark": g("تَرْك", "ت ر ك", "noun", "leaving, abandoning (masdar)", "terk, bırakma (masdar)", 4),
 "jumla": g("جُمْلَة", "ج م ل", "noun", "sentence, clause", "cümle", 3, plural="جُمَل"),
 "shaytan": g("شَيْطَان", "ش ط ن", "noun", "satan, devil", "şeytan", 2, plural="شَيَاطِين"),
 "shaara": g("شَعَرَ", "ش ع ر", "verb", "to feel, perceive", "hissetmek, sezmek", 4, form="I"),
 "manaa": g("مَنَعَ", "م ن ع", "verb", "to withhold, prevent", "esirgemek, engellemek", 3, form="I"),
 "aata": g("أَعْطَى", "ع ط و", "verb", "to give", "vermek", 2, form="IV"),
 "bad": copy_gloss("wasiyyat-abi-hanifa-samti", "bad"),
 "wa": copy_gloss("wasiyyat-abi-hanifa-samti", "wa") if False else None,  # wa already in talkhis
 "kataba": copy_gloss("jumal-al-tadrib", "kataba"),
 "dakhala": copy_gloss("wasiyyat-abi-hanifa-samti", "dakhala"),
 "kharaja": copy_gloss("wasiyyat-abi-hanifa-samti", "kharaja"),
 "thumma": copy_gloss("wasiyyat-abi-hanifa", "thumma"),
 "idha": copy_gloss("wasiyyat-abi-hanifa-samti", "idha"),
 "qala": copy_gloss("wasiyyat-abi-hanifa-samti", "qala"),
 "khala": None,  # resolved below: broadened gloss + the aqaid paradigm
}
# the khala entry: the aqaid gloss says «to pass away, be gone», which is the
# same verb خَلَا — the aya's use is خَلَا إِلَى, «to withdraw to be alone
# with». A global lex key must agree with itself across packages, so the
# BROADENED gloss is written into BOTH packages in the same run.
KHALA = {"lemma": "خَلَا", "root": "خ ل و", "pos": "verb", "form": "I",
         "gloss": {"en": "to be devoid, pass away; (خَلَا إِلَى) to withdraw to be alone with",
                   "tr": "boş kalmak, geçip gitmek; (خَلَا إِلَى) biriyle baş başa kalmak"},
         "level": 4}
GLOSS_ADD["khala"] = KHALA
del GLOSS_ADD["wa"]

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/31.json").write_text(
    json.dumps({"chapter": 31, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 31 for c in man["chapters"]):
    man["chapters"].append({"n": 31, "title": TITLE31})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.31.0"
ADD_EN = (" Chapter 31 carries the fasl-wasl bab's first slice (lines ~2245-2300, sahifa "
          "78-79): s7-s8 are received Qur'anic text quoted exactly — al-Baqara 2:14 (from "
          "وَإِذَا خَلَوْا) and the opening clause of 2:15 — in standard imla as the source "
          "itself prints them; the two definitions are the Talkhis matn's wording, restored "
          "from the source's «وصل؛ عَطْفُ…» headings to full nominal sentences (a recorded "
          "restoration); the four worked examples are the source's own, verbatim.")
ADD_TR = (" Otuz birinci bâb, fasl-vasl bâbının ilk dilimini taşır (satır ~2245-2300, sahife "
          "78-79): s7-s8 aynen alınmış mervî Kur'ân metnidir — Bakara 2:14 (وَإِذَا خَلَوْا'dan "
          "itibaren) ve 2:15'in açılış cümlesi — kaynağın kendi bastığı standart imlâ ile; iki "
          "tarif, Telhis metninin ifadesidir ve kaynaktaki «وصل؛ عَطْفُ…» başlıklarından tam "
          "isim cümlelerine tamamlanmıştır (kayıtlı bir tamamlama); dört işlenmiş örnek, "
          "kaynağın kendi örneklerinin aynen alınmışıdır.")
if "2245-2300" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
# …and the SAME broadened khala gloss into aqaid, so the global key agrees
AQ = ROOT / "content/samples/aqaid-ahl-al-sunna"
aqgl = json.loads((AQ / "glossary.json").read_text(encoding="utf-8"))
if "khala" in aqgl["entries"]:
    aqgl["entries"]["khala"]["gloss"] = dict(KHALA["gloss"])
    (AQ / "glossary.json").write_text(json.dumps(aqgl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "shaara" not in mo["verbs"]:
    mo["verbs"]["shaara"] = _sg.sound1(
        "nasara", "شَعَر", "شْعُر", "اُشْعُر", "شُعُور", "شَاعِر")
if "manaa" not in mo["verbs"]:
    mo["verbs"]["manaa"] = _sg.sound1(
        "fataha", "مَنَع", "مْنَع", "اِمْنَع", "مَنْع", "مَانِع",
        "مَمْنُوع", "مُنِعَ", "يُمْنَعُ")
if "aata" not in mo["verbs"]:
    mo["verbs"]["aata"] = _sg.derived_naqis(
        _sg.B4 + " — نَاقِصٌ", _sg.W4, "ُ", "أَعْطَ", "عْط", "i", "أَعْط",
        "إِعْطَاء", "مُعْطٍ", "مُعْطًى", "أُعْطِيَ", "يُعْطَى")
for key, pkg in [("kataba", "jumal-al-tadrib"), ("khala", "aqaid-ahl-al-sunna"),
                 ("qala", "wasiyyat-abi-hanifa-samti"), ("idha", None)]:
    if pkg and key not in mo["verbs"]:
        mo["verbs"][key] = copy_verb(pkg, key)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 135
GR = ROOT / "content/grammar"
NOTE135 = {
 "id": "al-fasl-wa-al-wasl",
 "title": {"ar": "الْفَصْلُ وَالْوَصْلُ", "en": "Fasl and wasl: when jumlas join", "tr": "Fasl ve vasl: cümleler ne zaman bağlanır"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح (الخطيب القزويني) — باب الفصل والوصل"],
 "question": {
  "en": ["Does the first jumla hold a mahall, and is sharing it intended? Then join as you would a mufrad — with the jihat jamia as the waw's price.",
         "Is a non-waw letter doing the joining? Its own meaning (fa: at once; thumma: after a pause) is the reason it was chosen.",
         "Would joining put the second jumla into the first speaker's mouth — اللَّهُ يَسْتَهْزِئُ بِهِمْ? Then FASL: leave the letter out."],
  "tr": ["İlk cümlenin mahalli var ve ortaklık mı kastediliyor? O hâlde müfred gibi bağla — vâvın bedeli cihet-i câmiadır.",
         "Bağlamayı vâv dışı bir harf mi yapıyor? Kendi mânâsı (fâ: hemen; ثُمَّ: mühletle) seçilme sebebidir.",
         "Bağlamak, ikinci cümleyi ilk konuşanın ağzına mı koyar — اللَّهُ يَسْتَهْزِئُ بِهِمْ? O hâlde FASL: harfi bırak."]},
 "plain": {
  "en": "Wasl joins jumla onto jumla with an atf letter; fasl deliberately leaves the letter out. The joined jumla takes the first one's seat, and the waw demands a jihat jamia — a direction uniting the two. Where joining would corrupt the meaning, silence IS the eloquence: no waw ties 2:15 to the mockers' speech.",
  "tr": "Vasl, cümleyi cümleye atıf harfiyle bağlar; fasl, harfi kasıtla bırakır. Atfedilen cümle ilkinin makamını alır; vâv, ikisini birleştiren bir cihet-i câmia ister. Bağlamanın mânâyı bozacağı yerde sükûtun kendisi belâgattir: hiçbir vâv اللَّهُ يَسْتَهْزِئُ بِهِمْ'i münafıkların sözüne bağlamaz."},
 "explanation": {
  "en": "الْوَصْلُ عَطْفُ بَعْضِ الْجُمَلِ عَلَى بَعْضٍ، وَالْفَصْلُ تَرْكُهُ. Where the first jumla HAS a mahall and the second is meant to share its hukm, the second is joined exactly as a mufrad would be: in زَيْدٌ يَكْتُبُ وَيَشْعُرُ the khabar clause is mahallan marfu' and وَيَشْعُرُ, joined onto it, is mahallan marfu' too. The waw's condition is the JIHAT JAMIA — a closeness in aql, wahm or khayal between the two jumlas: kindred musnads on one musnad ilayh (writing/perceiving), or opposed ones (يُعْطِي وَيَمْنَعُ — the mind holds a thing beside its opposite). Abu Tammam's وَأَنَّ أَبَا الْحُسَيْنِ كَرِيمٌ joined onto أَنَّ النَّوَى صَبِرٌ was faulted for exactly the missing jiha. Where the first jumla has NO mahall, a non-waw letter joins by its own table meaning — دَخَلَ زَيْدٌ فَخَرَجَ عَمْرٌو (ta'qib), ثُمَّ خَرَجَ عَمْرٌو (muhla) — and the FASL stands where joining would lie: in al-Baqara 2:14-15 the munafiqun's speech ends at مُسْتَهْزِئُونَ, and اللَّهُ يَسْتَهْزِئُ بِهِمْ is cut loose from it, because a waw would have read it as THEIR words.",
  "tr": "الْوَصْلُ عَطْفُ بَعْضِ الْجُمَلِ عَلَى بَعْضٍ، وَالْفَصْلُ تَرْكُهُ. İlk cümlenin mahalli VARSA ve ikincinin hükme ortaklığı kastediliyorsa, ikincisi tıpkı bir müfred gibi atfedilir: زَيْدٌ يَكْتُبُ وَيَشْعُرُ'de haber cümlesi mahallen merfûdur ve ona atfedilen وَيَشْعُرُ de mahallen merfûdur. Vâvın şartı CİHET-İ CÂMİAdır — iki cümle arasında akıl, vehim veya hayâl yönünden yakınlık: tek müsnedün ileyh üzerinde akraba müsnedler (yazmak/hissetmek) veya zıt müsnedler (يُعْطِي وَيَمْنَعُ — zihin, bir şeyi zıddının yanında tutar). Ebû Temmâm'ın أَنَّ النَّوَى صَبِرٌ üzerine bağladığı وَأَنَّ أَبَا الْحُسَيْنِ كَرِيمٌ, tam da eksik ciheti yüzünden ayıplandı. İlk cümlenin mahalli YOKSA, vâv dışı bir harf kendi tablo mânâsıyla bağlar — دَخَلَ زَيْدٌ فَخَرَجَ عَمْرٌو (takip), ثُمَّ خَرَجَ عَمْرٌو (mühlet) — ve bağlamanın yalan söyleyeceği yerde FASL durur: Bakara 2:14-15'te münafıkların sözü مُسْتَهْزِئُونَ'da biter; اللَّهُ يَسْتَهْزِئُ بِهِمْ ondan koparılmıştır, çünkü bir vâv onu ONLARIN sözü gibi okuturdu.",
 },
 "examples": [
  {"ar": "زَيْدٌ يَكْتُبُ وَيَشْعُرُ",
   "en": "«Zayd writes and feels» — wasl: the joined clause shares the khabar's mahall.",
   "tr": "«Zeyd yazar ve hisseder» — vasl: atfedilen cümle, haberin mahallini paylaşır.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "دَخَلَ زَيْدٌ فَخَرَجَ عَمْرٌو",
   "en": "«Zayd entered and Amr left at once» — the fa's own meaning does the joining.",
   "tr": "«Zeyd girdi, Amr hemen çıktı» — bağlamayı fânın kendi mânâsı yapar.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s5"},
  {"ar": "اللَّهُ يَسْتَهْزِئُ بِهِمْ",
   "en": "«Allah mocks them» (2:15) — the fasl: no waw, or it would read as the munafiqun's own speech.",
   "tr": "«Allah onlarla alay eder» (2:15) — fasl: vâv yok; olsaydı münafıkların kendi sözü gibi okunurdu.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s8"}],
 "commonMistakes": [
  {"wrong": "«Her iki cümle arasına vâv koymak güvenlidir»",
   "right": "«Vâv, cihet-i câmia ister; yanlış vâv mânâyı başkasının ağzına koyar»",
   "why": {"en": "The waw is the one atf letter with NO meaning of its own beyond joining — so what licenses it is entirely the uniting direction between the jumlas. Without one, the join is the fault the critics fixed on Abu Tammam; across a speech boundary, it rewrites who said what.",
           "tr": "Vâv, bağlamaktan öte KENDİ mânâsı olmayan tek atıf harfidir — onu meşrulaştıran, tamamen cümleler arasındaki birleştirici yöndür. O yön yoksa, atıf, eleştirmenlerin Ebû Temmâm'a yapıştırdığı ayıptır; bir söz sınırının üzerinden ise kimin ne dediğini yeniden yazar."}}],
 "relatedNotes": ["anwa-al-waw", "anwa-al-jumal", "qasr"]}

(GR / "al-fasl-wa-al-wasl.json").write_text(
    json.dumps(NOTE135, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch31:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + shaara, manaa, aata, copies; note 135")
