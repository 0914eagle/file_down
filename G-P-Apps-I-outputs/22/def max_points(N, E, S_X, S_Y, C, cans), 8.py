
def max_points(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    energy = E
    points = 0
    time = 0

    while time < 100:
        for x, y, ct in cans:
            if ct == time:
                if grid[x][y] == 1:
                    points += 1
                    grid[x][y] = 0
                    energy += 1
                elif (abs(x - S_X) + abs(y - S_Y)) <= 1:
                    energy += 1

        if energy <= 0:
            break

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = S_X + dx, S_Y + dy
            if 0 <= new_x < N and 0 <= new_y < N:
                energy -= 1
                S_X, S_Y = new_x, new_y

        time += 1

    return points

# Input parsing
N, E, S_X, S_Y, C = map(int, input().split())
cans = []
for _ in range(C):
    X, Y, CT = map(int, input().split())
    cans.append((X, Y, CT))

# Calculate and output the result
result = max_points(N, E, S_X, S_Y, C, cans)
print(result)
```
