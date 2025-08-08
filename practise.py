#Contour Detection
import cv2 as cv
import numpy as np
image1=cv.imread('pic3.jpg')
image=cv.resize(image1,(800,500),interpolation=cv.INTER_CUBIC)
blank=np.zeros(image.shape[:2],dtype='uint8')

cv.imshow('image',image)
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
blur=cv.GaussianBlur(image,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
#canny
canny=cv.Canny(blur,125,175)
cv.imshow('canny',canny)
#contour
res,thres=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('thres',thres)
contours,heirarchies=cv.findContours(thres,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))
d=cv.drawContours(blank,contours,-1,(255,0,0),1)
cv.imshow('draw',d)
cv.waitKey(0)