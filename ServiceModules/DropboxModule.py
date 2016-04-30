import dropbox
import webbrowser
import cv2
import datetime

class DropboxModule:
    def __init__(self):
        self.accessToken = "BqdBFIVK9UAAAAAAAAAADXXX_FSPz_UTqzc-V870k403PoO1Lrr2reIfeBkJ16_a"
        self.client = dropbox.client.DropboxClient(self.accessToken)
        self.name = "DropboxModule"

    def execute(self, image, photoPath):
        f = open(photoPath, 'rb')
        name = "BasicVisual/"+photoPath.split('/')[-1]
        print name
        response = self.client.put_file(name, f)
        print "Photo has been uploaded."
