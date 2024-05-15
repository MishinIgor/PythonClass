# Что такое факториал? Это последовательное умножение. !5 = 5*4*3*2*1 = 120

def factor(n):
    if n >= 2:
        return n*factor(n-1)
    if n == 1:
        return n
 