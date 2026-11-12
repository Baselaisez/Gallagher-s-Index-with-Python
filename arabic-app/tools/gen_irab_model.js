// Fit the IrabModel (the averaged perceptron over the corpus's i'rab seats) in the reader's own page and write it to
// content/models/irab_model.json, which tools/build_prototype.py embeds as IRAB_MODEL.
//
// Why ship the weights? Every analysis asks the model (predict → train), and a fresh install's FIRST analysis used to
// fit it on the tap: the whole corpus tagged and five epochs run — 1.5 s on a laptop, six on a throttled phone — before
// the first game question could paint (wave 136 measured it on the cold path of gWajh / gShop / gJinas). The fit is a
// pure function of the corpus and the engines, so the build computes it once and the gate refits and compares: a
// changed engine or corpus shows up here as a named DRIFT, exactly as the drill bank does. The reader uses the shipped
// weights only when their corpus signature matches its own (IrabModel.shipped()); otherwise it trains as before.
//
// Usage:  node tools/gen_irab_model.js            (writes content/models/irab_model.json)
//         node tools/gen_irab_model.js --check    (refit and diff; exit 1 on drift)
//         READER=<path> overrides the reader the fit runs in (a dry copy).
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright-core');

const ROOT = path.resolve(__dirname, '..');
const READER = process.env.READER ? path.resolve(process.env.READER) : path.join(ROOT, 'prototype/reader.html');
const OUT = path.join(ROOT, 'content/models/irab_model.json');

function findChrome() {
  const c = [];
  if (process.env.CHROMIUM_PATH) c.push(process.env.CHROMIUM_PATH);
  c.push('/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
         '/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/google-chrome');
  for (const p of c) { try { if (p && fs.existsSync(p)) return p; } catch (e) {} }
  throw new Error('no Chromium found — set CHROMIUM_PATH');
}

(async () => {
  const browser = await chromium.launch({ executablePath: findChrome() });
  const page = await browser.newPage();
  const errs = [];
  page.on('pageerror', e => errs.push(String(e)));
  await page.addInitScript(() => { window.__QISSA_QUIET_OFF = true; });
  await page.goto(pathToFileURL(READER).href);
  await page.waitForFunction(() => typeof window.__qissaBootedAt === 'number', null, { timeout: 300000 });
  const data = await page.evaluate(() => {
    // a FRESH fit — never the shipped or the cached model
    const rows = IrabModel.rows();
    const m = IrabModel.fit(rows);
    const roles = {}; rows.forEach(r => { roles[r.role] = (roles[r.role] || 0) + 1; });
    let weights = 0; Object.values(m.w).forEach(o => { weights += Object.keys(o).length; });
    return { w: m.w, total: m.total, sig: IrabModel.corpusSig(), stories: STORIES.length, roles, weights,
             epochs: IrabModel.EPOCHS, seed: IrabModel.SEED, roleList: IrabModel.ROLES };
  });
  await browser.close();
  if (errs.length) { console.error('page errors:', errs); process.exit(1); }

  const model = {
    generated: true,
    source: 'tools/gen_irab_model.js',
    note: {
      en: 'GENERATED, not authored: the averaged perceptron IrabModel.fit() returns over the corpus\'s own i\'rab seats, written by the build so the reader need not fit it on the first tap. The gate refits and compares at every release; the reader reads it only for the corpus it names.',
      tr: 'YAZILMADI, ÜRETİLDİ: IrabModel.fit()\'in külliyatın kendi i\'rab mahalleri üzerinde verdiği ortalamalı perseptron; okuyucu ilk dokunuşta eğitmek zorunda kalmasın diye derleme yazar. Kapı her sürümde yeniden eğitir ve karşılaştırır; okuyucu yalnız adını verdiği külliyat için okur.',
    },
    corpus: { sig: data.sig, stories: data.stories, rows: data.total, roles: data.roles },
    fit: { epochs: data.epochs, seed: data.seed, roles: data.roleList, weights: data.weights },
    total: data.total,
    w: data.w,
  };
  const text = JSON.stringify(model, null, 1);

  if (process.argv.includes('--check')) {
    if (!fs.existsSync(OUT)) { console.error('no committed model to check against'); process.exit(1); }
    const was = fs.readFileSync(OUT, 'utf8');
    if (was.normalize('NFC') !== text.normalize('NFC')) {
      console.error('DRIFT: the shipped IrabModel no longer matches a fresh fit.');
      console.error('Run `node tools/gen_irab_model.js`, rebuild the reader, and read the diff — the corpus or an engine changed.');
      process.exit(1);
    }
    console.log(`irab model unchanged — ${model.fit.weights} weights over ${model.total} rows`);
    return;
  }
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, text, 'utf8');
  console.log(`wrote ${path.relative(ROOT, OUT)}: ${model.fit.weights} weights over ${model.total} rows (${model.corpus.stories} texts, sig ${model.corpus.sig})`);
})().catch(e => { console.error(e); process.exit(1); });
