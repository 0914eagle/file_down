
import sys

def solve(C, N, vertices):
    return 0

def main():
    C = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    vertices = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        vertices.append((x, y))
    print(solve(C, N, vertices))

if __name__ == '__main__':
    main()

