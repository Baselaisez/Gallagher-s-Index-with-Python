// Builds the Android project for Finans360: copies the web app into www/,
// creates or syncs the Capacitor Android platform, and applies icons, splash and version.
import { cpSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';

const app = join(dirname(fileURLToPath(import.meta.url)), '..');
const web = join(app, '..');
const run = cmd => execSync(cmd, { cwd: app, stdio: 'inherit' });
const BRAND = '#0B6B5D';

// 1. Web assets
rmSync(join(app, 'www'), { recursive: true, force: true });
mkdirSync(join(app, 'www'), { recursive: true });
cpSync(join(web, 'index.html'), join(app, 'www', 'index.html'));
cpSync(join(web, 'icons'), join(app, 'www', 'icons'), { recursive: true });
// PDF reader for the on-device "Personel Bilgi Formu" import, bundled so it works offline.
mkdirSync(join(app, 'www', 'vendor'), { recursive: true });
for (const f of ['pdf.min.js', 'pdf.worker.min.js']) cpSync(join(app, 'node_modules', 'pdfjs-dist', 'build', f), join(app, 'www', 'vendor', f));

// 2. Native project
if (!existsSync(join(app, 'android'))) run('npx cap add android');
run('npx cap sync android');

// 3. Launcher icons, notification icon, splash
const res = join(app, 'android', 'app', 'src', 'main', 'res');
const icons = join(app, 'res-icons');
for (const dir of readdirSync(icons)) cpSync(join(icons, dir), join(res, dir), { recursive: true });
writeFileSync(join(res, 'values', 'ic_launcher_background.xml'),
  `<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">${BRAND}</color>\n</resources>\n`);
for (const dir of readdirSync(res)) if (dir.startsWith('drawable')) rmSync(join(res, dir, 'splash.png'), { force: true });
writeFileSync(join(res, 'drawable', 'splash.xml'),
  `<?xml version="1.0" encoding="utf-8"?>\n<layer-list xmlns:android="http://schemas.android.com/apk/res/android">\n    <item android:drawable="@color/ic_launcher_background"/>\n    <item android:drawable="@mipmap/ic_launcher_foreground" android:gravity="center" android:width="180dp" android:height="180dp"/>\n</layer-list>\n`);
const stylesPath = join(res, 'values', 'styles.xml');
let styles = readFileSync(stylesPath, 'utf8');
if (!styles.includes('windowSplashScreenBackground')) {
  styles = styles.replace('<item name="android:background">@drawable/splash</item>',
    '<item name="android:background">@drawable/splash</item>\n        <item name="windowSplashScreenBackground">@color/ic_launcher_background</item>');
  writeFileSync(stylesPath, styles);
}

// 4. Version from package.json; versionCode from the CI run number when available
const { version } = JSON.parse(readFileSync(join(app, 'package.json'), 'utf8'));
const gradlePath = join(app, 'android', 'app', 'build.gradle');
const code = Number(process.env.GITHUB_RUN_NUMBER) || 1;
writeFileSync(gradlePath, readFileSync(gradlePath, 'utf8')
  .replace(/versionCode\s+\d+/, `versionCode ${code}`)
  .replace(/versionName\s+"[^"]*"/, `versionName "${version}"`));
console.log(`Finans360 ${version} (${code}) hazır: android/`);
