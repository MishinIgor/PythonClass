def S(a,b):
    return a*b
def kvadratiki(a):
    j = 0
    for i in a:
        a[j] = i**2
        j+=1
    return a
def hello1():
    print('Hello world')
    z=3
def hello2(a):
    print(f'Hello world, and {a}')
    hello1()
    y = 5
def FX():
    global x
    x = str(x)+'Изменение'
def XF():
    x = 12
    x = str(x)+'Ну тоже изменение'
z = 17
hello2('Cat')
hello2(z)
hello2([3,5,1])
hello2({1:"Привет", 2: "Пока"})
x = 12
FX()
XF()
print(XF())

S1 = S(5,6)
S2 = S(13,18)
S3 = S(S1,S2)
print(S1,S2,S3,S(12,10))


a = [1,2,3,4,5,6,7,8,9]
print(kvadratiki(a))
print(kvadratiki([1,2,3,4,5,6,7,8,9]))
SN = S(int(input('a=')),int(input('b=')))
print(SN)