
from collections import deque

def min_magic_moves(H, W, C_h, C_w, D_h, D_w, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False for _ in range(W)] for _ in range(H)]
    magic_used = [[float('inf') for _ in range(W)] for _ in range(H)]
    
    queue = deque([(C_h-1, C_w-1, 0)])  # Start from the magician's position
    magic_used[C_h-1][C_w-1] = 0
    visited[C_h-1][C_w-1] = True
    
    # BFS traversal
    while queue:
        current_row, current_col, current_magic_used = queue.popleft()
        
        # Check if reached the destination
        if current_row == D_h-1 and current_col == D_w-1:
            return current_magic_used
        
        # Move A: Walk to adjacent road squares
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            
            if 0 <= new_row < H and 0 <= new_col < W and maze[new_row][new_col] == '.':
                if not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, current_magic_used))
        
        # Move B: Use magic to warp within 5x5 area
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                new_row, new_col = current_row + dr, current_col + dc
                
                if 0 <= new_row < H and 0 <= new_col < W and maze[new_row][new_col] == '.':
                    if current_magic_used + 1 < magic_used[new_row][new_col]:
                        magic_used[new_row][new_col] = current_magic_used + 1
                        queue.append((new_row, new_col, current_magic_used + 1))

    return -1  # If destination cannot be reached

# Read input
H, W = map(int, input().split())
C_h, C_w = map(int, input().split())
D_h, D_w = map(int, input().split())
maze = [input() for _ in range(H)]

# Call the function to calculate the minimum magic moves
result = min_magic_moves(H, W, C_h, C_w, D_h, D_w, maze)
print(result)
```
