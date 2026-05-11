# Burası kütüphane işlemlerinin yapıldığı (ekleme, listeleme) kısımdır.
from kitap import Kitap

class Kutuphane:
    def __init__(self):
        # Kitap nesnelerini tutacağımız liste
        self.kitaplar = []
        # Program başlar başlamaz dosyadan verileri çek
        self.verileri_yukle()

    def kitap_ekle(self, kitap_objesi):
        # ISBN'leri temizleyip karşılaştıralım (Boşluk kalmasın)
        yeni_isbn = str(kitap_objesi.isbn).strip()
        
        for mevcut_kitap in self.kitaplar:
            if str(mevcut_kitap.isbn).strip() == yeni_isbn:
                print(f"\n[HATA] {yeni_isbn} numaralı ISBN zaten kayıtlı!")
                return False
        
        # Ekleme işlemi
        self.kitaplar.append(kitap_objesi)
        self.verileri_kaydet()
        print(f"\n[SİSTEM] '{kitap_objesi.ad}' eklendi.")
        return True
    
    def kitap_sil(self, isbn):
        for kitap in self.kitaplar:
            if kitap.isbn == isbn:
                self.kitaplar.remove(kitap)
                self.verileri_kaydet()
                print(f"\n[SİSTEM] ISBN: {isbn} olan kitap başarıyla silindi.")
                return True
        print(f"\n[HATA] {isbn} numaralı kitap bulunamadı.")
        return False

    def kitaplari_listele(self):
        if not self.kitaplar:
            print("\nKütüphane şu an boş.")
        else:
            print("\n--- KÜTÜPHANE ENVANTER LİSTESİ ---")
            for kitap in self.kitaplar:
                print(kitap)

    def kitap_ara(self, aranan):
        sonuclar = [k for k in self.kitaplar if aranan.lower() in k.ad.lower() or aranan.lower() in k.yazar.lower()]
        if sonuclar:
            print(f"\n--- '{aranan}' Araması İçin Sonuçlar ---")
            for k in sonuclar:
                print(k)
        else:
            print(f"\n[BİLGİ] '{aranan}' aramasına uygun bir kayıt bulunamadı.")

    def verileri_kaydet(self):
        try:
            with open("kutuphane_verisi.txt", "w", encoding="utf-8") as f:
                for k in self.kitaplar:
                    # Tüm 6 veriyi virgülle ayırarak yazıyoruz
                    f.write(f"{k.ad},{k.yazar},{k.isbn},{k.raf},{k.sira},{k.durum}\n")
        except Exception as e:
            print(f"Veri yazma hatası: {e}")

    def verileri_yukle(self):
        try:
            with open("kutuphane_verisi.txt", "r", encoding="utf-8") as f:
                for satir in f:
                    veriler = satir.strip().split(",")
                    # 6 verinin de tam olduğundan emin oluyoruz
                    if len(veriler) == 6:
                        ad, yazar, isbn, raf, sira, durum = veriler
                        yeni_kitap = Kitap(ad, yazar, isbn, raf, sira)
                        yeni_kitap.durum = durum
                        self.kitaplar.append(yeni_kitap)
        except FileNotFoundError:
            # İlk çalıştırmada dosya yoksa hata vermez
            pass
# Bu modül projenin iş mantığını yürütür ve modüler yapı kuralını karşılar.