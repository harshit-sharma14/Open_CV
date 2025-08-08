import cv2 as cv
import numpy as np
pic=cv.imread('pic.png')
cv.imshow('pic',pic)
def translate(image,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimension=(image.shape[1],image.shape[0])
    return cv.warpAffine(image,transMat,dimension)
tr=translate(pic,200,300)
cv.imshow('Trasnlated',tr)
def rotate(image,angle,axisP=None):
    (height,width)=image.shape[:2]
    if(axisP==None):
        axisP=(width//2,height//2)
    rotationMat=cv.getRotationMatrix2D(axisP,angle,1.0)
    dimension=(width,height)
    return cv.warpAffine(image,rotationMat,dimension)
r=rotate(pic,30)
cv.imshow('rotated',r)
resized=cv.resize(pic,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)
cv.waitKey(0)