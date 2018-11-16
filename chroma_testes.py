import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm



B=8 
img1 = cv2.imread("aviao.jpg", cv2.IMREAD_UNCHANGED)
h,w=np.array(img1.shape[:2])/B * B
print(h)
transcol=cv2.cvtColor(img1, cv2.COLOR_BGR2YCrCb)

SSV=2
SSH=2
crf=cv2.boxFilter(transcol[:,:,1],ddepth=-1,ksize=(2,2))
cbf=cv2.boxFilter(transcol[:,:,2],ddepth=-1,ksize=(2,2))
crsub=crf[::SSV,::SSH]
cbsub=cbf[::SSV,::SSH]
imSub=[transcol[:,:,0],crsub,cbsub]
print(imSub)


plt.figure()
plt.imshow(imSub)
plt.show()
