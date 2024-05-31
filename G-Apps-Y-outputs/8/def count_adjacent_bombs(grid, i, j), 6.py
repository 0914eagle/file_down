
def count_adjacent_bombs(grid, i, j):
    num_bombs = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]):
                if grid[i+x][j+y] == '#':
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
result = replace_empty_squares(grid)

# Print the result
for row in result:
    print(row)
