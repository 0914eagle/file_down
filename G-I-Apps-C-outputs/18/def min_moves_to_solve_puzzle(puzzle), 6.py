
def min_moves_to_solve_puzzle(puzzle):
    # Find the positions of the rows in the puzzle
    row_positions = []
    for i in range(4):
        row_positions.append(puzzle.index('R'*4))
        puzzle = puzzle[row_positions[-1]:] + puzzle[:row_positions[-1]]

    # Calculate the minimum moves needed to solve the puzzle
    min_moves = min(row_positions)

    return min_moves

# Read input puzzle state
puzzle = []
for _ in range(4):
    puzzle.append(input())

# Calculate and output the minimum number of moves needed to solve the puzzle
print(min_moves_to_solve_puzzle(''.join(puzzle)))
```
