import cv2 as cv
capture=cv.VideoCapture('video.mp4')
while True:
    # takes two things istrue denotes every frame is captured ok, and frame is each frame
    isTrue, frame=capture.read()
    cv.imshow('video of a plant',frame)
    #it denotes that when d is pressed exit
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
