# Технологии выросли на столько, что хлебу стал доступен возраст.
# Но его нужно обязательно внести в реестр хлеба
# Реестр должен вывести {TypeHleb}, вам {age} лет/года/Год

TypeHleb = 'Бородинский'
age = int(input('Введите Ваш возраст товарищ хлеб: '))
if age<0:
    print('Удачно родиться, но сейчас введи норальный возраст, пока мечом по буханке не дали')
else:
    if age % 10 >= 5 or age % 10 == 0 or 10<age%100<15:#пропишем условие для "лет"
        print(f'{TypeHleb}, Вам {age} лет')
    elif age%10>1:#пропишем условие для "года"
        print(f'{TypeHleb}, Вам {age} года')
    else:
        print(f'{TypeHleb}, Вам {age} год')