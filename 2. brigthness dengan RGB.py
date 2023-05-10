#memanggil library
import numpy as np
import matplotlib.pyplot as plt
import cv2

#membaca gambar
img = cv2.imread('lah gambar.jpg')

#mendapatkan resolusi dan type dari gambar
img_height  = img.shape[0]
img_width   = img.shape[1]
img_channel = img.shape[2]
img_type    = img.dtype

#membuat variabel img_rgbbrightness untuk menampung hasil
img_rgbbright = np.zeros(img.shape, dtype = np.uint8)

#melakukan penambahan brightness dengan nilai yg menjadi parameter
def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red     = img[y][x][0]
            red     += nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            green   = img[y][x][1]
            green     += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            blue    = img[y][x][2]
            blue    += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            img_rgbbright[y][x] = (red, green, blue)

#menampilkan beberapa hasil dengan nilai brightness -100 dan 100
rgbbrighter(-100)
plt.imshow(img_rgbbright)
plt.title('Brightness -100')
plt.show()

rgbbrighter(100)
plt.imshow(img_rgbbright)
plt.title('Brightness 100')
plt.show()