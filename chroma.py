import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("jogador.jpg")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#converte em YCrCb
imgYCbCr=cv2.cvtColor( img, cv2.COLOR_BGR2YCR_CB)

B=8
hh,w=np.array(imgYCbCr.shape[:2])/B * B
#valor a dividir a crominância
v=2
h=2

cr= imgYCbCr[:,:,1]
cb= imgYCbCr[:,:,2]

cr_chroma=cr[::v,::h]
cb_chroma=cb[::v,::h]

#Função nrepeat( imagem, vezes, eixo )

"""
#Reproduzindo imagem com crominancia cr e cb valor igual a 2
m=2
img_aumentada_cr = np.repeat( cr_chroma, m, axis=0)
img_aumentada_cr = np.repeat(img_aumentada_cr, m, axis=1)

img_aumentada_cb = np.repeat( cb_chroma, m, axis=0)
img_aumentada_cb = np.repeat( img_aumentada_cb, m, axis=1)

pyplot python
imagemFinal = np.zeros( (img_aumentada_cr.shape[0],img_aumentada_cr.shape[1],3), np.uint8)
imagemFinal[:,:,0]= imgYCbCr[:,:,0]
imagemFinal[:,:,1]= img_aumentada_cr
imagemFinal[:,:,2]= img_aumentada_cb

imagem_final_rgb = cv2.cvtColor( imagemFinal, cv2.COLOR_YCrCb2RGB)
"""

plt.subplot(121)
plt.imshow(imgYCbCr[:,:,1])

plt.title("Imagem Crominancia Cr Original")

plt.subplot(122)
plt.imshow(cr_chroma)
plt.title("Imagem com Chroma Subsampling 4:2:2 canal Cr")


plt.show()







