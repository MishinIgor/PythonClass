#Напишите функцию которая переводит число из одной системы счисления в другую(до 16ой).
# int(стр(число),номер системы счисления) = десятичный вид 
def perevod(chislo,sist1,sist2): # chislo - то что зададут, sist1 - в какой системе зададут, sist2 - в какую перевести.
    chislo = int(str(chislo),sist1)
    slovarik = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    rezult = ''
    while chislo:
        ost = chislo % sist2
        chislo = chislo // sist2
        if ost >= 10:
            ost = slovarik[ost]
        rezult = str(ost) + rezult
    return rezult
print(perevod(61,10,16))
print(perevod('26',8,2))