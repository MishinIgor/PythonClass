#Если выпало 2 из 3, то на баланс поступит 250(300 не вернут). Если выпало 3 из 3, то на баланс поступит 2500(300 не вернут)
import random
variant = ['🥐','🍞','🥖','🥨','🥞','🌮','🥪','🥙','🌯','🍔','🌭']

balans = int(input('Введите баланс: '))

if balans >= 300: #300 - цена билета для игры
    z1 = random.choices(variant)
    z2 = random.choices(variant)
    z3 = random.choices(variant)
    print(z1,z2,z3)
    if z1==z2 and z1==z3:
        print(f'🤩😝🤩Вы выиграли 🤩😝🤩 Ваш баланс {balans-300+2500} 🤩😝🤩')
    elif z1==z2 or z1==z3 or z2==z3:
        print(f'👿💩😡Вы выиграли 👿💩😡 Ваш баланс {balans-300+250} 👿💩😡')
    else:
        print(f'😭😭😭Вы ПРОИГРАЛИ 😭😭😭 Ваш баланс {balans-300} 😭😭😭')
    
