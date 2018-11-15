import cv2
import numpy as np

img = cv2.imread( 'casa.jpg' )
imgY = cv2.cvtColor( img, cv2.COLOR_BGR2YCrCb)


imgRemontada=np.zeros(imgY.shape,np.uint8)
imgRemontada[:,:,0]=imgY[:,:,0]
imgRemontada[:,:,1]= imgY[:,:,1]
imgRemontada[:,:,2]=imgY[:,:,2]

tamanhoCbCr = zeros( )
print( img.shape[0],img.shape[1])
print( img.dtype)
#tamanho_img_final = 
#imgFinal=  = np.zeros( (), )


#cv2.imshow( 'Original', img )
#cv2.imshow( 'Ycbcr', imgY )
#cv2.imshow( 'RemontadaYcbcr', imgRemontada )
