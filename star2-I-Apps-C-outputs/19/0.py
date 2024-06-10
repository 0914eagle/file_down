
import sys

def solve(n, C, p, b, u):
    return 0

def main():
    n, C = map(int, sys.stdin.readline().split())
    p = [0] * n
    b = [0] * n
    u = [0] * n
    for i in range(n):
        p[i], b[i], u[i] = map(int, sys.stdin.readline().split())
    print(solve(n, C, p, b, u))

if __name__ == '__main__':
    main()

