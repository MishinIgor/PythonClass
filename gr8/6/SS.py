#напишите программу которая будет переводить число из 10ого вида в любую систему счиления до 10тичной.
a = int(input('Введите число: '))
ss = int(input('Введите номер системы: '))
chislo = ''
while a:
    ostatok = a % ss
    a = a // ss
    chislo = str(ostatok)+chislo # chislo = 01 ostatok = 0 => 001
print(f'{int(chislo,ss)} в системе {ss} будет {chislo}')
    