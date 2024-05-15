student = {
    'имя': 'Иван',
    'возраст': "Данные нужно уточнить",
    'курс': 'Python',
    'группа': 'A'
}
nagrada = {
    "стипендия": 3000,
    "курс": "JS",
    "группа": "А+",
    "Комната общаги": "№350"
}
student.update(nagrada)
print(student)
a = student.get('стипендия')
print(a)
t = 'задолженность'
c = student.get(t)
print(c)
if student.get(t) == None:
    print(f'ключа {t} нет')
at = student.pop('возраст')
print(at,student)

for i in student.items():
    print(i,end=" ")
print()
for i,j in student.items():
    print(i,j,sep="<-Key | Value->")
for i in student.keys():
    print(i,end=' ')
print()
for i in student.values():
    print(i,end=' ')
print()