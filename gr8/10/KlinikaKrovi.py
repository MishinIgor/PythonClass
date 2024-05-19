#Напишите программу которая будет собирать данные о клиентах банка крови. 
# Человек может сдавать кровь не чаще чем раз в месяц, и не может иметь некоторые заболевания, и быть старше 65 лет и младше 12.
#1) Добавлять нового клиента.
#   Должно быть отображено: 
#   ФИ, кол. полных лет, группа крови, резус фактор, наличие ограничений, кол. дней с последней сдачи крови.
#2) Принимать заявку на сдачу крови
#3) Распределять клиентов добавляя в blacklist или reglist.
#4) Отображать запрос на клиента.
#5) Вносить изменения по клиентам.
#6) Выводить blacklist, список зарегистрированных, и список ограничений.

reglist = {1: {'ФИ:': 'Мишин Игорь', 'Возраст:': 32, 'Группа крови:': 3, 'Резус фактор:': '+', "Крайний забор крови:": 19,'Ограничения:': ['Нет ограничений']},
           2: {'ФИ:': "Сергей Манжосов", "Возраст:": 16, "Группа крови:": 2, "Резус фактор:": "+", "Крайний забор крови:": -1,"Ограничения:": ['Нет ограничений']},
           3: {'ФИ:': 'Егорова Ирина', 'Возраст:': 15, 'Группа крови:': 1, 'Резус фактор:': '+', 'Крайний забор крови:': -1, 'Ограничения:': ['Нет ограничений']},
           4: {'ФИ:': 'Владислав Еникеев', 'Возраст:': 15, 'Группа крови:': 2, 'Резус фактор:': '-', 'Крайний забор крови:': 35, 'Ограничения:': ['Нет ограничений']}}
blacklist = {1: {'ФИ:': 'Трофимов Владимир', 'Возраст:': 66, 'Группа крови:': 3, 'Резус фактор:': '+', 
                 "Последняя сдача крови:": '75','Ограничения:': ['Нет ограничений']}}
ogranichen = ['Нет ограничений','Гепатит А', "Гепатит Б", "Спид"]

def inzapros():
    spisok = ['1 - Зарегистрироваться', "2 - Заявка на сдачу крови", 
              "3 - Вывести список ограничений", "4 - Вывести список зарегистрированных", 
              "5 - Вывести информацию о человеке", "6 - Редактировать анкету"]
    for i in spisok:
        print(i)

def reg():
    global ogranichen
    chelovek = {
        "ФИ:": input('Введите ФИ: '),
        "Возраст:": int(input('Введите кол. полных лет: ')),
        "Группа крови": int(input('Введите группу крови: ')),
        "Резус фактор": input('Введите + или - для резус фактора: '),
        "Крайний забор крови:": int(input('Введите кол. дней с последнего забора крови(если вы не сдавали кровь, введите -1): '))
    }
    chelovek['Ограничения:'] = []
    for i in range(1,len(ogranichen)):
        print(f'🍰 {i} - {ogranichen[i]}')
    otvet = input('Введите через пробел номера ограничений(если у вас их нет, введите 0): ').split()
    for i in otvet:
        chelovek['Ограничения:'].append(ogranichen[int(i)])
    distrib(chelovek)

def outinfo(spisok):
    for id, chelovek in spisok.items(): # (1, {ФИ: Мишин Игорь ....}), (2, {ФИ: Придумкин Хаширам ...})
        print(f'id{id}: ', end='')
        for key,value in chelovek.items():
            if key == 'Возраст:':
                print(f'{key} {sufics(value)}', end=';')
            elif key == 'Крайний забор крови:' and value < 0:
                print(f'{key} забора крови небыло', end=';')
            else:
                print(f'{key} {value}', end=';')
        print()

def sufics(age):
    if age % 10 >= 5 or age % 10 == 0 or 10<age%100<15:#пропишем условие для "лет"
        return str(age)+' лет'
    elif age%10>1:#пропишем условие для "года"
        return str(age)+' года'
    else:
        return str(age)+' год'

def distrib(chelovek):
    global reglist, blacklist
    flag = True
    for i in chelovek['Ограничения:']:
        if i in ogranichen[1:]:
            flag = False
            break
    if chelovek['Возраст:']>65 or chelovek['Возраст:']<12 or flag == False:
        blacklist[len(blacklist.keys())+1] = chelovek
    else:
        reglist[len(reglist.keys())+1] = chelovek

def application(name):
    flagreg = False
    for id,chelovek in reglist.items():
        if name in chelovek.values():
            flagreg = True
            if int(chelovek["Крайний забор крови:"])>30 or int(chelovek["Крайний забор крови:"])<0:
                print('Вы можете сдать кровь и взять хлеба с мясом 🍔')
            else:
                print(f'Вы уже сдавали кровь, и вам нужно подождать {30-int(chelovek["Крайний забор крови:"])} дней 🌹')
            break
    else:
        for id,chelovek in blacklist.items():
            if name in chelovek.values():
                flagreg = True
                print(f'К сожалению вы не можете сдавать кровь из за ограничений возраста или болезни ⭐️')
                break
    if flagreg == False:
        print('Необходимо пройти регистрацию! 👧')

def nameinfo(name):
    flagreg = False
    for id,chelovek in reglist.items():
        if name in chelovek.values():
            flagreg = True
            key = id
            mylist = reglist
            break
    else:
        for id,chelovek in blacklist.items():
            if name in chelovek.values():
                flagreg = True
                key = id
                mylist = blacklist
                break
    if flagreg == False:
        print('Необходимо пройти регистрацию! 👧')
    else:
        print(f'Информация по анкете: {mylist[id]}')

def edit(name):
    flagreg = False
    for id,chelovek in reglist.items():
        if name in chelovek.values():
            flagreg = True
            key = id
            mylist = reglist
            break
    else:
        for id,chelovek in blacklist.items():
            if name in chelovek.values():
                flagreg = True
                key = id
                mylist = blacklist
                break
    if flagreg == False:
        print('Необходимо пройти регистрацию! 👧')
    else:
        print(f'Информация по анкете: {mylist[id]}')
        while True:
            key = input('Введите название поля: ')
            if key == 'Ограничения':
                for i in range(1,len(ogranichen)):
                    print(f'🍰 {i} - {ogranichen[i]}')
                otvet = input('Введите через пробел номера ограничений(если у вас их нет, введите 0): ').split()
                for i in otvet:
                    mylist[id]['Ограничения:'].append(ogranichen[int(i)])
                zapros = input('Если хотите продолжить редактирование введите +:')
                if zapros != '+':
                    break
                else:
                    continue
            value = input('Введите данные для обновления: ')
            mylist[id][key+':'] = value
            zapros = input('Если хотите продолжить редактирование введите +:')
            if zapros != '+':
                break
        #Прописать удаление и добавление в другой список.
while True:
    inzapros()
    zapros = input('Введите номер пункта: ')
    if zapros == '0':
        break
    elif zapros == '1':
        reg()
    elif zapros == '2':
        application(input('Введите имя: '))
    elif zapros == '4':
        print('reglist: ')
        outinfo(reglist)
        print('blacklist: ')
        outinfo(blacklist)
    elif zapros == '5':
        nameinfo(input('Введите ФИ: '))
    elif zapros == '6':
        edit(input('Введите ФИ: '))