#Вводятся числа через пробел. Выведите какие числа делятся на 3, на 5, на 3 и 5 и не делятся ни на 3 ни на 5.
a = list(input('Введите числа через пробел: ').split())
na3 = []
na5 = []
na15 = []
korzina = []

for i in a:
    n = int(i)
    if n % 15 == 0:
        na15.append(n)
    elif n % 3 == 0:
        na3.append(n)
    elif n % 5 == 0:
        na5.append(n)
    else:
        korzina.append(n)
print(f'Числа делятся на 3: {na3}')
print(f'Числа делятся на 5: {na5}')
print(f'Числа делятся на 15: {na15}')
print(f'Числа неделюхи: {korzina}')