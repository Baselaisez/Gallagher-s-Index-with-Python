"""(v352-U) item 2 — «how the grammarians know»: al-Iqtirāḥ's own plan (the muqaddimāt, then السماع، الإجماع، القياس with its four pillars
الأصل، الفرع، الحكم، العلة، الاستصحاب، أدلة شتى، التعارض والترجيح، أحوال المستنبط) → content/rules/usul_nahw.json.
Each proof: al-Suyūṭī's defining sentence verbatim with its page (where he quotes Ibn al-Anbārī for it, `by` says so), our rendering; its
sub-topics from toc_iqtirah.json with the first sentence under each heading (verbatim, by script, Arabic only); and every place in the
proof's span where al-Suyūṭī names Ibn Jinnī / al-Khaṣāʾiṣ, with the passage FOUND in al-Khaṣāʾiṣ by script (first words of the quotation,
letters-only match) — its Shamela page, bāb and the verbatim line. Matn only: the hashiya is the modern editor's «الإصباح».
Run after build_toc.py: python3 tools/usul/build_usul.py"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from src import ROOT, matn_lines, norm, on_page, pages  # noqa: E402

PUNCT = re.compile(r"[^ء-ي\s]")


def nwords(s):
    return PUNCT.sub(" ", norm(s)).split()


# the defining sentences, chosen by reading (page, verbatim, by, en, tr)
PROOFS = [
    {"id": "usul", "ar_name": "أصول النحو", "kitab": None, "span": [10, 50],
     "def": (11, "أصول النحو: علم يبحث فيه عن أدلة النحو الإجمالية, من حيث هي أدلته, وكيفية الاستدلال بها, وحال المستدل.", "suyuti"),
     "en": "Uṣūl al-naḥw is a science that studies the proofs of grammar in general — as proofs — how one argues from them, and the one who argues.",
     "tr": "Usûlü'n-nahv, nahvin icmâlî delillerini — delil olmaları yönünden —, onlarla nasıl istidlâl edileceğini ve istidlâl edenin hâlini inceleyen ilimdir.",
     "also": [(12, "وأدلة النحو الغالبة أربعة.", "suyuti", "The proofs of grammar, mostly, are four.", "Nahvin delilleri çoğunlukla dörttür."),
              (12, "أدلة النحو ثلاثة: السماع, والإجماع, والقياس", "ibn-jinni", "Ibn Jinnī: the proofs of grammar are three — hearing, consensus and analogy.",
               "İbn Cinnî: nahvin delilleri üçtür — semâ', icmâ' ve kıyas."),
              (12, "أدلة النحو ثلاثة: نقل, وقياس, واستصحاب حال", "ibn-al-anbari", "Ibn al-Anbārī: three — transmission, analogy and presumption of the original state.",
               "İbnü'l-Enbârî: üçtür — nakil, kıyas ve istishâb-ı hâl.")]},
    {"id": "sama", "ar_name": "السماع", "kitab": "الكتاب الأول", "span": [51, 140],
     "def": (52, "وأعني به ما ثبت في كلام من يوثق بفصاحته, فشمل كلام الله تعالى, وكلام نبيه صلى الله عليه وسلم, وكلام العرب, قبل بعثته, وفي زمنه, وبعده, إلى أن فسدت الألسنة بكثرة المولدين, نظما ونثرا, عن مسلم أو كافر.", "suyuti"),
     "en": "By it I mean what is established in the speech of those whose eloquence is trusted: God's word, His Prophet's, and the Arabs' — before, during and after his mission, until tongues were spoilt by the many non-native-born — verse and prose, from Muslim or unbeliever.",
     "tr": "Bununla, fasâhatine güvenilenlerin sözünde sabit olanı kastediyorum: Allah'ın kelâmı, Peygamberinin sözü ve Arapların sözü — bi'setten önce, zamanında ve sonra, muvalledlerin çoğalmasıyla diller bozulana dek —, nazım ve nesir, Müslümandan da kâfirden de."},
    {"id": "ijma", "ar_name": "الإجماع", "kitab": "الكتاب الثاني", "span": [141, 155],
     "def": (142, "والمراد به إجماع نحاة البلدين: البصرة والكوفة", "suyuti"),
     "en": "What is meant is the consensus of the grammarians of the two cities, Basra and Kufa.",
     "tr": "Kastedilen, iki şehrin — Basra ve Kûfe — nahivcilerinin icmâıdır."},
    {"id": "qiyas", "ar_name": "القياس", "kitab": "الكتاب الثالث", "span": [156, 326],
     "def": (157, "هو حمل غير المنقول على المنقول إذا كان في معناه", "ibn-al-anbari"),
     "en": "(Ibn al-Anbārī:) it is carrying what is not transmitted over to what is transmitted, when it is of the same import.",
     "tr": "(İbnü'l-Enbârî:) nakledilmeyeni, aynı mânâda olduğunda nakledilene hamletmektir.",
     "also": [(157, "وهو معظم أدلة النحو، والمعول في غالب مسائله عليه", "suyuti", "It is the greater part of grammar's proofs; most of its questions rest on it.",
               "Nahvin delillerinin büyüğüdür; meselelerinin çoğunda dayanak odur."),
              (163, "للقياس أربعة أركان: أصل وهو المقيس عليه وفرع وهو المقيس وحكم وعلة جامعة", "suyuti",
               "Analogy has four pillars: the source (what is measured against), the branch (what is measured), the ruling, and the uniting reason.",
               "Kıyasın dört rüknü vardır: asıl (kendisine kıyas edilen), fer' (kıyas edilen), hüküm ve câmi' illet.")],
     "pillars": [
         {"id": "asl", "ar_name": "الأصل", "heading": "الفصل الأول", "span": [164, 190],
          "def": (164, "من شرطه ألا يكون شاذا خارجا عن سنن القياس", "suyuti"),
          "en": "Its condition: it must not be anomalous, outside the ways of analogy.", "tr": "Şartı: şâz, kıyas yolunun dışında olmamasıdır."},
         {"id": "far", "ar_name": "الفرع", "heading": "الفصل الثاني", "span": [191, 194],
          "def": (191, "ما قيس على كلام العرب فهو من كلام العرب", "al-mazini"),
          "en": "(al-Māzinī:) what is formed by analogy on the Arabs' speech is the Arabs' speech.", "tr": "(Mâzinî:) Arapların sözüne kıyas edilen, Arapların sözündendir."},
         {"id": "hukm", "ar_name": "الحكم", "heading": "الفصل الثالث", "span": [195, 198],
          "def": (195, "إنما يقاس على حكم ثبت استعماله عن العرب.", "suyuti"),
          "en": "One draws analogy only on a ruling whose use by the Arabs is established.", "tr": "Ancak Araplardan kullanımı sabit olan bir hükme kıyas edilir."},
         {"id": "illa", "ar_name": "العلة", "heading": "الفصل الرابع", "span": [199, 326],
          "def": (163, "والعلة الجامعة هي الإسناد", "ibn-al-anbari"),
          "en": "(Ibn al-Anbārī's example:) the uniting reason is the predication (isnād) — the nāʾib al-fāʿil is rafʿ like the fāʿil because a verb is predicated of it.",
          "tr": "(İbnü'l-Enbârî'nin misali:) câmi' illet isnaddır — nâib-i fâil, fiil kendisine isnad edildiği için fâil gibi merfûdur."}]},
    {"id": "istishab", "ar_name": "الاستصحاب", "kitab": "الكتاب الرابع", "span": [327, 333],
     "def": (328, "هو إبقاء حال اللفظ على ما يستحقه في الأصل عند عدم دليل النقل عن الأصل", "ibn-al-anbari"),
     "en": "(Ibn al-Anbārī:) keeping a word in the state it has by origin, when there is no proof that moves it from the origin.",
     "tr": "(İbnü'l-Enbârî:) asıldan çıkaran bir delil yokken lafzı asılda hak ettiği hâl üzere bırakmaktır."},
    {"id": "shatta", "ar_name": "أدلة شتى", "kitab": "الكتاب الخامس", "span": [334, 352],
     "def": (12, "ودونها الاستقراء والاستحسان, وعدم النظير, وعدم الدليل, المعقود لها الكتاب الخامس.", "suyuti"),
     "en": "Below them: induction, preference (istiḥsān), the lack of a parallel and the lack of a proof — the fifth book is given to these.",
     "tr": "Bunların altında: istikrâ, istihsân, nazîrin yokluğu ve delilin yokluğu — beşinci kitap bunlara ayrılmıştır."},
    {"id": "taarud", "ar_name": "التعارض والترجيح", "kitab": "الكتاب السادس", "span": [353, 393],
     "def": (354, "إذا تعارض نقلان أخذ بأرجحهما والترجيح في شيئين:", "ibn-al-anbari"),
     "en": "(Ibn al-Anbārī:) when two transmissions conflict, the stronger is taken; preference is by two things (the chain and the text).",
     "tr": "(İbnü'l-Enbârî:) iki nakil çatışınca daha râcih olanı alınır; tercih iki şeyledir (isnad ve metin)."},
    {"id": "mustanbit", "ar_name": "أحوال مستنبط هذا العلم", "kitab": "الكتاب السابع", "span": [394, 405], "def": None},
]
BY = {"suyuti": "السيوطي", "ibn-jinni": "ابن جني", "ibn-al-anbari": "ابن الأنباري", "al-mazini": "المازني"}
CITE = re.compile(r"(قال ابن جني(?: في \(?الخصائص\)?)?|قال في \(?الخصائص\)?|وفي الخصائص|وقال في موضع آخر(?: من الخصائص)?|وهذا موضع آخر من الخصائص)\s*:?\s*")


def kh_index():
    t, ps = pages("khasais")
    toc = json.loads((ROOT / "content/rules/toc_khasais.json").read_text(encoding="utf-8"))["babs"]
    idx = []
    for p in ps:
        raw = t[p["start"]:p["matn_end"]]
        # letters-only stream with a map back to raw offsets
        chars, pos = [], []
        for i, ch in enumerate(raw):
            c = norm(ch)
            if not c:
                continue
            if not re.match(r"[ء-ي]", c):
                if chars and chars[-1] != " ":
                    chars.append(" "); pos.append(i)
                continue
            chars.append(c); pos.append(i)
        idx.append((p, raw, "".join(chars), pos))
    def bab_of(sp):
        for b in toc:
            if b["from"]["shamela"] <= sp <= b["to"]["shamela"]:
                return b
        return None
    return idx, bab_of


def find_kh(q, idx, n=7):
    w = nwords(q)
    if len(w) < 4:
        return None
    key = " ".join(w[:n])
    for p, raw, s, pos in idx:
        k = s.find(key)
        if k != -1:
            a = pos[k]
            end = raw.find("\n", a)
            end = len(raw) if end == -1 else end
            cut = raw[a:end]
            if len(cut) > 260:
                m = re.search(r"[.؟!]\s", cut[120:260])
                cut = cut[:120 + m.end()].rstrip() if m else cut[:260]
            return {"shamela": p["sp"], "page": f"{p['vol']}:{p['pp']}", "ar": cut.strip()}
    return None


_BG = {}


def bigrams(ws):
    return {a + " " + b for a, b in zip(ws, ws[1:])}


def find_kh_fuzzy(q, idx):
    """al-Suyūṭī abridges («فلخصت منه»): the page sharing most word bigrams with the quotation's first 30 words, if ≥ 4 and ≥ 40 %;
    the cut is that page's line sharing most bigrams — verbatim from the page."""
    qb = bigrams(nwords(q)[:30])
    if len(qb) < 6:
        return None
    best = None
    for p, raw, s, pos in idx:
        if p["sp"] not in _BG:
            _BG[p["sp"]] = bigrams(s.split())
        n = len(qb & _BG[p["sp"]])
        if n >= 4 and (best is None or n > best[0]):
            best = (n, p, raw)
    if not best or best[0] < 0.4 * len(qb):
        return None
    n, p, raw = best
    ln = max((l for l in raw.split("\n") if l.strip()), key=lambda l: len(qb & bigrams(nwords(l))))
    cut = ln.strip()
    if len(cut) > 260:
        m = re.search(r"[.؟!]\s", cut[120:260])
        cut = cut[:120 + m.end()].rstrip() if m else cut[:260]
    return {"shamela": p["sp"], "page": f"{p['vol']}:{p['pp']}", "ar": cut, "match": f"bigrams {n}/{len(qb)}"}


def citations():
    t, ps, lines = matn_lines("iqtirah")
    idx, bab_of = kh_index()
    out = []
    for i, (p, ln, off) in enumerate(lines):
        for m in CITE.finditer(ln):
            if m.group(1).startswith("وقال في موضع آخر") and not (out and out[-1]["iqtirah"]["shamela"] >= p["sp"] - 2):
                continue
            rest = ln[m.end():].strip().lstrip('"').strip()
            j = i + 1
            while len(nwords(rest)) < 5 and j < len(lines) and lines[j][0] is p:
                rest = (rest + " " + lines[j][1].strip().lstrip('"')).strip(); j += 1
            j2, more = j, rest
            while len(nwords(more)) < 30 and j2 < len(lines) and lines[j2][0]["sp"] in (p["sp"], p["sp"] + 1):
                more = more + " " + lines[j2][1]; j2 += 1
            hit = find_kh(rest, idx) or find_kh(" ".join(rest.split()[1:]), idx) or find_kh_fuzzy(more, idx)
            src_line = ln.strip()
            e = {"iqtirah": {"shamela": p["sp"], "page": f"{p['vol']}:{p['pp']}", "ar": src_line[:300] if len(src_line) <= 300 else src_line[:300]},
                 "formula": m.group(1)}
            if hit:
                b = bab_of(hit["shamela"])
                e["khasais"] = {**hit, "bab_n": b and b["n"], "bab_ar": b and b["ar"]}
            out.append(e)
    return out


def first_sentence(lines, sp, heading, title):
    """the first sentence under a heading (verbatim; the line after the heading / its «في …» title)."""
    for i, (p, ln, off) in enumerate(lines):
        if p["sp"] == sp and ln.strip() == heading:
            j = i + 1
            if title and j < len(lines) and lines[j][1].strip() == title:
                j += 1
            while j < len(lines) and (not lines[j][1].strip() or re.match(r"^(فيه|فيها|وفيه) (مسائل|مسألتان):?$", lines[j][1].strip())):
                j += 1
            if j < len(lines) and lines[j][0]["sp"] in (sp, sp + 1):
                s = lines[j][1].strip()
                m = re.search(r"[.؟]", s[25:])
                s = s[:25 + m.end()] if m and 25 + m.end() <= 240 else s[:240]
                return {"shamela": lines[j][0]["sp"], "ar": s}
    return None


def main():
    t, ps = pages("iqtirah")
    vp = {p["sp"]: f"{p['vol']}:{p['pp']}" for p in ps}
    toc = json.loads((ROOT / "content/rules/toc_iqtirah.json").read_text(encoding="utf-8"))["headings"]
    _, _, lines = matn_lines("iqtirah")
    cites = citations()

    def dmk(d):
        sp, ar, by = d
        assert on_page("iqtirah", sp, ar, t, ps), (sp, ar)
        return {"ar": ar, "shamela": sp, "page": vp[sp], "by": by, "by_ar": BY[by]}

    def subs(a, b):
        out = []
        for h in toc:
            if a <= h["shamela"] <= b and h["level"] >= 2:
                fs = first_sentence(lines, h["shamela"], h["ar"], h.get("title"))
                out.append({"level": h["level"], "ar": h["ar"], **({"title": h["title"]} if "title" in h else {}), "shamela": h["shamela"],
                            "page": h["page"], **({"first": fs} if fs else {})})
        return out

    def node(x):
        o = {"id": x["id"], "ar_name": x["ar_name"], "span": x["span"]}
        if x.get("kitab"):
            o["kitab"] = x["kitab"]
        if x.get("heading"):
            o["heading"] = x["heading"]
        if x.get("def"):
            o["def"] = dmk(x["def"]); o["en"] = x["en"]; o["tr"] = x["tr"]
        if x.get("also"):
            o["also"] = [{**dmk(a[:3]), "en": a[3], "tr": a[4]} for a in x["also"]]
        if "pillars" in x:
            o["pillars"] = [node(y) for y in x["pillars"]]
        else:
            o["subs"] = subs(*x["span"])
        o["khasais"] = [c for c in cites if x["span"][0] <= c["iqtirah"]["shamela"] <= x["span"][1]]
        return o

    proofs = [node(x) for x in PROOFS]
    # a pillar's span sits inside the qiyās span: the qiyās node keeps only the citations outside its pillars (pp. 156–163)
    q = next(x for x in proofs if x["id"] == "qiyas")
    q["khasais"] = [c for c in q["khasais"] if c["iqtirah"]["shamela"] < 164]
    q["subs"] = subs(156, 163)
    found = sum(1 for c in cites if "khasais" in c)
    d = {"built_by": "tools/usul/build_usul.py (v352-U)",
         "about": "al-Suyūṭī's al-Iqtirāḥ, by its own plan: each proof of grammar with its defining sentence verbatim (Shamela page; `by` = whose "
                  "sentence al-Suyūṭī gives), our rendering (pending the hoca), its sub-topics from toc_iqtirah.json (first sentence under each "
                  "heading, verbatim, Arabic only) and the places he names Ibn Jinnī / al-Khaṣāʾiṣ — with the passage found in al-Khaṣāʾiṣ by "
                  "script where its first seven words match (letters only). Matn only: the hashiya («الإصباح») is the modern editor's.",
         "sources": {"iqtirah": "research/sources/al-iqtirah-suyuti-src.txt", "khasais": "research/sources/al-khasais-ibn-jinni-src.txt"},
         "counts": {"proofs": len(proofs), "pillars": 4, "citations": len(cites), "found_in_khasais": found,
                    "subs": sum(len(x.get("subs", [])) + sum(len(y.get("subs", [])) for y in x.get("pillars", [])) for x in proofs)},
         "proofs": proofs}
    (ROOT / "content/rules/usul_nahw.json").write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(d["counts"])
    for c in cites:
        if "khasais" not in c:
            print("  not found:", c["iqtirah"]["shamela"], c["iqtirah"]["ar"][:80])


if __name__ == "__main__":
    main()
