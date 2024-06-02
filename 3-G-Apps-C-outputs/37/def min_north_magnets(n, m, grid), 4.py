
def min_north_magnets(n, m, grid):
    rows = [False] * n
    cols = [False] * m
    black_cells = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                black_cells += 1
                rows[i] = True
                cols[j] = True

    if all(rows) and all(cols):
        return black_cells
    else:
        return -1

# Input parsing
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# Call the function and print the result
result = min_north_magnets(n, m, grid)
print(result)
