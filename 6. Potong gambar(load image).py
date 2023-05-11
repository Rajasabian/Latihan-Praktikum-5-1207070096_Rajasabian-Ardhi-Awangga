#Mengimpor modul pyplot dari library matplotlib untuk membuat plot grafik
import matplotlib.pyplot as plt

#Mengimpor beberapa modul dari scikit-image, yaitu data, imread, rgb2gray, dan invert, serta modul numpy
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

#Membaca dua gambar dan menyimpannya ke dalam variabel loadimage dan myimage
loadimage = imread('gambar tau.png')
myimage = imread('ini juga gambar.jpg')

#Menggandakan gambar asli dengan menggunakan method copy(), dan memotong bagian tertentu dari gambar menggunakan slicing.
loadimageCropped = loadimage.copy()
loadimageCropped = loadimageCropped[0:256,64:320]

myimageCropped = myimage.copy()
myimageCropped = myimageCropped[64:256,128:320]

#Membuat figure dengan menggunakan plt.subplots(), yang menghasilkan array 2D dengan 2 baris dan 2 kolom
fig, axes = plt.subplots(2, 2, figsize=(12,12))
ax = axes.ravel()
ax[0].imshow(loadimage)
ax[0].set_title("Citra Input 1")
ax[1].imshow(myimage, cmap='gray')
ax[1].set_title('Citra Input 2')
ax[2].imshow(loadimageCropped)
ax[2].set_title('CItra Output 1')
ax[3].imshow(myimageCropped, cmap='gray')
ax[3].set_title("Citra Output 2")

#Menampilkan gambar
plt.show()