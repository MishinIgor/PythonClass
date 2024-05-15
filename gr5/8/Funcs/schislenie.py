#Напишите функцию перевода числа из одной системы в другую(до 16ичной).
def perevod(chislo,sist1,sist2): # chislo - заданное число в системе счисления sist1, для перевода в sist2
    chislo = int(chislo,sist1) # Получаем десятичный вид числа
    rezult = ''
    slovarik = {10: 'A',11: 'B',12: 'C',13: 'D',14: 'E',15: 'F'}
    while chislo:
        ost = chislo % sist2
        if ost > 10:
            ost = slovarik[ost]
        chislo = chislo // sist2
        rezult = str(ost) + rezult
    return rezult
print(perevod('1723',8,2)) #11 1101 0011
print(perevod('1723',8,16))
def kvadratiki(a):
    j = 0
    for i in a:
        a[j] = i**2
        j += 1
    return a
c = kvadratiki([1,2,3,4,5,6,7,8,9,10,11,12,13])
print(c)