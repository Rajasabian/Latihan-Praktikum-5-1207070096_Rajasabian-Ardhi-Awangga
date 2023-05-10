import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

loadimage = imread('lah gambar.jpg')

loadimageCropped = loadimage.copy()
loadimageCropped = loadimageCropped[0:256,64:320]

copyloadimage = loadimageCropped.copy().astype(float)

shape = np.shape(copyloadimage)
output1 = np.empty(shape)

for baris in range(0, shape[0]):
    for kolom in range(0, shape[1]):
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyloadimage[baris, kolom] + 100
        
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

plt.show()