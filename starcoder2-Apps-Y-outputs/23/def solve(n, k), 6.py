
import sys

def solve(n, k):
    return n * k - n + 1

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    print(solve(n, k))

