# -*- coding: utf-8 -*-
"""Author chapter 28 of talkhis-al-miftah — بَابُ الْأَمْرِ.

The amr bab (sahifa 75): طَلَبُ الْفِعْلِ عَلَى وَجْهِ الِاسْتِعْلَاءِ.

  • the sigha's three dresses: with the lam (لِيَحْضُرْ زَيْدٌ), without it
    (أَكْرِمْ عَمْرًا), and the ISM FI'L (رُوَيْدَ بَكْرًا) — the musannif's
    mawdu'-lah: the mind runs straight to talab-on-isti'la at any of them.
  • the departures: tahdid (اِعْمَلُوا مَا شِئْتُمْ, Fussilat 41:40),
    taskhir (كُونُوا قِرَدَةً خَاسِئِينَ, al-Baqara 2:65), taswiya
    (اِصْبِرُوا أَوْ لَا تَصْبِرُوا, al-Tur 52:16), du'a (رَبِّ اغْفِرْ لِي,
    al-A'raf 7:151) — ibaha, ta'jiz, ihana, tamanni (the Imru' al-Qays
    bayt) and iltimas in note 130, with Sakkaki's fawr claim and the
    musannif's nazar.

ATTRIBUTION: the four ayat are received Qur'anic text quoted exactly;
لِيَحْضُرْ زَيْدٌ, أَكْرِمْ عَمْرًا and رُوَيْدَ بَكْرًا are the source's own
worked examples verbatim (research/sources/talkhis-al-miftah-balagha.txt
lines ~2158-2185, sahifa 75), Ottoman plain-alif normalized to standard
orthography — a recorded normalization.

Grammar this chapter teaches:
  • note 130 `al-amr-wa-wujuhuh` — the definition, the mawdu'-lah khilaf,
    the fawr khilaf, the wujuh with their ayat.
  • engine work: the ism-fil closed-class row (رُوَيْدَ governs like a
    verb, conjugates like nothing), the lam-of-command named on the
    majzum's own row, MaEngine 6i (the OBJECT SEAT as the fourth
    definiteness route), CaseEngine's trimmed-vocative guard (رَبِّ's
    kasra is a dalil, not a jarr), and the three amr frames the surface
    settles: amrDua, amrTaswiya, amrTahdid.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
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

TITLE28 = {"ar": "بَابُ الْأَمْرِ — طَلَبُ الْفِعْلِ عَلَى وَجْهِ الِاسْتِعْلَاءِ",
           "en": "The Amr: Demanding the Deed From Above",
           "tr": "Emir Bâbı: Fiili İsti'lâ ile Talep"}

# ------------------------------------------------- s1 — the lam of command
S.append({"id": "s1", "translation": {
 "en": "Let Zayd be present! (The amr's first dress: the LAM of command jazming its mudari.)",
 "tr": "Zeyd hazır olsun! (Emrin ilk kılığı: muzârisini cezmeden emir LÂMI.)"},
 "tokens": [
  tok("لِيَحْضُرْ","hadara","verb",["al-amr-wa-wujuhuh","lam-amr"],
      "اللَّامُ لَامُ الْأَمْرِ جَازِمَةٌ، وَ«يَحْضُرْ» فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِهَا وَعَلَامَةُ جَزْمِهِ السُّكُونُ.",
      "«let him be present» — the LAM OF COMMAND, and its mudari jazmed by it, the sukun its sign. The request rides a letter: this is the amr's dress for the third person, where the bare sigha cannot reach.",
      "«hazır olsun» — EMİR LÂMI ve onunla meczum muzârisi; alâmeti sükûndur. Talep bir harfe biner: bu, yalın sîganın ulaşamadığı üçüncü şahıs için emrin kılığıdır.",
      segments=[seg("لِ","lam-amr","part"), seg("يَحْضُرْ","hadara","verb")]),
  tok("زَيْدٌ","zayd","propn",["al-amr-wa-wujuhuh"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Zayd» — the doer, marfu' by the plain damma: the commanded one, named in the third person.",
      "«Zeyd» — fâil; açık dammeyle merfû: üçüncü şahısta adlandırılmış emrolunan.",
      punct="!")],
 "jumal": [
  J("لِيَحْضُرْ زَيْدٌ",
    "جُمْلَةٌ فِعْلِيَّةٌ إِنْشَائِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The bab opens: a verbal insha'i clause, no mahall — and the DEFINITION rides it: amr is demanding the deed عَلَى وَجْهِ الِاسْتِعْلَاءِ, from one who counts himself above.",
    "Bâb açılıyor: fiilî inşâî cümle, mahalli yok — ve TARİF onun üzerinde: emir, fiili عَلَى وَجْهِ الِاسْتِعْلَاءِ — kendini üstün sayanın ağzından — talep etmektir."),
  J("لِيَحْضُرْ",
    "الْمُصَنِّفُ: الصِّيغَةُ — بِلَامٍ أَوْ بِغَيْرِ لَامٍ — مَوْضُوعَةٌ لِطَلَبِ الْفِعْلِ اسْتِعْلَاءً.",
    "THE MAWDU'-LAH: the scholars differed over what the sigha is COINED for; the musannif answers that with the lam or without it, the mind runs straight (سُرْعَةً) to demand-on-isti'la the moment it is heard — the speed of the understanding is his evidence.",
    "MEVZÛ'UN-LEH: âlimler sîganın NEYE konulduğunda ihtilâf etti; musannif, lâmlı yahut lâmsız, işitildiği anda zihnin SÜR'ATLE isti'lâ ile talebe gittiğini söyler — anlayışın hızı onun delilidir.")]})

# ------------------------------------------------- s2 — the bare sigha
S.append({"id": "s2", "translation": {
 "en": "Honour 'Amr! (The bare sigha — and 'Amr's silent waw drops in nasb, where the tanwin's alif already tells him from 'Umar.)",
 "tr": "Amr'a ikram et! (Yalın sîga — ve Amr'ın sessiz vâvı nasbda düşer: tenvin elifi onu Ömer'den zaten ayırır.)"},
 "tokens": [
  tok("أَكْرِمْ","akrama","verb",["al-amr-wa-wujuhuh","imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ أَنْتَ — الصِّيغَةُ بِلَا لَامٍ.",
      "«honour!» — the amr of أَكْرَمَ, MABNI on the sukun (no jazim stands anywhere), its doer the concealed «you»: the sigha without the lam, the second person's own dress.",
      "«ikram et!» — أَكْرَمَ'nin emri; sükûn üzere MEBNÎ (ortada hiçbir câzim yok); fâili gizli «sen»: lâmsız sîga, ikinci şahsın kendi kılığı."),
  tok("عَمْرًا","amr-alam","propn",["al-amr-wa-wujuhuh"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ — وَسَقَطَتْ وَاوُ عَمْرٍو هُنَا، لِأَنَّ أَلِفَ التَّنْوِينِ تَفْصِلُهُ مِنْ عُمَرَ.",
      "«'Amr» — the object, mansub by the plain fatha. And the name's SILENT WAW is gone: it is written only in raf' and jarr, to tell عَمْرو from عُمَر in an unpointed text — in nasb the tanwin's alif already does that work.",
      "«Amr'ı» — mef'ûl; açık fethayla mansub. Ve adın SESSİZ VÂVI yok: o, noktasız yazıda عَمْرو'ı عُمَر'den ayırmak için yalnız ref ve cerde yazılır — nasbda o işi tenvin elifi zaten görür.",
      punct="!")],
 "jumal": [
  J("أَكْرِمْ عَمْرًا",
    "جُمْلَةٌ فِعْلِيَّةٌ إِنْشَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The second dress: the bare sigha, mabni, its doer concealed — one word carrying the whole demand.",
    "İkinci kılık: yalın sîga, mebnî, fâili gizli — bütün talebi tek kelime taşıyor."),
  J("أَكْرِمْ عَمْرًا",
    "سُقُوطُ الْوَاوِ فِي النَّصْبِ — الرَّسْمُ يَكْتُبُ مَا يَحْتَاجُهُ فَقَطْ.",
    "THE ORTHOGRAPHIC WAJH: the script writes only what it needs. The silent waw exists to split two names the consonants confuse; where the tanwin's alif splits them already, the waw is not written — عَمْرًا, never عَمْرًوا.",
    "İMLÂ VECHİ: yazı yalnız muhtaç olduğunu yazar. Sessiz vâv, ünsüzlerin karıştırdığı iki adı ayırmak için vardır; tenvin elifi zaten ayırdığı yerde vâv yazılmaz — عَمْرًا, asla عَمْرًوا değil.")]})

# ------------------------------------------------- s3 — the ism fi'l
S.append({"id": "s3", "translation": {
 "en": "Respite Bakr! (The third dress: رُوَيْدَ, an ISM with a verb's force — it governs the nasb and conjugates nothing.)",
 "tr": "Bekir'e mühlet ver! (Üçüncü kılık: رُوَيْدَ — fiil kuvvetinde bir İSİM; nasb eder, hiç çekilmez.)"},
 "tokens": [
  tok("رُوَيْدَ","ruwayd","pron",["al-amr-wa-wujuhuh"],
      "اسْمُ فِعْلِ أَمْرٍ بِمَعْنَى أَمْهِلْ، مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ.",
      "«grant respite!» — an ISM FI'L: a noun meaning أَمْهِلْ, mabni on the fatha, its doer concealed. It has a verb's FORCE — it governs its object's nasb — and none of a verb's body: no tenses, no doer's ta, no jazim can touch it.",
      "«mühlet ver!» — bir İSM-İ FİİL: أَمْهِلْ mânâsında bir isim; fetha üzere mebnî, fâili gizli. Fiilin KUVVETİ onda vardır — mef'ûlünü nasb eder — gövdesi ise yoktur: ne çekim, ne fâil tâsı; ona hiçbir câzim dokunamaz."),
  tok("بَكْرًا","bakr","propn",["al-amr-wa-wujuhuh"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ — نَصَبَهُ اسْمُ الْفِعْلِ.",
      "«Bakr» — the object, mansub by the plain fatha — and what governed it is the NOUN before it: the proof that رُوَيْدَ carries a verb's amal.",
      "«Bekir'i» — mef'ûl; açık fethayla mansub — ve onu amel eden, önündeki İSİMdir: رُوَيْدَ'nin fiil ameli taşıdığının ispatı.",
      punct="!")],
 "jumal": [
  J("رُوَيْدَ بَكْرًا",
    "جُمْلَةٌ إِنْشَائِيَّةٌ — صَدْرُهَا اسْمٌ يَعْمَلُ عَمَلَ الْفِعْلِ.",
    "The third dress completes the musannif's roll: lam-verb, bare sigha, and now an ism doing a verb's work — three spellings, one mawdu'-lah, and the mind runs to the same demand at each.",
    "Üçüncü kılık musannifin listesini tamamlar: lâmlı fiil, yalın sîga ve şimdi fiil işi gören bir isim — üç imlâ, tek mevzû'un-leh; zihin üçünde de aynı talebe koşar."),
  J("رُوَيْدَ",
    "أَسْمَاءُ الْأَفْعَالِ — قُوَّةُ الْفِعْلِ بِلَا جِسْمِهِ.",
    "THE CLASS: asma' al-af'al (صَهْ «hush!», مَهْ «stop!», هَيْهَاتَ «how far!») — nouns coined to carry a verb's meaning and government whole, while refusing every verbal inflection. The nasb on بَكْرًا is their signature.",
    "SINIF: esmâ-i ef'âl (صَهْ «sus!», مَهْ «yeter!», هَيْهَاتَ «ne uzak!») — fiilin mânâsını ve amelini bütünüyle taşımak için konulmuş, fiil çekimlerinin hepsini reddeden isimler. بَكْرًا'daki nasb onların imzasıdır.")]})

# ------------------------------------------------- s4 — tahdid, Fussilat 41:40
S.append({"id": "s4", "translation": {
 "en": "Do what you willed. (Fussilat 41:40 — the whole choice surrendered to the hearer: not permission, THREAT.)",
 "tr": "Dilediğinizi işleyin. (Fussilet 41:40 — bütün seçim muhataba teslim: izin değil, TEHDİT.)"},
 "tokens": [
  tok("اِعْمَلُوا","amila","verb",["al-amr-wa-wujuhuh","khuruj-al-istifham"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْأَمْرُ خَارِجٌ إِلَى التَّهْدِيدِ.",
      "«do!» — the amr, mabni on the DROPPED NUN (its mudari was one of the five verbs), the waw its doer. And the command commands nothing: a commander who names no deed has stopped commanding.",
      "«işleyin!» — emir; DÜŞEN NÛN üzere mebnî (muzârisi ef'âl-i hamsedendi), vâvı fâildir. Ve buyruk hiçbir şey buyurmaz: fiil adlandırmayan buyurucu, buyurmayı bırakmıştır."),
  tok("مَا","ma-mawsula","pron",["al-amr-wa-wujuhuh","ism-mawsul"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "«what» — the relative, mabni, standing in the OBJECT SEAT the verb left open: the fourth road to definiteness, by position.",
      "«ne ki» — mevsûl; mebnî; fiilin açık bıraktığı MEF'ÛL koltuğunda: marifeliğe dördüncü yol, mevki ile."),
  tok("شِئْتُمْ","shaa","verb",["al-amr-wa-wujuhuh"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِالتَّاءِ، وَالتَّاءُ فَاعِلٌ — صِلَةُ الْمَوْصُولِ، وَالْعَائِدُ مَحْذُوفٌ: مَا شِئْتُمُوهُ.",
      "«you willed» — the sila's madi, mabni for its doer's ta; the 'aid is DROPPED (مَا شِئْتُمُوهُ) — the commonest concealment, and the surrendered choice is the whole threat.",
      "«dilediğiniz» — sılanın mâzîsi; fâil tâsı için mebnî; âid DÜŞMÜŞtür (مَا شِئْتُمُوهُ) — en yaygın gizlenme; ve teslim edilen seçim, tehdidin tamamıdır.",
      punct=".")],
 "jumal": [
  J("اِعْمَلُوا مَا شِئْتُمْ",
    "جُمْلَةٌ فِعْلِيَّةٌ إِنْشَائِيَّةٌ لَا مَحَلَّ لَهَا — وَالْأَمْرُ لِلتَّهْدِيدِ.",
    "THE WAJH: tahdid. The aya's own close is the proof — إِنَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ follows it: «He sees what you do». Freedom offered under a watching eye is a warning wearing permission's letters.",
    "VECİH: tehdit. Âyetin kendi devamı delildir — ardından إِنَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ gelir: «O, yaptıklarınızı görür». Gözetleyen bir göz altında sunulan serbestlik, izin harflerini giymiş bir uyarıdır."),
  J("مَا شِئْتُمْ",
    "صِلَةُ الْمَوْصُولِ فِي مَحَلِّ نَصْبٍ مَعَ مَوْصُولِهَا — وَالْعَائِدُ مَحْذُوفٌ.",
    "The sila-clause with its ma fills the object seat whole; the returning pronoun is dropped and the seat it left is the visible receipt — the ch15-16 'aid doctrine, here inside an amr.",
    "Sıla cümlesi, mâ'sıyla birlikte mef'ûl koltuğunu bütün doldurur; âid düşmüştür ve bıraktığı koltuk görünür makbuzdur — 15-16. bâbların âid doktrini, burada bir emrin içinde.")]})

# ------------------------------------------------- s5 — taskhir, Baqara 2:65
S.append({"id": "s5", "translation": {
 "en": "Be apes, despised! (al-Baqara 2:65 — no one can obey «become an ape»: the amr is TASKHIR, the subduing word.)",
 "tr": "Aşağılık maymunlar olun! (Bakara 2:65 — «maymun ol» emrine kimse itaat edemez: emir TESHÎRdir, boyun eğdiren söz.)"},
 "tokens": [
  tok("كُونُوا","kana","verb",["al-amr-wa-wujuhuh","kana-wa-akhawatuha"],
      "فِعْلُ أَمْرٍ نَاقِصٌ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ اسْمُهَا — وَالْأَمْرُ لِلتَّسْخِيرِ لَا لِلتَّكْلِيفِ.",
      "«be!» — kana's own amr, mabni on the dropped nun, the waw its ISM. And no one is being asked to comply: a deed no creature can perform is commanded so that it simply HAPPENS — taskhir, the word that subdues.",
      "«olun!» — kâne'nin kendi emri; düşen nûn üzere mebnî; vâv İSMİdir. Ve kimseden itaat istenmiyor: hiçbir yaratığın yapamayacağı fiil, sırf OLSUN diye buyrulur — teshîr; boyun eğdiren söz."),
  tok("قِرَدَةً","qird","noun",["al-amr-wa-wujuhuh"],
      "خَبَرُ كُونُوا مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ.",
      "«apes» — kana's khabar, mansub by the plain fatha: the broken plural of قِرْد.",
      "«maymunlar» — kâne'nin haberi; açık fethayla mansub: قِرْد'in cem-i mükesseri."),
  tok("خَاسِئِينَ","khasi","noun",["al-amr-wa-wujuhuh"],
      "خَبَرٌ ثَانٍ — أَوْ نَعْتٌ لِقِرَدَةً — مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "«despised» — a second khabar (or a na't to the apes), mansub by the YA of the sound plural: the ism fa'il of خَسَأَ, «driven off in contempt».",
      "«aşağılanmış» — ikinci haber (yahut maymunlara na't); cem-i müzekker sâlim YÂSIyla mansub: خَسَأَ'nın ism-i fâili, «hor görülüp kovulmuş».",
      punct=".")],
 "jumal": [
  J("كُونُوا قِرَدَةً خَاسِئِينَ",
    "جُمْلَةٌ فِعْلِيَّةٌ إِنْشَائِيَّةٌ — وَالْأَمْرُ لِلتَّسْخِيرِ.",
    "THE WAJH: taskhir. Its test is ABILITY — an amr whose deed lies outside the hearer's power cannot seek compliance; it manufactures the outcome. Beside it the note sets ihana (كُونُوا حِجَارَةً أَوْ حَدِيدًا) — the same shape bent to contempt.",
    "VECİH: teshîr. Ölçüsü KUDRETtir — fiili muhatabın gücünün dışında kalan emir itaat isteyemez; neticeyi imal eder. Not, yanına ihâneti koyar (كُونُوا حِجَارَةً أَوْ حَدِيدًا) — aynı kalıp, hakarete bükülmüş."),
  J("كُونُوا قِرَدَةً",
    "كَانَ لَهَا أَمْرٌ كَسَائِرِ الْأَفْعَالِ — وَاسْمُهَا الْوَاوُ وَخَبَرُهَا مَنْصُوبٌ.",
    "The nasikh conjugates like any verb: its amr keeps its government whole — the waw is its ism in raf' position and the khabar wears the nasb. One more proof that كان's sisterhood is about GOVERNMENT, not tense.",
    "Nâsih her fiil gibi çekilir: emri, amelini bütün tutar — vâv ref mevkiinde ismidir, haber nasb giyer. كان kardeşliğinin zamanla değil AMELLE ilgili olduğuna bir delil daha.")]})

# ------------------------------------------------- s6 — taswiya, Tur 52:16
S.append({"id": "s6", "translation": {
 "en": "Endure, or do not endure. (al-Tur 52:16 — the deed and its absence offered as equals: TASWIYA.)",
 "tr": "Sabredin yahut sabretmeyin. (Tûr 52:16 — fiil ve yokluğu eşit sunulmuş: TESVİYE.)"},
 "tokens": [
  tok("اِصْبِرُوا","sabara","verb",["al-amr-wa-wujuhuh"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْأَمْرُ لِلتَّسْوِيَةِ.",
      "«endure!» — the amr, mabni on the dropped nun, the waw its doer — and the next three words will unsay it.",
      "«sabredin!» — emir; düşen nûn üzere mebnî; vâvı fâil — ve sonraki üç kelime onu geri alacak."),
  tok("أَوْ","aw","conj",["al-amr-wa-wujuhuh"],
      "حَرْفُ عَطْفٍ — سَوَّى بَيْنَ الْفِعْلِ وَتَرْكِهِ.",
      "«or» — the joining letter that sets the deed and its abandonment side by side as EQUALS: the hinge of the taswiya.",
      "«yahut» — fiili ve terkini yan yana EŞİT koyan atıf harfi: tesviyenin menteşesi."),
  tok("لَا","la","part",["al-amr-wa-wujuhuh"],
      "نَاهِيَةٌ جَازِمَةٌ.",
      "«do not» — the prohibiting la, jazming what follows.",
      "«-meyin» — nehiy lâsı; ardındakini cezmeder."),
  tok("تَصْبِرُوا","sabara","verb",["al-amr-wa-wujuhuh"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.",
      "«(do not) endure» — the SAME verb back as a jazmed mudari, its nun dropped by the prohibition: command and prohibition of one deed in one breath, which is how the sentence commands nothing.",
      "«sabretmeyin» — AYNI fiil, nehiyle meczum bir muzâri olarak geri döner; nûnu düşmüş: tek nefeste bir fiilin emri ve nehyi — cümlenin hiçbir şey buyurmaması bundandır.",
      punct=".")],
 "jumal": [
  J("اِصْبِرُوا أَوْ لَا تَصْبِرُوا",
    "جُمْلَتَانِ إِنْشَائِيَّتَانِ سُوِّيَ بَيْنَهُمَا بِأَوْ — وَالْمُرَادُ: سَوَاءٌ عَلَيْكُمْ.",
    "THE WAJH: taswiya, and the receipt is fully mechanical — amr + أَوْ + لَا + the very verb just commanded. The aya's close spells the meaning out: سَوَاءٌ عَلَيْكُمْ, «it is all one for you».",
    "VECİH: tesviye; makbuz tamamen mekaniktir — emir + أَوْ + لَا + az önce emredilen fiilin kendisi. Âyetin devamı mânâyı açık yazar: سَوَاءٌ عَلَيْكُمْ, «sizin için birdir»."),
  J("لَا تَصْبِرُوا",
    "جُمْلَةُ النَّهْيِ مَعْطُوفَةٌ عَلَى جُمْلَةِ الْأَمْرِ — لَا مَحَلَّ لَهُمَا.",
    "The nahy-clause joined onto the amr-clause: the next bab's particle (لَا الْجَازِمَة) makes its first appearance INSIDE this one — the tie the source itself draws between amr and nahy.",
    "Emir cümlesine atfedilmiş nehiy cümlesi: sonraki bâbın edatı (lâ-i câzime) ilk görünüşünü bu bâbın İÇİNDE yapar — kaynağın emir ile nehiy arasında kurduğu bağ.")]})

# ------------------------------------------------- s7 — du'a, A'raf 7:151
S.append({"id": "s7", "translation": {
 "en": "My Lord, forgive me. (al-A'raf 7:151 — an amr aimed upward cannot command: DU'A.)",
 "tr": "Rabbim, beni bağışla. (A'râf 7:151 — yukarıya yöneltilmiş emir buyuramaz: DUÂ.)"},
 "tokens": [
  tok("رَبِّ","rabb","noun",["al-amr-wa-wujuhuh","vocative-munada"],
      "مُنَادَىً مُضَافٌ حُذِفَ مِنْهُ حَرْفُ النِّدَاءِ — مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَيَاءُ الْمُتَكَلِّمِ الْمَحْذُوفَةُ مُضَافٌ إِلَيْهِ وَالْكَسْرَةُ دَلِيلٌ عَلَيْهَا.",
      "«my Lord» — the TRIMMED vocative: يَا dropped, and the speaker's ya dropped too, its kasra left as the dalil. Mansub by an estimated fatha as a mudaf munada — the whole call worn down to one word, as pleas are.",
      "«Rabbim» — KISALTILMIŞ nidâ: يَا düşmüş, mütekellim yâsı da düşmüş; kesrası delil olarak kalmış. Muzâf münâdâ olarak takdîrî fethayla mansub — bütün seslenme, yakarışlarda olduğu gibi tek kelimeye inmiş."),
  tok("اغْفِرْ","ghafara","verb",["al-amr-wa-wujuhuh","imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ — وَالصِّيغَةُ خَارِجَةٌ إِلَى الدُّعَاءِ لِاسْتِحَالَةِ الِاسْتِعْلَاءِ عَلَى الرَّبِّ.",
      "«forgive» — the amr sigha, mabni on the sukun — and it cannot be a command: isti'la toward one's Lord is impossible, so the sigha decays to DU'A. Musa's word on the mountain, after the calf.",
      "«bağışla» — emir sîgası; sükûn üzere mebnî — ve emir olamaz: Rabbe karşı isti'lâ muhaldir, sîga DUÂya düşer. Mûsâ'nın dağdaki sözü, buzağıdan sonra."),
  tok("لِي","li","part",["al-amr-wa-wujuhuh"],
      "اللَّامُ حَرْفُ جَرٍّ وَالْيَاءُ ضَمِيرٌ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِاغْفِرْ.",
      "«me» — the jarr lam with the speaker's ya, hanging on the plea.",
      "«beni» — cer lâmı ile mütekellim yâsı; yakarışa asılı.",
      punct=".",
      segments=[seg("لِ","li","part"), seg("ي","pron-1s","pron")])],
 "jumal": [
  J("رَبِّ اغْفِرْ لِي",
    "جُمْلَةٌ إِنْشَائِيَّةٌ — نِدَاءٌ مَحْذُوفُ الْحَرْفِ ثُمَّ طَلَبٌ خَرَجَ إِلَى الدُّعَاءِ.",
    "THE WAJH: du'a — the receipt is the ADDRESSEE. The wujuh sort by rank: aimed above, the sigha is du'a; at an equal, iltimas («do this» between friends, no isti'la); below, and only below, true amr. One scale, three names.",
    "VECİH: duâ — makbuz MUHATAPtır. Vecihler rütbeyle ayrılır: yukarıya yönelirse sîga duâdır; denke yönelirse iltimâs («şunu yapıver» — isti'lâsız); aşağıya, yalnız aşağıya yönelirse gerçek emir. Tek terazi, üç ad."),
  J("رَبِّ",
    "حَذْفُ حَرْفِ النِّدَاءِ وَحَذْفُ الْيَاءِ — وَالْكَسْرَةُ شَاهِدَةٌ.",
    "Two drops in one word — the call-letter and the possessive ya — and the kasra stands as the witness of the second. The plea's URGENCY lives in the trimming: no time for particles.",
    "Tek kelimede iki hazif — nidâ harfi ve mütekellim yâsı — ve kesra, ikincisinin şahidi olarak durur. Yakarışın ACİLİYETİ kısaltmanın kendisindedir: edata vakit yok.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "ruwayd": g("رُوَيْدَ", None, "pron", "grant respite! (an ism fi'l: a noun with a verb's force — it governs the nasb yet never conjugates)",
             "mühlet ver! (ism-i fiil: fiil kuvvetinde bir isim — nasb eder ama asla çekilmez)", 5),
 "bakr": g("بَكْر", None, "propn", "Bakr (a man's name)", "Bekir (bir erkek adı)", 2),
 "qird": g("قِرْد", "ق ر د", "noun", "ape, monkey", "maymun", 3, plural="قِرَدَة"),
 "khasi": g("خَاسِئ", "خ س أ", "noun", "despised, driven off in contempt (ism fa'il of خَسَأَ)",
            "hor görülüp kovulmuş, aşağılık (خَسَأَ'nın ism-i fâili)", 5),
 "ghafara": g("غَفَرَ", "غ ف ر", "verb", "to forgive, cover over", "bağışlamak, örtmek", 2, form="I"),
 "amila": copy_gloss("wasiyyat-abi-hanifa-l4", "amila"),
 "sabara": copy_gloss("wasiyyat-abi-hanifa", "sabara"),
 "lam-amr": copy_gloss("wasiyyat-abi-yusuf-l5", "lam-amr"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/28.json").write_text(
    json.dumps({"chapter": 28, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 28 for c in man["chapters"]):
    man["chapters"].append({"n": 28, "title": TITLE28})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.28.0"
ADD_EN = (" Chapter 28 carries the amr bab (lines ~2158-2185, sahifa 75): اِعْمَلُوا مَا شِئْتُمْ, "
          "كُونُوا قِرَدَةً خَاسِئِينَ, اِصْبِرُوا أَوْ لَا تَصْبِرُوا and رَبِّ اغْفِرْ لِي are received "
          "Qur'anic text quoted exactly — Fussilat 41:40, al-Baqara 2:65, al-Tur 52:16 and al-A'raf "
          "7:151; لِيَحْضُرْ زَيْدٌ, أَكْرِمْ عَمْرًا and رُوَيْدَ بَكْرًا are the source's own worked "
          "examples verbatim, Ottoman plain-alif normalized to standard orthography — a recorded "
          "normalization.")
ADD_TR = (" Yirmi sekizinci bâb, emir bâbını taşır (satır ~2158-2185, sahife 75): اِعْمَلُوا مَا "
          "شِئْتُمْ, كُونُوا قِرَدَةً خَاسِئِينَ, اِصْبِرُوا أَوْ لَا تَصْبِرُوا ve رَبِّ اغْفِرْ لِي "
          "aynen alınmış mervî Kur'ân metnidir — Fussilet 41:40, Bakara 2:65, Tûr 52:16 ve A'râf "
          "7:151; لِيَحْضُرْ زَيْدٌ, أَكْرِمْ عَمْرًا ve رُوَيْدَ بَكْرًا kaynağın kendi işlenmiş "
          "örneklerinin aynen alınmışıdır; Osmanlı düz-elif imlâsı standart imlâya çevrilmiştir — "
          "kayıtlı bir normalizasyondur.")
if "2158-2185" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "ghafara" not in mo["verbs"]:
    mo["verbs"]["ghafara"] = _sg.sound1(
        "daraba", "غَفَر", "غْفِر", "اِغْفِر", "غُفْرَان", "غَافِر",
        "مَغْفُور", "غُفِرَ", "يُغْفَرُ")
if "amila" not in mo["verbs"]:
    mo["verbs"]["amila"] = copy_verb("wasiyyat-abi-hanifa-l4", "amila")
if "sabara" not in mo["verbs"]:
    mo["verbs"]["sabara"] = copy_verb("wasiyyat-abi-hanifa", "sabara")
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch28:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD), "; morph + ghafara, amila(copy), sabara(copy)")
