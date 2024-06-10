
import sys

def is_valid(pos, r, c, t, l, k, t_map):
    x, y = pos
    if x < 0 or x >= r or y < 0 or y >= c:
        return False
    if t_map[x][y] == -1:
        return False
    if t < t_map[x][y] or t >= t_map[x][y] + k:
        return False
    return True
    
def solve(r, c, k, l, x0, y0, t_map):
    queue = [(x0, y0, 1)]
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[x0][y0] = True
    
    count = 0
    
    while queue:
        x, y, t = queue.pop(0)
        if is_valid((x, y), r, c, t, l, k, t_map):
            count += 1
            queue.append((x - 1, y, t + 1))
            queue.append((x, y - 1, t + 1))
            queue.append((x + 1, y, t + 1))
            queue.append((x, y + 1, t + 1))
    return count
    
r, c, k, l = map(int, input().split())
x0, y0 = map(int, input().split())
t_map = []
for _ in range(r):
    t_map.append(list(map(int, input().split())))
print(solve(r, c, k, l, x0, y0, t_map))

