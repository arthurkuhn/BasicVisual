import cv2
import imutils
import numpy as np

class DrawModule(object):

    def __init__(self):
        #cvController.CVController.__init__(self)
        self.currentFrame = None

    def run(image,parts):

        for (x, y, w, h) in parts:
            cv2.rectangle(image, (x, y), (x+w, y+h),  (0, 255, 0), 2)

        return image
