#range(start,stop,step). start - начало, stop - конец(не входит в перчень значений), step - шаг
#range(15,25,2) - начало в 15, конец в 25, шаг 2
#range(15,25) - тоже, что выше но шаг = 1.
#range(25) - конец в 25, начало в 0, шаг = 1.
#range(25,15,-2) - начало в 25, конец в 15, шаг 2(но в обратную сторону)
for i in range(15,26,2):
    print(i,end='🍞')
print()
for i in range(15,25):
    print(i,end='🥪')
print()
n = 12#int(input('Введите до какого числа вывод включительно: '))
for i in range(n+1):
    print(i,end='🍔')
print()
for i in range(125,25,-5):
    print(i,end='🍕')
print()
kakayatostroka = 'Какая-то строка да и только строка'

for i in kakayatostroka:
    if i == 'а' or i == 'д':
        print('💥',end='')
    else:
        print(i,end='')
print()
spisok = [['Котик', 'НеКотик', '2'],1, ['Собачка', 'НеСобачка', '3'], ['Черепаха', 'НеЧерепаха', '4'], ['Хлеб', 'Игорь', '12']] # Основной список с информацией
for i in spisok:
    if type(i) == list:
        for j in i:
            print(j,end='🥓')
    else:
        print(i,end='🍰')