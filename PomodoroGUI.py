import tkinter as tk
import tkinter.font as tkFont
import time
import Constants
from WebsitesBlocker import WebsitesBlocker
from playsound import playsound
from GoogleSheetsWriter import GoogleSheetsWriter


class PomodoroGUI():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title(Constants.WINDOWS_TITLE)
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        self.text = tk.StringVar()
        self.text.set("Test")
        self.second_text = tk.StringVar()
        self.window.geometry(Constants.SIZE_OF_WINDOW_GUI)
        self.window.resizable(0, 0)
        self.photo = tk.PhotoImage(file=Constants.PATH_TO_TOMATO_IMAGE)
        self.font_style = tkFont.Font(family="Arial", size=15)
        self.label = tk.Label(self.window, fg="dark green", font=self.font_style, textvariable=self.text)
        self.label.pack()
        self.second_label = tk.Label(self.window, fg="dark green", font=self.font_style, textvariable=self.second_text)
        self.second_label.pack()
        self.button = tk.Button(self.frame, text="QUIT", image=self.photo, fg="red",
                                command=lambda: self.start_learning(Constants.LEARNING_MINUTES,
                                                                    Constants.SHORT_BREAK_MINUTES,
                                                                    Constants.LONG_BREAK_MINUTES)).pack(side=tk.TOP)
        self.window.mainloop()

    def start_learning(self, learning_minutes, short_break_minutes, long_break_minutes):
        website_blocker = WebsitesBlocker(Constants.LISTS_OF_BLOCKED_WEBSITES)
        google_writer = GoogleSheetsWriter(Constants.SPREADSHEET_ID)
        while True:
            for number_of_breaks in range(Constants.NUMBER_OF_BREAKS):
                website_blocker.block()
                self._timer('Pomodoro!', learning_minutes)  # Pomodoro
                website_blocker.unlock()
                self._timer('Short break', short_break_minutes)  # Short break
            self._timer('Long break', long_break_minutes)  # Long break
            google_writer.update_sheet("Nauka", '22', '23')

    def _timer(self, text, minutes):
        self.second_text.set(text)
        self.countdown(minutes)
        playsound(Constants.PATH_TO_SOUND)

    def countdown(self, number_of_minutes):
        when_to_stop = abs(int(number_of_minutes))
        while when_to_stop >= 0:
            m, s = divmod(when_to_stop, 60)
            time_left = str(m).zfill(2) + ":" + str(s).zfill(2)
            self.__change_text(time_left + "\r")
            self.window.update()
            time.sleep(1)
            when_to_stop -= 1

    def __change_text(self, text):
        self.text.set(text)
