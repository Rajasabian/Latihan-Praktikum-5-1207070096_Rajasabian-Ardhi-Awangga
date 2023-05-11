#Mengimpor modul pyplot dari library matplotlib untuk membuat plot grafik
import matplotlib.pyplot as plt

#Mengimpor beberapa modul dari scikit-image, yaitu data, imread, rgb2gray, dan invert, serta modul numpy
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

#Membaca gambar dan menyimpannya ke dalam variabel myimage
myimage = imread('ini juga gambar.jpg')

#Menggandakan gambar asli dengan menggunakan method copy(), dan memotong bagian tertentu dari gambar menggunakan slicing.
myimageCropped = myimage.copy()
myimageCropped = myimageCropped[0:256,64:320]

# Membalikkan (inverting) gambar pertama menggunakan fungsi invert dari scikit-image
inv = invert(myimageCropped)

# Menampilkan informasi mengenai bentuk (shape) gambar asli dan hasil flipping
print('Shape Input : ', myimageCropped.shape)
print('Shape Output : ',inv.shape)

# Membuat subplot baru untuk menampilkan gambar asli, histogramnya, gambar hasil peningkatan kecerahan, dan histogramnya 
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(myimageCropped)
ax[0].set_title("Citra Input")
ax[1].hist(myimageCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')
ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')
ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')

#Menampilkan gambar
plt.show()