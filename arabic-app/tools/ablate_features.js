// Feature ablation for IrabModel. NOTE: `base` is the SHIPPED feature set, so
// every variant here ADDS to it — never re-add a feature that already ships,
// or the row scores a double count and reads as a regression.
// Run it BEFORE adding a feature and keep
// only what measurably helps — the length bucket earned its place this way,
// and a mim-initial flag and a shadda flag were dropped by the same run.
//   NODE_PATH=... CHROMIUM_PATH=... node tools/ablate_features.js
// Edit the `variants` map to try something new; `base` is always the
// shipped feature set, so every row is read against it.
const { chromium } = require('playwright-core');
const { pathToFileURL } = require('url'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  const p = await b.newPage();
  await p.goto(pathToFileURL(path.resolve('prototype/reader.html')).href);
  const r = await p.evaluate(() => {
    const BASE = IrabModel.features.bind(IrabModel);
    const variants = {
      base: BASE,
      len:  (w,i,n,pv) => { const f = BASE(w,i,n,pv); const L = stripAr(w).replace(/[^ء-ي]/g,'').length;
             f.push('len-' + (L <= 3 ? L : L <= 5 ? '45' : '6')); return f; },
      mim:  (w,i,n,pv) => { const f = BASE(w,i,n,pv); const bare = stripAr(w).replace(/[^ء-ي]/g,'');
             if (/^م/.test(bare) && bare.length > 3) f.push('mim'); return f; },
      shad: (w,i,n,pv) => { const f = BASE(w,i,n,pv); if (/ّ/.test(w)) f.push('shadda'); return f; },
      all:  (w,i,n,pv) => { const f = BASE(w,i,n,pv); const bare = stripAr(w).replace(/[^ء-ي]/g,'');
             const L = bare.length; f.push('len-' + (L <= 3 ? L : L <= 5 ? '45' : '6'));
             if (/^م/.test(bare) && L > 3) f.push('mim');
             if (/ّ/.test(w)) f.push('shadda'); return f; },
    };
    const run = () => { IrabModel._model = null; let ok=0,n=0,t2=0;
      STORIES.forEach(st => st.chapters.forEach(ch => ch.sentences.forEach(sen => {
        let prev=null; const N=sen.tokens.length;
        sen.tokens.forEach((t,i) => { const role = RoleEngine.of(t);
          if (role) { const pr = IrabModel.predict(t.s.full,i,N,prev); n++;
            if (pr[0] && pr[0].r===role) ok++; if (pr.slice(0,2).some(x=>x.r===role)) t2++; }
          prev = t.pos==='verb'?'verb':(t.irab && /حَرْفُ جَرٍّ|جَارَّة/.test(t.irab.ar||''))?'jarr':t.pos==='noun'?'noun':null; });
      }))); return { top1: Math.round(ok/n*1000)/10, top2: Math.round(t2/n*1000)/10 }; };
    const out = {};
    for (const k of Object.keys(variants)) { IrabModel.features = variants[k]; out[k] = run(); }
    IrabModel.features = BASE;
    return out;
  });
  console.log(JSON.stringify(r, null, 1));
  await b.close();
})();
