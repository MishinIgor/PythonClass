#Игра в однорукого бандита. Вводится кол. денег. Если хватает денег начинается игра. Если денег мало, то вывод "Вали отсюда за деньгами!"
#Попытка стоит 300, если проиграл предлагает сыграть ещё раз если хватает денег.
#Победить можно если 1) совпадёт все 3 числа, и тогда на баланс поступит 2500. 2) если совпадёт 2 числа на баланс попадёт 250.
#При победе повторной игры не предлагается. Выводится баланс. 
import random

balans = int(input('Введите кол. средств: '))
dsp = ['🥐','🍞','🥖','🍔','🍕','🥪','🥙','🌮','🌯']

if balans >= 300:
    zn1 = random.randrange(1,len(dsp))
    zn2 = random.randrange(1,len(dsp))
    zn3 = random.randrange(1,len(dsp))
    print(f'<*{dsp[zn1-1]}*><*{dsp[zn2-1]}*><*{dsp[zn3-1]}*>')
    if zn1 == zn2 == zn3:
        print(f'Ваш баланс: {balans-300+2500}')
    elif zn1 == zn2 or zn1 == zn3 or zn2==zn3:
        print(f'Ваш баланс: {balans-300+250}')
    else: #Все 3 различные
        vibor = input('Если хотите сыграть ещё раз введите "+": ')
        balans -= 300
        if vibor == '+' and balans>=300:
            zn1 = random.randrange(1,10)
            zn2 = random.randrange(1,10)
            zn3 = random.randrange(1,10)
            print(f'<*{dsp[zn1-1]}*><*{dsp[zn2-1]}*><*{dsp[zn3-1]}*>')
            if zn1 == zn2 == zn3:
                print(f'Ваш баланс: {balans-300+2500}')
            elif zn1 == zn2 or zn1 == zn3 or zn2==zn3:
                print(f'Ваш баланс: {balans-300+250}')
            else: #Все 3 различные
                print(f'Ваш баланс: {balans-300}')
        else:
            print(f'Ну и вали отсюда неудачник!')
else:
    print('Вали отсюда за деньгами')
