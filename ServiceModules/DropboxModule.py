import dropbox
import webbrowser

class DropboxModule:
    def __init__(self, accessToken):
        self.accessToken = accessToken
        self.client = dropbox.client.DropboxClient(self.accessToken)

    def uploadPhoto(self, photoPath, dropboxPath):
        f = open(photoPath, 'rb')
        response = self.client.put_file(dropboxPath, f)
        print "Photo has been uploaded."
