#range(start,stop,step), start - начало, stop - окончание, step - шаг.
#range(15) - по дефолту шаг 1, начало в 0 и конец в 15(без самой 15); range(7,20) - Начало в 7, конец в 20(без самого 20), шаг 1;
#range(15,26,5) - начало 15, конец 26, шаг 5.
#range(510,400,-10) - начало в 510, конец в 400, шаг - 10
n = 4#int(input('Эй, пс, сколько мне нужно вывести? ->'))
for shtougodno in range(n+1):
    print(shtougodno,end='🍔') # sep - шаг между элементами print , end - действие после завершения print
print()
for i in range(15,21):
    print(i,end='🍕')
print()
for i in range(10,23,2):
    print('👽',end='🌭')
print()
for i in range(600,500,-20): #цикл в обратную сторону от 500 до 400 с шагом 20
    print(i,end='🤯')
print()
a = 'Я люблю свою работу, если эта работа связанна с группой №15'
b = [1,2,'Терапия',['С наступающей', "Пасхой"],True]
schet = 0
for i in a:
    schet += 1
    print(i,end='')
print()
for i in b:
    print(b,end=' ')