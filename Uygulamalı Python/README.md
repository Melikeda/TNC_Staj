# 📝 To-Do List Uygulaması

Bu proje, Python ile geliştirilmiş, konsol tabanlı, basit ve kullanıcı dostu bir To-Do List (Yapılacaklar Listesi) uygulamasıdır.
Kullanıcıların görevlerini eklemesine, görüntülemesine, düzenlemesine ve silmesine olanak sağlar.

# 🚀 Özellikler

🎯 Ana Menü — 5 kolay seçenek sunar:

- Görevleri Listele

- Yeni Görev Ekle

- Görev Düzenle

- Görev Sil

- Çıkış

➕ Görev Ekleme — Boş görev girişini engeller, yeni görevler eklenir.

📋 Görev Listeleme — Görevler numaralandırılmış şekilde gösterilir. Liste boşsa bilgilendirme yapılır.

✏️ Görev Düzenleme — Görev numarasıyla var olan görev düzenlenir, boş giriş ve geçersiz numara engellenir.

🗑️ Görev Silme — Görev numarasına göre görev silinir, hatalı girişlerde uyarı verir.

💾 Dosya İşlemleri — Görevler gorevler.txt dosyasında UTF-8 kodlaması ile saklanır ve program başlangıcında yüklenir.

⚠️ Hata Yönetimi — Kullanıcı girişleri try-except bloklarıyla kontrol edilir, hata mesajları gösterilir.

🧩 Modüler Kod Yapısı — Fonksiyonlar sayesinde okunabilir ve kolay bakımı mümkün.

# 📖 Kullanım

Program başladığında, varsa gorevler.txt dosyasından mevcut görevler yüklenir.

Ana menüde 1-5 arasında bir seçenek seçin:

Seçenek	İşlem
1	Görevleri Listele
2	Yeni Görev Ekle
3	Görev Düzenle
4	Görev Sil
5	Çıkış

Her işlem sonrası görevler gorevler.txt dosyasına kaydedilir.

Geçersiz girişlerde kullanıcıya bilgilendirici hata mesajları gösterilir.