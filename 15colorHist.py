import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image1=cv.imread('pic4.jpg')
image=cv.resize(image1,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Image',image)
blank=np.zeros(image.shape[:2],dtype='uint8')
circle=cv.circle(blank,(image.shape[1]//2,image.shape[0]//2),(200),255,-1)
cv.imshow('circle',circle)
masked=cv.bitwise_and(image,image,mask=circle)
cv.imshow('mask',masked)

plt.figure()
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.title('Histogram')
#COlor histogram
colors=('b','g','r') #color codes for plotting
for i,col in enumerate(colors): #for i, col in enumerate(colors): Loops over the channels (i=0 for Blue, i=1 for Green, i=2 for Red) and corresponding plot colors.
    hist=cv.calcHist([image],[i],circle,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)