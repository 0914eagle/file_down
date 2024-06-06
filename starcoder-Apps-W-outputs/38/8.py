
a = list(input())
b = list(input())
if a == b:
    print('YES')
    exit()

a.sort()
b.sort()

if a == b:
    print('YES')
else:
    print('NO')
