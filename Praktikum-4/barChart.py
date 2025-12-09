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

st.title("Bar Chart")
st.header("Praktikum 4 Bar Chart")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

data = {
    'Jurusan' : ['Informatika', 'Teknik Komputer', 'Teknik Elektro', 'Teknik Mesin', 'Teknik Industri', 'ADILI JOKOWI'],
    'Jumlah' : [100, 150, 200, 250, 300, 800]
}

df = pd.DataFrame(data)

st.title("Basic Bar Chart - Jumlah Mahasiswa Per Jurusan")
st.bar_chart(df.set_index('Jurusan'))

st.title("Basic Bar Chart Dengan Matplotlib")
fig, ax = plt.subplots()
ax.bar(data['Jurusan'], data['Jumlah'], color = 'skyblue')
ax.set_title("Jumlah Mahasiswa Per Jurusan")
ax.set_xlabel("Jurusan")
ax.set_ylabel("Jumlah Mahasiswa")
ax.tick_params(axis='x', rotation=45) 
st.pyplot(fig)

st.title("Kustomasi Bar Chart")
fig, ax = plt.subplots()
colors = ['green', 'blue', 'yellow', 'orange', 'black', 'red']
bars = ax.bar(data['Jurusan'], data['Jumlah'], color=colors)
ax.set_title("Jumlah Mahasiswa Per Jurusan")
ax.set_xlabel("Jurusan")
ax.set_ylabel("Jumlah Mahasiswa")
ax.tick_params(axis='x', rotation=45) 
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5, str(bar.get_height()), ha='center')
st.pyplot(fig)

st.title("Multiple Bar Chart")
data_2023 = [100, 150, 200, 250, 300, 800]
data_2024 = [120, 100, 150, 200, 250, 300]
x = range(len(data['Jurusan']))
width = 0.4
fig, ax = plt.subplots()
ax.bar(x, data_2023, width=width, label='2023')
ax.bar([p + width for p in x], data_2024, width=width, label='2024')
ax.set_title("Jumlah Mahasiswa Per Jurusan")
ax.set_xlabel("Jurusan")
ax.set_ylabel("Jumlah Mahasiswa")
ax.set_xticks([i + (width / 2) for i in x])
ax.set_xticklabels(data['Jurusan'], rotation=45, ha='right') 
ax.legend()
st.pyplot(fig)

st.title("analisis pola tren")
data = {
    'Tahun' : ['2019', '2020', '2021', '2022'],
    'Sastra Mesin' : [100, 150, 200, 250],
    'Teknik Biologi' : [120, 100, 150, 200],
    'Teknik Elektro' : [150, 200, 250, 300],
    'Adili Jokowi' : [500, 450, 400, 650]
}
df = pd.DataFrame(data)
st.header("Visualisasi Tren 4 Tahun Terakhir")
filter_tahun = st.multiselect("Pilih Tahun:", df['Tahun'], default=df['Tahun'])
jur_list = ['Sastra Mesin', 'Teknik Biologi', 'Teknik Elektro', 'Adili Jokowi']
filter_jur = st.multiselect("Pilih Jurusan:", jur_list, default=jur_list)
filtered_data = df[df['Tahun'].isin(filter_tahun)][['Tahun'] + filter_jur]
st.subheader('Data Jumlah Mahasiswa')
st.dataframe(filtered_data)
st.subheader("Bar Chart Dengan Filter")
fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(filtered_data['Tahun']))
width = 0.2
for i, jur in enumerate(filter_jur):
    ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)
ax.set_title("Jumlah Mahasiswa Per Jurusan")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Mahasiswa")
ax.set_xticks([p + width * len(filter_jur) / 2 - width / 2 for p in x])
ax.set_xticklabels(filtered_data['Tahun'], rotation=45, ha='right') 
ax.legend()
st.pyplot(fig)


