
def flood_fill(grid, i, j, target_altitude, current_volume):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] >= target_altitude:
        return current_volume
    
    grid[i][j] = target_altitude
    current_volume += 1
    
    current_volume = flood_fill(grid, i+1, j, target_altitude, current_volume)
    current_volume = flood_fill(grid, i-1, j, target_altitude, current_volume)
    current_volume = flood_fill(grid, i, j+1, target_altitude, current_volume)
    current_volume = flood_fill(grid, i, j-1, target_altitude, current_volume)
    
    return current_volume

def solve(grid, i, j):
    target_altitude = grid[i][j]
    volume = flood_fill(grid, i, j, target_altitude, 0)
    
    return volume

h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(list(map(int, input().split())))
    
i, j = map(int, input().split())
i -= 1
j -= 1

print(solve(grid, i, j))

