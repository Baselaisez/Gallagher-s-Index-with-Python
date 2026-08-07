// Leave-one-story-out cross-validation for IrabModel. The in-app score is a
// RESUBSTITUTION number — the model graded on the very corpus it memorised.
// This trains on every story but one and tests on the one held out, which is
// the only number that says anything about a sentence the app has not seen.
const { chromium } = require('playwright-core');
const { pathToFileURL } = require('url'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  const p = await b.newPage();
  await p.goto(pathToFileURL(path.resolve('prototype/reader.html')).href);
  console.log(JSON.stringify(await p.evaluate(() => {
    const R = IrabModel.ROLES, FEAT = IrabModel.features.bind(IrabModel);
    const PREV = t => t.pos === 'verb' ? 'verb'
      : (t.irab && /حَرْفُ جَرٍّ|جَارَّة/.test(t.irab.ar || '')) ? 'jarr'
      : t.pos === 'noun' ? 'noun' : null;
    // materialise every labeled token once, tagged with its story
    const DATA = [];
    STORIES.forEach(st => st.chapters.forEach(ch => ch.sentences.forEach(sen => {
      let prev = null; const N = sen.tokens.length;
      sen.tokens.forEach((t, i) => {
        const role = RoleEngine.of(t);
        if (role) DATA.push({ st: st.id, fs: FEAT(t.s.full, i, N, prev), role });
        prev = PREV(t);
      });
    })));
    function fit(rows){
      const m = { roleN: {}, feat: {}, total: 0 };
      R.forEach(r => { m.roleN[r] = 0; m.feat[r] = {}; });
      rows.forEach(x => { m.roleN[x.role]++; m.total++;
        x.fs.forEach(f => { m.feat[x.role][f] = (m.feat[x.role][f] || 0) + 1; }); });
      return m;
    }
    function guess(m, fs, alpha){
      const w = 1 / Math.pow(Math.max(1, fs.length), alpha);
      let best = null, bestLp = -Infinity, second = -Infinity, secondR = null;
      R.forEach(r => { let lp = Math.log((m.roleN[r] + 1) / (m.total + R.length));
        fs.forEach(f => { lp += w * Math.log(((m.feat[r][f] || 0) + 1) / (m.roleN[r] + 2)); });
        if (lp > bestLp) { second = bestLp; secondR = best; bestLp = lp; best = r; }
        else if (lp > second) { second = lp; secondR = r; } });
      return [best, secondR];
    }
    const ids = [...new Set(DATA.map(x => x.st))];
    const out = {};
    for (const alpha of [0.25, 0.35, 0.5, 0.65]) {
      let ok = 0, t2 = 0, n = 0;
      ids.forEach(held => {
        const m = fit(DATA.filter(x => x.st !== held));
        DATA.filter(x => x.st === held).forEach(x => {
          const [a, c] = guess(m, x.fs, alpha);
          n++; if (a === x.role) ok++; if (a === x.role || c === x.role) t2++;
        });
      });
      out['alpha' + alpha] = { top1: Math.round(ok / n * 1000) / 10,
                               top2: Math.round(t2 / n * 1000) / 10 };
    }
    out.n = DATA.length; out.folds = ids.length;
    return out;
  }), null, 1));
  await b.close();
})();
