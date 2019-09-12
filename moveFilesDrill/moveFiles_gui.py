from tkinter import *
import tkinter as tk

import moveFiles_main
import moveFiles_func

def load_gui(self, w, h):

    #============================CREATE DATABASE==================
    moveFiles_func.create_db(self) 
    
    #============================LABELS============================
    self.lbl_srcDir = tk.Label(self.master, text="Source Directory:", bg='#FF1494', font=(50))
    self.lbl_srcDir.grid(row=0, column =0,  padx = (30,0), pady= (50, 0), sticky=W)
    self.lbl_dstnDir = tk.Label(self.master, text="Destination Directory:", bg='#FF1494', font=(50))
    self.lbl_dstnDir.grid(row=1, column=0, padx = (30,0), pady = (15,0), sticky=W)
    #=============================BUTTONS========================
    # Source Directory
    self.btn_srcDir = tk.Button(self.master, width = 3, height = 1, text = '...', font=('20'), \
                                   command = lambda: moveFiles_func.srcDir(self))
    self.btn_srcDir.grid(row = 0, column = 3, padx=(10,0), pady=(50,0))
    # Destination Directory
    self.btn_dstnDir = tk.Button(self.master, width = 3, height = 1, text = "...", font=('20'), \
                                 command = lambda: moveFiles_func.dstnDir(self))
    self.btn_dstnDir.grid(row = 1, column = 3, padx=(10,0), pady= (15,0))
    # Move
    self.btn_move = tk.Button(self.master, width = 17, height = 1, text= "Move", font=('20'), \
                              command = lambda: moveFiles_func.moveDir(self))
    self. btn_move.grid(row = 2, column =1, padx = (40, 0), pady = (30, 0))
    # Close Program
    self.btn_close = tk.Button(self.master, width = 17, height = 1, text = "Close", font=('20'), \
                              command = lambda: moveFiles_func.ask_quit(self))
    self.btn_close.grid(row = 2, column = 2, padx = (0,0), pady = (30,0))

    #=============================TEXTBOXES========================
    # Source Directory
    self.txt_srcDir = tk.Entry(self.master, text='', width = 70)
    self.txt_srcDir.grid(row = 0, column =1, columnspan = 2, padx=(10,0), pady = (50,0), sticky = N+E+W+S )
    # Destination Directory
    self.txt_dstnDir = tk.Entry(self.master, text='', width = 70)
    self.txt_dstnDir.grid(row = 1, column=1, columnspan = 2, padx= (10,0), pady= (15,0), sticky = N+E+W+S)

    #===========================CENTER WINDOW====================
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo
                                                                                    

if __name__== "__main__":
    pass
  
