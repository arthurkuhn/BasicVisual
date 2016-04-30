import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cvController

class MotionModule(object):

    def __init__(self,cap):
        #cvController.CVController.__init__(self)
        self.cap = cap
        self.isMotion = False
        self.numObjects = 0

        self.toPrint = True
        self.currentFrame = None
        self.firstFrame = None

    def run(self,image):

        results = []
        frame = image

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.firstFrame is None:
    		self.firstFrame = gray
    		return (True,[])

        frameDelta = cv2.absdiff(self.firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

        thresh = cv2.dilate(thresh, None, iterations=2)
        (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            z = None
            if cv2.contourArea(c) >= 500:
        		z = cv2.boundingRect(c)
            if(z is not None):
                results.append((z[0],z[1],z[2],z[3]))

        self.currentFrame = frame

        return (True, results)
