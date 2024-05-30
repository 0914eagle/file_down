
import sys

def solve(x, a, b):
    if a-b <= x:
        return "safe"
    elif a-b <= x+1:
        return "delicious"
    else:
        return "dangerous"

x, a, b = map(int, sys.stdin.readline().split())
print(solve(x, a, b))

