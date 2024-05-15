x = 5
y = 10
z = 15
A = x<0 # 0
B = y>0 # 1
C = z>5 # 1

if (A or B) and C: # or -> +  ; and -> * ; (A+B)*C
    print('ЭТО РАБОТАЕТ! О БОЖЕ! РАБОТАЕТ!')
else:
    print('Кто-то хлеба мало ел')