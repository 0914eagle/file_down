
s = input()
s = list(s)
s = set(s)
s = list(s)
if len(s) == len(set(s)):
    print('YES')
else:
    print('NO')
