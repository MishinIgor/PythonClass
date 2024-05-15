a = input('a=')
c = input('c=')
znak = input('Введите знак(+,-,*,/,**,//,%):')
# a = 5 ; c = 7; znak = + ; вывод-> '5+7' -> eval('5+7') -> 5+7 -> 12
if c == '0' and (znak == '/' or znak == '//' or znak == '%'):
    print('У вас выпало: 🧠')
else:
    print(eval(a+znak+c))