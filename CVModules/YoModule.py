import cv2
import requests

class YoModule(object):

    def __init__(self):
        self.url = "https://maker.ifttt.com/trigger/event2/with/key/c1AxRQLO4QaTP-NiC4M_PN"
        self.name = "yoModule"
    def execute(self,image,name):
        r = requests.post(self.url)
