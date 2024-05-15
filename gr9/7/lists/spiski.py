arr = []
for x in range(6):
    if x % 2 == 0:
        arr.append('четное')
    else:
        arr.append('нечетное')
print(arr)

arr = ['четное' if x % 2 == 0 else 'нечетное' for x in range(6)]
print(arr)
print(', '.join(arr))