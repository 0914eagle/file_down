
import sys

def solve(D, N):
    if D == 0:
        return 100
    elif D == 1:
        return 100 * N
    elif D == 2:
        return 100 * (N + 1)
    else:
        return 0

if __name__ == '__main__':
    D, N = map(int, sys.stdin.readline().split())
    print(solve(D, N))

