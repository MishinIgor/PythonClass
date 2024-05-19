from ahk import AHK
import os

ahk = AHK()

def my_message():
    print('Вот моё вам сообщение')
def over():
    print(f'{os.system("taskkill /im autohotkey.exe")}')
def fire():
    for i in range(50):
        ahk.click()
ahk.add_hotkey('^q',callback=my_message)
ahk.add_hotkey('^t',callback=over)
ahk.add_hotkey('^f',callback=fire)
ahk.start_hotkeys()
ahk.block_forever()