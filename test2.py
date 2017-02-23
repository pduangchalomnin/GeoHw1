import os
import numpy as np
import scipy.ndimage
from scipy import ndimage
import matplotlib.pyplot as plt

from PIL import Image

allfiles=os.listdir(os.getcwd())
ims = [scipy.ndimage.imread(str(i + 1) + '.jpg', flatten=True) for i in range(68)]
# ims = [scipy.ndimage.imread(str(i + 1) + '.png', flatten=True) for i in range(5)]
print ims[0].shape # (100, 100)

ims = np.vstack([im.reshape(1,im.shape[0] * im.shape[1]) for im in ims])
print ims.shape # (5, 10000)

median = np.mean(ims, axis=0).reshape(2032, 2032)

fig = plt.figure(figsize=(500./109., 500./109.), dpi=109, frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.imshow(median, cmap='Greys',interpolation='nearest')
plt.show()
fig.savefig('output.jpg',dpi=100)


image_file = Image.open("output.jpg") # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save('result.png')

im2 = Image.open('result.png')
im2 = ndimage.binary_dilation(im2, iterations = 6)
scipy.misc.imsave('dilation.png', im2)
