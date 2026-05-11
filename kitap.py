# Bu dosya projenin "Veri Yapısı" kısmıdır. Her bir kitabın hangi özelliklere sahip olacağını burada tanımlıyoruz.
class Kitap:
    def __init__(self, ad, yazar, isbn, raf, sira):
        self.ad = ad
        self.yazar = yazar
        self.isbn = isbn
        self.raf = raf
        self.sira = sira
        self.durum = "Mevcut"

    def __str__(self):
        return f"Kitap: {self.ad} | Yazar: {self.yazar} | Konum: Raf {self.raf}, Sıra {self.sira} | ISBN: {self.isbn}"
# __init__ fonksiyonu kitap nesnesi oluşturulduğunda çalışan kurucu (constructor) metodudur.