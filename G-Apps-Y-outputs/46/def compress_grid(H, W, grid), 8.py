
def compress_grid(H, W, grid):
    rows = [False] * H
    cols = [False] * W

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                rows[i] = True
                cols[j] = True

    for i in range(H):
        if rows[i]:
            for j in range(W):
                print(grid[i][j], end='')
            print()

    # Check if there are any remaining columns
    remaining_cols = []
    for j in range(W):
        if not cols[j]:
            remaining_cols.append(j)

    for i in range(H):
        for col in remaining_cols:
            print(grid[i][col], end='')
        print()

# Read input
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# Call the function and print the final state of the grid
compress_grid(H, W, grid)
