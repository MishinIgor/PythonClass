#Напишите программу которая будет собирать данные о клиентах банка крови. Человек может сдавать кровь не чаще чем раз в месяц, и не может иметь некоторые заболевания, и быть старше 65 лет и младше 12.
#1) Добавлять нового клиента.
#   Должно быть отображено: 
#   ФИ, кол. полных лет, группа крови, резус фактор, наличие ограничений, кол. дней с последней сдачи крови(если сдаёте в первый раз поставьте -).
#2) Принимать заявку на сдачу крови
#3) Удалять клиента из базы и добавлять в blacklist.
#4) Отображать запрос на клиента.
#5) Вносить изменения по клиентам.
#6) Выводить blacklist, список зарегистрированных, и список ограничений.

reglist = {1: {'ФИ:': 'Мишин Игорь', 'Возраст:': 32, 'Группа крови:': 3, 'Резус фактор:': '+', "Последняя сдача крови:": '19','Ограничения:': ['Нет ограничений']},
           2: {'ФИ:': "Сергей Манжосов", "Возраст:": 16, "Группа крови:": 2, "Резус фактор:": "+", "Последняя сдача крови:": '-1',"Ограничения:": ['Нет ограничений']},
           3: {'ФИ:': 'Егорова Ирина', 'Возраст:': 15, 'Группа крови:': 1, 'Резус фактор:': '+', 'Последняя сдача крови:': '-1', 'Ограничения:': ['Нет ограничений']},
           4: {'ФИ:': 'Владислав Еникеев', 'Возраст:': 15, 'Группа крови:': 2, 'Резус фактор:': '-', 'Последняя сдача крови:': '35', 'Ограничения:': ['Нет ограничений']}}
blacklist = {1: {'ФИ:': 'Трофимов Владимир', 'Возраст:': 66, 'Группа крови:': 3, 'Резус фактор:': '+', "Последняя сдача крови:": '75','Ограничения:': ['Нет ограничений']}}
listall = {1: {'ФИ:': 'Мишин Игорь', 'Возраст:': 32, 'Группа крови:': 3, 'Резус фактор:': '+', "Последняя сдача крови:": '19','Ограничения:': ['Нет ограничений']},
           2: {'ФИ:': "Сергей Манжосов", "Возраст:": 16, "Группа крови:": 2, "Резус фактор:": "+", "Последняя сдача крови:": '-1',"Ограничения:": ['Нет ограничений']},
           3: {'ФИ:': 'Егорова Ирина', 'Возраст:': 15, 'Группа крови:': 1, 'Резус фактор:': '+', 'Последняя сдача крови:': '-1', 'Ограничения:': ['Нет ограничений']},
           4: {'ФИ:': 'Владислав Еникеев', 'Возраст:': 15, 'Группа крови:': 2, 'Резус фактор:': '-', 'Последняя сдача крови:': '35', 'Ограничения:': ['Нет ограничений']}}
ogranichen = ['Нет ограничений','Гипотит А', "Гипотит Б", "Спид"]

def inzapros():
    spisok = ['1 - зарегистрироваться', "2 - Заявка на сдачу крови", 
              "3 - Вывести список ограничений", "4 - Вывести список зарегистрированных", 
              "5 - Вывести информацию о человеке", "6 - Редактировать анкету"]
    for i in spisok:
        print(i)

def reg():
    global ogranichen, listall
    chelovek = {
        'ФИ:': input('Введите ФИ: '),
        "Возраст:": int(input('Введите кол. полных лет: ')),
        "Группа крови:": int(input('Введите группу крови: ')),
        "Резус фактор:": input('Введите резус фактор(+ или -): '),
        "Последняя сдача крови:": input('Введите кол. дней с последней сдачи крови(если впервые сдаёте, поставьте -1): ')
    }
    chelovek['Ограничения:'] = []
    for i in range(1,len(ogranichen)):
        print(f'🍞 {i} {ogranichen[i]}')
    otvet = input('Введите номера ограничений через пробел, которые у вас присуствуют(если ограничений нет, введие 0.): ').split()
    for i in otvet:
        chelovek['Ограничения:'].append(ogranichen[int(i)])
    raspred(chelovek)

def sufics(age):
    if age % 10 >= 5 or age % 10 == 0 or 10<age%100<15:
        return str(age)+' лет'
    elif age%10>1:#пропишем условие для "года"
        return str(age)+' года'
    else:
        return str(age)+' год'

def outinfo(spisok):
    for i,j in spisok.items(): # (1, 'ФИ:': 'Мишин Игорь', 'Возраст:': 32, ...)
        print(f'id{i}. ', end='')
        for key,value in j.items():
            if key == 'Возраст:':
                print(f'{key} {sufics(value)}',end='; ')
            elif key == 'Последняя сдача крови:' and value == "-1":
                print(f'{key} Не сдавал кровь',end='; ')
            else:
                print(f'{key} {value}',end='; ')
        print() # id1. ФИ: Мишин Игорь; Возраст: 32 года; ...

def raspred(chelovek):
    global reglist, blacklist, ogranichen
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
    for key,value in reglist.items():
        if name in value.values():
            flagreg = True
            if int(value['Последняя сдача крови:']) > 30 or int(value['Последняя сдача крови:']) < 0:
                print('Вы можете сдать кровь и взять хлеба с мясом 🍔')
            else:
                print('Вы уже сдавали кровь, спасибо Вам, но нужно ещё подождать. 🍮⛔️')
            break
    else:
        for key,value in blacklist.items():
            if name in value.values():
                flagreg = True
                print('Вы не можете сдать кровь из за ограничений 🍮⛔️')
                break
    if flagreg == False:
        print('Вам необходимо зарегистрироваться и взять ☕️')

def edit(name):
    flagreg = False
    for key,value in reglist.items():
        if name in value.values():
            flagreg = True
            index = key
            mylist = reglist
            break
    else:
        for key,value in blacklist.items():
            if name in value.values():
                flagreg = True
                index = key
                mylist = blacklist
                break
    if flagreg == False:
        print('Вам необходимо зарегистрироваться и взять ☕️')
    else:
        print(f'Мы нашли анкету: {mylist[index]}')
        zapros = input('Введите пункт для изменений: ')
        mylist[index][zapros+':'] = input('Введите данные для обновления: ')
def outnameinfo(name):
    flagreg = False
    for key,value in reglist.items():
        if name in value.values():
            flagreg = True
            index = key
            mylist = reglist
            break
    else:
        for key,value in blacklist.items():
            if name in value.values():
                flagreg = True
                index = key
                mylist = blacklist
                break
    if flagreg == False:
        print('Такой анкеты нет 😢')
    else:
        print(f'Мы нашли анкету: {mylist[index]}')
        
while True:
    inzapros()
    zapros = input('Введите подходящий номер: ')
    if zapros == "0":
        break
    elif zapros == "1":
        reg()
    elif zapros == '2':
        application(input('Введите ФИ: '))
    elif zapros == '3':
        print(*ogranichen[1:])
    elif zapros == "4":
        print('Лист тех кто может сдавать: ')
        outinfo(reglist)
        print('Blacklist: ')
        outinfo(blacklist)
    elif zapros == "5":
        outnameinfo(input('Введите ФИ: '))
    elif zapros == '6':
        edit(input('Введите ФИ: '))







