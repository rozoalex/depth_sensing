from webcam import Webcam
import cv2
from threading import Thread
class DualWebcam (Webcam):
    def __init__(self, name='Dual Webcam', camera1=0, camera2=1, x_resolution=720, y_resolution=480, timeout=10):
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
            while(True):
                # Capture frame-by-frame
                ret1, frame1 = self.cam_left.capture.read()
                ret2, frame2 = self.cam_right.capture.read()

                # Our operations on the frame come here
                #self.output_img =  cv2.cvtColor(frame, self.color)
                if(isDepth):
                    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
                    disparity = stereo.compute(frame1,frame2)
                    print disparity
                cv2.imshow(self.cam_left.name,frame1)
                cv2.imshow(self.cam_right.name,frame2)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
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
