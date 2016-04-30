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

    def start(self):

        while(True):

            (grabbed, frame) = self.cap.read()

            if not grabbed:
        		break

            frame = imutils.resize(frame, width=500)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            if self.firstFrame is None:
        		self.firstFrame = gray
        		continue

            frameDelta = cv2.absdiff(self.firstFrame, gray)
            thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

            thresh = cv2.dilate(thresh, None, iterations=2)
            (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)

            for c in cnts:

            	if cv2.contourArea(c) < 500:
            		continue

            	(x, y, w, h) = cv2.boundingRect(c)
            	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                #cv2.putText(frame, "Room Status: {}".format(text), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                #cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

                cv2.imshow("Output", frame)


            self.currentFrame = frame

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
