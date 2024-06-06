
s = input()
s = '^' + s + '='
c = [0] * len(s)
for i in range(1, len(s)):
    c[i] = c[i - 1] + 1 if s[i] == '=' else 0

s = s.replace('=', '')
c = c[:-1]
a, b = c[s.index('^')], c[-1] - c[s.index('^')]
if a < b:
    print('left')
elif a > b:
    print('right')
else:
    print('balance')

