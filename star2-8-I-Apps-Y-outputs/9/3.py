
def find_water(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'V':
                return i, j
    return -1, -1

def spread_water(grid, i, j):
    if i - 1 >= 0 and grid[i - 1][j] == '.':
        grid[i - 1][j] = 'V'
    if i - 1 >= 0 and grid[i - 1][j] == '#':
        if j - 1 >= 0 and grid[i][j - 1] == '.':
            grid[i][j - 1] = 'V'
        if j + 1 < len(grid[i]) and grid[i][j + 1] == '.':
            grid[i][j + 1] = 'V'

def solve(grid):
    while True:
        i, j = find_water(grid)
        if i == -1:
            break
        spread_water(grid, i, j)
    for row in grid:
        print(''.join(row))

n, m = list(map(int, input().split()))
grid = []
for _ in range(n):
    grid.append(list(input()))
solve(grid)

