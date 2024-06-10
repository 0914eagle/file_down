
grid = []

N, M = map(int, input().split())
for _ in range(N):
    grid.append(list(input()))

def spread_water(grid):
    new_grid = [row[:] for row in grid]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'V':
                if i > 0 and grid[i-1][j] == '.':
                    new_grid[i-1][j] = 'V'
                if i > 0 and j > 0 and grid[i-1][j-1] == '.':
                    new_grid[i-1][j-1] = 'V'
                if i > 0 and j < M-1 and grid[i-1][j+1] == '.':
                    new_grid[i-1][j+1] = 'V'
    return new_grid

while True:
    new_grid = spread_water(grid)
    if grid == new_grid:
        break
    grid = new_grid

for row in grid:
    print(''.join(row))

