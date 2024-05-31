
def count_adjacent_bombs(grid, row, col):
    num_bombs = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_row = row + i
            new_col = col + j
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '#':
                num_bombs += 1
    return str(num_bombs)

def replace_empty_squares(grid):
    new_grid = []
    for i in range(len(grid)):
        new_row = ''
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                new_row += count_adjacent_bombs(grid, i, j)
            else:
                new_row += '#'
        new_grid.append(new_row)
    return new_grid

# Read input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# Replace empty squares with adjacent bomb counts
new_grid = replace_empty_squares(grid)

# Print the output
for row in new_grid:
    print(row)
