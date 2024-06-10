
import sys

def solve(n, m, h, u, c):
    return 0

if __name__ == "__main__":
    n, m, h = map(int, sys.stdin.readline().split())
    u = list(map(int, sys.stdin.readline().split()))
    c = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    print(solve(n, m, h, u, c))

