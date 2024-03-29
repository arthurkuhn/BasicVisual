import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

class SheetsModule:
    def __init__(self, url):
        self.rows = 1
        self.jsonFile = "BasicVisual-e88fe6c9fb47.json"
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.jsonFile, self.scope)
        self.gc = gspread.authorize(self.credentials)
        self.url = url
        self.sheet = self.gc.open_by_url(self.url)
        self.worksheet = self.sheet.sheet1
        self.updateCurrentRow("Date", "Time")
        self.name = "Sheets"

    def updateCurrentRow(self, date, time):
        self.worksheet.update_cell(self.rows, 1, date)
        self.worksheet.update_cell(self.rows, 2, time)
        self.rows += 1
        print "Row " + str(self.rows) + " has been added."

    def execute(self, image, name):
        filename = name.split("/")[-1]
        filename = filename[:-4]
        dateVars = filename.split("_")
        date = ".".join(dateVars[0:3])
        time = ".".join(dateVars[3:])
        self.updateCurrentRow(date, time)
        return "True"
