def fact(n):# !5 = 5*4*3*2*1
    if n>1:
        return n*fact(n-1)
    if n <= 1:
        return 1
# Алгоритм вычисления значения функции F(n), где n  — целое неотрицательное число, задан следующими соотношениями:
# F(0) = 0; F(n) -> F(0) = y => y = 0, n = 0
# F(n) = F(n / 2), если n > 0 и при этом чётно;
# F(n) = 1 + F(n − 1), если n нечётно.
# Сколько существует таких чисел n, что 1 ≤ n ≤ 1000 и F(n)  =  3?
def F(n):
    if n == 0:
        return 0
    elif n>0 and n%2==0:
        return F(n/2)
    elif n%2 == 1:
        return 1+F(n-1)
schetchik = 0
for n in range(1,1001):
    if F(n) == 3:
        schetchik += 1
print(schetchik)