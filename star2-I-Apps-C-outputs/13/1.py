
import sys
from collections import deque

def solve(grid, start, K):
    N, M = len(grid), len(grid[0])
    dist = [[float('inf')] * M for _ in range(N)]
    dist[start[0]][start[1]] = 0
    q = deque([start])
    while q:
        i, j = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] != '#' and dist[ni][nj] == float('inf'):
                cost = 1 if grid[ni][nj] == '.' else 2 if grid[ni][nj] == 'F' else 3
                if dist[i][j] + cost <= K:
                    dist[ni][nj] = dist[i][j] + cost
                    q.append((ni, nj))
                else:
                    dist[ni][nj] = dist[i][j] + K + 1 - cost
                    q.append((ni, nj))
    return dist[end[0]][end[1]] if dist[end[0]][end[1]] != float('inf') else -1

N, M, K = map(int, input().split())
grid = [input() for _ in range(N)]
start, end = None, None
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            end = (i, j)
print(solve(grid, start, K))

