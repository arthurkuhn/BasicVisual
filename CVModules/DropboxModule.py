import dropbox
import webbrowser
import cv2
import datetime

class DropboxModule:
    def __init__(self, accessToken):
        self.accessToken = accessToken
        self.client = dropbox.client.DropboxClient(self.accessToken)
        self.name = "DropboxModule"

    def execute(self, image, photoPath):
        f = open(photoPath, 'rb')
        response = self.client.put_file("BasicVisual/test.jpg", f)
        print "Photo has been uploaded."
