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
import fbModule
import GmailModule
import DropboxModule
import SheetsModule

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
    cond["expression"] = components["expression"]
    
    if(cond["expression"] == "PostImageToFacebook"):
        expression.append(cvTakePicture.PictureModule(30))
        expression.append(fbModule.FbModule())
    if(cond["expression"] == "PostImageToDropbox"):
        expression.append(cvTakePicture.PictureModule(30))
        expression.append(DropboxModule.DropboxModule())
    if(cond["expression"] == "SendAnEmail"):
        expression.append(cvTakePicture.PictureModule(30))
        expression.append(GmailModule.GmailModule("fbhackathon16@gmail.com","fbhackathon16@gmail.com","movefast"))

    return ifModule.IFModule(cvModule,cond,expression)

            
        
        
        
        
    
    