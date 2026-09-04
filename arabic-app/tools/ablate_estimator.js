// Estimator ablation for IrabModel: the shipped averaged perceptron against
// the estimator it replaced (naive Bayes with 1/k^0.35 damping), and against
// the perceptron's own settings, all leave-one-story-out on the SAME rows.
// This is the run that decided v146: NB 54.5/71.9 → AP 60.2/74.5, flat
// across epochs 5-20 and three seeds. Re-run it before touching EPOCHS or
// SEED, or before proposing another estimator; complement NB was tried in
// an earlier round and was far worse (42.8) — it is the wrong medicine for
// this skew.
//   NODE_PATH=... CHROMIUM_PATH=... node tools/ablate_estimator.js
const { chromium } = require('playwright-core');
const { pathToFileURL } = require('url'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  const p = await b.newPage();
  await p.goto(pathToFileURL(path.resolve('prototype/reader.html')).href);
  const r = await p.evaluate(() => {
    const R = IrabModel.ROLES;
    const rows = IrabModel.rows();
    // ---- the retired estimator, kept here as the yardstick ----
    const ALPHA = 0.35;
    const nbFit = subset => {
      const m = { roleN: {}, feat: {}, total: 0 };
      R.forEach(r => { m.roleN[r] = 0; m.feat[r] = {}; });
      subset.forEach(x => { m.roleN[x.role]++; m.total++;
        x.fs.forEach(f => { m.feat[x.role][f] = (m.feat[x.role][f] || 0) + 1; }); });
      return m;
    };
    const nbTwo = (m, fs) => {
      const w = 1 / Math.pow(Math.max(1, fs.length), ALPHA);
      let b1 = null, l1 = -Infinity, b2 = null, l2 = -Infinity;
      R.forEach(r => {
        let lp = Math.log((m.roleN[r] + 1) / (m.total + R.length));
        fs.forEach(f => { lp += w * Math.log(((m.feat[r][f] || 0) + 1) / (m.roleN[r] + 2)); });
        if (lp > l1) { l2 = l1; b2 = b1; l1 = lp; b1 = r; }
        else if (lp > l2) { l2 = lp; b2 = r; }
      });
      return [b1, b2];
    };
    const cv = (fit, two) => {
      const ids = [...new Set(rows.map(x => x.st))];
      let ok = 0, t2 = 0, n = 0;
      ids.forEach(h => {
        const m = fit(rows.filter(x => x.st !== h));
        rows.filter(x => x.st === h).forEach(x => {
          const [a, c] = two(m, x.fs);
          n++; if (a === x.role) ok++; if (a === x.role || c === x.role) t2++;
        });
      });
      return { top1: Math.round(ok / n * 1000) / 10, top2: Math.round(t2 / n * 1000) / 10 };
    };
    const apTwo = (m, fs) => {
      const pr = IrabModel.rank(m, fs);
      return [pr[0] && pr[0].r, pr[1] && pr[1].r];
    };
    const withSettings = (epochs, seed, fn) => {
      const e0 = IrabModel.EPOCHS, s0 = IrabModel.SEED;
      IrabModel.EPOCHS = epochs; IrabModel.SEED = seed;
      try { return fn(); } finally { IrabModel.EPOCHS = e0; IrabModel.SEED = s0; }
    };
    const out = { n: rows.length };
    out.nbDamped = cv(nbFit, nbTwo);
    out.shipped = cv(s => IrabModel.fit(s), apTwo);
    out.ap5  = withSettings(5,  IrabModel.SEED, () => cv(s => IrabModel.fit(s), apTwo));
    out.ap20 = withSettings(20, IrabModel.SEED, () => cv(s => IrabModel.fit(s), apTwo));
    out.seedB = withSettings(IrabModel.EPOCHS, 987654321, () => cv(s => IrabModel.fit(s), apTwo));
    return out;
  });
  console.log(JSON.stringify(r, null, 1));
  await b.close();
})();
