cnt = 0
f = open('9.csv')
for s in f:
    a = list(map(int,s.split(';')))
    a.sort()
    if a[0] + a[1] > a[2]:
        cnt+=1
print(cnt)