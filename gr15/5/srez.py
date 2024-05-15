a = 'Если я не пойду в школу, значит я школу прогуляю.'
c = list(a.split())
print(*c)
t = a[:15]
print(t)
t = int(input('Введите начало: '))
b = int(input('Введите конец: '))
print(a[t:b])