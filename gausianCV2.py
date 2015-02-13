import cv2
import numpy as np
import math

img=cv2.imread("sheldon.jpg")
(h,w)=img.shape[:2]
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # change to gray scale image
# gausian filtering

blur=cv2.GaussianBlur(img,(5,5),0)

# using sobel to get gradent
sobelx=cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=5)
# making matriks kosong for hasilt
#sobel=np.zeros(img.shape,dtype="uint8")
#for i in range(h):
#	for j in range(w):
#		sobel[i,j]=cv2.sqrt(sobelx[i,j]*sobelx[i,j]+sobely[i,j]+sobely[i,j])


sobelcv=cv2.Sobel(blur,cv2.CV_64F,1,1,ksize=5)
#cv2.imshow("result self sobel",sobel)
cv2.imshow("result cv",sobelcv)
cv2.waitKey(0)

