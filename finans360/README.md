# Finans360: İzin ve Toplantı

İzin talepleri, yıllık izin bakiyesi ve toplantı yönetimi için tek dosyalık, internetsiz çalışan uygulama.
Üç biçimde kullanılabilir:

| Biçim | Nasıl alınır | Ne zaman |
| --- | --- | --- |
| **Android uygulaması** | [Finans360.apk](https://github.com/Baselaisez/Gallagher-s-Index-with-Python/releases/download/finans360/Finans360.apk) | Telefonda uygulama olarak, bildirimlerle |
| **Tek dosya HTML** | [Finans360.html](https://github.com/Baselaisez/Gallagher-s-Index-with-Python/releases/download/finans360/Finans360.html) | Kurulum olmadan; telefon ya da bilgisayar tarayıcısında |
| **Ana ekrana eklenen web uygulaması** | Bu klasörü herhangi bir HTTPS sunucuda (ör. GitHub Pages) yayınlayın | iPhone dahil her cihazda “Ana Ekrana Ekle” ile |

İndirme bağlantıları, `finans360/` klasöründeki her değişiklikten sonra GitHub Actions tarafından yeniden üretilir
(**Releases › finans360**).

## Kurulum

**Android:** APK’yı indirip açın. Telefon izin isterse “bu kaynaktan yüklemeye izin ver” seçeneğini açın ve **Yükle**’ye dokunun.
Güncelleme için yeni APK’yı aynı şekilde yükleyin; verileriniz korunur.

**HTML:** Dosyayı indirip tarayıcıda açın. Tek dosyadır, internet gerekmez.

**iPhone / web uygulaması:** Yayınlanmış adresi Safari’de açın, Paylaş › **Ana Ekrana Ekle**.

## Özellikler

**İzin**
- Yıllık izin bakiyesi, İş Kanunu md. 53’e göre kıdem ve yaştan otomatik hesaplanır (14 / 20 / 26 gün, 18 yaş altı ve 50 yaş üstü için en az 20 gün). Şirket farklı hak tanımlıyorsa elle girilebilir; devreden izin eklenebilir.
- İş günü hesabı hafta sonlarını, resmî tatilleri ve arife yarım günlerini düşer (md. 56). Yarım gün başlangıç ve bitiş desteklenir.
- İşe başlama tarihi, bakiyenin talep sonrası durumu, tarih aralığındaki toplantılar ve aynı dönemde izinli ekip arkadaşları talep yazılırken gösterilir.
- İzin türleri: yıllık, mazeret (evlilik 3, babalık 5, ölüm 3, evlat edinme 3 gün…), saatlik, sağlık raporu, ücretsiz, doğum, idari, doğum günü.
- Onay durumu (bekliyor / onaylandı / reddedildi / iptal) ve değişiklik geçmişi.
- Amirinize hazır **talep mesajı** (WhatsApp, e-posta, kopyala) ve imza alanlı **İzin Talep Formu** (yazdır / PDF).
- **Köprü fırsatları:** en az izinle en uzun tatili veren tarihleri önerir ve tek dokunuşla taslak oluşturur.
- Ekibin izinleri de kaydedilebilir; takvimde taralı çubukla gösterilir.

**Toplantı**
- Sıradaki toplantı ve geri sayım, “Katıl” bağlantısı.
- Çakışma kontrolü: aynı saatteki toplantılar, resmî tatiller, sizin izniniz ve **izinli katılımcılar**.
- Gündem kontrol listesi, katılım işaretleme, otomatik kaydedilen notlar.
- Kararlar ve aksiyonlar (sorumlu, termin); gecikenler ana sayfada görünür.
- Haftalık / iki haftalık / aylık tekrarlanan toplantılar.
- Davet metni (WhatsApp), Google Takvim bağlantısı, `.ics` takvim dosyası ve imza alanlı **Toplantı Tutanağı**.
- Android uygulamasında toplantıdan önce ve izinden bir gün önce telefon bildirimi.

**Genel**
- Aylık takvim: izinler, toplantılar ve tatiller bir arada.
- Açık / koyu tema, telefon ve masaüstü düzeni.
- Yedek al / yedekten yükle (JSON), izinleri Excel’e aktar (CSV), tüm kayıtları takvime aktar (ICS).
- Veriler yalnızca cihazda saklanır; sunucu yoktur.

Dinî bayram tarihleri 2025–2027 için yüklüdür. Sonraki yılların bayramlarını ve ilan edilen idari izinleri
**Ayarlar › Tatil günleri** bölümünden ekleyin.

## Dosyalar

```
finans360/
  index.html             Uygulamanın tamamı (HTML + CSS + JS, tek dosya)
  manifest.webmanifest   Ana ekrana ekleme bilgileri
  sw.js                  Çevrimdışı çalışma (service worker)
  icons/                 Uygulama simgeleri
  app/                   Android kabuğu (Capacitor 8)
    package.json
    capacitor.config.json
    scripts/prepare-android.mjs
    res-icons/           Android başlatıcı ve bildirim simgeleri
.github/workflows/finans360-android.yml   APK derleme ve indirme sayfası
```

## APK’yı kendiniz derlemek

Gerekenler: Node 22+, JDK 21, Android SDK (Android Studio ile gelir).

```bash
cd finans360/app
npm ci
npm run build:apk
# Çıktı: android/app/build/outputs/apk/debug/app-debug.apk
```
