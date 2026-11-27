// v358-A — the Alfiyya course's page half, evaluated INSIDE the built page (by tools/alfiyya_course.py; build time only).
// node tools/alfiyya_course_probe.js <in.json> <out.json>
// in:  { probes: [{ s, w, re } | { s, any }], corpus: [{ u, re: [regex on folded letters], notes: [the unit's note ids] }], topics: [note id] }
// out: { probes: [{ ok, i, w, e (the engine's line, vowelled), role, fam, sibs (same-family roles NOT named on the line), off }],
//        corpus: { u: [{ k: "story:ch:sid:ti(1-based)", ar (the sentence as the story writes it), w (the token), a (its authored line), re }] },
//        topics: { id: level } }
// A probe reads the book's example AS PRINTED through SentenceAnalyzer + Murib.line (tools/ledger/aqil_probe.js's road); the asked word is
// the probe's word, or for a construction probe the first word whose line names the construction. Corpus: a token whose AUTHORED line and
// whose ENGINE line (Murib.line over SentenceAnalyzer on the sentence) both match the bāb's ruling regex on the word's own clauses, naming
// the same role where the ruling is a role — ≤ 3, distinct stories.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH }); const p = await b.newPage();
  await p.addInitScript(() => { try { localStorage.setItem('qissa-welcomed', '1'); } catch (e) {} });
  await p.goto('file://' + path.resolve(process.env.SMOKE_READER || path.join(__dirname, '../prototype/reader.html')), { waitUntil: 'load', timeout: 600000 });
  await p.waitForFunction(() => typeof STORIES !== 'undefined' && STORIES.length > 10 && typeof Murib !== 'undefined' && typeof Illa346 !== 'undefined', null, { timeout: 600000, polling: 2000 });
  const inp = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const out = await p.evaluate((I) => {
    const H = x => String(x || '').normalize('NFC').replace(/[ً-ْٰـ]/g, '').replace(/[أإآٱ]/g, 'ا').replace(/ى/g, 'ي').replace(/ة/g, 'ه');
    const OFF = /(^|[^ء-ي])(او|وقيل|ويجوز)([^ء-ي]|$)/, R = Illa346.roles(), fam = r => (Illa346.famOf(r) || {}).k || null, cache = {};
    // the ruling's regex on the word's OWN clauses (Illa346.read): what it matches, and the role that match names (a role's own pattern,
    // folded, on the matched words) — a role-like ruling holds only when the line's role IS that role (خبر in «خبر كان» is not the khabar)
    const RF = R.map(x => [x, new RegExp(H(x.re.source))]);
    const judge = (line, w, rx) => { const rd = Illa346.read(line, w) || {}; if (rd.cited) return { hit: false, rd }; const own = H(rd.own || ''), m = own.match(new RegExp(rx));
      if (!m) return { hit: false, rd }; const m0 = m[0].replace(/^[^ء-ي]+|[^ء-ي]+$/g, ''), nm = (RF.find(([x, re]) => re.test(m0)) || [])[0];
      return { hit: !nm || (rd.role && rd.role.id === nm.id), named: nm ? nm.id : null, m0, rd }; };
    const probes = I.probes.map(q => {
      try {
        const rows = cache[q.s] || (cache[q.s] = SentenceAnalyzer.analyze(q.s)), lines = rows.map((r, i) => (Murib.line(rows, i) || {}).ar || '');
        const i = q.any ? lines.findIndex(l => new RegExp(H(q.any)).test(H(l))) : rows.findIndex(r => H(r.w) === H(q.w));
        if (i < 0) return { ok: false };
        const e = lines[i], ok = q.any ? true : new RegExp(H(q.re)).test(H(e));
        const J = judge(e, rows[i].w, H(q.any || q.re)), rd = J.rd, role = rd.role ? rd.role.id : null, fk = rd.role ? fam(rd.role) : null, S = Illa346.S(e);
        const sibs = fk ? R.filter(x => x.id !== role && fam(x) === fk && !x.re.test(S)).map(x => x.id) : [];
        const mr = rd.role ? (S.match(rd.role.re) || [''])[0].trim() : '', tw = mr ? Illa346.frag(e, mr).replace(/[\s،.]+$/, '') : '';   // the line's own vowelled words for the role
        return { ok, i, w: rows[i].w, e, t: tw, role, named: J.named, keyOk: !!(J.hit && J.named && J.named === role), fam: fk, sibs, off: OFF.test(H(e)),
          clash: !!(role && /^فعل/.test(H(e))) };   // a noun's role on a line that opens «فِعْلٌ»: the line contradicts itself — never shown
      } catch (err) { return { ok: false, err: String(err.message || err) }; }
    });
    const toks = [];
    STORIES.forEach(st => (st.chapters || []).forEach(ch => (ch.sentences || []).forEach(sen => { if (sen.tokens.length < 3 || sen.tokens.length > 12) return;
      sen.tokens.forEach((t, ti) => { if (t.irab && t.irab.ar) toks.push([st, ch, sen, ti, H(t.irab.ar)]); }); })));
    const corpus = {}, memo = new Map(), GEN = new Set(['ناقص', 'اسمها', 'خبرها', 'مبني علي الفتح', 'شرط', 'عطف', 'نداء', 'مصدر', 'اشتغال', 'لازم', 'متعد', 'للتوكيد', 'الالف', 'الواو', 'الياء', 'مقدره', 'متعلق', 'جار']);   // «اشتغال المحل» of an estimated vowel is not the bāb of ishtighāl
    // a role or a construction is CLAIMED by the first unit (in the book's order) that finds a story token for it; a later unit does not
    // show the same kind again (الترخيم does not repeat النداء's munādā), and no token is shown twice
    const claim = new Map(), used = new Set();
    // a corpus hit belongs to the unit: a role the ruling names only where one of the role's notes is a note of the unit; a construction
    // that is not a role only when the matched words are not a bare generic word (ناقص, مبني على الفتح, شرط …)
    const belongs = (j, c) => j.named ? (R.find(x => x.id === j.named).notes || []).some(n => c.notes.includes(n)) : !GEN.has(j.m0);
    for (const c of I.corpus) {
      const got = [], seen = new Set(); let tried = 0;
      for (const rs0 of c.re) { const rs = '(?:^|[^ء-ي])(?:' + rs0 + ')(?:[^ء-ي]|$)', re = new RegExp(rs);   // whole words: «فصل» is not «منفصل»
        for (const [st, ch, sen, ti, a] of toks) { if (got.length >= 3 || tried >= 40) break; if (seen.has(st.id) || !re.test(a)) continue;
          const ja = judge(sen.tokens[ti].irab.ar, sen.tokens[ti].s.full, rs); if (!ja.hit || !belongs(ja, c)) continue; const ck = ja.named || ja.m0;
          if (claim.has(ck) && claim.get(ck) !== c.u) continue; if (used.has(st.id + ':' + ch.n + ':' + sen.id)) continue; tried++;
          const key = st.id + ':' + ch.n + ':' + sen.id; let rows = memo.get(key);
          if (!rows) { try { rows = SentenceAnalyzer.analyze(sen.tokens.map(t => t.s.full).join(' ')); } catch (e) { rows = []; } memo.set(key, rows); }
          if (rows.length !== sen.tokens.length) continue;
          let eng = ''; try { eng = (Murib.line(rows, ti) || {}).ar || ''; } catch (e) {}
          const je = judge(eng, sen.tokens[ti].s.full, rs); if (!je.hit || je.named !== ja.named) continue;
          seen.add(st.id); claim.set(ck, c.u); used.add(key); got.push({ k: key + ':' + (ti + 1), ar: sen.tokens.map(t => t.s.full + (t.punctAfter || '')).join(' '), w: sen.tokens[ti].s.full, a: sen.tokens[ti].irab.ar, re: rs0, m: ck }); }
        if (got.length >= 3) break; }
      corpus[c.u] = got;
    }
    const topics = {}; for (const t of I.topics) if (GRAMMAR[t]) topics[t] = GRAMMAR[t].level || 0;
    return { probes, corpus, topics };
  }, inp);
  fs.writeFileSync(process.argv[3], JSON.stringify(out)); await b.close();
})();
