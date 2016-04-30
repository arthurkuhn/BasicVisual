import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cvController

class FaceModule(object):

    def __init__(self,cap):
        #cvController.CVController.__init__(self)
        self.cap = cap
        self.isFace = False
        self.numFaces = 0
        self.faceCasc = "../cascades/haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.faceCasc)
        self.toPrint = True
        self.currentFrame = None

    def start(self):

        while(True):
            ret,image = self.cap.read()
            image = imutils.resize(image, width=min(400, image.shape[1]))

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.02,
                minNeighbors = 5,
                minSize=(30,30),
                flags = cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            if(len(faces) > 0):
                self.isFace = True
            else:
                self.isFace = False

            numFace = len(faces)

            if(self.toPrint):
                for (x, y, w, h) in faces:
                    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

                cv2.putText(image, "Face Status: {}".format(self.isFace), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            cv2.imshow("Output", image)
            self.currentFrame = image

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
