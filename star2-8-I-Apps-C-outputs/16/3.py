
import sys
n = int(sys.stdin.readline())
if n == 1:
    print(0)
    print(1)
    print(0)
    print(1)
else:
    print(n)
    print(' '.join([str(i) for i in [0]*n + [1]]))
    print(1)
    print(0, 1)

