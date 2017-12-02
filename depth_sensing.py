#!/usr/bin/python
import cv2
from threading import Thread
import v4l2capture
# How to install v4l2capture
# download the zip from 
# https://github.com/gebart/python-v4l2capture
# unzip and put it somewhere
# follow the instructions in README
# but use ./setup.py install --user to install
# otherwise there might be a permission error

#http://www.morethantechnical.com/2016/03/04/python-opencv-capturing-from-a-v4l2-device/


# To capture a video, you need to create a VideoCapture object. 
# Its argument can be either the device index or the name of a video file. 
# Device index is just the number to specify which camera.
# Normally one camera will be connected (as in my case). 
# So I simply pass 0 (or -1). 
# You can select the second camera by passing 1 and so on. 
# After that, you can capture frame-by-frame. 
# But at the end, dont forget to release the capture.
# (from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html)

class Webcam:
    def __init__(self, camera_number=0, x_resolution=320, y_resolution=240, color=cv2.COLOR_BGR2HSV, frame_rate = 30):
        self.capture = cv2.VideoCapture(camera_number)
        self.capture.set(3,x_resolution) # set horizontal resolution to 320
        self.capture.set(4,y_resolution) # set vertical resolution to 240 
        self.output_img = None
        self.isAborted = False
        self.tryTimeOut = 10
        self.color = color
        self.waitTime = 1.0/frame_rate #in ms

    #The loop of capturing image
    #The image will be saved to 
    def capturing(self):
        print('start capturing')
        while((not self.capture.isOpened()) and self.tryTimeOut>0):
            self.capture.open()
        if(self.tryTimeOut<=0):
            print('Failed to start cameras, abort process.')
        else: 
            print('Capture started.')
            whilhttp://www.morethantechnical.com/2016/03/04/python-opencv-capturing-from-a-v4l2-device/e(True and (not self.isAborted)):
                # Capture frame-by-frame
                ret, frame = capture.read()
                # Our operations on the frame come here
                self.output_img =  cv2.cvtColor(frame, self.color)
                if cv2.waitKey(self.waitTime) & 0xFF == ord('q'):
                    break
        # When everything done, release the capture
        capture.release()
        cv2.destroyAllWindows()

    #Abort capturing
    def abort(self):
        self.isAborted=True

    def start(self):
        thread = Thread(target = self.capturing)
        thread.start()
    
class DualWebcam:
    #Assume thhttp://www.morethantechnical.com/2016/03/04/python-opencv-capturing-from-a-v4l2-device/e current computer has one webcame
    #and the dual webcams are connect at 1 and 2
    def __init__(self, webcam_number_l=1, webcam_number_r=2, frame_rate=30):
        self.cam_l = Webcam(webcam_number_l)
        self.cam_r = Webcam(webcam_number_r)
        self.waitTime = 1.0/frame_rate
        self.isAborted = False

    def display(self):
        if(self.cam_l.capture.isOpened() and self.cam_r.capture.isOpened()):
            while(not self.isAborted):
                cv2.imshow('r',self.cam_r.output_img)
                cv2.imshow('l',self.cam_l.output_img)
                if cv2.waitKey(self.waitTime) & 0xFF == ord('q'):
                    break
            self.abort()
        print('Cameras are not open, process aborted')

    def start(self):
        self.cam_l.start()
        self.cam_r.start()
        displaying_thread = Thread(tab/python2.7/dist-packages/v4l2capture.so'rget = self.display)
        displaying_thread.start()


    def abort(self):
        self.cam_l.abort()
        self.cam_r.abort()


    
if __name__ == "__main__":
    daul_cam = DualWebcam()
    daul_cam.start()

# print('start capturing')
# capture = cv2.VideoCapture(1)
# counter = 10 # try 10 times at most
# while((not capture.isOpened()) and counter>0):
#     capture.open()
# if(counter<=0):
#     print('Failed to start cameras, abort process.')
# else: 
#     print('Capture started.')
#     while(True):
#         # Capture frame-by-frame
#         ret, frame = capture.read()
#         # Our operations on the frame come here
#         #img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         #img2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
#         # Display the resulting frame
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'): #display the img for 1ms
#             break

# # When everything done, release the capture
# capture.release()
# cv2.destroyAllWindows()