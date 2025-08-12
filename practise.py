import cv2 as cv
import numpy as np
image1=cv.imread('pic4.jpg')
image=cv.resize(image1,(800,500),interpolation=cv.INTER_CUBIC)
blank=np.zeros((image.shape[:3]),dtype='uint8')

cv.imshow('original image',image)
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
canny=cv.Canny(blur,125,175)
cv.imshow('canny',canny)
contours,heirarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# cv.imshow('contour',)
d=cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('Draw',d)
cv.waitKey(0)