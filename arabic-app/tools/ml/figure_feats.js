// Dump the FigurePredictor's features and the authored badiʿ labels of every corpus sentence — the training table for
// tools/ml/train_figures.py. Runs the reader in Chromium so the features are the page's own (one feature function, no copy).
// One chapter per evaluate: a single call over the whole corpus outran the renderer (the wave-20 first run died with
// «Target page, context or browser has been closed»), and a chapter at a time also lets a crash name its chapter.
//   NODE_PATH=… CHROMIUM_PATH=… node tools/ml/figure_feats.js [reader.html] > content/models/figure_feats.json
const { chromium } = require('playwright-core');
const path = require('path');
const FILE = process.argv[2] || path.resolve(__dirname, '../../prototype/reader.html');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  // a fresh page every few chapters: the renderer's caches grow with every analysed sentence, and one page over the
  // whole corpus was closed by Chromium (v174 dry run, after 46 chapters) — so the page is renewed, and a chapter whose
  // evaluate dies is retried once on a new page before the run gives up
  let p = null;
  const fresh = async () => { if (p) { try { await p.close(); } catch (e) {} } p = await b.newPage(); p.on('pageerror', e => console.error('PAGEERR', e.message));
    await p.goto('file://' + FILE); await p.waitForSelector('.lib-card', { timeout: 30000 }); };
  await fresh();
  const plan = await p.evaluate(() => STORIES.map(st => ({ id: st.id, n: st.chapters.length })));
  const kinds = await p.evaluate(() => FigurePredictor.KINDS);
  const rows = []; let since = 0;
  const one = ([sid, ci]) => {
      const st = STORIES.find(s => s.id === sid); const ch = st.chapters[ci]; const out = [];
      for (const sen of ch.sentences) {
        const text = sen.tokens.map(t => t.s.full).join(' ');
        let r = []; try { r = SentenceAnalyzer.analyze(text); } catch (e) { continue; }
        if (!r.length) continue;
        let f = null; try { f = FigurePredictor.feats(r); } catch (e) { continue; }
        const labels = Array.from(new Set((sen.badi ? (Array.isArray(sen.badi) ? sen.badi : [sen.badi]) : []).map(h => h.kind).filter(k => FigurePredictor.KINDS.includes(k))));
        out.push({ story: st.id, ch: ch.n, sen: sen.id, n: r.length, feats: f, labels });
      }
      return out;
    };
  for (const st of plan) for (let c = 0; c < st.n; c++) {
    if (since >= 8) { await fresh(); since = 0; }
    let part = null;
    try { part = await p.evaluate(one, [st.id, c]); }
    catch (e) { console.error('RETRY', st.id, c + 1, e.message.split('\n')[0]); await fresh(); since = 0; part = await p.evaluate(one, [st.id, c]); }
    since++; rows.push(...part); console.error(st.id, c + 1 + '/' + st.n, rows.length);
  }
  process.stdout.write(JSON.stringify({ kinds, rows }, null, 0));
  await b.close();
})();
