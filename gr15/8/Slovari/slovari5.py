#Собираемся в поход. Есть список требований к походным принадлежностям(некий минимум для проживания).
#Мальчики самостоятельно собираются в поход. Необходимо проверить хватит ли им запасов.
trebovanie = {
    "Вода": 8,
    "Консервы": 5,
    "Макароны": 2,
    "Палатка": 1,
    "Спички": 1,
    "Гитара": 1
}
rukzakpeti = {}
for i in trebovanie.keys():
    rukzakpeti[i] = int(input(f"Введите сколько взять {i}: "))
proverka = {}

for i in trebovanie.keys():
    if trebovanie[i] > rukzakpeti[i]:
        raznost = trebovanie[i] - rukzakpeti[i]
        proverka[i] = "Нехватка на " +str(raznost)
if proverka == {}:
    print('Ребята к походу готовы!')
else:
    print(proverka)