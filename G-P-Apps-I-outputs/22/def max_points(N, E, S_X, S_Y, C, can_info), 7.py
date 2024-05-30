
def max_points(N, E, S_X, S_Y, C, can_info):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    for x, y, t in can_info:
        grid[y][x] = max(grid[y][x], t)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def can_collect(x, y, t):
        if grid[y][x] == t:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and grid[ny][nx] == t:
                return True
        return False

    points = 0
    for t in range(max(map(max, grid)) + 1):
        if E == 0:
            break
        for x, y, _ in can_info:
            if can_collect(x, y, t):
                points += 1
                E += 1
        E -= 1

    return points

# Read input
N, E, S_X, S_Y, C = map(int, input().split())
can_info = [list(map(int, input().split())) for _ in range(C)]

# Output the result
print(max_points(N, E, S_X, S_Y, C, can_info))
