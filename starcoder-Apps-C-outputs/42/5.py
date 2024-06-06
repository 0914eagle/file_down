
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

# 1
from math import sqrt

b = []
for i in range(n):
    b.append(0)

for i in range(n):
    for j in range(i):
        if b[i] == 0 and b[j] == 0:
            b[i] = int(sqrt(a[i][j]))
            b[j] = a[i][j] // b[i]

for i in range(n):
    print(b[i], end=' ')
