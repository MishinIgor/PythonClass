# Разность двух множеств включает в
# себя все элементы, которые есть в
# первом множестве, но которых нет
# во втором:
my_set1 = {1,2,3,4}
my_set2 = {3,8,9,1}

diff = my_set1.difference(my_set2)
print(diff)

diff = my_set2.difference(my_set1)
print(diff)

# Симметрическая разность двух
# множеств включает в себя все
# элементы, которые есть только в
# одном из этих множеств:

symm_diff = my_set1 ^ my_set2

print(symm_diff)

symm_diff = my_set1.symmetric_difference(my_set2)

print(symm_diff)