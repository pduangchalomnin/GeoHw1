import cv2
import numpy as np
from matplotlib import pyplot as plt

import os



counter = 0
for filename in os.listdir('/Users/Jules/Documents/cartography/test'):
	
	img = cv2.imread(filename,0)
	edges = cv2.Canny(img,50,100)
	edges = cv2.bitwise_not(edges)
	name = str(counter)+".jpg"
	#print counter
	cv2.imwrite(name,edges)
	counter = counter + 1
	