#Игра в однорукого бандита. Вводится кол. денег. Если хватает денег начинается игра. Если денег мало, то вывод "Вали отсюда за деньгами!"
#Попытка стоит 300, если проиграл предлагает сыграть ещё раз если хватает денег.
#Победить можно если 1) совпадёт все 3 числа, и тогда на баланс поступит 2500. 2) если совпадёт 2 числа на баланс попадёт 250.
#При победе повторной игры не предлагается. Выводится баланс. 
import random

balans = int(input('Введите кол. средств: '))
dsp = ['🥐','🍞','🥖','🍔','🍕','🥪','🥙','🌮','🌯']

while balans >= 300:
    zn1 = random.randrange(1,len(dsp))
    zn2 = random.randrange(1,len(dsp))
    zn3 = random.randrange(1,len(dsp))
    print(f'<*{dsp[zn1-1]}*><*{dsp[zn2-1]}*><*{dsp[zn3-1]}*>')
    if zn1 == zn2 == zn3:
        balans = balans-300+2500
        print(f'😍🤑😍Ваш баланс: {balans}😍🤑😍')
        vibor = input('Хотите сыграть ещё?(введите + для продолжения): ')
        if vibor == '+':
            continue
        else:
            break
    elif zn1 == zn2 or zn1 == zn3 or zn2==zn3:
        balans = balans-300+250
        print(f'😰😥😰Ваш баланс: {balans}😰😥😰')
        vibor = input('Хотите сыграть ещё?(введите + для продолжения): ')
        if vibor == '+':
            continue
        else:
            break
    else:
        balans = balans - 300
        vibor = input('☠️💀☠️Поражение! Хотите сыграть ещё?☠️💀☠️(введите + для продолжения): ')
        if vibor == '+':
            continue
        else:
            break
print('Ну и вали отсюда!')