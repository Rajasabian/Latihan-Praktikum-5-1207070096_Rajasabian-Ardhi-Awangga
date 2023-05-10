#Menambahkan Library
import numpy as np
import matplotlib.pyplot as plt
import cv2

#Membaca gambar
img = cv2.imread('ini juga gambar.jpg')

#Mendapatkan resolusi dan type dari gambar
img_height  = img.shape[0]
img_width   = img.shape[1]
img_channel = img.shape[2]
img_type    = img.dtype

#Membuat variabel img_contrass untuk menampung hasil
img_contrass = np.zeros(img.shape, dtype = np.uint8)

#Melakukan penambahan contrass dengan nilai yg menjadi parameter
def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red     = img[y][x][0]
            green   = img[y][x][1]
            blue    = img[y][x][2]
            gray    = (int(red) + int(green) + int(blue))/3
            gray    += nilai
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_contrass[y][x] = (gray, gray, gray)

#Menampilkan beberapa hasil dengan nilai contrass 2 dan 25
contrass(2)
plt.imshow(img_contrass)
plt.title('Contrass 2')
plt.show()

contrass(25)
plt.imshow(img_contrass)
plt.title('Contrass 25')
plt.show()