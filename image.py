import cv2 as cv
import numpy as np
image1=cv.imread('pic4.jpg')
image=cv.resize(image1,(800,500),interpolation=cv.INTER_CUBIC)

cv.waitKey(0)