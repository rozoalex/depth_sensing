import cv2
from threading import Thread
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
    def __init__(self, name, camera_number=0, x_resolution=720, y_resolution=480, color=cv2.COLOR_BGR2HSV, frame_rate = 30):
        self.capture = cv2.VideoCapture(camera_number)
        self.capture.set(3,x_resolution) # set horizontal resolution to 320
        self.capture.set(4,y_resolution) # set vertical resolution to 240 
        #self.output_img = None
        self.isAborted = False
        self.tryTimeOut = 10
        self.color = color
        self.waitTime = int(1000/frame_rate) #in ms
        self.name = name

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
            while(not self.isAborted):
                # Capture frame-by-frame
                ret, frame = self.capture.read()
                # Our operations on the frame come here
                #self.output_img =  cv2.cvtColor(frame, self.color)
                cv2.imshow(self.name,frame)
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