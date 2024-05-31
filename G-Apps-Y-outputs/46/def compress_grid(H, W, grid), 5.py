
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
            compressed_row = []
            for j in range(W):
                if j not in cols_to_remove:
                    compressed_row.append(grid[i][j])
            compressed_grid.append(compressed_row)

    for row in compressed_grid:
        print(''.join(row))

# Reading input
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# Call the function to compress the grid and print the final state
compress_grid(H, W, grid)
