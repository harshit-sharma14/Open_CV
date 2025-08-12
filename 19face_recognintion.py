import numpy as np
import cv2 as cv 
haar_cascade=cv.CascadeClassifier('haar_face.xml')

features=np.load('features.npy')
labels=np.load('labels.npy')
