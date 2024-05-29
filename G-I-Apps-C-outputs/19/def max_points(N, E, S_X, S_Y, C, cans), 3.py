
def max_points(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    current_energy = E
    current_points = 0

    for t in range(1, 101):  # Maximum game time is 100 seconds
        # Collect cans at this time and update grid
        for x, y, ct in cans:
            if t == ct:
                if grid[x][y] == 0:  # Oil can is not collected yet
                    if x == S_X and y == S_Y:
                        current_points += 1
                    elif abs(x - S_X) <= 1 and abs(y - S_Y) <= 1:
                        current_energy += 1
                    grid[x][y] = 1

        # Output energy
        if current_energy <= 0:
            break

        # Move Johnny5 to the adjacent cell with the highest number of cans
        max_adj_cans = 0
        max_adj_cell = (S_X, S_Y)
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x, new_y = S_X + i, S_Y + j
                if 0 <= new_x < N and 0 <= new_y < N:
                    if (i != 0 or j != 0) and grid[new_x][new_y] > max_adj_cans:
                        max_adj_cans = grid[new_x][new_y]
                        max_adj_cell = (new_x, new_y)
        
        S_X, S_Y = max_adj_cell
        current_energy -= 1

    return current_points

# Read input
N, E, S_X, S_Y, C = map(int, input().split())
cans = [tuple(map(int, input().split())) for _ in range(C)]

# Calculate and print output
print(max_points(N, E, S_X, S_Y, C, cans))
```
