import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

loadimage = imread('gambar tau.png')
myimage = imread('ini juga gambar.jpg')

loadimageCropped = loadimage.copy()
loadimageCropped = loadimageCropped[0:256,64:320]

myimageCropped = myimage.copy()
myimageCropped = myimageCropped[64:256,128:320]

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

plt.show()