import os.path
import time
import shutil
import datetime
from datetime import timedelta
import tkinter.filedialog
import tkinter
from tkinter import *

def sourceDir():
    txtSource.delete(0,END)
    my_dir = tkinter.filedialog.askdirectory()
    txtSource.insert(0,my_dir)
def fileDes():
    txtDes.delete(0,END)
    my_dir2 = tkinter.filedialog.askdirectory()
    txtDes.insert(0,my_dir2)
def moveFiles():
    destination = txtDes.get()
    source = txtSource.get()
    file = os.listdir(source)
    for i in file:
        filepath = os.path.join(source,i)
        mod = os.path.getmtime(filepath)
        twentyFour = datetime.datetime.now()-timedelta(hours=24)
        filedate = datetime.datetime.fromtimestamp(mod)
        if twentyFour < filedate:
            shutil.move(source+'/'+i,destination)
            print('move succesful!')
        else:
            print('No files have been modified today')

m = tkinter.Tk()
m.minsize(750,150)
m.title('File Transfer')


btnSource = Button(m, text='Source',width=10, height=2, command=sourceDir)
btnSource.grid(row=1,column=0,padx=(0,0),pady=(30,0), sticky=NE)
txtSource = Entry(m,text='',font=('Helvetica',16), fg='black', bg='lightblue')
txtSource.grid(row=1,column=1,padx=(30,0),pady=(30,0))

btnDes = Button(m, text='Move to',width=10, height=2, command=fileDes)
btnDes.grid(row=1,column=3,padx=(30,0),pady=(30,0), sticky=NE)
txtDes = Entry(m,text='',font=('Helvetica',16), fg='black', bg='lightblue')
txtDes.grid(row=1,column=4,padx=(30,0),pady=(30,0))


btngo = Button(m, text='Transfer',width=10, height=2, command=moveFiles)
btngo.grid(row=6,column=5,padx=(10,10),pady=(30,0), sticky=NE)

m.mainloop()
