#!/usr/bin/python
import cv2
print('start capturing')
capture = cv2.VideoCapture(1)
capture0 = cv2.VideoCapture(0)
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
        ret0, frame0 = capture0.read()
        # Our operations on the frame come here
        #img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #img2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
        # Display the resulting frame
        cv2.imshow('frame',frame)
        cv2.imshow('frame0',frame0)
        if cv2.waitKey(1) & 0xFF == ord('q'): #display the img for 1ms
            break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows() 