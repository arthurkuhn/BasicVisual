import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

class GmailModule:
    def __init__(self, sender, receiver, senderPassword):
        self.sender = sender
        self.receiver = receiver
        self.senderPassword = senderPassword
        self.message = MIMEMultipart()

    def createMessage(self, subject, body):
        self.message['From'] = self.sender
        self.message['To'] = self.receiver
        self.message['Subject'] = subject
        self.message.attach(MIMEText(body, 'plain'))
        print "Message is created."

    def attachPhoto(self, photoPath, fileName):
        attachment = open(photoPath, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % fileName)
        self.message.attach(part)
        print "Photo is attached."

    def sendEmail(self):
        try:
           server = smtplib.SMTP('smtp.gmail.com', 587)
           server.starttls()
           server.login(self.sender, self.senderPassword)

           text = self.message.as_string()
           server.sendmail(self.sender, self.receiver, text)
           server.quit()
           print "Successfully sent email"
        except smtplib.SMTPException:
           print "Error: unable to send email"
