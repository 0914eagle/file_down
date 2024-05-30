
from collections import deque

def min_magic_moves(H, W, C_h, C_w, D_h, D_w, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False for _ in range(W)] for _ in range(H)]
    
    queue = deque([(C_h - 1, C_w - 1, 0)])
    visited[C_h - 1][C_w - 1] = True
    
    while queue:
        r, c, moves = queue.popleft()
        
        if r == D_h - 1 and c == D_w - 1:
            return moves
        
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < H and 0 <= new_c < W and not visited[new_r][new_c] and maze[new_r][new_c] == '.':
                visited[new_r][new_c] = True
                queue.append((new_r, new_c, moves))
        
        for i in range(max(0, r - 2), min(H, r + 3)):
            for j in range(max(0, c - 2), min(W, c + 3)):
                if not visited[i][j] and maze[i][j] == '.':
                    visited[i][j] = True
                    queue.append((i, j, moves + 1))
    
    return -1

# Input
H, W = map(int, input().split())
C_h, C_w = map(int, input().split())
D_h, D_w = map(int, input().split())
maze = [input() for _ in range(H)]

# Output
print(min_magic_moves(H, W, C_h, C_w, D_h, D_w, maze))
```
