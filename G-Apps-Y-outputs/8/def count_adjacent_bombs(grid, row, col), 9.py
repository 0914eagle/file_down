
def count_adjacent_bombs(grid, row, col):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    count = 0
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '#':
            count += 1
    return count

def replace_empty_with_adjacent_bombs(grid):
    new_grid = []
    for i in range(len(grid)):
        new_row = ''
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                bombs = count_adjacent_bombs(grid, i, j)
                new_row += str(bombs)
            else:
                new_row += '#'
        new_grid.append(new_row)
    return new_grid

# Input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# Output
new_grid = replace_empty_with_adjacent_bombs(grid)
for row in new_grid:
    print(row)
