
# 宽度搜索法
def walk_step(x, y, t, q, map):
    if x < 0 or x >= W or y < 0 or y >= H:
        return
    z_x, z_y = map[y][x]
    if t + 1 >= z_x or t + 1 >= z_y:
        return
    q.append((x, y, t + 1))

def walk_cliff(map):
    queue = [(X, Y, 0)]
    while queue:
        x, y, t = queue.pop(0)
        if x == X and y == Y and t > 0:
            print(round(math.sqrt(W * W + H * H) * (1 - 0.5 * (math.cos(t * math.pi / 6) + 1)), 10))
            return
        walk_step(x + 1, y, t, queue, map)
        walk_step(x - 1, y, t, queue, map)
        walk_step(x, y + 1, t, queue, map)
        walk_step(x, y - 1, t, queue, map)

import math

a, m = [float(x) for x in input().split()]
W, H, X, Y = [int(x) for x in input().split()]
map = [[(0, 0)] * W for _ in range(H)]
for y in range(H):
    map[y] = [(0, z) for z in [int(x) for x in input().split()]]
walk_cliff(map)
