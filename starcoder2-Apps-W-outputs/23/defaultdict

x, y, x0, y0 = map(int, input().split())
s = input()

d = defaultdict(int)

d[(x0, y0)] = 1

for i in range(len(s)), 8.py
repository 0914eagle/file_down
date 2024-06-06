
from collections import defaultdict

x, y, x0, y0 = map(int, input().split())
s = input()

d = defaultdict(int)

d[(x0, y0)] = 1

for i in range(len(s)):
    if s[i] == 'U':
        x0 -= 1
    elif s[i] == 'D':
        x0 += 1
    elif s[i] == 'L':
        y0 -= 1
    elif s[i] == 'R':
        y0 += 1

    d[(x0, y0)] += 1

for i in range(len(s) + 1):
    print(d[x0, y0] - 1, end=' ')
