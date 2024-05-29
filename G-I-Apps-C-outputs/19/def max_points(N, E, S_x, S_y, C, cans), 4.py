
def max_points(N, E, S_x, S_y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    for x, y, ct in cans:
        grid[y][x] = ct

    points = 0
    energy = E

    for t in range(101):
        for y in range(N):
            for x in range(N):
                if grid[y][x] == t:
                    if (x == S_x and y == S_y) or (abs(x - S_x) + abs(y - S_y) == 1):
                        points += 1
                        energy += 1
                    else:
                        if energy > 0:
                            energy -= 1

        if energy == 0:
            break

    return points

# Input processing
N, E, S_x, S_y, C = map(int, input().split())
cans = [list(map(int, input().split())) for _ in range(C)]

# Compute and output the result
print(max_points(N, E, S_x, S_y, C, cans))
```
