my_set1 = set('privet')
my_set2 = set('proshai')

print(my_set1,my_set2) #Даны 2 множества

union = my_set1.union(my_set2)
union = my_set1 | my_set2
print(union) # Сумма множеств

intersection = my_set1.intersection(my_set2)
intersection = my_set1 & my_set2
print(intersection) #Пересечение множеств

diff = my_set1.difference(my_set2)
print(diff) # Разность первое минус второе
diff = my_set2 - my_set1
print(diff) #второе минус первое

symm_diff = my_set1 ^ my_set2
symm_diff = my_set1.symmetric_difference(my_set2)
print(symm_diff)