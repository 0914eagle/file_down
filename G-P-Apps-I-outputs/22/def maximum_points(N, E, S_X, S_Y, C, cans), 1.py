
def maximum_points(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    for x, y, ct in cans:
        grid[y][x] = max(grid[y][x], ct)
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    collected_points = 0
    energy = E
    x, y = S_X, S_Y
    
    for t in range(101):
        if x < 0 or x >= N or y < 0 or y >= N:
            break
        
        if grid[y][x] == t:
            collected_points += 1
            energy += 1
        
        if energy == 0:
            break
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                energy -= 1
        
        if energy == 0:
            break
        
        x, y = min(N - 1, max(0, x)), min(N - 1, max(0, y))
    
    return collected_points

# Input parsing
N, E, S_X, S_Y, C = map(int, input().split())
cans = [list(map(int, input().split())) for _ in range(C)]

# Output result
print(maximum_points(N, E, S_X, S_Y, C, cans))
