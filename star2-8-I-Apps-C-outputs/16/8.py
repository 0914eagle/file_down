
import sys

def euclid_steps(a, b):
    if b == 0:
        return 0
    else:
        return 1 + euclid_steps(b, a % b)

n = int(sys.stdin.readline())

if n == 1:
    print("0\n0 1")
    print("0\n1")
elif n == 2:
    print("2\n-1 0 1")
    print("1\n0 1")
else:
    print("-1")

