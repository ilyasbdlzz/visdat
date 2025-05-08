import matplotlib.pyplot as plt

tahun = [2018, 2019, 2020, 2021, 2022]
penjualan_A = [100, 120, 90, 150, 200]
penjualan_B = [90, 110, 80, 130, 180]

plt.subplot(1, 2, 1)
plt.plot(tahun, penjualan_A, 'b-')
plt.title('Produk A')

plt.subplot(1, 2, 2)
plt.plot(tahun, penjualan_B, 'g-')
plt.title('Produk B')

plt.suptitle('Penjualan Produk per Tahun')
plt.tight_layout()
plt.show()
