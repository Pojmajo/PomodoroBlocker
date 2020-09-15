import Constans
from WebsitesBlocker import WebsitesBlocker
from GoogleSheetsWriter import GoogleSheetsWriter
from PomodoroGUI import PomodoroGUI

#websiteBlocker = WebsitesBlocker(Constans.listOfBlockedWebsites)
#googleSheetsWriter = GoogleSheetsWriter(Constans.spreadsheetId)
#googleSheetsWriter.update_sheet(subject, timeStart, timeEnd, time_elapsed, number_of_pomodoro_sessions)

pomodoroWindow = PomodoroGUI()

##googleSheetsWriter.update_sheet('Matematyka', startTime, endTime, timeElapsed, numberOfSessions)