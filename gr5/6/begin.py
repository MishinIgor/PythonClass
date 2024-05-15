#range(start,stop,step); start - начало, stop - конец(без самого числа stop), step - шаг
#range(13,27,2) - начало в 13, конец в 27, шаг 2.
#range(13,27) - начало в 13, конец в 27, шаг 1
#range(27) - начало в 0, конец в 27, шаг 1.
#range(27,13,-2) - начало 27, конец 13, шаг -2
for i in range(13,27,2):
    print(i,end='🍞')
print()
for i in range(13,27):
    print(i,end='🍔')
print()
n = 3#int(input('Сколько чисел вывести? ->'))
for i in range(n+1):
    print(i,end='🌭')
print()
start = 5#int(input('С чего начать: '))
stop = 7#int(input('чем закончить: '))
step = 1#int(input('Какой шаг: '))
for i in range(start,stop+1,step):
    print(i,end='🍰')
print()
stroka = 'Какой-то текста ав страоке'
for i in stroka:
    if i == 'а':
        print("🥘",end='')
    else:
        print(i,end='')
print()
kakoitospisok = [['Сева', '6'], ['Сема', '1'],'Text', ['кокос', '6'], ['Тайсон', '75'],1,2,3,4,5]
for i in kakoitospisok:
    if type(i) == list:
        for j in i:
            print(j,end=' ')
    else:
        print(i,end=' ')
            
