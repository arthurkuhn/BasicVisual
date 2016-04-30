import FbModule
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
    jsonFile = "../../BasicVisual-e88fe6c9fb47.json"
    scope = ['https://spreadsheets.google.com/feeds']
    url = "https://docs.google.com/spreadsheets/d/1v30p35_yLDHV2Oefi0zvbUBqqbMZOD4or_4mrkge-EY/edit#gid=0"

    s = SheetsModule.SheetsModule(jsonFile, scope, url)
    s.updateCurrentRow("4th April 16", "8:09pm", "5 faces")
    s.updateCurrentRow("4th April 16", "8:10pm", "5 faces")
    s.updateCurrentRow("4th April 16", "8:10pm", "5 faces")

runSheetsModule()
