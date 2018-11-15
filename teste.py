import cv2
import numpy as np

img = cv2.imread( 'jogador.jpg' )
imgY = cv2.cvtColor( img, cv2.COLOR_BGR2YCrCb)
imgY1 = imgY[::2,::2,1]
imgY2 =  imgY[::2,::2,2]

imgYampliada1 = np.repeat( imgY1, 2, axis=0 )
imgFinalAmpliada1 = np.repeat( imgYampliada1, 2, axis=1 )

imgYampliada2 = np.repeat( imgY2, 2, axis=0 )
imgFinalAmpliada2 = np.repeat( imgYampliada2, 2, axis=1 )

print( imgY1.shape )

imgRemontada=np.zeros(imgY.shape,np.uint8)
imgRemontada[:,:,0]=imgY[:,:,0]
imgRemontada[:,:,1]= imgY[:,:,1]
imgRemontada[:,:,2]=imgY[:,:,2]

img[:,:,1]= imgY1

#cv2.imshow('inYcbcr', imgY)


#cv2.imshow( 'normal1', imgY[:,:,1])
#cv2.imshow( 'normal2', imgY[:,:,2])

#cv2.imshow( 'reduzida1', imgY1)
#cv2.imshow( 'reduzida2', imgY2)
"""
cv2.imshow( 'ampliada1', imgFinalAmpliada1)
cv2.imshow( 'ampliada2', imgFinalAmpliada2)

cv2.imshow( 'Imagem Remontada', imgRemontada)


#cv2.imshow('remontada', img2)
#cv2.imshow('original', imgY)

#cv2.imshow( 'reconstruida', imgY2)
#cv2.imshow( 'inY', imgY)
#cv2.imshow( 'imagem YCC', imgFinalAmpliada )



imgReduzida = img[::2,::2]
imgAmpliada = np.repeat( imgReduzida, 2, axis=0 )
imgAmpliada = np.repeat( imgAmpliada, 2, axis=1 )
cv2.imwrite( '.jpg', imgAmpliada)

cv2.imshow('reduzida', imgReduzida )
cv2.imshow('in', img )
cv2.imshow('out', imgAmpliada )

cv2.imshow('in', img)
"""
