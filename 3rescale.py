#reading images and video
import cv2 as cv
capture=cv.VideoCapture('video.mp4')
def changeRes(width,height):
    #works only for live video
    capture.set(3,width)
    capture.set(4,height)

def rescale(frame, scale=0.75):
    #works for live, video and image
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
while True:
    # takes two things istrue denotes every frame is captured ok, and frame is each frame
    isTrue, frame=capture.read()
    cv.imshow('video of a plant',frame)
    frame_resized=rescale(frame)
    cv.imshow('resized',frame_resized)
    #it denotes that when d is pressed exit
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()