# -*- coding: utf-8 -*-
"""The Qiṣaṣ al-Nabiyyīn authoring shim: talkhis_common with its package switched to content/samples/qisas-al-nabiyyin-1,
and the package bootstrapped (manifest, empty glossary and morphology) when it does not exist yet. The text is Abū
al-Ḥasan ʿAlī al-Nadwī's graded reader for children, transcribed page by page from the Karachi scan the project owner
supplied (research/sources/qisas-al-nabiyyin-nadwi-leveling-notes.txt documents the edition). RIGHTS: the work is in
copyright (Nadwī d. 1999) — the manifest says so, and the package must not be distributed without the rights holder's
permission. Everything is pending-scholarly-review."""
import json, os, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import talkhis_common as _tc
_tc.PKG = pathlib.Path(os.environ["DRY_PKG"]) if os.environ.get("DRY_PKG") else _tc.ROOT / "content/samples/qisas-al-nabiyyin-1"
if os.environ.get("DRY_GR"): _tc.GR = pathlib.Path(os.environ["DRY_GR"])
from talkhis_common import *
PKG = _tc.PKG

MANIFEST = {
 "id": "qisas-al-nabiyyin-1",
 "storyGroup": "qisas-al-nabiyyin",
 "title": {"ar": "قِصَصُ النَّبِيِّينَ — الْجُزْءُ الْأَوَّلُ", "en": "Stories of the Prophets — Part One", "tr": "Peygamber Kıssaları — Birinci Cüz"},
 "subtitle": {"ar": "مَنْ كَسَرَ الْأَصْنَامَ؟ — قِصَّةُ إِبْرَاهِيمَ لِلْأَطْفَالِ، بِقَلَمِ أَبِي الْحَسَنِ النَّدْوِيِّ",
              "en": "Who broke the idols? — the story of Ibrāhīm for children, by Abū al-Ḥasan al-Nadwī",
              "tr": "Putları kim kırdı? — çocuklar için İbrâhim kıssası, Ebü'l-Hasen en-Nedvî'nin kaleminden"},
 "level": 1, "levelName": "Newbie", "access": "premium", "published": "2026-10-01", "version": "0.1.0",
 "chapters": [],
 "attribution": {
  "ar": "قِصَصُ النَّبِيِّينَ لِلْأَطْفَالِ، الْجُزْءُ الْأَوَّلُ، لِأَبِي الْحَسَنِ عَلِيٍّ الْحَسَنِيِّ النَّدْوِيِّ (ت 1420هـ/1999م). النَّصُّ مَنْقُولٌ صَفْحَةً صَفْحَةً مِنْ طَبْعَةِ كَرَاتْشِي (مَجْلِسُ نَشْرِيَّاتِ إِسْلَام)، بِضَبْطِهَا. الْحُقُوقُ مَحْفُوظَةٌ لِأَصْحَابِهَا؛ لَا يُنْشَرُ هٰذَا النَّصُّ إِلَّا بِإِذْنِهِمْ.",
  "en": "Qiṣaṣ al-Nabiyyīn li-l-aṭfāl, Part One, by Abū al-Ḥasan ʿAlī al-Ḥasanī al-Nadwī (d. 1999). The Arabic is transcribed page by page, with its printed vowelling, from the Karachi edition (Majlis Nashriyāt-i Islām) the project owner supplied; the section numbers and titles are the book's. RIGHTS: the work is in copyright and this package is a study build — it must not be distributed without the rights holder's permission. The i'rab, the glossary and the translations are the app's own.",
  "tr": "Kısasü'n-Nebiyyîn li'l-etfâl, Birinci Cüz, Ebü'l-Hasen Ali el-Hasenî en-Nedvî (ö. 1999). Arapça metin, proje sahibinin verdiği Karaçi baskısından (Meclis-i Neşriyât-ı İslâm) sayfa sayfa, basılı harekesiyle aktarılmıştır; bölüm numaraları ve başlıkları kitabındır. HAKLAR: eser telif altındadır ve bu paket bir çalışma sürümüdür — hak sahibinin izni olmadan dağıtılamaz. İ'râb, sözlük ve çeviriler uygulamanındır.",
  "reviewStatus": "pending-scholarly-review"
 }
}
def bootstrap():
    (PKG / "chapters").mkdir(parents=True, exist_ok=True)
    if not (PKG / "manifest.json").exists(): (PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
    if not (PKG / "glossary.json").exists(): (PKG / "glossary.json").write_text(json.dumps({"entries": {}}, ensure_ascii=False, indent=1), encoding="utf-8")
    if not (PKG / "morphology.json").exists(): (PKG / "morphology.json").write_text(json.dumps({"verbs": {}}, ensure_ascii=False, indent=1), encoding="utf-8")
bootstrap()

def pr(form, lex): return seg(form, lex, "pron")
def wa_(form, lex, pos): return [seg("وَ", "wa", "conj"), seg(form, lex, pos)]

# ---------------------------------------------------------------- the Level-1 reader's token helpers (shared by chapter 3 onward;
# chapters 1–2 carry their own copies — written once there, lifted here unchanged)
K = "kana-wa-akhawatuha"
def W(wa): return ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "")
def Wen(wa): return ("«and» + " if wa else "")
def Wtr(wa): return ("«ve» + " if wa else "")
def qala(full="قَالَ", punct=":", wa=False, hidden=None, tags=()):
    ar = W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}" if hidden else "") + " — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ."
    return tok(full, "qala", "verb", ["hollow-verbs", "maful-bihi"] + list(tags), ar, Wen(wa) + "«said» — a māḍī built on fatḥa; what is said is its object.", Wtr(wa) + "«dedi» — fetha üzere mebnî mâzî; söylenen söz mef'ûlüdür.", punct=punct, segments=(wa_(full[2:], "qala", "verb") if wa else None))
def qalu(full="قَالُوا", punct=":", wa=False, tags=()):
    return tok(full, "qala", "verb", ["hollow-verbs", "maful-bihi"] + list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ.", Wen(wa) + "«they said» — a māḍī built on ḍamma before the group's wāw; the wāw is the doer.", Wtr(wa) + "«dediler» — cemi vâvı sebebiyle zamme üzere mebnî mâzî; vâv fâildir.", punct=punct, segments=(wa_(full[2:], "qala", "verb") if wa else None))
def mazi(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, wa=False, extra_ar=""):
    ar = W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}" if hidden else "") + extra_ar + "."
    return tok(full, lex, "verb", list(tags), ar, Wen(wa) + en + (" — a māḍī built on fatḥa; the doer is the concealed pronoun." if hidden else " — a māḍī built on fatḥa."), Wtr(wa) + tr + (" — fetha üzere mebnî mâzî; fâil gizli zamirdir." if hidden else " — fetha üzere mebnî mâzî."), punct=punct, segments=(wa_(full[2:], lex, "verb") if wa else None))
def mazi_pl(full, lex, en, tr, tags=(), punct=None, wa=False):
    return tok(full, lex, "verb", list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ.", Wen(wa) + en + " — a māḍī built on ḍamma before the group's wāw; the wāw is the doer.", Wtr(wa) + tr + " — cemi vâvı ile zamme üzere mebnî mâzî; vâv fâildir.", punct=punct, segments=(wa_(full[2:], lex, "verb") if wa else None))
def mazi_ta(full, lex, en, tr, tags=(), punct=None, wa=False, extra=""):
    return tok(full, lex, "verb", list(tags), W(wa) + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ" + extra + ".", Wen(wa) + en + " — a māḍī built on fatḥa; the tāʾ marks the feminine.", Wtr(wa) + tr + " — fetha üzere mebnî mâzî; tâ te'nis içindir.", punct=punct, segments=(wa_(full[2:], lex, "verb") if wa else None))
def fail(full, lex, en, tr, tags=(), punct=None, extra_ar=""):
    return tok(full, lex, "noun", ["fail"] + list(tags), "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ" + extra_ar + ".", en + " — the doer, rafʿ by ḍamma.", tr + " — fâil, damme ile merfû.", punct=punct)
def fail_name(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", ["fail", "mamnu-min-sarf"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the doer; a foreign name, a diptote.", tr + " — fâil; yabancı özel isim, gayr-i munsarıf.", punct=punct)
def allah_fail(full="اللهُ", punct=None):
    return tok(full, "allah", "propn", ["fail"], "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Allah» — the doer, in rafʿ.", "«Allah» — lafza-i celâl, fâil, merfû.", punct=punct)
def maful(full, lex, en, tr, tags=(), punct=None, extra_ar=""):
    return tok(full, lex, "noun", ["maful-bihi"] + list(tags), "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ" + extra_ar + ".", en + " — the object, naṣb by fatḥa.", tr + " — mef'ûl-i bih, fetha ile mansub.", punct=punct)
def maful_name(full, lex, en, tr, punct=None):
    return tok(full, lex, "propn", ["maful-bihi", "mamnu-min-sarf"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", en + " — the object; a diptote name.", tr + " — mef'ûl-i bih; gayr-i munsarıf özel isim.", punct=punct)
def nas_fail(punct=None): return fail("النَّاسُ", "nas", "«the people»", "«insanlar»", punct=punct)
def mudari(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, extra_ar=""):
    return tok(full, lex, "verb", ["mudari-marfu"] + list(tags), f"فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: {hidden}{extra_ar}.", en + " — a muḍāriʿ in rafʿ; the doer is concealed.", tr + " — merfû muzari; fâil gizli zamirdir.", punct=punct)
def khamsa(full, lex, en, tr, tags=(), punct=None, extra_ar="", wa=False):
    return tok(full, lex, "verb", ["afal-khamsa", "mudari-marfu"] + list(tags), W(wa) + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ" + extra_ar + ".", Wen(wa) + en + " — one of the five verbs, rafʿ by the kept nūn; the wāw is the doer.", Wtr(wa) + tr + " — ef'âl-i hamseden, nûnun sübûtu ile merfû; vâv fâildir.", punct=punct, segments=(wa_(full[2:], lex, "verb") if wa else None))
def la_nafiya(full="لَا", wa=False, punct=None):
    return tok(full, "la-nafiya", "part", ["la-nafiya"], W(wa) + "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", Wen(wa) + "«not» — the negating lā, no government.", Wtr(wa) + "«değil/-mez» — nefiy lâ'sı, amel etmez.", punct=punct, segments=(wa_("لَا", "la-nafiya", "part") if wa else None))
def neg_mudari(full, lex, en, tr, tags=(), hidden="هِيَ", punct=None, extra=""):
    return tok(full, lex, "verb", ["la-nafiya", "mudari-marfu"] + list(tags), f"فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: {hidden}{extra}.", en + " — rafʿ after the negating lā; the doer is concealed.", tr + " — nefiy lâ'sından sonra merfû; fâil gizli zamirdir.", punct=punct)
def inna(full="إِنَّ", wa=False, tags=()):
    return tok(full, "inna", "part", ["inna-wa-akhawatuha"] + list(tags), W(wa) + "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", Wen(wa) + "«indeed» — a particle like a verb: naṣb on its ism, rafʿ on its khabar.", Wtr(wa) + "«şüphesiz» — fiile benzeyen harf: ismini nasb, haberini ref eder.", segments=(wa_("إِنَّ", "inna", "part") if wa else None))
def anna(wa=False, full=None, obj_of="يَعْرِفُ", tags=()):
    full = full or ("وَأَنَّ" if wa else "أَنَّ")
    return tok(full, "anna", "part", ["inna-wa-akhawatuha"] + (["atf-nasaq"] if wa else []) + list(tags), W(wa) + f"حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ، وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولُ {obj_of}.", Wen(wa) + "«that» — a particle like a verb: naṣb on its ism, rafʿ on its khabar; the clause is the verb's object.", Wtr(wa) + "«-dığını» — fiile benzeyen harf: ismini nasb, haberini ref eder; cümle fiilin mef'ûlüdür.", segments=(wa_("أَنَّ", "anna", "part") if wa else None))
def allah_ism(full="اللهَ", part="إِنَّ", punct=None):
    return tok(full, "allah", "propn", ["inna-wa-akhawatuha"], f"لَفْظُ الْجَلَالَةِ اسْمُ {part} مَنْصُوبٌ بِالْفَتْحَةِ.", f"«Allah» — the ism of {('inna' if part == 'إِنَّ' else 'anna')}, in naṣb.", "«Allah» — " + ("inne" if part == "إِنَّ" else "enne") + "'nin ismi, mansub.", punct=punct)
def ism_inna(full, lex, en, tr, tags=(), punct=None, extra="", part="إِنَّ"):
    return tok(full, lex, "noun", ["inna-wa-akhawatuha"] + list(tags), f"اسْمُ {part} مَنْصُوبٌ بِالْفَتْحَةِ" + extra + ".", en + " — the ism of " + ("inna" if part == "إِنَّ" else "anna") + ", in naṣb.", tr + " — " + ("inne" if part == "إِنَّ" else "enne") + "'nin ismi, mansub.", punct=punct)
def khabar_inna(full, lex, en, tr, tags=(), punct=None, extra="", part="إِنَّ"):
    return tok(full, lex, "noun", ["inna-wa-akhawatuha"] + list(tags), f"خَبَرُ {part} مَرْفُوعٌ بِالضَّمَّةِ" + extra + ".", en + " — the khabar of " + ("inna" if part == "إِنَّ" else "anna") + ", in rafʿ.", tr + " — " + ("inne" if part == "إِنَّ" else "enne") + "'nin haberi, merfû.", punct=punct)
def kana(full="وَكَانَ", punct=None, wa=True):
    return tok(full, "kana", "verb", [K, "hollow-verbs"], W(wa) + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", Wen(wa) + "«was» — the defective verb kāna: it raises its ism and puts its khabar in naṣb.", Wtr(wa) + "«idi» — nâkıs fiil kâne: ismini ref, haberini nasb eder.", punct=punct, segments=(wa_("كَانَ", "kana", "verb") if wa else None))
def ishara(full, lex, case, en, tr, punct=None, tags=()):
    C = {"nasb": ("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "object"), "jarr": ("فِي مَحَلِّ جَرٍّ", "in the place of jarr"), "raf": ("فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "the mubtadaʾ")}[case]
    return tok(full, lex, "pron", ["asma-al-ishara"] + list(tags), f"اسْمُ إِشَارَةٍ مَبْنِيٌّ {C[0]}.", en + f" — a demonstrative, built; {C[1]}.", tr + " — ism-i işâret, mebnî; mahallen " + {"nasb": "mansub (mef'ûl)", "jarr": "mecrûr", "raf": "merfû (mübtedâ)"}[case] + ".", punct=punct)
def li_pron(full, lex_pron, en, tr, ar, punct=None, tags=()):
    return tok(full, "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"] + list(tags), ar, en, tr, punct=punct, segments=[seg("لِأَنَّ", "lianna", "part"), seg(full[len("لِأَنَّ"):], lex_pron, "pron")])
def sen_of(S):
    def sen(sid, en, tr, toks): S.append({"id": sid, "translation": {"en": en, "tr": tr}, "tokens": toks})
    return sen
def quran(toks, first_tag=True):
    toks[0]["quoteBefore"] = "«"; toks[-1]["quoteAfter"] = "»"
    if first_tag: toks[0].setdefault("grammar", []).insert(0, "al-iqtibas-wal-tadmin")
    return toks
