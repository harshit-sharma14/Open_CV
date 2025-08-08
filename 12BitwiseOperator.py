import cv2 as cv
import numpy as np
blank=np.zeros((400,400),dtype='uint8')
rec=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cir=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('recetangle',rec)
cv.imshow('circle',cir)
#BITWISE AND
bitwise_and=cv.bitwise_and(rec,cir)
cv.imshow('bitwise_and',bitwise_and)
#Bitwise or
bitwise_or=cv.bitwise_or(rec,cir)
cv.imshow('bitwise_or',bitwise_or)
#Bitwise XOR
bitwise_xor=cv.bitwise_xor(rec,cir)
cv.imshow('bitwise_xor',bitwise_xor)
#bitwise not
bitwise_not=cv.bitwise_not(rec)
cv.imshow('not',bitwise_not)
cv.waitKey(0)