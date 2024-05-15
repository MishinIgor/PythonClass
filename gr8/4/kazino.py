# Играем в однорукого бандита.
# Вводится баланс. Если баланса хватает на игру то начинается игра. Если не хватает то выводится "Вали за деньгами!"
# Если попытка не удачная и хватает баланса на вторую игру, предлагается повторить 1 раз. Попытка стоит 300
# Если человек выиграл, выводится баланс. Без предложения повторить.
# Правила: генерируется рандомно 3 числа. Если совпало 2, то баланс пополняется на 250(300 за попытку не возвращаются)
#Если совпало 3 из 3 то баланс поплняется на 2500(за попытку не возвр.)

import random

balans = int(input('Введите баланс: '))

if balans >= 300:
    z1 = random.randrange(1,11) # задаём рандомное число от 1 до 11(11 не входит)
    z2 = random.randrange(1,11)
    z3 = random.randrange(1,11)
    print(f'🐵{z1}🙈{z2}🙉{z3}')
    if z1==z2==z3:
        print(f'Вы выиграли! {balans-300+2500}')
    elif z1==z2 or z1==z3 or z2==z3:
        print(f'Вы выиграли! {balans-300+250}')
    else:
        balans = balans - 300
        if balans >= 300:
            vibor = input('Хотите сыграть ещё? Введите + или -')
            if vibor == '+':
                z1 = random.randrange(1,11) # задаём рандомное число от 1 до 11(11 не входит)
                z2 = random.randrange(1,11)
                z3 = random.randrange(1,11)
                print(f'🐵{z1}🙈{z2}🙉{z3}')
                if z1==z2==z3:
                    print(f'Вы выиграли! {balans-300+2500}')
                elif z1==z2 or z1==z3 or z2==z3:
                    print(f'Вы выиграли! {balans-300+250}')
            else:
                print(f'Ваш баланс: {balans}')
        else:
            print('Ты проиграл! Вали за деньгами!')
else:
    print('Вали за деньгами!')