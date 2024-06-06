
s = input()
l = len(s)
a = 0
b = 0
for i in range(l-1):
    if s[i] != '=':
        a += int(s[i])*(i+1)
for i in range(l-1):
    if s[i+1] != '=':
        b += int(s[i+1])*(i+1)
if a == b:
    print('balance')
elif a > b:
    print('left')
else:
    print('right')
