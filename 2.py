import matplotlib.pyplot as plt

tahun = [2018, 2019, 2020, 2021, 2022]
penjualan = [100, 120, 90, 150, 200]

plt.plot(tahun, penjualan, color='green', linestyle='--', marker='o')
plt.xlabel('Tahun')
plt.ylabel('Penjualan')
plt.title('Penjualan per Tahun')
plt.grid(True)
plt.show()
