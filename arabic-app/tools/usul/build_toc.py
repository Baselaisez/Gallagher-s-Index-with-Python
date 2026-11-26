"""(v352-U) item 1 — index al-Khaṣāʾiṣ and al-Iqtirāḥ BY SCRIPT → content/rules/toc_khasais.json, toc_iqtirah.json.
al-Khaṣāʾiṣ: every bāb with its heading verbatim, Shamela page span, size and key terms. Vol. 1 (no index printed in this e-text):
the in-text heading lines (the book's own line preferred to Shamela's bracketed label). Vols. 2–3: the editor's printed index
(«فهرس الجزء …»: number, heading, printed page range, its sub-entries = the bāb's key terms), printed pages mapped to Shamela pages
by the page headers. al-Iqtirāḥ: kitāb → faṣl / khātima / dhikr → masʾala / farʿ / maslak / qādiḥ from its heading lines (matn
only: the hashiya is the modern editor's). Run: python3 tools/usul/build_toc.py"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from src import AR_DIG, BOOKS, ROOT, matn_lines, norm, pages  # noqa: E402

TERMS = ["القياس", "السماع", "العلة", "الإجماع", "الاستحسان", "الحمل", "الإعراب", "البناء", "الحذف", "التقديم", "الزيادة",
         "العوض", "البدل", "الإدغام", "القلب", "الهمز", "الحركة", "السكون", "الشذوذ", "الاطراد", "الأصل", "الفرع", "الضرورة",
         "المجاز", "الحقيقة", "الاشتقاق", "التصريف", "الإمالة", "النسب", "التصغير", "الجمع", "الفاعل", "المفعول", "المبتدأ",
         "الخبر", "الحال", "الاستثناء", "الإضافة", "النداء", "الصفة", "العطف", "التوكيد", "الضمير", "الجر", "النصب", "الرفع",
         "الجزم", "الوقف", "التأنيث", "اللغة", "المعنى", "اللفظ", "الشعر", "القرآن", "الكوفيين", "البصريين", "سيبويه"]


def key_terms(body):
    nb = norm(body)
    out = []
    for t in TERMS:
        stem = norm(t[2:])
        n = len(re.findall(r"(?:^|[\s(«\"،,.:؛])(?:[وفبلك]?ال)?" + re.escape(stem) + r"(?=[\s)»\"،,.:؛؟]|$)", nb))
        if n >= 3:
            out.append([t, n])
    out.sort(key=lambda x: -x[1])
    return out[:6]


def _key(h):
    h = re.sub(r"[٠-٩0-9\[\]\"()،,.:؛؟\-]", "", h)
    h = re.sub(r"^\s*(هذا )?باب\s*", "", h.strip())
    return re.sub(r"\s+", "", norm(h))


HEAD_K = re.compile(r"^\[?(?:هذا )?باب\S?\s")


def khasais():
    t, ps, lines = matn_lines("khasais")
    by_sp = {p["sp"]: p for p in ps}
    vp = {}
    for p in ps:
        vp.setdefault((p["vol"], p["pp"]), p["sp"])

    def sp_of(vol, pp):
        c = [sp for (v, q), sp in vp.items() if v == vol and q <= pp]
        return max(c) if c else None

    babs = []
    # vol. 1 — the in-text heading lines
    seen = {}
    for p, ln, off in lines:
        if p["vol"] != 1 or p["sp"] > 396:
            continue
        s = ln.strip()
        if HEAD_K.match(s) and len(s) < 110 and not re.match(r"^هذا باب (ظاهره|من|يتلقاه)", s):
            br = s.startswith("[")
            cur = seen.get(p["sp"])
            if cur is None or (cur["heading_src"] == "shamela" and not br):
                seen[p["sp"]] = {"ar": s, "heading_src": "shamela" if br else "book", "vol": 1, "from": p["sp"]}
    for sp in sorted(seen):
        babs.append({**seen[sp], "n": None, "index": None})
    # vols. 2–3 — the printed index
    ent = re.compile(r"^([٠-٩]+)[-\s]+(.*?)\s*(?:\"?([٠-٩]+)-([٠-٩]+)\"?)?[:.]?\s*$")
    hdr = {}
    for p in ps:
        hdr.setdefault(_key(p["sec"]), p["sp"])

    def by_hdr(h):
        k = _key(h)
        c = [sp for name, sp in hdr.items() if k and name and (name.startswith(k[:18]) or k.startswith(name[:18]))]
        return min(c) if len(c) == 1 else None
    for vol, rng in ((2, range(922, 934)), (3, range(1266, 1278))):
        cur = None
        for p, ln, off in lines:
            if p["sp"] not in rng or not ln.strip() or ln.startswith("["):
                continue
            m = ent.match(ln.strip())
            if m and ("باب" in m.group(2)[:6] or m.group(2).startswith("في") or m.group(2).startswith("ذكر")):
                a = int(m.group(3).translate(AR_DIG)) if m.group(3) else None
                b = int(m.group(4).translate(AR_DIG)) if m.group(4) else None
                hs = by_hdr(m.group(2))
                ps_ = sp_of(vol, a) if a else None
                if hs and ps_ and 0 < hs - ps_ <= 2 and by_sp[ps_]["sec"].startswith("المجلد"):
                    hs = None          # the bāb starts on the printed page, before Shamela's label (vol. 2's first page)
                cur = {"ar": ln.strip(), "heading_src": "index", "vol": vol, "n": int(m.group(1).translate(AR_DIG)),
                       "index": {"shamela": p["sp"], "printed": [a, b]}, "from": hs or sp_of(vol, a),
                       "from_by": "shamela_label" if hs else "printed_page", "sub": []}
                babs.append(cur)
            elif cur is not None:
                cur["sub"].append(ln.strip())
    # spans: each bāb runs to the page before the next one (vol. ends: the index / the volume's last page)
    ends = {1: 396, 2: 921, 3: 1265}
    babs.sort(key=lambda b: (b["vol"], b["from"] or 0))
    for i, b in enumerate(babs):
        nxt = babs[i + 1] if i + 1 < len(babs) and babs[i + 1]["vol"] == b["vol"] else None
        b["to"] = (nxt["from"] - 1 if nxt["from"] > b["from"] else b["from"]) if nxt else ends[b["vol"]]
    n1 = 0
    out = []
    for b in babs:
        if b["vol"] == 1:
            n1 += 1
            b["n"] = n1
        body = "".join(t[by_sp[s]["start"]:by_sp[s]["matn_end"]] for s in range(b["from"], b["to"] + 1) if s in by_sp)
        fus = [s for s in b.get("sub", []) if re.match(r"^(فصل|حذف|الفروق)", s)]
        terms = [s for s in b.get("sub", []) if s not in fus]
        out.append({"n": b["n"], "vol": b["vol"], "ar": b["ar"], "heading_src": b["heading_src"], "index": b["index"], **({"from_by": b["from_by"]} if "from_by" in b else {}),
                    "from": {"shamela": b["from"], "page": f"{by_sp[b['from']]['vol']}:{by_sp[b['from']]['pp']}"},
                    "to": {"shamela": b["to"], "page": f"{by_sp[b['to']]['vol']}:{by_sp[b['to']]['pp']}"},
                    "pages": b["to"] - b["from"] + 1, "chars": len(body), "key_terms": key_terms(body),
                    **({"index_entries": terms} if terms else {}), **({"fusul": fus} if fus else {})})
    return out, len(ps)


ORD_F = "الأولى|الثانية|الثالثة|الرابعة|الخامسة|السادسة|السابعة|الثامنة|التاسعة|العاشرة|الحادية عشرة?|الثانية عشرة?|الثالثة عشرة?|الرابعة عشرة?|الخامسة عشرة?|السادسة عشرة?"
ORD_M = "الأول|الثاني|الثالث|الرابع|الخامس|السادس|السابع|الثامن|التاسع|العاشر|الحادي عشر|الثاني عشر|الثالث عشر|الرابع عشر"
I_KITAB = re.compile(r"^(الكتاب (?:الأول|الثاني|الثالث|الرابع|الخامس|السادس|السابع)|الكلام في المقدمات)$")
I_FASL = re.compile(r"^(الفصل (?:الأول|الثاني|الثالث|الرابع)|فصل|خاتمة|فروع|ذكر مسالك العلة|ذكر القوادح في العلة)$")
I_MAS = re.compile(r"^(\(?(?:" + ORD_F + r")\)?|المسألة (?:" + ORD_F + r")|\(مسألة\)|مسألة(?: في الدور)?|الفرع الثاني|الفرع الرابع|(?:"
                   + ORD_M + r"))$")
I_MASLAK = re.compile(r"^((?:أحدها|الثاني|الثالث|الرابع|الخامس|السادس|السابع|الثامن):? [^:]{2,20}:?|(?:و)?منها \(?[^)]{2,20}\)?)$")
I_NOTE = re.compile(r"^(تنبيه(?:ان)?:?|فائدة|تذنيب)$")


def iqtirah():
    t, ps, lines = matn_lines("iqtirah")
    out, kit, fasl = [], None, None
    for i, (p, ln, off) in enumerate(lines):
        s = ln.strip()
        if p["sp"] < 10 or not s:
            continue
        nxt = lines[i + 1][1].strip() if i + 1 < len(lines) and lines[i + 1][0] is p else ""
        sub = nxt if re.match(r'^"?(في|القول في) [^.]{2,40}"?$', nxt) or re.match(r"^(فيها|فيه|وفيه) (مسائل|مسألتان):?$", nxt) else None
        lvl = None
        if I_KITAB.match(s):
            lvl = 1
        elif I_FASL.match(s):
            lvl = 2
        elif I_MAS.match(s):
            lvl = 3
        elif 254 <= p["sp"] <= 312 and I_MASLAK.match(s):
            lvl = 3
        elif I_NOTE.match(s):
            lvl = 4
        elif 334 <= p["sp"] <= 352 and I_MASLAK.match(s):
            lvl = 3
        if lvl is None:
            continue
        e = {"level": lvl, "ar": s, "shamela": p["sp"], "page": f"{p['vol']}:{p['pp']}", "section": p["sec"]}
        if sub:
            e["title"] = sub
        out.append(e)
    # spans: to the page of the next heading of the same or a higher level
    for i, e in enumerate(out):
        j = next((k for k in range(i + 1, len(out)) if out[k]["level"] <= e["level"]), None)
        e["to"] = out[j]["shamela"] if j is not None else len(ps)
    return out, len(ps)


def main():
    kb, kp = khasais()
    b = BOOKS["khasais"]
    d = {"book": "khasais", "title": {"ar": b["ar"], "en": b["en"], "tr": b["tr"]}, "source_file": "research/sources/" + b["file"],
         "built_by": "tools/usul/build_toc.py (v352-U)", "pages": kp,
         "note": "vol. 1: in-text heading lines (heading_src book / shamela); vols. 2–3: the printed index's entries (heading_src index) "
                 "with their sub-entries; key_terms = [term, count] from a fixed list of 57 technical words, by script",
         "counts": {"babs": len(kb), "vol1": sum(1 for x in kb if x["vol"] == 1), "vol2": sum(1 for x in kb if x["vol"] == 2),
                    "vol3": sum(1 for x in kb if x["vol"] == 3)}, "babs": kb}
    (ROOT / "content/rules/toc_khasais.json").write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("khasais", d["counts"])
    ib, ip = iqtirah()
    b = BOOKS["iqtirah"]
    d = {"book": "iqtirah", "title": {"ar": b["ar"], "en": b["en"], "tr": b["tr"]}, "source_file": "research/sources/" + b["file"],
         "built_by": "tools/usul/build_toc.py (v352-U)", "pages": ip,
         "note": "level 1 kitāb, 2 faṣl / khātima / dhikr, 3 masʾala / farʿ / maslak / qādiḥ, 4 tanbīh / fāʾida; matn only — the hashiya "
                 "is the modern editor's «الإصباح»; pp. 1–9 (the muqaddima listing Ibn al-Anbārī's chapters) are not headings",
         "counts": {"headings": len(ib), **{f"level{k}": sum(1 for x in ib if x["level"] == k) for k in (1, 2, 3, 4)}},
         "headings": ib}
    (ROOT / "content/rules/toc_iqtirah.json").write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("iqtirah", d["counts"])


if __name__ == "__main__":
    main()
