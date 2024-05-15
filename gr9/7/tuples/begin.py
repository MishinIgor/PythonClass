card = ('7', '8', '9')
print(card)
a = ()
print(a)
t = (18,)
print(t)
print(len(card), card[0], card + t)

(1, 2) == (1, 3) # False
(1, 2) < (1, 3) # True
(1, 2) < (5,) # True
('7', 'червей') < ('7', 'треф') # False
(1, 2) < ('7', 'пик') # А вот так сравнивать нельзя: 