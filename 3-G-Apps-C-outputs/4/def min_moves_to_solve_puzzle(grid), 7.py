
def min_moves_to_solve_puzzle(grid):
    target_grid = ['R'*4, 'G'*4, 'B'*4, 'Y'*4]
    moves = 0
    
    for row in range(4):
        for col in range(4):
            if grid[row][col] != target_grid[row][col]:
                target_row = target_grid.index(grid[row])
                target_col = target_grid[target_row].index(grid[row][col])
                
                row_diff = abs(target_row - row)
                col_diff = abs(target_col - col)
                
                moves += min(row_diff, 4 - row_diff) + min(col_diff, 4 - col_diff)
    
    return moves

# Read input
grid = [input() for _ in range(4)]

# Calculate and output the minimum number of moves needed to solve the puzzle
print(min_moves_to_solve_puzzle(grid))
