#!/usr/bin/python
from daul_webcam import DualWebcam
if __name__ == "__main__":
    cam = DualWebcam(x_resolution=480,y_resolution=320)
    #VERY IMPORTANT NOTE 
    #USE v4l2-ctl --list-devices to see what are all the devices first
    cam.startDepthVision()
    #cam.start()