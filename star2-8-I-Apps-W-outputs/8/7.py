
def triplet(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row]) - 2):
            if grid[row][col] != '.' and grid[row][col + 1] != '.' and grid[row][col + 2] != '.':
                count += 1
    for col in range(len(grid[0])):
        for row in range(len(grid) - 2):
            if grid[row][col] != '.' and grid[row + 1][col] != '.' and grid[row + 2][col] != '.':
                count += 1
    for row in range(len(grid) - 2):
        for col in range(len(grid[row]) - 2):
            if grid[row][col] != '.' and grid[row + 1][col + 1] != '.' and grid[row + 2][col + 2] != '.':
                count += 1
    for row in range(len(grid) - 2):
        for col in range(2, len(grid[row])):
            if grid[row][col] != '.' and grid[row + 1][col - 1] != '.' and grid[row + 2][col - 2] != '.':
                count += 1
    
    return count

