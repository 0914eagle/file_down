
s = input()
a = 0
b = 0
c = 0
for i in range(0, len(s)):
    if s[i] == 'a':
        a += 1
    elif s[i] == 'b':
        b += 1
    else:
        c += 1
if a == c or b == c:
    print('YES')
else:
    print('NO')
