
def spread_water(grid, row, col, rows, cols):
    if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '.':
        return
    grid[row][col] = 'V'
    
    spread_water(grid, row - 1, col, rows, cols)
    spread_water(grid, row, col - 1, rows, cols)
    spread_water(grid, row, col + 1, rows, cols)
    
def solve_problem(grid):
    rows, cols = len(grid), len(grid[0])
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'V':
                spread_water(grid, row - 1, col, rows, cols)
    
    return grid
    
def main():
    rows, cols = map(int, input().split())
    
    grid = []
    
    for _ in range(rows):
        grid.append(list(input()))
        
    grid = solve_problem(grid)
    
    for row in grid:
        print(''.join(row))

if __name__ == '__main__':
    main()

