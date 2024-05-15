# Множество — это составной тип данных, представляющий собой
# несколько значений (элементов множества) под одним именем. Этот
# тип называется set.
mammals = {'cat','dog','fox','elephant'}
empty = set() 

mammals_and_numbers = {'cat', 5,'dog', 3,'fox', 12,'elephant', 4,' ',}
print(mammals_and_numbers)

my_set = {'a', 'b', 'c'}
n = len(my_set) # => 3

my_set = {'a', 'b', 'c'}
print(my_set)

new_elem = 'e'
my_set.add(new_elem)
print(my_set)

new_list = [1,2,3,'1',2,'3','15',15,'2','1',1,3]
my_set = set(new_list)
print(my_set)

set_1 = {1, 2, 3}
set_2 = {4, 5, 1, 6}
set_1.update(set_2)
print(set_1, set_2)

a = set("hello")
print(a) # {'e', 'l', 'h', 'o'}

a = set("hello")
a.update("world")
print(a) # {'o', 'd', 'w', 'h', 'r', 'l', 'e'}