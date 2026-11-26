// v351-I — the Iẓhār map's corpus examples, checked by the engines INSIDE the built page.
// node tools/ledger/izhar_course_probe.js <cands.json> <out.json>
// cands: [{ id, k: "pkg:ch:sid:ti(1-based)", e: regex the engine's line must match (harakāt stripped) }]
// out:   [{ id, k, ok, n (Illa346 steps on the authored line), eng (the engine's line, cut) }]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH }); const p = await b.newPage();
  await p.addInitScript(() => { try { localStorage.setItem('qissa-welcomed', '1'); } catch (e) {} });
  await p.goto('file://' + path.resolve(process.env.SMOKE_READER || path.join(__dirname, '../../prototype/reader.html')), { waitUntil: 'load', timeout: 600000 });
  await p.waitForFunction(() => typeof STORIES !== 'undefined' && STORIES.length > 10 && typeof Murib !== 'undefined', null, { timeout: 600000, polling: 2000 });
  const cands = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const out = await p.evaluate((C) => {
    const H = x => String(x || '').normalize('NFC').replace(/[ً-ْٰـ]/g, '');
    const memo = new Map();
    return C.map(c => {
      const [pkg, ch, sid, ti1] = c.k.split(':'); const ti = +ti1 - 1;
      try {
        const st = STORIES.find(s => s.id === pkg); const C2 = st && st.chapters.find(x => String(x.n) === ch);
        const sen = C2 && C2.sentences.find(s => s.id === sid); if (!sen) return { id: c.id, k: c.k, ok: false, eng: 'no sentence' };
        const T = sen.tokens; let rows = memo.get(c.k.split(':').slice(0, 3).join(':'));
        if (!rows) { try { rows = SentenceAnalyzer.analyze(T.map(t => t.s.full).join(' ')); } catch (e) { rows = []; } memo.set(c.k.split(':').slice(0, 3).join(':'), rows); }
        if (rows.length !== T.length) return { id: c.id, k: c.k, ok: false, eng: 'misaligned' };
        const eng = H((Murib.line(rows, ti) || {}).ar);
        let n = 0; try { const chn = Illa346.chain(T[ti]); n = chn ? chn.steps.length : 0; } catch (e) {}
        return { id: c.id, k: c.k, ok: new RegExp(c.e).test(eng), n, eng: eng.slice(0, 140) };
      } catch (e) { return { id: c.id, k: c.k, ok: false, eng: 'ERR ' + e.message }; }
    });
  }, cands);
  fs.writeFileSync(process.argv[3], JSON.stringify(out)); await b.close();
})();
