
def min_moves_to_solve_puzzle(grid):
    target_grid = ['R' * 4, 'G' * 4, 'B' * 4, 'Y' * 4]
    
    def get_row_moves(grid):
        moves = 0
        for i in range(4):
            row = grid[i]
            target_row = target_grid[i]
            moves += min(abs(row.index('R') - target_row.index('R')), 4 - abs(row.index('R') - target_row.index('R')))
        return moves
    
    def get_col_moves(grid):
        moves = 0
        for j in range(4):
            col = [grid[i][j] for i in range(4)]
            target_col = [target_grid[i][j] for i in range(4)]
            moves += min(abs(col.index('R') - target_col.index('R')), 4 - abs(col.index('R') - target_col.index('R')))
        return moves
    
    row_moves = get_row_moves(grid)
    col_moves = get_col_moves(grid)
    
    return min(row_moves, col_moves)

# Read input
grid = [input() for _ in range(4)]

# Output the minimum number of moves needed to solve the puzzle
print(min_moves_to_solve_puzzle(grid))
