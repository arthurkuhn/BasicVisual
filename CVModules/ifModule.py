import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cvBodyModule
import cvFaceModule
import cvMotionModule

class IFModule(object):
    def __init__(self, cvMod,cond,expr):
        self.cvModule = cvMod
        self.condition = cond
        self.expression = expr

    def testCondition(self,frame):
        result, drawList = self.cvModule.run(frame)
        return (result,drawList)
