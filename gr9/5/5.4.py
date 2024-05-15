#Вводятся числа через пробел. Выведите отдельно чётные и нечётные числа
a = list(input('Введите числа через пробел: ').split())
chet = []
nechet = []
for i in a:
    if int(i) % 2 == 0:
        chet.append(int(i))
    else:
        nechet.append(int(i))
chet.sort()
nechet.sort()
print(f'Список чётных: {chet}')
print(f'Список нечётных: {nechet}')