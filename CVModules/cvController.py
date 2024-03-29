import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cvBodyModule
import cvFaceModule
import cvMotionModule
import ifModule


class CVController(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

'''
def drawResult(image,parts,color):

    for (x, y, w, h) in parts:
        cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)

    return image


if __name__ == '__main__':

    y = CVController()
    x = cvFaceModule.FaceModule(y.cap)
    z = cvBodyModule.BodyModule(y.cap)
    b = cvMotionModule.MotionModule(y.cap)

    ifStatement = ifModule.IFModule(x,"","")

    while(True):
        ret,image = y.cap.read()
        image = imutils.resize(image, width=min(400, image.shape[1]))

        #result, drawList = x.run(image)
        #result2,drawList2 = z.run(image)
        result, drawList = ifStatement.testCondition(image)

        image = drawResult(image,drawList,(0, 255, 0))
        #image = drawResult(image,drawList2,(255, 0, 0))

        cv2.imshow("Output", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    self.cap.release()
    cv2.destroyAllWindows()
'''
