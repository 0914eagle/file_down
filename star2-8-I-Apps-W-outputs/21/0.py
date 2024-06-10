
from sys import stdin
n = int(stdin.readline())
p = list(map(int, stdin.readline().split()))
a = 1
for i in range(n):
    a = a * (100 - p[i]) // 100
print((a - 1) % 998244353)

