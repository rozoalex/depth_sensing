#!/usr/bin/python
from daul_webcam import DualWebcam
if __name__ == "__main__":
    cam = DualWebcam(x_resolution=480,y_resolution=320)
    cam.startDepthVision()