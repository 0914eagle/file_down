
from collections import deque

def magic_maze_solver(H, W, C_h, C_w, D_h, D_w, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Initialize a 2D array to store the minimum number of magic uses to reach each square
    magic_uses = [[-1] * W for _ in range(H)]
    
    # Initialize a deque for BFS
    queue = deque([(C_h-1, C_w-1)])
    magic_uses[C_h-1][C_w-1] = 0
    
    while queue:
        current_i, current_j = queue.popleft()
        current_magic_uses = magic_uses[current_i][current_j]
        
        for di, dj in directions:
            new_i, new_j = current_i + di, current_j + dj
            
            if 0 <= new_i < H and 0 <= new_j < W and maze[new_i][new_j] == '.':
                if magic_uses[new_i][new_j] == -1 or current_magic_uses < magic_uses[new_i][new_j]:
                    magic_uses[new_i][new_j] = current_magic_uses
                    queue.appendleft((new_i, new_j))
        
        for di in range(-2, 3):
            for dj in range(-2, 3):
                new_i, new_j = current_i + di, current_j + dj
                
                if 0 <= new_i < H and 0 <= new_j < W and maze[new_i][new_j] == '.':
                    if magic_uses[new_i][new_j] == -1 or current_magic_uses + 1 < magic_uses[new_i][new_j]:
                        magic_uses[new_i][new_j] = current_magic_uses + 1
                        queue.append((new_i, new_j))
    
    return magic_uses[D_h-1][D_w-1]

# Read input
H, W = map(int, input().split())
C_h, C_w = map(int, input().split())
D_h, D_w = map(int, input().split())
maze = [input() for _ in range(H)]

# Call the function and print the result
result = magic_maze_solver(H, W, C_h, C_w, D_h, D_w, maze)
print(result)
```
