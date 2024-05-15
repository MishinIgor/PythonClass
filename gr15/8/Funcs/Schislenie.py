#Функция которая может переводить из одной системы счисления в другую(до 10ичной)
def sistNinM(chislo,sist1,sist2): # chislo в системе sist1, переводим в sist2
    chislo = int(str(chislo),sist1)
    rezult = ''
    alf = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    while chislo:
        ost = str(chislo % sist2)
        chislo = chislo // sist2
        if int(ost) >= 10:
            ost = alf[int(ost)]
        rezult = ost+rezult
    return rezult
print(sistNinM('1111',2,8))
print(sistNinM('275',8,10))
print(sistNinM('254',8,2))
print(sistNinM('1023',10,16))