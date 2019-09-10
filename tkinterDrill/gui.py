from tkinter import *
import tkinter as tk
import main
import func

def load_gui(self, w, h): # called in main
    #====================BUTTONS========================
    # Browse button1
    self.btn_browse1 = tk.Button(self.master, width = 15, height = 1, text = 'Browse...', font=('20'), \
                                 command=lambda: func.browse_folder(self))
                                 
    self.btn_browse1.grid(row = 0, column = 1, padx=(30,0), pady=(50,0) )
    # Browse button2
    self.btn_browse2 = tk.Button(self.master, width = 15, height = 1, text = 'Browse...', font=('20'))
    self.btn_browse2.grid(row = 1, column = 1, padx=(30,0), pady=(15,0))
    # Check for files button
    self.btn_chkfiles = tk.Button(self.master, width = 15, height =2, text = 'Check for files...', font=('20'))
    self.btn_chkfiles.grid(row = 2, column = 1, padx=(30,0), pady=(15,0))
    # Close program button
    self.btn_closePgm = tk.Button(self.master, width = 15, height = 2, text ='Close Program', font=('20'))
    self.btn_closePgm.grid(row=2, column = 3, padx=(30,0), pady=(15,0), sticky=E)

    #==================TEXTBOXES=========================
    self.txt_browse1 = tk.Entry(self.master, text='', width= 70)
    self.txt_browse1.grid(row = 0, column = 2, columnspan=2, padx=(50,0), pady=(50,0), sticky=N+E+W+S)

    self.txt_browse2 = tk.Entry(self.master, text='', width=70)
    self.txt_browse2.grid(row = 1, column = 2, columnspan=2, padx=(50,0), pady=(15,0), sticky=N+E+W+S)

    #=================CENTER WINDOW======================
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo







