from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("Message box")

window.geometry('350x200')

def clicked():
    res = messagebox.askyesno('Message title', 'Message content')
    if res == True:
        print("Yes")
    else:
        print("No")


btn = Button(window, text='Click here', command=clicked)

btn.grid(column=0, row=0)

window.mainloop()