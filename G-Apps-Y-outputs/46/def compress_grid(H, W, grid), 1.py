
def compress_grid(H, W, grid):
    # Helper functions to check if a row or column is all white
    def is_white_row(row):
        return all(cell == '.' for cell in row)
    
    def is_white_col(col):
        return all(row[col] == '.' for row in grid)
    
    # Remove all white rows and columns
    compressed_grid = [row for row in grid if not is_white_row(row)]
    compressed_grid = [list(col) for col in zip(*compressed_grid) if not is_white_col(col)]
    
    # Convert the compressed grid back to the original format
    compressed_grid = [''.join(row) for row in compressed_grid]
    
    return compressed_grid

# Read input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# Compress the grid
final_grid = compress_grid(H, W, grid)

# Print the final grid
for row in final_grid:
    print(row)
