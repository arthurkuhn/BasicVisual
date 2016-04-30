import FbModule
import GmailModule

"""
f = FbModule.FbModule()

photoPath = '../photos/test-photo.jpg'
message = "Wow, noiceeee."
f.postPhoto(photoPath, message)
"""


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
