
def min_moves_to_solve_puzzle(grid):
    target_grid = ['R' * 4, 'G' * 4, 'B' * 4, 'Y' * 4]
    moves = 0
    for row in grid:
        moves += min(abs(row.count('R') - 4), abs(row.count('G') - 4), abs(row.count('B') - 4), abs(row.count('Y') - 4))
    for col in range(4):
        moves += min(abs(grid[0][col] == 'R' and grid[1][col] == 'G' and grid[2][col] == 'B' and grid[3][col] == 'Y'),
                     abs(grid[0][col] == 'G' and grid[1][col] == 'B' and grid[2][col] == 'Y' and grid[3][col] == 'R'),
                     abs(grid[0][col] == 'B' and grid[1][col] == 'Y' and grid[2][col] == 'R' and grid[3][col] == 'G'),
                     abs(grid[0][col] == 'Y' and grid[1][col] == 'R' and grid[2][col] == 'G' and grid[3][col] == 'B'))
    return moves

# Read input
grid = [input() for _ in range(4)]

# Calculate and output the minimum number of moves needed to solve the puzzle
print(min_moves_to_solve_puzzle(grid))
