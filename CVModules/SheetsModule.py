import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

class SheetsModule:
    def __init__(self, jsonFile, scope, url):
        self.rows = 0
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonFile, scope)
        self.gc = gspread.authorize(self.credentials)
        self.url = url
        self.sheet = self.gc.open_by_url(self.url)
        self.worksheet = self.sheet.sheet1
        self.updateCurrentRow("Date", "Time", "Details")

    def updateCurrentRow(self, date, time, details):
        self.worksheet.update_cell(self.rows, 1, date)
        self.worksheet.update_cell(self.rows, 2, time)
        self.worksheet.update_cell(self.rows, 3, details)
        self.rows += 1
        print "Row " + str(self.row) + " has been added."
