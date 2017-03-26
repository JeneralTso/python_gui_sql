'''
Python 3.6.0

Jenny Tso
Tkinter and SQLite Drill

'''

from tkinter import *
import tkinter as ttk

import fileTransfer2_gui
import fileTransfer2_functions


class ParentFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.minsize(480, 450)
        self.master.maxsize(480, 450)
        self.master.title("Transfer New or Modified Files")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: fileTransfer2_functions.on_quit(self))
        fileTransfer2_gui.window(self)
        fileTransfer2_functions.create_table(self)
        fileTransfer2_functions.show_datetime(self)
        

if __name__ == "__main__":
    root = ttk.Tk()
    Application = ParentFrame(root)
    root.mainloop()
    
