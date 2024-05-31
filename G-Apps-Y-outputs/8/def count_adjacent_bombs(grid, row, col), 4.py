
def count_adjacent_bombs(grid, row, col):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "#":
            count += 1
    return count

def replace_empty_squares(grid):
    new_grid = []
    for i in range(len(grid)):
        new_row = ""
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                count = count_adjacent_bombs(grid, i, j)
                new_row += str(count)
            else:
                new_row += "#"
        new_grid.append(new_row)
    return new_grid

H, W = map(int, input().split())
grid = []
for _ in range(H):
    grid.append(input())

output_grid = replace_empty_squares(grid)

for row in output_grid:
    print(row)
