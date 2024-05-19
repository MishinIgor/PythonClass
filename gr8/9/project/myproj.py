from tkinter import *

n = 0
tk = Tk()
tk.title('Наш замечательный Проект!')
tk.geometry("500x400") #500x500 - размер окна, +750+200 - сдвиг появления окна.

def nplus():
    global n 
    n += 1
    label1["text"] = 'n = '+str(n)
def nsbros():
    global n 
    n = 0
    label1["text"] = 'n = '+str(n)
def dvoika():
    a = n
    a = bin(n)[2:]
    label2["text"] = 'В двоичной системе n = '+a
    


btn1 = Button(text='Кликай!', padx="20", pady="8",foreground="#fff" ,background="#000",command=nplus)
btn2 = Button(text='Сбрасывай!',command=nsbros)
btn3 = Button(text='Переводи!',command=dvoika)
label1 = Label(tk, text='n = ', font='Helvetica 50')
label1.pack()
label2 = Label(tk, text='В двоичной системе n = ', font='Helvetica 20',background="#FFCDD2", foreground="#B71C1C",)
label2.pack()
btn1.pack()
btn2.pack()
btn3.pack()

mainloop()