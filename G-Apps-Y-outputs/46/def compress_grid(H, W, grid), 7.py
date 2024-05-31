
def compress_grid(H, W, grid):
    rows_to_remove = set()
    cols_to_remove = set()
    
    for i in range(H):
        if all(grid[i][j] == '.' for j in range(W)):
            rows_to_remove.add(i)
    
    for j in range(W):
        if all(grid[i][j] == '.' for i in range(H)):
            cols_to_remove.add(j)
    
    compressed_grid = [['' for _ in range(W - len(cols_to_remove))] for _ in range(H - len(rows_to_remove))]
    
    new_row_idx = 0
    new_col_idx = 0
    for i in range(H):
        if i not in rows_to_remove:
            for j in range(W):
                if j not in cols_to_remove:
                    compressed_grid[new_row_idx][new_col_idx] = grid[i][j]
                    new_col_idx += 1
            new_row_idx += 1
            new_col_idx = 0
    
    return compressed_grid

# Read input
H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

# Get the final state of the grid
final_grid = compress_grid(H, W, grid)

# Output the final state of the grid
for row in final_grid:
    print(''.join(row))
