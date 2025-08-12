import cv2 as cv
import numpy as np
image1=cv.imread('pic3.jpg')
image=cv.resize(image1,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Image',image)
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#laplacian
#The Laplacian operator detects edges by finding areas of rapid intensity change in all directions.
#cv.cv_64F means it will be stored in 64 bit floating point number

lap=cv.Laplacian(gray,cv.CV_64F)
#now it can contain negative values as well so abosulte 
lap=np.uint8(np.absolute(lap))
cv.imshow('lapacian',lap)
#Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobel x',sobelx)
cv.imshow('Sobel y',sobely)
cv.imshow('Sobelx and y',combined_sobel)
canny=cv.Canny(gray,125,175)
cv.imshow('canny',canny)
cv.waitKey(0)