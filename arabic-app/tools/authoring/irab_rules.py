#!/usr/bin/env python3
"""irab_rules.py — the AI pre-check's CONFIRMED patterns as rule objects over the shipped iʿrāb lines.

    python3 tools/authoring/irab_rules.py [--rule D03] [--write]

Every rule is a class with the same shape: an id (the pattern of the review sheets), the source it stands on (book, file,
line, the rule quoted verbatim), `candidates(sentence)` — where it applies — and `rewrite(token)` — the new trilingual
line, or None when the line is not in a shape the rule knows (then it is reported, never guessed). A rule touches only
what its condition names; everything else in the line and the sentence stays as written.

Without --write it only prints what would change. With --write the chapters are updated and every change is appended
to review/ai-precheck/rule-applied.jsonl (package, place, before, after, rule, source), so the hoca can see exactly
which unreviewed lines a rule changed. Tokens already corrected one by one (review/ai-precheck/applied.jsonl) are left
alone.
"""
import json, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
N = lambda s: unicodedata.normalize("NFC", s or "")
bare = lambda s: re.sub(r"[ً-ْٰـ]", "", N(s))


class IrabRule:
    id = ""; title = ""; source = {}

    def candidates(self, toks, prev=None):
        """Indexes of the tokens this rule speaks for, in one sentence (prev: the sentence before it, or None)."""
        return []

    def rewrite(self, tok, toks=None, j=None):
        """The token's new {ar, en, tr}, or None if its line has a shape this rule does not know."""
        return None


class AmmaFaRule(IrabRule):
    """D03 — the fāʾ that opens the answer of أَمَّا is not a conjunction: «الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»»."""
    id = "D03"
    title = "the fāʾ answering أَمَّا"
    source = {"book": "Iẓhār al-Asrār (Birgivî), Arabic matn", "file": "research/sources/izhar-al-asrar-matn-lithograph.txt",
              "locator": "line 104", "quote": "وإن كان المبتدأ بعد أما وجب دخول الفاء في خبره نحو أما زيد فمنطلق"}
    AR_HEAD = re.compile(r"^الْفَاءُ\s+(?:عَاطِفَةٌ|لِلتَّفْرِيعِ|سَبَبِيَّةٌ)\s*،\s*")
    EN_HEAD = re.compile(r"^The fa (?:conjoins|joins|is conjunctive|is causal)[^;,.]*[;,.]\s*", re.I)
    TR_HEAD = re.compile(r"^«bunun üzerine»\s*\+?\s*")

    def candidates(self, toks, prev=None):
        out = []
        for i, t in enumerate(toks):
            s = bare((t.get("surface") or {}).get("full")).lstrip("وف")
            if s not in ("أما", "اما") or "ّ" not in N((t.get("surface") or {}).get("full")): continue
            for j in range(i + 1, len(toks)):
                u = toks[j]
                if u.get("quoteBefore") or u.get("quoteAfter"): continue          # a fāʾ inside a quotation is not the answer
                line = N((u.get("irab") or {}).get("ar"))
                if not bare(line).startswith("الفاء"): continue                     # فِي, فَوْقَ … are not the fāʾ
                if re.search(r"الْفَاءُ\s+(?:(?:وَاقِعَةٌ|دَاخِلَةٌ|رَابِطَةٌ)|فِي\s+جَوَابِ)", line): break   # already read as the answer
                if j not in out: out.append(j)
                break
        return out

    def rewrite(self, tok, toks=None, j=None):
        ir = tok.get("irab") or {}
        ar, en, tr = N(ir.get("ar")), ir.get("en") or "", ir.get("tr") or ""
        if not self.AR_HEAD.match(ar): return None
        new_ar = self.AR_HEAD.sub("الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، ", ar, count=1)
        new_en = self.EN_HEAD.sub("The fa answers «أَمَّا»; ", en, count=1) if self.EN_HEAD.match(en) else "The fa answers «أَمَّا»; " + en
        new_tr = self.TR_HEAD.sub("Fâ «أَمَّا»nın cevabındadır; ", tr, count=1) if self.TR_HEAD.match(tr) else "Fâ «أَمَّا»nın cevabındadır; " + tr
        return {"ar": new_ar, "en": new_en, "tr": new_tr}


class HeadlessLineRule(IrabRule):
    """H01 — a line whose ROLE was dropped by the authoring pass, leaving only the sign: « بِالْفَتْحَةِ، مُضَافٌ.».
    The role is read off the context the sentence itself gives, and only in five shapes; anything else is reported."""
    id = "H01"
    title = "the role a line lost"
    SRC = {
        "munada": {"book": "Iẓhār al-Asrār (Birgivî), Arabic matn", "file": "research/sources/izhar-al-asrar-matn-lithograph.txt", "locator": "al-munādā / line 195",
                   "quote": "وإن كان مضافا أو مشابها به أو نكرة ينصب بفعل مقدر نحو يا عبد الله"},
        "idafa": {"book": "Iẓhār al-Asrār (Birgivî), Arabic matn", "file": "research/sources/izhar-al-asrar-matn-lithograph.txt", "locator": "al-majrūrāt / line 175",
                  "quote": "والثاني المجرور بالإضافة"},
        "jarr": {"book": "Iẓhār al-Asrār (Birgivî), Arabic matn", "file": "research/sources/izhar-al-asrar-matn-lithograph.txt", "locator": "ḥurūf al-jarr / line 30",
                 "quote": "حروف الجر وحروف الإضافة وهي عشرون: الباء للإلصاق"},
        "ghayr": {"book": "Iẓhār al-Asrār (Birgivî), Arabic matn", "file": "research/sources/izhar-al-asrar-matn-lithograph.txt", "locator": "al-mustathnā / line 122",
                  "quote": "وأصل غير أن يكون صفة ويحمل على إلا في الاستثناء ويعرب كإعراب المستثنى بإلا على التفصيل"},
        "kana": {"book": "Iẓhār al-Asrār (Birgivî), Arabic matn", "file": "research/sources/izhar-al-asrar-matn-lithograph.txt", "locator": "al-ʿāmil fī ismayn / line 20",
                 "quote": "والعامل في اسمين على قسمين أيضا: قسم منصوب قبل مرفوعه، وقسم على العكس"},
    }
    source = SRC["munada"]

    def candidates(self, toks, prev=None):
        return [i for i, t in enumerate(toks) if re.match(r"^\s", (t.get("irab") or {}).get("ar") or "")]

    def rewrite(self, tok, toks=None, j=None):
        ir = tok.get("irab") or {}
        ar, en, tr = N(ir.get("ar")).strip(), (ir.get("en") or "").lstrip(" ;"), (ir.get("tr") or "").lstrip(" ;")
        pv = toks[j - 1] if j else {}
        pl = N((pv.get("irab") or {}).get("ar"))
        nx = bare((toks[j + 1].get("surface") or {}).get("full")) if j + 1 < len(toks) else ""
        undup = lambda a: re.sub(r"،\s*وَهُوَ مُضَافٌ،", "،", re.sub(r"،\s*مُضَافٌ(?=\.?$)", "", a))
        if pl.startswith("حَرْفُ نِدَاءٍ"):
            self.source = self.SRC["munada"]
            return {"ar": "مُنَادًى مُضَافٌ مَنْصُوبٌ " + undup(ar), "en": "A vocative in annexation, in nasb; " + re.sub(r";\s*annexed(?: \(mudaf\))?(?=\.?$|[;,])", "", en),
                    "tr": "Muzâf münâdâ, mansûb; " + re.sub(r";\s*muzâf(?=\.?$|[;,])", "", tr)}
        if pl.startswith("نَعْتٌ") and bare((pv.get("surface") or {}).get("full")).lstrip("و") in ("بن", "ابن", "بنت"):
            self.source = self.SRC["idafa"]
            return {"ar": "مُضَافٌ إِلَيْهِ مَجْرُورٌ " + ar, "en": "The annexed noun (mudaf ilayh), in jarr; " + en, "tr": "Muzâfun ileyh, mecrûr; " + tr}
        m = re.match(r"^«(عَنْ|مِنْ|إِلَى|فِي|عَلَى)» حَرْفُ جَرٍّ", pl)
        if m:
            self.source = self.SRC["jarr"]
            return {"ar": f"مَجْرُورٌ بِـ«{m.group(1)}» " + ar, "en": "In jarr after the preposition; " + en, "tr": "Harf-i cerle mecrûr; " + tr}
        if bare((tok.get("surface") or {}).get("full")) == "غير" and nx.startswith("أن"):
            self.source = self.SRC["ghayr"]
            return {"ar": "اسْمٌ مَنْصُوبٌ عَلَى الِاسْتِثْنَاءِ " + ar, "en": "A noun in nasb as the exception (istithnāʾ); " + en, "tr": "İstisna olarak mansûb isim; " + tr}
        k = next((i for i in range(j - 1, -1, -1) if re.search(r"نَاقِصٌ.*وَخَبَرُهَا .*مُقَدَّمٌ", N((toks[i].get("irab") or {}).get("ar")))), None)
        if k is not None and "مُقَدَّرَةٍ" in ar:
            self.source = self.SRC["kana"]
            return {"ar": "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ " + ar.rstrip(".") + "، وَهُوَ مُضَافٌ.", "en": "The noun of كَانَ (placed after its predicate), in raf'; " + en.rstrip(".") + "; annexed (mudaf).",
                    "tr": "Kâne'nin ismi (haberinden sonraya bırakılmış), merfû; " + tr.rstrip(".") + "; muzâf."}
        return None


class AmrTakidRule(IrabRule):
    """S01 — a recited row of emphatic forms right after the row of the IMPERATIVE («وَبِالتَّأْكِيدِ …» after «فِي الْأَمْرِ …»)
    holds imperatives, built, never a muḍāriʿ in rafʿ or jazm. The line is built from the cell's ending."""
    id = "S01"
    title = "the emphatic imperative row"
    source = {"book": "Marāḥ al-Arwāḥ (Ibn Masʿūd), matn", "file": "research/sources/marah-al-arwah-matn.txt", "locator": "bāb al-lafīf, وَقَى / line 517",
              "quote": "الأمر: قِ قِيَا قُوْا قِيْ قِيْنَ و تقول بنون التاكيد قِيَنَّ قِيَانِّ قُنَّ قِنَّ قِيَانِّ قِيْنَانِّ"}
    source2 = {"book": "Iẓhār al-Asrār (Birgivî), Arabic matn", "file": "research/sources/izhar-al-asrar-matn-lithograph.txt", "locator": "al-mabnī / line 186",
               "quote": "والمبني على نوعين: مبني الأصل ومبني العارض، والأول أربعة الحرف والماضي والأمر بغير اللام عند البصريين"}
    TAKID = re.compile(r"^(?:و?ب)?(?:التأكيد|التاكيد|نون التأكيد|نون التاكيد)$")
    L_FATH = {"ar": "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الثَّقِيلَةِ، وَالنُّونُ حَرْفُ تَوْكِيدٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ أَنْتَ.",
              "en": "An imperative built on fatḥa because the heavy nūn of emphasis is attached; the heavy nūn is a particle of emphasis; its doer is a hidden «you».",
              "tr": "Emir fiili; şeddeli (sakîle) te'kid nûnuna bitiştiği için fetha üzere mebnî; şeddeli (sakîle) nûn te'kid harfi; fâili gizli «sen»."}
    L_DUAL = {"ar": "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَنُونُ التَّوْكِيدِ الثَّقِيلَةُ مَكْسُورَةٌ بَعْدَ الْأَلِفِ.",
              "en": "An imperative built on the dropping of the nūn; the alif of the dual is its doer, and the heavy nūn of emphasis takes a kasra after the alif.",
              "tr": "Emir fiili, nûnun hazfi üzere mebnî; tesniye elifi fâil, şeddeli te'kid nûnu eliften sonra kesrelidir."}
    L_WAW = {"ar": "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَوَاوُ الْجَمَاعَةِ الْمَحْذُوفَةُ لِالْتِقَاءِ السَّاكِنَيْنِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالضَّمَّةُ دَلِيلٌ عَلَيْهَا، وَالنُّونُ حَرْفُ تَوْكِيدٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.",
             "en": "An imperative built on the dropping of the nūn; the wāw of the group, dropped where two quiescent letters met, is its doer — the ḍamma points to it; the heavy nūn is a particle of emphasis.",
             "tr": "Emir fiili, nûnun hazfi üzere mebnî; iki sâkinin buluşmasıyla düşen cemâat vâvı fâil; zamme ona delildir; şeddeli (sakîle) nûn te'kid harfi."}
    L_YA = {"ar": "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ الْمَحْذُوفَةُ لِالْتِقَاءِ السَّاكِنَيْنِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْكَسْرَةُ دَلِيلٌ عَلَيْهَا، وَالنُّونُ حَرْفُ تَوْكِيدٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.",
            "en": "An imperative built on the dropping of the nūn; the yāʾ of the woman addressed, dropped where two quiescent letters met, is its doer — the kasra points to it; the heavy nūn is a particle of emphasis.",
            "tr": "Emir fiili, nûnun hazfi üzere mebnî; iki sâkinin buluşmasıyla düşen muhâtaba yâ'sı fâil; kesre ona delildir; şeddeli (sakîle) nûn te'kid harfi."}
    L_FEM = {"ar": "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْأَلِفُ فَاصِلَةٌ بَيْنَ النُّونَاتِ، وَنُونُ التَّوْكِيدِ الثَّقِيلَةُ مَكْسُورَةٌ بَعْدَهَا.",
             "en": "An imperative built on sukūn because the women's nūn is attached; that nūn is its doer, an alif parts the nūns, and the heavy nūn of emphasis follows with a kasra.",
             "tr": "Emir fiili; nûn-ı nisveye bitiştiği için sükûn üzere mebnî, nûn fâil; elif nûnların arasını ayırır, ardından kesreli şeddeli te'kid nûnu gelir."}

    def candidates(self, toks, prev=None):
        if not toks or not prev or not self.TAKID.match(bare((toks[0].get("surface") or {}).get("full"))): return []
        if not any(bare((t.get("surface") or {}).get("full")) in ("الأمر", "أمرت") for t in prev): return []
        return [i for i, t in enumerate(toks) if i and N((t.get("irab") or {}).get("ar")).startswith("فِعْلٌ مُضَارِعٌ")]

    def rewrite(self, tok, toks=None, j=None):
        f = N((tok.get("surface") or {}).get("full"))
        if re.search(r"نَانِّ$", f): return dict(self.L_FEM)
        if re.search(r"َانِّ$", f): return dict(self.L_DUAL)
        if re.search(r"[^و]ُنَّ$", f): return dict(self.L_WAW)
        if re.search(r"[^ي]ِنَّ$", f): return dict(self.L_YA)
        if re.search(r"َنَّ$", f): return dict(self.L_FATH)
        return None


class IbnNatRule(IrabRule):
    """D07 — «بْنُ» written WITHOUT its alif stands between two names and is the naʿt of the first; a nisba after the
    name («الْكُوفِيُّ») is a naʿt too. Neither is a doer: the doer is the name the chain opens with."""
    id = "D07"
    title = "ibn between two names, and the nisba"
    source = {"book": "Iẓhār al-Asrār (Birgivî), Arabic matn", "file": "research/sources/izhar-al-asrar-matn-lithograph.txt", "locator": "al-maʿmūl bi-l-tabaʿiyya, al-ṣifa / line 137",
              "quote": "وعاملها عامل متبوعها وإعرابها كإعرابه. الأول الصفة وهي تابع يدل على معنى في متبوعه مطلقا"}

    def candidates(self, toks, prev=None):
        out = []
        for i, t in enumerate(toks):
            f, a = N((t.get("surface") or {}).get("full")), N((t.get("irab") or {}).get("ar"))
            if not a.startswith("فَاعِلٌ"): continue
            if f.startswith("بْن") and i >= 1 and i + 1 < len(toks): out.append(i)                    # بْنُ: the alif is dropped only between two names
            elif re.search(r"ِيُّ$", f) and i >= 2 and bare(f).startswith("ال") and any(N((toks[k].get("surface") or {}).get("full")).startswith("بْن") for k in range(max(0, i - 3), i)):
                out.append(i)                                                                         # the nisba closing «X bnu Y»
        return out

    def rewrite(self, tok, toks=None, j=None):
        a = N((tok.get("irab") or {}).get("ar"))
        k = j - 1                                     # the name this one qualifies: back over the chain to the word the line calls fāʿil
        isdoer = lambda x: N((toks[x].get("irab") or {}).get("ar")).startswith("فَاعِلٌ") and not N((toks[x].get("surface") or {}).get("full")).startswith("بْن")
        while k > 0 and not isdoer(k): k -= 1
        if not isdoer(k) or k == j: return None
        e = k + 1                                     # the name runs from the doer to the first «بْن» after it: «عَبْدُ الْمَلِكِ»
        while e < j and not N((toks[e].get("surface") or {}).get("full")).startswith("بْن"): e += 1
        head = " ".join(N((toks[x].get("surface") or {}).get("full")) for x in range(k, e))
        mud = "، مُضَافٌ" if "مُضَافٌ" in a else ""
        return {"ar": f"نَعْتٌ لِـ«{head}» مَرْفُوعٌ مِثْلُهُ بِالضَّمَّةِ{mud}.",
                "en": f"An attribute (naʿt) of «{head}», in rafʿ like it; the sign is the damma" + ("; annexed (mudaf)." if mud else "."),
                "tr": f"«{head}» kelimesinin na'tı, onun gibi merfû; alâmeti damme ile" + ("; muzâf." if mud else ".")}


class ZarfSingularRule(IrabRule):
    """D06 — a singular whose own last letters are ين/ون (حِين، دُون) given the sound plural's sign. Taking the ending off
    leaves one letter: the ending is its root, and the sign is the vowel it shows."""
    id = "D06"
    title = "a singular given the plural's sign"
    source = {"book": "Iẓhār al-Asrār (Birgivî), Arabic matn", "file": "research/sources/izhar-al-asrar-matn-lithograph.txt", "locator": "iʿrāb al-ism, tāmm bi-l-ḥarakāt / line 162",
              "quote": "فهو الاسم المفرد والجمع المكسر المنصرفان نحو جاءني رجل ورجال ورأيت رجلا ورجالا ومررت برجل ورجال"}

    @staticmethod
    def stem(f):
        b = re.sub(r"^(?:[وف]?(?:بال|لل|كال|ال)|[وف])(?=..)", "", bare(f)); b = re.sub(r"(?:كم|هم|هما|هن|ها|نا|ه|ك)$", "", b)
        return len(re.sub(r"(?:ون|ين)$", "", b))

    def candidates(self, toks, prev=None):
        return [i for i, t in enumerate(toks) if re.search(r"بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ|بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", N((t.get("irab") or {}).get("ar")))
                and self.stem((t.get("surface") or {}).get("full")) < 2]

    def rewrite(self, tok, toks=None, j=None):
        ir = tok.get("irab") or {}; a = N(ir.get("ar"))
        sign = ("بِالْفَتْحَةِ", "fatha", "fetha") if "مَنْصُوبٌ" in a else ("بِالْكَسْرَةِ", "kasra", "kesre") if "مَجْرُورٌ" in a else ("بِالضَّمَّةِ", "damma", "damme")
        na = re.sub(r"بِال(?:ْ)?(?:يَاءِ|وَاوِ) لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", sign[0], a)
        ne = re.sub(r"the sign is the (?:ya|waw) — a sound masculine plural", "the sign is the " + sign[1], ir.get("en") or "")
        nt = re.sub(r"alâmeti (?:yâ|vâv) ile — cem'-i müzekker sâlim", "alâmeti " + sign[2] + " ile", ir.get("tr") or "")
        if na == a or ne == ir.get("en") or nt == ir.get("tr"): return None
        return {"ar": na, "en": ne, "tr": nt}


RULES = [AmmaFaRule(), HeadlessLineRule(), AmrTakidRule(), IbnNatRule(), ZarfSingularRule()]


def main():
    write = "--write" in sys.argv
    only = sys.argv[sys.argv.index("--rule") + 1] if "--rule" in sys.argv else None
    import review_batch as rb
    pre = ROOT / "review/ai-precheck"
    done = set()
    if (pre / "applied.jsonl").is_file():
        for l in (pre / "applied.jsonl").read_text(encoding="utf-8").splitlines():
            if l.strip():
                a = json.loads(l); done.add((a["package"], a["where"]))
    log, unknown = [], []
    for p in rb.pending_packages():
        pk = json.loads((p / "manifest.json").read_text(encoding="utf-8"))["id"]
        for f in sorted((p / "chapters").glob("*.json"), key=lambda q: int(q.stem)):
            ch = json.loads(f.read_text(encoding="utf-8")); changed = False
            prev = None
            for sen in ch["sentences"]:
                toks = sen.get("tokens") or []
                for r in RULES:
                    if only and r.id != only: continue
                    for j in r.candidates(toks, prev):
                        where = f"{ch.get('chapter', f.stem)}:{sen['id']}:{j}"
                        if (pk, where) in done: continue
                        new = r.rewrite(toks[j], toks, j)
                        if new is None: unknown.append((r.id, pk, where, N((toks[j].get("irab") or {}).get("ar"))[:80])); continue
                        log.append({"rule": r.id, "package": pk, "where": where, "surface": N(toks[j]["surface"]["full"]),
                                    "before": dict(toks[j].get("irab") or {}), "after": new, "source": dict(r.source),
                                    **({"source2": r.source2} if getattr(r, "source2", None) else {}), "model": "claude-opus-5-5", "by": "ai", "confirmed_by_human": False})
                        toks[j]["irab"] = new; changed = True
                prev = toks
            if write and changed: f.write_text(json.dumps(ch, ensure_ascii=False, indent=1), encoding="utf-8")
    for c in log: print(f"{c['rule']} {c['package']} {c['where']} {c['surface']}\n   - {c['before'].get('ar', '')[:90]}\n   + {c['after']['ar'][:90]}")
    for u in unknown: print("UNKNOWN SHAPE", *u)
    print(f"{len(log)} lines rewritten, {len(unknown)} left for a reader" + ("" if write else " — dry run"))
    if write and log:
        with open(pre / "rule-applied.jsonl", "a", encoding="utf-8") as fh:
            for c in log: fh.write(json.dumps(c, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
