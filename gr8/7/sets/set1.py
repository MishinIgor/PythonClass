# Множество — это составной тип данных, представляющий собой
# несколько значений (элементов множества) под одним именем. Этот
# тип называется set.

mammals = {'cat','dog','fox','elephant'}
print(mammals)

empty = set()
empty.add(3)
empty.add(2)
empty.add(3)
print(empty)

print(len(mammals))

for i in mammals:
    print(i)

mam = 'dogs'
if mam in mammals:
    print('Элемент есть в множестве')
else:
    print('Элемента нет в множестве') 

set_1 = {1, 2, 3}
set_2 = {4, 5, 1, 6}
set_1.update(set_2)
print(set_1, set_2)

a = set("hello")
print(a) # {'e', 'l', 'h', 'o'}

even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
a = set(even_squares)
print(a)

my_set = set('Hello my World')
print(my_set)
my_set.discard('H') # Удалён
print(my_set)
my_set.discard('hello') # Не удалён, ошибки нет
print(my_set)
my_set.remove('e') # Удалён
print(my_set) # В множестве остался один элемент 'c'
#my_set.remove('world') # Не удалён, ошибка KeyError

print('до удаления:', my_set)
elem = my_set.pop()
print('удалённый элемент:', elem)
print('после удаления:', my_set)

my_set.clear()
print(my_set)