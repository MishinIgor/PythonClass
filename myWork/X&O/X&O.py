from tkinter import *
from tkinter import ttk

win = Tk()
win.title('X & O game')
win.geometry("500x350")
x = True
def CX():
    if btn == True:
        btn[""] = "X" 
        x = False
    else:
        btn[""] = "O"
        x = True
    return x
for c in range(3): win.columnconfigure(index=c, weight=1)
for r in range(3): win.rowconfigure(index=r, weight=1)

for r in range(3):
    for c in range(3):
        btn = ttk.Button(text='', command = CX)
        btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4, sticky=NSEW)
win.mainloop()