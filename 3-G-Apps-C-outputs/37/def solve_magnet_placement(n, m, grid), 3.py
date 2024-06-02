
def solve_magnet_placement(n, m, grid):
    rows = [False] * n
    cols = [False] * m
    black_cells = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                black_cells += 1
                rows[i] = True
                cols[j] = True
    
    if black_cells == 0:
        return 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#' and not (rows[i] and cols[j]):
                return -1
    
    return 1

# Input parsing
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# Call the function and print the result
print(solve_magnet_placement(n, m, grid))
