
from collections import deque

def min_magic_moves(H, W, C_h, C_w, D_h, D_w, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def bfs():
        queue = deque([(C_h, C_w, 0)])
        visited = set([(C_h, C_w)])

        while queue:
            r, c, moves = queue.popleft()

            if r == D_h and c == D_w:
                return moves

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 1 <= nr <= H and 1 <= nc <= W and maze[nr-1][nc-1] == '.' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, moves))

            for i in range(-2, 3):
                for j in range(-2, 3):
                    nr, nc = r+i, c+j
                    if 1 <= nr <= H and 1 <= nc <= W and maze[nr-1][nc-1] == '.' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, moves+1))

        return -1

    return bfs()

# Read inputs
H, W = map(int, input().split())
C_h, C_w = map(int, input().split())
D_h, D_w = map(int, input().split())
maze = [input() for _ in range(H)]

# Call the function and print the result
result = min_magic_moves(H, W, C_h, C_w, D_h, D_w, maze)
print(result)
```
