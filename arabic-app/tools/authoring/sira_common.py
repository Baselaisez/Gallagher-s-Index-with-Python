"""sira_common — the kit of the ONE package `al-sira-al-nabawiyya-nadwi` (v359-S): al-Nadwī's «السيرة النبوية», one story in parts.

THE BOOK: Abū al-Ḥasan ʿAlī al-Ḥasanī al-Nadwī (1333–1420 AH), «السيرة النبوية», Dār Ibn Kathīr, Damascus–Beirut, 12th ed. 2004,
767 pp., with notes by Sayyid ʿAbd al-Mājid al-Ghawrī (Shamela 9914; research/sources/al-sira-al-nabawiyya-nadwi-src.txt, built by
tools/authoring/sira_src.py). The owner (2026-11-27): «This is a new story (make it ONE story with many parts; do not cut it into
different stories)» and «I do have the permission of al-Nadwī. And al-Nadwī bestowed all his Arabic teaching materials of this kind on
the whole Islamic world; his family holds no copyright.» — recorded in the attribution in his words (PERMISSION_*).

ONE PACKAGE, CHAPTERS APPENDED IN PARTS. tools/authoring/author_al_sira_al_nabawiyya_nadwi.py is the package's source of truth: it
imports the chapter modules `sira_ch<N>.py` listed in CHAPTER_IDS (in the book's order) and calls `finish()`. THE CHAPTER-ID SCHEME
(decided in v359-S, append-only — saved progress, the teacher's verdicts and the audit key on package:chapter:sentence:token):
  * chapters 1–100 are RESERVED for what precedes the Prophet's life in the book: al-Nadwī's own preface(s) and «الفصل الأول: مدخل إلى
    السيرة النبوية» (about forty headed sections). They are not authored yet; when they are, they take 1, 2, 3 … in the book's order.
  * chapter 101 is the first paragraph of «الفصل الثاني: من الولادة الكريمة إلى البعثة العظيمة», and every later chapter takes the
    next number, in the book's order, with no gap: a later wave APPENDS (102, 103 … then Faṣl 3 …) and never renumbers.
  * one chapter = one of al-Nadwī's own headed sections; a long section is cut at a paragraph into parts that keep its heading
    («… (٢)»). The square-bracketed headings of the print are the editor's (his preface: «بين المعقوفتين») and are not shown.
CHAPTER_IDS is the ledger; `finish()` refuses a chapter list that does not extend it, and the smoke check «v359 — al-Nadwī's Sīra is
ONE story» pins the same ledger.

RULES (v333, carried, and the brief's): only al-Nadwī's own text is authored — the editor's footnotes, his lineage tree (Shamela pp.
146–148) and his bracketed headings are another man's work and are never shown; the text is never retold, re-ordered or silently
corrected; the e-text's received marks (it carries only the shadda) are KEPT, every other vowel is ours and declared; a vowel not
certain from the lexicon and the grammar is left unwritten and listed for the hoca; Qurʾān and ḥadīth quoted inside stay as printed
(letters and received marks), honorifics as printed.
"""
import pathlib, sys, json, re, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from khasais_common import *          # noqa: F401,F403 — tok, seg, X, SEN, NOTE, NN/NV/NP, the house wordings …
from amthal_common import finish as _finish, ROOT, OUT_ROOT, N, PRON, PRON_AR

SLUG = "al-sira-al-nabawiyya-nadwi"
SRC = ROOT / "research/sources/al-sira-al-nabawiyya-nadwi-src.txt"
FIRST_LIFE = 101                         # chapters 1–100 reserved for the preface and Faṣl 1

# THE LEDGER — append-only. (n, the heading in the print's letters, the Shamela page the chapter opens on)
CHAPTER_IDS = [
    (101, "من الولادة الكريمة إلى البعثة العظيمة", 149),
    (102, "ولادته الكريمة ونسبه الزكي", 149),
    (103, "ولادته الكريمة ونسبه الزكي", 150),
    (104, "ولادته الكريمة ونسبه الزكي", 151),
    (105, "ولادته الكريمة ونسبه الزكي", 152),
    (106, "ولادته الكريمة ونسبه الزكي", 154),
    (107, "وفاة عبد الله وآمنة وعبد المطلب وكفالة أبي طالب", 154),
    (108, "وفاة عبد الله وآمنة وعبد المطلب وكفالة أبي طالب", 155),
    (109, "قصة الراهب بحيرى", 156),
    (110, "قصة الراهب بحيرى", 156),
    (111, "قصة الراهب بحيرى", 157),
    (112, "قصة الراهب بحيرى", 157),
]

PERMISSION_EN = ("PERMISSION — the project owner's statement, in his words (2026-11-27): «I do have the permission of al-Nadwī. And "
                 "al-Nadwī bestowed all his Arabic teaching materials of this kind on the whole Islamic world; his family holds no copyright.» ")
PERMISSION_TR = ("İZİN — proje sahibinin kendi sözleriyle beyanı (2026-11-27): «I do have the permission of al-Nadwī. And al-Nadwī bestowed "
                 "all his Arabic teaching materials of this kind on the whole Islamic world; his family holds no copyright.» (Türkçesi: «Nedvî'nin "
                 "iznine sahibim. Nedvî bu türden bütün Arapça öğretim malzemesini bütün İslâm âlemine bağışlamıştır; ailesinin telif hakkı yoktur.») ")
PERMISSION_AR = ("الْإِذْنُ: قَالَ صَاحِبُ الْمَشْرُوعِ (٢٠٢٦-١١-٢٧) بِلَفْظِهِ: «I do have the permission of al-Nadwī. And al-Nadwī bestowed all his "
                 "Arabic teaching materials of this kind on the whole Islamic world; his family holds no copyright.» ")

# ---- the source: al-Nadwī's matn, page by page --------------------------------------------------------------------------
_HDR = re.compile(r"=== p\. (\d+) \((\d+)\)(?: \[(.*)\])? ===")
def matn_pages():
    """{shamela page: (printed page, [paragraphs of the matn])} — footnote markers «N» dropped, the hashiya never read"""
    P, cur, inh = {}, None, False
    for l in SRC.read_text(encoding="utf-8").split("\n"):
        m = _HDR.match(l)
        if m: cur = int(m.group(1)); P[cur] = (m.group(2), []); inh = False; continue
        if cur is None or not l.strip() or l.startswith("#"): continue
        if l.startswith("--- hashiya"): inh = True; continue
        if not inh: P[cur][1].append(re.sub(r"\s*«[٠-٩]+»\s*", " ", l).strip())
    return P

def fold(s):
    """letters only — the guard's fold (vowels, shadda, tatweel, punctuation, digits and spaces dropped; alif/hamza seats kept apart)"""
    s = unicodedata.normalize("NFC", s)
    return re.sub("[^ء-ي]", "", re.sub("[ً-ْٰـ]", "", s))

def received_shadda_ok(token_full, src_word):
    """every shadda the print sets on a letter is on the same letter of the token"""
    def units(w):
        out = []
        for ch in unicodedata.normalize("NFD", w):
            if "ء" <= ch <= "ي": out.append([ch, ""])
            elif ch in "ًٌٍَُِّْٰ" and out: out[-1][1] += ch
        return out
    a, b = units(token_full), units(src_word)
    if [x[0] for x in a] != [x[0] for x in b]: return False
    return all(("ّ" not in y[1]) or ("ّ" in x[1]) for x, y in zip(a, b))

def guard(CHAPS):
    """each sentence's letters a substring of the matn of the pages its chapter spans (vowels stripped), and every received shadda
    kept — the same proof the smoke check makes on the built package"""
    P = matn_pages()
    text = " ".join(" ".join(P[p][1]) for p in sorted(P))
    F = fold(text)
    words = [w for w in re.split(r"[\s\-–—«»\"()\[\]،؛:.!؟?,]+", text) if fold(w)]
    W = {}
    for w in words: W.setdefault(fold(w), set()).add(w)
    bad = []
    for n, S in CHAPS:
        for s in S:
            L = fold("".join(t["surface"]["full"] + t.get("punctAfter", "") for t in s["tokens"]))
            if L not in F: bad.append((n, s["id"], "letters"))
            for t in s["tokens"]:
                f = fold(t["surface"]["full"])
                cands = W.get(f, set())
                if not cands: bad.append((n, s["id"], "word not in the matn: " + t["surface"]["full"])); continue
                if not any(received_shadda_ok(t["surface"]["full"], w) for w in cands):
                    bad.append((n, s["id"], "received shadda dropped: " + t["surface"]["full"] + " / " + "|".join(sorted(cands))))
    assert not bad, bad
    return True

# ---- the shelf's own helpers ----------------------------------------------------------------------------------------------
def SAW(p=None, wa_hal=False):
    """«صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ» after the Prophet's name — four tokens, a prayer set in the sentence with no seat of its own"""
    J = " — وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ"
    return [
     tok("صَلَّى", "salla", "verb", ["form-ii-verbs", "naqis-verbs", "jumla-mutarida"],
         "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الْمُقَدَّرِ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، لَفْظُهُ خَبَرٌ وَمَعْنَاهُ الدُّعَاءُ" + J + ".",
         "«may (Allah) bless» — a past verb built on an estimated fatha (on the alif); a statement in form, a prayer in meaning; the prayer is set in the sentence and has no seat.",
         "«salât etsin» — elif üzerinde takdîrî fetha ile mebnî mâzî; lafzı haber, anlamı duâdır; duâ cümlesi ara cümledir, i'râbdan mahalli yoktur."),
     tok("اللهُ", "allah", "propn", ["fail"], "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Allah» — the doer, in raf'.", "«Allah» — lafza-i celâl, fâil, merfû."),
     X("عَلَيْهِ", "ala", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
       "حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى النَّبِيِّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«صَلَّى».",
       "«upon him» — a jarr letter with the pronoun (the Prophet) in the seat of jarr; the phrase hangs on «bless».",
       "«onun üzerine» — cer harfi; zamir (Peygamber'e döner) mahallen mecrûr; câr-mecrûr «sallâ»ya müteallik.", enc="هِ"),
     X("وَسَلَّمَ", "sallama", "verb", ["atf-nasaq", "form-ii-verbs"],
       "الْوَاوُ عَاطِفَةٌ، وَسَلَّمَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى اللهِ — وَالْجُمْلَةُ مُعْتَرِضَةٌ مِثْلُ «صَلَّى» الْمَعْطُوفَةِ عَلَيْهَا، لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
       "The waw conjoins; «and grant (him) peace» — a past verb built on fatha; its doer is the hidden «He» (Allah); conjoined to «bless», the clause is part of the same parenthesis and has no seat.",
       "Vâv atıf; «ve selâm versin» — fetha üzere mebnî mâzî; fâili gizli «hüve» (Allah); «sallâ»ya ma'tûf olup onun gibi ara cümledir, i'râbdan mahalli yoktur.", p=p, pre=("wa",))]

def QUOTE(toks, kind="hadith"):
    """a quoted saying: the print's «…»; the first token tagged as received speech"""
    toks[0]["quoteBefore"] = "«"; toks[-1]["quoteAfter"] = "»"
    toks[0].setdefault("grammar", []).insert(0, "al-iqtibas-wal-tadmin")
    return toks

LEVEL = 5
SOURCE_AR = "«السِّيرَةُ النَّبَوِيَّةُ» لِأَبِي الْحَسَنِ عَلِيٍّ الْحَسَنِيِّ النَّدْوِيِّ (١٣٣٣–١٤٢٠ هـ)، دَارُ ابْنِ كَثِيرٍ، ط ١٢، ٢٠٠٤ (الشَّامِلَةُ ٩٩١٤)"
SOURCE_EN = ("«al-Sīra al-Nabawiyya» by Abū al-Ḥasan ʿAlī al-Ḥasanī al-Nadwī (1333–1420 AH), Dār Ibn Kathīr, Damascus–Beirut, 12th ed. 2004, "
             "767 pp., with notes by Sayyid ʿAbd al-Mājid al-Ghawrī (Shamela book 9914)")
SOURCE_TR = ("Ebü'l-Hasan Ali el-Hasenî en-Nedvî'nin (1333–1420) «es-Sîretü'n-Nebeviyye» adlı eseri (Dâru İbn Kesîr, Dımaşk–Beyrut, 12. bs., "
             "2004, 767 s.; Seyyid Abdülmâcid el-Gavrî'nin notlarıyla; Şâmile kitap 9914)")

def manifest(chapters_meta, hoca=(), left=(), extra=("", "", "")):
    """the package's manifest: the RECEIVED-text attribution in three languages, the parts read so far (each chapter with its printed
    pages), the chapter-id scheme, what is left out and why, the vowelling, the points left for the hoca and the owner's permission"""
    K = len(chapters_meta)
    last = chapters_meta[-1]
    parts_en = "; ".join(f"ch. {m['n']} «{m['title']['ar']}» (printed pp. {m['pages']}): {m['en']}" for m in chapters_meta)
    parts_tr = "; ".join(f"Bölüm {m['n']} «{m['title']['ar']}» (matbû s. {m['pages']}): {m['tr']}" for m in chapters_meta)
    parts_ar = "؛ ".join(f"الْفَصْلُ {m['n']} «{m['title']['ar']}» (ص {m['pages']})" for m in chapters_meta)
    hz_en = ("LEFT FOR THE SCHOLAR: " + "; ".join(h[0] for h in hoca) + ". ") if hoca else ""
    hz_tr = ("HOCAYA BIRAKILANLAR: " + "; ".join(h[1] for h in hoca) + ". ") if hoca else ""
    hz_ar = ("وَتُرِكَ لِلْعَالِمِ الْمُرَاجِعِ " + str(len(hoca)) + " مَوَاضِعَ مَذْكُورَةٌ فِي الْإِنْكِلِيزِيَّةِ وَالتُّرْكِيَّةِ. ") if hoca else ""
    lf_en = ("LEFT OUT INSIDE THE SPAN, each declared: " + "; ".join(x[0] for x in left) + ". ") if left else ""
    lf_tr = ("ARALIKTA ALINMAYANLAR (her biri bildirilerek): " + "; ".join(x[1] for x in left) + ". ") if left else ""
    return {
     "id": SLUG, "storyGroup": SLUG,
     "title": {"ar": "السِّيرَةُ النَّبَوِيَّةُ", "en": "The Life of the Prophet (al-Nadwī)", "tr": "Siyer-i Nebî (Nedvî)"},
     "subtitle": {"ar": "لِأَبِي الْحَسَنِ عَلِيٍّ الْحَسَنِيِّ النَّدْوِيِّ",
                  "en": "Abū al-Ḥasan ʿAlī al-Nadwī's Sīra, in parts — the first part: from the noble birth onward",
                  "tr": "Ebü'l-Hasan Ali en-Nedvî'nin Siyer'i, kısım kısım — ilk kısım: mübarek doğumdan itibaren"},
     "level": LEVEL, "levelName": "Advanced", "version": "0.1.0", "published": "2026-11-27", "access": "free",
     "attribution": {
      "en": ("The RECEIVED text, verbatim — al-Nadwī's own prose — from " + SOURCE_EN + ". The whole e-text is research/sources/"
             "al-sira-al-nabawiyya-nadwi-src.txt (built by tools/authoring/sira_src.py). ONE STORY IN PARTS: this package is the whole book "
             "as one story, read in instalments; it now holds " + str(K) + " chapters from «الفصل الثاني: من الولادة الكريمة إلى البعثة العظيمة» "
             "(printed pp. 157–" + last["pages"].split("–")[-1] + "), and the story continues in later parts in the book's order. CHAPTER NUMBERS: "
             "chapters 1–100 are reserved for al-Nadwī's preface and «الفصل الأول: مدخل إلى السيرة النبوية» (the world before Islam), not yet "
             "read; the Prophet's life begins at chapter 101 and each later section takes the next number, so a chapter's number never changes. "
             "Each chapter is one of al-Nadwī's own headed sections (a long one cut at a paragraph keeps its heading with a part number). The parts "
             "read so far: " + parts_en + ". ONLY al-Nadwī's text is here: the editor's footnotes, his lineage tree (printed pp. 154–156, «من إضافات "
             "المحقق») and his square-bracketed headings are another man's work and are left out. VOWELLING: the e-text carries only the shadda, "
             "which is kept wherever it stands; EVERY other vowel is ours (editorial), as is the division of the print's long sentences at its own "
             "pauses (no word moved); a vowel we could not settle is left unwritten and listed below. Qurʾān and ḥadīth quoted inside keep the "
             "print's letters; the honorifics are as printed. NO correction was made to the text. " + lf_en + extra[0] + hz_en + PERMISSION_EN +
             "The English and Turkish translations and every iʿrāb line are ours; the whole awaits a scholar's review."),
      "tr": ("LAFZIYLA AKTARILAN metin — Nedvî'nin kendi nesri: " + SOURCE_TR + ". Elektronik metnin tamamı research/sources/"
             "al-sira-al-nabawiyya-nadwi-src.txt dosyasındadır (tools/authoring/sira_src.py ile kuruldu). KISIM KISIM TEK HİKÂYE: bu paket kitabın "
             "tamamıdır, tek hikâye olarak bölüm bölüm okunur; şimdi «الفصل الثاني: من الولادة الكريمة إلى البعثة العظيمة» faslından " + str(K) +
             " bölüm içerir (matbû s. 157–" + last["pages"].split("–")[-1] + ") ve hikâye kitabın sırasıyla sonraki kısımlarda devam eder. BÖLÜM "
             "NUMARALARI: 1–100 arası Nedvî'nin mukaddimesine ve «الفصل الأول: مدخل إلى السيرة النبوية» faslına (İslâm'dan önceki dünya) ayrılmıştır, "
             "henüz okunmadı; Peygamber'in hayatı 101. bölümle başlar ve sonraki her kısım bir sonraki numarayı alır; bir bölümün numarası hiç "
             "değişmez. Her bölüm Nedvî'nin kendi başlıklı kısımlarından biridir (uzun olan bir paragrafta bölünür, başlığını kısım numarasıyla "
             "korur). Şimdiye kadar okunanlar: " + parts_tr + ". Burada YALNIZCA Nedvî'nin metni vardır: muhakkikin dipnotları, nesep ağacı (matbû "
             "s. 154–156, «من إضافات المحقق») ve köşeli parantezli başlıkları başka birinin emeğidir ve alınmamıştır. HAREKE: elektronik metin yalnız "
             "şeddeyi taşır; şedde bulunduğu her yerde korunmuştur; diğer HER hareke bize aittir (editoryal); baskının uzun cümlelerinin kendi "
             "duraklarında bölünmesi de öyle (hiçbir kelimenin yeri değişmedi); kesinleştiremediğimiz hareke yazılmamış ve aşağıda sayılmıştır. "
             "İçinde geçen âyet ve hadisler baskının harfleriyle, salavat baskıdaki gibidir. Metinde HİÇBİR düzeltme yapılmamıştır. " + lf_tr +
             extra[1] + hz_tr + PERMISSION_TR + "İngilizce ve Türkçe tercümeler ile bütün i'râb satırları bize aittir; metnin tamamı bir âlimin "
             "incelemesini beklemektedir."),
      "ar": ("نَصٌّ مَنْقُولٌ بِلَفْظِهِ مِنْ " + SOURCE_AR + "، قِصَّةٌ وَاحِدَةٌ تُقْرَأُ أَجْزَاءً، وَهٰذَا أَوَّلُهَا: مِنَ «الْفَصْلِ الثَّانِي: مِنَ الْوِلَادَةِ "
             "الْكَرِيمَةِ إِلَى الْبَعْثَةِ الْعَظِيمَةِ»: " + parts_ar + "؛ وَتَتْلُوهُ الْأَجْزَاءُ عَلَى تَرْتِيبِ الْكِتَابِ. وَالْفُصُولُ مِنْ ١ إِلَى ١٠٠ مَحْفُوظَةٌ "
             "لِمُقَدِّمَةِ الْمُؤَلِّفِ وَلِلْفَصْلِ الْأَوَّلِ. وَلَيْسَ هُنَا إِلَّا كَلَامُ النَّدْوِيِّ، وَتُرِكَتْ حَوَاشِي الْمُحَقِّقِ وَشَجَرَتُهُ وَعَنَاوِينُهُ الَّتِي بَيْنَ "
             "الْمَعْقُوفَتَيْنِ. الضَّبْطُ: لَيْسَ فِي النَّصِّ الْإِلِكْتُرُونِيِّ مِنَ الشَّكْلِ إِلَّا الشَّدَّةُ فَأُبْقِيَتْ، وَكُلُّ حَرَكَةٍ غَيْرُهَا مِنْ ضَبْطِنَا نَحْنُ؛ وَمَا "
             "لَمْ نَقْطَعْ بِضَبْطِهِ تُرِكَتْ حَرَكَتُهُ غَيْرَ مَكْتُوبَةٍ. وَلَمْ يُصَحَّحْ فِي النَّصِّ شَيْءٌ. " + extra[2] + hz_ar + PERMISSION_AR +
             "وَالتَّرْجَمَتَانِ الْإِنْكِلِيزِيَّةُ وَالتُّرْكِيَّةُ وَالْإِعْرَابُ مِنْ عَمَلِنَا، وَالنَّصُّ كُلُّهُ يَنْتَظِرُ مُرَاجَعَةَ الْعَالِمِ."),
      "reviewStatus": REVIEW,
     },
    }

def finish(CHAPS, metas, NEW_GLOSS, MANIFEST, **kw):
    """write the package: chapters numbered from 101 by the ledger, glossary and morphology by the proverbs' finish (every key by
    lemma identity on the shelf, every new key checked free), then the chapter files renamed to their ledger numbers"""
    ns = [n for n, S in CHAPS]
    assert ns == [x[0] for x in CHAPTER_IDS[:len(ns)]], ("the chapters must be the ledger's prefix, in order", ns)
    assert ns == list(range(FIRST_LIFE, FIRST_LIFE + len(ns))), ("no gap after 101", ns)
    for (n, S), m in zip(CHAPS, metas):
        led = dict((x[0], x) for x in CHAPTER_IDS)[n]
        assert fold(m["title"]["ar"]) == fold(led[1]), ("the heading is the ledger's", n, m["title"]["ar"])
    guard(CHAPS)
    TITLES = [m["title"] for m in metas]
    PKG = _finish(SLUG, TITLES, [S for n, S in CHAPS], NEW_GLOSS, MANIFEST, **kw)
    man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
    for i, (n, S) in enumerate(CHAPS, 1):
        (PKG / f"chapters/{i}.json").rename(PKG / f"chapters/tmp{n}.json")
    for n, S in CHAPS:
        f = PKG / f"chapters/tmp{n}.json"
        d = json.loads(f.read_text(encoding="utf-8")); d["chapter"] = n
        (PKG / f"chapters/{n}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8"); f.unlink()
    man["chapters"] = [{"n": n, "title": t} for (n, S), t in zip(CHAPS, TITLES)]
    (PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
    return PKG

def T(full, lex, pos, g, ar, en, tr, p=None, pre=(), enc=None, s=None, spos=None, segs=None):
    """one token (khasais_common.X) — or with its segments given whole (`segs`: [(form, lex, pos), …]) for shapes X does not cut"""
    if segs:
        return tok(full, lex, pos, g, ar, en, tr, punct=p, segments=[seg(*x) for x in segs])
    return X(full, lex, pos, g, ar, en, tr, p=p, pre=pre, enc=enc, s=s, spos=spos)

def VW(full, lex, g, ar, en, tr, p=None, pre=None):
    """a past verb with the waw of the group (كَانُوا، زَهِدُوا): the house cut — stem + «ا» (pron-3mp); `pre` a fused وَ / فَ"""
    rest, segs = N(full), []
    if pre: segs.append((pre[0], pre[1], "conj")); rest = rest[len(pre[0]):]
    segs += [(rest[:-1], lex, "verb"), ("ا", "pron-3mp", "pron")]
    return T(full, lex, "verb", g, ar, en, tr, p=p, segs=segs)

def Q(toks, kind="hadith"):
    """the print's quotation marks «…» round a span (a quoted saying or the print's own marks round a name)"""
    toks[0]["quoteBefore"] = "«"; toks[-1]["quoteAfter"] = "»"
    if kind in ("hadith", "quran"): toks[0].setdefault("grammar", []).insert(0, "al-iqtibas-wal-tadmin")
    return toks

# ---- helpers shared by the chapter modules (from ch104/105, v359-S round 2) ------------------------------------------------
J = lambda s: "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ " + s
D = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}
CE = {"raf": "raf'", "nasb": "nasb", "jarr": "jarr"}; CT = {"raf": "merfû", "nasb": "mansûb", "jarr": "mecrûr"}
def NA(full, lex, of, case, en, tr, p=None, g=()):
    return T(full, lex, "noun", ["naat-sifa", *g], "نَعْتٌ لِـ«" + of + "» " + D[case] + ".", "An adjective of «" + en[0] + "», in " + CE[case] + ": «" + en[1] + "».", "«" + tr[0] + "»nin na'tı, " + CT[case] + ": «" + tr[1] + "».", p=p)
def MI(full, lex, en, tr, p=None, g=(), note=("", "", "")):
    return T(full, lex, "noun", ["idafa-definiteness", *g], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ" + note[0] + ".", "The second term of the idafa, in jarr: «" + en + "»" + note[1] + ".", "Muzâfun ileyh, mecrûr: «" + tr + "»" + note[2] + ".", p=p)
def P_(full, lex="fi", en="in", tr="-de"):
    return T(full, lex, "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "A jarr letter: «" + en + "».", "Cer harfi: «" + tr + "».")
def MJ(full, lex, by, hang, en, tr, p=None, g=(), mudaf=False, enc=None, extra=("", "", "")):
    m = ("، مُضَافٌ", ", annexed", ", muzâf") if mudaf else ("", "", "")
    if enc:
        m = ("، مُضَافٌ، وَ" + PRON_AR.get(enc, enc) + " ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + extra[0], ", annexed to the pronoun" + extra[1], ", muzâf; zamir muzâfun ileyh" + extra[2])
    return T(full, lex, "noun", ["huruf-jarr", *g], "مَجْرُورٌ بِـ«" + by + "» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ" + m[0] + J(hang[0]) + ".", "In jarr after " + by + m[1] + " — the phrase hangs on " + hang[1] + ": «" + en + "».",
             "«" + tr[1] + "» ile mecrûr" + m[2] + " — câr-mecrûr " + hang[2] + " müteallik: «" + tr[0] + "».", p=p, enc=enc)
def JP(full, lex, enc, hang, who, en, tr, p=None):
    """a jarr letter with an attached pronoun, hanging on a verb"""
    return T(full, lex, "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "حَرْفُ جَرٍّ، وَ" + PRON_AR.get(enc, enc) + " ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى " + who[0] + J("بِـ«" + hang[0] + "»") + ".",
             "A jarr letter with «" + who[1] + "» — the phrase hangs on «" + hang[1] + "»: «" + en + "».", "Cer harfi; zamir (" + who[2] + ") mahallen mecrûr — câr-mecrûr «" + hang[2] + "»e müteallik: «" + tr + "».", p=p, enc=enc)
