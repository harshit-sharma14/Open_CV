import cv2 as cv
im=cv.imread('pic.png')
#1. GrayScale
gray=cv.cvtColor(im,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#2. blur
blur=cv.GaussianBlur(im,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
#Edge cascade 125 and 175 are pixel threshold you can pass blur instead of im to detect less edges
canny=cv.Canny(im,125,175)
cv.imshow('edge',canny)
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilate',dilated)
eroded=cv.erode(canny,(7,7),iterations=3)
cv.imshow('erode',eroded)

#resize
resize=cv.resize(im,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resize)

#cropping
cropped=im[200:300,300:450]
cv.imshow('cropped',cropped)
cv.waitKey(0)