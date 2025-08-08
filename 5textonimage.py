import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
#cv.putText(image, text, org, font, fontScale, color, thickness)

cv.putText(blank,'Harshit',(255,255),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),2)
cv.imshow('text',blank)
cv.waitKey(0)