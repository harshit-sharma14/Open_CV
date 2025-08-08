import numpy as np
import cv2 as cv
image=cv.imread('pic.png')
def translate(image,x,y):
    mat=np.float32([[1,0,x],[0,1,y]])
    dimension=(image.shape[1],image.shape[0])
    return cv.warpAffine(image,mat,dimension)
new_i=translate(image,-200,34)
def rotate(image,angle,rotatePoint=None):
    (height,width)=image.shape[:2]
    if(rotatePoint==None):
        rotatePoint=(width//2,height//2)
        #arguments point, angle and scale
    rotMat=cv.getRotationMatrix2D(rotatePoint,angle,1.0)
    dimension=(width,height)
    return cv.warpAffine(image,rotMat,dimension)
cv.imshow('translate',new_i)
rotate=rotate(image,50)
cv.imshow('rotate',rotate)
resized=cv.resize(image,(500,500),interpolation=cv.INTER_LINEAR)
cv.imshow('resize',resized)
#flip 0-vertical 1- horizontal -1-both
flip=cv.flip(image,-1)
cv.imshow('flip',flip)
#cropping
crop=image[200:300,200:400]
cv.imshow('crop',crop)
cv.waitKey(0)