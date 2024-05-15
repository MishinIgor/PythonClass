my_set = {'a', 'b', 'c'}
my_set.discard('a') # Удалён
my_set.discard('hello') # Не удалён, ошибки нет
my_set.remove('b') # Удалён
print(my_set) # В множестве остался один элемент 'c'
my_set.remove('world') # Не удалён, ошибка KeyError