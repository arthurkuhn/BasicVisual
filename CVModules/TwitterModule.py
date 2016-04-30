import cv2
import requests

class TwitterModule(object):

    def __init__(self):
        self.url = "https://maker.ifttt.com/trigger/event3/with/key/c1AxRQLO4QaTP-NiC4M_PN"
        self.name = "TwitterModule"
    def execute(self,image,name):
        r = requests.post(self.url)
