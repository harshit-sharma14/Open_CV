import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#Thresholding is the binariziation of image if a pixel value is less than a particular value is is 0, else 1

image1=cv.imread('pic4.jpg')
image=cv.resize(image1,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Image',image)
#simple thresholding
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
#arguments image, threshold value, if val>=150 then set to 255,method
thresholding,thres=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Binary Simple',thres)

thresholding,thres_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Binary Simple Inverse',thres_inv)
#Advaptive Thresholding
adaptive=cv.adaptiveThreshold(gray,255,cv.Adap)
cv.waitKey(0)