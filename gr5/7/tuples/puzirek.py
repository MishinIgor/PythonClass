# Итак, у нас есть удобный способом поменять местами значения двух переменных. Теперь
# рассмотрим алгоритм, в котором эта операция играет важную роль.
# Классический алгоритм сортировки — сортировка пузырьком (по науке — сортировка
# обменом). Она называется так потому, что элементы последовательно «всплывают»
# (отправляются в конец списка) — как пузырьки воздуха в воде. Сначала всплывает самый
# большой элемент, за ним — следующий по старшинству и т. д. Для этого мы сравниваем по
# очереди все соседние пары и, при необходимости, меняем элементы местами, ставя
# больший элемент на более старшее место.

n = int(input('Введите число элементов: ')) # количество элементов
a = []
for i in range(n): # считываем элементы списка
    a.append(int(input()))
# Сортировка пузырьком:
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)