import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cvBodyModule
import cvFaceModule
import cvMotionModule
import cvController
import ifModule
import cvTakePicture

def drawResult(image,parts,color):

    for (x, y, w, h) in parts:
        cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)

    return image

if __name__ == '__main__':

    cvControl = cvController.CVController()
    cvFace = cvFaceModule.FaceModule(cvControl.cap)
    cvBody = cvBodyModule.BodyModule(cvControl.cap)
    cvMotion = cvMotionModule.MotionModule(cvControl.cap)
    #cvPicture = cvTakePicture.PictureModule()

    ifStatements = [ifModule.IFModule(cvMotion,{"var":"ThereIsMotion", "comp":"=","eq":"True"},"")]

    while(True):
        ret,image = cvControl.cap.read()
        image = imutils.resize(image, width=min(400, image.shape[1]))
        for ifS in ifStatements:
            result,drawList = ifS.testCondition(image)
            if result:
                print True
                #ifS.executeExpressions(image)

            image = drawResult(image,drawList,(0, 255, 0))
            cv2.imshow("Output", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    self.cap.release()
    cv2.destroyAllWindows()
