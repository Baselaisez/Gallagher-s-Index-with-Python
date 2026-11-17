#!/usr/bin/env python3
"""review_batch.py — an AI pre-review of every package marked `pending-scholarly-review`, for the human scholar.

It READS the packages and WRITES a report. It never edits content: every finding is a suggestion for the scholar.

    python3 tools/review_batch.py --dry-run                 # build every request, count input tokens (free), estimate cost
    python3 tools/review_batch.py --pilot 3                 # a real batch on 3 packages; measured cost + extrapolation
    python3 tools/review_batch.py --all                     # the whole shelf (only after the pilot numbers are approved)
    python3 tools/review_batch.py --collect <report dir>    # resume: poll a submitted batch and write its report

Options: --packages id,id (choose packages; with --pilot, overrides the automatic pick), --effort low|medium|high|xhigh|max
(default high), --max-findings N (per request, default 60), --no-wait (submit and exit; --collect later),
--out <dir> (default reports/review-<UTC date>).

Model: Claude Fable 5.2 through the Message Batches API (50% of standard price: $4 / $20 per MTok in / out). Thinking is
always on for this model, so no `thinking` parameter is sent; depth is set by `output_config.effort`. The answer comes
back as JSON constrained by `output_config.format`. One request per package, or per chapter when a package is large
(per chapter part when one chapter alone is very large); `custom_id` names the package and chapter, and results are
keyed by it, never by their order. The rubric and the grammar registry form one system prompt shared by every request,
marked for caching (1-hour TTL, since batch requests can be processed far apart).

Refusals: the Batches API does not accept the server-side `fallbacks` parameter. A request that ends with
`stop_reason: "refusal"` is recorded with its category and listed in `refused.json` for a re-run; one that ends at
`max_tokens` is recorded in `truncated.json`. Neither stops the run.

API key: read from the environment variable QISSA_ANTHROPIC_API_KEY, or from the gitignored arabic-app/.env.local
(a line `QISSA_ANTHROPIC_API_KEY=...`), and passed explicitly to the client. The tool never reads ANTHROPIC_API_KEY
(that variable would also move Claude Code's own billing) and never prints, logs or writes the key.
"""
import argparse, concurrent.futures as cf, datetime as dt, json, os, re, sys, time, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # arabic-app/
MODEL = "claude-fable-5-2"
PRICE = {"in": 4.00, "out": 20.00, "cache_read": 0.10, "cache_write_1h": 8.00, "cache_write_5m": 5.00}   # $/MTok, batch (50%)
MAX_TOKENS = 64000                                    # thinking + the JSON answer; a hard cap on output, billed as used
PKG_CHARS = 150_000                                   # a package whose compact text is longer is sent chapter by chapter
CHAPTER_CHARS = 220_000                               # a chapter longer than this is sent in sentence parts
ISSUE_TYPES = ["irab_ar", "irab_en", "irab_tr", "tashkeel", "lex_gloss", "grammar_id", "doctrinal_sensitivity"]
SEVERITIES = ["critical", "major", "minor"]
FIELDS = ["surface", "irab.ar", "irab.en", "irab.tr", "lex", "gloss", "grammar", "translation.en", "translation.tr", "other"]
N = lambda s: unicodedata.normalize("NFC", s or "")


# ---------------------------------------------------------------- the key
def api_key():
    k = os.environ.get("QISSA_ANTHROPIC_API_KEY", "").strip()
    if not k:
        f = ROOT / ".env.local"
        if f.is_file():
            for line in f.read_text(encoding="utf-8").splitlines():
                m = re.match(r"\s*(?:export\s+)?QISSA_ANTHROPIC_API_KEY\s*=\s*(.*)$", line)
                if m: k = m.group(1).strip().strip("'\"")
    if not k:
        sys.exit("QISSA_ANTHROPIC_API_KEY is not set (environment or arabic-app/.env.local). Stopping: no request was made.")
    return k


def client():
    import anthropic
    os.environ.pop("ANTHROPIC_AUTH_TOKEN", None)      # only the key given here authenticates this process
    return anthropic.Anthropic(api_key=api_key(), max_retries=8)


# ---------------------------------------------------------------- the content
def pending_packages():
    out = []
    for m in sorted(list((ROOT / "content/samples").glob("*/manifest.json")) + list((ROOT / "content/user-uploads").glob("*/manifest.json"))):
        man = json.loads(m.read_text(encoding="utf-8"))
        if ((man.get("attribution") or {}).get("reviewStatus") or man.get("reviewStatus")) == "pending-scholarly-review":
            out.append(m.parent)
    return out


def irab_tr_memory():
    p = ROOT / "content/i18n/irab-tr.json"
    return json.loads(p.read_text(encoding="utf-8")).get("entries", {}) if p.is_file() else {}


def one_line(s):
    return re.sub(r"\s+", " ", N(s)).strip()


def token_line(i, t, trm):
    ir = t.get("irab") or {}
    tr = ir.get("tr") or trm.get(ir.get("en") or "", "")      # the Turkish the reader shows (the builder merges the same memory)
    seg = " + ".join(f"{N(s.get('form'))}/{s.get('lex')}" for s in (t.get("segments") or []))
    parts = [str(i), N((t.get("surface") or {}).get("full")), f"lex={t.get('lex')}", f"pos={t.get('pos')}",
             "g=" + ",".join(t.get("grammar") or []), ("seg=" + seg) if seg else "",
             "AR: " + one_line(ir.get("ar")), "EN: " + one_line(ir.get("en")), "TR: " + one_line(tr)]
    return "\t".join(p for p in parts if p)


def sentence_block(ch, s, trm):
    tr = s.get("translation") or {}
    head = f"@{ch}:{s['id']}\tEN: {one_line(tr.get('en'))}\tTR: {one_line(tr.get('tr'))}"
    return "\n".join([head] + [token_line(i, t, trm) for i, t in enumerate(s.get("tokens") or [])])


def glossary_block(pkg, keys):
    g = json.loads((pkg / "glossary.json").read_text(encoding="utf-8")).get("entries", {}) if (pkg / "glossary.json").is_file() else {}
    rows = []
    for k in sorted(keys):
        e = g.get(k)
        if not e: continue
        gl = e.get("gloss") or {}
        rows.append(f"{k} | {N(e.get('lemma'))} | {e.get('pos')} | {e.get('root', '')} | {one_line(gl.get('en'))} | {one_line(gl.get('tr'))}")
    return "\n".join(rows)


def build_requests(pkgs, trm):
    """Each request: (custom_id, package id, chapters, user text, location index {ch:sid:i -> surface})."""
    reqs = []
    for pkg in pkgs:
        man = json.loads((pkg / "manifest.json").read_text(encoding="utf-8"))
        att = man.get("attribution") or {}
        head = (f"PACKAGE {man['id']} — {one_line((man.get('title') or {}).get('en'))} (level {man.get('level')})\n"
                f"PROVENANCE AND DELIBERATE READINGS (do not report these as errors):\n{one_line(att.get('en'))}\n")
        chs = []
        for f in sorted((pkg / "chapters").glob("*.json"), key=lambda p: int(p.stem)):
            d = json.loads(f.read_text(encoding="utf-8"))
            chs.append((int(d.get("chapter", f.stem)), d.get("sentences") or []))
        units = []                                    # (label, [(ch, sentence)])
        whole = [(c, s) for c, ss in chs for s in ss]
        if sum(len(sentence_block(c, s, trm)) for c, s in whole) <= PKG_CHARS:
            units.append(("", whole))
        else:
            for c, ss in chs:
                blocks = [(c, s, len(sentence_block(c, s, trm))) for s in ss]
                if sum(b[2] for b in blocks) <= CHAPTER_CHARS:
                    units.append((f"c{c}", [(c, s) for c, s, _ in blocks]))
                    continue
                part, size, k = [], 0, 1
                for c2, s, n in blocks:
                    if part and size + n > CHAPTER_CHARS:
                        units.append((f"c{c}-p{k}", part)); part, size, k = [], 0, k + 1
                    part.append((c2, s)); size += n
                if part: units.append((f"c{c}-p{k}", part))
        for label, items in units:
            cid = (man["id"] + ("--" + label if label else ""))[:64]
            keys = {t.get("lex") for _, s in items for t in s.get("tokens") or []} | {sg.get("lex") for _, s in items for t in s.get("tokens") or [] for sg in t.get("segments") or []}
            loc = {f"{c}:{s['id']}:{i}": N((t.get("surface") or {}).get("full")) for c, s in items for i, t in enumerate(s.get("tokens") or [])}
            titles = {int(x.get("n", k + 1)): ((x.get("title") or {}).get("en") or "") for k, x in enumerate(man.get("chapters") or [])}
            chap_titles = "\n".join(f"chapter {c}: {one_line(titles.get(c, ''))}" for c in sorted({c for c, _ in items}))
            text = (head + chap_titles + "\n\nGLOSSARY (key | lemma | pos | root | gloss EN | gloss TR):\n" + glossary_block(pkg, keys - {None})
                    + "\n\nSENTENCES (@chapter:sentence, then one line per token: index, word, lex key, pos, grammar note ids, segments, iʿrāb AR / EN / TR):\n"
                    + "\n".join(sentence_block(c, s, trm) for c, s in items))
            reqs.append({"custom_id": cid, "package": man["id"], "unit": label or "all", "text": text, "loc": loc})
    ids = [r["custom_id"] for r in reqs]
    assert len(ids) == len(set(ids)), "custom_id collision"
    assert all(re.fullmatch(r"[A-Za-z0-9_-]{1,64}", i) for i in ids), "custom_id outside [A-Za-z0-9_-]{1,64}"
    return reqs


# ---------------------------------------------------------------- the prompt
RUBRIC = """You are reviewing lessons of Qissa, an app that teaches Classical Arabic through classical texts and original graded stories. Every word carries an iʿrāb line in Arabic, with an English and a Turkish rendering, a glossary key, and the ids of the grammar notes it teaches. The texts are classical Islamic works (grammar, ṣarf, creed, fiqh, prophetic stories). A human scholar will sign each package off; your review is a pre-review that tells the scholar where to look first. You change nothing yourself.

Report only what a careful teacher of Arabic grammar would correct:
- irab_ar: the Arabic iʿrāb line is wrong — the office (fāʿil, mafʿūl bihi, khabar …), the case, the sign of the case, the governor, or a verb's tense, mood or build (bināʾ) — or it does not fit the ending written on the word.
- irab_en / irab_tr: the English or Turkish line does not say what the Arabic line says, or is wrong in itself.
- tashkeel: a vowel, sukūn, shadda or tanwīn on the word is wrong (including a case ending that contradicts the iʿrāb). Do not ask for marks the style leaves out.
- lex_gloss: the lex key points to the wrong lemma for this word in this place, or the glossary gloss is wrong for this use.
- grammar_id: a listed grammar note does not apply to the word, or one clearly central note is missing. Use only ids from the registry below.
- doctrinal_sensitivity: a translation or iʿrāb line could misstate a point of creed or law, or misquote the Qurʾān or a ḥadīth. Flag it for the scholar; do not rule on the doctrine yourself. "suggested" may be empty here.

Do not report: style preferences, alternative wordings that are equally correct, the transcription of the classical text itself (only its vowelling), or anything the PROVENANCE AND DELIBERATE READINGS paragraph already explains. Where the grammarians differ and the line follows a recognised view, leave it. A quoted example word («…») is cited for its wording (ḥikāya); judge its line as a cited word.

Severity: critical — a learner would absorb a wrong rule or a wrong Arabic form (wrong case or office, a vowel that changes the word, a doctrinal misstatement); major — the English or Turkish misstates the Arabic, a wrong gloss or lemma, a wrong grammar note; minor — an imprecise or incomplete line that is not wrong.

Location: give the chapter number, the sentence id and the token index exactly as written in the input, and copy the word into "surface". Use token -1 for a problem in a sentence's translation. "current" quotes the value as it stands (shorten long lines with …); "suggested" gives the corrected value in the same language as the field. Give each reason in English (reason_en) and Turkish (reason_tr), one or two short sentences each.

List at most {max_findings} findings, the most severe first. If you found more, put the number left out in more_findings_not_listed. Write summary_en and summary_tr for the scholar: two to four sentences on the overall quality of this part and the kinds of problems seen, so a reader who has not seen the text understands it.

GRAMMAR NOTE REGISTRY (id | group | title EN / TR | plain EN):
"""


def registry_text():
    rows = []
    for f in sorted((ROOT / "content/grammar").glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        t = d.get("title") or {}
        rows.append(f"{d.get('id')} | {d.get('group')} | {one_line(t.get('en'))} / {one_line(t.get('tr'))} | {one_line((d.get('plain') or {}).get('en'))}")
    return "\n".join(rows)


def system_blocks(max_findings):
    return [{"type": "text", "text": RUBRIC.replace("{max_findings}", str(max_findings)) + registry_text(),
             "cache_control": {"type": "ephemeral", "ttl": "1h"}}]


SCHEMA = {
    "type": "object",
    "properties": {
        "summary_en": {"type": "string"},
        "summary_tr": {"type": "string"},
        "overall": {"type": "string", "enum": ["clean", "minor_issues", "needs_attention", "serious_problems"]},
        "more_findings_not_listed": {"type": "integer"},
        "findings": {"type": "array", "items": {
            "type": "object",
            "properties": {
                "chapter": {"type": "integer"}, "sentence": {"type": "string"}, "token": {"type": "integer"},
                "surface": {"type": "string"},
                "issue_type": {"type": "string", "enum": ISSUE_TYPES},
                "severity": {"type": "string", "enum": SEVERITIES},
                "field": {"type": "string", "enum": FIELDS},
                "current": {"type": "string"}, "suggested": {"type": "string"},
                "reason_en": {"type": "string"}, "reason_tr": {"type": "string"},
            },
            "required": ["chapter", "sentence", "token", "surface", "issue_type", "severity", "field", "current", "suggested", "reason_en", "reason_tr"],
            "additionalProperties": False}},
    },
    "required": ["summary_en", "summary_tr", "overall", "more_findings_not_listed", "findings"],
    "additionalProperties": False,
}


def params(req, system, effort):
    return {"model": MODEL, "max_tokens": MAX_TOKENS, "system": system,
            "output_config": {"effort": effort, "format": {"type": "json_schema", "schema": SCHEMA}},
            "messages": [{"role": "user", "content": "Review this part of the shelf.\n\n" + req["text"]}]}


# ---------------------------------------------------------------- dry run
def count_all(c, reqs, system, effort):
    def one(r):
        p = params(r, system, effort)
        n = c.messages.count_tokens(model=p["model"], system=p["system"], messages=p["messages"], output_config=p["output_config"]).input_tokens
        return r["custom_id"], n
    out = {}
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for k, n in ex.map(one, reqs): out[k] = n
    return out


def estimate(counts, sys_tokens, out_ratio, out_base):
    n = len(counts)
    user_in = sum(max(0, v - sys_tokens) for v in counts.values())
    out = sum(out_base + out_ratio * max(0, v - sys_tokens) for v in counts.values())
    best = (user_in * PRICE["in"] + sys_tokens * PRICE["cache_write_1h"] + sys_tokens * (n - 1) * PRICE["cache_read"] + out * PRICE["out"]) / 1e6
    worst = (sum(counts.values()) * PRICE["in"] + out * PRICE["out"]) / 1e6       # no cache hit at all
    return {"requests": n, "user_input_tokens": user_in, "system_tokens": sys_tokens, "assumed_output_tokens": int(out),
            "cost_cache_hits_usd": round(best, 2), "cost_no_cache_usd": round(worst, 2)}


def sys_token_count(c, system, effort):
    probe = {"custom_id": "probe", "text": "."}
    full = c.messages.count_tokens(model=MODEL, system=system, messages=params(probe, system, effort)["messages"], output_config={"effort": effort, "format": {"type": "json_schema", "schema": SCHEMA}}).input_tokens
    bare = c.messages.count_tokens(model=MODEL, messages=params(probe, system, effort)["messages"], output_config={"effort": effort, "format": {"type": "json_schema", "schema": SCHEMA}}).input_tokens
    return full - bare


# ---------------------------------------------------------------- batch
def submit(c, reqs, system, effort, outdir, mode):
    from anthropic.types.messages.batch_create_params import Request
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    batch = c.messages.batches.create(requests=[Request(custom_id=r["custom_id"], params=MessageCreateParamsNonStreaming(**params(r, system, effort))) for r in reqs])
    state = {"batch_id": batch.id, "mode": mode, "effort": effort, "model": MODEL, "created": dt.datetime.now(dt.timezone.utc).isoformat(),
             "requests": {r["custom_id"]: {"package": r["package"], "unit": r["unit"], "loc": r["loc"]} for r in reqs}}
    (outdir / "batch.json").write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"submitted batch {batch.id}: {len(reqs)} requests ({mode}); state in {outdir / 'batch.json'}")
    return state


def wait(c, batch_id, every=60):
    while True:
        b = c.messages.batches.retrieve(batch_id)
        rc = b.request_counts
        print(f"{dt.datetime.now(dt.timezone.utc):%H:%M:%S} {b.processing_status}: processing {rc.processing}, succeeded {rc.succeeded}, errored {rc.errored}, expired {rc.expired}", flush=True)
        if b.processing_status == "ended": return b
        time.sleep(every)


def usage_cost(u):
    cc = getattr(u, "cache_creation", None)
    w1 = getattr(cc, "ephemeral_1h_input_tokens", None) if cc else None
    w5 = getattr(cc, "ephemeral_5m_input_tokens", None) if cc else None
    wtot = u.cache_creation_input_tokens or 0
    if w1 is None and w5 is None: w1, w5 = wtot, 0
    return (u.input_tokens * PRICE["in"] + (u.cache_read_input_tokens or 0) * PRICE["cache_read"] + (w1 or 0) * PRICE["cache_write_1h"]
            + (w5 or 0) * PRICE["cache_write_5m"] + u.output_tokens * PRICE["out"]) / 1e6


def collect(c, state, outdir):
    reqs = state["requests"]
    got, refused, truncated, failed, usage = {}, [], [], [], {}
    for res in c.messages.batches.results(state["batch_id"]):
        cid = res.custom_id
        if cid not in reqs: continue
        r = res.result
        if r.type != "succeeded":
            failed.append({"custom_id": cid, "result": r.type, "error": getattr(getattr(r, "error", None), "type", None)}); continue
        msg = r.message
        u = msg.usage
        usage[cid] = {"input": u.input_tokens, "cache_read": u.cache_read_input_tokens or 0, "cache_write": u.cache_creation_input_tokens or 0,
                      "output": u.output_tokens, "cost_usd": usage_cost(u)}
        if msg.stop_reason == "refusal":
            sd = getattr(msg, "stop_details", None)
            refused.append({"custom_id": cid, "category": getattr(sd, "category", None), "explanation": getattr(sd, "explanation", None)}); continue
        if msg.stop_reason == "max_tokens":
            truncated.append({"custom_id": cid, "output_tokens": u.output_tokens}); continue
        text = next((b.text for b in msg.content if b.type == "text"), "")
        try:
            got[cid] = json.loads(text)
        except json.JSONDecodeError as e:
            failed.append({"custom_id": cid, "result": "unparsable", "error": str(e)[:200]})
    write_report(state, got, refused, truncated, failed, usage, outdir)
    return got, usage


# ---------------------------------------------------------------- report
SEV_RANK = {s: i for i, s in enumerate(SEVERITIES)}


def write_report(state, got, refused, truncated, failed, usage, outdir):
    reqs = state["requests"]
    by_pkg = {}
    for cid, meta in reqs.items():
        by_pkg.setdefault(meta["package"], []).append(cid)
    all_findings = []
    for pkg, cids in sorted(by_pkg.items()):
        parts, findings = [], []
        for cid in sorted(cids):
            d = got.get(cid)
            if not d:
                parts.append({"custom_id": cid, "unit": reqs[cid]["unit"], "status": "missing"}); continue
            parts.append({"custom_id": cid, "unit": reqs[cid]["unit"], "overall": d.get("overall"), "summary_en": d.get("summary_en"),
                          "summary_tr": d.get("summary_tr"), "more_findings_not_listed": d.get("more_findings_not_listed", 0)})
            for f in d.get("findings") or []:
                key = f"{f.get('chapter')}:{f.get('sentence')}:{f.get('token')}"
                at = reqs[cid]["loc"].get(key)
                f = dict(f, package=pkg, custom_id=cid,
                         location_ok=(f.get("token") == -1 and any(k.startswith(f"{f.get('chapter')}:{f.get('sentence')}:") for k in reqs[cid]["loc"]))
                         or (at is not None and N(at) == N(f.get("surface"))))
                findings.append(f)
        findings.sort(key=lambda f: (SEV_RANK.get(f.get("severity"), 9), f.get("chapter") or 0, f.get("sentence") or "", f.get("token") or 0))
        all_findings += findings
        cost = sum(usage[c]["cost_usd"] for c in cids if c in usage)
        (outdir / f"{pkg}.json").write_text(json.dumps({"package": pkg, "model": state["model"], "effort": state["effort"], "batch_id": state["batch_id"],
                                                        "cost_usd": round(cost, 4), "parts": parts, "findings": findings}, ensure_ascii=False, indent=1), encoding="utf-8")
    (outdir / "refused.json").write_text(json.dumps(refused, ensure_ascii=False, indent=1), encoding="utf-8")
    (outdir / "truncated.json").write_text(json.dumps(truncated, ensure_ascii=False, indent=1), encoding="utf-8")
    (outdir / "failed.json").write_text(json.dumps(failed, ensure_ascii=False, indent=1), encoding="utf-8")
    (outdir / "usage.json").write_text(json.dumps(usage, ensure_ascii=False, indent=1), encoding="utf-8")
    write_summary(state, by_pkg, got, all_findings, refused, truncated, failed, usage, outdir)


def md(s):
    return one_line(str(s)).replace("|", "\\|")


def write_summary(state, by_pkg, got, findings, refused, truncated, failed, usage, outdir):
    sev = {s: sum(1 for f in findings if f.get("severity") == s) for s in SEVERITIES}
    cost = sum(u["cost_usd"] for u in usage.values())
    L = [f"# Qissa — yapay zekâ ön incelemesi / AI pre-review ({state['created'][:10]})", "",
         "**TR:** Bu rapor, «pending-scholarly-review» durumundaki paketlerin yapay zekâ ile yapılmış bir ön incelemesidir. "
         "İçerikte hiçbir şey değiştirilmedi; her bulgu, hocanın karar vereceği bir öneridir.",
         "**EN:** This report is an AI pre-review of the packages marked «pending-scholarly-review». "
         "Nothing in the content was changed; every finding is a suggestion for the scholar to decide on.", "",
         f"Model `{state['model']}` · effort `{state['effort']}` · batch `{state['batch_id']}` · {len(state['requests'])} requests · "
         f"cost / maliyet ${cost:.2f}", "",
         "| Önem / Severity | Sayı / Count |", "|---|---|"] + [f"| {s} | {sev[s]} |" for s in SEVERITIES] + [""]
    if refused or truncated or failed:
        L += ["## Yeniden çalıştırılacaklar / To re-run", ""]
        L += [f"- refused / reddedildi: `{r['custom_id']}` ({r.get('category')})" for r in refused]
        L += [f"- max_tokens / kesildi: `{r['custom_id']}`" for r in truncated]
        L += [f"- {r['result']}: `{r['custom_id']}`" for r in failed]
        L += [""]
    L += ["## Paketler / Packages", ""]
    for pkg, cids in sorted(by_pkg.items()):
        n = [f for f in findings if f["package"] == pkg]
        counts = ", ".join(f"{s} {sum(1 for f in n if f['severity'] == s)}" for s in SEVERITIES)
        L += [f"### {pkg} ({counts})", ""]
        for cid in sorted(cids):
            d = got.get(cid)
            if not d: L += [f"- `{cid}`: sonuç yok / no result", ""]; continue
            more = d.get("more_findings_not_listed") or 0
            L += [f"- `{cid}` — **{d.get('overall')}**" + (f" (+{more} listelenmedi / not listed)" if more else ""),
                  f"  - TR: {md(d.get('summary_tr'))}", f"  - EN: {md(d.get('summary_en'))}"]
        L += [""]
    for s in SEVERITIES:
        rows = [f for f in findings if f.get("severity") == s]
        if not rows: continue
        L += [f"## {s} ({len(rows)})", "",
              "| Paket / Package | Yer / Location | Tür / Type | Alan / Field | Şimdi / Current | Öneri / Suggested | Gerekçe (TR) | Reason (EN) |",
              "|---|---|---|---|---|---|---|---|"]
        for f in rows:
            loc = f"{f['chapter']}:{f['sentence']}:{f['token']} {f.get('surface', '')}" + ("" if f.get("location_ok") else " ⚠")
            L.append(f"| {f['package']} | {md(loc)} | {f['issue_type']} | {f['field']} | {md(f['current'])} | {md(f['suggested'])} | {md(f['reason_tr'])} | {md(f['reason_en'])} |")
        L += [""]
    L += ["⚠ = konum girdiyle eşleşmedi, elle doğrulayın / the location did not match the input; check it by hand.", ""]
    (outdir / "SUMMARY.md").write_text("\n".join(L), encoding="utf-8")
    print(f"report: {outdir}  ({sum(sev.values())} findings: " + ", ".join(f"{s} {sev[s]}" for s in SEVERITIES) + f"; cost ${cost:.2f})")


# ---------------------------------------------------------------- main
def pick_pilot(pkgs, reqs, n):
    size = {}
    for r in reqs: size[r["package"]] = size.get(r["package"], 0) + len(r["text"])
    ranked = sorted(size, key=size.get)
    if len(ranked) <= n: return ranked
    # spread across the size range, skewed upward: most of the shelf's tokens are in the long classical texts, so a pilot
    # of short stories alone would understate the output per input token of the full run
    return list(dict.fromkeys(ranked[min(len(ranked) - 1, round((len(ranked) - 1) * q))] for q in ([0.2, 0.55, 0.85] if n == 3 else [(k + 1) / (n + 1) for k in range(n)])))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--pilot", type=int); g.add_argument("--all", action="store_true")
    g.add_argument("--collect")
    ap.add_argument("--packages"); ap.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--max-findings", type=int, default=60); ap.add_argument("--no-wait", action="store_true"); ap.add_argument("--out")
    ap.add_argument("--assume-output-ratio", type=float, default=0.25, help="dry run: output tokens per input token (excluding the shared system prompt)")
    ap.add_argument("--assume-output-base", type=int, default=6000, help="dry run: output tokens per request on top of the ratio (thinking, summary)")
    a = ap.parse_args()
    c = client()
    if a.collect:
        outdir = Path(a.collect)
        state = json.loads((outdir / "batch.json").read_text(encoding="utf-8"))
        wait(c, state["batch_id"]); collect(c, state, outdir); return
    outdir = Path(a.out) if a.out else ROOT / "reports" / f"review-{dt.datetime.now(dt.timezone.utc):%Y-%m-%d}"
    outdir.mkdir(parents=True, exist_ok=True)
    pkgs = pending_packages()
    if a.packages:
        want = set(a.packages.split(",")); pkgs = [p for p in pkgs if p.name in want]
        missing = want - {p.name for p in pkgs}
        if missing: sys.exit(f"not pending or not found: {', '.join(sorted(missing))}")
    trm = irab_tr_memory()
    reqs = build_requests(pkgs, trm)
    system = system_blocks(a.max_findings)
    if a.dry_run:
        print(f"{len(pkgs)} packages pending review → {len(reqs)} requests ({sum(1 for r in reqs if r['unit'] == 'all')} whole packages, "
              f"{sum(1 for r in reqs if r['unit'] != 'all')} chapter or chapter-part requests)")
        sys_t = sys_token_count(c, system, a.effort)
        counts = count_all(c, reqs, system, a.effort)
        est = estimate(counts, sys_t, a.assume_output_ratio, a.assume_output_base)
        per_pkg = {}
        for r in reqs: per_pkg[r["package"]] = per_pkg.get(r["package"], 0) + counts[r["custom_id"]] - sys_t
        (outdir / "dry-run.json").write_text(json.dumps({"effort": a.effort, "system_tokens": sys_t, "counts": counts, "estimate": est,
                                                         "assumption": {"output_ratio": a.assume_output_ratio, "output_base": a.assume_output_base}},
                                                        ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"shared system prompt (rubric + {len(list((ROOT / 'content/grammar').glob('*.json')))} grammar notes): {sys_t:,} tokens, cached")
        print(f"input outside the system prompt: {est['user_input_tokens']:,} tokens; largest request {max(counts.values()):,} tokens")
        print(f"assumed output: {a.assume_output_base:,} + {a.assume_output_ratio} × input per request = {est['assumed_output_tokens']:,} tokens")
        print(f"estimated cost, batch prices ($4 / $20 per MTok): ${est['cost_cache_hits_usd']:.2f} with the system prompt cached, "
              f"${est['cost_no_cache_usd']:.2f} with no cache hit")
        print("largest packages by input tokens: " + ", ".join(f"{k} {v:,}" for k, v in sorted(per_pkg.items(), key=lambda x: -x[1])[:6]))
        pil = pick_pilot(pkgs, reqs, 3)
        pc = {k: v for k, v in counts.items() if any(r["custom_id"] == k and r["package"] in pil for r in reqs)}
        pe = estimate(pc, sys_t, a.assume_output_ratio, a.assume_output_base)
        print(f"default --pilot 3 packages: {', '.join(pil)} — {pe['requests']} requests, about ${pe['cost_cache_hits_usd']:.2f}–${pe['cost_no_cache_usd']:.2f} on the same assumption")
        print(f"written: {outdir / 'dry-run.json'}")
        return
    if a.pilot:
        names = a.packages.split(",") if a.packages else pick_pilot(pkgs, reqs, a.pilot)
        reqs = [r for r in reqs if r["package"] in names]
        print("pilot packages: " + ", ".join(names))
    state = submit(c, reqs, system, a.effort, outdir, "pilot" if a.pilot else "all")
    if a.no_wait: return
    wait(c, state["batch_id"])
    got, usage = collect(c, state, outdir)
    if a.pilot:
        cost = sum(u["cost_usd"] for u in usage.values()); uin = sum(u["input"] for u in usage.values())
        uout = sum(u["output"] for u in usage.values()); ucr = sum(u["cache_read"] for u in usage.values()); ucw = sum(u["cache_write"] for u in usage.values())
        print(f"pilot usage: input {uin:,}, cache read {ucr:,}, cache write {ucw:,}, output {uout:,} tokens → ${cost:.2f}")
        dr = sorted(ROOT.glob("reports/review-*/dry-run.json"))
        if dr:
            d = json.loads(dr[-1].read_text(encoding="utf-8")); sys_t = d["system_tokens"]
            user_pilot = sum(max(0, d["counts"].get(cid, 0) - sys_t) for cid in usage)
            if user_pilot:
                ratio = uout / user_pilot
                full = estimate(d["counts"], sys_t, ratio, 0)
                print(f"measured output per input token (outside the system prompt): {ratio:.2f}")
                print(f"extrapolated full run ({full['requests']} requests): ${full['cost_cache_hits_usd']:.2f} with cache hits, ${full['cost_no_cache_usd']:.2f} without")


if __name__ == "__main__":
    main()
