import cv2
import Image


#image=cv2.imread("sheldon.jpg")
#print image[0]
img=Image.open("sheldon.jpg")
# gausian mask for convultion of image
gausian_mask=[[2,4,5,4,2],[4,9,12,9,4],[5,12,15,12,5],[4,9,12,9,4],[2,4,5,4,2]]
gausian_konst=float(1)/115
width,height=img.size
for i in range(width):
	for j in range(height):
		

