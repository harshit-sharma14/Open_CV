#maksing allows us to focus on sepcific parts of an image, like if we want to focus only on the face of the people, it will do so
#A mask is typically a grayscale image where non-zero pixels (e.g., 255) indicate regions of interest, and zero pixels indicate areas to ignore
import cv2 as cv
import numpy as np
image1=cv.imread('pic4.jpg')
image=cv.resize(image1,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('image',image)
blank=np.zeros(image.shape[:2],dtype='uint8')
cv.imshow('blank',blank)
c=cv.circle(blank,(image.shape[1]//2+85,image.shape[0]//2),400,255,-1)
s=cv.rectangle(blank,(int(0.2*image.shape[1]),int(0.2*image.shape[0])),(int(0.8*image.shape[1]),int(0.8*image.shape[0])),255,-1)
mask=cv.bitwise_or(c,s)
cv.imshow('mask',mask)
masked=cv.bitwise_and(image,image,mask=mask)
cv.imshow('Masked Image',masked)
cv.waitKey(0)