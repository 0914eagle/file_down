
s = input()
l = s.index('^')
r = l

n = 0
left_weight = 0
right_weight = 0
for i in range(0, len(s)):
    if s[i] != '=':
        n += int(s[i])
        if i < l:
            left_weight += int(s[i]) * (l - i)
        else:
            right_weight += int(s[i]) * (i - l)

if left_weight == right_weight:
    print('balance')
elif left_weight > right_weight:
    print('left')
else:
    print('right')

