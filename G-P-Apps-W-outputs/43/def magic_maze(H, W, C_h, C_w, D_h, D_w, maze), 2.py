
from collections import deque

def magic_maze(H, W, C_h, C_w, D_h, D_w, maze):
    dh = [0, 0, 1, -1]
    dw = [1, -1, 0, 0]

    INF = float('inf')
    dist = [[INF] * W for _ in range(H)]
    dist[C_h-1][C_w-1] = 0

    queue = deque([(C_h-1, C_w-1)])
    while queue:
        h, w = queue.popleft()
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                continue
            if maze[nh][nw] == '#' or dist[nh][nw] <= dist[h][w]:
                continue
            dist[nh][nw] = dist[h][w]
            queue.appendleft((nh, nw))

        for i in range(-2, 3):
            for j in range(-2, 3):
                nh, nw = h + i, w + j
                if nh < 0 or nh >= H or nw < 0 or nw >= W:
                    continue
                if maze[nh][nw] == '#' or dist[nh][nw] <= dist[h][w] + 1:
                    continue
                dist[nh][nw] = dist[h][w] + 1
                queue.append((nh, nw))

    if dist[D_h-1][D_w-1] == INF:
        return -1
    else:
        return dist[D_h-1][D_w-1]

# Input processing
H, W = map(int, input().split())
C_h, C_w = map(int, input().split())
D_h, D_w = map(int, input().split())
maze = [input() for _ in range(H)]

# Output the result
result = magic_maze(H, W, C_h, C_w, D_h, D_w, maze)
print(result)
```
