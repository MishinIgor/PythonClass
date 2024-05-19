Название питоновского файла не должно совпадать с ahk(с импортированной библиотекой)

Устанавливаем в VSC расширение AutoHotkey Plus

Переходим на сайт https://www.autohotkey.com/ и скачиваем AHK версии 1.1
Устанавливаем и на этом все.

Далее создаем папку проекта, допустим “AHK”, открываем в ней VSC.
Открываем терминал и вписываем сначала: 
pip install ahk
Затем:
pip install "ahk[binary]"
```py
from ahk import AHK

ahk = AHK()

ahk.mouse_move(x=500,y=100,speed=7,blocking=True)
ahk.mouse_move(x=1028,y=64,speed=7,blocking=True)
#input()
ahk.click()
print(ahk.mouse_position)
```
from ahk import AHK: Эта строка импортирует класс AHK из библиотеки "ahk". Она готовит ваш Python-скрипт для использования функциональности AutoHotkey.

ahk = AHK(): В этой строке создается экземпляр класса AHK, который вы будете использовать для взаимодействия с AutoHotkey. Это инициализирует среду AutoHotkey.

ahk.mouse_move(x=100, y=100, blocking=True): Эта строка перемещает указатель мыши на экране к координатам (100, 100). Аргумент blocking=True означает, что код будет ждать завершения движения мыши, прежде чем перейдет к следующей строке.

ahk.mouse_move(x=300, y=300, speed=10, blocking=True): Эта строка перемещает указатель мыши на экране к координатам (300, 300). Аргумент speed=10 устанавливает скорость движения мыши (значение 10 означает быстрое движение). Аргумент blocking=True означает ожидание завершения движения мыши перед продолжением выполнения кода.

print(ahk.mouse_position): Эта строка выводит текущие координаты указателя мыши на экране. ahk.mouse_position - это атрибут объекта ahk, который хранит текущие координаты мыши.

Таким образом, этот код использует библиотеку "ahk" для перемещения указателя мыши по заданным координатам на экране и вывода текущих координат мыши.

```py
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
```
import os: Этот оператор импортирует модуль os, который позволяет выполнять системные команды, такие как os.system.

print(f'{os.system("taskkill /im autohotkey.exe")}'): В этой строке выполняется команда os.system("taskkill /im autohotkey.exe"). Она используется для завершения процесса AutoHotkey (autohotkey.exe) при активации горячей клавиши. Результат выполнения команды (возвращаемый код) выводится с помощью функции print(). Команда taskkill используется для завершения процессов в Windows.

ahk.add_hotkey('#n', callback=my_callback): В этой строке создается горячая клавиша с помощью ahk.add_hotkey(). Горячая клавиша указана как #n, что означает, что она будет активирована при одновременном нажатии клавиши Win (Windows) и клавиши N. Когда эта горячая клавиша будет активирована, будет вызвана функция my_callback.

ahk.start_hotkeys(): Эта строка запускает обработку горячих клавиш. Благодаря этой строке, горячая клавиша #n будет активироваться и выполнять функцию my_callback при ее нажатии.

ahk.block_forever(): Эта строка запускает бесконечный цикл, который предотвращает завершение программы. Она используется, чтобы программа продолжала работать, ожидая активации горячей клавиши, и чтобы не завершала выполнение после ее активации.
