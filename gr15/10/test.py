reglist = {1: {'ФИ:': 'Мишин Игорь', 'Возраст:': 32, 'Группа крови:': 3, 'Резус фактор:': '+', "Последняя сдача крови": '19','Ограничения:': ['Нет ограничений']},
           2: {'ФИ': "Сергей Манжосов", "Возраст:": 16, "Группа крови:": 2, "Резус фактор:": "+", "Последняя сдача крови": '-',"Ограничения:": ['Нет ограничений']}}
blacklist = {1: {'ФИ:': 'Мишин Владимир', 'Возраст:': 32, 'Группа крови:': 3, 'Резус фактор:': '+', "Последняя сдача крови": '75','Ограничения:': ['Нет ограничений']}}

name = 'Мишин Владимир'

index = 0
flagreg = False
for key,value in reglist.items():
    if name in value.values():
        print(True)
        index = key
        flagreg = True
        print('Вы можете подать заявку')
        break
for key,value in blacklist.items():
    if name in value.values():
        print(True)
        index = key
        flagreg = True
        print('Вы не можете подать заявку из за ограничений')
        break
if flagreg == False:
    print('Вам необходимо пройти регистрацию')