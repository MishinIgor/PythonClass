#print([i * j for i in range(1,3) for j in range(3,7)])

a = [int(x) for x in '976 929 289 809 7677'.split()]
evil, good = [int(x) for x in '666 777'.split()]
print(evil, good, sep='\n')
print(a)
a = [int(x) for x in input('Введите числа через пробел: ').split()]
print(a)