
def max_points(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    energy = E
    points = 0

    for i in range(C):
        X, Y, CT = cans[i]
        grid[X][Y] = CT

    for t in range(1, 101):  # Maximum time limit
        for i in range(N):
            for j in range(N):
                if grid[i][j] == t and energy > 0:
                    if (i == S_X and j == S_Y) or (i + 1 < N and grid[i + 1][j] == t) or (i - 1 >= 0 and grid[i - 1][j] == t) or (j + 1 < N and grid[i][j + 1] == t) or (j - 1 >= 0 and grid[i][j - 1] == t):
                        points += 1
                        grid[i][j] = 0
                        energy += 1
                    else:
                        energy -= 1

    return points

# Input
N, E, S_X, S_Y, C = map(int, input().split())
cans = [list(map(int, input().split())) for _ in range(C)]

# Output
print(max_points(N, E, S_X, S_Y, C, cans))
```
