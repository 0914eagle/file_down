
def compress_grid(H, W, grid):
    rows_to_remove = set()
    cols_to_remove = set()

    for i in range(H):
        if all(grid[i][j] == '.' for j in range(W)):
            rows_to_remove.add(i)

    for j in range(W):
        if all(grid[i][j] == '.' for i in range(H)):
            cols_to_remove.add(j)

    compressed_grid = []
    for i in range(H):
        if i not in rows_to_remove:
            row = ''
            for j in range(W):
                if j not in cols_to_remove:
                    row += grid[i][j]
            compressed_grid.append(row)

    return '\n'.join(compressed_grid)

# Input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# Output
print(compress_grid(H, W, grid))
