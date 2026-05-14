# 📚 Kütüphane Yönetim Sistemi (Python OOP)

Bu proje, bir kütüphanenin dijital envanterini yönetmek için geliştirilmiş, **Nesne Yönelimli Programlama (OOP)** prensiplerine dayalı modüler bir konsol uygulamasıdır. Verileri kalıcı olarak saklar, arama ve filtreleme yapılmasına olanak tanır.

---

## 🏗️ Proje Mimarisi

Sistem üç temel katman üzerine inşa edilmiştir. Bu yapı, kodun bakımını kolaylaştırır ve gelecekte yeni özellikler eklenmesine (örneğin grafik arayüz) imkan tanır.



### 1. `kitap.py` (Veri Modeli)
Kütüphanedeki her bir kitabı temsil eden sınıftır.
- **Özellikler:** Ad, Yazar, ISBN, Raf, Sıra ve Durum.
- **Metotlar:** Kitap bilgilerini okunaklı bir şekilde yazdırmak için `__str__` metodunu kullanır.

### 2. `kutuphane.py` (Yönetim Motoru)
Sistemin tüm mantıksal işlemlerini yürüten sınıftır.
- **Veri Kaydı:** `txt` dosyası üzerinden okuma ve yazma işlemlerini yönetir.
- **Güvenlik:** Aynı ISBN numarasına sahip kitapların mükerrer kaydını engeller.
- **Arama:** Hem yazar hem kitap ismi üzerinden akıllı filtreleme yapar.

### 3. `app.py` (Kullanıcı Arayüzü)
Kullanıcı ile etkileşim kuran ana kontrolcü dosyasıdır.
- Terminal ekranını temizleyerek düzenli bir görünüm sunar.
- `while` döngüsü ile kesintisiz bir menü deneyimi sağlar.

---

## 📂 Dosya Yapısı

```text
.
├── app.py                # 🚀 Uygulamayı başlatan ana dosya
├── kutuphane.py          # ⚙️ Arka plan mantığı ve dosya yönetimi
├── kitap.py              # 📖 Kitap nesne kalıbı
└── kutuphane_verisi.txt  # 💾 Verilerin saklandığı kalıcı dosya (CSV formatında)

---

**Hazırlayan:** Muzaffer Enes Haklı - 255815035
