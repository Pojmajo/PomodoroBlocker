from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
import Constants
from oauth2client import file, client, tools
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheetsWriter:
    def __init__(self, spreadsheet_id):
        self.__spreadsheetId = spreadsheet_id

    def update_sheet(self, sheet_name, date, start_time, end_time, number_of_sessions):
        scopes = 'https://www.googleapis.com/auth/spreadsheets'
        creds = ServiceAccountCredentials.from_json_keyfile_name(Constants.PATH_TO_JSON, scopes)
        service = build('sheets', 'v4', http=creds.authorize(Http()))
        values = [[date, start_time, end_time, number_of_sessions]]
        body = {'values': values}
        result = service.spreadsheets().values().append(spreadsheetId=self.__spreadsheetId, range=sheet_name + '!A1:D1', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body=body).execute()





