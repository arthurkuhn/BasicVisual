import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cvFaceModule

class CVController(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def test(self):
        print 'Im in parent class'

if __name__ == '__main__':
    x = cvFaceModule.FaceModule()
    x.start()
    self.cap.release()
    cv2.destroyAllWindows()
