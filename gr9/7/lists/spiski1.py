squares = [] #Создаём пустой список
for i in range(11):
    squares.append(i ** 2) #заоплняем внури цикла
print(squares)

t = [i ** 2 for i in range(10)] #тоже самое что и выше
print(t) 
