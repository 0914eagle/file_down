
def min_north_magnets(n, m, grid):
    rows = [0] * n
    cols = [0] * m
    black_cells = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                rows[i] += 1
                cols[j] += 1
                black_cells += 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#' and (rows[i] == 1 or cols[j] == 1):
                return -1

    return black_cells

# Input parsing
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# Call the function and print the result
result = min_north_magnets(n, m, grid)
print(result)
