
from tkinter import *
import webbrowser

window = Tk()

window.title("Webpage Generator")

window.geometry('350x200')

lbl = Label(window, text="Welcome!")

lbl.grid(column=0, row=0)

v = StringVar()

txt = Entry(window,textvariable = v, width=10)

txt.grid(column=1, row=0)


def clicked():
    usertext = txt.get()
    f=open('2.html','w')
    htmlcode = "<html><head><title>Web page generator</title></head><body>"+ usertext + "</body></html>"
    f.write(htmlcode)
    f.close()
    webbrowser.open_new_tab('2.html')

btn = Button(window, text="Create", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()
