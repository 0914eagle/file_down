

import math

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
b = []
for i in range(n):
    for j in range(n):
        if i != j:
            b.append(a[i][j])
c = []
for i in range(n):
    c.append(math.sqrt(b[i]))
for i in range(n):
    for j in range(n):
        if i == j:
            c[i] = 0
d = []
for i in range(n):
    d.append(math.sqrt(c[i]))
e = []
for i in range(n):
    if d[i] not in e:
        e.append(d[i])
print(e)

