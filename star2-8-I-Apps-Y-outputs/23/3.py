
[SOL]
from bisect import bisect_left
s = input()
q = int(input())

l, r, c = 0, 0, 0

ans = []
for i in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        l, r = t[1] - 1, t[2]
        s = s[:l] + r + s[l + 1:]
    else:
        l, r = t[1] - 1, t[2]
        sub = sorted(set(s[l:r + 1]))
        ans.append(bisect_left(sub, r + 1) - bisect_left(sub, l))

for i in ans:
    print(i)

[/SOL]

