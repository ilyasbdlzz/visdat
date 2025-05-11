import matplotlib.pyplot as plt

# Data
tahun = [2018, 2019, 2020, 2021, 2022]
penjualan = [100, 120, 90, 150, 200]

# Membuat plot
plt.plot(tahun, penjualan)
plt.xlabel('Tahun')
plt.ylabel('Penjualan')
plt.title('Penjualan per Tahun')

# Tambahkan nama kelompok ke dalam plot
anggota = [
    "Ilyas Abdul Aziz - 0110223292",
    "Muhamad Hilmi Kamil - 0110223293",
    "Ferisha Adilla Hidayat - 0110223286"
]
plt.figtext(0.5, -0.1, "\n".join(anggota), wrap=True, horizontalalignment='center', fontsize=10)

plt.tight_layout()
plt.show()
