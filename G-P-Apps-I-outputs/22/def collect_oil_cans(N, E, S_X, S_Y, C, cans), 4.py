
def collect_oil_cans(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    points = 0
    energy = E

    for i in range(1, 101):  # maximum 100 seconds
        if energy == 0:
            break

        for x, y, ct in cans:
            if ct == i:
                if grid[x][y] == 1:
                    points += 1
                    grid[x][y] = 0
                    energy += 1
                elif ((x == S_X and abs(y - S_Y) == 1) or (y == S_Y and abs(x - S_X) == 1)):
                    energy += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = S_X + dx, S_Y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] == 1:
                    points += 1
                    grid[nx][ny] = 0
                    energy += 1
        energy -= 1

    return points

# Input
N, E, S_X, S_Y, C = map(int, input().split())
cans = [list(map(int, input().split())) for _ in range(C)]

# Output
print(collect_oil_cans(N, E, S_X, S_Y, C, cans))
```
