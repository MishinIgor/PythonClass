#Напишите программу которая будет собирать данные о клиентах банка крови. Человек может сдавать кровь не чаще чем раз в месяц, и не может иметь некоторые заболевания, и быть старше 65 лет и младше 12.
#1) Добавлять нового клиента.
#   Должно быть отображено: 
#   ФИ, кол. полных лет, группа крови, резус фактор, наличие ограничений, кол. дней с последней сдачи крови(если сдаёте в первый раз поставьте -).
#2) Принимать заявку на сдачу крови
#3) Удалять клиента из базы и добавлять в blacklist.
#4) Отображать запрос на клиента.
#5) Вносить изменения по клиентам.
#6) Выводить blacklist, и список ограничений.

blacklist = {1: {'ФИ:': 'Мишин Владимир', 'Возраст:': 32, 'Группа крови:': 3, 'Резус фактор:': '+', "Последняя сдача крови:": '75','Ограничения:': ['Нет ограничений']}}
reglist = {1: {'ФИ:': 'Мишин Игорь', 'Возраст:': 32, 'Группа крови:': 3, 'Резус фактор:': '+', "Последняя сдача крови:": '19','Ограничения:': ['Нет ограничений']},
           2: {'ФИ': "Сергей Манжосов", "Возраст:": 16, "Группа крови:": 2, "Резус фактор:": "+", "Последняя сдача крови:": '-',"Ограничения:": ['Нет ограничений']}}
ogranichen = ['Нет ограничений','Гипотит А', "Гипотит Б", "Спид"]

def inzapros():
    spisok = ['1 - зарегистрироваться', "2 - Заявка на сдачу крови", 
              "3 - Вывести список ограничений", "4 - Вывести список зарегистрированных", 
              "5 - Вывести blacklist", "6 - Редактировать анкету"]
    for i in spisok:
        print(i)

def reg():
    global ogranichen
    chelovek = {
        'ФИ:': input('Введите ФИ: '),
        "Возраст:": int(input('Введите кол. полных лет: ')),
        "Группа крови:": int(input('Введите группу крови: ')),
        "Резус фактор:": input('Введите резус фактор(+ или -): '),
        "Последняя сдача крови:": input('Введите кол. дней с последней сдачи крови(если впервые сдаёте, поставьте -): ')
    }
    chelovek['Ограничения:'] = []
    for i in range(len(ogranichen)-1):
        print(f'😱 {i+1} - {ogranichen[i+1]}')
    while True:
        otvet = input('Введите номера ограничеий через пробел, которые у вас присутствуют(если ограничений нет, введите 0.): ').split()
        if len(otvet)>1 and otvet.count('0') >= 1 or len(otvet[0])>1:
            print('Вы ввели не корректные данные попробуйте снова')
        else:
            for i in otvet:
                chelovek['Ограничения:'].append(ogranichen[int(i)])
            break
    raspred(chelovek)
def agesuf(age):
    if age % 10 >= 5 or age % 10 == 0 or 10<age%100<15:
        return str(age) + " лет"
    elif age%10>1:
        return str(age) + " года"
    else:
        return str(age) + " год"

def vivod(spisok):
    for i,j in spisok.items():
        print(f'id{i}. ', end='')
        for key,value in j.items():
            if key == 'Возраст:':
                print(f'{key} {agesuf(value)}',end='; ')
            else:
                print(f'{key} {value}',end='; ')
        print()

def raspred(chelovek):
    global blacklist, reglist, ogranichen
    flag = True
    for i in chelovek['Ограничения:']:
        if i in ogranichen[1:]:
            flag = False
            break
    if chelovek['Возраст:']>65 or chelovek['Возраст:']<12 or flag == False:
        blacklist[len(blacklist.keys())+1] = chelovek
    else:
        reglist[len(blacklist.keys())+1] = chelovek

def zayavka(name):
    flagreg = False
    for key,value in reglist.items():
        if name in value.values():
            print(True)
            flagreg = True
            print('Вы можете подать заявку 🤩')
            break
    for key,value in blacklist.items():
        if name in value.values():
            print(True)
            flagreg = True
            print('Вы не можете подать заявку из за ограничений ☠️')
            break
    if flagreg == False:
        print('Вам необходимо пройти регистрацию😭')

def redaktor(name):
    flagreg = False
    spisok = {}
    for key,value in reglist.items():
        if name in value.values():
            print(True)
            index = key
            spisok = reglist
            flagreg = True
            break
    for key,value in blacklist.items():
        if name in value.values():
            print(True)
            index = key
            spisok = blacklist
            flagreg = True
            break
    if flagreg == False:
        print('Вам необходимо пройти регистрацию😭')
    else:
        while True:
            print(f'Хотите отредактировать это: {spisok[index]} ?')
            key = input('Какой пункт редактировать(введите название): ')
            spisok[index][key+':'] = input('Введите новое значение: ')
            povtor = input('Хотите отредактировать ещё что=то? Введите + или -:')
            if povtor != '+':
                break

while True:
    inzapros()
    zapros = input('Введите подходящий номер: ')
    if zapros == "0":
        break
    elif zapros == '1':
        reg()
    elif zapros == '2':
        zayavka(input('Введите ФИ: '))
    elif zapros == "3":
        print(*ogranichen[1:])
    elif zapros == '4':
        vivod(reglist)
    elif zapros == '5':
        vivod(blacklist)
    elif zapros == '6':
        redaktor(input('Введите ФИ: '))
    