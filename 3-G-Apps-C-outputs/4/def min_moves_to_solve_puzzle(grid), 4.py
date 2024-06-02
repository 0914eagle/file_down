
def min_moves_to_solve_puzzle(grid):
    target = ['R', 'G', 'B', 'Y']
    moves = 0
    for i in range(4):
        row = grid[i]
        if row == target:
            continue
        for j in range(4):
            if row[j] != target[j]:
                diff = (target.index(row[j]) - j) % 4
                moves += min(diff, 4 - diff)
    return moves

# Read input
grid = [input().strip() for _ in range(4)]

# Calculate and output the minimum number of moves needed to solve the puzzle
print(min_moves_to_solve_puzzle(grid))
