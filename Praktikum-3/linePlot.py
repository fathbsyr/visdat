import streamlit as st 
import matplotlib.pyplot as plt 

st.title("Matplotlib Line Plot")
st.header("Praktikum 3 Visualisasi Data")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

# Mengubah nama variabel data bulan dan penjualan
list_bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sept', 'Okt', 'Nov', 'Des']
data_jual_a = [56, 78.90, 43, 45, 67, 12, 48, 80, 12, 24, 50, 90]
data_jual_b = [66, 71.35, 36, 48, 70, 24, 34, 90, 98, 1, 30, 90]
data_jual_c = [56, 24, 67, 45, 24, 10, 90, 78, 56, 34, 23, 45]
data_jual_d = [67, 34, 78, 23, 45, 66, 77, 12, 34, 56, 89, 99]

# Judul Utama
st.title("Dashboard Penjualan Produk")

# Sidebar Konfigurasi
st.sidebar.header("Pengaturan Tampilan")
menu_pilihan = st.sidebar.selectbox(
    "Pilih Tipe Visualisasi", 
    ("Grafik Garis Tunggal", "Grafik Ganda & Kustomisasi", "Analisa Tren Garis", "Subplot Terpisah")
)

# Fungsi 1: Grafik Tunggal
def single_plot():
    figur, area = plt.subplots()
    area.plot(list_bulan, data_jual_a, label="Produk A")
    area.set_title('Grafik Penjualan Produk A (Bulanan)')
    area.set_xlabel('Bulan')
    area.set_ylabel('Total Penjualan')
    area.grid(True)
    st.pyplot(figur)

# Fungsi 2: Grafik Ganda
def multi_plot():
    figur, area = plt.subplots()
    area.plot(list_bulan, data_jual_a, label="Produk A", marker="o", linestyle="--")
    area.plot(list_bulan, data_jual_b, label="Produk B", marker="x", linestyle="-")

    area.set_title('Perbandingan Penjualan Produk')
    area.set_xlabel('Periode Bulan')
    area.set_ylabel('Total Penjualan')
    area.legend()
    area.grid(True)
    st.pyplot(figur)

# Fungsi 3: Tren Garis
def tren():
    figur, area = plt.subplots()
    area.plot(list_bulan, data_jual_c, label="Produk C", color='green', linestyle="dashdot")
    area.plot(list_bulan, data_jual_d, label="Produk D", color='purple', linestyle=":")
    area.set_title('Analisa Tren Penjualan (Style Garis)')
    area.set_xlabel('Periode')
    area.set_ylabel('Jumlah Terjual')
    area.grid(axis='y', linestyle=':')
    area.legend() # Menambahkan legend agar label muncul
    st.pyplot(figur)

# Fungsi 4: Subplots
def sub_plot():
    figur, area = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    # Plot Atas
    area[0].plot(list_bulan, data_jual_c, label="Produk C", linestyle="--")
    area[0].set_title('Laporan Penjualan Produk C')
    area[0].set_ylabel('Unit Terjual')
    area[0].legend()
    area[0].grid(True)

    # Plot Bawah
    area[1].plot(list_bulan, data_jual_d, label="Produk D", linestyle="--")
    area[1].set_title('Laporan Penjualan Produk D')
    area[1].set_xlabel('Bulan')
    area[1].set_ylabel('Unit Terjual')
    area[1].legend()
    area[1].grid(True)

    plt.tight_layout()
    st.pyplot(figur)

# Logika Menu
if menu_pilihan == "Grafik Garis Tunggal":
    single_plot()
elif menu_pilihan == "Grafik Ganda & Kustomisasi":
    multi_plot()
elif menu_pilihan == "Analisa Tren Garis":
    tren()
elif menu_pilihan == "Subplot Terpisah":
    sub_plot()