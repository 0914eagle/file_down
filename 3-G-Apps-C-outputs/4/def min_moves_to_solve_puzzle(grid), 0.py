
def min_moves_to_solve_puzzle(grid):
    target = ['R', 'G', 'B', 'Y']
    moves = 0
    for row in grid:
        if row != target:
            moves += min(abs(target.index(row[0]) - target.index('R')), 4 - abs(target.index(row[0]) - target.index('R')))
            target = [target[(target.index(row[0]) + 1) % 4], target[(target.index(row[1]) + 1) % 4], target[(target.index(row[2]) + 1) % 4], target[(target.index(row[3]) + 1) % 4]]
    return moves

# Read input
grid = [list(input().strip()) for _ in range(4)]

# Calculate and output the minimum number of moves needed to solve the puzzle
print(min_moves_to_solve_puzzle(grid))
