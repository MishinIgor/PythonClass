#Вводится два числа. Если первое делится на второе или второе на первое то вывести "делится". Иначе вывести "не делится"

ch1 = int(input('Введите первое число: '))
ch2 = int(input('Введите второе число: '))

if ch1 % ch2 == 0 or ch2 % ch1 == 0:
    print('Делится')
else:
    print('не делится')