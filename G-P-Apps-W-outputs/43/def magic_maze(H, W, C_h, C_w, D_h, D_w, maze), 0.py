
from collections import deque

def magic_maze(H, W, C_h, C_w, D_h, D_w, maze):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    magic_count = [[float('inf')] * W for _ in range(H)]
    magic_count[C_h-1][C_w-1] = 0
    
    queue = deque([(C_h-1, C_w-1, 0)])
    
    while queue:
        i, j, count = queue.popleft()
        
        if i == D_h-1 and j == D_w-1:
            return count
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < H and 0 <= nj < W and maze[ni][nj] == '.':
                if count < magic_count[ni][nj]:
                    magic_count[ni][nj] = count
                    queue.append((ni, nj, count))
        
        for si in range(max(0, i-2), min(H, i+3)):
            for sj in range(max(0, j-2), min(W, j+3)):
                if maze[si][sj] == '.' and count + 1 < magic_count[si][sj]:
                    magic_count[si][sj] = count + 1
                    queue.append((si, sj, count + 1))
    
    return -1

# Read input
H, W = map(int, input().split())
C_h, C_w = map(int, input().split())
D_h, D_w = map(int, input().split())
maze = [list(input().strip()) for _ in range(H)]

result = magic_maze(H, W, C_h, C_w, D_h, D_w, maze)
print(result)
```
