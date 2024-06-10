
from collections import deque

def solve():
    N, M, K = map(int, input().split())
    grid = [input() for _ in range(N)]
    start_pos = (0, 0)
    end_pos = (0, 0)
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start_pos = (i, j)
            elif grid[i][j] == 'G':
                end_pos = (i, j)
    queue = deque([(start_pos, 0, K)])
    visited = set()
    while queue:
        pos, days, stamina = queue.popleft()
        i, j = pos
        if pos == end_pos:
            return days
        if pos in visited or grid[i][j] == '#':
            continue
        visited.add(pos)
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if grid[ni][nj] == '.':
                    queue.append(((ni, nj), days + 1, stamina - 1))
                elif grid[ni][nj] == 'F':
                    queue.append(((ni, nj), days + 1, stamina - 2))
                elif grid[ni][nj] == 'M':
                    queue.append(((ni, nj), days + 1, stamina - 3))
        if stamina > 0:
            queue.append((pos, days + 1, K))
    return -1

print(solve())

