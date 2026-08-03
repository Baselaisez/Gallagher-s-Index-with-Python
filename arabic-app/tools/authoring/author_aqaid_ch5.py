# -*- coding: utf-8 -*-
"""Author chapter 5 of content/samples/aqaid-ahl-al-sunna.

The project owner supplied the COMPLETE matn of al-'Aqa'id al-Nasafiyya
(research/sources/aqaid-nasafi-matn-full.txt). Chapter 5 continues exactly
where chapter 3 stopped: the Muhdith of the world and His attributes, then
the Qur'an as Allah's uncreated kalam — the matn's own order, taken as
verbatim contiguous spans and re-vowelled against the received text.
Everything remains pending-scholarly-review.

Unlike the story-length regenerators this script only ADDS chapter 5 to the
already-authored package: it writes chapters/5.json, appends the chapter to
the manifest (bumping the version), and merges the new glossary entries and
verb paradigms. It is idempotent — run it twice and nothing changes twice.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PKG = ROOT / "content/samples/aqaid-ahl-al-sunna"

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import sarf_gen as _sg

DIA = re.compile("[ً-ٰ]")
def bare(s): return DIA.sub("", s)

def tok(full, lex, pos, grammar, ar, en, tr, punct=None, segments=None):
    t = {"surface": {"full": full, "smart": full, "bare": bare(full)},
         "lex": lex, "pos": pos}
    if grammar: t["grammar"] = grammar
    t["irab"] = {"ar": ar, "en": en, "tr": tr}
    if segments: t["segments"] = segments
    if punct: t["punctAfter"] = punct
    return t

def seg(form, lex, pos): return {"form": form, "lex": lex, "pos": pos}

J = lambda text, ar, en, tr: {"text": text, "ar": ar, "en": en, "tr": tr}

S = []

# -- s1: the Muhdith and the parade of na'ts ---------------------------------
S.append({"id": "s1", "translation": {
 "en": "And the Originator of the world is Allah the Exalted — the One, the Beginninglessly-Eternal, the Living, the Able, the All-Knowing, the All-Hearing, the All-Seeing.",
 "tr": "Âlemi yoktan var eden Allah Teâlâ'dır — Vâhid'dir, Kadîm'dir, Hayy'dır, Kâdir'dir, Alîm'dir, Semî'dir, Basîr'dir."},
 "tokens": [
  tok("وَالْمُحْدِثُ","muhdith","noun",["mubtada-khabar","ism-fail","form-iv-verbs"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الْمُحْدِثُ» مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «أَحْدَثَ»؛ قَابِلْهُ بِـ«مُحْدَث» بِالْفَتْحِ، اسْمِ الْمَفْعُولِ.",
      "Isti'naf waw; mubtada in raf' — the ism fa'il of أَحْدَثَ (Form IV). Contrast مُحْدَث with fatha, the ism maf'ul of chapter 3.",
      "İstinâf vâvı; merfû mübteda — «أَحْدَثَ» (if'âl) fiilinin ism-i fâili. 3. bölümdeki fethalı «مُحْدَث» (ism-i mef'ûl) ile karşılaştırın.",
      segments=[seg("وَ","wa","conj"), seg("الْمُحْدِثُ","muhdith","noun")]),
  tok("لِلْعَالَمِ","li","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«الْمُحْدِثُ».",
      "Preposition + noun, attached to the ism fa'il الْمُحْدِث.",
      "«الْمُحْدِثُ» ism-i fâiline mütealliḳ câr-mecrûr.",
      segments=[seg("لِ","li","prep"), seg("الْعَالَمِ","alam","noun")]),
  tok("هُوَ","pron-3ms-munfasil","pron",["damir-fasl"],
      "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.",
      "A damir fasl (pronoun of separation) between mubtada and khabar — no place in i'rab.",
      "Mübteda ile haber arasında zamîr-i fasl — i'râbdan mahalli yoktur."),
  tok("اللهُ","allah","noun",["mubtada-khabar"],
      "لَفْظُ الْجَلَالَةِ خَبَرٌ مَرْفُوعٌ.",
      "The majestic name — khabar in raf'.",
      "Lafza-i celâl — merfû haber."),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "Past verb with a hidden fa'il; the clause is parenthetic, for exaltation.",
      "Mâzî fiil, fâili gizli zamir; cümle ta'zîm için mu'terizadır.", punct="،"),
  tok("الْوَاحِدُ","wahid","noun",["naat-sifa"],
      "نَعْتٌ لِلَفْظِ الْجَلَالَةِ مَرْفُوعٌ.",
      "A na't (adjective) of the majestic name, in raf'.",
      "Lafza-i celâlin merfû na'tı.", punct="،"),
  tok("الْقَدِيمُ","qadim","noun",["naat-sifa","sifa-mushabbaha"],
      "نَعْتٌ ثَانٍ مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ عَلَى «فَعِيل».",
      "Second na't in raf' — a sifa mushabbaha on the فَعِيل pattern.",
      "İkinci merfû na't — «فَعِيل» vezninde sıfat-ı müşebbehe.", punct="،"),
  tok("الْحَيُّ","hayy","noun",["naat-sifa","sifa-mushabbaha","doubled-verbs"],
      "نَعْتٌ مَرْفُوعٌ — أَصْلُهُ «حَيِيَ»، صِفَةٌ مُشَبَّهَةٌ أُدْغِمَتْ يَاؤُهَا.",
      "Na't in raf' — from حَيِيَ; a sifa mushabbaha whose two yas merged.",
      "Merfû na't — aslı «حَيِيَ»dir; iki yâsı idgam edilmiş sıfat-ı müşebbehe.", punct="،"),
  tok("الْقَادِرُ","qadir","noun",["naat-sifa","ism-fail"],
      "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «قَدَرَ».",
      "Na't in raf' — the ism fa'il of قَدَرَ.",
      "Merfû na't — «قَدَرَ» fiilinin ism-i fâili.", punct="،"),
  tok("الْعَلِيمُ","alim","noun",["naat-sifa","sighat-mubalagha"],
      "نَعْتٌ مَرْفُوعٌ — صِيغَةُ مُبَالَغَةٍ عَلَى «فَعِيل».",
      "Na't in raf' — a mubalagha form on فَعِيل: knowing utterly.",
      "Merfû na't — «فَعِيل» vezninde mübalağa sîgası: hakkıyla bilen.", punct="،"),
  tok("السَّمِيعُ","sami","noun",["naat-sifa","sighat-mubalagha"],
      "نَعْتٌ مَرْفُوعٌ — صِيغَةُ مُبَالَغَةٍ.",
      "Na't in raf' — a mubalagha form: hearing utterly.",
      "Merfû na't — mübalağa sîgası: hakkıyla işiten.", punct="،"),
  tok("الْبَصِيرُ","basir","noun",["naat-sifa","sighat-mubalagha"],
      "نَعْتٌ مَرْفُوعٌ — صِيغَةُ مُبَالَغَةٍ.",
      "Na't in raf' — a mubalagha form: seeing utterly.",
      "Merfû na't — mübalağa sîgası: hakkıyla gören.", punct="."),
 ],
 "jumal": [
  J("وَالْمُحْدِثُ لِلْعَالَمِ هُوَ اللهُ تَعَالَى...",
    "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "A resumed nominal clause — no place in i'rab.",
    "Müste'nefe isim cümlesi — i'râbdan mahalli yoktur."),
  J("تَعَالَى",
    "جُمْلَةٌ مُعْتَرِضَةٌ لِلتَّعْظِيمِ — لَا مَحَلَّ لَهَا.",
    "A parenthetic clause of exaltation — i'rabless.",
    "Ta'zîm için mu'teriza cümlesi — mahalsizdir."),
 ]})

# -- s2: laysa with the extra ba --------------------------------------------
S.append({"id": "s2", "translation": {
 "en": "He is not an accident, nor a body, nor a substance.",
 "tr": "O, araz değildir; cisim de, cevher de değildir."},
 "tokens": [
  tok("لَيْسَ","laysa","verb",["kana-wa-akhawatuha"],
      "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ «كَانَ»، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ.",
      "Defective past verb of the kana family; its ism is a hidden هُوَ.",
      "Kâne'nin kardeşlerinden nâkıs fiil; ismi gizli «هُوَ» zamiridir."),
  tok("بِعَرَضٍ","bi","prep",["huruf-jarr","kana-wa-akhawatuha"],
      "الْبَاءُ زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ، وَ«عَرَضٍ» خَبَرُ «لَيْسَ» مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.",
      "The ba is extra, strengthening the negation; عَرَض is laysa's khabar — jarr in form, nasb in place.",
      "Bâ, nefyi te'kid için zâiddir; «عَرَضٍ» leysenin haberi — lafzan mecrur, mahallen mansubdur.",
      segments=[seg("بِ","bi","prep"), seg("عَرَضٍ","arad","noun")], punct="،"),
  tok("وَلَا","la-nafiya","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.",
      "Joining waw; the لا is extra, re-affirming the negation.",
      "Atıf vâvı; «لَا» nefyi pekiştirmek için zâiddir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("جِسْمٍ","jism","noun",["atf-nasaq"],
      "مَعْطُوفٌ عَلَى «عَرَضٍ» مَجْرُورٌ.",
      "Joined to عَرَضٍ, in jarr.",
      "«عَرَضٍ» üzerine ma'tûf, mecrurdur.", punct="،"),
  tok("وَلَا","la-nafiya","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.",
      "Joining waw; the لا is extra, re-affirming the negation.",
      "Atıf vâvı; «لَا» nefyi pekiştirmek için zâiddir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("جَوْهَرٍ","jawhar","noun",["atf-nasaq"],
      "مَعْطُوفٌ عَلَى «عَرَضٍ» مَجْرُورٌ.",
      "Joined to عَرَضٍ, in jarr.",
      "«عَرَضٍ» üzerine ma'tûf, mecrurdur.", punct="."),
 ],
 "jumal": [
  J("لَيْسَ بِعَرَضٍ وَلَا جِسْمٍ وَلَا جَوْهَرٍ",
    "جُمْلَةٌ مُسْتَأْنَفَةٌ فِي وَصْفِهِ تَعَالَى — لَا مَحَلَّ لَهَا.",
    "A resumed clause continuing His description — i'rabless.",
    "O'nun vasfını sürdüren müste'nefe cümle — mahalsizdir."),
 ]})

# -- s3: nothing resembles Him ----------------------------------------------
S.append({"id": "s3", "translation": {
 "en": "Nothing resembles Him, and nothing passes outside His knowledge and His power.",
 "tr": "Hiçbir şey O'na benzemez; hiçbir şey O'nun ilminden ve kudretinden dışarı çıkmaz."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ غَيْرُ عَامِلَةٍ.",
      "Joining waw; the لا negates without governing.",
      "Atıf vâvı; «لَا» amel etmeyen nefiy lâsıdır.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يُشْبِهُهُ","ashbaha","verb",["mudari-marfu","form-iv-verbs","maful-bihi"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مِنْ «أَشْبَهَ»، وَالْهَاءُ مَفْعُولٌ بِهِ مُقَدَّمٌ.",
      "Mudari in raf' from أَشْبَهَ (Form IV); the ha is a fronted direct object.",
      "«أَشْبَهَ» (if'âl) fiilinin merfû muzârisi; hâ zamiri öne alınmış mef'ûlün bihtir.",
      segments=[seg("يُشْبِهُ","ashbaha","verb"), seg("هُ","pron-3ms","pron")]),
  tok("شَيْءٌ","shay","noun",["fail"],
      "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ.",
      "The fa'il, delayed after its object, in raf'.",
      "Mef'ûlünden sonraya bırakılmış merfû fâil.", punct="،"),
  tok("وَلَا","la-nafiya","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ غَيْرُ عَامِلَةٍ.",
      "Joining waw; the لا negates without governing.",
      "Atıf vâvı; «لَا» amel etmeyen nefiy lâsıdır.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يَخْرُجُ","kharaja","verb",["mudari-marfu","thulathi-mujarrad-babs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — «خَرَجَ يَخْرُجُ» مِنْ بَابِ نَصَرَ.",
      "Mudari in raf' — خَرَجَ يَخْرُجُ of bab نَصَرَ.",
      "Merfû muzâri — «خَرَجَ يَخْرُجُ», nasara bâbındandır."),
  tok("عَنْ","an","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلْمُجَاوَزَةِ.",
      "The jarr letter of passing-beyond.",
      "Mücâvezet (aşma) bildiren cer harfi."),
  tok("عِلْمِهِ","ilm","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«عَنْ» وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "In jarr after عَنْ, itself a mudaf; the ha is its mudaf ilayh.",
      "«عَنْ» ile mecrur ve muzâf; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("عِلْمِ","ilm","noun"), seg("هِ","pron-3ms","pron")]),
  tok("وَقُدْرَتِهِ","qudra","noun",["atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «عِلْمِهِ» مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "Joined to عِلْمِهِ in jarr; the ha is its mudaf ilayh.",
      "«عِلْمِهِ» üzerine ma'tûf, mecrur; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("وَ","wa","conj"), seg("قُدْرَتِ","qudra","noun"), seg("هِ","pron-3ms","pron")]),
  tok("شَيْءٌ","shay","noun",["fail"],
      "فَاعِلُ «يَخْرُجُ» مَرْفُوعٌ.",
      "The fa'il of يَخْرُجُ, in raf'.",
      "«يَخْرُجُ» fiilinin merfû fâili.", punct="."),
 ],
 "jumal": [
  J("وَلَا يُشْبِهُهُ شَيْءٌ",
    "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
    "A joined verbal clause — i'rabless.",
    "Ma'tûf fiil cümlesi — mahalsizdir."),
  J("وَلَا يَخْرُجُ عَنْ عِلْمِهِ وَقُدْرَتِهِ شَيْءٌ",
    "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
    "A joined verbal clause — i'rabless.",
    "Ma'tûf fiil cümlesi — mahalsizdir."),
 ]})

# -- s4: the eternal attributes — khabar muqaddam ---------------------------
S.append({"id": "s4", "translation": {
 "en": "And He has beginninglessly-eternal attributes, subsisting in His essence.",
 "tr": "O'nun, zâtıyla kâim ezelî sıfatları vardır."},
 "tokens": [
  tok("وَلَهُ","li","prep",["huruf-jarr","mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.",
      "Isti'naf waw; the preposition-phrase is a fronted khabar.",
      "İstinâf vâvı; câr-mecrûr öne geçmiş haberdir (haber-i mukaddem).",
      segments=[seg("وَ","wa","conj"), seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
  tok("صِفَاتٌ","sifa","noun",["mubtada-khabar","jam-muannath-salim"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.",
      "The delayed mubtada in raf' — a sound feminine plural.",
      "Sonraya bırakılmış merfû mübteda (mübteda-i muahhar) — cem'-i müennes-i sâlim."),
  tok("أَزَلِيَّةٌ","azali","noun",["naat-sifa"],
      "نَعْتٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى «الْأَزَل».",
      "Na't in raf' — the nisba of الْأَزَل, beginningless eternity.",
      "Merfû na't — «الْأَزَل»e nisbettir: ezelî. (Atölyedeki nisbe kuralının ta kendisi.)"),
  tok("قَائِمَةٌ","qaim","noun",["naat-sifa","ism-fail","hollow-verbs"],
      "نَعْتٌ ثَانٍ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنَ الْأَجْوَفِ «قَامَ»، قُلِبَتْ أَلِفُهُ هَمْزَةً.",
      "Second na't in raf' — the ism fa'il of hollow قَامَ; its alif turned hamza: قَائِم.",
      "İkinci merfû na't — ecvef «قَامَ» fiilinin ism-i fâili; elifi hemzeye dönmüştür: قَائِم."),
  tok("بِذَاتِهِ","bi","prep",["huruf-jarr","idafa-definiteness"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«قَائِمَةٌ»، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "Preposition-phrase attached to قَائِمَة; the ha is the mudaf ilayh.",
      "«قَائِمَةٌ» ismine mütealliḳ câr-mecrûr; hâ zamiri muzâfun ileyhtir.",
      segments=[seg("بِ","bi","prep"), seg("ذَاتِ","dhat","noun"), seg("هِ","pron-3ms","pron")], punct="."),
 ],
 "jumal": [
  J("وَلَهُ صِفَاتٌ أَزَلِيَّةٌ قَائِمَةٌ بِذَاتِهِ",
    "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ مِنْ خَبَرٍ مُقَدَّمٍ وَمُبْتَدَإٍ مُؤَخَّرٍ — لَا مَحَلَّ لَهَا.",
    "A resumed nominal clause of fronted khabar and delayed mubtada — i'rabless.",
    "Haber-i mukaddem ile mübteda-i muahhardan kurulu müste'nefe isim cümlesi — mahalsizdir."),
 ]})

# -- s5: the Qur'an is Allah's uncreated speech -----------------------------
S.append({"id": "s5", "translation": {
 "en": "And the Qur'an is the speech of Allah the Exalted — uncreated.",
 "tr": "Kur'ân, Allah Teâlâ'nın kelâmıdır — mahlûk değildir."},
 "tokens": [
  tok("وَالْقُرْآنُ","quran","noun",["mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الْقُرْآنُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "Isti'naf waw; الْقُرْآن is the mubtada in raf'.",
      "İstinâf vâvı; «الْقُرْآنُ» merfû mübtedadır.",
      segments=[seg("وَ","wa","conj"), seg("الْقُرْآنُ","quran","noun")]),
  tok("كَلَامُ","kalam","noun",["mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "The khabar in raf', itself a mudaf.",
      "Merfû haber ve muzâftır."),
  tok("اللهِ","allah","noun",["idafa-definiteness"],
      "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The majestic name — mudaf ilayh in jarr.",
      "Lafza-i celâl — mecrûr muzâfun ileyhtir."),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "Past verb; the clause is parenthetic, for exaltation.",
      "Mâzî fiil; cümle ta'zîm için mu'terizadır."),
  tok("غَيْرُ","ghayr","noun",["mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ ثَانٍ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "A second khabar in raf', itself a mudaf.",
      "İkinci merfû haber ve muzâftır."),
  tok("مَخْلُوقٍ","makhluq","noun",["idafa-definiteness","ism-maful"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ «خَلَقَ».",
      "Mudaf ilayh in jarr — the ism maf'ul of خَلَقَ.",
      "Mecrûr muzâfun ileyh — «خَلَقَ» fiilinin ism-i mef'ûlüdür.", punct="."),
 ],
 "jumal": [
  J("وَالْقُرْآنُ كَلَامُ اللهِ تَعَالَى غَيْرُ مَخْلُوقٍ",
    "جُمْلَةٌ اسْمِيَّةٌ مُسْتَأْنَفَةٌ — لَا مَحَلَّ لَهَا.",
    "A resumed nominal clause — i'rabless.",
    "Müste'nefe isim cümlesi — mahalsizdir."),
  J("تَعَالَى",
    "جُمْلَةٌ مُعْتَرِضَةٌ لِلتَّعْظِيمِ — لَا مَحَلَّ لَهَا.",
    "A parenthetic clause of exaltation — i'rabless.",
    "Ta'zîm için mu'teriza cümlesi — mahalsizdir."),
 ]})

# -- s6: the ism maf'ul parade ----------------------------------------------
S.append({"id": "s6", "translation": {
 "en": "And it is written in our mushafs, preserved in our hearts, recited with our tongues, heard with our ears.",
 "tr": "O, mushaflarımızda yazılıdır, kalplerimizde mahfuzdur, dillerimizle okunur, kulaklarımızla işitilir."},
 "tokens": [
  tok("وَهُوَ","pron-3ms-munfasil","pron",["mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«هُوَ» مُبْتَدَأٌ.",
      "Joining waw; هُوَ is the mubtada.",
      "Atıf vâvı; «هُوَ» mübtedadır.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","pron-3ms-munfasil","pron")]),
  tok("مَكْتُوبٌ","maktub","noun",["mubtada-khabar","ism-maful"],
      "خَبَرٌ أَوَّلُ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «كَتَبَ»: مَفْعُول.",
      "First khabar in raf' — the ism maf'ul of كَتَبَ, on مَفْعُول.",
      "Birinci merfû haber — «كَتَبَ» fiilinin ism-i mef'ûlü: «مَفْعُول» vezninde."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلظَّرْفِيَّةِ.",
      "The jarr letter of containment.",
      "Zarfiyyet bildiren cer harfi."),
  tok("مَصَاحِفِنَا","mushaf","noun",["idafa-definiteness","mamnu-min-sarf"],
      "مَجْرُورٌ بِالْكَسْرَةِ — «مَصَاحِف» صِيغَةُ مُنْتَهَى الْجُمُوعِ مَمْنُوعَةٌ مِنَ الصَّرْفِ، لَكِنَّهَا جُرَّتْ بِالْكَسْرَةِ لِإِضَافَتِهَا إِلَى «نَا».",
      "In jarr with kasra — مَصَاحِف is a diptote (muntaha al-jumu'), yet the idafa to نَا restores its kasra.",
      "Kesra ile mecrur — «مَصَاحِف» gayr-i munsariftir (müntehe'l-cümû); fakat «نَا»ya izâfetle kesrayı geri kazanır.",
      segments=[seg("مَصَاحِفِ","mushaf","noun"), seg("نَا","pron-1p","pron")], punct="،"),
  tok("مَحْفُوظٌ","mahfuz","noun",["mubtada-khabar","ism-maful"],
      "خَبَرٌ ثَانٍ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «حَفِظَ».",
      "Second khabar in raf' — the ism maf'ul of حَفِظَ.",
      "İkinci merfû haber — «حَفِظَ» fiilinin ism-i mef'ûlü."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلظَّرْفِيَّةِ.",
      "The jarr letter of containment.",
      "Zarfiyyet bildiren cer harfi."),
  tok("قُلُوبِنَا","qalb","noun",["idafa-definiteness"],
      "مَجْرُورٌ وَهُوَ مُضَافٌ، وَ«نَا» مُضَافٌ إِلَيْهِ.",
      "In jarr, a mudaf; نَا is its mudaf ilayh.",
      "Mecrur ve muzâf; «نَا» muzâfun ileyhtir.",
      segments=[seg("قُلُوبِ","qalb","noun"), seg("نَا","pron-1p","pron")], punct="،"),
  tok("مَقْرُوءٌ","maqru","noun",["mubtada-khabar","ism-maful"],
      "خَبَرٌ ثَالِثٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنَ الْمَهْمُوزِ «قَرَأَ»: مَقْرُوء.",
      "Third khabar in raf' — the ism maf'ul of hamzated قَرَأَ: مَقْرُوء.",
      "Üçüncü merfû haber — mehmûz «قَرَأَ» fiilinin ism-i mef'ûlü: مَقْرُوء."),
  tok("بِأَلْسِنَتِنَا","bi","prep",["huruf-jarr","idafa-definiteness"],
      "جَارٌّ وَمَجْرُورٌ، وَ«أَلْسِنَة» مُضَافٌ إِلَى «نَا».",
      "Preposition + noun; أَلْسِنَة in idafa to نَا.",
      "Câr-mecrûr; «أَلْسِنَة» kelimesi «نَا»ya muzâftır.",
      segments=[seg("بِ","bi","prep"), seg("أَلْسِنَتِ","alsina","noun"), seg("نَا","pron-1p","pron")], punct="،"),
  tok("مَسْمُوعٌ","masmu","noun",["mubtada-khabar","ism-maful"],
      "خَبَرٌ رَابِعٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «سَمِعَ».",
      "Fourth khabar in raf' — the ism maf'ul of سَمِعَ.",
      "Dördüncü merfû haber — «سَمِعَ» fiilinin ism-i mef'ûlü."),
  tok("بِآذَانِنَا","bi","prep",["huruf-jarr","idafa-definiteness"],
      "جَارٌّ وَمَجْرُورٌ، وَ«آذَان» جَمْعُ «أُذُن» مُضَافٌ إِلَى «نَا».",
      "Preposition + noun; آذَان, plural of أُذُن, in idafa to نَا.",
      "Câr-mecrûr; «أُذُن» kelimesinin cem'i «آذَان», «نَا»ya muzâftır.",
      segments=[seg("بِ","bi","prep"), seg("آذَانِ","udhun","noun"), seg("نَا","pron-1p","pron")], punct="."),
 ],
 "jumal": [
  J("وَهُوَ مَكْتُوبٌ فِي مَصَاحِفِنَا...",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ، وَأَخْبَارُهَا مُتَعَدِّدَةٌ — لَا مَحَلَّ لَهَا.",
    "A joined nominal clause with multiple khabars — i'rabless.",
    "Ma'tûf isim cümlesi; haberi müteaddittir — mahalsizdir."),
 ]})

TITLE5 = {"ar": "صِفَاتُ اللهِ تَعَالَى",
          "en": "The Attributes of Allah",
          "tr": "Allah Teâlâ'nın Sıfatları"}

# -- glossary additions ------------------------------------------------------
GLOSS_ADD = {
 "muhdith": {"lemma": "مُحْدِث", "root": "ح د ث", "pos": "noun",
   "gloss": {"en": "originator, who brings into being", "tr": "muhdis; yoktan var eden"}, "level": 5},
 "wahid": {"lemma": "وَاحِد", "root": "و ح د", "pos": "noun",
   "gloss": {"en": "one; the One", "tr": "bir; Vâhid"}, "level": 2},
 "qadim": {"lemma": "قَدِيم", "root": "ق د م", "pos": "noun",
   "gloss": {"en": "beginninglessly eternal", "tr": "kadîm; başlangıcı olmayan"}, "level": 4},
 "hayy": {"lemma": "حَيّ", "root": "ح ي ي", "pos": "noun",
   "gloss": {"en": "living", "tr": "hayy; diri"}, "level": 3},
 "qadir": {"lemma": "قَادِر", "root": "ق د ر", "pos": "noun",
   "gloss": {"en": "able, powerful", "tr": "kâdir; güç yetiren"}, "level": 3},
 "alim": {"lemma": "عَلِيم", "root": "ع ل م", "pos": "noun",
   "gloss": {"en": "all-knowing", "tr": "alîm; hakkıyla bilen"}, "level": 3},
 "sami": {"lemma": "سَمِيع", "root": "س م ع", "pos": "noun",
   "gloss": {"en": "all-hearing", "tr": "semî'; hakkıyla işiten"}, "level": 3},
 "basir": {"lemma": "بَصِير", "root": "ب ص ر", "pos": "noun",
   "gloss": {"en": "all-seeing", "tr": "basîr; hakkıyla gören"}, "level": 3},
 "jism": {"lemma": "جِسْم", "root": "ج س م", "pos": "noun",
   "gloss": {"en": "body", "tr": "cisim"}, "level": 3},
 "ashbaha": {"lemma": "أَشْبَهَ", "root": "ش ب ه", "pos": "verb",
   "gloss": {"en": "to resemble", "tr": "benzemek"}, "level": 4},
 "kharaja": {"lemma": "خَرَجَ", "root": "خ ر ج", "pos": "verb",
   "gloss": {"en": "to go out, pass beyond", "tr": "çıkmak"}, "level": 2},
 "an": {"lemma": "عَنْ", "pos": "prep",
   "gloss": {"en": "from, away from, beyond", "tr": "-den (aşarak); hakkında"}, "level": 1},
 "qudra": {"lemma": "قُدْرَة", "root": "ق د ر", "pos": "noun",
   "gloss": {"en": "power", "tr": "kudret"}, "level": 3},
 "azali": {"lemma": "أَزَلِيّ", "root": "أ ز ل", "pos": "noun",
   "gloss": {"en": "beginninglessly eternal (nisba of azal)", "tr": "ezelî"}, "level": 4},
 "qaim": {"lemma": "قَائِم", "root": "ق و م", "pos": "noun",
   "gloss": {"en": "subsisting, standing", "tr": "kâim; ayakta duran"}, "level": 3},
 "quran": {"lemma": "الْقُرْآن", "root": "ق ر أ", "pos": "noun",
   "gloss": {"en": "the Qur'an", "tr": "Kur'ân"}, "level": 1},
 "kalam": {"lemma": "كَلَام", "root": "ك ل م", "pos": "noun",
   "gloss": {"en": "speech", "tr": "kelâm; söz"}, "level": 2},
 "ghayr": {"lemma": "غَيْر", "pos": "noun",
   "gloss": {"en": "other than; non-", "tr": "gayr; başka; olmayan"}, "level": 2},
 "makhluq": {"lemma": "مَخْلُوق", "root": "خ ل ق", "pos": "noun",
   "gloss": {"en": "created", "tr": "mahlûk; yaratılmış"}, "level": 3},
 "maktub": {"lemma": "مَكْتُوب", "root": "ك ت ب", "pos": "noun",
   "gloss": {"en": "written", "tr": "yazılı; yazılmış"}, "level": 2},
 "mushaf": {"lemma": "مُصْحَف", "root": "ص ح ف", "pos": "noun",
   "gloss": {"en": "mushaf, codex of the Qur'an", "tr": "mushaf"}, "level": 2},
 "mahfuz": {"lemma": "مَحْفُوظ", "root": "ح ف ظ", "pos": "noun",
   "gloss": {"en": "preserved", "tr": "mahfuz; korunmuş"}, "level": 3},
 "maqru": {"lemma": "مَقْرُوء", "root": "ق ر أ", "pos": "noun",
   "gloss": {"en": "recited, read", "tr": "okunan"}, "level": 3},
 "masmu": {"lemma": "مَسْمُوع", "root": "س م ع", "pos": "noun",
   "gloss": {"en": "heard", "tr": "işitilen"}, "level": 3},
 "udhun": {"lemma": "أُذُن", "root": "أ ذ ن", "pos": "noun",
   "gloss": {"en": "ear", "tr": "kulak"}, "level": 1},
 "pron-1p": {"lemma": "نَا", "pos": "pron",
   "gloss": {"en": "our / us (attached)", "tr": "-imiz / bizi (bitişik)"}, "level": 1},
}

# -- paradigms: kharaja copied from Kitab al-Waqf (lemma identity), ---------
# ashbaha engine-built on the Form IV road.
def build_morph_add():
    waqf = json.loads((ROOT / "content/samples/kitab-al-waqf/morphology.json")
                      .read_text(encoding="utf-8"))["verbs"]
    return {
        "kharaja": waqf["kharaja"],
        "ashbaha": _sg.derived(
            _sg.B4, _sg.W4, "ُ", "أَشْبَه", "شْبِه", "أَشْبِه",
            "إِشْبَاه", "مُشْبِه", "مُشْبَه", "أُشْبِهَ", "يُشْبَهُ"),
    }

def main():
    # chapter file
    (PKG / "chapters/5.json").write_text(
        json.dumps({"chapter": 5, "sentences": S}, ensure_ascii=False, indent=1),
        encoding="utf-8")
    # manifest: append chapter 5 once, bump version
    man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
    if not any(c["n"] == 5 for c in man["chapters"]):
        man["chapters"].append({"n": 5, "title": TITLE5})
    man["chapters"].sort(key=lambda c: c["n"])
    man["version"] = "0.3.0"
    man["attribution"]["en"] = (
        "Arabic passages quoted in the Nasafi creed lesson notes supplied by the project "
        "owner (pages 1, 2, 4, 6, 7 and 12), transcribed from the rendered pages and "
        "segmented for study. The surrounding exposition in that source is in Ottoman "
        "Turkish; only its vocalized Arabic is used here. Chapter 5 onward is taken "
        "directly from the complete matn of al-'Aqa'id al-Nasafiyya supplied by the "
        "project owner (research/sources/aqaid-nasafi-matn-full.txt), as verbatim "
        "contiguous spans re-vowelled against the received text. Three sentences — "
        "2:s2, 2:s6 and 3:s2 — are the matn as the lesson notes render it.")
    (PKG / "manifest.json").write_text(
        json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
    # glossary merge
    gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
    gl["entries"].update(GLOSS_ADD)
    (PKG / "glossary.json").write_text(
        json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
    # morphology merge
    mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
    mo["verbs"].update(build_morph_add())
    (PKG / "morphology.json").write_text(
        json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
    ntok = sum(len(s["tokens"]) for s in S)
    print(f"chapter 5 written: {len(S)} sentences, {ntok} tokens; "
          f"glossary +{len(GLOSS_ADD)}, verbs +2; manifest -> {man['version']}")

if __name__ == "__main__":
    main()
