
#20/100
import sys

n = int(sys.stdin.readline())
x = []
y = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)
d = int(sys.stdin.readline())

s = 0
for i in range(n):
    for j in range(n):
        s += abs(x[i] - x[j]) + abs(y[i] - y[j])

print(s)
