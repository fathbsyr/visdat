import streamlit as st
from PIL import Image

st.title("PADDING")
st.header("Praktikum 2 Visualisasi Data")
st.subheader("Bagian 2: Navigasi Kolom")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

img = Image.open("../../Praktikum-1/assets/w11-in-barcelona.jpg")
# Defining Padding with columns
col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)