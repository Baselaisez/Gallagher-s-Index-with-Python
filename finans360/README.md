# Finans360: İzin ve Toplantı

İzin talepleri, yıllık izin bakiyesi ve toplantı yönetimi için tek dosyalık, internetsiz çalışan uygulama.
İsterseniz bir **şirket sunucusuna** bağlanır. O zaman herkes kendi hesabıyla girer, izin talepleri amirin onayına gider ve yönetici kullanıcıları ve yetkileri yönetir (bkz. [sunucu kurulum rehberi](server/README.md)).
Uygulamada örnek ya da uydurma kayıt yoktur: boş açılır ve yalnızca sizin yüklediğiniz gerçek personelle çalışır.
İlk açılışta üç adımlı kurulum Personel Bilgi Formu PDF’ini yüklemenizi, listeden kendinizi seçmenizi ve isteğe bağlı PIN kilidini açmanızı ister.
Üç biçimde kullanılabilir:

| Biçim | Nasıl alınır | Ne zaman |
| --- | --- | --- |
| **Android uygulaması** | [Finans360.apk](https://github.com/Baselaisez/Gallagher-s-Index-with-Python/releases/download/finans360/Finans360.apk) | Telefonda uygulama olarak, bildirimlerle |
| **Tek dosya HTML** | [Finans360.html](https://github.com/Baselaisez/Gallagher-s-Index-with-Python/releases/download/finans360/Finans360.html) | Kurulum olmadan; telefon ya da bilgisayar tarayıcısında |
| **Ana ekrana eklenen web uygulaması** | Bu klasörü herhangi bir HTTPS sunucuda (ör. GitHub Pages) yayınlayın | iPhone dahil her cihazda “Ana Ekrana Ekle” ile |
| **Şirket sunucusu** | [Finans360-sunucu.tar.gz](https://github.com/Baselaisez/Gallagher-s-Index-with-Python/releases/download/finans360/Finans360-sunucu.tar.gz) · [kurulum](server/README.md) | Ekipçe kullanım: hesaplar, roller, onay akışı, yönetim paneli |

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

**Personel** (2.1)
- Personel listesi şirketlere göre gruplanır; arama, şirket filtresi ve herkesin yıllık izin hakkını, kullandığını ve kalanını gösteren **izin tablosu**.
- **Personel Bilgi Formu PDF’inden içe aktarma:** PDF telefonda/bilgisayarda okunur, hiçbir sunucuya gönderilmez. Ad, ünvan, işe giriş ve doğum tarihleri, iletişim, adres, eğitim, dil, medeni hal, ilgi alanları, TC kimlik no ve kan grubu alınır. Kaydetmeden önce önizleme gösterilir: şirket adları düzeltilebilir, “bu kişi benim” seçilebilir, eksik/hatalı alanlar (geçersiz TC, hatalı telefon, yalnızca yıl olan tarihler) listelenir.
- Excel’den CSV ile içe/dışa aktarma (boş şablon dahil), telefon rehberine aktarma (.vcf), izin bakiyeleri raporu (.csv).
- Kişi kartı: ara / WhatsApp / e-posta, kıdem ve yaş, izin durumu, yaklaşan izin ve toplantılar, yeniden üretilen Personel Bilgi Formu.
- Her kişinin izin hakkı kendi işe giriş ve doğum tarihinden hesaplanır; 1 yılını doldurmayanlarda ilk hakkın doğacağı tarih gösterilir.
- Ana sayfada yaklaşan doğum günleri ve iş yıldönümleri (WhatsApp ile “Kutla”); takvimde doğum günleri.
- Toplantılara isimle ya da tüm şirketi tek dokunuşla katılımcı ekleme; katılımcılara e-posta daveti.
- **Gizlilik:** TC kimlik no ve kan grubu varsayılan olarak maskelenir; isteğe bağlı **PIN kilidi** (arka planda belirli süre kalınca yeniden kilitlenir).

> Bu depo herkese açıktır. Personel PDF’lerini, yedekleri ve dışa aktarılan dosyaları buraya **yüklemeyin**;
> `finans360/.gitignore` bu dosya türlerini engeller. Veriler, sunucusuz kullanımda yalnızca uygulamanın çalıştığı cihazda,
> sunucu kurulduğunda yalnızca sizin sunucunuzda saklanır.

**Şirket sunucusu** (2.3)

- Kayıtlar şirketin kendi sunucusunda tek yerde durur. Telefon, bilgisayar ve Android uygulaması aynı kayıtları görür.
- Üç rol vardır:
  - **Personel:** Kendi kaydını ve izinlerini görür, izin talebi oluşturur.
  - **Birim yöneticisi:** Sorumlu olduğu şirketlerin izinlerini görür ve onaylar.
  - **Yönetici:** Her şeyi yönetir.
- Diğer çalışanlar yalnız rehber bilgisiyle (ad, ünvan, şirket, iş e-postası) görünür.
- **İzin onay akışı:**
  - Talep, birim yöneticisinin ana sayfasına ve İzin sayfasına “Onayla / Reddet” düğmeleriyle düşer. Kalan bakiye de yanında gösterilir.
  - İzin geçmişinde kararı kimin verdiği yazar.
  - Çalışan bekleyen talebini düzenleyebilir ya da iptal edebilir.
- **Toplantılar:** Herkes oluşturduğu ve katıldığı toplantıları görür. Katılımcılar gündem, katılım, not ve aksiyonları güncelleyebilir.
- **Yönetim paneli:**
  - Kullanıcılar: tek tek ya da personel listesinden toplu hesap açma, tek kullanımlık şifreler, rol ve şirket ataması, şifre sıfırlama, oturum kapatma, hesabı durdurma.
  - Yetki modeli tablosu.
  - Denetim kaydı: girişler, hatalı girişler, izin kararları, hassas veri görüntülemeleri.
  - Sunucu yedeği; cihaz yedeğini sunucuya taşıma.
- **Hesabım:** Hesap ve personel kaydı, yetkileriniz, izin bakiyesi, şifre değiştirme, açık oturumlar ve “diğer oturumları kapat”.
- **Kişisel veri koruması:**
  - TC kimlik no, kan grubu ve adres listelerde hiç gönderilmez. Yalnız yetkili kişi “Göster” dediğinde gönderilir ve bu görüntüleme denetim kaydına yazılır.
  - Şifreler scrypt ile saklanır. Hatalı girişler sınırlanır.
- Kurulum adımları: [server/README.md](server/README.md). Gereken: Node.js 22.13+ ve bir alan adı. HTTPS için Caddy kullanılır.
- Android uygulaması ve tek dosya HTML, **Ayarlar › Şirket sunucusu** bölümünden bağlanır.

**Genel**
- Aylık takvim: izinler, toplantılar ve tatiller bir arada.
- Açık / koyu tema, telefon ve masaüstü düzeni.
- Yedek al / yedekten yükle (JSON), izinleri Excel’e aktar (CSV), tüm kayıtları takvime aktar (ICS).
- Sunucusuz kullanımda veriler yalnızca cihazda saklanır; şirket sunucusuna bağlanınca ortak kayıtlar sunucuda durur.

Dinî bayram tarihleri 2025–2027 için yüklüdür. Sonraki yılların bayramlarını ve ilan edilen idari izinleri
**Ayarlar › Tatil günleri** bölümünden ekleyin.

## Dosyalar

```
finans360/
  index.html             Uygulamanın tamamı (HTML + CSS + JS, tek dosya)
  .gitignore             Kişisel veri dosyalarının depoya girmesini engeller
  manifest.webmanifest   Ana ekrana ekleme bilgileri
  sw.js                  Çevrimdışı çalışma (service worker)
  icons/                 Uygulama simgeleri
  server/                Şirket sunucusu (Node.js 22.13+, ek paket yok)
    server.js            Hesaplar, roller, API, denetim kaydı, SQLite veritabanı
    test/                API testleri
    deploy/              systemd birimi ve Caddy (HTTPS) ayarı
    README.md            Kurulum rehberi
  app/                   Android kabuğu (Capacitor 8)
    package.json
    capacitor.config.json
    scripts/prepare-android.mjs
    res-icons/           Android başlatıcı ve bildirim simgeleri
.github/workflows/finans360-android.yml   APK derleme ve indirme sayfası
```

## APK’yı kendiniz derlemek

Gerekenler: Node 22+, JDK 21, Android SDK (Android Studio ile gelir). PDF okuyucu (pdf.js) APK’ya gömülür;
tek dosya HTML sürümü onu ilk içe aktarmada internetten yükler.

```bash
cd finans360/app
npm ci
npm run build:apk
# Çıktı: android/app/build/outputs/apk/debug/app-debug.apk
```
