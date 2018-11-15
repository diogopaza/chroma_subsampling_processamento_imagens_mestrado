import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm



B=8 
img1 = cv2.imread("jogador.jpg", cv2.IMREAD_UNCHANGED)
h,w=np.array(img1.shape[:2])/B * B




transcol=cv2.cvtColor(img1, cv2.COLOR_BGR2YCrCb)

SSV=2
SSH=2
crf=transcol[:,:,1]
cbf=transcol[:,:,2]
y=transcol[:,:,0]
crsub=crf[::SSV,::SSH]
cbsub=cbf[::SSV,::SSH]
ysub=y[::SSV,::SSH]

imagem=np.zeros((313,313,3), np.uint8)
imagem[:,:,0]=ysub
imagem[:,:,1]=crsub
imagem[:,:,2]=cbsub
cv2.imshow("Crhoma", imagem)

