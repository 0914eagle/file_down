
import sys

def solve(C, N, vertices):
    pass

if __name__ == '__main__':
    C = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    vertices = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().strip().split())
        vertices.append((x, y))
    M, placements = solve(C, N, vertices)
    print(M)
    for x in placements:
        print(x)

