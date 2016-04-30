import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cvBodyModule
import cvFaceModule
import cvMotionModule
import cvTakePicture

class IFModule(object):
    def __init__(self, cvMod,cond,expr):
        self.cvModule = cvMod
        self.condition = cond
        self.expressions = expr

    def testCondition(self,frame):
        result, drawList = self.cvModule.run(frame,self.condition)
        return (result,drawList)

    def executeExpressions(self,frame):
        picture = ""
        for exp in self.expressions:
            result = exp.execute(frame,picture)
            if(result == ""):
                break
            if(exp.name == "Picture"):
                picture = result
