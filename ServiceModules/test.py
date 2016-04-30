import GmailModule
import SheetsModule

def runFbModule():
    f = FbModule.FbModule()

    photoPath = '../photos/test-photo.jpg'
    message = "Wow, noiceeee."
    f.postPhoto(photoPath, message)

def runGmailModule():
    sender = 'fbhackathon16@gmail.com'
    receiver = 'fbhackathon16@gmail.com'
    senderPassword = "movefast"
    g = GmailModule.GmailModule(sender, receiver, senderPassword)

    subject = "Hello from BasicVisual!"
    body = "Here is the photo that you requested."
    g.createMessage(subject, body)

    photoPath = "../photos/test-photo.jpg"
    fileName = "Photo1.jpg"
    g.attachPhoto(photoPath, fileName)

    g.sendEmail()

def runSheetsModule():
    url = "https://docs.google.com/spreadsheets/d/1v30p35_yLDHV2Oefi0zvbUBqqbMZOD4or_4mrkge-EY/edit#gid=0"

    s = SheetsModule.SheetsModule(jsonFile, scope, url)
    s.updateCurrentRow("4th April 16", "8:09pm", "5 faces")

def runDropbox():
    accessToken = "BqdBFIVK9UAAAAAAAAAADXXX_FSPz_UTqzc-V870k403PoO1Lrr2reIfeBkJ16_a"
    d = DropboxModule.DropboxModule(accessToken)

    photoPath = "../photos/test-photo.jpg"
    dropboxPath = "BasicVisual/test-photo.jpg"
    d.uploadPhoto(photoPath, dropboxPath)


runGmailModule()
