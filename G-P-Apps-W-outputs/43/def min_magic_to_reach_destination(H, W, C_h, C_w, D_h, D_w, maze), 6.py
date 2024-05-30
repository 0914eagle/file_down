
from collections import deque

def min_magic_to_reach_destination(H, W, C_h, C_w, D_h, D_w, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False for _ in range(W)] for _ in range(H)]
    
    queue = deque([(C_h-1, C_w-1, 0)])
    visited[C_h-1][C_w-1] = True
    
    while queue:
        current_row, current_col, magic_count = queue.popleft()
        
        if current_row == D_h-1 and current_col == D_w-1:
            return magic_count
        
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            
            if 0 <= new_row < H and 0 <= new_col < W and not visited[new_row][new_col] and maze[new_row][new_col] == '.':
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, magic_count))
        
        for i in range(-2, 3):
            for j in range(-2, 3):
                new_row, new_col = current_row + i, current_col + j
                
                if 0 <= new_row < H and 0 <= new_col < W and not visited[new_row][new_col] and maze[new_row][new_col] == '.':
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, magic_count + 1))
    
    return -1

# Read input
H, W = map(int, input().split())
C_h, C_w = map(int, input().split())
D_h, D_w = map(int, input().split())
maze = [input() for _ in range(H)]

# Call the function and print the result
print(min_magic_to_reach_destination(H, W, C_h, C_w, D_h, D_w, maze))
```
