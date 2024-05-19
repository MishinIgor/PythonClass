from ahk import AHK
import os

def my_callback():
    print(f'{os.system("taskkill /im autohotkey.exe")}')

ahk = AHK()
ahk.add_hotkey('#n', callback=my_callback)
ahk.start_hotkeys()
ahk.block_forever()