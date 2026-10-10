# Finans360 sunucusu

Finans360’ı bir ekip uygulamasına çevirir. Kayıtlar tek bir şirket sunucusunda durur, herkes kendi hesabıyla girer.
Her kullanıcı yalnız rolünün izin verdiği kayıtları görür.
Sunucusuz kullanımda veriler yalnızca o cihazda kalır. Sunucu kurulduğunda telefonlar, bilgisayarlar ve Android uygulaması aynı kayıtları paylaşır.

- **Hesaplar ve roller:** Personel, Birim yöneticisi ve Yönetici.
- **İzin onay akışı:** Çalışanın talebi birim yöneticisinin ekranına düşer; onay ya da ret izin geçmişine kimin karar verdiğiyle yazılır.
- **Yönetim paneli:** Kullanıcılar, personelden toplu hesap açma, yetki modeli, denetim kaydı, veri ve yedek.
- **Hesabım:** Hesap bilgileri, yetkiler, izin bakiyesi, şifre değiştirme, açık oturumlar.
- **Kişisel veri koruması:**
  - TC kimlik no, kan grubu ve adres listelerde hiç gönderilmez. Yalnız yetkili kişi “Göster” dediğinde gönderilir ve bu görüntüleme denetim kaydına yazılır.
  - Şifreler scrypt ile özetlenir.
  - 8 hatalı girişten sonra giriş 15 dakika engellenir.

Ek paket gerekmez. Sunucu tek dosyadır (`server.js`) ve veritabanı olarak Node.js’in yerleşik SQLite’ını kullanır.

## Yetki modeli

| Yetki | Personel | Birim yöneticisi | Yönetici |
| --- | --- | --- | --- |
| Kendi kaydını ve izin bakiyesini görme | Evet | Evet | Evet |
| İzin talebi oluşturma | Kendisi için | Kendisi ve birimi için | Herkes için |
| İzin onaylama ve reddetme | — | Birimi (kendi izni hariç) | Herkes |
| Personel kayıtlarını görme | Kendisi; diğerleri rehber | Birimi; diğerleri rehber | Herkes |
| TC kimlik no, kan grubu, adres | Kendisi | Kendisi; izin verilirse birimi | Herkes |
| Personel ekleme, düzenleme, içe aktarma | — | — | Evet |
| Toplantıları görme | Oluşturduğu ve katıldığı | Oluşturduğu ve katıldığı | Hepsi |
| Kurum ayarları (toplantı yerleri, tatiller) | — | — | Evet |
| Kullanıcı ve rol yönetimi, denetim kaydı, yedek | — | — | Evet |

**Rehber bilgisi**, ad, ünvan, şirket ve iş e-postasından oluşur.
**Birim**, birim yöneticisine atanan şirketlerdir (Yönetim › Kullanıcılar › kişi › Sorumlu olduğu şirketler).
Kurallar sunucuda uygulanır: uygulama, yetkinin dışındaki kayıtları hiç almaz.

## Gerekenler

- Bir Linux sunucu (VPS). Ubuntu 24.04 önerilir; 30–300 kişi için 1 vCPU ve 1 GB RAM yeterlidir.
- **Node.js 22.13 ya da üstü.**
- Bir alan adı, örneğin `izin.sirketiniz.com`. Bu adın A kaydı sunucunun IP adresini göstermelidir.
- HTTPS için [Caddy](https://caddyserver.com). Sertifikayı kendisi alır ve yeniler. Android uygulaması yalnız HTTPS adrese bağlanır.

> **KVKK:** Personel verileri yurt dışındaki bir sunucuya konursa bu, KVKK md. 9 kapsamında yurt dışına aktarımdır.
> Türkiye’de barındırılan bir sunucu seçmek işinizi kolaylaştırır. Karar vermeden önce şirketinizin KVKK sorumlusuna danışın.

## Kurulum

Komutlar Ubuntu içindir ve `sudo` yetkisi olan bir kullanıcıyla çalıştırılır.

**1. Node.js’i kurun**

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
node --version          # v22.13.0 ya da üstü olmalı
```

**2. Sunucu dosyalarını indirin**

```bash
sudo useradd --system --home /opt/finans360 --shell /usr/sbin/nologin finans360
sudo mkdir -p /opt/finans360 && cd /opt/finans360
sudo curl -fL -o sunucu.tar.gz https://github.com/Baselaisez/Gallagher-s-Index-with-Python/releases/download/finans360/Finans360-sunucu.tar.gz
sudo tar xzf sunucu.tar.gz && sudo rm sunucu.tar.gz
ls /opt/finans360/finans360/server/server.js
```

Paket uygulamanın kendisini (`index.html`) ve PDF okuyucuyu da içerir. Depoyu `git clone` ile de alabilirsiniz; sunucu `finans360/server` klasöründedir.

**3. Hizmeti başlatın (systemd)**

```bash
cd /opt/finans360/finans360/server
sudo cp deploy/finans360.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now finans360
systemctl status finans360       # "active (running)" görmelisiniz
```

Sunucu yalnız `127.0.0.1:8360` adresini dinler, yani dışarıdan doğrudan erişilemez.
Veriler `/var/lib/finans360/finans360.db` dosyasındadır; dosyayı yalnız `finans360` kullanıcısı okuyabilir.

**4. İlk yönetici hesabını oluşturun**

Siteyi açmadan önce yönetici hesabını komut satırından oluşturun:

```bash
cd /opt/finans360/finans360/server
sudo -u finans360 env DATA_DIR=/var/lib/finans360 node --no-warnings server.js create-admin yonetici "Ad Soyad"
```

Komut tek kullanımlık bir şifre yazar; ilk girişte kendi şifrenizi belirlersiniz.
Bu adımı atlarsanız siteyi ilk açan kişi yönetici hesabını oluşturur. O yüzden ya bu komutu çalıştırın ya da siteyi açar açmaz kurulumu kendiniz yapın.

**5. HTTPS’i açın (Caddy)**

```bash
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update && sudo apt install -y caddy

sudo cp deploy/Caddyfile /etc/caddy/Caddyfile
sudo nano /etc/caddy/Caddyfile   # izin.sirketiniz.com yerine kendi alan adınızı yazın
sudo systemctl reload caddy
sudo ufw allow 80/tcp && sudo ufw allow 443/tcp   # güvenlik duvarı açıksa
```

`https://izin.sirketiniz.com` adresini açın. Giriş ekranı gelmelidir.

## İlk gün: personel ve hesaplar

1. Yönetici hesabıyla girin. Size verilen tek kullanımlık şifreyi kullanın ve ardından kendi şifrenizi belirleyin.
2. **Yönetim › Veri ve yedek › İçe aktar** bölümünden Personel Bilgi Formu PDF’ini, Excel listesini (CSV) ya da daha önce aldığınız personel dosyasını (.json) seçin.
   Dosya sizin cihazınızda okunur; önizlemede onayladığınız kayıtlar sunucuya kaydedilir.
3. **Yönetim › Kullanıcılar** bölümünde kendi satırınıza dokunun ve **Personel kaydı** listesinden kendinizi seçin.
   Böylece izin bakiyeniz ve izin formlarınız kendi kaydınızdan dolar.
4. **Personelden hesap aç** düğmesiyle çalışanların hepsine tek seferde hesap açın.
   - Kullanıcı adı iş e-postasından üretilir.
   - Tek kullanımlık şifreler bir kez gösterilir. **Excel listesi (.csv)** ile kaydedip her kişiye kendi bilgisini iletin.
5. Birim yöneticilerinin satırına dokunun, rolü **Birim yöneticisi** yapın ve sorumlu olduğu şirketleri işaretleyin.
   Gerekirse “hassas bilgileri görebilir” iznini de verin.
6. Uygulamanın sunucusuz sürümünde kayıtlarınız varsa önce o cihazda **Ayarlar › Yedek al** ile yedek alın.
   Sonra **Yönetim › Veri ve yedek › Cihaz yedeğini yükle** ile yedeği sunucuya taşıyın.

## Telefonlar ve bilgisayarlar

- **Tarayıcı:** `https://izin.sirketiniz.com` adresini açın.
  - Android Chrome’da menü › Ana ekrana ekle.
  - iPhone Safari’de Paylaş › Ana Ekrana Ekle.
- **Android uygulaması (APK) ya da tek dosya HTML:** **Ayarlar › Şirket sunucusu** bölümüne adresi yazıp **Bağlan**’a dokunun, sonra giriş yapın.
  Cihazdaki eski kayıtlar silinmez, ama bağlıyken kullanılmaz. **Sunucudan ayrıl** ile cihaz kendi kayıtlarına döner.

Sunucu modunda cihazda yalnız oturum anahtarı ve kişisel tercihler (tema, hatırlatma, PIN) saklanır.
Ortak kayıtlar her açılışta sunucudan gelir ve uygulama açıkken dakikada bir yenilenir; bu yüzden internet bağlantısı gerekir.
Uygulama açıkken bağlantı koparsa yapılan değişiklikler bağlantı gelince gönderilir; uygulamayı kapatmadan önce “Şimdi eşitle” ile gönderildiğinden emin olun.

## Yedek

Her gece yedek almak için (30 günden eski yedekler silinir):

```bash
sudo mkdir -p /var/backups/finans360 && sudo chown finans360: /var/backups/finans360 && sudo chmod 700 /var/backups/finans360
sudo crontab -u finans360 -e
```

Açılan dosyanın sonuna şu satırı ekleyin:

```
15 2 * * * cd /opt/finans360/finans360/server && DATA_DIR=/var/lib/finans360 /usr/bin/node --no-warnings server.js backup /var/backups/finans360/yedek-$(date +\%F).json && find /var/backups/finans360 -name 'yedek-*.json' -mtime +30 -delete
```

Yedek dosyası bütün personel verisini içerir ama şifreleri içermez. Yedekleri sunucunun dışında da güvenli bir yerde saklayın.
Yönetici, **Yönetim › Veri ve yedek › Sunucu yedeği** ile aynı dosyayı tarayıcıdan da indirebilir.

## Bakım

| İş | Komut |
| --- | --- |
| Güncelleme | 2. adımdaki indirme komutlarını tekrarlayın, sonra `sudo systemctl restart finans360`. Veriler `/var/lib/finans360` altında kalır. |
| Kayıtlar (log) | `journalctl -u finans360 -f` |
| Bir kullanıcının şifresini sıfırlama | Yönetim › Kullanıcılar › kişi › Şifreyi sıfırla |
| Yönetici şifresini unuttuysanız | `sudo -u finans360 env DATA_DIR=/var/lib/finans360 node --no-warnings server.js reset-password yonetici` |
| Yeni yönetici | `sudo -u finans360 env DATA_DIR=/var/lib/finans360 node --no-warnings server.js create-admin <kullanıcı-adı> "Ad Soyad"` |

Komut satırı komutlarını `/opt/finans360/finans360/server` klasöründe çalıştırın.

## Ayarlar

| Değişken | Varsayılan | Açıklama |
| --- | --- | --- |
| `PORT` | `8360` | Dinlenen port |
| `HOST` | `127.0.0.1` | Dinlenen adres. Önünde Caddy varken değiştirmeyin. |
| `DATA_DIR` | `server/data` | Veritabanı klasörü |
| `TRUST_PROXY` | — | `1` olunca istemci IP’si ve HTTPS bilgisi `X-Forwarded-*` başlıklarından okunur. Yalnız önünde Caddy ya da nginx varken açın. |
| `SESSION_DAYS` | `30` | Kullanılmayan oturumun kapanma süresi (gün) |
| `WEB_DIR` | `..` | Uygulama dosyalarının (`index.html`) klasörü |

## Geliştirme

```bash
cd finans360/server
npm start        # http://127.0.0.1:8360
npm test         # API testleri (bellekte veritabanı, kurgusal kişiler)
```

Uygulama, sunucudan açıldığında `index.html` içine eklenen `<meta name="f360-server">` etiketinden sunucu modunu anlar.
Başka bir adresten açılan kopyalar (APK, tek dosya HTML) **Ayarlar › Şirket sunucusu** ile bağlanır.
API yalnız `Authorization: Bearer` anahtarıyla çalışır ve çerez kullanmaz.

| Uç nokta | Açıklama |
| --- | --- |
| `GET /api/health` | Durum; ilk kurulum gerekiyorsa `setup: true` |
| `POST /api/setup`, `POST /api/login`, `POST /api/logout` | Kurulum ve oturum |
| `GET /api/me`, `POST /api/me/password`, `PUT /api/me/prefs`, `GET /api/me/sessions` | Hesabım |
| `GET /api/bootstrap` | Kullanıcının görebildiği personel, izin, toplantı ve kurum ayarları |
| `PUT/DELETE /api/leaves/:id`, `PUT/DELETE /api/meetings/:id`, `PUT /api/org` | Kayıtlar |
| `PUT/DELETE /api/people/:id`, `GET /api/people/:id/sensitive`, `POST /api/people/import` | Personel |
| `/api/admin/users…`, `GET /api/admin/audit`, `GET /api/admin/export`, `POST /api/admin/import-backup` | Yönetim |
