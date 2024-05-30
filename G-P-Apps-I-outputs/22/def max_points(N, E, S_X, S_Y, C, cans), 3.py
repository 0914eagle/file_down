
def max_points(N, E, S_X, S_Y, C, cans):
    grid = [[0] * N for _ in range(N)]
    energy = E
    points = 0

    for i in range(1, 101):  # simulate up to 100 seconds
        # update grid with cans
        for x, y, ct in cans:
            if ct == i:
                grid[y][x] += 1

        # collect cans
        if grid[S_Y][S_X] > 0:
            points += grid[S_Y][S_X]
            energy += grid[S_Y][S_X]
            grid[S_Y][S_X] = 0

        # collect spilled oil
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = S_X + dx, S_Y + dy
            if 0 <= nx < N and 0 <= ny < N:
                points += grid[ny][nx]
                energy += grid[ny][nx]
                grid[ny][nx] = 0

        # check energy
        if energy <= 0:
            break

    return points

# Read input
N, E, S_X, S_Y, C = map(int, input().split())
cans = [list(map(int, input().split())) for _ in range(C)]

# Calculate and output the maximum number of points
print(max_points(N, E, S_X, S_Y, C, cans))
