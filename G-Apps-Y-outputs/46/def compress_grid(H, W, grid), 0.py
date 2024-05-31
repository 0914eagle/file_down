
def compress_grid(H, W, grid):
    rows = [False] * H
    cols = [False] * W
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                rows[i] = True
                cols[j] = True
    
    compressed_grid = []
    for i in range(H):
        if rows[i]:
            compressed_row = ''
            for j in range(W):
                if cols[j]:
                    compressed_row += grid[i][j]
            compressed_grid.append(compressed_row)
    
    for row in compressed_grid:
        print(row)

# Read input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# Call the function with the input grid
compress_grid(H, W, grid)
