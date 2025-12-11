import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.header("Praktikum 6 Visualisasi Data")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

stores = ['Store A', 'Store B', 'Store C']
laki = [150, 200, 180]
cewek = [120, 230, 170]

prod_a = [200, 250, 300]
prod_b = [150, 300, 200]

q1_laki = [150, 180, 160]
q1_cewek = [140, 200, 180]
q2_laki = [170, 190, 175]
q2_cewek = [150, 250, 120]

st.subheader("1. Stacked Vertival Bar Chart")
fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, laki, label='Pria', color='grey')
ax.bar(x, cewek, bottom=laki, label='Wanita', color='pink')
ax.set_title('Populasi Antara Gender dan Toko')
ax.set_xlabel('Toko')
ax.set_ylabel('Populasi')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()
st.pyplot(fig)

st.subheader("2. Stacked Vertival Bar Chart Dengan Matplotlib")
fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, prod_a, label='Produk A', color='blue')
ax.bar(x, prod_b, bottom=prod_a, label='Produk B', color='green')
ax.set_title('Penjualan Di Toko')
ax.set_xlabel('Toko')
ax.set_ylabel('Sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()
st.pyplot(fig)

st.subheader("3. Kustomisasi Stacked Vertival Bar Chart")
for i in range(len(x)):
    plt.text(x[i], prod_a[i]/2, str(prod_a[i]), ha='center', color='white')
    plt.text(x[i], prod_a[i] + prod_b[i]/2, str(prod_b[i]), ha='center', color='black')
st.pyplot(fig)

st.subheader("4. Multiple Stacked Vertival Bar Chart")
fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))
ax.bar(x - width/2, q1_laki, label='Q1 Pria', color='lightblue', width=width)
ax.bar(x - width/2, q1_cewek, bottom=q1_laki, label='Q1 Wanita', color='pink', width=width)
ax.bar(x + width/2, q2_laki, label='Q2 Pria', color='blue', width=width)
ax.bar(x + width/2, q2_cewek, bottom=q2_laki, label='Q2 Wanita', color='red', width=width)
ax.set_title('Populasi Antara Gender dan Toko (multiple)')
ax.set_xlabel('Toko')
ax.set_ylabel('Sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()
st.pyplot(fig)