import cv2
import numpy as np
from matplotlib import pyplot as plt
import scipy.ndimage
from scipy import ndimage

from PIL import Image

import os

if not os.path.exists('Input'):
    os.makedirs('Input')

if not os.path.exists('Output'):
    os.makedirs('Output')

if not os.path.exists('Intermediate'):
    os.makedirs('Intermediate')

folder='./Intermediate'

for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

counter = 0

allfiles=os.listdir(os.getcwd()+'/Input')
imlist=[filename for filename in allfiles if  filename[-4:] in ['.jpg','.jpg']]
print "Step 1 edge detection."
for filename in imlist:
	filename = './Input/'+filename
	print "Working on: "
	print filename
	img = cv2.imread(filename,0)
	edges = cv2.Canny(img,50,100)
	edges = cv2.bitwise_not(edges)
	name = './Intermediate/'+str(counter)+'.jpg'
	#print counter 
	cv2.imwrite(name,edges)
	counter = counter + 1

print "Intermediate images generated: "
print counter


allfiles=os.listdir(os.getcwd()+'/Intermediate')
imlist=[filename for filename in allfiles if  filename[-4:] in ['.jpg','.jpg']]
ims = []

print "Step 2 averaging images."
for filename in imlist:
	filename = './Intermediate/'+filename
	print "Working on: "
	print filename
	ims.append(scipy.ndimage.imread(filename, flatten = True))

print ims[0].shape # (100, 100)

ims = np.vstack([im.reshape(1,im.shape[0] * im.shape[1]) for im in ims])
print ims.shape # (5, 10000)

median = np.mean(ims, axis=0).reshape(2032, 2032)

fig = plt.figure(figsize=(500./109., 500./109.), dpi=109, frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.imshow(median, cmap='Greys',interpolation='nearest')

fig.savefig('./Intermediate/mean.png',dpi=100)


image_file = Image.open('./Intermediate/mean.png') # open colour image
#image_file = image_file.convert('1') # convert image to black and white
image_file = image_file.convert('L')
bw = image_file.point(lambda x: 0 if x<10 else 255, '1')
bw.save('./Intermediate/grey.png')

im2 = Image.open('./Intermediate/grey.png')
im2 = ndimage.binary_dilation(im2, iterations = 4)
scipy.misc.imsave('./Output/dilation.png', im2)
print "Done!"