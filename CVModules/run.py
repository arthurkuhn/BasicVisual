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

def execute(ifStatements):

    cvControl = cvController.CVController()
    cvFace = cvFaceModule.FaceModule()
    cvBody = cvBodyModule.BodyModule()
    cvMotion = cvMotionModule.MotionModule()
    #cvPicture = cvTakePicture.PictureModule()

    #ifStatements = [ifModule.IFModule(cvFace,{"var":"ThereIsAFace", "comp":"=","eq":"True"},"")]

    while(True):
        ret,image = cvControl.cap.read()
        #print cvControl.cap.read()
        #if(image is None):
        #    continue
        image = imutils.resize(image, width=min(400, image.shape[1]))
        
        for ifS in ifStatements:
            result,drawList = ifS.testCondition(image)
            if result:
                #print True
                ifS.executeExpressions(image)

            image = drawResult(image,drawList,(0, 255, 0))
            cv2.imshow("Output", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cvControl.cap.release()
    cv2.destroyAllWindows()
