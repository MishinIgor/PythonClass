from ahk import AHK

ahk = AHK()

ahk.mouse_move(x=500,y=100,speed=7,blocking=True)
ahk.mouse_move(x=1028,y=64,speed=7,blocking=True)
#input()
ahk.click()
print(ahk.mouse_position)