
from collections import deque

R, C = map(int, input().split())
maze = [input() for _ in range(R)]

def bfs(r, c):
    queue = deque([(r, c, 0)])
    visited = set()
    while queue:
        r, c, d = queue.popleft()
        if maze[r][c] == 'F':
            return d
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, d+1))

for r in range(R):
    for c in range(C):
        if maze[r][c] == 'J':
            result = bfs(r, c)
            if result is not None:
                print(result)
            else:
                print("IMPOSSIBLE")
            break
    else:
        continue
    break

