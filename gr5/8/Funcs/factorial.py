# Напишите функцию вычисляющую факториал. !5 = 5*4*3*2*1
def fact(n):
    if n>1:
        return n*fact(n-1)
    elif n<=1:
        return 1
print(fact(5))
print(fact(6))
print(fact(7))