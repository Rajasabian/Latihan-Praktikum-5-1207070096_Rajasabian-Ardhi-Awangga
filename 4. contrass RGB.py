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

#Membuat variabel img_rgbcontrass untuk menampung hasil
img_rgbcontrass = np.zeros(img.shape, dtype = np.uint8)

#Melakukan penambahan contrass dengan nilai yg menjadi parameter
def rgbcontrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red     = img[y][x][0]
            red     += nilai
            if red > 255:
                red = 255
            green   = img[y][x][1]
            green     += nilai
            if green > 255:
                green = 255
            blue    = img[y][x][2]
            blue    += nilai
            if blue > 255:
                blue = 255
            img_rgbcontrass[y][x] = (red, green, blue)

#Menampilkan beberapa hasil dengan nilai contrass 2 dan 25
rgbcontrass(2)
plt.imshow(img_rgbcontrass)
plt.title('Contrass 2')
plt.show()

rgbcontrass(50)
plt.imshow(img_rgbcontrass)
plt.title('Contrass 50')
plt.show()