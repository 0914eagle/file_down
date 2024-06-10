
import sys
import math

def solve(C, N, points):
    return 0

def main():
    C = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    points = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().strip().split())
        points.append((x, y))
    print(solve(C, N, points))

if __name__ == "__main__":
    main()

