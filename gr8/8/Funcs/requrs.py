#Напишите функцию вычисления факториала числа. !5 = 5*4*3*2*1
def fact(n):
    if n > 1:
        return n*fact(n-1)
    if n <= 1:
        return 1

print(fact(fact(fact(3))))
