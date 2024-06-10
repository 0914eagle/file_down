
def trojke(grid):
    triplets = 0
    for row in grid:
        for i in range(len(row) - 2):
            if row[i] != '.' and row[i + 1] != '.' and row[i + 2] != '.':
                triplets += 1
    for col in range(len(grid[0])):
        for row in range(len(grid) - 2):
            if grid[row][col] != '.' and grid[row + 1][col] != '.' and grid[row + 2][col] != '.':
                triplets += 1
    return triplets

