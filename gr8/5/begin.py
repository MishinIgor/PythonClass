a = [1,2,3,4,5,6]
print(a)
a = list(range(1,15)) # range(a,c) - начать в а, закончить в c-1
print(a)
a = list(range(1,15,2)) # range(a,c,s) - начасть в a, закончить в с-1 с шагом s
print(a)
a = list(input('Введите значения через пробел: ').split())
b = list(input('Введите значения через запятую: ').split(','))
print(a,b)
a = [True, False, 5+6, 'Привет', 'Всё могу и не могу', [1,2,3,4,['Оп','Па']]]
print(a)