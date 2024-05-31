
def count_adjacent_bombs(grid, i, j):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for dx, dy in directions:
        ni, nj = i + dx, j + dy
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '#':
            count += 1
    return count

def update_grid(grid):
    updated_grid = []
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                adjacent_bombs = count_adjacent_bombs(grid, i, j)
                row += str(adjacent_bombs)
            else:
                row += '#'
        updated_grid.append(row)
    return updated_grid

# Read input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# Update the grid
updated_grid = update_grid(grid)

# Print the updated grid
for row in updated_grid:
    print(row)
