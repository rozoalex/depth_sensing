#!/usr/bin/python
import cv2

# To capture a video, you need to create a VideoCapture object. 
# Its argument can be either the device index or the name of a video file. 
# Device index is just the number to specify which camera.
# Normally one camera will be connected (as in my case). 
# So I simply pass 0 (or -1). 
# You can select the second camera by passing 1 and so on. 
# After that, you can capture frame-by-frame. 
# But at the end, dont forget to release the capture.
# (from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html)

class webcam:
    def __init__(self, camera_number, x_resolution, y_resolution):
        self.capture = cv2.VideoCapture(camera_number)
        self.capture.set(3,x_resolution) # set horizontal resolution to 320
        self.capture.set(4,y_resolution) # set vertical resolution to 240 
        self.output_img = 



print('start capturing')
capture = cv2.VideoCapture(1)

counter = 10 # try 10 times at most
while((not capture.isOpened()) and counter>0):
    capture.open()
if(counter<=0):
    print('Failed to start cameras, abort process.')
else: 
    print('Capture started.')
    while(True):
        # Capture frame-by-frame
        ret, frame = capture.read()

        # Our operations on the frame come here
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'): #display the img for 1ms
            break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()