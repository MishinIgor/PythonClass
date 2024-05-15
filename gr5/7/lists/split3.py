a = 'Я конечно люблю вопросы, но прежде чем задать задумайтесь, нет ли уже у вас ответа.'
a = a.split(maxsplit=2)
print(a)
name, lastname, *buy = 'Betty Botter bought a bit of butter'.split(maxsplit=2)
print(name, lastname, buy, sep='\n')