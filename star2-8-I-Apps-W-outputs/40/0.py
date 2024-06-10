
from sys import stdin
from collections import defaultdict

n, m = map(int, stdin.readline().split())

a = defaultdict(int)
b = defaultdict(int)

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    a[x] += 1
    b[y] += 1

for x in a:
    if a[x] == m:
        print("YES")
        break
else:
    for y in b:
        if b[y] == m:
            print("YES")
            break
    else:
        print("NO")

