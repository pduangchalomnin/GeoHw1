import cv2
import numpy as np
from matplotlib import pyplot as plt

import os



counter = 0

allfiles=os.listdir(os.getcwd())
imlist=[filename for filename in allfiles if  filename[-4:] in [".jpg",".jpg"]]

for filename in imlist:
	
	img = cv2.imread(filename,0)
	edges = cv2.Canny(img,50,100)
	edges = cv2.bitwise_not(edges)
	name = str(counter)+".jpg"
	#print counter 
	cv2.imwrite(name,edges)
	counter = counter + 1
	