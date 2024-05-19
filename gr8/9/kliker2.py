from ahk import AHK
import os
ahk = AHK()
def message():
    print('Окей, всё хорошо')
def message2():
    print('Окей, хорошо вль и всё')
def mycrazymouse():
    for i in range(25):
        ahk.mouse_move(x=100,y=200,speed=6,blocking=True)
        ahk.mouse_move(x=250,y=150,speed=6,blocking=True)
def myover():
    print(f'{os.system("taskkill /im autohotkey.exe")}')

ahk.add_hotkey('^q',callback=message)
ahk.add_hotkey('^w',callback=message2)
ahk.add_hotkey('^e',callback=mycrazymouse)
ahk.add_hotkey('^t',callback=myover)
ahk.start_hotkeys()
ahk.block_forever()
    

