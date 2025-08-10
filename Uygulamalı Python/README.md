To-Do List Uygulaması
Bu proje, Python ile yazılmış, basit ve kullanıcı dostu bir konsol tabanlı To-Do List uygulamasıdır. Kullanıcıların görevlerini eklemesine, görüntülemesine, düzenlemesine ve silmesine olanak tanır. Görevler bir metin dosyasında saklanır ve her işlem sonrası dosya güncellenir. Türkçe karakter desteği için UTF-8 kodlaması kullanılmıştır. Modüler, okunabilir ve hata yönetimine sahip bir kod yapısı benimsenmiştir.
Özellikler

Ana Menü: Kullanıcıya 5 seçenek sunar:
Görevleri Listele
Yeni Görev Ekle
Görev Düzenle
Görev Sil
Çıkış


Görev Ekleme: Yeni görev ekleme, boş görev girişini engeller.
Görev Listeleme: Görevler numaralandırılmış şekilde listelenir; liste boşsa kullanıcı bilgilendirilir.
Görev Düzenleme: Görevler numara ile düzenlenir, boş giriş ve geçersiz numara kontrol edilir.
Görev Silme: Görevler numara ile silinir, geçersiz numara girişi hata mesajı döndürür.
Dosya İşlemleri: Görevler gorevler.txt dosyasına kaydedilir ve program başlangıcında okunur. Dosya işlemleri UTF-8 kodlamasıyla yapılır ve hatalar ele alınır.
Hata Yönetimi: Kullanıcı girdileri (sayı yerine harf, geçersiz numara vb.) try-except bloklarıyla doğrulanır.
Modüler Kod: Fonksiyonlar kullanılarak okunabilir ve bakımı kolay bir yapı oluşturulmuştur.


Kullanım

Program başladığında, varsa gorevler.txt dosyasından mevcut görevler yüklenir.
Ana menüde 1-5 arasında bir seçenek seçin:
1 - Görevleri Listele: Mevcut görevleri numaralandırılmış şekilde gösterir.
2 - Yeni Görev Ekle: Yeni bir görev eklemenizi sağlar (boş giriş yasaktır).
3 - Görev Düzenle: Görev numarası ile mevcut bir görevi düzenler.
4 - Görev Sil: Görev numarası ile bir görevi siler.
5 - Çıkış: Programı sonlandırır.


Her işlem sonrası görevler gorevler.txt dosyasına kaydedilir.
Geçersiz girişlerde (örn. sayı yerine harf, geçersiz görev numarası) hata mesajları gösterilir.

Örnek Kullanım
=== To-Do List Uygulaması ===
1. Görevleri Listele
2. Yeni Görev Ekle
3. Görev Düzenle
4. Görev Sil
5. Çıkış
Bir seçenek girin (1-5): 2
Yeni görevi girin (boş bırakmayın): Alışveriş yap
Görev eklendi!

=== To-Do List Uygulaması ===
1. Görevleri Listele
2. Yeni Görev Ekle
3. Görev Düzenle
4. Görev Sil
5. Çıkış
Bir seçenek girin (1-5): 1
Görevler:
1. Alışveriş yap
