import cv2 as cv

image1=cv.imread('pic4.jpg')
image=cv.resize(image1,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('image',image)
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#Loads a pre-trained Haar Cascade model for face detection from the XML file haar_face.xml.


haar_cascade=cv.CascadeClassifier('haar_face.xml')
#detects faces, takes input image, 
'''
What scaleFactor=1.1 means
1.1 means reduce the image size by 10% at each step in this pyramid.

First pass: Original size (100%)

Next pass: 90% of original size

Then: 81% (90% of 90%), and so on.

Lower the value higher the accuracy


When Haar Cascade scans the image at different scales and positions, it may detect the same object multiple times in slightly different positions.
Each detection appears as a rectangle (bounding box).

The minNeighbors parameter tells OpenCV:

“Only keep a detection if at least this many rectangles (neighbors) overlap it.”
'''
faces_r=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)
print(len(faces_r))
for (x,y,w,h) in faces_r:
    cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow('faces_box',image)
cv.waitKey(0)
'''
detectMultisclae is a method that detects multiple objects in image
Multi-Scale Detection: Faces can appear at different sizes in an image (e.g., close-up vs. far away). To handle this, the algorithm creates a "pyramid" of scaled versions of the image (scaling it down repeatedly) and scans each scale for faces. It slides a detection window (starting at a base size defined in the cascade) over the image, checking for matches at every position and scale.

scaleFactor=1.1: This controls how much the image is scaled down at each level of the pyramid. A value of 1.1 means the image is reduced by 10% each time (e.g., from 100% to 90.9%, then 82.6%, etc.). Smaller values (closer to 1) detect more scales but are slower and may find more false positives. Larger values speed it up but might miss smaller or larger faces. 1.1 is a common balance for accuracy and speed.

minNeighbors=3: This reduces false positives by requiring that a detected face region must have at least 3 neighboring detections (overlapping rectangles from nearby scales/positions) to be considered valid. It groups nearby detections into one (non-maximum suppression). Higher values make detection stricter (fewer false positives but might miss some faces); lower values are more lenient.

Output: faces_r is a NumPy array of detected rectangles. Each row is a tuple (x, y, w, h):

x, y: Top-left corner coordinates of the bounding box.
w, h: Width and height of the box.
'''