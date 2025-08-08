import cv2 as cv
import numpy as np
#generates image of size 500*500 pixels of 3 chanels unit8 means each pixle is unsigned 8bit integer from 0 to 255
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)


# blank[:]=0,255,0
# cv.imshow('green',blank)


#rows from 200 to 300 and columns from 200 to 300 values are bgr(0,255,0)
# blank[200:300,200:300]=0,255,0
# cv.imshow('green',blank)


#command to draw a rectangel on blank with starting and ending point  with color and thickness specified
# cv.rectangle(blank,(0,0),(400,400),(0,255,0),thickness=2)
# cv.imshow('rec',blank)


#fills with color
# cv.rectangle(blank,(0,0),(400,400),(0,255,0),thickness=-1)
# cv.imshow('rec',blank)

# cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,255,0),thickness=-1)
# cv.imshow('rec',blank)

#draw a cirlce
# cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),30,(255,0,0),thickness=3)
# cv.imshow('cirlce',blank)

#draw a line
cv.line(blank,(0,0),(250,250),(240,4,5),thickness=2)
cv.imshow('line',blank)
cv.waitKey(0)