import tkinter as tk
import time
import Constans
from WebsitesBlocker import WebsitesBlocker

class PomodoroGUI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(Constans.windowTitle)
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        self.text = tk.StringVar()
        self.text.set("Test")
        self.window.geometry("512x524")
        self.window.resizable(0, 0)
        self.photo = tk.PhotoImage(file="Images/tomato.png")
        self.label = tk.Label(self.window, fg="dark green", textvariable = self.text)
        self.label.pack()
        self.button = tk.Button(self.frame, text="QUIT", image=self.photo, fg="red", command=lambda:[self.countdown(Constans.numberOfMinutes*60), WebsitesBlocker(Constans.listOfBlockedWebsites).Block()]).pack(side=tk.TOP)
        self.window.mainloop()

    def countdown(self, uint):
        when_to_stop = abs(int(uint))
        while when_to_stop >= 0:
            m, s = divmod(when_to_stop, 60)
            time_left = str(m).zfill(2) + ":" + str(s).zfill(2)
            self.__changeText(time_left + "\r")
            self.window.update()
            time.sleep(1)
            when_to_stop -= 1

    def __changeText(self, text):
        self.text.set(text)








