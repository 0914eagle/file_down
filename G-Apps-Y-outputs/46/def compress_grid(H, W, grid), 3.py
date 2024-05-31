
def compress_grid(H, W, grid):
    rows_to_remove = set()
    cols_to_remove = set()
    
    for i in range(H):
        if all(cell == '.' for cell in grid[i]):
            rows_to_remove.add(i)
    
    for j in range(W):
        if all(grid[i][j] == '.' for i in range(H)):
            cols_to_remove.add(j)
    
    compressed_grid = []
    for i in range(H):
        if i not in rows_to_remove:
            compressed_row = [grid[i][j] for j in range(W) if j not in cols_to_remove]
            compressed_grid.append(''.join(compressed_row))
    
    return compressed_grid

# Input processing
H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

# Get the final state of the grid after compression
final_grid = compress_grid(H, W, grid)

# Print the final state of the compressed grid
for row in final_grid:
    print(row)
