
def max_points(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(C):
        X, Y, CT = cans[i]
        grid[X][Y] = CT
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    
    def dfs(x, y, energy):
        if (x, y) in visited:
            return 0
        
        visited.add((x, y))
        max_points = 0
        
        if grid[x][y] > 0 and energy >= abs(x - S_X) + abs(y - S_Y):
            max_points += 1
            energy += 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and energy > abs(nx - S_X) + abs(ny - S_Y):
                max_points = max(max_points, dfs(nx, ny, energy - 1))
        
        visited.remove((x, y))
        return max_points
    
    return dfs(S_X, S_Y, E)

# Read input
N, E, S_X, S_Y, C = map(int, input().split())
cans = [list(map(int, input().split())) for _ in range(C)]

# Output maximum points
print(max_points(N, E, S_X, S_Y, C, cans))
