# Teacher X • İki kule, tek sahne
Webots R2025a için öğrenci ve jüri demosu. Ölçüler fotoğraftan esinlenen temsilî ölçülerdir. Yeşil taban, iki kule, model ağaçlar, mavi sensör maketi ve turuncu konum göstergesi tek sahnededir.

## Başlat
ZIP’i tamamen çıkar. Webots’ta File → Open World ile worlds/parkur.wbt dosyasını aç. Python 3 kullanılabilir olmalı. Simülasyonu ▶ ile başlat. 3B görüntüye tıklayarak klavyeyi sahneye odakla. Panel görünmezse Webots konsolunda Python denetleyicisinin başlayıp başlamadığına bak. Dosyaları ayrı klasörlere taşıma.

## Bir dakikalık jüri gösterimi
1. **Hazır:** “Wokwi’de devre ve kodu, burada ise kararların maketteki karşılığını gösteriyoruz.” Turuncu gösterge ilk kulede; panel 400 birim ve %0 gösterir.
2. **H:** Sanal sinyal 850 olur, 600 eşiğini geçer. Turuncu gösterge iki simülasyon saniyesinde karşı kuleye gider ve %100’de durur. Erken G komutu etkisizdir.
3. **G:** Uzak uçtayken bas. Gösterge iki saniyede %0’a döner. “Sinyal yüksek kaldığı hâlde niçin tekrar gitmedi?” Öğrenci: “Aynı olayı iki kez saymıyoruz.”
4. **L:** Sinyal 400’e iner; panel yeniden HAZIR olur. Bir sonraki öğrenci H ile tekrarlayabilir. Baştan almak için dünyayı yeniden yükleyebilirsin.

## İki gösterimi karıştırma
[Wokwi: MQ-2 ve iki servo](https://wokwi.com/projects/481403712147359745) analog giriş ve servo konumlarını gösterir. Webots’ta gösterge konumu yazılımla canlandırılır; H/L kısayolları gaz ölçümü değildir. 400 ve 850 temsili sayılardır, ppm veya ESP32 ADC ölçümü değildir. Wokwi ile canlı veri alışverişi yoktur. Mekanik tork, taşıma kapasitesi, akım ve telefon bağlantısı bu demoda ölçülmez.

## Öğrenci deneyi
H’den önce G’ye bas: hareket beklenmez. H’ye bas ve uzak uçta bekle: geri dönüş kendiliğinden başlamamalı. G ile dön, L’ye basmadan bekle: gösterge yerinde kalmalı. L ve ardından H yeni tur başlatmalı. Bu dört gözlemden birini seçip jüriye nedenini anlat.

Ayrı kontrol: proje klasöründe `python test_akis.py` komutu durum mantığını Webots olmadan sınar.
