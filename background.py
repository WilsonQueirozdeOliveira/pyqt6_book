import cv2
import numpy as np

x = 1200
y = 900

#img = np.zeros([y,x,3]).astype(np.uint8)

img = np.full((y,x),200).astype(np.uint8) 

img = cv2.imwrite("background_gray.jpg",img)
