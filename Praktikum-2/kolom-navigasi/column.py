import streamlit as st

st.title("COLUMN NAVIGATION")
st.header("Praktikum 2 Visualisasi Data")
st.subheader("Bagian 1 (COLUMN): Navigasi Kolom")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../../Praktikum-1/assets/w11-in-barcelona.jpg", caption="Gambar W11 di Barcelona")

col2.write("Ini adalah kolom kedua")
col2.image("../../Praktikum-1/assets/w11-in-tuscan.jpg", caption="Gambar W11 di Tuscan")