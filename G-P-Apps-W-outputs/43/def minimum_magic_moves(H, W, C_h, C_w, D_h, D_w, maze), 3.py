
from collections import deque

def minimum_magic_moves(H, W, C_h, C_w, D_h, D_w, maze):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    
    INF = float('inf')
    
    visited = [[INF] * W for _ in range(H)]
    visited[C_h][C_w] = 0
    
    q = deque([(C_h, C_w)])
    
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < H and 0 <= nc < W and maze[nr][nc] == '.' and visited[nr][nc] == INF:
                visited[nr][nc] = visited[r][c]
                q.appendleft((nr, nc))
    
    for r in range(max(0, D_h - 2), min(H, D_h + 3)):
        for c in range(max(0, D_w - 2), min(W, D_w + 3)):
            if visited[r][c] == INF:
                visited[r][c] = visited[D_h-1][D_w-1] + 1
                q.appendleft((r, c))
    
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < H and 0 <= nc < W and visited[nr][nc] == INF:
                visited[nr][nc] = visited[r][c] + 1
                q.appendleft((nr, nc))
    
    if visited[D_h-1][D_w-1] == INF:
        return -1
    else:
        return visited[D_h-1][D_w-1]

# Input processing
H, W = map(int, input().split())
C_h, C_w = map(int, input().split())
D_h, D_w = map(int, input().split())
maze = [input() for _ in range(H)]

# Call the function and print the result
print(minimum_magic_moves(H, W, C_h, C_w, D_h, D_w, maze))
```
