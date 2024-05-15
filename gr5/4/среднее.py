#Вводится 3 числа. Определите среднее.

a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))

mx = max(a,b,c)
mn = min(a,b,c)
sred = a+b+c-mx-mn
print(sred)