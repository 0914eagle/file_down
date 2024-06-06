
# 4 8 11 12 14 16 17 20 21 22 25 27 29
s = input()
l = []
count = 0
for i in s:
    if count == 0:
        l.append(i)
        count = 1
    elif i == l[-1]:
        count += 1
    elif i != l[-1]:
        if count == 1:
            l.append(i)
        else:
            l.append(i)
            l.append(l[-1])
            count = 1

if len(l) % 3 == 0:
    print('YES')
else:
    print('NO')
