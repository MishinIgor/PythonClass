# Ваня решил сходить в поход сам и сам собрать свою сумку через приложение "СобериСам"

trebovanie = {
    "Вода": 5,
    "Консервы": 3,
    "Палатка": 2,
    "Спички": 1,
    "Спальный мешок": 2,
    "Гитара": 1
}

rukzakvani = {}
rukzakpeti = {}
for i in trebovanie.keys():
    rukzakvani[i] = int(input(f'Введите количество {i}: '))
    rukzakpeti[i] = int(input(f'Введите количество {i}: '))
print("Содержимое рюкзака: ", rukzakvani)