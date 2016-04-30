import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cvController

class BodyModule(object):

    def __init__(self,cap):
        self.cap = cap
        self.isBody = False
        self.numBodies = 0
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        self.toPrint = True
        self.currentFrame = None

    def start(self):

        while(True):
            ret,image = self.cap.read()

            image = imutils.resize(image, width=min(400, image.shape[1]))

            orig = image.copy()

            # detect people in the image
            (rects, weights) = self.hog.detectMultiScale(image, winStride=(4, 4),
            padding=(8, 8), scale=1.01)

            # draw the original bounding boxes
            if self.toPrint:
                for (x, y, w, h) in rects:
                    cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # apply non-maxima suppression to the bounding boxes using a
            # fairly large overlap threshold to try to maintain overlapping
            # boxes that are still people
            rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
            pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

            # draw the final bounding boxes
            if self.toPrint:
                for (xA, yA, xB, yB) in pick:
                    cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)


            self.numBodies = len(pick)

            if(len(pick) > 0):
                self.isBody = True
            else:
                self.isBody = False

            # show the output images
            cv2.imshow("Output", image)
            self.currentFrame = image

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
