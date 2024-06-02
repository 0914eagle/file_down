
def min_moves_to_solve_puzzle(grid):
    target = ['R', 'G', 'B', 'Y']
    current = [row for row in grid]
    moves = 0

    for _ in range(4):
        if current == target:
            return moves
        current = [current[-1]] + current[:-1]  # Move one row left
        moves += 1

    for _ in range(4):
        if current == target:
            return moves
        current = [current[1]] + [current[0]] + current[2:]  # Move one column up
        moves += 1

    return moves

# Read input from file
with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

result = min_moves_to_solve_puzzle(grid)
print(result)
