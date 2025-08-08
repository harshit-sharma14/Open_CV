#Contours are like edges but not edges, they are used in obj detection
import cv2 as cv
import numpy as np
'''
Summary 
first import a pic, then convert to grayscale for further processing
apply canny edge detection to find the edges of the image
now use findContours to get contotus and then display them on blank screen using drawContours and passing the array 
pic import-> grayscale-> canny-> contours -> draw or visualize
or 
pic import -> blur-> grayscale->thresholding->contouts->viuslaize

'''
pic=cv.imread('pic.png')
blank=np.zeros(pic.shape[:3],dtype='uint8')
cv.imshow('blank',blank)
gray=cv.cvtColor(pic,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
blur=cv.GaussianBlur(pic,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
canny=cv.Canny(blur,125,175)
cv.imshow('canny',canny)
#it gives two things a list of numpy array contours (x,y) and their heirarchies
#also diff b/w canny and contours is that canny wherever detects intensity change mark it using white pixel but contour connects them use for obj detection and checks for heirarchies

#The mode argument specifies the contour retrieval mode, which determines how the contours are organized, particularly with respect to their hierarchy (e.g., nested contours like a circle inside a square).
#cv.RETR_LIST retrieves all contours without establishing any hierarchical relationships.
#cv.RETR_EXTERNAL: Retrieves only the outermost contours, ignoring any contours inside other contours.
#cv.RETR_TREE: Builds a full hierarchical tree of contours, capturing all nesting levels (e.g., a shape inside a shape inside another shape).

#method is the contour approximation method which determines how contours are stored
#chain_approx_none stores all the points without any approximation for ex- in a line it will store all the pixel
#chain_approx_simple stores only endpoint
res,thres=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thres',thres)
contours,heirarchies=cv.findContours(thres,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
#arguments img,array of contours, number of list to display if all then -1,color,thickness
drawcontour=cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('Contour display',drawcontour)
cv.waitKey(0)