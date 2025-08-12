import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image1=cv.imread('pic4.jpg')
image=cv.resize(image1,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Image',image)

gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
blank=np.zeros(image.shape[:2],dtype='uint8')
circle=cv.circle(blank,(image.shape[1]//2,image.shape[0]//2),(200),(255,0,0),-1)
cv.imshow('circle',circle)
mask=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('mask',mask)
gray_hist=cv.calcHist([image],[0],mask,[256],[0,256])
plt.figure()
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.xlim([0,256])
plt.title('Histogram')
plt.plot(gray_hist)
plt.show()
cv.waitKey(0)