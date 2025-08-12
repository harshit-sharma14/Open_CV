import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#image import 
image1=cv.imread('pic4.jpg')
image=cv.resize(image1,(800,500),interpolation=cv.INTER_CUBIC)
blank=np.zeros(image.shape[:2],dtype='uint8')
cv.imshow('image',image)


gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


circle=cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),200,255,-1)
cv.imshow('circle',circle)

masked=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('mask',masked)

#arguments- list of images can be passed, number of chanles for grayscale it is 0, mask if you want to calculaye for a certain region, number og bins it will have, range [1:x] x excluded
gray_hist=cv.calcHist([gray],[0],masked,[256],[0,256])
plt.figure()
plt.title('Histogram')
plt.xlabel('Bins')
plt.ylabel('number of pixles')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)
