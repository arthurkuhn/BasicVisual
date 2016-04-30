import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import datetime
import time

class PictureModule(object):

    def __init__(self,timeout,savePic):
        self.time = datetime.datetime.now()
        self.timeout = timeout
        self.name = "Picture"
        self.savePic = savePic

    def execute(self,image,name):

        if(datetime.datetime.now() > self.time):
            dateText =  datetime.datetime.now().strftime("%d_%B_%Y_%I_%M_%S%p")
            picName = "../photos/" + dateText + ".jpg" 
            print picName
            if(self.savePic):
                cv2.imwrite(picName, image)
            self.time = datetime.datetime.now() + datetime.timedelta(0,self.timeout)
            return picName

        print "Blocking Action"
        return ""
