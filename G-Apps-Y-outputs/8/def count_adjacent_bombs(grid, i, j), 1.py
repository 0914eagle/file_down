
def count_adjacent_bombs(grid, i, j):
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dx, dy in directions:
        ni, nj = i + dx, j + dy
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '#':
            count += 1
    return count

def replace_empty_with_adjacent_bombs(grid):
    new_grid = []
    for i in range(len(grid)):
        new_row = ''
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                count = count_adjacent_bombs(grid, i, j)
                new_row += str(count)
            else:
                new_row += '#'
        new_grid.append(new_row)
    return new_grid

# Input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# Process
result = replace_empty_with_adjacent_bombs(grid)

# Output
for row in result:
    print(row)
