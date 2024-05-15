my_set = {'a', 'b', 'c'}
new_elem = 'e'
my_set.add(new_elem)
print(my_set)

set_1 = {1, 2, 3}
set_2 = {4, 5, 1, 6}
set_1.update(set_2)
print(set_1, set_2)

a = set("hello my world") 
print(a) # {' ', 'w', 'r', 'o', 'e', 'y', 'd', 'h', 'l', 'm'}

a = set("hello")
a.update("world")
print(a) # {'o', 'd', 'w', 'h', 'r', 'l', 'e'}