import streamlit as st 
from PIL import Image

st.title("SPACED OUT")
st.header("Praktikum 2 Visualisasi Data")
st.subheader("Bagian 2: Navigasi Kolom")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

img = Image.open("../../Praktikum-1/assets/w11-in-barcelona.jpg")
# Defining two Rows
for _ in range(2):
# Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)