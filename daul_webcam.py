from webcam import Webcam
import cv2
from threading import Thread
from matplotlib import pyplot as plt
import numpy as np
class DualWebcam (Webcam):
    def __init__(self, name='Dual Webcam', camera1=1, camera2=3, x_resolution=720, y_resolution=480, timeout=10):
        self.name = name
        self.cam_left = Webcam('cam1',camera1, x_resolution, y_resolution)
        self.cam_right = Webcam('cam2',camera2, x_resolution, y_resolution)
        self.tryTimeOut = 10


    def capturing(self, isDepth):
        print('start capturing')
        while((not self.cam_left.capture.isOpened()) and (not self.cam_right.capture.isOpened()) and self.tryTimeOut>0):
            self.cam_left.capture.open()
            self.cam_right.capture.open()
        if(self.tryTimeOut<=0):
            print('Failed to start cameras, abort process.')
        else: 
            print('Capture started.')
            window_size = 2
            min_disp = 64
            num_disp = 112-min_disp
            # stereo = cv2.StereoSGBM_create(
            #     minDisparity = min_disp,
            #     numDisparities = num_disp,
            #     blockSize = 30,
            #     uniquenessRatio = 10,
            #     speckleWindowSize = 100,
            #     speckleRange = 32,
            #     disp12MaxDiff = 1,
            #     P1 = 8*3*window_size**2,
            #     P2 = 32*3*window_size**2,
            #     )
            stereo = cv2.StereoSGBM_create(numDisparities=112-min_disp, minDisparity=min_disp, blockSize=2)
            #stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
            while(True):
                # Capture frame-by-frame
                ret1, frame1 = self.cam_left.capture.read()
                ret2, frame2 = self.cam_right.capture.read()
                frame1_new=cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
                frame2_new=cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
                # Our operations on the frame come here
                #self.output_img =  cv2.cvtColor(frame, self.color)
                
                if(isDepth):
                    disparity = stereo.compute(frame1_new,frame2_new).astype(np.float32) / 16.0
                    disparity = (disparity-min_disp)/num_disp
                    #cv2.imshow('deep',disparity)
                    cv2.imshow(self.cam_left.name,frame1_new)
                    cv2.imshow(self.cam_right.name,frame2_new)
                    cv2.imshow('disparity', disparity)
                    k = cv2.waitKey(30) & 0xff
                    if k == 27:
                        break

                #cv2.imshow(self.cam_left.name,frame1)
                #cv2.imshow(self.cam_right.name,frame2)
                #if cv2.waitKey(1) & 0xFF == ord('q'):
                #    break
        # When everything done, release the capture
        self.cam_left.capture.release()
        self.cam_right.capture.release()
        cv2.destroyAllWindows()

    def start(self):
        thread = Thread(target = self.capturing, args=(False,))
        thread.start()

    def startDepthVision(self):
        thread = Thread(target = self.capturing, args=(True,))
        thread.start()
