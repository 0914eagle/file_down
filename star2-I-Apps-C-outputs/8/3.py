
from math import sqrt
def solve(n, x, y, r):
    pass

n = int(input())
x = [0] * n
y = [0] * n
r = [0] * n
for i in range(n):
    x[i], y[i], r[i] = map(float, input().split())

print(solve(n, x, y, r))

