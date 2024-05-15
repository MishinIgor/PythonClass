from tkinter import *
root = Tk()
win = Tk()
 
def change(event):
    global X
    if X == True:
        b['fg'] = "red"
        b['activeforeground'] = "red"
        X = False
        win.mainloop()
    else:
        b['fg'] = "green"
        b['activeforeground'] = "red"
        X = True
X = True
for i in range(1,3):
    b = Button(text='RED', width=10, height=3)
    b.bind('<Button-1>', change)
    b.bind('<Return>', change)
    b.pack()
 
root.mainloop()