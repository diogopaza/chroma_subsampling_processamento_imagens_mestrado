import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("aviao.jpg")

#converte em YCrCb
imgYCrCb=cv2.cvtColor( img, cv2.COLOR_BGR2YCR_CB)

"""
crf=cv2.boxFilter(img3[:,:,1],ddepth=-1,ksize=(2,2))
cbf=cv2.boxFilter(img3[:,:,2],ddepth=-1,ksize=(2,2))
"""

chroma_cr= imgYCrCb[:,:,1]
chroma_cb= imgYCrCb[:,:,2]





