import streamlit as st
import numpy as np

st.title("CONTAINERS")
st.header("Praktikum 2 Visualisasi Data")
st.subheader("Bagian 2: Navigasi Kolom")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

with st.container():
    st.write("Element Inside Contianer")
    # Defining Chart Element
    st.line_chart(np.random.randn(40, 4))
st.write("Element Outside Container")

st.title("Out of Order Container")
# Defining Contianers
container_one = st.container()
container_one.write("Element One Inside Contianer")
st.write("Element Outside Contianer")
# Now insert few more elements in the container_one
container_one.write("Element Two Inside Contianer")
container_one.line_chart(np.random.randn(40, 4))