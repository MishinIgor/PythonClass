# join же всегда принимает один аргумент — список слов, которые
# нужно склеить. Разделителем (точнее, «соединителем») служит та самая
# строка, чей метод join вызывается. Это может быть и пустая строка, и пробел,
# и символ новой строки, и что угодно ещё.

s = ['Тот', 'Кого', 'Нельзя', 'Называть']
print(''.join(s))
print(' '.join(s))
print('🥚'.join(s))
print('🧁'.join(s))
print(('🥚🧁'.join(s)).join(s))