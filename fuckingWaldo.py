import numpy as np
import argparse
#import imutils
import cv2

# costruct the argument parser and parse the argument
ap = argparse.ArgumentParser();
ap.add_argument("-p","--puzzle",required=True,
		help="Path to the puzzle iamge")
ap.add_argument("-w","--waldo",required=True,
		help="path to the waldo's image")
args=vars(ap.parse_args())

#load the puzzle and waldo images
puzzle=cv2.imread(args["puzzle"])
waldo=cv2.imread(args["waldo"])
(waldoHeight,waldoWidth)=waldo.shape[:2]

result=cv2.matchTemplate(puzzle,waldo,cv2.TM_CCOEFF)
(_,_,minLoc,maxLoc)=cv2.minMaxLoc(result)
topLeft=maxLoc
botRight=(topLeft[0]+waldoWidth,topLeft[1]+waldoHeight)
roi=puzzle[topLeft[1]:botRight[1],topLeft[0]:botRight[0]]

mask=np.zeros(puzzle.shape,dtype="uint8")
puzzle=cv2.addWeighted(puzzle,0.25,mask,0.75,0)
#brighter than the rest of image
puzzle[topLeft[1]:botRight[1],topLeft[0]:botRight[0]]=roi

# display the images


