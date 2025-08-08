import cv2 as cv
import numpy as np

img1=cv.imread('pic3.jpg')
img=cv.resize(img1,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('pic',img)
b,g,r=cv.split(img)
#reprented as grayscale regions where are low pixel conceentration are dark and where is more is lightz
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merge=cv.merge([b,g,r])
cv.imshow('Merged',merge)

#TO see actual color
blank=np.zeros(img.shape[:2],dtype='uint8')
blue=cv.merge([b,blank,blank]) # it is like merging merge(b,0,0) bgr
cv.imshow('blue',blue)

green=cv.merge([blank,g,blank]) # it is like merging merge(b,0,0) bgr
cv.imshow('green',green)

red=cv.merge([blank,blank,r]) # it is like merging merge(b,0,0) bgr
cv.imshow('red',red)
cv.waitKey(0)