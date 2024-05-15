# def - Задаём функцию, затем пишем name, и задаём в скобках аргументы
def squad(a,b):#Функция подсчёта площади
    kef = 2
    return kef*a*b # return - возвращает значение функции.
 
S1 = squad(5,6)
S2 = squad(3,7)
S3 = squad(S1,S2)
print(S1, S2, S3,S1+S2)