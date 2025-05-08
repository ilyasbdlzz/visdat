import streamlit as st
import matplotlib.pyplot as plt

# Data
tahun = [2018, 2019, 2020, 2021, 2022]
penjualan = [100, 120, 90, 150, 200]

# Judul
st.title("Visualisasi Penjualan per Tahun")

# Menampilkan data
st.write("Data Penjualan:")
st.write(penjualan)

# Membuat plot
fig, ax = plt.subplots()
ax.plot(tahun, penjualan)
ax.set_xlabel('Tahun')
ax.set_ylabel('Penjualan')
ax.set_title('Penjualan per Tahun')

# Menampilkan plot di Streamlit
st.pyplot(fig)
