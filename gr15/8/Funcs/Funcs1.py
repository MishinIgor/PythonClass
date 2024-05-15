def summa(a,b,c):
    return a+b+c
def kvadratspiska(a):
    j=0
    for i in a:
        a[j]= i**2
        j+=1
    return a
def V(a,b,c):
    return a*b*c
def S(a,b):
    return a*b
a = 5
b = 7
c = 9
print(S(S(a,b),c))
print(V(a,b,c))