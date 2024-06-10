
from collections import deque
def solve(R, C, maze):
    def neighbors(r, c):
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= r + dr < R and 0 <= c + dc < C and maze[r + dr][c + dc] != '#':
                yield r + dr, c + dc
    fire = deque()
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'F':
                fire.append((r, c))
    joe = None
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'J':
                joe = (r, c)
    visited = set()
    queue = deque([(joe, 0)])
    while queue:
        (r, c), t = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if r == 0 or c == 0 or r == R - 1 or c == C - 1:
            return t
        for r2, c2 in neighbors(r, c):
            queue.append(((r2, c2), t + 1))
        for r2, c2 in neighbors(r, c):
            if maze[r2][c2] != 'F':
                maze[r2][c2] = 'F'
                fire.append((r2, c2))
    while fire:
        r, c = fire.popleft()
        for r2, c2 in neighbors(r, c):
            if maze[r2][c2] != 'F':
                maze[r2][c2] = 'F'
                fire.append((r2, c2))
    return 'IMPOSSIBLE'
R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]
print(solve(R, C, maze))

