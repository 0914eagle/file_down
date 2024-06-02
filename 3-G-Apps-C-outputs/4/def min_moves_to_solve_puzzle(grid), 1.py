
def min_moves_to_solve_puzzle(grid):
    target_grid = ['R' * 4, 'G' * 4, 'B' * 4, 'Y' * 4]
    moves = 0
    for row in grid:
        moves += min(abs(target_grid.index(row) - i) for i in range(4))
    return moves

# Read input
grid = [input() for _ in range(4)]

# Calculate and output the minimum number of moves needed to solve the puzzle
print(min_moves_to_solve_puzzle(grid))
