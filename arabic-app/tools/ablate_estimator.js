// Estimator comparison for IrabModel. `multinomial` is whatever predict()
// currently ships; the others are candidates scored against it on the same
// labeled corpus. The 1/sqrt(k) feature weighting was adopted this way
// (51.9 -> 53.2 first guess) and complement naive Bayes was rejected (42.8).
//   NODE_PATH=... CHROMIUM_PATH=... node tools/ablate_estimator.js
const { chromium } = require('playwright-core');
const { pathToFileURL } = require('url'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  const p = await b.newPage();
  await p.goto(pathToFileURL(path.resolve('prototype/reader.html')).href);
  const r = await p.evaluate(() => {
    const NB = IrabModel.predict.bind(IrabModel);
    // Complement naive Bayes: score a class by how POORLY its complement
    // explains the features. Known to beat multinomial NB on skewed classes.
    const CNB = function(full, i, n, prev){
      const m = IrabModel.train(); if (!m.total) return [];
      const fs = IrabModel.features(full, i, n, prev);
      const R = IrabModel.ROLES;
      const scores = R.map(r => {
        let lp = Math.log((m.roleN[r] + 1) / (m.total + R.length));
        fs.forEach(f => {
          let cNot = 0, nNot = 0;
          R.forEach(o => { if (o !== r) { cNot += (m.feat[o][f] || 0); nNot += m.roleN[o]; } });
          lp -= Math.log((cNot + 1) / (nNot + 2));      // complement: subtract
        });
        return { r, lp };
      });
      const mx = Math.max(...scores.map(s => s.lp)); let z = 0;
      scores.forEach(s => { s.p = Math.exp(s.lp - mx); z += s.p; });
      scores.forEach(s => { s.p /= z; });
      return scores.sort((a, b) => b.p - a.p);
    };
    // NB with a length-normalised feature weight — damps correlated features
    const WNB = function(full, i, n, prev){
      const m = IrabModel.train(); if (!m.total) return [];
      const fs = IrabModel.features(full, i, n, prev);
      const w = 1 / Math.sqrt(Math.max(1, fs.length));
      const scores = IrabModel.ROLES.map(r => {
        let lp = Math.log((m.roleN[r] + 1) / (m.total + IrabModel.ROLES.length));
        fs.forEach(f => { lp += w * Math.log(((m.feat[r][f] || 0) + 1) / (m.roleN[r] + 2)); });
        return { r, lp };
      });
      const mx = Math.max(...scores.map(s => s.lp)); let z = 0;
      scores.forEach(s => { s.p = Math.exp(s.lp - mx); z += s.p; });
      scores.forEach(s => { s.p /= z; });
      return scores.sort((a, b) => b.p - a.p);
    };
    const run = () => { let ok=0,n=0,t2=0;
      STORIES.forEach(st => st.chapters.forEach(ch => ch.sentences.forEach(sen => {
        let prev=null; const N=sen.tokens.length;
        sen.tokens.forEach((t,i) => { const role = RoleEngine.of(t);
          if (role) { const pr = IrabModel.predict(t.s.full,i,N,prev); n++;
            if (pr[0] && pr[0].r===role) ok++; if (pr.slice(0,2).some(x=>x.r===role)) t2++; }
          prev = t.pos==='verb'?'verb':(t.irab && /حَرْفُ جَرٍّ|جَارَّة/.test(t.irab.ar||''))?'jarr':t.pos==='noun'?'noun':null; });
      }))); return { n, top1: Math.round(ok/n*1000)/10, top2: Math.round(t2/n*1000)/10 }; };
    const out = {};
    IrabModel.predict = NB;  out.multinomial = run();
    IrabModel.predict = CNB; out.complement  = run();
    IrabModel.predict = WNB; out.weighted    = run();
    IrabModel.predict = NB;
    return out;
  });
  console.log(JSON.stringify(r, null, 1));
  await b.close();
})();
