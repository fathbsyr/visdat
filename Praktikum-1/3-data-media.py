import streamlit as st 
import base64
from PIL import Image

st.header("Praktikum 3 Visualisasi Data")
st.subheader("Bagian 3: Data Media")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

# menampilkan gambar biasa
st.write("Menampilkan Gambar Mercedes W11 di tuscan")
st.image("assets\w11-in-tuscan.jpg")
st.write("Sumber Image: Wikipedia")
# menampilkan multiple gambar
st.write("Menampilkan Multiple Gambar Mercedes W15")
w15 = [
    "assets\w15-in-belgian.jpg",
    "assets\w15-in-silverstone.jpg",
    "assets\w15-in-vegas.jpg",
]
st.image(w15, width=230)
st.write("Sumber Image: Google")


# backgound image
def background_image(gambar):
    with open(gambar, "rb") as gambar:
        encoded_string = base64.b64encode(gambar.read())
    st.write("Sumber Image: Google")
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }},
    </style>
    """,
    unsafe_allow_html=True
    )
st.write("Menampilkan Background Image")
background_image("assets\mercedes-dark.jpg")


# mengubah ukuran gambar 
gambar_ori = Image.open("assets\w11-in-barcelona.jpg")
st.title("Gambar Asli")
st.image(gambar_ori)
ubah_ukuran = gambar_ori.resize((400, 300))
st.title("Gambar Resized")
st.image(ubah_ukuran)