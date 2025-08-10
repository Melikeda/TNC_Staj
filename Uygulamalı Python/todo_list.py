# To-Do List Uygulaması
# Görevlerin eklenmesi, listelenmesi, düzenlenmesi ve silinmesi için bir konsol uygulaması
# Görevler bir metin dosyasında saklanır

import os

# Görevleri saklamak için global liste
gorevler = []

# Dosya adı sabiti
DOSYA_ADI = "gorevler.txt"

def dosya_oku():
    """Metin dosyasından görevleri oku ve listeye ekle."""
    try:
        if os.path.exists(DOSYA_ADI):
            with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    gorev = satir.strip()
                    if gorev:  # Boş satırları atla
                        gorevler.append(gorev)
    except Exception as e:
        print(f"Dosya okunurken hata oluştu: {e}")

def dosya_yaz():
    """Görevleri metin dosyasına kaydet."""
    try:
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            for gorev in gorevler:
                dosya.write(gorev + "\n")
    except Exception as e:
        print(f"Dosya yazılırken hata oluştu: {e}")

def gorevleri_listele():
    """Mevcut görevleri numaralandırılmış şekilde listele."""
    if not gorevler:
        print("Görev listesi boş!")
        return
    print("\nGörevler:")
    for i, gorev in enumerate(gorevler, 1):
        print(f"{i}. {gorev}")

def yeni_gorev_ekle():
    """Yeni bir görev ekle."""
    while True:
        gorev = input("Yeni görevi girin (boş bırakmayın): ").strip()
        if not gorev:
            print("Hata: Görev boş olamaz!")
            continue
        gorevler.append(gorev)
        dosya_yaz()
        print("Görev eklendi!")
        break

def gorev_duzenle():
    """Mevcut bir görevi düzenle."""
    gorevleri_listele()
    if not gorevler:
        return
    while True:
        try:
            secim = input("Düzenlemek istediğiniz görev numarasını girin: ")
            gorev_no = int(secim) - 1
            if 0 <= gorev_no < len(gorevler):
                yeni_gorev = input("Yeni görev metnini girin (boş bırakmayın): ").strip()
                if not yeni_gorev:
                    print("Hata: Yeni görev boş olamaz!")
                    continue
                gorevler[gorev_no] = yeni_gorev
                dosya_yaz()
                print("Görev düzenlendi!")
                break
            else:
                print("Hata: Geçersiz görev numarası!")
        except ValueError:
            print("Hata: Lütfen bir sayı girin!")

def gorev_sil():
    """Mevcut bir görevi sil."""
    gorevleri_listele()
    if not gorevler:
        return
    while True:
        try:
            secim = input("Silmek istediğiniz görev numarasını girin: ")
            gorev_no = int(secim) - 1
            if 0 <= gorev_no < len(gorevler):
                silinen = gorevler.pop(gorev_no)
                dosya_yaz()
                print(f"'{silinen}' görevi silindi!")
                break
            else:
                print("Hata: Geçersiz görev numarası!")
        except ValueError:
            print("Hata: Lütfen bir sayı girin!")

def ana_menu():
    """Uygulamanın ana menüsünü göster ve kullanıcı seçimini işle."""
    dosya_oku()  # Program başında görevleri oku
    while True:
        print("\n=== To-Do List Uygulaması ===")
        print("1. Görevleri Listele")
        print("2. Yeni Görev Ekle")
        print("3. Görev Düzenle")
        print("4. Görev Sil")
        print("5. Çıkış")
        secim = input("Bir seçenek girin (1-5): ").strip()
        
        if secim == "1":
            gorevleri_listele()
        elif secim == "2":
            yeni_gorev_ekle()
        elif secim == "3":
            gorev_duzenle()
        elif secim == "4":
            gorev_sil()
        elif secim == "5":
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Hata: Geçersiz seçim! Lütfen 1-5 arasında bir sayı girin.")

# Programın başlangıç noktası
if __name__ == "__main__":
    ana_menu()