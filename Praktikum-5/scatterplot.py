import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Bar Chart")
st.header("Praktikum 4 Bar Chart")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

climate = [20, 22, 24, 26, 28, 30, 32, 34, 36]
jualan = [50, 70, 90, 100, 130, 150, 155, 160, 180]

st.title('Visualisasi hubungan penjualan eskrim dengan suhu')
fig, ax = plt.subplots()
ax.scatter(climate, jualan, color='blue')
ax.set_title('Hubungan Penjualan Eskrim dengan Suhu')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan')
st.pyplot(fig)

st.title('Kustomisasi Scatter Plot')
fig, ax = plt.subplots()
ax.scatter(climate, jualan, color='green', s=100, alpha=0.5, edgecolors='black')
ax.set_title('Hubungan Penjualan Eskrim dengan Suhu')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan')
ax.grid(True)
st.pyplot(fig)

st.title('Multiple Scatter Plot')
jualan = [50, 70, 90, 100, 130, 150, 155, 160, 180]
jualan_weekend = [60, 73, 94, 105, 136, 157, 158, 169, 180]
ax.scatter(climate, jualan, color='green', s=100, alpha=0.5, edgecolors='black', label='hari biasa')
ax.scatter(climate, jualan_weekend, color='blue', s=100, alpha=0.5, edgecolors='black', label='hari libur')
ax.set_title('Hubungan Penjualan Eskrim dengan Suhu')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan')
ax.legend()
st.pyplot(fig)

st.title('Analisa Scatterplot')
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Chocolate': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Vanilla': [60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Nutella': [40, 50, 60, 70, 80, 90, 100, 110, 120],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}
df = pd.DataFrame(data)
st.subheader('Analisis penjualan eskrim berdasarkan suhu')
jenis = st.selectbox('Pilih Jenis Eksrim: ', ['Chocolate', 'Vanilla', 'Nutella'])
penjualan = df[jenis]
if jenis == 'Chocolate':
    penjualan = df['Chocolate']
elif jenis == 'Vanilla':
    penjualan = df['Vanilla']
elif jenis == 'Nutella':
    penjualan = df['Nutella']
st.subheader('Data Penjualan dan Suhu')
st.dataframe(df)
fig, ax = plt.subplots()
scatter = ax.scatter (df ['Suhu'], penjualan, c=df['Kelembapan'], s = 100 , cmap='coolwarm', alpha=0.7)
ax.set_title(f'Hasil Penjualan {jenis} vs Suhu dan Kelembapan')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel(f'Penjualan Es Krim {jenis}')
fig.colorbar (scatter, label='Kelembapan (%)')
st.pyplot(fig)
st.write(f"Grafik menunjukkan hubungan antara suhu, kelembapan, dan penjualan es krim jenis **{jenis}**.")