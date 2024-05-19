from tkinter import *

tk = Tk()

tk.title('Clicker')
tk.geometry("350x350")
n=15
def nplus():
    global n 
    n += 1
    label['text'] = str(n)+'P'
    
def nsbros():
    global n
    n = 0
    label['text'] = str(n)+'P'

label = Label(tk, text=str(n)+'P',font=("Helvetica 25"))
label.pack()

btn1 = Button(text="Клик", background="#000", foreground="#fff",
              padx="20",pady="8",font=(25), command=nplus)
btn1.pack()

btn2 = Button(text="Сброс",background="#fff",foreground="#000",
              padx="20",pady="8",font=(25), command=nsbros)
btn2.pack()
mainloop()