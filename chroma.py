import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("aviao.jpg")
#cv2.imshow("original", img)

img2 = np.zeros(img.shape, np.uint8 )
img2[:,:,2] = img[:,:,2]
img2[:,:,1] = img[:,:,1]
img2[:,:,0] = img[:,:,0]
#cv2.imshow( "img2", img2)


#converte em YCrCb
img3=cv2.cvtColor( img, cv2.COLOR_BGR2YCR_CB)
cv2.imshow("YCrCb", img3)
#print( img.shape[0])

