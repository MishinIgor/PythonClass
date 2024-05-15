stud = {
    'имя': 'Иван',
    'возраст': 20,
    'курс': 'Python',
    'группа': 'A'
}

semestr = {
    "рейтинг": 4.5,
    "Стипендию": 3000,
    "общежитие": "Комната 305",
    "курс": "JS"
}
a = stud.get('рейтинг')
print(a)
stud.update(semestr)
print(stud)

for i in stud.values():
    print(i,end='<Value>')
print()
for i in stud.keys():
    print(i,end='<Keys>')
print()
for i in stud.items():
    print(i,end='<Items>')
print()
for i,j in stud.items():
    print(i,j,sep='<-Key   Value->')
print()
