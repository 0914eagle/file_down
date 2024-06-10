
from collections import deque

def bfs(R, C, maze, start, end):
    queue = deque([start])
    visited = set([start])
    dist = {start: 0}
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            
            if (nx, ny) in visited:
                continue
            
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                return dist[(x, y)] + 1
            
            if maze[nx][ny] == "#":
                continue
            
            queue.append((nx, ny))
            visited.add((nx, ny))
            dist[(nx, ny)] = dist[(x, y)] + 1
            
    return "IMPOSSIBLE"


R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if maze[i][j] == "J":
            start = (i, j)
            
for i in range(R):
    for j in range(C):
        if maze[i][j] == ".":
            end = (i, j)
            
print(bfs(R, C, maze, start, end))

