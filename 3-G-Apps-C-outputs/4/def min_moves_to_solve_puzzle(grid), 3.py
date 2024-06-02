
def min_moves_to_solve_puzzle(grid):
    colors = ['R', 'G', 'B', 'Y']
    target_grid = ['R' * 4, 'G' * 4, 'B' * 4, 'Y' * 4]
    
    def get_row_moves(row, target_row):
        moves_left = 0
        moves_right = 0
        for i in range(4):
            diff = abs(colors.index(row[i]) - colors.index(target_row[i]))
            moves_left += min(diff, 4 - diff)
            moves_right += min(4 - diff, diff)
        return min(moves_left, moves_right)
    
    def get_column_moves(grid, target_grid):
        moves_up = 0
        moves_down = 0
        for j in range(4):
            column = [grid[i][j] for i in range(4)]
            target_column = [target_grid[i][j] for i in range(4)]
            moves_up += get_row_moves(column, target_column)
            moves_down += get_row_moves(column[::-1], target_column)
        return min(moves_up, moves_down)
    
    return min(get_column_moves(grid, target_grid), get_column_moves(grid[::-1], target_grid))

# Read input
grid = [input() for _ in range(4)]

# Output the minimum number of moves needed to solve the puzzle
print(min_moves_to_solve_puzzle(grid))
