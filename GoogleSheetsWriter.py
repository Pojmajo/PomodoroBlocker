from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetsWriter:
    def __init__(self, spreadsheet_id):
        self.__spreadsheetId = spreadsheet_id

    def update_sheet(self, sheet_name, start_time, end_time, time_elapsed, number_of_pomodoro_sessions):
        scopes = 'https://www.googleapis.com/auth/spreadsheets'
        creds = ServiceAccountCredentials.from_json_keyfile_name('pomodoro-blocker.json', scopes)
        service = build('sheets', 'v4', http=creds.authorize(Http()))
        values = [[str(datetime.datetime.now()), start_time, end_time, time_elapsed, number_of_pomodoro_sessions]]
        body = {'values': values}
        result = service.spreadsheets().values.append(spreadsheetId=self.__spreadsheetId, range=sheet_name + '!A1:G1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body=body).execute()




