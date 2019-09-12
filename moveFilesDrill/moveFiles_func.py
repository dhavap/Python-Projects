from tkinter import filedialog
from tkinter import *
import time
import tkinter as tk
import os
import shutil
from tkinter import messagebox
import sqlite3

import moveFiles_main
import moveFiles_func

def create_db(self):  # create database for .txt files
    conn = sqlite3.connect('db_txtFiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_txtFiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            file_name TEXT, \
            last_modified TEXT );")
        conn.commit()
    conn.close()

def srcDir(self):  # select source directory
    var_srcDir = filedialog.askdirectory()
    self.txt_srcDir.delete(0,END)
    self.txt_srcDir.insert(INSERT,var_srcDir)

def dstnDir(self): # select destination directory
    var_dstnDir = filedialog.askdirectory()
    self.txt_dstnDir.delete(0,END)
    self.txt_dstnDir.insert(INSERT,var_dstnDir)

def moveDir(self): # move .txt files from source directory to destination directory
    get_srcDir = self.txt_srcDir.get() #get the source directory from the widget
    get_dstnDir = self.txt_dstnDir.get() # get the destination directory from the widget
    srcDir_contents = os.listdir(get_srcDir)  # get a list of all the files in the directory
    i = 0
    while i < len(srcDir_contents): # iterate through the files
        fName = srcDir_contents[i]
        if fName.endswith('.txt'): #select for files with .txt extension
            abPath_src = os.path.join(get_srcDir, fName) # filepath for source file
            abPath_dstn = os.path.join(get_dstnDir, fName) # filepath for destination file
            timeStamp = os.path.getmtime(abPath_src)
            convertTime = time.ctime(timeStamp)

            conn = sqlite3.connect('db_txtFiles.db')  # insert .txt file name and time stamp into table
            with conn:
                cur = conn.cursor()
                cur.execute("""INSERT INTO tbl_txtFiles (file_name, last_modified) VALUES (?, ?)""", (fName, convertTime))
                conn.commit()
            conn.close()
            
            print("File Name: {}, Latest date created/modified: {}\n".format(fName, convertTime)) # print to console
            shutil.move(abPath_src, abPath_dstn)  # move files from source directory to destination directory
        i+=1

def ask_quit(self):
    if messagebox.askokcancel("Goodbye!", "Okay to exit application?"):
        self.master.destroy()

if __name__ == "__main__":
    pass
