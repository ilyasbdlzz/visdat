import matplotlib.pyplot as plt

# Data
tahun = [2018, 2019, 2020, 2021, 2022]
penjualan = [100, 120, 90, 150, 200]


# Membuat plot
plt.plot(tahun, penjualan)
plt.xlabel('Tahun')
plt.ylabel('Penjualan')
plt.title('Penjualan per Tahun')
plt.show()
