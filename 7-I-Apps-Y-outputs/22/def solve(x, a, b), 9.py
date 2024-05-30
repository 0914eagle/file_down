
import sys

def solve(x, a, b):
    if b-a <= x:
        return "delicious"
    elif b-a <= x+1:
        return "safe"
    else:
        return "dangerous"

x, a, b = map(int, sys.stdin.readline().split())
print(solve(x, a, b))

