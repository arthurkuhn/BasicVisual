import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cvController

class MotionModule(object):

    def __init__(self):
        self.isMotion = False
        self.toPrint = True
        self.currentFrame = None
        self.firstFrame = None

    def run(self,image,condition):

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

        if(len(results) > 0):
            self.isMotion = True
        else:
            self.isMotion = False

        self.currentFrame = frame

        return (self.testCondition(condition), results)

    def testCondition(self,condition):
        variable = condition["var"]
        comparison = condition["comp"]
        equality = condition["eq"]

        result = False
        if (variable == "ThereIsMotion"):
            eqFlag = False
            if(equality == "True"):
                eqFlag = True

            if comparison == "=":
                if(self.isMotion == eqFlag):
                    result = True
            elif comparison == "!=":
                if(self.isMotion != eqFlag):
                    result = True
        return result
