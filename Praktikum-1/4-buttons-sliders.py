import streamlit as st
import time 

st.header("Praktikum 4 Button & Sliders")
st.subheader("Bagian 4: Button & Sliders")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

# membuat tombol biasa
st.header("Buat Tombol")
tombol = st.button("Klik Saya")
if tombol:
    st.write("Lu pada udah klik")
else :
    st.write("Lu pada beloman klik njir")

# membuat tombol radio
st.header("Buat Tombol Radio")
team = st.radio("Pilih Team F1", ("Mercedes-AMG Petronas F1 Team", "Mclaren", "Oracle Red Bull Racing", "Scuderia Ferrari"))
if team == "Mercedes-AMG Petronas F1 Team":
    st.write("Anda fans Mercedes-AMG Petronas F1 Team")
elif team == "Mclaren":
    st.write("Anda fans Mclaren")
elif team == "Oracle Red Bull Racing":
    st.write("Anda fans Oracle Red Bull Racing")
elif team == "Scuderia Ferrari":
    st.write("Anda fansScuderia Ferrari")
else:
    st.write("Anda bukan fans F1")

# membuat tombol check
st.header("Buat Tombol Check")
st.write("Pilihlah yang anda suka")
hobi = st.checkbox("Futsal")
hobi2 = st.checkbox("Bulu Tangkis")
hobi3 = st.checkbox("Sepak Bola")

# membuat tombol dropdown
st.header("Buat Tombol Dropdown")
team = st.selectbox("Pilih Team F1", ("Mercedes-AMG Petronas F1 Team", "Mclaren", "Oracle Red Bull Racing", "Scuderia Ferrari"))

# membuat tombol multi pilihan 
st.header("Buat Tombol Multi Pilihan")
team = st.multiselect("Pilih Team F1", ("Mercedes-AMG Petronas F1 Team", "Mclaren", "Oracle Red Bull Racing", "Scuderia Ferrari"))

# membuat tombol download 
st.header("Buat Tombol Download")
downLoad = st.download_button(
label = "Download Gambar",
data =open("assets\silverstone.jpg", "rb"),
file_name = "silverstone.jpg",
mime = "image/jpg"
)

# membuat tampilan batang progress
st.header("Progress Lu Sekarang")
progres = st.progress(0)
for i in range(100):
    time.sleep(0.5)
    progres.progress(i+1)
st.write("Selesai")

# membuat tampilan spinner
st.header("Spinner Lu Sekarang")
with st.spinner("Loading...."):
    time.sleep(0.1)
st.write("Selesai")