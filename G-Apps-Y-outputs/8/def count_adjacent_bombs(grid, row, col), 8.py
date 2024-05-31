
def count_adjacent_bombs(grid, row, col):
    count = 0
    for i in range(max(0, row-1), min(row+2, len(grid))):
        for j in range(max(0, col-1), min(col+2, len(grid[0]))):
            if grid[i][j] == '#':
                count += 1
    return count

def replace_empty_with_count(grid):
    new_grid = [list(row) for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                count = count_adjacent_bombs(grid, i, j)
                new_grid[i][j] = str(count)
    return [''.join(row) for row in new_grid]

# Read input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# Replace empty squares with counts and print the updated grid
for row in replace_empty_with_count(grid):
    print(row)
