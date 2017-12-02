#!/usr/bin/python
#Example from https://docs.opencv.org/3.1.0/dd/d53/tutorial_py_depthmap.html

import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('tsukuba_l.png',0)
imgR = cv2.imread('tsukuba_r.png',0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
print disparity
cv2.imshow('f',disparity)
plt.imshow(disparity,'gray')
plt.show()