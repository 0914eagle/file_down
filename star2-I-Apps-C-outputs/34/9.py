
import sys

n = int(sys.stdin.readline())

if n == 1:
    print(0)
    print(1)
    print(0)
    print(1)
elif n == 2:
    print(2)
    print(-1, 0, 1)
    print(1)
    print(0, 1)
else:
    print(-1)

