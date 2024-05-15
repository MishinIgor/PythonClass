a = []
id = 0
i = 0
while True:
    zapros = int(input('Введите номер действия: 1) Добавить животное 2) удалить животное 3) вывести на экран имеющихся 4) завершить работу ->'))
    if zapros == 4:
        break
    elif zapros == 1:
        id += 1
        name = input('Введите имя питомца: ')
        owner = input('Введите фамилию хозяина: ')
        age = input('Введите возраст хозяина: ')
        a.append('id: '+str(id)+' name: '+name+' owner: '+owner+' age: '+age)
    elif zapros == 3:
        print(a)
    elif zapros == 2:
        a.pop(int(input('Введите id для удаления: '))-1)