from ahk import AHK
import os
def my_callback():
    print(f'{os.system("taskkill /im autohotkey.exe")}')
def my_crazymouse():
    while True:
        ahk.mouse_move(x=100, y=100, blocking=True)
        ahk.mouse_move(x=1023, y=57, speed=10, blocking=True)
ahk = AHK()

ahk.add_hotkey('#n', callback=my_callback)
ahk.add_hotkey('#t', callback=my_crazymouse)
ahk.start_hotkeys()
ahk.block_forever()