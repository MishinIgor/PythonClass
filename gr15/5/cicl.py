#Вводится числа через пробел. Вывести отдельно все числа которые делятся на 2 и те котоыре делятся на 3. Если они делятся на 2 и на 3, вывести их в отдельно.

a = list(input('Вводите числа через пробел: ').split())
na2=[]
na3=[]
na6=[]
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
print(f'Делятся на 2: {na2}')
print(f'Делятся на 3: {na3}')
print(f'Делятся на 2 и на 3: {na6}')
print(f'Не делятся на 2 или 3: {musor}')

