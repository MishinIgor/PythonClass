from tkinter import *

tk = Tk()
tk.title('Кликер')
tk.geometry('550x200')
n = 0
def nplus():
    global n 
    n += 1
    label1['text'] = 'Изначально n = '+str(n)
def nsbros():
    global n 
    n = 0
    label1['text'] = 'Изначально n = '+str(n)
    label2['text'] = 'В двоичном виде n = '
def dvoichka():
    global n
    a = n
    rezult = ''
    while a:
        ost = a % 2
        a = a // 2
        rezult = str(ost)+rezult
    label2['text'] = 'В двоичном виде n = '+str(rezult)
btn1 = Button(text="Кликай!", background="#000", foreground='#fff',
              padx="20", pady="8",font="25", command=nplus)
btn2 = Button(text="Обнуляй!", background="#fff", foreground='#000',
              padx="20", pady="8",font="25", command=nsbros)
btn3 = Button(text="Переведи в двоинчую систему!", background="#fff", foreground='#000',
              padx="20", pady="8",font="25",command=dvoichka)
label1 = Label(tk, text='Изначально n = '+str(n),font=('25'),background='#00f',foreground='#fff')
label2 = Label(tk, text='В двоичном виде n = ',font=('25'),background='#00f',foreground='#fff')
btn1.pack(anchor="nw")
btn2.pack(anchor="se")
label1.pack()
label2.pack()
btn3.pack()
mainloop()