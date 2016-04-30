import cv2
import requests

class TextModule(object):

    def __init__(self):
        self.url = "https://maker.ifttt.com/trigger/event/with/key/c1AxRQLO4QaTP-NiC4M_PN"

    def execute(self,image,name):
        r = requests.post(self.url)
        #print(r.text)
