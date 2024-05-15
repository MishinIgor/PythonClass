cards = [('7', 'пик'), ('Д', 'треф')]

value, suit = cards[0]

print('Достоинство карты:', value)
print('Масть карты:', suit)

a, b = 1, 2 # теперь a == 1 and b == 2
a, b = b, a # теперь a == 2 and b == 1

a, b, с = 3, 2, 1 # a = 3, b = 2, c = 1
b, a, c = с, a, b # b = 1, a = 3, c = 2
print(b, c, a) # b - 1, c - 2, a - 3

# 1,1,2,3,5,8,13,21...
n = int(input())
f1, f2 = 0, 1
for i in range(n):
    print(f2)
    f1, f2 = f2, f1 + f2