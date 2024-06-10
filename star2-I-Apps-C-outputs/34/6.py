
import sys
n = int(sys.stdin.readline())
if n == 1:
    print(0)
    print(1)
    print(0)
    print(1)
else:
    print(n)
    print(-1, end = " ")
    for i in range(n):
        print(0, end = " ")
    print()
    print(1)
    print(0, end = " ")
    for i in range(n):
        print(1, end = " ")
    print()

