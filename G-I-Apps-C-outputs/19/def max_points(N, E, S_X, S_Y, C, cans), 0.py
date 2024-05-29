
def max_points(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    energy = E
    points = 0

    for t in range(1, 101):  # At most 100 seconds
        # Check if there are new cans appearing
        for x, y, ct in cans:
            if ct == t:
                grid[x][y] += 1

        # Check if Johnny5 can collect any cans or oil spills
        if grid[S_X][S_Y] > 0:
            points += grid[S_X][S_Y]
            energy += grid[S_X][S_Y]
            grid[S_X][S_Y] = 0

        # Check adjacent cells for oil spills
        for i, j in [(S_X-1, S_Y), (S_X+1, S_Y), (S_X, S_Y-1), (S_X, S_Y+1)]:
            if 0 <= i < N and 0 <= j < N and grid[i][j] > 0:
                points += grid[i][j]
                energy += grid[i][j]
                grid[i][j] = 0

        # Move Johnny5 if there is energy
        if energy > 0:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                new_x, new_y = S_X + dx, S_Y + dy
                if 0 <= new_x < N and 0 <= new_y < N:
                    S_X, S_Y = new_x, new_y
                    energy -= 1
                    break

    return points

# Input parsing
N, E, S_X, S_Y, C = map(int, input().split())
cans = []
for _ in range(C):
    X, Y, CT = map(int, input().split())
    cans.append((X, Y, CT))

print(max_points(N, E, S_X, S_Y, C, cans))
```
