import matplotlib.pyplot as plt

tahun = [2018, 2019, 2020, 2021, 2022]
penjualan_A = [100, 120, 90, 150, 200]
penjualan_B = [90, 110, 80, 130, 180]

plt.plot(tahun, penjualan_A, label='Produk A')
plt.plot(tahun, penjualan_B, label='Produk B')
plt.xlabel('Tahun')
plt.ylabel('Penjualan')
plt.title('Penjualan Produk A dan B per Tahun')
plt.legend()
plt.show()
