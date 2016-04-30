'''
Created on Apr 30, 2016

@author: Arthur
'''

import cvBodyModule
import cvFaceModule
import cvMotionModule
import cvController
import ifModule
import cvTakePicture


def createIF( components):
    cvModule = None
    cond = {}
    expression = []
    
    if(components["module"]== "FaceDetect"):
        cvModule = cvFaceModule.FaceModule()
    elif(components["module"] == "BodyDetect"):
        cvModule = cvBodyModule.BodyModule()
    elif(components["module"] == "MotionDetect"):
        cvModule = cvMotionModule.MotionModule()
    
    cond["var"] = components["var"]
    cond["comp"] = components["comp"]
    cond["eq"] = components["eq"]
    
    return ifModule.IFModule(cvModule,cond,"")

            
        
        
        
        
    
    