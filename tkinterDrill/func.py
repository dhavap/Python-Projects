from tkinter import filedialog
from tkinter import *
import tkinter as tk
import main
import gui

def browse_folder(self):
    directory = filedialog.askdirectory()
    if directory:
        self.txt_browse1.delete(0,END)  # delete text currently in the textbox
        self.txt_browse1.insert(INSERT, directory)
    else:
        return None 
        
