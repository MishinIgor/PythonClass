chelovek = {'Ограничения:': []}
ogranichen = ['Нет ограничений','Гепатит А', "Гепатит Б", "Спид"]
for i in range(1,len(ogranichen)):
        print(f'🍰 {i} - {ogranichen[i]}')
otvet = input('Введите через пробел номера ограничений(если у вас их нет, введите 0):').split()
chelovek['Ограничения:'] += otvet
print(chelovek)