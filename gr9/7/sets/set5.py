# Объединение двух множеств
# включает в себя все элементы,
# которые есть хотя бы в одном из
# них. Для этой операции существует
# метод union:

my_set1 = {1,2,3,4}
my_set2 = {3,8,9,1}

#union = my_set1.union(my_set2)
union = my_set1 | my_set2
print(union)