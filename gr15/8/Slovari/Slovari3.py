student = {
    'имя': 'Иван',
    'возраст': 20,
    'курс': ['Python','JS','C#'],
    'группа': 'A'
}
student_update = {
    'имя': 'Иван',
    'возраст': 23,
    'курс': ['Python','JS','C#','Git','Math'],
    "Талон-Столовая": 5,
    "Комната общежития": 1
}
if student.get('Яблоко в обед') == None:
    student["Яблоко в обед"] = 3
else:
    print(student)
print(f'Всё исправили:{student}')
print("Выводим ключи: ",end='')
for i in student.keys():
    print(i,end=',')
print("Выводим значения: ")
for i in student.values():
    print(i,end=',')
print("Выводим ключи и значения: ")
for i in student.items():
    print(i,end=';')
print()
for key, value in student.items():
    print(value,key,sep='<-Value : Key->')