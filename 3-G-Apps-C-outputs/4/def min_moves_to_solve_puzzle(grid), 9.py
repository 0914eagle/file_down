
def min_moves_to_solve_puzzle(grid):
    target_grid = ['R' * 4, 'G' * 4, 'B' * 4, 'Y' * 4]
    moves = 0
    for row in grid:
        moves += min(abs(target_grid.index(row) - i) for i in range(4))
    return moves

# Read input from file
with open('input.txt', 'r') as file:
    puzzle = [line.strip() for line in file]

# Calculate minimum moves to solve the puzzle
min_moves = min_moves_to_solve_puzzle(puzzle)
print(min_moves)
