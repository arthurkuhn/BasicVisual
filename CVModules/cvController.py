import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cvBodyModule
import cvFaceModule
import cvMotionModule

class CVController(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

if __name__ == '__main__':

    y = CVController()
    x = cvMotionModule.MotionModule(y.cap)
    x.start()
    self.cap.release()
    cv2.destroyAllWindows()
