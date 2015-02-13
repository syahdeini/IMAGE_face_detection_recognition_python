import cv2

image=cv2.imread("/home/syahdeini/LABO/IMAGE/monalisa.jpg")
cv2.imshow("original",image)
cv2.waitKey(0) # wait until someone press the key then exit, parameter 0 
# means that we can press any key

# we need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- threfore, we calculate
# the ratio of the new image to the old image
r= 100.0/image.shape[1] # Y
dim=(100,int(image.shape[0]*r))

# perform the actual resizing of theimage
resized=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("resized",resized)
cv2.waitKey(0)
