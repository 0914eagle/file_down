
def count_adjacent_bombs(grid, i, j):
    count = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '#':
                count += 1
    return count

def solve_grid(H, W, grid):
    result = [['' for _ in range(W)] for _ in range(H)]
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                result[i][j] = str(count_adjacent_bombs(grid, i, j))
            else:
                result[i][j] = '#'
    
    for row in result:
        print(''.join(row))

# Input parsing
H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

solve_grid(H, W, grid)
