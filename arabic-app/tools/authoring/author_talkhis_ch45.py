# -*- coding: utf-8 -*-
"""Author chapter 45 of talkhis-al-miftah — the tail of the itnab chapter:
the MULTI-JUMLA i'tirad, the closing khilafs, itnab by OTHER causes, and
the RELATIVE ijaz and itnab (sahifa 100-101, lines ~2905-2950).

  • 2:222-223 — فَأْتُوهُنَّ مِنْ حَيْثُ أَمَرَكُمُ اللهُ | إِنَّ اللهَ يُحِبُّ
    التَّوَّابِينَ وَيُحِبُّ الْمُتَطَهِّرِينَ | نِسَاؤُكُمْ حَرْثٌ لَكُمْ — TWO jumlas
    of parenthesis between two speeches joined in meaning (the second is
    the bayan of the first).
  • the three closing khilafs on i'tirad's reach (s4-s7).
  • itnab by a cause the list did not name: 40:7 وَيُؤْمِنُونَ بِهِ — the
    nobility of faith shown to make it desired (s8-s9).
  • ijaz and itnab as RELATIVE descriptions — by the count of a speech's
    letters against another speech equal to it in the root of its meaning
    (s10-s11): Abu Tammam's bayt (ijaz in its first hemistich, s12-s13)
    against 'Abd al-Samad's (itnab, s14-s15); 21:23 (s16) against
    al-Hamasi's bayt (s17-s18) — «and near to it», says the musannif.

ATTRIBUTION: s1-s3 are al-Baqara 2:222-223 (parts), s9 is Ghafir 40:7
(part), s16 is al-Anbiya 21:23 — received Qur'anic text quoted in
standard imla; the source prints فَاْتُوهُنَّ، اَمَرَكُمُ، اِنَّ، اَلَّذِينَ،
يُسْئَلُ، يُسْئَلُونَ with its own hamza seats, written here فَأْتُوهُنَّ،
أَمَرَكُمُ، إِنَّ، الَّذِينَ، يُسْأَلُ، يُسْأَلُونَ. s12-s13 (Abu Tammam), s14-s15
('Abd al-Samad) and s17-s18 (al-Hamasi) are the bayts as the source
recites them, split at the hemistich, نَاهِدِ keeping the source's rhyme
kasra without tanwin. s10-s11 are the musannif's own words on the
relative ijaz (the source quotes the matn in its paraphrase and the
received text is unmistakable). s4-s8 are RESTORATIONS: the source gives
these khilafs and the lead-in to 40:7 only in Ottoman-Turkish
paraphrase, and the Arabic here restores them in the musannif's
definitional register — they are marked in their translations and are
NOT quotations of the matn.

Grammar this chapter teaches:
  • note 149 `ijaz-itnab-nisbi` — ijaz and itnab as relative
    descriptions, and the four texts weighed against each other.
  • the amr on the group's waw before an attached pronoun (فَأْتُوهُنَّ);
    حَيْثُ annexed to a jumla; the mubalagha shapes تَوَّاب and نَظَّار; the
    zaida ba in لَيْسَ's khabar; لَوْ الْوَصْلِيَّة; a rhyme's dropped tanwin;
    the two passives of سَأَلَ side by side (21:23).
  • new paradigms: أَمَرَ (hamzated), أَحَبَّ (IV geminate, from أَحَلَّ's
    stored pattern), جَوَّزَ and سَبَّحَ (II), شَمِلَ, بَرَزَ, and the two
    Form I geminates صَدَّ (from سَرَّ) and عَنَّ (from شَبَّ); copies of
    حَمَلَ، آمَنَ، أَنْكَرَ، وَلِيَ from their packages.
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
def copy_morph(pkg, key):
    return json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))["verbs"][key]
S = []

TITLE45 = {"ar": "الِاعْتِرَاضُ بِجُمْلَتَيْنِ، وَالْإِيجَازُ وَالْإِطْنَابُ النِّسْبِيَّانِ",
           "en": "The Two-Jumla Parenthesis, and Ijaz and Itnab as Relative Terms",
           "tr": "İki Cümlelik Ara Cümle; Nispî Îcâz ve Itnâb"}

# ----------- s1 — 2:222, the first speech
S.append({"id": "s1", "translation": {
 "en": "So come to them from where Allah has commanded you — (2:222) — the first speech, before the parenthesis.",
 "tr": "Onlara Allah'ın size emrettiği yerden gelin — (2:222) — ara cümleden önceki ilk söz."},
 "tokens": [
  tok("فَأْتُوهُنَّ","ata","verb",["itirad","imperative-amr"],
      "الْفَاءُ عَاطِفَةٌ، وَأْتُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَهُنَّ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ.",
      "«so come to them» — the group's amr, built on dropping its nun; the waw is the doer, and the attached هُنَّ its object. Before a pronoun the waw sheds its alif of separation.",
      "«onlara gelin» — cemi emri, nûnunun hazfi üzere mebnî; vâv fâil, bitişik هُنَّ mef'ûl. Zamirden önce vâv, ayırma elifini bırakır.",
      segments=[seg("فَ","fa","conj"), seg("أْتُوا","ata","verb"), seg("هُنَّ","pron-3fp","pron")]),
  tok("مِنْ","min","part",["itirad","huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«from» —",
      "«-den» —"),
  tok("حَيْثُ","hayth","noun",["itirad","maful-fih"],
      "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ بِمِنْ، وَهُوَ مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.",
      "«where» — the place-zarf built on damma, in the place of jarr after مِنْ, and annexed to the whole clause that follows it.",
      "«yerden» — damme üzere mebnî mekân zarfı, مِنْ'den sonra mahallen mecrur; ardındaki cümleye muzâf."),
  tok("أَمَرَكُمُ","amara-v","verb",["itirad","maful-bihi"],
      "فِعْلٌ مَاضٍ، وَالْكَافُ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ — وَضُمَّتْ مِيمُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ حَيْثُ.",
      "«has commanded you» — mazi with its object pronoun; the mim takes a damma before the jalala's wasl (two quiescents meeting), and the clause sits in jarr as حَيْثُ's mudaf ilayh.",
      "«size emretti» — mef'ûl zamirli mâzî; mîm, celâlenin vaslından önce (iki sâkin buluşunca) damme alır; cümle حَيْثُ'ün muzâfun ileyhi olarak mahallen mecrur.",
      segments=[seg("أَمَرَ","amara-v","verb"), seg("كُمُ","pron-2mp","pron")]),
  tok("اللهُ","allah","propn",["itirad","fail"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.",
      "«Allah» — the fa'il.",
      "«Allah» — fâil.",
      punct="،")],
 "jumal": [
  J("فَأْتُوهُنَّ مِنْ حَيْثُ أَمَرَكُمُ اللهُ",
    "الْكَلَامُ الْأَوَّلُ — وَالِاعْتِرَاضُ يَلِيهِ بِجُمْلَتَيْنِ.",
    "The first of the two speeches; the two-jumla parenthesis follows it.",
    "İki sözün ilki; iki cümlelik ara cümle onu izler."),
  J("أَمَرَكُمُ اللهُ",
    "جُمْلَةٌ فِي مَحَلِّ جَرٍّ — مُضَافٌ إِلَيْهَا حَيْثُ.",
    "A clause in the place of jarr: حَيْثُ is annexed to sentences, never to single words.",
    "Mahallen mecrur cümle: حَيْثُ tek kelimeye değil, cümleye muzâf olur.")]})

# ----------- s2 — the two-jumla parenthesis
S.append({"id": "s2", "translation": {
 "en": "Truly Allah loves those who turn in repentance and loves those who purify themselves — TWO jumlas of parenthesis between the two speeches.",
 "tr": "Şüphesiz Allah çok tevbe edenleri sever ve temizlenenleri sever — iki söz arasında İKİ cümlelik ara cümle."},
 "tokens": [
  tok("إِنَّ","inna","part",["itirad","inna-wa-akhawatuha"],
      "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.",
      "«truly» — the parenthesis opens on inna.",
      "«şüphesiz» — ara cümle inne ile açılır."),
  tok("اللهَ","allah","propn",["itirad","inna-wa-akhawatuha"],
      "اسْمُ إِنَّ مَنْصُوبٌ.",
      "«Allah» — inna's ism.",
      "«Allah» — inne'nin ismi."),
  tok("يُحِبُّ","ahabba","verb",["itirad","form-iv-verbs","doubled-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ إِنَّ. مُضَاعَفٌ مِنَ الْإِفْعَالِ: أَحَبَّ يُحِبُّ.",
      "«loves» — a Form IV geminate (أَحَبَّ يُحِبُّ); its clause is inna's khabar.",
      "«sever» — IV. bâbdan muzâaf (أَحَبَّ يُحِبُّ); cümlesi inne'nin haberi."),
  tok("التَّوَّابِينَ","tawwab","noun",["itirad","sighat-mubalagha","jam-mudhakkar-salim"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — وَفَعَّالٌ صِيغَةُ مُبَالَغَةٍ.",
      "«those who ever repent» — the sound masculine plural's nasb is a ya; فَعَّال is the intensive shape.",
      "«çok tevbe edenleri» — cem'-i müzekker-i sâlimin nasbı yâ iledir; فَعَّال mübalağa sîgası."),
  tok("وَيُحِبُّ","ahabba","verb",["itirad","atf-nasaq","form-iv-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ الْخَبَرِ.",
      "«and loves» — the second jumla of the parenthesis, joined to the first.",
      "«ve sever» — ara cümlenin ikinci cümlesi, ilkine atfedilmiş.",
      segments=[seg("وَ","wa","conj"), seg("يُحِبُّ","ahabba","verb")]),
  tok("الْمُتَطَهِّرِينَ","mutatahhir","noun",["itirad","ism-fail","form-v-verbs","jam-mudhakkar-salim"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ — اسْمُ فَاعِلٍ مِنْ تَطَهَّرَ.",
      "«those who purify themselves» — Form V's ism fa'il, plural in the ya.",
      "«temizlenenleri» — V. bâbın ism-i fâili, yâ ile cemi.",
      punct="،")],
 "jumal": [
  J("إِنَّ اللهَ يُحِبُّ التَّوَّابِينَ وَيُحِبُّ الْمُتَطَهِّرِينَ",
    "جُمْلَتَا الِاعْتِرَاضِ — بَيْنَ كَلَامَيْنِ مُتَّصِلَيْنِ مَعْنًى، وَلَا مَحَلَّ لَهُمَا.",
    "The parenthesis as TWO jumlas («one jumla OR MORE», the definition said), placeless between two speeches joined in meaning.",
    "İKİ cümlelik ara cümle (tarif «bir cümle YAHUT DAHA ÇOK» demişti); mânâca bağlı iki söz arasında, mahalsiz.")]})

# ----------- s3 — 2:223, the second speech
S.append({"id": "s3", "translation": {
 "en": "Your women are a tilth for you (2:223) — the second speech, the bayan of the first: the two are joined in meaning across the parenthesis.",
 "tr": "Kadınlarınız sizin için bir tarladır (2:223) — ikinci söz, ilkinin beyânı: ikisi ara cümlenin üstünden mânâca bağlıdır."},
 "tokens": [
  tok("نِسَاؤُكُمْ","nisa","noun",["itirad","mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — وَكُتِبَتِ الْهَمْزَةُ عَلَى وَاوٍ لِضَمَّتِهَا.",
      "«your women» — the mubtada, definite by its annexation; the hamza sits on a waw because it carries the damma.",
      "«kadınlarınız» — izâfetle mârife mübtedâ; hemze dammeli olduğundan vâv üzerine yazılır.",
      segments=[seg("نِسَاءُ","nisa","noun"), seg("كُمْ","pron-2mp","pron")]),
  tok("حَرْثٌ","harth","noun",["itirad","mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.",
      "«a tilth» — the khabar.",
      "«bir tarladır» — haber."),
  tok("لَكُمْ","li","part",["itirad","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِصِفَةٍ مَحْذُوفَةٍ لِحَرْثٍ.",
      "«for you» — the jarr phrase hanging on an unspoken sifa of حَرْثٌ.",
      "«sizin için» — حَرْثٌ'ün hazfedilmiş sıfatına bağlı câr-mecrûr.",
      punct=".",
      segments=[seg("لَ","li","part"), seg("كُمْ","pron-2mp","pron")])],
 "jumal": [
  J("نِسَاؤُكُمْ حَرْثٌ لَكُمْ",
    "الْكَلَامُ الثَّانِي — بَيَانٌ لِلْأَوَّلِ، فَهُمَا مُتَّصِلَانِ مَعْنًى.",
    "The second speech explains the first: that meaning-bond is what makes what stood between them a parenthesis.",
    "İkinci söz ilkini açıklar: aradakini ara cümle yapan bu mânâ bağıdır.")]})

# ----------- s4 — khilaf 1 (restored)
S.append({"id": "s4", "translation": {
 "en": "And some said: its point may be other than what was mentioned. (Restored from the source's paraphrase.)",
 "tr": "Bir topluluk da dedi ki: nüktesi, zikredilenin dışında da olabilir. (Kaynağın paraphrase'inden geri yazılmıştır.)"},
 "tokens": [
  tok("وَقَالَ","qala","verb",["itirad","hollow-verbs"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَالَ فِعْلٌ مَاضٍ.",
      "«and said» —",
      "«ve dedi» —",
      segments=[seg("وَ","wa","conj"), seg("قَالَ","qala","verb")]),
  tok("قَوْمٌ","qawm","noun",["itirad","fail"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "«a group» — the fa'il: the dissenters, unnamed.",
      "«bir topluluk» — fâil: adı verilmeyen muhâlifler.",
      punct=":"),
  tok("قَدْ","qad","part",["itirad","qad-harf"],
      "حَرْفُ تَقْلِيلٍ — مَعَ الْمُضَارِعِ.",
      "«may (sometimes)» — qad before a mudari lessens.",
      "«bazen» — muzâriden önce kad, azlık bildirir."),
  tok("تَكُونُ","kana","verb",["itirad","kana-wa-akhawatuha","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.",
      "«may be» — kana's mudari.",
      "«olur» — kâne'nin muzârisi."),
  tok("نُكْتَتُهُ","nukta","noun",["itirad","kana-wa-akhawatuha"],
      "اسْمُ تَكُونُ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«its point» — kana's ism, annexed to the parenthesis's pronoun.",
      "«nüktesi» — kâne'nin ismi, ara cümlenin zamirine muzâf.",
      segments=[seg("نُكْتَةُ","nukta","noun"), seg("هُ","pron-3ms","pron")]),
  tok("غَيْرَ","ghayr","noun",["itirad","kana-wa-akhawatuha"],
      "خَبَرُ تَكُونُ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«other than» — kana's khabar, a mudaf.",
      "«-den başka» — kâne'nin haberi, muzâf."),
  tok("مَا","ma-mawsula","pron",["itirad","ism-mawsul"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "«what» — the relative, mudaf ilayh in place.",
      "«şey» — ism-i mevsûl, mahallen muzâfun ileyh."),
  tok("ذُكِرَ","dhakara","verb",["itirad","naib-al-fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةٌ.",
      "«was mentioned» — the passive's sila; the daf' al-iham the definition shut out is let back in.",
      "«zikredildi» — meçhûlün sılası; tarifin dışarıda tuttuğu îhâm def'i içeri alınır.",
      punct=".")],
 "jumal": [
  J("قَدْ تَكُونُ نُكْتَتُهُ غَيْرَ مَا ذُكِرَ",
    "مَقُولُ الْقَوْلِ فِي مَحَلِّ نَصْبٍ.",
    "The quoted view, in the place of nasb as the object of قَالَ.",
    "Söylenen görüş; قَالَ'nin mef'ûlü olarak mahallen mansub.")]})

# ----------- s5 — khilaf 2 (restored)
S.append({"id": "s5", "translation": {
 "en": "And a group allowed the parenthesis at the END of a sentence that no sentence connected to it follows (restored),",
 "tr": "Bir topluluk da ara cümleyi, kendisine bağlı bir cümlenin izlemediği bir cümlenin SONUNDA câiz gördü (geri yazılmıştır),"},
 "tokens": [
  tok("وَجَوَّزَ","jawwaza","verb",["itirad","form-ii-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَجَوَّزَ فِعْلٌ مَاضٍ — مِنَ التَّفْعِيلِ.",
      "«and (a group) allowed» — Form II.",
      "«ve câiz gördü» — II. bâb.",
      segments=[seg("وَ","wa","conj"), seg("جَوَّزَ","jawwaza","verb")]),
  tok("قَوْمٌ","qawm","noun",["itirad","fail"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "«a group» —",
      "«bir topluluk» —"),
  tok("الِاعْتِرَاضَ","itirad","noun",["itirad","maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "«the parenthesis» — the object.",
      "«ara cümleyi» — mef'ûl."),
  tok("فِي","fi","part",["itirad","huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«at» —",
      "«-de» —"),
  tok("آخِرِ","akhir","noun",["itirad"],
      "مَجْرُورٌ بِفِي وَهُوَ مُضَافٌ.",
      "«the end of» — a mudaf.",
      "«sonunda» — muzâf."),
  tok("جُمْلَةٍ","jumla","noun",["itirad"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«a sentence» —",
      "«bir cümlenin» —"),
  tok("لَا","la-nafiya","part",["itirad"],
      "نَافِيَةٌ.",
      "«not» —",
      "«-mez» —"),
  tok("يَلِيهَا","waliya","verb",["itirad","mithal-verbs","naqis-verbs","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِفَةٌ لِجُمْلَةٍ. لَفِيفٌ مَفْرُوقٌ: وَلِيَ يَلِي.",
      "«follows it» — a lafif mafruq (وَلِيَ يَلِي: the waw dropped, the ya kept); the clause is a sifa of جُمْلَةٍ.",
      "«onu izler» — lefîf-i mefrûk (وَلِيَ يَلِي: vâv düşer, yâ kalır); cümle, جُمْلَةٍ'in sıfatı.",
      segments=[seg("يَلِي","waliya","verb"), seg("هَا","pron-3fs","pron")]),
  tok("جُمْلَةٌ","jumla","noun",["itirad","fail"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "«a sentence» — the fa'il of يَلِي.",
      "«bir cümle» — يَلِي'nin fâili."),
  tok("مُتَّصِلَةٌ","muttasil","noun",["itirad","ism-fail","naat-sifa"],
      "صِفَةٌ مَرْفُوعَةٌ.",
      "«connected» — its sifa.",
      "«bağlı» — sıfatı."),
  tok("بِهَا","bi","part",["itirad","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمُتَّصِلَةٍ.",
      "«to it» — hanging on مُتَّصِلَة.",
      "«ona» — مُتَّصِلَة'ye bağlı.",
      punct="،",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")])],
 "jumal": [
  J("لَا يَلِيهَا جُمْلَةٌ مُتَّصِلَةٌ بِهَا",
    "جُمْلَةٌ فِي مَحَلِّ جَرٍّ صِفَةٌ لِجُمْلَةٍ.",
    "A clause-sifa in the place of jarr: the sentence that ENDS the speech.",
    "Mahallen mecrur cümle-sıfat: sözü BİTİREN cümle.")]})

# ----------- s6 — its consequence (restored)
S.append({"id": "s6", "translation": {
 "en": "— so it covers part of takmil, and tadhyil. (Restored.)",
 "tr": "— böylece tekmîlin bir kısmını ve tezyîli kapsar. (Geri yazılmıştır.)"},
 "tokens": [
  tok("فَيَشْمَلُ","shamila","verb",["itirad"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَيَشْمَلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (الِاعْتِرَاضُ).",
      "«so it covers» — the fa of consequence; the hidden doer is the parenthesis on that wider reading.",
      "«böylece kapsar» — tefrî' fâsı; gizli fâil, o geniş okuyuştaki ara cümle.",
      segments=[seg("فَ","fa","conj"), seg("يَشْمَلُ","shamila","verb")]),
  tok("بَعْضَ","bad","noun",["itirad","maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«part of» — the object, a mudaf.",
      "«bir kısmını» — mef'ûl, muzâf."),
  tok("التَّكْمِيلِ","takmil","noun",["itirad","takmil-wa-tatmim"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«takmil» —",
      "«tekmîlin» —"),
  tok("وَالتَّذْيِيلَ","tadhyil","noun",["itirad","tadhyil","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَالتَّذْيِيلَ مَعْطُوفٌ عَلَى بَعْضَ مَنْصُوبٌ — لَا عَلَى التَّكْمِيلِ.",
      "«and tadhyil» — joined to بَعْضَ (nasb), not to التَّكْمِيلِ: ALL of tadhyil falls in, only PART of takmil.",
      "«ve tezyîli» — التَّكْمِيلِ'e değil بَعْضَ'ya atfedilmiş (nasb): tezyîlin TAMAMI, tekmîlin yalnız BİR KISMI girer.",
      punct=".",
      segments=[seg("وَ","wa","conj"), seg("التَّذْيِيلَ","tadhyil","noun")])],
 "jumal": [
  J("فَيَشْمَلُ بَعْضَ التَّكْمِيلِ وَالتَّذْيِيلَ",
    "جَوَابُ التَّفْرِيعِ — وَالْعَطْفُ عَلَى بَعْضَ يُقَرِّرُ الْحُدُودَ.",
    "The consequence; the atf onto بَعْضَ, not onto the mudaf ilayh, fixes exactly how much of each chapter is swallowed.",
    "Netice; atfın muzâfun ileyhe değil بَعْضَ'ya olması, her bâbdan ne kadarının yutulduğunu tam belirler.")]})

# ----------- s7 — khilaf 3 (restored)
S.append({"id": "s7", "translation": {
 "en": "And some of them allowed the parenthesis with something other than a sentence, so it covers some forms of tatmim and takmil. (Restored.)",
 "tr": "Kimileri de ara cümleyi cümle olmayanla câiz gördü; böylece tetmîm ve tekmîlin bazı sûretlerini kapsar. (Geri yazılmıştır.)"},
 "tokens": [
  tok("وَجَوَّزَ","jawwaza","verb",["itirad","form-ii-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَجَوَّزَ فِعْلٌ مَاضٍ.",
      "«and (some) allowed» —",
      "«ve câiz gördü» —",
      segments=[seg("وَ","wa","conj"), seg("جَوَّزَ","jawwaza","verb")]),
  tok("بَعْضُهُمُ","bad","noun",["itirad","fail"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَضُمَّتْ مِيمُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "«some of them» — the fa'il; the mim takes a damma before the next word's wasl.",
      "«kimileri» — fâil; mîm, sonraki kelimenin vaslından önce damme alır.",
      segments=[seg("بَعْضُ","bad","noun"), seg("هُمُ","pron-3mp","pron")]),
  tok("الِاعْتِرَاضَ","itirad","noun",["itirad","maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "«the parenthesis» —",
      "«ara cümleyi» —"),
  tok("بِغَيْرِ","ghayr","noun",["itirad","huruf-jarr"],
      "الْبَاءُ جَارَّةٌ، وَغَيْرِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "«with other than» —",
      "«olmayanla» —",
      segments=[seg("بِ","bi","part"), seg("غَيْرِ","ghayr","noun")]),
  tok("جُمْلَةٍ","jumla","noun",["itirad"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«a sentence» — a single word may then interrupt.",
      "«bir cümle» — o zaman tek kelime de araya girebilir.",
      punct="،"),
  tok("فَيَشْمَلُ","shamila","verb",["itirad"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَيَشْمَلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ.",
      "«so it covers» —",
      "«böylece kapsar» —",
      segments=[seg("فَ","fa","conj"), seg("يَشْمَلُ","shamila","verb")]),
  tok("بَعْضَ","bad","noun",["itirad","maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«some» —",
      "«bazı» —"),
  tok("صُوَرِ","sura","noun",["itirad"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — جَمْعُ صُورَةٍ.",
      "«forms of» — plural of صُورَة, itself a mudaf.",
      "«sûretlerini» — صُورَة'nin cem'i; kendisi de muzâf."),
  tok("التَّتْمِيمِ","tatmim","noun",["itirad","takmil-wa-tatmim"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«tatmim» —",
      "«tetmîm» —"),
  tok("وَالتَّكْمِيلِ","takmil","noun",["itirad","takmil-wa-tatmim","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَالتَّكْمِيلِ مَعْطُوفٌ عَلَى التَّتْمِيمِ مَجْرُورٌ.",
      "«and takmil» — this time joined to the mudaf ilayh: some FORMS of both.",
      "«ve tekmîlin» — bu kez muzâfun ileyhe atıf: her ikisinin bazı SÛRETLERİ.",
      punct=".",
      segments=[seg("وَ","wa","conj"), seg("التَّكْمِيلِ","takmil","noun")])],
 "jumal": [
  J("فَيَشْمَلُ بَعْضَ صُوَرِ التَّتْمِيمِ وَالتَّكْمِيلِ",
    "جَوَابُ التَّفْرِيعِ — تَتْمِيمٌ أَوْ تَكْمِيلٌ بِكَلِمَةٍ وَاحِدَةٍ يَصِيرُ اعْتِرَاضًا.",
    "The consequence: a one-word tatmim or takmil would become a parenthesis — which is why the musannif's definition says «a jumla».",
    "Netice: tek kelimelik bir tetmîm yahut tekmîl ara cümle olurdu — musannifin tarifinin «cümle» demesi bundandır.")]})

# ----------- s8 — itnab by other causes (restored lead-in)
S.append({"id": "s8", "translation": {
 "en": "And itnab may come by causes other than those mentioned — (restored lead-in) — for instance:",
 "tr": "Itnâb, zikredilenlerin dışında başka sebeplerle de olabilir — (geri yazılmış giriş) — meselâ:"},
 "tokens": [
  tok("وَقَدْ","qad","part",["asbab-al-itnab","qad-harf"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ.",
      "«and (sometimes)» —",
      "«ve bazen» —",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يَكُونُ","kana","verb",["asbab-al-itnab","kana-wa-akhawatuha"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.",
      "«may be» —",
      "«olur» —"),
  tok("الْإِطْنَابُ","itnab","noun",["asbab-al-itnab","kana-wa-akhawatuha"],
      "اسْمُ يَكُونُ مَرْفُوعٌ.",
      "«itnab» — kana's ism.",
      "«ıtnâb» — kâne'nin ismi."),
  tok("بِأَسْبَابٍ","sabab","noun",["asbab-al-itnab","huruf-jarr"],
      "الْبَاءُ جَارَّةٌ، وَأَسْبَابٍ مَجْرُورٌ — جَمْعُ سَبَبٍ، وَشِبْهُ الْجُمْلَةِ خَبَرُ يَكُونُ.",
      "«by causes» — the jarr phrase stands as kana's khabar.",
      "«sebeplerle» — câr-mecrûr, kâne'nin haberi.",
      segments=[seg("بِ","bi","part"), seg("أَسْبَابٍ","sabab","noun")]),
  tok("أُخْرَى","ukhra","noun",["asbab-al-itnab","mamnu-min-sarf","ism-maqsur-manqus"],
      "صِفَةٌ مَجْرُورَةٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ.",
      "«other» — a diptote (the feminine alif) on a maqsur alif: its jarr is an unseen fatha.",
      "«başka» — te'nîs elifiyle gayr-ı munsarif, maksûr elif üzerinde: cerri görünmez bir fetha."),
  tok("غَيْرِ","ghayr","noun",["asbab-al-itnab","naat-sifa"],
      "صِفَةٌ ثَانِيَةٌ مَجْرُورَةٌ وَهُوَ مُضَافٌ.",
      "«other than» — a second sifa, a mudaf.",
      "«dışında» — ikinci sıfat, muzâf."),
  tok("مَا","ma-mawsula","pron",["asbab-al-itnab","ism-mawsul"],
      "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "«what» —",
      "«şey» —"),
  tok("ذُكِرَ","dhakara","verb",["asbab-al-itnab","naib-al-fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةٌ.",
      "«was mentioned» — the eight causes just counted.",
      "«zikredildi» — az önce sayılan sekiz sebep.",
      punct="،")],
 "jumal": [
  J("وَقَدْ يَكُونُ الْإِطْنَابُ بِأَسْبَابٍ أُخْرَى",
    "جُمْلَةٌ اسْتِئْنَافِيَّةٌ — بَابُ الْأَسْبَابِ لَا يُغْلَقُ.",
    "A fresh start: the list of causes was never closed.",
    "Yeni bir başlangıç: sebepler listesi hiç kapanmamıştı.")]})

# ----------- s9 — 40:7
S.append({"id": "s9", "translation": {
 "en": "Those who bear the Throne and those around it glorify their Lord with praise and believe in Him (40:7) — «and believe in Him» is itnab: the nobility of faith shown, to make faith desired.",
 "tr": "Arşı taşıyanlar ve çevresindekiler Rablerini hamd ile tesbih ederler ve O'na iman ederler (40:7) — «O'na iman ederler» ıtnâbdır: imana rağbet için imanın şerefi gösterilir."},
 "tokens": [
  tok("الَّذِينَ","alladhina","pron",["asbab-al-itnab","ism-mawsul"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "«those who» — the relative as mubtada.",
      "«onlar ki» — mübtedâ olan ism-i mevsûl."),
  tok("يَحْمِلُونَ","hamala","verb",["asbab-al-itnab","afal-khamsa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ صِلَةٌ.",
      "«bear» — the sila.",
      "«taşırlar» — sıla."),
  tok("الْعَرْشَ","arsh","noun",["asbab-al-itnab","maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "«the Throne» —",
      "«Arşı» —"),
  tok("وَمَنْ","man-mawsula","pron",["asbab-al-itnab","ism-mawsul","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَمَنْ اسْمٌ مَوْصُولٌ مَعْطُوفٌ عَلَى الَّذِينَ فِي مَحَلِّ رَفْعٍ.",
      "«and those who» — joined to الَّذِينَ in place.",
      "«ve onlar ki» — الَّذِينَ'ye mahallen atıf.",
      segments=[seg("وَ","wa","conj"), seg("مَنْ","man-mawsula","pron")]),
  tok("حَوْلَهُ","hawl","noun",["asbab-al-itnab","maful-fih"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ مُتَعَلِّقٌ بِصِلَةٍ مَحْذُوفَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«around it» — a zarf standing for the unspoken sila («are around it»).",
      "«çevresinde» — hazfedilmiş sılanın yerini tutan zarf.",
      segments=[seg("حَوْلَ","hawl","noun"), seg("هُ","pron-3ms","pron")]),
  tok("يُسَبِّحُونَ","sabbaha","verb",["asbab-al-itnab","form-ii-verbs","afal-khamsa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.",
      "«glorify» — the khabar clause, at last.",
      "«tesbih ederler» — nihayet haber cümlesi."),
  tok("بِحَمْدِ","hamd","noun",["asbab-al-itnab","hal"],
      "الْبَاءُ لِلْمُلَابَسَةِ، وَحَمْدِ مَجْرُورٌ وَهُوَ مُضَافٌ — وَشِبْهُ الْجُمْلَةِ حَالٌ: مُلْتَبِسِينَ بِحَمْدِهِ.",
      "«with the praise of» — a ba of accompaniment; the phrase is a hal (glorifying WHILE praising).",
      "«hamdiyle» — mülâbese bâsı; câr-mecrûr hâldir (hamd ederek tesbih).",
      segments=[seg("بِ","bi","part"), seg("حَمْدِ","hamd","noun")]),
  tok("رَبِّهِمْ","rabb","noun",["asbab-al-itnab","idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«their Lord» —",
      "«Rablerinin» —",
      segments=[seg("رَبِّ","rabb","noun"), seg("هِمْ","pron-3mp","pron")]),
  tok("وَيُؤْمِنُونَ","amana","verb",["asbab-al-itnab","form-iv-verbs","afal-khamsa","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَيُؤْمِنُونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَهُوَ الْإِطْنَابُ.",
      "«and believe» — the itnab: the angels' faith went without saying; saying it shows faith's rank.",
      "«ve iman ederler» — ıtnâb: meleklerin imanı söylenmese de bilinirdi; söylenmesi imanın rütbesini gösterir.",
      segments=[seg("وَ","wa","conj"), seg("يُؤْمِنُونَ","amana","verb")]),
  tok("بِهِ","bi","part",["asbab-al-itnab","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِيُؤْمِنُونَ.",
      "«in Him» —",
      "«O'na» —",
      punct=".",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")])],
 "jumal": [
  J("يَحْمِلُونَ الْعَرْشَ",
    "صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
    "The sila.",
    "Sıla."),
  J("يُسَبِّحُونَ بِحَمْدِ رَبِّهِمْ",
    "خَبَرُ الْمُبْتَدَأِ فِي مَحَلِّ رَفْعٍ.",
    "The khabar, in the place of raf'.",
    "Mahallen merfû haber."),
  J("وَيُؤْمِنُونَ بِهِ",
    "مَعْطُوفَةٌ عَلَى الْخَبَرِ — وَهِيَ مَوْضِعُ الْإِطْنَابِ: إِظْهَارُ شَرَفِ الْإِيمَانِ تَرْغِيبًا فِيهِ.",
    "Joined to the khabar; the seat of the itnab — the nobility of faith shown, to make it desired.",
    "Habere atıf; ıtnâbın yeri — imana rağbet için şerefinin gösterilmesi.")]})

# ----------- s10 — the relative ijaz and itnab (matn), first half
S.append({"id": "s10", "translation": {
 "en": "A speech may be described as ijaz and as itnab by the reckoning of the MANY-ness and the FEW-ness of its letters",
 "tr": "Söz, harflerinin ÇOKLUĞU ve AZLIĞI itibariyle de îcâz ve ıtnâb ile vasfedilebilir"},
 "tokens": [
  tok("وَقَدْ","qad","part",["ijaz-itnab-nisbi","qad-harf"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَقْلِيلٍ.",
      "«and (sometimes)» —",
      "«ve bazen» —",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يُوصَفُ","wasafa","verb",["ijaz-itnab-nisbi","naib-al-fail","mithal-verbs"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — مِثَالٌ وَاوِيٌّ، وَالْوَاوُ تَثْبُتُ فِي الْمَجْهُولِ.",
      "«is described» — the passive of a mithal verb: the waw that the active mudari drops (يَصِفُ) stands here (يُوصَفُ).",
      "«vasfedilir» — misâl fiilin meçhûlü: ma'lûm muzâride düşen vâv (يَصِفُ) burada durur (يُوصَفُ)."),
  tok("الْكَلَامُ","kalam","noun",["ijaz-itnab-nisbi","naib-al-fail"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ.",
      "«a speech» — the deputy doer.",
      "«söz» — nâib-i fâil."),
  tok("بِالْإِيجَازِ","ijaz","noun",["ijaz-itnab-nisbi","huruf-jarr","ijaz-itnab-musawat"],
      "الْبَاءُ جَارَّةٌ، وَالْإِيجَازِ مَجْرُورٌ.",
      "«as ijaz» —",
      "«îcâz ile» —",
      segments=[seg("بِ","bi","part"), seg("الْإِيجَازِ","ijaz","noun")]),
  tok("وَالْإِطْنَابِ","itnab","noun",["ijaz-itnab-nisbi","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَالْإِطْنَابِ مَعْطُوفٌ مَجْرُورٌ.",
      "«and as itnab» —",
      "«ve ıtnâb ile» —",
      segments=[seg("وَ","wa","conj"), seg("الْإِطْنَابِ","itnab","noun")]),
  tok("بِاعْتِبَارِ","itibar","noun",["ijaz-itnab-nisbi","huruf-jarr"],
      "الْبَاءُ جَارَّةٌ، وَاعْتِبَارِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "«by the reckoning of» — the second ba: the yardstick.",
      "«itibariyle» — ikinci bâ: ölçü.",
      segments=[seg("بِ","bi","part"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("كَثْرَةِ","kathra","noun",["ijaz-itnab-nisbi"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "«the many-ness of» —",
      "«çokluğu» —"),
  tok("حُرُوفِهِ","harf","noun",["ijaz-itnab-nisbi","idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«its letters» — letters COUNTED: this ijaz is arithmetic.",
      "«harflerinin» — SAYILAN harfler: bu îcâz aritmetiktir.",
      segments=[seg("حُرُوفِ","harf","noun"), seg("هِ","pron-3ms","pron")]),
  tok("وَقِلَّتِهَا","qilla","noun",["ijaz-itnab-nisbi","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَقِلَّتِ مَعْطُوفٌ عَلَى كَثْرَةِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«and their few-ness» — joined to كَثْرَةِ.",
      "«ve azlığı» — كَثْرَةِ'ye atıf.",
      segments=[seg("وَ","wa","conj"), seg("قِلَّتِ","qilla","noun"), seg("هَا","pron-3fs","pron")])],
 "jumal": [
  J("وَقَدْ يُوصَفُ الْكَلَامُ بِالْإِيجَازِ وَالْإِطْنَابِ",
    "جُمْلَةٌ اسْتِئْنَافِيَّةٌ — بَابٌ ثَانٍ لِلْإِيجَازِ وَالْإِطْنَابِ: بِالنِّسْبَةِ لَا بِالْمُتَعَارَفِ.",
    "A second doorway to ijaz and itnab: not against the customary measure, but against ANOTHER speech.",
    "Îcâz ve ıtnâba ikinci kapı: müteârefe göre değil, BAŞKA bir söze göre.")]})

# ----------- s11 — second half
S.append({"id": "s11", "translation": {
 "en": "in relation to another speech equal to it in the root of its meaning.",
 "tr": "— mânâsının aslında kendisine denk başka bir söze nispetle."},
 "tokens": [
  tok("بِالنِّسْبَةِ","nisba","noun",["ijaz-itnab-nisbi","huruf-jarr"],
      "الْبَاءُ جَارَّةٌ، وَالنِّسْبَةِ مَجْرُورٌ.",
      "«in relation» —",
      "«nispetle» —",
      segments=[seg("بِ","bi","part"), seg("النِّسْبَةِ","nisba","noun")]),
  tok("إِلَى","ila","part",["ijaz-itnab-nisbi","huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«to» —",
      "«-e» —"),
  tok("كَلَامٍ","kalam","noun",["ijaz-itnab-nisbi"],
      "مَجْرُورٌ بِإِلَى.",
      "«a speech» —",
      "«bir söze» —"),
  tok("آخَرَ","akhar","noun",["ijaz-itnab-nisbi","mamnu-min-sarf","naat-sifa"],
      "صِفَةٌ مَجْرُورَةٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — عَلَى وَزْنِ أَفْعَلَ.",
      "«another» — a diptote on the أَفْعَل scale: its jarr wears a fatha and no tanwin.",
      "«başka» — أَفْعَل vezninde gayr-ı munsarif: cerri fetha, tenvinsiz."),
  tok("مُسَاوٍ","musawin","noun",["ijaz-itnab-nisbi","ism-maqsur-manqus","ism-fail","naat-sifa"],
      "صِفَةٌ ثَانِيَةٌ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — مَنْقُوصٌ.",
      "«equal» — a manqus: its ya has dropped and its kasra is unseen.",
      "«denk» — manqûs: yâsı düşmüş, kesresi görünmez."),
  tok("لَهُ","li","part",["ijaz-itnab-nisbi","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمُسَاوٍ.",
      "«to it» —",
      "«ona» —",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("فِي","fi","part",["ijaz-itnab-nisbi","huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«in» —",
      "«-de» —"),
  tok("أَصْلِ","asl","noun",["ijaz-itnab-nisbi"],
      "مَجْرُورٌ بِفِي وَهُوَ مُضَافٌ.",
      "«the root of» — equal in the ROOT of the meaning, not in every nuance.",
      "«aslında» — her incelikte değil, mânânın ASLINDA denk."),
  tok("الْمَعْنَى","mana","noun",["ijaz-itnab-nisbi","ism-maqsur-manqus"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.",
      "«the meaning» — a maqsur, its jarr unseen.",
      "«mânânın» — maksûr, cerri görünmez.",
      punct=".")],
 "jumal": [
  J("مُسَاوٍ لَهُ فِي أَصْلِ الْمَعْنَى",
    "الصِّفَةُ الثَّانِيَةُ وَمَا تَعَلَّقَ بِهَا — شَرْطُ الْمُقَارَنَةِ.",
    "The condition of the comparison: two speeches can be weighed only when their core meaning is one.",
    "Karşılaştırmanın şartı: iki söz ancak öz mânâları bir olunca tartılır.")]})

# ----------- s12 — Abu Tammam, first hemistich (ijaz)
S.append({"id": "s12", "translation": {
 "en": "He turns from the world whenever eminence appears — (Abu Tammam) — the first hemistich: ijaz beside the next bayt.",
 "tr": "Ululuk belirince dünyadan yüz çevirir — (Ebû Temmâm) — ilk mısra: sonraki beyte göre îcâz."},
 "tokens": [
  tok("يَصُدُّ","sadda","verb",["ijaz-itnab-nisbi","doubled-verbs","thulathi-mujarrad-babs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (الْمَمْدُوحُ) — مُضَاعَفٌ: صَدَّ يَصُدُّ.",
      "«he turns away» — a Form I geminate (صَدَّ يَصُدُّ); the hidden doer is the praised man.",
      "«yüz çevirir» — I. bâbdan muzâaf (صَدَّ يَصُدُّ); gizli fâil, medhedilen kişi."),
  tok("عَنِ","an","part",["ijaz-itnab-nisbi","huruf-jarr"],
      "حَرْفُ جَرٍّ — كُسِرَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "«from» — its nun takes a kasra before the article's wasl.",
      "«-den» — nûnu, harf-i tarifin vaslından önce kesre alır."),
  tok("الدُّنْيَا","dunya","noun",["ijaz-itnab-nisbi","ism-maqsur-manqus"],
      "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.",
      "«the world» —",
      "«dünyadan» —"),
  tok("إِذَا","idha","part",["ijaz-itnab-nisbi","idha-shartiyya","maful-fih"],
      "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مُتَعَلِّقٌ بِيَصُدُّ.",
      "«whenever» — the conditional zarf, hanging on يَصُدُّ (its own answer, fronted).",
      "«-ince» — şart mânâlı zarf, يَصُدُّ'ya bağlı (cevabı öne alınmış)."),
  tok("عَنَّ","anna-verb","verb",["ijaz-itnab-nisbi","doubled-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا — مُضَاعَفٌ: عَنَّ يَعِنُّ.",
      "«appears» — a geminate mazi (عَنَّ يَعِنُّ, «to present itself»); the clause is إِذَا's mudaf ilayh.",
      "«belirir» — muzâaf mâzî (عَنَّ يَعِنُّ, «ortaya çıkmak»); cümle إِذَا'nın muzâfun ileyhi."),
  tok("سُودَدٌ","sudad","noun",["ijaz-itnab-nisbi","fail"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "«eminence» — the fa'il: lordship, high standing.",
      "«ululuk» — fâil: efendilik, yüksek mevki.")],
 "jumal": [
  J("يَصُدُّ عَنِ الدُّنْيَا إِذَا عَنَّ سُودَدٌ",
    "الْمِصْرَاعُ الْأَوَّلُ — فِيهِ الْإِيجَازُ بِالنِّسْبَةِ إِلَى بَيْتِ عَبْدِ الصَّمَدِ.",
    "The first hemistich: measured against 'Abd al-Samad's whole bayt it is the ijaz — the same thought in fewer letters.",
    "İlk mısra: Abdüssamed'in bütün beytine göre îcâzdır — aynı düşünce, daha az harfle.")]})

# ----------- s13 — second hemistich
S.append({"id": "s13", "translation": {
 "en": "— even were it to come forth in the guise of a full-breasted virgin.",
 "tr": "— dünya, göğsü kabarmış bir bâkire kılığında ortaya çıksa bile."},
 "tokens": [
  tok("وَلَوْ","law","part",["ijaz-itnab-nisbi","hal"],
      "الْوَاوُ حَالِيَّةٌ، وَلَوْ وَصْلِيَّةٌ — لَا جَوَابَ لَهَا، وَجُمْلَتُهَا حَالٌ.",
      "«even if» — the waw of hal with لَوْ of concession: no answer follows, the clause is a hal.",
      "«olsa bile» — hâl vâvı ile vasliyye لَوْ: cevabı yoktur, cümlesi hâldir.",
      segments=[seg("وَ","wa","conj"), seg("لَوْ","law","part")]),
  tok("بَرَزَتْ","baraza","verb",["ijaz-itnab-nisbi","thulathi-mujarrad-babs"],
      "فِعْلٌ مَاضٍ وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ (الدُّنْيَا).",
      "«it came forth» — feminine: the world is the doer.",
      "«ortaya çıktı» — müennes: fâil dünyadır."),
  tok("فِي","fi","part",["ijaz-itnab-nisbi","huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«in» —",
      "«-de» —"),
  tok("زِيِّ","ziyy","noun",["ijaz-itnab-nisbi"],
      "مَجْرُورٌ بِفِي وَهُوَ مُضَافٌ.",
      "«the guise of» —",
      "«kılığında» —"),
  tok("عَذْرَاءَ","adhra","noun",["ijaz-itnab-nisbi","mamnu-min-sarf","ism-mamdud"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ.",
      "«a virgin» — a mamdud on the feminine hamza, a diptote: jarr as fatha.",
      "«bir bâkire» — te'nîs hemzeli memdûd, gayr-ı munsarif: cerri fetha."),
  tok("نَاهِدِ","nahid","noun",["ijaz-itnab-nisbi","ism-fail","naat-sifa"],
      "صِفَةٌ مَجْرُورَةٌ — وَحُذِفَ تَنْوِينُهَا لِلْقَافِيَةِ.",
      "«full-breasted» — a sifa of عَذْرَاءَ; its tanwin dropped for the rhyme, as the source prints it.",
      "«göğsü kabarmış» — عَذْرَاءَ'nin sıfatı; kafiye için tenvini düşmüş, kaynağın bastığı gibi.",
      punct=".")],
 "jumal": [
  J("وَلَوْ بَرَزَتْ فِي زِيِّ عَذْرَاءَ نَاهِدِ",
    "جُمْلَةُ لَوِ الْوَصْلِيَّةِ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "The concessive clause, a hal: he turns away even at the world's most tempting.",
    "Vasliyye cümlesi, hâl: dünyanın en cazip hâlinde bile yüz çevirir.")]})

# ----------- s14 — 'Abd al-Samad, first hemistich (itnab)
S.append({"id": "s14", "translation": {
 "en": "And I am no gazer toward the side of wealth — ('Abd al-Samad) — the bayt that says the same in more letters: itnab beside the first hemistich.",
 "tr": "Ben zenginlik tarafına bakan biri değilim — (Abdüssamed) — aynı şeyi daha çok harfle söyleyen beyit: ilk mısraa göre ıtnâb."},
 "tokens": [
  tok("وَلَسْتُ","laysa","verb",["ijaz-itnab-nisbi","kana-wa-akhawatuha"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهَا.",
      "«and I am not» — laysa with the speaker's ta as its ism.",
      "«ve ben değilim» — leyse; mütekellim tâsı ismidir.",
      segments=[seg("وَ","wa","conj"), seg("لَسْتُ","laysa","verb")]),
  tok("بِنَظَّارٍ","nazzar","noun",["ijaz-itnab-nisbi","sighat-mubalagha","huruf-jarr"],
      "الْبَاءُ زَائِدَةٌ فِي خَبَرِ لَيْسَ، وَنَظَّارٍ خَبَرُهَا مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا — فَعَّالٌ لِلْمُبَالَغَةِ.",
      "«a gazer» — the zaida ba on laysa's khabar: jarr on the surface, nasb in place; فَعَّال intensifies.",
      "«bakan biri» — leyse'nin haberinde zâid bâ: lafzan mecrur, mahallen mansub; فَعَّال mübalağa.",
      segments=[seg("بِ","bi","part"), seg("نَظَّارٍ","nazzar","noun")]),
  tok("إِلَى","ila","part",["ijaz-itnab-nisbi","huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِنَظَّارٍ.",
      "«toward» —",
      "«-e» —"),
  tok("جَانِبِ","janib","noun",["ijaz-itnab-nisbi"],
      "مَجْرُورٌ بِإِلَى وَهُوَ مُضَافٌ.",
      "«the side of» —",
      "«tarafına» —"),
  tok("الْغِنَى","ghina","noun",["ijaz-itnab-nisbi","ism-maqsur-manqus"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.",
      "«wealth» — a maqsur.",
      "«zenginliğin» — maksûr.")],
 "jumal": [
  J("وَلَسْتُ بِنَظَّارٍ إِلَى جَانِبِ الْغِنَى",
    "لَيْسَ وَاسْمُهَا وَخَبَرُهَا — الْبَيْتُ كُلُّهُ يُقَابِلُ مِصْرَاعًا وَاحِدًا.",
    "Laysa, its ism and khabar; this whole bayt answers a single hemistich of Abu Tammam's — hence the itnab.",
    "Leyse, ismi ve haberi; bu bütün beyit, Ebû Temmâm'ın tek mısraına karşılık gelir — ıtnâb bundandır.")]})

# ----------- s15 — second hemistich
S.append({"id": "s15", "translation": {
 "en": "when eminence is on the side of poverty.",
 "tr": "— yücelik fakirlik tarafında olduğu zaman."},
 "tokens": [
  tok("إِذَا","idha","part",["ijaz-itnab-nisbi","idha-shartiyya","maful-fih"],
      "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.",
      "«when» —",
      "«-dığı zaman» —"),
  tok("كَانَتِ","kana","verb",["ijaz-itnab-nisbi","kana-wa-akhawatuha","hollow-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجُمْلَةُ مُضَافٌ إِلَيْهَا.",
      "«is» — kana with the feminine ta, which takes a kasra before the article's wasl.",
      "«oldu» — te'nîs tâlı kâne; tâ, harf-i tarifin vaslından önce kesre alır."),
  tok("الْعَلْيَاءُ","alya","noun",["ijaz-itnab-nisbi","ism-mamdud","kana-wa-akhawatuha"],
      "اسْمُ كَانَ مَرْفُوعٌ — مَمْدُودٌ.",
      "«eminence» — kana's ism, a mamdud.",
      "«yücelik» — kâne'nin ismi, memdûd."),
  tok("فِي","fi","part",["ijaz-itnab-nisbi","huruf-jarr"],
      "حَرْفُ جَرٍّ، وَشِبْهُ الْجُمْلَةِ خَبَرُ كَانَ.",
      "«on» — the phrase is kana's khabar.",
      "«-de» — câr-mecrûr kâne'nin haberi."),
  tok("جَانِبِ","janib","noun",["ijaz-itnab-nisbi"],
      "مَجْرُورٌ بِفِي وَهُوَ مُضَافٌ.",
      "«the side of» —",
      "«tarafında» —"),
  tok("الْفَقْرِ","faqr","noun",["ijaz-itnab-nisbi"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«poverty» —",
      "«fakirliğin» —",
      punct=".")],
 "jumal": [
  J("إِذَا كَانَتِ الْعَلْيَاءُ فِي جَانِبِ الْفَقْرِ",
    "جُمْلَةُ الشَّرْطِ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا — وَالْجَوَابُ مَا تَقَدَّمَ.",
    "The condition, annexed to إِذَا; its answer is the whole preceding line.",
    "Şart cümlesi, إِذَا'ya muzâf; cevabı önceki mısraın tamamıdır.")]})

# ----------- s16 — 21:23
S.append({"id": "s16", "translation": {
 "en": "He is not questioned about what He does, while they are questioned (21:23) — ijaz beside al-Hamasi's bayt; «and near to it», says the musannif, for a Qur'anic aya and a verse are not weighed on one scale.",
 "tr": "O yaptığından sorulmaz, onlar ise sorulurlar (21:23) — Hamâsî'nin beytine göre îcâz; musannif «ona yakındır» der, zira âyet ile şiir bir terazide tartılmaz."},
 "tokens": [
  tok("لَا","la-nafiya","part",["ijaz-itnab-nisbi"],
      "نَافِيَةٌ.",
      "«not» —",
      "«-maz» —"),
  tok("يُسْأَلُ","saala","verb",["ijaz-itnab-nisbi","naib-al-fail"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ (اللهُ).",
      "«He is questioned» — the passive; its deputy doer is hidden: He.",
      "«sorulur» — meçhûl; nâib-i fâil gizli: O."),
  tok("عَمَّا","an","part",["ijaz-itnab-nisbi","anwa-ma","ism-mawsul"],
      "عَنْ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — أُدْغِمَتِ النُّونُ فِي الْمِيمِ.",
      "«about what» — عَنْ fused with the relative مَا; the nun melts into the mim.",
      "«hakkında» — عَنْ ile mevsûl مَا kaynaşmış; nûn mîme idğam edilmiş.",
      segments=[seg("عَنْ","an","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يَفْعَلُ","faala","verb",["ijaz-itnab-nisbi"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ صِلَةٌ، وَالْعَائِدُ مَحْذُوفٌ: يَفْعَلُهُ.",
      "«He does» — the sila with its returning pronoun unspoken.",
      "«yapar» — âidi söylenmemiş sıla."),
  tok("وَهُمْ","hum","pron",["ijaz-itnab-nisbi","hal","mubtada-khabar"],
      "الْوَاوُ حَالِيَّةٌ، وَهُمْ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "«while they» — the waw of hal opens a nominal clause: the creatures.",
      "«onlar ise» — hâl vâvı isim cümlesi açar: yaratılmışlar.",
      segments=[seg("وَ","wa","conj"), seg("هُمْ","hum","pron")]),
  tok("يُسْأَلُونَ","saala","verb",["ijaz-itnab-nisbi","naib-al-fail","afal-khamsa"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ نَائِبُ فَاعِلٍ — وَالْجُمْلَةُ خَبَرٌ.",
      "«are questioned» — the same passive on the group's waw; the clause is the khabar.",
      "«sorulurlar» — aynı meçhûl, cemi vâvıyla; cümle haber.",
      punct=".")],
 "jumal": [
  J("لَا يُسْأَلُ عَمَّا يَفْعَلُ",
    "جُمْلَةٌ فِعْلِيَّةٌ — الْكَلَامُ الْمُوجَزُ.",
    "The concise speech: one negation, one relative, and the whole of divine sovereignty.",
    "Mûcez söz: bir nefiy, bir mevsûl, ve ilâhî hâkimiyetin tamamı."),
  J("وَهُمْ يُسْأَلُونَ",
    "جُمْلَةٌ اسْمِيَّةٌ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "A nominal clause as hal, in the place of nasb.",
    "Mahallen mansub hâl olan isim cümlesi.")]})

# ----------- s17 — al-Hamasi, first hemistich
S.append({"id": "s17", "translation": {
 "en": "And we reject, if we will, the people's word — (al-Hamasi) — the bayt beside which the aya is ijaz: the same balance of power, spelled out at length.",
 "tr": "Dilersek insanların sözünü reddederiz — (Hamâsî) — âyetin ona göre îcâz olduğu beyit: aynı güç dengesi, uzun uzun söylenmiş."},
 "tokens": [
  tok("وَنُنْكِرُ","ankara","verb",["ijaz-itnab-nisbi","form-iv-verbs"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَنُنْكِرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.",
      "«and we reject» — Form IV, the speakers' cell.",
      "«ve reddederiz» — IV. bâb, mütekellim hücresi.",
      segments=[seg("وَ","wa","conj"), seg("نُنْكِرُ","ankara","verb")]),
  tok("إِنْ","in-shart","part",["ijaz-itnab-nisbi","in-shartiyya"],
      "حَرْفُ شَرْطٍ جَازِمٌ.",
      "«if» — the conditional, jazim.",
      "«-se» — cezmeden şart edatı."),
  tok("شِئْنَا","shaa","verb",["ijaz-itnab-nisbi","hollow-verbs","in-shartiyya"],
      "فِعْلُ الشَّرْطِ مَاضٍ فِي مَحَلِّ جَزْمٍ، وَنَا فَاعِلٌ — وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.",
      "«we will» — a hollow mazi as the shart (كَسْرُ الْفَاءِ: شِئْنَا), its answer unspoken — the line before it already said it.",
      "«dilersek» — şart fiili olan ecvef mâzî (شِئْنَا), cevabı söylenmemiş — önceki söz zaten söyledi.",
      segments=[seg("شِئْ","shaa","verb"), seg("نَا","pron-1p","pron")]),
  tok("عَلَى","ala","part",["ijaz-itnab-nisbi","huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِنُنْكِرُ.",
      "«against» —",
      "«-e karşı» —"),
  tok("النَّاسِ","nas","noun",["ijaz-itnab-nisbi"],
      "مَجْرُورٌ بِعَلَى.",
      "«the people» —",
      "«insanlara» —"),
  tok("قَوْلَهُمْ","qawl","noun",["ijaz-itnab-nisbi","maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«their word» — the object, delayed past the jarr phrase.",
      "«sözlerini» — câr-mecrûrdan sonraya bırakılmış mef'ûl.",
      segments=[seg("قَوْلَ","qawl","noun"), seg("هُمْ","pron-3mp","pron")])],
 "jumal": [
  J("إِنْ شِئْنَا",
    "جُمْلَةُ الشَّرْطِ اعْتِرَاضٌ بَيْنَ الْفِعْلِ وَمَعْمُولِهِ — وَجَوَابُهَا مَحْذُوفٌ.",
    "The condition breaks in between the verb and its object — a small parenthesis inside the very bayt that teaches itnab.",
    "Şart, fiil ile mef'ûlünün arasına girer — ıtnâbı öğreten beytin içinde küçük bir ara cümle.")]})

# ----------- s18 — second hemistich
S.append({"id": "s18", "translation": {
 "en": "— and they do not reject the word when we speak.",
 "tr": "— biz söylediğimiz zaman ise onlar sözü reddedemezler."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["ijaz-itnab-nisbi"],
      "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.",
      "«and not» —",
      "«ve -mez» —",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يُنْكِرُونَ","ankara","verb",["ijaz-itnab-nisbi","form-iv-verbs","afal-khamsa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ.",
      "«they reject» — the group's cell of the same verb: the bayt's symmetry mirrors the aya's.",
      "«reddederler» — aynı fiilin cemi hücresi: beytin simetrisi âyetinkini yansıtır."),
  tok("الْقَوْلَ","qawl","noun",["ijaz-itnab-nisbi","maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "«the word» —",
      "«sözü» —"),
  tok("حِينَ","hin","noun",["ijaz-itnab-nisbi","maful-fih"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.",
      "«when» — a time-zarf annexed to the clause after it.",
      "«-dığı zaman» — ardındaki cümleye muzâf zaman zarfı."),
  tok("نَقُولُ","qala","verb",["ijaz-itnab-nisbi","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهَا.",
      "«we speak» — the clause in jarr as حِينَ's mudaf ilayh.",
      "«söyleriz» — حِينَ'nin muzâfun ileyhi olarak mahallen mecrur cümle.",
      punct=".")],
 "jumal": [
  J("وَلَا يُنْكِرُونَ الْقَوْلَ حِينَ نَقُولُ",
    "مَعْطُوفَةٌ عَلَى الْأُولَى — تَمَامُ الْبَيْتِ الَّذِي تُقَابِلُهُ الْآيَةُ بِالْإِيجَازِ.",
    "Joined to the first hemistich; the whole bayt is what the aya says in six words.",
    "İlk mısraa atıf; bütün beyit, âyetin altı kelimede söylediğidir.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "amara-v": g("أَمَرَ", "أ م ر", "verb", "to command", "emretmek", 2, form="I"),
 "ahabba": g("أَحَبَّ", "ح ب ب", "verb", "to love", "sevmek", 2, form="IV"),
 "tawwab": g("تَوَّاب", "ت و ب", "noun", "ever-repentant (sighat mubalagha فَعَّال)", "tevvâb, çok tevbe eden (فَعَّال mübalağa sîgası)", 4),
 "mutatahhir": g("مُتَطَهِّر", "ط ه ر", "noun", "one who purifies himself (ism fa'il of تَطَهَّرَ)", "temizlenen (تَطَهَّرَ'nin ism-i fâili)", 4),
 "harth": g("حَرْث", "ح ر ث", "noun", "tilth, tillage", "ekin yeri, tarla", 3),
 "jawwaza": g("جَوَّزَ", "ج و ز", "verb", "to allow, hold permissible", "câiz görmek", 4, form="II"),
 "shamila": g("شَمِلَ", "ش م ل", "verb", "to include, cover", "şâmil olmak, kapsamak", 4, form="I"),
 "tadhyil": g("تَذْيِيل", "ذ ي ل", "noun", "tadhyil: the appended sentence (balagha)", "tezyîl: ekleme cümle (belâgat)", 6),
 "sura": g("صُورَة", "ص و ر", "noun", "form, shape", "sûret, şekil", 2, plural="صُوَر"),
 "sabbaha": g("سَبَّحَ", "س ب ح", "verb", "to glorify", "tesbih etmek", 2, form="II"),
 "hamd": g("حَمْد", "ح م د", "noun", "praise", "hamd, övgü", 1),
 "qilla": g("قِلَّة", "ق ل ل", "noun", "fewness, scarcity (masdar)", "kıllet, azlık (masdar)", 3),
 "nisba": g("نِسْبَة", "ن س ب", "noun", "relation, ratio", "nispet", 3),
 "sadda": g("صَدَّ", "ص د د", "verb", "to turn away (from)", "yüz çevirmek", 3, form="I"),
 "anna-verb": g("عَنَّ", "ع ن ن", "verb", "to appear, present itself", "belirmek, zuhur etmek", 5, form="I"),
 "sudad": g("سُودَد", "س و د", "noun", "lordship, eminence", "efendilik, ululuk", 5),
 "baraza": g("بَرَزَ", "ب ر ز", "verb", "to come forth, appear", "ortaya çıkmak, belirmek", 3, form="I"),
 "ziyy": g("زِيّ", "ز ي ي", "noun", "dress, guise", "kılık, kıyafet", 4),
 "adhra": g("عَذْرَاء", "ع ذ ر", "noun", "virgin (mamdud, diptote)", "bâkire (memdûd, gayr-ı munsarif)", 4),
 "nahid": g("نَاهِد", "ن ه د", "noun", "full-breasted (a girl come of age)", "göğsü kabarmış (yetişkin genç kız)", 5),
 "nazzar": g("نَظَّار", "ن ظ ر", "noun", "one who gazes much (sighat mubalagha)", "çok bakan (mübalağa sîgası)", 4),
 "ghina": g("غِنًى", "غ ن ي", "noun", "wealth (maqsur)", "zenginlik (maksûr)", 3),
 "alya": g("عَلْيَاء", "ع ل و", "noun", "eminence, high standing (mamdud)", "yücelik, ulviyet (memdûd)", 5),
 "faqr": g("فَقْر", "ف ق ر", "noun", "poverty", "fakirlik", 2),
 "pron-3fp": {"lemma": "ـهُنَّ", "pos": "pron", "gloss": {"en": "them / their (f. pl.)", "tr": "onlar / onları (diş. çoğul)"}, "level": 2},
 "hayth": copy_gloss("mukhtasar-al-manar", "hayth"),
 "nisa": copy_gloss("bad-al-amali", "nisa"),
 "akhir": copy_gloss("aqaid-ahl-al-sunna", "akhir"),
 "waliya": copy_gloss("wasiyyat-abi-hanifa-samti", "waliya"),
 "ukhra": copy_gloss("kitab-al-sulh", "ukhra"),
 "hamala": copy_gloss("mukhtasar-al-manar", "hamala"),
 "arsh": copy_gloss("bad-al-amali", "arsh"),
 "amana": copy_gloss("yunus-wa-al-hut", "amana"),
 "kathra": copy_gloss("mukhtasar-al-manar", "kathra"),
 "akhar": copy_gloss("kitab-al-sulh", "akhar"),
 "janib": copy_gloss("wasiyyat-abi-hanifa-samti", "janib"),
 "nas": copy_gloss("aqaid-ahl-al-sunna", "nas"),
 "ankara": copy_gloss("aqaid-ahl-al-sunna", "ankara"),
 "qawl": copy_gloss("wasiyyat-abi-hanifa-samti", "qawl"),
 "hin": copy_gloss("wasiyyat-abi-hanifa-samti", "hin"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/45.json").write_text(
    json.dumps({"chapter": 45, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 45 for c in man["chapters"]):
    man["chapters"].append({"n": 45, "title": TITLE45})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.45.0"
ADD_EN = (" Chapter 45 carries the tail of the itnab chapter (lines ~2905-2950, sahifa 100-101): s1-s3 "
          "are al-Baqara 2:222-223 (parts), s9 Ghafir 40:7 (part) and s16 al-Anbiya 21:23 — received "
          "Qur'anic text in standard imla; the source prints فَاْتُوهُنَّ، اَمَرَكُمُ، اِنَّ، اَلَّذِينَ، يُسْئَلُ، "
          "يُسْئَلُونَ with its own hamza seats, written here فَأْتُوهُنَّ، أَمَرَكُمُ، إِنَّ، الَّذِينَ، يُسْأَلُ، "
          "يُسْأَلُونَ. s12-s13 (Abu Tammam), s14-s15 ('Abd al-Samad) and s17-s18 (al-Hamasi) are the "
          "bayts as the source recites them, split at the hemistich, نَاهِدِ keeping the printed rhyme "
          "kasra without tanwin. s10-s11 are the musannif's words on the relative ijaz and itnab. "
          "s4-s8 are RESTORATIONS, not quotations: the source gives the three closing khilafs and the "
          "lead-in to 40:7 only in Ottoman-Turkish paraphrase, and the Arabic restores them in the "
          "musannif's definitional register; each is marked «restored» in its translation.")
ADD_TR = (" Kırk beşinci bâb ıtnâb bahsinin sonunu taşır (satır ~2905-2950, sahife 100-101): s1-s3 "
          "Bakara 2:222-223 (kısmen), s9 Mü'min 40:7 (kısmen), s16 Enbiyâ 21:23 — standart imlâ ile "
          "mervî Kur'ân metni; kaynak فَاْتُوهُنَّ، اَمَرَكُمُ، اِنَّ، اَلَّذِينَ، يُسْئَلُ، يُسْئَلُونَ'yi kendi "
          "hemze oturaklarıyla basar, burada فَأْتُوهُنَّ، أَمَرَكُمُ، إِنَّ، الَّذِينَ، يُسْأَلُ، يُسْأَلُونَ "
          "yazılmıştır. s12-s13 (Ebû Temmâm), s14-s15 (Abdüssamed) ve s17-s18 (Hamâsî) kaynağın okuduğu "
          "beyitlerdir, mısra başından bölünmüş; نَاهِدِ basılı kafiye kesresini tenvinsiz korur. "
          "s10-s11 musannifin nispî îcâz ve ıtnâb hakkındaki sözleridir. s4-s8 ALINTI DEĞİL GERİ YAZIMDIR: "
          "kaynak üç kapanış hilâfını ve 40:7'ye girişi yalnız Osmanlıca paraphrase ile verir; Arapça, "
          "onları musannifin tarif üslûbunda geri yazar; her biri tercümesinde «geri yazılmıştır» diye "
          "işaretlidir.")
if "2905-2950" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
for k, v in GLOSS_ADD.items():
    gl["entries"].setdefault(k, v)                 # author scripts only ADD
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
def subst(obj, table):
    s = json.dumps(obj, ensure_ascii=False)
    s = re.sub("|".join(map(re.escape, table)), lambda m: table[m.group(0)], s)
    return json.loads(s)
V = mo["verbs"]
if "amara-v" not in V:
    # أَمَرَ يَأْمُرُ — bab نَصَرَ, hamzated fa; the amr drops its hamza: مُرْ.
    V["amara-v"] = _sg.sound1("nasara", "أَمَر", "أْمُر", "مُر", "أَمْر", "آمِر",
                              "مَأْمُور", "أُمِرَ", "يُؤْمَرُ",
                              "مَهْمُوزُ الْفَاءِ: أَمْرُهُ مُرْ — حُذِفَتْ هَمْزَتُهُ مَعَ هَمْزَةِ الْوَصْلِ.")
if "ahabba" not in V:
    ahalla = copy_morph("kitab-al-sulh", "ahalla")
    e = subst(ahalla, {"ل": "ب"})
    e["bab"] = ahalla["bab"]; e["wazn"] = ahalla["wazn"]
    e["masdar"] = "إِحْبَاب"
    e["note"] = "مُضَاعَفٌ مِنَ الْإِفْعَالِ عَلَى مِثَالِ أَحَلَّ: الْجَزْمُ بِالْفَتْحِ — لَمْ يُحِبَّ، وَيَجُوزُ لَمْ يُحْبِبْ."
    V["ahabba"] = e
if "jawwaza" not in V:
    V["jawwaza"] = _sg.derived(_sg.B2, _sg.W2, "ُ", "جَوَّز", "جَوِّز", "جَوِّز",
                               "تَجْوِيز", "مُجَوِّز", "مُجَوَّز", "جُوِّزَ", "يُجَوَّزُ")
if "sabbaha" not in V:
    V["sabbaha"] = _sg.derived(_sg.B2, _sg.W2, "ُ", "سَبَّح", "سَبِّح", "سَبِّح",
                               "تَسْبِيح", "مُسَبِّح", "مُسَبَّح", "سُبِّحَ", "يُسَبَّحُ")
if "shamila" not in V:
    V["shamila"] = _sg.sound1("samia", "شَمِل", "شْمَل", "اِشْمَل", "شُمُول", "شَامِل",
                              "مَشْمُول", "شُمِلَ", "يُشْمَلُ")
if "baraza" not in V:
    V["baraza"] = _sg.sound1("nasara", "بَرَز", "بْرُز", "اُبْرُز", "بُرُوز", "بَارِز")
if "sadda" not in V:
    sarra = V["sarra"]
    e = subst(sarra, {"س": "ص", "ر": "د"})
    e["bab"] = sarra["bab"]; e["wazn"] = sarra["wazn"]
    e["masdar"] = "صَدّ"; e["ismFail"] = "صَادّ"; e["ismMaful"] = "مَصْدُود"
    e["note"] = "مُضَاعَفٌ عَلَى مِثَالِ سَرَّ يَسُرُّ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَصُدَّ، وَيَجُوزُ لَمْ يَصْدُدْ."
    V["sadda"] = e
if "anna-verb" not in V:
    shabba = V["shabba"]
    e = subst(shabba, {"ش": "ع", "ب": "ن"})
    e["bab"] = shabba["bab"]; e["wazn"] = shabba["wazn"]
    e = _sg.idgham(e)                              # نْنَ → نَّ (يَعْنِنْنَ → يَعْنِنَّ)
    e["masdar"] = "عَنّ"; e["ismFail"] = "عَانّ"
    e.pop("ismMaful", None)
    e["note"] = "مُضَاعَفٌ عَلَى مِثَالِ شَبَّ يَشِبُّ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَعِنَّ، وَيَجُوزُ لَمْ يَعْنِنْ."
    V["anna-verb"] = e
for pkg, key in [("mukhtasar-al-manar", "hamala"), ("yunus-wa-al-hut", "amana"),
                 ("aqaid-ahl-al-sunna", "ankara"), ("wasiyyat-abi-hanifa-samti", "waliya")]:
    if key not in V:
        V[key] = copy_morph(pkg, key)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 149
GR = ROOT / "content/grammar"
NOTE149 = {
 "id": "ijaz-itnab-nisbi",
 "title": {"ar": "الْإِيجَازُ وَالْإِطْنَابُ النِّسْبِيَّانِ",
           "en": "Ijaz and itnab as relative terms",
           "tr": "Nispî îcâz ve ıtnâb"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — الإيجاز والإطناب: خاتمة الباب"],
 "question": {
  "en": ["Are two speeches equal in the ROOT of their meaning? Only then can one be weighed against the other.",
         "Which has fewer letters? That one is the ijaz — relative to the other, not to any customary measure.",
         "Is one an aya and the other a verse? Then say «near to it», as the musannif does: a Qur'anic text and a poet's are not weighed on one scale."],
  "tr": ["İki söz mânâlarının ASLINDA denk mi? Ancak o zaman biri ötekiyle tartılır.",
         "Hangisinin harfi az? O, îcâzdır — herhangi bir müteârefe göre değil, ötekine göre.",
         "Biri âyet, öteki şiir mi? O zaman musannif gibi «ona yakındır» de: Kur'ân metni ile şairin sözü bir terazide tartılmaz."]},
 "plain": {
  "en": "A second ruler for ijaz and itnab: count a speech's letters against ANOTHER speech that says the same thing. Abu Tammam needs one hemistich where 'Abd al-Samad needs a bayt; 21:23 says in six words what al-Hamasi spends fourteen on. Neither is faulty — the names are relative.",
  "tr": "Îcâz ve ıtnâba ikinci cetvel: bir sözün harflerini aynı şeyi söyleyen BAŞKA bir söze karşı say. Ebû Temmâm'ın tek mısraa sığdırdığını Abdüssamed bir beyitte söyler; 21:23'ün altı kelimesi Hamâsî'de on dört olur. İkisi de kusurlu değildir — adlar nispîdir."},
 "explanation": {
  "en": "The matn: وَقَدْ يُوصَفُ الْكَلَامُ بِالْإِيجَازِ وَالْإِطْنَابِ بِاعْتِبَارِ كَثْرَةِ حُرُوفِهِ وَقِلَّتِهَا بِالنِّسْبَةِ إِلَى كَلَامٍ آخَرَ مُسَاوٍ لَهُ فِي أَصْلِ الْمَعْنَى — «a speech may be described as ijaz and as itnab by the reckoning of the many-ness and few-ness of its letters, in relation to ANOTHER speech equal to it in the root of its meaning». Three conditions hide in the wording. (1) بِاعْتِبَارِ كَثْرَةِ حُرُوفِهِ — the measure is arithmetic, letters counted, not a judgment of the addressee's need. (2) مُسَاوٍ لَهُ فِي أَصْلِ الْمَعْنَى — the two speeches must share their CORE meaning; a difference of nuance does not break the comparison, a difference of substance does. (3) بِالنِّسْبَةِ إِلَى كَلَامٍ آخَرَ — the description is RELATIVE: the same speech may be ijaz beside one text and itnab beside another. The four texts: Abu Tammam's يَصُدُّ عَنِ الدُّنْيَا إِذَا عَنَّ سُودَدٌ • وَلَوْ بَرَزَتْ فِي زِيِّ عَذْرَاءَ نَاهِدِ, whose FIRST HEMISTICH alone is the ijaz beside 'Abd al-Samad's whole bayt وَلَسْتُ بِنَظَّارٍ إِلَى جَانِبِ الْغِنَى • إِذَا كَانَتِ الْعَلْيَاءُ فِي جَانِبِ الْفَقْرِ (itnab: a full bayt for one hemistich's thought — honour preferred to wealth); then 21:23 لَا يُسْأَلُ عَمَّا يَفْعَلُ وَهُمْ يُسْأَلُونَ beside al-Hamasi's وَنُنْكِرُ إِنْ شِئْنَا عَلَى النَّاسِ قَوْلَهُمْ • وَلَا يُنْكِرُونَ الْقَوْلَ حِينَ نَقُولُ — the same balance of unanswerable power, in six words against fourteen. Of this second pair the musannif says only «and near to it» (وَيَقْرُبُ مِنْهُ), because an aya and a poet's bayt are not weighed on one scale in wording or in meaning. Grammar the four texts carry: the geminates صَدَّ and عَنَّ; لَوْ الْوَصْلِيَّة with the waw of hal and no jawab; the diptote mamdud عَذْرَاءَ and a rhyme's dropped tanwin (نَاهِدِ); the zaida ba on لَيْسَ's khabar (بِنَظَّارٍ) and the فَعَّال mubalagha; كَانَتِ's kasra before the wasl; the two passives of سَأَلَ side by side; إِنْ شِئْنَا with its answer unspoken.",
  "tr": "Matn: وَقَدْ يُوصَفُ الْكَلَامُ بِالْإِيجَازِ وَالْإِطْنَابِ بِاعْتِبَارِ كَثْرَةِ حُرُوفِهِ وَقِلَّتِهَا بِالنِّسْبَةِ إِلَى كَلَامٍ آخَرَ مُسَاوٍ لَهُ فِي أَصْلِ الْمَعْنَى — «söz, harflerinin çokluğu ve azlığı itibariyle, mânâsının aslında kendisine denk BAŞKA bir söze nispetle de îcâz ve ıtnâb ile vasfedilebilir». İfadede üç şart saklıdır. (1) بِاعْتِبَارِ كَثْرَةِ حُرُوفِهِ — ölçü aritmetiktir: harfler sayılır, muhâtabın ihtiyacı yargılanmaz. (2) مُسَاوٍ لَهُ فِي أَصْلِ الْمَعْنَى — iki söz ÖZ mânâlarını paylaşmalıdır; incelik farkı mukayeseyi bozmaz, cevher farkı bozar. (3) بِالنِّسْبَةِ إِلَى كَلَامٍ آخَرَ — vasıf NİSPÎDİR: aynı söz bir metnin yanında îcâz, başkasının yanında ıtnâb olabilir. Dört metin: Ebû Temmâm'ın يَصُدُّ عَنِ الدُّنْيَا إِذَا عَنَّ سُودَدٌ • وَلَوْ بَرَزَتْ فِي زِيِّ عَذْرَاءَ نَاهِدِ beyti — yalnız İLK MISRAI, Abdüssamed'in bütün beyti وَلَسْتُ بِنَظَّارٍ إِلَى جَانِبِ الْغِنَى • إِذَا كَانَتِ الْعَلْيَاءُ فِي جَانِبِ الْفَقْرِ yanında îcâzdır (ıtnâb: tek mısraın düşüncesi için tam bir beyit — şeref zenginliğe tercih edilir); sonra 21:23 لَا يُسْأَلُ عَمَّا يَفْعَلُ وَهُمْ يُسْأَلُونَ, Hamâsî'nin وَنُنْكِرُ إِنْ شِئْنَا عَلَى النَّاسِ قَوْلَهُمْ • وَلَا يُنْكِرُونَ الْقَوْلَ حِينَ نَقُولُ beyti yanında — aynı sorgulanamaz güç dengesi, on dörde karşı altı kelimede. Bu ikinci çift için musannif yalnız «ona yakındır» (وَيَقْرُبُ مِنْهُ) der; çünkü âyet ile şairin beyti lafızda da mânâda da bir terazide tartılmaz. Dört metnin taşıdığı gramer: muzâaf صَدَّ ve عَنَّ; hâl vâvlı, cevapsız vasliyye لَوْ; gayr-ı munsarif memdûd عَذْرَاءَ ve kafiyenin düşürdüğü tenvin (نَاهِدِ); لَيْسَ'nin haberindeki zâid bâ (بِنَظَّارٍ) ve فَعَّال mübalağası; كَانَتِ'nin vasıldan önceki kesresi; سَأَلَ'nin yan yana iki meçhûlü; cevabı söylenmeyen إِنْ شِئْنَا."},
 "examples": [
  {"ar": "يَصُدُّ عَنِ الدُّنْيَا إِذَا عَنَّ سُودَدٌ",
   "en": "one hemistich — the ijaz beside 'Abd al-Samad's whole bayt.",
   "tr": "tek mısra — Abdüssamed'in bütün beyti yanında îcâz.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s12"},
  {"ar": "وَلَسْتُ بِنَظَّارٍ إِلَى جَانِبِ الْغِنَى",
   "en": "a whole bayt for the same thought — the itnab.",
   "tr": "aynı düşünce için bütün bir beyit — ıtnâb.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s14"},
  {"ar": "لَا يُسْأَلُ عَمَّا يَفْعَلُ وَهُمْ يُسْأَلُونَ",
   "en": "six words beside al-Hamasi's fourteen — «and near to it».",
   "tr": "Hamâsî'nin on dört kelimesi yanında altı kelime — «ona yakındır».",
   "sourceStory": "talkhis-al-miftah", "sentence": "s16"}],
 "commonMistakes": [
  {"wrong": "«Abdüssamed'in beyti ıtnâb olduğuna göre kusurludur»",
   "right": "«Nispî ıtnâb bir kusur değil, bir ölçüdür — beyit ancak Ebû Temmâm'ın mısraına göre uzundur»",
   "why": {"en": "The chapter's second ruler names speeches by COUNT against one another, not against the addressee's need. A bayt called itnab beside one hemistich may be perfect musawat beside the customary speech; the label moves with the comparison.",
           "tr": "Bâbın ikinci cetveli sözleri muhâtabın ihtiyacına değil, birbirine karşı SAYARAK adlandırır. Bir mısra yanında ıtnâb denen beyit, müteâref söze göre tam müsâvât olabilir; etiket mukayeseyle yer değiştirir."}}],
 "relatedNotes": ["ijaz-itnab-musawat", "asbab-al-itnab", "itirad", "tadhyil", "takmil-wa-tatmim",
                  "sighat-mubalagha", "mamnu-min-sarf", "ism-mamdud", "doubled-verbs", "kana-wa-akhawatuha"]}

(GR / "ijaz-itnab-nisbi.json").write_text(
    json.dumps(NOTE149, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch45:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + amara-v/ahabba/jawwaza/sabbaha/shamila/baraza/sadda/anna-verb (+hamala/amana/ankara/waliya copied); note 149")
