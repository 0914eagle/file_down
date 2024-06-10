
import math
from sys import stdin
input = stdin.readline
n, k1, k2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if k1 + k2 >= n:
    print(0)
else:
    a.sort()
    b.sort()
    for _ in range(k1):
        a[0] += 1
        a[-1] -= 1
    for _ in range(k2):
        b[0] += 1
        b[-1] -= 1
    a.sort()
    b.sort()
    e = 0
    for i in range(n):
        e += (a[i] - b[i])**2
    print(e)

