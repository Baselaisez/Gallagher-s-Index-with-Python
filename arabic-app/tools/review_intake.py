#!/usr/bin/env python3
"""review_intake.py — read the review sheets back from the hoca and the students, validate them, and turn the decisions
into work.

    python3 tools/review_intake.py <returned .xlsx/.csv files or folders> [--master reports/hoca-inceleme/master.json]
                                   [--out reports/hoca-inceleme/donus-<date>]

Accepts the student sheets (02-grup-*.xlsx, header row starting with «id») and the hoca's pattern sheet
(01-hoca-desenler.xlsx, header row starting with «No»), as .xlsx or exported .csv. Writes, in Turkish:

  dogrulama-raporu.md      every problem found in the returned sheets, by file and row: unknown ids, decisions
                           outside ONAY / RET / DÜZELT / ŞÜPHELİ, DÜZELT without a corrected iʿrāb, ŞÜPHELİ without a
                           note, a missing reviewer name, the same id decided differently in two sheets
  kararlar.json            the valid decisions, keyed by finding id (with the finding they answer)
  kok-neden-duzeltmeleri.md / .json
                           the root-cause fix list: each pattern with the hoca's decision on the pattern and the
                           students' ONAY / DÜZELT / RET counts, ranked by the core-mission order (taṣrīf/iʿlāl first,
                           then iʿrāb) and then by size; findings outside any pattern are listed as single fixes per
                           package
  supheli.md               every ŞÜPHELİ row, for the hoca
  reports/review-false-positives.jsonl
                           every RET, appended and de-duplicated by id: the AI review's false positives, which
                           review_batch.py --learn-from-rejections shows to the next review run

Nothing here edits content: the fix list is what the next engine/authoring wave works from.
"""
import argparse, csv, datetime as dt, json, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANON = {"ONAY": "ONAY", "RET": "RET", "DUZELT": "DÜZELT", "SUPHELI": "ŞÜPHELİ"}
TASRIF_FIRST = {"D02", "D08", "D11"}          # patterns that sit in verb morphology (taṣrīf/iʿlāl) — the core-mission order
ARABIC = re.compile(r"[؀-ۿ]")


def norm_decision(v):
    s = unicodedata.normalize("NFKD", str(v or "").strip()).replace("ı", "i").replace("İ", "I")
    s = "".join(ch for ch in s if not unicodedata.combining(ch)).upper()
    return CANON.get(s, None if s else "")


def read_rows(path):
    """(kind, header, [(row number, dict)]) for one returned sheet. kind is 'student' or 'patterns'."""
    if path.suffix.lower() == ".csv":
        with open(path, encoding="utf-8-sig", newline="") as fh:
            grid = [r for r in csv.reader(fh)]
    else:
        from openpyxl import load_workbook
        wb = load_workbook(path, data_only=True)
        ws = wb["İnceleme"] if "İnceleme" in wb.sheetnames else wb["Desenler"] if "Desenler" in wb.sheetnames else wb.active
        grid = [[("" if c is None else str(c)) for c in row] for row in ws.iter_rows(values_only=True)]
    for i, row in enumerate(grid):
        first = (row[0] if row else "").strip().lower()
        if first in ("id", "no"):
            hdr = [h.strip() for h in row]
            kind = "student" if first == "id" else "patterns"
            rows = []
            for j, r in enumerate(grid[i + 1:], start=i + 2):
                if not any((c or "").strip() for c in r): continue
                rows.append((j, {hdr[k]: (r[k] if k < len(r) else "") for k in range(len(hdr)) if hdr[k]}))
            return kind, hdr, rows
    return None, [], []


def col(d, prefix):
    for k, v in d.items():
        if k.lower().startswith(prefix): return (v or "").strip()
    return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--master", default=str(ROOT / "reports/hoca-inceleme/master.json"))
    ap.add_argument("--out")
    ap.add_argument("--fp", default=str(ROOT / "reports/review-false-positives.jsonl"), help="the cumulative false-positive log")
    a = ap.parse_args()
    master = json.loads(Path(a.master).read_text(encoding="utf-8"))
    F = master["findings"]; P = master.get("patterns", {})
    sheet_of = {i: name for name, ids in master.get("sheets", {}).items() for i in ids}
    out = Path(a.out) if a.out else Path(a.master).parent / f"donus-{dt.date.today():%Y-%m-%d}"
    out.mkdir(parents=True, exist_ok=True)

    files = []
    for p in map(Path, a.paths):
        files += sorted(q for q in p.rglob("*") if q.suffix.lower() in (".xlsx", ".csv")) if p.is_dir() else [p]
    problems, warnings = [], []
    decisions, pattern_dec = {}, {}
    for f in files:
        kind, hdr, rows = read_rows(f)
        if kind is None:
            problems.append((f.name, 0, "başlık satırı bulunamadı («id» ya da «No» ile başlayan satır)")); continue
        for rn, d in rows:
            dec_raw = col(d, "karar"); dec = norm_decision(dec_raw); note = col(d, "not")
            if kind == "patterns":
                pid = col(d, "no")
                if not re.fullmatch(r"D\d\d", pid): continue
                if pid not in P: problems.append((f.name, rn, f"bilinmeyen desen no «{pid}»")); continue
                if dec is None: problems.append((f.name, rn, f"geçersiz karar «{dec_raw}» (ONAY / RET / DÜZELT / ŞÜPHELİ)")); continue
                if dec == "": continue
                if dec in ("DÜZELT", "ŞÜPHELİ") and not note: problems.append((f.name, rn, f"{dec} için not gerekli"))
                pattern_dec[pid] = {"decision": dec, "note": note, "file": f.name}
                continue
            fid = col(d, "id")
            if not fid: continue
            if fid not in F: problems.append((f.name, rn, f"bilinmeyen id «{fid}»")); continue
            if dec is None: problems.append((f.name, rn, f"{fid}: geçersiz karar «{dec_raw}» (ONAY / RET / DÜZELT / ŞÜPHELİ)")); continue
            if dec == "": continue
            fixed = col(d, "düzeltilmiş"); who = col(d, "inceleyen")
            bad = False
            if dec == "DÜZELT" and not fixed: problems.append((f.name, rn, f"{fid}: DÜZELT seçilmiş ama «düzeltilmiş iʿrâb» boş")); bad = True
            if dec == "DÜZELT" and fixed and not ARABIC.search(fixed): warnings.append((f.name, rn, f"{fid}: düzeltilmiş iʿrâb Arapça görünmüyor"))
            if dec == "ŞÜPHELİ" and not note: problems.append((f.name, rn, f"{fid}: ŞÜPHELİ seçilmiş ama not boş")); bad = True
            if not who: warnings.append((f.name, rn, f"{fid}: inceleyen adı yok"))
            if sheet_of.get(fid) and Path(sheet_of[fid]).stem not in f.stem: warnings.append((f.name, rn, f"{fid}: bu id «{sheet_of[fid]}» sayfasına ait"))
            if bad: continue
            rec = {"decision": dec, "fixed": fixed, "reviewer": who, "note": note, "file": f.name, "row": rn}
            if fid in decisions and decisions[fid]["decision"] != dec:
                problems.append((f.name, rn, f"{fid}: çelişki — {decisions[fid]['file']} satır {decisions[fid]['row']} «{decisions[fid]['decision']}» dedi, burada «{dec}»"))
                decisions[fid].setdefault("conflicts", []).append(rec); continue
            decisions[fid] = rec

    # ---- outputs
    (out / "kararlar.json").write_text(json.dumps({i: dict(r, finding=F[i]) for i, r in decisions.items()}, ensure_ascii=False, indent=1), encoding="utf-8")
    L = [f"# Dönüş doğrulama raporu ({dt.date.today():%Y-%m-%d})", "", f"Okunan dosya: {len(files)} · geçerli karar: {len(decisions)} · "
         f"desen kararı: {len(pattern_dec)} · hata: {len(problems)} · uyarı: {len(warnings)}", "",
         "Karar dağılımı: " + ", ".join(f"{k} {v}" for k, v in Counter(r["decision"] for r in decisions.values()).most_common()), ""]
    if problems: L += ["## Hatalar (düzeltilip yeniden gönderilmeli)", ""] + [f"- {f} satır {r}: {m}" for f, r, m in problems] + [""]
    if warnings: L += ["## Uyarılar", ""] + [f"- {f} satır {r}: {m}" for f, r, m in warnings] + [""]
    (out / "dogrulama-raporu.md").write_text("\n".join(L), encoding="utf-8")

    by_pat = defaultdict(list)
    for i, r in decisions.items(): by_pat[F[i].get("pattern") or ""].append((i, r))
    fixes = []
    for pid, meta in P.items():
        rs = by_pat.get(pid, []); c = Counter(r["decision"] for _, r in rs)
        decided = c["ONAY"] + c["DÜZELT"] + c["RET"]
        fixes.append({"pattern": pid, "title": meta["title"], "rule": meta["fix"], "hoca": pattern_dec.get(pid),
                      "onay": c["ONAY"], "duzelt": c["DÜZELT"], "ret": c["RET"], "supheli": c["ŞÜPHELİ"],
                      "precision": round((c["ONAY"] + c["DÜZELT"]) / decided, 3) if decided else None,
                      "flagged": meta.get("flagged"), "shelf_scan": meta.get("shelf_scan"),
                      "area": "taṣrīf/iʿlāl" if pid in TASRIF_FIRST else "iʿrāb",
                      "corrections": [{"id": i, "surface": F[i]["surface"], "current": F[i]["current"], "fixed": r["fixed"] or F[i]["suggested"]}
                                      for i, r in rs if r["decision"] in ("ONAY", "DÜZELT")][:12]})
    hoca_rank = {"ONAY": 0, "DÜZELT": 1, None: 2, "ŞÜPHELİ": 3, "RET": 9}
    fixes.sort(key=lambda x: (hoca_rank.get((x["hoca"] or {}).get("decision")), 0 if x["area"] == "taṣrīf/iʿlāl" else 1, -(x["onay"] + x["duzelt"]), -(x["flagged"] or 0)))
    single = defaultdict(list)
    for i, r in by_pat.get("", []):
        if r["decision"] in ("ONAY", "DÜZELT"): single[F[i]["package"]].append((i, r))
    (out / "kok-neden-duzeltmeleri.json").write_text(json.dumps({"patterns": fixes, "single": {k: [dict(r, id=i, finding=F[i]) for i, r in v] for k, v in single.items()}},
                                                                  ensure_ascii=False, indent=1), encoding="utf-8")
    M = [f"# Kök-neden düzeltme listesi ({dt.date.today():%Y-%m-%d})", "",
         "Sıra: önce hocanın ONAY verdiği desenler, onların içinde önce taṣrīf/iʿlāl, sonra iʿrāb (CLAUDE.md: önce derinlik). "
         "RET alan desen uygulanmaz. Hiçbir içerik bu listeyle kendiliğinden değişmez; her kural ayrı bir dalga olarak uygulanır ve test edilir.", ""]
    for x in fixes:
        h = x["hoca"] or {}
        M += [f"## {x['pattern']} — {x['title']}  [{x['area']}]", "",
              f"- Hoca kararı: **{h.get('decision') or 'bekliyor'}**" + (f" — {h['note']}" if h.get("note") else ""),
              f"- Öğrenciler: ONAY {x['onay']} · DÜZELT {x['duzelt']} · RET {x['ret']} · ŞÜPHELİ {x['supheli']}"
              + (f" · isabet {x['precision']:.0%}" if x["precision"] is not None else ""),
              f"- Yapay zekânın işaretlediği: {x['flagged']} · raf taraması: {x['shelf_scan'] if x['shelf_scan'] is not None else '—'}",
              "- Önerilen kural: " + re.sub(r"^Kural:\s*", "", x["rule"]), ""]
        for cfix in x["corrections"][:5]: M.append(f"  - `{cfix['id']}` {cfix['surface']}: {cfix['current']} → **{cfix['fixed']}**")
        M.append("")
    if single:
        M += ["## Desene girmeyen tekil düzeltmeler (pakete göre)", ""]
        for pk, v in sorted(single.items(), key=lambda kv: -len(kv[1])):
            M.append(f"- {pk}: {len(v)} düzeltme (ONAY {sum(1 for _, r in v if r['decision'] == 'ONAY')}, DÜZELT {sum(1 for _, r in v if r['decision'] == 'DÜZELT')})")
    (out / "kok-neden-duzeltmeleri.md").write_text("\n".join(M) + "\n", encoding="utf-8")

    S = [f"# ŞÜPHELİ işaretlenenler — hocanın bakması için ({dt.date.today():%Y-%m-%d})", ""]
    for i, r in decisions.items():
        if r["decision"] != "ŞÜPHELİ": continue
        f = F[i]
        S += [f"- `{i}` {f['package']} {f['chapter']}:{f['sentence']} **{f['surface']}** ({r['reviewer'] or '?'})",
              f"  - şimdi: {f['current']}", f"  - öneri: {f['suggested']}", f"  - not: {r['note']}"]
    (out / "supheli.md").write_text("\n".join(S) + "\n", encoding="utf-8")

    fp = Path(a.fp)
    have = set()
    if fp.is_file():
        for line in fp.read_text(encoding="utf-8").splitlines():
            try: have.add(json.loads(line)["id"])
            except Exception: pass
    new = 0
    with open(fp, "a", encoding="utf-8") as fh:
        for i, r in decisions.items():
            if r["decision"] != "RET" or i in have: continue
            f = F[i]
            fh.write(json.dumps({"id": i, "package": f["package"], "issue_type": f["issue_type"], "field": f["field"], "pattern": f.get("pattern"),
                                 "surface": f["surface"], "current": f["current"], "suggested": f["suggested"], "reason_en": f["reason_en"],
                                 "reviewer": r["reviewer"], "note": r["note"], "date": f"{dt.date.today():%Y-%m-%d}"}, ensure_ascii=False) + "\n")
            new += 1
    hist = master.setdefault("intake", [])
    hist.append({"date": f"{dt.date.today():%Y-%m-%d}", "files": [p.name for p in files], "decisions": len(decisions), "problems": len(problems)})
    Path(a.master).write_text(json.dumps(master, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(files)} files, {len(decisions)} decisions ({dict(Counter(r['decision'] for r in decisions.values()))}), "
          f"{len(pattern_dec)} pattern decisions, {len(problems)} problems, {len(warnings)} warnings, {new} new false positives logged")
    print(f"written: {out}/dogrulama-raporu.md, kararlar.json, kok-neden-duzeltmeleri.md/.json, supheli.md; {fp}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
