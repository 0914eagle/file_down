
a = input()
b = ''
for i in a:
    if i not in b:
        b += i
if len(b) <= 2:
    print('YES')
else:
    print('NO')
