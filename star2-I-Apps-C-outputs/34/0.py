
import sys

def euclid_steps(a, b):
    steps = 0
    while b != 0:
        a, b = b, a % b
        steps += 1
    return steps

n = int(sys.stdin.readline())

if n == 1:
    print(0)
    print(1)
    print(0)
    print(1)
else:
    print(n)
    print(' '.join([str(1 if i == n else 0) for i in range(n + 1)]))
    print(1)
    print(0, 1)

