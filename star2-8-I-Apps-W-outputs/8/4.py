
def solve(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])-2):
            if grid[row][col] != '.' and grid[row][col+1] != '.' and grid[row][col+2] != '.':
                count += 1
    
    for col in range(len(grid[0])):
        for row in range(len(grid)-2):
            if grid[row][col] != '.' and grid[row+1][col] != '.' and grid[row+2][col] != '.':
                count += 1
    
    return count

n = int(input())
grid = [input() for i in range(n)]
print(solve(grid))

