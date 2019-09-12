# Python ver:   3.7.45
# Author:         Dhava
# Purpose:       Python drill - The Tech Academy. Creating an application that moves files from  \
#                      repository to destination repository
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk
import moveFiles_gui
import moveFiles_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(700, 220)
        self.master.maxsize(700, 220)

        self.master.title("Move .txt files")
        self.master.configure(bg = "#FF1494")

        self.master.protocol("WM_DELETE_WINDOW", lambda: moveFiles_func.ask_quit(self))
        arg = self.master

        moveFiles_gui.load_gui(self, 700, 220)
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
