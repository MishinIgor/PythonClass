# Множество — это составной тип данных, представляющий собой
# несколько значений (элементов множества) под одним именем. Этот
# тип называется set.

mammals = {'cat','dog','fox','elephant'}
print(mammals)
empty = set()
print(empty)
mammals_and_numbers = {'cat', 5,'dog', 3,'fox', 12,'elephant', 4, True}
print(mammals_and_numbers)

# Итак, у множеств есть три ключевые особенности:
#  Порядок элементов в множестве не определён.
#  Элементы множеств — строки и/или числа.
#  Множество не может содержать одинаковых элементов.