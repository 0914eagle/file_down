

s = input()

i = 0

cnt = 0

while i < len(s):
    if s[i] == '^':
        break
    elif s[i] == '=':
        i += 1
    else:
        cnt += int(s[i])
        i += 1

i += 1

while i < len(s):
    if s[i] == '^':
        break
    elif s[i] == '=':
        i += 1
    else:
        cnt -= int(s[i])
        i += 1

if cnt > 0:
    print('left')
elif cnt < 0:
    print('right')
else:
    print('balance')
