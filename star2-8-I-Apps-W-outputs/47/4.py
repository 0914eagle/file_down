
import itertools
import sys

def solve(n, a, b, c, d):
    return sum(1 for i in range(n) for j in range(n) for k in range(n) for l in range(n) if (i + j + k + l) % n == (a + b + c + d) % n)

if __name__ == "__main__":
    n, a, b, c, d = map(int, sys.stdin.read().split())
    print(solve(n, a, b, c, d))

