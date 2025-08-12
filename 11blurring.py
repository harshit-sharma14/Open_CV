import cv2 as cv
image1=cv.imread('pic3.jpg')
image=cv.resize(image1,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('image',image)
#high kernel size high blur
average=cv.blur(image,(7,7))
cv.imshow('average',average)
#guassian blur is more natural and is less blur 
guass=cv.GaussianBlur(image,(7,7),0) #third arhgument is deviation in x
#median it used to remove noise, 3 is the kernel size
median=cv.medianBlur(image,3)
cv.imshow('median',median)

cv.imshow('guass',guass)
#most advanced blurring Bilateral bluriing it retains the edges
#arguments first image, second is diameter how much area from each pixel is to be considered, 3rd sigmaColor means larger value means more pixel with different color will be mixed toegter, last is sigma space how far the pixels can affect a computation
bilateral=cv.bilateralFilter(image,5,35,25)
cv.imshow('bilateral',bilateral )
cv.waitKey(0)