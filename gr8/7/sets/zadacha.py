#Вводятся числа через пробел. Выведите все уникальные числа(без повторений)
a = list(input('Вводите числа через пробел: ').split())
a = set(a)
a = list(a)
print(a)

