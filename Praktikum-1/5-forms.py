import streamlit as st
import datetime 

st.header("Praktikum 5 Forms")
st.subheader("Bagian 5: membuat banyak tipe form")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

# membuat textbox
st.header("Buat Textbox")
NamaLengkap = st.text_input("Masukkan Nama Lengkap Anda")
st.write("Nama Lengkap Anda Adalah: ",NamaLengkap)
# membuat textbox tipe password
st.header("Buat Textbox Tipe Password")
Password = st.text_input("Masukkan Password Anda", type="password")
# membuat textbox maksimal 5 karakter
st.header("Buat Textbox Maksimal 5 Karakter")
NamaLengkap = st.text_input("Masukkan Nama Lengkap Anda", max_chars=5)

# membuat text area
TeksArea = st.text_area("Masukkan Teks Anda")
st.write("Teks Anda Adalah: ",TeksArea)

# membuat form pengisian angka
st.header("Buat Form Pengisian Angka")
st.write("minimal angka adalah 0, \n maksimal angka adalah 1000")
AngkA = st.number_input("Masukkan angka", min_value=0, max_value=1000, value=5, step=10)
st.write("default angka adalah 5, \n step angka adalah 10")
st.write("Total Nilai Angka Anda Adalah: ",AngkA)

# membuat form input waktu
st.header("Buat Form Input Waktu")
st.time_input("Masukkan waktu lokal anda")

# membuat form input tanggal
st.header("Buat Form Input Tanggal")
st.date_input("Pilih Tanggal Mu", value=datetime.date(2025, 11, 2),
min_value=datetime.date(2025, 11, 2),
max_value=datetime.date(2100, 1, 1))

