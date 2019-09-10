# Python ver:   3.7.4
# Author:         Dhava
# Purpose:       Tkinter drill - The Tech Academy
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk
import gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(680, 220)
        self.master.maxsize(680, 220)

        self.master.title("Check files")
        self.master.configure(bg = "#F0F0F0")

        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        gui.load_gui(self,680,220) #function to create window and center it


if __name__=="__main__":
    root = tk.Tk()  #creates the window
    App = ParentWindow(root)
    root.mainloop()
