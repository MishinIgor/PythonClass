#Вводятся числа через пробел. Вывести отдельно те которые делятся на 2, на 3 и те которые делятся на 2 и на 3. Также вывести оставшиеся отдельно.

a = list(input('Введите числа через пробел: ').split())
na2 = []
na3 = []
na6 = []
musor = []
for i in a:
    num = int(i)
    if num % 6 == 0:
        na6.append(num)
    elif num % 2 == 0:
        na2.append(num)
    elif num % 3 == 0:
        na3.append(num)
    else:
        musor.append(num)
print(f'Числа делятся на 2: {na2}')
print(f'Числа делятся на 3: {na3}')
print(f'Числа делятся на 2 и 3: {na6}')
print(f'Числа не делятся на 2 и 3: {musor}')