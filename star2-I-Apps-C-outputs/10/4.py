
import math

def solve(C, N, vertices):
    return 0

C = int(input())
N = int(input())
vertices = []
for i in range(N):
    x, y = map(int, input().split())
    vertices.append((x, y))

print(solve(C, N, vertices))

