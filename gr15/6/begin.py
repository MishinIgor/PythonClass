#Списки и условные конструкции.
#Вводится числа через пробел. Если чисел больше 10, то определить сколько чисел двусоставных. Иначе, сколько чисел состоят из 
#одного разряда.

a = list(input('->').split())
rez = []
print(a)
if len(a)>10:
    for i in a:
        if (len(i)==2 and int(i)>0) or (int(i)<0 and len(i)==3): 
            rez.append(i)
else:
    for i in a:
        if (len(i)==1 and int(i)>0) or (int(i)<0 and len(i)==2): 
            rez.append(i)
print(f'Нужные числа: {rez} в количестве: {len(rez)} из {len(a)}')