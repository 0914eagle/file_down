
def fishing(r, c, k, l, x0, y0, t):
    grid = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if t[x][y] <= l:
                grid[x][y] = 1
    queue = [(x0, y0)]
    seen = set()
    count = 0
    while queue:
        x, y = queue.pop(0)
        if (x, y) in seen:
            continue
        if grid[x][y] == 1:
            count += 1
        seen.add((x, y))
        if x > 0:
            queue.append((x - 1, y))
        if y > 0:
            queue.append((x, y - 1))
        if x < r - 1:
            queue.append((x + 1, y))
        if y < c - 1:
            queue.append((x, y + 1))
    return count

