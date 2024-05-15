a = []
for i in range(20):
    if i%2 == 0:
        a.append(i)
    elif i%3 == 0:
        a.append(i)
    else:
        a.append('Не делится на 2 и 3')
print(a)