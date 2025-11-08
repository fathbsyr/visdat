import streamlit as st
import pandas as pd
import numpy as np

st.title("LINE CHART")
st.header("Praktikum 2 Visualisasi Data")
st.subheader("Bagian 2: LINE CHART")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

st.subheader("Line Chart Biasa")
df = pd.DataFrame (
    np.random.randn(50, 10),
    columns=['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10']
)
st.line_chart(df)
