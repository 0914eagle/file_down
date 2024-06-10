
import sys
from collections import deque

def bfs(maze, start, end, walls, fire, time):
    queue = deque([start])
    visited = set([start])
    while queue:
        cur_row, cur_col, cur_time = queue.popleft()
        if (cur_row, cur_col) == end:
            return cur_time
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_col = cur_row + dr, cur_col + dc
            if 0 <= next_row < R and 0 <= next_col < C and (next_row, next_col) not in visited and (next_row, next_col) not in walls and (next_row, next_col) not in fire:
                queue.append((next_row, next_col, cur_time + 1))
                visited.add((next_row, next_col))
    return -1

R, C = map(int, input().split())
maze = [input() for _ in range(R)]

walls, fire, joe = set(), set(), None
for r in range(R):
    for c in range(C):
        if maze[r][c] == '#':
            walls.add((r, c))
        elif maze[r][c] == 'F':
            fire.add((r, c))
        elif maze[r][c] == 'J':
            joe = (r, c)

end = (-1, -1)
for r in range(R):
    for c in range(C):
        if (r, c) not in walls:
            end = (r, c)
            break
    if end != (-1, -1):
        break

time = bfs(maze, joe, end, walls, fire, 0)
if time == -1:
    print('IMPOSSIBLE')
else:
    print(time)


