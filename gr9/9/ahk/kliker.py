from tkinter import *

tk = Tk()
tk.title('Кликер')
tk.geometry("1000x500")
n = 0
def nplus():
    global n
    n = n + 1
    label['text'] = str(n) + 'P'
def nsbros():
    global n
    n = 0
    label['text'] = str(n)+'P'
btn1 = Button(text='Клик', background="#000", foreground="#fff",
              padx='20', pady='8',font = "16", command=nplus)
btn1.pack()
label = Label(tk, text=str(n)+'P', font='Helvectica 26')
label.pack()
btn2 = Button(text='Клик', background="#fff", foreground="#000",
              padx='20', pady='8',font = "16", command=nsbros)
btn2.pack() 
mainloop()
