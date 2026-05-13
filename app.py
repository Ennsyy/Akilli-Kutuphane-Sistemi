import streamlit as st
from kutuphane import Kutuphane
from kitap import Kitap

# Sayfa Ayarları
st.set_page_config(page_title="Tosya MYO Kütüphane", layout="centered")

# Kütüphane nesnesini oturumda sakla (Sayfa yenilendiğinde veriler gitmesin)
if 'kutuphane' not in st.session_state:
    st.session_state.kutuphane = Kutuphane()

lib = st.session_state.kutuphane

st.title("📚 Tosya MYO Kütüphane Sistemi")
st.sidebar.header("İşlem Menüsü")

menu = st.sidebar.selectbox("Yapmak istediğiniz işlemi seçin:", 
                           ["Kitap Listele", "Yeni Kitap Ekle", "Kitap Ara", "Kitap Sil"])

if menu == "Kitap Listele":
    st.subheader("📋 Mevcut Kitaplar")
    if not lib.kitaplar:
        st.info("Kütüphane şu an boş.")
    else:
        for k in lib.kitaplar:
            st.write(f"**{k.ad}** - {k.yazar} (ISBN: {k.isbn})")
            st.caption(f"📍 Konum: Raf {k.raf}, Sıra {k.sira} | Durum: {k.durum}")
            st.divider()

elif menu == "Yeni Kitap Ekle":
    st.subheader("🆕 Yeni Kitap Kaydı")
    with st.form("ekleme_formu"):
        col1, col2 = st.columns(2)
        with col1:
            ad = st.text_input("Kitap Adı")
            yazar = st.text_input("Yazar")
            isbn = st.text_input("ISBN")
        with col2:
            raf = st.text_input("Raf No")
            sira = st.text_input("Sıra No")
        
        submit = st.form_submit_button("Sisteme Ekle")
        
        if submit:
            if ad and yazar and isbn:
                yeni = Kitap(ad, yazar, isbn, raf, sira)
                sonuc = lib.kitap_ekle(yeni)
                if sonuc:
                    st.success(f"{ad} başarıyla eklendi!")
                else:
                    st.error("Bu ISBN zaten kayıtlı!")
            else:
                st.warning("Lütfen zorunlu alanları doldurun.")

elif menu == "Kitap Ara":
    st.subheader("🔍 Kitap Arama")
    aranan = st.text_input("Kitap adı veya yazar girin:")
    if aranan:
        sonuclar = [k for k in lib.kitaplar if aranan.lower() in k.ad.lower() or aranan.lower() in k.yazar.lower()]
        if sonuclar:
            for k in sonuclar:
                st.write(f"✅ Bulundu: **{k.ad}** - Raf: {k.raf}")
        else:
            st.error("Sonuç bulunamadı.")

elif menu == "Kitap Sil":
    st.subheader("🗑️ Kitap Silme")
    sil_isbn = st.text_input("Silinecek kitabın ISBN numarasını girin:")
    if st.button("Sistemden Sil"):
        if lib.kitap_sil(sil_isbn):
            st.success("Kitap başarıyla silindi.")
        else:
            st.error("Kitap bulunamadı.")