
import sys
from collections import deque

def main():
    N, M, K = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(N)]
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
        if pos == end_pos:
            print(days)
            return
        if pos in visited:
            continue
        visited.add(pos)
        i, j = pos
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] != '#':
                if grid[ni][nj] == '.':
                    cost = 1
                elif grid[ni][nj] == 'F':
                    cost = 2
                elif grid[ni][nj] == 'M':
                    cost = 3
                else:
                    continue
                if stamina >= cost:
                    queue.append(((ni, nj), days, stamina - cost))
                else:
                    queue.append(((ni, nj), days + 1, K - cost))
    print(-1)

if __name__ == '__main__':
    main()

