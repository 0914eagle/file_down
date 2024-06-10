
grid = []
N, M = map(int, input().split())
for i in range(N):
    grid.append(list(input()))
def expand_water(grid):
    new_grid = [[c for c in row] for row in grid]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'V':
                if i > 0 and grid[i-1][j] == '.':
                    new_grid[i-1][j] = 'V'
                if j > 0 and grid[i][j-1] == '.':
                    new_grid[i][j-1] = 'V'
                if j < M-1 and grid[i][j+1] == '.':
                    new_grid[i][j+1] = 'V'
    return new_grid
while True:
    new_grid = expand_water(grid)
    if grid == new_grid:
        break
    grid = new_grid
for row in grid:
    print("".join(row))

