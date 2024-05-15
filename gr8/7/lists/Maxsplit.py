# У метода split есть еще некоторые приятные возможности. У него дополнительный аргумент maxsplit.
# С его помощью можно не просто разбить строку по разделителю и превратить ее в список, но еще и
# указать, сколько раз считать разделители с начала строки.
a = '1,2,3, Ёлочка гори'
a = a.split(',',maxsplit=3)
print(a)

name, lastname, *buy = 'Betty Botter bought a bit of butter'.split(maxsplit=2)
print(name, lastname, buy, sep='\n')

