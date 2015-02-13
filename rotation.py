import cv2

image=cv2.imread("/home/syahdeini/LABO/IMAGE/monalisa.jpg")
#cv2.imshow("original",image)
#cv2.waitKey(0) # wait until someone press the key then exit, parameter 0 
# means that we can press any key

# we need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- threfore, we calculate
# the ratio of the new image to the old image
(h,w)=image.shape[:2]
center=(w/2,h/2)

# rotate the image by 180 degrees
M=cv2.getRotationMatrix2D(center,180,0.5) #compute the matrix that cna be used to rotating (and scaling), the second argument is the rotation degree and the third argument is the scalling
rotated=cv2.warpAffine(image,M,(w,h))#perform the actual rotation, second argument is rotation matrix, and the output dimension
cv2.imshow("rotated",rotated)
cv2.waitKey(0)
