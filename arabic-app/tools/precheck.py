#!/usr/bin/env python3
"""precheck.py — the AI verification-and-correction pass over the critical findings, before the students see them.

    python3 tools/precheck.py packets            # build the work packets (patterns first, then the rest by package)
    python3 tools/precheck.py check [batch …]    # validate verdict files; a citation that cannot be found is ŞÜPHELİ
    python3 tools/precheck.py status             # coverage per batch and the resume point

Everything lives in review/ai-precheck/ (committed on the precheck branch only; the owner merges):
  findings-critical.json   the critical findings with their sheet, row, pattern and sentence context (stable ids)
  packets/<batch>.json     one work packet per batch (a pattern, or a package slice)
  verdicts/<batch>.jsonl   one line per finding:
        {"id", "verdict": "AI-ONAY" | "AI-RET" | "AI-ŞÜPHELİ",
         "corrected": {"ar": …, "en": …, "tr": …}   (AI-ONAY: the corrected value of the finding's field; for an iʿrāb
                                                     field all three lines, so the line stays trilingual),
         "source": {"book": …, "file": "research/sources/….txt", "locator": "chapter / page / line", "quote": …},
         "note_tr": …, "note_en": …}
  checked/<batch>.jsonl    the verdicts after `check`: an AI-ONAY without a source, or whose quote is not found in the
                           cited file, becomes AI-ŞÜPHELİ with the reason; nothing else is changed

The rule (owner, 2026-11-17): verify against the uploaded books in the repo, not from memory; no citation, no ONAY.
"""
import json, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "review/ai-precheck"
MASTER = ROOT / "reports/hoca-inceleme/master.json"
ENGINE_FIRST = ["al-usul-al-munifa", "talkhis-al-miftah", "tasrif-al-izzi", "izhar-al-asrar", "marah-al-arwah", "al-kafiya",
                "mukhtasar-al-manar", "shudhur-al-dhahab", "min-muqaddimat-al-maqsud", "jumal-al-tadrib"]
VERDICTS = {"AI-ONAY", "AI-RET", "AI-ŞÜPHELİ"}
N = lambda s: unicodedata.normalize("NFC", s or "")


def fold(s):
    """For matching a quote against a source: no harakat or tatweel, one alif, one yāʾ/hāʾ form, no punctuation, single spaces."""
    s = re.sub(r"[ً-ْٰـ]", "", N(s))
    s = re.sub(r"[أإآٱ]", "ا", s).replace("ى", "ي").replace("ة", "ه").replace("ؤ", "و").replace("ئ", "ي")
    s = re.sub(r"[^\w\s]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def context(pkg_id):
    """{(chapter, sid): sentence} for one package, plus its folder."""
    import review_batch as rb
    for p in rb.pending_packages():
        m = json.loads((p / "manifest.json").read_text(encoding="utf-8"))
        if m["id"] != pkg_id: continue
        out = {}
        for f in (p / "chapters").glob("*.json"):
            d = json.loads(f.read_text(encoding="utf-8"))
            for s in d.get("sentences") or []: out[(int(d.get("chapter", f.stem)), s["id"])] = s
        return p, out
    return None, {}


def packets():
    sys.path.insert(0, str(ROOT / "tools"))
    slim = D / "findings-critical.json"
    if MASTER.is_file():
        master = json.loads(MASTER.read_text(encoding="utf-8"))
        row = {}
        for name, ids in master["sheets"].items():
            for k, i in enumerate(ids): row[i] = (name, k)
        crit = [dict(f, sheet=row.get(f["id"], (None, None))[0], row=row.get(f["id"], (None, None))[1])
                for f in master["findings"].values() if f["severity"] == "critical"]
    else:                                                    # the container was replaced: rebuild from the committed list
        crit = json.loads(slim.read_text(encoding="utf-8"))
    ctx = {}
    out = []
    for f in crit:
        if f["package"] not in ctx: ctx[f["package"]] = context(f["package"])
        p, sens = ctx[f["package"]]
        sid = str(f["sentence"]).split(":")[-1]
        s = sens.get((int(f["chapter"]), sid)) or {}
        toks = s.get("tokens") or []
        out.append({"id": f["id"], "sheet": f.get("sheet"), "row": f.get("row"), "pattern": f.get("pattern") or "", "package": f["package"],
                    "folder": str(p.relative_to(ROOT)) if p else None, "chapter": int(f["chapter"]), "sentence": sid,
                    "token": f["token"], "surface": f["surface"], "issue_type": f["issue_type"], "field": f["field"],
                    "current": f["current"], "suggested": f["suggested"], "reason_en": f["reason_en"], "reason_tr": f.get("reason_tr"),
                    "context": {"translation": s.get("translation"),
                                "tokens": [f"{i}\t{N((t.get('surface') or {}).get('full'))}\t{N((t.get('irab') or {}).get('ar'))}" for i, t in enumerate(toks)]},
                    "irab_now": (toks[f["token"]].get("irab") if 0 <= int(f["token"]) < len(toks) else None)})
    D.mkdir(parents=True, exist_ok=True); (D / "packets").mkdir(exist_ok=True)
    keep = ("id", "sheet", "row", "pattern", "package", "chapter", "sentence", "token", "surface", "issue_type", "field",
            "current", "suggested", "reason_en", "reason_tr", "custom_id", "severity", "run")
    slim.write_text(json.dumps([{k: f.get(k) for k in keep} for f in (out if not MASTER.is_file() else
                    [dict(c, **{k: o[k] for k in ("sheet", "row")}) for c, o in zip(sorted(crit, key=lambda x: x["id"]), sorted(out, key=lambda x: x["id"]))])],
                    ensure_ascii=False, indent=1), encoding="utf-8")
    batches = {}
    pat = defaultdict(list)
    for f in out:
        if f["pattern"]: pat[f["pattern"]].append(f)
    for pid in sorted(pat):
        rows = pat[pid]; size = 50; parts = -(-len(rows) // size)
        for j in range(parts):
            batches[f"p-{pid}-{j + 1}" if parts > 1 else f"p-{pid}"] = rows[j * len(rows) // parts:(j + 1) * len(rows) // parts]
    rest = defaultdict(list)
    for f in out:
        if not f["pattern"]: rest[f["package"]].append(f)
    order = [p for p in ENGINE_FIRST if p in rest] + sorted([p for p in rest if p not in ENGINE_FIRST], key=lambda p: -len(rest[p]))
    n = 0
    small = []
    for pk in order:
        rows = sorted(rest[pk], key=lambda f: (f["chapter"], f["sentence"], f["token"]))
        if len(rows) < 15 and pk not in ENGINE_FIRST: small += rows; continue
        parts = -(-len(rows) // 40)
        for j in range(parts):
            n += 1; batches[f"r{n:02d}-{pk}"] = rows[j * len(rows) // parts:(j + 1) * len(rows) // parts]
    for j in range(0, len(small), 40):
        n += 1; batches[f"r{n:02d}-small"] = small[j:j + 40]
    for name, rows in batches.items():
        (D / "packets" / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(out)} critical findings → {len(batches)} packets")
    for name, rows in batches.items(): print(f"  {name}: {len(rows)}")


def load_sources():
    return {str(p.relative_to(ROOT)): fold(p.read_text(encoding="utf-8", errors="ignore")) for p in (ROOT / "research/sources").glob("*.txt")}


def check(names=None):
    src = load_sources()
    (D / "checked").mkdir(parents=True, exist_ok=True)
    files = sorted((D / "verdicts").glob("*.jsonl"))
    if names: files = [f for f in files if f.stem in names]
    total = Counter()
    for vf in files:
        pk = json.loads((D / "packets" / f"{vf.stem}.json").read_text(encoding="utf-8"))
        ids = {f["id"] for f in pk}
        rows, seen, problems = [], set(), []
        for ln, line in enumerate(vf.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip(): continue
            try: v = json.loads(line)
            except json.JSONDecodeError as e: problems.append(f"line {ln}: not JSON ({e})"); continue
            if v.get("id") not in ids: problems.append(f"line {ln}: id {v.get('id')} not in the packet"); continue
            if v["id"] in seen: problems.append(f"line {ln}: {v['id']} twice"); continue
            seen.add(v["id"])
            if v.get("verdict") not in VERDICTS: problems.append(f"{v['id']}: verdict «{v.get('verdict')}»"); v["verdict"] = "AI-ŞÜPHELİ"
            if v["verdict"] == "AI-ONAY":
                s = v.get("source") or {}; q = fold(s.get("quote")); f_ = s.get("file") or ""
                why = None
                if not v.get("corrected"): why = "no corrected value"
                elif not q or len(q) < 8: why = "no citation quote"
                elif f_ not in src: why = f"cited file «{f_}» is not in research/sources"
                elif q not in src[f_]: why = "the quote was not found in the cited file"
                if why:
                    v["verdict"] = "AI-ŞÜPHELİ"; v["downgraded"] = why
                    v["note_tr"] = (v.get("note_tr") or "") + f" [Otomatik: ONAY → ŞÜPHELİ — {why}]"
            rows.append(v)
        missing = ids - seen
        (D / "checked" / f"{vf.stem}.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")
        c = Counter(r["verdict"] for r in rows); total.update(c)
        dg = sum(1 for r in rows if r.get("downgraded"))
        print(f"{vf.stem}: {len(rows)}/{len(ids)} — " + ", ".join(f"{k} {c[k]}" for k in sorted(c)) + (f"; {dg} ONAY downgraded" if dg else "")
              + (f"; MISSING {len(missing)}" if missing else "") + (f"; {len(problems)} problems" if problems else ""))
        for p in problems[:8]: print("    ", p)
    print("total:", dict(total))


def status():
    pk = sorted((D / "packets").glob("*.json"))
    done = 0
    for p in pk:
        n = len(json.loads(p.read_text(encoding="utf-8")))
        v = D / "checked" / f"{p.stem}.jsonl"
        k = sum(1 for l in v.read_text(encoding="utf-8").splitlines() if l.strip()) if v.is_file() else 0
        done += k
        print(f"{'✓' if k >= n else '…' if k else ' '} {p.stem}: {k}/{n}")
    nxt = next((p.stem for p in pk if not (D / "checked" / f"{p.stem}.jsonl").is_file()), None)
    print(f"verified {done}; resume at: {nxt or 'nothing left'}")


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "tools"))
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    {"packets": packets, "status": status}.get(cmd, lambda: check(sys.argv[2:]))()
