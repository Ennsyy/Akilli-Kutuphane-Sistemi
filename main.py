# Bu dosya ana çalışma dosyasıdır. Program sadece buradan çalıştır. Diğer iki modülü burada birleştiriyoruz.
from kitap import Kitap
from kutuphane import Kutuphane

def menu():
    my_kutuphane = Kutuphane()
    
    while True:
        print("\n--- TOSYA MYO KÜTÜPHANE SİSTEMİ ---")
        print("1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Sil")
        print("4. Kitap Ara")
        print("5. Çıkış")
        
        secim = input("Seçiminiz: ")
        
        if secim == "1":
            ad = input("Kitap Adı: ")
            yazar = input("Yazarı: ")
            isbn = input("ISBN: ")
            raf = input("Raf: ")
            sira = input("Sıra: ")
            yeni_kitap = Kitap(ad, yazar, isbn, raf, sira)
            my_kutuphane.kitap_ekle(yeni_kitap)
            
        elif secim == "2":
            my_kutuphane.kitaplari_listele()
            
        elif secim == "3":
            silinecek_isbn = input("Silinecek kitabın ISBN numarasını girin: ")
            my_kutuphane.kitap_sil(silinecek_isbn)

        elif secim == "4":
            kelime = input("Aranacak kitap adı veya yazar: ")
            my_kutuphane.kitap_ara(kelime)
            
        elif secim == "5":
            print("Sistemden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()