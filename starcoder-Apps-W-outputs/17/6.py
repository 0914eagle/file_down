
from queue import deque
from sys import stdin

input = stdin.readline

n = int(input())
a = list(map(int, input().split()))

out = []
g = [[] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if a[i] >= 1 and a[j] >= 1:
            g[i].append(j)
            g[j].append(i)
            a[i] -= 1
            a[j] -= 1
            out.append((i + 1, j + 1))

if any(a):
    print('NO')
else:
    print('YES', max(len(g[i]) for i in range(n)))
    for u, v in out:
        print(u, v)
