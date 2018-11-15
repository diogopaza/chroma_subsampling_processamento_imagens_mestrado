import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("aviao.jpg")

#converte em YCrCb
imgYCbCr=cv2.cvtColor( img, cv2.COLOR_BGR2YCR_CB)

#cv2.imshow("afs", imgYCbCr[:,:,1])
nova=np.zeros(imgYCbCr.shape)/2
print(nova.shape[0]/2)
v=2
h=2

y=  imgYCbCr[::2,::2,0]
cr= imgYCbCr[::2,::2,1]
cb= imgYCbCr[::2,::2,2]

#cr=cv2.boxFilter(imgYCbCr[:,:,1],ddepth=-1,ksize=(2,2))
#cb=cv2.boxFilter(imgYCbCr[:,:,2],ddepth=-1,ksize=(2,2))
#y=cv2.boxFilter(imgYCbCr[:,:,0],ddepth=-1,ksize=(2,2))
"""
Y=y[::v,::h]
chroma_cr=cr[::v,::h]
chroma_cb=cb[::v,::h]
"""
#nova[0]=y

#nova=np.array(imgYCbCr[::2,::2,0] + chroma_cr+chroma_cb)
#nova=np.zeros(imgYCbCr[:,:,0] + imgYCbCr[:,:,1]+imgYCbCr[:,:,2],dtype=uint8 )
"""
cv2.imshow("original", imgYCbCr)
cv2.imshow("chroma", nova)
"""






