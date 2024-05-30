
from collections import deque

def min_magic_moves(H, W, C_h, C_w, D_h, D_w, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False]*W for _ in range(H)]
    queue = deque([(C_h-1, C_w-1, 0)])
    visited[C_h-1][C_w-1] = True

    while queue:
        curr_i, curr_j, moves = queue.popleft()

        if curr_i == D_h-1 and curr_j == D_w-1:
            return moves

        for di, dj in directions:
            new_i, new_j = curr_i + di, curr_j + dj

            if 0 <= new_i < H and 0 <= new_j < W and maze[new_i][new_j] == "." and not visited[new_i][new_j]:
                visited[new_i][new_j] = True
                queue.append((new_i, new_j, moves))

        for i in range(-2, 3):
            for j in range(-2, 3):
                new_i, new_j = curr_i + i, curr_j + j
                if 0 <= new_i < H and 0 <= new_j < W and maze[new_i][new_j] == "." and not visited[new_i][new_j]:
                    visited[new_i][new_j] = True
                    queue.append((new_i, new_j, moves+1))

    return -1

# Sample input
H, W = 4, 4
C_h, C_w = 1, 1
D_h, D_w = 4, 4
maze = [
    "..#.",
    "..#.",
    ".#..",
    ".#.."
]

result = min_magic_moves(H, W, C_h, C_w, D_h, D_w, maze)
print(result)
```
