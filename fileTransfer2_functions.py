'''
Python 3.6.0

Jenny Tso
Tkinter and SQLite Drill

'''

from os import listdir, path, remove, _exit
from datetime import datetime
from time import mktime
from tkinter import *
from tkinter import filedialog
from shutil import copy
import sqlite3

import fileTransfer2_main
import fileTransfer2_gui


conn = sqlite3.connect('dateTime.db')
c = conn.cursor()

time_now = datetime.now()
time_now_epoch = mktime(time_now.timetuple())
timeframe = 86400 #seconds in 24 hours

def create_table(self):
    c.execute('CREATE TABLE IF NOT EXISTS filechecks(col_datetime TEXT)')
    conn.commit

def show_datetime(self):
    c.execute('SELECT * FROM filechecks ORDER BY col_datetime DESC LIMIT 1') 
    dateTime = c.fetchone()
    if dateTime is None:
        none = '( No transfer record. )'
        self.date_and_time.set(none)
    else:
        dateTime_str = datetime.strptime(dateTime[0], '%Y-%m-%d %H:%M:%S.%f').strftime('%m-%d-%Y %H:%M:%S')
        self.date_and_time.set(dateTime_str)

def send_datetime(self):
    c.execute('INSERT INTO filechecks (col_datetime) VALUES (?)',(time_now,))
    conn.commit()  

def on_quit(self):
    c.close()     
    conn.close()
    self.master.destroy()
    _exit(0)

def browseSrc(self):
    sourceDirectory = filedialog.askdirectory(initialdir="C:\\")
    self.srcDir.set(sourceDirectory)

def browseDest(self):
    destDirectory = filedialog.askdirectory(initialdir="C:\\")
    self.destDir.set(destDirectory)

def listFiles(self):
    sourceDir = self.srcDir.get()
    filesInDir = listdir(sourceDir)
    for filename in filesInDir:
        eachFile = path.join(sourceDir, filename)
        self.listbox.insert(0,eachFile)

# Transfer files if created or modified within 24 hrs
def transfer(self):
    sourceDir = self.srcDir.get()
    destDir = self.destDir.get()
    filesToTrans = listdir(sourceDir)
    for file in filesToTrans:
        origFile = path.join(sourceDir, file)
        timestamp = path.getmtime(origFile)
        if (time_now_epoch - timestamp) <= timeframe:
            copy(origFile, destDir)
            remove(origFile)
    messagebox.showinfo(title='Success!',message='Your files have been transferred. \nHave a wonderful day. :-)')
    send_datetime(self)

# Clear all fields    
def clear(self):
    self.field_src.delete(0,END)
    self.field_dest.delete(0,END)
    self.listbox.delete(0,END)


if __name__ == "__main__":
    pass
