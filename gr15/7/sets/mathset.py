my_set1 = {'a1', 'b1', 'c1','a','b'}
my_set2 = {'a2', 'b2', 'c2','a','b'}

union = my_set1.union(my_set2)
print(union)
union = my_set1 | my_set2
print(union)

intersection = my_set1.intersection(my_set2)
print(intersection)
intersection = my_set1 & my_set2
print(intersection)

diff = my_set1.difference(my_set2)
print(diff)
diff = my_set1 - my_set2
print(diff)

symm_diff = my_set1 ^ my_set2
print(symm_diff)
symm_diff = my_set1.symmetric_difference(my_set2)
print(symm_diff)