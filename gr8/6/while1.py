#Вводятся строки пока не будет введено "стоп". Определите длинну наименьшей и наибольшей строчки.
a = ''
maxs = 0
mins = 1000000
while a != 'стоп':
    a = input('Введите строку: ')
    maxs = max(maxs,len(a))
    if a != 'стоп':
        mins = min(mins,len(a))
print(f'Самая большая длинна: {maxs}; Самая короткая длинна: {mins}')