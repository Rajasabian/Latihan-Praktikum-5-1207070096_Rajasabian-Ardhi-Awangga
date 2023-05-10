import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

myimage = imread('ini juga gambar.jpg')

myimageCropped = myimage.copy()
myimageCropped = myimageCropped[0:256,64:320]

inv = invert(myimageCropped)
print('Shape Input : ', myimageCropped.shape)
print('Shape Output : ',inv.shape)

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

plt.show()