my_set1 = {'a1', 'b1', 'c1','d1','e','f'}
my_set3 = {'a1','b1','c1'}
my_set2 = {'a2', 'b2', 'c2','d2','e','f'}

union = my_set1.union(my_set2)
union = my_set1 | my_set2
print(union)

intersection = my_set1.intersection(my_set2)
intersection = my_set1 & my_set2
print(intersection)

diff = my_set1.difference(my_set2)
diff = my_set1 - my_set2
diff2 = my_set1 - my_set3
print(diff,diff2)

symm_diff = my_set1 ^ my_set2
symm_diff = my_set1.symmetric_difference(my_set2)
print(symm_diff)

print(union.difference(intersection))
