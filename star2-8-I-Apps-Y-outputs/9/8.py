
n, m = [int(x) for x in input().split()]
grid = [input() for _ in range(n)]
for r in range(n):
    for c in range(m):
        if grid[r][c] == 'V':
            if r > 0 and grid[r-1][c] == '.':
                grid[r-1] = grid[r-1][:c] + 'V' + grid[r-1][c+1:]
            if r < n-1 and grid[r+1][c] == '.':
                grid[r+1] = grid[r+1][:c] + 'V' + grid[r+1][c+1:]
            if c > 0 and grid[r][c-1] == '.':
                grid[r] = grid[r][:c-1] + 'V' + grid[r][c:]
            if c < m-1 and grid[r][c+1] == '.':
                grid[r] = grid[r][:c+1] + 'V' + grid[r][c+2:]
            if c > 0 and grid[r][c-1] == '#':
                if r > 0 and grid[r-1][c] == '.':
                    grid[r-1] = grid[r-1][:c] + 'V' + grid[r-1][c+1:]
                if r < n-1 and grid[r+1][c] == '.':
                    grid[r+1] = grid[r+1][:c] + 'V' + grid[r+1][c+1:]
            if c < m-1 and grid[r][c+1] == '#':
                if r > 0 and grid[r-1][c] == '.':
                    grid[r-1] = grid[r-1][:c] + 'V' + grid[r-1][c+1:]
                if r < n-1 and grid[r+1][c] == '.':
                    grid[r+1] = grid[r+1][:c] + 'V' + grid[r+1][c+1:]
for r in range(n):
    print(grid[r])

