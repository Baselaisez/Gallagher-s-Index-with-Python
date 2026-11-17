#!/usr/bin/env python3
"""review_sheets.py — the AI pre-review's findings, turned into Turkish review material for the hoca and the students.

    python3 tools/review_sheets.py [--out reports/hoca-inceleme] [--rows 120] [--severity critical]

Reads every finished review batch under reports/ (review-*/ and review-*/w*/ with a batch.json), keeps the newest result
for each request (a re-run supersedes the first run; the @medium comparison copy is left out) and writes:

  01-hoca-desenler.xlsx   the systematic error patterns, most frequent first: what the pattern is, 2–3 examples, how
                          many findings it covers, how many tokens on the whole shelf carry its signature, the proposed
                          RULE fix, and a decision column (ONAY / RET / DÜZELT + not)
  02-grup-NN-<paket>.xlsx one sheet per student group: the findings of one package, at most --rows rows each,
                          al-usul-al-munifa first, then tasrif-al-izzi, then the rest; a Turkish instruction block on top
  master.json             every finding with its stable id and pattern — tools/review_intake.py reads the returned
                          sheets against it

Nothing here edits content. The ids are stable (a hash of package, request, location, field and the current value), so
re-running after a new batch adds rows without renumbering what has already been sent out; a sheet once written is
never overwritten (new findings go to new group files).
"""
import argparse, glob, hashlib, json, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
N = lambda s: unicodedata.normalize("NFC", s or "")
HARAKAT = re.compile(r"[ً-ْٰـ]")
bare = lambda s: HARAKAT.sub("", N(s))
SKIP = {"batch", "plan", "usage", "refused", "truncated", "failed", "deferred", "assumptions", "assumptions-by-group", "dry-run"}
SEV_TR = {"critical": "kritik", "major": "önemli", "minor": "küçük"}
ORDER = ["al-usul-al-munifa", "tasrif-al-izzi"]           # the owner's order; everything else follows by finding count
DECISIONS = ["ONAY", "RET", "DÜZELT", "ŞÜPHELİ"]
FIELD_TR = {"surface": "[hareke] ", "irab.en": "[iʿrâb EN] ", "irab.tr": "[iʿrâb TR] ", "lex": "[sözlük anahtarı] ", "gloss": "[anlam] ",
            "grammar": "[gramer notu] ", "translation.en": "[çeviri EN] ", "translation.tr": "[çeviri TR] ", "other": "[diğer] "}


# ---------------------------------------------------------------- findings
def load_findings():
    dirs = sorted({str(Path(p).parent) for p in glob.glob(str(ROOT / "reports/review-*/batch.json")) + glob.glob(str(ROOT / "reports/review-*/w*/batch.json"))})
    runs = []
    for d in dirs:
        st = json.loads(Path(d, "batch.json").read_text(encoding="utf-8"))
        if not Path(d, "usage.json").is_file(): continue                    # still running: not collected yet
        runs.append((st["created"], d, st))
    runs.sort()
    newest = {}                                                            # custom_id -> (created, dir)
    for created, d, st in runs:
        for cid, meta in st["requests"].items():
            if "@" in meta.get("report_as", ""): continue
            newest[cid] = (created, d)
    out = []
    for created, d, st in runs:
        for f in glob.glob(d + "/*.json"):
            name = Path(f).stem
            if name in SKIP or "@" in name: continue
            for x in json.loads(Path(f).read_text(encoding="utf-8"))["findings"]:
                if newest.get(x["custom_id"]) != (created, d): continue
                x = dict(x, run=Path(d).relative_to(ROOT).as_posix())
                key = "|".join(str(x.get(k)) for k in ("package", "custom_id", "chapter", "sentence", "token", "field", "issue_type")) + "|" + N(x.get("current"))
                x["id"] = "QR-" + hashlib.sha1(key.encode()).hexdigest()[:8].upper()
                out.append(x)
    seen, uniq = set(), []
    for x in out:
        if x["id"] in seen: continue
        seen.add(x["id"]); uniq.append(x)
    return uniq, [d for _, d, _ in runs]


# ---------------------------------------------------------------- the shelf (for the signature scans)
def shelf():
    """(package, chapter, sentence id, [tokens]) for every package, plus each package's glossary."""
    import review_batch as rb
    trm = rb.irab_tr_memory()
    for p in rb.pending_packages():
        man = json.loads((p / "manifest.json").read_text(encoding="utf-8"))
        gl = json.loads((p / "glossary.json").read_text(encoding="utf-8")).get("entries", {}) if (p / "glossary.json").is_file() else {}
        for f in sorted((p / "chapters").glob("*.json"), key=lambda q: int(q.stem)):
            d = json.loads(f.read_text(encoding="utf-8"))
            for s in d.get("sentences") or []:
                yield man["id"], int(d.get("chapter", f.stem)), s["id"], s.get("tokens") or [], gl


def ar(t): return bare((t.get("irab") or {}).get("ar"))
def surf(t): return N((t.get("surface") or {}).get("full"))
def is_verb(t): return t.get("pos") == "verb" or ar(t).startswith("فعل") or re.search(r"(?:^|، ?|و)فعل (ماض|مضارع|أمر)", ar(t)) is not None
def head_fail(a):
    """The line names THIS word a fāʿil (not nāʾib al-fāʿil, not «ism fāʿil», not «its fāʿil is …»)."""
    a = re.sub(r"اسم فاعل\S*", "", a)
    m = re.search(r"(?:^|، ?|و)فاعل\b", a)
    return bool(m) and "نائب" not in a[:max(0, m.start()) + 12] and not re.search(r"والفاعل|وفاعله", a[:m.end() + 1])


PASSIVE_MAZI = re.compile(r"^[وف]?َ?.ُ[^ً-ْ]*.*ِ.َ$")
def looks_passive(t):
    """Surface signature of the majhūl: mudāriʿ prefix with ḍamma and fatḥa on the letter before the last;
    māḍī with ḍamma on the first letter and kasra on the letter before the last. Hollow passives (قِيلَ) are not
    caught — the scan undercounts rather than guesses."""
    s = re.sub(r"^[وف]َ", "", surf(t))
    letters = re.findall(r"([^ً-ْٰ])([ً-ْٰ]*)", s)
    if len(letters) < 3: return False
    v = [m for _, m in letters]
    if letters[0][0] in "يتنأ" and "ُ" in v[0]:
        return "َ" in v[-2] and "ّ" not in v[-2] or ("َ" in v[-2] and len(letters) > 3)
    return "ُ" in v[0] and "ِ" in v[-2] and v[-1].startswith("َ")


# ---------------------------------------------------------------- the patterns
def P(pid, title, what, fix, match, scan=None, scan_note=""):
    return {"id": pid, "title": title, "what": what, "fix": fix, "match": match, "scan": scan, "scan_note": scan_note}

QUOTES = re.compile(r"[«»\"'()]")
def cur(f): return QUOTES.sub("", bare(f.get("current")))
def sug(f): return QUOTES.sub("", bare(f.get("suggested")))

def scan_fail_no_verb():
    n = 0
    for pk, c, sid, toks, gl in shelf():
        seen_verb = False
        for t in toks:
            a = ar(t)
            if head_fail(a) and not seen_verb and t.get("pos") not in ("verb",) and not re.search(r"اسم فاعل|مصدر", a): n += 1
            if is_verb(t) or re.search(r"مصدر|اسم فاعل|اسم مفعول", a): seen_verb = True
    return n

def scan_passive():
    n = 0
    for pk, c, sid, toks, gl in shelf():
        for t in toks:
            a = ar(t)
            if "للمجهول" in a and re.search(r"(?:^|، ?|و)(?:ال)?فاعل", a) and "نائب" not in a: n += 1
            elif t.get("pos") == "verb" and looks_passive(t) and "للمجهول" not in a and "نائب" not in a: n += 1
    return n

def scan_amma():
    n = 0
    for pk, c, sid, toks, gl in shelf():
        for i, t in enumerate(toks):
            if bare(surf(t)).lstrip("و") in ("أما", "اما") and "ّ" in surf(t):
                for u in toks[i + 1:]:
                    if bare(surf(u)).startswith("ف"):
                        if "جواب" not in ar(u) and "رابطة" not in ar(u) and "واقعة" not in ar(u): n += 1
                        break
    return n

def scan_hidden_vs_overt():
    n = 0
    for pk, c, sid, toks, gl in shelf():
        for i, t in enumerate(toks):
            if is_verb(t) and "ضمير مستتر" in ar(t):
                for u in toks[i + 1:i + 4]:
                    if is_verb(u): break
                    if head_fail(ar(u)): n += 1; break
    return n

def scan_hal_definite():
    n = 0
    for pk, c, sid, toks, gl in shelf():
        for t in toks:
            a = ar(t)
            if re.match(r"^(?:الواو \S+، و)?حال\b", a) and (re.match(r"^[وفبلك]?ال", bare(surf(t))) or "مضاف" in a and "مضاف إليه" not in a): n += 1
    return n

def scan_sound_sign_on_singular():
    n = 0
    for pk, c, sid, toks, gl in shelf():
        for t in toks:
            a = ar(t)
            m = re.search(r"لأنه (جمع مذكر سالم|مثنى)", a)
            if not m: continue
            lemma = bare((gl.get(t.get("lex")) or {}).get("lemma") or "")
            if lemma and re.search(r"(ين|ون|ان)$", lemma): n += 1
    return n

def scan_ibn():
    n = 0
    for pk, c, sid, toks, gl in shelf():
        for t in toks:
            if bare(surf(t)).lstrip("و") in ("بن", "ابن", "بنت") and not re.search(r"نعت|صفة|بدل|عطف بيان", ar(t)): n += 1
    return n

def scan_ya_fail():
    n = 0
    for pk, c, sid, toks, gl in shelf():
        for t in toks:
            if re.search(r"الياء فاعل|والياء ضمير[^،]*فاعل", ar(t)) and re.search(r"ُو[اهنك]|ُونَ", surf(t)): n += 1
    return n

def scan_lam_lan():
    n = 0
    for pk, c, sid, toks, gl in shelf():
        for t in toks:
            if re.search(r"منصوب بلم|مجزوم بلن|منصوب بـ?لم\b|مجزوم بـ?لن\b", ar(t)): n += 1
    return n


def scan_person():
    """A hidden pronoun must agree with the prefix: يـ هو، تـ أنتَ/هي، أ أنا، نـ نحن."""
    ok = {"ي": {"هو"}, "ت": {"أنت", "هي"}, "أ": {"أنا"}, "ن": {"نحن"}}
    n = 0
    for pk, c, sid, toks, gl in shelf():
        for t in toks:
            a = ar(t)
            m = re.search(r"ضمير مستتر[^،.]*تقديره (هو|هي|أنت|أنا|نحن)", a)
            if not m or "مضارع" not in a: continue
            pre = re.sub(r"^(?:[وف]|ل|س)", "", bare(surf(t)))[:1]
            if pre in ok and m.group(1) not in ok[pre]: n += 1
    return n


PATTERNS = [
    P("D01", "Fiil yokken «fâil» etiketi (isim cümlesi)",
      "Merfû bir kelimeye «fâil» denmiş, ama önünde onu talep eden bir fiil (ya da fiil manasında bir kelime) yok. "
      "İsim cümlesinde merfû kelime mübteda veya haberdir; fâil ancak fiilden sonra gelir.",
      "Yazım hattına kural: bir kelime «فَاعِلٌ» diye işaretlenecekse, aynı cümlede ondan ÖNCE bir fiil, masdar veya "
      "ism-i fâil/meful bulunmalı; yoksa kelime mübteda/haber adayı olarak işaretlenir ve hocanın onayına düşer. "
      "Doğrulayıcıya (validate_content) aynı şart uyarı olarak eklenir.",
      lambda f: "فاعل" in cur(f) and "نائب" not in cur(f) and re.search(r"مبتدأ|خبر", sug(f)) and not head_fail(sug(f)),
      scan_fail_no_verb, "cümlede önünde fiil / masdar / ism-i fâil olmayan «فاعل» satırları"),
    P("D02", "Meçhul fiil: fâil yerine nâib-i fâil",
      "Fiil meçhul (مَبْنِيٌّ لِلْمَجْهُولِ) olduğu halde satırda «fâil» veya «gizli fâil» yazıyor; ya da fiilin meçhul olduğu hiç "
      "söylenmemiş. Meçhul fiilin fâili yoktur, nâib-i fâili vardır.",
      "Kural: harekesi meçhul kalıbında olan fiil (mâzîde ilk harf ötre + sondan önceki esre; muzâride ötreli harf-i "
      "muzâraat + sondan önceki üstün) «مَبْنِيٌّ لِلْمَجْهُولِ» alır ve fâil yerine «نَائِبُ الْفَاعِلِ» yazılır. Ecvef "
      "meçhuller (قِيلَ، يُقَالُ) kalıba uymaz; onlar sarf tablosundan okunur.",
      lambda f: re.search(r"نائب الفاعل|للمجهول", sug(f)) and not re.search(r"نائب الفاعل|للمجهول", cur(f)),
      scan_passive, "«للمجهول» deyip «فاعل» yazan satırlar + harekesi meçhul kalıbında olup meçhul denmeyen fiiller (tahmini)"),
    P("D03", "«أَمَّا»dan sonraki fâ: atıf değil, cevap fâsı",
      "«أَمَّا»nın cevabına giren fâ, «عاطفة» veya «سببية» diye okunmuş. Bu fâ «الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا» dır; "
      "«أَمَّا» kelimesine de أَمَّا التَّفْصِيلِيَّة notu düşer.",
      "Kural: cümlede «أَمَّا»dan sonra gelen İLK fâ ile başlayan kelimenin iʿrâbı «الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا» ile "
      "başlar (tek kural, bütün metinler). Doğrulayıcı aynı yeri kontrol eder.",
      lambda f: "جواب أما" in sug(f) and "جواب أما" not in cur(f),
      scan_amma, "«أَمَّا»dan sonraki ilk fâ'lı kelimede «جواب» geçmeyen satırlar"),
    P("D04", "Açık fâil varken «gizli zamir fâil»",
      "Fiilin satırı «وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ» diyor, ama fâil fiilden sonra açıkça zikredilmiş (ism-i zâhir). "
      "Açık fâil varken gizli zamir takdir edilmez.",
      "Kural: fiilden sonra, araya başka fiil girmeden «فَاعِل» diye işaretlenmiş bir kelime varsa, fiilin satırı "
      "«ضَمِيرٌ مُسْتَتِرٌ» diyemez; iki satır birbirini tutmalı (doğrulayıcıda çelişki kontrolü).",
      lambda f: "ضمير مستتر" in cur(f) and "ضمير مستتر" not in sug(f) and re.search(r"فاعل|اسمه|اسمها", sug(f)),
      scan_hidden_vs_overt, "«ضمير مستتر» diyen fiilden sonraki 3 kelime içinde «فاعل» işaretli kelime"),
    P("D05", "Hâl olamayacak kelimeye «hâl»",
      "Kelime «حَالٌ» diye işaretlenmiş, ama aslında mefûlün bih (çoğu zaman ikinci mefûl) veya haber. Hâl nekre olur; "
      "harf-i tarifli ya da muzâf (marife) bir kelime hâl olamaz.",
      "Kural: «حَالٌ» satırı ancak nekre kelimeye yazılabilir (ال yok, ma'rifeye muzâf değil); aksi halde doğrulayıcı "
      "uyarır. İki mefûl alan fiillerde (سَمَّى، أَلْزَمَ، جَعَلَ…) ikinci mansûb önce mefûl olarak denenir.",
      lambda f: "حال" in cur(f) and "حال" not in sug(f),
      scan_hal_definite, "«حال» denmiş ama ال'li ya da muzâf olan kelimeler"),
    P("D06", "Müfred kelimeye cem/tesniye alameti",
      "Kelime müfred (عَيْن، نُون، دُون…) ama satır «بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ / مُثَنًّى» diyor. Sondaki "
      "ين/ون kökün harfidir; iʿrâb alameti görünen harekedir.",
      "Kural: «جمع مذكر سالم / مثنى» alameti yazılmadan önce sözlükteki lemma'ya bakılır; lemma'nın kendisi ين/ون/ان ile "
      "bitiyorsa o harfler kökündür ve alamet harekedir.",
      lambda f: re.search(r"لأنه (جمع مذكر سالم|مثنى)", cur(f)) and not re.search(r"لأنه (جمع مذكر سالم|مثنى)", sug(f)),
      scan_sound_sign_on_singular, "lemma'sı ين/ون/ان ile biten ama cem/tesniye alameti verilen kelimeler"),
    P("D07", "Senet zincirinde «ibn» ve nisbe: na't, fâil değil",
      "Hadis senedinde «بْنُ» veya nisbe (الْأَشْجَعِيُّ…) fâil/mübteda diye işaretlenmiş. Bunlar önceki ismin na'tıdır "
      "(veya bedel); fâil zincirin başındaki isimdir.",
      "Kural: iki alem arasındaki «بْنُ / ابْنُ / بِنْتُ» ve alemden sonraki nisbe kelimesi, önceki ismin iʿrâbını alan "
      "na't (نَعْتٌ) olarak işaretlenir; senetler için tek şablon.",
      lambda f: bare(f.get("surface")).lstrip("و") in ("بن", "ابن", "بنت") or ("نعت" in sug(f) and "فاعل" in cur(f) and "نعت" not in cur(f)),
      scan_ibn, "«بن/ابن/بنت» olup na't/bedel denmeyen kelimeler"),
    P("D08", "Gizli zamirin şahsı harf-i muzâraata uymuyor",
      "Muzâri fiilin gizli zamiri yanlış şahısla takdir edilmiş (ör. تَـ ile başlayan fiile «هُوَ»). يـ → هُوَ، تـ → أَنْتَ "
      "veya هِيَ، أَ → أَنَا، نـ → نَحْنُ.",
      "Kural: «تَقْدِيرُهُ …» harf-i muzâraattan türetilir, elle yazılmaz; تـ için bağlam (muhatap / müennes gaib) hocaya "
      "bırakılır ama يـ ile هِيَ, أَ ile هُوَ gibi imkânsız eşleşmeler doğrulayıcıda hata olur.",
      lambda f: re.search(r"تقديره (هو|هي|أنت|أنا|نحن)", cur(f)) and re.search(r"تقديره (هو|هي|أنت|أنا|نحن)", sug(f))
                and re.search(r"تقديره (\S+)", cur(f)).group(1) != re.search(r"تقديره (\S+)", sug(f)).group(1),
      scan_person, "harf-i muzâraatla çelişen «تقديره» satırları (kesin)"),
    P("D11", "Ef'âl-i hamsede fâil: harf-i muzâraat yâsı değil, cemi vavı",
      "«يَعْبُدُوهُ، يَعْرِفُوهُ» gibi fiillerde satır «وَالْيَاءُ فَاعِلٌ» diyor. Baştaki yâ harf-i muzâraattır; fâil "
      "cemi vavıdır (وَاوُ الْجَمَاعَةِ), müsenna elifi veya muhatabe yâsıdır (ef'âl-i hamse).",
      "Kural: ef'âl-i hamse kalıbındaki (ـُونَ، ـَانِ، ـِينَ ve nûnu düşmüş halleri) fiilde fâil, sondaki vav/elif/yâdır; "
      "harf-i muzâraat hiçbir zaman fâil yazılmaz. Satır şablonu bu kalıptan otomatik üretilir.",
      lambda f: re.search(r"الياء فاعل|والياء ضمير[^،]*فاعل", cur(f)) and not re.search(r"الياء فاعل", sug(f)),
      scan_ya_fail, "«الياء فاعل» deyip yüzeyinde cemi vavı olan fiiller (kesin)"),
    P("D12", "«لَمْ» nasb etmez, «لَنْ» cezm etmez",
      "Satır «مَنْصُوبٌ بِلَمْ» diyor (ya da tersi). لَمْ cezm eder; mansûb fiil «لَامُ الْجُحُودِ»dan sonra gizli «أَنْ» ile "
      "mansûbdur (مَا كَانَ … لِيَفْعَلَ / لَمْ يَكُنْ … لِيَفْعَلَ).",
      "Kural: «منصوب بلم» ve «مجزوم بلن» doğrulayıcıda HATA olur; «لَمْ يَكُنْ … لِـ + muzâri» kalıbında nasb «أَنْ مُضْمَرَةٌ "
      "وُجُوبًا بَعْدَ لَامِ الْجُحُودِ» ile yazılır.",
      lambda f: re.search(r"منصوب بلم|مجزوم بلن", cur(f)),
      scan_lam_lan, "«منصوب بلم / مجزوم بلن» satırları (kesin)"),
    P("D09", "Vav / fâ türü: atıf değil (istînâf, hâl, kasem…)",
      "Vav veya fâ «عاطفة» diye okunmuş; oysa yeni bir cümle başlatıyor (istînâfiyye), hâl cümlesi bağlıyor (hâliyye), "
      "kasem vavı veya cevap/râbıta fâsı.",
      "Kural yok — bağlam ister. Öneri: cümle başındaki vav/fâ için iki aday (atıf / istînâf) gösterilir ve hoca seçer "
      "(uygulamadaki WawEngine'in kısa listesi ile aynı ilke).",
      lambda f: "عاطفة" in cur(f) and "عاطفة" not in sug(f) and re.search(r"استئناف|حالية|قسم|رابطة|واقعة|سببية|زائدة", sug(f)),
      None, ""),
    P("D10", "Tâbi' (na't, bedel, atıf) ile muzâfun ileyh karışması",
      "Bir kelime «مُضَافٌ إِلَيْهِ» denmiş ama önceki kelimenin bedeli/na'tı/ma'tûfu; ya da tersi.",
      "Kural yok — anlam ister. Öneri: muzâfın kendisi tenvinli veya ال'li ise sonraki kelime muzâfun ileyh OLAMAZ "
      "(لا يجتمع الألف واللام والإضافة); bu kısmı doğrulayıcı yakalar.",
      lambda f: ("مضاف إليه" in cur(f)) != ("مضاف إليه" in sug(f)) and re.search(r"بدل|نعت|معطوف", cur(f) + " " + sug(f)),
      None, ""),
]


def classify(f):
    if f.get("issue_type") not in ("irab_ar", "tashkeel"): return ""
    for p in PATTERNS:
        try:
            if p["match"](f): return p["id"]
        except Exception:
            pass
    return ""


# ---------------------------------------------------------------- xlsx
def xlsx_patterns(path, findings, scans):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.worksheet.datavalidation import DataValidation
    wb = Workbook(); ws = wb.active; ws.title = "Desenler"
    intro = [
        "Hocam için: yapay zekâ ön incelemesinde tekrar eden SİSTEMATİK hata desenleri (en sık olan önce).",
        "Her desen tek bir kural düzeltmesiyle bütün raftaki benzer yerleri düzeltebilir; bu yüzden önce bu sayfaya karar vermenizi rica ediyoruz.",
        "Karar: ONAY = desen doğru, önerilen kural uygulansın · RET = desen yanlış, kural uygulanmasın · DÜZELT = desen doğru ama kural "
        "Not sütunundaki gibi düzeltilsin · emin değilseniz ŞÜPHELİ yazıp not bırakın.",
        "«İşaretlenen» = yapay zekânın bu desene giren bulgu sayısı. «Raf taraması» = bütün kitaplarda (54 paket) bu desenin MEKANİK imzasını "
        "taşıyan, yani bir kuralla şimdiden bulunabilen token sayısı. Bağlama bağlı olanları yakalamaz, bu yüzden işaretlenenden az olabilir; "
        "«—» olan desenler kuralla taranamıyor (anlam ister). Hiçbir içerik henüz değiştirilmedi.",
    ]
    for i, t in enumerate(intro, 1):
        ws.cell(row=i, column=1, value=t).font = Font(bold=(i == 1)); ws.merge_cells(start_row=i, start_column=1, end_row=i, end_column=11)
        ws.cell(row=i, column=1).alignment = Alignment(wrap_text=True); ws.row_dimensions[i].height = 32
    hdr = ["No", "Desen", "Ne oluyor", "Örnek 1", "Örnek 2", "Örnek 3", "İşaretlenen (kritik / tümü)", "Raf taraması (token)",
           "Önerilen kural düzeltmesi", "Karar (ONAY/RET/DÜZELT/ŞÜPHELİ)", "Not"]
    H = len(intro) + 2
    for j, h in enumerate(hdr, 1):
        c = ws.cell(row=H, column=j, value=h); c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="44546A")
        c.alignment = Alignment(wrap_text=True, vertical="center")
    by = defaultdict(list)
    for f in findings: by[f.get("pattern") or ""].append(f)
    rows = sorted([p for p in PATTERNS], key=lambda p: -len(by[p["id"]]))
    dv = DataValidation(type="list", formula1='"' + ",".join(DECISIONS) + '"', allow_blank=True); ws.add_data_validation(dv)
    for i, p in enumerate(rows):
        r = H + 1 + i
        fs = by[p["id"]]; crit = [f for f in fs if f["severity"] == "critical"]
        pool = crit or fs; ex, pk_seen = [], set()
        for f in pool:                                                   # one example per package first, then any
            if f["package"] not in pk_seen: ex.append(f); pk_seen.add(f["package"])
            if len(ex) == 3: break
        for f in pool:
            if len(ex) == 3: break
            if f not in ex: ex.append(f)
        exs = [f"{f['package']} {f['chapter']}:{f['sentence']} — {f['surface']}\nŞimdi: {N(f['current'])}\nÖneri: {N(f['suggested'])}\n({f.get('reason_tr') or ''})" for f in ex]
        sc = scans.get(p["id"])
        vals = [p["id"], p["title"], p["what"], *(exs + ["", "", ""])[:3], f"{len(crit)} / {len(fs)}",
                ("—" if sc is None else f"{sc}  ({p['scan_note']})"), p["fix"], "", ""]
        for j, v in enumerate(vals, 1):
            c = ws.cell(row=r, column=j, value=v); c.alignment = Alignment(wrap_text=True, vertical="top")
        dv.add(ws.cell(row=r, column=10)); ws.row_dimensions[r].height = 210
    rest = by[""]
    r = H + 2 + len(rows)
    ws.cell(row=r, column=1, value=f"Desene girmeyen bulgular: {sum(1 for f in rest if f['severity'] == 'critical')} kritik / {len(rest)} tümü — "
                                   "bunlar öğrenci sayfalarında tek tek inceleniyor.").font = Font(italic=True)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=11)
    for j, w in enumerate([6, 26, 42, 46, 46, 46, 14, 26, 46, 16, 30], 1): ws.column_dimensions[chr(64 + j)].width = w
    ws.freeze_panes = ws.cell(row=H + 1, column=3)
    ws.sheet_view.rightToLeft = False
    wb.save(path)


STUDENT_INTRO = [
    "Yapay zekâ ön incelemesi — öğrenci inceleme sayfası. İçerikte hiçbir şey değiştirilmedi; her satır bir ÖNERİDİR, karar sizindir.",
    "Her satır bir kelime: «mevcut iʿrâb» uygulamada şu an yazan satır, «önerilen iʿrâb» yapay zekânın önerisi, «gerekçe» neden.",
    "Karar sütununa yalnızca şunlardan birini yazın (listeden seçin):",
    "   ONAY = öneri doğru, aynen alınsın.   RET = öneri yanlış, mevcut satır doğru (Not'a kısaca neden).",
    "   DÜZELT = mevcut satır yanlış ama öneri de tam doğru değil: doğrusunu «düzeltilmiş iʿrâb» sütununa Arapça yazın.",
    "   Emin değilseniz ŞÜPHELİ yazın ve Not'a ne konuda tereddüt ettiğinizi yazın — hocamız bakacak.",
    "«İnceleyen» sütununa adınızı yazın. «id» sütununu ve satırların sırasını DEĞİŞTİRMEYİN (geri okuma id ile yapılıyor).",
    "Yer: «bölüm:cümle» uygulamadaki bölüm numarası ve cümle kimliğidir (ör. 14:s28); kelime aynı cümlede o sıradaki kelimedir (#numara).",
    "Satırların çoğu Arapça iʿrâb satırıdır; başında [hareke], [çeviri TR] gibi etiket olan satırlar o alanı (kelimenin harekesi, çeviri…) önerir.",
]

def xlsx_group(path, title, rows):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.worksheet.datavalidation import DataValidation
    wb = Workbook(); ws = wb.active; ws.title = "İnceleme"
    ws.cell(row=1, column=1, value=title).font = Font(bold=True, size=13)
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=13)
    for i, t in enumerate(STUDENT_INTRO, 2):
        ws.cell(row=i, column=1, value=t).alignment = Alignment(wrap_text=True)
        ws.merge_cells(start_row=i, start_column=1, end_row=i, end_column=13)
    H = len(STUDENT_INTRO) + 3
    hdr = ["id", "paket", "bölüm:cümle", "kelime", "mevcut iʿrâb (ar)", "önerilen iʿrâb (ar)", "gerekçe (tr)", "önem",
           "karar (ONAY/RET/DÜZELT/ŞÜPHELİ)", "düzeltilmiş iʿrâb (DÜZELT ise)", "inceleyen", "not", "desen"]
    for j, h in enumerate(hdr, 1):
        c = ws.cell(row=H, column=j, value=h); c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="44546A")
        c.alignment = Alignment(wrap_text=True, vertical="center")
    dv = DataValidation(type="list", formula1='"' + ",".join(DECISIONS) + '"', allow_blank=True); ws.add_data_validation(dv)
    yellow = PatternFill("solid", fgColor="FFF2CC")
    for i, f in enumerate(rows):
        r = H + 1 + i
        lab = FIELD_TR.get(f.get("field"), "")
        vals = [f["id"], f["package"], f"{f['chapter']}:{f['sentence']}", f"{f['surface']}  (#{f['token']})", lab + N(f["current"]), lab + N(f["suggested"]),
                f.get("reason_tr") or "", SEV_TR.get(f["severity"], f["severity"]), "", "", "", "", f.get("pattern") or ""]
        for j, v in enumerate(vals, 1):
            c = ws.cell(row=r, column=j, value=v); c.alignment = Alignment(wrap_text=True, vertical="top", readingOrder=(2 if j in (4, 5, 6, 10) else 0))
            if j in (9, 10, 11, 12): c.fill = yellow
        dv.add(ws.cell(row=r, column=9))
    for j, w in enumerate([13, 18, 11, 16, 44, 44, 44, 9, 16, 40, 14, 28, 7], 1): ws.column_dimensions[chr(64 + j)].width = w
    ws.freeze_panes = ws.cell(row=H + 1, column=2)
    ws.auto_filter.ref = f"A{H}:M{H + len(rows)}"
    wb.save(path)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=str(ROOT / "reports/hoca-inceleme"))
    ap.add_argument("--rows", type=int, default=120, help="rows per student sheet")
    ap.add_argument("--severity", default="critical", help="severities for the student sheets, comma-separated")
    ap.add_argument("--no-scan", action="store_true")
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    findings, runs = load_findings()
    for f in findings: f["pattern"] = classify(f)
    mpath = out / "master.json"
    master = json.loads(mpath.read_text(encoding="utf-8")) if mpath.is_file() else {"findings": {}, "sheets": {}}
    for f in findings: master["findings"].setdefault(f["id"], f)
    scans = {} if a.no_scan else {p["id"]: p["scan"]() for p in PATTERNS if p["scan"]}
    master["patterns"] = {p["id"]: {"title": p["title"], "fix": p["fix"], "flagged": sum(1 for f in master["findings"].values() if f.get("pattern") == p["id"]),
                                    "shelf_scan": scans.get(p["id"])} for p in PATTERNS}
    master["runs"] = runs
    xlsx_patterns(out / "01-hoca-desenler.xlsx", list(master["findings"].values()), scans)
    # student groups: only findings not yet on a sheet
    sent = {i for ids in master["sheets"].values() for i in ids}
    sev = set(a.severity.split(","))
    todo = [f for f in master["findings"].values() if f["severity"] in sev and f["id"] not in sent]
    by = defaultdict(list)
    for f in todo: by[f["package"]].append(f)
    pk_order = [p for p in ORDER if p in by] + sorted([p for p in by if p not in ORDER], key=lambda p: -len(by[p]))
    n = len(master["sheets"])
    made = []
    for pk in pk_order:
        rows = sorted(by[pk], key=lambda f: (int(f["chapter"] or 0), str(f["sentence"]), int(f["token"] or 0)))
        parts = -(-len(rows) // a.rows); size = -(-len(rows) // parts)          # even split: 121 rows -> 61 + 60, not 120 + 1
        for k in range(0, len(rows), size):
            n += 1
            part = rows[k:k + size]
            name = f"02-grup-{n:02d}-{pk}.xlsx"
            first, last = part[0], part[-1]
            xlsx_group(out / name, f"Grup {n:02d} — {pk} — bölüm {first['chapter']}–{last['chapter']} — {len(part)} satır", part)
            master["sheets"][name] = [f["id"] for f in part]; made.append((name, len(part)))
    mpath.write_text(json.dumps(master, ensure_ascii=False, indent=1), encoding="utf-8")
    allf = list(master["findings"].values())
    print(f"{len(allf)} findings ({Counter(f['severity'] for f in allf)}), from {len(runs)} runs")
    for p in sorted(PATTERNS, key=lambda p: -master["patterns"][p["id"]]["flagged"]):
        m = master["patterns"][p["id"]]
        print(f"  {p['id']} {m['flagged']:4d} flagged, shelf scan {m['shelf_scan']}: {p['title']}")
    print(f"  no pattern: {sum(1 for f in allf if not f.get('pattern'))} (critical {sum(1 for f in allf if not f.get('pattern') and f['severity'] == 'critical')})")
    print(f"written: {out / '01-hoca-desenler.xlsx'}")
    for name, k in made: print(f"written: {out / name} ({k} rows)")


if __name__ == "__main__":
    main()
