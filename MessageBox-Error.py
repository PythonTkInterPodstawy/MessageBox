from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("Message box")

window.geometry('350x200')

def clicked_retry():
    res = messagebox.askretrycancel('Message title', 'Retry')
    if res == True:
        print("RETRY")
    if res == False:
        print("CANCEL")

def clicked_warrning():
    messagebox.showwarning('Message title', 'Warrning')

def clicked_error():
    messagebox.showerror('Message title', 'Error')



btn = Button(window, text="Retry", command=clicked_retry)
btn.grid(column=0, row=0)

btn = Button(window, text="Warrning", command=clicked_warrning)
btn.grid(column=1, row=0)

btn = Button(window, text="Error", command=clicked_error)
btn.grid(column=2, row=0)

window.mainloop()