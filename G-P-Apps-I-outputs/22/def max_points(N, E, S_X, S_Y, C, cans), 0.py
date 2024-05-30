
def max_points(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    energy = E
    points = 0
    
    for t in range(1, 101):
        # Check if new cans appear at time t
        for x, y, ct in cans:
            if ct == t:
                grid[y][x] += 1
        
        # Check if Johnny5 can collect oil cans or spilled oil
        if grid[S_Y][S_X] > 0:
            points += grid[S_Y][S_X]
            energy += grid[S_Y][S_X]
            grid[S_Y][S_X] = 0
        
        # Check for adjacent cells
        adjacent_cells = [(S_X-1, S_Y), (S_X+1, S_Y), (S_X, S_Y-1), (S_X, S_Y+1)]
        for x, y in adjacent_cells:
            if 0 <= x < N and 0 <= y < N:
                if grid[y][x] > 0:
                    points += grid[y][x]
                    energy += grid[y][x]
                    grid[y][x] = 0
        
        # Update energy
        energy -= 1
        if energy == 0:
            break
    
    return points

# Parse input
N, E, S_X, S_Y, C = map(int, input().split())
cans = []
for _ in range(C):
    X, Y, CT = map(int, input().split())
    cans.append((X, Y, CT))

# Call the function and output the result
print(max_points(N, E, S_X, S_Y, C, cans))
```
