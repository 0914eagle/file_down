
from sys import stdin
n = int(stdin.readline())
if n == 1:
    print(0)
    print(1)
    print(0)
    print(1)
else:
    print(n)
    print(*([1] + [0] * (n - 1)))
    print(n - 1)
    print(*([1] + [0] * (n - 2) + [-1]))

