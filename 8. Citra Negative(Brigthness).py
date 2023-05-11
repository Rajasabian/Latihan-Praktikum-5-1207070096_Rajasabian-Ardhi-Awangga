#Mengimpor modul pyplot dari library matplotlib untuk membuat plot grafik
import matplotlib.pyplot as plt

#Mengimpor beberapa modul dari scikit-image, yaitu data, imread, rgb2gray, dan invert, serta modul numpy
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

#Membaca gambar dan menyimpannya ke dalam variabel loadimage
loadimage = imread('lah gambar.jpg')

#Menggandakan gambar asli dengan menggunakan method copy(), dan memotong bagian tertentu dari gambar menggunakan slicing.
loadimageCropped = loadimage.copy()
loadimageCropped = loadimageCropped[0:256,64:320]

#Membuat copy dari gambar yang telah dipotong
copyloadimage = loadimageCropped.copy().astype(float)

#mengubah tipe data menjadi float untuk menghindari overflow pada operasi penjumlahan
shape = np.shape(copyloadimage)
output1 = np.empty(shape)

#melakukan iterasi pada setiap piksel gambar dan menambahkan nilai brightness sebanyak 100 pada setiap piksel tersebut
#dan hasilnya disimpan di dalam variabel output1.
for baris in range(0, shape[0]):
    for kolom in range(0, shape[1]):
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyloadimage[baris, kolom] + 100
        
#Membuat figure dengan menggunakan plt.subplots(), yang menghasilkan array 2D dengan 2 baris dan 2 kolom
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(loadimageCropped, cmap='gray')
ax[0].set_title("Citra Input")

ax[1].hist(loadimageCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(output1, cmap='gray')
ax[2].set_title('Citra Output (Brightnes)')

ax[3].hist(output1.ravel(), bins=256)
ax[3].set_title('Histogram Output')

#Menampilkan gambar
plt.show()