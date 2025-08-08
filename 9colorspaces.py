import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('pic.png')
cv.imshow('pic',img)
#BGR to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV) 
cv.imshow('HSV',hsv)
#BGR to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('Lab',lab)
#opencv shows BGR image it viewed on another module it will show inverted image
#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RBG',rgb)
plt.imshow(img)
plt.show()
cv.waitKey(0)
