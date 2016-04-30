import dropbox
import webbrowser
import cv2
import datetime
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

class DropboxSheetsModule:
    def __init__(self, sheetsURL):
        # Dropbox.
        self.accessToken = "BqdBFIVK9UAAAAAAAAAADXXX_FSPz_UTqzc-V870k403PoO1Lrr2reIfeBkJ16_a"
        self.client = dropbox.client.DropboxClient(self.accessToken)
        self.name = "DropboxSheetsModule"

        # Sheets.
        self.rows = 1
        self.jsonFile = "BasicVisual-e88fe6c9fb47.json"
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.jsonFile, self.scope)
        self.gc = gspread.authorize(self.credentials)
        self.url = sheetsURL
        self.sheet = self.gc.open_by_url(self.url)
        self.worksheet = self.sheet.sheet1
        self.updateCurrentRow("Date", "Time", "Link")

    def updateCurrentRow(self, date, time, link):
        self.worksheet.update_cell(self.rows, 1, date)
        self.worksheet.update_cell(self.rows, 2, time)
        self.worksheet.update_cell(self.rows, 3, link)
        self.rows += 1
        print "Row " + str(self.rows) + " has been added."

    def execute(self, image, name):
        f = open(name, 'rb')
        dropboxPutLink = "BasicVisual/"+name.split('/')[-1]
        response = self.client.put_file(dropboxPutLink, f)
        print response
        path = response["path"]
        print "Photo has been uploaded."

        # Updates sheet
        filename = name.split("/")[-1]
        filename = filename[:-4]
        dateVars = filename.split("_")
        date = ".".join(dateVars[0:3])
        time = ".".join(dateVars[3:])
        link = "www.dropbox.com/home/BasicVisual?preview=" + name.split('/')[-1]
        self.updateCurrentRow(date, time, link)
        return "True"
