
from collections import deque

def magic_maze(H, W, C_h, C_w, D_h, D_w, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def is_valid_move(x, y):
        return 0 <= x < H and 0 <= y < W and maze[x][y] == '..'
    
    def min_magic_moves():
        queue = deque([(C_h-1, C_w-1, 0)])
        visited = set()
        
        while queue:
            x, y, moves = queue.popleft()
            
            if x == D_h-1 and y == D_w-1:
                return moves
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, moves))
                    visited.add((new_x, new_y))
            
            for i in range(-2, 3):
                for j in range(-2, 3):
                    new_x, new_y = x + i, y + j
                    if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                        queue.append((new_x, new_y, moves+1))
                        visited.add((new_x, new_y))
        
        return -1

    return min_magic_moves()

# Input parsing
H, W = map(int, input().split())
C_h, C_w = map(int, input().split())
D_h, D_w = map(int, input().split())
maze = [input() for _ in range(H)]

print(magic_maze(H, W, C_h, C_w, D_h, D_w, maze))
```
