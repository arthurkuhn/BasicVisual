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
import IFTextModule
import TwitterModule
import DropboxSheetsModule


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
    
    timeInterval = components["time"]
    
    if(cond["expression"] == "PostImageToFacebook"):
        expression.append(cvTakePicture.PictureModule(timeInterval,True))
        expression.append(fbModule.FbModule())
    if(cond["expression"] == "PostImageToDropbox"):
        expression.append(cvTakePicture.PictureModule(timeInterval,True))
        expression.append(DropboxModule.DropboxModule())
    if(cond["expression"] == "SendAnEmail"):
        expression.append(cvTakePicture.PictureModule(timeInterval,True))
        expression.append(GmailModule.GmailModule("fbhackathon16@gmail.com","fbhackathon16@gmail.com","movefast"))
    if(cond["expression"] == "LogToSheets"):
        expression.append(cvTakePicture.PictureModule(timeInterval,False))
        expression.append(SheetsModule.SheetsModule("https://docs.google.com/spreadsheets/d/1v30p35_yLDHV2Oefi0zvbUBqqbMZOD4or_4mrkge-EY/edit#gid=0"))        
    if(cond["expression"] == "SendText"):
        expression.append(cvTakePicture.PictureModule(timeInterval,False))
        expression.append(IFTextModule.TextModule())
    if(cond["expression"] == "SendTweet"):
        expression.append(cvTakePicture.PictureModule(timeInterval,False))
        expression.append(TwitterModule.TwitterModule())
    if(cond["expression"] == "UploadAndLog"):
        expression.append(cvTakePicture.PictureModule(timeInterval,True))
        expression.append(DropboxSheetsModule.DropboxSheetsModule("https://docs.google.com/spreadsheets/d/1v30p35_yLDHV2Oefi0zvbUBqqbMZOD4or_4mrkge-EY/edit#gid=0"))
    return ifModule.IFModule(cvModule,cond,expression)

            
        
        
        
        
    
    