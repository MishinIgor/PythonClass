n, s = 10, 'hello'
# то же самое, что
n = 10
s = 'hello'

cards = [('7', 'пик'), ('Д', 'треф')]
value, suit = cards[0]

a, b = 1, 2 # теперь a == 1 and b == 2
a, b = b, a # теперь a == 2 and b == 1

# кручу-верчу
a, b, с = 3, 2, 1
b, a, c = с, a, b
print(b, c, a)