import matplotlib.pyplot as plt

tahun = [2018, 2019, 2020, 2021, 2022]
penjualan = [100, 120, 90, 150, 200]

plt.plot(tahun, penjualan, 'r--')  # Garis merah putus-putus
plt.xlabel('Tahun')
plt.ylabel('Penjualan')
plt.title('Trend Penjualan')
plt.show()
