
def flood(grid, i, j):
    if grid[i][j] >= 0:
        return 0
    
    grid[i][j] = 0
    volume = 1
    
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i+1, j+1), (i-1, j+1), (i+1, j-1)]:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            volume += flood(grid, x, y)
    
    return volume

def solve(grid, i, j):
    return flood(grid, i-1, j-1)

h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
i, j = map(int, input().split())

print(solve(grid, i, j))

